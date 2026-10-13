# Vocabulario cientifico transcrito de Owee Matematicas 2.0 y Owee Fisica 2.0 (PDF en 03_Material_Ensenanza).
# Las correcciones heredadas (vara->bara, vade->daku, veka->dufa, vola->bola, dira->tora) ya vienen aplicadas.
# formato: (owee, concepto, dominio, seccion)
MAT = "Matemáticas"
FIS = "Física"
RAICES = [
 # --- Matematicas: algebra
 ("banu","número",MAT,"Álgebra"),("kedo","unidad",MAT,"Álgebra"),("bara","variable",MAT,"Álgebra"),("kenu","constante",MAT,"Álgebra"),
 ("reda","resultado",MAT,"Álgebra"),("telu","potencia (exponente)",MAT,"Álgebra"),("raku","raíz matemática",MAT,"Álgebra"),("seka","ecuación",MAT,"Álgebra"),
 ("rebo","expresión matemática",MAT,"Álgebra"),("teda","término matemático",MAT,"Álgebra"),("kofa","coeficiente",MAT,"Álgebra"),("daku","incógnita",MAT,"Álgebra"),
 ("funa","función",MAT,"Álgebra"),("duno","dominio",MAT,"Álgebra"),("remu","rango / imagen",MAT,"Álgebra"),("loge","logaritmo",MAT,"Álgebra"),("seta","conjunto / colección (en matemáticas: conjunto)",MAT,"Álgebra"),
 # geometria
 ("pota","punto geométrico",MAT,"Geometría"),("loka","línea",MAT,"Geometría"),("pana","plano geométrico",MAT,"Geometría"),("dora","dimensión",MAT,"Geometría"),
("selo","círculo",MAT,"Geometría"),("kado","lado geométrico",MAT,"Geometría"),("sufa","superficie",MAT,"Geometría"),("bola","volumen",MAT,"Geometría"),
 # trigonometria
 ("shenu","seno trigonométrico",MAT,"Trigonometría"),("kosu","coseno",MAT,"Trigonometría"),("taga","tangente",MAT,"Trigonometría"),
 # calculo
 ("nufa","infinito",MAT,"Cálculo"),("rata","razón / tasa",MAT,"Cálculo"),("dera","derivada",MAT,"Cálculo"),("koma","acumulación",MAT,"Cálculo"),
 ("tega","integral",MAT,"Cálculo"),("sora","secuencia / sucesión",MAT,"Cálculo"),("geda","serie matemática",MAT,"Cálculo"),
 # estadistica
 ("poba","población estadística",MAT,"Estadística y probabilidad"),("musa","muestra",MAT,"Estadística y probabilidad"),("fere","frecuencia",MAT,"Estadística y probabilidad"),
 ("baga","media / promedio",MAT,"Estadística y probabilidad"),("neda","mediana",MAT,"Estadística y probabilidad"),("foda","moda estadística",MAT,"Estadística y probabilidad"),
 ("desa","dispersión",MAT,"Estadística y probabilidad"),("laku","probabilidad matemática",MAT,"Estadística y probabilidad"),("ranu","azar / aleatorio",MAT,"Estadística y probabilidad"),
 # vectores
 ("dufa","vector",MAT,"Vectores y matrices"),("tora","dirección / orientación",MAT,"Vectores y matrices"),
 ("mata","matriz",MAT,"Vectores y matrices"),("raga","fila",MAT,"Vectores y matrices"),("kola","columna",MAT,"Vectores y matrices"),
 # --- Fisica
 ("akela","aceleración",FIS,"Cinemática"),
 ("gama","masa",FIS,"Dinámica"),("fasa","fuerza física",FIS,"Dinámica"),("shaku","inercia",FIS,"Dinámica"),("mota","momento lineal",FIS,"Dinámica"),
 ("dafu","trabajo físico",FIS,"Dinámica"),("enu","energía",FIS,"Dinámica"),("panu","potencia física",FIS,"Dinámica"),
 ("gadu","gravedad",FIS,"Gravedad y rotación"),("kapa","campo físico",FIS,"Gravedad y rotación"),("sata","fricción",FIS,"Gravedad y rotación"),
 ("lema","elasticidad",FIS,"Gravedad y rotación"),("loda","rotación",FIS,"Gravedad y rotación"),("choma","centro / región central",FIS,"Gravedad y rotación"),
 ("dena","densidad",FIS,"Fluidos"),("pesa","presión",FIS,"Fluidos"),("fuda","fluido",FIS,"Fluidos"),("nosa","viscosidad",FIS,"Fluidos"),
 ("shome","calor (transferencia térmica)",FIS,"Termodinámica"),("tupa","entropía",FIS,"Termodinámica"),
 ("goda","estado sólido",FIS,"Estados de la materia"),("luda","estado líquido",FIS,"Estados de la materia"),("boga","estado gaseoso",FIS,"Estados de la materia"),("pura","plasma",FIS,"Estados de la materia"),
 ("shola","onda",FIS,"Ondas y óptica"),("falo","reflexión",FIS,"Ondas y óptica"),("kuda","refracción",FIS,"Ondas y óptica"),
 ("chaga","carga eléctrica",FIS,"Electricidad"),("eleka","electricidad",FIS,"Electricidad"),("kura","corriente eléctrica",FIS,"Electricidad"),
 ("shelu","potencial eléctrico",FIS,"Electricidad"),("kesa","resistencia eléctrica",FIS,"Electricidad"),("reku","circuito / red conectada",FIS,"Electricidad"),
 ("magu","magnetismo",FIS,"Magnetismo"),
 ("ganu","átomo",FIS,"Física atómica"),("elenu","electrón",FIS,"Física atómica"),("poru","protón",FIS,"Física atómica"),("netu","neutrón",FIS,"Física atómica"),("shara","radiación",FIS,"Física atómica"),
 ("sapa","espacio físico",FIS,"Espacio-tiempo"),
]
# construcciones documentadas (guion = raiz + modificador). (forma, significado, dominio)
COMPUESTOS = [
 ("ga-kado","triángulo",MAT),("fo-kado","cuadrilátero",MAT),("sa-kado","pentágono",MAT),("ku-kado","hexágono",MAT),
 ("du-dora","2D",MAT),("ga-dora","3D",MAT),("seka-rela","sistema de ecuaciones",MAT),("gabu-palo","porcentaje",MAT),
 ("pa-lo-se","mayor o igual",MAT),("po-lo-se","menor o igual",MAT),("pose-mede","coordenada",MAT),
 ("duma-loka","trayectoria",FIS),("gadu-fasa","peso / fuerza gravitatoria",FIS),("gadu-kapa","campo gravitatorio",FIS),("fasa-dure","impulso",FIS),
 ("gama-choma","centro de masa",FIS),("loda-rata","velocidad angular",FIS),("loda-akela","aceleración angular",FIS),("loda-fasa","torque",FIS),
 ("dore-telo","deformación",FIS),("fuda-duma","flujo de fluido",FIS),("fuda-go-fasa","empuje",FIS),("fure-enu","energía térmica",FIS),
 ("fure-telo","cambio de temperatura",FIS),("fure-se","equilibrio térmico",FIS),("shola-dase","longitud de onda",FIS),("shola-gore","amplitud",FIS),
 ("kelo-dure","periodo",FIS),("sone-shola","onda sonora",FIS),("salo-shola","onda luminosa",FIS),("eleka-kapa","campo eléctrico",FIS),
 ("eleka-fasa","fuerza eléctrica",FIS),("shelu-telo","voltaje",FIS),("eleka-enu","energía eléctrica",FIS),("eleka-panu","potencia eléctrica",FIS),
 ("eleka-reku","circuito eléctrico",FIS),("chaga-pa","carga positiva",FIS),("chaga-po","carga negativa",FIS),("magu-kapa","campo magnético",FIS),
 ("magu-fasa","fuerza magnética",FIS),("eleka-magu","electromagnetismo",FIS),("eleka-magu-shola","onda electromagnética",FIS),
 ("ganu-choma","núcleo atómico",FIS),("sapa-tera","espacio-tiempo",FIS),("dase-rata","rapidez (distancia por tiempo)",FIS),("faro-enu","fuerza energética",FIS),
]

