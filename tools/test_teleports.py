#!/usr/bin/env python3
"""surf_forbidden_ways_* and surf_10x_*: a player stood in each teleport lands at the source's destination.

For every trigger_teleport that moves players, the player's feet are put at the centre of each of
its brushes; the converted map's first RESPAWN pit there (the one Fatal Contact acts on) must send
him to the destination Source resolves, after the same to_godot transform, or to one the teleport
chains on to. A teleport that starts disabled and only a button or trigger enables must be no pit.
Skipped without the mapsrc store ($GS_MAPSRC_STORE or ~/mapsrc/store).

    python3 -P tools/test_teleports.py
"""
import json
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for _p in (os.environ.get("GS_MAP_CONVERT_PATH", ""), str(ROOT.parent / "gs-map-convert")):
    if _p and (Path(_p) / "tools" / "check_teleports.py").is_file():
        sys.path.insert(0, str(Path(_p) / "tools"))
        break
import check_teleports as ct  # noqa: E402

STORE = Path(os.environ.get("GS_MAPSRC_STORE", str(Path.home() / "mapsrc" / "store")))
MAPS = ("surf_forbidden_ways_reloaded", "surf_forbidden_ways_2nd", "surf_10x_final", "surf_10x_reloaded_fixed")
SWITCHED = {"surf_forbidden_ways_reloaded": {"tele_TO_END", "tele_shortend", "tele_jail_top", "tele_jail_secret_1"},
            "surf_forbidden_ways_2nd": {"portal_secret_2", "portal_ubersecret"}}


def load(mid):
    src = ct.source_of(mid, STORE, None)
    if src is None:
        raise unittest.SkipTest("no mapsrc store source for " + mid)
    bsp = ct.Bsp(str(src))
    bsp.load()
    base = ROOT / "maps" / mid / mid
    m = ct.cp.Map(mid, json.loads(base.with_suffix(".json").read_text()), base.with_suffix(".bin").read_bytes())
    ts = ct.triggers(bsp, ct.bi.Zoner(bsp))
    ct._reach(ts)
    return m, ts


class Teleports(unittest.TestCase):
    def test_every_live_teleport_lands_at_its_source_destination(self):
        for mid in MAPS:
            m, ts = load(mid)
            landed = 0
            for t in ts:
                if t["gated"] or not t["sends"]:
                    continue
                for lo, hi in t["boxes"]:
                    c = [(lo[a] + hi[a]) / 2 for a in range(3)]
                    pit = ct.first_pit(m.zones, list(ct.bi.to_godot(c)))
                    if pit is None:
                        continue
                    here = [o for o in ts if o["sends"] and not o["gated"] and any(ct._inside(c, a, b) for a, b in o["boxes"])]
                    with self.subTest(map=mid, teleport=t["name"]):
                        self.assertTrue(any(ct._close(pit["destination"], s) for o in here for s in o["reach"]),
                                        "lands at %s, source sends to %s" % (pit["destination"], t["sends"]))
                    landed += 1
                    break
            self.assertGreater(landed, 10, mid)

    def test_switched_on_teleports_are_no_pit(self):
        for mid, names in SWITCHED.items():
            m, ts = load(mid)
            for t in ts:
                if t["e"].get("targetname") not in names:
                    continue
                self.assertTrue(t["gated"], t["name"])
                for lo, hi in t["boxes"]:
                    c = [(lo[a] + hi[a]) / 2 for a in range(3)]
                    pit = ct.first_pit(m.zones, list(ct.bi.to_godot(c)))
                    with self.subTest(map=mid, teleport=t["name"]):
                        self.assertFalse(pit is not None and any(ct._close(pit["destination"], s) for s in t["sends"]),
                                         "a button-enabled teleport fires from the start")

    def test_check_teleports_is_clean(self):
        for mid in MAPS:
            m, ts = load(mid)
            src = ct.source_of(mid, STORE, None)
            bsp = ct.Bsp(str(src))
            bsp.load()
            fails = [p for p in ct.check_map(bsp, m) if p[0] in ct.FAILS]
            self.assertEqual(fails, [], mid)


if __name__ == "__main__":
    unittest.main()
