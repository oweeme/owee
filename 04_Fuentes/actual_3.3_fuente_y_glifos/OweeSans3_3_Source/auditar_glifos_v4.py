"""Auditoría de parecidos entre los glifos de la propuesta v4 (consonantes, vocales sueltas y marcas).

Rasteriza cada glifo, lo normaliza a un cuadrado y mide el solapamiento (IoU) con cada otro
glifo tal cual y también girado 90/180/270° y espejado. Un valor alto del segundo tipo entre dos
consonantes que NO son pareja (p/b, t/d, k/g, sh/ch) es el problema que se quiere evitar.

    python3 auditar_glifos_v4.py
"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw
import glifos_v4 as g

PAREJAS = {frozenset(p) for p in [("p", "b"), ("t", "d"), ("k", "g"), ("sh", "ch"), ("l", "r")]}


def bez(p0, c1, c2, p1, n=20):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u**3*p0[0] + 3*u*u*t*c1[0] + 3*u*t*t*c2[0] + t**3*p1[0],
                    u**3*p0[1] + 3*u*u*t*c1[1] + 3*u*t*t*c2[1] + t**3*p1[1]))
    return out


def raster(parts):
    im = Image.new("L", (400, 400), 0); d = ImageDraw.Draw(im); S = 22
    for p in parts:
        w = p["width"] * S * 0.9; pl = []
        for sg in p["segments"]:
            pts = [tuple(sg[1]), tuple(sg[2])] if sg[0] == "L" else bez(*[tuple(q) for q in sg[1:]])
            pl += pts if not pl else pts[1:]
        xy = [(200 + x * S, 200 - y * S) for x, y in pl]
        if len(xy) >= 2: d.line(xy, fill=255, width=int(w))
        for x, y in xy: d.ellipse([x - w/2, y - w/2, x + w/2, y + w/2], fill=255)
    return im


def norm(im, size=64):
    return np.array(im.crop(im.getbbox()).resize((size, size))) > 100


def iou(a, b): return (a & b).sum() / max((a | b).sum(), 1)


def giros(a):
    out = []
    for k in range(4):
        r = np.rot90(a, k); out += [r, np.fliplr(r)]
    return out[1:]          # sin la identidad


def main():
    sk = {}; g.aplicar(sk, "sans")
    items = {c: norm(raster(sk[c + "a"][:-1])) for c in g.C}
    for v in "aeou": items["vocal " + v] = norm(raster(g.vowel_isolated(v)))
    items["marca de nombre"] = norm(raster(g.name_mark()))
    items["nexo"] = norm(raster(g.joiner()))
    filas = []
    for k1, k2 in itertools.combinations(items, 2):
        A, B = items[k1], items[k2]
        filas.append((iou(A, B), max(iou(A, t) for t in giros(B)), k1, k2))
    print("Giros/espejos casi idénticos entre consonantes que no son pareja (>= 0.90):")
    malos = [f for f in filas if f[1] >= 0.90 and f[2] in g.C and f[3] in g.C
             and frozenset((f[2], f[3])) not in PAREJAS]
    for _, gir, k1, k2 in malos: print(f"  {k1} ~ {k2}  {gir:.2f}")
    if not malos: print("  ninguno")
    print("Iguales sin girar (>= 0.90), cualquier glifo:")
    iguales = [f for f in filas if f[0] >= 0.90]
    for d, _, k1, k2 in iguales: print(f"  {k1} ~ {k2}  {d:.2f}")
    if not iguales: print("  ninguno")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
