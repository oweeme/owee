#!/usr/bin/env python3
"""Adapta nombres propios del espanol a Owee con la norma de la Gramatica 1.1 (seccion 14).
Reglas: se escribe por el sonido; i->e, v->b, z/c suave->s, j y g suave->k, h->(nada), y consonante->e, q/c fuerte->k, w->u,
n con tilde->ne, x->kes; consonante final o grupo -> vocal de eco (la vocal anterior; en grupo inicial, la siguiente);
acento en la primera silaba; el nombre se marca con inicial mayuscula (y U+E03D en Owee Script).
Uso: python3 adaptar_nombre.py Pedro Carlos   |   sin argumentos genera nombres_propios.tsv"""
import pathlib, re, sys, unicodedata
V = "aeou"
CONS = {"p", "b", "t", "d", "k", "g", "f", "s", "m", "n", "l", "r"}

def sonidos(n):
    n = n.lower().replace("ñ", "NY"); n = unicodedata.normalize("NFD", n)
    n = "".join(c for c in n if unicodedata.category(c) != "Mn" or c == "̈")   # quita tildes (la dieresis se trata abajo)
    n = n.replace("̈", "").replace("NY", "ñ")
    out, i = [], 0
    while i < len(n):
        c, s = n[i], n[i + 1:i + 2]
        if c in "aou": out.append(c)
        elif c in "ei": out.append("e")
        elif c == "y": out.append("e")
        elif c == "h": pass
        elif c == "c" and s == "h": out.append("ch"); i += 1
        elif c == "s" and s == "h": out.append("sh"); i += 1
        elif c == "c": out.append("s" if s in ("e", "i") else "k")
        elif c == "q": out.append("k"); i += 1 if s == "u" else 0
        elif c == "g" and s in ("e", "i"): out.append("k")
        elif c == "g" and s == "u" and n[i + 2:i + 3] in ("e", "i"): out.append("g"); i += 1
        elif c == "l" and s == "l": out.append("e"); i += 1
        elif c == "r" and s == "r": out.append("r"); i += 1
        elif c in "vb": out.append("b")
        elif c in "zs": out.append("s")
        elif c == "j": out.append("k")
        elif c == "w": out.append("u")
        elif c == "ñ": out += ["n", "e"]
        elif c == "x": out += ["k", "e", "s"]
        elif c in CONS or c in "bdfgklmnprt": out.append(c)
        elif c in " -'": out.append(" ")
        else: raise ValueError(f"letra no soportada '{c}' en {n}")
        i += 1
    return out

def adaptar(nombre):
    palabras, cur = [], []
    for s in sonidos(nombre):
        if s == " ":
            if cur: palabras.append(cur); cur = []
        else: cur.append(s)
    if cur: palabras.append(cur)
    res = []
    for p in palabras:
        o, ultima = [], None
        for j, s in enumerate(p):
            if s in V:
                if o and o[-1] in V and o[-1] != "": pass
                o.append(s); ultima = s
            else:
                if o and o[-1] not in V:            # dos consonantes seguidas: eco antes de la segunda
                    o.append(ultima if ultima else next((x for x in p[j:] if x in V), "e"))
                o.append(s)
        if o and o[-1] not in V: o.append(ultima if ultima else "e")
        # un grupo inicial (sin vocal previa) ya recibio eco de la vocal siguiente; juntar vocales repetidas se deja como estan
        w = "".join(o)
        res.append(w[0].upper() + w[1:])
    return " ".join(res)

def valido(w):
    return re.fullmatch(r"(?:(?:sh|ch|[pbtdkgfsmnlr])?[aeou])+", w.lower().replace(" ", "")) is not None

NOMBRES = """Bolivia|país
La Paz|ciudad
Cochabamba|ciudad
Santa Cruz|ciudad
Sucre|ciudad
Oruro|ciudad
Potosí|ciudad
Tarija|ciudad
Trinidad|ciudad
Cobija|ciudad
El Alto|ciudad
Tiahuanaco|lugar
Titicaca|lugar
Uyuni|lugar
Illimani|lugar
Amazonas|lugar
Argentina|país
Brasil|país
Chile|país
Perú|país
Paraguay|país
Uruguay|país
Colombia|país
Ecuador|país
Venezuela|país
México|país
España|país
Estados Unidos|país
Canadá|país
Francia|país
Alemania|país
Italia|país
Portugal|país
Inglaterra|país
China|país
Japón|país
India|país
Rusia|país
Egipto|país
Nigeria|país
Australia|país
Europa|continente
Asia|continente
África|continente
América|continente
Oceanía|continente
Antártida|continente
Pedro|persona
Carlos|persona
María|persona
Elena|persona
Ana|persona
Hidrógeno|elemento químico (H)
Helio|elemento químico (He)
Litio|elemento químico (Li)
Carbono|elemento químico (C)
Nitrógeno|elemento químico (N)
Oxígeno|elemento químico (O)
Flúor|elemento químico (F)
Neón|elemento químico (Ne)
Sodio|elemento químico (Na)
Magnesio|elemento químico (Mg)
Aluminio|elemento químico (Al)
Silicio|elemento químico (Si)
Fósforo|elemento químico (P)
Azufre|elemento químico (S)
Cloro|elemento químico (Cl)
Argón|elemento químico (Ar)
Potasio|elemento químico (K)
Calcio|elemento químico (Ca)
Zinc|elemento químico (Zn)
Estaño|elemento químico (Sn)
Yodo|elemento químico (I)
Mercurio|elemento químico (Hg)
Plomo|elemento químico (Pb)
Uranio|elemento químico (U)""".split("\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for n in sys.argv[1:]: print(n, "->", adaptar(n), "" if valido(adaptar(n)) else "(NO VALIDO)")
    else:
        filas, mal = ["original\towee\ttipo"], []
        for l in NOMBRES:
            n, t = l.split("|"); a = adaptar(n)
            if not valido(a): mal.append((n, a))
            filas.append(f"{n}\t{a}\t{t}")
        pathlib.Path(__file__).with_name("nombres_propios.tsv").write_text("\n".join(filas) + "\n", encoding="utf8")
        print(len(NOMBRES), "nombres;", "no validos:", mal)
