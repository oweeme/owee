"""Owee Sans 2.1 — glifos según la documentación Owee.

Fuentes de diseño:
- Especificación Normativa Digital §10: familias consonánticas
  P/B lateral curva, T/D arco superior, K/G ángulo, F/S diagonal curva,
  M/N curva inferior, L/R curva ascendente, SH/CH doble curva;
  la segunda consonante de cada familia es la primera con "cierre" o "cruce".
  Vocal = extensión del trazo: A arriba, E izquierda, O derecha, U abajo.
- Caligrafía Escolar Visual 0.2: dibujo de cada familia y de las vocales
  (círculo + trazo recto).
- Matemáticas 1.0: dígitos 0 = círculo, 1-3 = palos, 4 = ⊐,
  5 = punto, 6-9 = punto + 1..4.

Cada glifo se define como líneas centrales; se trazan con grosor uniforme
y remates redondos, y se unen en un contorno limpio con skia-pathops.

    PYTHONPATH=.pydeps python3 build_font_21.py
"""
from pathlib import Path
from math import cos, sin, pi
import json

import pathops
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).parent
UPM = 1000
SW = 96            # grosor de trazo
BOT, TOP = 90, 560 # caja del cuerpo consonántico (línea base = 0)
L0, R0 = 0, 420    # ancho del cuerpo
VLEN = 250         # longitud del trazo vocálico
GAP = 40           # separación entre cuerpo y trazo vocálico cuando no toca
SIDE = 75          # margen lateral
DIGIT_SIDE = 150   # los dígitos llevan más aire: si no, 1|2|3 se funden en una fila de palos
SPACE = 360
N = 48             # segmentos por curva

CX, CY = (L0 + R0) / 2, (BOT + TOP) / 2
H = TOP - BOT


# ---- utilidades de geometría (líneas centrales) ----
def Y(f):  # fracción de la altura del cuerpo -> y
    return BOT + f * H


def X(f):
    return L0 + f * (R0 - L0)


def arc(cx, cy, rx, ry, a0, a1, n=N):
    return [(cx + rx * cos(a0 + (a1 - a0) * i / n),
             cy + ry * sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]


def bez(p0, p1, p2, p3, n=N):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u**3 * p0[0] + 3 * u*u*t * p1[0] + 3 * u*t*t * p2[0] + t**3 * p3[0],
                    u**3 * p0[1] + 3 * u*u*t * p1[1] + 3 * u*t*t * p2[1] + t**3 * p3[1]))
    return out


def join(*parts):
    out = []
    for p in parts:
        out += p if not out else p[1:] if p[0] == out[-1] else p
    return out


# ---- cuerpos consonánticos: lista de trazos (polilíneas) ----
def body_p():   # lateral curva: pierna izquierda + arco que cae a media altura
    r = (R0 - L0) / 2
    return [join([(X(0), Y(0)), (X(0), Y(0.55))],
                 arc(CX, Y(0.55), r, H * 0.45, pi, -0.1 * pi))]


def body_b():   # P cerrada: bucle
    r = (R0 - L0) / 2
    top = arc(CX, Y(0.55), r, H * 0.45, pi, 0)
    low = arc(CX, Y(0.55), r, H * 0.55, 0, -pi)
    return [join([(X(0), Y(0)), (X(0), Y(0.55))], top, low)]


def body_t():   # arco superior tipo "ʔ": arco arriba y caída en diagonal
    return [join(arc(CX, Y(0.68), (R0 - L0) / 2, H * 0.32, pi * 0.95, -pi * 0.25),
                 [(CX + (R0 - L0) / 2 * cos(-pi * 0.25), Y(0.68) + H * 0.32 * sin(-pi * 0.25)),
                  (X(0.38), Y(0))])]


def body_d():   # T cerrada: escudo
    a = arc(CX, Y(0.68), (R0 - L0) / 2, H * 0.32, pi, -pi * 0.25)
    return [join(a, [a[-1], (CX, Y(0)), a[0]])]


def body_k():   # ángulo Λ
    return [[(X(0), Y(0)), (CX, Y(1)), (X(1), Y(0))]]


def body_g():   # K cerrada: triángulo
    return [[(X(0), Y(0)), (CX, Y(1)), (X(1), Y(0)), (X(0), Y(0))]]


def body_f():   # diagonal curva: arco ∩ con piernas abiertas
    return [bez((X(0), Y(0)), (X(0.12), Y(1.3)), (X(0.88), Y(1.3)), (X(1), Y(0)))]


def body_s():   # F con cruce
    # el cruce va alto para no confundirse con el trazo de E/O (a media altura)
    return body_f() + [[(X(0.02), Y(0.78)), (X(0.98), Y(0.78))]]


