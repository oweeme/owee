# Owee --- Registro maestro del idioma, escritura y sistema digital

**Estado:** consolidación de todo lo definido desde el inicio del
proyecto hasta Owee Script / Owee Sans 3.0\
**Objetivo:** servir como fuente maestra de referencia para continuar el
idioma, los cuadernos, el diccionario, la fuente, el IME y futuras
implementaciones.

------------------------------------------------------------------------

## 1. Visión general

Owee es un idioma construido orientado a ser práctico, internacional,
fácil de pronunciar, contextualmente expresivo y con una escritura
propia.

Principios del proyecto:

-   no traducir español → Owee palabra por palabra;
-   vocabulario conceptual y composicional;
-   gramática analítica, sin conjugaciones por persona, género o número;
-   pronunciación regular;
-   escritura por bloques silábicos;
-   representación romanizada oficial para aprendizaje y sistemas
    digitales;
-   escritura nativa propia para uso visual;
-   complejidad principalmente visual/compositiva, manteniendo simple la
    lengua hablada;
-   capacidad de funcionar en web, Linux, documentos, aplicaciones y
    posteriormente otras plataformas.

Inspiraciones conceptuales: economía contextual/directa de lenguas como
chino y persa, y claridad fonética comparable a sistemas regulares como
finés o español. Owee no copia ninguna de estas lenguas.

------------------------------------------------------------------------

# PARTE I --- FONOLOGÍA

## 2. Owee Phonology 1.0 --- cerrada

### Vocales

``` text
a e o u
```

La vocal **i no existe en Owee**.

### Alargamiento opcional

``` text
aa ee oo uu
```

### Consonantes

``` text
p b t d k g
f s
m n
l r
sh ch
```

Hay 14 consonantes.

`sh` y `ch` son fonemas individuales.

### R

Owee utiliza una sola `r` suave/corta, comparable a la r simple
española.

No existe `rr`.

### Estructura silábica

Solo:

``` text
V
CV
```

No existen:

-   consonantes finales;
-   grupos consonánticos;
-   letras mudas;
-   tonos gramaticales;
-   vocal `i`.

### Acento

Siempre en la primera sílaba.

### Inventario silábico

14 consonantes × 4 vocales = 56 sílabas CV.

Más 4 vocales aisladas:

``` text
A E O U
```

Total:

**60 sílabas básicas.**

### Matriz canónica

``` text
      A   E   O   U
P     PA  PE  PO  PU
B     BA  BE  BO  BU
T     TA  TE  TO  TU
D     DA  DE  DO  DU
K     KA  KE  KO  KU
G     GA  GE  GO  GU
F     FA  FE  FO  FU
S     SA  SE  SO  SU
M     MA  ME  MO  MU
N     NA  NE  NO  NU
L     LA  LE  LO  LU
R     RA  RE  RO  RU
SH    SHA SHE SHO SHU
CH    CHA CHE CHO CHU
```

------------------------------------------------------------------------

# PARTE II --- GRAMÁTICA

## 3. Filosofía gramatical

Regla general:

> **La estructura comunica lo necesario; el contexto evita repetir lo
> obvio.**

Owee es principalmente analítico.

No hay flexión obligatoria por:

-   persona;
-   género;
-   número;
-   tiempo verbal.

## 4. Orden básico

Orden principal:

``` text
SUJETO + COMPLEMENTOS / OBJETO + ACCIÓN
```

SOV.

Ejemplo:

``` text
me suna nume
```

Análisis:

``` text
me   suna   nume
yo   agua   desear
```

Sentido: «Quiero agua».

## 5. Tiempo

Presente normalmente no marcado.

``` text
pe = anterior / pasado
te = ahora / actual
pu = posterior / futuro
```

Plantilla:

``` text
S + O/C + TIEMPO + V
```

`te` normalmente puede omitirse cuando el presente es evidente.

## 6. Negación

``` text
no
```

Se coloca inmediatamente antes del elemento o acción negados.

Regla general:

``` text
TIEMPO + NEGACIÓN + ACCIÓN
```

## 7. Preguntas

Pregunta sí/no:

``` text
... ka
```

`ka` funciona como partícula interrogativa final.

Interrogativos conceptuales:

``` text
ka-nara = quién
ka-kore = dónde
ka-bema = cuánto/cuántos
ka-kasu = por qué
ka-mode = cómo
ka-tera = cuándo
```

La posición exacta de los interrogativos informativos todavía debe
terminar de normativizarse.

## 8. Pronombres

Confirmados:

``` text
me = yo
tu = tú
ra = él / ella
ne = grupo / plural humano
```

Formas utilizadas y pendientes de auditoría final:

``` text
mene = nosotros
tune = ustedes
rane = ellos/ellas
```

No existe género gramatical obligatorio.

## 9. Artículos

No existen artículos obligatorios equivalentes a:

``` text
el la los las un una
```

## 10. Plural

El plural se interpreta principalmente por contexto.

Se utiliza una marca explícita de grupo solamente cuando sea necesaria.

Regla:

> **No expresar dos veces una información que ya está inequívocamente
> expresada.**

## 11. Modificadores y compuestos

Orden:

``` text
CONCEPTO + MODIFICADOR
```

La misma lógica se aplica a palabras compuestas:

``` text
principal + modificador
```

## 12. Posesión

Orden:

``` text
POSEEDOR + POSEÍDO
```

Ejemplo:

``` text
me kuma
```

= mi casa.

Raíz:

``` text
pase = posesión / pertenencia
```

Ejemplo:

``` text
me kuma pase
```

= tengo una casa / casa pertenece a mí según contexto.

## 13. Identidad, existencia y localización

``` text
gade = identidad
mora = existencia / presencia
```

La localización puede expresarse sin cópula mediante operadores
espaciales.

Ejemplo:

``` text
me kuma bo
```

= estoy en casa.

## 14. Espacio

``` text
bo = interior / en
ba = exterior / fuera
to = hacia
de = desde
go = arriba
gu = abajo
le = cerca
lu = lejos
```

## 15. Lógica y relaciones

``` text
re = y
lo = o
ke = si / condición
ko = con
so = sin
balo = contraste / pero
kasu = causa / razón
mode = manera / método
```

## 16. Cantidad y comparación

``` text
bema = cantidad
pa = más / incremento
po = menos / reducción
se = igualdad / similitud
```

Ejemplos derivados:

``` text
bema-pa = más
bema-po = menos
fure-pa = caliente
fure-po = frío
faro-pa = fuerte
faro-po = débil
gore-pa = grande
gore-po = pequeño
sape-pa = rápido
sape-po = lento
dema-pa = difícil
dema-po = fácil
```

## 17. Modalidad

``` text
pode = posibilidad / capacidad
pelo = responsabilidad / deber
nume = deseo
moke = necesidad
```

Ejemplos:

``` text
daro nume = querer trabajar
daro moke = necesitar trabajar
daro pode = poder trabajar
daro pelo = deber trabajar
```

------------------------------------------------------------------------

