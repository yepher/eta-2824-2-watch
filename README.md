# ETA 2824-2 — a Cade reference reconstruction

see also [Printables](https://www.printables.com/model/1833588-eta-2824-2-watch-movement)

An ETA 2824-2 movement and a simplified watch around it, reconstructed in
[Cade](#the-cade-toolchain) from published references and explicitly labeled
engineering estimates.

This is an **educational reference model, not a manufacturing drawing package.**
Parts named `*_envelope` are provisional volumes, not real geometry. Read
[ASSUMPTIONS.md](ASSUMPTIONS.md) and [GAPS.md](GAPS.md) before trusting any
dimension, and [NOTICE.md](NOTICE.md) for trademark and third-party terms.

## Layout

| Path | What it is |
|---|---|
| `watch.cade` | Top-level entry point; the `watch` part is the full assembly |
| `eta_2824_design/` | Subsystem sources — main plate, going train, escapement, balance, barrel and winding, automatic winding, dial side, hand setting, case, fasteners |
| `output/` | Exported geometry — `watch_assembly.step`, the same assembly as Parasolid `watch_assembly.x_t`, per-part STEP in `step/`, and the 3MF you regenerate |
| `tools/` | `build_step_assembly.py`, which assembles the per-part STEP using the placements in the Cade sources |
| `references/README.md` | Index of the third-party sources used, with links to their publishers |
| `chatgpt_session_one.md` | The unedited working transcript of the first build session |
| `CLAUDE.md` | Working instructions for the CAD agent |
| `MODEL_STATUS.md` | What is modeled, at what fidelity, right now |
| `ASSUMPTIONS.md` | Every estimate, and what it is based on |
| `GAPS.md` | Known holes in the model and in the toolchain |
| `COMMANDS.md` | The commands actually used to view, check, and export |

## Exports

`output/` holds geometry exported from `watch.cade`, plus the notes on how it
was produced. The STEP files are committed; the 3MF is not — it is tens of MB.

```sh
cade build watch.cade -o output/watch.3mf --part watch --cell 0.095mm
```

That is the coarsest cell size at which every one of the 71 parts meshes as a
closed manifold, which is what 3MF requires. `output/README.md` records the
cell sizes that fail and which part fails at each.

`output/watch_assembly.step` is the single file to open: 60 of the 94
placements as exact solids, in the subsystem hierarchy, with the Cade colors.
`cade export` writes each part in its own local frame, so
[`tools/build_step_assembly.py`](tools/build_step_assembly.py) reads the
placements out of the `.cade` sources and assembles them.

```sh
pip install cadquery-ocp
python3 tools/build_step_assembly.py -o output/watch_assembly.step
```

The 34 placements it is missing are parts `cade export` refuses on their own
geometry — the toothed wheels, threaded fasteners, main plate, case middle,
hairspring, and two hands. The 3MF has all 94, meshed rather than exact.
[`output/README.md`](output/README.md) has the full accounting.

## Viewing it live

```sh
cade view watch.cade --raymarch -p 7879 --part watch --watch
```

`--watch` rebuilds the view as the source changes. `COMMANDS.md` has the
subsystem previews and the clearance diagnostics.

## The Cade toolchain

Cade is a separate project and is not vendored here. The commands above assume
a `cade` binary on your `PATH`; the docs in this repository refer to it as
living under `~/src/cade_research/cade/`. Adjust the paths to wherever you keep
it.

## References

No third-party reference material is redistributed in this repository.
[`references/README.md`](references/README.md) identifies every source used and
links to its publisher so you can download it yourself.

## Use

No license is granted. All rights are reserved by the author; the contents of
this repository are published to be read, not to be reused. See
[NOTICE.md](NOTICE.md) for the separate question of third-party material, which
is not included here at all.
