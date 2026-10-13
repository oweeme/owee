#!/usr/bin/env python3
"""Genera lexico_ciencias.tsv desde ciencias_fuente.py (lo consumen el validador y el sitio web)."""
import pathlib, re, sys
aqui = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(aqui))
from ciencias_fuente import RAICES, COMPUESTOS
SIL = re.compile(r"(?:sh|ch|[pbtdkgfsmnlr])?[aeou]")
def sil(w): s = SIL.findall(w); return "-".join(s) if "".join(s) == w else ""
REVISAR = {}   # formas invalidas pendientes (ya no hay: ango/akso se sustituyeron por compuestos)
NOTAS = {"tora-telo": "sustituye a «ango» (fonología inválida)", "loka-mede": "sustituye a «akso» (fonología inválida)"}
filas = []
APROBADAS = {l.strip() for l in (aqui / "aprobadas.txt").read_text(encoding="utf8").splitlines() if l.strip() and not l.startswith("#")}
base = {l.split("\t")[0]: l.split("\t")[3] for l in (aqui / "lexico.tsv").read_text(encoding="utf8").splitlines()[1:]}
raices = {r[0] for r in RAICES} | set(base)
EXCEPCION_LARGO = {"pa-lo-se", "po-lo-se"}
def norm(m): return re.sub(r"\s*\(.*?\)", "", m).strip().lower()

for w, c, d, s in RAICES:
    est = "AUDITADO 2.0" if d in ("Matemáticas", "Física") else ("APROBADA" if w in APROBADAS else "VERIFICADA")
    filas.append([w, sil(w), "raíz técnica", c, est, s, d, "raíz nueva (mezcla recortada de bo-sa + m-ado)" if w == "bomo" else ""])
for item in COMPUESTOS:
    f, m, d = item[:3]; sec = item[3] if len(item) > 3 else "Construcciones"
    filas.append([f, f, "construcción", m, "", sec, d, ""])

# --- verificacion automatica de las construcciones
significados = {}
for w, m in base.items(): significados.setdefault(norm(m), []).append(w)
for r in filas: significados.setdefault(norm(r[3]), []).append(r[0])
formas = [r[0] for r in filas]
for r in filas:
    if r[2] != "construcción": continue
    f, d = r[0], r[6]
    problemas = []
    partes = f.split("-")
    if len(partes) > 3 and f not in EXCEPCION_LARGO: problemas.append("más de 3 elementos")
    if len(re.findall(r"(?:sh|ch|[pbtdkgfsmnlr])?[aeou]", f.replace("-", ""))) > 6 and d not in ("Matemáticas", "Física"): problemas.append("más de 6 sílabas (poco práctico)")
    for p in partes:
        if p not in raices and not sil(p): problemas.append(f"'{p}' no existe ni es fonología válida")
    if formas.count(f) > 1 or f in base: problemas.append("forma repetida")
    otros = [x for x in significados.get(norm(r[3]), []) if x != f]
    if otros and f not in ("kuna-salo",): problemas.append("mismo significado que " + ", ".join(otros))
    if d in ("Matemáticas", "Física") and f not in NOTAS:
        r[4] = "AUDITADO 2.0"
    elif problemas:
        r[4] = "REVISAR"; r[7] = "; ".join(problemas)
    elif f in APROBADAS:
        r[4] = "APROBADA"
    else:
        r[4] = "VERIFICADA"
    if f in NOTAS and r[4] != "REVISAR":
        r[7] = NOTAS[f]
(aqui / "lexico_ciencias.tsv").write_text("owee\tsilabas\tclase\tsignificado\testado\tseccion\tdominio\tnota\n" + "".join("\t".join(r) + "\n" for r in filas), encoding="utf8")
from collections import Counter
print(len(filas), "filas ->", aqui / "lexico_ciencias.tsv")
print("estados:", dict(Counter(r[4] for r in filas)))
for r in filas:
    if r[4] == "REVISAR": print("  REVISAR", r[0], "-", r[7])
