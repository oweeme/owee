#!/usr/bin/env python3
"""Verificacion completa del proyecto Owee. Uso: python3 verificar_todo.py [--rapido]
Comprueba: textos Owee (fonologia + lexico), lexico cientifico (estados), auditoria de colisiones, sitio web
(generacion + enlaces internos + anclas), traducciones de interfaz, sintaxis de Python/JavaScript, cobertura
de vocabulario basico y estado de git. Termina con codigo 1 si algo falla."""
import collections, glob, html.parser, os, pathlib, py_compile, re, subprocess, sys

RAIZ = pathlib.Path(__file__).resolve().parent
PY = sys.executable
res = []

def correr(cmd, **kw):
    return subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, **kw)

def ok(nombre, pasa, detalle=""):
    res.append((nombre, pasa, detalle)); print(("  OK   " if pasa else "  FALLA"), nombre, ("- " + detalle) if detalle else "")

# 1. textos Owee
val = RAIZ / "03_Material_Ensenanza/Literatura_Poesia/herramientas/validar_owee.py"
mds = sorted(glob.glob(str(RAIZ / "03_Material_Ensenanza/*/Owee_*.md")) + [str(RAIZ / "08_Integracion/README.md")])
malos = [m for m in mds if correr([PY, "-I", str(val), m]).returncode != 0]
ok(f"Textos Owee validos ({len(mds)} archivos)", not malos, ", ".join(pathlib.Path(m).name for m in malos))

# 2. lexico cientifico
r = correr([PY, "-I", "02_Diccionario/datos/generar_ciencias.py"])
estados = re.search(r"estados: (\{.*\})", r.stdout)
est = eval(estados.group(1)) if estados else {}
ok("Lexico cientifico generado", r.returncode == 0 and "REVISAR" not in est, str(est))

# 3. auditoria de colisiones / fonologia
a = correr([PY, "-I", "02_Diccionario/datos/auditar_ciencias.py"]).stdout
inval = re.search(r"== 1\..*?\n(.*?)== 2", a, re.S).group(1).strip()
colis = re.search(r"== 2\..*?\n(.*?)== 3", a, re.S).group(1).strip()
nodef = re.search(r"== 4\..*?\n(.*?)== Resumen", a, re.S).group(1).strip()
ok("Fonologia valida y sin colisiones exactas", not inval and not colis and not nodef, (inval + colis + nodef)[:120])

# 4. sitio web
r = correr([PY, "07_Sitio_Web/build_site.py"])
ok("Sitio web se genera", r.returncode == 0, r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[-200:])
docs = RAIZ / "07_Sitio_Web/docs"
class L(html.parser.HTMLParser):
    def __init__(s): super().__init__(); s.links, s.ids = [], set()
    def handle_starttag(s, t, at):
        d = dict(at)
        if "id" in d: s.ids.add(d["id"])
        for k in ("href", "src"):
            if k in d and d[k] and not d[k].startswith(("http", "mailto", "javascript", "data:")): s.links.append(d[k])
paginas = {p.name: L() for p in docs.glob("*.html")}
for n, p in paginas.items(): p.feed((docs / n).read_text(encoding="utf8"))
rotos = []
for n, p in paginas.items():
    for l in p.links:
        f, _, anc = l.partition("#")
        dest = (docs / f) if f else docs / n
        if f and not dest.exists(): rotos.append(f"{n} -> {l}")
        elif anc and dest.suffix == ".html" and anc not in paginas.get(dest.name, L()).ids: rotos.append(f"{n} -> {l}")
ok(f"Enlaces internos y anclas ({len(paginas)} paginas)", not rotos, "; ".join(rotos[:6]) + (f" (+{len(rotos)-6})" if len(rotos) > 6 else ""))

# 5. traducciones de interfaz
r = correr([PY, "08_Integracion/herramientas/generar_traducciones.py"])
avisos = [l for l in r.stdout.splitlines() if "AVISO" in l]
ok("Traducciones de interfaz", r.returncode == 0, f"{len(avisos)} avisos de aprobacion pendiente" if avisos else "sin avisos")

# 6. sintaxis
fallos = []
for f in RAIZ.rglob("*.py"):
    s = str(f)
    if any(x in s for x in (".pydeps", "99_Archivo", "versiones_anteriores", "/.git/")): continue
    try: py_compile.compile(s, doraise=True)
    except Exception as e: fallos.append(f.name)
ok("Python compila", not fallos, ", ".join(fallos))
js = [str(p) for p in (RAIZ / "08_Integracion/web").glob("*.js") if p.name != "qow.js"] + [str(RAIZ / "04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3/web/owee.js")]
nodo = subprocess.run("command -v node", shell=True, capture_output=True).returncode == 0
fj = [pathlib.Path(j).name for j in js if nodo and subprocess.run(["node", "--check", j], capture_output=True).returncode]
ok("JavaScript con sintaxis valida" if nodo else "JavaScript (node no disponible)", not fj, ", ".join(fj))

# 7. cobertura
c = correr([PY, "-I", "02_Diccionario/datos/cobertura.py"]).stdout
m = re.search(r"TOTAL (\d+): con raíz (\d+) \((\d+)%\), componible (\d+) \((\d+)%\), falta (\d+) \((\d+)%\)", c)
ok("Cobertura de vocabulario basico", bool(m), f"{m.group(2)} con raiz, {m.group(4)} componibles, {m.group(6)} faltan de {m.group(1)}" if m else "")

# 8. git
g = correr(["git", "status", "--porcelain"]).stdout.strip().splitlines()
ok("Git: sin cambios sin guardar", not g, f"{len(g)} archivos con cambios" if g else "")

# resumen de metricas
filas = [l.split("\t") for l in (RAIZ / "02_Diccionario/datos/lexico_ciencias.tsv").read_text(encoding="utf8").splitlines()[1:]]
base = (RAIZ / "02_Diccionario/datos/lexico.tsv").read_text(encoding="utf8").splitlines()[1:]
por_dom = collections.Counter(f[6] for f in filas)
print("\nMETRICAS")
print(f"  lexico general (Base 1.0): {len(base)} formas")
print(f"  lexico ampliado: {len(filas)} formas -> " + ", ".join(f"{k} {v}" for k, v in sorted(por_dom.items())))
print(f"  estados: {dict(collections.Counter(f[4] for f in filas))}")
print(f"  paginas del sitio: {len(paginas)}")
fallan = [n for n, p, d in res if not p]
print("\nRESULTADO:", "TODO CORRECTO" if not fallan else "FALLAN: " + "; ".join(fallan))
sys.exit(1 if fallan else 0)
