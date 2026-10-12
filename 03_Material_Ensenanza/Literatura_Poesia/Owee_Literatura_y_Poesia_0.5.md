# Owee — Literatura y Poesía 0.5

**Estado:** borrador de trabajo. 0.2 añadió poemas de vida, filiales, de amor, de guerra y de filosofía; 0.3 añadió música y canciones (§8); 0.4 añadió mitos, dioses y cuentos (§9); 0.5 añade canto suave y romance (§8.8–8.9) con la herramienta `ritmo_cancion.py`.
**Línea editorial (decidida):** poesía de **pocas raíces muy cargadas**; el diccionario se amplía solo cuando un texto lo demuestra necesario.
**Base:** Registro maestro + Diccionario Base 1.0 (163 entradas). Todo texto Owee de este documento se
comprueba con `herramientas/validar_owee.py` (fonología V/CV, sin `i`, y que cada raíz exista en el léxico).

> **Regla de oro de este material:** los textos usan **solo vocabulario ya existente**. Lo que haría falta
> y no existe se lista en la sección 7 como *pendiente de decisión*; no se inventa en silencio
> (regla del Registro: las propuestas nuevas permanecen separadas hasta ser aceptadas).

---

## 1. Qué le da Owee a la poesía

Lo que ya define el idioma crea una poética propia sin añadir nada:

| Rasgo de Owee | Efecto poético |
|---|---|
| Solo sílabas V / CV, sin consonantes finales | Todo verso es una cadena limpia de sílabas abiertas; el ritmo se cuenta sin ambigüedad |
| Acento siempre en la 1.ª sílaba | Cada palabra de 2 sílabas es un pie *fuerte–débil*; un verso de 3 palabras tiene 3 golpes regulares |
| Solo 4 vocales (`a e o u`) | La rima por la vocal final es natural: `-a`, `-e`, `-o`, `-u` |
| Sin género, número ni conjugación | Los versos son densos y no obligan a precisar lo que el poeta quiere dejar abierto |
| Vocabulario conceptual (`suna` = agua, `salo` = luz…) | Imágenes elementales; cada raíz carga un campo, no un objeto concreto |
| Modificador **después** del concepto | Las imágenes se construyen concepto → matiz (`kuna-bore`, cielo + negro) |
| Escritura: 1 sílaba = 1 bloque | La métrica es **visible**: contar bloques es contar sílabas |

## 2. Reglas métricas propuestas

*(Convenciones de estilo literario, no de gramática. Pueden cambiarse sin tocar el idioma.)*

1. **Medida:** se cuenta en sílabas Owee (= bloques escritos). La vocal larga (`aa ee oo uu`) cuenta como una.
2. **Verso:** de 3 a 8 sílabas es la medida natural; versos de 4–6 son el estándar.
3. **Ritmo:** el acento cae en la primera sílaba de cada palabra; un verso de *n* palabras tiene *n* acentos.
4. **Rima:** por **vocal final** (asonancia). Rima plena opcional: misma sílaba final (`-ra`, `-ne`…).
5. **Pausa:** el verso termina donde termina la frase; el salto de línea hace de signo de pausa.
6. **Tiempo en relato:** el marcador (`pe`, `pu`) se pone **una vez** al abrir el relato; el contexto lo sostiene
   (aplicación de «no expresar dos veces lo ya expresado»).
7. **Puntuación:** aún no hay puntuación propia de Owee (pendiente en el Registro, §65). Aquí se usa `,` y `.`
   latinos, que el IME deja pasar.

## 3. Formas poéticas propuestas

Los nombres están en español; los nombres Owee son una **propuesta** (compuestos de raíces existentes) y
solo se vuelven estables si los aceptas.

| Forma | Descripción | Nombre Owee propuesto |
|---|---|---|
| **Dístico** | 2 versos | `soma-du` (idea-2) |
| **Cuarteto** | 4 versos, asonancia libre | `soma-fo` (idea-4) |
| **Poema-ciclo** | El último verso reenvía al primero | `kelo` (ciclo) |
| **Poema-cadena** | Cada verso empieza con la última palabra del anterior; encadena y cierra en círculo | `rela` (unión) |
| **Tríptico temporal** | Tres versos: pasado `pe` / presente `te` / futuro `pu` | `tera-ga` (tiempo-3) |
| **Dicho** | Una sentencia breve de 2–3 palabras | `soma` (idea) |

