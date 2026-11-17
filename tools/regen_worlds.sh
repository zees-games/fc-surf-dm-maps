#!/bin/bash
# Rebuild worlds/<id> through the shared converter; sources default to the Airdrift inspirations folder.
export SRC="${SRC:-$HOME/godot/inspirations/airdrift}"
exec "${DOTBSP_PATH:-$(dirname "$0")/../../dot-map-convert}/tools/regen_worlds.sh" "$(dirname "$0")/.." "$@"
