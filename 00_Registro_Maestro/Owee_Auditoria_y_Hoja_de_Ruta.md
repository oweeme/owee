# Owee — Auditoría y hoja de ruta

**Fecha:** 2026-10-12 · **Alcance:** todo el proyecto (Registro Maestro, Diccionario Base 1.0, Matemáticas 2.0, Física 2.0, fuentes 3.x, IME, literatura).
Cada punto indica **qué encontré**, **por qué importa** y **qué haría**. Las cifras salen de scripts reproducibles (`02_Diccionario/datos/`).

## Resumen: dónde mejorar más (por prioridad)

| # | Área | Hallazgo clave | Impacto |
|---|---|---|---|
| 1 | Gramática funcional | Faltan demostrativos, «sí», «todo/nada», «muy», «también», oraciones relativas, imperativo, vocativo y saludos | **Alto**: sin esto no hay diálogo ni textos largos |
| 2 | Coherencia de documentos | El PDF de Matemáticas 2.0 aún usa formas imposibles (`vara`, `vade`, `veka`, `vola`, `dira`, `ango`, `akso`); Matemáticas 1.0 usa `por`, «negativo», «potencia» y «raíz» (palabras no Owee o no adoptadas); el Registro no incluye ni los **números compuestos** (definidos en Matemáticas 1.0) ni las 89 raíces científicas | **Alto**: la «fuente maestra» está desfasada |
| 3 | Fonología hablada | 55 parejas de raíces difieren solo en un par de sonidos cercanos (p/b, t/d, k/g, m/n, f/s…), incluidas **palabras funcionales** (`te`/`de`, `bo`/`po`, `ga`/`ka`) | **Alto** para el idioma hablado y cantado |
| 4 | Composición de palabras | No hay regla escrita para guion vs. espacio ni para el acento en compuestos | Medio-alto: afecta a poesía, música y a todo el léxico científico |
| 5 | Vocabulario | Sobre 114 conceptos básicos: 41 % con raíz, 29 % componible, **28 % sin resolver** | Medio-alto |
| 6 | Nombres propios y préstamos | Sin `i`, `v`, `h`, `y`, `z`, `j`, sin codas: no hay regla para escribir nombres, países, elementos químicos | Medio-alto |
| 7 | Escritura y tecnología | Sin puntuación propia; vocales largas sin glifo; solo PUA; el IME solo existe para Fcitx5/Linux | Medio |
| 8 | Proceso | Sin control de versiones, sin licencias, copias duplicadas, sin pruebas de audio | Medio (pero barato de arreglar) |

## 1. Gramática funcional (la mayor carencia)

El Registro cierra bien fonología, orden SOV, tiempo, negación, preguntas sí/no, espacio y modalidad. Pero hoy **no se puede** decir con normas escritas:

- **Demostrativos:** este / ese / aquel (¿`le`/`lu` cerca/lejos como determinantes?).
- **Cuantificadores:** todo, nada, algo, alguien, cada, otro, mismo.
- **Intensificador y adición:** muy, también, otra vez, siempre.
- **«Sí»** (la respuesta a `ka`) y **«qué»**.
- **Oraciones subordinadas y relativas** («la persona que…»): `ke` cubre el condicional; falta el resto.
- **Imperativo y ruego** (en la canción de cuna `sule` = «duerme» funciona por contexto, pero no hay marca).
- **Vocativo** («hijo, duerme»).
- **Saludos y cortesía:** hola, adiós, gracias, por favor, perdón.
- **Números:** *corrección de mi primera versión de esta auditoría:* los números compuestos **sí están definidos** en Matemáticas 1.0 (`25` = `du tanu sa`, `2026` = `du soku du tanu ku`, decimales con `doto`). Lo que falta es pasarlos al **Registro Maestro**, y definir los **negativos** (la guía usa la palabra española «negativo»), los **ordinales** y la lectura de **paréntesis**.
- **Interrogativos informativos:** su posición sigue pendiente (Registro §7 y §65).
- **Pronombres plurales** (`mene`, `tune`, `rane`) siguen provisionales.

