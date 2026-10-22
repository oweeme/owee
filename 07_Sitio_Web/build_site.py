#!/usr/bin/env python3
"""Genera el sitio web de Owee (HTML estatico, sin dependencias) en ./docs

Fuentes de verdad (no se duplican, se leen):
  00_Registro_Maestro/Owee_Registro_Maestro_Completo.md
  02_Diccionario/datos/lexico.tsv
  03_Material_Ensenanza/Literatura_Poesia/Owee_Literatura_y_Poesia_*.md
  04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3  (fuentes web, owee.js, Owee Pad)

Uso:  python3 07_Sitio_Web/build_site.py
Despues, para el PDF imprimible:  python3 07_Sitio_Web/make_pdf.py
"""
import html, json, os, re, shutil, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("OWEE_OUT") or Path(__file__).resolve().parent / "docs")
# Modo publico (OWEE_PUBLICO=1 o --publico): sin la seccion "Proyecto" (registro maestro, estado, auditoria, plan, integracion, revision):
# es material de trabajo interno. El sitio publico solo muestra aprender, leer, ciencias y descargas.
PUBLICO = os.environ.get("OWEE_PUBLICO") == "1" or "--publico" in sys.argv
INTERNAS = ("idioma.html", "estado.html", "revision.html", "auditoria.html", "plan.html", "integracion.html")
GM = ROOT / "04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3"
LIT = sorted((ROOT / "03_Material_Ensenanza/Literatura_Poesia").glob("Owee_Literatura_y_Poesia_*.md"))[-1]
REG = ROOT / "00_Registro_Maestro/Owee_Registro_Maestro_Completo.md"
VERSION = "3.4"

# ---------------------------------------------------------------- lexico
def load_lex():
    rows = []
    for l in (ROOT / "02_Diccionario/datos/lexico.tsv").read_text(encoding="utf8").splitlines()[1:]:
        w, sil, cls, mean, est, sec = l.split("\t")
        rows.append(dict(w=w, sil=sil, cls=cls, mean=mean, est=est, sec=sec))
    return rows

LEX = load_lex()
for e in LEX: e["dom"] = "General"; e["nota"] = ""

def load_sci():
    rows = []
    for l in (ROOT / "02_Diccionario/datos/lexico_ciencias.tsv").read_text(encoding="utf8").splitlines()[1:]:
        w, sil, cls, mean, est, sec, dom, nota = (l.split("\t") + [""] * 8)[:8]
        rows.append(dict(w=w, sil=sil, cls=cls, mean=mean, est=est, sec=sec, dom=dom, nota=nota))
    return rows

SCI = load_sci()
LEXSET = {e["w"] for e in LEX} | {p for e in SCI for p in e["w"].split("-")}
ALL = LEX + SCI

def is_owee(text):
    toks = re.findall(r"[a-z]+", text.lower())
    ok = lambda p: p in LEXSET or re.fullmatch(r"(?:(?:sh|ch|[pbtdkgfsmnlr])?[aeou])+", p) is not None
    return bool(toks) and all(ok(p) for t in toks for p in t.split("-")) and bool(re.fullmatch(r"[a-z ,.\-¿?¡!]+", text.lower()))

def _glosario():
    m = {}
    for e in ALL:
        r = pron(e["w"])
        m.setdefault(e["w"], (e["mean"], (f"{r[1]} /{r[0]}/" if r else "")))
    return m
def glosa(word):
    """Traduccion y pronunciacion de una palabra (o de un compuesto por partes) para el lector."""
    w = word.lower()
    if w in ALLMAP:
        mean, pr = ALLMAP[w]
        return f"{mean} · {pr}" if pr else mean
    if "-" in w:
        partes = [ALLMAP.get(p) for p in w.split("-")]
        if all(partes):
            return " + ".join(x[0].split(" / ")[0].split(" (")[0] for x in partes) + " · " + (pron(w)[1] if pron(w) else "")
    return None

def _prs(w):
    r = pron(w)
    return f"{r[1]} · /{r[0]}/" if r else ""

def expand(text):
    """Sustituye <!--vocab Dominio|Seccion--> y <!--construcciones Dominio--> por tablas."""
    def vocab(m):
        dom, sec = m.group(1), m.group(2)
        rows = [e for e in SCI if e["dom"] == dom and e["cls"] == "raíz técnica" and (sec == "*" or e["sec"] == sec)]
        out = ["| Owee | Pronunciación | Concepto | Estado |", "|---|---|---|---|"]
        for e in rows:
            est = e["est"] + (" — " + e["nota"] if e["nota"] else "")
            out.append(f"| {e['w']} | {_prs(e['w'])} | {e['mean']} | {est} |")
        return "\n".join(out)
    def cons(m):
        rows = [e for e in SCI if e["dom"] == m.group(1) and e["cls"] == "construcción" and (not m.group(2) or e["sec"] == m.group(2))]
        out = ["| Owee | Pronunciación | Significado | Estado |", "|---|---|---|---|"]
        out += [f"| {e['w']} | {_prs(e['w'])} | {e['mean']} | {e['est']}{(' — ' + e['nota']) if e['nota'] else ''} |" for e in rows]
        return "\n".join(out)
    def vocabulario(m):
        palabras = m.group(1).split()
        malas = [w for w in palabras if w not in ALLMAP]
        if malas: raise ValueError("vocabulario: palabras fuera del lexico: " + ", ".join(malas))
        out = ["| Owee | Pronunciación | Significado |", "|---|---|---|"]
        for w in palabras:
            out.append(f"| {w} | {_prs(w)} | {ALLMAP[w][0]} |")
        return "\n".join(out)
    text = re.sub(r"<!--vocabulario ([^>]+?)-->", vocabulario, text)
    text = text.replace("<!--digitos-->", tabla_digitos())
    text = text.replace("<!--pronunciacion-->", tabla_pron()).replace("<!--silabas-->", tabla_silabas())
    text = re.sub(r"<!--vocab ([^|>]+)\|([^>]+?)-->", vocab, text)
    return re.sub(r"<!--construcciones ([^|>]+?)(?:\|([^>]+?))?-->", cons, text)


# ---------------------------------------------------------------- numerales Owee (Matematicas 1.0)
def leer3(n):
    """0-999 -> palabras Owee. Se omiten las posiciones con 0 (909 = she gabu she)."""
    h, t, u = n // 100, (n // 10) % 10, n % 10
    w = []
    if h: w.append(f"{NOMBRES[h]} gabu")
    if t: w.append(f"{NOMBRES[t]} tanu")
    if u: w.append(NOMBRES[u])
    return " ".join(w)

NOMBRES = "cho be du ga fo sa ku mu na she".split()

def leer_num(txt):
    ent, _, dec = txt.partition(".")
    n = int(ent)
    if n == 0:
        w = ["cho"]
    else:
        w = []
        m, k, r = n // 1_000_000, (n // 1000) % 1000, n % 1000
        if n >= 1_000_000_000: raise ValueError(f"numero demasiado grande: {txt}")
        if m: w.append(leer3(m) + " benu")
        if k: w.append(leer3(k) + " soku")
        if r: w.append(leer3(r))
    if dec:
        w.append("doto " + " ".join(NOMBRES[int(d)] for d in dec))
    return " ".join(w)

OPS = {"+": "dapa", "-": "dopo", "−": "dopo", "×": "kebu", "*": "kebu", "÷": "faku", "=": "se", "<": "po", ">": "pa",
       "≥": "pa-lo-se", "≤": "po-lo-se", "%": "gabu-palo", "^": "telu", "√": "raku", "/": "palo"}

def leer_expr(expr):
    toks = re.findall(r"\d+(?:\.\d+)?|[+\-−×*÷=<>≥≤%^√/]", expr.replace(" ", ""))
    if "".join(toks) != expr.replace(" ", ""): raise ValueError(f"expresion no soportada: {expr}")
    out, prev = [], None
    for t in toks:
        if t[0].isdigit(): out.append(leer_num(t))
        elif t in "-−" and (prev is None or not prev[0].isdigit() and prev != "%"):
            out.append("po")          # signo negativo: po (menos escalar); la resta es dopo
        elif t == "+" and (prev is None or not prev[0].isdigit() and prev != "%"):
            out.append("pa")          # signo positivo explicito
        else: out.append(OPS[t])
        prev = t
    return " ".join(out)

def comprobar(expr):
    """Si la expresion es una igualdad/desigualdad entera, verifica que sea cierta (evita ejemplos erroneos)."""
    if "%" in expr: return
    from fractions import Fraction
    import math
    e = expr.replace("−", "-").replace("×", "*").replace("÷", "/").replace("^", "**").replace("≥", ">=").replace("≤", "<=")
    e = re.sub(r"√(\d+)", lambda m: f"_r({m.group(1)})", e)
    e = re.sub(r"(?<![<>=!])=(?!=)", "==", e)
    e = re.sub(r"(\d+(?:\.\d+)?)", lambda m: f"_F('{m.group(1)}')", e)
    def _r(x):
        x = int(x); r = math.isqrt(x)
        return Fraction(r) if r * r == x else Fraction(math.sqrt(x)).limit_denominator(10**9)
    if not eval(e, {"__builtins__": {}}, {"_F": Fraction, "_r": lambda x: _r(x.numerator if hasattr(x, "numerator") else x)}):
        raise ValueError(f"ejemplo numerico FALSO: {expr}")

def numhtml(expr, leer=True):
    if leer and any(c in expr for c in "=<>≥≤"): comprobar(expr)
    num = f'<span class="n" data-n="{esc(expr)}">{esc(expr)}</span>'
    if not leer: return num
    w = leer_expr(expr)
    return (f'<span class="nx">{num}<span class="rd"><span class="o" data-o="{w}" title="{w}">{w}</span>'
            f'<small>{w}</small></span></span>')

def tabla_digitos():
    rows = ["| Número | Nombre | Escritura fonética | Glifo numérico |", "|---|---|---|---|"]
    for i, n in enumerate(NOMBRES):
        rows.append(f"| {i} | **{n}** (romano) | `{n}` | `#{i}` |")
    return "\n".join(rows)


# ---------------------------------------------------------------- pronunciacion
_IC = {"p": "p", "b": "b", "t": "t", "d": "d", "k": "k", "g": "ɡ", "f": "f", "s": "s", "m": "m", "n": "n", "l": "l", "r": "ɾ", "sh": "ʃ", "ch": "tʃ"}
_SIL = re.compile(r"(sh|ch|[pbtdkgfsmnlr])?([aeou])")

def _sylls(part):
    out = [(m.group(1) or "", m.group(2)) for m in _SIL.finditer(part)]
    return out if "".join(c + v for c, v in out) == part else None

def pron(word):
    """(AFI, transcripcion para hispanohablantes) de una palabra o compuesto; None si no es Owee valido."""
    ipa, resp = [], []
    for pi, part in enumerate(word.lower().split("-")):
        ss = _sylls(part)
        if not ss: return None
        for si, (c, v) in enumerate(ss):
            mark = "ˈ" if (pi == 0 and si == 0) else ("ˌ" if (si == 0 and len(ss) >= 2) else "")
            ipa.append((mark, _IC.get(c, "") + v))
            resp.append((c + v).upper() if mark else c + v)
    a = ""
    for i, (mark, sy) in enumerate(ipa):
        a += (mark if mark else ("." if i else "")) + sy
    return a, "-".join(resp)

def tabla_pron():
    ej = ["me", "tu", "suna", "nara", "kuma", "sade", "shome", "choma", "tare", "tera", "ganu", "kuna-bore", "sade-kelo", "suna-gore-pa", "gura-lena"]
    allm = {e["w"]: e["mean"] for e in ALL}
    rows = ["| Owee | Romano | AFI | Pronunciación | Significado |", "|---|---|---|---|---|"]
    for w in ej:
        a, r = pron(w)
        rows.append(f"| {w} | {w} | /{a}/ | {r} | {allm.get(w, '')} |")
    return "\n".join(rows)