# PARTE III --- VOCABULARIO CONCEPTUAL

## 18. Núcleo inicial

``` text
nara = persona
suma = vida
gora = mundo / entorno
kore = lugar
duma = movimiento
dare = hacer / producir
rela = unión / conexión
faro = fuerza (vigor)   [2026-10-12: la energía es `enu`; `faro-enu` = fuerza energética]
salo = luz
suna = agua
gume = materia
sura = aire
fure = temperatura
bema = cantidad
lare = saber / conocer
rena = pensar
sone = sonido
reka = comunicación
luma = percepción
nume = deseo
kuma = hogar
```

## 19. Ontología

``` text
mora = existencia
gade = identidad
kema = objeto
palo = parte
dore = forma
```

## 20. Naturaleza

``` text
taro = tierra
kuna = cielo
pore = fuego
nelo = planta
ruma = animal
sade = sol
mune = luna
```

## 21. Cuerpo y funciones

``` text
bora = cuerpo
maku = mano
tume = cabeza
loke = ojo
sabe = boca
noke = nariz
kalu = pierna
doma = corazón / centro corporal
pume = comer
sule = dormir
```

## 22. Mente

``` text
mena = memoria
karo = entender
dune = sentir / estado interno
soma = idea
paku = atención
```

## 23. Acciones

``` text
kade = usar
pema = dar
gura = recibir
telo = cambiar
bure = abrir
kose = cerrar
delo = tomar
fena = poner
```

## 24. Relaciones humanas

``` text
naro = grupo humano
mela = familia
reme = amistad
daro = trabajo
kume = intercambio
galo = ayuda
```

## 25. Tiempo conceptual

``` text
tera = tiempo
pado = comienzo
gune = fin
dure = duración
kelo = ciclo
```

## 26. Necesidades y hogar

``` text
fame = comida
nobe = bebida
kopa = contenedor
tabe = superficie de apoyo
sede = asiento
bume = ropa
gase = limpieza
dabo = suciedad
moke = necesidad
fadu = seguridad
```

## 27. Cualidades escalares

``` text
gore = tamaño
lafe = calidad / valoración (propuesto; no totalmente congelado)
sape = velocidad
dema = dificultad
kare = corrección
mude = lleno
nuse = vacío
tame = nuevo
gule = viejo
fese = límite / completitud
```

## 28. Colores

``` text
rale = rojo
nede = verde
kulo = azul
kale = amarillo
bore = negro
fale = blanco
```

`kulo` y `kale` requieren todavía prueba auditiva final.

## 29. Familia

``` text
pade = progenitor
naku = descendiente / hijo
sare = hermano/a
```

`sare` es el candidato actual.

## 30. Sociedad

``` text
saro = comunidad
bade = autoridad
foma = regla
dese = decisión
pelo = responsabilidad
```

## 31. Aprendizaje e información

``` text
tase = aprender
fela = enseñar
doke = información / datos
sena = signo
beka = escritura
lodu = lectura
```

## 32. Tecnología

``` text
meka = máquina
mado = cálculo / procesamiento
```

## 33. Objetos y acceso

``` text
lobe = cubierta / techo
feke = herramienta
nado = acceso / paso
```

## 34. Estado físico

``` text
pose = posición / postura
tada = contacto
kefe = sostener / soporte
bosa = rotura
rude = reparación
sado = salud
```

## 35. Emociones

``` text
lena = agrado
saku = alerta / miedo
malo = calma
fada = enojo
lore = afecto
```

## 36. Comercio y valor

``` text
bado = valor
mase = recurso
kera = obtener
fedo = pago
```

## 37. Medición

``` text
mede = medir
dase = distancia
```

## 38. Abstractos

``` text
pode = posibilidad
tare = realidad / verdad
```

------------------------------------------------------------------------

# PARTE IV --- MATEMÁTICAS

## 39. Nombres oficiales de los dígitos

``` text
0 = cho
1 = be
2 = du
3 = ga
4 = fo
5 = sa
6 = ku
7 = mu
8 = na
9 = she
```

## 40. Escalas

``` text
10        = tanu
100       = gabu
1 000     = soku
1 000 000 = benu
```

## 41. Operaciones

``` text
dapa = suma
dopo = resta
kebu = multiplicación
faku = división
se   = igualdad
pa   = mayor / más
po   = menor / menos
doto = separador decimal
palo = parte / fracción
```

La antigua propuesta `por` para porcentaje no está establecida y no debe
adoptarse silenciosamente.

------------------------------------------------------------------------

# PARTE V --- OWEE SCRIPT

## 42. Principio de escritura

Owee utiliza una escritura propia.

Regla fundamental:

> **1 sílaba = 1 bloque visual.**

Dirección:

``` text
izquierda → derecha
```

Una palabra es una secuencia de bloques silábicos.

La escritura romanizada sigue siendo oficial como modo de:

-   aprendizaje;
-   entrada de teclado;
-   intercambio digital;
-   depuración;
-   compatibilidad.

## 43. Estética y construcción

Objetivos:

-   escritura propia, no mezcla de alfabetos existentes;
-   apariencia geométrica + orgánica;
-   apta para escritura manual;
-   deducible, no colección arbitraria de símbolos;
-   formas impresas y manuscritas reconocibles;
-   preferiblemente 1--3 trazos por bloque;
-   evitar puntos minúsculos obligatorios;
-   construcción conceptual sobre celda aproximada;
-   esqueleto consonántico central;
-   extensión vocálica integrada.

## 44. Regla direccional de vocales

``` text
       A
       ↑
E ← [C] → O
       ↓
       U
```

Por tanto:

``` text
A = extensión superior
E = extensión izquierda
O = extensión derecha
U = extensión inferior
```

No se trata de dibujar una flecha literal; la dirección se integra en el
diseño.

Vocales largas pueden representarse mediante una extensión
reconociblemente prolongada o duplicada.

Las vocales aisladas utilizan un portador neutro más la misma regla
direccional.

## 45. Familias consonánticas

Siete familias:

``` text
P/B   = curva lateral
T/D   = arco superior
K/G   = ángulo
F/S   = diagonal curva
M/N   = curva inferior / recipiente
L/R   = curva ascendente
SH/CH = doble curva
```

Transformaciones de pareja:

### Cierre

``` text
P/B
T/D
K/G
M/N
```

### Cruce

``` text
F/S
L/R
SH/CH
```

No se debe usar rotación o espejo como única diferencia entre
consonantes.

## 46. Ejemplos de segmentación

``` text
NARA = NA + RA
SUNA = SU + NA
NUME = NU + ME
```

Frase:

``` text
me suna nume
```

Bloques:

``` text
ME | SU NA | NU ME
```

Compuesto:

``` text
luma-salo
LU-MA + SA-LO
```

## 47. Niveles de escritura previstos

``` text
Nivel 1: romanización
Nivel 2: bloques normales
Nivel 3: escritura avanzada fusionada / fluida
```

