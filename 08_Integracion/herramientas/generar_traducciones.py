#!/usr/bin/env python3
"""Genera, desde datos/ui_glosario.tsv, los archivos de traduccion para oweelinux y la web:

  linux/qow.po          catalogo gettext en Owee romano (msgid en ingles)
  linux/qow@owee.po     el mismo catalogo en Owee Script (para que las apps muestren los glifos con la fuente Owee)
  web/qow.json          {en: {es, owee, script}}
  web/qow.js            lo mismo, listo para <script> (sin fetch)
Tambien comprueba que cada termino exista en el lexico y avisa de su estado.
Uso: python3 herramientas/generar_traducciones.py
"""
import json, pathlib, sys, datetime
aqui = pathlib.Path(__file__).resolve().parent
raiz = aqui.parent
sys.path.insert(0, str(aqui))
from owee_script import to_script, valida

lex = {}
for f in ("lexico.tsv", "lexico_ciencias.tsv"):
    for l in (raiz.parent / "02_Diccionario/datos" / f).read_text(encoding="utf8").splitlines()[1:]:
        c = l.split("\t"); lex[c[0]] = c[4]

filas, avisos = [], []
for l in (raiz / "datos/ui_glosario.tsv").read_text(encoding="utf8").splitlines()[1:]:
    en, es, owee, *_ = l.split("\t") + [""]
    for p in owee.replace(" ", "-").split("-"):
        if not valida(p):
            avisos.append(f"{en}: '{p}' no es Owee valido")
    for p in owee.split():
        for q in p.split("-"):
            if q not in lex and not valida(q): avisos.append(f"{en}: '{q}' no existe")
    est = lex.get(owee, "")
    filas.append(dict(en=en, es=es, owee=owee, script=to_script(owee), estado=est))
    if est not in ("ESTABLE", "APROBADA", "AUDITADO 2.0", "PROVISIONAL") and owee in lex:
        avisos.append(f"{en} = {owee}: estado {est} (aprueba en aprobadas.txt)")

cab = '''# Traduccion de oweelinux al Owee ({tipo})
# Generado por 08_Integracion/herramientas/generar_traducciones.py el {fecha}. No editar a mano: edita datos/ui_glosario.tsv.
msgid ""
msgstr ""
"Project-Id-Version: oweelinux 0.1\\n"
"Language: qow\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=1; plural=0;\\n"

'''
hoy = datetime.date.today().isoformat()
for nombre, tipo, campo in (("qow.po", "romano", "owee"), ("qow@owee.po", "Owee Script", "script")):
    out = cab.format(tipo=tipo, fecha=hoy)
    for f in filas:
        out += f'#. {f["es"]}\nmsgid "{f["en"]}"\nmsgstr "{f[campo]}"\n\n'
    (raiz / "linux" / nombre).write_text(out, encoding="utf8")
datos = {f["en"]: dict(es=f["es"], owee=f["owee"], script=f["script"]) for f in filas}
(raiz / "web/qow.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf8")
(raiz / "web/qow.js").write_text("window.OWEE_DICT = " + json.dumps(datos, ensure_ascii=False) + ";\n", encoding="utf8")
print(f"{len(filas)} cadenas -> linux/qow.po, linux/qow@owee.po, web/qow.json, web/qow.js")
for a in avisos: print("  AVISO:", a)
