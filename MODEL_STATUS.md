# ETA 2824-2 model status

Status meanings: `placeholder` is a simple envelope; `estimated` has constrained
expert geometry; `supported` is directly grounded in cited dimensions. No row is
manufacturing-qualified.

The third column records a conceptual grouping from the parts ledger. It does
not prescribe filenames: all modeling begins in `watch.cade`, and the CAD agent
will choose if and when to split it.

| ETA position | Component | Conceptual group | Geometry | Placement | Clearance review | Next refinement |
|---:|---|---|---|---|---|---|
| 1 | Main plate, assembled | main_plate.cade | estimated | estimated | pending | Calibrate plate outline, bearing seats, and screw axes |
| 1-1 | Dial fastener | main_plate.cade | placeholder | estimated | pending | ETA fastener geometry |
| 1-2 | Bottom balance shock absorber | main_plate.cade | estimated | estimated | pending | Confirm jewel and press-seat dimensions |
| 2 | Sliding pinion | hand_setting.cade | estimated | estimated | pending | Confirm provisional 12 teeth and stem interface |
| 3 | Winding pinion | hand_setting.cade | estimated | estimated | pending | Confirm provisional 12 teeth and stem interface |
| 4 | Winding stem | hand_setting.cade | estimated | estimated | pending | S 0.9 detail and case length |
| 5 | Corrector lever | hand_setting.cade | placeholder | estimated | pending | Lever outline and travel |
| 6 | Setting lever | hand_setting.cade | placeholder | estimated | pending | Pivot and engagement geometry |
| 7 | Yoke | hand_setting.cade | placeholder | estimated | pending | Fork and spring contact |
| 8 | Setting lever jumper | hand_setting.cade | placeholder | estimated | pending | Spring outline and detents |
| 9 | Escape wheel | going_train.cade | estimated | estimated | pending | Replace provisional tooth blocks with escapement profile |
| 10 | Intermediate wheel | going_train.cade | estimated | estimated | pending | Confirm provisional 84/7 count and pitch geometry |
| 11 | Third wheel | going_train.cade | estimated | estimated | pending | Confirm provisional 75/10 count and pitch geometry |
| 12 | Second wheel | going_train.cade | estimated | estimated | pending | Confirm provisional 80/10 count and pitch geometry |
| 13 | Train wheel bridge | going_train.cade | estimated | estimated | pending | Calibrate outline and confirm jewel/screw centers |
| 14 | Movement barrel | barrel_and_winding.cade | estimated | estimated | pending | Confirm 80-tooth hypothesis and add mainspring/arbor detail |
| 15 | Stop lever | barrel_and_winding.cade | placeholder | estimated | pending | Functional outline and travel |
| 16 | Barrel bridge | barrel_and_winding.cade | estimated | estimated | pending | Calibrate outline and confirm barrel/crown-wheel supports |
| 17 | Click | barrel_and_winding.cade | placeholder | estimated | pending | Ratchet engagement |
| 18 | Click spring | barrel_and_winding.cade | placeholder | estimated | pending | Spring path and preload |
| 19 | Crown wheel | barrel_and_winding.cade | estimated | estimated | pending | Confirm provisional 26-tooth count and support |
| 20 | Ratchet wheel | barrel_and_winding.cade | estimated | estimated | pending | Confirm provisional 63-tooth count and arbor fit |
| 21 | Pallet fork | escapement.cade | estimated | estimated | pending | Calibrate pallet faces, fork slot, and banking |
| 22 | Pallet bridge | escapement.cade | placeholder | estimated | pending | Pivot seat and outline |
| 23 | Timed balance | balance.cade | estimated | estimated | pending | Replace concentric hairspring proxy and add staff/roller |
| 24 | Balance bridge assembly | balance.cade | composed assembly | estimated | pending | Refine positions 24-1 through 24-6 |
| 24-1 | Balance bridge | balance.cade | placeholder | estimated | pending | Outline, jewel axis, screw seat |
| 24-2 | Stud support | balance.cade | placeholder | estimated | pending | Clamp geometry |
| 24-3 | Lower index | balance.cade | placeholder | estimated | pending | Regulator geometry |
| 24-4 | Upper index | balance.cade | placeholder | estimated | pending | Fine regulator geometry |
| 24-5 | Regulator corrector | balance.cade | placeholder | estimated | pending | Corrector geometry |
| 24-6 | Top balance shock absorber | balance.cade | placeholder | estimated | pending | Jewel and press-seat dimensions |
| 25 | Automatic framework | automatic_winding.cade | estimated | estimated | pending | Calibrate outline and confirm reverser jewel/screw centers |
| 26 | Ratchet-wheel driving wheel | automatic_winding.cade | estimated | estimated | pending | Confirm provisional 42-tooth count and pitch |
| 27 | Auxiliary reversing wheel | automatic_winding.cade | estimated | estimated | pending | Confirm 34-tooth estimate and add reverser internals |
| 28 | Reversing wheel | automatic_winding.cade | estimated | estimated | pending | Confirm 34-tooth estimate and add reverser internals |
| 29 | Reduction wheel | automatic_winding.cade | estimated | estimated | pending | Confirm provisional 52/12 count and center distance |
| 30 | Automatic lower bridge | automatic_winding.cade | placeholder | estimated | pending | Bearings and outline |
| 31 | Oscillating weight assembly | automatic_winding.cade | composed assembly | estimated | pending | Refine positions 31-1 and 31-2 |
| 31-1 | Oscillating weight | automatic_winding.cade | estimated | estimated | pending | Calibrate mass sector and arm outline |
| 31-2 | Ball bearing | automatic_winding.cade | placeholder | estimated | pending | Bearing dimensions |
| 32 | Setting wheel | dial_side.cade | estimated | estimated | pending | Confirm provisional 24-tooth count and center |
| 33 | Cannon pinion | dial_side.cade | estimated | supported axis | pending | Confirm 12-tooth driver and refine H2 detail |
| 34 | Minute wheel | dial_side.cade | estimated | estimated | pending | Confirm ratio-constrained 36/10 geometry |
| 35 | Date corrector | dial_side.cade | estimated | estimated | pending | Confirm provisional 18-tooth count, finger, and travel |
| 36 | Date indicator | dial_side.cade | supported | supported axis | pending | Refine drawing-supported 31 internal teeth and printing |
| 37 | Hour wheel | dial_side.cade | estimated | supported axis | pending | Confirm ratio-constrained 40 teeth and H2 detail |
| 38 | Date-indicator driving wheel | dial_side.cade | estimated | estimated | pending | Confirm provisional 24 teeth, finger, and center |
| 39 | Minute train bridge | dial_side.cade | placeholder | estimated | pending | Bearings and outline |
| 40 | Date jumper | dial_side.cade | placeholder | estimated | pending | Tooth engagement and spring |
| 41 | Date-jumper maintaining plate | dial_side.cade | placeholder | estimated | pending | Outline and fastener seat |
| 42 | Dial support | dial_side.cade | placeholder | estimated | pending | Support height and contact |
| 43 | Key-bolt | dial_side.cade | placeholder | estimated | pending | Outline and interface |
| 900 | Screw class for positions 8/41 | fasteners.cade | estimated | estimated | pending | Confirm countersink, shank, and thread dimensions |
| 901 | Bridge screw class | fasteners.cade | estimated | estimated | pending | Confirm countersink, shank, and thread dimensions |
| 902 | Crown-wheel screw | fasteners.cade | estimated | estimated | pending | Confirm collar and thread dimensions |
| 903 | Ratchet-wheel screw | fasteners.cade | estimated | estimated | pending | Confirm known left-hand thread dimensions |
| 904 | Automatic-framework screw | fasteners.cade | estimated | estimated | pending | Confirm countersink, shank, and thread dimensions |
| 905 | Automatic-lower-bridge screw | fasteners.cade | estimated | estimated | pending | Confirm countersink, shank, and thread dimensions |
| 906 | Oscillating-weight screw | fasteners.cade | estimated | estimated | pending | Confirm collar and thread dimensions |
| 907 | Minute-train-bridge screw | fasteners.cade | estimated | estimated | pending | Confirm shoulder and thread dimensions |

## Whole-assembly gates

- [ ] All part-ledger envelopes compile through `watch`.
- [x] Movement/case diagnostic volume is zero at 0.15 mm diagnostic cell.
- [ ] Rotor/caseback clearance is verified.
- [ ] Strap attachment interfaces are represented and clear the case.
- [x] Every ETA ledger row has an evidence class and next refinement.
- [x] Known Cade gaps are recorded in `GAPS.md`.
