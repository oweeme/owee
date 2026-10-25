#!/usr/bin/env python3
"""Valida los bloques ```owee de un .md contra fonologia y lexico Owee 1.0.

Uso: python3 validar_owee.py ARCHIVO.md [...]
Comprueba por cada palabra: solo a/e/o/u + 14 consonantes, silaba V o CV,
sin consonante final, sin 'i'; y que cada raiz (separadas por '-') exista
en 02_Diccionario/datos/lexico.tsv. Cuenta silabas por verso.
"""
import re, sys, pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[3]
LEX = {l.split("\t")[0] for l in (RAIZ / "02_Diccionario/datos/lexico.tsv").read_text(encoding="utf8").splitlines()[1:]}
LEX |= {p for l in (RAIZ / "02_Diccionario/datos/lexico_ciencias.tsv").read_text(encoding="utf8").splitlines()[1:] for p in l.split("\t")[0].split("-")}
SIL = re.compile(r"(?:sh|ch|[pbtdkgfsmnlr])?[aeou]")

def silabas(p):
    s = SIL.findall(p)
    return s if "".join(s) == p else None

def main(paths):
    malos = 0
    for path in paths:
        bloque = False
        for n, linea in enumerate(pathlib.Path(path).read_text(encoding="utf8").splitlines(), 1):
            if linea.startswith("```"):
                bloque = linea.strip() == "```owee" if not bloque else False
                continue
            if not bloque or not linea.strip() or linea.lstrip().startswith('#'):
                continue
            total = 0
            for tok in re.findall(r"[A-Za-z-]+", linea):
                nombre = tok[0].isupper()   # nombre propio (Gramatica 1.1 §14): solo se comprueba la fonologia
                for raiz in tok.lower().split("-"):
                    if not raiz:
                        continue
                    s = silabas(raiz)
                    if s is None:
                        print(f"{path}:{n}: fonologia invalida: {raiz}"); malos += 1
                    else:
                        total += len(s)
                    # vocal larga opcional (aa ee oo uu): se valida la raiz con la vocal simple
                    if not nombre and raiz not in LEX and re.sub(r"([aeou])\1+", r"\1", raiz) not in LEX:
                        print(f"{path}:{n}: fuera del lexico: {raiz}"); malos += 1
            print(f"  l.{n:>3} [{total:>2} sil] {linea.strip()}") if "-v" in sys.argv else None
    print("OK: todo valido" if not malos else f"{malos} problema(s)")
    return 1 if malos else 0

if __name__ == "__main__":
    sys.exit(main([a for a in sys.argv[1:] if not a.startswith("-")]))
