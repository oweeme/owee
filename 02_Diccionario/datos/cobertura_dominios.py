#!/usr/bin/env python3
"""Cobertura del léxico por áreas de uso diario: hogar, informática (sistema operativo), comprar y vender,
cuerpo humano, cocina y alimentos, agricultura y campo.

Cada área es una lista de trabajo de conceptos en español (no una norma: sirve para priorizar).
Para cada concepto dice si ya había palabra (había), si la añadió un lote nuevo (nuevo, lotes 9-14) o si falta.
Una palabra «cubre» un concepto si el concepto es uno de los significados de su glosa (sin los paréntesis).

    python3 cobertura_dominios.py            resumen y lista de lo que falta
    python3 cobertura_dominios.py --todo     además, cada concepto con su palabra
    python3 cobertura_dominios.py --md       escribe cobertura_dominios.md"""
import pathlib, re, sys
aqui = pathlib.Path(__file__).resolve().parent

AREAS = {
 "Hogar y casa": "casa puerta ventana techo pared suelo escalera cocina baño dormitorio sala comedor habitación jardín patio garaje sótano azotea "
   "mesa silla cama armario estante espejo cortina alfombra almohada manta sábana lámpara llave cerradura timbre ventilador calefacción refrigerador "
   "estufa lavadora escoba basura grifo tubería ducha enchufe interruptor cable foco electricidad televisión radio teléfono reloj valla alquiler dueño "
   "vecino mudarse limpiar barrer lavar buzón papel cepillo peine tijeras aguja toalla jabón mueble edificio calle "
   "madera ladrillo vidrio clavo martillo pintura sofá escritorio vela colchón plancha inodoro bañera",
 "Informática y sistema": "archivo carpeta ruta programa ventana pantalla teclado ratón impresora red internet servidor cliente nube base de datos usuario contraseña "
   "cuenta de usuario sesión administrador permiso instalar desinstalar descargar subir actualizar reiniciar apagar guardar copiar pegar cortar borrar seleccionar "
   "buscar enviar un mensaje recibir un mensaje mensaje notificación correo electrónico enlace sitio web navegador cámara micrófono altavoz audio imagen comprimir "
   "virus informático antivirus cortafuegos copia de seguridad restaurar proceso de programa procesador memoria rápida disco almacenamiento sistema operativo núcleo del sistema "
   "controlador de dispositivo terminal de comandos script bucle programar depurar código sincronizar historial portapapeles pestaña de ventana cargador batería sensor robot "
   "dispositivo aplicación tarea video arranque red social pila cola memoria virtual",
 "Comprar y vender": "comprar vender tienda mercado dinero precio pagar cobrar vuelto moneda billete tarjeta de pago recibo comprador vendedor comerciante descuento "
   "regatear préstamo ahorrar cuenta bancaria banco cajero cajero automático pesar balanza paquete caja bolsa carrito inventario almacén entrega garantía devolver "
   "trueque total a pagar puesto de venta negocio contabilidad presupuesto pedido ganancia pérdida deuda salario impuesto contrato gratis caro barato producto "
   "calidad cantidad oferta factura interés crédito efectivo propina supermercado feria",
 "Cuerpo humano": "cabeza cabello cara ojo oreja nariz boca labio diente lengua garganta cuello hombro brazo codo muñeca mano palma dedo uña pecho espalda vientre "
   "cintura ombligo cadera pierna muslo rodilla tobillo pie talón dedo del pie piel hueso músculo tendón articulación columna vertebral costilla cráneo corazón "
   "pulmón estómago hígado riñón intestino vejiga cerebro vaso sanguíneo sangre saliva lágrima sudor orina excremento aliento voz latido respiración edad embarazo "
   "tos sonrisa mejilla frente ceja párpado pestaña barba mentón huella dactilar cuerpo humano órgano visión oír oler "
   "nuca axila vello dolor fiebre herida estornudo bostezo diarrea",
 "Cocina y alimentos": "cocinar hervir freír hornear asar cortar mezclar pelar lavar calentar enfriar servir comida comer beber cocina horno olla sartén plato vaso cuchara "
   "tenedor cuchillo cubierto jarra botella tabla de cortar receta ingrediente porción crudo cocido podrido sabroso dulce salado amargo picante sal azúcar aceite "
   "harina masa de harina condimento salsa sopa ensalada postre pan arroz papa maíz quinua grano fruta verdura carne pollo pescado huevo leche queso mantequilla jugo "
   "té café cacao plátano yuca palta tomate cebolla zanahoria trigo frijol haba arveja ajo limón naranja manzana uva camote lechuga desayuno almuerzo cena hambre sed "
   "cocinero restaurante panadería carnicería comedor chuño vinagre miel yogur caldo fideo galleta vino cerveza taza colador licuadora mantel servilleta lenteja garbanzo "
   "pimienta papaya piña sandía durazno pera pepino calabaza espinaca repollo choclo",
 "Agricultura y campo": "agricultura agricultor campo de cultivo terreno cultivar sembrar cosechar cosecha época de cosecha regar arar abono canal de riego tractor arado "
   "pala azada hoz granja corral ganadería pastor pasto gallina vaca oveja lana cerdo caballo llama andina perro gato plaga maleza helada silo molino río lago pozo huerto "
   "semilla planta árbol flor hoja raíz de planta tronco rama fruta bosque lluvia sequía estación del año verano invierno época de lluvias época seca suelo fértil "
   "burro pato conejo abeja invernadero terraza de cultivo semillero podar injertar alambre cosechadora establo yunta arriero cooperativa",
 "Saludos y vida social": "hola adiós gracias por favor perdón bienvenido buenos días buenas tardes buenas noches felicidades cumpleaños fiesta regalo invitación invitar "
   "celebrar pastel boda amigo novio esposo visita visitar abrazo beso sonrisa felicitar aniversario brindis música bailar cantar juego jugar nacimiento edad "
   "saludar despedirse presentar conocer encuentro cita juntos",
 "Personas": "hombre mujer niño niña bebé joven anciano chico chica abuelo tío primo esposo vecino señor señora gente persona adulto gemelos",
 "Ropa": "ropa camisa camiseta pantalón falda vestido zapato zapatilla bota sandalia calcetín ropa interior sostén abrigo chaqueta suéter sombrero gorra bufanda "
   "guantes cinturón corbata traje uniforme pijama bolsillo botón cremallera bolso cartera mochila anillo collar arete reloj de pulsera gafas manga tela",
 "Tecnología del hogar": "teléfono celular cargador batería bluetooth wifi parlante auriculares televisión control remoto computadora portátil tableta cámara micrófono "
   "enchufe cable pantalla consola videojuego refrigerador microondas lavadora aspiradora licuadora ventilador aire acondicionado plancha foco linterna router impresora "
   "reloj alarma radio antena",
 "Internet y correo": "internet red correo electrónico mensaje contraseña usuario enlace sitio web página web descargar subir buscar navegador video foto llamada "
   "videollamada chat red social publicar compartir seguir comentario archivo adjunto correo postal carta sobre sello cartero paquete llamar contestar",
 "Viajes": "viaje viajar maleta pasaporte boleto hotel aeropuerto avión tren autobús taxi coche bicicleta moto barco puerto estación mapa turista vacaciones playa "
   "montaña frontera equipaje reserva guía llegar salir camino carretera puente",
 "Jardinería": "jardín flor rosa árbol arbusto césped semilla regar maceta tierra abono podar manguera regadera rastrillo pala hoja rama huerto gusano caracol cactus "
   "plantar crecer",
 "Animales de casa y de campo": "perro gato pájaro pez caballo vaca toro oveja cerdo gallina gallo pollito pato conejo cabra burro loro tortuga ratón mascota",
 "Animales salvajes": "león tigre oso lobo zorro mono elefante jirafa cebra serpiente cocodrilo águila búho ballena delfín tiburón ciervo ardilla rana murciélago "
   "cóndor puma lagarto pingüino",
 "Insectos y bichos": "insecto mosca mosquito hormiga abeja mariposa araña cucaracha escarabajo grillo gusano caracol pulga piojo libélula avispa",
 "Día a día": "despertar levantarse ducharse vestirse desayunar almuerzo descansar dormir cepillo de dientes pasta dental jabón champú toalla espejo peinarse "
   "limpiar hora minuto mañana tarde noche fin de semana feriado llave dinero basura lista tarea esperar ayudar llegar empezar terminar",
}
# conceptos de varias palabras: se separan por espacios, así que se declaran aquí
FRASES = ["base de datos", "cuenta de usuario", "enviar un mensaje", "recibir un mensaje", "correo electrónico", "sitio web", "virus informático", "copia de seguridad",
 "memoria rápida", "proceso de programa", "terminal de comandos", "sistema operativo", "núcleo del sistema", "controlador de dispositivo", "pestaña de ventana", "red social", "memoria virtual", "tarjeta de pago",
 "cuenta bancaria", "cajero automático", "total a pagar", "puesto de venta", "dedo del pie", "columna vertebral", "vaso sanguíneo", "huella dactilar", "cuerpo humano",
 "servir comida", "tabla de cortar", "masa de harina", "campo de cultivo", "época de cosecha", "canal de riego", "llama andina", "raíz de planta", "estación del año",
 "época de lluvias", "época seca", "suelo fértil", "terraza de cultivo", "por favor", "buenos días", "buenas tardes", "buenas noches", "ropa interior", "reloj de pulsera", "control remoto", "aire acondicionado", "página web", "archivo adjunto", "correo postal", "fin de semana", "cepillo de dientes", "pasta dental"]

