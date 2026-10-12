"""Owee romano <-> Owee Script (Python). Mismas reglas que owee.js y el IME Fcitx5 1.2.

  to_script("sade-kelo Ana") -> texto con U+E000..E049, nexo U+E03C y marca de nombre U+E03D
  to_roman(texto_script)     -> romano
  valida(palabra)            -> True si es Owee valido (V/CV, sin i)
Una palabra imposible se deja en romano (no se pierde texto).
"""
import re

VOCALES = "aeou"
CONS = ["p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r", "sh", "ch"]
JOIN, NAME = chr(0xE03C), chr(0xE03D)
_POR_ROMANO = {}
_cp = 0xE000
for _v in VOCALES:
    _POR_ROMANO[_v] = chr(_cp); _cp += 1
for _c in CONS:
    for _v in VOCALES:
        _POR_ROMANO[_c + _v] = chr(_cp); _cp += 1
_POR_CHAR = {v: k for k, v in _POR_ROMANO.items()}
_POR_CHAR.update({JOIN: "-"})
for _d in range(10):
    _POR_CHAR[chr(0xE040 + _d)] = str(_d)
_SIL = re.compile(r"(sh|ch|[pbtdkgfsmnlr])?([aeou])")


def silabas(palabra):
    w = palabra.lower()
    out = [(m.group(1) or "") + m.group(2) for m in _SIL.finditer(w)]
    return out if out and "".join(out) == w else None


def valida(palabra):
    return silabas(palabra) is not None


def _palabra(p):
    s = silabas(p)
    return "".join(_POR_ROMANO[x] for x in s) if s else None


def to_script(texto, digitos=True):
    def tok(m):
        t = m.group(0)
        if t.isdigit():
            return chr(0xE040 + int(t)) if digitos else t
        partes = t.split("-")
        conv = [_palabra(p) for p in partes]
        nombre = bool(re.fullmatch(r"[A-Z][a-z]*", partes[0]))
        out = JOIN.join(conv) if all(c is not None for c in conv) else "-".join(c if c is not None else p for c, p in zip(conv, partes))
        return (NAME if nombre and conv[0] is not None else "") + out
    return re.sub(r"[A-Za-z]+(?:-[A-Za-z]+)*|[0-9]", tok, texto)


def to_roman(texto):
    out, may = "", False
    for ch in texto:
        if ch == NAME:
            may = True; continue
        r = _POR_CHAR.get(ch, ch)
        if may and ch in _POR_CHAR:
            r = r[:1].upper() + r[1:]; may = False
        out += r
    return out


if __name__ == "__main__":
    import sys
    t = " ".join(sys.argv[1:]) or "sade-kelo Ana suna 2026"
    s = to_script(t)
    print(t, "->", s, "->", to_roman(s))
