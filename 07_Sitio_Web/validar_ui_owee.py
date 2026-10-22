#!/usr/bin/env python3
"""Valida ui_owee.tsv: cada texto Owee usa solo palabras que existen en el léxico (forma completa o raíz con -pa/-po),
sin consonantes finales ni `i`, y cada texto en español no se repite con dos traducciones distintas.

    python3 validar_ui_owee.py"""
import pathlib, re, sys
aqui = pathlib.Path(__file__).resolve().parent
RAIZ = aqui.parent
LEX = {l.split("\t")[0] for f in ("lexico.tsv", "lexico_ciencias.tsv") for l in (RAIZ / "02_Diccionario/datos" / f).read_text(encoding="utf8").splitlines()[1:]}
SIL = re.compile(r"(?:sh|ch|[pbtdkgfsmnlr])?[aeou]")

def cargar():
    d = {}
    for n, l in enumerate((aqui / "ui_owee.tsv").read_text(encoding="utf8").splitlines(), 1):
        if not l.strip() or l.startswith("#"): continue
        es, ow = l.split("\t")
        yield n, es, ow

def valido(tok):
    if tok in LEX: return True
    m = re.fullmatch(r"([a-z]+(?:-[a-z]+)*?)((?:-pa|-po)+)", tok)
    return bool(m and m.group(1) in LEX)

def main():
    malos, vistos = [], {}
    for n, es, ow in cargar():
        if es in vistos and vistos[es] != ow: malos.append(f"línea {n}: «{es}» tiene dos traducciones")
        vistos[es] = ow
        for tok in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", ow):
            if tok[0].isupper():          # nombre propio (Ouee): basta con que su fonología sea válida
                if "".join(SIL.findall(tok.lower().replace("-", ""))) != tok.lower().replace("-", ""): malos.append(f"línea {n}: nombre «{tok}» con fonología inválida")
                continue
            if not valido(tok): malos.append(f"línea {n}: «{tok}» no es una palabra del léxico ({ow})")
    for m in malos: print(m)
    print(f"{len(vistos)} textos de interfaz; {len(malos)} problemas")
    return 1 if malos else 0

if __name__ == "__main__":
    sys.exit(main())
