"""Owee Glyph Master 3.3 — genera todos los formatos desde una sola fuente de verdad.

Fuente de verdad: ../OweeSans3_3_Source (esqueletos del Curso Práctico para
Adultos + build_font_33.py con los estilos 'sans' y 'school').

Salida:
  fonts/ttf    TTF   escritorio (Linux, Windows), Android en apps que aceptan fuentes
  fonts/otf    OTF   (CFF) macOS, iPhone/iPad, diseño
  fonts/woff2  WOFF2 web moderna
  fonts/woff   WOFF  web antigua
  svg/sans, svg/school   un SVG por glifo, nombrado por ID estable
  owee-glyph-map.json    roman, ID, code point, lectura de dígitos
  mobile/ios/Owee-Fonts.mobileconfig   perfil para instalar las fuentes en iPhone/iPad
  web/fonts              copia de WOFF2/WOFF/TTF para el kit web

    python3 build_glyph_master.py
"""
from pathlib import Path
import base64, json, os, shutil, subprocess, sys, uuid

ROOT = Path(__file__).parent
SRC = ROOT.parent / "OweeSans3_3_Source"
DEPS = ROOT.parent.parent / "versiones_anteriores" / "Owee_Script_2.0_Source" / "owee-script-2.0-source" / ".pydeps"
sys.path.insert(0, str(DEPS))

from fontTools.ttLib import TTFont
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.svgPathPen import SVGPathPen

VERSION = "3.4"
STYLES = {
    "sans":   {"ttf": "OweeSans3_3-Canonical-Regular.ttf", "base": "OweeSans-Regular",
               "family": "Owee Sans", "ps": "OweeSans-Regular"},
    "school": {"ttf": "OweeSchool3_3-Regular.ttf", "base": "OweeSchool-Regular",
               "family": "Owee School", "ps": "OweeSchool-Regular"},
}
VOWELS = ["a", "e", "o", "u"]
CONS = ["p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"]
DIGIT_READ = ["cho", "be", "du", "ga", "fo", "sa", "ku", "mu", "na", "she"]


def glyph_map():
    units, cp = [], 0xE000
    for v in VOWELS:
        units.append({"roman": v, "id": f"OWEE_SYL_{v.upper()}", "codepoint": f"U+{cp:04X}", "kind": "vowel"}); cp += 1
    for c in CONS:
        for v in VOWELS:
            units.append({"roman": c + v, "id": f"OWEE_SYL_{(c + v).upper()}", "codepoint": f"U+{cp:04X}", "kind": "syllable"}); cp += 1
    units.append({"roman": "-", "id": "OWEE_MARK_JOIN", "codepoint": "U+E03C", "kind": "mark",
                  "note": "nexo de compuesto: el guion de sade-kelo"})
    units.append({"roman": "^", "id": "OWEE_MARK_NAME", "codepoint": "U+E03D", "kind": "mark",
                  "note": "marca de nombre propio; en romano, la inicial mayúscula (Ana)"})
    for d in range(10):
        units.append({"roman": str(d), "id": f"OWEE_DIGIT_{d}", "codepoint": f"U+{0xE040 + d:04X}",
                      "kind": "digit", "reading": DIGIT_READ[d]})
    return units


def run(cmd, **kw):
    print("$", " ".join(map(str, cmd)))
    subprocess.run(cmd, check=True, **kw)


def rename(font, family, ps):
    """Familia estable sin número de versión: los documentos no se rompen al actualizar."""
    name = font["name"]
    for rec in list(name.names):
        if rec.nameID in (1, 4, 6, 16, 17, 3):
            name.removeNames(nameID=rec.nameID)
    name.setName(family, 1, 3, 1, 0x409); name.setName("Regular", 2, 3, 1, 0x409)
    name.setName(f"{family} {VERSION}", 3, 3, 1, 0x409)
    name.setName(f"{family} Regular", 4, 3, 1, 0x409)
    name.setName(f"Version {VERSION}", 5, 3, 1, 0x409)
    name.setName("Copyright (c) 2026, Hector Martinez (https://oweeme.com)", 0, 3, 1, 0x409)
    name.setName("This Font Software is licensed under the SIL Open Font License, Version 1.1. https://openfontlicense.org", 13, 3, 1, 0x409)
    name.setName("https://openfontlicense.org", 14, 3, 1, 0x409)
    name.setName(ps, 6, 3, 1, 0x409)
    for nid, val in ((1, family), (2, "Regular"), (4, f"{family} Regular"), (6, ps)):
        name.setName(val, nid, 1, 0, 0)


