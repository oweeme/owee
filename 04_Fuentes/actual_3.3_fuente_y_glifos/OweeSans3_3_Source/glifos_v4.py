"""Owee Script 4 (propuesta): sistema de glifos geométrico y por familias.

Un solo esqueleto de líneas rectas y círculos, dibujado de dos maneras:
  sans    recto, en bloque (pantalla, teclado, pancartas)
  school  los mismos trazos con las esquinas redondeadas (escritura a mano, fluido)

Sílaba = consonante en un recuadro central + una barra de vocal suelta (con aire)
pegada a un lado del recuadro:  a arriba · e izquierda · o derecha · u abajo.
La barra es corta y nunca toca la consonante, así no se confunde con sus trazos.

Consonantes (rasgo = significado, igual en todas las familias):
    labiales   m ▯▯ cuadro con división · p ⊔ abierta arriba · b ⊔ con barra · f ⊏ abierta de lado
    dentales   t Λ · d A (barra = sonora) · s Z (en la mano, S) · n ○
               l <  · r <· (la r lleva un punto)
    velares    k ┐ · g ┐ con barra
    palatales  sh X · ch X con raya vertical (✱)
Barra al medio = sonora (b, d, g). Coordenadas en pt de la tabla; y hacia arriba.
"""
import math

W = 2.0             # grosor nominal en pt (el estilo lo sube al mínimo de su fuente)
DOT_W = 3.6
MIN_W = {"sans": 88, "school": 64}   # grosor del trazo en unidades de fuente (1000 por em)
X0, X1, XC = -1.2, 7.8, 3.3          # recuadro de la consonante
Y0, Y1, YC = -4.5, 4.5, 0.0
G = 3.3                              # centro de la barra de vocal, medido desde el borde
BAR = 4.4                            # largo de la barra de vocal

# --- esqueletos: lista de (puntos, cerrado) por trazo; ("dot", x, y) para un punto ---
def box(): return [((X0, Y1), (X0, Y0), (X1, Y0), (X1, Y1), (X0, Y1)), True]

def poly(*pts, closed=False): return (list(pts), closed)

MIDY = 0.0
C = {
    "m":  [poly((X0, Y1), (X1, Y1), (X1, Y0), (X0, Y0), closed=True), poly((XC, Y1), (XC, Y0))],
    "p":  [poly((X0, Y1), (X0, Y0), (X1, Y0), (X1, Y1))],
    "b":  [poly((X0, Y1), (X0, Y0), (X1, Y0), (X1, Y1)), poly((X0, MIDY), (X1, MIDY))],
    "f":  [poly((X1, Y1), (X0, Y1), (X0, Y0), (X1, Y0))],
    "t":  [poly((X0, Y0), (XC, Y1), (X1, Y0))],
    "d":  [poly((X0, Y0), (XC, Y1), (X1, Y0)), poly((X0 + 2.0, -1.8), (X1 - 2.0, -1.8))],
    "s":  [poly((X0, Y1), (X1, Y1), (X0, Y0), (X1, Y0))],
    "n":  "circle",
    "l":  [poly((X1, Y1), (X0, YC), (X1, Y0))],
    "r":  [poly((X1, Y1), (X0, YC), (X1, Y0)), ("dot", 5.6, YC)],
    "k":  [poly((X0, Y1), (X1, Y1), (X1, Y0))],
    "g":  [poly((X0, Y1), (X1, Y1), (X1, Y0)), poly((X0, MIDY), (X1, MIDY))],
    "sh": [poly((X0, Y1), (X1, Y0)), poly((X0, Y0), (X1, Y1))],
    "ch": [poly((X0, Y1), (X1, Y0)), poly((X0, Y0), (X1, Y1)), poly((XC, Y1), (XC, Y0))],
}
# la "s" y el zigzag necesitan esquinas más suaves en la mano; el círculo es siempre círculo
CORNER = {"sans": 0.0, "school": 3.6}


def L(a, b): return ["L", list(a), list(b)]
def Cb(a, b, c, d): return ["C", list(a), list(b), list(c), list(d)]