def tabla_silabas():
    rows = ["| | A | E | O | U |", "|---|---|---|---|---|", "| *vocal sola* | " + " | ".join(f"`{v}` /{v}/" for v in "aeou") + " |"]
    for c in ["p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"]:
        rows.append(f"| **{c}** /{_IC[c]}/ | " + " | ".join(f"`{c+v}` /{_IC[c]}{v}/" for v in "aeou") + " |")
    return "\n".join(rows)

ALLMAP = _glosario()

# ---------------------------------------------------------------- markdown minimo
def slug(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def esc(s):
    return html.escape(s, quote=False)

def oweespan(text, cls="o"):
    g = glosa(text) if re.fullmatch(r"[a-z]+(?:-[a-z]+)*", text) else None
    if g:   # palabra conocida: tooltip con traduccion y pronunciacion (cursor o toque)
        return f'<span class="{cls} ow" tabindex="0" data-o="{esc(text)}" data-g="{esc(g)}" title="{esc(text)}">{esc(text)}</span>'
    return f'<span class="{cls}" data-o="{esc(text)}" title="{esc(text)}">{esc(text)}</span>'

def inline(s, convert=True):
    codes = []
    def keep(m):
        t = m.group(1)
        if t.startswith("#"):
            codes.append(numhtml(t[1:].strip(), leer=False))
        else:
            codes.append(oweespan(t) if convert and is_owee(t) else f"<code>{esc(t)}</code>")
        return f"\x00{len(codes)-1}\x00"
    def keepnum(m):
        codes.append(numhtml(m.group(1).strip()))
        return f"\x00{len(codes)-1}\x00"
    s = re.sub(r"`([^`]+)`", keep, s)
    s = re.sub(r"\[\[(.+?)\]\]", keepnum, s)
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)
    return s

def verso_html(linea):
    """Una linea Owee: cada palabra es un span con glifos y, al pasar el cursor o tocar, su traduccion y pronunciacion."""
    sp = ""
    for t in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*|[^A-Za-z]+", linea):
        if re.match(r"[A-Za-z]", t):
            g = glosa(t)
            sp += f'<span class="ow" tabindex="0" data-o="{esc(t)}"' + (f' data-g="{esc(g)}"' if g else "") + f'>{esc(t)}</span>'
        else:
            sp += esc(t)
    return f'<div class="v" data-say="{esc(linea)}"><span class="o">{sp}</span><small class="r">{esc(linea)}</small></div>'

def md(text, convert=True):
    """Devuelve (html, toc[(nivel, texto, id)], poems[(id, titulo, [lineas])])"""
    lines = text.splitlines()
    out, toc, poems = [], [], []
    i, para, h3 = 0, [], None
    def flush():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para), convert) + "</p>")
            para = []
    while i < len(lines):
        l = lines[i]
        s = l.strip()
        if s.startswith("```"):
            flush()
            lang = s.strip("`").strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i]); i += 1
            if lang == "owee":
                ls = [b for b in body if b.strip() and not b.lstrip().startswith("#")]
                if h3: poems.append((h3[0], h3[1], ls))
                out.append('<div class="poema">' + "".join(verso_html(b.strip()) for b in ls) + "</div>")
            else:
                out.append("<pre>" + esc("\n".join(body)) + "</pre>")
        elif s == "<!--resp-->":
            flush(); out.append('<details class="resp"><summary>Ver respuestas</summary>')
        elif s == "<!--/resp-->":
            flush(); out.append("</details>")
        elif re.match(r"^#{1,6} ", s):
            flush()
            n = len(s.split()[0]); t = s[n + 1:].strip()
            hid = slug(re.sub(r"[`*]", "", t))
            toc.append((n, re.sub(r"[`*]", "", t), hid))
            if n == 3: h3 = (hid, re.sub(r"[`*]", "", t))
            out.append(f'<h{n} id="{hid}">{inline(t, convert)}</h{n}>')
        elif re.fullmatch(r"-{3,}|\*{3,}", s):
            flush(); out.append("<hr>")
        elif s.startswith(">"):
            flush(); q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip()); i += 1
            i -= 1
            out.append("<blockquote><p>" + inline(" ".join(q), convert) + "</p></blockquote>")
        elif s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            flush()
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            head = cells(s); i += 2; rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            i -= 1
            owee_cols = {j for j, h in enumerate(head) if h.strip().lower() in ("owee", "forma owee")}
            def cell(c, j):
                if j in owee_cols:
                    t = c.strip().strip("`")
                    if is_owee(t): return oweespan(t) + f'<br><small class="rm">{esc(t)}</small>'
                return inline(c, convert)
            out.append('<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline(h, False)}</th>" for h in head) +
                       "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{cell(c, j)}</td>" for j, c in enumerate(r)) + "</tr>" for r in rows) +
                       "</tbody></table></div>")
        elif re.match(r"^(\d+\.|-|\*)\s+", s):
            flush()
            ordered = bool(re.match(r"^\d+\.", s)); items = []
            while i < len(lines):
                m = re.match(r"^(\d+\.|-|\*)\s+(.*)$", lines[i].strip())
                if m:
                    items.append([m.group(2)]); i += 1
                elif lines[i].startswith("  ") and lines[i].strip() and items:
                    items[-1].append(lines[i].strip()); i += 1
                else:
                    break
            i -= 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join("<li>" + inline(" ".join(it), convert) + "</li>" for it in items) + f"</{tag}>")
        elif not s:
            flush()
        else:
            para.append(s.rstrip("\\").strip())
        i += 1
    flush()
    return "\n".join(out), toc, poems

# ---------------------------------------------------------------- plantilla
NAV = [("index.html", "Inicio", "pado"),
       ("Aprender", [("curso.html", "Curso por niveles", "tase-kelo"), ("escritura.html", "Escritura", "beka"), ("pronunciacion.html", "Pronunciación", "sone"),
                     ("gramatica.html", "Gramática", "foma"), ("diccionario.html", "Diccionario", "reka-doke"), ("traductor.html", "Traductor"), ("calculadora.html", "Calculadora de números", "banu-meka"), ("teclado.html", "Teclado Owee", "maku-tabe"), ("nombres.html", "Nombres propios", "sena-nara")], "tase"),
       ("Leer", [("literatura.html", "Literatura y canciones", "lodu-lena")], "lodu"),
       ("Ciencias", [("matematicas.html", "Matemáticas"), ("fisica.html", "Física"), ("quimica.html", "Química"), ("astronomia.html", "Astronomía y astrología"),
                     ("informatica.html", "Informática")], "lare"),
       ("Proyecto", [("idioma.html", "Registro Maestro"), ("estado.html", "Estado y pendientes"), ("revision.html", "Revisión semántica"), ("auditoria.html", "Auditoría inicial"), ("plan.html", "Plan de ampliación"),
                     ("integracion.html", "Integración (oweelinux, web)"), ("descargas.html", "Descargas", "gura")], "dare")]

if PUBLICO:
    NAV = [it for it in NAV if it[0] != "Proyecto"] + [("descargas.html", "Descargas", "gura")]

