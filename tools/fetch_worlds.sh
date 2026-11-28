#!/bin/bash
# Puts the world .bin files (kept out of git; the CDN holds them) back into worlds/<id>/ so the check tools and
# regen_worlds.sh's diff work on a fresh clone. It fetches the pinned pack(s) with gs-bootstrap's fetch_lock.sh
# and copies maps/<id>/worlds/<id>/<id>.bin into worlds/<id>/.
#   tools/fetch_worlds.sh              # every pinned pack whose bin is missing
#   tools/fetch_worlds.sh <id> [<id>]  # just these
# Dev packs: GS_CDN_URL=https://x-tmc-storez GS_CDN_CA=/opt/tmc-local-ca.crt tools/fetch_worlds.sh
# A bin can also be rebuilt from its source with tools/regen_worlds.sh; stage_packs.sh needs it present either way.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FETCH="${GS_FETCH_LOCK:-$ROOT/../gs-bootstrap/tools/fetch_lock.sh}"
[ -f "$FETCH" ] || { echo "fetch_worlds: gs-bootstrap's fetch_lock.sh not found at $FETCH (set GS_FETCH_LOCK)" >&2; exit 1; }
ids=("$@")
if [ ${#ids[@]} -eq 0 ]; then
    for d in "$ROOT"/worlds/*/; do i=$(basename "$d"); [ -f "$d/$i.bin" ] || ids+=("$i"); done
fi
[ ${#ids[@]} -gt 0 ] || { echo "fetch_worlds: every world bin is present"; exit 0; }
only=$(IFS=,; echo "${ids[*]/#/maps/}")
"$FETCH" "$ROOT/content.lock.json" --root "$ROOT" --only "$only"
miss=0
for i in "${ids[@]}"; do
    src="$ROOT/maps/$i/worlds/$i/$i.bin"
    if [ -f "$src" ]; then cp -n "$src" "$ROOT/worlds/$i/$i.bin"; else echo "fetch_worlds: $i is not in content.lock.json or not fetched" >&2; miss=1; fi
done
exit $miss
