# Owee — plan de ampliación: de idioma fácil a idioma usable en el mundo

**Fecha:** 2026-10-12. Esta hoja responde a: *¿qué más se puede agregar para que Owee sea rico y práctico?* Parte de lo que ya funciona (fonología simple, gramática analítica, escritura propia, fuentes, teclado, sitio web, ciencias, poesía) y propone qué sigue, **en orden de utilidad**.

> **Lo que ya es una ventaja real.** Solo 4 vocales y sílabas V/CV: casi cualquier persona puede pronunciarlo bien. Sin conjugación, género ni artículos: se aprende rápido. Vocabulario conceptual y composicional: pocas raíces rinden mucho. Escritura propia con 60 bloques: se memoriza en una semana. **No pierdas esto**: cada ampliación debe conservarlo.

## 1. El cuello de botella: tamaño y consistencia del vocabulario

**Dónde estás.** El léxico general tiene ~180 raíces; las ciencias aportan 89 raíces técnicas; hay ~190 compuestos propuestos. Eso ya permite poemas y frases sencillas, pero una conversación cotidiana pide unas **800–1 000 raíces** y la lectura de textos generales unas **2 000**.

**Un límite matemático que conviene conocer.** Con las reglas actuales hay 56 sílabas CV + 4 vocales = 60 sílabas, o sea **3 136 palabras de 2 sílabas** posibles. Con 1 500 raíces de 2 sílabas se ocuparía casi la mitad y habría centenares de pares casi iguales. **Recomendación:** raíces de **2 sílabas** para los ~800 conceptos básicos; **3 sílabas** para términos técnicos raros (ahí hay 175 000 combinaciones); y **componer** siempre que sea posible, como se ha hecho en Química, Astronomía y la Gramática 1.1.

**Metas de vocabulario** (orientativas, tipo MCER):

| Nivel | Raíces + compuestos fijos | Qué permite |
|---|---|---|
| A1 | ~300 | presentarse, necesidades, frases cortas |
| A2 | ~700 | conversación cotidiana simple, relatos breves |
| B1 | ~1 500 | opinar, contar, leer textos sencillos |
| B2 | ~3 000 | prensa, ciencia divulgativa, literatura |

## 2. Dominios que faltan o están en borrador

| Dominio | Estado | Qué hace falta |
|---|---|---|
| Matemáticas, Física | Hecho (2.0) | Negativos, paréntesis, ordinales (Gramática 1.1) |
| Química | Borrador 0.1 | Nombres de elementos, nomenclatura |
| Astronomía y astrología | **Borrador 0.1 (nuevo)** | Fases lunares, calendario, nombres de estrellas |
| Mitología y cuentos | **Primeros textos (nuevo)** | Más mitos, panteón completo, cuentos largos |
| Cuerpo, salud y medicina | Parcial | Enfermedades, síntomas, medicinas, emergencias |
| Biología, geología, ecología | Falta | Células, especies, rocas, clima |
| Comida, cocina, ropa, casa | Parcial | Ingredientes, utensilios, medidas culinarias |
| Geografía y viajes | Falta | Países, continentes, transporte, direcciones |
| Calendario | Falta | Días de la semana, meses, estaciones, horas |
| Tecnología e internet | Falta (importante) | Computadora, red, archivo, programa, mensaje, contraseña |
| Economía, dinero, trabajo | Parcial | Banco, precio, impuesto, contrato |
| Política, derecho, sociedad | Parcial | Ley, justicia, derechos, voto |
| Educación | Parcial | Escuela, examen, carrera |
| Arte, música, deporte, juegos | Falta | Notas, ritmo, equipo, partido |
| Religión y filosofía | Mínimo | Conceptos abstractos (bien, mal, alma, destino) |
| Emociones y carácter | Bueno | Matices (nostalgia, vergüenza, orgullo) |
| Frases hechas, humor, modismos | Falta | Refranes propios, expresiones |

## 3. Gramática y lengua escrita que aún pide decisiones

Resumidas en la **Gramática 1.1**: «sí», imperativo, vocativo, demostrativos, cuantificadores, compuestos y su acento, relativas, saludos, nombres propios. Además:

- **Puntuación propia** y vocales largas en el script.
- **Registro formal vs. coloquial** (¿cortesía? hoy no existe).
- **Evidencialidad** y voz pasiva (opcionales).
- **Escritura rápida / cursiva** (Owee School ya existe; falta una norma de enlaces entre bloques).

