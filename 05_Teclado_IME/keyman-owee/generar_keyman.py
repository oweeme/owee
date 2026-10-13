#!/usr/bin/env python3
"""Genera el teclado Keyman de Owee (Windows, macOS, Linux, Android, iOS y navegadores) a partir del mismo mapa de
glifos que usa el IME de Fcitx5 (../fcitx5-owee-1.2-marks/data/owee-pua-map.json).

Comportamiento (igual que el IME de Linux, pero silaba a silaba):
  - escribes romano: consonante + vocal -> el glifo de la silaba (su, ke, sha...); vocal sola -> glifo;
  - 'sh' y 'ch' se reconocen como una consonante;
  - guion tras un glifo -> nexo de compuesto U+E03C (sade-kelo);
  - mayuscula inicial -> marca de nombre propio U+E03D + glifo (Ana);
  - 0-9 -> cifras Owee U+E040..E049; AltGr + cifra escribe la cifra normal.
Uso: python3 generar_keyman.py   (escribe source/owee.kmn, source/owee.keyman-touch-layout y source/owee.kps)"""
import json, pathlib
aqui = pathlib.Path(__file__).resolve().parent
mapa = json.loads((aqui.parent / "fcitx5-owee-1.2-marks/data/owee-pua-map.json").read_text(encoding="utf8"))["syllables"]
src = aqui / "source"; src.mkdir(exist_ok=True)
U = lambda cp: cp.replace("+", "_") if False else cp  # 'U+E000' ya es sintaxis Keyman
CONS = ["p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"]
VOC = "aeou"

L = []
w = L.append
w("c Teclado Owee 1.0 para Keyman. Generado por generar_keyman.py: no editar a mano.")
w("c Escribe en romano y obtiene Owee Script (glifos en la zona privada U+E000..E049).")
w("store(&VERSION) '17.0'")
w("store(&NAME) 'Owee'")
w("store(&KEYBOARDVERSION) '1.0'")
w("store(&COPYRIGHT) '(c) 2026 Hector Martinez - MIT'")
w("store(&MESSAGE) 'Escribe en romano: suna -> glifos Owee. Guion para compuestos, Mayuscula para nombres, AltGr+cifra para cifras normales.'")
w("store(&TARGETS) 'any'")
w("store(&LAYOUTFILE) 'owee.keyman-touch-layout'")
w("")
w("begin Unicode > use(main)")
w("store(glifos) U+E000 .. U+E03B")
w("")
w("group(main) using keys")
w("")
w("c --- cifras: 0-9 -> glifos numericos; AltGr + cifra -> cifra normal")
for d in range(10):
    w(f"+ [RALT K_{d}] > '{d}'")
    w(f"+ '{d}' > U+{0xE040 + d:04X}")
w("")
w("c --- sh y ch (minuscula y mayuscula inicial)")
for c in ("sh", "ch"):
    w(f"'{c[0]}' + 'h' > '{c}'")
    w(f"'{c[0].upper()}' + 'h' > '{c[0].upper()}h'")
w("")
w("c --- silabas: consonante + vocal -> glifo; con mayuscula inicial -> marca de nombre + glifo")
for c in CONS:
    for v in VOC:
        cp = mapa[c + v]
        cap = c[0].upper() + c[1:]
        w(f"'{c}' + '{v}' > {cp}")
        w(f"'{cap}' + '{v}' > U+E03D {cp}")
w("")
w("c --- vocal sola (con mayuscula: nombre propio)")
for v in VOC:
    w(f"+ '{v}' > {mapa[v]}")
    w(f"+ '{v.upper()}' > U+E03D {mapa[v]}")
