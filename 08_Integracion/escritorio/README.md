# Owee en el escritorio de oweelinux: programas, ajustes y nombres

**Respuesta corta: sí se puede**, por capas. Todo texto de interfaz de un programa está en un **catálogo de traducción**; si Owee tiene un catálogo para ese programa, el programa muestra Owee (romano o glifos). Lo que cambia es **cuánto trabajo** pide cada programa y **cuánto vocabulario** hace falta.

## Cifras reales de este sistema (Deepin 25)

Medido con `frecuencia_cadenas.py` sobre los catálogos del español ya instalados:

| Dato | Valor |
|---|---|
| Programas y bibliotecas con traducción | **177** |
| Cadenas de interfaz en total | **≈ 82 000** |
| Cadenas cortas distintas (≤ 40 letras: menús, botones, etiquetas) | ≈ 36 000 |
| El glosario de Owee actual (96 textos) cubre | ≈ 1 % de las apariciones |
| Las 400 cadenas más repetidas suman | solo ≈ 7 % |

**Conclusión:** la interfaz es una **cola larga**: unas pocas palabras (Guardar, Abrir, Configuración…) se repiten mucho y el resto es muy variado. Por eso la estrategia es **por capas**, no «traducirlo todo de golpe».

## Cómo se traduce cada familia de programas

| Familia | Mecanismo | Ejemplos | Esfuerzo |
|---|---|---|---|
| **GTK / GNOME y herramientas** | gettext (`.po` → `.mo`) | **GIMP** (≈ 8 500 cadenas), **Inkscape**, Nautilus, `git`, NetworkManager | medio |
| **KDE / Qt** | gettext (KF) y archivos Qt `.ts`/`.qm` | Dolphin, Kate, Ajustes del sistema | medio |
| **Deepin / DDE** | Qt `.ts`/`.qm` | Centro de control, Administrador de archivos, Terminal | medio |
| **LibreOffice** | catálogos propios `.po` | Writer, Calc, Impress | alto |
| **Firefox / Thunderbird** | paquetes de idioma `.xpi` (Fluent/`.properties`) | Firefox | alto (hay que construir el paquete) |
| **VS Code** | extensión de idioma (VSIX) con JSON de textos | VS Code | alto |
| **Programas Electron/Chrome** | paquetes de idioma propios | Chrome | alto |
| **Archivos `.desktop`** (menú de aplicaciones) | claves `Name[qow]`, `GenericName[qow]` | todos | **bajo** |

## Plan por capas

**Capa 0 — Menú y nombres (esfuerzo bajo, resultado inmediato).**
Los nombres de marca (**GIMP, Inkscape, Firefox, VS Code**) **no se traducen**: son nombres propios y se conservan. Lo que sí tiene Owee es el **nombre genérico** («editor de imágenes» = `loke-dore-feke`, «navegador web» = `gora-rela-duma`). `generar_desktop.py` crea copias de los `.desktop` con `GenericName[qow]` (romano) y `GenericName[qow@owee]` (glifos). En este sistema ya genera **15 programas** (VS Code, GIMP, Chrome, LibreOffice, Administrador de archivos, Monitor del sistema…).

**Capa 1 — Textos de interfaz más usados (≈ 500 cadenas).**
Menús estándar (Archivo, Editar, Ver, Ayuda), botones (Aceptar, Cancelar, Guardar) y categorías de ajustes. El glosario de Owee (`../datos/ui_glosario.tsv`, 96 textos) ya los cubre en parte; con `generar_traducciones.py` se obtienen los catálogos `qow.po` y `qow@owee.po`. Con `LANGUAGE=qow:es` lo que falta **se ve en español**, así nada se rompe.

**Capa 2 — Programas completos, uno a uno.**
Elegir un programa (p. ej. los de oweelinux o el Centro de control de Deepin), extraer sus cadenas y traducirlas. `ts_rellenar.py` (Qt) y `frecuencia_cadenas.py` te dicen **qué traducir primero**. Cada programa añade vocabulario nuevo al idioma (con el mismo flujo PROPUESTA → VERIFICADA → APROBADA).

**Capa 3 — Cobertura amplia.**
Con unas 3 000–5 000 palabras de interfaz, la traducción **asistida** (traductor + glosario) cubre la mayor parte de lo que se repite; el resto necesita revisión humana. Es un proyecto de meses, no de días, y crece con la comunidad.

## Equivalencias, no solo traducción

Para programas cuyo nombre es una marca, la **equivalencia** es lo práctico:

| Programa | Genérico en Owee | En glifos |
|---|---|---|
| GIMP | editor de imágenes: `loke-dore-feke` | (se ve en el menú) |
| Inkscape | editor de imágenes: `loke-dore-feke` | |
| Visual Studio Code | editor de código: `foma-beka-feke` | |
| Firefox / Chrome | navegador web: `gora-rela-duma` | |
| LibreOffice Writer / Calc | procesador de texto `beka-feke` / hoja de cálculo `banu-feke` | |
| Administrador de archivos | gestor de archivos: `doke-kopa-feke` | |
| Papelera, Equipo, Teclado, Ratón | `dabo-kopa`, `meka-mado`, `maku-tabe`, `maku-feke` | |

La tabla completa y editable es `apps_escritorio.tsv`; los textos genéricos de ajustes están en `../datos/ui_glosario.tsv`.

## Mostrar glifos en vez de romano

Los catálogos `qow@owee.po` llevan los textos en **Owee Script** (caracteres de uso privado): los programas los muestran con la fuente **Owee Sans** instalada (`fonts-owee`). Los atajos de teclado tipo `&Archivo` se ignoran al buscar la traducción; en glifos conviene definir los atajos aparte.

## Comandos

```bash
# 1) cuánto hay y qué traducir primero (lee tus catálogos del español)
python3 frecuencia_cadenas.py 400          # escribe prioridad_cadenas.tsv

# 2) nombres genéricos en el menú de aplicaciones (no modifica el sistema)
python3 generar_desktop.py                  # escribe salida/applications/*.desktop
cp salida/applications/*.desktop ~/.local/share/applications/    # solo tu usuario

# 3) traducciones de interfaz (gettext y web)
python3 ../herramientas/generar_traducciones.py

# 4) un programa Qt/Deepin
python3 ../herramientas/ts_rellenar.py app_en.ts app_qow.ts
```

## Lo que NO conviene prometer todavía

- Traducir **todo** KDE o Deepin: son decenas de miles de cadenas y el vocabulario aún crece.
- Que **Firefox** o **VS Code** acepten el código de idioma `qow` sin pruebas: hay que construir sus paquetes de idioma y comprobarlo.
- Que los glifos se vean en programas que **recortan** o **normalizan** texto de uso privado: se prueba programa por programa.