def conceptos(texto):
    t = " " + texto + " "; out = []
    for f in sorted(FRASES, key=len, reverse=True):
        if f" {f} " in t: out.append(f); t = t.replace(f" {f} ", " § ", 1)
    out += [w for w in t.split() if w != "§"]
    return out

def glosas(m):
    """Significados de una glosa: la parte sin paréntesis, cada alternativa «a / b», los alias entre paréntesis que
    son una sola palabra o frase corta (p. ej. «flujo de agua (río)») y las glosas que empiezan por el concepto
    («ventana de la casa» cubre «ventana»)."""
    base = re.sub(r"\s*\(.*?\)", "", m)
    out = {x.strip().lower().replace("/a", "") for x in base.split(" / ")}
    for par in re.findall(r"\((.*?)\)", m):
        if len(par.split()) <= 2 and not par.startswith(("de ", "del ")): out.add(par.strip().lower())
    out |= {x.split()[0] for x in list(out) if len(x.split()) > 1 and x.split()[1] in ("de", "del", "web", "conectada", "según")}
    return out

L = {}   # concepto -> [(forma, nuevo)]
for f, col in (("lexico.tsv", None), ("lexico_ciencias.tsv", 6)):
    for l in (aqui / f).read_text(encoding="utf8").splitlines()[1:]:
        c = l.split("\t"); nuevo = bool(col) and bool(re.search(r"lote (9|1[0-4])\)", c[col]))
        for g in glosas(c[3]): L.setdefault(g, []).append((c[0], nuevo))