## 4. Poemas

### 4.1 Tera kelo — *El ciclo del tiempo* (poema-ciclo, 5 sílabas)

```owee
sade go duma
sade gu duma
mune go duma
mune gu duma
```

*sol arriba se mueve / sol abajo se mueve / luna arriba se mueve / luna abajo se mueve.*
Sube y baja el sol; sube y baja la luna. Al terminar, el verso 1 vuelve a empezar: el poema no acaba, **gira**.

### 4.2 Rela — *Unión* (poema-cadena, 4 sílabas)

```owee
suna salo
salo sura
sura sone
sone doma
doma lore
lore suma
suma suna
```

*agua, luz / luz, aire / aire, sonido / sonido, corazón / corazón, afecto / afecto, vida / vida, agua.*
Ocho conceptos del Núcleo inicial, cada uno atado al siguiente. El último (`suna`) es el primero: cierra el círculo.
Es también un ejercicio: lee cada par como «A con B».

### 4.3 Kuma — *Casa* (cuarteto, 6 sílabas)

```owee
me kuma bo mora
tu kuma bo mora
ne kuma bo malo
kuma lore mude
```

*yo en casa existo / tú en casa existes / el grupo en casa, en calma / casa de afecto lleno.*
Muestra: localización sin cópula (`kuma bo`), pronombres, y la construcción **concepto + modificador**
(`kuma` + `lore mude`, «casa [de afecto lleno]»).

### 4.4 Kuna-bore — *Noche* (cuarteto, 5-4-4-4)

```owee
kuna-bore bo
mune salo
nara sule
doma malo
```

*en la noche / luna, luz / la persona duerme / corazón, calma.*
Cuatro imágenes sin verbo: el cuadro lo completa el lector. `kuna-bore` (cielo + negro) es una **composición
poética**, no una palabra aprobada (ver §6).

### 4.5 Pe, te, pu — *Antes, ahora, después* (tríptico temporal, 4 sílabas)

```owee
me pe lare
me te karo
me pu tase
```

*yo antes supe / yo ahora entiendo / yo después aprenderé.*
Los tres marcadores temporales (`pe`, `te`, `pu`) en paralelo: el saber como camino en el tiempo.

### 4.6 Vida — *Kelo suma* (poema-ciclo)

```owee
suma-pado
nara tame
tera duma
nara gule
suma-gune
suma-pado
```

*nacimiento / persona nueva / el tiempo se mueve / persona vieja / muerte / nacimiento.*
`tame` (nuevo) y `gule` (viejo) son los dos extremos; el tiempo (`tera duma`) es lo único que se mueve entre ellos.
El último verso repite el primero: la vida es un ciclo (`kelo`).

### 4.7 Filial — *Pade naku* (progenitor y descendiente)

```owee
me pade pe suma pema
me pade pe fela
me pade pe galo
me naku pu pema
```

*mi progenitor me dio vida / me enseñó / me ayudó / mi descendiente dará.*
Lo recibido se vuelve lo que se da. Los verbos `pema` (dar) cierran y abren la cadena entre generaciones.
`pade` y `naku` son neutros: sirven para padre o madre, hijo o hija.

Segundo poema, el reverso (voz del progenitor):

```owee
me naku pe tame
me naku te gore-pa
me naku pu daro
me lore no fese
```

*mi descendiente fue nuevo / mi descendiente ahora es grande / mi descendiente trabajará / mi afecto no tiene límite.*

### 4.8 Amor — *Tu ko* (contigo)

```owee
tu ko, me kuna-salo
tu so, me kuna-bore
me doma tu bo
```

*contigo, mi día / sin ti, mi noche / mi corazón, en ti.*
El contraste nace solo de dos relaciones, `ko` (con) y `so` (sin). `kuna-salo` y `kuna-bore` son composiciones
(§6). El último verso no lleva verbo: el corazón *está en* ti (`bo`, interior).

### 4.9 Guerra y paz — *Naro balo naro* (grupo contra grupo)

```owee
naro balo naro
fada pore ko
taro bosa
kore nuse
suma-gune mude
sone nuse
```