# --- Quimica 0.1: PROPUESTA (no auditada). Raices nuevas elegidas sin vecinos a distancia 1 en el lexico actual.
QUI = "Química"
COMPUESTOS += [
 # ángulo y eje: sustituyen a las formas inválidas ango / akso (sin raíz nueva)
 ("tora-telo","ángulo (cambio de dirección)",MAT),("loka-mede","eje (línea de medida)",MAT),("loda-loka","eje de rotación",FIS),
 # Química: TODO por composición, 0 raíces nuevas
 ("ganu-rela","enlace químico",QUI),("ganu-chaga","ion",QUI),("ganu-chaga-pa","catión",QUI),("ganu-chaga-po","anión",QUI),
 ("ganu-dore","elemento químico (forma de átomo)",QUI),("ganu-dore-seta","conjunto de elementos",QUI),("ganu-banu","número atómico",QUI),
 ("ganu-gama","masa atómica",QUI),("ganu-kema","molécula (objeto de átomos)",QUI),("ganu-kema-gama","masa molecular",QUI),
 ("gume-ko","mezcla (materia con materia)",QUI),("gume-rela","compuesto químico (materia unida)",QUI),
 ("luda-ko","disolución (líquido con algo)",QUI),("suna-ko","disolución acuosa",QUI),("luda-ko-bema","concentración",QUI),
 ("poru-pema","ácido (dador de protones)",QUI),("poru-gura","base (receptor de protones)",QUI),("chaga-rela","sal (unión de cargas)",QUI),
 ("poru-telo","reacción ácido-base (transferencia de protones)",QUI),("poru-mede","escala de pH (medida de protones)",QUI),
 ("gume-telo","reacción química",QUI),("gume-telo-galo","catalizador",QUI),("gume-telo-se","equilibrio químico",QUI),("gume-telo-sape","velocidad de reacción",QUI),
 ("pore-gume-telo","combustión",QUI),("elenu-pema","oxidación (ceder electrones)",QUI),("elenu-gura","reducción (ganar electrones)",QUI),
 ("suma-gume","química orgánica (materia de la vida)",QUI),("shome-pema","dar calor (exotérmico)",QUI),("shome-gura","recibir calor (endotérmico)",QUI),
]