CSS = r"""
:root{--bg:#fbfaf7;--surface:#fff;--ink:#1c2430;--ink2:#566170;--rule:#e2dfd7;--accent:#2F6FB0;--accent-ink:#fff;--soft:#eaf1f9;--warn:#a65f00;--ok:#2d7a4b;--owee-size:1.6rem}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14181e;--surface:#1b2129;--ink:#e8ebef;--ink2:#9aa6b4;--rule:#2b3440;--accent:#6aa8e6;--accent-ink:#0c1620;--soft:#1e2a38;--warn:#e0a24a;--ok:#6ccf93}}
:root[data-theme=dark]{--bg:#14181e;--surface:#1b2129;--ink:#e8ebef;--ink2:#9aa6b4;--rule:#2b3440;--accent:#6aa8e6;--accent-ink:#0c1620;--soft:#1e2a38;--warn:#e0a24a;--ok:#6ccf93}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:1rem/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}
header.top{position:sticky;top:0;z-index:5;background:var(--surface);border-bottom:1px solid var(--rule)}
header.top .in{max-width:1100px;margin:0 auto;padding:10px 16px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 20px}
.brand{display:flex;align-items:baseline;gap:10px;text-decoration:none;color:var(--ink)}
.brand b{font-size:1.25rem}.brand .mark{font-family:'Owee Sans';font-size:1.7rem;color:var(--accent);line-height:1}
nav{display:flex;flex-wrap:wrap;gap:4px}
nav a{padding:6px 12px;border-radius:8px;text-decoration:none;color:var(--ink2);font-size:.95rem}
nav a:hover{background:var(--soft)}nav a[aria-current=page]{background:var(--accent);color:var(--accent-ink)}
main{max-width:1100px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:2rem;line-height:1.2;margin:.2em 0 .5em}h2{margin:2em 0 .5em;padding-top:.3em;border-top:1px solid var(--rule)}h3{margin:1.6em 0 .4em}
.o{font-family:'Owee Sans',system-ui;font-size:var(--owee-size);line-height:1.5;color:var(--ink)}
code{font:.9em ui-monospace,"IBM Plex Mono",Menlo,monospace;background:var(--soft);padding:1px 5px;border-radius:5px}
pre{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:12px 14px;overflow:auto;font:.88rem/1.5 ui-monospace,Menlo,monospace}
blockquote{margin:1em 0;padding:.2em 1em;border-left:4px solid var(--accent);background:var(--soft);border-radius:0 8px 8px 0}
.tw{overflow-x:auto;margin:1em 0}table{border-collapse:collapse;width:100%;font-size:.95rem}
th,td{border:1px solid var(--rule);padding:6px 10px;text-align:left;vertical-align:top}th{background:var(--soft)}
.o{white-space:pre-wrap}td .o{font-size:1.3rem}
.hero{display:grid;gap:12px;padding:28px 0 8px}.hero .big{font-family:'Owee Sans';font-size:clamp(3rem,10vw,5.5rem);line-height:1.1;color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;margin:18px 0}
.card{background:var(--surface);border:1px solid var(--rule);border-radius:12px;padding:16px;text-decoration:none;color:var(--ink);display:block}
a.card:hover{border-color:var(--accent)}.card h3{margin:0 0 .3em;border:0}.card p{margin:.2em 0;color:var(--ink2);font-size:.93rem}
.chip{display:inline-block;font-size:.72rem;letter-spacing:.04em;border-radius:99px;padding:1px 9px;background:var(--soft);color:var(--ink2);margin-right:4px}
.chip.prov{background:transparent;border:1px solid var(--warn);color:var(--warn)}.chip.st{border:1px solid var(--ok);background:transparent;color:var(--ok)}
.stats{display:flex;flex-wrap:wrap;gap:12px;margin:16px 0}.stats div{background:var(--surface);border:1px solid var(--rule);border-radius:12px;padding:10px 16px}.stats b{font-size:1.5rem;display:block}
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:16px 0}
.controls input[type=search],.controls select{font:inherit;padding:8px 12px;border:1px solid var(--rule);border-radius:8px;background:var(--surface);color:var(--ink)}
.controls input[type=search]{flex:1 1 220px;min-width:0}
.seg{display:inline-flex;border:1px solid var(--rule);border-radius:8px;overflow:hidden}.seg button{font:inherit;font-size:.9rem;border:0;background:var(--surface);color:var(--ink);padding:7px 12px;cursor:pointer}.seg button[aria-pressed=true]{background:var(--accent);color:var(--accent-ink)}
.entry{background:var(--surface);border:1px solid var(--rule);border-radius:12px;padding:12px 14px;display:grid;grid-template-columns:auto 1fr;gap:4px 14px;align-items:center;scroll-margin-top:80px}
.entry:target{border-color:var(--accent);box-shadow:0 0 0 3px var(--soft)}
.entry{align-content:center}.entry .g{grid-row:1/5;font-size:2.4rem;min-width:3.2rem;text-align:center}
.entry .w{font-weight:700;font-size:1.15rem}.entry .w small{font-weight:400;color:var(--ink2);font-size:.85rem;margin-left:6px}
.entry .m{color:var(--ink)}.entry .u{font-size:.82rem;color:var(--ink2)}
.sec{margin:28px 0 8px;font-size:1.1rem;color:var(--ink2);border:0;padding:0}
.matrix{display:grid;grid-template-columns:70px repeat(4,1fr);gap:6px;max-width:640px;margin:14px 0}
.matrix div{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:8px 4px;text-align:center}
.matrix .h{background:var(--soft);font-weight:700}.matrix .o{font-size:2.1rem;display:block;line-height:1.2}.matrix small{color:var(--ink2)}
.poema{background:var(--surface);border:1px solid var(--rule);border-radius:12px;padding:16px 22px;margin:14px 0;max-width:640px}
.poema .v{padding:2px 0}.poema .v .o{font-size:1.9rem;display:block}.poema .v .r{display:block;color:var(--ink2);font-size:.85rem;margin-top:-6px}
body[data-mode=glifos] .poema .r{display:none}body[data-mode=romano] .poema .o{display:none}
body[data-mode=romano] .poema .r{font-size:1.2rem;color:var(--ink);margin:0}
.layout{display:grid;grid-template-columns:240px minmax(0,1fr);gap:28px}
@media(max-width:860px){.layout{grid-template-columns:1fr}.toc{position:static!important;max-height:none!important}}
.toc{position:sticky;top:70px;align-self:start;max-height:calc(100vh - 90px);overflow:auto;font-size:.88rem;border-right:1px solid var(--rule);padding-right:12px}
.toc a{display:block;padding:3px 0;color:var(--ink2);text-decoration:none}.toc a:hover{color:var(--accent)}.toc .l3{padding-left:14px;font-size:.84rem}
.dl{display:flex;flex-direction:column;gap:6px}.dl a{display:flex;justify-content:space-between;gap:12px;padding:8px 12px;background:var(--surface);border:1px solid var(--rule);border-radius:8px;text-decoration:none}
.dl a span{color:var(--ink2);font-size:.85rem}
footer{max-width:1100px;margin:0 auto;padding:0 16px 40px;color:var(--ink2);font-size:.85rem}
.n .o{font-size:1.2em;line-height:1}.n{white-space:nowrap}
.nx{display:inline-flex;flex-wrap:wrap;align-items:baseline;gap:2px 14px}.nx .rd{display:inline-flex;flex-direction:column;line-height:1.25}.nx .rd .o{font-size:1.25rem}.nx .rd small{color:var(--ink2);font-size:.78rem}
.dd{position:relative}.dd summary{list-style:none;cursor:pointer;padding:6px 12px;border-radius:8px;color:var(--ink2);font-size:.95rem}.dd summary::-webkit-details-marker{display:none}
.dd summary:hover,.dd[open] summary{background:var(--soft)}.dd[data-on] summary{background:var(--accent);color:var(--accent-ink)}
.dd .dm{position:absolute;top:100%;left:0;z-index:9;min-width:220px;background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:6px;display:flex;flex-direction:column;box-shadow:0 6px 20px rgba(0,0,0,.12)}
.dd .dm a{white-space:nowrap}
.say{cursor:pointer;border-bottom:1px dotted var(--accent)}.say:hover{background:var(--soft)}.playbtn{border:1px solid var(--rule);background:var(--surface);color:var(--accent);border-radius:50%;width:1.9rem;height:1.9rem;cursor:pointer;font-size:.7rem;margin-left:10px;vertical-align:middle;line-height:1}.playbtn:hover{background:var(--soft)}
.rm{color:var(--ink2);font-size:.78rem}.chip.ver{border:1px solid var(--accent);background:transparent;color:var(--accent)}
.ow{position:relative}.ow[data-g]{cursor:help;border-bottom:1px dotted transparent}.ow[data-g]:hover,.ow[data-g]:focus{border-bottom-color:var(--accent);outline:none}
.ow[data-g]:hover::after,.ow[data-g]:focus::after{content:attr(data-g);position:absolute;z-index:20;left:0;bottom:calc(100% + 6px);width:max-content;max-width:17rem;background:var(--ink);color:var(--bg);font:.8rem/1.35 system-ui,sans-serif;padding:5px 9px;border-radius:7px;white-space:normal;pointer-events:none}
details.resp{margin:1em 0;border:1px solid var(--rule);border-radius:10px;padding:.2em 1em;background:var(--surface)}details.resp summary{cursor:pointer;font-weight:600;padding:.5em 0;color:var(--accent)}
.uimode{margin-left:auto}.uimode button{padding:5px 9px!important;font-size:.82rem!important}.uimode .o{font-size:1.15rem;line-height:1}
.ruta{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:18px 0}.nivel{border-left:5px solid var(--accent)}.nivel .n{font-size:2rem;font-weight:700;color:var(--accent);line-height:1}
.fdd{background:var(--soft);border:1px solid var(--rule);border-radius:14px;padding:14px 20px;margin:18px 0}.fdd .o{font-size:2rem;display:block}.fdd small{color:var(--ink2)}
.hide{display:none!important}
@media print{header.top,.controls,.toc,footer,.noprint{display:none!important}body{background:#fff;color:#000}.layout{display:block}main{max-width:none;padding:0}
.poema,.entry,.card{break-inside:avoid;border-color:#bbb;background:#fff}h2{break-before:auto}}
"""

JS_COMMON = r"""
(function(){
  try{var t=localStorage.getItem('owee-theme');if(t)document.documentElement.dataset.theme=t}catch(e){}
  function conv(root){
    if(!window.Owee)return;
    (root||document).querySelectorAll('[data-o]').forEach(function(n){n.textContent=Owee.toScript(n.dataset.o,{digits:true});});
  }
  function numconv(root){
    (root||document).querySelectorAll('[data-n]').forEach(function(n){
      n.textContent='';
      n.dataset.n.split(/([0-9]+)/).forEach(function(part){
        if(!part)return;
        if(/^[0-9]+$/.test(part)){var sp=document.createElement('span');sp.className='o';
          sp.textContent=part.split('').map(function(d){return String.fromCharCode(0xE040+Number(d))}).join('');n.appendChild(sp)}
        else n.appendChild(document.createTextNode(part));
      });
    });
  }
  document.addEventListener('click',function(e){document.querySelectorAll('details.dd[open]').forEach(function(d){if(!d.contains(e.target))d.removeAttribute('open')})});
  function uiMode(m){
    try{localStorage.setItem('owee-ui',m)}catch(e){}
    document.querySelectorAll('[data-ow]').forEach(function(el){
      if(!el.dataset.esOrig)el.dataset.esOrig=el.textContent;
      if(m==='es'){el.textContent=el.dataset.esOrig;el.classList.remove('o');el.removeAttribute('title');return}
      if(m==='owee'){el.textContent=el.dataset.ow;el.classList.remove('o');el.title=el.dataset.esOrig;return}
      el.textContent=window.Owee?Owee.toScript(el.dataset.ow):el.dataset.ow;el.classList.add('o');el.title=el.dataset.ow+' — '+el.dataset.esOrig;
    });
    document.querySelectorAll('[data-ui]').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.ui===m)});
  }
  window.oweeConv=conv;
  document.addEventListener('DOMContentLoaded',function(){conv();numconv();
    document.querySelectorAll('[data-ui]').forEach(function(b){b.onclick=function(){uiMode(b.dataset.ui)}});
    var um;try{um=localStorage.getItem('owee-ui')}catch(e){}if(um&&um!=='es')uiMode(um);
    var m;try{m=localStorage.getItem('owee-mode')}catch(e){}
    document.body.dataset.mode=document.body.dataset.forcemode||m||'ambos';
    document.querySelectorAll('[data-setmode]').forEach(function(b){
      b.setAttribute('aria-pressed',b.dataset.setmode===document.body.dataset.mode);
      b.onclick=function(){document.body.dataset.mode=b.dataset.setmode;try{localStorage.setItem('owee-mode',b.dataset.setmode)}catch(e){}
        document.querySelectorAll('[data-setmode]').forEach(function(x){x.setAttribute('aria-pressed',x===b)})}});
    var tb=document.getElementById('theme');if(tb)tb.onclick=function(){var d=document.documentElement.dataset.theme;
      var n=d==='dark'?'light':'dark';document.documentElement.dataset.theme=n;try{localStorage.setItem('owee-theme',n)}catch(e){}};
  });

  /* Audio de pronunciacion (voz sintetica): .v[data-say] ganan un boton, las palabras y los <code> con audio se pueden pulsar */
  var cur=null;
  function say(t){var A=window.OWEE_AUDIO,f=A&&A[String(t).toLowerCase().trim()];if(!f)return false;
    try{if(cur)cur.pause();cur=new Audio('audio/'+f);cur.play().catch(function(){})}catch(e){}return true}
  window.oweeSay=say;
  document.addEventListener('DOMContentLoaded',function(){
    var A=window.OWEE_AUDIO;if(!A)return;
    document.querySelectorAll('.v[data-say]').forEach(function(v){var t=v.dataset.say;if(!A[t.toLowerCase()])return;
      var b=document.createElement('button');b.className='playbtn noprint';b.type='button';b.title='Escuchar';b.setAttribute('aria-label','Escuchar');b.textContent='▶';
      b.onclick=function(){say(t)};v.appendChild(b)});
    document.querySelectorAll('.ow[data-o]').forEach(function(w){if(!A[w.dataset.o.toLowerCase()])return;
      w.addEventListener('click',function(){say(w.dataset.o)})});
    document.querySelectorAll('code').forEach(function(c){var t=c.textContent;if(!A[t.toLowerCase()]||c.closest('pre'))return;
      c.classList.add('say');c.title='Escuchar';c.onclick=function(){say(t)}});
    var fd=document.getElementById('fr');if(fd){var f=fd.textContent;if(A[f.toLowerCase()]){var b=document.createElement('button');b.className='playbtn noprint';b.type='button';b.title='Escuchar';b.textContent='▶';b.onclick=function(){say(f)};fd.parentNode.insertBefore(b,fd.nextSibling)}}
  });
})();
"""

def page(fname, title, body, active=None, extra_head="", body_attrs="", chrome=True, extra_js=""):
    def lab(txt, ow=None):
        return f'<span data-ow="{ow}">{txt}</span>' if ow else txt
    def navitem(it):
        if isinstance(it[1], list):
            on = any(k[0] == active for k in it[1])
            kids = "".join(f'<a href="{k[0]}"{" aria-current=page" if k[0] == active else ""}>{lab(k[1], k[2] if len(k) > 2 else None)}</a>' for k in it[1])
            return f'<details class="dd"{" data-on=1" if on else ""}><summary>{lab(it[0], it[2] if len(it) > 2 else None)} ▾</summary><div class="dm">{kids}</div></details>'
        return f'<a href="{it[0]}"{" aria-current=page" if it[0] == active else ""}>{lab(it[1], it[2] if len(it) > 2 else None)}</a>'
    nav = "".join(navitem(it) for it in NAV)
    top = (f'<header class="top"><div class="in"><a class="brand" href="index.html"><span class="mark o" data-o="owee">owee</span><b>Owee</b></a>'
           f'<nav>{nav}</nav><span class="seg uimode noprint" role="group" aria-label="Idioma de la interfaz"><button data-ui="es" aria-pressed="true">ES</button><button data-ui="owee">Owee</button><button data-ui="script" class="o">owee</button></span><button id="theme" class="noprint" style="font:inherit;border:1px solid var(--rule);background:var(--surface);color:var(--ink);border-radius:8px;padding:5px 10px;cursor:pointer" aria-label="Cambiar tema">◐</button></div></header>') if chrome else ""
    foot = f'<footer><p>Owee · sitio generado desde el Registro Maestro y el Diccionario Base · Owee Script/Sans {VERSION}. La romanización es la forma oficial; los glifos requieren la fuente Owee (incluida en esta página). Licencias: texto y datos CC BY-SA 4.0 · fuentes SIL OFL 1.1 · código MIT.</p></footer>' if chrome else ""
    doc = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} · Owee</title>