w("")
w("c --- guion tras un glifo -> nexo de compuesto")
w("any(glifos) + '-' > index(glifos,1) U+E03C")
(src / "owee.kmn").write_text("\n".join(L) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- touch (Android / iOS / navegadores)
def tecla(i, txt, **kw):
    d = {"id": i, "text": txt}; d.update(kw); return d
def fila(n, teclas): return {"id": n, "key": teclas}
def letras(up):
    f = (lambda s: s.upper()) if up else (lambda s: s)
    R = lambda s: [tecla("K_" + c.upper(), f(c)) for c in s]
    return [
        fila(1, R("ptbdkgf")),
        fila(2, R("smnlrhc")),
        fila(3, [tecla("K_SHIFT", "*Shift*", sp="1", width="130", nextlayer="default" if up else "shift")] + R("aeou") + [tecla("K_BKSP", "*BkSp*", sp="1", width="130")]),
        fila(4, [tecla("K_LOPT", "*Menu*", sp="1", width="110"), tecla("K_NUMLOCK", "*123*", sp="1", width="130", nextlayer="numeric"), tecla("K_HYPHEN", "-", width="110"), tecla("K_SPACE", "", sp="0", width="360", nextlayer="default"),
                 tecla("K_PERIOD", ".", width="110"), tecla("K_ENTER", "*Enter*", sp="1", width="130")]),
    ]
numeric = [
    fila(1, [tecla("K_" + str(d), str(d)) for d in range(1, 10)] + [tecla("K_0", "0")]),
    fila(2, [tecla("K_HYPHEN", "-"), tecla("K_PERIOD", "."), tecla("K_COMMA", ","), tecla("K_COLON", ":"), tecla("K_SLASH", "/"), tecla("K_QUOTE", "'"), tecla("K_BKSP", "*BkSp*", sp="1", width="130")]),
    fila(3, [tecla("K_LOPT", "*Menu*", sp="1", width="110"), tecla("K_LOWER", "*abc*", sp="1", width="130", nextlayer="default"), tecla("K_SPACE", "", sp="0", width="500"), tecla("K_ENTER", "*Enter*", sp="1", width="130")]),
]
capas = [{"id": "default", "row": letras(False)}, {"id": "shift", "row": letras(True)}, {"id": "numeric", "row": numeric}]
touch = {"tablet": {"font": "OweeSans", "layer": capas, "displayUnderlying": False, "defaultHint": "none"},
         "phone": {"font": "OweeSans", "layer": capas, "displayUnderlying": False, "defaultHint": "none"}}
(src / "owee.keyman-touch-layout").write_text(json.dumps(touch, indent=2, ensure_ascii=False), encoding="utf-8")

# ---------------------------------------------------------------- paquete .kmp
kps = '''<?xml version="1.0" encoding="utf-8"?>
<Package>
  <System>
    <KeymanDeveloperVersion>18.0.253.0</KeymanDeveloperVersion>
    <FileVersion>7.0</FileVersion>
  </System>
  <Options>
    <ReadMeFile>readme.htm</ReadMeFile>
    <FollowKeyboardVersion/>
  </Options>
  <StartMenu><Folder>Owee</Folder><Items/></StartMenu>
  <Info>
    <Name URL="https://oweeme.com">Owee</Name>
    <Copyright URL="">(c) 2026 Hector Martinez</Copyright>
    <Author URL="mailto:hector@oweeme.com">Proyecto Owee</Author>
    <Version URL="">1.0</Version>
    <Description URL="">Teclado Owee: escribe en romano y obtén la escritura Owee Script (glifos). Incluye cifras Owee y compuestos.</Description>
  </Info>
  <Files>
    <File><Name>../build/owee.kmx</Name><Description>Keyboard Owee</Description><CopyLocation>0</CopyLocation><FileType>.kmx</FileType></File>
    <File><Name>../build/owee.js</Name><Description>Keyboard Owee (web, Android, iOS)</Description><CopyLocation>0</CopyLocation><FileType>.js</FileType></File>
    <File><Name>OweeSans-Regular.ttf</Name><Description>Fuente Owee Sans</Description><CopyLocation>0</CopyLocation><FileType>.ttf</FileType></File>
    <File><Name>readme.htm</Name><Description>Lee esto</Description><CopyLocation>0</CopyLocation><FileType>.htm</FileType></File>
  </Files>
  <Keyboards>
    <Keyboard>
      <Name>Owee</Name>
      <ID>owee</ID>
      <Version>1.0</Version>
      <OSKFont>OweeSans-Regular.ttf</OSKFont>
      <DisplayFont>OweeSans-Regular.ttf</DisplayFont>
      <Languages><Language ID="qow">Owee</Language></Languages>
    </Keyboard>
  </Keyboards>
</Package>
'''
(src / "owee.kps").write_text(kps, encoding="utf-8")
(src / "readme.htm").write_text("""<!doctype html><meta charset="utf-8"><title>Teclado Owee</title>
<h1>Teclado Owee</h1><p>Escribe en romano y se convierte en Owee Script: <code>su</code> + <code>na</code> = suna.</p>
<ul><li><b>sh</b> y <b>ch</b> son una sola consonante.</li><li>Un <b>guion</b> tras una sílaba une compuestos (<code>sade-kelo</code>).</li>
<li>Una <b>mayúscula</b> inicial marca un nombre propio.</li><li>Las cifras 0-9 salen en Owee; <b>AltGr + cifra</b> escribe la cifra normal.</li>
<li>Sin vocal tras la consonante, el texto queda en romano para no perderlo.</li></ul>
<p>Más información: https://github.com/oweeme/owee</p>""", encoding="utf-8")
print("escrito", src)
