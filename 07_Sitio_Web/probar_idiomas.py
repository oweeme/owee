#!/usr/bin/env python3
"""Prueba en un navegador real que el selector ES / Owee / Script cambia la interfaz de todo el sitio.

Para cada página pública: ES -> Owee (romano) -> Script -> ES; comprueba que en Script cada texto traducido sea solo
glifos, que en Owee sea romano, que ES restaure el original exacto, que Script -> romano coincida con el texto Owee, y
que el modo se conserve al pasar a otra página. Muestra además cuántos textos de títulos y etiquetas tienen traducción.

Necesita: pip install playwright (usa el Chromium ya instalado). Uso:
    python3 probar_idiomas.py [carpeta_del_sitio]      (por defecto 07_Sitio_Web/docs; se genera con build_site.py)
    python3 probar_idiomas.py --captura salida.png     guarda capturas de la portada en los 3 modos"""
import functools, http.server, os, pathlib, re, sys, threading
from playwright.sync_api import sync_playwright

aqui = pathlib.Path(__file__).resolve().parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
captura = sys.argv[sys.argv.index("--captura") + 1] if "--captura" in sys.argv else None
if captura and captura in args: args.remove(captura)
raiz = pathlib.Path(args[0]) if args else aqui / "docs"
PUA = re.compile(r"[-]")

class Quieto(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

def main():
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quieto, directory=str(raiz)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_port}/"
    paginas = sorted(p.name for p in raiz.glob("*.html") if "imprimir" not in p.name)
    fallos, resumen = [], []
    exe = os.environ.get("PLAYWRIGHT_CHROMIUM", "/opt/pw-browsers/chromium")
    with sync_playwright() as pw:
        try: nav = pw.chromium.launch()
        except Exception: nav = pw.chromium.launch(executable_path=exe)
        ctx = nav.new_context(viewport={"width": 1280, "height": 900}); pg = ctx.new_page()
        for nombre in paginas:
            pg.goto(base + nombre); pg.wait_for_load_state("load")
            pg.evaluate("localStorage.clear()"); pg.goto(base + nombre); pg.wait_for_load_state("load")
            info = pg.evaluate("""() => [...document.querySelectorAll('[data-ow]')].map(e => ({es: e.textContent, ow: e.dataset.ow}))""")
            tit = pg.evaluate("""() => document.querySelectorAll('main h1, main h2, main h3, main th, main button').length""")
            for modo in ("owee", "script", "es"):
                pg.click(f'[data-ui="{modo}"]'); pg.wait_for_timeout(30)
                est = pg.evaluate("""() => [...document.querySelectorAll('[data-ow]')].map(e => ({t: e.textContent, c: e.classList.contains('o'), r: window.Owee ? Owee.toRoman(e.textContent) : ''}))""")
                for e, x in zip(info, est):
                    if modo == "es" and x["t"] != e["es"]: fallos.append(f"{nombre}: ES no restaura «{e['es']}» (queda «{x['t']}»)")
                    if modo == "owee" and (x["t"] != e["ow"] or PUA.search(x["t"])): fallos.append(f"{nombre}: Owee de «{e['es']}» = «{x['t']}»")
                    if modo == "script":
                        sin_marcas = re.sub(r"\b(?:Owee|Sans|School|Keyman|Windows|Android|iPhone|macOS|Linux|ES|V|CV|AFI|i)\b", "", x["t"])
                        if not x["c"] or re.search(r"[A-Za-z]", sin_marcas):
                            fallos.append(f"{nombre}: Script de «{e['es'][:40]}» deja letras latinas: «{x['t'][:60]}»")
                        if not PUA.search(x["t"]): fallos.append(f"{nombre}: Script de «{e['es']}» sin glifos")
                        if x["r"].replace(" ", "") != e["ow"].replace(" ", ""): fallos.append(f"{nombre}: Script -> romano de «{e['es']}»: «{x['r']}» != «{e['ow']}»")
            resumen.append((nombre, len(info), tit))
        # el modo se conserva al cambiar de página
        pg.goto(base + "index.html"); pg.click('[data-ui="script"]'); pg.wait_for_timeout(30)
        pg.evaluate("document.querySelector('nav a[href=\"escritura.html\"]').click()"); pg.wait_for_load_state("load"); pg.wait_for_timeout(150)
        persiste = pg.evaluate("""() => document.querySelector('[data-ui="script"]').getAttribute('aria-pressed') === 'true' && [...document.querySelectorAll('[data-ow]')].some(e => e.classList.contains('o') && /[\\uE000-\\uE0FF]/.test(e.textContent))""")
        if not persiste: fallos.append("el modo Script no se conserva al cambiar de página")
        # el modo Script usa la fuente Owee (si no, se verían cuadros)
        pg.goto(base + "index.html"); pg.click('[data-ui="script"]'); pg.wait_for_timeout(300)
        fuente = pg.evaluate("""() => document.fonts.ready.then(() => [...document.fonts].some(f => /Owee/.test(f.family) && f.status === 'loaded'))""")
        if not fuente: fallos.append("la fuente Owee no se cargó en modo Script")
        # la etiqueta del propio selector y el nombre del sitio también van en glifos con la fuente Owee
        etiqueta = pg.evaluate("""() => { const e = document.querySelector('[data-ui="script"] .o'); return e ? getComputedStyle(e).fontFamily + '|' + e.textContent : '' }""")
        if "Owee" not in etiqueta.split("|")[0] or not PUA.search(etiqueta.split("|")[-1]): fallos.append(f"etiqueta del selector sin fuente Owee o sin glifos: {etiqueta}")
        marca = pg.evaluate("""() => { const b = document.querySelector('.brand b'); return b ? getComputedStyle(b).fontFamily + '|' + b.textContent : '' }""")
        if "Owee" not in marca.split("|")[0] or not PUA.search(marca.split("|")[-1]): fallos.append(f"el nombre del sitio no sale en glifos en modo Script: {marca}")
        if captura:
            for modo in ("es", "owee", "script"):
                pg.goto(base + "index.html"); pg.evaluate("localStorage.clear()"); pg.goto(base + "index.html"); pg.click(f'[data-ui="{modo}"]'); pg.wait_for_timeout(500)
                pg.screenshot(path=captura.replace(".png", f"_{modo}.png"))
        nav.close()
    tot = sum(n for _, n, _ in resumen); print(f"{len(paginas)} páginas, {tot} textos traducibles (de ellos {sum(1 for _, n, _ in resumen if n)} páginas con alguno)")
    for nombre, n, t in resumen:
        if n: print(f"  {nombre:24} {n:3} textos de interfaz en Owee")
    for f in fallos[:40]: print("FALLO", f)
    print("Modo conservado al cambiar de página:", "sí" if persiste else "NO", "· fuente Owee:", "cargada" if fuente else "NO")
    print(f"{len(fallos)} fallos"); srv.shutdown()
    return 1 if fallos else 0

if __name__ == "__main__":
    sys.exit(main())
