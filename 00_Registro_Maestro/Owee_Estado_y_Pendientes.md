# Owee — estado actual y pendientes

**Fecha:** 2026-10-25 (tras los lotes 19 a 22). Resultado de `python3 verificar_todo.py`, que se ejecuta con un solo comando y termina con código de error si algo falla.

## 1. Verificación: todo en orden

| Comprobación | Resultado |
|---|---|
| Textos Owee (22 archivos: curso, guías, cuadernos, especificaciones, literatura): fonología V/CV sin `i` y vocabulario existente | ✅ válidos |
| Léxico: **1 832 formas** (233 base + 1 599 por áreas), todas aprobadas o auditadas; 0 verificadas pendientes; 0 por revisar | ✅ |
| Colisiones exactas, vecinos acústicos, sinónimos, partes inexistentes | ✅ ninguno |
| Revisión semántica (forma única, sin sinónimos, raíces adecuadas) | ✅ 1 241 OK · 25 ajustados · 0 en espera |
| Inglés (pivote) para todas las formas | ✅ 1 832 formas |
| Cobertura Swadesh-100 | ✅ 91 % con forma · 9 % componible · **0 faltan** |
| Lista básica de 114 conceptos | ✅ 69 % con raíz · 30 % componible · **0 faltan** |
| Cobertura por áreas (43 áreas, 1 489 conceptos de uso diario, estudio y profesión) | ✅ 94 %; lo que figura como «falta» lo cubre casi siempre una raíz-concepto (`beka` escribir, `sado` sano) |
| Sitio web: 43 páginas, enlaces y anclas; sitio público sin la sección Proyecto | ✅ |
| Traductor, calculadora, teclado Keyman, «Crear palabras»: pruebas automáticas | ✅ |
| Audio de pronunciación (voz sintética): 2 118 audios | ✅ |
| Glifos 3.4: ningún glifo es giro o espejo de otro; todo el léxico tiene glifo | ✅ |
| Paquetes `.deb` instalados y probados en este equipo (Deepin 25: fuentes, teclado 1.2, cifras, locale, catálogos) | ✅ `probar_host.sh` |

## 2. Qué hay hecho

| Área | Estado |
|---|---|
| **Fonología y escritura** | cerrada; Owee Script 3.4 en línea, marcas ‿ y ᚠ, dígitos propios; puntuación internacional |
| **Gramática 1.1** | **confirmada** (sí, imperativo, cortesía, demostrativos, cuantificadores, comparación, relativas, nombres propios, puntuación) |
| **Norma de practicidad** (lote 20) | lo de cada día con raíz corta; derivados de 2 elementos; ya no quedan raíces de 2 sílabas: las nuevas son de 3 |
| **Vocabulario** | vida diaria, personas, saludos y fiestas, ropa, hogar, cocina, animales, insectos, tecnología, internet y correo, viajes, jardinería, cartas, literatura, fantasía, trabajo, salud, educación, sociedad, biología, clima, historia, derecho, economía, artes, música, filosofía, medios, medicina, ingeniería, energía, deporte, seguridad, signos, matemáticas, física, química, astronomía, informática, interfaz |
| **Nombres propios** | 76: países, ciudades, continentes, personas y 24 elementos químicos (con su símbolo) |
| **Curso** | 4 niveles, 39 lecciones con glifos, pronunciación, traducción, ejercicios y lecturas |
| **Certificación** | ruta infantil (Semilla, Brote, Árbol) y de adultos (Niveles 0–4); exámenes modelo con clave; requisitos para maestros y examinadores; registro público y certificado imprimible |
| **Literatura** | 50 textos: poemas, canciones, mitos, cuentos |
| **Documentos PDF** | 15, generados desde las fuentes actuales (especificaciones, diccionario, curso, cuadernos, caligrafía, matemáticas, física, química, pronunciación, literatura) |
| **Herramientas** | fuentes TTF/OTF/WOFF2, teclados Fcitx5 y Keyman, Owee Pad, traductor, calculadora, «Crear palabras», validadores, audio |
| **Integración** | paquetes `.deb`, traducciones gettext y Qt, módulo web, locale `qow_BO` |

## 3. Lo que queda (necesita personas o equipos reales)

Nada de lo siguiente bloquea el uso del idioma; son pruebas y crecimiento que no se pueden automatizar.

1. **Prueba auditiva con personas:** los pares de sonidos parecidos (sobre todo `kulo`/`kale` y partículas como `te`/`de`, `bo`/`po`) y la claridad de las raíces nuevas de 3 sílabas.
2. **Grabaciones de voz humana** (`03_Material_Ensenanza/Pronunciacion/herramientas/grabar_voz.py`): sustituyen a la voz sintética al regenerar el sitio.
3. **Probar los teclados en otros equipos:** Keyman en Android y Windows reales; Fcitx5 en otro equipo oweelinux.
4. **Seguridad (tuya):** rotar las claves del archivo `oweeme/oweeme.md` y guardarlas en un gestor de contraseñas.
5. **Primeros certificados:** el examinador fundador certifica a los primeros maestros; cada certificado se añade a `03_Material_Ensenanza/Certificacion/certificados.tsv`.
6. **Crecer con el uso:** más textos de literatura (meta: 100), traducciones de obras de dominio público y las palabras que propongan los usuarios.
7. **Opcional:** `sudo apt install gettext` (para compilar `.po` con `msgfmt`); publicar el teclado en keyman.com.

## 4. Cómo seguir creciendo

- **Palabras nuevas:** página «Crear palabras» → correo a hector@oweeme.com («Idioma Owee: nueva palabra») o GitHub → revisión → `ciencias_fuente.py` → `generar_ciencias.py` → `verificar_todo.py`. Guía en `CONTRIBUTING.md`.
- **Fase 2 (cuando haya comunidad):** base de datos de propuestas con cuentas y votos (MySQL + API en Python/FastAPI en el VPS); el léxico aprobado se sigue exportando al repositorio como fuente pública.

> Para comprobar el estado en cualquier momento: `python3 verificar_todo.py`.
