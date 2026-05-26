#!/bin/zsh
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "$0")/.." && pwd)"
TARGET_DIR="${HOME}/.codex/skills"

install_skill() {
  local name="$1"
  local src="$ROOT_DIR/skills/$name"
  local dst="$TARGET_DIR/$name"
  mkdir -p "$dst"
  cp -R "$src"/* "$dst"/
}

mkdir -p "$TARGET_DIR"
install_skill "start-my-day"
install_skill "end-of-this-week"
install_skill "llm-learn-devbox"

printf 'Installed skills into %s\n' "$TARGET_DIR"
