#!/usr/bin/env bash
# Genera el teclado Keyman de Owee y deja el paquete listo en dist/ (Owee.kmp, owee.kmx, owee.js).
# Requiere Node y el compilador de Keyman:  npm install --prefix ~/.keyman-kmc @keymanapp/kmc
# No envia informes de errores a keyman.com (--no-error-reporting).
set -euo pipefail
cd "$(dirname "$0")"
KMC="${KMC:-$HOME/.keyman-kmc/node_modules/.bin/kmc}"
python3 generar_keyman.py
mkdir -p build dist
"$KMC" build --no-error-reporting source/owee.kmn -o build/owee.kmx
"$KMC" build --no-error-reporting source/owee.kps -o build/Owee.kmp
cp build/owee.kmx build/owee.js build/Owee.kmp dist/
ls -la dist