def body_m():   # curva inferior: copa
    r = (R0 - L0) / 2
    return [join([(X(0), Y(1)), (X(0), Y(0.5))],
                 arc(CX, Y(0.5), r, H * 0.5, pi, 2 * pi),
                 [(X(1), Y(0.5)), (X(1), Y(1))])]


def body_n():   # M cerrada: copa con tapa
    return [body_m()[0] + [(X(0), Y(1))]]


def body_l():   # curva ascendente
    return [bez((X(0.05), Y(0)), (X(0.25), Y(0.75)), (X(0.45), Y(1)), (X(1), Y(1)))]


def body_r():   # L con cruce
    return body_l() + [[(X(-0.12), Y(0.3)), (X(0.5), Y(0.3))]]


def body_sh():  # doble curva: onda
    pts = []
    for i in range(N * 2 + 1):
        t = i / (N * 2)
        pts.append((X(-0.15 + 1.3 * t), CY - H * 0.42 * cos(3 * pi * t)))
    return [pts]


def body_ch():  # SH con cruce
    # cruce corto sobre el tramo central (el trazo de E/O queda fuera del cuerpo)
    return body_sh() + [[(X(0.36), CY), (X(0.64), CY)]]


def body_vowel():  # vocal independiente: círculo
    r = H * 0.38
    return [arc(CX, CY, r, r, 0, 2 * pi, N * 2)]


BODIES = {"": body_vowel, "p": body_p, "b": body_b, "t": body_t, "d": body_d,
          "k": body_k, "g": body_g, "f": body_f, "s": body_s, "m": body_m,
          "n": body_n, "l": body_l, "r": body_r, "sh": body_sh, "ch": body_ch}


def extent(strokes):
    xs = [p[0] for s in strokes for p in s]; ys = [p[1] for s in strokes for p in s]
    return min(xs), min(ys), max(xs), max(ys)


def touches(strokes, pt, axis):
    """True si el trazo vocálico parte de un punto que ya pertenece al cuerpo."""
    for s in strokes:
        for x, y in s:
            if abs(x - pt[0]) < SW * 0.6 and abs(y - pt[1]) < SW * 0.6:
                return True
    return False


def vowel_stroke(strokes, v):
    x0, y0, x1, y1 = extent(strokes)
    if v == "a":
        start = (CX, y1)
        if not touches(strokes, start, 1): start = (CX, y1 + GAP)
        return [start, (CX, y1 + VLEN)]
    if v == "u":
        start = (CX, y0)
        if not touches(strokes, start, 1): start = (CX, y0 - GAP)
        return [start, (CX, y0 - VLEN)]
    if v == "e":
        start = (x0, CY)
        if not touches(strokes, start, 0): start = (x0 - GAP, CY)
        return [start, (x0 - VLEN * 0.8, CY)]
    if v == "o":
        start = (x1, CY)
        if not touches(strokes, start, 0): start = (x1 + GAP, CY)
        return [start, (x1 + VLEN * 0.8, CY)]


# ---- dígitos (Matemáticas 1.0) ----
def bars(n, x):
    step = 180
    return [[(x + i * step, Y(0)), (x + i * step, Y(1))] for i in range(n)], x + (n - 1) * step


def four(x):
    w = 300
    return [[(x, Y(1)), (x + w, Y(1)), (x + w, Y(0)), (x, Y(0))]], x + w


DOT_R = 88


def digit(d):
    strokes, dots = [], []
    x = 0
    if d == 0:
        r = H * 0.5
        return [arc(r, CY, r * 0.85, r, 0, 2 * pi, N * 2)], []
    if d >= 5:
        dots.append((DOT_R, CY)); x = DOT_R * 2 + 90
        d -= 5
    if 1 <= d <= 3:
        s, _ = bars(d, x); strokes += s
    elif d == 4:
        s, _ = four(x); strokes += s
    return strokes, dots


# ---- trazado y unión ----
def circle_path(pen, cx, cy, r, n=32):
    # sentido horario, igual que los rectángulos, para que la unión no deje huecos
    pts = [(cx + r * cos(-2 * pi * i / n), cy + r * sin(-2 * pi * i / n)) for i in range(n)]
    pen.moveTo(pts[0])
    for p in pts[1:]: pen.lineTo(p)
    pen.closePath()


