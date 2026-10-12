#!/usr/bin/env bash
set -euo pipefail
echo "== Owee IME 1.1 / Deepin user install =="
rm -rf build
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build -j"$(nproc)"
mkdir -p "$HOME/.local/lib/fcitx5" "$HOME/.local/share/fcitx5/addon" "$HOME/.local/share/fcitx5/inputmethod"
cp build/src/owee.so "$HOME/.local/lib/fcitx5/"
cp build/src/owee-addon.conf "$HOME/.local/share/fcitx5/addon/owee.conf"
cp src/owee.conf "$HOME/.local/share/fcitx5/inputmethod/owee.conf"
echo "Owee IME 1.1 instalado para el usuario."
