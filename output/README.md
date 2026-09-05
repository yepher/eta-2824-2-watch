# Exported geometry

Files here are generated from `watch.cade`. They are **not committed** — a
manifold mesh of a 71-part movement is large (see below). Regenerate them
locally, or attach them to a GitHub Release if you want them downloadable.

## 3MF — meshed assembly

```sh
cade build watch.cade -o output/watch.3mf --part watch --cell 0.095mm
```

71 part definitions placed 94 times. ~810 MB as cade writes it (3MF is a ZIP
container and cade stores its entries uncompressed); recompressing the same
archive with deflate brings it to ~85 MB without changing a triangle:

```python
import zipfile
zin = zipfile.ZipFile("output/watch.3mf")
zout = zipfile.ZipFile("output/watch-small.3mf", "w", zipfile.ZIP_DEFLATED)
for i in zin.infolist():
    zout.writestr(i.filename, zin.read(i.filename))
zout.close()
```

### Why 0.095 mm

3MF requires every part to be a closed manifold mesh, and the marching lattice
pinches thin features when the grid lands badly on them. Cell size is therefore
not free — it has to be searched. Measured on this model:

| Cell | Result |
|---|---|
| 0.13 – 0.30 mm | fails — `eta_pos_9_escape_wheel_envelope` (and at 0.16 mm the third wheel) pinches; the escapement teeth are thinner than the grid |
| 0.10 mm | fails — `eta_pos_23_hairspring_envelope` pinches |
| **0.095 mm** | **passes — coarsest clean setting found** |
| 0.09 mm | passes, larger file |
| 0.08 mm | fails — `eta_pos_12_second_wheel_envelope` |
| 0.06 mm | fails — `eta_pos_29_reduction_wheel_envelope` |
| 0.05 mm | fails — `eta_pos_26_driving_wheel_envelope` |
| 0.048 / 0.049 mm | fails — `eta_pos_23_timed_balance_envelope` |
| 0.047 mm | fails — `eta_pos_23_hairspring_envelope` |
| 0.046 mm | passes, ~3.7 GB stored |

A part that meshes cleanly on its own can still pinch inside the assembly: the
assembly places it with a transform, which changes the grid it lands on. Sweep
against `--part watch`, not against the part alone.

`--chord-error` does not reduce the triangle count on this model; the lattice
is what sets it.

## STEP — exact solids

### The whole assembly does not export

```sh
cade export watch.cade -o output/watch.step --part watch
```

refuses, at the default divisions and at higher `-n` alike:

```
an assembly is written whole or not at all: a file holding 46 of 71 parts
is a wrong assembly that opens without complaint
```

STEP export needs a confirmed loop set for every face of every part. Parts
declared in imported modules report `n of m face(s) have no confirmed loop set
— it is defined in an imported module; run 'cade loops' on the file that
declares it`, and raising `-n` does not resolve them. See
[`../GAPS.md`](../GAPS.md).

### Per-part STEP does work, for most parts

Exported one solid at a time, from the file that declares it, **48 of the 78
solids in this model write valid STEP.** `output/step/` holds them:

```sh
cade export eta_2824_design/going_train.cade \\
  -o output/step/eta_pos_13_train_bridge_envelope.step \\
  --part eta_pos_13_train_bridge_envelope
```

Three of those 48 only appear at a raised division count — `cade export` picks
its own `n`, and the default is not always enough:

| Part | Needs |
|---|---|
| `hour_hand_envelope` | `-n 192` |
| `eta_pos_38_date_driving_wheel_envelope` | `-n 192` |
| `eta_pos_21_pallet_fork_envelope` | `-n 256` |

Raising `n` further does not recover any more: a sweep to `n=320` produced
nothing new. The remaining 30 refuse on their own geometry rather than on
resolution — reported as unresolved face pairs (`Edges::unresolved`) — and it is
the toothed wheels, the threaded fasteners, the main plate, the case middle,
the hairspring, and two of the three hands that hit it.

### The assembled STEP

`cade export` writes every part in its own local frame, so the directory of
per-part files has no positions in it. The positions are in the Cade sources:
each subsystem assembly is a flat `together(...)` of

```
part_name()
  |> place(frame = frame(origin = point(x =, y =, z =), axis =, angle =),
           color = rgb(r =, g =, b =))
```

[`tools/build_step_assembly.py`](../tools/build_step_assembly.py) reads those
placements directly out of the `.cade` files, loads each part's STEP, and writes
one AP214 assembly:

```sh
pip install cadquery-ocp
python3 tools/build_step_assembly.py -o output/watch_assembly.step
```

`output/watch_assembly.step` — **60 of the 94 placements, 48 distinct parts,
6.2 MB.** It opens as a single file with the subsystem hierarchy
(`main_plate`, `going_train`, `escapement`, …), the part names, and the colors
from the Cade sources. Overall extent 42.30 x 36.00 x 9.20 mm.

The 34 placements it is missing are the parts in the refusal list above; the
script prints them when it runs. For a view of the **whole** model with nothing
missing, use the 3MF — it is meshed rather than exact, but it holds all 94
placements.

The placement parser is checked against the 3MF: the rotation matrices and
translations it derives match the transforms cade writes into
`3D/3dmodel.model`, to the digit.

### Parasolid

Two notes on it. `fasteners` is absent as a node, because none of the fastener
parts export to b-rep in the first place, so that subsystem was already empty
upstream. And the header's `DATE` field reads `5-sep-2116` — a clock artifact
from the exporting device, not a meaningful date.

Note that STL cannot hold this model at all — `cade` refuses it, because STL has
no objects, names, or placements and the entry point is a 71-part assembly.
