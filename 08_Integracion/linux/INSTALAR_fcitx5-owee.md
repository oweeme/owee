# Instalar el teclado Owee (fcitx5-owee) en Linux

Paquetes ya construidos en `08_Integracion/linux/paquetes/` (también en la página Descargas del sitio):

| Paquete | Qué es |
|---|---|
| `fcitx5-owee_1.2-3_amd64.deb` | el teclado: escribes romano (`suna`), espacio confirma y se inserta Owee Script; compuestos con `-` y nombres propios |
| `fonts-owee_3.4-1_all.deb` | fuentes Owee Sans y Owee School 3.4 (hace falta para ver los glifos) |

## Instalación (Debian, Ubuntu, Deepin)

    sudo apt install ./fonts-owee_3.4-1_all.deb ./fcitx5-owee_1.2-3_amd64.deb
    fcitx5 -rd            # reinicia Fcitx5
    fcitx5-configtool     # Entrada de texto → añade «Owee» al grupo activo

Prueba en cualquier editor: `me daro dare` + espacio tras cada palabra.

Requisitos: `fcitx5` y `libfcitx5core7` (el paquete los pide solo). Construido con Fcitx5 5.1.7 (Ubuntu 24.04); funciona con Fcitx5 5.x de Deepin 25 y Debian 12/13. Si APT rechaza la dependencia en tu versión, recompila: `bash build-debs.sh` (necesita `cmake g++ libfcitx5core-dev`).

## Quitar

    sudo apt remove fcitx5-owee fonts-owee

## Reconstruir

    cd 08_Integracion/linux && bash build-debs.sh      # deja los .deb en paquetes/