# --- Gramatica 1.1, vocabulario cotidiano, astronomia, astrologia y mitologia: PROPUESTA, 0 raices nuevas
GRA, COT, AST, ASL, MIT = "Gramática 1.1", "Cotidiano 0.1", "Astronomía", "Astrología", "Mitología"
COMPUESTOS += [
 # gramatica funcional
 ("ka-kema","qué / cuál",GRA),("tera-fese","siempre",GRA),("tera-no","nunca",GRA),("kema-no","nada",GRA),("nara-no","nadie",GRA),
 ("nara-fese","todos (las personas)",GRA),("kema-fese","todo",GRA),("kema-le","esto",GRA),("kema-lu","aquello",GRA),("kore-le","aquí",GRA),
 ("kore-lu","allí",GRA),("gore-pa-pa","muy grande",GRA),("gore-po-po","muy pequeño",GRA),("re-se","también",GRA),("gura-lena","gracias",GRA),
 ("bosa-rude","perdón",GRA),("pu-reme","adiós / hasta la próxima",GRA),("pu-kelo","otra vez (otro ciclo)",GRA),("be-pose","primero",GRA),("ga-pose","tercero",GRA),
 # verbos y nombres cotidianos
 
 ("kalu-duma","caminar",COT),("loke-suna","llorar",COT),("sabe-lena","reír",COT),("sabe-sone","cantar",COT),("lena-duma","jugar",COT),
 ("nume-reka","pedir",COT),("kera-nume","buscar",COT),("reka-pema","responder",COT),("pu-dure","esperar",COT),("reka-tera","cuento / narración",COT),
 ("sena-nara","nombre (signo de persona)",COT),("ruma-kuna","pájaro",COT),("ruma-suna","pez",COT),("nelo-lena","flor",COT),("saro-kore","país",COT),
 ("sade-kelo","año (ciclo del sol)",COT),("mune-kelo","mes (ciclo de la luna)",COT),("loda-kelo","día (ciclo de rotación)",COT),
 ("suna-gore-pa","mar",COT),("taro-go","montaña",COT),("nelo-gore-pa","árbol",COT),("sura-duma","viento",COT),
 ("sura-suna","nube",COT),("kuna-suna","lluvia",COT),("kuna-bore","noche",COT),("kuna-salo","luz del día (poético)",COT),("mune-salo","luz de luna",COT),
 ("suma-pado","nacimiento",COT),("suma-gune","muerte",COT),("doma-duma","emoción",COT),("doma-bosa","tristeza",COT),
 ("dase-pa","largo",COT),("dase-po","corto",COT),
 # astronomia
 ("gora-fese","universo",AST),("sade-lu","estrella (sol lejano)",AST),("taro-duma","planeta (tierra que se mueve)",AST),("sade-lu-seta","galaxia",AST),
 ("sade-lu-sena","constelación",AST),("sade-rela","sistema solar",AST),("duma-selo","órbita",AST),("sade-kose","eclipse solar",AST),("mune-kose","eclipse lunar",AST),
 ("suna-goda-duma","cometa (hielo móvil)",AST),("kuna-pore","meteoro (fuego del cielo)",AST),("loke-lu","telescopio",AST),("loke-le","microscopio",AST),
 ("gadu-bore","agujero negro",AST),("boga-kuna","nebulosa (gas del cielo)",AST),("sura-taro","atmósfera",AST),("gora-pado","Big Bang (comienzo del universo)",AST),
 # astrologia: 4 elementos x 3 modalidades
 ("pore-pado","Aries (fuego cardinal)",ASL),("taro-dure","Tauro (tierra fija)",ASL),("sura-telo","Géminis (aire mutable)",ASL),("suna-pado","Cáncer (agua cardinal)",ASL),
 ("pore-dure","Leo (fuego fijo)",ASL),("taro-telo","Virgo (tierra mutable)",ASL),("sura-pado","Libra (aire cardinal)",ASL),("suna-dure","Escorpio (agua fija)",ASL),
 ("pore-telo","Sagitario (fuego mutable)",ASL),("taro-pado","Capricornio (tierra cardinal)",ASL),("sura-dure","Acuario (aire fijo)",ASL),("suna-telo","Piscis (agua mutable)",ASL),
 # mitologia
 ("kuna-nara","deidad (persona del cielo)",MIT),("pore-nara","deidad del fuego",MIT),("suna-nara","deidad del agua",MIT),("taro-nara","deidad de la tierra",MIT),
 ("sura-nara","deidad del aire",MIT),("suma-nara","deidad de la vida",MIT),("sade-nara","deidad del sol",MIT),("mune-nara","deidad de la luna",MIT),
 ("suma-gune-nara","deidad de la muerte",MIT),
]

COMPUESTOS += [
 ("du-pose","segundo",GRA),("fo-pose","cuarto",GRA),("sa-pose","quinto",GRA),("ku-pose","sexto",GRA),("mu-pose","séptimo",GRA),("na-pose","octavo",GRA),("she-pose","noveno",GRA),
 ("sade-pado","este (donde nace el sol)",AST),("sade-gune","oeste (donde acaba el sol)",AST),("kore-go","norte (lugar arriba)",AST),("kore-gu","sur (lugar abajo)",AST),
]

