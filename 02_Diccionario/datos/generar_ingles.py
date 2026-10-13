#!/usr/bin/env python3
"""Genera ingles.tsv (forma -> glosa en ingles) a partir del significado en espanol y diccionario_es_en.tsv.
El ingles se obtiene por PIVOTE: el significado en espanol de cada forma se traduce con un diccionario espanol->ingles
(una entrada por cada significado distinto). Asi 'Owee -> ingles' pasa por el espanol y se mantiene coherente.
Si falta un significado, lo lista (hay que anadirlo a diccionario_es_en.tsv). Salida: ingles.tsv"""
import pathlib, re, sys
aqui = pathlib.Path(__file__).resolve().parent
d = {}
for l in (aqui / "diccionario_es_en.tsv").read_text(encoding="utf8").splitlines()[1:]:
    k, v = l.split("\t"); d[k] = v
filas = [l.split("\t") for l in (aqui / "lexico.tsv").read_text(encoding="utf8").splitlines()[1:]]
filas += [l.split("\t") for l in (aqui / "lexico_ciencias.tsv").read_text(encoding="utf8").splitlines()[1:]]
out, faltan = {}, set()
for r in filas:
    w, m = r[0], r[3]
    base = re.sub(r"\s*\(.*?\)", "", m)
    partes = []
    for v in re.split(r"\s+/\s+", base):
        v = re.sub(r"/a\b", "", v.strip().lower())
        if v in d:
            if d[v] not in partes: partes.append(d[v])
        else:
            faltan.add(v)
    out[w] = " / ".join(partes)
(aqui / "ingles.tsv").write_text("forma\tingles\n" + "".join(f"{w}\t{e}\n" for w, e in out.items()), encoding="utf8")
print(len(out), "formas con ingles; significados sin traducir:", len(faltan))
for f in sorted(faltan): print("  falta:", f)
sys.exit(1 if faltan else 0)