def ttf_to_otf(tt, out, ps):
    """Mismos contornos en formato CFF (OpenType/PostScript)."""
    order = tt.getGlyphOrder(); gs = tt.getGlyphSet(); hmtx = tt["hmtx"]
    charstrings = {}
    for g in order:
        pen = T2CharStringPen(hmtx[g][0], gs)
        gs[g].draw(pen)
        charstrings[g] = pen.getCharString()
    fb = FontBuilder(tt["head"].unitsPerEm, isTTF=False)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(tt.getBestCmap())
    fb.setupCFF(ps, {"FullName": tt["name"].getDebugName(4), "FamilyName": tt["name"].getDebugName(1)},
                charstrings, {})
    fb.setupHorizontalMetrics({g: hmtx[g] for g in order})
    h = tt["hhea"]; fb.setupHorizontalHeader(ascent=h.ascent, descent=h.descent, lineGap=h.lineGap)
    names = {"familyName": tt["name"].getDebugName(1), "styleName": "Regular",
             "uniqueFontIdentifier": tt["name"].getDebugName(3), "fullName": tt["name"].getDebugName(4),
             "psName": ps, "version": f"Version {VERSION}"}
    fb.setupNameTable(names)
    o = tt["OS/2"]
    fb.setupOS2(version=4, sTypoAscender=o.sTypoAscender, sTypoDescender=o.sTypoDescender, sTypoLineGap=0,
                usWinAscent=o.usWinAscent, usWinDescent=o.usWinDescent, sxHeight=o.sxHeight,
                sCapHeight=o.sCapHeight, fsSelection=o.fsSelection, achVendID="OWEE")
    fb.setupPost(); fb.save(out)


def export_svgs(tt, units, outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob("*.svg"): old.unlink()
    gs = tt.getGlyphSet(); cmap = tt.getBestCmap(); asc = tt["hhea"].ascent; desc = tt["hhea"].descent
    for u in units:
        cp = int(u["codepoint"][2:], 16); g = cmap[cp]
        pen = SVGPathPen(gs); gs[g].draw(pen); adv = tt["hmtx"][g][0]
        (outdir / f'{u["codepoint"][2:]}_{u["id"]}.svg').write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {-asc} {adv} {asc - desc}">'
            f'<title>{u["id"]} ({u["roman"]})</title>'
            f'<path transform="scale(1,-1)" fill="currentColor" d="{pen.getCommands()}"/></svg>\n')


def mobileconfig(ttf_paths, out):
    payloads = []
    for p in ttf_paths:
        payloads.append(f"""    <dict>
      <key>Font</key><data>{base64.b64encode(p.read_bytes()).decode()}</data>
      <key>Name</key><string>{p.name}</string>
      <key>PayloadType</key><string>com.apple.font</string>
      <key>PayloadVersion</key><integer>1</integer>
      <key>PayloadIdentifier</key><string>org.owee.font.{p.stem}</string>
      <key>PayloadUUID</key><string>{uuid.uuid5(uuid.NAMESPACE_URL, 'owee-font-' + p.stem)}</string>
      <key>PayloadDisplayName</key><string>{p.stem}</string>
    </dict>""")
    out.write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>PayloadContent</key>
  <array>
{chr(10).join(payloads)}
  </array>
  <key>PayloadDisplayName</key><string>Owee Fonts {VERSION}</string>
  <key>PayloadDescription</key><string>Owee Sans y Owee School para escribir y leer Owee Script.</string>
  <key>PayloadIdentifier</key><string>org.owee.fonts</string>
  <key>PayloadType</key><string>Configuration</string>
  <key>PayloadUUID</key><string>{uuid.uuid5(uuid.NAMESPACE_URL, 'owee-fonts-profile')}</string>
  <key>PayloadVersion</key><integer>1</integer>
</dict>
</plist>
""")


def build_index(web):
    """index.html para alojar Owee Pad en un sitio propio: app.html + cabecera + PWA."""
    app = (web / "app.html").read_text()
    (web / "index.html").write_text(f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#2F6FB0">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon.svg">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}[hidden]{{display:none!important}}</style>
</head>
<body>
{app}
<script>if ("serviceWorker" in navigator && location.protocol !== "file:") navigator.serviceWorker.register("sw.js").catch(function () {{}});</script>
</body>
</html>
""")


