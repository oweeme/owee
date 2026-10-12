#!/usr/bin/env bash
# Construye los paquetes .deb de Owee para oweelinux (Debian/Deepin/Ubuntu). No instala nada: solo crea dist/*.deb
#   fonts-owee      fuentes Owee Sans y Owee School 3.3 (TTF + OTF)
#   fcitx5-owee     teclado Owee para Fcitx5 1.2 (compuestos con "-" y nombres propios)
#   owee-locale     locale qow_BO (definicion) y catalogos de traduccion qow.po / qow@owee.po
# Uso: ./build-debs.sh        Requiere: dpkg-deb, cmake, g++, libfcitx5core-dev
set -euo pipefail
AQUI="$(cd "$(dirname "$0")" && pwd)"; RAIZ="$(cd "$AQUI/../.." && pwd)"
GM="$RAIZ/04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3"
IME="$RAIZ/05_Teclado_IME/fcitx5-owee-1.2-marks"
DIST="$AQUI/dist"; TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
MANT="${OWEE_MAINTAINER:-Proyecto Owee <hector@oweeme.com>}"
mkdir -p "$DIST"

paquete() {  # nombre version arch descripcion dependencias
  local d="$TMP/$1"; mkdir -p "$d/DEBIAN"
  cat > "$d/DEBIAN/control" <<CTL
Package: $1
Version: $2
Section: ${6:-misc}
Priority: optional
Architecture: $3
Maintainer: $MANT
Depends: ${5:-}
Description: $4
CTL
  sed -i '/^Depends: $/d' "$d/DEBIAN/control"
}
copyright() {  # directorio paquete
  mkdir -p "$1/usr/share/doc/$2"
  cat > "$1/usr/share/doc/$2/copyright" <<'CR'
Copyright (c) 2026 Hector Martinez (https://oweeme.com)
Fuentes: SIL Open Font License 1.1 (ver OFL.txt en el repositorio).
Codigo (teclado Fcitx5, scripts): MIT. Texto y datos: CC BY-SA 4.0.
Textos completos en https://github.com/oweeme/owee/tree/main/LICENSES
CR
}

# ---- fonts-owee
paquete fonts-owee 3.3-1 all "Fuentes Owee Sans y Owee School (escritura Owee Script)" "" fonts
d="$TMP/fonts-owee"
mkdir -p "$d/usr/share/fonts/truetype/owee" "$d/usr/share/fonts/opentype/owee"
cp "$GM"/fonts/ttf/*.ttf "$d/usr/share/fonts/truetype/owee/"
cp "$GM"/fonts/otf/*.otf "$d/usr/share/fonts/opentype/owee/"
copyright "$d" fonts-owee
printf '#!/bin/sh\nset -e\n[ "$1" = configure ] && command -v fc-cache >/dev/null && fc-cache -f /usr/share/fonts/truetype/owee /usr/share/fonts/opentype/owee || true\nexit 0\n' > "$d/DEBIAN/postinst"; chmod 755 "$d/DEBIAN/postinst"
dpkg-deb --root-owner-group --build "$d" "$DIST/fonts-owee_3.3-1_all.deb" >/dev/null

# ---- fcitx5-owee (compila el addon)
cmake -S "$IME" -B "$TMP/ime" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr >/dev/null
cmake --build "$TMP/ime" -j"$(nproc)" >/dev/null
paquete fcitx5-owee 1.2-1 "$(dpkg --print-architecture)" "Teclado Owee para Fcitx5: romano a Owee Script, compuestos y nombres propios" "fcitx5" inputmethods
d="$TMP/fcitx5-owee"
DESTDIR="$d" cmake --install "$TMP/ime" >/dev/null
copyright "$d" fcitx5-owee
dpkg-deb --root-owner-group --build "$d" "$DIST/fcitx5-owee_1.2-1_$(dpkg --print-architecture).deb" >/dev/null

# ---- owee-locale
paquete owee-locale 0.1-1 all "Locale qow_BO y catalogos de traduccion de oweelinux al Owee" "fonts-owee" localization
d="$TMP/owee-locale"
mkdir -p "$d/usr/share/i18n/locales" "$d/usr/share/oweelinux/po"
cp "$AQUI/qow_BO" "$d/usr/share/i18n/locales/qow_BO"
cp "$AQUI/qow.po" "$AQUI/qow@owee.po" "$d/usr/share/oweelinux/po/"
copyright "$d" owee-locale
printf '#!/bin/sh\nset -e\n[ "$1" = configure ] && command -v localedef >/dev/null && localedef -i qow_BO -f UTF-8 qow_BO.UTF-8 || true\nexit 0\n' > "$d/DEBIAN/postinst"; chmod 755 "$d/DEBIAN/postinst"
dpkg-deb --root-owner-group --build "$d" "$DIST/owee-locale_0.1-1_all.deb" >/dev/null

ls -la "$DIST"
