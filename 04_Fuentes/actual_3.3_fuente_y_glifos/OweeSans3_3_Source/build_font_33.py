"""Owee Sans 3.3 Canonical.

- 56 sílabas CV: esqueletos vectoriales exactos de la tabla 'Sistema silábico'
  del Curso Práctico para Adultos (extract_skeletons.py -> skeletons.json),
  trazados de nuevo con grosor uniforme y remates redondos.
- Vocales aisladas A/E/O/U: portador neutro (círculo) + la misma extensión
  direccional, como en Caligrafía Escolar 0.2.
- Dígitos 0-9: Matemáticas 1.0 (0 círculo, 1-3 palos, 4 = ⊐, 5 punto, 6-9 punto + 1..4).
- PUA idéntico a Owee Sans 1/3.x (U+E000..U+E03B, U+E040..U+E049): compatible con el IME.
- Marcas nuevas: U+E03C nexo de compuesto (el guion de sade-kelo) y U+E03D marca de nombre propio.

    PYTHONPATH=../Owee_Script_2.0_Source/owee-script-2.0-source/.pydeps python3 build_font_33.py
"""
from pathlib import Path
from math import cos, sin, pi
import json, sys, math

from consonantes_v34 import aplicar as consonantes_v34

import pathops
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

ROOT = Path(__file__).parent
UPM = 1000
S = 50             # unidades de fuente por punto PDF de la tabla
CY_FONT = 330      # dónde cae el centro de la celda (y=0 de la tabla)
STROKE = 0.82      # grosor relativo al de la tabla (3.07 pt consonante, 2.63 vocal)
MIN_W = 105        # grosor mínimo en unidades, para que nada quede fino
SIDE = 60          # margen lateral de las sílabas
DIGIT_SIDE = 170   # los dígitos llevan más aire para que 1|2|3 no se fundan
SPACE = 330
ASC, DESC = 900, -200
N = 24             # segmentos por curva

# Dos estilos desde el mismo esqueleto canónico: sólo cambian proporción,
# inclinación, grosor y espaciado; la forma de cada glifo es la misma.
STYLES = {
    # computadora: más bajo y ancho, trazo grueso, texto compacto
    "sans": dict(family="Owee Sans 3.3 Canonical", ps="OweeSans3_3-Canonical-Regular",
                 SX=0.96, SY=0.88, SLANT=0, STROKE=0.90, MIN_W=110, SIDE=32, DIGIT_SIDE=150),
    # a mano: más alto y estrecho, inclinado, trazo más fino
    "school": dict(family="Owee School 3.3", ps="OweeSchool3_3-Regular",
                   SX=0.84, SY=1.22, SLANT=13, STROKE=0.60, MIN_W=78, SIDE=55, DIGIT_SIDE=150),
}
SX, SY, SLANT = 1.0, 1.0, 0

CONS = ["p","b","t","d","k","g","f","s","m","n","l","r","sh","ch"]
VOW = ["a","e","o","u"]


def bez(p0, c1, c2, p1, n=N):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u**3*p0[0] + 3*u*u*t*c1[0] + 3*u*t*t*c2[0] + t**3*p1[0],
                    u**3*p0[1] + 3*u*u*t*c1[1] + 3*u*t*t*c2[1] + t**3*p1[1]))
    return out


def circle(pen, cx, cy, r, n=32):
    # sentido horario, como los rectángulos: la unión no deja huecos
    pts = [(cx + r*cos(-2*pi*i/n), cy + r*sin(-2*pi*i/n)) for i in range(n)]
    pen.moveTo(pts[0])
    for p in pts[1:]: pen.lineTo(p)
    pen.closePath()


def tf(p):
    """Proporción e inclinación del estilo, alrededor del centro de la celda."""
    x, y = p[0] * SX, CY_FONT + (p[1] - CY_FONT) * SY
    return (x + (y - CY_FONT) * math.tan(math.radians(SLANT)), y)


def stroke(strokes, dots=()):
    strokes = [(w, [tf(p) for p in pts]) for w, pts in strokes]
    dots = [(*tf((x, y)), r) for x, y, r in dots]
    """strokes: [(ancho, [puntos])]. Traza cada polilínea con remates redondos."""
    path = pathops.Path(); pen = path.getPen()
    for w, pts in strokes:
        r = w / 2
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            dx, dy = x2 - x1, y2 - y1; L = (dx*dx + dy*dy) ** .5
            if L < 1e-6: continue
            nx, ny = -dy/L*r, dx/L*r
            pen.moveTo((x1+nx, y1+ny)); pen.lineTo((x2+nx, y2+ny))
            pen.lineTo((x2-nx, y2-ny)); pen.lineTo((x1-nx, y1-ny)); pen.closePath()
        for x, y in pts:
            circle(pen, x, y, r)
    for x, y, r in dots:
        circle(pen, x, y, r, 40)
    return pathops.simplify(path, fix_winding=True, clockwise=True)


def width(w_pt):
    return max(MIN_W, w_pt * S * STROKE)


def to_font(pt):
    return (pt[0] * S, pt[1] * S + CY_FONT)


def syllable(parts):
    strokes = []
    for part in parts:
        pts = []
        for sg in part["segments"]:
            if sg[0] == 'L':
                seg = [to_font(sg[1]), to_font(sg[2])]
            else:
                seg = bez(*[to_font(p) for p in sg[1:]])
            pts += seg if not pts else seg[1:]
        strokes.append((width(part["width"]), pts))
    return stroke(strokes)


# ---- vocales aisladas: portador neutro + extensión ----
VW = width(2.632171)
CW = width(3.070866)
R_CARRIER = 150
EXT = 190


