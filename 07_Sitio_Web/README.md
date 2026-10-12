# Sitio web de Owee

Sitio estático (sin servidor, sin dependencias) generado desde los archivos del proyecto.

    python3 07_Sitio_Web/build_site.py   # regenera docs/
    python3 07_Sitio_Web/make_pdf.py     # PDF imprimible de Literatura (necesita Chrome)

Abrir `docs/index.html` en el navegador funciona sin conexión. Para publicarlo, subir la carpeta `docs/`
a cualquier hosting estático (GitHub Pages, Netlify…).

Fuentes de verdad: Registro Maestro (`00_`), `02_Diccionario/datos/lexico.tsv`, texto de Literatura (`03_.../Literatura_Poesia/*.md`)
y el Glyph Master 3.3 (`04_Fuentes/actual_3.3…`). **No editar `docs/` a mano**: se sobrescribe en cada build.
Al añadir un poema: escribirlo en el `.md` dentro de un bloque ```owee, validar con
`python3 -I 03_Material_Ensenanza/Literatura_Poesia/herramientas/validar_owee.py <archivo>.md`, y regenerar.