El nivel avanzado queda para una fase posterior y nunca debe destruir la
lectura fonética básica.

------------------------------------------------------------------------

# PARTE VI --- ESTÁNDAR DIGITAL

## 48. Romanización como representación digital oficial

Owee Roman no es solamente una transliteración para principiantes.

Es la **representación fonológica digital canónica**.

Arquitectura:

``` text
OWEE ROMAN
    ↓
normalización
    ↓
parser fonológico
    ↓
segmentación V / CV
    ↓
IDs OWEE_SYL_*
    ↓
codificación
    ↓
fuente
    ↓
OWEE SCRIPT
```

Ejemplo:

``` text
me suna nume
↓
me | su-na | nu-me
↓
ME | SU NA | NU ME
↓
[ME] [SU][NA] [NU][ME]
```

## 49. Tres niveles de representación

``` text
Nivel 1: Roman Owee
nara

Nivel 2: representación interna
NA + RA

Nivel 3: Owee Script
[NA][RA]
```

## 50. IDs y Unicode

Los IDs de las sílabas deben ser estables e independientes de:

-   forma del glifo;
-   fuente;
-   punto Unicode provisional.

Primera implementación:

**Unicode Private Use Area (PUA).**

Orden congelado:

``` text
U+E000 A
U+E001 E
U+E002 O
U+E003 U
U+E004 PA
U+E005 PE
...
U+E03B CHU
```

Orden completo:

``` text
A E O U |
PA PE PO PU |
BA BE BO BU |
TA TE TO TU |
DA DE DO DU |
KA KE KO KU |
GA GE GO GU |
FA FE FO FU |
SA SE SO SU |
MA ME MO MU |
NA NE NO NU |
LA LE LO LU |
RA RE RO RU |
SHA SHE SHO SHU |
CHA CHE CHO CHU
```

Los rangos:

``` text
U+E000 – U+E03B = 60 sílabas
U+E03C – U+E03F = reservados
U+E040 – U+E049 = dígitos Owee 0–9
```

Una futura propuesta Unicode puede migrar la codificación sin redefinir
el idioma.

------------------------------------------------------------------------

# PARTE VII --- FUENTES

## 51. Owee Sans 1

Primera fuente funcional.

Formatos producidos:

``` text
TTF
OTF
WOFF2
```

Logró demostrar:

``` text
PUA → fuente → glifo Owee
```

Problema observado en uso real:

-   glifos visualmente pequeños;
-   detalles demasiado finos;
-   lectura difícil a tamaños normales;
-   demasiado espacio alrededor de algunos símbolos.

Aun así, sus glifos constituyen la referencia canónica visual sobre la
que se decidió continuar.

## 52. Owee Sans 2

Fue una exploración de estética:

-   más geométrica;
-   modular;
-   tecnológica.

También añadió una propuesta digital para números.

Sin embargo, la prueba real mostró dos problemas:

1.  cambió demasiado las formas establecidas en los documentos
    educativos;
2.  el generador TTF no conservó correctamente algunos trazos y produjo
    segmentos/cuadrados incorrectos.

Decisión:

**Owee Sans 2 no se considera estándar.**

Sirve como experimento de diseño.

## 53. Owee Sans 3

Objetivo:

-   volver a los glifos canónicos de Owee Sans 1;
-   hacerlos claramente legibles;
-   aumentar el tamaño visual;
-   reducir espacio horizontal;
-   mantener frases compactas;
-   integrar los números oficiales;
-   conservar los mismos PUA de las 60 sílabas.

Criterios de diseño:

``` text
EM:              1000
altura visible:  mayor que Sans 1
advance width:   aproximadamente 650
margen lateral:  reducido
lectura objetivo: 16–20 pt
```

Una frase Owee no debe ocupar innecesariamente mucho más ancho que una
frase romanizada.

Como cada glifo Owee representa una sílaba completa, la escritura tiene
potencial para ser bastante compacta.

## 54. Regla de consistencia tipográfica

Los materiales educativos son una referencia normativa.

La fuente digital debe reproducir el mismo sistema visual.

No se debe:

-   redefinir silenciosamente un glifo;
-   cambiar su valor fonológico;
-   crear otra forma incompatible solamente por estética.

Sí se puede mejorar:

-   grosor;
-   curvas;
-   hinting;
-   proporción;
-   espaciado;
-   tamaño visible;
-   legibilidad.

------------------------------------------------------------------------

# PARTE VIII --- NÚMEROS EN OWEE SCRIPT

## 55. Representación

La pronunciación y el glifo numérico son conceptos relacionados pero
distintos.

Ejemplo:

``` text
2
```

se pronuncia:

``` text
du
```

pero al escribir con teclado Owee, la tecla `2` debe insertar
directamente el glifo numérico Owee para 2.

No es necesario escribir `du`.

## 56. PUA numérico

``` text
0 → U+E040 → cho
1 → U+E041 → be
2 → U+E042 → du
3 → U+E043 → ga
4 → U+E044 → fo
5 → U+E045 → sa
6 → U+E046 → ku
7 → U+E047 → mu
8 → U+E048 → na
9 → U+E049 → she
```

Las formas deben corresponder con los símbolos establecidos en los
materiales de matemáticas Owee, no con una reinterpretación arbitraria.

------------------------------------------------------------------------

# PARTE IX --- IME OWEE / FCITX5

## 57. Motivo del IME

Instalar Owee Sans por sí solo no convierte texto romano.

Una aplicación como OnlyOffice recibe:

``` text
suna
```

como caracteres latinos normales.

La fuente Owee contiene los caracteres PUA, por lo que es necesario:

``` text
teclado romano
→ parser Owee
→ PUA
→ Owee Sans
```

El IME realiza esta conversión.

Se descartó usar ligaduras OpenType para transformar secuencias latinas
automáticamente, porque mezclaría:

-   representación;
-   búsqueda;
-   copia;
-   edición;
-   semántica del texto.

## 58. Comportamiento del IME

Ejemplo:

El usuario escribe:

``` text
suna
```

El preedit puede mostrar:

``` text
suna
```

Al pulsar espacio:

``` text
SU + NA
```

se convierten en los caracteres PUA correspondientes.

Comportamientos definidos:

-   Space confirma palabra;
-   Enter confirma palabra y permite Enter;
-   Backspace edita preedit;
-   Escape cancela;
-   puntuación confirma palabra y continúa;
-   palabra Owee inválida puede conservarse en romano para evitar
    pérdida de datos;
-   `sh` y `ch` se detectan antes que consonantes simples;
-   `i` es inválida;
-   Ctrl/Alt/Super deben pasar atajos al sistema.

## 59. Desarrollo en Deepin 25.2

Entorno comprobado:

``` text
Fcitx5 5.1.12
GCC/G++ 12.3
CMake 3.31.4
```

El primer código falló porque `fcitx::Instance` no estaba declarado por
los includes usados.

Corrección:

``` cpp
#include <fcitx/instance.h>
#include <fcitx/inputcontextmanager.h>
```

Después:

