#!/bin/bash
# Render a .drawio file to PNG for visual self-checking.
# Usage: render.sh <file.drawio> [out.png]
# Requires draw.io desktop (macOS: brew install --cask drawio).
set -euo pipefail

IN="${1:?usage: render.sh <file.drawio> [out.png]}"
OUT="${2:-${IN%.drawio}.png}"

BIN=""
for candidate in drawio "/Applications/draw.io.app/Contents/MacOS/draw.io"; do
    if command -v "$candidate" >/dev/null 2>&1 || [ -x "$candidate" ]; then
        BIN="$candidate"
        break
    fi
done

if [ -z "$BIN" ]; then
    echo "draw.io CLI not found — skip the visual check, or install once with:" >&2
    echo "  brew install --cask drawio" >&2
    exit 2
fi

"$BIN" -x -f png --scale 2 -b 10 -o "$OUT" "$IN" >/dev/null 2>&1
echo "$OUT"
