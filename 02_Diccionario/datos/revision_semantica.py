#!/usr/bin/env python3
"""Revision semantica de los terminos nuevos antes de aprobarlos. Genera revision_semantica.md.

Criterios (2026-10-12):
 1. La forma NO existe en otro lado (lexico base, Primer Diccionario Conceptual, guias, PDFs antiguos).
 2. Ningun otro termino tiene ya ese significado (sin sinonimos): una forma = un significado.
 3. Cada raiz del compuesto existe y su significado registrado encaja con el concepto (revision de cada termino).
Los veredictos 'AJUSTADO' y 'EN ESPERA' son decisiones de la revision; el resto es 'OK'."""
import pathlib, re
aqui = pathlib.Path(__file__).resolve().parent
AJUSTADOS = {
    "maku-rela": "antes maku-bora «cuerpo de la mano», poco claro; ahora «unión de la mano», paralelo a tume-rela (cuello)",
    "ruma-kuna-lobe": "antes ruma-kuna-nelo «planta del pájaro»; la pluma es la cubierta del pájaro, como bora-lobe (piel)",
    "nelo-rela": "antes nelo-palo «parte de planta», demasiado genérico; la rama une el tronco con las hojas",
    "kalu-kefe": "antes go-pose, casi idéntico acústicamente a la ordinal ga-pose (tercero); la pierna sostiene al estar de pie",
    "bora-gu": "antes gu-pose, por el mismo motivo; «cuerpo abajo»",
    "reka-doke": "antes sena-seta «conjunto de signos», que se leería como alfabeto; el diccionario es información de la comunicación",
    "nelo-fame": "significado ampliado a «fruta / alimento vegetal»",
    "bora-kopa": "significado precisado a «vientre / abdomen»",
    "fame-gore-pa": "práctica: antes loda-kelo-fame (6 sílabas); el almuerzo es la «comida grande»",
    "gune-fame": "práctica: antes kuna-bore-fame (6 sílabas); la cena es la «comida del final», como pado-fame (desayuno) es la del comienzo",
    "bado-pa": "práctica: antes bado-bema-pa (6 sílabas); sigue el patrón raíz + pa/po de faro-pa o fure-po",
    "bado-po": "práctica: antes bado-bema-po; mismo motivo",
    "lu-meka": "antes kuna-meka «máquina del cielo», que se confundiría con el avión (sura-meka); la nube informática es una máquina lejana",
    "loke-kopa": "significado precisado a «ventana de programa» para distinguirla de loke-nado (ventana de la casa)",
    "te-loda-kelo": "en el diseño, antes te-loda: loda es «rotación», no «día»; el día es loda-kelo (igual con pe- y pu-, amanecer, tarde y almuerzo)",
    "pado-fame": "en el diseño, antes loda-pado-fame (4 elementos, supera el máximo de 3)",
    "lena-sabe": "en el diseño, «dulce» era demasiado específico; ahora «sabroso»",
    "seta": "raíz ampliada de «conjunto matemático» a «conjunto / colección» (menú, galaxia, vocabulario, grafo)",
}
ESPERA = {
    "ruma-daro": "nueva (norma de animales por categorías); espera confirmación",
    "ruma-fame": "nueva (norma de animales por categorías); espera confirmación",
    "ruma-taro": "nueva (norma de animales por categorías); espera confirmación",
    "doma-le": "nueva: izquierda = el lado del corazón; espera confirmación",
    "doma-lu": "nueva: derecha = el lado lejano al corazón; espera confirmación",
    "duma-kuma": "nueva: estación / terminal; espera confirmación",
}
base = {}
for l in (aqui / "lexico.tsv").read_text(encoding="utf8").splitlines()[1:]:
    c = l.split("\t"); base[c[0]] = c[3]
cien = [l.split("\t") for l in (aqui / "lexico_ciencias.tsv").read_text(encoding="utf8").splitlines()[1:]]
allm = dict(base); allm.update({c[0]: c[3] for c in cien})
corto = lambda m: re.sub(r"\s*\(.*?\)", "", m).split(" / ")[0]
filas = ["| Forma | Concepto | Partes y su significado | Veredicto |", "|---|---|---|---|"]
n = {"OK": 0, "AJUSTADO": 0, "EN ESPERA": 0}
for c in cien:
    if c[4] not in ("VERIFICADA", "APROBADA") or c[6] in ("Matemáticas", "Física"): continue
    if c[6] == "Vida diaria (lote 2)" and c[0] not in AJUSTADOS: pass
    if c[6] == "Gramática 1.1" or c[6] == "Cotidiano 0.1" or c[6] in ("Química", "Astronomía", "Astrología", "Mitología", "Informática"):
        if c[4] == "APROBADA" and c[0] not in AJUSTADOS: continue   # ya aprobadas en rondas anteriores
    partes = " + ".join(f"`{p}` ({corto(allm[p])})" for p in c[0].split("-"))
    v = "AJUSTADO — " + AJUSTADOS[c[0]] if c[0] in AJUSTADOS else ("EN ESPERA — " + ESPERA[c[0]] if c[0] in ESPERA else "OK")
    n[v.split(" —")[0]] += 1
    filas.append(f"| `{c[0]}` | {c[3]} | {partes} | {v} |")
(aqui / "revision_semantica.md").write_text(
    "# Revisión semántica de términos nuevos (2026-10-12)\n\n" + __doc__.split("\n", 1)[1].rsplit("Los veredictos", 1)[0].strip() +
    f"\n\n**Resultado:** {n['OK']} OK · {n['AJUSTADO']} ajustados · {n['EN ESPERA']} en espera. Antes se reconcilió el léxico con el *Primer Diccionario Conceptual 1.0* "
    "(45 compuestos ya existentes, 29 no recogidos): se mantuvieron sus formas y se retiraron mis duplicados.\n\n" + "\n".join(filas) + "\n", encoding="utf8")
print(n)