# --- Informatica 0.1: PROPUESTA, 0 raices nuevas. (forma, significado, dominio, seccion)
INF = "Informática"
HW, PR, DA, RE, SE, DE, IA = ("Equipos y sistema", "Programación", "Datos", "Redes y web", "Seguridad", "Calidad y depuración", "Inteligencia artificial")
COMPUESTOS += [
 # equipos y sistema
 ("meka-gume","hardware (materia de la máquina)",INF,HW),("meka-gora","sistema operativo (entorno de la máquina)",INF,HW),
 ("loke-tabe","pantalla (superficie para el ojo)",INF,HW),("maku-tabe","teclado (superficie de la mano)",INF,HW),("lu-meka","nube informática (máquina lejana)",INF,HW),
 ("meka-bosa","fallo del equipo (máquina rota)",INF,HW),("pado-telo","reiniciar (cambio al comienzo)",INF,HW),("tame-telo","actualizar (cambio a nuevo)",INF,HW),
 ("cho-be","bit (0-1)",INF,HW),("du-banu","binario (número dos)",INF,HW),
 # programacion
 ("mado-foma","programa / software (reglas de cálculo)",INF,PR),("mode-mado","algoritmo (método de cálculo)",INF,PR),("foma-beka","código (regla escrita)",INF,PR),
 ("foma-reka","lenguaje de programación (comunicación de reglas)",INF,PR),("mado-nara","programador (persona del cálculo)",INF,PR),("nara-kade","usuario (persona que usa)",INF,PR),
 ("kema-dore","clase (forma de objeto)",INF,PR),("funa-kema","método de objeto (función de objeto)",INF,PR),("doke-dore","tipo de dato (forma de datos)",INF,PR),
 ("mado-seta","biblioteca de código (conjunto de código)",INF,PR),("mado-dare","ejecutar (hacer el cálculo)",INF,PR),("beka-telo","compilar (cambiar la escritura)",INF,PR),
 ("ke-no","si no (else)",INF,PR),("tare-no","falso (no verdad)",INF,PR),("telo-tera","evento (cambio en el tiempo)",INF,PR),("sape-mado","rendimiento (velocidad de cálculo)",INF,PR),
 # datos
 ("doke-kopa","archivo (contenedor de datos)",INF,DA),("doke-mena","base de datos (memoria de datos)",INF,DA),("mena-fena","guardar (poner en la memoria)",INF,DA),
 ("sena-rela","cadena de texto (signos unidos)",INF,DA),("doke-raga","lista (datos en fila)",INF,DA),("doke-mata","arreglo / array (datos en matriz)",INF,DA),("nelo-doke","árbol de datos (planta de datos)",INF,DA),
 ("rela-seta","grafo (conjunto de conexiones)",INF,DA),("doke-gura","entrada de datos (datos que entran)",INF,DA),("doke-pema","salida de datos (datos que salen)",INF,DA),
 ("nuse-dare","borrar (hacer vacío)",INF,DA),("dare-se","copiar (hacer igual)",INF,DA),("tera-dore","versión (forma en el tiempo)",INF,DA),("tera-dore-mena","control de versiones (memoria de versiones)",INF,DA),
 # redes y web
 ("rela-kuma","sitio web (hogar de conexión)",INF,RE),("rela-foma","protocolo (reglas de conexión)",INF,RE),
 ("nado-foma","API (acceso con reglas)",INF,RE),("meka-pema","servidor (máquina que da)",INF,RE),("meka-gura","cliente (máquina que recibe)",INF,RE),
 ("reka-rela","correo electrónico (mensaje por conexión)",INF,RE),
 # seguridad
 ("sena-fadu","contraseña (signo de seguridad)",INF,SE),("doke-kose","cifrar (datos cerrados)",INF,SE),("doke-bure","descifrar (datos abiertos)",INF,SE),
 # calidad y depuracion
 ("kare-no","error (no corrección)",INF,DE),("bomo-kera","depurar (obtener el bug)",INF,DE),("kare-mede","prueba / test (medir la corrección)",INF,DE),
 # inteligencia artificial
 ("meka-rena","inteligencia artificial (máquina que piensa)",INF,IA),("meka-tase","aprendizaje automático (máquina que aprende)",INF,IA),("doke-fela","datos de entrenamiento (datos que enseñan)",INF,IA),
]

# Unica raiz nueva de Informatica: bomo = bug (defecto del programa). Mezcla recortada bo(sa) + m(ado), con armonia de vocal o:
# 2 silabas, sin vecinos acusticos en el lexico, ligada a mado (informatica) y bosa (rotura).
RAICES += [("bomo","bug (defecto del programa)",INF,DE)]

# --- Interfaz (UI) para oweelinux / sitios web: PROPUESTA, 0 raices nuevas
UI = "Interfaz"
COMPUESTOS += [
 ("foma-fena","configuración (poner reglas)",UI,"Menús y sistema"),("meka-gune","apagar (fin de la máquina)",UI,"Menús y sistema"),("meka-sule","suspender (la máquina duerme)",UI,"Menús y sistema"),
 ("saku-reka","advertencia (mensaje de alerta)",UI,"Menús y sistema"),
 ("seta-nado","menú (conjunto de accesos)",UI,"Elementos"),("loke-kopa","ventana de programa (contenedor para el ojo)",UI,"Elementos"),("tada-sena","botón (signo de contacto)",UI,"Elementos"),
 ("dabo-kopa","papelera (contenedor de suciedad)",UI,"Elementos"),("meka-tabe","escritorio (superficie de la máquina)",UI,"Elementos"),
 ("enu-kopa","batería (contenedor de energía)",UI,"Equipo"),("sone-gore","volumen de sonido (tamaño del sonido)",UI,"Equipo"),("salo-gore","brillo (tamaño de la luz)",UI,"Equipo"),
 ("rela-sura","red inalámbrica (conexión del aire)",UI,"Equipo"),("meka-beka","impresora (máquina de escritura)",UI,"Equipo"),
 ("pe-telo","deshacer (cambio al pasado)",UI,"Acciones"),("pu-telo","rehacer (cambio al futuro)",UI,"Acciones"),("tera-sena","fecha y hora (signo de tiempo)",UI,"Acciones"),
]