``` text
[100%] Built target owee
```

confirmó la compilación correcta.

## 60. Sistema `/usr` de solo lectura

La instalación de sistema intentó copiar:

``` text
/usr/lib/x86_64-linux-gnu/fcitx5/owee.so
```

Deepin respondió:

``` text
Read-only file system
```

Por tanto se adoptó instalación por usuario:

``` text
~/.local/lib/fcitx5/owee.so
~/.local/share/fcitx5/addon/owee.conf
~/.local/share/fcitx5/inputmethod/owee.conf
```

Finalmente Deepin mostró **Owee** dentro de:

``` text
Bluetooth and Devices
→ Keyboard
→ Input Methods
```

Esto confirmó que el IME fue descubierto y agregado correctamente.

## 61. Validación real

Se logró escribir caracteres Owee desde Fcitx5 en OnlyOffice usando Owee
Sans.

Por tanto quedó demostrada la cadena:

``` text
teclado
→ Fcitx5 Owee
→ parser
→ PUA
→ Owee Sans
→ OnlyOffice
```

------------------------------------------------------------------------

# PARTE X --- VERSIONADO Y ARTEFACTOS

## 62. Documentos creados durante el proyecto

Entre los documentos producidos se encuentran:

``` text
Owee_0.1_resumen_grafico.pdf
Owee_Base_1.0_Guia_Estudio_Practica.pdf
Owee_1.0_Cuaderno_Prueba_Conversacional.pdf
Owee_1.0_Tutorial_Completo_Familias.pdf
Owee_Caligrafia_Escolar_Visual_0.2.pdf
Owee_Matematicas_1.0_Cuaderno_Escolar.pdf
Owee_Matematicas_1.0_Completo.pdf
Owee_1.0_Cuaderno_Intermedio_Completo_6_a_12.pdf
Owee_1.0_Cuaderno_Infantil_5_a_10.pdf
Owee_1.0_Curso_Practico_Adultos.pdf
Owee_1.0_Primer_Diccionario_Conceptual.pdf
Owee_Base_1.0_Especificacion_Normativa_Digital.pdf
Owee_Escritura_y_Glifos_Especificacion_3.0.pdf
```

## 63. Fuentes y glifos creados

``` text
Owee_Script_1.0_Glyph_Master.zip
OweeSans_1.0_Font_Package.zip
Owee Script 2.0 experimental
Owee Sans 3.0
```

## 64. IME

``` text
fcitx5-owee-1.0
fcitx5-owee-1.0.1
fcitx5-owee-1.1-digits
```

------------------------------------------------------------------------

# PARTE XI --- DECISIONES PENDIENTES

## 65. Elementos todavía no completamente congelados

Deben revisarse antes de declarar una especificación lingüística
posterior totalmente cerrada:

-   forma final de `mene`, `tune`, `rane`;
-   posición normativa definitiva de interrogativos informativos;
-   `lafe` como raíz de calidad/valoración;
-   prueba auditiva de `kulo` y `kale`;
-   `sare` como término definitivo para hermano/a;
-   porcentaje: no adoptar `por` sin decisión explícita;
-   reglas definitivas de vocales largas en escritura;
-   escritura avanzada fusionada/fluidificada;
-   signos matemáticos propios más allá de los dígitos;
-   eventual puntuación específicamente Owee;
-   futura migración desde PUA si se busca estandarización Unicode.

## 66. Colisiones y decisiones históricas a recordar

``` text
paku = atención
pore = fuego
gune = fin
kalu = pierna
suma = vida
nara = persona
bure = abrir
```

Formas rechazadas o evitadas:

-   `sume` como azul, por proximidad/conflicto;
-   `nare` como atención;
-   reutilizar `bure` para miedo;
-   introducir la vocal `i`.

------------------------------------------------------------------------

# PARTE XII --- REGLAS PARA CONTINUAR EL PROYECTO

## 67. Regla de compatibilidad

No cambiar una decisión lingüística estable solamente para resolver un
problema de software o tipografía.

Separar siempre:

``` text
IDIOMA
↓
FONOLOGÍA / GRAMÁTICA / VOCABULARIO

ESCRITURA
↓
BLOQUES / GLIFOS

CODIFICACIÓN
↓
IDs / PUA / Unicode

TIPOGRAFÍA
↓
TTF / OTF / WOFF2

ENTRADA
↓
IME / parser / teclado
```

Cada capa puede evolucionar sin redefinir innecesariamente las
anteriores.

## 68. Regla para nuevas fuentes

Antes de declarar estable una nueva versión:

-   probar 12 pt;
-   probar 16 pt;
-   probar 20 pt;
-   probar 26 pt;
-   probar texto continuo;
-   probar números;
-   probar OnlyOffice/LibreOffice;
-   probar navegador;
-   comprobar ancho de oración;
-   comprobar diferencias entre glifos similares;
-   comprobar lectura para usuarios con dificultades visuales.

## 69. Regla de referencia visual

Los cuadernos y especificaciones aprobadas deben permanecer
sincronizados con la fuente.

Si una fuente cambia solamente por legibilidad:

``` text
valor fonológico = igual
ID = igual
PUA = igual
forma reconocible = igual
```

Solo deben variar detalles tipográficos.

------------------------------------------------------------------------

# PARTE XIII --- ESTADO ACTUAL CONSOLIDADO

## 70. Lo que ya funciona

``` text
Fonología Owee 1.0            ✓
60 sílabas básicas            ✓
gramática base                ✓
vocabulario conceptual amplio ✓
sistema numérico              ✓
escritura silábica            ✓
romanización oficial          ✓
PUA provisional               ✓
fuente TTF/OTF/WOFF2          ✓
web                           ✓
Fcitx5 IME                    ✓
Deepin                        ✓
OnlyOffice                    ✓
entrada real de Owee          ✓
```

## 71. Trabajo actual

La prioridad actual es:

**Owee Sans 3 y refinamiento de legibilidad.**

Objetivos inmediatos:

1.  mantener los glifos educativos ya establecidos;
2.  hacerlos mucho más claros;
3.  reducir espacio horizontal;
4.  integrar correctamente los diez números;
5.  probar texto real a tamaños normales;
6.  actualizar el IME con números;
7.  mantener coherencia entre documentación, fuente e implementación.

------------------------------------------------------------------------

# PARTE XIV --- PRINCIPIOS FUNDAMENTALES RESUMIDOS

``` text
OWEE
│
├── 4 vocales: a e o u
├── 14 consonantes
├── 60 sílabas básicas
├── V / CV
├── acento inicial
├── sin i
├── sin género gramatical
├── sin conjugaciones personales
├── SOV
├── contexto antes que redundancia
│
├── escritura:
│   ├── izquierda → derecha
│   ├── 1 sílaba = 1 bloque
│   ├── consonante = esqueleto
│   └── vocal = dirección
│
├── digital:
│   ├── Roman Owee
│   ├── parser
│   ├── IDs estables
│   ├── PUA
│   ├── Owee Sans
│   └── Fcitx5 IME
│
└── objetivo:
    ├── simple al hablar
    ├── compacto al escribir
    ├── legible
    ├── tecnológicamente usable
    └── independiente de una plataforma
```

