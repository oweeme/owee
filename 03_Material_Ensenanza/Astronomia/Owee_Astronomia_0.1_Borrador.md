# Owee Astronomía y Astrología — borrador 0.1

**Estado: VERIFICADA (pendiente de aprobación).** Material nuevo; cada término pasó la verificación automática (fonología, partes existentes, forma y significado únicos). Como en Química, **no se añade ninguna raíz nueva**: todo se compone con raíces que ya existen (`sade` sol, `mune` luna, `kuna` cielo, `salo` luz, `gadu` gravedad, `duma` movimiento…). Los números llevan glifo numérico y lectura; los cálculos se verifican al generar el sitio.

> **Astronomía y astrología se mantienen separadas.** La astronomía es una ciencia; la astrología es un sistema **simbólico y cultural**. Owee sirve para nombrar ambas, pero no afirma que la segunda tenga valor científico.

## 1. El cielo y los astros
<!--construcciones Astronomía-->

**Cómo se nombran** (principio *concepto + modificador*): una **estrella** es un **sol lejano** (`sade-lu`); un **planeta** es una **tierra que se mueve** (`taro-duma`, como «errante»); la **galaxia** es un conjunto de estrellas (`sade-lu-seta`); una **constelación**, un «signo» de estrellas (`sade-lu-sena`). El telescopio es el **ojo lejano** (`loke-lu`) y el microscopio el **ojo cercano** (`loke-le`).

## 2. Los planetas por orden

Se nombran por **ordinal** (`número-pose`, Gramática 1.1 §10) + `taro-duma`: así no hace falta adaptar los nombres propios (que no caben en la fonología de Owee).

| Planeta | Owee |
|---|---|
| Mercurio | `be-pose taro-duma` |
| Venus | `du-pose taro-duma` |
| Tierra | `ga-pose taro-duma` (o simplemente `taro`) |
| Marte | `fo-pose taro-duma` |
| Júpiter | `sa-pose taro-duma` |
| Saturno | `ku-pose taro-duma` |
| Urano | `mu-pose taro-duma` |
| Neptuno | `na-pose taro-duma` |

El **Sol** es `sade` y la **Luna** es `mune`. El **sistema solar** es `sade-rela` («unión del sol»).

## 3. Movimientos, tiempo y calendario

- **Rotación** de la Tierra: `loda`. El **día** astronómico es `loda-kelo` («ciclo de rotación»).
- **Órbita**: `duma-selo` («movimiento circular»). El **año** es `sade-kelo` («ciclo del sol»).
- El **mes** es `mune-kelo` («ciclo de la luna»).
- **Eclipse solar**: `sade-kose` («sol cerrado»); **eclipse lunar**: `mune-kose`.
- **Direcciones**: este `sade-pado` («donde nace el sol»), oeste `sade-gune` («donde acaba el sol»), norte `kore-go` («lugar arriba»), sur `kore-gu` («lugar abajo»).

```owee
sade go duma
mune sade kose
taro sade duma-selo
loda-kelo sade-kelo palo
```

*El sol sube. · La luna cierra el sol (eclipse). · La Tierra orbita el sol. · El día es una parte del año.*

**Ejemplos numéricos.** Un año tiene unos [[365]] días. La Luna tarda unos [[27]] días en dar una vuelta a la Tierra; entre dos lunas llenas pasan unos 29,5 días: [[29.5]]. Una semana de [[7]] días y un mes de [[4]] semanas suman [[7 × 4 = 28]] días (aproximación).

## 4. Distancias y luz

La distancia media Tierra–Sol es de unos 150 millones de km: [[150 × 1000000 = 150000000]] km. La luz recorre unos 300 000 km cada segundo (`sape salo`): [[300000]] km/s. Tiempo que tarda la luz del Sol en llegar: [[150000000 ÷ 300000 = 500]] s, es decir, unos 8 minutos y 20 segundos.

El **año luz** es la **distancia** (`dase`) que recorre la luz en un año (`sade-kelo`): se conserva como unidad internacional (al).

## 5. Gravedad, órbitas y objetos extremos

`gadu` (gravedad, Física 2.0) mantiene a los astros en órbita (`duma-selo`). Un **agujero negro** es `gadu-bore` («gravedad negra»): la gravedad es tan fuerte que ni la luz (`salo`) escapa. Una **nebulosa** es `boga-kuna` («gas del cielo»). La **atmósfera** es `sura-taro` («aire de la tierra»). Un **cometa** es `suna-goda-duma` («hielo que se mueve») y un **meteoro**, `kuna-pore` («fuego del cielo»).

El **comienzo del universo** (Big Bang) es `gora-pado`, y el **universo** entero es `gora-fese`.

## 6. Astrología (simbólica)

Los **12 signos** del zodiaco combinan **4 elementos** (`pore` fuego, `taro` tierra, `sura` aire, `suna` agua) con **3 modalidades** (`pado` cardinal = «comienzo», `dure` fijo = «duración», `telo` mutable = «cambio»). El nombre Owee de cada signo es simplemente **elemento + modalidad**, un sistema que **coincide exactamente** con la clasificación tradicional.

| Signo tradicional | Owee | Elemento | Modalidad |
|---|---|---|---|
| Aries | `pore-pado` | fuego | cardinal |
| Tauro | `taro-dure` | tierra | fijo |
| Géminis | `sura-telo` | aire | mutable |
| Cáncer | `suna-pado` | agua | cardinal |
| Leo | `pore-dure` | fuego | fijo |
| Virgo | `taro-telo` | tierra | mutable |
| Libra | `sura-pado` | aire | cardinal |
| Escorpio | `suna-dure` | agua | fijo |
| Sagitario | `pore-telo` | fuego | mutable |
| Capricornio | `taro-pado` | tierra | cardinal |
| Acuario | `sura-dure` | aire | fijo |
| Piscis | `suna-telo` | agua | mutable |

Una persona de «fuego cardinal» es `pore-pado`; las cuatro triplicidades (fuego, tierra, aire, agua) y las tres modalidades salen de las mismas raíces con las que se habla del mundo, lo que hace el sistema **fácil de memorizar**.

## 7. Poema: *Kuna*

```owee
kuna-bore bo
sade-lu salo
taro-duma duma
mune go duma
me loke-lu
```

*en la noche / la estrella, luz / el planeta se mueve / la luna sube / mi telescopio.*

## 8. Pendientes de Astronomía

- Nombres de **galaxias, estrellas y constelaciones concretas** (Orión, Sirio…): requieren la norma de nombres propios (Gramática 1.1 §14) o numeración.
- **Fases lunares** (nueva, creciente, llena, menguante): composiciones con `mune`, `pa/po` y `fese`.
- **Calendario**: días de la semana y meses (los nombres tradicionales no caben en Owee; se propone numerarlos: `be-pose loda-kelo`…).
- **Unidades**: al (año luz), UA, parsec se conservan como símbolos.