# --- Lote 1: cuerpo, naturaleza concreta y posturas (cierra el hueco de Swadesh). 0 raices nuevas. PROPUESTA -> VERIFICADA
CN = "Cuerpo y naturaleza"
CU, NA, AC = "Cuerpo humano y animal", "Naturaleza concreta", "Posturas y acciones"
COMPUESTOS += [
 # cuerpo: piel, fluidos, tejidos
 ("bora-lobe","piel (cubierta del cuerpo)",CN,CU),("suma-suna","sangre (agua de la vida)",CN,CU),("bora-kefe","hueso (soporte del cuerpo)",CN,CU),
 ("bora-gume","carne (materia del cuerpo)",CN,CU),("bora-mase","grasa (recurso del cuerpo)",CN,CU),("bora-suna","sudor (agua del cuerpo)",CN,CU),
 # cabeza
 ("tume-nelo","cabello (planta de la cabeza)",CN,CU),("sone-loke","oreja (ojo del sonido)",CN,CU),("sabe-faro","diente (fuerza de la boca)",CN,CU),
 ("sabe-duma","lengua (movimiento de la boca)",CN,CU),("loke-sabe","cara (ojo y boca)",CN,CU),("tume-rela","cuello (unión de la cabeza)",CN,CU),
 ("tume-rena","cerebro (cabeza que piensa)",CN,CU),
 # tronco y miembros
 ("bora-kopa","vientre / abdomen (contenedor del cuerpo)",CN,CU),("doma-kopa","pecho (contenedor del corazón)",CN,CU),("sura-kopa","pulmón (contenedor de aire)",CN,CU),
 ("fame-kopa","estómago (contenedor de comida)",CN,CU),("bora-gase","hígado (limpieza del cuerpo)",CN,CU),("maku-rela","brazo (unión de la mano)",CN,CU),
 ("maku-palo","dedo (parte de la mano)",CN,CU),("maku-fese","uña (límite de la mano)",CN,CU),("kalu-gune","pie (fin de la pierna)",CN,CU),("kalu-telo","rodilla (cambio de la pierna)",CN,CU),
 # animales
 ("bora-gune","cola (fin del cuerpo)",CN,CU),("tume-faro","cuerno (fuerza de la cabeza)",CN,CU),("ruma-kuna-lobe","pluma (cubierta del pájaro)",CN,CU),
 ("pado-kopa","huevo (contenedor del comienzo)",CN,CU),("naku-nobe","leche (bebida del hijo)",CN,CU),("ruma-lore","mascota (animal de afecto)",CN,CU),
 # tierra, agua, fuego, aire
 ("taro-goda","piedra (tierra sólida)",CN,NA),("taro-gore-po","arena (tierra pequeña)",CN,NA),("taro-suna","barro (tierra y agua)",CN,NA),("taro-sura","polvo (tierra en el aire)",CN,NA),
 ("pore-sura","humo (aire de fuego)",CN,NA),("pore-taro","ceniza (tierra de fuego)",CN,NA),("pore-salo","llama (luz de fuego)",CN,NA),
 ("suna-goda","hielo (agua sólida)",CN,NA),("kuna-suna-goda","nieve (hielo del cielo)",CN,NA),("suna-boga","vapor (agua gaseosa)",CN,NA),
 ("kuna-sone","trueno (sonido del cielo)",CN,NA),("kuna-faro","rayo (fuerza del cielo)",CN,NA),("suna-taro","isla (tierra del agua)",CN,NA),
 ("taro-nuse","cueva (tierra vacía)",CN,NA),("suna-nuse","seco (agua vacía)",CN,NA),("suna-mude","húmedo (lleno de agua)",CN,NA),("selo-dore","redondo (forma de círculo)",CN,NA),
 # plantas
 ("nelo-saro","bosque (comunidad de plantas)",CN,NA),("nelo-fame","fruta / alimento vegetal (comida de planta)",CN,NA),("nelo-maku","hoja (mano de la planta)",CN,NA),("nelo-taro","raíz de planta (planta de tierra)",CN,NA),
 ("nelo-lobe","corteza (cubierta de planta)",CN,NA),("pado-nelo","semilla (comienzo de planta)",CN,NA),("nelo-rela","rama (unión de la planta)",CN,NA),("nelo-bora","tronco (cuerpo de planta)",CN,NA),
 # posturas y acciones del cuerpo
 ("kalu-kefe","estar de pie (la pierna sostiene)",CN,AC),("bora-gu","acostarse (cuerpo abajo)",CN,AC),("sede-pose","sentarse (postura de asiento)",CN,AC),("sabe-bosa","morder (romper con la boca)",CN,AC),
]
# --- Interfaz del sitio (para el modo inmersion): PROPUESTA -> VERIFICADA
SI = "Sitio"
COMPUESTOS += [
 ("reka-doke","diccionario (información de la comunicación)",SI,"Navegación"),("lodu-lena","literatura (lectura agradable)",SI,"Navegación"),("tase-palo","lección (parte del aprender)",SI,"Navegación"),
 ("tase-daro","ejercicio (trabajo de aprender)",SI,"Navegación"),("tase-kelo","curso (ciclo de aprendizaje)",SI,"Navegación"),("reka-seta","vocabulario (conjunto de palabras)",SI,"Navegación"),
]

# --- Reconciliacion con el Primer Diccionario Conceptual 1.0 (2026-10-12): las formas ya existentes mandan.
# Sentidos con el patron percepcion + estimulo (luma-salo ver, luma-sone oir ya existen en el Primer Diccionario)
COMPUESTOS += [
 ("luma-sura","oler (percibir el aire)",COT),("luma-fame","saborear (percibir la comida)",COT),("luma-tada","tocar (percibir el contacto)",COT),
 # fisica: formas usadas en la guia 2.0 que faltaban en el lexico
 ("no-duma","reposo (no movimiento)",FIS),("no-telo","conservación (ausencia de cambio)",FIS),("pema-enu","emisión de energía",FIS),
 ("gura-enu","absorción de energía",FIS),("fuda-duma-rata","caudal (tasa de flujo de fluido)",FIS),("dore-fese","contorno (límite de la forma)",MAT),
]