def build_package(web, out):
    """package/: lo único que hay que copiar a un proyecto web (Vite, Quasar, Tauri o HTML)."""
    if out.exists(): shutil.rmtree(out)
    (out / "fonts").mkdir(parents=True)
    for st in STYLES.values():
        for ext in ("woff2", "woff"):
            shutil.copy(web / "fonts" / f'{st["base"]}.{ext}', out / "fonts")
    for f in ("owee.ts", "owee.js", "owee.css"):
        shutil.copy(web / f, out / f)
    shutil.copy(ROOT / "owee-glyph-map.json", out / "owee-glyph-map.json")
    if (ROOT / "OFL.txt").exists(): shutil.copy(ROOT / "OFL.txt", out / "OFL.txt")
    (out / "package.json").write_text(json.dumps({
        "name": "@oweeme/owee-script", "version": VERSION + ".0", "private": True,
        "description": "Owee Script para la web: fuentes Owee Sans / Owee School y parser Roman <-> Owee.",
        "type": "module", "main": "owee.ts", "types": "owee.ts",
        "exports": {".": "./owee.ts", "./owee.css": "./owee.css", "./owee.js": "./owee.js",
                    "./owee-glyph-map.json": "./owee-glyph-map.json", "./fonts/*": "./fonts/*"},
        "sideEffects": ["*.css"]}, indent=2) + "\n")
    (out / "README.md").write_text(f"""# @oweeme/owee-script {VERSION}

Copia esta carpeta al proyecto. Nada más es necesario.

| Archivo | Para qué |
|---|---|
| `owee.css` | carga Owee Sans y Owee School; clases `.owee`, `.owee-sans`, `.owee-school` |
| `fonts/*.woff2`, `fonts/*.woff` | las fuentes (owee.css las referencia con rutas relativas) |
| `owee.ts` | parser para proyectos Vite / Vue / Quasar / Tauri (TypeScript) |
| `owee.js` | el mismo parser para HTML sin compilar (`window.Owee`) |
| `owee-glyph-map.json` | roman, ID estable y code point de las 70 unidades |

## Vite / Vue / Quasar / Tauri
```ts
import 'src/lib/owee-script/owee.css'          // una vez (boot, main.ts o quasar.config css)
import {{ toScript, toRoman }} from 'src/lib/owee-script/owee'
toScript('me suna nume 2026', {{ digits: true }})
```
```html
<span class="owee">{{{{ toScript(texto) }}}}</span>
<span class="owee-school">{{{{ toScript(texto) }}}}</span>
```

## HTML
```html
<link rel="stylesheet" href="owee-script/owee.css">
<script src="owee-script/owee.js"></script>
<p class="owee" id="t"></p>
<script>t.textContent = Owee.toScript('me suna nume 2026', {{ digits: true }})</script>
```

Guarda siempre el texto en roman (base de datos, URLs, búsqueda) y convierte
a Owee sólo al mostrarlo: así funciona aunque la fuente no esté disponible.
""")


def main():
    env = dict(os.environ, PYTHONPATH=str(DEPS))
    for style in STYLES:
        run([sys.executable, "build_font_33.py", style], cwd=SRC, env=env)

    units = glyph_map()
    (ROOT / "owee-glyph-map.json").write_text(json.dumps(
        {"name": "Owee Glyph Master", "version": VERSION,
         "ranges": {"syllables": "U+E000..U+E03B", "marks": "U+E03C..U+E03D", "reserved": "U+E03E..U+E03F", "digits": "U+E040..U+E049"},
         "units": units}, ensure_ascii=False, indent=1))

    dirs = {k: ROOT / "fonts" / k for k in ("ttf", "otf", "woff2", "woff")}
    for d in dirs.values(): d.mkdir(parents=True, exist_ok=True)
    web = ROOT / "web" / "fonts"; web.mkdir(parents=True, exist_ok=True)
    ttfs = []
    for style, st in STYLES.items():
        tt = TTFont(SRC / st["ttf"])
        rename(tt, st["family"], st["ps"])
        cmap = tt.getBestCmap()
        missing = [u["codepoint"] for u in units if int(u["codepoint"][2:], 16) not in cmap]
        assert not missing, (style, missing)
        ttf = dirs["ttf"] / f'{st["base"]}.ttf'; tt.save(ttf); ttfs.append(ttf)
        ttf_to_otf(TTFont(ttf), dirs["otf"] / f'{st["base"]}.otf', st["ps"])
        for flavor in ("woff2", "woff"):
            f = TTFont(ttf); f.flavor = flavor; f.save(dirs[flavor] / f'{st["base"]}.{flavor}')
        export_svgs(TTFont(ttf), units, ROOT / "svg" / style)
        for ext in ("woff2", "woff", "ttf"):
            shutil.copy(dirs[ext] / f'{st["base"]}.{ext}', web / f'{st["base"]}.{ext}')

    ios = ROOT / "mobile" / "ios"; ios.mkdir(parents=True, exist_ok=True)
    mobileconfig(ttfs, ios / "Owee-Fonts.mobileconfig")
    shutil.copy(ROOT / "owee-glyph-map.json", ROOT / "web" / "owee-glyph-map.json")
    build_index(ROOT / "web")
    build_package(ROOT / "web", ROOT / "package")
    print("Glyph Master listo:", len(units), "unidades x", len(STYLES), "estilos")


if __name__ == "__main__":
    main()