**Qué haría:** abrir una «Gramática 1.1» corta que cierre estos puntos con ejemplos, empezando por números compuestos, «sí», imperativo/vocativo y demostrativos (son los que más se usan al escribir poemas y diálogos).

## 2. Coherencia de documentos

- **Matemáticas 2.0 (PDF)** presenta como «estables» `ango` (ángulo) y `akso` (eje), que **no son pronunciables** (`ng` y `ks` son grupos). Además conserva `vara`, `vade`, `veka`, `vola` y `dira` (con `v` e `i`, que no existen); la Física 2.0 ya las corrige (`bara`, `daku`, `dufa`, `bola`, `tora`) pero el PDF de Matemáticas no. En esta web se aplicaron las correcciones y se sustituyeron `ango` por el compuesto `tora-telo` (cambio de dirección) y `akso` por `loka-mede` (línea de medida).
- **Registro Maestro** declara estado «hasta Owee Sans 3.0»; la fuente vigente es la 3.3, y no incluye ni los números compuestos, ni el léxico de Matemáticas/Física (89 raíces) ni sus construcciones.
- **Cifras que no cuadran:** el Diccionario Base dice «163 entradas»; con derivadas, números y matemáticas básicas el léxico general tiene 200 formas; con las 89 raíces científicas y sus construcciones (incluidas las de Química, que son todas compuestos) suma 367.
- **Física 2.0** usa términos no definidos en ningún diccionario aparte de ella: `rata` (razón), `fere` (frecuencia), `kedo` (unidad) vienen de Matemáticas, pero `dase rata`, `duma-loka`, `dore-telo` no están en ningún inventario formal.
- Los cuadernos PDF muestran glifos de versiones anteriores de la fuente (3.1/3.2); la regla 69 del Registro pide mantenerlos sincronizados.

**Qué haría:** una **única tabla maestra** (ya está en `02_Diccionario/datos/lexico*.tsv`) de la que se generen el Registro, los PDF y la web. Y un registro de decisiones con fecha.

## 3. Fonología y confusión acústica

Con 4 vocales y 14 consonantes, el espacio de palabras CVCV es pequeño (3 136 formas). Hay **278 raíces** sin guion y ya existen **55 parejas** que difieren en un único par de consonantes acústicamente cercano. Ejemplos de las más peligrosas, por ser **palabras funcionales** de una sílaba:

| Pareja | Significados |
|---|---|
| `te` / `de` | ahora / desde |
| `be` / `pe` | 1 / pasado |
| `bo` / `po` | interior / menos |
| `ba` / `pa` | exterior / más |
| `go` / `ko` | arriba / con |
| `gu` / `ku` | abajo / 6 |
| `ga` / `ka` | 3 / pregunta |
| `du` / `tu` | 2 / tú |
| `fo` / `so` | 4 / sin |

y entre palabras de contenido: `pade`/`bade` (progenitor/autoridad), `taro`/`daro` (tierra/trabajo), `tera`/`dera` (tiempo/derivada), `salo`/`falo`/`faro`/`saro` (luz/reflexión/fuerza/comunidad), `suna`/`funa`, `gume`/`kume`/`gune`.

**Por qué importa:** en lengua hablada y en canciones (sin contexto escrito), estas parejas se confunden con facilidad, y las más críticas son justo las partículas que organizan la frase.

**Qué haría:** (a) grabar una **prueba auditiva** con hablantes: pares mínimos, en ruido y cantados; (b) para las parejas que fallen, reasignar una de las dos (la regla «no cambiar decisiones estables» del Registro §67 admite excepciones motivadas por fonología); (c) fijar una **regla de diseño**: no aprobar raíces nuevas a distancia 1 de otra (el script `auditar_ciencias.py` ya lo comprueba).

