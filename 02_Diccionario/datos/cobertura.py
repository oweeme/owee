#!/usr/bin/env python3
"""Cobertura del lexico sobre ~120 conceptos basicos (lista de trabajo propia, tipo 'Swadesh reducida').
estado: R = ya hay raiz/operador; C = se puede componer con raices existentes (propuesta); F = falta, hay que decidir.
La clasificacion es un juicio de trabajo, no una norma: sirve para priorizar."""
BASICOS = {
 "Acciones": {"ser/estar":"R gade/mora","tener":"R pase","hacer":"R dare","dar":"R pema","recibir":"R gura","tomar":"R delo","usar":"R kade","comer":"R pume","dormir":"R sule","saber":"R lare","pensar":"R rena","entender":"R karo","querer":"R nume","poder":"R pode","deber":"R pelo",
   "ir/moverse":"R duma","venir":"C duma + to me","ver":"C loke + luma","oír":"C sone + luma","decir/hablar":"C reka","vivir":"R suma","morir":"C suma-gune","amar":"R lore","beber":"C nobe + pume","caminar":"C kalu + duma","sentarse":"C sede + pose","correr":"C sape-pa + duma","cantar":"C sone + lena","dormir/soñar":"F distinguir","jugar":"R lena-duma","llorar":"R loke-suna","reír":"R sabe-lena","matar":"C suma-gune + dare","luchar":"C naro + balo + fada","pedir":"R nume-reka","preguntar":"C ka + reka","responder":"R reka-pema","esperar":"R pu-dure","encontrar":"R kera","buscar":"R kera-nume","empezar/terminar":"R pado/gune","llamar/nombrar":"C sena-nara (nombre) + reka"},
 "Seres y lugares": {"persona":"R nara","hombre/mujer":"R nara (neutro por diseño)","niño/adulto":"C naku / nara gore-pa","familia":"R mela","amigo":"R reme","casa":"R kuma","ciudad":"C saro + kore","país":"R saro-kore","camino":"C duma + kore","puerta":"R nado","mar":"C suna + gore-pa","río":"C suna + duma","montaña":"C taro + go","árbol":"C nelo + gore-pa","flor":"R nelo-lena","estrella":"C kuna + salo","nube":"C kuna + suna","viento":"C sura + duma","lluvia":"C kuna-suna","animal":"R ruma","pájaro/pez":"R ruma-kuna / ruma-suna","dios":"R kuna-nara","nombre":"R sena-nara","libro":"C beka + kema"},
 "Tiempo y espacio": {"hoy/ahora":"R te","ayer":"R pe + tera","mañana":"R pu + tera","día/noche":"C kuna-salo / kuna-bore","año/mes/semana":"C sade-kelo / mune-kelo (semana: falta)","siempre":"R tera-fese","nunca":"C no + tera","otra vez":"R pu-kelo","aquí/allí":"C kore + le/lu","arriba/abajo":"R go/gu","dentro/fuera":"R bo/ba","cerca/lejos":"R le/lu"},
 "Cualidades": {"grande/pequeño":"R gore-pa/po","nuevo/viejo":"R tame/gule","bueno/malo":"R lafe (prov.)","bello":"C lafe-pa","triste/alegre":"C dune-lena / doma-bosa","caliente/frío":"R fure-pa/po","rápido/lento":"R sape-pa/po","fuerte/débil":"R faro-pa/po","lleno/vacío":"R mude/nuse","verdadero/falso":"C tare / tare no","colores (6)":"R","largo/corto":"R dase-pa / dase-po","alto/bajo":"C gore + go/gu","limpio/sucio":"R gase/dabo","difícil/fácil":"R dema-pa/po"},
 "Gramática y función": {"yo/tú/él":"R me/tu/ra","nosotros/ustedes/ellos":"R mene/tune/rane (prov.)","este/ese (demostrativos)":"R le / lu","todo":"R kema-fese","nada/algo/alguien":"R kema-no / nara-no","mucho/poco":"C bema-pa/po","otro/mismo":"C se / se no","muy":"R gore-pa-pa (doble operador)","también":"R re-se","y/o/si/pero/porque":"R re/lo/ke/balo/kasu","con/sin":"R ko/so","para (finalidad)":"C to (hacia)","de (pertenencia)":"R pase (orden)","quién/dónde/cuánto/por qué/cómo/cuándo":"R ka-…","qué":"R ka-kema","sí":"R tare","gracias/por favor/hola/adiós":"R gura-lena / pode ka / reme / pu-reme","relativo (que, el cual)":"R ra (Gramática 1.1 §9)","vocativo":"R nombre + coma","imperativo/ruego":"R verbo desnudo / pode ka","número compuesto (25, 2026)":"R Matemáticas 1.0 (falta pasarlo al Registro)"},
}
tot = {"R": 0, "C": 0, "F": 0}
for grupo, d in BASICOS.items():
    c = {"R": 0, "C": 0, "F": 0}
    for k, v in d.items(): c[v.split()[0]] += 1
    for k in c: tot[k] += c[k]
    print(f"{grupo:22} R={c['R']:2} C={c['C']:2} F={c['F']:2}  de {len(d)}")
n = sum(tot.values())
print(f"TOTAL {n}: con raíz {tot['R']} ({tot['R']*100//n}%), componible {tot['C']} ({tot['C']*100//n}%), falta {tot['F']} ({tot['F']*100//n}%)")
print("\nFaltan (F):")
for g, d in BASICOS.items():
    print(" -", g + ":", ", ".join(k for k, v in d.items() if v.split()[0] == "F"))
