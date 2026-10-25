# Owee 2.0 — especificación normativa del idioma y estándar digital

Fonología, gramática, vocabulario, números, escritura, codificación y entrada digital. Sustituye a *Owee Base 1.0 — Especificación normativa y digital*: incorpora la Gramática 1.1, Owee Script 3.4 (en línea), la codificación definitiva y las herramientas ya construidas (fuentes, teclados, sitio web, paquetes).

> **Principio central:** la estructura comunica lo necesario; el contexto evita repetir lo obvio.
> **Principio de univocidad:** una forma = un significado.
> **Principio digital:** el romano es la representación digital canónica; Owee Script es la representación gráfica nativa del mismo sistema silábico.

## 1. Alcance y estabilidad

| Área | Estado en 2.0 |
|---|---|
| Fonología | **cerrada** |
| Estructura silábica (V / CV) | **cerrada** |
| Romanización | **estable** |
| Gramática nuclear (orden SOV, tiempo, negación, preguntas) | **estable** |
| Gramática 1.1 (sí, imperativo, cortesía, demostrativos, cuantificadores, comparación, relativas, nombres propios) | **confirmada** |
| Números 0–9 y escalas | **estable** |
| Owee Script: forma de los 60 glifos, marcas y dígitos (3.4, en línea) | **estable** |
| Codificación (uso privado U+E000–U+E049) | **asignada**; IDs estables |
| Fuentes, teclados, sitio web y paquetes | **implementados** |
| Puntuación propia y signos matemáticos propios | abiertos |

**Versionado:** una Owee 2.x puede ampliar vocabulario y herramientas sin romper esta base. Un cambio incompatible de fonología, sílabas o gramática nuclear requiere una versión mayor.

## 2. Fonología

| Elemento | Norma |
|---|---|
| Vocales | `a` `e` `o` `u` |
| Vocal inexistente | i |
| Alargamiento | expresivo y opcional: `tare` → `tareee` (no cambia el significado) |
| Consonantes | p b t d k g f s m n l r sh ch |
| r | una sola r, simple y clara (como en «pero»); no existe la rr |
| sh / ch | un solo fonema cada una |
| Sílaba | V o CV |
| Coda, grupos, letras mudas, tonos | no existen |
| Acento | en la primera sílaba de cada elemento; el primero del compuesto es el más fuerte |

Letras no nativas: c, j, q, v, w, x, y, z, i. Solo aparecen al adaptar nombres propios (§10).

## 3. Sílabas y romano

Cada sílaba tiene una forma romana única: 56 sílabas CV + 4 vocales solas = **60 unidades**.

<!--silabas-->

El romano no es una ayuda secundaria: es la forma canónica en teclados, código, bases de datos y URLs. Segmentación: `nara` → NA + RA · `meka-mado` → ME + KA ‿ MA + DO.

<!--pagina-->

## 4. Gramática nuclear

Owee es **analítico**: sin flexión de persona, género, número ni tiempo. Orden base: **SUJETO + COMPLEMENTOS / OBJETO + ACCIÓN** (SOV). Plantilla completa: sujeto + receptor + objeto + lugar + tiempo + negación + acción.

| Función | Formas |
|---|---|
| Pronombres | `me` yo · `tu` tú · `ra` él / ella · `mene` nosotros · `tune` ustedes · `rane` ellos |
| Conectores | `re` y · `lo` o · `ke` si · `balo` pero · `kasu` porque |
| Relación | `ko` con · `so` sin |
| Escala | `pa` más · `po` menos · `se` igual |
| Posesión | poseedor + poseído: `me kuma` (mi casa); tener: `pase` |
| Existencia | `mora` (hay, estar) |
| Modificador | concepto + modificador: `kuma gore-pa` (casa grande) |

```owee
me suna nume
me fame pume
me doke lodu
me tu suna pema
```

*Quiero agua. Como. Leo información. Te doy agua.*

**Regla de economía:** no se expresa dos veces lo que el contexto ya dice. Owee no tiene verbo «ser»: `me nara` = «soy una persona».

## 5. Tiempo, negación, respuestas y preguntas

| Sistema | Forma | Regla |
|---|---|---|
| Presente | sin marca | contexto actual |
| Pasado | `pe` | justo antes de la acción |
| Ahora (énfasis) | `te` | normalmente se omite |
| Futuro | `pu` | justo antes de la acción |
| Negación | `no` | justo antes de lo negado |
| Sí / no | `tare` / `no` | `tare` = verdad |
| Pregunta sí/no | `ka` | al final |
| Pregunta informativa | `ka-nara` quién · `ka-kema` qué · `ka-kore` dónde · `ka-bema` cuánto · `ka-kasu` por qué · `ka-mode` cómo · `ka-tera` cuándo | en el lugar de lo preguntado, **sin** `ka` final |

