#!/usr/bin/env python3
"""Cobertura sobre la lista Swadesh de 100 palabras (medida estandar de vocabulario basico entre lenguas).
R = ya hay forma en el lexico; C = se puede componer con raices existentes; F = falta.
La clasificacion es un juicio de trabajo; sirve para priorizar el vocabulario nuevo."""
import collections
LISTA = [
 ("yo","R me"),("tú","R tu"),("nosotros","R mene (prov.)"),("este","R kema-le"),("ese/aquel","R kema-lu"),("quién","R ka-nara"),("qué","R ka-kema"),("no","R no"),
 ("todo","R kema-fese"),("mucho","R bema-pa"),("uno","R be"),("dos","R du"),("grande","R gore-pa"),("largo","R dase-pa"),("pequeño","R gore-po"),
 ("mujer","R nara (neutro)"),("hombre","R nara (neutro)"),("persona","R nara"),("pez","R ruma-suna"),("pájaro","R ruma-kuna"),("perro","C ruma-lore (categoría) o ruma-taro"),
 ("piojo","F"),("árbol","R nelo-gore-pa"),("semilla","R pado-nelo"),("hoja","R nelo-maku"),("raíz (planta)","R nelo-taro"),("corteza","R nelo-lobe"),("piel","R bora-lobe"),("carne","R bora-gume"),("sangre","R suma-suna"),("hueso","R bora-kefe"),
 ("grasa","R bora-mase"),("huevo","R pado-kopa"),("cuerno","R tume-faro"),("cola","R bora-gune"),("pluma","R kafumo"),("cabello","R tume-nelo"),("cabeza","R tume"),("oreja","R sone-loke"),("ojo","R loke"),("nariz","R noke"),("boca","R sabe"),
 ("diente","R sabe-faro"),("lengua (órgano)","R sabe-duma"),("uña/garra","R maku-fese"),("pie","R kalu-gune"),("rodilla","R kalu-telo"),("mano","R maku"),("vientre","R bora-kopa"),("cuello","R tume-rela"),("pecho/seno","R doma-kopa"),("corazón","R doma"),
 ("hígado","R bora-gase"),("beber","C nobe pume"),("comer","R pume"),("morder","R sabe-bosa"),("ver","R luma-salo"),("oír","R luma-sone"),("saber","R lare"),("dormir","R sule"),("morir","C suma-gune"),
 ("matar","C suma-gune dare"),("nadar","C suna bo duma"),("volar","C sura bo duma"),("caminar","R kalu-duma"),("venir","C duma to me"),("yacer/acostarse","R bora-gu"),("sentarse","R sede-pose"),("estar de pie","R kalu-kefe"),
 ("dar","R pema"),("decir","R reka"),("sol","R sade"),("luna","R mune"),("estrella","R sade-lu"),("agua","R suna"),("lluvia","R kuna-suna"),("piedra","R taro-goda"),("arena","R taro-gore-po"),("tierra","R taro"),
 ("nube","R sura-suna"),("humo","R pore-sura"),("fuego","R pore"),("ceniza","R pore-taro"),("quemar","C pore dare"),("camino","C duma kore"),("montaña","R taro-go"),("rojo","R rale"),("verde","R nede"),
 ("amarillo","R kale (prov.)"),("blanco","R fale"),("negro","R bore"),("noche","R kuna-bore"),("caliente","R fure-pa"),("frío","R fure-po"),("lleno","R mude"),("nuevo","R tame"),
 ("bueno","R lafe (prov.)"),("redondo","R selo-dore"),("seco","R suna-nuse"),("nombre","R sena-nara"),
]
c = collections.Counter(s.split()[0] for _, s in LISTA)
n = len(LISTA)
print(f"Swadesh-100: {n} conceptos -> con forma {c['R']} ({c['R']*100//n}%), componible {c['C']} ({c['C']*100//n}%), faltan {c['F']} ({c['F']*100//n}%)")
faltan = [k for k, s in LISTA if s.startswith("F")]
print("Faltan:", ", ".join(faltan))