def vowel(v):
    cx, cy = 0, CY_FONT
    ring = [(cx + R_CARRIER*cos(2*pi*i/48), cy + R_CARRIER*sin(2*pi*i/48)) for i in range(49)]
    d = {"a": (0, 1), "e": (-1, 0), "o": (1, 0), "u": (0, -1)}[v]
    start = (cx + d[0]*R_CARRIER, cy + d[1]*R_CARRIER)
    end = (start[0] + d[0]*EXT, start[1] + d[1]*EXT)
    return stroke([(CW, ring), (VW, [start, end])])


# ---- dígitos (Matemáticas 1.0) ----
DH = 560                    # altura de los palos
DB = CY_FONT - DH / 2
BAR_GAP = 195
DOT_R = 80


def digit(n):
    strokes, dots, x = [], [], 0
    if n == 0:
        r = DH / 2
        pts = [(r*0.8*cos(2*pi*i/48), CY_FONT + r*sin(2*pi*i/48)) for i in range(49)]
        return stroke([(CW, pts)])
    if n >= 5:
        dots.append((0, CY_FONT, DOT_R)); x = DOT_R + 110; n -= 5
    if 1 <= n <= 3:
        for i in range(n):
            strokes.append((CW, [(x + i*BAR_GAP, DB), (x + i*BAR_GAP, DB + DH)]))
    elif n == 4:
        w = 300
        strokes.append((CW, [(x, DB + DH), (x + w, DB + DH), (x + w, DB), (x, DB)]))
    return stroke(strokes, dots)


# ---- marcas de escritura (U+E03C, U+E03D) ----
JOIN_LEN = 240
def joiner():
    """U+E03C nexo de compuesto: barra baja con remates redondos, visible entre dos bloques (sade-kelo)."""
    y = CY_FONT - 250
    return stroke([(CW * 0.9, [(0, y), (JOIN_LEN, y)])])


def namemark():
    """U+E03D marca de nombre propio: dos puntos apilados (el 5 es un solo punto)."""
    return stroke([], dots=[(0, CY_FONT + 170, 85), (0, CY_FONT - 170, 85)])


def glyph(path, side):
    b = path.bounds; shift = side - b[0]
    pen = TTGlyphPen(None)
    for verb, pts in path.segments:
        pts = [(round(x + shift), round(y)) for x, y in pts]
        if verb == "moveTo": pen.moveTo(pts[0])
        elif verb == "lineTo": pen.lineTo(pts[0])
        elif verb == "qCurveTo": pen.qCurveTo(*pts)
        elif verb == "curveTo": pen.curveTo(*pts)
        elif verb == "closePath": pen.closePath()
    return pen.glyph(), round(b[2] - b[0]) + 2 * side


def main():
    style = sys.argv[1] if len(sys.argv) > 1 else "sans"
    st = STYLES[style]
    g_ = globals()
    for k in ("SX", "SY", "SLANT", "STROKE", "MIN_W", "SIDE", "DIGIT_SIDE"):
        g_[k] = st[k]
    g_["VW"] = width(2.632171); g_["CW"] = width(3.070866)
    sk = consonantes_v34(json.loads((ROOT / "skeletons.json").read_text()))
    outlines = {}
    cp = 0xE000
    for v in VOW:
        outlines[cp] = (vowel(v), SIDE); cp += 1
    for c in CONS:
        for v in VOW:
            outlines[cp] = (syllable(sk[c + v]), SIDE); cp += 1
    assert cp == 0xE03C
    outlines[0xE03C] = (joiner(), 40)
    outlines[0xE03D] = (namemark(), 80)
    for n in range(10):
        outlines[0xE040 + n] = (digit(n), DIGIT_SIDE)

    order = [".notdef", "space"] + [f"uni{c:04X}" for c in sorted(outlines)]
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    glyphs = {".notdef": TTGlyphPen(None).glyph(), "space": TTGlyphPen(None).glyph()}
    metrics = {".notdef": (SPACE, 0), "space": (SPACE, 0)}
    for c, (path, side) in outlines.items():
        g, adv = glyph(path, side)
        glyphs[f"uni{c:04X}"] = g; metrics[f"uni{c:04X}"] = (adv, side)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=ASC, descent=DESC, lineGap=0)
    cmap = {c: f"uni{c:04X}" for c in outlines}
    cmap[0x20] = "space"; cmap[0xA0] = "space"
    fb.setupCharacterMap(cmap)
    fb.setupNameTable({
        "familyName": st["family"], "styleName": "Regular",
        "uniqueFontIdentifier": st["family"], "fullName": st["family"] + " Regular",
        "psName": st["ps"], "version": "Version 3.4",
    })
    fb.setupOS2(version=4, sTypoAscender=ASC, sTypoDescender=DESC, sTypoLineGap=0,
                usWinAscent=ASC, usWinDescent=-DESC, sxHeight=660, sCapHeight=660,
                fsSelection=0x40 | 0x80, achVendID="OWEE")
    fb.setupPost(); fb.setupMaxp()
    g = fb.font["glyf"]
    ys = [(g[n].yMin, g[n].yMax) for n in order if g[n].numberOfContours]
    lo, hi = min(a for a, _ in ys), max(b for _, b in ys)
    assert DESC <= lo and hi <= ASC, (lo, hi)
    out = ROOT / (st["ps"] + ".ttf")
    fb.save(out)
    print("Creado:", out, "glifos:", len(outlines), "y:", lo, "..", hi)


if __name__ == "__main__":
    main()
