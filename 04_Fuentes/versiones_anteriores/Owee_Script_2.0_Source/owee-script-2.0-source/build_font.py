
from pathlib import Path
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.boundsPen import BoundsPen
import json, re

ROOT=Path(__file__).parent
data=json.loads((ROOT/"owee-pua-map.json").read_text())
entries={}
for s,cp in data["syllables"].items(): entries[int(cp[2:],16)] = s
for d,x in data["digits"].items(): entries[int(x["codepoint"][2:],16)] = "digit_"+d

units=1000
SIDE=80          # margen lateral a cada lado del glifo
BASE=900         # y_fuente = BASE - y_svg: la celda SVG 0..1000 queda en -100..900
SPACE=380        # ancho del espacio
SCALE=1.2        # ampliación de los glifos respecto al diseño SVG (centro 500,500)
HALF=41*SCALE    # mitad del grosor de trazo (stroke-width 82 en los SVG)

fb=FontBuilder(units, isTTF=True)
glyph_order=[".notdef","space"]+[f"uni{cp:04X}" for cp in sorted(entries)]
fb.setupGlyphOrder(glyph_order)

glyphs={}
metrics={}
pen=TTGlyphPen(None); glyphs[".notdef"]=pen.glyph(); metrics[".notdef"]=(SPACE,0)
pen=TTGlyphPen(None); glyphs["space"]=pen.glyph(); metrics["space"]=(SPACE,0)

for cp,name in sorted(entries.items()):
    svgfile=next((ROOT/"svg").glob(f"{cp:04X}_*.svg"))
    txt=svgfile.read_text()
    # Cada <line> se convierte en un rectángulo con remate cuadrado
    # (se alarga HALF por cada extremo) para que las esquinas queden cerradas.
    # Todos los rectángulos tienen la misma orientación, así que los solapes
    # se rellenan (regla nonzero) sin dejar huecos.
    raw=[]
    for m in re.finditer(r'x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"',txt):
        x1,y1,x2,y2=(500+(v-500)*SCALE for v in map(float,m.groups()))
        y1=BASE-y1; y2=BASE-y2
        dx=x2-x1; dy=y2-y1; L=(dx*dx+dy*dy)**0.5 or 1
        ux=dx/L*HALF; uy=dy/L*HALF
        x1-=ux; y1-=uy; x2+=ux; y2+=uy
        nx=-uy; ny=ux
        raw.append([(x1+nx,y1+ny),(x2+nx,y2+ny),(x2-nx,y2-ny),(x1-nx,y1-ny)])
    xmin=min(p[0] for r in raw for p in r); xmax=max(p[0] for r in raw for p in r)
    shift=SIDE-xmin   # el glifo empieza a SIDE unidades del origen
    pen=TTGlyphPen(None)
    for r in raw:
        pts=[(round(x+shift),round(y)) for x,y in r]
        pen.moveTo(pts[0])
        for p in pts[1:]: pen.lineTo(p)
        pen.closePath()
    g=f"uni{cp:04X}"; glyphs[g]=pen.glyph()
    metrics[g]=(round(xmax-xmin)+2*SIDE, SIDE)

fb.setupGlyf(glyphs)
fb.setupHorizontalMetrics(metrics)
fb.setupHorizontalHeader(ascent=950, descent=-200, lineGap=0)
cmap={cp:f"uni{cp:04X}" for cp in entries}
cmap[0x20]="space"; cmap[0xA0]="space"
fb.setupCharacterMap(cmap)
fb.setupNameTable({
 "familyName":"Owee Sans 2",
 "styleName":"Regular",
 "uniqueFontIdentifier":"Owee Sans 2.0",
 "fullName":"Owee Sans 2 Regular",
 "psName":"OweeSans2-Regular",
 "version":"Version 2.0",
})
fb.setupOS2(version=4,sTypoAscender=950,sTypoDescender=-200,sTypoLineGap=0,
            usWinAscent=950,usWinDescent=200,
            sxHeight=500,sCapHeight=700,fsSelection=0x40|0x80,
            achVendID="OWEE")
fb.setupPost()
fb.setupMaxp()
out=ROOT/"OweeSans2-Regular.ttf"
fb.save(out)
print("Creado:",out)
