# Teclado Owee para Keyman (Windows, macOS, Linux, Android, iOS y navegadores)

Escribes en **romano** y obtienes **Owee Script** (glifos). Es el mismo comportamiento que el IME de Fcitx5 de Linux, pero sílaba a sílaba:

| Escribes | Resultado |
|---|---|
| `su` + `na` | los glifos de *suna* |
| `sh`, `ch` | una sola consonante (*shome*, *chuko*) |
| `sade-kelo` | el guion tras un glifo pone el **nexo de compuesto** |
| `Ana` | mayúscula inicial = **marca de nombre propio** + glifos |
| `0`–`9` | **cifras Owee**; `AltGr` + cifra escribe la cifra normal |
| consonante sin vocal | queda en romano (no se pierde texto) |

Comprobado en el motor real KeymanWeb 18: 904 de 904 palabras del léxico dan exactamente el mismo resultado que `owee.js` (las dos diferencias eran palabras de prueba no válidas, con `l`, `w`, `i`).

## Instalar

1. **Windows** — instala [Keyman para Windows](https://keyman.com/windows), descarga `dist/Owee.kmp` y ábrelo con doble clic. Instala también la fuente Owee Sans.
2. **Android** (límite: en aplicaciones de terceros los glifos pueden verse como cuadros, porque Android no deja instalar fuentes en todo el sistema; se ven bien en el editor de Keyman y en el navegador) — instala [Keyman para Android](https://keyman.com/android), copia `Owee.kmp` al teléfono y ábrelo desde Keyman (*Instalar teclado desde archivo*). Activa Keyman como teclado del sistema.
3. **iPhone/iPad y macOS** — igual, con Keyman para iOS / macOS.
4. **Navegadores** — la página *Teclado* del sitio incluye una caja de prueba con KeymanWeb; para tu propia web usa `dist/owee.js` con KeymanWeb.
5. **Linux** — usa este teclado con Keyman para Linux o el IME `fcitx5-owee` (`../fcitx5-owee-1.2-marks`).

## Reconstruir

    npm install --prefix ~/.keyman-kmc @keymanapp/kmc     # una sola vez
    ./construir.sh                                        # genera dist/Owee.kmp, owee.kmx y owee.js

`generar_keyman.py` crea `source/owee.kmn` (reglas), `owee.keyman-touch-layout` (teclado táctil) y `owee.kps` (paquete) desde el mismo mapa de glifos del IME de Linux (`owee-pua-map.json`). **No edites los archivos de `source/` a mano.**

Publicarlo en keyman.com (opcional) requiere enviar el paquete a https://github.com/keymanapp/keyboards.

Licencia: código MIT; la fuente Owee Sans, SIL OFL 1.1.
