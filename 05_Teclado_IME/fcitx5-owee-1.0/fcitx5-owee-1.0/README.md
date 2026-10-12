# Owee IME 1.0 para Fcitx5

Motor nativo de entrada para Owee Script 1.0.

## Comportamiento

- Escribes `suna`; durante la composición ves `suna`.
- Espacio confirma: `SU + NA` se insertan como caracteres PUA y luego un espacio.
- Enter confirma la palabra y deja que Enter llegue a la aplicación.
- Backspace edita la preedición.
- Escape cancela la palabra.
- Una palabra no válida se conserva en romano para no perder texto.
- Ctrl/Alt/Super y otros atajos pasan a la aplicación.
- `sh` y `ch` se reconocen antes que consonantes simples.
- `i` no existe en Owee.

El mapa es el mismo de Owee Sans 1.0:
U+E000..U+E03B.

## Dependencias en Deepin/Debian

Primero comprueba:

    fcitx5 --version
    fcitx5-configtool

Para compilar hacen falta CMake, compilador C++ y los archivos de desarrollo
de Fcitx5 Core. En Debian/Deepin el nombre habitual del paquete de desarrollo
es `libfcitx5core-dev`; si APT no lo encuentra, usa:

    apt search fcitx5 | grep -E 'dev|core'

## Compilar

    ./install-deepin.sh

O manualmente:

    cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
    cmake --build build -j"$(nproc)"
    sudo cmake --install build
    fcitx5 -rd

Después abre:

    fcitx5-configtool

Busca `Owee` y añádelo al grupo activo.

## Prueba

Con Owee Sans instalada y Owee IME activo, abre LibreOffice y escribe:

    me daro dare

Pulsa espacio después de cada palabra. El documento recibirá caracteres PUA,
no las letras romanas.

## Diagnóstico

Si Owee no aparece:

    fcitx5-diagnose | less

Comprueba además:

    ls /usr/share/fcitx5/addon/owee.conf
    ls /usr/share/fcitx5/inputmethod/owee.conf
    find /usr/lib -path '*fcitx5*' -name 'owee.so' 2>/dev/null

## Test del parser sin Fcitx

    g++ -std=c++17 tests/parser_test.cpp src/oweeparser.cpp -o /tmp/owee-parser-test
    /tmp/owee-parser-test
