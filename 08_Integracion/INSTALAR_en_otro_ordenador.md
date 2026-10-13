# Usar el proyecto en otro ordenador (oweelinux)

## Camino rápido (Deepin 25, Debian, Ubuntu)

```bash
git clone https://github.com/oweeme/owee.git && cd owee/08_Integracion
./instalar_en_host.sh            # modo usuario: sin sudo, solo toca ~/.local y ~/.config (guarda copia de lo que reemplaza)
./probar_host.sh                 # comprueba cada pieza: OK / FALLA / AVISO, con la solución de cada fallo
```

Opciones: `--con-cifras` (las cifras de todas tus apps salen en Owee; se quita borrando `~/.config/fontconfig/conf.d/60-owee-numerals.conf`) y `--sistema` (paquetes `.deb` para todo el equipo, pide sudo). Para ver un programa instalado en Owee: `LANG=es_ES.UTF-8 LANGUAGE=qow:es <programa>` (glifos: `LANGUAGE=qow@owee:qow:es`); lo que Owee aún no traduce se ve en español. Hoy hay catálogos para unos 130 programas, con unos 2 100 textos de más de 82 000: crece al ampliar `datos/ui_glosario.tsv` y volver a ejecutar `herramientas/gettext_rellenar.py`.

Los pasos de abajo son lo mismo, uno por uno.

Pasos para traer todo desde GitHub a otra máquina Debian/Deepin/Ubuntu y dejar Owee funcionando.

## 1. Descargar

```bash
sudo apt install git
git clone https://github.com/oweeme/owee.git
cd owee
```

## 2. Dependencias (solo para compilar el teclado y generar los paquetes)

```bash
sudo apt install cmake g++ pkg-config dpkg-dev libfcitx5core-dev fcitx5 python3
# opcional (PDF del sitio): google-chrome o chromium; (reconstruir fuentes): pip install -r requirements.txt
```

## 3. Construir e instalar los paquetes

```bash
cd 08_Integracion/linux
./build-debs.sh                      # crea dist/fonts-owee, fcitx5-owee, owee-numerals y owee-locale (.deb)
sudo dpkg -i dist/*.deb && sudo apt -f install
```

- **Fuentes** (`fonts-owee`): Owee Sans y Owee School, disponibles en todo el sistema.
- **Cifras Owee** (`owee-numerals`, opcional): fuente que solo tiene las cifras 0-9 en Owee Script; con su regla de fontconfig, la calculadora, el reloj y el calendario muestran los números en Owee sin tocar los programas. Para volver a cifras normales: `sudo apt remove owee-numerals`. Se regenera con `04_Fuentes/actual_3.3_fuente_y_glifos/numeros/hacer_fuente_numeros.py` (requiere fontTools).
- **Teclado** (`fcitx5-owee`): añade «Owee» en Fcitx5; el guion une compuestos y la mayúscula marca nombres propios.
- **Locale** (`owee-locale`): define `qow_BO` y deja los catálogos en `/usr/share/oweelinux/po/`.

## 4. Teclado Owee activado por defecto

```bash
mkdir -p ~/.config/fcitx5 && cp fcitx5-profile.snippet ~/.config/fcitx5/profile
fcitx5 -rd
```

Para los usuarios nuevos del sistema que estás construyendo: copia ese archivo a `/etc/skel/.config/fcitx5/profile`.

## 5. Nombres genéricos en el menú de aplicaciones

```bash
cd ../escritorio
python3 generar_desktop.py                          # solo crea copias en ./salida/applications
cp salida/applications/*.desktop ~/.local/share/applications/    # solo para tu usuario
```

## 6. Traducciones de interfaz

```bash
cd ../
python3 herramientas/generar_traducciones.py        # regenera qow.po y qow@owee.po
# con gettext instalado:   msgfmt linux/qow.po -o /usr/share/locale/qow/LC_MESSAGES/<dominio>.mo
LANGUAGE=qow@owee:qow:es  <programa>                # glifos Owee; lo que falte se ve en español
```

## 7. Comprobar que todo está bien

```bash
cd ~/owee && python3 verificar_todo.py     # textos, léxico, sitio web, traductor, inglés, git
python3 07_Sitio_Web/build_site.py         # genera la web local en 07_Sitio_Web/docs (abre index.html)
```

## Actualizar más adelante

```bash
cd ~/owee && git pull
cd 08_Integracion/linux && ./build-debs.sh && sudo dpkg -i dist/*.deb
```

**Si el teclado no compila** por la versión de Fcitx5 de la otra máquina, instala `libfcitx5core-dev` de esa versión; las fuentes y el locale no dependen de ello.


## Teclado Keyman (Android, Windows, iOS, macOS y navegadores)

Paquete listo en `05_Teclado_IME/keyman-owee/dist/Owee.kmp` (también descargable en la página *Teclado* del sitio). Instálalo con Keyman (ver `05_Teclado_IME/keyman-owee/README.md`). En oweelinux sigue usándose `fcitx5-owee`; Keyman es para teléfonos y otros sistemas.
