# Owee — estado actual, pendientes y áreas por cubrir

**Fecha:** 2026-10-12 (actualizado tras la revisión semántica, la aprobación y el lote 2). Resultado de una verificación completa con `verificar_todo.py` (se ejecuta con un solo comando y termina con código de error si algo falla).

## 1. Verificación: todo en orden

| Comprobación | Resultado |
|---|---|
| Textos Owee (9 archivos): fonología V/CV sin `i` y vocabulario existente | ✅ válidos |
| Léxico base: 233 formas (incluye los 29 compuestos recuperados del *Primer Diccionario Conceptual*) · Léxico ampliado: 1 027 formas (lotes 3–14) | ✅ 142 auditadas · **885 aprobadas** · **0 verificadas pendientes** · 0 por revisar |
| Colisiones exactas, fonología inválida, partes inexistentes | ✅ ninguna |
| Sitio web: 26 páginas (curso incluido), enlaces internos y anclas | ✅ sin enlaces rotos |
| **Revisión semántica de términos nuevos** (forma única en todo el proyecto y los PDFs antiguos, sin sinónimos, raíces con significado adecuado) | ✅ 168 OK · 27 ajustados · 0 en espera — ver `02_Diccionario/datos/revision_semantica.md` |
| Traducciones de interfaz (66 textos) | ✅ generan; 19 avisos por términos aún sin aprobar |
| Python (compila) y JavaScript (sintaxis) | ✅ |
| Repositorio público en GitHub (licencias CC BY-SA / OFL / MIT) | ✅ |
| Cobertura de vocabulario básico (lista de trabajo de 114 conceptos) | 66 % con forma · 32 % componible · 1 pendiente (`soñar`) |
| **Cobertura Swadesh-100 (lista estándar entre lenguas)** | **90 % con forma · 9 % componible · 1 % falta (`piojo`)** — antes del lote 1 era 56 / 9 / 35 |
| Cada bloque Owee con su traducción | ✅ sin excepciones |

> **Hallazgo y resolución:** la lista propia de 114 conceptos daba una cobertura casi completa, pero la lista **Swadesh de 100 palabras** (más exigente y objetiva) revela el hueco real: **35 conceptos faltan**, casi todos de **cuerpo humano y naturaleza concreta** (piel, sangre, hueso, oreja, diente, lengua, rodilla, cuello, hoja, semilla, raíz, piedra, arena, humo, ceniza, huevo, cola, pluma, cabello…) y de **acciones del cuerpo** (morder, nadar, volar, yacer, estar de pie). **Resuelto con el lote 1** (60 términos de cuerpo, animales, naturaleza y posturas, todos compuestos de raíces existentes).

## 2. Qué hay hecho (organizado por área)

| Área | Contenido | Estado |
|---|---|---|
| **Fonología y escritura** | 4 vocales, 14 consonantes, 60 sílabas, acento inicial; Owee Script 3.4 con 72 glifos nuevos (sílabas, dígitos, nexo `‿`, marca de nombre `ᚠ`): geométricos, por familias, recto y fluido; vocales con forma propia; ver `GUIA_DE_ESTILO_v4.md` | cerrado |
| **Pronunciación** | Guía con AFI y transcripción para hispanohablantes, alargamiento expresivo (`tareee`) | aprobado |
| **Gramática** | Base 1.0 + propuesta 1.1 (sí, imperativo, vocativo, demostrativos, cuantificadores, relativas con `ra`, ordinales, negativos con `po`, nombres propios) | **parcialmente confirmada** |
| **Vocabulario general** | 200 formas (Base 1.0) + 40 de vida diaria + 27 de gramática | aprobado |
| **Matemáticas** | Numeración con glifos numéricos, aritmética a cálculo, estadística, vectores; ejemplos verificados automáticamente | auditado 2.0 |
| **Física** | De cinemática a relatividad, con ejemplos resueltos | auditado 2.0 |
| **Química** | Materia, reacciones, ácidos y bases, redox, 0 raíces nuevas | aprobado |
| **Astronomía / astrología / mitología** | Planetas por ordinal, zodiaco elemento × modalidad, panteón elemental | aprobado |
| **Informática** | 58 términos y 1 raíz nueva (`bomo`, bug); guía para desarrolladores | aprobado |
| **Interfaz (UI)** | 19 términos y 66 textos de menú (archivo, guardar, configuración…) | **verificado, falta aprobar** |
| **Cuerpo y naturaleza (lote 1)** | 60 términos: piel, sangre, hueso, oreja, diente, lengua, piedra, arena, humo, hoja, semilla…; posturas | **aprobado** |
| **Vida diaria (lote 2)** | 92 términos: hoy/ayer/mañana, semana, comidas, ciudad y geografía, familia ampliada, cocina, casa y ropa, salud, dinero y compras, transporte y viaje; verificados por practicidad (máximo 6 sílabas) | **aprobado** |
| **Animales y orientación** | norma de animales por categoría (`ruma-taro`, `ruma-daro`, `ruma-fame`), izquierda/derecha (`doma-kado`, `doma-kado-no`) y terminal (`duma-kuma`) | verificado, falta confirmar |
| **Curso por niveles** | 4 niveles (0–3), 34 lecciones con glifos, romano, pronunciación, traducción, ejercicios y lecturas; lector con glosa en cada palabra; modo inmersión de la interfaz | **nuevo** |
| **Literatura y música** | 34 textos: poemas, canciones, mitos, cuentos; herramienta de ritmo y acento con melodía automática o propia | 0.5 |
| **Integración** | Paquetes `.deb`, traducciones gettext y Qt, módulo web, locale `qow_BO` | kit listo |
| **Infraestructura** | Sitio web de 19 páginas, validadores, verificación completa, repositorio público | operativo |

