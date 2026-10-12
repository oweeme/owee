# Owee en tus proyectos: oweelinux, oweeme.com y mibolivia.online

**Sí es posible**, y la parte de informática ayuda mucho. Este kit trae lo necesario para tres destinos. Todo se genera desde el mismo glosario (`datos/ui_glosario.tsv`) y el mismo léxico del idioma, así que **un cambio se propaga a la web y a Linux a la vez**.

| Destino | Qué obtiene | Estado del kit |
|---|---|---|
| **oweelinux** | Paquetes `.deb` de fuentes, teclado y locale; traducciones gettext y Qt | `.deb` construidos y comprobados |
| **oweeme.com** | Selector Español / Owee / Owee Script, fuentes y parser | probado en navegador |
| **mibolivia.online** | El mismo módulo web (idioma opcional + sección «Aprende Owee») | probado en navegador |

## Contenido de `08_Integracion/`

```
datos/ui_glosario.tsv              66 textos de interfaz: inglés, español y Owee (fuente única)
herramientas/owee_script.py        romano <-> Owee Script en Python (compuestos y nombres propios)
herramientas/generar_traducciones.py   glosario -> qow.po, qow@owee.po, qow.json, qow.js
herramientas/ts_rellenar.py        rellena archivos Qt (.ts) de apps Deepin/DDE con el glosario
web/owee-i18n.js, qow.js, ejemplo.html, owee-script/, nginx-owee.conf
linux/build-debs.sh                construye fonts-owee, fcitx5-owee y owee-locale (dist/*.deb)
linux/qow_BO                       definición del locale Owee para Bolivia
linux/qow.po, qow@owee.po          catálogos gettext (romano y Owee Script)
linux/fcitx5-profile.snippet       teclado Owee activado por defecto
```

## Principios (los mismos para todos los destinos)

1. **Guarda siempre el texto en romano** (el latino). Convierte a Owee Script **solo al mostrarlo**: así funciona aunque falte la fuente, la búsqueda sigue funcionando y la base de datos no cambia.
2. **Código de idioma `qow`** (uso privado, dentro de `qaa`–`qtz` de ISO 639-3). En HTML: `<html lang="qow">`.
3. El script Owee vive en el área de uso privado de Unicode (U+E000–E049, marcas U+E03C–E03D): **no lo guardes como dato principal** ni lo normalices.
4. Un texto Owee **solo se publica si pasó el validador** (`validar_owee.py`) y su vocabulario está aprobado.

## 1. Web: oweeme.com y mibolivia.online

Tu stack (Nginx + MariaDB `utf8mb4` + subida por SFTP) ya soporta todo; **no hay que cambiar la base de datos**.

1. **Copia a `/public`** de cada sitio: la carpeta `web/owee-script/` (fuentes WOFF2/WOFF + `owee.css` + `owee.js`), `web/qow.js` y `web/owee-i18n.js`.
2. **En el `<head>`**: `<link rel="stylesheet" href="/owee-script/owee.css">`.
3. **Al final del `<body>`**, en este orden: `qow.js`, `owee-script/owee.js`, `owee-i18n.js`, y `OweeI18n.init({ default: "es" })`.
4. **Marca los textos**: `<button data-i18n="Save">Guardar</button>` (la clave es el texto en inglés del glosario). Añade tres botones con `data-owee-set="es" | "owee" | "script"`.
5. **Nginx**: pega `web/nginx-owee.conf` dentro del `server { }` (tipos MIME de fuentes, caché de un año y CORS para usar las fuentes desde tus otros dominios).

El módulo recuerda la elección del visitante y cambia `lang` entre `es` y `qow`. Mira `web/ejemplo.html`.

**Con Vue / Quasar** (como Tervat): copia `owee-script/owee.ts` y `owee.css` (ver su README) y usa `toScript()` en un componente:

```vue
<span :class="{ owee: modo === 'script' }">{{ modo === 'script' ? toScript(msg.owee) : msg.owee }}</span>
```

**mibolivia.online:** ofrécelo como **idioma opcional de la interfaz** y añade una sección «Aprende Owee» enlazando a la guía de pronunciación y al diccionario.

