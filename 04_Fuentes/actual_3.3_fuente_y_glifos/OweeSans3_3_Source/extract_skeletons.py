"""Extrae los esqueletos (líneas centrales) de las 56 sílabas CV de la tabla
'Sistema silábico' (pág. 4) de Owee_1.0_Curso_Practico_Adultos.pdf.

    pdftocairo -svg -f 4 -l 4 Owee_1.0_Curso_Practico_Adultos.pdf curso_adultos_p4.svg
    python3 extract_skeletons.py      -> skeletons.json

Coordenadas en puntos PDF, relativas al origen de cada celda (y hacia arriba).
Cada trazo guarda su grosor original: 3.07 = consonante, 2.63 = vocal, 2.30 = cierre/cruce.
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent
CONS = ["p","b","t","d","k","g","f","s","m","n","l","r","sh","ch"]
VOW = ["a","e","o","u"]

s = (ROOT / "curso_adultos_p4.svg").read_text()
raw = [(float(w), d) for w, d in
       re.findall(r'<path fill="none" stroke-width="([\d.]+)"[^>]*? d="([^"]+)"', s)
       if float(w) > 2]

def parse(d):
    """Devuelve una lista de segmentos: ('L', p0, p1) o ('C', p0, c1, c2, p1)."""
    toks = re.findall(r'[MLC]|-?[\d.]+', d)
    segs, cur, i = [], None, 0
    while i < len(toks):
        t = toks[i]
        if t == 'M':
            cur = (float(toks[i+1]), float(toks[i+2])); i += 3
        elif t == 'L':
            p = (float(toks[i+1]), float(toks[i+2])); segs.append(('L', cur, p)); cur = p; i += 3
        elif t == 'C':
            c1 = (float(toks[i+1]), float(toks[i+2])); c2 = (float(toks[i+3]), float(toks[i+4]))
            p = (float(toks[i+5]), float(toks[i+6])); segs.append(('C', cur, c1, c2, p)); cur = p; i += 7
        else:
            i += 1
    return segs

X0, DX = 175.27, 87.8725
items = []
for w, d in raw:
    segs = parse(d)
    allp = [p for sg in segs for p in sg[1:]]
    cx = sum(p[0] for p in allp) / len(allp); cy = sum(p[1] for p in allp) / len(allp)
    col = round((segs[0][1][0] - X0) / DX)
    items.append((w, segs, col, cy))

# filas: agrupa por y y ajusta una rejilla de paso constante
ys = sorted(cy for *_, cy in items)
clusters = []
for y in ys:
    if clusters and y - clusters[-1][-1] < 15: clusters[-1].append(y)
    else: clusters.append([y])
assert len(clusters) == 14, len(clusters)
means = [sum(c) / len(c) for c in clusters][::-1]          # de arriba (P) a abajo (CH)
n = len(means); k = list(range(n))
pitch = (sum(ki*m for ki, m in zip(k, means)) - sum(k)*sum(means)/n) / (sum(ki*ki for ki in k) - sum(k)**2/n)
y0 = sum(means)/n - pitch*sum(k)/n

out = {}
for w, segs, col, cy in items:
    row = round((cy - y0) / pitch)
    ox, oy = X0 + col * DX, y0 + row * pitch
    key = CONS[row] + VOW[col]
    loc = [[sg[0]] + [[round(p[0]-ox, 3), round(p[1]-oy, 3)] for p in sg[1:]] for sg in segs]
    out.setdefault(key, []).append({"width": w, "segments": loc})

assert len(out) == 56, len(out)
(ROOT / "skeletons.json").write_text(json.dumps(out, indent=1))
print("sílabas:", len(out), "paso de fila %.3f" % pitch)