<link rel="icon" href="pad/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/owee.css"><style>{CSS}</style>{extra_head}</head>
<body {body_attrs}>{top}<main>{body}</main>{foot}
<script src="assets/owee.js"></script><script src="assets/audio.js"></script><script>{JS_COMMON}</script>{extra_js}</body></html>"""
    if PUBLICO:
        doc = re.sub(r'<a [^>]*href=["\'](?:%s)(?:#[^"\']*)?["\'][^>]*>(.*?)</a>' % "|".join(re.escape(x) for x in INTERNAS), r"\1", doc, flags=re.S)
    (OUT / fname).write_text(doc, encoding="utf8")

# ---------------------------------------------------------------- paginas
def frases_html():
    filas = [l.split("\t") for l in (Path(__file__).resolve().parent / "frases.tsv").read_text(encoding="utf8").splitlines() if l.strip()]
    for o, _ in filas:
        for t in re.findall(r"[a-z]+(?:-[a-z]+)*", o.lower()):
            if t not in ALLMAP and not all(p in ALLMAP for p in t.split("-")):
                raise ValueError(f"frases.tsv: palabra fuera del lexico: {t}")
    datos = json.dumps([[o, es] for o, es in filas], ensure_ascii=False)
    return f"""<div class="fdd"><small>Frase del día</small><span class="o" id="fo"></span><span id="fr" style="color:var(--ink2)"></span><div id="fes"></div>
<script>(function(){{var F={datos},d=new Date(),k=(d.getFullYear()*372+d.getMonth()*31+d.getDate())%F.length,f=F[k];
window.addEventListener('DOMContentLoaded',function(){{document.getElementById('fo').textContent=Owee.toScript(f[0],{{digits:true}});
document.getElementById('fr').textContent=f[0];document.getElementById('fes').textContent=f[1]}})}})()</script></div>"""

def build_index(stats):
    if PUBLICO:
        proy_href, proy_t, proy_p = "descargas.html", "Descargas", "PDF, fuentes, teclado y audio para usar Owee en tu ordenador."
    else:
        proy_href, proy_t, proy_p = "estado.html", "Proyecto", "Estado, pendientes, plan de ampliación, integración con Linux y la web, descargas."
    body = f"""
<div class="hero"><div class="big o" data-o="owee suma">owee suma</div>
<h1>Owee — aprende un idioma construido, fácil y completo</h1>
<p>4 vocales, 14 consonantes, 60 sílabas, gramática sin género ni conjugaciones y una escritura propia donde <strong>1 sílaba = 1 bloque</strong>.
Empieza aquí: sumérgete en el idioma con glifos, romanización, pronunciación y traducción en cada frase.</p></div>
{frases_html()}
<h2>Tu ruta de aprendizaje</h2>
<div class="ruta">
<a class="card nivel" href="nivel-0.html"><div class="n">0</div><h3>Ver y oír</h3><p>Vocales, sílabas, glifos, números. 1–2 h.</p></a>
<a class="card nivel" href="nivel-1.html"><div class="n">1</div><h3>Primeras frases</h3><p>Tú y yo, casa, lugar, tiempo, cuerpo, naturaleza. A1.</p></a>
<a class="card nivel" href="nivel-2.html"><div class="n">2</div><h3>Conversar</h3><p>Negar, comparar, pedir, verbos, diálogos. A2.</p></a>
<a class="card nivel" href="nivel-3.html"><div class="n">3</div><h3>Leer y crear</h3><p>Compuestos, historias, ciencia, poesía, tu texto. B1.</p></a></div>
<div class="stats"><div><b>{stats['n']}</b>léxico base</div><div><b>{stats['sci']}</b>términos ampliados</div><div><b>60</b>sílabas</div>
<div><b>{stats['poems']}</b>textos y canciones</div><div><b>{stats['pdfs']}</b>PDF</div></div>
<h2>Explora</h2>
<div class="grid">
<a class="card" href="escritura.html"><h3>Escritura</h3><p>Los 60 bloques silábicos, los dígitos y las marcas de compuesto y nombre propio.</p></a>
<a class="card" href="pronunciacion.html"><h3>Pronunciación</h3><p>Cómo suena cada letra, con AFI y notas escritas en Owee.</p></a>
<a class="card" href="gramatica.html"><h3>Gramática</h3><p>Las reglas con ejemplos: sí, imperativo, demostrativos, compuestos, relativas.</p></a>
<a class="card" href="diccionario.html"><h3>Diccionario</h3><p>Todas las palabras con glifo, romano, pronunciación y traducción; buscador Owee ↔ español.</p></a>
<a class="card" href="literatura.html"><h3>Literatura y canciones</h3><p>Poemas, mitos, cuentos y canciones con ritmo y acordes.</p></a>
<a class="card" href="matematicas.html"><h3>Ciencias</h3><p>Matemáticas, física, química, astronomía e informática con ejemplos verificados.</p></a>
<a class="card" href="{proy_href}"><h3>{proy_t}</h3><p>{proy_p}</p></a>
<a class="card" href="pad/index.html"><h3>Owee Pad</h3><p>Escribe en romano y obtén Owee Script al instante.</p></a></div>
<h2>Probar la escritura</h2>
<div class="controls"><input id="t" type="search" value="me suna nume" aria-label="Texto en romano Owee"></div>
<div class="poema"><div class="v"><span class="o" id="tr" style="font-size:2.2rem">me suna nume</span></div></div>
<script>document.getElementById('t').addEventListener('input',function(e){{document.getElementById('tr').textContent=Owee.toScript(e.target.value,{{digits:true}})}});
window.addEventListener('DOMContentLoaded',function(){{document.getElementById('tr').textContent=Owee.toScript(document.getElementById('t').value,{{digits:true}})}});</script>
"""
    page("index.html", "Owee", body, "index.html")

def build_escritura():
    cons = "p b t d k g f s m n l r sh ch".split()
    cells = '<div class="h"></div>' + "".join(f'<div class="h">{v.upper()}</div>' for v in "aeou")
    for c in cons:
        cells += f'<div class="h">{c.upper()}</div>'
        for v in "aeou":
            cells += f'<div>{oweespan(c+v)}<small>{c+v}</small></div>'
    vow = "".join(f'<div>{oweespan(v)}<small>{v}</small></div>' for v in "aeou")
    dig = "".join(f'<div>{oweespan(str(i))}<small>{n} · {i}</small></div>' for i, n in enumerate("cho be du ga fo sa ku mu na she".split()))
    body = f"""<h1>Escritura: Owee Script</h1>
<p>Cada sílaba es un bloque visual, escrito de izquierda a derecha. La consonante es el esqueleto y la vocal es una <em>dirección</em>:
<strong>A</strong> arriba, <strong>E</strong> izquierda, <strong>O</strong> derecha, <strong>U</strong> abajo. Siete familias consonánticas agrupan las 14 consonantes.</p>
<div class="controls"><div class="seg" role="group" aria-label="Fuente"><button data-fam="sans" aria-pressed="true">Owee Sans</button><button data-fam="school" aria-pressed="false">Owee School</button></div></div>
<h2>Vocales</h2><div class="matrix" style="grid-template-columns:repeat(4,1fr)">{vow}</div>
<h2>Matriz de 56 sílabas CV</h2><div class="matrix" id="mx">{cells}</div>
<h2>Marcas de escritura</h2>
<p>Dos glifos permiten <strong>demostrar en la escritura nativa</strong> la estructura de las palabras (principio de una forma = un significado):</p>
<div class="matrix" style="grid-template-columns:repeat(3,1fr);max-width:720px">
<div>{oweespan("sade-kelo")}<small>sade-kelo · compuesto «año» (nexo U+E03C)</small></div>
<div>{oweespan("sade kelo")}<small>sade kelo · frase libre «sol, ciclo» (sin nexo)</small></div>
<div>{oweespan("Ana")}<small>Ana · nombre propio (marca U+E03D)</small></div></div>
<p>Pronunciación de todo lo anterior en la <a href="pronunciacion.html">guía de pronunciación</a>.</p>
<h2>Dígitos</h2><div class="matrix" style="grid-template-columns:repeat(5,1fr)">{dig}</div>
<p>Escalas: <code>tanu</code> 10 · <code>gabu</code> 100 · <code>soku</code> 1 000 · <code>benu</code> 1 000 000. Detalles completos en <a href="idioma.html#parte-v-owee-script">Parte V del Registro Maestro</a>.</p>
<script>document.querySelectorAll('[data-fam]').forEach(function(b){{b.onclick=function(){{
document.querySelectorAll('[data-fam]').forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});
document.querySelectorAll('.matrix .o').forEach(function(n){{n.style.fontFamily=b.dataset.fam==='school'?"'Owee School'":"'Owee Sans'"}})}}}});</script>"""
    page("escritura.html", "Escritura", body, "escritura.html")

def build_idioma():
    h, toc, _ = md(REG.read_text(encoding="utf8"), convert=False)
    t = "".join(f'<a class="l{n}" href="#{i}">{esc(x)}</a>' for n, x, i in toc if n in (1, 2))
    # el primer h1 del registro es el titulo: lo dejamos como esta
    body = f'<div class="layout"><aside class="toc">{t}</aside><article>{h}</article></div>'
    page("idioma.html", "El idioma (Registro Maestro)", body, "idioma.html")

def usage_index(poems):
    use = {}
    for pid, title, lines in poems:
        for ln in lines:
            for tok in re.findall(r"[a-z]+(?:-[a-z]+)*", ln.lower()):
                for root in [tok] + tok.split("-"):
                    use.setdefault(root, {})[pid] = title
    return use

def chipcls(est):
    return {"ESTABLE": "st", "AUDITADO 2.0": "st", "APROBADA": "st", "VERIFICADA": "ver", "PROVISIONAL": "prov", "PROPUESTA": "prov", "REVISAR": "prov"}.get(est, "")

def export_diccionario(ENG):
    """Diccionario completo descargable: TSV y JSON (Owee, sílabas, clase, español, inglés, área, estado, partes)."""
    cols = ["owee", "silabas", "clase", "espanol", "ingles", "area", "estado", "partes"]
    filas = []
    for e in ALL:
        partes = " + ".join(f"{p} ({ALLMAP.get(p, ('',))[0].split(' (')[0]})" for p in e["w"].split("-")) if "-" in e["w"] else ""
        filas.append([e["w"], e["sil"], e["cls"], e["mean"], ENG.get(e["w"], ""), e["dom"], e["est"], partes])
    (OUT / "assets").mkdir(exist_ok=True)
    (OUT / "assets" / "diccionario_owee.tsv").write_text("\t".join(cols) + "\n" + "".join("\t".join(r) + "\n" for r in filas), encoding="utf8")
    (OUT / "assets" / "diccionario_owee.json").write_text(json.dumps([dict(zip(cols, r)) for r in filas], ensure_ascii=False, indent=1), encoding="utf8")

def build_dic(use):
    ENG = {l.split("\t")[0]: l.split("\t")[1] for l in (ROOT / "02_Diccionario/datos/ingles.tsv").read_text(encoding="utf8").splitlines()[1:]}
    secs, order = {}, []
    for e in ALL:
        e["label"] = e["sec"] if e["dom"] == "General" else f'{e["dom"]} · {e["sec"]}'
        secs.setdefault(e["label"], []).append(e)
    for e in ALL:
        parts = e["w"].split("-")
        e["parts"] = parts if len(parts) > 1 else []
    meanings = {}
    html_secs = []
    for sec, es in secs.items():
        cards = []
        for e in es:
            w = e["w"]; u = use.get(w, {})
            links = "".join(f'<a href="literatura.html#{pid}">{esc(t)}</a>, ' for pid, t in u.items()).rstrip(", ")
            comp = ""
            if e["parts"]:
                comp = " · " + " + ".join(f'<a href="#w-{p}">{p}</a>' if p in LEXSET else p for p in e["parts"])
            used = f'<div class="u">Usado en: {links}</div>' if u else '<div class="u">Sin uso aún en los textos</div>'
            pr = pron(w)
            prstr = f'/{pr[0]}/ · {pr[1]}' if pr else ""
            eng = ENG.get(w, "")
            search = (w + " " + e["mean"] + " " + e["cls"] + " " + eng).lower()
            search = "".join(c for c in unicodedata.normalize("NFD", search) if unicodedata.category(c) != "Mn")
            cards.append(
                f'<article class="entry" id="w-{w}" data-s="{esc(search)}" data-est="{e["est"].lower()}" data-used="{1 if u else 0}" data-sec="{esc(sec)}" data-dom="{e["dom"]}" data-w="{w}" data-m="{esc(e["mean"].lower())}">'
                f'<div class="g">{oweespan(w)}</div><div class="w">{w}<small>{prstr}{comp}</small></div>'
                f'<div class="m">{esc(e["mean"])} <span class="chip">{esc(e["cls"])}</span>'
                f'<span class="chip {chipcls(e["est"])}">{esc(e["est"].lower())}</span>'
                f'{"<span class=chip>"+e["dom"]+"</span>" if e["dom"]!="General" else ""}'
                f'{"<div class=u>"+esc(e["nota"])+"</div>" if e["nota"] else ""}</div>{"<div class=u lang=en>EN: "+esc(eng)+"</div>" if eng else ""}{used}</article>')
        html_secs.append(f'<section data-secbox><h2 class="sec">{esc(sec)}</h2><div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(330px,1fr))">{"".join(cards)}</div></section>')
    n_used = sum(1 for e in LEX if e["w"] in use)
    unused = [e["w"] for e in LEX if e["w"] not in use and not e["parts"] and e["sec"] != "Sistema numérico"]
    doms = ["General"] + list(dict.fromkeys(e["dom"] for e in SCI))
    dopts = "".join(f"<option>{d}</option>" for d in doms)
    opts = "".join(f'<option>{esc(s)}</option>' for s in secs)
    body = f"""<h1>Diccionario Owee</h1>