def _circle(cx, cy, rx, ry):
    k = 0.5523
    return [Cb((cx + rx, cy), (cx + rx, cy + k*ry), (cx + k*rx, cy + ry), (cx, cy + ry)),
            Cb((cx, cy + ry), (cx - k*rx, cy + ry), (cx - rx, cy + k*ry), (cx - rx, cy)),
            Cb((cx - rx, cy), (cx - rx, cy - k*ry), (cx - k*rx, cy - ry), (cx, cy - ry)),
            Cb((cx, cy - ry), (cx + k*rx, cy - ry), (cx + rx, cy - k*ry), (cx + rx, cy))]


def _segments(pts, closed, r):
    """Polilínea -> segmentos L/C, con las esquinas redondeadas a distancia r (0 = vivas)."""
    pts = list(pts)
    if closed:
        pts = pts[:-1] if pts[0] == pts[-1] else pts
        mid = ((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2)
        pts = [mid] + pts[1:] + [pts[0], mid]
    if r <= 0:
        return [L(a, b) for a, b in zip(pts, pts[1:])]
    out, cur = [], pts[0]
    for i in range(1, len(pts) - 1):
        a, v, b = pts[i - 1], pts[i], pts[i + 1]
        la, lb = math.dist(a, v), math.dist(v, b)
        ra, rb = min(r, la * 0.5), min(r, lb * 0.5)
        p1 = (v[0] + (a[0] - v[0]) * ra / la, v[1] + (a[1] - v[1]) * ra / la)
        p2 = (v[0] + (b[0] - v[0]) * rb / lb, v[1] + (b[1] - v[1]) * rb / lb)
        if math.dist(cur, p1) > 1e-6: out.append(L(cur, p1))
        c1 = (p1[0] + (v[0] - p1[0]) * 2 / 3, p1[1] + (v[1] - p1[1]) * 2 / 3)
        c2 = (p2[0] + (v[0] - p2[0]) * 2 / 3, p2[1] + (v[1] - p2[1]) * 2 / 3)
        out.append(Cb(p1, c1, c2, p2)); cur = p2
    out.append(L(cur, pts[-1]))
    return out


def vowel_part(v):
    h = BAR / 2
    ex = G + (Y1 - Y0) / 2           # distancia del centro a la barra
    ey = G + (X1 - X0) / 2
    if v == "a": return (W, [L((XC - h, Y1 + G), (XC + h, Y1 + G))])
    if v == "u": return (W, [L((XC - h, Y0 - G), (XC + h, Y0 - G))])
    if v == "e": return (W, [L((X0 - G, YC - h), (X0 - G, YC + h))])
    return (W, [L((X1 + G, YC - h), (X1 + G, YC + h))])


def vowel_isolated(v, d=3.6):
    """A E O U sueltas: un punto portador y la barra de su lado."""
    h = BAR / 2
    pos = {"a": [L((XC - h, d), (XC + h, d))], "u": [L((XC - h, -d), (XC + h, -d))],
           "e": [L((XC - d, -h), (XC - d, h))], "o": [L((XC + d, -h), (XC + d, h))]}[v]
    return [{"width": DOT_W, "segments": [L((XC, YC), (XC, YC))]}, {"width": W, "segments": pos}]


def aplicar(sk, style):
    r = CORNER[style]
    for c, shape in C.items():
        parts = []
        if shape == "circle":
            parts.append({"width": W, "segments": _circle(XC, YC, (X1 - X0) / 2, (Y1 - Y0) / 2)})
        else:
            for item in shape:
                if item[0] == "dot":
                    parts.append({"width": DOT_W, "segments": [L((item[1], item[2]), (item[1], item[2]))]})
                else:
                    pts, closed = item
                    parts.append({"width": W, "segments": _segments(pts, closed, r)})
        for v in "aeou":
            w, segs = vowel_part(v)
            sk[c + v] = parts + [{"width": w, "segments": segs}]
    for v in "aeou":
        sk["_" + v] = vowel_isolated(v)
    return sk
