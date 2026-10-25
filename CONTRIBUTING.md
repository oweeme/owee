# Cómo contribuir a Owee

Owee crece con quienes lo usan. Puedes proponer palabras nuevas, corregir textos o escribir literatura en Owee, sepas o no de programación.

## Proponer una palabra (sin saber de programación)

1. Abre la página **«Crear palabras»** del sitio (menú *Aprender*).
2. **Busca la idea** por su significado: quizá ya existe, o se puede formar uniendo dos raíces (`nelo-kopa` = planta + contenedor = maceta).
3. Escribe tu palabra y su significado. La página comprueba al instante las reglas del idioma:
   - solo sílabas V o CV con las vocales `a e o u` (no existe la `i`) y las consonantes `p b t d k g f s m n l r sh ch`;
   - que no exista ya, ni suene casi igual que otra raíz (a una sola letra);
   - que su significado no tenga ya una palabra (una forma = un significado);
   - que sea práctica: 2 elementos para lo de cada día, como máximo 3; las raíces nuevas, de 3 sílabas;
   - que no copie una palabra de otra lengua (solo los nombres propios se adaptan por el sonido).
4. Pulsa **«Guardar en mis palabras»** para usarla ya en tus textos.
5. Envíala por **correo a hector@oweeme.com** con el asunto **«Idioma Owee: nueva palabra»** (el botón «Enviar por correo» lo prepara): la palabra, su significado y **cómo la usarías**, con el contexto y una o dos frases de ejemplo. Puedes enviar varias juntas con «Enviar todas por correo». Si tienes cuenta de GitHub, también puedes usar **«Proponer en GitHub»**.

La lección 3.8 del curso explica el método con ejemplos.

## Qué pasa con tu propuesta

Cada palabra pasa por **PROPUESTA → VERIFICADA → APROBADA**:

- **Verificada:** cumple las reglas automáticas (las mismas de la página).
- **Aprobada:** el autor del idioma revisa que el significado sea claro y no choque con otra palabra; entonces entra en el diccionario oficial, en el sitio, en el audio y en los PDF.

## Para quien usa GitHub

- **Propuestas de palabras:** abre un *issue* con la etiqueta `propuesta` (la página «Crear palabras» lo prepara por ti).
- **Cambios en el léxico:** se editan en `02_Diccionario/datos/ciencias_fuente.py` y se regeneran los datos:

  ```bash
  cd 02_Diccionario/datos
  python3 generar_ciencias.py        # léxico + verificación automática
  python3 verificar_propuestas.py    # vecinos acústicos y sinónimos
  python3 generar_ingles.py          # glosas en inglés
  ```

- **Textos en Owee:** escríbelos en bloques ```` ```owee ```` dentro de un `.md` y valídalos con
  `python3 03_Material_Ensenanza/Literatura_Poesia/herramientas/validar_owee.py ARCHIVO.md`.
- **Antes de enviar un cambio:** `python3 verificar_todo.py` debe terminar en «TODO CORRECTO».

## Licencias

Al contribuir aceptas que tu aporte se publique con las licencias del proyecto: idioma, diccionario y textos en **CC BY-SA 4.0**; fuentes en **SIL OFL 1.1**; código en **MIT**.
