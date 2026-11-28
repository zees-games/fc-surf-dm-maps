#!/usr/bin/env python3
"""The map logic players can set off on every map, and what of it gs-map's runtime does not run; the tool is gs-map-convert's tools/io_coverage.py.

    tools/io_coverage.py                   every map: the gaps ranked by maps affected, and the ratchet (needs the mapsrc store: $GS_MAPSRC_STORE or ~/mapsrc/store)
    tools/io_coverage.py surf_pavilion     these maps
    tools/io_coverage.py -v                each map's broken player chains, hop by hop
    tools/io_coverage.py --write           record the current gaps as the ratchet

Gaps not fixed yet are held per map in tools/io_known.json. gs-map's io/ is read from $GS_MAP_DIR (else the sibling checkout).
gs-map-convert is a sibling checkout (`../gs-map-convert`, where gs-bootstrap clones it) or `$GS_MAP_CONVERT_PATH`.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for _p in (os.environ.get("GS_MAP_CONVERT_PATH", ""), os.path.join(ROOT, "..", "gs-map-convert")):
    if _p and os.path.isfile(os.path.join(_p, "tools", "io_coverage.py")):
        sys.path.insert(0, os.path.join(_p, "tools"))
        break
else:
    sys.exit("io_coverage: gs-map-convert (with tools/io_coverage.py) was not found. Clone it beside this repository or set GS_MAP_CONVERT_PATH.")
import io_coverage  # noqa: E402

sys.exit(io_coverage.main(root=ROOT))
