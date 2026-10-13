#!/usr/bin/env python3
"""Mide cuanto hay que traducir en tu sistema y que cadenas conviene traducir primero.

Lee los catalogos .mo de /usr/share/locale/es (los textos de interfaz que ya tienen traduccion al espanol), cuenta los
textos originales (msgid, en ingles) y los ordena por frecuencia entre programas. Compara con el glosario de Owee
(08_Integracion/datos/ui_glosario.tsv) y escribe prioridad_cadenas.tsv: la lista de lo que falta, por orden de uso.
Uso: python3 frecuencia_cadenas.py [N]     (N = filas de la lista, 400 por defecto)
"""
import collections, gettext, glob, os, pathlib, sys
aqui = pathlib.Path(__file__).resolve().parent
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
cobertura = {l.split("\t")[0].strip().lower() for l in (aqui.parent / "datos/ui_glosario.tsv").read_text(encoding="utf8").splitlines()[1:]}
por_cadena = collections.Counter(); dominios = 0; total = 0
for p in glob.glob("/usr/share/locale/es/LC_MESSAGES/*.mo"):
    try:
        t = gettext.GNUTranslations(open(p, "rb"))
    except Exception:
        continue
    dominios += 1
    for k in t._catalog:
        if isinstance(k, str) and k:
            total += 1
            limpio = k.replace("&", "").replace("_", "").strip().rstrip(".…:")
            if 1 < len(limpio) <= 40 and "%" not in limpio and "\n" not in limpio:
                por_cadena[limpio.lower()] += 1
unicas = len(por_cadena)
cortas = sum(por_cadena.values())
top = por_cadena.most_common(N)
cubiertas = sum(n for c, n in por_cadena.items() if c in cobertura)
cub_top = sum(n for c, n in top if c in cobertura)
with open(aqui / "prioridad_cadenas.tsv", "w", encoding="utf8") as f:
    f.write("texto_original\tprogramas\tcubierto_por_glosario\n")
    for c, n in top: f.write(f"{c}\t{n}\t{'si' if c in cobertura else ''}\n")
print(f"{dominios} programas/bibliotecas con traduccion; {total} cadenas en total")
print(f"cadenas cortas (<=40 letras) distintas: {unicas}; apariciones: {cortas}")
print(f"glosario actual ({len(cobertura)} textos) cubre {cubiertas} apariciones ({cubiertas*100//max(1,cortas)} %)")
print(f"las {N} cadenas mas repetidas suman {sum(n for _, n in top)} apariciones ({sum(n for _, n in top)*100//max(1,cortas)} % del total); el glosario cubre {cub_top} de ellas")
print("primeras sin cubrir:", ", ".join(c for c, n in top if c not in cobertura)[:300])
