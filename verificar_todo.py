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
mds = sorted(glob.glob(str(RAIZ / "03_Material_Ensenanza/*/Owee_*.md")) + glob.glob(str(RAIZ / "01_Especificacion/Owee_*.md")) + [str(RAIZ / "08_Integracion/README.md")])
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

# 7b. cada bloque Owee lleva su traduccion; cobertura Swadesh
falt = []
for f in mds:
    L = pathlib.Path(f).read_text(encoding="utf8").splitlines(); n = len(L); i = 0
    while i < n:
        if L[i].strip() == "```owee":
            j = i + 1
            while j < n and L[j].strip() != "```": j += 1
            k = j + 1
            while k < n and not L[k].strip(): k += 1
            nx = L[k].strip() if k < n else ""
            if not (nx.startswith("*") or nx.startswith("|") or nx.startswith("<!--")): falt.append(f"{pathlib.Path(f).name}:{i+1}")
            i = j
        i += 1
ok("Cada bloque Owee tiene su traduccion", not falt, ", ".join(falt[:5]))
sw = correr([PY, "-I", "02_Diccionario/datos/swadesh100.py"]).stdout.splitlines()[0]
mm = re.search(r"con forma (\d+) \((\d+)%\), componible (\d+) \((\d+)%\), faltan (\d+)", sw)
ok("Cobertura Swadesh-100 >= 90%", bool(mm) and int(mm.group(2)) + int(mm.group(4)) >= 90, sw.split("->")[1].strip() if "->" in sw else sw)
nlec = len(list((RAIZ / "03_Material_Ensenanza/Curso").glob("Owee_Curso_Nivel_*.md")))
ok(f"Curso por niveles ({nlec} niveles + indice)", nlec == 4)

# 7b2. ingles completo por pivote
ri = correr([PY, "-I", "02_Diccionario/datos/generar_ingles.py"])
ok("Ingles (pivote) para todas las formas", ri.returncode == 0, ri.stdout.strip().splitlines()[-1] if ri.returncode else ri.stdout.strip().splitlines()[0])

# 7c. traductor: pruebas de humo en Node con el lexico generado
if nodo:
    prueba = """
const fs=require('fs');globalThis.window=globalThis;
eval(fs.readFileSync('07_Sitio_Web/docs/assets/lexico.js','utf8').replace('window.OWEE_LEX=','globalThis.OWEE_LEX='));
eval(fs.readFileSync('07_Sitio_Web/traductor.js','utf8'));
const T=globalThis.OweeTraductor, fallos=[];
const oe={'me suna nume':'yo deseo agua','ra fame no pume':'él/ella no comer comida','me pe fame pume':'yo [pasado] comer comida'};
for(const k in oe){ if(T.owee2es(k)[0].aproximada!==oe[k]) fallos.push(k+' => '+T.owee2es(k)[0].aproximada); }
const eo={'Yo quiero agua':'me suna nume','Tu duermes en casa':'tu kuma bo sule','No quiero comer':'no nume pume'};
for(const k in eo){ if(T.es2owee(k)[0].sugerencia!==eo[k]) fallos.push(k+' => '+T.es2owee(k)[0].sugerencia); }
const oi={'me suna nume':'I want water','me pe fame pume':'I ate food','ra fame no pume':'he/she does not eat food','tu fame pume ka':'do you eat food?'};
for(const k in oi){ if(T.owee2en(k)[0].aproximada!==oi[k]) fallos.push('EN '+k+' => '+T.owee2en(k)[0].aproximada); }
const io={'I want water':'me suna nume','She does not eat food':'ra fame no pume','Tomorrow I will go to the city':'pu-fusu me kuma-seta to duma'};
for(const k in io){ if(T.en2owee(k)[0].sugerencia!==io[k]) fallos.push('EN '+k+' => '+T.en2owee(k)[0].sugerencia); }
console.log(JSON.stringify(fallos));"""
    r = subprocess.run(["node", "-e", prueba], cwd=RAIZ, capture_output=True, text=True)
    fl = r.stdout.strip() if r.returncode == 0 else r.stderr[-200:]
    ok("Traductor Owee <-> español: pruebas de humo", r.returncode == 0 and fl == "[]", "" if fl == "[]" else fl[:160])

# 7d. calculadora de numeros Owee: lectura, ida y vuelta, cifras y evaluador
if nodo:
    pc = """
const C=require('./07_Sitio_Web/calculadora.js'),f=[];
const L={'0':'cho','10':'be tanu','25':'du tanu sa','100':'be gabu','909':'she gabu she','2026':'du soku du tanu ku','1200000':'be benu du gabu soku','25.50':'du tanu sa doto sa cho'};
for(const k in L){const r=C.leerNum(k);if(r!==L[k])f.push(k+' => '+r);}
for(let n=0;n<3000;n+=7){const r=C.leerOwee(C.leerNum(String(n)));if(r!==n)f.push('ida-vuelta '+n);}
if(C.normales('\\uE042\\uE040\\uE042\\uE046')!=='2026')f.push('normales');
if(C.evaluar('2+3*4')!==14||C.evaluar('(2+3)*4/8')!==2.5||!isNaN(C.evaluar('2+')))f.push('evaluar');
if(C.leerExpr('-5+3')!=='po sa dapa ga')f.push('expr '+C.leerExpr('-5+3'));
console.log(JSON.stringify(f));"""
    r = subprocess.run(["node", "-e", pc], cwd=RAIZ, capture_output=True, text=True)
    fl = r.stdout.strip() if r.returncode == 0 else r.stderr[-200:]
    ok("Calculadora de numeros Owee: pruebas", r.returncode == 0 and fl == "[]", "" if fl == "[]" else fl[:160])