------------------------------------------------------------------------

## 72. Regla maestra del proyecto

> **Owee debe poder evolucionar técnicamente sin perder su identidad
> lingüística.**

La fonología define lo que se dice.\
La gramática define cómo se organiza.\
Los conceptos definen lo que significa.\
Owee Script define cómo se representa visualmente.\
Los IDs y PUA permiten almacenarlo.\
Owee Sans permite verlo.\
El IME permite escribirlo.

Estas capas deben mantenerse separadas y compatibles.

------------------------------------------------------------------------

## 73. Principio de univocidad (decidido el 2026-10-12)

> **Una forma = un significado.** Una raíz **no se reutiliza** como palabra para otra idea, y ninguna raíz debe cargar dos significados muy distintos.

Si hace falta una idea nueva, se **extiende con guion** a partir de la raíz (`sade-kelo`, «año»). En el alfabeto romano latino el guion lo muestra; en Owee Script lo muestra el nexo de compuesto (§74).

Cada propuesta nueva se comprueba con `02_Diccionario/datos/verificar_propuestas.py` contra todo el léxico (colisiones exactas, vecinos acústicos, formas distintas con el mismo significado).

## 74. Marcas de escritura en Owee Script

| Código | Glifo | Romano | Función |
|---|---|---|---|
| U+E03C | nexo de compuesto (barra baja) | `-` | une los elementos de un compuesto: `sade-kelo` |
| U+E03D | marca de nombre propio (dos puntos) | inicial mayúscula | precede a un nombre propio: `Ana` |

Disponibles en Owee Sans y Owee School 3.3, en `owee.js`/`owee.ts` y en el IME Fcitx5 1.2. Quedan reservados U+E03E y U+E03F.

## 75. Convención de mayúsculas

En romano Owee **solo los nombres propios** llevan mayúscula inicial; no hay mayúscula de inicio de oración. Esto permite distinguir `Kale` (nombre) de `kale` («amarillo»).

## 76. Pronunciación

Cada letra se pronuncia siempre igual, la sílaba es V o CV y el acento va en la primera sílaba de cada palabra (en un compuesto, de cada elemento). Ver la *Guía de pronunciación* (`03_Material_Ensenanza/Pronunciacion/`).

------------------------------------------------------------------------

## 77. Decisiones del 2026-10-12 (confirmadas por el autor)

| Tema | Decisión |
|---|---|
| Fuerza y energía | `faro` = fuerza (vigor); `enu` = energía; `faro-enu` = fuerza energética |
| Cortesía | «por favor» se expresa con `pode ka` («¿puedes…?»); se descartó `ko lena` |
| Relativas | `NOMBRE, [oración con ra], …`: `ra` hace de «que / quien» y toma el papel del nombre en la subordinada (Gramática 1.1 §9) |
| Negativos | el **signo** negativo es `po` (positivo `pa`); la **resta** es `dopo`; la **negación lógica** es `no` |
| Ordinales | número + `pose`: `be-pose`, `du-pose`, `ga-pose`… |
| Nombres propios | inicial mayúscula en romano y glifo U+E03D en Owee Script |
| Comas | **Relativa**: nombre + coma + oración con `ra`. **Vocativo**: nombre + coma + imperativo, pregunta u oración con `tu` (nunca `ra`). **Repetición**: misma palabra repetida. Ninguna se confunde con otra |
| Canto | el acento sigue en la primera sílaba; en el canto se realiza por duración y altura (romance) o por intensidad (marcha); ver Literatura §8.8 |

------------------------------------------------------------------------

## 78. Niveles de estado de las palabras nuevas

| Estado | Significado |
|---|---|
| ESTABLE / AUDITADO 2.0 | ya forma parte del idioma |
| APROBADA | confirmada por el autor (lista `02_Diccionario/datos/aprobadas.txt`) |
| VERIFICADA | pasó la verificación automática y espera aprobación |
| REVISAR | falló una comprobación (se indica el motivo) |
| PROPUESTA | sin verificar |

La verificación (en `generar_ciencias.py`) comprueba: fonología V/CV sin `i`, que cada parte exista, máximo 3 elementos, forma única y significado único. Para aprobar una forma, añádela a `aprobadas.txt`.

## 79. Informática

Dominio nuevo con **58 términos y una sola raíz nueva**, `bomo` («bug», mezcla recortada de **bo**sa + **m**ado, 2 sílabas, sin vecinos acústicos); el resto son compuestos (`meka-mado` computadora, `mado-foma` programa, `doke-kopa` archivo, `gora-rela` internet, `sena-fadu` contraseña…). Ver la guía *Owee Informática* y la tabla de recomendaciones para desarrolladores.

------------------------------------------------------------------------

## 80. Alargamiento expresivo de vocales (decidido el 2026-10-12)

Las vocales largas (`aa ee oo uu`) ya eran opcionales. Se extienden: la **última vocal puede repetirse** (`tareee` = «¡síííí!») para dar énfasis o prolongar una nota al cantar. No crea palabras ni cambia el significado ni el acento. En Owee Script se repite el bloque de la vocal.

------------------------------------------------------------------------

## 81. Integración con oweelinux y sitios web

El idioma se integra por tres vías, todas generadas desde `08_Integracion/datos/ui_glosario.tsv` y el léxico: **paquetes `.deb`** (fuentes, teclado Fcitx5 1.2, locale `qow_BO`), **traducciones** (gettext `qow.po` / `qow@owee.po` y Qt `.ts` con `ts_rellenar.py`) y un **módulo web** (`owee-i18n.js`: Español / Owee / Owee Script). Regla: **se guarda siempre el romano; el Owee Script solo se pinta al mostrar**. Código de idioma de uso privado: `qow`. Ver `08_Integracion/README.md`.

------------------------------------------------------------------------

## 82. Lote 1 y curso por niveles (2026-10-12)

**Lote 1:** 60 términos de cuerpo, animales, naturaleza concreta y posturas, **sin raíces nuevas** (por ejemplo `bora-lobe` piel, `suma-suna` sangre, `sabe-faro` diente, `taro-goda` piedra, `nelo-maku` hoja, `kalu-kefe` estar de pie); con ellos la cobertura de la lista Swadesh-100 pasa del 56 % al 91 %. **Curso:** 4 niveles (0 Ver y oír, 1 Primeras frases A1, 2 Conversar A2, 3 Leer y crear B1) en `03_Material_Ensenanza/Curso/`, con glifos, romano, pronunciación, traducción, ejercicios y lecturas. Todo texto Owee del curso pasa el validador.

------------------------------------------------------------------------

## 83. Reconciliación con el Primer Diccionario y revisión semántica (2026-10-12)

**Regla confirmada:** una forma nueva no puede existir ya en ningún otro lugar del proyecto, ninguna otra forma puede tener su significado, y las raíces que la componen deben tener un significado adecuado a su creación.

