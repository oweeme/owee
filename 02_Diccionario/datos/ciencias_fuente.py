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
 ("funa","función",MAT,"Álgebra"),("duno","dominio",MAT,"Álgebra"),("remu","rango / imagen",MAT,"Álgebra"),("loge","logaritmo",MAT,"Álgebra"),("seta","conjunto matemático",MAT,"Álgebra"),
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
 ("loke-luma","ver",COT),("sone-luma","oír",COT),("maku-tada","tocar",COT),("noke-luma","oler",COT),("sabe-luma","saborear",COT),
 ("kalu-duma","caminar",COT),("loke-suna","llorar",COT),("sabe-lena","reír",COT),("sabe-sone","cantar",COT),("lena-duma","jugar",COT),
 ("nume-reka","pedir",COT),("kera-nume","buscar",COT),("reka-pema","responder",COT),("pu-dure","esperar",COT),("reka-tera","cuento / narración",COT),
 ("sena-nara","nombre (signo de persona)",COT),("ruma-kuna","pájaro",COT),("ruma-suna","pez",COT),("nelo-lena","flor",COT),("saro-kore","país",COT),
 ("sade-kelo","año (ciclo del sol)",COT),("mune-kelo","mes (ciclo de la luna)",COT),("loda-kelo","día (ciclo de rotación)",COT),
 ("suna-duma","río",COT),("suna-gore-pa","mar",COT),("taro-go","montaña",COT),("nelo-gore-pa","árbol",COT),("sura-duma","viento",COT),
 ("sura-suna","nube",COT),("kuna-suna","lluvia",COT),("kuna-bore","noche",COT),("kuna-salo","luz del día (poético)",COT),("mune-salo","luz de luna",COT),
 ("suma-pado","nacimiento",COT),("suma-gune","muerte",COT),("doma-duma","emoción",COT),("doma-salo","alegría",COT),("doma-bosa","tristeza",COT),
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
 ("meka-mado","computadora (máquina de cálculo)",INF,HW),("meka-gume","hardware (materia de la máquina)",INF,HW),("meka-gora","sistema operativo (entorno de la máquina)",INF,HW),
 ("loke-tabe","pantalla (superficie para el ojo)",INF,HW),("maku-tabe","teclado (superficie de la mano)",INF,HW),("kuna-meka","nube informática (máquina del cielo)",INF,HW),
 ("meka-bosa","fallo del equipo (máquina rota)",INF,HW),("pado-telo","reiniciar (cambio al comienzo)",INF,HW),("tame-telo","actualizar (cambio a nuevo)",INF,HW),
 ("cho-be","bit (0-1)",INF,HW),("du-banu","binario (número dos)",INF,HW),
 # programacion
 ("mado-foma","programa / software (reglas de cálculo)",INF,PR),("mode-mado","algoritmo (método de cálculo)",INF,PR),("foma-beka","código (regla escrita)",INF,PR),
 ("foma-reka","lenguaje de programación (comunicación de reglas)",INF,PR),("mado-nara","programador (persona del cálculo)",INF,PR),("nara-kade","usuario (persona que usa)",INF,PR),
 ("kema-dore","clase (forma de objeto)",INF,PR),("funa-kema","método de objeto (función de objeto)",INF,PR),("doke-dore","tipo de dato (forma de datos)",INF,PR),
 ("mado-seta","biblioteca (conjunto de código)",INF,PR),("mado-dare","ejecutar (hacer el cálculo)",INF,PR),("beka-telo","compilar (cambiar la escritura)",INF,PR),
 ("ke-no","si no (else)",INF,PR),("tare-no","falso (no verdad)",INF,PR),("telo-tera","evento (cambio en el tiempo)",INF,PR),("sape-mado","rendimiento (velocidad de cálculo)",INF,PR),
 # datos
 ("doke-kopa","archivo (contenedor de datos)",INF,DA),("doke-mena","base de datos (memoria de datos)",INF,DA),("mena-fena","guardar (poner en la memoria)",INF,DA),
 ("sena-rela","cadena de texto (signos unidos)",INF,DA),("doke-raga","lista (datos en fila)",INF,DA),("doke-mata","arreglo / array (datos en matriz)",INF,DA),("nelo-doke","árbol de datos (planta de datos)",INF,DA),
 ("rela-seta","grafo (conjunto de conexiones)",INF,DA),("doke-gura","entrada de datos (datos que entran)",INF,DA),("doke-pema","salida de datos (datos que salen)",INF,DA),
 ("nuse-dare","borrar (hacer vacío)",INF,DA),("dare-se","copiar (hacer igual)",INF,DA),("tera-dore","versión (forma en el tiempo)",INF,DA),("tera-dore-mena","control de versiones (memoria de versiones)",INF,DA),
 # redes y web
 ("rela-gora","internet (conexión del mundo)",INF,RE),("rela-kuma","sitio web (hogar de conexión)",INF,RE),("rela-foma","protocolo (reglas de conexión)",INF,RE),
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
 ("nado-bure","iniciar sesión (abrir acceso)",UI,"Menús y sistema"),("nado-kose","cerrar sesión (cerrar acceso)",UI,"Menús y sistema"),("saku-reka","advertencia (mensaje de alerta)",UI,"Menús y sistema"),
 ("seta-nado","menú (conjunto de accesos)",UI,"Elementos"),("loke-kopa","ventana (contenedor para el ojo)",UI,"Elementos"),("tada-sena","botón (signo de contacto)",UI,"Elementos"),
 ("dabo-kopa","papelera (contenedor de suciedad)",UI,"Elementos"),("meka-tabe","escritorio (superficie de la máquina)",UI,"Elementos"),
 ("enu-kopa","batería (contenedor de energía)",UI,"Equipo"),("sone-gore","volumen de sonido (tamaño del sonido)",UI,"Equipo"),("salo-gore","brillo (tamaño de la luz)",UI,"Equipo"),
 ("rela-sura","red inalámbrica (conexión del aire)",UI,"Equipo"),("beka-meka","impresora (máquina de escritura)",UI,"Equipo"),
 ("pe-telo","deshacer (cambio al pasado)",UI,"Acciones"),("pu-telo","rehacer (cambio al futuro)",UI,"Acciones"),("tera-sena","fecha y hora (signo de tiempo)",UI,"Acciones"),
]
