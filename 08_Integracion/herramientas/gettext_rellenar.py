#!/usr/bin/env python3
"""Crea catalogos de interfaz en Owee (qow y qow@owee) para los programas YA instalados, sin tocar el sistema.

Para cada catalogo de espanol de /usr/share/locale/es/LC_MESSAGES/*.mo toma los textos originales (msgid, casi siempre en ingles)
y, donde el texto coincide con el glosario de Owee (datos/ui_glosario.tsv), genera la traduccion en Owee. Lo que no coincide
no se incluye: con LANGUAGE=qow:es ese texto se ve en espanol (nada se rompe). No necesita gettext (lee y escribe .mo en Python).

Uso:  python3 gettext_rellenar.py [--salida DIR] [--origen DIR] [--dominios a,b,c]
      por defecto escribe en ~/.local/share/locale/{qow,qow@owee}/LC_MESSAGES/<dominio>.mo
Probar: LANG=es_ES.UTF-8 LANGUAGE=qow:es  <programa>        (romano)
        LANG=es_ES.UTF-8 LANGUAGE=qow@owee:qow:es <programa>  (glifos; hace falta la fuente Owee Sans)"""
import argparse, collections, pathlib, re, struct, sys
aqui = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(aqui))
from owee_script import to_script

def leer_mo(ruta):
    d = pathlib.Path(ruta).read_bytes()
    if len(d) < 28: return {}
    magic = struct.unpack("<I", d[:4])[0]
    fmt = "<" if magic == 0x950412de else (">" if magic == 0xde120495 else None)
    if fmt is None: return {}
    n, o_orig, o_trad = struct.unpack(fmt + "III", d[8:20])
    out = {}
    for i in range(n):
        lo, po = struct.unpack(fmt + "II", d[o_orig + 8 * i:o_orig + 8 * i + 8])
        lt, pt = struct.unpack(fmt + "II", d[o_trad + 8 * i:o_trad + 8 * i + 8])
        out[d[po:po + lo]] = d[pt:pt + lt]
    return out

def escribir_mo(ruta, tabla):
    claves = sorted(tabla)
    ids = b"".join(k + b"\0" for k in claves); strs = b"".join(tabla[k] + b"\0" for k in claves)
    n = len(claves); ini = 7 * 4 + 16 * n
    tabo, tabt, po, pt = [], [], ini, ini + len(ids)
    for k in claves:
        tabo.append((len(k), po)); po += len(k) + 1
    for k in claves:
        tabt.append((len(tabla[k]), pt)); pt += len(tabla[k]) + 1
    cab = struct.pack("<7I", 0x950412de, 0, n, 28, 28 + 8 * n, 0, 0)
    t = b"".join(struct.pack("<II", a, b) for a, b in tabo) + b"".join(struct.pack("<II", a, b) for a, b in tabt)
    pathlib.Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(ruta).write_bytes(cab + t + ids + strs)

def norm(s):
    s = s.replace("&", "").replace("_", "").replace("…", "").replace("...", "").strip().rstrip(":").strip()
    return re.sub(r"\s+", " ", s).lower()

def glosario():
    g = {}
    for l in (aqui.parent / "datos/ui_glosario.tsv").read_text(encoding="utf8").splitlines()[1:]:
        c = l.split("\t")
        if len(c) >= 3 and c[0] and c[2]: g[norm(c[0])] = c[2]
    return g

def acelerador(original, owee):
    """Conserva '...' final y ':' final del texto original."""
    suf = "…" if original.rstrip().endswith("…") else ("..." if original.rstrip().endswith("...") else "")
    if original.rstrip().endswith(":") and not suf: suf = ":"
    return owee + suf

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--origen", default="/usr/share/locale/es/LC_MESSAGES")
    ap.add_argument("--salida", default=str(pathlib.Path.home() / ".local/share/locale"))
    ap.add_argument("--dominios", default="")
    a = ap.parse_args()
    g = glosario()
    solo = set(filter(None, a.dominios.split(",")))
    total = col = dom = 0; top = collections.Counter()
    for mo in sorted(pathlib.Path(a.origen).glob("*.mo")):
        if solo and mo.stem not in solo: continue
        try: t = leer_mo(mo)
        except Exception: continue
        rom, scr = {}, {}
        for k in t:
            if k == b"" or b"\0" in k: continue          # cabecera y plurales: se omiten
            orig = k.split(b"\x04", 1)[-1].decode("utf8", "replace")   # con contexto (msgctxt) se compara el texto
            o = g.get(norm(orig))
            if o:
                texto = acelerador(orig, o)
                rom[k] = texto.encode("utf8"); scr[k] = to_script(texto).encode("utf8"); top[norm(orig)] += 1
        total += len(t)
        if not rom: continue
        cab = b"Content-Type: text/plain; charset=UTF-8\nLanguage: qow\nPlural-Forms: nplurals=1; plural=0;\n"
        rom[b""] = cab; scr[b""] = cab.replace(b"Language: qow", b"Language: qow@owee")
        escribir_mo(pathlib.Path(a.salida) / "qow/LC_MESSAGES" / mo.name, rom)
        escribir_mo(pathlib.Path(a.salida) / "qow@owee/LC_MESSAGES" / mo.name, scr)
        col += len(rom) - 1; dom += 1
    print(f"{dom} catalogos con traduccion en Owee ({col} textos de {total} revisados) -> {a.salida}")
    print("mas frecuentes:", ", ".join(f"{k} ({n})" for k, n in top.most_common(12)))

if __name__ == "__main__":
    main()
