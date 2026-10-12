# Owee Script 2.0 — fuente de glifos

Rediseño de alta legibilidad:
- trazos gruesos y uniformes;
- formas geométricas grandes dentro de la celda;
- estética tecnológica de bloque, inspirada en la disciplina visual de escrituras de Asia oriental, sin copiar caracteres japoneses o coreanos;
- conserva las 60 sílabas y sus PUA U+E000..U+E03B;
- añade dígitos Owee en U+E040..U+E049.

## Crear la fuente localmente
Instala FontTools y ejecuta:

    python3 -m pip install --user fonttools
    python3 build_font.py

Esto genera `OweeSans2-Regular.ttf` en esta carpeta.

## Instalar para tu usuario
    mkdir -p ~/.local/share/fonts
    cp OweeSans2-Regular.ttf ~/.local/share/fonts/
    fc-cache -fv

## Correcciones locales (27-09-2026)
- Las marcas de vocal A y U estaban invertidas en los SVG (A apuntaba abajo, U arriba).
  Se intercambiaron en las 30 sílabas afectadas para cumplir A↑ E← O→ U↓.
  Originales en `svg.orig/` y `build_font.py.orig`.
- `build_font.py`: glifos con márgenes laterales reales (antes quedaban pegados a la
  izquierda de una celda de 1000), ampliación `SCALE=1.2`, remates cuadrados,
  glifo de espacio propio y métricas verticales completas.

## Compilar en Deepin 25 (sin pip)
FontTools está descargado en `.pydeps/`:

    PYTHONPATH=.pydeps python3 build_font.py
    cp OweeSans2-Regular.ttf ~/.local/share/fonts/Owee/
    fc-cache -f

## Owee Sans 2.1 — glifos según la documentación (27-09-2026)
`build_font_21.py` sustituye al dibujo de bloques. Sigue:
- Especificación Normativa §10: familias P/B lateral curva, T/D arco superior,
  K/G ángulo, F/S diagonal curva, M/N curva inferior, L/R curva ascendente,
  SH/CH doble curva; la segunda consonante = cierre o cruce.
- Caligrafía Escolar 0.2: vocal = trazo recto (A arriba, E izquierda,
  O derecha, U abajo); vocal sola = círculo + trazo.
- Matemáticas 1.0: dígitos 0 = círculo, 1-3 = palos, 4 = ⊐, 5 = punto, 6-9 = punto + 1..4.

Mismo nombre de familia ("Owee Sans 2") y mismos code points, así que el IME
y los documentos existentes siguen funcionando. Los SVG generados quedan en
`svg-2.1/`; la fuente de bloques anterior en `OweeSans2-Block-backup.ttf`.

    PYTHONPATH=.pydeps python3 build_font_21.py
    cp OweeSans2-Regular.ttf ~/.local/share/fonts/Owee/ && fc-cache -f

Parámetros de ajuste al inicio del script: SW (grosor), BOT/TOP (altura del
cuerpo), VLEN (largo del trazo vocálico), SIDE (espaciado).