# 7e. teclado Keyman: paquete listo y reglas al dia con el mapa de glifos
import hashlib
kd = RAIZ / "05_Teclado_IME/keyman-owee"
falta = [f for f in ("Owee.kmp", "owee.kmx", "owee.js") if not (kd / "dist" / f).exists()]
kmn0 = (kd / "source/owee.kmn").read_text(encoding="utf8") if (kd / "source/owee.kmn").exists() else ""
subprocess.run(["python3", "generar_keyman.py"], cwd=kd, capture_output=True)
kmn1 = (kd / "source/owee.kmn").read_text(encoding="utf8")
ok("Teclado Keyman (Owee.kmp) generado y al dia", not falta and kmn0 == kmn1, ("falta " + ", ".join(falta)) if falta else ("owee.kmn desactualizado" if kmn0 != kmn1 else ""))

# 7f. sitio publico: sin la seccion Proyecto y sin enlaces rotos
import tempfile, os as _os
with tempfile.TemporaryDirectory() as td:
    env = dict(_os.environ, OWEE_PUBLICO="1", OWEE_OUT=td + "/pub")
    rp = subprocess.run(["python3", "-W", "ignore", "07_Sitio_Web/build_site.py"], cwd=RAIZ, env=env, capture_output=True, text=True)
    prob = []
    if rp.returncode: prob.append("no compila: " + rp.stderr[-120:])
    else:
        pub = pathlib.Path(td) / "pub"
        for i in ("idioma", "estado", "plan", "integracion", "revision", "auditoria"):
            if (pub / f"{i}.html").exists(): prob.append(f"{i}.html no deberia publicarse")
        for h in pub.glob("*.html"):
            t = h.read_text(encoding="utf8")
            if "Proyecto" in t and ">Proyecto" in t.replace("▾", "").replace(" ", ""): prob.append(f"{h.name}: menu Proyecto")
            for m in re.findall(r"""(?:href|src)=["']([^"'#:?]+)(?:#[^"']*)?["']""", t):
                if not (pub / m).exists() and not m.startswith("http"): prob.append(f"{h.name} -> {m}")
    ok("Sitio publico (sin Proyecto, sin enlaces rotos)", not prob, "; ".join(prob[:5]))

# 7g. audio de pronunciacion: cubre todo el lexico y los archivos existen
import json as _json
ad = RAIZ / "03_Material_Ensenanza/Pronunciacion/audio"
try:
    idx = _json.loads((ad / "indice.json").read_text(encoding="utf8"))
    lex = [l.split("\t")[0] for f in ("lexico.tsv", "lexico_ciencias.tsv") for l in (RAIZ / "02_Diccionario/datos" / f).read_text(encoding="utf8").splitlines()[1:]]
    sin = [w for w in lex if w not in idx]
    vacios = [f for f in set(idx.values()) if not (ad / f).exists() or (ad / f).stat().st_size < 500]
    ok(f"Audio de pronunciacion ({len(idx)} textos)", not sin and not vacios, (f"sin audio: {', '.join(sin[:6])}" if sin else "") + (f" archivos vacios: {vacios[:3]}" if vacios else "") + (" (regenera con sintetizar_audio.py)" if sin or vacios else ""))
except Exception as e:
    ok("Audio de pronunciacion", False, str(e)[:100])

# 7h. glifos 3.4 y palabras: ningun glifo es giro de otro, todo el lexico se escribe con la fuente
fd = "04_Fuentes/actual_3.3_fuente_y_glifos/OweeSans3_3_Source"
r1 = correr([PY, "-I", fd + "/auditar_glifos_v4.py"]); r2 = correr([PY, "-I", fd + "/auditar_palabras_v4.py"])
ok("Glifos 3.4: sin giros ni espejos entre consonantes; todo el lexico tiene glifo", r1.returncode == 0 and r2.returncode == 0,
   ((r1.stdout + r2.stdout + r1.stderr + r2.stderr).strip().splitlines() or [""])[-1][:120] if (r1.returncode or r2.returncode) else "")

# 7i. interfaz del sitio en Owee: catalogo valido y selector ES / Owee / Script probado en un navegador
r = correr([PY, "-I", "07_Sitio_Web/validar_ui_owee.py"])
ok("Interfaz en Owee: textos validos", r.returncode == 0, r.stdout.strip().splitlines()[-1] if r.returncode else r.stdout.strip().splitlines()[-1])
try:
    import playwright  # noqa: F401
    with tempfile.TemporaryDirectory() as td2:
        env2 = dict(_os.environ, OWEE_PUBLICO="1", OWEE_OUT=td2 + "/pub")
        subprocess.run(["python3", "-W", "ignore", "07_Sitio_Web/build_site.py"], cwd=RAIZ, env=env2, capture_output=True, text=True)
        rb = correr([PY, "07_Sitio_Web/probar_idiomas.py", td2 + "/pub"])
        ok("Selector ES / Owee / Script en el navegador", rb.returncode == 0, rb.stdout.strip().splitlines()[-1] if rb.returncode else rb.stdout.strip().splitlines()[-1])
except ImportError:
    ok("Selector ES / Owee / Script (playwright no instalado: omitido)", True)

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
