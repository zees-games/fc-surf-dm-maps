#!/bin/bash
# Rebuild worlds/<id> through the shared converter; sources default to the Airdrift inspirations folder.
export SRC="${SRC:-$HOME/godot/inspirations/airdrift}"
exec "${GSBSP_PATH:-$(dirname "$0")/../../gs-map-convert}/tools/regen_worlds.sh" "$(dirname "$0")/.." "$@"
