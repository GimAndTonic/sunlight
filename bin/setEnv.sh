#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
export SUNLIGHT_HOME=$(cd "$SCRIPT_DIR/.." && pwd)
echo "SUNLIGHT_HOME is set to $SUNLIGHT_HOME"