*grupo contra grupo / enojo con fuego / la tierra se rompe / el lugar queda vacío / lleno de muerte / el sonido vacío.*
Seis versos sin una palabra de adorno: causa (`fada`), medio (`pore`), efecto (`bosa`, `nuse`), balance
(`mude` de muerte, `nuse` de sonido). Se cierra con silencio: `sone nuse`.

Poema de respuesta:

```owee
fada gune
malo pado
saro reme
tera duma
```

*el enojo termina / la calma comienza / comunidad, amistad / el tiempo se mueve.*
Un poema que mira al primero como un espejo: `gune` (fin) ↔ `pado` (comienzo).

### 4.10 Filosofía — *Rena* (pensar)

```owee
me rena, me mora
tera duma, me telo
me gade telo ka
tare ka-kore
```

*pienso, existo / el tiempo se mueve, yo cambio / ¿mi identidad cambia? / ¿dónde está la verdad?*
Cuatro versos con las tres raíces ontológicas (`mora`, `gade`, `tare`). Las dos preguntas usan `ka`
(sí/no) y `ka-kore` (dónde). Nota: la posición de interrogativos informativos aún es una decisión pendiente
del Registro (§7): aquí aparece sola al final del verso, que es la lectura más segura.

Dichos filosóficos:

```owee
nara gora palo
pado gune, gune pado
rela suma
mora gade ko
```

*la persona es parte del mundo / el comienzo es fin, el fin es comienzo / la unión es vida / la existencia, con identidad.*

## 5. Prosa y otros textos

### 5.1 Relato breve — *Nara ko suna* (La persona y el agua)

El marcador `pe` se pone una sola vez; el resto del relato queda en pasado por contexto.

```owee
nara pe duma
nara suna nume
suna lu
nara sape-po duma
suna kera
nobe pume
nara malo
```

| Owee | Español |
|---|---|
| nara pe duma | Una persona se puso en marcha. |
| nara suna nume | Deseaba agua. |
| suna lu | El agua estaba lejos. |
| nara sape-po duma | Caminó despacio. |
| suna kera | Consiguió agua. |
| nobe pume | Bebió. |
| nara malo | Quedó en calma. |

*Estructura:* partida → deseo → obstáculo → esfuerzo → logro → calma. Es el molde del cuento mínimo en Owee.

### 5.2 Dichos (proverbios)

```owee
suma duma
reme faro-pa
ke tu galo, ne galo
lare no fese
tera telo, tare no telo
```

| Owee | Español |
|---|---|
| suma duma | La vida es movimiento. |
| reme faro-pa | La amistad es fuerte. |
| ke tu galo, ne galo | Si tú ayudas, el grupo ayuda. |
| lare no fese | El saber no tiene límite. |
| tera telo, tare no telo | El tiempo cambia; la verdad no cambia. |

### 5.3 Diálogo mínimo (para teatro y práctica oral)

```owee
tu sado ka
me sado, me malo
tu ka
```

*¿Estás bien? — Estoy bien, estoy en calma. — ¿Y tú?*

## 6. Composiciones poéticas sugeridas (NO son léxico)

Combinaciones **concepto + modificador** con raíces existentes, útiles como imágenes. Se escriben con guion,
como las derivaciones del diccionario, pero **no** se añaden al léxico mientras no las apruebes.

| Composición | Construcción | Imagen |
|---|---|---|
| `kuna-suna` | cielo + agua | lluvia |
| `kuna-bore` | cielo + negro | noche |
| `mune-salo` | luna + luz | luz de luna |
| `suma-pado` | vida + comienzo | nacimiento |
| `suma-gune` | vida + fin | muerte |
| `doma-duma` | corazón + movimiento | emoción, latido |
| `dune-lena` | sentir + agrado | alegría (forma establecida en el Primer Diccionario) |

## 7. Lo que falta para una literatura más rica (decisiones tuyas)

Conceptos que la poesía pedirá pronto y que **no existen** en el léxico actual. Para cada uno conviene decidir
si se **compone** (barato, sin tocar el vocabulario) o se **crea una raíz nueva** (cuesta; hay que revisar colisiones).