## 4. Composición de palabras (clave para poesía y música)

Hoy conviven, sin norma escrita: `bema-pa` (raíz+operador), `fuda-go-fasa` (raíz+operador+raíz), `goda-to-luda telo` (guiones **y** espacio), `pa-lo-se` (tres operadores unidos), `gabu-palo`, `sufa mede` (espacio). Y el Registro dice que el acento es **siempre en la primera sílaba**, pero no dice si un compuesto tiene **uno o varios** acentos.

**Por qué importa:** para métrica y ritmo. `kuna-bore` (4 sílabas): ¿un pulso o dos? Cambia cómo se canta y cómo se cuenta el verso. Para la web y el IME, cambia qué se considera «una palabra».

**Qué haría:** fijar (1) cuándo se escribe con guion y cuándo con espacio, (2) acento: propongo **un solo acento principal (en la primera sílaba del compuesto) y un secundario en cada raíz**, y (3) límite razonable de elementos por compuesto (≤ 3).

## 5. Vocabulario: cobertura real

Sobre una lista de trabajo de 114 conceptos básicos (`02_Diccionario/datos/cobertura.py`):

| Grupo | Con raíz | Componible | Falta |
|---|---|---|---|
| Acciones | 19 | 13 | 10 |
| Seres y lugares | 6 | 12 | 6 |
| Tiempo y espacio | 6 | 3 | 3 |
| Cualidades | 10 | 4 | 1 |
| Gramática y función | 6 | 2 | **13** |
| **Total** | **47 (41 %)** | **34 (29 %)** | **33 (28 %)** |

Lo que falta con más peso para literatura: `jugar`, `llorar`, `reír`, `pedir`, `responder`, `esperar`, `buscar`, `encontrar`, `soñar`, `nombre`, `flor`, `país`, `dios`, `año/mes/semana`, `siempre`, `largo/corto`.
(La clasificación es un juicio de trabajo; sirve para priorizar, no es norma.)

**Qué haría:** no inventar vocabulario por lotes. Escribir 30–50 textos (poemas, diálogos, cuentos) y **añadir solo lo que falte de verdad**, siempre con la regla de no-colisión.

## 6. Nombres propios y préstamos

Owee no tiene `i`, `v`, `h`, `y`, `z`, `j`, ni consonantes finales ni grupos. Por eso **no se puede escribir** el nombre propio de casi ninguna persona, ciudad o elemento químico sin una regla de adaptación.

**Qué haría:** una **norma de adaptación fonológica** (p. ej. *i → e*, *v → b*, *grupo consonántico → inserción de vocal*, *coda → vocal de apoyo*), con una lista de ejemplos y la excepción de conservar el nombre original **entre comillas** en romano. Es imprescindible para Química (118 elementos) y para cualquier relato.

## 7. Escritura y tecnología

- **Puntuación:** no hay signos propios (pendiente del Registro). Por ahora se usan `, . ¿ ?` latinos.
- **Vocales largas** (`aa ee oo uu`): el Registro admite que su representación en el script no está cerrada.
- **PUA:** todo vive en la zona de uso privado (U+E000…E049). Funciona, pero el texto copiado fuera de las apps con la fuente se ve como cuadros. Opciones: registrarlo en el *ConScript Unicode Registry* (informal) o proponer un bloque Unicode real (largo plazo).
- **Teclado:** solo existe el IME Fcitx5 (Linux/Deepin). Owee Pad cubre la web y móviles, pero **no hay** IME para Windows, macOS, Android ni iOS.
- **Accesibilidad:** comprobar contraste y tamaño mínimo (el Registro §68 ya lo pide) y añadir texto alternativo (romanización) en toda la web (ya se incluye como `title`).
- **Dos fuentes** (Sans y School): confirmar que los glifos reconocibles son idénticos entre ambas.

## 8. Proceso y mantenimiento

