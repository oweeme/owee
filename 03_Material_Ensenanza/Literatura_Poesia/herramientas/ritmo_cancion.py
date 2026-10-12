#!/usr/bin/env python3
"""Convierte una letra Owee en un boceto musical (MIDI + WAV + ABC) segun el ESTILO de acento.

El acento de Owee NO cambia: cae siempre en la primera silaba de cada palabra (de cada elemento de un
compuesto). Lo que cambia es COMO se realiza al cantar:

  marcha   acento = intensidad + staccato                       (grito, himno, marcha)
  romance  acento = duracion + altura, volumen casi igual, legato  (canto suave, 4/4)
  cuna     como romance, aun mas lento, rango estrecho (3/4)
  hadas    canción de cuna de cuento de hadas: 6/8, escala mayor pentatonica, caja de musica

Tres formas de usar la melodia (--melodia):
  auto       (por defecto) melodia elaborada: frases A-A'-B-A, motivos que se repiten, cadencias y acompanamiento
  ritmo      solo el RITMO: hoja con silaba, acento y duracion, y una sola nota, para que compongas tu melodia
  ARCHIVO    tu propia melodia: un .txt con las notas de cada silaba (ver --plantilla)

Uso:
  python3 ritmo_cancion.py ARCHIVO.md -s "Mune kuma" --estilo hadas [--melodia auto|ritmo|ARCHIVO.txt]
        [-t BPM] [--acomp si|no] [--tono C#m] [--plantilla] [-o CARPETA]

  Dentro del bloque ```owee puedes poner directivas (lineas que empiezan con #):
      # tono: C#m                  tonalidad (escala de la melodia)
      # acordes: C#m B A E         acordes que se reparten verso a verso (se repiten en ciclo)

  --plantilla   escribe <nombre>_melodia.txt con un '?' por silaba: rellena las notas (C4 D4 F#4 Bb3 ...,
                opcional duracion en tiempos: D4:1.5) y vuelve a ejecutar con --melodia ese.txt
Es un boceto de ritmo, acento y armonia (sin voz): sirve para oir como se siente cada estilo.
"""
import math, random, re, struct, sys, wave, pathlib

SIL = re.compile(r"(sh|ch|[pbtdkgfsmnlr])?([aeou])")

D_MENOR_PENT = [62, 65, 67, 69, 72, 74, 77, 79]
D_MAYOR_PENT = [62, 64, 66, 69, 71, 74, 76, 78, 81, 83]
ACORDES_MAYOR = [("D", [50, 57, 62, 66]), ("Bm", [47, 54, 59, 62]), ("G", [43, 50, 55, 59]), ("A", [45, 52, 57, 61])]
ACORDES_MENOR = [("Dm", [50, 57, 62, 65]), ("C", [48, 55, 60, 64]), ("Bb", [46, 53, 58, 62]), ("A", [45, 52, 57, 61])]

ESTILOS = {
    # bpm, dur acentuada, dur atona (en negras), velocidad ac./at., legato, dur final, pausa, programa voz, escala, acordes, compas
    "marcha":  dict(bpm=112, ds=0.50, du=0.25, vs=112, vu=70, leg=0.55, fin=1.0, pausa=0.25, prog=56, escala=D_MENOR_PENT,
                    acordes=ACORDES_MENOR, compas="2/4", barra=2.0, acomp=False, plana=True),
    "romance": dict(bpm=66, ds=1.00, du=0.50, vs=60, vu=54, leg=1.06, fin=2.0, pausa=0.50, prog=52, escala=D_MENOR_PENT,
                    acordes=ACORDES_MENOR, compas="4/4", barra=4.0, acomp=True, plana=False),
    "cuna":    dict(bpm=54, ds=1.50, du=0.75, vs=46, vu=42, leg=1.10, fin=3.0, pausa=0.75, prog=52, escala=D_MENOR_PENT,
                    acordes=ACORDES_MENOR, compas="3/4", barra=3.0, acomp=True, plana=False),
    "balada":  dict(bpm=76, ds=1.00, du=0.50, vs=70, vu=60, leg=1.04, fin=2.0, pausa=0.50, prog=52, escala=D_MENOR_PENT,
                    acordes=ACORDES_MENOR, compas="4/4", barra=4.0, acomp=True, plana=False),
    "hadas":   dict(bpm=58, ds=1.00, du=0.50, vs=58, vu=52, leg=1.06, fin=2.0, pausa=0.50, prog=52, escala=D_MAYOR_PENT,
                    acordes=ACORDES_MAYOR, compas="6/8", barra=3.0, acomp=True, plana=False),
}
SOSTENIDOS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


