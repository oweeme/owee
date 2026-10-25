#!/usr/bin/env python3
"""Extrae lexico.tsv desde el PDF Diccionario Base 1.0 (pdftotext). lexico.tsv es la fuente
legible por programas; si el diccionario cambia, editar lexico.tsv a mano o regenerar con esto."""
import re, subprocess, pathlib
raiz = pathlib.Path(__file__).resolve().parents[2]
pdf = raiz / "02_Diccionario/versiones_anteriores/Owee_Diccionario_Base_1.0_Inventario_Completo.pdf"
txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
L = [re.sub(r"[-\x0c]", "", l).rstrip() for l in txt.splitlines()]
sec, rows, i = "", {}, 0
def add(w, sil, cls, mean, est, s): rows.setdefault(w, [w, sil, cls, mean, est, s])
while i < len(L):
    l = L[i]
    m = re.match(r"^(\d+)\. (.+)$", l)
    if m:
        if l.startswith("21."): break
        sec = m.group(2)
    m = re.match(r"^(\w+)\s+([a-z]+(?:-[a-z]+)*)\s*$", l)
    if m and not l.startswith("Owee"):
        j = i + 1
        while j < len(L) and not L[j].strip(): j += 1
        m2 = re.match(r"^\s*(.*?)\s{2,}(.*?)\s{2,}(ESTABLE|PROVISIONAL)\s*$", L[j])
        if m2:
            add(m.group(1), m.group(2), m2.group(1).strip(), m2.group(2).strip(), m2.group(3), sec); i = j
    m = re.match(r"^\s{2}([a-z]+-[a-z]+)\s{2,}(\S+ \+ \S+)\s{2,}(.+)$", l)
    if m: add(m.group(1), m.group(1), "derivado (" + m.group(2) + ")", m.group(3).strip(), "ESTABLE", "Derivaciones y formas compuestas")
    i += 1
for w, n in zip("cho be du ga fo sa ku mu na she".split(), range(10)): add(w, w, "dígito", str(n), "ESTABLE", "Sistema numérico")
for w, n in [("tanu", "10"), ("gabu", "100"), ("soku", "1 000"), ("benu", "1 000 000")]: add(w, w, "escala numérica", n, "ESTABLE", "Sistema numérico")
for w, n in [("dapa", "suma"), ("dopo", "resta"), ("kebu", "multiplicación"), ("faku", "división"), ("doto", "separador decimal")]: add(w, w, "operación matemática", n, "ESTABLE", "Sistema numérico")
# Primer Diccionario Conceptual 1.0 (PDF): sus compuestos ya forman parte del idioma
pdf2 = raiz / "02_Diccionario/versiones_anteriores/Owee_1.0_Primer_Diccionario_Conceptual.pdf"
txt2 = subprocess.run(["pdftotext", "-layout", str(pdf2), "-"], capture_output=True, text=True, check=True).stdout
for l in txt2.splitlines():
    l = re.sub(r"[\ue000-\uf8ff\x0c]", "", l).rstrip()
    m = re.match(r"^\s{1,6}([a-z]+(?:-[a-z]+)+)\s{2,}(.+?)\s{2,}([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ +/-]+)\s*$", l)
    if m: add(m.group(1), m.group(1), "derivado (" + m.group(3).lower() + ")", m.group(2).strip(), "ESTABLE", "Derivaciones (Primer Diccionario 1.0)")

# decisiones posteriores al PDF (se reaplican al regenerar)
OVERRIDES = {"faro": "fuerza (vigor)", "nado-bure": "acceso abierto (iniciar sesión)", "nado-kose": "acceso cerrado (cerrar sesión)", "suna-duma": "flujo de agua (río)",
             "dune-fada": "enojo sentido (estado interno)"}   # fada ya es «enojo»: evita dos formas con el mismo significado   # 2026-10-12: la energia es `enu`; faro-enu = fuerza energetica
for w, m in OVERRIDES.items():
    if w in rows: rows[w][3] = m
out = raiz / "02_Diccionario/datos/lexico.tsv"
out.write_text("owee\tsilabas\tclase\tsignificado\testado\tseccion\n" + "".join("\t".join(r) + "\n" for r in rows.values()), encoding="utf8")
print(len(rows), "entradas ->", out)