- **Sin git**: no hay historial. Recomiendo `git init` ya; el proyecto es pequeño (≈ 35 MB).
- **Sin licencia**: ni para las fuentes (¿SIL OFL?) ni para el material (¿CC BY-SA?). Sin licencia, nadie puede reutilizarlo legalmente.
- **Duplicados**: varias versiones completas de fuentes y IME; ya movidas a `99_Archivo/`.
- **Pruebas automáticas**: el validador (`validar_owee.py`) cubre fonología y vocabulario; falta añadirlo a un `make check` o a una acción de CI.
- **Sin audio**: no existe ninguna grabación de pronunciación ni lista de palabras con audio.
- **Sin corpus**: hay ≈ 20 textos breves; para estabilizar la gramática conviene llegar a 100+.

## 9. Para poesía y canciones (lo que más te servirá)

1. Cerrar **imperativo, vocativo, «sí» y demostrativos** (punto 1).
2. Fijar la **norma de compuestos y su acento** (punto 4).
3. Añadir 20–30 raíces de **emoción y naturaleza** que la poesía pedirá (`tristeza`, `alegría`, `flor`, `mar`, `río`…): primero como **composiciones aprobadas**, solo después como raíces.
4. Hacer la **prueba auditiva** (punto 3) con tus canciones: son el mejor banco de pruebas porque en el canto no hay contexto que desambigüe.
5. Opcional: notación musical (pentagrama) y una versión grabada de cada canción.

## 11. Univocidad: una forma = un significado

Principio decidido el 2026-10-12 (Registro §73). Resultado de revisar **todo** el léxico (general, ciencias y propuestas):

- **0 formas repetidas** con dos significados.
- **0 formas distintas** con el mismo significado (sinónimos).
- **5 raíces del léxico base** cargan un sentido doble que conviene vigilar:

| Raíz | Significados actuales | Riesgo | Propuesta |
|---|---|---|---|
| `faro` | ~~fuerza / energía~~ → **fuerza (vigor)** | **Resuelto 2026-10-12**: la energía es `enu`; `faro-enu` = fuerza energética | `faro-pa` («fuerte») no cambia |
| `fese` | límite / completitud | Medio: en matemáticas es «límite»; en gramática se propuso para «todo» | Mantener: ambos son «alcanzar el extremo». Los usos van en compuestos (`kema-fese`) |
| `lafe` | calidad / valoración | Medio (provisional) | Decidir si es neutro («calidad») o positivo («bueno») |
| `saku` | alerta / miedo | Bajo: misma familia emocional | Mantener |
| `doma` | corazón / centro corporal | Bajo | Mantener; el «centro» en general es `choma` |

- **Decisiones ya tomadas por este principio** (ver Gramática 1.1, §15): se rechazó `ko lena` («por favor»), `gade` como relativo, `bema-po` como «negativo» y `kelo` solo como «otra vez»; se adoptó `pode ka`, parataxis con `ra`, `dopo` para el signo menos y `pu-kelo`.
- **Nombres propios:** pueden sonar como una palabra común (`Kale` / `kale`); la marca de nombre (mayúscula en romano, U+E03D en Owee Script) mantiene la univocidad.

## 12. Plan sugerido (en orden)

1. `git init` + licencias (1 hora).
2. Aprobar `tora-telo`, `loka-mede`, las construcciones de Química (ya sin raíces nuevas) y las composiciones poéticas (1 sesión).
3. Gramática 1.1: «sí», imperativo, vocativo, demostrativos, negativos y regla de compuestos con su acento; pasar al Registro los números compuestos (2 sesiones).
4. Norma de nombres propios y préstamos (1 sesión).
5. Prueba auditiva de pares mínimos funcionales (1 día con 3–5 personas).
6. Escribir 30–50 textos y ampliar el léxico solo con lo que falte.
7. Regenerar Registro Maestro y PDF desde `lexico*.tsv`; actualizar cuadernos a la fuente 3.3.