| Concepto | ¿Componer? | Nota |
|---|---|---|
| noche / día | `kuna-bore` / `kuna-salo` | Parece que una composición basta |
| mar, río, lago | `suna` + modificador de tamaño/lugar | p. ej. `suna gore-pa` |
| montaña | `taro gore-pa` o `taro go` | Requiere decisión |
| viento | `sura duma` | Natural |
| estrella | `kuna salo` | Natural |
| flor, árbol | `nelo` + modificador | Probable raíz propia si se usa mucho |
| canto, palabra, nombre | `sone`, `reka`, `sena` + modificador | `sone lena` = sonido agradable |
| bello / triste | `lafe-pa` / `dune-po` | `lafe` es aún PROVISIONAL |
| amor | `lore` | Ya existe (afecto) |
| sueño (dormir/soñar) | `sule` + `soma` | Distinguir dormir de soñar |
| verbos «decir», «cantar», «caminar» | — | No hay verbo dedicado: hoy `reka`, `sone`, `duma` cargan ese sentido por contexto |

**Decisión tomada:** poesía de pocas raíces muy cargadas, y construir el diccionario con rigor por debajo
(sitio web: sección *Diccionario*, con campos, uso en textos y raíces sin usar). Ampliar solo lo que los textos
demuestren necesario.

## 8. Música y canciones

Owee es una lengua muy **cantable** por construcción. Esta sección fija una prosodia musical propuesta y presenta las primeras canciones.

### 8.1 Por qué Owee canta bien

| Rasgo | Consecuencia musical |
|---|---|
| Todas las sílabas son abiertas (V/CV) | Cualquier sílaba admite una nota larga: no hay consonantes finales que cortar |
| Solo 4 vocales (`a e o u`) | Vocales puras y estables; `a` y `o` son las más abiertas para notas sostenidas, `u` para notas graves |
| Acento siempre en la 1.ª sílaba | La **primera sílaba de cada palabra cae en tiempo fuerte**: sin conflicto entre acento y compás |
| Sin `i` ni consonantes finales | No hay diptongos ni cierres: el canto fluye |
| Sin conjugación | Se puede cambiar de lugar o repetir una palabra sin romper la gramática |

### 8.2 Prosodia musical propuesta

1. **Una palabra de 2 sílabas = un pulso** (dos corcheas: fuerte–débil).
2. **Los monosílabos son átonos** (`me`, `tu`, `bo`, `ko`, `pe`…): forman anacrusa y se apoyan en la palabra siguiente.
3. **Compás por número de pulsos del verso:** 2 palabras → 2/4 (o 4/4 lento, dos tiempos por palabra) · 3 palabras → 3/4 (o 6/8) · 4 palabras → 4/4. Un verso solo de monosílabos (`tu ko`) lleva un pulso por palabra.
4. **Rima:** asonancia por vocal final; en estribillos, rima plena (misma sílaba final).
5. **Repetición:** una palabra repetida (`sule, sule`) es un recurso normal; no cambia la gramática.
6. **Canon:** cualquier poema-ciclo (`kelo`) es un canon natural: el §4.1 *Tera kelo* se canta a 4 voces, cada una entrando un verso más tarde.

La herramienta `herramientas/prosodia.py` calcula pulsos y compás de cada verso (la `▲` marca el tiempo fuerte; el `·` un átono):

```text
python3 herramientas/prosodia.py Owee_Literatura_y_Poesia_0.5.md -s Sule
```

### 8.3 Sule — *Canción de cuna* (2/4, lento, ♩ = 60)

Forma: A (estrofa) · B (estribillo) · A · B.

```owee
naku sule
mune salo
kuna malo
me lore mora
```

*hijo, duerme / la luna, luz / el cielo, calma / mi afecto está.*

Estribillo (se repite):

```owee
sule sule
kuma bo, kuma bo
fadu mora
```

*duerme, duerme / en casa, en casa / la seguridad existe.*

### 8.4 Doma bo — *Canción de amor* (4/4, balada lenta, ♩ = 72)

> Cántala en **estilo romance** (§8.8): acento por duración y altura, legato. En estilo marcha suena a grito.

Forma: A · A · B (estribillo) · A · B.

```owee
tu ko, me kuna-salo
tu so, me kuna-bore
tera duma
doma no duma
```

