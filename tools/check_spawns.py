#!/usr/bin/env python3
"""Every spawn of every map is one a round can start at, on the mapper's side; the check is gs-map-convert's tools/check_spawns.py.

    tools/check_spawns.py                  every map (team and disabled checks need the mapsrc store: $GS_MAPSRC_STORE or ~/mapsrc/store)
    tools/check_spawns.py surf_pavilion    these maps
    tools/check_spawns.py -v               list every problem

Failures not fixed yet are held by exact count in tools/spawns_known.json.
gs-map-convert is a sibling checkout (`../gs-map-convert`, where gs-bootstrap clones it) or `$GS_MAP_CONVERT_PATH`.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for _p in (os.environ.get("GS_MAP_CONVERT_PATH", ""), os.path.join(ROOT, "..", "gs-map-convert")):
    if _p and os.path.isfile(os.path.join(_p, "tools", "check_spawns.py")):
        sys.path.insert(0, os.path.join(_p, "tools"))
        break
else:
    sys.exit("check_spawns: gs-map-convert (with tools/check_spawns.py) was not found. Clone it beside this repository or set GS_MAP_CONVERT_PATH.")
import check_spawns  # noqa: E402

sys.exit(check_spawns.main(root=ROOT))
