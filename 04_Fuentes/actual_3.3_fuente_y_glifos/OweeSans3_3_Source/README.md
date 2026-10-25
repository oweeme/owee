# Owee Sans 3.4 (glifos nuevos)

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

## Glifos 3.4 (activos, escritura en línea)
La vocal va a la derecha de la consonante, en el mismo renglón (`OWEE_V4_LAYOUT=linear`, por defecto).

Desde la 3.4 los glifos salen de `glifos_v4.py`, un sistema geométrico por familias:
recto en `sans` y con las esquinas redondeadas en `school`. Ver `GUIA_DE_ESTILO_v4.md`
(qué define a cada glifo y qué puede variar) y `VOCALES_v4.md` (origen de las vocales).
Los esqueletos de `skeletons.json` ya no se usan para el dibujo; sólo quedan para la 3.3.

    python3 build_font_33.py sans          # o school
    OWEE_GLIFOS=v33 python3 build_font_33.py sans   # regenera los glifos de 3.3 (archivo .v33.ttf)
    OWEE_V4_LAYOUT=around python3 build_font_33.py sans   # disposición anterior, vocal alrededor
    python3 auditar_glifos_v4.py           # comprueba que ningún glifo sea giro de otro

El PUA y el romano no cambian: U+E000..U+E03B sílabas, U+E03C nexo `‿`,
U+E03D marca de nombre `ᚠ`, U+E040..U+E049 dígitos.