*contigo, mi día / sin ti, mi noche / el tiempo se mueve / el corazón no se mueve.*

Estribillo:

```owee
tu ko, tu ko
me doma lena
tu ko, tu ko
me suma salo
```

*contigo, contigo / mi corazón, agrado / contigo, contigo / mi vida, luz.*

### 8.5 Naro duma — *Canción de comunidad y trabajo* (2/4, marcha, ♩ = 112)

Forma: estrofa solista · estribillo coral (todos).

```owee
ke tu galo, ne galo
saro faro-pa
daro kefe
fadu mora
```

*si tú ayudas, el grupo ayuda / la comunidad es fuerte / el trabajo sostiene / la seguridad existe.*

Estribillo coral:

```owee
naro duma
daro galo
reme faro-pa
saro fadu
```

*el grupo se mueve / el trabajo ayuda / la amistad es fuerte / la comunidad, seguridad.*

### 8.6 Tera kelo — *Canon a 4 voces*

Letra del §4.1 (sin cambios), 2/4 o 3/4 lento. Cada voz canta el poema entero; la voz 2 entra cuando la 1 llega al segundo verso, etc. Como el último verso enlaza con el primero, el canon **no tiene final natural**: se detiene cuando el director decide.

### 8.7 Cómo escribir una canción nueva

1. Elige el **compás** y cuenta palabras por verso (2, 3 o 4).
2. Escribe el verso en el `.md` dentro de un bloque `owee`.
3. Valida: `validar_owee.py` (vocabulario y fonología).
4. Analiza: `prosodia.py` (pulsos y compás).
5. Pon la melodía: la primera sílaba de cada palabra de 2+ sílabas va en tiempo fuerte.

### 8.8 Cantar con suavidad: el acento sin gritar

**El problema.** En Owee el acento cae **siempre en la primera sílaba** de cada palabra. Si cada acento se canta *fuerte y seco* sobre el tiempo fuerte, suena a **marcha o a grito**: perfecto para un himno, pero no para un romance. **No hace falta tocar la raíz de los acentos.** El acento sigue donde está; lo que se elige es **cómo se realiza al cantar**.

**Idea clave:** un acento puede marcarse con cuatro cosas distintas. La marcha lo hace con *intensidad*; el romance lo hace con *duración* y *altura*:

| Dimensión del acento | Marcha / grito | Romance | Canción de cuna |
|---|---|---|---|
| Intensidad (volumen) | fuerte (f–ff) | casi pareja (p–mp) | muy suave (pp) |
| Duración | corta | **la sílaba acentuada dura el doble** | larga, tres veces |
| Altura | plana (tónica/quinta) | **un grado más aguda** | rango estrecho |
| Articulación | staccato | **legato** (las notas se unen) | legato muy ligado |
| Tempo | 112 BPM | 54–72 BPM | ~54 BPM |
| Final de verso | corto | **largo (2 tiempos)** y vuelve a la nota base | muy largo |

**Recetas para un romance**

1. **Acento = nota larga o más aguda, no más fuerte.** Dinámica pareja y **legato**: así el acento se *oye* sin golpear.
2. **Aprovecha que todo es sílaba abierta.** No hay consonante final que corte: las palabras se ligan solas. Canta en **frases largas** y respira tras 2 o 3 palabras.
3. **Rompe el vaivén de marcha.** Muchas palabras de dos sílabas seguidas dan «fuerte-débil, fuerte-débil»; mézclalas con **monosílabos de anacrusa** (`me`, `tu`, `bo`, `ko`) y con **compuestos largos** (`kuna-bore`, `sade-kelo`), que hacen arcos más amplios.
4. **Melismas con vocales largas.** Owee ya permite alargar las vocales (`aa ee oo uu`): escribe `suuna` o `lenaa` y canta varias notas sobre esa vocal. La sílaba acentuada **sigue siendo la misma**.
5. **Paleta de consonantes suaves.** Las consonantes `m n l r s f sh` (sonantes y fricativas) suenan envolventes; `p t k b d g ch` (oclusivas) suenan secas. Para un romance, elige palabras de la paleta suave:
   - **Suaves (41 del léxico base):** `mene` · `rane` · `nara` · `suma` · `rela` · `faro` · `salo` · `suna` · `sura` · `fure` · `lare` · `rena` · `sone` · `luma` · `nume` · `mora` · `nelo` · `ruma` · `mune` · `sule` · `mena` · `soma` · `lena` · `malo` · `lore` · `fena` · `naro` · `mela` · `reme` · `sare` · `saro` · `foma` · `fame` · `lafe` · `nuse` · `fese` · `rale` · `fale` · `fela` · `sena` · `mase`
   - **Fuertes (19):** `gade` · `pode` · `paku` · `kade` · `pade` · `bade` · `pado` · `kopa` · `tabe` · `dabo` · `doke` · `beka` · `bado` · `tada` · `gabu` · `dapa` · `dopo` · `kebu` · `doto`
