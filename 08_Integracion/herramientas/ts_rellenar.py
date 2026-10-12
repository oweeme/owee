#!/usr/bin/env python3
"""Rellena un archivo Qt Linguist (.ts) con las traducciones al Owee del glosario (coincidencia exacta del texto fuente).

Las apps de Deepin/DDE (Qt/DTK) no usan gettext sino .ts/.qm. Con esto partes de la traduccion al Owee de cada app:
  python3 herramientas/ts_rellenar.py app_en.ts app_qow.ts [--script]
  lrelease app_qow.ts            # genera app_qow.qm
    --script   escribe Owee Script (glifos) en lugar de romano
Los textos no cubiertos quedan 'unfinished' y se listan al final, ordenados por frecuencia: es la lista de
vocabulario que falta por definir en el idioma (ui_glosario.tsv).
"""
import collections, pathlib, sys
import xml.etree.ElementTree as ET
aqui = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(aqui))
from owee_script import to_script

def main(entrada, salida, script):
    gl = {}
    for l in (aqui.parent / "datos/ui_glosario.tsv").read_text(encoding="utf8").splitlines()[1:]:
        en, es, owee, *_ = l.split("\t") + [""]
        gl[en.strip().rstrip(".…")] = to_script(owee) if script else owee
    arbol = ET.parse(entrada); raiz = arbol.getroot()
    raiz.set("language", "qow")
    hechas, faltan = 0, collections.Counter()
    for m in raiz.iter("message"):
        src = (m.findtext("source") or "").strip()
        clave = src.rstrip(".…").replace("&", "")          # los atajos de teclado (&Archivo) se ignoran al buscar
        tr = m.find("translation")
        if tr is None: tr = ET.SubElement(m, "translation")
        if clave in gl:
            tr.text = gl[clave]; tr.attrib.pop("type", None); hechas += 1
        else:
            faltan[src] += 1
    arbol.write(salida, encoding="utf-8", xml_declaration=True)
    print(f"{hechas} cadenas rellenadas; {sum(faltan.values())} sin traducir -> {salida}")
    for s, n in faltan.most_common(15): print(f"   falta ({n}x): {s}")

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 2: sys.exit(__doc__)
    main(a[0], a[1], "--script" in sys.argv)