def estado(c):
    ws = L.get(c, [])
    if not ws: return "falta", ""
    if any(not n for _, n in ws): return "había", ", ".join(w for w, n in ws if not n)
    return "nuevo", ", ".join(w for w, _ in ws)

def main():
    todo, md = "--todo" in sys.argv, "--md" in sys.argv
    out = ["# Cobertura de vocabulario por áreas", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
           "| Área | Conceptos | Ya había | Añadido (lotes 9-14) | Falta |", "|---|---|---|---|---|"]
    detalle, tot = [], [0, 0, 0, 0]
    for area, texto in AREAS.items():
        cs = conceptos(texto); est = {c: estado(c) for c in cs}
        n = [sum(1 for e, _ in est.values() if e == k) for k in ("había", "nuevo", "falta")]
        out.append(f"| {area} | {len(cs)} | {n[0]} | {n[1]} | {n[2]} |")
        for i, v in enumerate([len(cs)] + n): tot[i] += v
        detalle.append((area, est))
    out.append(f"| **Total** | {tot[0]} | {tot[1]} | {tot[2]} | {tot[3]} |")
    out += ["", "## Lo que falta (por decidir en el próximo lote)", ""]
    for area, est in detalle: out.append(f"- **{area}:** " + (", ".join(c for c, (e, _) in est.items() if e == "falta") or "—"))
    if todo or md:
        for area, est in detalle:
            out += ["", f"## {area}", "", "| Concepto | Estado | Palabra |", "|---|---|---|"]
            out += [f"| {c} | {e} | {w} |" for c, (e, w) in est.items()]
    texto = "\n".join(out) + "\n"
    if md: (aqui / "cobertura_dominios.md").write_text(texto, encoding="utf8")
    print(texto if not md else f"escrito cobertura_dominios.md ({len(texto.splitlines())} líneas)")

main()