## 3. Pendientes

### 3.1 Decisiones (resueltas por delegación) y lo que sigue abierto

**Aceptadas** (por delegación del autor, con la opción recomendada en cada caso; se pueden reabrir con una frase):
1. Los 6 términos de animales y orientación (`ruma-taro`, `ruma-daro`, `ruma-fame`, `doma-kado`, `doma-kado-no`, `duma-kuma`) están **aprobados** desde el lote 2.
2. **Gramática 1.1:** `le`/`lu` como demostrativos (cerca/lejos); imperativo como verbo desnudo; compuestos con guion (≤ 3 elementos) y acento inicial en cada elemento; adaptación de nombres con vocal de eco; interrogativos informativos sin `ka` final; cuantificadores (`kema-fese`, `nara-no`), intensificación (`gore-pa-pa`) y comparativos con `pa`/`po`.
3. **Pronombres:** se mantienen `mene`, `tune`, `rane`; `sare` = hermano/a; `lafe` = calidad/valoración. Siguen **abiertas** solo las pruebas auditivas de `kulo` y `kale`, la puntuación propia y los signos matemáticos propios.
4. **Calendario:** sin nombres propios para días y meses: `loda-kelo` + ordinal (`loda-kelo be-pose` = lunes) y `mune-kelo` + ordinal (`mune-kelo ga-pose` = marzo). Palabras nuevas: `loda-kelo-seta` (calendario).
5. **Verbos de interfaz** (lote 7): arrastrar, soltar, pulsar, desplazar, importar, exportar, confirmar, compartir, renombrar, mostrar, ocultar…
6. **Nombres propios:** hecho (`adaptar_nombre.py`, 52 nombres de países, ciudades de Bolivia, continentes y personas; página «Nombres propios»). **Siguen abiertos**, y necesitan una decisión de método tuya: los **nombres de los elementos químicos** (opción A: nombre numérico `ganu` + número atómico, que solo cabe hasta Z = 20 con la regla de 3 elementos; opción B: nombres adaptados con la norma de nombres propios, p. ej. `Oksegeno`; recomendada la B para los comunes y símbolos para el resto) y los **nombres de los símbolos de código** (leerlos por su sonido en español o crear nombres propios).
7. **Univocidad:** vigilar `fese` (límite/completitud), `lafe`, `saku`, `doma`.

### 3.2 Trabajo técnico pendiente

- **Probar de verdad:** instalar los `.deb` en oweelinux, probar el teclado 1.2 con compuestos y nombres, probar `ts_rellenar.py` con un `.ts` real de Deepin, compilar el `.mo` (falta `msgfmt`).
- **Prueba auditiva** de los 55 pares de sonidos parecidos (sobre todo partículas: `te/de`, `bo/po`, `ga/ka`) y **audio de pronunciación**.
- **Registro Maestro:** el cuerpo principal sigue declarando «hasta Owee Sans 3.0» y no integra los números compuestos ni el léxico ampliado; regenerarlo desde los `.tsv`.
- **PDFs antiguos:** Matemáticas 2.0 aún trae formas imposibles (`ango`, `akso`, `vara`…); los cuadernos usan fuentes 3.1/3.2.
- ✅ **Teclado multiplataforma Keyman** (Windows, macOS, Linux, Android, iOS y navegadores): `05_Teclado_IME/keyman-owee`, paquete `Owee.kmp`, probado en el motor real KeymanWeb (904/904 palabras idénticas a `owee.js`). Pendiente: probarlo en un teléfono Android y en Windows reales; publicarlo en keyman.com (opcional).
- **Publicar el sitio** (GitHub Pages u oweeme.com) y preparar `CONTRIBUTING`.
- **Seguridad (tuya):** rotar las claves del archivo `oweeme/oweeme.md` y moverlas a un gestor de contraseñas.
- **Curso de 30 lecciones** y ampliar la antología de 34 a 100 textos; traducciones de textos de dominio público.

