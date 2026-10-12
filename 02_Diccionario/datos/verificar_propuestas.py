#!/usr/bin/env python3
"""Verifica propuestas de gramatica/vocabulario contra todo el lexico: colisiones exactas, vecinos acusticos
(distancia 1 con la misma cantidad de silabas) y formas con el mismo significado."""
import re, sys, pathlib, itertools, collections
aqui = pathlib.Path(__file__).resolve().parent
SIL = re.compile(r"(?:sh|ch|[pbtdkgfsmnlr])?[aeou]")
def sil(w): s = SIL.findall(w); return s if "".join(s) == w else None
def lev(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]
L = {}
for f in ("lexico.tsv", "lexico_ciencias.tsv"):
    for l in (aqui / f).read_text(encoding="utf8").splitlines()[1:]:
        c = l.split("\t"); L[c[0]] = c[3]
roots = {w: m for w, m in L.items() if "-" not in w and sil(w)}
def vecinos(w):
    n = len(sil(w))
    return [(x, m) for x, m in roots.items() if x != w and len(sil(x)) == n and lev(w, x) == 1]
def metatesis(w):
    s = sil(w)
    if len(s) != 2: return []
    inv = s[0][:-1] + s[1][-1] + s[1][:-1] + s[0][-1]   # intercambia vocales
    return [(inv, roots[inv])] if inv in roots and inv != w else []
if len(sys.argv) > 1:
    for w in sys.argv[1:]:
        print(f"{w} = {L.get(w, '(no existe)')}")
        for x, m in vecinos(w): print(f"   cercano: {x} = {m}")
        for x, m in metatesis(w): print(f"   metatesis: {x} = {m}")
    sys.exit()
# sinonimos: misma glosa en dos formas distintas
g = collections.defaultdict(list)
for w, m in L.items(): g[m.lower()].append(w)
print("== Mismo significado en mas de una forma:")
for m, ws in g.items():
    if len(ws) > 1: print(f"   {m}: {', '.join(ws)}")