<p>Owee no se traduce palabra por palabra: cada raíz es un <strong>concepto</strong> y su sentido concreto depende de la estructura y del contexto. Incluye el léxico general (Base 1.0), Matemáticas y Física 2.0 y las propuestas de Química, Gramática, Astronomía, Astrología, Mitología, vida diaria e Informática.
<br><strong>Estados:</strong> <em>estable / auditado</em> = ya en el idioma; <em>aprobada</em> = confirmada por el autor; <em>verificada</em> = pasó la verificación automática (fonología V/CV sin i, partes existentes, ≤ 3 elementos, forma y significado únicos) y espera aprobación; <em>por revisar</em> = falló una comprobación.
Las formas con guion se construyen con raíces y operadores existentes (<code>bema-pa</code> = más cantidad).</p>
<p><a href="assets/diccionario_owee.tsv" download>Descargar el diccionario completo (TSV)</a> · <a href="assets/diccionario_owee.json" download>JSON</a> — {len(ALL)} formas con español, inglés, área, estado y partes. Las fichas llevan también el inglés y se pueden buscar en inglés.</p>
<div class="stats"><div><b>{len(LEX)}</b>léxico general</div><div><b>{sum(1 for e in SCI if e['dom'] in ('Matemáticas','Física'))}</b>matemática y física</div>
<div><b>{sum(1 for e in SCI if e['est'] == 'VERIFICADA')}</b>verificadas</div><div><b>{sum(1 for e in SCI if e['est'] == 'APROBADA')}</b>aprobadas</div><div><b>{n_used}</b>usadas en textos</div></div>
<div class="controls"><input id="q" type="search" placeholder="Buscar en Owee o en español (sin acentos)…" aria-label="Buscar">
<select id="fd"><option value="">Todas las áreas</option>{dopts}</select>
<select id="fs"><option value="">Todas las secciones</option>{opts}</select>
<select id="fe"><option value="">Todo estado</option><option value="estable">Estables</option><option value="auditado 2.0">Auditado 2.0 (ciencias)</option><option value="aprobada">Aprobadas</option><option value="verificada">Verificadas (esperan aprobación)</option><option value="provisional">Provisionales</option><option value="propuesta">Propuestas</option><option value="revisar">Por revisar</option></select>
<select id="fu"><option value="">Uso: todas</option><option value="1">Usadas en textos</option><option value="0">Sin usar</option></select>
<div class="seg"><button data-sort="sec" aria-pressed="true">Por tema</button><button data-sort="owee" aria-pressed="false">A–Z Owee</button><button data-sort="es" aria-pressed="false">A–Z español</button></div></div>
<p id="cnt" class="u" style="color:var(--ink2)"></p>
<div id="list">{"".join(html_secs)}</div>
<h2>Formas rechazadas o no establecidas</h2>
<div class="tw"><table><thead><tr><th>Forma</th><th>Estado</th><th>Motivo</th></tr></thead><tbody>
<tr><td><code>sume</code></td><td>rechazada</td><td>No usar como azul; conflicto/proximidad con <code>suma</code>.</td></tr>
<tr><td><code>nare</code></td><td>rechazada</td><td>No usar como atención; <code>paku</code> es la raíz vigente.</td></tr>
<tr><td><code>bure</code> (miedo)</td><td>rechazada</td><td><code>bure</code> ya significa abrir.</td></tr>
<tr><td><code>por</code></td><td>no establecida</td><td>No adoptar como porcentaje sin decisión explícita.</td></tr></tbody></table></div>
<h2>Raíces todavía sin uso en los textos</h2>
<p>Útil para el siguiente poema: estas raíces del léxico aún no aparecen en ningún verso.</p>
<p>{" ".join(f'<a href="#w-{w}">{w}</a>' for w in unused)}</p>"""
    js = """<script>(function(){
var q=document.getElementById('q'),fs=document.getElementById('fs'),fd=document.getElementById('fd'),fe=document.getElementById('fe'),fu=document.getElementById('fu'),list=document.getElementById('list');
var entries=[].slice.call(document.querySelectorAll('.entry')),boxes=[].slice.call(document.querySelectorAll('[data-secbox]'));
var origin=boxes.map(function(b){return b});var flat=null,mode='sec';
function norm(s){return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}
function apply(){var t=norm(q.value.trim()),n=0;
 entries.forEach(function(e){var ok=(!t||e.dataset.s.indexOf(t)>=0)&&(!fd.value||e.dataset.dom===fd.value)&&(!fs.value||e.dataset.sec===fs.value)&&(!fe.value||e.dataset.est===fe.value)&&(!fu.value||e.dataset.used===fu.value);
  e.classList.toggle('hide',!ok);if(ok)n++});
 boxes.forEach(function(b){b.classList.toggle('hide',!b.querySelector('.entry:not(.hide)'))});
 document.getElementById('cnt').textContent=n+' entrada'+(n==1?'':'s')}
function sort(m){mode=m;
 if(m==='sec'){if(flat){flat.remove();flat=null}boxes.forEach(function(b){list.appendChild(b);b.querySelector('.grid').append.apply(b.querySelector('.grid'),entries.filter(function(e){return e.dataset.sec===b.querySelector('h2').textContent}))})}
 else{if(!flat){flat=document.createElement('section');flat.innerHTML='<div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(330px,1fr))"></div>';list.appendChild(flat)}
  boxes.forEach(function(b){b.classList.add('hide')});var g=flat.firstChild;
  entries.slice().sort(function(a,b){var k=m==='owee'?'w':'m';return a.dataset[k].localeCompare(b.dataset[k],'es')}).forEach(function(e){g.appendChild(e)})}
 apply()}
document.querySelectorAll('[data-sort]').forEach(function(b){b.onclick=function(){document.querySelectorAll('[data-sort]').forEach(function(x){x.setAttribute('aria-pressed',x===b)});sort(b.dataset.sort)}});
[q,fd,fs,fe,fu].forEach(function(c){c.addEventListener('input',function(){if(mode!=='sec')boxes.forEach(function(b){b.classList.add('hide')});apply()})});
apply()})();</script>"""
    export_diccionario(ENG)
    page("diccionario.html", "Diccionario", body, "diccionario.html", extra_js=js)

def build_lit(html_body, toc, imprimir=False):
    t = "".join(f'<a class="l{n}" href="#{i}">{esc(x)}</a>' for n, x, i in toc if n in (2, 3))
    ctrl = ('<div class="controls"><span style="color:var(--ink2)">Ver versos como:</span><div class="seg" role="group">'
            '<button data-setmode="ambos">Glifos + romano</button><button data-setmode="glifos">Solo glifos</button><button data-setmode="romano">Solo romano</button></div>'
            '<button class="seg" style="font:inherit;padding:7px 12px;cursor:pointer;background:var(--surface);color:var(--ink)" onclick="print()">Imprimir / PDF</button></div>')
    if imprimir:
        cover = ('<section class="cover"><div class="o" data-o="owee" style="font-size:5rem;color:#2F6FB0">owee</div><h1>Literatura y Poesía</h1>'
                 '<p>Poemas, canciones, mitos, dioses y cuentos, con reglas métricas y musicales.</p><p>Versión 0.4 · Owee Sans / Owee School</p></section>')
        css = """<style>@page{size:A4;margin:16mm 15mm}body{font-size:11pt}.cover{min-height:240mm;display:flex;flex-direction:column;justify-content:center;gap:6mm;break-after:page}