## 4. Áreas que faltan para un idioma de todos los campos

Método de siempre: **componer primero con raíces existentes; crear raíces nuevas solo para lo muy frecuente; verificar cada lote (30–50 términos por dominio) con el flujo PROPUESTA → VERIFICADA → APROBADA**, con guía, ejemplos y ejercicios por dominio.

### Nivel 1 — para conversar y vivir (≈ 350 términos)

| Dominio | Qué falta | Por qué primero |
|---|---|---|
| **Cuerpo y anatomía** | piel, sangre, hueso, oreja, diente, lengua, cuello, rodilla, vientre, cabello… (todo el hueco de Swadesh) | El 35 % que falta de la lista estándar |
| **Naturaleza concreta** | piedra, arena, humo, ceniza, hoja, semilla, raíz, flor ✓, río ✓, mar ✓, clima, estaciones | Describir el entorno |
| **Animales y plantas** | perro, gato, caballo, vaca, insectos; árboles y frutas comunes | Vida diaria y cuentos |
| **Comida y cocina** | pan, carne, fruta, sal ✓, sabores, utensilios, recetas | Necesidad básica |
| **Casa y ropa** | habitaciones, muebles, herramientas, prendas | Vida diaria |
| **Familia ampliada** | abuelo, tío, primo, cónyuge, amigo, vecino | Hablar de personas |
| **Salud y emergencias** | enfermedad, dolor, medicina, hospital, ayuda urgente | Seguridad y viajes |
| **Dinero y compras** | precio, pagar ✓, comprar, vender, banco | Uso práctico |
| **Transporte y viaje** | coche, tren, avión, ruta, mapa, país ✓, ciudad | «Práctico en el mundo» |
| **Calendario y tiempo** | semana, días, meses, hora, estaciones | Citas y planes |
| **Geografía básica** | continentes, países, ciudades, direcciones ✓ | Orientación |

### Nivel 2 — para estudiar y leer (≈ 500 términos)

Biología (célula, ADN, especies, ecosistemas) · Geología y clima · Historia y sociedad · Derecho y política · Economía · Educación (escuela, examen, carrera) · Lingüística (el idioma para hablar del idioma: sustantivo, verbo, frase…) · Artes (pintura, teatro, cine, danza) · **Música** (notas, escalas, instrumentos) · Filosofía, ética y religión · Psicología y sociología · Medios y redes sociales.

### Nivel 3 — profesional y técnico (≈ 600 términos)

Medicina · Ingeniería, construcción y electrónica · Telecomunicaciones · Agricultura · Industria y energía · Deporte y juegos · Seguridad pública y defensa · Derecho especializado · Finanzas.

### Transversal (no son «campos», pero hacen que sea un idioma completo)

- **Registros de habla:** formal/coloquial, cortesía, cartas y documentos.
- **Expresiones hechas, refranes y humor.**
- **Nombres propios y préstamos:** países, ciudades, personas (norma ya propuesta; falta la lista).
- **Números y medidas:** fracciones, grandes cifras, unidades.
- **Corpus y enseñanza:** 100+ textos, 30 lecciones, ejercicios y pruebas.

## 5. Siguiente paso recomendado

1. ~~Lote 1: cuerpo y naturaleza~~ y ~~lote 2: vida diaria~~ **hechos y aprobados**; norma de animales y orientación **hechas**.
2. **Confirmar** los 6 términos en espera y las decisiones restantes de Gramática 1.1.
4. **Lote 3 (≈ 100 términos):** biología, geología y clima, educación, derecho y política, economía, lingüística y metalenguaje, artes y teoría musical.
5. ✅ **Audio de pronunciación** con voz sintética (1 164 audios; botón ▶ en las frases y clic en las palabras). **Pendiente: grabaciones humanas** y más lecturas y ejercicios autocorregibles en el curso.
6. **Regenerar el Registro Maestro** y los PDF antiguos desde los datos actuales.
7. **Prueba auditiva** de pares mínimos antes de congelar más vocabulario.

> Para comprobar el estado en cualquier momento: `python3 verificar_todo.py`.