> **Contenido nuevo con IA:** si usas un modelo para redactar textos en Owee, **valida siempre** el resultado con `validar_owee.py` y contra `lexico.tsv` antes de publicarlo: los modelos inventan palabras y rompen la regla V/CV.

## 2. oweelinux

### 2.1 Paquetes

```bash
cd 08_Integracion/linux
./build-debs.sh            # crea dist/fonts-owee_3.3-1_all.deb, fcitx5-owee_1.2-1_amd64.deb, owee-locale_0.1-1_all.deb
sudo dpkg -i dist/*.deb && sudo apt -f install
```

- **`fonts-owee`**: Owee Sans y Owee School en `/usr/share/fonts`; las apps las usan automáticamente por *fallback* (cubren U+E000–E049).
- **`fcitx5-owee`**: el teclado. El guion une compuestos (`sade-kelo`) y la inicial mayúscula marca un nombre propio.
- **`owee-locale`**: define el locale `qow_BO` y deja los catálogos en `/usr/share/oweelinux/po/`.

**Para la ISO** (Cubic, live-build o tu sistema de construcción): copia los `.deb` al repositorio de la imagen, instálalos en el chroot y pon `linux/fcitx5-profile.snippet` en `/etc/skel/.config/fcitx5/profile` para que los usuarios nuevos tengan el teclado Owee activado.

### 2.2 Traducciones

- **Apps con gettext** (GTK, herramientas propias): compila el catálogo y úsalo con *fallback* al español:

```bash
msgfmt linux/qow.po -o /usr/share/locale/qow/LC_MESSAGES/<dominio>.mo
LANGUAGE=qow:es  <aplicación>          # lo que falte se ve en español
LANGUAGE=qow@owee:qow:es  <aplicación> # con glifos Owee Script (requiere la fuente)
```

- **Apps de Deepin/DDE (Qt/DTK)** usan archivos `.ts`, no gettext. Con `ts_rellenar.py` partes de la traducción de cada app y obtienes la **lista de lo que falta, ordenada por frecuencia**:

```bash
python3 herramientas/ts_rellenar.py dde-file-manager_en.ts dde-file-manager_qow.ts
lrelease dde-file-manager_qow.ts
```

  Esa lista es tu **hoja de ruta de vocabulario**: las palabras que más se repiten en la interfaz son las primeras que hay que definir en Owee.
- **Locale**: `sudo localedef -i qow_BO -f UTF-8 qow_BO.UTF-8` (lo hace el paquete) y selecciona `qow_BO.UTF-8` en el inicio de sesión o con `LANG=qow_BO.UTF-8`.

### 2.3 Fases sugeridas

| Fase | Entregable |
|---|---|
| 1 | `.deb` en tu repositorio y en la ISO; teclado Owee activo por defecto |
| 2 | Tus propias apps de oweelinux (bienvenida, instalador, configuración) en Owee |
| 3 | Menús y ajustes de Deepin con `ts_rellenar.py`; extender el glosario con lo más frecuente |
| 4 | Fondo de pantalla, GRUB y pantalla de arranque con textos Owee (imágenes, no traducción) |

## 3. Lo que falta decidir

- **Aprobar los 19 términos de interfaz** (por ejemplo `foma-fena` configuración, `loke-kopa` ventana, `tada-sena` botón): están VERIFICADOS, no aprobados. Añádelos a `02_Diccionario/datos/aprobadas.txt`.
- **Licencia** (fuentes y textos) **antes de distribuir** la ISO. Recomendado: SIL Open Font License 1.1 para las fuentes y CC BY-SA 4.0 para el texto.
- **Verbos de la interfaz** (arrastrar, soltar, pulsar, desplazar, deslizar) y **mensajes largos** (confirmaciones, errores): hace falta un lote de vocabulario y un corpus de frases tipo.
- **Código de idioma en repositorios** (por si quieres el locale en listas públicas): `qow` es de uso privado; para estandarizarlo habría que gestionar un código propio.

## 4. Mantener todo al día

```bash
python3 herramientas/generar_traducciones.py     # tras editar datos/ui_glosario.tsv
cd linux && ./build-debs.sh                      # reconstruye los paquetes
```

El glosario valida sus formas contra el léxico y avisa de las que aún no están aprobadas.