- Se incorporaron al léxico los **29 compuestos del *Primer Diccionario Conceptual 1.0*** que no estaban en los datos (`luma-salo` ver, `luma-sone` oír, `reka-sone` hablar, `duma-bo` entrar, `duma-ba` salir, `gora-rela` internet, `nara-daro` trabajador, `dune-lena` alegría, `bado-bema` precio, `mede-tera`…). **Sus formas mandan:** se retiraron los duplicados propios (`loke-luma`, `sone-luma`, `rela-gora`, `suna-kopa`, `doma-salo`…); `nado-bure`/`nado-kose` conservan su sentido («acceso abierto/cerrado») y sirven también para iniciar y cerrar sesión.
- **Sentidos con el patrón percepción + estímulo:** `luma-salo` (ver), `luma-sone` (oír), `luma-sura` (oler), `luma-fame` (saborear), `luma-tada` (tocar).
- **Aprobados 84 términos** tras la revisión (`02_Diccionario/datos/revision_semantica.md`); ajustados 15 por significado de raíces o confusión acústica (p. ej. `go-pose` ≈ `ga-pose`).
- **Lote 2** (92 términos de vida diaria) verificado y en espera de aprobación. `loda` es «rotación» y el día es `loda-kelo`: hoy, ayer y mañana son `te-/pe-/pu-loda-kelo`.

------------------------------------------------------------------------

## 84. Practicidad, lote 2 aprobado y norma de animales (2026-10-12)

**Criterio de practicidad:** una palabra nueva debe ser **fácil de decir y de recordar**: como máximo **3 elementos y 6 sílabas** (la mayoría de las formas, 334 de 757, tienen 4). La verificación automática lo comprueba. Para simplificar: el almuerzo es `fame-gore-pa`, la cena `gune-fame` (como `pado-fame`, desayuno) y caro/barato son `bado-pa` / `bado-po`.

**Aprobados:** el lote 2 completo (92 términos) y `lu-meka` (nube informática). **Una forma = un significado:** se corrigió además `dune-fada` («enojo sentido») para que no duplique a `fada` («enojo»).

**Animales:** no se crea una palabra por especie; se usa **categoría + rasgo** (`ruma-taro`, `ruma-daro`, `ruma-fame`, `ruma-lore`…). Se retiró `ruma-galo`. **Izquierda/derecha:** `doma-kado` / `doma-kado-no`. En espera de confirmación.

------------------------------------------------------------------------

## 85. Aprobaciones del 2026-10-13, escritorio y traductor

**Aprobados:** `ruma-taro`, `ruma-daro`, `ruma-fame`, `duma-kuma` y la pareja de orientación, que cambió a `doma-kado` (izquierda, «el lado del corazón») y `doma-kado-no` (derecha): `doma-le`/`doma-lu` se descartaron porque, hablados, **suenan igual que la frase «corazón cerca/lejos»** (principio de una forma = un significado). Se corrigió además la lección 1.3 del curso para que su frase no coincida con el compuesto `suna-nuse` («seco»).

**Escritorio:** nombres genéricos de programas y ajustes (`salo-sena-mado` editor de imágenes, `gora-rela-duma` navegador web…) y guía por capas para localizar programas (`08_Integracion/escritorio/README.md`). Los **nombres de marca** (GIMP, Firefox, VS Code…) **no se traducen**; se les añade el nombre genérico en Owee. **Traductor asistido** Owee ⇄ español (prototipo) en la página «Traductor».

------------------------------------------------------------------------

## 86. Revisión del escritorio e inglés por pivote (2026-10-13)

**Escritorio:** al revisar choques acústicos y matices se cambiaron 10 nombres: se evitó el patrón `X-ado-feke` (`nado-`, `mado-`, `sado-`, `bado-feke` sonaban casi igual) y `beka-feke` (que también sería «bolígrafo»). Quedan, por ejemplo, `lodu-beka` (editor de texto), `foma-lodu-beka` (editor de código), `doke-kopa-mado` (gestor de archivos), `salo-sena-mado` (editor de imágenes), `banu-mata` (hoja de cálculo), `banu-meka` (calculadora), `pose-feke` (ratón), `meka-paku` (monitor del sistema); «dispositivos» usa `meka-gume` (hardware). Los 15 se aprobaron.

**Inglés:** cada forma tiene glosa en inglés **por pivote** (su significado en español → `diccionario_es_en.tsv` → `ingles.tsv`); toda forma nueva necesita su entrada (lo exige `verificar_todo.py`). Con ello el **traductor** ofrece Owee ⇄ español e Owee ⇄ inglés.

------------------------------------------------------------------------

**Fin del registro maestro consolidado.**

## 87. Lote 3 — Ciencia y sociedad (95 términos, aprobado)

Biología, Tierra y clima, Educación, Derecho y política, Economía, Lengua, Artes y música, Cultura. Revisión por raíces: cada compuesto usa raíces existentes con significado adecuado, forma y significado únicos, máx. 3 elementos. Correcciones de la revisión: `alumno`=`tase-nara` y `juez`=`foma-nara` (el sufijo `po` significa «menos», no «persona»); `ciudadano`=`saro-nara`; eliminado «tiempo atmosférico» (casi sinónimo de `clima`); ~30 formas renombradas para evitar confusiones al oído (p. ej. terremoto `taro-faro-duma`, libro `beka-seta`, ciencia `lare-seta`).

## 88. Lotes 4 y 5 — Vocabulario de interfaz de oweelinux/KDE (62 términos, aprobados)

Surgen de las capturas de oweelinux (cadenas sin traducir) y de las cadenas más frecuentes de los catálogos KDE/Deepin (`prioridad_cadenas.tsv`). Lote 4: `dore-salo` (apariencia), `dore-seta` (tema), `salo-pa`/`salo-po` (claro/oscuro), `bore-fale` (gris), `meka-tabe-seta` (escritorios), `luma-tada-tabe` (touchpad), `sape-nado` (atajo), `fadu-kose` (bloquear), `nara-pase` (personal), `nara-meka-rela` (interfaz), `loke-tabe-kera` (captura), `mado-foma-kume` (tienda de apps), `gade-no` (otro). Lote 5 (48): opciones, comentario, éxito, ruta, título, fuente, estado, icono, filtro, licencia, imprimir, comando, fecha, color, tipo, etc.

Reglas aplicadas: un solo significado por forma (se descartaron `tera-no` y `nume-reka`, que ya existían; «dispositivo» sigue siendo `meka-gume`); fechas sin palabras nuevas (`loda-kelo` + número para los días, `mune-kelo` + número para los meses); el glosario `ui_glosario.tsv` (190 textos, una fila por texto en inglés, sin repetir) es la única fuente de las traducciones de interfaz y de él se generan `qow.po`, `qow@owee.po` y los JSON web.

## 89. Lote 6 — Alimentos (23 términos, aprobado) y calculadora web

