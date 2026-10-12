#!/usr/bin/env python3
"""Cobertura sobre la lista Swadesh de 100 palabras (medida estandar de vocabulario basico entre lenguas).
R = ya hay forma en el lexico; C = se puede componer con raices existentes; F = falta.
La clasificacion es un juicio de trabajo; sirve para priorizar el vocabulario nuevo."""
import collections
LISTA = [
 ("yo","R me"),("tú","R tu"),("nosotros","R mene (prov.)"),("este","R kema-le"),("ese/aquel","R kema-lu"),("quién","R ka-nara"),("qué","R ka-kema"),("no","R no"),
 ("todo","R kema-fese"),("mucho","R bema-pa"),("uno","R be"),("dos","R du"),("grande","R gore-pa"),("largo","R dase-pa"),("pequeño","R gore-po"),
 ("mujer","R nara (neutro)"),("hombre","R nara (neutro)"),("persona","R nara"),("pez","R ruma-suna"),("pájaro","R ruma-kuna"),("perro","F animal concreto"),
 ("piojo","F"),("árbol","R nelo-gore-pa"),("semilla","F"),("hoja","F"),("raíz (planta)","F"),("corteza","F"),("piel","F"),("carne","F"),("sangre","F"),("hueso","F"),
 ("grasa","F"),("huevo","F"),("cuerno","F"),("cola","F"),("pluma","F"),("cabello","F"),("cabeza","R tume"),("oreja","F"),("ojo","R loke"),("nariz","R noke"),("boca","R sabe"),
 ("diente","F"),("lengua (órgano)","F"),("uña/garra","F"),("pie","C kalu"),("rodilla","F"),("mano","R maku"),("vientre","F"),("cuello","F"),("pecho/seno","F"),("corazón","R doma"),
 ("hígado","F"),("beber","C nobe pume"),("comer","R pume"),("morder","F"),("ver","R loke-luma"),("oír","R sone-luma"),("saber","R lare"),("dormir","R sule"),("morir","C suma-gune"),
 ("matar","C suma-gune dare"),("nadar","F"),("volar","F"),("caminar","R kalu-duma"),("venir","C duma to me"),("yacer/acostarse","F"),("sentarse","C sede pose"),("estar de pie","F"),
 ("dar","R pema"),("decir","R reka"),("sol","R sade"),("luna","R mune"),("estrella","R sade-lu"),("agua","R suna"),("lluvia","R kuna-suna"),("piedra","F"),("arena","F"),("tierra","R taro"),
 ("nube","R sura-suna"),("humo","F"),("fuego","R pore"),("ceniza","F"),("quemar","C pore dare"),("camino","C duma kore"),("montaña","R taro-go"),("rojo","R rale"),("verde","R nede"),
 ("amarillo","R kale (prov.)"),("blanco","R fale"),("negro","R bore"),("noche","R kuna-bore"),("caliente","R fure-pa"),("frío","R fure-po"),("lleno","R mude"),("nuevo","R tame"),
 ("bueno","R lafe (prov.)"),("redondo","C selo"),("seco","F"),("nombre","R sena-nara"),
]
c = collections.Counter(s.split()[0] for _, s in LISTA)
n = len(LISTA)
print(f"Swadesh-100: {n} conceptos -> con forma {c['R']} ({c['R']*100//n}%), componible {c['C']} ({c['C']*100//n}%), faltan {c['F']} ({c['F']*100//n}%)")
faltan = [k for k, s in LISTA if s.startswith("F")]
print("Faltan:", ", ".join(faltan))
