# Owee

<p align="center"><img src="06_Logo/owee-logo-256.png" alt="Logo de Owee: un koi con la palabra ouee en Owee Script" width="160"></p>

**Owee** es un idioma construido: fácil de pronunciar, regular, sin conjugaciones ni género, con una escritura propia (**Owee Script**) y herramientas para usarlo hoy en computadoras, la web y Linux.

- **Fonología:** 4 vocales (`a e o u`), 14 consonantes, sílabas solo `V` o `CV` (60 sílabas), acento siempre en la primera sílaba. No existe la `i`.
- **Gramática:** analítica, orden SOV, sin género, número ni conjugación; contexto antes que redundancia.
- **Vocabulario:** conceptual y composicional (pocas raíces, muchos compuestos); principio de **una forma = un significado**.
- **Escritura:** en línea, de izquierda a derecha: 1 sílaba = consonante + vocal a su derecha, con marcas para compuestos y nombres propios.
- **Herramientas:** fuentes (Owee Sans y Owee School), teclado Fcitx5, validador, sitio web, paquetes `.deb` y traducciones para oweelinux.

## Estructura

| Carpeta | Contenido |
|---|---|
| `00_Registro_Maestro/` | Registro maestro del idioma, auditoría y planes |
| `01_Especificacion/` | Especificaciones normativas (PDF) |
| `02_Diccionario/` | Diccionario y léxico en `datos/*.tsv` (fuente única para los programas) |
| `03_Material_Ensenanza/` | Gramática 1.1, pronunciación, matemáticas, física, química, astronomía, informática, literatura y cuadernos |
| `04_Fuentes/` | Fuentes y glifos (Owee Glyph Master 3.3) y versiones anteriores |
| `05_Teclado_IME/` | Teclado Fcitx5 para Linux (1.2: compuestos y nombres propios) |
| `06_Logo/` | Logo de Owee (koi + «ouee» en Owee Script): SVG, PNG y el script que lo construye |
| `07_Sitio_Web/` | Generador del sitio web estático |
| `08_Integracion/` | Integración con oweelinux y sitios web: `.deb`, traducciones, módulo i18n |

## Empezar

```bash
# sitio web (genera 07_Sitio_Web/docs/)
python3 07_Sitio_Web/build_site.py

# validar un texto Owee contra la fonología y el léxico
python3 03_Material_Ensenanza/Literatura_Poesia/herramientas/validar_owee.py ARCHIVO.md

# boceto musical de una canción (ritmo, acento y armonía)
python3 03_Material_Ensenanza/Literatura_Poesia/herramientas/ritmo_cancion.py 03_Material_Ensenanza/Literatura_Poesia/Owee_Literatura_y_Poesia_0.5.md -s "Mune kuma" --estilo hadas -o audio

# regenerar el léxico científico y verificar términos nuevos
python3 02_Diccionario/datos/generar_ciencias.py

# reconstruir fuentes (necesita las dependencias de requirements.txt)
python3 04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3/build_glyph_master.py

# paquetes .deb para oweelinux
08_Integracion/linux/build-debs.sh
```

Dependencias de Python (fuentes, auditoría de glifos y audio) en un entorno local:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python verificar_todo.py
```

**PDFs:** cada documento tiene su fuente `.md` (especificaciones, cuadernos, curso, matemáticas, física…) y el diccionario se genera desde el léxico. Se imprimen con Chrome/Chromium:

```bash
python3 07_Sitio_Web/build_site.py && python3 07_Sitio_Web/make_pdf.py && python3 07_Sitio_Web/build_site.py
```

Los PDF anteriores (versión 1.0, glifos con la vocal alrededor) se conservan en las carpetas `versiones_anteriores/`.

## Usar Owee

- **Traductor Owee ⇄ español / inglés** (prototipo, en el navegador): `07_Sitio_Web` → página «Traductor».
- **oweelinux y otros ordenadores:** paquetes `.deb`, teclado, traducciones y menú en [`08_Integracion/INSTALAR_en_otro_ordenador.md`](08_Integracion/INSTALAR_en_otro_ordenador.md).

## Estado y verificación

El estado actual, los pendientes y las áreas por cubrir están en [`00_Registro_Maestro/Owee_Estado_y_Pendientes.md`](00_Registro_Maestro/Owee_Estado_y_Pendientes.md). Para verificar todo el proyecto (textos, léxico, sitio web, enlaces, herramientas y git):

```bash
python3 verificar_todo.py
```

## Cómo contribuir

**Cualquier persona puede crear y proponer palabras** en la página «Crear palabras» del sitio: comprueba las reglas en el navegador, sugiere raíces libres y abre la propuesta en GitHub. Guía en la lección 3.8 del curso.

Cada palabra nueva pasa por un flujo: **PROPUESTA → VERIFICADA → APROBADA** (ver `00_Registro_Maestro`, secciones 73–78). Una forma nueva debe cumplir V/CV sin `i`, usar partes que existan, tener como máximo 3 elementos y un significado único. Añade tus propuestas a `02_Diccionario/datos/ciencias_fuente.py` y ejecuta `generar_ciencias.py`; la aprobación final la da el autor en `aprobadas.txt`.

## Licencias

| Material | Licencia |
|---|---|
| Idioma, documentación, diccionario, datos, textos, literatura | **CC BY-SA 4.0** |
| Fuentes y glifos | **SIL Open Font License 1.1** |
| Código (Python, JavaScript, C++, scripts) | **MIT** |

Detalles en [`LICENSE`](LICENSE) y la carpeta [`LICENSES/`](LICENSES/).

Autor: Hector Martinez · [oweeme.com](https://oweeme.com)