.poema{max-width:none}.poema .v .o{font-size:21pt}h2{break-after:avoid}h3{break-after:avoid}.o{font-size:15pt}td .o{font-size:14pt}</style>"""
        page("literatura-imprimir.html", "Literatura y Poesía (impresión)", cover + html_body, extra_head=css, chrome=False, body_attrs='data-forcemode="ambos"')
        return
    body = f'{ctrl}<div class="layout"><aside class="toc">{t}</aside><article>{html_body}</article></div>'
    page("literatura.html", "Literatura y poesía", body, "literatura.html")

GUIAS = [
    # (archivo, titulo, md, aviso_borrador, pdf_imprimible, activo_nav)
    ("matematicas.html", "Matemáticas", ROOT / "03_Material_Ensenanza/Matematicas/Owee_Matematicas_2.0_Web.md", None, False),
    ("fisica.html", "Física", ROOT / "03_Material_Ensenanza/Fisica/Owee_Fisica_2.0_Web.md", None, False),
    ("quimica.html", "Química", ROOT / "03_Material_Ensenanza/Quimica/Owee_Quimica_0.1_Borrador.md",
     "Material nuevo, sin raíces nuevas. Los términos están verificados automáticamente; ninguno aprobado todavía.", True),
    ("astronomia.html", "Astronomía y astrología", ROOT / "03_Material_Ensenanza/Astronomia/Owee_Astronomia_0.1_Borrador.md",
     "Material nuevo, sin raíces nuevas. Todos los términos están VERIFICADOS automáticamente; faltan tu aprobación.", False),
    ("curso.html", "Curso por niveles", ROOT / "03_Material_Ensenanza/Curso/Owee_Curso_Indice.md", None, False),
    ("nivel-0.html", "Nivel 0 — Ver y oír", ROOT / "03_Material_Ensenanza/Curso/Owee_Curso_Nivel_0.md", None, False),
    ("nivel-1.html", "Nivel 1 — Primeras frases (A1)", ROOT / "03_Material_Ensenanza/Curso/Owee_Curso_Nivel_1.md", None, False),
    ("nivel-2.html", "Nivel 2 — Conversar (A2)", ROOT / "03_Material_Ensenanza/Curso/Owee_Curso_Nivel_2.md", None, False),
    ("nivel-3.html", "Nivel 3 — Leer y crear (B1)", ROOT / "03_Material_Ensenanza/Curso/Owee_Curso_Nivel_3.md", None, False),
    ("informatica.html", "Informática", ROOT / "03_Material_Ensenanza/Informatica/Owee_Informatica_0.1_Borrador.md",
     "Material nuevo con una sola raíz nueva (bomo, «bug»); el resto son compuestos. Términos aprobados.", False),
    ("pronunciacion.html", "Pronunciación", ROOT / "03_Material_Ensenanza/Pronunciacion/Owee_Pronunciacion_1.0.md", None, True),
    ("gramatica.html", "Gramática 1.1", ROOT / "03_Material_Ensenanza/Gramatica/Owee_Gramatica_1.1_Propuesta.md",
     "Propuesta que completa el Registro Maestro; nada está aprobado hasta que lo confirmes.", False),
]

def build_ciencias():
    for fname, nombre, path, borrador, pdf in GUIAS:
        h, toc, _ = md(expand(path.read_text(encoding="utf8")))
        t = "".join(f'<a class="l{n}" href="#{i}">{esc(x)}</a>' for n, x, i in toc if n == 2)
        aviso = f'<blockquote><p><strong>Borrador propuesto.</strong> {borrador}</p></blockquote>' if borrador else ""
        extra = f'<p class="noprint"><a href="documentos/{path.with_suffix(".pdf").name}">Descargar PDF imprimible</a></p>' if pdf else ""
        body = f'<div class="layout"><aside class="toc">{t}</aside><article>{aviso}{h}{extra}</article></div>'
        page(fname, nombre, body, "curso.html" if fname.startswith("nivel-") else fname)
        if pdf:
            css = "<style>@page{size:A4;margin:16mm 15mm}body{font-size:11pt}.o{font-size:14pt}td .o{font-size:13pt}</style>"
            page(fname.replace(".html", "-imprimir.html"), nombre + " (impresión)", aviso + h, extra_head=css, chrome=False)

def build_plan():
    h, toc, _ = md((ROOT / "00_Registro_Maestro/Owee_Plan_de_Ampliacion.md").read_text(encoding="utf8"), convert=False)
    t = "".join(f'<a class="l{n}" href="#{i}">{esc(x)}</a>' for n, x, i in toc if n == 2)
    page("plan.html", "Plan de ampliación", f'<div class="layout"><aside class="toc">{t}</aside><article>{h}</article></div>', "plan.html")

def build_integracion():
    h, toc, _ = md((ROOT / "08_Integracion/README.md").read_text(encoding="utf8"), convert=False)
    t = "".join(f'<a class="l{n}" href="#{i}">{esc(x)}</a>' for n, x, i in toc if n == 2)
    page("integracion.html", "Integración (oweelinux y web)", f'<div class="layout"><aside class="toc">{t}</aside><article>{h}</article></div>', "integracion.html")

def build_revision():
    h, toc, _ = md((ROOT / "02_Diccionario/datos/revision_semantica.md").read_text(encoding="utf8"), convert=True)
    page("revision.html", "Revisión semántica de términos", f'<article>{h}</article>', "revision.html")

def build_traductor():
    cl = {e["w"]: e["cls"] for e in ALL}
    en = {l.split("\t")[0]: l.split("\t")[1] for l in (ROOT / "02_Diccionario/datos/ingles.tsv").read_text(encoding="utf8").splitlines()[1:]}
    lex = {w: [m, (pron(w)[1] if pron(w) else ""), cl.get(w, ""), en.get(w, "")] for w, (m, pr) in ALLMAP.items()}
    (OUT / "assets" / "lexico.js").write_text("window.OWEE_LEX=" + json.dumps(lex, ensure_ascii=False) + ";", encoding="utf8")
    shutil.copy2(Path(__file__).resolve().parent / "traductor.js", OUT / "assets/traductor.js")
    body = """<h1>Traductor asistido Owee ⇄ español</h1>
<p><strong>Prototipo.</strong> Traduce <em>palabra por palabra</em> con el diccionario (tiene {n} formas), separa los compuestos, reconoce <code>pe/te/pu</code>, <code>no</code> y <code>ka</code>, y propone una lectura aproximada. El inglés se obtiene <strong>por pivote</strong>: cada forma Owee tiene su significado en español y de ahí su glosa en inglés (<code>ingles.tsv</code>). No resuelve ambigüedades: el contexto lo pones tú. Todo ocurre en tu navegador.</p>
<div class="controls"><div class="seg" role="group"><button data-dir="oe" aria-pressed="true">Owee → español</button><button data-dir="eo" aria-pressed="false">Español → Owee</button><button data-dir="oi" aria-pressed="false">Owee → English</button><button data-dir="io" aria-pressed="false">English → Owee</button></div></div>
<textarea id="entrada" rows="4" style="width:100%;font:1.2rem/1.5 system-ui;padding:12px;border:1px solid var(--rule);border-radius:10px;background:var(--surface);color:var(--ink)" aria-label="Texto de entrada">me suna nume</textarea>
<div id="resultado"></div>
<h2>Ejemplos</h2><p class="noprint" id="ej"></p>
<script src="assets/lexico.js"></script><script src="assets/traductor.js"></script>
<script>(function(){{
var dir='oe',ent=document.getElementById('entrada'),res=document.getElementById('resultado');
function esc(s){{return String(s).replace(/[&<>]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c]}})}}
function fila(o,t,ok){{return '<tr><td><span class="o">'+(window.Owee?Owee.toScript(o):o)+'</span><br><small class="rm">'+esc(o)+'</small></td><td'+(ok?'':' style="color:var(--warn)"')+'>'+esc(t)+'</td></tr>'}}
function pinta(){{var t=ent.value,h='';
 if(dir==='oe'||dir==='oi'){{(dir==='oe'?OweeTraductor.owee2es(t):OweeTraductor.owee2en(t)).forEach(function(f){{
  h+='<div class="poema"><div class="v"><span class="o">'+(window.Owee?Owee.toScript(f.frase):f.frase)+'</span><small class="r">'+esc(f.frase)+'</small></div>'
   +'<p><strong>Lectura aproximada:</strong> '+esc(f.aproximada)+'</p>'
   +'<div class="tw"><table><thead><tr><th>Owee</th><th>'+(dir==='oi'?'Meaning':'Significado')+'</th></tr></thead><tbody>'+f.palabras.map(function(p){{return fila(p.owee,p.es,p.ok)}}).join('')+'</tbody></table></div></div>'}})}}
 else{{(dir==='eo'?OweeTraductor.es2owee(t):OweeTraductor.en2owee(t)).forEach(function(f){{
  h+='<div class="poema"><p><strong>«'+esc(f.frase)+'»</strong></p><div class="v"><span class="o">'+(window.Owee?Owee.toScript(f.sugerencia):f.sugerencia)+'</span><small class="r">'+esc(f.sugerencia)+'</small></div>'
   +'<div class="tw"><table><thead><tr><th>Español</th><th>Owee (candidatas)</th></tr></thead><tbody>'+f.palabras.map(function(p){{return '<tr><td>'+esc(p.es)+'</td><td'+(p.ok?'':' style="color:var(--warn)"')+'>'+esc(p.owee)+'</td></tr>'}}).join('')+'</tbody></table></div>'
   +'<p><small>Revisa la sugerencia: Owee no usa artículos ni conjugación; el tiempo se marca con <code>pe</code> / <code>pu</code>.</small></p></div>'}})}}
 res.innerHTML=h}}
ent.addEventListener('input',pinta);
document.querySelectorAll('[data-dir]').forEach(function(b){{b.onclick=function(){{dir=b.dataset.dir;document.querySelectorAll('[data-dir]').forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});
 ent.value={{oe:'me suna nume',eo:'Yo quiero agua',oi:'me pe fame pume',io:'I want water'}}[dir];pinta()}}}});
var EJ={{oe:['me pe fame pume','tu kuma bo mora ka','ra fame no pume','te-loda-kelo me daro'],eo:['Hoy trabajo','Ayer comí fruta','No quiero comer','Mañana voy a la ciudad'],oi:['me suna nume','ra pe sule','tu fame pume ka'],io:['I want water','She does not eat food','Tomorrow I will go to the city']}};
document.getElementById('ej').innerHTML=['oe','eo','oi','io'].map(function(k){{return EJ[k].map(function(x){{return '<button class="btn" data-x="'+k+'|'+x+'">'+x+'</button>'}}).join(' ')}}).join(' ');
document.getElementById('ej').addEventListener('click',function(e){{var d=e.target.dataset.x;if(!d)return;var a=d.split('|');dir=a[0];ent.value=a[1];
 document.querySelectorAll('[data-dir]').forEach(function(x){{x.setAttribute('aria-pressed',x.dataset.dir===dir)}});pinta()}});
window.addEventListener('load',pinta);
}})();</script>""".replace("{n}", str(len(ALLMAP))).replace("{{", "{").replace("}}", "}")
    page("traductor.html", "Traductor asistido", body, "traductor.html")

def build_calculadora():
    shutil.copy2(Path(__file__).resolve().parent / "calculadora.js", OUT / "assets/calculadora.js")
    head = """<style>
