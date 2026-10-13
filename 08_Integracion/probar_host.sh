#!/usr/bin/env bash
# Comprueba, sin cambiar nada, que Owee esta instalado y funciona en este equipo. Muestra OK / FALLA / AVISO por cada pieza.
AQUI="$(cd "$(dirname "$0")" && pwd)"; RAIZ="$(cd "$AQUI/.." && pwd)"; F=0
ok()   { printf '  OK     %s\n' "$1"; }
mal()  { printf '  FALLA  %s\n         -> %s\n' "$1" "$2"; F=$((F+1)); }
avi()  { printf '  AVISO  %s\n         -> %s\n' "$1" "$2"; }
t() { if eval "$2" >/dev/null 2>&1; then ok "$1"; else mal "$1" "$3"; fi; }

echo "Sistema: $(grep PRETTY_NAME /etc/os-release | cut -d'"' -f2)"
t "Fuente Owee Sans instalada"            'fc-list | grep -qi "Owee Sans"'                 "instala el paquete fonts-owee (instalar_en_host.sh)"
t "Fuente Owee School instalada"          'fc-list | grep -qi "Owee School"'               "instala el paquete fonts-owee"
if fc-list | grep -qi "Owee Numerals"; then
  t "Cifras Owee activas en el sistema"   'fc-match "sans-serif" family | grep -qi "Owee Numerals"' "ejecuta: sudo fc-cache -f ; cierra sesion y entra de nuevo"
else avi "Cifras Owee no instaladas (opcional)" "paquete owee-numerals: las calculadoras seguiran con cifras normales"; fi
t "Teclado Owee instalado (sistema o usuario)" 'dpkg -s fcitx5-owee 2>/dev/null | grep -q "install ok" || [ -f ~/.local/lib/fcitx5/owee.so ]' "ejecuta ./instalar_en_host.sh"
t "El teclado es la version 1.2 (compuestos y nombres)" 'grep -q "1.2-marks" ~/.local/share/fcitx5/owee.version 2>/dev/null || dpkg -s fcitx5-owee 2>/dev/null | grep -q "Version: 1.2"' "ejecuta ./instalar_en_host.sh (reemplaza el teclado antiguo)"
t "Owee esta en tu perfil de Fcitx5"      'grep -q "^Name=owee" ~/.config/fcitx5/profile'  "copia linux/fcitx5-profile.snippet a ~/.config/fcitx5/profile y ejecuta fcitx5 -rd"
t "Fcitx5 en ejecucion"                   'pgrep -x fcitx5'                                "ejecuta fcitx5 -d (o cierra sesion y vuelve a entrar)"
if locale -a | grep -qi "^qow_BO"; then ok "Locale qow_BO disponible"; else avi "Locale qow_BO no instalado (opcional)" "con LANG=es_ES.UTF-8 LANGUAGE=qow:es ya funcionan los catalogos; qow_BO solo hace falta como idioma del sistema (paquete owee-locale)"; fi
t "Catalogos de interfaz en Owee (usuario)" 'ls ~/.local/share/locale/qow/LC_MESSAGES/*.mo'  "ejecuta: python3 08_Integracion/herramientas/gettext_rellenar.py"
t "Los catalogos se leen (gtk30: Open -> bure)" 'python3 -c "
import gettext,os
t=gettext.translation(\"gtk30\",os.path.expanduser(\"~/.local/share/locale\"),languages=[\"qow\"])
assert t.gettext(\"_Open\")==\"bure\""'                                                      "regenera con gettext_rellenar.py"
t "Nombres genericos en el menu (GenericName[qow])" 'grep -l "GenericName\[qow\]" ~/.local/share/applications/*.desktop'  "ejecuta escritorio/generar_desktop.py y copia a ~/.local/share/applications"
if command -v msgfmt >/dev/null; then ok "gettext (msgfmt) instalado"; else avi "gettext no instalado (opcional)" "sudo apt install gettext  (solo para compilar .po con msgfmt; gettext_rellenar.py no lo necesita)"; fi
t "Proyecto verificado (verificar_todo.py)" "cd '$RAIZ' && ! python3 verificar_todo.py | grep '^  FALLA' | grep -v 'Git: sin cambios'" "ejecuta python3 verificar_todo.py y mira que falla"
echo
[ $F = 0 ] && echo "TODO LISTO." || echo "Faltan $F cosas (ver arriba)."
exit $F
