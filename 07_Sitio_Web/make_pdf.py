#!/usr/bin/env python3
"""Genera los PDF imprimibles (Literatura y Quimica) con Chrome headless, usando las fuentes Owee del sitio."""
import subprocess, shutil
from pathlib import Path
here = Path(__file__).resolve().parent
M = here.parent / "03_Material_Ensenanza"
JOBS = [("literatura-imprimir.html", sorted((M / "Literatura_Poesia").glob("Owee_Literatura_y_Poesia_*.md"))[-1].with_suffix(".pdf")),
        ("quimica-imprimir.html", M / "Quimica/Owee_Quimica_0.1_Borrador.pdf"),
        ("pronunciacion-imprimir.html", M / "Pronunciacion/Owee_Pronunciacion_1.0.pdf")]
chrome = shutil.which("google-chrome") or shutil.which("chromium")
for src, dst in JOBS:
    subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={dst}", (here / "docs" / src).as_uri()], check=True, capture_output=True)
    shutil.copy2(dst, here / "docs/documentos" / dst.name)
    print("PDF:", dst.name, dst.stat().st_size // 1024, "KB")
