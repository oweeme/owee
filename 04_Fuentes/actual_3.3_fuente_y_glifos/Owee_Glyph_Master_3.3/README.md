# Owee Glyph Master 3.3

Paquete canónico de Owee Script para todos los dispositivos. Todo se genera
desde una sola fuente de verdad: los esqueletos vectoriales de la tabla
"Sistema silábico" del Curso Práctico para Adultos (`../OweeSans3_3_Source`).

| Estilo | Familia | Uso |
|---|---|---|
| sans   | **Owee Sans**   | pantalla, documentos, web: compacta y gruesa |
| school | **Owee School** | escritura a mano, cuadernos: alta, inclinada, fina |

Las familias no llevan número de versión: al actualizar, los documentos y
páginas siguen funcionando.

## Contenido
```
fonts/ttf    Linux, Windows, Android (apps que aceptan fuentes)
fonts/otf    macOS, iPhone/iPad, programas de diseño
fonts/woff2  web (todos los navegadores actuales)
fonts/woff   web (navegadores antiguos)
svg/sans, svg/school   70 SVG por estilo, nombrados CODEPOINT_ID (fill=currentColor)
owee-glyph-map.json    roman, ID estable, code point, lectura de los dígitos
web/                   kit web: owee.css, owee.js, Owee Pad (index.html, PWA)
mobile/ios/Owee-Fonts.mobileconfig   instala las dos fuentes en iPhone/iPad
build_glyph_master.py  regenera todo
```

Codificación (igual que el IME Fcitx5): U+E000..U+E03B sílabas (A E O U, PA..CHU),
U+E03C..U+E03F reservados, U+E040..U+E049 dígitos 0-9.

## Escritorio (Linux / Deepin)
    cp fonts/ttf/*.ttf ~/.local/share/fonts/Owee/ && fc-cache -f
El teclado Owee (Fcitx5) ya escribe estos caracteres.

## Web: qué copiar a un proyecto
Copia la carpeta **`package/`** (fuentes WOFF2/WOFF + `owee.css` + `owee.ts` +
`owee.js`). En proyectos Vite / Vue / Quasar / Tauri usa `owee.css` + `owee.ts`;
en HTML sin compilar, `owee.css` + `owee.js`. Instrucciones en `package/README.md`.
Ejemplo integrado: tervat, rama `feat/owee-script` → `frontend/src/lib/owee-script/`
y `css: ['app.scss', '~src/lib/owee-script/owee.css']` en `quasar.config.ts`.

Uso en HTML:

    <link rel="stylesheet" href="owee.css">
    <script src="owee.js"></script>
    <p class="owee" id="t"></p>
    <script>t.textContent = Owee.toScript("me suna nume 2026", {digits: true});</script>
`owee.js` sigue las mismas reglas que el IME: sh/ch primero, sólo V/CV, sin i,
las palabras imposibles quedan en roman. `Owee.toRoman()` hace la conversión inversa.
Clases: `.owee` / `.owee-sans` y `.owee-school`.

Owee Pad (`web/index.html`) funciona abriendo la carpeta `web/` desde cualquier
hosting estático con https (GitHub Pages, Netlify…); en el móvil se puede
"Añadir a pantalla de inicio" y funciona sin conexión.

## Móvil
- **Android:** no permite instalar fuentes en todo el sistema sin root. Usa
  Owee Pad en el navegador (o instalado como app) para escribir y copiar.
  Las apps que aceptan fuentes propias (editores, lectores) pueden usar `fonts/ttf`.
- **iPhone / iPad:** abre `mobile/ios/Owee-Fonts.mobileconfig` en el dispositivo
  (AirDrop, correo o descarga) → Ajustes → Perfil descargado → Instalar.
  El perfil no está firmado, así que iOS lo muestra como "No verificado".
  Las fuentes quedan disponibles en Pages, Keynote, Notas con formato, etc.

En ambos móviles, el texto Owee copiado sólo se ve como Owee donde la fuente
está disponible; en otras apps aparece como cuadros. El roman es la forma
segura para compartir (regla 17 de la especificación).

## Regenerar
    python3 build_glyph_master.py
