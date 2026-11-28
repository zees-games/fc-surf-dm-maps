# Surf batch 2 (maps-surf-1)

Community maps converted from the owner's Surf Combat list. Each is credited (author, GameBanana page, removal contact in `licence.json`), has modes ffa/tdm/gungame, free/own textures and models in the delivered pack, and an internal unedited `_orig` replica kept outside git.

Gates run per map: `tools/check_teleports.py` and `tools/check_playable.py` (both pass for every row; `ratchet` = known, reasoned entry in `tools/teleports_known.json`), `tools/check_packs.py` (27 staged packs clean).

| Map | Author | Teleports | Playable | Modes | Look |
|---|---|---|---|---|---|
| `surf_phenomenon` | equaleyez90 | ok | ok | ffa, tdm, gungame | 2026-11-28: ok: brick ramps, water channels, sky fine |
| `surf_machinery` | That Deviant | ok | ok | ffa, tdm, gungame | 2026-11-28: ok: rusty metal and tile roofs, sky fine |
| `surf_concordia` | razEr^surf | ratchet | ok | ffa, tdm, gungame | ok 2026-11-28 (tiled deck, sky, floating discs) |
| `surf_snowycave` | Moskin | ok | ok | ffa, tdm, gungame | ok 2026-11-28 (terrazzo walls, sky) |
| `surf_ag_texture_final` | SmOoth123 | ok | ok | ffa, tdm, gungame | ok 2026-11-28 (brick, signs, rails) |
| `surf_olympics` | THAY-imagine- | ok | ok | ffa, tdm, gungame | 2026-11-28: spawn was blown out white; fixed in the converter (overexposed bakes are capped, hue kept), room now shows its tile texture |
| `surf_2heaven_b1` | arcangel845 | ok | ok | ffa, tdm, gungame | ok 2026-11-28 (brick, stairs, metal floor) |
| `surf_banocanyon` | BANORRACHY | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: textured canyon walls, sand ramps, sky; sparse but correct |
| `surf_crzyfrog_reloaded` | JackTheStripper | ratchet | ok | ffa, tdm, gungame | 2026-11-28 rendered: timber floor, lit, no defects |
| `surf_buzzkill2` | SmirnOFF. | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: cave rock textured, dim by design |
| `surf_skyscraper` | Goerge | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: dark tiled room, textured, dim by design |
| `surf_buck_ed_up` | BuckNasty | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: grass arena, textured |
| `surf_2012_beta12` | Ryan S | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: dim olive interior, textured |
| `surf_dusty_roads` | Rebell | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: brick tunnel with lamps, textured |
| `surf_meister_v3_final2` | VVeltmeister | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: rock island overview fine; spawn view is distant and plain |
| `surf_melons` | kaos4u | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: water surface, textured |
| `surf_amplitude_encore` | BuckNasty | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: space skybox, lava trim, dark by design |
| `surf_funpark_reloaded_v1` | Paper-Cut | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: textured, no defects |
| `surf_prisoner_v2` | EncryptedCell | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: night map, very dark by design |
| `surf_ny__resist` | FAJ | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: night map, dark by design, textures present |
| `surf_buck_fever2` | BuckNasty | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: pale water arena, textured |
| `surf_bedroom` | .Nixon^ | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: giant bedroom, textured, hazy |
| `surf_vindictive` | -[Element]- | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: sunset sky, textured |
| `surf_gforce` | latrosicarius | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: rusty steel at night, textured |
| `surf_flowing` | G-FLOW | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: sandstone with tree, textured |
| `surf_xiv_v3b` | SmOoth123 | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: dark but textured |
| `surf_eternity_v1` | TheApexi | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: no defects seen |
| `surf_construction` | see licence.json | ok | ok | ffa, tdm, gungame | 2026-11-28 rendered: grey steel hall, textured, no defects |

## Not converted

- Conflux: banned by the owner.

## Replaced

- `surf_xiv_v2a` is replaced by `surf_xiv_v3b`. A server config that names `surf_xiv_v2a` must switch to `surf_xiv_v3b`.
