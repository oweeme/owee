"""Consonantes rediseñadas de Owee 3.4: f, s, l, r, d, ch.

En 3.3 estas se distinguían de su pareja sólo por una barrita corta casi
horizontal (s/f, r/l, d/t, ch/sh) que se pegaba al trazo de la vocal, y f/l eran
casi la misma curva. Ahora cada una tiene una silueta propia:

    f  /  diagonal curva           l  \\  la diagonal opuesta
    s  X  f cruzada por una barra  r  \\  l con un punto arriba a la derecha
    t  ∩  arco abierto             d  D  el mismo arco cerrado por su base
    sh ∿  onda                     ch Z  zigzag

Ningún rasgo distintivo va en la horizontal ni en la vertical del centro, donde
caen los trazos de las vocales a/e/o/u. sh y las demás consonantes no cambian.

Coordenadas de la tabla del curso (y hacia arriba, centro de la celda = 0,0).
Cada consonante es una lista de (ancho_pt, [segmentos]); el trazo de la vocal se
conserva de skeletons.json (siempre es el último trazo de cada sílaba).
"""
CW = 3.070866     # grosor de consonante en la tabla
DOT_W = 4.2       # un punto es un trazo de largo cero: su grosor es su diámetro


def L(a, b): return ["L", list(a), list(b)]
def C(a, b, c, d): return ["C", list(a), list(b), list(c), list(d)]


def mirror(seg, cx=3.3):
    return [seg[0]] + [[2 * cx - p[0], p[1]] for p in seg[1:]]


_DIAG = C((-0.7, -4.4), (1.8, 0.0), (4.8, 0.0), (7.5, 4.4))
_ARCH = C((-1.3, -0.1), (1.1, 5.0), (5.5, 5.0), (7.9, -0.1))

NUEVAS = {
    "f":  [(CW, [_DIAG])],
    "s":  [(CW, [_DIAG]), (CW, [L((0.6, 3.0), (6.0, -3.0))])],
    "l":  [(CW, [mirror(_DIAG)])],
    "r":  [(CW, [mirror(_DIAG)]), (DOT_W, [L((6.4, 3.4), (6.4, 3.4))])],
    "d":  [(CW, [_ARCH, L((7.9, -0.1), (-1.3, -0.1))])],
    "ch": [(CW, [L((-0.6, 3.4), (6.6, 3.4)), L((6.6, 3.4), (0.0, -3.4)),
                 L((0.0, -3.4), (7.2, -3.4))])],
}


def aplicar(sk):
    """Sustituye en `sk` (skeletons.json cargado) la parte de consonante de cada sílaba."""
    for c, partes in NUEVAS.items():
        for v in "aeou":
            vocal = sk[c + v][-1]
            sk[c + v] = [{"width": w, "segments": segs} for w, segs in partes] + [vocal]
    return sk