**Raíces nuevas (8), justificadas por frecuencia cotidiana y cultural:** `tabu` (pan), `sebu` (arroz), `fuko` (papa), `mugo` (maíz), y cuatro nombres de la cocina boliviana adaptados a la fonología de Owee, sin `i` ni grupos de consonantes: `kenua` (quinua), `salotena` (salteña), `kunape` (cuñapé), `charake` (charque). **Compuestos (15):** `tabu-gume` harina, `nede-fame` verdura, `ruma-kuna-gume` pollo, `ruma-suna-gume` pescado, `naku-nobe-gume` queso, `lena-gume` azúcar, `nelo-mase` aceite, `suna-fame` sopa, `nelo-nobe` jugo, `fuko-suna-nuse` chuño (papa sin agua), `mugo-nobe` bebida de maíz (api, chicha), `pore-nelo` ají, `pore-sabe` picante, `kale-nelo-fame` plátano, `saro-fame` comida típica. Se reutilizan los ya existentes: `fame` comida, `nelo-fame` fruta, `bora-gume` carne, `naku-nobe` leche, `pado-kopa` huevo, `chaga-rela` sal.

**Calculadora de números** (`calculadora.html`, `07_Sitio_Web/calculadora.js`): teclado con cifras Owee, lectura en voz alta (coeficiente + escala, `doto` decimal, `po` negativo), convertidor número normal ⇄ cifras Owee ⇄ lectura Owee (sin números romanos). Probada con `verificar_todo.py` (lecturas, ida y vuelta 0–3000, evaluador sin `eval`).

## 90. Teclado Keyman de Owee y ajustes de la calculadora

Teclado Keyman (`05_Teclado_IME/keyman-owee`): romano → Owee Script sílaba a sílaba (consonante + vocal → glifo, `sh`/`ch`, guion → nexo de compuesto, mayúscula → marca de nombre, 0–9 → cifras Owee, AltGr + cifra → cifra normal), con teclado táctil para Android/iOS. Se genera con `generar_keyman.py` desde el mismo mapa de glifos que el IME de Fcitx5; el paquete `Owee.kmp` está en `dist/` y en la página *Teclado* del sitio, que incluye una caja de prueba con KeymanWeb. La calculadora ya no usa números romanos: convierte entre cifras Owee, números normales y lectura Owee.

## 91. Lote 7, decisiones aceptadas, sitio público e instalación en el equipo

**Lote 7 (31 términos aprobados)**, vida diaria y verbos de interfaz: `reme-nara` amigo, `pade-pade-pade` bisabuelo/a, `mela-nara` pariente, `kuma-nado` puerta, `kema-tabe` mesa, `kuma-gore-pa` edificio, `kuma-duma-kore` calle, `gase-gume` jabón, `kuma-kema` mueble, `bume-fena` vestirse, `sado-no` enfermo, `sado-meka` ambulancia, `sado-feke-kuma` farmacia, `sape-moke` emergencia, `sado-dare` sanar, `naro-meka` autobús, `taro-meka-raga` tren, `kalu-meka` bicicleta, y los verbos `delo-duma` arrastrar, `delo-gune` soltar, `tada-kade` pulsar, `loke-duma` desplazar, `doke-duma-bo` importar, `doke-duma-ba` exportar, `tare-dare` confirmar, `saro-pema` compartir, `rela-bosa` desconectar, `sena-nara-telo` renombrar, `loke-pema` mostrar, `loke-kose` ocultar. Se descartaron los que ya existían (`sare-naku`, `naku-naku`, `salo-feke`, `maku-bume`, `sura-meka-kuma`, `sade-kelo-palo`, viaje, boleto, frontera). Calendario: días y meses con `loda-kelo` / `mune-kelo` + ordinal.

**Decisiones de Gramática 1.1 y pronombres:** aceptadas las opciones recomendadas (ver «Estado y pendientes», §3.1).

**Sitio público:** `OWEE_PUBLICO=1 python3 07_Sitio_Web/build_site.py` genera el sitio sin la sección *Proyecto* (registro maestro, estado, auditoría, plan, integración, revisión) y sin sus enlaces; `.github/workflows/pages.yml` lo publica en GitHub Pages.

**Instalación en el equipo (Deepin):** `08_Integracion/instalar_en_host.sh` (modo usuario, sin sudo, o `--sistema`) y `probar_host.sh` (comprueba cada pieza). `herramientas/gettext_rellenar.py` crea catálogos de interfaz en Owee para los programas ya instalados a partir del glosario (130 catálogos, 2 135 textos de 82 433; el resto se ve en español).

## 92. Audio de pronunciación (voz sintética)

`03_Material_Ensenanza/Pronunciacion/audio/`: 1 164 archivos `.ogg` (60 sílabas, cifras, las 973 palabras del léxico y las frases del curso y de «frase del día»), generados con `herramientas/sintetizar_audio.py` y la voz Piper `es_MX-ald-medium` (dominio público). Reciben los fonemas de Owee (sh = ʃ, ch = tʃ, r = ɾ, acento en la primera sílaba de cada elemento). Es una **aproximación hecha por una voz de español**, no una grabación nativa; no la he escuchado, solo he comprobado que los archivos existen, no están vacíos y duran lo esperado. En la web: botón ▶ junto a cada frase, clic en las palabras con glosa y en las palabras en código. Pendiente: grabaciones humanas y revisión auditiva.

## 93. Lote 8, nombres propios, r vibrante en el audio y grabación de voz humana

**Lote 8 (19 términos aprobados):** comedor `pume-kore`, toalla `suna-delo-feke`, abrigo `fure-fadu-bume`, vestido `doma-kalu-bume`, lavar `suna-gase`, regalo `pema-kema`, bolsa `kema-kopa`, cansancio `faro-po-dune`, sueño `sule-moke`, peligro `saku-kasu`, vacuna `sado-fadu-feke`, descansar `faro-gura`, dulce `lena-gume-sabe`, salado `chaga-rela-sabe`, yuca `taro-nelo-fame`, alto `go-gore`, ancho `kado-gore`, vertical `go-gu`, horizontal `taro-tabe`. Se descartaron sala, dormitorio, isla, desierto y capital, que ya existían.

**Nombres propios:** `02_Diccionario/datos/adaptar_nombre.py` aplica la norma de la Gramática 1.1 §14 (reproduce los ejemplos documentados: Pedro → Pedero, Carlos → Karaloso, María → Marea) y genera `nombres_propios.tsv` (52 nombres) y la página *Nombres propios*.

**Audio:** la voz sintética pronunciaba la `r` como una `d` (`tare` sonaba `tade`); ahora usa la `r` vibrante. Para grabar tu propia voz: `03_Material_Ensenanza/Pronunciacion/herramientas/grabar_voz.py` (graba palabra por palabra, recorta, normaliza y guarda en `audio_humano/`; tus grabaciones reemplazan a la voz sintética al regenerar el sitio).

## 94. Glifos 3.4 (rediseño del sistema de escritura)