.calc{display:grid;grid-template-columns:minmax(280px,360px) 1fr;gap:24px;align-items:start}
@media(max-width:760px){.calc{grid-template-columns:1fr}}
.calc .pad{background:var(--surface);border:1px solid var(--rule);border-radius:14px;padding:14px}
.calc .pant{background:var(--soft);border-radius:10px;padding:10px 14px;min-height:5.4rem;text-align:right;overflow-x:auto}
.calc .pant .ex{font-size:1.1rem;color:var(--ink2);min-height:1.6rem;white-space:nowrap}
.calc .pant .re{font-size:2.2rem;line-height:1.3;white-space:nowrap}
.calc .teclas{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:12px}
.calc .teclas button{font:inherit;border:1px solid var(--rule);background:var(--surface);color:var(--ink);border-radius:10px;padding:8px 0 4px;cursor:pointer;min-height:3.4rem;line-height:1.1}
.calc .teclas button:hover{background:var(--soft)}.calc .teclas button.op{background:var(--soft)}.calc .teclas button.ig{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.calc .teclas .o{font-size:1.7rem;display:block}.calc .teclas small{display:block;font-size:.7rem;color:var(--ink2)}.calc .teclas .ig small{color:var(--accent-ink)}
.cv input{width:100%;font:1.3rem/1.4 system-ui;padding:10px 12px;border:1px solid var(--rule);border-radius:10px;background:var(--surface);color:var(--ink)}
.cv .o{font-size:1.9rem}.cv .big2{font-size:2.6rem;line-height:1.3}
</style>"""
    teclas = ""
    for k in ["C", "(", ")", "\u00f7", "7", "8", "9", "\u00d7", "4", "5", "6", "\u2212", "1", "2", "3", "+", "0", ".", "\u232b", "="]:
        if k.isdigit():
            teclas += f'<button data-k="{k}" aria-label="{k}"><span class="o">{chr(0xE040 + int(k))}</span><small>{NOMBRES[int(k)]}</small></button>'
        else:
            nm = {"+": "dapa", "\u2212": "dopo", "\u00d7": "kebu", "\u00f7": "faku", "=": "se", ".": "doto"}.get(k, "")
            cls = "ig" if k == "=" else ("op" if k in "+\u2212\u00d7\u00f7" else "")
            teclas += f'<button class="{cls}" data-k="{k}"><span style="font-size:1.4rem">{k}</span><small>{nm}</small></button>'
    body = """<h1>Calculadora de números Owee</h1>
<p>Calcula con las cifras de Owee Script y lee el resultado en voz alta. Convierte entre las cifras Owee y los números normales. Reglas: <code>coeficiente + escala</code> (<code>tanu</code> 10, <code>gabu</code> 100, <code>soku</code> 1 000, <code>benu</code> 1 000 000), las posiciones con 0 no se leen y la coma decimal es <code>doto</code>. Todo ocurre en tu navegador.</p>
<div class="calc">
<div class="pad" aria-label="Calculadora"><div class="pant"><div class="ex" id="cx"></div><div class="re" id="cr"><span class="o">\ue040</span></div></div>
<div class="teclas">""" + teclas + """</div></div>
<div><div class="poema" id="cl"><p><strong>Se lee:</strong></p><div class="v" id="cls"></div><p id="clr"></p><p id="cro"></p></div>
<p class="noprint"><small>Puedes escribir con el teclado: cifras, <code>+ − × ÷</code>, paréntesis, Enter (=), Retroceso y Escape (C).</small></p></div></div>
<h2>Convertidor</h2>
<p>Escribe un <strong>número normal</strong> (<code>2026</code>), <strong>cifras Owee</strong> (pégalas o escríbelas con el teclado Owee) o la <strong>lectura Owee</strong> (<code>du soku du tanu ku</code>) y verás las tres formas.</p>
<div class="cv"><input id="cin" value="2026" aria-label="Número normal, cifras Owee o lectura Owee" autocomplete="off" spellcheck="false">
<div class="poema" id="cout" style="margin-top:14px"></div></div>
<p class="noprint" id="cej"></p>
<h2>Cómo se lee</h2>
<div class="tw"><table><thead><tr><th>Cifra</th><th>Owee</th><th>Cifra</th><th>Owee</th></tr></thead><tbody>""" + "".join(
        f'<tr><td><span class="o">{chr(0xE040+i)}</span> {i}</td><td><code>{NOMBRES[i]}</code></td><td><span class="o">{chr(0xE040+i+5)}</span> {i+5}</td><td><code>{NOMBRES[i+5]}</code></td></tr>' for i in range(5)) + """</tbody></table></div>
<script src="assets/calculadora.js"></script>
<script>(function(){
var C=OweeCalc,ex='',res=null,cx=document.getElementById('cx'),cr=document.getElementById('cr');
function sc(t){return window.Owee?Owee.toScript(t):t}
function esc(s){return String(s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function lectura(t,id){var h='<span class="o">'+sc(t)+'</span><br><small class="rm">'+esc(t)+'</small>';document.getElementById(id).innerHTML=h}
function muestra(){
 cx.innerHTML=ex?'<span class="o">'+C.glifos(ex).replace(/[+\u2212\u00d7\u00f7()]/g,function(c){return '</span> '+c+' <span class="o">'})+'</span>':'';
 var cur=res!==null?res:(ex.match(/\d+\.?\d*$/)||['0'])[0];
 cr.innerHTML='<span class="o">'+C.glifos(String(cur))+'</span>';
 var txt=res!==null?C.leerValor(+res):C.leerExpr(ex);
 document.getElementById('cls').innerHTML=txt?'<span class="o">'+sc(txt)+'</span><br><small class="rm">'+esc(txt)+'</small>':'<small>Escribe una operación.</small>';
 document.getElementById('clr').innerHTML=res!==null?'<strong>Resultado:</strong> '+esc(+(+res).toFixed(8)):'';
 document.getElementById('cro').innerHTML=res!==null?'<strong>Cifras Owee:</strong> <span class="o">'+C.glifos(String(+(+res).toFixed(8)))+'</span>':'';
}
function tecla(k){
 if(res!==null&&/[0-9.(]/.test(k))ex='';
 if(res!==null&&/[+\u2212\u00d7\u00f7]/.test(k)){ex=String(+(+res).toFixed(8));}
 if(k!=='='){res=null}
 if(k==='C'){ex='';res=null}
 else if(k==='\u232b'){ex=ex.slice(0,-1)}
 else if(k==='='){var v=C.evaluar(ex);if(isNaN(v)||!isFinite(v)){cr.innerHTML='<small>Operación no válida</small>';return}res=+v.toFixed(8)}
 else if(k==='.'){if(/\d+\.\d*$/.test(ex))return;ex+=(/\d$/.test(ex)?'.':'0.')}
 else ex+=k;
 muestra();
}
document.querySelectorAll('.teclas button').forEach(function(b){b.onclick=function(){tecla(b.dataset.k)}});
document.addEventListener('keydown',function(e){
 if(e.target.tagName==='INPUT'||e.ctrlKey||e.metaKey||e.altKey)return;
 var k=e.key,m={'*':'\u00d7','/':'\u00f7','-':'\u2212',Enter:'=',Backspace:'\u232b',Escape:'C',',':'.'};
 if(m[k])k=m[k];
 if(/^[0-9+()=.\u00d7\u00f7\u2212\u232bC]$/.test(k)){e.preventDefault();tecla(k)}
});
var cin=document.getElementById('cin'),cout=document.getElementById('cout');
function conv(){
 var t=cin.value.trim(),n=null,modo='';
 var tn=C.normales(t);
 if(/^\d+(\.\d+)?$/.test(tn)){n=parseFloat(tn);modo=tn===t?'número normal':'cifras Owee'}
 else {n=C.leerOwee(t);modo='lectura Owee'}
 if(n===null||isNaN(n)||Math.abs(n)>=1e9){cout.innerHTML='<p style="color:var(--warn)">No reconozco «'+esc(t)+'». Prueba con un número (2026), cifras Owee o una lectura como <code>be soku ga gabu</code>.</p>';return}
 var lee=C.leerValor(n);
 cout.innerHTML='<p><small>Entendido como '+modo+'</small></p>'
  +'<div class="v"><span class="big2 o">'+C.glifos(String(n))+'</span></div>'
  +'<p><strong>Número normal:</strong> '+n+'</p>'
  +'<p><strong>Lectura Owee:</strong></p><div class="v"><span class="o">'+sc(lee)+'</span><br><small class="rm">'+esc(lee)+'</small></div>'
  ;
}
cin.addEventListener('input',conv);
var EJ=['25','2026','1994','70712345','be soku ga gabu','du tanu sa doto sa cho'];
document.getElementById('cej').innerHTML=EJ.map(function(x){return '<button class="btn" data-x="'+esc(x)+'">'+esc(x)+'</button>'}).join(' ');
document.getElementById('cej').addEventListener('click',function(e){var d=e.target.dataset.x;if(d){cin.value=d;conv()}});
window.addEventListener('load',function(){muestra();conv()});
})();</script>"""
    page("calculadora.html", "Calculadora de números", body, "calculadora.html", extra_head=head)

def build_teclado():
    d = OUT / "teclado"; d.mkdir(exist_ok=True)
    dist = ROOT / "05_Teclado_IME/keyman-owee/dist"
    for f in ("Owee.kmp", "owee.js", "owee.kmx"):
        shutil.copy2(dist / f, d / f)
    body = """<h1>Teclado Owee</h1>
<p>Escribe en <strong>romano</strong> y obtén la escritura <strong>Owee Script</strong>. Funciona en Windows, Android, iPhone, macOS, Linux y navegadores con <a href="https://keyman.com">Keyman</a>, y en Linux también con el IME <code>fcitx5-owee</code>.</p>
<h2>Pruébalo aquí</h2>
<p>Escribe <code>suna</code>, <code>sade-kelo</code>, <code>Ana</code>, <code>shome</code> o una cifra (<code>2026</code>).</p>
<textarea id="kt" rows="4" class="o" style="width:100%;font-size:1.8rem;line-height:1.5;padding:12px;border:1px solid var(--rule);border-radius:10px;background:var(--surface);color:var(--ink)" aria-label="Escribe aquí en romano" placeholder="me suna nume"></textarea>
<p id="kmsg"><small>Cargando el teclado… (necesita conexión para el motor KeymanWeb)</small></p>
<p class="noprint"><button class="btn" id="kosk">Mostrar teclado en pantalla</button></p>
<h2>Descargar</h2>
<div class="dl"><a href="teclado/Owee.kmp">Owee.kmp<span>Paquete Keyman (Windows, Android, iOS, macOS)</span></a><a href="teclado/owee.js">owee.js<span>Teclado para KeymanWeb (tu propia página)</span></a></div>
<h2>Instalar</h2>
<div class="tw"><table><thead><tr><th>Sistema</th><th>Pasos</th></tr></thead><tbody>
<tr><td><strong>Windows</strong></td><td>Instala <a href="https://keyman.com/windows">Keyman para Windows</a>, descarga <code>Owee.kmp</code> y ábrelo con doble clic. Instala también la fuente Owee Sans.</td></tr>
<tr><td><strong>Android</strong></td><td>Instala <a href="https://keyman.com/android">Keyman para Android</a>, copia <code>Owee.kmp</code> al teléfono y ábrelo desde Keyman («Instalar teclado desde archivo»). Activa Keyman como teclado.</td></tr>
<tr><td><strong>iPhone / iPad / macOS</strong></td><td>Instala Keyman para <a href="https://keyman.com/iphone-and-ipad">iOS</a> o <a href="https://keyman.com/mac">macOS</a> e importa <code>Owee.kmp</code>.</td></tr>
<tr><td><strong>Linux</strong></td><td>Keyman para Linux con <code>Owee.kmp</code>, o el paquete <code>fcitx5-owee</code> (ver Integración).</td></tr>
<tr><td><strong>Navegadores</strong></td><td>La caja de arriba usa KeymanWeb. Para tu propia web, carga KeymanWeb y <code>teclado/owee.js</code>.</td></tr>
</tbody></table></div>
<h2>Probar en tu Android, paso a paso</h2>
<ol>
<li>Instala <strong>Keyman</strong> desde Google Play.</li>
<li>Desde el navegador del teléfono abre esta página y toca <a href="teclado/Owee.kmp">Owee.kmp</a> para descargarlo.</li>
<li>Abre el archivo descargado y elige <strong>Keyman</strong> (o, dentro de Keyman: <em>Ajustes → Instalar teclado o diccionario → Desde archivo</em>). Acepta instalar «Owee».</li>
<li>En Keyman sigue los dos pasos: <em>Activar Keyman como teclado del sistema</em> y <em>Elegir Keyman como teclado actual</em>.</li>
<li>Abre cualquier caja de texto, pulsa el icono del globo y elige <strong>Owee</strong>. Escribe <code>suna</code>.</li>
</ol>
<p><strong>Límite en Android:</strong> los glifos son caracteres de la fuente Owee Sans y Android no permite instalar fuentes en todo el sistema sin permisos especiales. Por eso el texto se verá bien en el <strong>editor de Keyman</strong> y en el <strong>navegador</strong> (esta web carga la fuente), pero en otras aplicaciones (WhatsApp, notas…) puede verse como cuadros vacíos. En Windows y macOS, Keyman sí instala la fuente y se ve en todas partes.</p>
<h2>Cómo escribir</h2>
<div class="tw"><table><thead><tr><th>Escribes</th><th>Resultado</th></tr></thead><tbody>
<tr><td><code>su</code> + <code>na</code></td><td>los glifos de <em>suna</em> (cada sílaba al escribir la vocal)</td></tr>
<tr><td><code>sh</code>, <code>ch</code></td><td>una sola consonante (<em>shome</em>, <em>chuko</em>)</td></tr>
<tr><td><code>sade-kelo</code></td><td>el guion tras una sílaba pone el nexo de compuesto</td></tr>
<tr><td><code>Ana</code></td><td>mayúscula inicial: marca de nombre propio + glifos</td></tr>
<tr><td><code>0</code>–<code>9</code></td><td>cifras Owee; <code>AltGr</code> + cifra escribe la cifra normal</td></tr>
<tr><td>consonante sin vocal</td><td>queda en romano, no se pierde texto</td></tr>
</tbody></table></div>
<script src="https://s.keyman.com/kmw/engine/18.0.253/keymanweb.js"></script>
<script>(function(){
var msg=document.getElementById('kmsg'),ta=document.getElementById('kt');
if(!window.keyman){msg.innerHTML='<small>No se pudo cargar KeymanWeb (¿sin conexión?). Descarga el paquete para instalar el teclado.</small>';return}
keyman.init({attachType:'manual',ui:'none'}).then(function(){
 keyman.attachToControl(ta);
 return keyman.addKeyboards({id:'owee',name:'Owee',languages:{id:'qow',name:'Owee'},filename:'teclado/owee.js'});
}).then(function(){return keyman.setActiveKeyboard('Keyboard_owee','qow')}).then(function(){
 msg.innerHTML='<small>Teclado Owee activo. Escribe en romano.</small>';
 document.getElementById('kosk').onclick=function(){ta.focus();keyman.osk.show(true)};
}).catch(function(e){msg.innerHTML='<small>No se pudo activar el teclado: '+e+'</small>'});
})();</script>"""
    page("teclado.html", "Teclado Owee", body, "teclado.html")

def build_nombres():
    filas = [l.split("\t") for l in (ROOT / "02_Diccionario/datos/nombres_propios.tsv").read_text(encoding="utf8").splitlines()[1:]]
    por = {}
    for o, ow, t in filas: por.setdefault(t, []).append((o, ow))
    tit = {"país": "Países", "continente": "Continentes", "ciudad": "Ciudades de Bolivia", "lugar": "Lugares", "persona": "Nombres de persona"}
    sec = ""
    for t in ("país", "continente", "ciudad", "lugar", "persona"):
        if t not in por: continue
        f = "".join(f'<tr><td>{esc(o)}</td><td>{verso_html(ow)}</td></tr>' for o, ow in por[t])
        sec += f'<h2>{tit[t]}</h2><div class="tw"><table><thead><tr><th>En español</th><th>En Owee</th></tr></thead><tbody>{f}</tbody></table></div>'
    body = ("<h1>Nombres propios en Owee</h1><p>Owee no tiene <code>i</code>, <code>v</code>, <code>h</code>, <code>y</code>, <code>z</code>, <code>j</code>, <code>c</code>, <code>q</code>, <code>w</code>, <code>x</code> ni consonantes finales, así que los nombres se <strong>adaptan por el sonido</strong>: "
            "<code>i</code> → <code>e</code>, <code>v</code> → <code>b</code>, <code>z</code>/<code>c</code> suave → <code>s</code>, <code>j</code> → <code>k</code>, <code>h</code> no se escribe, y a la consonante final o al grupo se le añade una <strong>vocal de eco</strong> (la anterior). "
            "El acento va en la primera sílaba y el nombre se escribe con <strong>inicial mayúscula</strong> (en Owee Script lleva la marca de nombre, los dos puntos), así nunca se confunde con una palabra común. Pulsa ▶ para escuchar.</p>"
            + sec + "<p><small>Generados con <code>02_Diccionario/datos/adaptar_nombre.py</code>: prueba cualquier nombre con <code>python3 adaptar_nombre.py Rosa Miguel</code>.</small></p>")
    page("nombres.html", "Nombres propios", body, "nombres.html")

def build_estado():
    for doc, fname, titulo in (("Owee_Estado_y_Pendientes.md", "estado.html", "Estado y pendientes"),
                               ("Owee_Auditoria_y_Hoja_de_Ruta.md", "auditoria.html", "Auditoría inicial (histórica)")):
        h, toc, _ = md((ROOT / "00_Registro_Maestro" / doc).read_text(encoding="utf8"), convert=False)
        t = "".join(f'<a class="l{n}" href="#{i}">{esc(x)}</a>' for n, x, i in toc if n == 2)
        page(fname, titulo, f'<div class="layout"><aside class="toc">{t}</aside><article>{h}</article></div>', fname)

def build_descargas():
    D = OUT / "documentos"; D.mkdir(exist_ok=True)
    def sz(p): return f"{p.stat().st_size/1024:.0f} KB"
    groups = [
        ("Especificación", ROOT / "01_Especificacion", "*.pdf"),
        ("Diccionario", ROOT / "02_Diccionario", "*.pdf"),
        ("Lectura y escritura", ROOT / "03_Material_Ensenanza/Lectura_Escritura", "*.pdf"),
        ("Matemáticas", ROOT / "03_Material_Ensenanza/Matematicas", "*.pdf"),
        ("Física", ROOT / "03_Material_Ensenanza/Fisica", "*.pdf"),
    ]
    sections, npdf = [], 0
    for name, d, pat in groups:
        links = []
        for f in sorted(d.glob(pat)):
            shutil.copy2(f, D / f.name); npdf += 1
            links.append(f'<a href="documentos/{f.name}">{esc(f.stem.replace("_", " "))}<span>PDF · {sz(f)}</span></a>')
        sections.append(f"<h3>{name}</h3><div class='dl'>{''.join(links)}</div>")
    pro = ROOT / "03_Material_Ensenanza/Pronunciacion/Owee_Pronunciacion_1.0.pdf"
    if pro.exists():
        shutil.copy2(pro, D / pro.name); npdf += 1
        sections.insert(0, f"<h3>Pronunciación</h3><div class='dl'><a href='documentos/{pro.name}'>Owee — guía de pronunciación<span>PDF · {sz(pro)}</span></a></div>")
    qui = ROOT / "03_Material_Ensenanza/Quimica/Owee_Quimica_0.1_Borrador.pdf"
    if qui.exists():
        shutil.copy2(qui, D / qui.name); npdf += 1
        sections.append(f"<h3>Química (borrador propuesto)</h3><div class='dl'><a href='documentos/{qui.name}'>Owee Química 0.1 — borrador<span>PDF · {sz(qui)}</span></a></div>")
    lit = LIT.with_suffix(".pdf")
    if lit.exists():
        shutil.copy2(lit, D / lit.name)
        sections.insert(0, f"<h3>Literatura y poesía</h3><div class='dl'><a href='documentos/{lit.name}'>Owee Literatura y Poesía<span>PDF · {sz(lit)}</span></a></div>"); npdf += 1
    aud = ROOT / "03_Material_Ensenanza/Literatura_Poesia/audio"
    if aud.exists():
        (D / "audio").mkdir(exist_ok=True)
        al = []
        for f in sorted(aud.glob("*")):
            shutil.copy2(f, D / "audio" / f.name)
            al.append(f"<a href='documentos/audio/{f.name}'>{f.stem.replace('_', ' ')} ({f.suffix[1:].upper()})<span>{sz(f)}</span></a>")
        sections.insert(0, "<h3>Canciones: bocetos de ritmo y acento (sin voz)</h3><p>Compara <em>doma bo romance</em> con <em>doma bo marcha</em>: misma letra, distinto acento musical.</p><div class='dl'>" + "".join(al) + "</div>")
    debs = ROOT / "08_Integracion/linux/dist"
    if debs.exists() and list(debs.glob("*.deb")):
        (D / "linux").mkdir(exist_ok=True)
        dl = []
        for f in sorted(debs.glob("*.deb")):
            shutil.copy2(f, D / "linux" / f.name); dl.append(f"<a href='documentos/linux/{f.name}'>{f.name}<span>DEB · {sz(f)}</span></a>")
        sections.insert(0, "<h3>oweelinux: paquetes .deb (fuentes, teclado y locale)</h3><p>Instalación en el repositorio de GitHub (carpeta <code>08_Integracion</code>).</p><div class='dl'>" + "".join(dl) + "</div>")
    F = OUT / "fuentes"; F.mkdir(exist_ok=True)
    fl = []
    for f in sorted((GM / "fonts/ttf").glob("*.ttf")) + sorted((GM / "fonts/otf").glob("*.otf")) + sorted((GM / "fonts/woff2").glob("*.woff2")):
        shutil.copy2(f, F / f.name); fl.append(f'<a href="fuentes/{f.name}">{f.name}<span>{sz(f)}</span></a>')
    body = f"""<h1>Descargas</h1>
<h2>Fuentes</h2><p><strong>Owee Sans</strong> (pantalla y documentos) y <strong>Owee School</strong> (escritura a mano). Linux: copiar los <code>.ttf</code> a <code>~/.local/share/fonts/Owee/</code> y ejecutar <code>fc-cache -f</code>.</p>
<div class="dl">{''.join(fl)}</div>
<h2>Teclado</h2><div class="dl"><a href="teclado/Owee.kmp">Owee.kmp — teclado Keyman<span>Windows, Android, iOS, macOS</span></a><a href="teclado.html">Teclado Owee: instalar y probar<span>página con instrucciones</span></a></div>
<p>Alternativa sin instalar nada: <a href="pad/index.html">Owee Pad</a>. Para Linux (Fcitx5) está el paquete <code>fcitx5-owee</code> en el repositorio de GitHub.</p>
<h2>Documentos</h2>{''.join(sections)}"""
    page("descargas.html", "Descargas", body, "descargas.html")
    return npdf

# ---------------------------------------------------------------- main
def main():
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT / "assets/fonts").mkdir(parents=True)
    for f in (GM / "package/fonts").iterdir(): shutil.copy2(f, OUT / "assets/fonts" / f.name)
    for n in ("owee.css", "owee.js", "owee-glyph-map.json"): shutil.copy2(GM / "package" / n, OUT / "assets" / n)
    shutil.copytree(GM / "web", OUT / "pad")
    lit_html, lit_toc, poems = md(LIT.read_text(encoding="utf8"))
    use = usage_index(poems)
    npdf = build_descargas()
    build_index(dict(n=len(LEX), sci=len(SCI), poems=len(poems), pdfs=npdf))
    build_escritura(); build_dic(use); build_ciencias(); build_traductor(); build_calculadora(); build_teclado(); build_nombres()
    if not PUBLICO: build_idioma(); build_estado(); build_plan(); build_integracion(); build_revision()
    build_lit(lit_html, lit_toc); build_lit(lit_html, lit_toc, imprimir=True)
    aud = ROOT / "03_Material_Ensenanza/Pronunciacion/audio"
    idx = {}
    if (aud / "indice.json").exists():
        idx = json.loads((aud / "indice.json").read_text(encoding="utf8"))
        shutil.copytree(aud, OUT / "audio", ignore=shutil.ignore_patterns("indice.json"))
    hum = ROOT / "03_Material_Ensenanza/Pronunciacion/audio_humano"      # grabaciones humanas: reemplazan a la voz sintetica
    if (hum / "indice.json").exists():
        (OUT / "audio").mkdir(exist_ok=True)
        for t, f in json.loads((hum / "indice.json").read_text(encoding="utf8")).items():
            if (hum / f).exists():
                shutil.copy2(hum / f, OUT / "audio" / ("h_" + f)); idx[t.lower()] = "h_" + f
    (OUT / "assets/audio.js").write_text("window.OWEE_AUDIO=" + json.dumps(idx, ensure_ascii=False) + ";", encoding="utf8")
    (OUT / ".nojekyll").write_text("")
    print(f"OK {OUT}: {len(LEX)} entradas, {len(poems)} textos poeticos, {npdf} PDFs, fuente literatura: {LIT.name}")

if __name__ == "__main__":
    main()
