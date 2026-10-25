# Owee Script 3.4 — especificación de escritura y glifos

Documento de referencia para que la escritura Owee sea la misma en los materiales educativos, las fuentes, la web, el teclado y el Owee Pad. Sustituye a la especificación 3.0, en la que la vocal se indicaba con una extensión arriba, a la izquierda, a la derecha o abajo de la consonante.

## 1. Principios

- **Una sílaba hablada = una sílaba escrita.** Owee Script es silábico y se escribe de izquierda a derecha.
- **El romano es la forma digital canónica.** `suna` y su escritura en glifos son el mismo texto; el romano sirve de respaldo en teclados, código, URLs y bases de datos.
- **Inventario cerrado:** vocales `a e o u` (no existe la `i`); consonantes `p b t d k g f s m n l r sh ch`. Sílabas solo **V** o **CV**: sin consonantes finales ni grupos. `sh` y `ch` son un solo sonido.
- **Acento** siempre en la primera sílaba de cada elemento.

## 2. Escritura en línea

Desde la versión 3.4, cada sílaba es la **consonante** (forma grande) seguida, **a su derecha y en el mismo renglón**, de la **marca de la vocal** (pequeña, suelta, con aire). Se lee consonante → vocal → siguiente sílaba, sin saltar arriba ni abajo.

| Vocal | Marca | Origen | Ejemplo |
|---|---|---|---|
| **a** | barra vertical | raya del Ogham y del hebreo | `pa` |
| **e** | viga エ | la *e* del katakana | `pe` |
| **o** | anillo pequeño | la omicron griega | `po` |
| **u** | runa ᚢ | la runa Uruz | `pu` |

Reglas de espacio:

1. La marca de vocal **no toca** la consonante.
2. Entre dos sílabas hay **más aire** que entre una consonante y su vocal: así se ve qué vocal pertenece a cada consonante.
3. Una **vocal sola** (`a`, `e`, `o`, `u`) es solo su marca, más grande y centrada.

> La disposición anterior (vocal alrededor de la consonante) solo se conserva para comparar materiales antiguos; no se usa en documentos nuevos.

## 3. Consonantes

Siete pares. La **barra al medio** marca la consonante sonora (`b`, `d`, `g`). Ningún glifo es el giro o el espejo de otro (comprobado con `auditar_glifos_v4.py`).

| Consonante | Forma | Rasgo que no puede cambiar | Sílaba |
|---|---|---|---|
| **p** | copa abierta arriba ⊔ | abierta arriba, sin barra | `pa` |
| **b** | copa con barra | la barra cruza toda la copa | `ba` |
| **t** | Λ | dos patas en punta | `ta` |
| **d** | A | punta + barra de pata a pata | `da` |
| **k** | esquina ┐ | una esquina: arriba y derecha | `ka` |
| **g** | esquina con barra | esquina + barra completa | `ga` |
| **f** | T | barra superior + palo central, grande | `fa` |
| **s** | Z | barra arriba, barra abajo, diagonal | `sa` |
| **m** | cuadro con raya vertical | cerrada, esquinas, dos cuartos | `ma` |
| **n** | círculo con barra Θ | redonda, barra horizontal entera | `na` |
| **l** | horquilla Y | sin punto | `la` |
| **r** | horquilla con punto | punto dentro de la horquilla | `ra` |
| **sh** | X | dos diagonales que se cruzan | `sha` |
| **ch** | ✱ | X + raya vertical | `cha` |

## 4. Las 60 unidades

Cuatro vocales solas y 56 sílabas CV, en el orden canónico del código (U+E000 a U+E03B):

| | A | E | O | U |
|---|---|---|---|---|
| *vocal sola* | `a` | `e` | `o` | `u` |
| **p** | `pa` | `pe` | `po` | `pu` |
| **b** | `ba` | `be` | `bo` | `bu` |
| **t** | `ta` | `te` | `to` | `tu` |
| **d** | `da` | `de` | `do` | `du` |
| **k** | `ka` | `ke` | `ko` | `ku` |
| **g** | `ga` | `ge` | `go` | `gu` |
| **f** | `fa` | `fe` | `fo` | `fu` |
| **s** | `sa` | `se` | `so` | `su` |
| **m** | `ma` | `me` | `mo` | `mu` |
| **n** | `na` | `ne` | `no` | `nu` |
| **l** | `la` | `le` | `lo` | `lu` |
| **r** | `ra` | `re` | `ro` | `ru` |
| **sh** | `sha` | `she` | `sho` | `shu` |
| **ch** | `cha` | `che` | `cho` | `chu` |

