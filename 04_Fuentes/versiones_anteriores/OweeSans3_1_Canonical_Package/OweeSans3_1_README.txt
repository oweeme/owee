Owee Sans 3.1 Canonical

Esta versión corrige el problema de Owee Sans 3:
- Los 56 glifos CV se reconstruyen directamente desde la página
  'Las 60 sílabas básicas' del cuaderno educativo Owee 1.0.
- Mantiene U+E000..U+E03B.
- Mantiene los números U+E040..U+E049.
- Mantiene compatibilidad con el IME existente.
- Reduce el ancho para texto continuo.
- Las vocales aisladas A/E/O/U conservan temporalmente el portador anterior,
  porque la tabla educativa define su regla pero no dibuja sus cuatro glifos finales.

Instalación:
mkdir -p ~/.local/share/fonts
cp OweeSans3_1-Canonical-Regular.ttf ~/.local/share/fonts/
fc-cache -fv

La familia aparecerá como: Owee Sans 3.1 Canonical
