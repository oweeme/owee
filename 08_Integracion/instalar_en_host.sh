#!/usr/bin/env bash
# Instala Owee en ESTE equipo (probado para Deepin 25; sirve en Debian/Ubuntu). Dos modos:
#   ./instalar_en_host.sh              modo USUARIO (por defecto, sin sudo): solo toca ~/.local y ~/.config. Guarda copia de lo que reemplaza.
#   ./instalar_en_host.sh --sistema    paquetes .deb para todo el sistema (pide sudo)
#   Opciones: --con-cifras (cifras Owee en todas las apps del usuario)   --sin-cifras (por defecto: no tocar las cifras)
# Instala: fuentes, teclado Fcitx5 (con compuestos y nombres), catalogos de interfaz en Owee para los programas instalados,
# nombres genericos del menu y, si lo pides, las cifras Owee. Despues: ./probar_host.sh
set -euo pipefail
AQUI="$(cd "$(dirname "$0")" && pwd)"; RAIZ="$(cd "$AQUI/.." && pwd)"
MODO=usuario; CIFRAS=0
for a in "$@"; do case "$a" in --sistema) MODO=sistema;; --con-cifras) CIFRAS=1;; --sin-cifras) CIFRAS=0;; esac; done
say() { printf '\n== %s\n' "$*"; }
GM="$RAIZ/04_Fuentes/actual_3.3_fuente_y_glifos/Owee_Glyph_Master_3.3"

say "1. Dependencias"
FALTAN=""
for p in cmake g++ pkg-config libfcitx5core-dev fcitx5 python3; do dpkg -s "$p" >/dev/null 2>&1 || FALTAN="$FALTAN $p"; done
if [ -n "$FALTAN" ]; then echo "Faltan:$FALTAN  ->  sudo apt install$FALTAN"; [ "$MODO" = sistema ] && sudo apt install -y $FALTAN || exit 1; else echo "ok"; fi
command -v msgfmt >/dev/null || echo "(opcional) sudo apt install gettext   # para compilar .po con msgfmt"

if [ "$MODO" = sistema ]; then
  say "2. Paquetes .deb para todo el sistema"
  ( cd "$AQUI/linux" && ./build-debs.sh )
  PAQ=("$AQUI"/linux/dist/fonts-owee_*.deb "$AQUI"/linux/dist/fcitx5-owee_*.deb "$AQUI"/linux/dist/owee-locale_*.deb)
  [ "$CIFRAS" = 1 ] && PAQ+=("$AQUI"/linux/dist/owee-numerals_*.deb)
  sudo apt install -y "${PAQ[@]}"
else
  say "2. Fuentes Owee Sans y Owee School 3.3 (usuario)"
  mkdir -p ~/.local/share/fonts/Owee
  cp "$GM"/fonts/ttf/*.ttf ~/.local/share/fonts/Owee/ && fc-cache -f ~/.local/share/fonts/Owee

  say "3. Teclado Owee 1.2 (compuestos con guion y nombres propios) para tu usuario"
  B="$(mktemp -d)"; trap 'rm -rf "$B"' EXIT
  cmake -S "$RAIZ/05_Teclado_IME/fcitx5-owee-1.2-marks" -B "$B" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr >/dev/null
  cmake --build "$B" -j"$(nproc)" >/dev/null
  mkdir -p ~/.local/lib/fcitx5 ~/.local/share/fcitx5/addon ~/.local/share/fcitx5/inputmethod
  [ -f ~/.local/lib/fcitx5/owee.so ] && cp --update=none ~/.local/lib/fcitx5/owee.so ~/.local/lib/fcitx5/owee.so.antes
  cp "$B/src/owee.so" ~/.local/lib/fcitx5/owee.so
  cp "$B/src/owee-addon.conf" ~/.local/share/fcitx5/addon/owee.conf
  cp "$RAIZ/05_Teclado_IME/fcitx5-owee-1.2-marks/src/owee.conf" ~/.local/share/fcitx5/inputmethod/owee.conf
  echo "1.2-marks" > ~/.local/share/fcitx5/owee.version
  echo "teclado instalado (copia anterior: owee.so.antes)"

  if [ "$CIFRAS" = 1 ]; then
    say "3b. Cifras Owee en todas tus aplicaciones (para quitarlas: borra ~/.config/fontconfig/conf.d/60-owee-numerals.conf)"
    cp "$AQUI/linux/fontconfig/OweeNumerals-Regular.ttf" ~/.local/share/fonts/Owee/
    mkdir -p ~/.config/fontconfig/conf.d && cp "$AQUI/linux/fontconfig/60-owee-numerals.conf" ~/.config/fontconfig/conf.d/
    fc-cache -f
  fi
fi

say "4. Perfil de Fcitx5"
mkdir -p ~/.config/fcitx5
if grep -q '^Name=owee' ~/.config/fcitx5/profile 2>/dev/null; then echo "Owee ya esta en tu perfil"; else
  [ -f ~/.config/fcitx5/profile ] && cp ~/.config/fcitx5/profile ~/.config/fcitx5/profile.antes-de-owee
  cp "$AQUI/linux/fcitx5-profile.snippet" ~/.config/fcitx5/profile; echo "perfil instalado (copia anterior: profile.antes-de-owee)"; fi

say "5. Catalogos de interfaz en Owee para los programas instalados (solo tu usuario)"
python3 "$AQUI/herramientas/generar_traducciones.py" | tail -1
python3 "$AQUI/herramientas/gettext_rellenar.py"

say "6. Nombres genericos del menu de aplicaciones (solo tu usuario)"
( cd "$AQUI/escritorio" && python3 generar_desktop.py | tail -2 && mkdir -p ~/.local/share/applications && cp salida/applications/*.desktop ~/.local/share/applications/ 2>/dev/null || true )

say "Listo. Reinicia Fcitx5 (fcitx5 -rd) o cierra sesion y vuelve a entrar; despues:  $AQUI/probar_host.sh"
echo "Ver un programa en Owee:  LANG=es_ES.UTF-8 LANGUAGE=qow:es <programa>      (glifos: LANGUAGE=qow@owee:qow:es)"
