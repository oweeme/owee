#!/usr/bin/env python3
"""Comprueba que todo el léxico se escribe con los glifos 3.4 y busca palabras que se distingan por UNA sílaba
cuyos dos glifos se parezcan mucho (pares mínimos visuales).

1. Cada sílaba de cada palabra tiene su glifo en la fuente (no queda romano suelto).
2. Se mide el parecido (IoU) entre los 56 glifos de sílaba, tal cual están en la fuente, y se listan los pares
   de palabras del léxico con el mismo número de sílabas que sólo difieren en una sílaba parecida.

    python3 auditar_palabras_v4.py [umbral]        umbral de parecido entre glifos de sílaba (por defecto 0.80)"""
import itertools, pathlib, re, sys
import numpy as np
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
aqui = pathlib.Path(__file__).resolve().parent
RAIZ = aqui.parents[2]
FUENTE = RAIZ / "04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3/fonts/ttf/OweeSans-Regular.ttf"
CONS = ["p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"]
SIL = re.compile(r"(sh|ch|[pbtdkgfsmnlr])?([aeou])")
cp = {}
for i, v in enumerate("aeou"): cp[v] = 0xE000 + i
for ci, c in enumerate(CONS):
    for vi, v in enumerate("aeou"): cp[c + v] = 0xE004 + ci * 4 + vi

def silabas(w):
    s = [(c or "") + v for c, v in SIL.findall(w)]
    return s if "".join(s) == w else None

def main():
    umbral = float(sys.argv[1]) if len(sys.argv) > 1 else 0.80
    cmap = TTFont(FUENTE).getBestCmap()
    lex = {}
    for f in ("lexico.tsv", "lexico_ciencias.tsv"):
        for l in (RAIZ / "02_Diccionario/datos" / f).read_text(encoding="utf8").splitlines()[1:]:
            c = l.split("\t")
            if len(c) > 3: lex[c[0]] = c[3]
    sin_glifo = {}
    for w in lex:
        for p in w.split("-"):
            ss = silabas(p)
            if ss is None or any(cp[s] not in cmap for s in ss): sin_glifo[w] = p
    print(f"Palabras del léxico: {len(lex)} · sin glifo o con fonología inválida: {len(sin_glifo)}", *list(sin_glifo)[:5])
    f = ImageFont.truetype(str(FUENTE), 120)
    bm = {}
    for s, c in cp.items():
        im = Image.new("L", (260, 260), 0); ImageDraw.Draw(im).text((10, 20), chr(c), font=f, fill=255)
        bm[s] = np.array(im) > 100
    iou = lambda a, b: (a & b).sum() / max((a | b).sum(), 1)
    sims = {frozenset((a, b)): iou(bm[a], bm[b]) for a, b in itertools.combinations([s for s in cp if len(s) > 1], 2)}
    print("Sílabas más parecidas entre sí (glifo completo):")
    for k, v in sorted(sims.items(), key=lambda x: -x[1])[:8]: print(f"  {' ~ '.join(sorted(k))}  {v:.2f}")
    por_larga = {}
    for w in lex:
        ss = [s for p in w.split("-") for s in (silabas(p) or [])]
        if ss: por_larga.setdefault(len(ss), []).append((w, ss))
    pares = []
    for n, ws in por_larga.items():
        for (w1, s1), (w2, s2) in itertools.combinations(ws, 2):
            dif = [i for i in range(n) if s1[i] != s2[i]]
            if len(dif) == 1 and sims.get(frozenset((s1[dif[0]], s2[dif[0]])), 0) >= umbral:
                pares.append((sims[frozenset((s1[dif[0]], s2[dif[0]]))], w1, w2, s1[dif[0]], s2[dif[0]]))
    print(f"Pares de palabras que sólo difieren en una sílaba con glifos parecidos (>= {umbral}): {len(pares)}")
    for v, w1, w2, a, b in sorted(pares, reverse=True)[:25]:
        print(f"  {w1} = {lex[w1][:30]} | {w2} = {lex[w2][:30]}   ({a} ~ {b} {v:.2f})")
    return 1 if sin_glifo else 0

if __name__ == "__main__":
    sys.exit(main())