```owee
me suna pe no nume
tu suna nume ka
tu ka-kore mora
```

*Antes no quería agua. ¿Quieres agua? ¿Dónde estás?*

<!--pagina-->

## 6. Espacio, demostrativos y cuantificadores

| Owee | Idea | Owee | Idea |
|---|---|---|---|
| `bo` | dentro, en | `ba` | fuera |
| `to` | hacia | `de` | desde |
| `go` | arriba | `gu` | abajo |
| `le` | cerca, este | `lu` | lejos, aquel |
| `kema-le` | esto | `kore-le` | aquí |
| `kema-fese` | todo | `nara-fese` | todos |
| `kema-no` | nada | `nara-no` | nadie |
| `tera-fese` | siempre | `tera-no` | nunca |

El operador de lugar va **después** del nombre: `me kuma bo` = estoy en casa.

## 7. Modalidad, órdenes y cortesía

| Raíz | Función | Ejemplo |
|---|---|---|
| `nume` | deseo | `me daro nume` quiero trabajar |
| `moke` | necesidad | `me daro moke` necesito trabajar |
| `pode` | capacidad | `me daro pode` puedo trabajar |
| `pelo` | deber | `me daro pelo` debo trabajar |
| `lare` | saber hacer | `me lodu lare` sé leer |

- **Imperativo:** el verbo solo: `sule` (¡duerme!).
- **Por favor:** pregunta de capacidad: `tu suna pema pode ka`.
- **Vocativo:** el nombre al principio, con coma: `naku, sule`.
- **Saludos:** `reme` hola · `pu-reme` adiós · `gura-lena` gracias · `bosa-rude` perdón.

## 8. Comparación, intensidad y relativas

- Comparativo: `[comparado] [referencia] [escala]`: `ra me gore-pa` (él es más grande que yo).
- Igualdad: `ra me gore se`. Superlativo: `gore-pa fese`.
- Intensidad: se repite el operador: `gore-pa-pa` (muy grande).
- Relativas: el nombre una vez y `ra` como copia dentro de la subordinada: `nara, ra suna nume, me reme` (la persona que quiere agua es mi amiga).

<!--pagina-->

## 9. Composición del vocabulario

**Concepto principal + modificador.** Antes de crear una raíz nueva se intenta una composición transparente.

| Regla | Detalle |
|---|---|
| Guion | compuesto léxico (una idea fija), máximo **3 elementos**: `kuna-bore` noche, `sade-kelo` año |
| Operadores | raíz + `pa` `po` `se` `no` `le` `lu` `fese`: `gore-pa` grande, `tera-no` nunca |
| Espacio | frase libre, no fija: `kuma gore-pa` casa grande |
| Raíz nueva | solo si ninguna composición es clara: 2 sílabas, a distancia ≥ 2 de toda raíz de 2 sílabas, sin parecerse a una palabra de otra lengua |
| Préstamos | **no** para nombres comunes: `rale-nede-fame` tomate, `suna-nelo-fame` sandía, `nolu` cebolla (lote 19) |

| Compuesto | Partes | Significado |
|---|---|---|
| `luma-salo` | percepción + luz | ver |
| `reka-sone` | comunicación + sonido | hablar |
| `meka-mado` | máquina + cálculo | computadora |
| `doke-beka` | información + escritura | texto |
| `suna-goda` | agua + sólida | hielo |
| `tabu-nelo` | pan + planta | trigo |

**Flujo de una palabra nueva:** PROPUESTA → VERIFICADA (fonología, partes existentes, sin colisión, sin sinónimo, ≤ 3 elementos) → APROBADA por el autor. El estado de cada forma está en `02_Diccionario/datos/`.

**Léxico actual:** 233 formas base y 1 191 de vocabulario por áreas (matemáticas, física, química, astronomía, informática, interfaz, vida diaria, cocina, campo, cuerpo, gramática…), todas aprobadas o auditadas.

## 10. Nombres propios

Se adaptan **por el sonido**: `i` → `e`, `v` → `b`, `z`/`c` suave → `s`, `j` → `k`, `h` muda, `ñ` → `ne`; a una consonante final o un grupo se le añade una vocal de eco. Se marcan con **mayúscula** en romano y con **ᚠ** en Owee Script: `Ana`, `Pedero` (Pedro), `Karaloso` (Carlos), `Marea` (María). El idioma se llama `Ouee` en Owee.

<!--pagina-->

## 11. Números y matemáticas

<!--digitos-->