# --- Lote 2: vida diaria (calendario, geografia, familia, comida, casa y ropa, salud, dinero, transporte). 0 raices nuevas.
V2 = "Vida diaria (lote 2)"
CT, GE, FA, CC, CR, SA, DI, TR = ("Calendario y tiempo", "Geografía", "Familia y personas", "Comida y cocina", "Casa y ropa", "Salud", "Dinero y comercio", "Transporte y viaje")
COMPUESTOS += [
 ("te-loda-kelo","hoy (el día de ahora)",V2,CT),("pe-loda-kelo","ayer (el día anterior)",V2,CT),("pu-loda-kelo","mañana, el día siguiente (el día posterior)",V2,CT),
 ("loda-kelo-pado","amanecer (comienzo del día)",V2,CT),("loda-kelo-gune","tarde (fin del día)",V2,CT),("fame-gore-pa","almuerzo (comida grande)",V2,CT),
 ("pado-fame","desayuno (comida del comienzo)",V2,CT),("gune-fame","cena (comida del final)",V2,CT),("mu-loda-kelo","semana (siete días)",V2,CT),
 ("sade-kelo-palo","estación del año (parte del año)",V2,CT),("fure-pa-tera","verano (tiempo caliente)",V2,CT),("fure-po-tera","invierno (tiempo frío)",V2,CT),
 ("suna-tera","época de lluvias (tiempo de agua)",V2,CT),("suna-nuse-tera","época seca (tiempo sin agua)",V2,CT),
 ("taro-gore-pa","continente (gran tierra)",V2,GE),("kuma-seta","ciudad / pueblo (conjunto de casas)",V2,GE),("bade-kore","capital (lugar de autoridad)",V2,GE),
 ("saro-fese","frontera (límite de la comunidad)",V2,GE),("kore-sena","mapa (signo de lugar)",V2,GE),("duma-kore","camino / ruta (lugar de movimiento)",V2,GE),
 ("suna-go-kore","puente (lugar sobre el agua)",V2,GE),("taro-gu","valle (tierra abajo)",V2,GE),("suna-taro-fese","costa (límite del agua y la tierra)",V2,GE),
 ("taro-suna-nuse","desierto (tierra sin agua)",V2,GE),("taro-pore","volcán (tierra de fuego)",V2,GE),
 ("pade-pade","abuelo/a (progenitor del progenitor)",V2,FA),("naku-naku","nieto/a (descendiente del descendiente)",V2,FA),("pade-sare","tío/a (hermano/a del progenitor)",V2,FA),
 ("sare-naku","sobrino/a (hijo/a del hermano/a)",V2,FA),("pade-sare-naku","primo/a (hijo/a del tío/a)",V2,FA),("lore-rela","pareja / cónyuge (unión de afecto)",V2,FA),
 ("kuma-le-nara","vecino/a (persona de la casa cercana)",V2,FA),("naku-tame","bebé (descendiente nuevo)",V2,FA),("nara-tame","joven (persona nueva)",V2,FA),
 ("nara-gore-pa","adulto/a (persona grande)",V2,FA),("nara-gule","anciano/a (persona vieja)",V2,FA),
 ("pore-dare","cocinar (hacer con fuego)",V2,CC),("fame-kore","cocina (lugar de comida)",V2,CC),("fame-tabe","plato (superficie de comida)",V2,CC),
 ("nobe-kopa","vaso (contenedor de bebida)",V2,CC),("pore-kopa","olla (contenedor de fuego)",V2,CC),("fame-feke","cubierto (herramienta de comida)",V2,CC),
 ("bosa-feke","cuchillo (herramienta de romper)",V2,CC),("fame-moke","hambre (necesidad de comida)",V2,CC),("nobe-moke","sed (necesidad de bebida)",V2,CC),
 ("lena-sabe","sabroso (agrado de la boca)",V2,CC),
 ("kuma-palo","habitación (parte de la casa)",V2,CR),("sule-kore","dormitorio (lugar de dormir)",V2,CR),("gase-kore","baño (lugar de limpieza)",V2,CR),
 ("reme-kore","sala (lugar de amistad)",V2,CR),("nelo-kore","jardín (lugar de plantas)",V2,CR),("loke-nado","ventana de la casa (acceso del ojo)",V2,CR),
 ("kuma-fese","pared (límite de la casa)",V2,CR),("kuma-tabe","suelo (superficie de la casa)",V2,CR),("go-nado","escalera (acceso hacia arriba)",V2,CR),
 ("nado-feke","llave (herramienta de acceso)",V2,CR),("sule-tabe","cama (superficie de dormir)",V2,CR),("salo-feke","lámpara (herramienta de luz)",V2,CR),
 ("tume-bume","sombrero (ropa de la cabeza)",V2,CR),("doma-bume","camisa (ropa del pecho)",V2,CR),("kalu-bume","pantalón (ropa de la pierna)",V2,CR),
 ("kalu-gune-bume","zapato (ropa del pie)",V2,CR),("maku-bume","guante (ropa de la mano)",V2,CR),
 ("sado-bosa","enfermedad (rotura de la salud)",V2,SA),("bosa-dune","dolor (sentir rotura)",V2,SA),("sado-feke","medicina (herramienta de salud)",V2,SA),
 ("sado-nara","médico (persona de salud)",V2,SA),("sado-kuma","hospital (casa de salud)",V2,SA),("bora-fure-pa","fiebre (cuerpo caliente)",V2,SA),
 ("bora-bosa","herida (rotura del cuerpo)",V2,SA),("sado-rude","curar (reparar la salud)",V2,SA),
 ("bado-feke","dinero (herramienta de valor)",V2,DI),("kera-fedo","comprar (obtener con pago)",V2,DI),("pema-fedo","vender (dar con pago)",V2,DI),
 ("kume-kuma","tienda (casa de intercambio)",V2,DI),("kume-kore","mercado (lugar de intercambio)",V2,DI),("bado-kopa","banco (contenedor de valor)",V2,DI),
 ("bado-pa","caro / valioso (valor más)",V2,DI),("bado-po","barato / de poco valor (valor menos)",V2,DI),("fedo-no","gratis (sin pago)",V2,DI),("fedo-pu","deuda (pago futuro)",V2,DI),
 ("daro-fedo","salario (pago del trabajo)",V2,DI),
 ("meka-duma","vehículo (máquina de movimiento)",V2,TR),("taro-meka","coche (máquina de tierra)",V2,TR),("suna-meka","barco (máquina de agua)",V2,TR),
 ("sura-meka","avión (máquina de aire)",V2,TR),("duma-lu","viaje (movimiento lejano)",V2,TR),("duma-nara","viajero (persona que se mueve)",V2,TR),
 ("suna-meka-kuma","puerto (casa de barcos)",V2,TR),("sura-meka-kuma","aeropuerto (casa de aviones)",V2,TR),("nado-sena","boleto (signo de acceso)",V2,TR),
 ("bume-kopa","maleta (contenedor de ropa)",V2,TR),
]

