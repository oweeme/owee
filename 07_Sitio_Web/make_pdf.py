#!/usr/bin/env python3
"""Genera los PDF imprimibles con Chrome headless, usando las fuentes Owee del sitio: Literatura, Quimica, Pronunciacion
y los documentos de build_site.DOCUMENTOS (especificacion, escritura, diccionario, curso, cuadernos, matematicas, fisica),
que build_site.py anota en docs/imprimir.json. Despues vuelve a ejecutar build_site.py para que Descargas liste los PDF nuevos."""
import json, os, subprocess, shutil, tempfile
from pathlib import Path
here = Path(__file__).resolve().parent
ROOT = here.parent
M = ROOT / "03_Material_Ensenanza"
JOBS = [("literatura-imprimir.html", sorted((M / "Literatura_Poesia").glob("Owee_Literatura_y_Poesia_*.md"))[-1].with_suffix(".pdf")),
        ("quimica-imprimir.html", M / "Quimica/Owee_Quimica_0.1_Borrador.pdf"),
        ("pronunciacion-imprimir.html", M / "Pronunciacion/Owee_Pronunciacion_1.0.pdf")]
lista = here / "docs/imprimir.json"
if lista.exists():
    JOBS += [(html, ROOT / pdf) for html, pdf in json.loads(lista.read_text(encoding="utf8"))]
chrome = shutil.which("google-chrome") or shutil.which("chromium")

def fontconfig_sin_cifras_owee():
    """Si el equipo tiene las cifras Owee en todo el sistema (owee-numerals), Chrome pondria cifras Owee tambien en el texto en
    espanol de los PDF. Para imprimir se usa una copia de la configuracion de fontconfig sin ese archivo (el sistema no cambia)."""
    base = Path("/etc/fonts/fonts.conf")
    if not base.exists(): return {}
    tmp = Path(tempfile.mkdtemp(prefix="owee-fc-")); cd = tmp / "conf.d"; cd.mkdir()
    for f in sorted(Path("/etc/fonts/conf.d").glob("*.conf")):
        if "owee-numerals" not in f.name and f.name != "50-user.conf": (cd / f.name).symlink_to(f.resolve())
    (tmp / "fonts.conf").write_text(base.read_text().replace("<include ignore_missing=\"yes\">conf.d</include>", f"<include ignore_missing=\"yes\">{cd}</include>"))
    return {"FONTCONFIG_FILE": str(tmp / "fonts.conf")}

ENV = dict(os.environ, **fontconfig_sin_cifras_owee())
(here / "docs/documentos").mkdir(exist_ok=True)
for src, dst in JOBS:
    subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                    f"--print-to-pdf={dst}", (here / "docs" / src).as_uri()], check=True, capture_output=True, env=ENV)
    shutil.copy2(dst, here / "docs/documentos" / dst.name)
    print("PDF:", dst.relative_to(ROOT), dst.stat().st_size // 1024, "KB")
