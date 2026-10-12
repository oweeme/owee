Owee Sans 3.2 Canonical

Corrección sobre 3.1:
La versión 3.1 recortó algunos trazos separados (especialmente extensiones
vocálicas superiores/inferiores) al extraer los símbolos del PDF.
3.2 reconstruye cada glifo usando la celda completa de la tabla educativa
'Las 60 sílabas básicas'.

- 56 CV reconstruidos desde el cuaderno educativo.
- PUA U+E000..U+E03B sin cambios.
- Dígitos U+E040..U+E049 conservados.
- Compatible con el IME Fcitx5 ya instalado.
- Métrica compacta para texto continuo.
- Familia: Owee Sans 3.2 Canonical

Instalación:
mkdir -p ~/.local/share/fonts
cp OweeSans3_2-Canonical-Regular.ttf ~/.local/share/fonts/
fc-cache -fv