# ------------------------------------------------------------ analisis de la letra
def silabas(elemento):
    """Silabas de un elemento; una vocal repetida (aa, ee, oo, uu) alarga la silaba anterior (melisma)."""
    out = []
    for m in SIL.finditer(elemento):
        c, v = m.group(1) or "", m.group(2)
        if not c and out and out[-1]["v"] == v:
            out[-1]["largo"] += 1                       # aa = 2, aaa = 3 (alargamiento expresivo)
        else:
            out.append(dict(c=c, v=v, largo=1))
    return out


def analiza(linea):
    """Silabas con acento: la primera de cada elemento de 2+ silabas; monosilabos atonos (salvo verso solo de monosilabos)."""
    elems, palabra_de, ultimo = [], [], []
    for pi, palabra in enumerate(re.findall(r"[a-z]+(?:-[a-z]+)*", linea.lower())):
        partes = palabra.split("-")
        for k, e in enumerate(partes):
            elems.append(silabas(e)); palabra_de.append(pi); ultimo.append(k == len(partes) - 1)
    todo_mono = all(len(e) == 1 for e in elems)
    out = []
    for e, pw, fin_pal in zip(elems, palabra_de, ultimo):
        for i, s in enumerate(e):
            s["acento"] = (i == 0 and (len(e) >= 2 or todo_mono))
            s["texto"] = s["c"] + s["v"] * s["largo"]
            s["palabra"] = pw
            s["fin_elem"] = (i == len(e) - 1)
            s["fin_pal"] = (i == len(e) - 1) and fin_pal
            out.append(s)
    return out


def nota_a_midi(nombre):
    m = re.fullmatch(r"([A-Ga-g])([#b]?)(-?\d)", nombre)
    if not m: raise ValueError(f"nota no valida: {nombre!r} (usa C4, D4, F#4, Bb3…)")
    base = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}[m.group(1).upper()]
    return 12 * (int(m.group(3)) + 1) + base + {"#": 1, "b": -1, "": 0}[m.group(2)]


