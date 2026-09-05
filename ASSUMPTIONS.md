# Assumptions and interfaces

## Model status

This is a reference reconstruction. Published values take priority over derived
values, which take priority over photo estimates, which take priority over expert
estimates and placeholders. Fit in this model does not promote an estimate to an
authoritative ETA dimension.

## Coordinate system

- Origin: movement center on the dial-seat datum plane.
- +X: toward 3 o'clock and the winding stem.
- +Y: toward 12 o'clock.
- +Z: from the dial side toward the rotor side.
- All primitive envelopes are modeled about their local origin and placed by
  explicit frames.
- Rotor-side layout is reconciled to the ETA assembly illustration with the
  winding stem as the fixed datum. The balance lies on the negative-Y side of
  the stem axis; train, supports, jewels, arbors, and fasteners follow that hand.

## Configuration choices

| Choice | Current value | Class | Basis |
|---|---:|---|---|
| Calibre | ETA 2824-2 | published | ETA identification |
| Hand-height execution | H2 normal | published selection | ETA hand-height drawing; common execution |
| Overall movement diameter | 26.00 mm | published | ETA manufacturing information |
| Case-fitting diameter | 25.60 mm | published | ETA manufacturing information |
| Overall movement height | 4.60 mm | published | ETA manufacturing information |
| Case bore diameter | 26.80 mm | expert_estimate | 0.40 mm radial envelope clearance for the first scaffold |
| Case outside diameter | 37.00 mm | expert_estimate | Conservative round case around the 26.80 mm movement cavity |
| Case-middle height | 7.00 mm | expert_estimate | Spans the complete rough movement stack and supports crystal/caseback faces |
| Crystal diameter / thickness | 34.40 / 1.00 mm | expert_estimate | Flat transparent scaffold seated on the case-middle front face |
| Caseback diameter / thickness | 36.00 / 1.20 mm | expert_estimate | Solid rough back seated on the case-middle rear face |
| Preview cell | 0.05 mm | workflow setting | visualization only; not a tolerance |
| Strap/lug width | 20.00 mm | placeholder | no target case or strap specification supplied |
| Spring-bar/hole nominal diameter | 1.30 mm | expert_estimate | common watch attachment scale; requires case specification |

## Interface ledger

| Interface | Relationship | Nominal/allowance | Source | Verification |
|---|---|---|---|---|
| Movement to case bore | radial clearance | 26.00 mm envelope in 26.80 mm bore | ETA + expert_estimate | zero-volume diagnostic at 0.15 mm cell |
| Dial feet to main plate | location/clearance | diameter 0.736-0.750 mm at (+11.60,+3.78) and (-11.60,-3.78) mm | ETA drawing Z0091446 | geometry pending |
| Hour hand to hour wheel | fitted | diameter 1.500 +0.004/-0.002 mm | ETA hand-height drawing | geometry pending |
| Minute hand to cannon pinion | fitted | diameter 0.900 +0.006/-0.004 mm | ETA hand-height drawing | geometry pending |
| Seconds hand to pin | fitted | diameter 0.250 mm nominal | ETA hand-height drawing | geometry pending |
| Rotor to case middle | radial clearance | 24.40 mm swept envelope in 26.80 mm bore | expert_estimate | zero-volume diagnostic at 0.15 mm cell |
| Upper strap attachment to case | clearance marker in lug holes | 1.00 mm marker in 1.30 mm hole | placeholder | diagnostic pending |
| Lower strap attachment to case | clearance marker in lug holes | 1.00 mm marker in 1.30 mm hole | placeholder | diagnostic pending |

## Envelope-layout assumptions

The first modeling pass should create deliberately simple movement parts in
plausible axial bands, initially within `watch.cade`. Their XY centers and most
local sizes will be `expert_estimate` values chosen to produce a coherent first
assembly. They must be revised against better orthographic references and
kinematic constraints. Placeholder gear cylinders do not assert tooth count,
module, pressure angle, or exact outside diameter.

## Change rule

When an assumption changes, update this file, the corresponding named Cade
parameter or adjacent comment, `MODEL_STATUS.md`, and every affected clearance
diagnostic in the same change, wherever the CAD agent has chosen to locate it.
