# Owee Script 1.0 — Glyph Master

Fuente de verdad vectorial para las 60 unidades fonológicas de Owee.

## Reglas congeladas
- 4 vocales: A E O U. No existe I.
- 56 sílabas CV + 4 vocales = 60 glifos.
- Dirección vocálica: A arriba, E izquierda, O derecha, U abajo.
- Un glifo representa exactamente una sílaba.
- IDs `OWEE_SYL_*` son estables.
- PUA v1: U+E000..U+E03B.
- Los SVG usan un em conceptual de 1000 unidades.

## Archivos
- `svg/`: 60 glifos maestros.
- `owee-pua-map.json`: mapa machine-readable para parser/IME/web.
- `MAPA_PUA.md`: referencia humana.

## Importante
El PUA es una codificación privada de Owee 1.0. Los IDs silábicos deben mantenerse aunque en el futuro cambie la codificación pública.