6. **Rima y final en vocales abiertas.** Termina el verso en `a` u `o` para sostener la nota; la `u` da intimidad. Cierra siempre en la **nota base**.
7. **Compás.** 3/4 lento o 6/8 de balada; 54 a 72 BPM.
8. **Permitido:** que la sílaba acentuada vaya en un tiempo débil, sincopada, **siempre que siga siendo la más prominente de su palabra** por duración o altura. **Prohibido:** mover el acento a otra sílaba (eso sí rompería la raíz).

**Herramienta.** `herramientas/ritmo_cancion.py` convierte una letra en un boceto (MIDI, WAV y ABC) según el estilo, para *oír la diferencia* sin cantante:

```text
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Doma bo" --estilo romance -o audio
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Doma bo" --estilo marcha  -o audio
```

La misma letra de *Doma bo* suena a balada con `romance` y a grito con `marcha`. Son bocetos de ritmo y acento (sin voz); los archivos de demostración están en `audio/`.

### 8.9 Mune lore — *Canción de romance* (paleta suave, 3/4 lento)

Toda la letra usa **consonantes suaves** y vocales abiertas; solo `tu` aporta una oclusiva.

```owee
mune salo mora
suna sone lena
me lore, tu nume
lena, lena, malo
```

*la luna, luz, existe / el agua, sonido, agrado / mi afecto, tu deseo / agrado, agrado, calma.*

Estribillo (se repite):

```owee
tu me suma
me tu lore
mune, mune, salo
```

*tú eres mi vida / yo te quiero (yo, a ti, afecto) / luna, luna, luz.*

Para cantarla: tempo 60, estilo `romance`, estribillo con la vocal final de `salo` alargada (`saloo`). Pronúnciala siguiendo la guía de pronunciación.

### 8.10 Mune kuma — *Canción de cuna de cuento de hadas* (6/8, ♩ = 58)

Un cuento cantado para dormir. Estructura: **apertura** (`pado`, «al principio») → **cuento** → **estribillo de arrullo**. Lleva el **vocativo** (`naku, sule`) y usa casi solo consonantes suaves.

**Estrofa 1 — el cuento de la luna**

```owee
pado, mune pe mora
mune kuma kuna bo
mune naku, sade-lu
sade-lu salo lena
```

*al principio, la luna existía / la casa de la luna, en el cielo / los hijos de la luna, las estrellas / las estrellas, luz agradable.*

**Estrofa 2 — el pájaro del sueño**

```owee
kuna-bore, ruma-kuna duma
ruma-kuna sule pema
naku sule
mune malo
```

*en la noche, el pájaro se mueve / el pájaro da sueño / el niño duerme / la luna, calma.*

**Estribillo (se repite al final de cada estrofa)**

```owee
naku, sule, sule
mune lore
kuma bo, kuma bo
fadu mora
```

*hijo, duerme, duerme / la luna te quiere (afecto) / en casa, en casa / la seguridad existe.*

**Cómo está pensada**
- **Compás 6/8 y paso de balanceo**: cada palabra de dos sílabas es una «mecida» (larga–corta); el acento sigue en la primera sílaba.
- **Escala mayor pentatónica** (re–mi–fa♯–la–si) y **acompañamiento de caja de música** (acordes D – Bm – G – A): suena a cuento sin resultar infantil.
- **Frases A – A′ – B – A**: la tercera frase repite el motivo de la primera una nota más arriba; la última cierra en la tónica.
- **Paleta suave**: `mune`, `salo`, `lena`, `malo`, `lore`, `suma`, `kuma`. El vocativo `naku,` inicia el estribillo.

