#!/usr/bin/env python3
"""Graba TU voz para el audio de Owee, palabra por palabra, desde la terminal (Linux con PulseAudio/PipeWire + ffmpeg).

Las grabaciones se guardan en ../audio_humano/<texto>.ogg y, al regenerar el sitio, REEMPLAZAN a la voz sintetica de ese texto.
Orden de grabacion (de lo mas util a lo menos): silabas, cifras, palabras muy usadas, frases del curso, resto del diccionario.
Teclas:  Enter = empezar a grabar / parar     r = repetir     o = escuchar lo grabado     s = saltar     q = salir (puedes seguir otro dia)
Uso:     python3 grabar_voz.py [--solo silabas,cifras,basicas,frases,resto] [--lista] [--fuente pulse|alsa]
Consejos: ambiente silencioso, microfono a un palmo, di solo la palabra (acento fuerte en la PRIMERA silaba), 1 segundo de pausa antes y despues."""
import argparse, json, pathlib, re, subprocess, sys, tempfile, time
aqui = pathlib.Path(__file__).resolve().parent
RAIZ = aqui.parents[2]
SAL = aqui.parent / "audio_humano"

def nombre(t): return re.sub(r"[^a-z\-]+", "_", t.lower()).strip("_") + ".ogg"

def lista(solo):
    sil = [c + v for c in ["", "p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"] for v in "aeou"]
    cif = "cho be du ga fo sa ku mu na she tanu gabu soku benu".split()
    lex = {}
    for f in ("lexico.tsv", "lexico_ciencias.tsv"):
        for l in (RAIZ / "02_Diccionario/datos" / f).read_text(encoding="utf8").splitlines()[1:]:
            c = l.split("\t"); lex[c[0]] = c[3]
    basicas = [w for w in lex if "-" not in w][:240]      # las raices simples: lo que mas se repite
    frases = []
    for l in (RAIZ / "07_Sitio_Web/frases.tsv").read_text(encoding="utf8").splitlines():
        if l.strip(): frases.append((l.split("\t")[0], l.split("\t")[1]))
    for md in sorted((RAIZ / "03_Material_Ensenanza/Curso").glob("Owee_Curso_Nivel_*.md")):
        for b in re.findall(r"```owee\n(.*?)```", md.read_text(encoding="utf8"), re.S):
            for x in b.splitlines():
                if x.strip() and not x.startswith("#"): frases.append((x.strip(), ""))
    out = []
    if "silabas" in solo: out += [(s, "sílaba") for s in sil]
    if "cifras" in solo: out += [(c, "cifra") for c in cif]
    if "basicas" in solo: out += [(w, lex[w]) for w in basicas]
    if "frases" in solo: out += frases
    if "resto" in solo: out += [(w, m) for w, m in lex.items() if w not in basicas]
    vistos, res = set(), []
    for t, m in out:
        if t.lower() not in vistos: vistos.add(t.lower()); res.append((t, m))
    return res

def grabar(archivo, fuente):
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", fuente, "-i", "default", "-ac", "1", "-ar", "44100", archivo],
                         stdin=subprocess.PIPE)
    input("   ● grabando… (Enter para parar) ")
    try: p.stdin.write(b"q"); p.stdin.flush()
    except Exception: pass
    p.wait(timeout=10)

def procesar(wav, destino):
    # recorta silencios del principio y del final, normaliza el volumen y codifica en Opus
    filtro = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,"
              "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,loudnorm=I=-18:TP=-2,"
              "adelay=60,apad=pad_dur=0.06")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-af", filtro, "-ac", "1", "-c:a", "libopus", "-b:a", "32k", str(destino)], check=True)

def escuchar(f):
    for cmd in (["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", str(f)], ["paplay", str(f)]):
        try: subprocess.run(cmd, check=True); return
        except Exception: continue
    print("   (no pude reproducir; abre el archivo con tu reproductor)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", default="silabas,cifras,basicas,frases")
    ap.add_argument("--fuente", default="pulse")
    ap.add_argument("--lista", action="store_true", help="solo muestra cuantas faltan")
    a = ap.parse_args()
    items = lista(set(a.solo.split(",")))
    SAL.mkdir(exist_ok=True)
    idxf = SAL / "indice.json"
    idx = json.loads(idxf.read_text(encoding="utf8")) if idxf.exists() else {}
    falta = [(t, m) for t, m in items if t.lower() not in idx]
    print(f"{len(items)} textos en esta lista; ya grabados: {len(items) - len(falta)}; faltan: {len(falta)}")
    if a.lista: return
    for n, (t, m) in enumerate(falta, 1):
        while True:
            print(f"\n[{n}/{len(falta)}]   {t}" + (f"      ({m})" if m else ""))
            r = input("   Enter = grabar · s = saltar · q = salir: ").strip().lower()
            if r == "q": idxf.write_text(json.dumps(dict(sorted(idx.items())), ensure_ascii=False, indent=0), encoding="utf8"); return
            if r == "s": break
            with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
                grabar(tmp.name, a.fuente)
                destino = SAL / nombre(t)
                try: procesar(tmp.name, destino)
                except subprocess.CalledProcessError: print("   no se pudo procesar; repite"); continue
            while True:
                k = input("   o = escuchar · r = repetir · Enter = guardar y seguir: ").strip().lower()
                if k == "o": escuchar(destino)
                else: break
            if k == "r": continue
            idx[t.lower()] = destino.name
            idxf.write_text(json.dumps(dict(sorted(idx.items())), ensure_ascii=False, indent=0), encoding="utf8")
            break
    print("\nListo. Regenera el sitio (python3 07_Sitio_Web/build_site.py): tu voz reemplaza a la sintetica.")

if __name__ == "__main__":
    main()
