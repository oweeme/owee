# Owee Informática — guía para desarrolladores (borrador 0.1)

**Estado: aprobada.** Material nuevo con **una sola raíz nueva** (`bomo`, bug); todo lo demás se compone con raíces que ya existen (`meka` máquina, `mado` cálculo, `doke` datos, `foma` regla, `beka` escritura, `rela` conexión, `mena` memoria, `kare` corrección, `bosa` rotura…). Cada término pasó la **verificación automática** (fonología V/CV sin `i`, partes existentes, ≤ 3 elementos, forma y significado únicos). Ninguno está **aprobado** hasta que lo confirmes.

> **Principio:** el **código no se traduce**. Palabras clave, nombres de funciones y símbolos se quedan como están (`if`, `for`, `==`, `{ }`). Owee aporta el **vocabulario para hablar, enseñar y documentar** el software, igual que en Matemáticas y Física.

## 1. Cómo se construyen los términos

Todos siguen el patrón **raíz principal + modificador** (Gramática 1.1 §6), con el acento en la primera sílaba de cada elemento:

- **Máquina** (`meka`): `meka-mado` computadora, `meka-gume` hardware, `meka-gora` sistema operativo.
- **Regla** (`foma`) y **cálculo** (`mado`): `mado-foma` programa, `foma-beka` código, `mode-mado` algoritmo.
- **Datos** (`doke`) y **memoria** (`mena`): `doke-kopa` archivo, `doke-mena` base de datos, `mena-fena` guardar.
- **Conexión** (`rela`): `rela-gora` internet, `rela-foma` protocolo, `meka-pema` servidor, `meka-gura` cliente.
- **Corrección** (`kare`) y **rotura** (`bosa`): `kare-no` error, `bomo` bug (raíz corta), `bomo-kera` depurar, `kare-mede` prueba.

Cada término cumple el principio de **una forma = un significado**.

## 2. Equipos y sistema
<!--construcciones Informática|Equipos y sistema-->

## 3. Programación
<!--construcciones Informática|Programación-->

**Condiciones y lógica:** `ke` es «si» (if), `ke-no` es «si no» (else), `re` es «y» (and), `lo` es «o» (or), `no` es «no» (not), `se` es «igual» (==), `pa`/`po` son «mayor»/«menor» (`>`, `<`), `tare` es «verdadero» y `tare-no`, «falso». `kelo` es «ciclo» (bucle) y `nuse` es «vacío» (null).

## 4. Datos
<!--construcciones Informática|Datos-->

**Lista y arreglo** son dos conceptos distintos en programación, así que tienen dos formas: `doke-raga` («datos en fila», lista) y `doke-mata` («datos en matriz», arreglo), con las raíces `raga` (fila) y `mata` (matriz) de Matemáticas.

## 5. Redes y web
<!--construcciones Informática|Redes y web-->

## 6. Seguridad
<!--construcciones Informática|Seguridad-->

`fadu` es «seguridad». Cifrar es *cerrar* los datos (`doke-kose`) y descifrar es *abrirlos* (`doke-bure`): las mismas raíces `kose` / `bure` de cerrar y abrir.

## 7. Calidad y depuración
<!--construcciones Informática|Calidad y depuración-->

**`bomo` — bug (raíz corta).** Para el término más frecuente del desarrollador se creó **una raíz corta de 2 sílabas**: **`bomo`** (BO-mo). Es una **mezcla recortada** de las dos raíces que lo explican: **`bo`**(sa), «rotura», y **m**(ado), «cálculo», con armonía de vocal en *o*. Cumple las reglas: V/CV, sin `i`, y **ningún vecino acústico** en el léxico (no se parece a otra palabra), así que no se confunde al oír. Mantiene el vínculo con informática y con `meka-bosa` (fallo del equipo). Con ella: `bomo-kera` = depurar («obtener el bug»).

## 8. Inteligencia artificial
<!--construcciones Informática|Inteligencia artificial-->

## 9. Leer código en voz alta

Las frases se leen con el orden SOV. Los **identificadores se conservan**; el verbo es una raíz Owee:

| Código | Lectura en Owee | Significado |
|---|---|---|
| `x = 5` | `bara fena sa` | la variable pone cinco |
| `x == 5` | `bara se sa` | la variable es igual a cinco |
| `x > 3` | `bara pa ga` | la variable es mayor que tres |
| `if x > 3` | `ke bara pa ga` | si la variable es mayor que tres |
| `else` | `ke-no` | si no |
| `a and b` | `a re b` | a y b |
| `not a` | `no a` | no a |
| `x + 1` | `bara dapa be` | variable más uno |
| `return` | `pema` | dar (devolver) |

```owee
bara fena sa
ke bara pa ga
mado-dare
ke-no
bomo kera
```

*la variable pone cinco / si la variable es mayor que tres / ejecutar / si no / encontrar el bug.*

## 10. Owee en tu software: guía práctica

| Tema | Recomendación |
|---|---|
| **Almacenar texto** | Guarda **siempre en romano** (el texto latino) en bases de datos, URLs, búsqueda y archivos. Convierte a Owee Script **solo al mostrarlo** (así funciona aunque falte la fuente) |
| **Código de idioma** | Usa `lang="qow"` (uso privado, dentro de `qaa`–`qtz` de ISO 639-3) |
| **Validar una palabra** | Expresión regular: `^(?:(?:sh\|ch\|[pbtdkgfsmnlr])?[aeou])+$` (en minúsculas; sin `i`, sin consonante final) |
| **Compuestos** | En el texto, el guion une los elementos (`sade-kelo`). **En identificadores de código** usa guion bajo (`sade_kelo`) o camelCase (`sadeKelo`); en URLs, guion (`/sade-kelo`) |
| **Nombres propios** | Inicial mayúscula en romano (`Ana`); en Owee Script, glifo de marca de nombre U+E03D |
| **Mostrar Owee Script** | Fuente `Owee Sans`/`Owee School` y `owee.js` / `owee.ts` (convierte romano ↔ Owee Script; guion → nexo U+E03C) |
| **Unicode** | El script vive en el área de uso privado U+E000–E049 (y marcas U+E03C–E03D): no lo normalices ni lo guardes como texto principal |
| **Entrada de teclado** | Fcitx5 1.2 (Linux); para otras plataformas, Owee Pad (web) o un futuro teclado Keyman |
| **Internacionalización (i18n)** | Trata Owee como un idioma más: archivos `qow.json` con claves en romano |
| **Tokenizar** | Separa por espacios; cada palabra se divide en sílabas con la regex `(sh\|ch\|[pbtdkgfsmnlr])?[aeou]` |

Ejemplo mínimo (JavaScript):

```js
import { toScript, toRoman, syllables } from './owee.js';
const frase = 'mado-foma kare-mede';      // «programa, prueba»
toScript(frase);                            // texto en Owee Script
syllables('meka');                          // ['me', 'ka']
```

## 11. Palabras que conviene decidir pronto

- **Verbos de uso diario** en el desarrollo: `enviar`, `devolver`, `importar`, `desplegar`, `confirmar` (commit), `ramificar` (branch), `fusionar` (merge): se componen con `pema`, `gura`, `rela`, `fena`, `dare`.
- **Nombres de símbolos**: `{ }`, `[ ]`, `( )`, `;`, `:`, `_` (hace falta decidir si se leen en Owee o en la lengua original).
- **Tecnologías con nombre propio** (Linux, Python, Git…): se escriben con la marca de nombre propio y la norma de adaptación (Gramática 1.1 §14).