Los glifos se rediseñaron para que cada uno se distinga a simple vista, incluso torcido, a mano o estirado en una pancarta. Salen de `04_Fuentes/actual_3.3_fuente_y_glifos/OweeSans3_3_Source/glifos_v4.py`: un solo esqueleto de líneas rectas y círculos, dibujado **recto** (Owee Sans, pantalla y pancartas) o con las **esquinas redondeadas** (Owee School, escritura a mano).

- **Sílaba:** consonante grande en el centro + marca de vocal pequeña y suelta, en su lado (a arriba, e izquierda, o derecha, u abajo). El lado sólo refuerza; la vocal se reconoce por su **forma**.
- **Vocales:** a `—` (Ogham, hebreo), e `エ` (katakana), o `○` (omicron griega), u `ᚢ` (runa Uruz). Ver `VOCALES_v4.md`.
- **Consonantes:** p `⊔`, b `⊔` con barra, f `T`, m cuadro con raya vertical, t `Λ`, d `A`, s `Z`, n `Θ`, l `Y`, r `Y` con punto, k `┐`, g `┐` con barra, sh `X`, ch `✱`. La barra al medio marca la sonora (b, d, g). Ninguna consonante es el giro o el espejo de otra (`auditar_glifos_v4.py`).
- **Marcas:** nombre propio `ᚠ` (runa Fehu, antes `=`), nexo de compuesto `‿` (antes una barra baja que se confundía con la vocal a).
- **No cambian:** el romano, los puntos de código (U+E000–U+E03B sílabas, U+E03C nexo, U+E03D nombre, U+E040–U+E049 dígitos) ni los números.
- **Guía de estilo:** `GUIA_DE_ESTILO_v4.md` (rasgo que define cada glifo, qué puede variar, con qué se confunde). Los PDF de especificación (`01_Especificacion`) describen aún la vocal como «extensión direccional» y las familias como pares por cierre o cruce: quedan **desactualizados**.

## 95. Lotes 9 a 14 — vocabulario de hogar, informática, comercio, cuerpo, cocina y campo (aprobados 2026-10-22)

268 términos aprobados (compuestos de raíces existentes más 17 nombres de alimentos adaptados): `02_Diccionario/datos/lotes_9_a_14.md`. Antes de aprobar se comprobó que ningún concepto tuviera dos formas y se evitó el paralelismo (palabras a una letra de otra del mismo tema): se cambiaron unas 50 formas. Cobertura por área (512 conceptos de trabajo): `cobertura_dominios.py` y `.md`. Todo el léxico (1 260 formas) se escribe con los glifos 3.4 (`auditar_palabras_v4.py`). **Audio:** los términos nuevos aún no tienen audio (la síntesis necesita el modelo Piper, que no se pudo descargar); ejecutar `sintetizar_audio.py` en el equipo con el modelo.

## 96. Diccionario descargable y El libro de los ciclos

**Diccionario:** la página *Diccionario* del sitio filtra ahora por todas las áreas (antes faltaban las de los lotes 3–14), muestra el inglés en cada ficha y permite buscar en inglés; incluye la descarga del diccionario completo en `assets/diccionario_owee.tsv` y `.json` (owee, sílabas, clase, español, inglés, área, estado, partes).

**Literatura §11 — El libro de los ciclos:** tres historias (*El universo que respira*, *El agua y la piedra*, *La semilla que esperó*) y 12 sentencias del universo, las plantas y la vida, de referencia filosófica al modo de los libros taoístas pero de autoría original. Solo vocabulario existente.

## 97. Lotes 15 y 16, `kumedo` e interfaz del sitio en Owee

**Vocabulario:** 127 términos aprobados el 2026-10-22 (`02_Diccionario/datos/lotes_15_y_16.md`): `kumedo` = red social (`kume` + `do`, pedida por el autor), ampliación diaria (lote 15) y las palabras para aprender y escribir Owee (lote 16). Léxico: 1 154 formas ampliadas, 1 012 aprobadas.

**Selector ES / Owee / Script:** el sitio traduce al Owee los títulos, las cabeceras de tabla, los botones y las tarjetas de la portada, del curso (niveles y lecciones), de escritura, pronunciación, teclado, descargas, nombres propios y diccionario: `07_Sitio_Web/ui_owee.tsv` (157 textos, validados contra el léxico con `validar_ui_owee.py`). Script pinta los glifos desde el romano; Owee muestra el romano; ES restaura el original; el modo se conserva al cambiar de página. La prosa larga (explicaciones de gramática, matemáticas, física…) sigue en español: Owee todavía no tiene vocabulario ni sintaxis para traducirla con fidelidad. Probado en un navegador con `07_Sitio_Web/probar_idiomas.py` (todas las páginas, los tres modos, ida y vuelta Script → romano).

## 98. Ronda 1 de la interfaz en Owee (prosa de aprendizaje)

El sitio tiene ahora **228 textos en Owee** (`07_Sitio_Web/ui_owee*.tsv`, validados con `validar_ui_owee.py`): títulos, tarjetas, cabeceras, etiquetas en negrita de las lecciones (*Fíjate*, *Respuestas*, *Ejercicios*…) y la **prosa de aprendizaje** de la portada, el curso, escritura, nombres, calculadora, teclado, las cuatro páginas de niveles (objetivos y reglas principales) y la pronunciación (reglas de oro). Son **borradores en frases cortas** con el vocabulario existente: el nombre del sitio se escribe `Ouee` (decisión del autor). Quedan en español, a propósito, las **glosas** (la traducción de cada palabra o frase Owee es lo que enseña la página), las instrucciones técnicas de instalación y las explicaciones largas de gramática, matemáticas, física, química, astronomía e informática: necesitan vocabulario de metalenguaje que aún no existe. Cobertura: 474 de 1 447 textos (títulos, etiquetas, párrafos y listas) de las páginas públicas.

## 99. Lote 17 (gramática), nombre del sitio y ronda 2–3 de la interfaz en Owee

**Lote 17:** 26 términos de gramática aprobados (`02_Diccionario/datos/lotes_17.md`) para traducir las reglas: vocativo, demostrativo, cuantificador, negativo, compuesto, guion, espacio, acento, intensidad, comparación, interrogativo, relativo, subordinación, saludo, cortesía, puntuación, préstamo, excepción, pronombre, conjunción, modificador, sujeto y objeto gramaticales…

**Interfaz:** 342 textos en Owee. Ronda 2: títulos y reglas principales de la Gramática y la Pronunciación. Ronda 3: títulos de las guías de Matemáticas, Física, Química, Astronomía e Informática. Los menús desplegables (Aprender, Ciencias), el nombre del sitio (`Ouee`: glifos en Script, `Ouee` en Owee) y la etiqueta del selector van ahora en los tres modos; la etiqueta del selector usaba una fuente del sistema y se veía como cuadros en algunos navegadores. Orden elegido para seguir: Gramática y Pronunciación (núcleo del aprendizaje) → niveles → Ciencias → Literatura.

