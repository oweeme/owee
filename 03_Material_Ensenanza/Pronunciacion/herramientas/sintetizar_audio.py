#!/usr/bin/env python3
"""Genera el audio de pronunciacion de Owee (silabas, cifras, palabras del diccionario y frases del curso) con una voz
sintetica de espanol latinoamericano (Piper, modelo es_MX-ald-medium, dominio publico / Unlicense).

IMPORTANTE: es una aproximacion. Owee no tiene hablantes nativos todavia; la voz espanola recibe los fonemas de Owee
(vocales a e o u, consonantes con sh y ch, acento en la primera silaba de cada elemento) y suena a un hispanohablante
pronunciando Owee. Sirve para estudiar el ritmo y el acento; una grabacion humana siempre sera mejor.

Requisitos (una vez):  numpy y onnxruntime (pip install numpy onnxruntime), el modelo de voz y ffmpeg.
   mkdir -p ~/.owee-tts && cd ~/.owee-tts
   curl -LO https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_MX/ald/medium/es_MX-ald-medium.onnx
   curl -LO https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_MX/ald/medium/es_MX-ald-medium.onnx.json
Uso:   python3 sintetizar_audio.py [--voz ~/.owee-tts/es_MX-ald-medium.onnx] [--salida ../audio] [--solo silabas,cifras,palabras,frases]
Genera  <salida>/<texto>.ogg  y  <salida>/indice.json  ({texto: archivo}).  OWEE_TTS_DEPS=ruta  anade rutas de Python extra."""
import argparse, json, os, pathlib, re, subprocess, sys, tempfile, wave
for extra in filter(None, os.environ.get("OWEE_TTS_DEPS", "").split(os.pathsep)): sys.path.insert(0, extra)
import numpy as np
import onnxruntime as ort

aqui = pathlib.Path(__file__).resolve().parent
RAIZ = aqui.parents[2]
IPA = {"p": ["p"], "b": ["b"], "t": ["t"], "d": ["d"], "k": ["k"], "g": ["ɡ"], "f": ["f"], "s": ["s"], "m": ["m"], "n": ["n"],
       "l": ["l"], "r": ["ɾ"], "sh": ["ʃ"], "ch": ["t", "ʃ"]}
SIL = re.compile(r"(sh|ch|[pbtdkgfsmnlr])?([aeou])")

def fonemas(texto):
    """'me suna-nume' -> lista de fonemas IPA con acento (ˈ) en la primera silaba de cada elemento."""
    out = []
    for pi, palabra in enumerate(re.findall(r"[a-z]+(?:-[a-z]+)*|\?|\.", texto.lower())):
        if palabra in "?.": out.append(palabra); continue
        if out and out[-1] not in ("?", "."): out.append(" ")
        for ei, parte in enumerate(palabra.split("-")):
            ss = SIL.findall(parte)
            if "".join(c + v for c, v in ss) != parte: raise ValueError(f"no es Owee valido: {parte} en '{texto}'")
            for si, (c, v) in enumerate(ss):
                out += IPA.get(c, [])
                if si == 0: out.append("ˈ")
                out.append(v)
    return out

class Voz:
    def __init__(self, onnx):
        self.cfg = json.load(open(str(onnx) + ".json"))
        self.sess = ort.InferenceSession(str(onnx), providers=["CPUExecutionProvider"])
        self.m = self.cfg["phoneme_id_map"]; self.sr = self.cfg["audio"]["sample_rate"]
    def sintetizar(self, texto, lento=1.0):
        ids = list(self.m["^"])
        for f in fonemas(texto):
            if f in self.m: ids += self.m[f] + self.m["_"]
        ids += self.m["$"]
        inf = self.cfg["inference"]
        r = self.sess.run(None, {"input": np.array([ids], dtype=np.int64), "input_lengths": np.array([len(ids)], dtype=np.int64),
                                 "scales": np.array([inf["noise_scale"], inf["length_scale"] * lento, inf["noise_w"]], dtype=np.float32)})
        a = np.squeeze(r[0]).astype(np.float32)
        return recortar(a, self.sr)

def recortar(a, sr, umbral=0.02, pad=0.06):
    if a.size == 0: return a
    a = a / max(1e-6, np.max(np.abs(a))) * 0.9
    idx = np.where(np.abs(a) > umbral)[0]
    if idx.size == 0: return a
    i, j = max(0, idx[0] - int(pad * sr)), min(a.size, idx[-1] + int(pad * sr))
    return a[i:j]

def guardar(a, sr, ruta):
    with tempfile.NamedTemporaryFile(suffix=".wav") as t:
        with wave.open(t.name, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a * 32767).astype(np.int16).tobytes())
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", t.name, "-ac", "1", "-c:a", "libopus", "-b:a", "28k", str(ruta)], check=True)

def nombre(texto): return re.sub(r"[^a-z\-]+", "_", texto.lower()).strip("_") + ".ogg"

def unidades(solo):
    u = {}
    if "silabas" in solo:
        for c in ["", "p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"]:
            for v in "aeou": u.setdefault(c + v, "silaba")
    if "cifras" in solo:
        for p in "cho be du ga fo sa ku mu na she tanu gabu soku benu doto dapa dopo kebu faku".split(): u.setdefault(p, "cifra")
    if "palabras" in solo:
        for f in ("lexico.tsv", "lexico_ciencias.tsv"):
            for l in (RAIZ / "02_Diccionario/datos" / f).read_text(encoding="utf8").splitlines()[1:]:
                u.setdefault(l.split("\t")[0], "palabra")
    if "frases" in solo:
        for l in (RAIZ / "07_Sitio_Web/frases.tsv").read_text(encoding="utf8").splitlines():
            if l.strip(): u.setdefault(l.split("\t")[0], "frase")
        for md in sorted((RAIZ / "03_Material_Ensenanza/Curso").glob("Owee_Curso_Nivel_*.md")):
            for bloque in re.findall(r"```owee\n(.*?)```", md.read_text(encoding="utf8"), re.S):
                for linea in bloque.splitlines():
                    linea = linea.strip()
                    if linea and not linea.startswith("#"): u.setdefault(linea, "frase")
    return u

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voz", default=str(pathlib.Path.home() / ".owee-tts/es_MX-ald-medium.onnx"))
    ap.add_argument("--salida", default=str(aqui.parent / "audio"))
    ap.add_argument("--solo", default="silabas,cifras,palabras,frases")
    a = ap.parse_args()
    voz = Voz(a.voz); sal = pathlib.Path(a.salida); sal.mkdir(parents=True, exist_ok=True)
    idx = json.loads((sal / "indice.json").read_text(encoding="utf8")) if (sal / "indice.json").exists() else {}
    u = unidades(set(a.solo.split(","))); n = err = 0
    for t, tipo in u.items():
        f = sal / nombre(t)
        if f.exists() and t in idx: continue
        try:
            guardar(voz.sintetizar(t, 1.25 if tipo in ("silaba", "cifra") else (1.1 if tipo == "palabra" else 1.0)), voz.sr, f)
            idx[t] = f.name; n += 1
        except ValueError as e:
            err += 1; print("omitido:", e)
    (sal / "indice.json").write_text(json.dumps(dict(sorted(idx.items())), ensure_ascii=False, indent=0), encoding="utf8")
    print(f"{n} audios nuevos, {len(idx)} en total, {err} omitidos -> {sal}")

if __name__ == "__main__":
    main()
