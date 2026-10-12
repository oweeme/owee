#!/usr/bin/env python3
"""Analiza la prosodia de letras Owee para canciones: pulsos, acentos y compas sugerido.

Reglas (propuestas, ver Literatura 0.3 §8 y Gramatica 1.1 §6):
  - cada palabra de 2+ silabas lleva UN pulso fuerte en su primera silaba (acento inicial);
  - los monosilabos (me, tu, bo, ko, pe...) son atonos: anacrusa que se apoya en la palabra siguiente
    (si el verso solo tiene monosilabos, cada uno lleva pulso);
  - una palabra bisilaba = un pulso (dos corcheas); trisilaba = pulso + corchea extra.
Uso: python3 prosodia.py ARCHIVO.md [-s "titulo parcial"]   (lee los bloques ```owee)
"""
import re, sys, pathlib
SIL = re.compile(r"(?:sh|ch|[pbtdkgfsmnlr])?[aeou]")
COMPAS = {1: "1 pulso (cabe en un compás de 2/4 con silencio)", 2: "2/4", 3: "3/4 (vals) o 6/8", 4: "4/4"}

def analiza(linea):
    pal = re.findall(r"[a-z]+(?:-[a-z]+)*", linea.lower())
    pulsos, sil, ana, mapa = 0, 0, 0, []
    for p in pal:
        partes = p.split("-")
        ss = [s for q in partes for s in SIL.findall(q)]
        sil += len(ss)
        if len(ss) == 1:
            ana += 1; mapa.append(ss[0] + "·")           # atono
        else:
            # compuesto con guion: 1 acento principal (primer elemento) + 1 secundario por elemento posterior
            # que tenga 2+ silabas (Gramatica 1.1 §6). Un elemento monosilabo (operador) no lleva pulso.
            elems = [SIL.findall(q) for q in partes]
            marcas = []
            for i, e in enumerate(elems):
                if len(e) >= 2 or (i == 0 and len(e) >= 1):
                    pulsos += 1
                    marcas.append(("▲" if i == 0 else "△") + e[0].upper() + "".join(e[1:]))
                else:
                    marcas.append("".join(e))
            mapa.append("-".join(marcas))
    if pulsos == 0 and ana:                       # verso solo de monosilabos: todos llevan pulso
        pulsos, ana = ana, 0; mapa = ["▲" + m[:-1].upper() for m in mapa]
    return pulsos, sil, ana, " ".join(mapa)

def main(path, filtro=None):
    bloque, titulo = False, ""
    for linea in pathlib.Path(path).read_text(encoding="utf8").splitlines():
        if linea.startswith("###"): titulo = linea.lstrip("# ").strip()
        if linea.startswith("```"):
            bloque = linea.strip() == "```owee" if not bloque else False
            if bloque and (not filtro or filtro.lower() in titulo.lower()): print(f"\n== {titulo}")
            continue
        if bloque and linea.strip() and not linea.lstrip().startswith('#') and (not filtro or filtro.lower() in titulo.lower()):
            p, s, a, m = analiza(linea)
            print(f"  {p} pulso(s) {s:>2} sil  {COMPAS.get(p, str(p) + ' pulsos'):<28} {m}")

if __name__ == "__main__":
    a = sys.argv[1:]
    main(a[0], a[a.index("-s") + 1] if "-s" in a else None)
