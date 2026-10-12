#!/usr/bin/env bash
set -euo pipefail

echo "== Owee IME 1.0 / Fcitx5 =="
command -v cmake >/dev/null || { echo "Falta cmake."; exit 1; }
command -v fcitx5 >/dev/null || { echo "Falta fcitx5."; exit 1; }

rm -rf build
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build -j"$(nproc)"
sudo cmake --install build

echo
echo "Instalado. Reiniciando Fcitx5..."
fcitx5 -rd || true
echo
echo "Abre: fcitx5-configtool"
echo "Busca 'Owee', agrégalo y pruébalo en LibreOffice."
