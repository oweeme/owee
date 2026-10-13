#!/usr/bin/env python3
"""Genera copias de los .desktop instalados con los nombres genericos en Owee (romano y Owee Script).

Para cada programa de apps_escritorio.tsv que exista en /usr/share/applications escribe en SALIDA un .desktop
con las claves extra   GenericName[qow]  y  GenericName[qow@owee]   (romano y glifos).
El NOMBRE de la marca (GIMP, Firefox...) no se traduce: se conserva. NO modifica el sistema: tu eliges si instalar
las copias en ~/.local/share/applications (solo tu usuario) o empaquetarlas para oweelinux.

Uso: python3 generar_desktop.py [SALIDA]   (por defecto ./salida/applications)
"""
import pathlib, sys
aqui = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(aqui.parent / "herramientas"))
from owee_script import to_script

ORIGEN = pathlib.Path("/usr/share/applications")
salida = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else aqui / "salida/applications"
salida.mkdir(parents=True, exist_ok=True)
hechos, ausentes = [], []
for l in (aqui / "apps_escritorio.tsv").read_text(encoding="utf8").splitlines()[1:]:
    did, nombre, es, owee, *_ = l.split("\t") + [""]
    src = ORIGEN / did
    if not src.exists():
        ausentes.append(did); continue
    lineas = src.read_text(encoding="utf8", errors="replace").splitlines()
    out, dentro, puesto = [], False, False
    for ln in lineas:
        if ln.startswith("["):
            if dentro and not puesto:
                out += [f"GenericName[qow]={owee}", f"GenericName[qow@owee]={to_script(owee)}"]; puesto = True
            dentro = ln.strip() == "[Desktop Entry]"
        if dentro and (ln.startswith("GenericName[qow") ):
            continue
        out.append(ln)
    if dentro and not puesto:
        out += [f"GenericName[qow]={owee}", f"GenericName[qow@owee]={to_script(owee)}"]
    (salida / did).write_text("\n".join(out) + "\n", encoding="utf8")
    hechos.append(did)
print(f"{len(hechos)} .desktop generados en {salida}")
for h in hechos: print("  +", h)
if ausentes: print(f"{len(ausentes)} programas del glosario no estan instalados aqui:", ", ".join(ausentes))