# --- Practicidad (2026-10-12): categorias de animales en lugar de una palabra por especie, orientacion y terminal. 0 raices nuevas.
COMPUESTOS += [
 ("ruma-daro","animal de trabajo (animal + trabajo)",V2,"Animales"),("ruma-fame","animal de alimento / ganado (animal + comida)",V2,"Animales"),
 ("ruma-taro","animal terrestre (animal + tierra)",V2,"Animales"),
 ("doma-kado","izquierda (el lado del corazón)",V2,"Orientación"),("doma-kado-no","derecha (el lado sin corazón)",V2,"Orientación"),
 ("duma-kuma","estación / terminal (casa del movimiento)",V2,GE),
]

# --- Escritorio (para oweelinux): nombres genericos de programas y ajustes. 0 raices nuevas.
# Revision 2026-10-13: se evito el patron X-ado-feke (nado/mado/sado/bado-feke sonaban casi igual) y 'beka-feke' (= tambien "boligrafo").
ES = "Escritorio"
EA, EB = "Programas", "Ajustes y sistema"
COMPUESTOS += [
 ("lodu-beka","editor / procesador de texto (lectura y escritura)",ES,EA),("foma-lodu-beka","editor de código (leer y escribir código)",ES,EA),
 ("gora-rela-duma","navegador web (moverse por internet)",ES,EA),("doke-kopa-mado","gestor de archivos (procesar archivos)",ES,EA),
 ("salo-sena","imagen (signo de luz)",ES,EA),("salo-sena-mado","editor de imágenes (procesar imágenes)",ES,EA),
 ("lodu-beka-seta","suite ofimática (conjunto de programas de texto)",ES,EA),("banu-mata","hoja de cálculo (números en matriz)",ES,EA),
 ("banu-meka","calculadora (máquina de números)",ES,EA),("meka-paku","monitor del sistema (atención a la máquina)",ES,EA),
 ("tera-mede-meka","reloj (máquina de medir el tiempo)",ES,EA),
 ("pose-feke","ratón / puntero (herramienta de posición)",ES,EB),("nara-fadu","privacidad (seguridad de la persona)",ES,EB),("mena-kopa","almacenamiento (contenedor de memoria)",ES,EB),
 ("loke-tabe-lobe","fondo de pantalla (cubierta de la pantalla)",ES,EB),
]