| Escala | Valor | Operación | Owee | Signo |
|---|---|---|---|---|
| `tanu` | 10 | suma | `dapa` | + |
| `gabu` | 100 | resta | `dopo` | − |
| `soku` | 1 000 | multiplicación | `kebu` | × |
| `benu` | 1 000 000 | división | `faku` | ÷ |
| | | igualdad | `se` | = |
| | | decimal | `doto` | . |

Se lee **cantidad + escala**, de mayor a menor, sin leer las posiciones con 0: [[247]] · [[909]] · [[2026]]. Se calcula con los glifos numéricos y se lee con las palabras; la notación matemática internacional se conserva.

## 12. Owee Script

Una sílaba = un bloque, escrito **en línea** de izquierda a derecha: la consonante y, a su derecha, la marca de la vocal (`a` barra, `e` viga エ, `o` anillo, `u` runa ᚢ). Siete parejas de consonantes; la sonora lleva una barra al medio. Nexo ‿ en los compuestos, ᚠ delante de los nombres propios, dígitos propios. Detalle completo: *Owee Script 3.4 — especificación de escritura y glifos*.

```owee
me suna nume
sade-kelo
```

*Quiero agua. Año (sol + ciclo, unidos por el nexo).*

## 13. Estándar digital

| Nivel | Ejemplo | Función |
|---|---|---|
| Romano | `nara` | entrada canónica y respaldo |
| Sílabas | NA + RA | segmentación (`sh` y `ch` primero) |
| ID estable | OWEE_SYL_NA + OWEE_SYL_RA | identidad independiente del dibujo y del código |
| Código | U+E028 U+E030 | almacenamiento (uso privado) |
| Glifo | `nara` | presentación |

| Rango | Contenido |
|---|---|
| U+E000–U+E03B | 4 vocales + 56 sílabas, en el orden de la matriz |
| U+E03C · U+E03D | nexo de compuesto · marca de nombre propio |
| U+E03E–U+E03F | reservados |
| U+E040–U+E049 | dígitos 0–9 |

**Conversión romano → Script:** minúsculas (salvo la mayúscula de nombre) → conservar espacios y puntuación → `sh`/`ch` primero → leer V o CV → una secuencia imposible queda en romano → emitir glifos manteniendo los límites de palabra. La conversión inversa es exacta.

<!--pagina-->

## 14. Implementación

| Pieza | Estado |
|---|---|
| Fuentes **Owee Sans** (pantalla) y **Owee School** (escritura a mano) | TTF, OTF, WOFF, WOFF2; paquete `fonts-owee` |
| Kit web `owee.css` + `owee.js` (`Owee.toScript`, `Owee.toRoman`) | listo; usado por el sitio |
| Teclado **Fcitx5** 1.2 (Linux): romano → Script, compuestos, nombres | paquete `fcitx5-owee` |
| Teclado **Keyman** (Windows, macOS, Android, iOS) | `Owee.kmp` |
| **Owee Pad** (web, sin instalar) | en el sitio; funciona sin conexión |
| Cifras Owee en todo el sistema | paquete `owee-numerals` (opcional) |
| Locale `qow_BO` y traducciones de interfaz | paquete `owee-locale` |
| Diccionario, traductor, calculadora, curso, audio de pronunciación | sitio web |

## 15. Compatibilidad

| Situación | Norma |
|---|---|
| Búsqueda | indexar también el romano |
| Copiar y pegar | conservar los códigos del Script; ofrecer el romano |
| Bases de datos | UTF-8 (utf8mb4); campo romano para buscar |
| URLs e identificadores de código | romano |
| Sin fuente instalada | mostrar el romano o incluir la fuente web |

Formato recomendado para aplicaciones: `{"roman": "suna", "syllables": ["su", "na"], "concept": "AGUA"}`.

## 16. Lista de comprobación

1. Cuatro vocales `a e o u`; la i no existe.
2. Catorce consonantes; `sh` y `ch` son una unidad.
3. Solo sílabas V y CV: 60 unidades.
4. Acento en la primera sílaba.
5. Orden SOV; sin género, número ni conjugación.
6. Tiempo con `pe` / `te` / `pu`; negación con `no`; `tare` = sí.
7. `ka` final en las preguntas de sí o no; palabra de pregunta sin `ka` final.
8. Composición concepto + modificador, máximo 3 elementos.
9. Nombres comunes con raíces Owee; solo los nombres propios se adaptan.
10. Decimal con `cho be du ga fo sa ku mu na she` y `tanu gabu soku benu`.
11. El romano es la forma digital canónica.
12. Owee Script en línea, con nexo, marca de nombre y dígitos propios.
13. IDs silábicos estables e independientes del código y del dibujo.