def midi_a_nombre(n):
    return SOSTENIDOS[n % 12] + str(n // 12 - 1)


# ------------------------------------------------------------ acordes y tono
def parse_acorde(nombre):
    """'C#m' -> (tonica pc, menor?, [bajo, quinta, octava, tercera]). Acepta m, 7, maj7 (se usa la triada)."""
    m = re.fullmatch(r"([A-G])([#b]?)(m?)(?:maj7|7)?", nombre)
    if not m: raise ValueError(f"acorde no valido: {nombre!r}")
    pc = ({"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}[m.group(1)] + {"#": 1, "b": -1, "": 0}[m.group(2)]) % 12
    menor = m.group(3) == "m"
    bajo = (36 + pc) if pc >= 7 else (48 + pc)
    return pc, menor, [bajo, bajo + 7, bajo + 12, bajo + 12 + (3 if menor else 4)]


def escala_tono(tono):
    """Pentatonica menor o mayor desde la tonica (aprox. C#4..): ~2 octavas."""
    pc, menor, _ = parse_acorde(tono)
    iv = [0, 3, 5, 7, 10] if menor else [0, 2, 4, 7, 9]
    base = 60 + pc
    return [base + 12 * o + i for o in (0, 1) for i in iv] + [base + 24]


# ------------------------------------------------------------ melodia
def melodia_auto(lineas, est, semilla):
    """Melodia elaborada: roles de frase (abre, responde, asciende, cierra), motivo repetido y cadencias."""
    esc = est["escala"]; top = len(esc) - 1
    rng = random.Random(semilla)
    roles = [(2, 3), (1, 2), (3, 4), (2, 0)]        # (nota inicial, nota final) por rol dentro de cada grupo de 4
    res, previo = [], None
    for li, sil in enumerate(lineas):
        n = len(sil)
        s, e = roles[li % 4]
        if li == len(lineas) - 1: e = 0             # el ultimo verso siempre cierra en la tonica
        if est["plana"]:
            idx = [min(top, 3 if x["acento"] else 0) for x in sil]
        elif li % 4 == 2 and previo is not None and len(previo) == n:
            idx = [min(top, k + 1) for k in previo]  # motivo del verso 1 una nota mas arriba (frase 'sube')
            idx[-1] = e
        else:
            idx = []
            for i, x in enumerate(sil):
                pos = i / max(1, n - 1)
                k = s + (e - s) * pos + 1.5 * math.sin(math.pi * pos) + rng.choice([-0.4, 0, 0, 0.4])
                k = round(k) + (1 if x["acento"] and i < n - 1 else 0)
                idx.append(max(0, min(top, k)))
            for i in range(1, n):                    # limitar saltos a 2 grados
                if idx[i] - idx[i - 1] > 2: idx[i] = idx[i - 1] + 2
                if idx[i - 1] - idx[i] > 2: idx[i] = idx[i - 1] - 2
            idx[-1] = e
        if li % 4 == 0: previo = idx
        res.append([esc[k] for k in idx])
    return res


def melodia_archivo(ruta, lineas):
    """Lee notas por silaba: una linea del .txt por verso; opcional ':duracion' en tiempos."""
    verso, errores = [], []
    for l in pathlib.Path(ruta).read_text(encoding="utf8").splitlines():
        if l.strip() and not l.lstrip().startswith("#"): verso.append(l.split())
    if len(verso) != len(lineas):
        raise SystemExit(f"El archivo tiene {len(verso)} lineas de notas y la letra {len(lineas)} versos.")
    notas, durs = [], []
    for i, (toks, sil) in enumerate(zip(verso, lineas), 1):
        if len(toks) != len(sil):
            errores.append(f"verso {i}: {len(sil)} silabas, pero hay {len(toks)} notas")
            continue
        n, d = [], []
        for t in toks:
            if t == "?": errores.append(f"verso {i}: falta rellenar una nota ('?')"); break
            nm, _, du = t.partition(":")
            n.append(nota_a_midi(nm)); d.append(float(du) if du else None)
        notas.append(n); durs.append(d)
    if errores: raise SystemExit("\n".join(errores))
    return notas, durs


# ------------------------------------------------------------ construccion
def duraciones(sil, est):
    out = []
    for i, s in enumerate(sil):
        d = est["ds"] if s["acento"] else est["du"]
        d *= s["largo"]
        if i == len(sil) - 1: d = max(d, est["fin"])
        out.append(d)
    return out


def construir(lineas, est, alturas, durs_usuario=None, ritmo_solo=False, acordes_linea=None):
    notas, tramos, t = [], [], 0.0               # nota: (inicio, dur, midi, vel, texto, acento)
    for li, (sil, alt) in enumerate(zip(lineas, alturas)):
        ds = duraciones(sil, est)
        if durs_usuario:
            ds = [u if u is not None else d for u, d in zip(durs_usuario[li], ds)]
        t0 = t
        for i, (s, d, m) in enumerate(zip(sil, ds, alt)):
            # letra del MIDI al estilo karaoke: '/' abre verso, ' ' cierra palabra, '-' une los elementos de un compuesto
            lyric = ("/" if i == 0 else "") + s["texto"] + (" " if s["fin_pal"] else ("-" if s["fin_elem"] else ""))
            notas.append((t, d, 67 if ritmo_solo else m, est["vs"] if s["acento"] else est["vu"], lyric, s["acento"]))
            t += d
        tramos.append((t0, t))
        t += est["pausa"]
    acomp = []
    if est["acomp"] and not ritmo_solo:
        for li, (t0, t1) in enumerate(tramos):
            if acordes_linea and acordes_linea[li]:
                nombre = acordes_linea[li]; ac = parse_acorde(nombre)[2]
            else:
                nombre, ac = est["acordes"][li % len(est["acordes"])]
            x = t0
            while x < t1 - 1e-6:
                if abs((x - t0) % est["barra"]) < 1e-6:
                    acomp.append((x, min(est["barra"], t1 - x), ac[0], 44))
                else:
                    acomp.append((x, 0.5, ac[[1, 2, 3, 2][int(round((x - t0) * 2)) % 4]], 32))
                x += 0.5
    return notas, acomp, tramos


def vlq(n):
    b = [n & 0x7F]; n >>= 7
    while n:
        b.append((n & 0x7F) | 0x80); n >>= 7
    return bytes(reversed(b))


def a_midi(notas, acomp, est):
    TPQ = 480
    ev = [(0, b"\xFF\x51\x03" + int(60_000_000 / est["bpm"]).to_bytes(3, "big")),
          (0, b"\xFF\x58\x04" + bytes([int(est["compas"].split("/")[0]), int(math.log2(int(est["compas"].split("/")[1]))), 24, 8])),
          (0, bytes([0xC0, est["prog"]])), (0, bytes([0xC1, 10]))]
    for ini, d, m, v, tx, ac in notas:
        a = int(ini * TPQ); fin = a + int(d * TPQ * (est["leg"] if est["leg"] < 1 else 1.0))
        ev += [(a, b"\xFF\x05" + vlq(len(tx.encode())) + tx.encode()), (a, bytes([0x90, m, v])), (fin, bytes([0x80, m, 0]))]
    for ini, d, m, v in acomp:
        a = int(ini * TPQ)
        ev += [(a, bytes([0x91, m, v])), (a + int(d * TPQ), bytes([0x81, m, 0]))]
    ev.sort(key=lambda e: (e[0], (e[1][0] & 0xF0) == 0x90))
    trk, ult = b"", 0
    for tick, data in ev:
        trk += vlq(tick - ult) + data; ult = tick
    trk += vlq(0) + b"\xFF\x2F\x00"
    return b"MThd" + struct.pack(">IHHH", 6, 0, 1, TPQ) + b"MTrk" + struct.pack(">I", len(trk)) + trk


def a_wav(notas, acomp, est, ruta, sr=16000):
    spb = 60.0 / est["bpm"]
    fin = max([n[0] + n[1] for n in notas] + [a[0] + a[1] for a in acomp]) * spb + 1.5
    buf = [0.0] * int(fin * sr)
    stacc = est["leg"] < 1
    for ini, d, m, v, _, _ in notas:                      # voz: seno suave con vibrato en notas largas
        f = 440.0 * 2 ** ((m - 69) / 12); dur = d * spb * (est["leg"] if stacc else 1.0) + (0.0 if stacc else 0.10)
        n = int(dur * sr); s0 = int(ini * spb * sr); amp = v / 127 * 0.30
        ataque = 0.006 if stacc else 0.07; rel = 0.05 if stacc else 0.14
        for i in range(n):
            tt = i / sr
            env = min(1.0, tt / ataque) * min(1.0, max(0.0, (dur - tt) / rel))
            vib = 1 + (0.004 * math.sin(2 * math.pi * 5.2 * tt) if (dur > 0.7 and tt > 0.25) else 0.0)
            x = math.sin(2 * math.pi * f * vib * tt) + 0.30 * math.sin(4 * math.pi * f * vib * tt) + 0.10 * math.sin(6 * math.pi * f * vib * tt)
            if s0 + i < len(buf): buf[s0 + i] += amp * env * x / 1.4
    for ini, d, m, v in acomp:                            # acompanamiento: caja de musica (parciales inarmonicos, caida exponencial)
        f = 440.0 * 2 ** ((m - 69) / 12); s0 = int(ini * spb * sr); n = int(min(1.3, d * spb + 0.9) * sr); amp = v / 127 * 0.26
        for i in range(n):
            tt = i / sr
            env = min(1.0, tt / 0.003) * math.exp(-tt / 0.45)
            x = math.sin(2 * math.pi * f * tt) + 0.40 * math.sin(2 * math.pi * f * 2.76 * tt) + 0.14 * math.sin(2 * math.pi * f * 5.4 * tt)
            if s0 + i < len(buf): buf[s0 + i] += amp * env * x / 1.5
    pico = max(1e-9, max(abs(x) for x in buf))
    datos = b"".join(struct.pack("<h", int(max(-1, min(1, x / pico * 0.9)) * 32767)) for x in buf)
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(datos)


def abc_pitch(m):
    n = SOSTENIDOS[m % 12]; octava = m // 12 - 1
    letra = n[0]; alt = "^" if "#" in n else ""
    if octava >= 5: return alt + letra.lower() + "'" * (octava - 5)
    return alt + letra + "," * (4 - octava)


def a_abc(notas, est, titulo, lineas, acordes_linea=None, tono=None):
    out = ["X:1", f"T:{titulo}", f"M:{est['compas']}", "L:1/16", f"Q:1/4={est['bpm']}", ("K:" + tono) if tono else ("K:D" if est["escala"] is D_MAYOR_PENT else "K:Dm")]
    k = 0
    for li, sil in enumerate(lineas):
        ns = notas[k:k + len(sil)]; k += len(sil)
        nom = (acordes_linea[li] if acordes_linea and acordes_linea[li] else est["acordes"][li % len(est["acordes"])][0])
        acorde = f'"{nom}"' if est["acomp"] else ""
        out.append(acorde + " ".join(f"{abc_pitch(m)}{max(1, round(d * 4))}" for _, d, m, _, _, _ in ns) + " |")
        w, ult = [], None
        for s in sil:
            w.append(("-" if ult == s["palabra"] and w else (" " if w else "")) + s["texto"]); ult = s["palabra"]
        out.append("w: " + "".join(w).strip())
    return "\n".join(out) + "\n"


def tabla(lineas, notas, ritmo_solo):
    k, out = 0, []
    for sil in lineas:
        ns = notas[k:k + len(sil)]; k += len(sil)
        out.append("  " + "  ".join(f"{'▲' if s['acento'] else ' '}{s['texto']}({n[1]:g}{'' if ritmo_solo else ' ' + midi_a_nombre(n[2])})" for s, n in zip(sil, ns)))
    return "\n".join(out)


def plantilla(lineas, letras, ruta):
    out = ["# Rellena una nota por silaba (C4 D4 F#4 Bb3 ...). Opcional: duracion en tiempos (negras), p. ej. D4:1.5",
           "# ▲ = silaba acentuada (cae en la primera silaba de cada palabra). No borres ni agregues lineas."]
    for sil, texto in zip(lineas, letras):
        out.append(f"# {texto}")
        out.append("# " + " ".join(("▲" if s["acento"] else "") + s["texto"] for s in sil))
        out.append(" ".join("?" for _ in sil))
    pathlib.Path(ruta).write_text("\n".join(out) + "\n", encoding="utf8")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    archivo, filtro, estilo = argv[0], opt("-s"), opt("--estilo", "romance")
    est = dict(ESTILOS[estilo])
    if opt("-t"): est["bpm"] = int(opt("-t"))
    if opt("--acomp"): est["acomp"] = opt("--acomp") == "si"
    modo = opt("--melodia", "auto")
    salida = pathlib.Path(opt("-o", ".")); salida.mkdir(parents=True, exist_ok=True)
    lineas, letras, dentro, tit = [], [], False, ""
    acordes_linea, ciclo, ci, tono = [], None, 0, opt("--tono")
    for l in pathlib.Path(archivo).read_text(encoding="utf8").splitlines():
        if l.startswith("###"): tit = l.lstrip("# ").strip()
        if l.startswith("```"):
            dentro = (l.strip() == "```owee") if not dentro else False
            continue
        if dentro and l.strip() and (not filtro or filtro.lower() in tit.lower()):
            if l.lstrip().startswith("#"):                       # directivas dentro del bloque
                d = l.lstrip("# ").strip()
                if d.lower().startswith("acordes:"): ciclo, ci = d.split(":", 1)[1].split(), 0
                elif d.lower().startswith("tono:") and not tono: tono = d.split(":", 1)[1].strip()
                continue
            lineas.append(analiza(l)); letras.append(l.strip())
            acordes_linea.append(ciclo[ci % len(ciclo)] if ciclo else None); ci += 1
    if tono:
        est["escala"] = escala_tono(tono); est["acordes"] = [(tono, parse_acorde(tono)[2])]
    if not lineas:
        print("No hay versos para ese filtro"); return
    base = re.sub(r"[^a-z0-9]+", "_", (filtro or "cancion").lower()).strip("_")
    if "--plantilla" in argv:
        plantilla(lineas, letras, salida / f"{base}_melodia.txt")
        print(f"Plantilla -> {salida}/{base}_melodia.txt (rellena las notas y usa --melodia ese archivo)"); return
    durs, ritmo_solo, sufijo = None, modo == "ritmo", ""
    if modo == "auto" or modo == "ritmo":
        alturas = melodia_auto(lineas, est, "".join(letras)) if modo == "auto" else [[67] * len(s) for s in lineas]
        sufijo = "" if modo == "auto" else "_ritmo"
    else:
        alturas, durs = melodia_archivo(modo, lineas); sufijo = "_propia"
    notas, acomp, _ = construir(lineas, est, alturas, durs, ritmo_solo, acordes_linea)
    nombre = f"{base}_{estilo}{sufijo}"
    (salida / f"{nombre}.mid").write_bytes(a_midi(notas, acomp, est))
    a_wav(notas, acomp, est, salida / f"{nombre}.wav")
    (salida / f"{nombre}.abc").write_text(a_abc(notas, est, filtro or "cancion", lineas, acordes_linea, tono), encoding="utf8")
    print(f"{filtro or 'cancion'} - estilo {estilo} ({est['compas']}, {est['bpm']} BPM) - melodia: {modo if modo in ('auto', 'ritmo') else 'propia'}")
    print(tabla(lineas, notas, ritmo_solo))
    print(f"-> {salida}/{nombre}.mid .wav .abc")


if __name__ == "__main__":
    main(sys.argv[1:])