**Hazla tuya (melodía propia o automática)**

```text
# 1) Boceto automático con melodía elaborada y acompañamiento
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Mune kuma" --estilo hadas -o audio
# 2) Solo el ritmo (una nota por sílaba) para que compongas tú la melodía
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Mune kuma" --estilo hadas --melodia ritmo -o audio
# 3) Tu propia melodía: genera la plantilla, rellena las notas y vuelve a ejecutar
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Mune kuma" --estilo hadas --plantilla -o audio
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Mune kuma" --estilo hadas --melodia audio/mune_kuma_melodia.txt -o audio
```

### 8.11 Mena bo — *Balada de nostalgia* (4/4, ♩ = 76, do♯ menor)

Canción **original** escrita en Owee con el ánimo de una balada de añoranza y la forma clásica: **estrofa – coro – solo – estrofa – coro – puente – coro final**. Usa la armonía de la balada (C#m, B, A, E, G#m, F#m) que me pasaste como **plantilla de acordes**; la letra es nueva. Las líneas que empiezan con `#` son **directivas** para la herramienta (tonalidad y acordes) y no forman parte de la letra.

**Estrofa 1** (acordes C#m B A E)

```owee
# tono: C#m
# acordes: C#m B A E
kuna-bore, me mena bo tu mora
tera pe duma, me nume no duma
tu kore lu, me doma tu bo
me suma tu so, fure-po
# acordes: C#m G#m A E B
me pe bosa, me lare
tu pe nume rude, me no pe karo
tera lu, kuna-bore le
me nume: tu ko pu-kelo
```

*en la noche, en mi memoria tú existes / el tiempo pasó, mi deseo no pasa / tu lugar está lejos, mi corazón en ti / mi vida sin ti, fría // yo rompí, lo sé / tú querías reparar, yo no entendí / el tiempo lejos, la noche cerca / quiero: contigo, otra vez.*

**Coro** (acordes F#m B G#m C#m A B E)

```owee
# acordes: F#m B G#m C#m A B E
tu ka-kore mora
me kuna-bore bo, tu sone
tu le, me fure-pa
tu lu, me fure-po
de pado, tu me lore
tu ka-kore mora
tu ka-kore mora
```

*¿dónde estás? / en mi noche, tu voz / tú cerca, yo cálido / tú lejos, yo frío / desde el comienzo, tú eres mi afecto / ¿dónde estás? / ¿dónde estás?*

**Solo** (instrumental, sobre la armonía de la estrofa)

**Estrofa 2** (acordes C#m B A E)

```owee
# acordes: C#m B A E
me kalu-duma, kuna-bore bo
sade-lu salo, mune malo
me tu nume, me tu pu kera
ke tu nume, tera bure
```

*camino en la noche / las estrellas brillan, la luna en calma / te deseo, te encontraré / si tú quieres, el tiempo se abre.*

**Puente** (acordes A B A B E)

```owee
# acordes: A B A B E
kuna-bore mude
sone nuse
me kuma nuse
ke tu pu duma, kuma mude
tu ka-kore mora
```

*la noche llena / el sonido vacío / mi casa vacía / si tú vienes, la casa se llena / ¿dónde estás?*

**Cómo está construida**
- **Nostalgia con la gramática de Owee:** `me nume no duma` («mi deseo no pasa») usa la negación `no` junto al verbo; `tu so` («sin ti») usa `so`; el paralelo `tu le, me fure-pa` / `tu lu, me fure-po` convierte cerca y lejos en calor y frío.
- **Vocativo y pregunta:** `tu ka-kore mora` («¿dónde estás?») es el gancho del coro: el interrogativo ocupa el lugar de lo preguntado, sin `ka` al final.
- **Estilo de canto:** `balada` (romance a 76 BPM): el acento por **duración y altura**, no por volumen, para que el coro emocione sin gritar.
- **Acordes:** la herramienta los reparte verso a verso y los usa para el acompañamiento y para la hoja ABC.

```text
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Mena bo" --estilo balada -o audio
python3 herramientas/ritmo_cancion.py Owee_Literatura_y_Poesia_0.5.md -s "Mena bo" --estilo balada --melodia ritmo -o audio
```

## 9. Mitos, dioses y cuentos

### 9.1 Nombrar a los dioses

Una **deidad** es una *persona del cielo* (`kuna-nara`). Los dioses **elementales** se nombran con su elemento + `nara`: así el panteón sale de las raíces que ya existen y no hace falta inventar nombres propios.

| Deidad | Owee | Construcción |
|---|---|---|
| deidad (en general) | `kuna-nara` | cielo + persona |
| del fuego | `pore-nara` | fuego + persona |
| del agua | `suna-nara` | agua + persona |
| de la tierra | `taro-nara` | tierra + persona |
| del aire | `sura-nara` | aire + persona |
| de la vida | `suma-nara` | vida + persona |
| del sol / de la luna | `sade-nara` / `mune-nara` | sol/luna + persona |
| de la muerte | `suma-gune-nara` | fin de la vida + persona |

### 9.2 Gora pado — *El comienzo del mundo* (mito de creación)

```owee
pado
gora nuse
salo no
sone no
kuna-nara pe mora
kuna-nara pe reka
salo pe mora
sade pe mora
mune pe mora
taro-nara pe suna dare
suna-nara pe suma dare
suma pe duma
nara pe mora
gora lena
```

*al principio / el mundo, vacío / ni luz / ni sonido / la deidad del cielo existió / la deidad del cielo habló / la luz existió / el sol existió / la luna existió / la deidad de la tierra hizo el agua / la deidad del agua hizo la vida / la vida se movió / la persona existió / el mundo, agrado.*

Estructura: **vacío** (`nuse`) → **palabra** (`reka`) → **luz** → **astros** → **agua** → **vida** → **persona**. Sin una sola palabra nueva.

### 9.3 Sade re mune — *El sol y la luna* (mito sobre los eclipses)

```owee
sade re mune pe reme
sade go duma
mune gu duma
sade re mune lu pe mora
sade mune tada pe nume
mune pe reka
kelo, tu me pu tada
ke kelo gune, sade-kose
```

*el sol y la luna fueron amigos / el sol sube / la luna baja / el sol y la luna estaban lejos / el sol deseó tocar a la luna / la luna habló: «en el ciclo, tú me tocarás» / cuando el ciclo termine, eclipse.*

### 9.4 Ruma-kuna re ruma-suna — *El pájaro y el pez* (fábula)

```owee
ruma-kuna pe duma
ruma-kuna suna nume
suna lu
ruma-kuna pe reka
«suna ka-kore»
ruma-suna pe reka
«suna kore-le mora»
ruma-kuna pe nobe pume
ruma-kuna lena
ke tu galo, ne galo
```

*el pájaro se movió / el pájaro deseaba agua / el agua estaba lejos / el pájaro habló: «¿dónde está el agua?» / el pez habló: «el agua existe aquí» / el pájaro bebió / el pájaro, agrado / si tú ayudas, el grupo ayuda.*

### 9.5 Convenciones narrativas

1. **Apertura:** `pado` («al principio») abre el relato; **cierre:** `gune` («fin») lo termina.
2. **Tiempo:** `pe` **una sola vez** en la primera oración; el resto queda en pasado por contexto.
3. **Diálogo:** el verbo `reka` presenta al que habla y su discurso va **entre « »** en la línea siguiente.
4. **Personajes:** sin nombres propios, se nombran por su **función** o su **elemento** (`ruma-kuna`, `sade-nara`), con el vocativo propuesto en la Gramática 1.1 si se les habla.
5. **Moraleja:** una línea final en forma de **dicho** (§5.2), separada del relato.

## 10. Siguientes pasos sugeridos

1. Que revises los poemas (§4) y el relato y me digas cuáles suenan *a Owee* y cuáles no.
2. Decidir las composiciones de la §6 (aprobar / rechazar).
3. Resolver los pendientes del Registro que afectan al texto largo: posición de interrogativos y puntuación.
4. Escribir 10–20 textos más breves (dichos, cuartetos) y **de ahí** extraer qué vocabulario falta.
5. ✓ PDF imprimible con Owee Sans: `Owee_Literatura_y_Poesia_0.5.pdf` (se genera desde el sitio web).
