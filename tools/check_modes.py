#!/usr/bin/env python3
"""Every map hosts free-for-all, team deathmatch and gun game and the README modes table is current; the check is gs-map-convert's tools/check_modes.py.

    tools/check_modes.py           check every map and the README table
    tools/check_modes.py --write   rewrite the README modes table

Failures not fixed yet are held in tools/modes_known.json.
gs-map-convert is a sibling checkout (`../gs-map-convert`, where gs-bootstrap clones it) or `$GS_MAP_CONVERT_PATH`.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for _p in (os.environ.get("GS_MAP_CONVERT_PATH", ""), os.path.join(ROOT, "..", "gs-map-convert")):
    if _p and os.path.isfile(os.path.join(_p, "tools", "check_modes.py")):
        sys.path.insert(0, os.path.join(_p, "tools"))
        break
else:
    sys.exit("check_modes: gs-map-convert (with tools/check_modes.py) was not found. Clone it beside this repository or set GS_MAP_CONVERT_PATH.")
import check_modes  # noqa: E402

sys.exit(check_modes.main(root=ROOT))
