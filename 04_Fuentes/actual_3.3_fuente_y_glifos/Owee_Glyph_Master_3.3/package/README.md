# @oweeme/owee-script 3.3

Copia esta carpeta al proyecto. Nada más es necesario.

| Archivo | Para qué |
|---|---|
| `owee.css` | carga Owee Sans y Owee School; clases `.owee`, `.owee-sans`, `.owee-school` |
| `fonts/*.woff2`, `fonts/*.woff` | las fuentes (owee.css las referencia con rutas relativas) |
| `owee.ts` | parser para proyectos Vite / Vue / Quasar / Tauri (TypeScript) |
| `owee.js` | el mismo parser para HTML sin compilar (`window.Owee`) |
| `owee-glyph-map.json` | roman, ID estable y code point de las 70 unidades |

## Vite / Vue / Quasar / Tauri
```ts
import 'src/lib/owee-script/owee.css'          // una vez (boot, main.ts o quasar.config css)
import { toScript, toRoman } from 'src/lib/owee-script/owee'
toScript('me suna nume 2026', { digits: true })
```
```html
<span class="owee">{{ toScript(texto) }}</span>
<span class="owee-school">{{ toScript(texto) }}</span>
```

## HTML
```html
<link rel="stylesheet" href="owee-script/owee.css">
<script src="owee-script/owee.js"></script>
<p class="owee" id="t"></p>
<script>t.textContent = Owee.toScript('me suna nume 2026', { digits: true })</script>
```

Guarda siempre el texto en roman (base de datos, URLs, búsqueda) y convierte
a Owee sólo al mostrarlo: así funciona aunque la fuente no esté disponible.
