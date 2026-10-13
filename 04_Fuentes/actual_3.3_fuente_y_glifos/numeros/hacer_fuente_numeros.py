#!/usr/bin/env python3
"""Genera 'Owee Numerals': una fuente que solo contiene las cifras 0-9 (U+0030..0039) dibujadas con los
glifos numericos de Owee Script (los mismos de U+E040..E049). Colocada antes de la fuente normal del sistema,
cualquier programa (calculadora, reloj, calendario, hojas de calculo) muestra sus cifras en Owee sin tocar el programa.
Requiere fontTools (pip install fonttools). Uso: python3 hacer_fuente_numeros.py [salida_dir]"""
import sys, pathlib
from fontTools.ttLib import TTFont
aqui = pathlib.Path(__file__).resolve().parent
origen = aqui.parent / "Owee_Glyph_Master_3.3/fonts/ttf/OweeSans-Regular.ttf"
salida = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else aqui
f = TTFont(origen)
cm = f.getBestCmap()
digitos = {0x30 + d: cm[0xE040 + d] for d in range(10)}
for t in f["cmap"].tables:
    if t.isUnicode():
        t.cmap = dict(digitos)
for rec in f["name"].names:
    s = rec.toUnicode()
    if rec.nameID in (1, 16): rec.string = "Owee Numerals"
    elif rec.nameID == 4: rec.string = "Owee Numerals Regular"
    elif rec.nameID == 6: rec.string = "OweeNumerals-Regular"
    elif rec.nameID == 3: rec.string = "OweeNumerals-Regular;digits"
    elif rec.nameID == 2 or rec.nameID == 17: rec.string = "Regular"
out = salida / "OweeNumerals-Regular.ttf"
f.save(out)
print("escrito", out, "con", len(digitos), "cifras")
