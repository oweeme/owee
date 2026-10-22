#!/usr/bin/env python3
"""Construye el logo de Owee: el koi del autor (owee-koi-original.png) con «ouee» escrito en Owee Script encima de la cabeza.

    python3 construir_logo.py            # SVG + PNG (1024, 512, 256, 128, 64, 32) + icono para el sitio

Los glifos salen del contorno real de la fuente Owee Sans (se dibujan como trazados, así el SVG no necesita la fuente).
Requiere: fontTools, Pillow y un Chromium (Playwright) para rasterizar el SVG."""
import base64, pathlib, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
aqui = pathlib.Path(__file__).resolve().parent
RAIZ = aqui.parent
FUENTE = RAIZ / "04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3/fonts/ttf/OweeSans-Regular.ttf"
PALABRA = [0xE002, 0xE003, 0xE001, 0xE001]          # o u e e  (ouee)
CREMA = "#FDEBAB"                                    # el color del cuerpo del koi
# zona libre encima de la cabeza (lienzo 945 x 945): el texto se centra en CX, CY con ancho ANCHO
CX, CY, ANCHO = 270, 400, 300

def trazado():
    f = TTFont(FUENTE); cmap = f.getBestCmap(); gs = f.getGlyphSet(); upm = f["head"].unitsPerEm
    asc, desc = f["hhea"].ascent, f["hhea"].descent
    ancho_total = sum(gs[cmap[c]].width for c in PALABRA)
    esc = ANCHO / ancho_total
    alto = (asc - desc) * esc
    x = CX - ANCHO / 2; base = CY + alto / 2 + desc * esc
    d = []
    for c in PALABRA:
        g = gs[cmap[c]]; pen = SVGPathPen(gs)
        g.draw(TransformPen(pen, (esc, 0, 0, -esc, x, base)))
        d.append(pen.getCommands()); x += g.width * esc
    return " ".join(d), esc

def svg(con_koi=True, texto=True, ruta_png="owee-koi-original.png"):
    b64 = base64.b64encode((aqui / ruta_png).read_bytes()).decode()
    d, _ = trazado()
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 945 945" width="945" height="945" role="img" aria-label="Logo de Owee: un koi y la palabra ouee en Owee Script">'
            f'<title>Owee</title>' + (f'<image width="945" height="945" href="data:image/png;base64,{b64}"/>' if con_koi else '')
            + (f'<path d="{d}" fill="{CREMA}"/>' if texto else '') + '</svg>')

def main():
    (aqui / "owee-logo.svg").write_text(svg(), encoding="utf8")
    (aqui / "owee-logo-solo-koi.svg").write_text(svg(texto=False), encoding="utf8")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        try: b = p.chromium.launch()
        except Exception: b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        for n in (1024, 512, 256, 128, 64, 32):
            pg = b.new_page(viewport={"width": n, "height": n})
            pg.set_content('<body style="margin:0;background:transparent">' + svg().replace('width="945" height="945" role', f'width="{n}" height="{n}" role', 1), wait_until="load")
            pg.screenshot(path=str(aqui / f"owee-logo-{n}.png"), omit_background=True); pg.close()
        b.close()
    print("logo listo en", aqui)

if __name__ == "__main__":
    main()
