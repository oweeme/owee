#!/usr/bin/env python3
"""Audita el vocabulario cientifico: fonologia, colisiones con el lexico base, y parejas casi identicas."""
import re, itertools, pathlib, sys
aqui = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(aqui))
from ciencias_fuente import RAICES, COMPUESTOS
SIL = re.compile(r"(?:sh|ch|[pbtdkgfsmnlr])?[aeou]")
def sil(w):
    s = SIL.findall(w); return s if "".join(s) == w else None
def lev(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]
base = {l.split("\t")[0]: l.split("\t")[3] for l in (aqui / "lexico.tsv").read_text(encoding="utf8").splitlines()[1:]}
sci = {r[0]: r for r in RAICES}
print("== 1. Fonologia invalida (no cumple V/CV):")
for w, c, d, s in RAICES:
    if not sil(w): print(f"   {w:8} {c}  [{d}]")
print("== 2. Colision exacta con el lexico base:")
for w in sci:
    if w in base: print(f"   {w}: ciencias='{sci[w][1]}'  base='{base[w]}'")
print("== 3. Parejas a distancia 1 (riesgo de confusion al oir), solo palabras de 2+ silabas:")
allw = {**{w: ("base", m) for w, m in base.items()}, **{w: (r[2], r[1]) for w, r in sci.items()}}
n = 0
for a, b in itertools.combinations(sorted(allw), 2):
    if len(a) >= 4 and len(b) >= 4 and sil(a) and sil(b) and len(sil(a)) == len(sil(b)) and lev(a, b) == 1:
        n += 1; print(f"   {a:7} {allw[a][1][:28]:28} ~ {b:7} {allw[b][1][:28]}")
print(f"   total: {n}")
print("== 4. Raices usadas en compuestos que no existen en base ni ciencias:")
for f, m, d, *_ in COMPUESTOS:
    for p in f.split("-"):
        if p not in base and p not in sci: print(f"   {f}: '{p}' no definido")
print(f"== Resumen: {len(sci)} raices cientificas, {len(COMPUESTOS)} compuestos")