<!--pagina-->

## 5. Marcas de estructura

Dos glifos muestran en la escritura nativa la estructura de las palabras (principio de **una forma = un significado**):

| Marca | Glifo | Código | Romano | Ejemplo |
|---|---|---|---|---|
| **Nexo de compuesto** | ‿ curva baja abierta arriba | U+E03C | guion `-` | `sade-kelo` «año» frente a `sade kelo` «sol, ciclo» |
| **Nombre propio** | ᚠ runa Fehu, antes del nombre | U+E03D | mayúscula inicial | `Ana` (nombre) · `Kale` (nombre) frente a `kale` «amarillo» |

## 6. Dígitos

Los nombres de los números son palabras del idioma; los dígitos son su notación escrita (U+E040 a U+E049). En el teclado, la tecla 0–9 inserta directamente el dígito Owee.

<!--digitos-->

Escalas: `tanu` 10 · `gabu` 100 · `soku` 1 000 · `benu` 1 000 000. Operaciones: `dapa` + · `dopo` − · `kebu` × · `faku` ÷ · `se` = · `doto` separador decimal.

## 7. Estilos y libertad de trazo

| Estilo | Familia | Uso |
|---|---|---|
| Recto | **Owee Sans** | pantalla, documentos, carteles |
| Fluido | **Owee School** | escritura a mano y cuadernos |

| Se puede variar | No se puede variar |
|---|---|
| Tamaño, estiramiento, inclinación | La silueta: abierta o cerrada, número de trazos |
| Grosor, remates, serifas | Si lleva barra, punto o raya, y dónde |
| Esquinas vivas o redondeadas | Qué marca de vocal usa |
| Un trazo continuo o varios | Que ninguna se lea como otra al torcerla |

**Regla de oro:** si al girar o espejar un glifo se lee como otro, está mal escrito.

## 8. Codificación y estándar digital

Cadena normativa: **romano → normalización → análisis silábico → ID estable → punto de código → fuente → Owee Script**.

| Nivel | Ejemplo | Función |
|---|---|---|
| Romano | `nara` | entrada canónica y respaldo |
| Sílabas | NA + RA | segmentación (primero `sh` y `ch`) |
| ID estable | OWEE_SYL_NA + OWEE_SYL_RA | identidad que no cambia aunque cambie el dibujo o el código |
| Código | U+E028 U+E030 (uso privado) | almacenamiento |
| Glifo | `nara` | presentación |

| Rango | Contenido |
|---|---|
| U+E000–U+E003 | vocales solas A E O U |
| U+E004–U+E03B | sílabas PA … CHU, en el orden de la matriz |
| U+E03C–U+E03D | nexo de compuesto y marca de nombre |
| U+E03E–U+E03F | reservados |
| U+E040–U+E049 | dígitos 0–9 |

Herramientas que siguen esta norma: fuentes **Owee Sans** y **Owee School** (TTF, OTF, WOFF, WOFF2), `owee.js` (`Owee.toScript`, `Owee.toRoman`), teclado **Fcitx5** 1.2 y **Keyman**, y el **Owee Pad**. Una secuencia imposible (por ejemplo, con `i` o con consonante final) se deja en romano.

## 9. Lista de comprobación

1. Cuatro vocales `a e o u`; la `i` no existe.
2. Catorce consonantes; `sh` y `ch` son una sola unidad.
3. Solo sílabas V y CV: 60 unidades.
4. Vocal **a la derecha** de la consonante, en el mismo renglón, sin tocarla.
5. Más aire entre sílabas que dentro de una sílaba.
6. Nexo ‿ en los compuestos; ᚠ delante de los nombres propios.
7. Dígitos Owee para los números; los signos matemáticos son los internacionales.
8. Ningún glifo es giro o espejo de otro.
