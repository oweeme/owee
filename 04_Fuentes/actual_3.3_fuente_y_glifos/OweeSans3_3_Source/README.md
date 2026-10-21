# Owee Sans 3.3 Canonical

Mejora de Owee Sans 3.2 construida desde los vectores originales del
Curso Práctico para Adultos (pág. 4, "Sistema silábico").

- 56 sílabas CV: `extract_skeletons.py` saca de la tabla del curso las líneas
  centrales exactas de cada sílaba (consonante 3.07 pt, vocal 2.63 pt,
  cierre/cruce 2.30 pt) a `skeletons.json`. `build_font_33.py` las vuelve a
  trazar con grosor uniforme y remates redondos: la forma es la del curso,
  sin manchas ni recortes de calcar una imagen.
- Vocales aisladas A E O U: portador neutro (círculo) + extensión en su
  dirección, como en la Caligrafía Escolar 0.2 (el curso no las dibuja).
- Dígitos: Matemáticas 1.0 (0 círculo, 1-3 palos, 4 ⊐, 5 punto, 6-9 punto + 1..4),
  con los palos de cada dígito agrupados y más aire entre dígitos.
- Mismo PUA (U+E000..U+E03B, U+E040..U+E049): funciona con el IME Fcitx5 actual.
- Métricas verticales correctas (no se recorta ni invade la línea anterior).

## Consonantes rediseñadas (3.4)
`consonantes_v34.py` sustituye f, s, l, r, d y ch por siluetas que se distinguen
a primera vista (antes s/f, r/l, d/t y ch/sh sólo se diferenciaban por una barrita
que se pegaba a la vocal): f `/`, l `\`, s `/` cruzada por una barra, r `\` con un
punto, d arco cerrado por su base (t queda abierto), ch zigzag (sh sigue siendo onda).
El PUA y el romano no cambian.

## Dos estilos desde el mismo esqueleto
| Estilo | Fuente | Uso | Proporción |
|---|---|---|---|
| `sans`   | Owee Sans 3.3 Canonical | computadora, texto compacto | más baja y ancha, trazo grueso, poco espacio |
| `school` | Owee School 3.3 | escritura a mano / aprendizaje | más alta y estrecha, inclinada 13°, trazo fino |

La forma de cada glifo es idéntica en los dos: sólo cambian proporción,
inclinación, grosor y espaciado (tabla `STYLES` en `build_font_33.py`).

## Regenerar

    pdftocairo -svg -f 4 -l 4 ../Owee_1.0_Curso_Practico_Adultos.pdf curso_adultos_p4.svg
    python3 extract_skeletons.py
    D=../Owee_Script_2.0_Source/owee-script-2.0-source/.pydeps
    PYTHONPATH=$D python3 build_font_33.py sans
    PYTHONPATH=$D python3 build_font_33.py school
    cp OweeSans3_3-Canonical-Regular.ttf OweeSchool3_3-Regular.ttf ~/.local/share/fonts/Owee/ && fc-cache -f

Ajustes al principio de `build_font_33.py`: `STROKE`/`MIN_W` (grosor),
`S` (tamaño), `SIDE` (espacio entre sílabas), `DIGIT_SIDE`/`BAR_GAP` (dígitos).
