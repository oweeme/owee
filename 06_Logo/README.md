# Logo de Owee

El koi (dibujo del autor, `owee-koi-original.png`) con la palabra **ouee** escrita en Owee Script encima de la cabeza, en el crema del cuerpo del pez.

| Archivo | Uso |
|---|---|
| `owee-logo.svg` | logo completo (vectorial; el texto son trazados, no necesita fuente) |
| `owee-logo-solo-koi.svg` | solo el koi, sin texto |
| `owee-logo-{1024,512,256,128,64,32}.png` | tamaños para web, iconos y documentos |

Dónde se usa: cabecera y portada del sitio web (y su favicon), Owee Pad (icono y manifiesto), el teclado Fcitx5 (`fcitx-owee`, icono del método de entrada en la bandeja) y el README.

Reconstruir (por ejemplo si cambian los glifos de la fuente): `python3 construir_logo.py`. La posición y el tamaño del texto están en `CX, CY, ANCHO` al principio del script.