## 4. Herramientas que lo vuelven práctico

Ordenadas por **valor / esfuerzo**:

1. **Tarjetas de estudio** (Anki/CSV) generadas del léxico: una orden y listas. *Esfuerzo: bajo.*
2. **Validador y corrector en el navegador**: pegar un texto Owee y marcar palabras inexistentes, fonología inválida y colisiones. Ya existe como script; llevarlo a la web. *Bajo.*
3. **Audio de pronunciación**: Owee cabe dentro de la fonología del español, así que un sintetizador libre (como eSpeak-NG) puede leer cada palabra; sirve para lecciones, para canciones y para la **prueba auditiva de pares mínimos** pendiente. *Medio.*
4. **Teclado para todas las plataformas**: hoy solo hay Fcitx5 (Linux). **Keyman** cubre Windows, macOS, Linux, Android, iOS y web con un solo archivo; es la mejor palanca de adopción. *Medio.*
5. **Código de idioma:** usar un código de **uso privado** (por ejemplo `qow`, dentro del rango `qaa`–`qtz` de ISO 639-3) y `lang="qow"` en HTML, para que los programas reconozcan el idioma.
6. **Traductor asistido** español↔Owee por conceptos (búsqueda ya existe en el diccionario) con sugerencia de composiciones.
7. **Aplicación de práctica** (diaria, con repetición espaciada) y modo oral.
8. **Estandarización del script**: del PUA a un registro (ConScript Unicode Registry) y, a largo plazo, una propuesta Unicode, que exige comunidad, textos y fuentes con licencia libre.

## 5. Contenido para aprender y leer

- **Curso gradual** de 30 lecciones (hay material de familias, niños, intermedios y adultos; falta una secuencia única).
- **Antología literaria**: poemas, canciones, mitos y cuentos (ya hay primeros textos; meta: 100+).
- **Traducciones de textos de dominio público**: Declaración Universal de Derechos Humanos (art. 1), fábulas de Esopo, cuentos tradicionales, refranes. Un banco de textos conocidos es el mejor material de enseñanza.
- **Frases de viaje y emergencia** (para que sea «práctico en el mundo»).
- **Cuaderno de canciones** con partitura sencilla y audio.

## 6. Comunidad y legitimidad

Un idioma es útil cuando alguien más lo usa. En orden:

1. **Licencias claras** (fuentes: SIL OFL; texto y diccionario: CC BY-SA). Sin licencia nadie puede reutilizarlo.
2. **Repositorio público** con el proyecto (git) y un manual de contribución.
3. **Reglas de gobernanza simples**: quién decide, cómo se proponen palabras, qué es «estable». (El Registro ya tiene el germen: estable / provisional / rechazada.)
4. **Primeros 10 hablantes** (aunque sean amistades): sin uso real no hay prueba de colisiones ni de ritmo.

## 7. Cautelas honestas

- **No hay atajo para la comunidad.** La facilidad no basta: hacen falta textos, hablantes y constancia.
- **Pares casi iguales** (55 ya detectados) pesan más en lo hablado; hazles la prueba auditiva antes de congelar más vocabulario.
- **Nombres propios**: sin una norma de adaptación (Gramática 1.1 §14), casi no se puede contar historias reales.
- **Astrología y mitología** conviene tratarlas como *cultura*, no como ciencia, y dejar claro el marco.
- **Calidad > cantidad**: 500 raíces bien probadas valen más que 3 000 sin probar.

## 8. Hoja de ruta propuesta

| Fase | Entregable | Tiempo orientativo |
|---|---|---|
| 1 | Aprobar Gramática 1.1, números en el Registro, compuestos y acento; licencia + git | 1–2 semanas |
| 2 | Ampliar a ~500 raíces: cuerpo, casa, comida, calendario, geografía básica, tecnología | 3–4 semanas |
| 3 | Prueba auditiva (pares mínimos) + audio de las 500 raíces | 1–2 semanas |
| 4 | Keyman + tarjetas Anki + corrector web | 2–3 semanas |
| 5 | Curso de 30 lecciones y antología (100 textos) | 2–3 meses |
| 6 | Traducciones de dominio público; publicación y primeros hablantes | continuo |