# --- Lote 3: ciencia y sociedad (biologia, tierra y clima, educacion, derecho y politica, economia, lengua, artes y musica, cultura). 0 raices nuevas.
L3 = "Ciencia y sociedad (lote 3)"
COMPUESTOS += [
 ("suma-kedo","célula (unidad de vida)",L3,"Biología"),
 ("suma-bora","organismo (cuerpo de vida)",L3,"Biología"),
 ("suma-seta","especie (forma de vida)",L3,"Biología"),
 ("suma-doke","gen (información de vida)",L3,"Biología"),
 ("suma-telo-tera","evolución (cambio de la vida en el tiempo)",L3,"Biología"),
 ("suma-rela","ecosistema (unión de vida)",L3,"Biología"),
 ("suma-kuma","hábitat (lugar de vida)",L3,"Biología"),
 ("nelo-salo-dare","fotosíntesis (la planta hace con luz)",L3,"Biología"),
 ("sura-gura","respiración (recibir aire)",L3,"Biología"),
 ("fame-bora-telo","digestión (cambio de la comida)",L3,"Biología"),
 ("suma-dare","reproducción (hacer vida)",L3,"Biología"),
 ("gore-pa-telo","crecimiento (cambio de tamaño)",L3,"Biología"),
 ("suma-gore-po","microbio (vida menor)",L3,"Biología"),
 ("ku-kalu","insecto (animal pequeño)",L3,"Biología"),
 ("luma-nado","nervio (conexión de percepción)",L3,"Biología"),
 ("bora-faro","músculo (fuerza del cuerpo)",L3,"Biología"),
 ("taro-gume","mineral (materia de la tierra)",L3,"Tierra y clima"),
 ("taro-fame","suelo fértil (tierra de vida)",L3,"Tierra y clima"),
 ("taro-faro-duma","terremoto (rotura de la tierra)",L3,"Tierra y clima"),
 ("sura-fure-tera","clima (aire y temperatura)",L3,"Tierra y clima"),
 ("kuna-faro-suna","tormenta (fuerza y agua del cielo)",L3,"Tierra y clima"),
 ("suna-taro-mude","inundación (el agua llena la tierra)",L3,"Tierra y clima"),
 ("suna-nuse-dure","sequía (falta de agua prolongada)",L3,"Tierra y clima"),
 ("suna-gora","océano (agua del mundo)",L3,"Tierra y clima"),
 ("taro-go-seta","cordillera (conjunto de montañas)",L3,"Tierra y clima"),
 ("dabo-gora","contaminación (suciedad del entorno)",L3,"Tierra y clima"),
 ("kade-pu-kelo","reciclaje (usar en ciclo)",L3,"Tierra y clima"),
 ("tase-kuma","escuela (casa de aprender)",L3,"Educación"),
 ("fela-nara","maestro (persona que enseña)",L3,"Educación"),
 ("tase-nara","alumno (persona que aprende)",L3,"Educación"),
 ("beka-seta","libro (objeto de escritura)",L3,"Educación"),
 ("beka-feke","bolígrafo / lápiz (herramienta de escritura)",L3,"Educación"),
 ("tase-mede","examen (medir el aprendizaje)",L3,"Educación"),
 ("tase-bado","calificación (valor del aprendizaje)",L3,"Educación"),
 ("lare-kuma","universidad (casa del saber)",L3,"Educación"),
 ("lodu-kuma","biblioteca pública (casa de lectura)",L3,"Educación"),
 ("lare-seta","ciencia (saber con reglas)",L3,"Educación"),
 ("lare-kera","investigación (obtener saber)",L3,"Educación"),
 ("soma-foma","teoría (conjunto de ideas)",L3,"Educación"),
 ("lare-dare","experimento (medir para saber)",L3,"Educación"),
 ("foma-bade","ley (regla de la autoridad)",L3,"Derecho y política"),
 ("pase-pode","derecho a algo (poseer la posibilidad)",L3,"Derecho y política"),
 ("kare-foma","justicia (regla correcta)",L3,"Derecho y política"),
 ("bade-saro","gobierno (autoridad de la comunidad)",L3,"Derecho y política"),
 ("dese-saro","elección (decisión de la comunidad)",L3,"Derecho y política"),
 ("dese-pema","voto (dar la decisión)",L3,"Derecho y política"),
 ("foma-bosa","delito (rotura de la regla)",L3,"Derecho y política"),
 ("foma-nara","juez (persona de la ley)",L3,"Derecho y política"),
 ("foma-fadu","policía (seguridad de la regla)",L3,"Derecho y política"),
 ("foma-fadu-nara","agente de policía (persona de la policía)",L3,"Derecho y política"),
 ("foma-kume","contrato (unión de reglas)",L3,"Derecho y política"),
 ("malo-saro","paz (calma de la comunidad)",L3,"Derecho y política"),
 ("naro-bosa","guerra (rotura entre grupos)",L3,"Derecho y política"),
 ("faro-naro","ejército (grupo de fuerza)",L3,"Derecho y política"),
 ("suma-gune-feke","arma (herramienta de muerte)",L3,"Derecho y política"),
 ("saro-nara","ciudadano (persona de la comunidad)",L3,"Derecho y política"),
 ("duma-pode","libertad (poder moverse)",L3,"Derecho y política"),
 ("mase-kume","economía (recursos e intercambio)",L3,"Economía"),
 ("daro-saro","empresa (comunidad de trabajo)",L3,"Economía"),
 ("daro-bade","jefe (autoridad del trabajo)",L3,"Economía"),
 ("bade-fedo","impuesto (pago a la autoridad)",L3,"Economía"),
 ("bado-kera","ganancia (obtener valor)",L3,"Economía"),
 ("bado-gune","pérdida (rotura del valor)",L3,"Economía"),
 ("mase-mude","riqueza (recursos llenos)",L3,"Economía"),
 ("mase-nuse","pobreza (recursos vacíos)",L3,"Economía"),
 ("dare-kema","producto (objeto hecho)",L3,"Economía"),
 ("saro-reka","idioma (comunicación de una comunidad)",L3,"Lengua"),
 ("reka-palo","palabra (parte de la comunicación)",L3,"Lengua"),
 ("reka-fese","oración (comunicación completa)",L3,"Lengua"),
 ("sone-palo","sílaba (parte del sonido)",L3,"Lengua"),
 ("reka-duma","verbo (palabra de acción)",L3,"Lengua"),
 ("reka-kema","sustantivo (palabra de objeto)",L3,"Lengua"),
 ("reka-lafe","adjetivo (palabra de forma)",L3,"Lengua"),
 ("reka-dore-foma","gramática (reglas de la forma de comunicación)",L3,"Lengua"),
 ("telo-reka","traducción (cambio de comunicación)",L3,"Lengua"),
 ("telo-reka-nara","traductor (persona que traduce)",L3,"Lengua"),
 ("soma-karo","significado (idea de la comunicación)",L3,"Lengua"),
 ("lena-dare","arte (hacer lo agradable)",L3,"Artes y música"),
 ("lena-dare-nara","artista (persona que hace arte)",L3,"Artes y música"),
 ("lena-sone","música (sonido agradable)",L3,"Artes y música"),
 ("lena-sone-feke","instrumento musical (herramienta de sonido)",L3,"Artes y música"),
 ("sone-sena","nota musical (signo de sonido)",L3,"Artes y música"),
 ("sone-kelo","ritmo (ciclo de sonido)",L3,"Artes y música"),
 ("sone-duma","melodía (movimiento del sonido)",L3,"Artes y música"),
 ("sone-rela","armonía (unión de sonidos)",L3,"Artes y música"),
 ("sone-nuse","silencio (sonido vacío)",L3,"Artes y música"),
 ("sabe-sone-nara","cantante (persona que canta)",L3,"Artes y música"),
 ("lena-bora-duma","danza (movimiento del cuerpo)",L3,"Artes y música"),
 ("salo-sena-dare","dibujo / pintura (hacer imagen)",L3,"Artes y música"),
 ("salo-sena-kera","fotografía (obtener imagen)",L3,"Artes y música"),
 ("salo-sena-duma","película (imagen en movimiento)",L3,"Artes y música"),
 ("mena-tera","historia (información del tiempo)",L3,"Cultura"),
 ("saro-mena","cultura (memoria de la comunidad)",L3,"Cultura"),
 ("naro-lena","fiesta (grupo agradable)",L3,"Cultura"),
 ("feke-lare","tecnología (saber de herramientas)",L3,"Cultura"),
]
