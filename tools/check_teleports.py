#!/usr/bin/env python3
"""Every trigger_teleport of every map, resolved in its source .bsp, lands where the converted map sends it; the check is gs-map-convert's tools/check_teleports.py.

    tools/check_teleports.py                          every map (needs the mapsrc store: $GS_MAPSRC_STORE or ~/mapsrc/store)
    tools/check_teleports.py surf_forbidden_ways_2nd  these maps
    tools/check_teleports.py -v                       list every problem, ambiguous overlaps too

Failures not fixed yet are held by exact count in tools/teleports_known.json.
gs-map-convert is a sibling checkout (`../gs-map-convert`, where gs-bootstrap clones it) or `$GS_MAP_CONVERT_PATH`.
It is not in CI: the runner has no source .bsp files.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for _p in (os.environ.get("GS_MAP_CONVERT_PATH", ""), os.path.join(ROOT, "..", "gs-map-convert")):
    if _p and os.path.isfile(os.path.join(_p, "tools", "check_teleports.py")):
        sys.path.insert(0, os.path.join(_p, "tools"))
        break
else:
    sys.exit("check_teleports: gs-map-convert (with tools/check_teleports.py) was not found. Clone it beside this repository or set GS_MAP_CONVERT_PATH.")
import check_teleports  # noqa: E402

sys.exit(check_teleports.main(root=ROOT))