def stroke_outline(strokes, dots=()):
    r = SW / 2
    path = pathops.Path()
    pen = path.getPen()
    for s in strokes:
        for (x1, y1), (x2, y2) in zip(s, s[1:]):
            dx, dy = x2 - x1, y2 - y1
            L = (dx * dx + dy * dy) ** 0.5
            if L < 1e-6: continue
            nx, ny = -dy / L * r, dx / L * r
            pen.moveTo((x1 + nx, y1 + ny)); pen.lineTo((x2 + nx, y2 + ny))
            pen.lineTo((x2 - nx, y2 - ny)); pen.lineTo((x1 - nx, y1 - ny)); pen.closePath()
        # remates y uniones redondas (sólo donde hay esquina o extremo)
        for i, (x, y) in enumerate(s):
            if i in (0, len(s) - 1) or len(s) < 12:
                circle_path(pen, x, y, r)
            else:
                (ax, ay), (bx, by) = s[i - 1], s[i + 1]
                # esquina si el ángulo cambia mucho
                v1 = (x - ax, y - ay); v2 = (bx - x, by - y)
                n1 = (v1[0]**2 + v1[1]**2) ** .5 or 1; n2 = (v2[0]**2 + v2[1]**2) ** .5 or 1
                if (v1[0]*v2[0] + v1[1]*v2[1]) / (n1 * n2) < 0.97:
                    circle_path(pen, x, y, r)
                else:
                    circle_path(pen, x, y, r, 32)
    for (x, y) in dots:
        circle_path(pen, x, y, DOT_R, 40)
    return pathops.simplify(path, fix_winding=True, clockwise=True)


def to_glyph(path, side=SIDE):
    b = path.bounds
    shift = side - b[0]
    pen = TTGlyphPen(None)
    for verb, pts in path.segments:
        pts = [(round(x + shift), round(y)) for x, y in pts]
        if verb == "moveTo": pen.moveTo(pts[0])
        elif verb == "lineTo": pen.lineTo(pts[0])
        elif verb == "qCurveTo": pen.qCurveTo(*pts)
        elif verb == "curveTo": pen.curveTo(*pts)
        elif verb == "closePath": pen.closePath()
        elif verb == "endPath": pen.endPath()
    return pen.glyph(), round(b[2] - b[0]) + 2 * side


def main():
    data = json.loads((ROOT / "owee-pua-map.json").read_text())
    outlines = {}
    for syl, cp in data["syllables"].items():
        cons, v = syl[:-1], syl[-1]
        strokes = BODIES[cons]()
        strokes = strokes + [vowel_stroke(strokes, v)]
        outlines[int(cp[2:], 16)] = stroke_outline(strokes)
    for d, x in data["digits"].items():
        strokes, dots = digit(int(d))
        outlines[int(x["codepoint"][2:], 16)] = stroke_outline(strokes, dots)

    order = [".notdef", "space"] + [f"uni{cp:04X}" for cp in sorted(outlines)]
    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    glyphs = {".notdef": TTGlyphPen(None).glyph(), "space": TTGlyphPen(None).glyph()}
    metrics = {".notdef": (SPACE, 0), "space": (SPACE, 0)}
    svgdir = ROOT / "svg-2.1"; svgdir.mkdir(exist_ok=True)
    for cp, path in sorted(outlines.items()):
        side = DIGIT_SIDE if cp >= 0xE040 else SIDE
        g, adv = to_glyph(path, side)
        name = f"uni{cp:04X}"
        glyphs[name] = g; metrics[name] = (adv, side)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=950, descent=-250, lineGap=0)
    cmap = {cp: f"uni{cp:04X}" for cp in outlines}
    cmap[0x20] = "space"; cmap[0xA0] = "space"
    fb.setupCharacterMap(cmap)
    fb.setupNameTable({
        "familyName": "Owee Sans 2", "styleName": "Regular",
        "uniqueFontIdentifier": "Owee Sans 2.1", "fullName": "Owee Sans 2 Regular",
        "psName": "OweeSans2-Regular", "version": "Version 2.1",
    })
    fb.setupOS2(version=4, sTypoAscender=950, sTypoDescender=-250, sTypoLineGap=0,
                usWinAscent=950, usWinDescent=250, sxHeight=TOP, sCapHeight=TOP,
                fsSelection=0x40 | 0x80, achVendID="OWEE")
    fb.setupPost(); fb.setupMaxp()
    out = ROOT / "OweeSans2-Regular.ttf"
    fb.save(out)

    # Exporta cada glifo como SVG para revisión.
    from fontTools.ttLib import TTFont
    f = TTFont(out); gs = f.getGlyphSet()
    names = {int(cp[2:], 16): s for s, cp in data["syllables"].items()}
    names.update({int(x["codepoint"][2:], 16): "digit_" + d for d, x in data["digits"].items()})
    for old in svgdir.glob("*.svg"): old.unlink()
    for cp in sorted(outlines):
        n = f"uni{cp:04X}"; p = SVGPathPen(gs); gs[n].draw(p)
        adv = f["hmtx"][n][0]
        (svgdir / f"{cp:04X}_{names[cp]}.svg").write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -950 {adv} 1200">'
            f'<path transform="scale(1,-1)" d="{p.getCommands()}"/></svg>\n')
    print("Creado:", out, "glifos:", len(outlines))


if __name__ == "__main__":
    main()
