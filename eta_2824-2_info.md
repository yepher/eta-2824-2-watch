# ETA 2824-2 Information and Assembly Model

## Purpose and evidence rule

This document is an evidence ledger and a proposed logical CAD assembly for the
ETA 2824-2. It does not claim that exploded-view proportions are manufacturing
dimensions. A value is a dimension only when a cited source states it or a
physical measurement records its method and uncertainty.

Primary source: ETA Technical Communication `CT 2824-2 ESI 481825 25`, dated
2022-10-06. The local reference file is
[`references/ETA Caliber 2824-2 Watch Movement.pdf`](references/ETA%20Caliber%202824-2%20Watch%20Movement.pdf).
The official current download is the [ETA technical document](https://shopb2b.eta.ch/en/technicaldocuments/index/pdf/id/1884/).

## Movement-level facts

| Property | Published value | CAD use |
|---|---:|---|
| Calibre | ETA 2824-2 | Configuration identity |
| Ligne size | 11 1/2''' | Trade size; do not convert back when 25.60 mm is given directly |
| Overall movement diameter | 26.00 mm | Maximum published radial envelope |
| Case-fitting diameter | 25.60 mm | Nominal movement-seat interface |
| Overall movement height | 4.60 mm | Preliminary axial envelope only |
| Jewels | **17 in the modelled execution**; 25 in ETA's published one | See *Which execution this model is of* |
| Frequency | 28,800 vibrations/hour (4 Hz) | Kinematic metadata |
| Balance lift angle | 50 degrees | Service/test metadata |
| Minimum power reserve | 38 hours | Performance metadata |
| Typical power reserve | 42 hours | Performance metadata |
| Functions | Hours, minutes, central seconds, date, stop seconds, quick date correction, bidirectional automatic winding | Functional decomposition |

The overall diameter and height do not define the casing seat, stem axis, dial
seat, hand stack, rotor clearance, clamp geometry, or individual components.

## Part ledger

`Position` is the identifier printed in the 2022 ETA exploded and assembly
diagrams. `Catalog identifier` is the published GTIN when ETA supplies one;
`Variant-controlled` means ETA directs the reader to the relevant calibre and
variant in ETAshop. It must not be replaced with a guessed legacy number.

The technical communication publishes no component envelope dimensions. That
absence is recorded explicitly so image scale cannot silently become a datum.

| Logical assembly | Position | Catalog identifier | ETA description | Published component dimensions |
|---|---:|---|---|---|
| Main plate | 1 | Variant-controlled | Main plate, assembled | Not published |
| Main plate | 1-1 | 7613226044203 | Dial fastener | Not published |
| Main plate | 1-2 | Variant-controlled | Bottom jewelled balance shock absorber, shouldered, press-in | Not published |
| Hand-setting mechanism | 2 | 7613226053519 | Sliding pinion | Not published |
| Hand-setting mechanism | 3 | 7613226057111 | Winding pinion | Not published |
| Hand-setting mechanism | 4 | Variant-controlled | Winding stem | Envelope not published; external supplier lists thread diameter 0.90 mm |
| Hand-setting mechanism | 5 | 7613226016064 | Corrector lever | Not published |
| Hand-setting mechanism | 6 | 7613226048171 | Setting lever, assembled | Not published |
| Hand-setting mechanism | 7 | 7613226032965 | Yoke | Not published |
| Hand-setting mechanism | 8 | Variant-controlled | Setting lever jumper | Not published |
| Going train | 9 | 7613226056473 | Escape wheel | Not published |
| Going train | 10 | 7613226041271 | Intermediate wheel, assembled | Not published |
| Going train | 11 | 7613226051010 | Third wheel | Not published |
| Going train | 12 | Variant-controlled | Second wheel | Not published |
| Going train | 13 | Variant-controlled | Train wheel bridge, jewelled | Not published |
| Barrel and winding | 14 | Variant-controlled | Movement barrel, complete | Not published |
| Barrel and winding | 15 | 7613226043121 | Stop lever | Not published |
| Barrel and winding | 16 | Variant-controlled | Barrel bridge | Not published |
| Barrel and winding | 17 | 7613226000254 | Click | Not published |
| Barrel and winding | 18 | 7613226028753 | Click spring | Not published |
| Barrel and winding | 19 | 7613226057326 | Crown wheel | Not published |
| Barrel and winding | 20 | Variant-controlled | Ratchet wheel | Not published |
| Escapement | 21 | 7613226023642 | Pallet fork | Not published |
| Escapement | 22 | Variant-controlled | Pallet bridge, jewelled | Not published |
| Balance and regulation | 23 | Variant-controlled | Timed balance regulated, with stud | Not published |
| Balance and regulation | 24 | Variant-controlled | Balance bridge, assembled | Not published |
| Balance and regulation | 24-1 | Variant-controlled | Balance bridge | Not published |
| Balance and regulation | 24-2 | 7613226046092 | Stud support | Not published |
| Balance and regulation | 24-3 | 7613226048713 | Lower index, assembled | Not published |
| Balance and regulation | 24-4 | 7613226033832 | Upper index, fine regulation | Not published |
| Balance and regulation | 24-5 | Variant-controlled | Regulator corrector | Not published |
| Balance and regulation | 24-6 | Variant-controlled | Top jewelled balance shock absorber, shouldered, press-in | Not published |
| Automatic winding | 25 | Variant-controlled | Automatic device framework, jewelled | Not published |
| Automatic winding | 26 | 7613226054400 | Ratchet wheel driving wheel | Not published |
| Automatic winding | 27 | 7613226023543 | Auxiliary reversing wheel | Not published |
| Automatic winding | 28 | 7613226044098 | Reversing wheel | Not published |
| Automatic winding | 29 | 7613226012943 | Reduction wheel, assembled | Not published |
| Automatic winding | 30 | 7613226025998 | Automatic device lower bridge, jewelled | Not published |
| Automatic winding | 31 | Variant-controlled | Oscillating weight, assembled | Not published |
| Automatic winding | 31-1 | Variant-controlled | Oscillating weight | Not published |
| Automatic winding | 31-2 | 7613226038509 | Ball bearing | Not published |
| Motion works and calendar | 32 | 7613226074163 | Setting wheel | Not published |
| Motion works and calendar | 33 | Variant-controlled | Cannon pinion with driving wheel | Not published; hand-fitting interface belongs in a separate controlled drawing |
| Motion works and calendar | 34 | 7613226031128 | Minute wheel | Not published |
| Motion works and calendar | 35 | 7613226033115 | Date corrector, assembled | Not published |
| Motion works and calendar | 36 | Variant-controlled | Date indicator | Not published |
| Motion works and calendar | 37 | Variant-controlled | Hour wheel, assembled | Not published; hand-fitting interface belongs in a separate controlled drawing |
| Motion works and calendar | 38 | 7613226014053 | Date indicator driving wheel | Not published |
| Motion works and calendar | 39 | Variant-controlled | Minute train bridge | Not published |
| Motion works and calendar | 40 | 7613226036208 | Date jumper | Not published |
| Motion works and calendar | 41 | 7613226054462 | Date jumper maintaining plate, assembled | Not published |
| Dial interface | 42 | Variant-controlled | Dial support | Not published |
| Dial interface | 43 | 7613226021778 | Key-bolt | Not published |
| Fasteners | 900 | Variant-controlled | Countersunk screw for positions 8 and 41 | Not published |
| Fasteners | 901 | Variant-controlled | Countersunk screw for bridges at positions 13, 16, 22, and 24 | Not published |
| Fasteners | 902 | Variant-controlled | Collared cylindrical-head screw for crown wheel, position 19 | Not published |
| Fasteners | 903 | Variant-controlled | Cylindrical-head screw for ratchet wheel, position 20 | Not published; left-hand thread is called out in assembly instructions |
| Fasteners | 904 | Variant-controlled | Countersunk screw for automatic framework, position 25 | Not published |
| Fasteners | 905 | Variant-controlled | Countersunk screw for automatic lower bridge, position 30 | Not published |
| Fasteners | 906 | Variant-controlled | Collared cylindrical-head screw for oscillating weight, position 31 | Not published |
| Fasteners | 907 | Variant-controlled | Shouldered screw for minute train bridge, position 39 | Not published |

## Published interface dimensions from secondary catalogs

These are useful leads, not replacements for controlled ETA drawings. Confirm
them against the selected movement variant and a physical sample before driving
CAD geometry.

| Interface | Reported value | Source and interpretation |
|---|---:|---|
| Hand fittings | 0.90 x 1.50 x 0.25 mm | Boley ETA 2824-2 catalogue; commonly minute/hour/seconds fitting diameters, but order and tolerances require confirmation |
| Winding stem thread | 0.90 mm diameter | Time Connection ETA 2824-2 parts listing |
| Mainspring listing | 1.23 x 10.5 x 0.132 AUT | Boley catalogue spelling; meanings and units must be confirmed before use |

## Common dimensions recoverable from ETA manufacturing drawings

ETA's service communication is a parts and lubrication document, not a set of
manufacturing drawings. A separate official *Manufacturing Information* document,
`IH 2824-2 FDE 478720 11` (2010-07-27), does publish the shared interfaces used to
design a case, dial, hands, date window, and crown. An archived copy is available
as a [16-page ETA manufacturing-information PDF](https://www.watch-spare.com/amfile/file/download/file/1/product/10107/).
It predates the 2022 service communication, so confirm the selected execution,
hand-height code, and supplied parts before releasing manufacturing geometry.

### Movement and dial envelope

| Feature | ETA dimension | CAD interpretation |
|---|---:|---|
| Overall movement diameter | 26.00 mm | Maximum published radial envelope |
| Case-fitting diameter | 25.60 mm | Nominal movement seat diameter; case clearance is a separate design choice |
| Overall movement height | 4.60 mm | Movement only; excludes dial and hands |
| Dial outside diameter | 26.00 mm | Drawing for calibres 2801-2, 2804-2, and 2824-2 |
| Flat dial nominal thickness | 0.40 mm | The hand-height table uses a 0.40 mm dial |
| Dial centre hole | 2.000 to 2.060 mm | Drawing callout `diameter 2 +0.060/0` |
| Dial-foot diameter | 0.736 to 0.750 mm | Drawing callout `diameter 0.75 +0/-0.014` |
| Upper-right dial-foot centre | x = +11.60 mm, y = +3.78 mm | Dial coordinates with +x toward 3 o'clock and +y toward 12 o'clock |
| Lower-left dial-foot centre | x = -11.60 mm, y = -3.78 mm | Diametrically opposed to the upper-right foot in the published drawing |
| Date-window clear opening | 3.30 x 2.00 mm | Rectangular opening shown at 3 o'clock |
| Movement centre to near edge of date window | 8.85 mm | Locates the opening radially |
| Date-window near edge to outer reference | 2.70 mm | Secondary radial location shown on the ETA dial drawing |
| Crown-to-case gap after casing | 0.02 to 0.10 mm | Crown-position drawing; the text separately requires no more than 0.10 mm |

The two foot coordinates above come from ETA drawing `Z0091446`, reproduced in
the local files
[`references/parts/1742079617617.png`](references/parts/1742079617617.png) and
[`references/parts/looking-for-documents-that-help-me-precisely-locate-dial-v0-n6h561v5yuga1.webp`](references/parts/looking-for-documents-that-help-me-precisely-locate-dial-v0-n6h561v5yuga1.webp).
The nearby `R 12.8`, `R 12.2`, `R 11.55`, and `R 11.45` annotations point to dial
profile/window construction and must not be substituted for the explicitly
dimensioned foot-centre coordinates.

### Date indicator, position 36

| Feature | ETA dimension | Notes |
|---|---:|---|
| Outside diameter | 23.30 mm | Flat and convex versions |
| Toothed inside reference diameter | 16.512 mm | 31 teeth |
| Flat indicator thickness | 0.23 mm | Edge section in the flat-indicator drawing |
| Inner free-of-varnish thickness | 0.18 mm | Local section near the inner diameter |
| Maximum varnish/printing layer | 0.03 mm | Explicit ETA maximum |
| Inner unvarnished reference diameter, flat version | 17.42 mm | Do not substitute for the 16.512 mm toothed reference |
| Inner unvarnished reference diameter, convex version | 17.40 mm | Convex drawing |
| Raised/convex reference diameter | 19.75 mm | Convex drawing only |
| Date-window corner radius | 11.55/2 mm | ETA notation: `R 11.55/2 x 2.7`; retain drawing notation until the window profile is reconstructed |

### Gear and pinion tooth-count ledger

The available ETA service and manufacturing documents identify the train parts
but do not publish a tooth schedule. ETA drawing `Z0465620`/`Z0112468` verifies
the date indicator's 31 internal teeth. The Movement Archive's examination of an
ETA 2824-2 specimen supplies secondary, direct-observation evidence for a
20-tooth escape wheel. A wheel and its coaxial pinion are separate toothed
members and must be counted separately; do not record one number against an
assembled part without naming which member it describes.

| Position | Component | Wheel/ring teeth | Pinion leaves or secondary teeth | Evidence status |
|---:|---|---:|---:|---|
| 2 | Sliding pinion | Unknown | Unknown | Requires direct count or controlled drawing |
| 3 | Winding pinion | - | **12** | Watchmaker's account, confirmed by the 2.625 ratio check; see *The winding train, resolved* |
| 9 | Escape wheel | **20** | Unknown | Secondary direct-observation evidence from [The Movement Archive](https://17jewels.info/movements/e/eta/eta-2824-2/); not stated in the ETA service document |
| 10 | Intermediate wheel, assembled | Unknown | Unknown | Count both toothed members separately |
| 11 | Third wheel | Unknown | Unknown | Count wheel teeth and pinion leaves separately |
| 12 | Second wheel | Unknown | Unknown | Count wheel teeth and pinion leaves separately |
| 14 | Movement barrel, complete | Unknown | Not applicable/unknown | Count the barrel's great-wheel teeth; do not count ratchet teeth as the same member |
| 19 | Crown wheel | **26** | - | `photo_measured` off `IMG_9577.JPG` (fit score 0.209, harmonics at 53 and 78), and independently confirmed by the 2.625 ratio check |
| 20 | Ratchet wheel | **63** | - | `photo_measured` off a teardown frame, confirmed by the 2.625 ratio check. The crown wheel engages these on **alternate teeth**, effective 31.5 |
| 26 | Ratchet-wheel driving wheel | Unknown | Unknown | Count every distinct toothed member |
| 27 | Auxiliary reversing wheel | Unknown | Unknown | Reversing-wheel internals may not be described by one external count |
| 28 | Reversing wheel | Unknown | Unknown | Reversing-wheel internals may not be described by one external count |
| 29 | Reduction wheel, assembled | Unknown | Unknown | Count wheel teeth and pinion leaves separately |
| 32 | Setting wheel | Unknown | Unknown | Requires direct count or controlled drawing |
| 33 | Cannon pinion with driving wheel | Unknown | Unknown | Record driving-wheel teeth separately from the cannon-pinion teeth/leaves |
| 34 | Minute wheel | Unknown | Unknown | Count minute-wheel teeth and its hour-wheel-driving pinion separately |
| 36 | Date indicator | **31** | Not applicable | Verified by ETA drawing `Z0465620`/`Z0112468` |
| 37 | Hour wheel, assembled | Unknown | Unknown | Requires direct count or controlled drawing |
| 38 | Date-indicator driving wheel | Unknown | Unknown | Include any separate finger or secondary member in the description |

Generic textbook train counts and counts from Sellita, Asian 2824-compatible
movements, or other ETA calibres are useful plausibility checks but are not
evidence for this ledger. For a physical movement, capture a calibrated,
face-on image of each wheel and mark every counted tooth. Validate the completed
going-train schedule against the observed rotation rates and 28,800-vph
escapement; validate the motion works against one hour-hand revolution per
12 cannon-pinion revolutions. These ratio checks catch miscounts but cannot
identify a unique tooth schedule by themselves.

#### Rejected or unverified tooth-count claims

A proposed schedule of `80/10`, `75/10`, and `70/7`, followed by a 20-tooth
escape wheel, is not compatible with 28,800 vibrations per hour if interpreted
as a conventional centre-to-third-to-fourth-to-escape train:

```text
fourth-wheel rate = (80/10) * (75/10) = 60 revolutions/hour
escape-wheel rate = 60 * (70/7) = 600 revolutions/hour
vibrations/hour   = 600 * 20 teeth * 2 vibrations/tooth = 24,000
```

At 28,800 vibrations/hour and 20 escape-wheel teeth, the escape wheel must turn
`720 revolutions/hour`, so the last stage would require a 12:1 ratio after a
60-revolutions/hour fourth wheel. The frequency does not determine a unique pair
of integer tooth counts, and the ETA 2824-2's indirectly driven hands make it
unsafe to paste conventional train names onto ETA positions 10-12.

The following submitted values remain leads only: barrel `about 80-84`, winding
pinion `12`, crown wheel `26`, and ratchet wheel `63`. The cited pages were not
specific technical drawings or count records, and winding-train tooth counts are
not mathematically fixed by the escapement frequency. Do not use these values in
geometry until a clear face-on part image, a counted specimen, or a controlled
drawing confirms each one.

#### Current CAD train hypothesis (2026-09-05)

The rough-envelope CAD uses the following explicitly provisional integer train
to constrain relative pitch diameters and wheel centers: second wheel `80/10`,
third wheel `75/10`, intermediate/fourth wheel `84/7`, and escape wheel `20`.
Only the escape-wheel count is supported by secondary direct-observation
evidence; every other count remains an `expert_estimate` until directly counted
or found on a controlled drawing.

The hypothesis closes the required rate exactly when the second/centre wheel
turns once per hour:

```text
intermediate/fourth rate = 1 * (80/10) * (75/10) = 60 revolutions/hour
escape-wheel rate        = 60 * (84/7) = 720 revolutions/hour
vibrations/hour          = 720 * 20 * 2 = 28,800
```

The current Cade radii are visualization envelopes rather than a declared
module or production tooth profile. They will be revised together when direct
tooth counts, calibrated images, or measured center distances become available.

The same 2026-09-05 detail pass uses the following additional CAD-only tooth
hypotheses. These values are `expert_estimate`, not new evidence: barrel great
wheel 80, crown wheel 26, ratchet wheel 63, automatic driving wheel 42,
auxiliary/reversing wheels 34 each, reduction wheel 52/12, setting wheel 24,
cannon-pinion driver 12, minute wheel 36/10, hour wheel 40, date corrector 18,
date driver 24, and sliding/winding pinions 12 each. The motion-work subset is
ratio-constrained: `(12/36) * (10/40) = 1/12`. The date indicator alone retains
its drawing-supported 31 internal teeth. Tooth blocks are visual envelopes, not
production involute or cycloidal profiles.

#### Derived train, 2026-09-05 (supersedes the 2026-09-05 rough hypothesis)

The rough-envelope counts were replaced with a chain that closes and a module
per mesh, so every wheel radius is now `m * z / 2` rather than an independent
estimate. Only the escape wheel's 20 teeth carry secondary evidence; every other
count is an `expert_estimate` constrained by the chain closing.

Going train, with the second wheel turning once an hour:

```text
second 75 / third pinion 10   = 7.5   -> third   7.5 rev/h
third  80 / fourth pinion 10  = 8     -> fourth  60  rev/h = 1 rev/min
fourth 84 / escape pinion 7   = 12    -> escape 720  rev/h
720 * 20 teeth * 2                    = 28,800 vibrations/hour
```

Modules step down toward the escapement so the wheels shrink as torque falls,
which is what lets the train fit a 25.60 mm plate: barrel-second 0.100,
second-third 0.085, third-fourth 0.070, fourth-escape 0.050.

The fourth wheel is the CENTRE SECONDS wheel and sits on the movement axis. The
cannon pinion is a tube around its arbor and is driven indirectly:

```text
second wheel (1 rev/h) -> dial pinion 12 -> idler 40 -> minute wheel 36
                       -> cannon pinion 12          (1:1, an idler adds no ratio)
cannon 12 / minute 36 * minute pinion 10 / hour 40  = 1/12
```

Automatic winding, module 0.120 from the rotor to the reduction wheel and 0.100
from there to the ratchet:

```text
rotor pinion 40 -> reversing wheels 27 and 28, 34 each -> reduction wheel 29, 52
reduction pinion 12 -> driving wheel 26, 42
driving pinion 10   -> ratchet wheel 20, 63
1 rotor turn = 0.03489 ratchet turns, so 28.7 turns of the weight per ratchet turn
```

The rotor pinion's 2.40 mm pitch radius is not a free choice: it is cut around
the ball bearing, and it sets the scale of the whole module.

Winding train: crown wheel 26 and ratchet wheel 63 on module 0.100, centre
distance 4.45 mm. The 90-degree face-gear interface from the stem's winding
pinion to the crown wheel is UNRESOLVED and deliberately not modelled.

### Hand-fitting diameters and normal H2 heights

The drawing's asymmetric diameter tolerances are stated in thousandths of a
millimetre. The table below expands them into millimetres. `H2 normal` is the
common normal-height execution, not a promise that every purchased 2824-2 uses
that execution.

| Interface | Nominal / limits | H2 normal height from dial seat |
|---|---:|---:|
| Hour hand fitting | 1.500 mm, +0.004/-0.002 mm; 3% taper | 0.95 mm |
| Minute hand fitting | 0.900 mm, +0.006/-0.004 mm; cylindrical | 1.35 mm |
| Seconds hand fitting | 0.250 mm nominal | 1.75 mm |
| Seconds pin outside diameter | 0.256 mm, +0.006/-0.004 mm | Included in the seconds-hand stack |
| Hour-wheel outside reference | 1.50 mm | Diameter shown around the hour fitting |
| Minute-wheel outside reference | 0.90 mm | Diameter shown around the minute fitting |
| Centre/seconds tube reference | 0.70 mm | Cylindrical reference shown in the stack |

For H2 normal the drawing also gives total lengths from its lower datum: cannon
pinion `A = 2.20 mm`, hour wheel `B = 1.25 mm`, seconds-wheel pin
`C = 5.07 mm`, and centre tube `D = 2.50 mm`. The other published hand-height
executions are H1, H3, H4, H5, and H6; model the execution code as configuration
data rather than changing these values silently.

### Winding stem and crown interface

| Feature | ETA dimension | Notes |
|---|---:|---|
| Stem thread | S 0.9 | Swiss watch-thread designation printed on the drawing; do not treat it as an ISO M0.9 thread |
| Normal stem length `L` | 16.00 mm | From movement-side shoulder datum to tip in the ETA drawing |
| Case-fitting diameter to stem tip `L1` | 8.65 mm | Drawing datum, not a cut-to-fit crown length |
| Opposite movement reference to stem tip `L2` | 21.65 mm | Drawing datum |
| Total setting travel with calendar `C` | 0.80 mm | `C = C1 + C2` |
| Running to date-correction travel `C1` | 0.30 mm | Calendar execution |
| Date-correction to time-setting travel `C2` | 0.50 mm | Calendar execution |

### How to obtain dimensions for the remaining internal parts

There is no reliable single public table of manufacturing dimensions for all
ETA 2824-2 components. Build the internal CAD model as a measured reconstruction:

1. Buy one known-genuine movement of the exact execution and record its calibre,
   grade, shock system, and hand-height code before disassembly.
2. Photograph every layer square to the plate with a stage micrometer in the same
   plane. Images without an in-plane scale are reference images, not measurements.
3. Measure outside diameters and thicknesses with a micrometer; use pin gauges or
   calibrated gauge pins for holes; use an optical comparator or calibrated
   microscope for tooth profiles, pivots, jewels, and irregular levers.
4. Establish one coordinate system from the main-plate centre and stem axis. Record
   wheel/jewel centres as coordinates, not as chained centre distances.
5. For every value record source, instrument, resolution, repeated readings,
   uncertainty, execution, and whether it is nominal, measured, or inferred.
6. Check each reconstructed gear pair by measured centre distance, tooth counts,
   and pitch/module consistency. A photograph scaled from the 25.60 mm seat is a
   useful initial estimate only; perspective and exploded-view displacement make
   it unsuitable for final fits.

This approach can recover practical assembly geometry, but pivots, jewel fits,
spring geometry, escapement faces, and press fits need substantially tighter
measurement and should not be reverse-engineered from catalog photographs.

## Drawing-scaled dimensions from the ETA materials page

Added 2026-09-05. This is a new and much stronger evidence class than the photo
estimates most of this model was built on, and it changes several parts
materially.

Page 6 of the local ETA Technical Communication (footer
`CT 2824-2 FDE 481688 22`, 10.05.2016) is the "Fournitures - Bestandteile -
Materials" page. Every component is drawn there in plan *and* elevation at one
common scale. Position `1 Var`, the main plate, is drawn in plan at the
published movement diameter of 25.60mm, and that single published number
calibrates the whole page. Every other silhouette on it therefore becomes a
measurable dimension.

Reproduce with:

```sh
python3 tools/scale_materials_page.py "references/ETA Caliber 2824-2 Watch Movement.pdf"
```

Confidence and limits. The embedded scan is 150 ppi, so the page is about
0.13mm per pixel at life size. An outline spanning many pixels -- a diameter, an
overall thickness -- is good to roughly +/-0.1mm. Individual teeth are at or
below one pixel and **cannot** be counted except on the coarsest wheels, so
tooth counts below are stated only where the count actually resolved. These are
`drawing_scaled` values: better than a photo estimate, weaker than a dimensioned
drawing, and never to be promoted to a manufacturing dimension.

| Pos | Part | Plan / diameter | Elevation / height |
| --- | --- | --- | --- |
| 1 Var | Main plate | 25.60 (calibration) | - |
| 2 | Winding pinion | 1.60 long | 1.45 dia |
| 3 | Sliding pinion | 1.21 long | 1.50 dia |
| 4 Var | Winding stem with crown | 17.13 overall length | crown 4.45 dia |
| 5 | Setting lever | 7.02 x 3.53 | 1.45 |
| 6 | Yoke | 5.86 x 3.19 | 1.74 |
| 7 | Setting lever jumper | 8.86 x 2.66 | - |
| 8 | Setting wheel assembly | 13.50 x 5.47 | - |
| 9 | Escape wheel | 4.94 dia | 2.71 over pivots |
| 10 | Third wheel | 6.78 dia | 3.29 over pivots |
| 11 | Second wheel | 6.97 dia | 3.24 over pivots |
| 12 Var | Centre / great wheel | 7.02 dia | 4.94 over pivots |
| 13 Var | Train wheel bridge | 20.81 x 13.60 | - |
| 14 Var | Barrel complete | **12.29 dia** | 3.29 over arbor |
| 15 | Click spring | 6.10 x 3.24 | - |
| 16 Var | Barrel bridge | 17.28 x 17.91 | - |
| 17 | Click | 3.34 x 3.00 | 1.31 |
| 18 | Click spring | 2.42 x 1.84 | - |
| 19 | Crown wheel | **6.29 dia, 26 teeth** | **0.82** |
| 20 | Ratchet wheel | **7.40 dia** | **0.53** |
| 21 Var | Pallet fork | 3.48 x 3.92 | 1.45 |
| 22 Var | Pallet bridge | 7.11 x 7.36 | 1.50 |
| 23 | Balance complete | **10.50 dia** | 2.95 over pivots |
| 24 Var | Balance cock with regulator | 8.23 x 15.44 | - |
| 25 Var | Automatic device framework | 13.50 x 16.45 | - |
| 26 | Automatic driving wheel | **5.86 dia** | 0.97 |
| 27 | Reversing wheel | 4.50 dia | 1.60 |
| 28 | Reversing wheel | 4.55 dia | 1.60 |
| 29 | Reduction wheel | 4.94 dia | 1.65 |
| 30 | Reduction wheel bridge | 10.65 x 5.76 | 1.50 |
| 31 Var | Oscillating weight | **24.92** x 16.45 | - |
| 31-2 | Ball bearing | 5.61 dia | 1.21 |

### Complete measured table

Every silhouette on the page, in page order. A part drawn in two views
has both listed: which is plan and which is elevation is stated where it
matters, and left open where the two are not distinguishable from the
outline alone. All values in millimetres.

| Pos | View 1 (w x h) | View 2 (w x h) | View 3 (w x h) |
| --- | --- | --- | --- |
| 1 Var | 25.60 x 25.60 | - | - |
| 1-1 | 4.21 x 2.23 | 2.47 x 1.45 | - |
| 1-2 | 2.47 x 0.92 | 2.42 x 2.47 | 2.76 x 1.45 |
| 2 | 1.60 x 2.03 | 1.02 x 1.45 | - |
| 3 | 0.92 x 2.95 | 1.02 x 1.50 | - |
| 4 Var | 17.13 x 4.84 | 4.45 x 1.50 | - |
| 5 | 7.02 x 1.45 | 6.97 x 3.53 | 1.02 x 1.50 |
| 6 | 5.86 x 1.74 | 5.81 x 3.19 | - |
| 7 | 8.86 x 2.66 | - | - |
| 8 | 13.50 x 5.47 | - | - |
| 9 | 4.94 x 2.71 | 4.94 x 4.94 | - |
| 10 | 6.82 x 3.29 | 6.78 x 6.73 | - |
| 11 | 7.07 x 3.24 | 6.97 x 6.97 | - |
| 12 Var | 7.02 x 4.94 | 7.02 x 6.97 | - |
| 13 Var | 20.81 x 13.60 | - | - |
| 14 Var | 12.29 x 3.29 | 12.29 x 12.29 | - |
| 15 | 6.10 x 3.24 | 1.98 x 1.50 | - |
| 16 Var | 17.28 x 17.91 | - | - |
| 17 | 3.48 x 1.31 | 3.34 x 3.00 | - |
| 18 | 2.42 x 1.84 | 2.03 x 1.50 | - |
| 19 | 6.44 x 0.82 | 6.29 x 6.24 | - |
| 20 | 7.55 x 0.53 | 7.40 x 7.45 | - |
| 21 Var | 3.58 x 1.45 | 3.48 x 3.92 | - |
| 22 Var | 7.11 x 7.36 | 5.47 x 1.50 | - |
| 23 | 10.55 x 2.95 | 10.50 x 10.55 | - |
| 24 Var | 8.23 x 15.44 | - | - |
| 24-1 Var | 8.18 x 13.84 | - | - |
| 24-2 | 5.27 x 4.21 | - | - |
| 24-3 | 4.94 x 3.68 | - | - |
| 24-4 | 6.39 x 3.34 | - | - |
| 24-5 | 1.45 x 0.97 | 1.45 x 1.36 | - |
| 24-6 | 3.63 x 0.92 | 3.58 x 3.58 | - |
| 25 Var | 13.50 x 16.45 | - | - |
| 26 | 5.90 x 0.97 | 5.86 x 5.86 | - |
| 27 | 4.65 x 1.60 | 4.50 x 4.45 | - |
| 28 | 4.60 x 1.60 | 4.55 x 4.45 | - |
| 29 | 5.08 x 1.65 | 4.94 x 4.98 | - |
| 30 | 10.65 x 5.76 | 2.08 x 1.50 | - |
| 31 Var | 24.92 x 16.45 | - | - |
| 31-1 Var | 24.87 x 16.45 | - | - |
| 31-2 | 5.71 x 1.21 | 5.61 x 5.61 | - |

### Stepped elevation profiles: the wheels that are two diameters

Added 2026-09-06, and this is the measurement that corrected the winding
train's module.

The bounding-box table above records each view's overall size, which hides the
thing that matters most about a watch wheel: many of them are **two diameters
on one arbor** -- a wheel and its pinion. Reading the elevation's width row by
row instead recovers the stepped profile, because in an elevation width IS
diameter. Reproduce with:

```sh
python3 tools/scale_materials_page.py "<the technical communication>" --profile
```

| Pos | Part | Large diameter | Small diameter |
| --- | --- | --- | --- |
| 9 | Escape wheel | 4.83 | 0.90 over the pinion, 0.45 arbor |
| 11 | Second wheel | 7.02 | 1.41 |
| 12 Var | Centre seconds wheel | 7.00 | 1.06, then a 0.61 arbor 3.77 long |
| 14 Var | Barrel | 12.27 over the teeth | 11.68 drum |
| 19 | Crown wheel | 6.41 | *one diameter only* |
| 20 | Ratchet wheel | 7.54 | *one diameter only* |
| 23 | Balance | 10.51 rim | 3.48 arms, 1.99 roller |
| 26 | Automatic driving wheel | 5.87 | **1.43** |
| 27, 28 | Reversing wheels | 4.60 | **4.24 — a second RING, not a pinion** |
| 29 | Reduction wheel | 4.99 | **1.16** |
| 31-2 | Rotor ring on its bearing | 5.69 over the teeth | 5.11 races |

Two things follow.

**The reversing wheels are not wheel-and-pinion.** Their two rings are almost
the same size, 4.60 and 4.24, which is what a reversing wheel with internal
pawls looks like: one ring takes the drive from the rotor, the other passes it
on, and the pawls between them lock one way and slip the other. The model had
one of them as a 0.72mm pinion.

**The winding train is module 0.12, not 0.23.** Every diameter on the page fits
both readings, because halving a tooth count and doubling the module leaves the
diameter unchanged -- which is exactly why the single tooth count that resolved
on the scan could not settle it. The pinions settle it:

| Part | Measured | at m 0.12 | at m 0.23 |
| --- | --- | --- | --- |
| Crown wheel | 6.41 | 51 t | 26 t |
| Ratchet wheel | 7.54 | 61 t | 31 t |
| Driving wheel ring | 5.87 | 47 t | 24 t |
| Driving wheel pinion | 1.43 | **10 t** | **4 t** |
| Reduction ring | 4.99 | 40 t | 20 t |
| Reduction pinion | 1.16 | **8 t** | **3 t** |
| Winding pinion | 1.55 | 11 t | 5 t |

Pinions are not cut below six leaves, so the module 0.23 column is not a real
gear train. The earlier 26-tooth count for the crown wheel was an aliasing
artefact: at 150 ppi a 51-tooth wheel of that size is about three pixels per
tooth, right at the sampling limit, and reading every other tooth is what a
moire produces.

Two independent checks agree. The automatic chain closes at **34.8 turns of the
weight per ratchet turn**, the right order for a calibre this size. And solving
the crown wheel's position from the barrel axis and the plate edge alone puts
the winding pinion **0.061mm** from the centre of the slot ETA actually cut,
against 0.14mm on the old module -- the solve is told nothing about the slot.

A caution this exercise also produced: **diameters below about 1mm are not
trustworthy on this scan.** The escape wheel's pinion measures 0.90, and no
integer tooth pair reproduces that against the measured 3.599 centre distance
and 7.00 wheel. Drawn line weight adds roughly 0.2 to 0.4mm to a feature only a
few pixels across, so small diameters are upper bounds, not dimensions.

### Assembly-order pages, and one correction they force

The technical communication's "Ordre d'assemblage" pages (8, 10, 12, 14, 16)
show each subsystem's parts in the order they are fitted, which is a second
independent read on the same geometry. Page 16, the self-winding mechanism, is
the one that changed the model.

**Position 31-2 is not a plain ball bearing.** It is drawn there as a bearing
with the rotor's gear ring cut around its outer race, teeth all the way round,
and the oscillating weight 31-1 Var drops onto it with a plain central bore. So
the 5.61mm measured for 31-2 on the materials page is that ring's tooth circle,
and the races are inside it -- the opposite of how this model first read it,
which had a bearing larger than the ring's own bore and no ring body at all.

5.61mm over the teeth on module 0.12 is 45 teeth, pitch radius 2.700. That
changes the automatic ratio from 28.45 to **32.24 turns of the weight per
ratchet turn**, and moves the reversing wheels in to a 4.860 centre distance
from the rotor axis.

The page also gives the fitting order for the module: framework 25 Var, then
the driving wheel 26, the two reversing wheels 27 and 28, the reduction wheel
29, the lower bridge 30, and last the weight on its bearing. Positions 27 and
28 carry the "do not lubricate" mark, which is the expected call-out for
reversing wheels with internal pawls and confirms which two they are.

That order puts the reduction wheel above the reversing wheels, where this
model has it below them. The model's stacking is not arbitrary -- at these
tooth counts the reduction wheel's pinion would have to pass the reversing
wheels' rims on its way down, and it is 1.19mm too big to do so -- but the
difference is recorded here rather than papered over. Resolving it needs the
reduction pinion and driving wheel re-derived onto a finer module, which is
tracked in ERRORS.md.

### What this changes

The crown wheel resolved its own tooth count: 26 teeth at 6.29mm outside
diameter gives module 0.23, not the 0.100 this model had been using for the
winding train. That one correction cascades:

- Crown wheel pitch radius 2.990, tip 3.220, root 2.700.
- Ratchet wheel on the same module at 7.40 outside diameter is 31 teeth, pitch
  radius 3.565. The model's earlier 63 teeth on module 0.100 is not supported.
- Crown-to-ratchet centre distance 6.555.
- Winding pinion at 1.45-1.60 outside diameter is 5 teeth on module 0.23,
  pitch radius 0.575, tip radius 0.805.

The crown wheel being modelled 2.5x too small is why the winding pinion could
not reach it, and why that interface was recorded as unresolved in `ERRORS.md`.
At 6.29mm the geometry closes.

Parts materially undersized in the model before this measurement:

| Part | Modelled | Drawing-scaled | Error |
| --- | --- | --- | --- |
| Barrel (14) | 7.60 dia | 12.29 | -38% |
| Crown wheel (19) | 2.60 dia | 6.29 | -59% |
| Ratchet wheel (20) | 6.50 dia | 7.40 | -12% |
| Balance (23) | 9.40 dia | 10.50 | -10% |
| Automatic driving wheel (26) | 4.20 dia | 5.86 | -28% |
| Oscillating weight (31) | 24.40 dia | 24.92 | -2% |

The barrel is the consequential one. At 12.29mm diameter it cannot sit at the
model's current barrel centre without leaving the plate, so the barrel centre,
the going-train layout that was solved against it, and the bridges that span it
all have to be re-derived. That work is tracked in `ERRORS.md`.

## Measured plate layout from the ETA materials page

Added 2026-09-05, and this supersedes the numerically solved layout that the
model used up to this point.

Position `1 Var` on the materials page is not a stylised icon: it is an
orthographic view of the main plate from the train side, drawn at exactly
25.60mm across, with the jewels coloured. Bearing centres can therefore be
measured directly off it rather than solved from assumed tooth counts.

Method. Segment the red jewel fill and the dark shock settings into connected
components, take each component's centroid, and scale by the same 25.60mm
calibration used for the dimension table. The keyless slot is found the same
way from the white through-openings. Reproduce with
`tools/measure_plate_layout.py`.

Orientation. The keyless slot breaks the plate rim at the top of the drawn
view, so drawn-up is the movement's +X, the 3 o'clock stem direction. Rotating
the view clockwise a quarter turn puts it in the project frame with no mirror;
the check that this is the correct handedness rather than its mirror is the
balance, which lands at 7-8 o'clock as it does on the real calibre. The
measured slot centre sits on y = 0.012mm, which is an
independent confirmation that the stem axis is the +X axis.

### Bearing centres, project frame

| Feature | X | Y | Radius from centre |
| --- | --- | --- | --- |
| Centre / fourth wheel, sweep seconds | +0.000 | +0.000 | 0.00 |
| Barrel arbor | +2.834 | +5.705 | 6.37 |
| Second (great) wheel | -4.075 | +5.957 | 7.22 |
| Third wheel | -2.738 | +2.473 | 3.69 |
| Escape wheel | -2.979 | -2.020 | 3.60 |
| Pallet fork | -1.303 | -4.219 | 4.42 |
| Balance staff | -2.388 | -6.567 | 6.99 |
| Unidentified sixth plate jewel | -6.135 | +0.803 | 6.19 |
| Keyless slot centre | +8.963 | +0.012 | - |

The keyless slot measures 4.79 along X by 2.66 along Y, so it runs from
X = 6.57 to X = 11.36 and opens through the plate rim. It is a **through-slot,
not a blind pocket** -- which is the direct confirmation of the winding-pinion
architecture: the pinion straddles the plate and stands proud on the train
side, where the crown wheel meets it.

The sixth jewel is recorded because it is there, not because it is understood.
It is 3.79 from the third wheel and 5.56 from the second, which is the right
order for a minute-train pivot in an indirect-seconds movement, but nothing in
the available evidence names it. It is not part of the going train.

### The going train closes on the measured centres

Measured centre distances against the tooth counts that satisfy 28,800 vph and
a one-hour second wheel:

| Mesh | Teeth | Measured C | C from teeth | Delta |
| --- | --- | --- | --- | --- |
| Barrel great wheel -> second pinion | 74 / 12 | 6.914 | 6.953 | 0.039 |
| Second wheel -> third pinion | 64 / 8 | 3.732 | 3.802 | 0.070 |
| Third wheel -> fourth pinion | 75 / 10 | 3.689 | 3.744 | 0.055 |
| Fourth wheel -> escape pinion | 96 / 6 | 3.599 | 3.652 | 0.053 |
| Escape wheel -> pallet | - | 2.765 | - | - |
| Pallet -> balance staff | - | 2.587 | - | - |

Every delta is inside the +/-0.1mm the 150 ppi scan supports. Two independent
routes -- diameters measured off the page, and tooth counts required by the
beat rate -- agree across four meshes, which is the strongest evidence this
model has for any part of its geometry.

Rates that follow:

- Fourth wheel at the centre: 1 turn per minute, carrying the sweep seconds.
- Escape wheel: 16 turns per minute; 15 teeth gives 480 beats per minute,
  **28,800 A/h**.
- Third wheel: 1 turn per 7.5 minutes.
- Second wheel: **1 turn per hour**, which is what lets the indirect minute
  train drive the cannon pinion 1:1.
- Barrel: 1 turn per 6.17 hours, so about **39 hours** at the 6.3 usable turns
  a mainspring of this height gives -- against ETA's published 38 hours.

The modules are then set by the measured centre distances rather than chosen:
0.1611 barrel to second, 0.1038 second to third, 0.0870 third to fourth,
0.0714 fourth to escape. Tip diameters computed from those modules land within
0.12mm of the diameters measured independently off the same page.

### Winding train placement

> Updated 2026-09-06 to the resolved winding train. The module-0.23 solve
> recorded here was correct all along; it was overturned in error on 2026-09-05
> and is now restored with the tooth counts that go with it.

The crown wheel sits on a circle about the barrel axis at the centre distance
its mesh requires, at the position whose pitch circle crosses the stem axis
inside the measured keyless slot while clearing every other wheel.

| | old (module 0.23 solve, 2026-09-05) | resolved (2026-09-06) |
|---|---|---|
| crown-to-barrel centre distance | 6.555 | **6.608** |
| crown wheel centre | (+8.788, +2.990) | to be re-solved on 6.608 |
| winding-pinion mesh on the stem axis | X = +8.799 | to be re-solved |
| offset from the centre of the slot ETA cut | 0.16 | to be re-checked |

The slot was measured independently and nothing in the solve was told about it,
so that offset remains the check on the whole placement.

Plan clearances recorded from the old solve, from the crown wheel's 3.220 tip
circle: 2.56 to the centre wheel, 5.00 to the third, 6.28 to the balance, and
0.30 to the plate edge. These move slightly with the re-solve; the tip circle
becomes 3.218 at the resolved module, so they change in the fourth decimal.

## CAD visualization colors

These colors identify mechanisms in the CAD assembly; they do not assert the
parts' real material, plating, lubricant, or finish. They use opaque sRGB because
Cade `rgb` has no alpha channel. Related parts share a color family, while parts
that touch or overlap use alternating shades. Position identifiers—not color—
remain the authoritative identity.

| Position | Part | Color | Hex | Cade value |
|---:|---|---|---|---|
| 1 | Main plate, assembled | Cool gray | `#9CA3AF` | `rgb(r = 156, g = 163, b = 175)` |
| 1-1 | Dial fastener | Light gray | `#D1D5DB` | `rgb(r = 209, g = 213, b = 219)` |
| 1-2 | Bottom balance shock absorber | Slate | `#64748B` | `rgb(r = 100, g = 116, b = 139)` |
| 2 | Sliding pinion | Blue | `#2563EB` | `rgb(r = 37, g = 99, b = 235)` |
| 3 | Winding pinion | Light blue | `#60A5FA` | `rgb(r = 96, g = 165, b = 250)` |
| 4 | Winding stem | Navy | `#1E3A8A` | `rgb(r = 30, g = 58, b = 138)` |
| 5 | Corrector lever | Sky | `#0EA5E9` | `rgb(r = 14, g = 165, b = 233)` |
| 6 | Setting lever, assembled | Blue | `#3B82F6` | `rgb(r = 59, g = 130, b = 246)` |
| 7 | Yoke | Cyan-blue | `#0284C7` | `rgb(r = 2, g = 132, b = 199)` |
| 8 | Setting lever jumper | Pale blue | `#93C5FD` | `rgb(r = 147, g = 197, b = 253)` |
| 9 | Escape wheel | Yellow | `#EAB308` | `rgb(r = 234, g = 179, b = 8)` |
| 10 | Intermediate wheel | Gold | `#D4A72C` | `rgb(r = 212, g = 167, b = 44)` |
| 11 | Third wheel | Amber | `#F59E0B` | `rgb(r = 245, g = 158, b = 11)` |
| 12 | Second wheel | Pale gold | `#FACC15` | `rgb(r = 250, g = 204, b = 21)` |
| 13 | Train wheel bridge | Ochre | `#A16207` | `rgb(r = 161, g = 98, b = 7)` |
| 14 | Movement barrel | Bronze | `#B7791F` | `rgb(r = 183, g = 121, b = 31)` |
| 15 | Stop lever | Light brown | `#D6A15D` | `rgb(r = 214, g = 161, b = 93)` |
| 16 | Barrel bridge | Dark bronze | `#92400E` | `rgb(r = 146, g = 64, b = 14)` |
| 17 | Click | Orange | `#EA580C` | `rgb(r = 234, g = 88, b = 12)` |
| 18 | Click spring | Light orange | `#FB923C` | `rgb(r = 251, g = 146, b = 60)` |
| 19 | Crown wheel | Copper | `#C2410C` | `rgb(r = 194, g = 65, b = 12)` |
| 20 | Ratchet wheel | Tan | `#CA8A04` | `rgb(r = 202, g = 138, b = 4)` |
| 21 | Pallet fork | Red | `#DC2626` | `rgb(r = 220, g = 38, b = 38)` |
| 22 | Pallet bridge | Rose | `#FB7185` | `rgb(r = 251, g = 113, b = 133)` |
| 23 | Timed balance | Magenta | `#C026D3` | `rgb(r = 192, g = 38, b = 211)` |
| 24 | Balance bridge, assembled | Purple | `#9333EA` | `rgb(r = 147, g = 51, b = 234)` |
| 24-1 | Balance bridge | Violet | `#7C3AED` | `rgb(r = 124, g = 58, b = 237)` |
| 24-2 | Stud support | Light violet | `#A78BFA` | `rgb(r = 167, g = 139, b = 250)` |
| 24-3 | Lower index | Pink | `#DB2777` | `rgb(r = 219, g = 39, b = 119)` |
| 24-4 | Upper index | Light pink | `#F472B6` | `rgb(r = 244, g = 114, b = 182)` |
| 24-5 | Regulator corrector | Deep purple | `#6D28D9` | `rgb(r = 109, g = 40, b = 217)` |
| 24-6 | Top balance shock absorber | Lavender | `#C4B5FD` | `rgb(r = 196, g = 181, b = 253)` |
| 25 | Automatic device framework | Green | `#16A34A` | `rgb(r = 22, g = 163, b = 74)` |
| 26 | Ratchet wheel driving wheel | Lime green | `#65A30D` | `rgb(r = 101, g = 163, b = 13)` |
| 27 | Auxiliary reversing wheel | Teal green | `#059669` | `rgb(r = 5, g = 150, b = 105)` |
| 28 | Reversing wheel | Light green | `#4ADE80` | `rgb(r = 74, g = 222, b = 128)` |
| 29 | Reduction wheel | Emerald | `#10B981` | `rgb(r = 16, g = 185, b = 129)` |
| 30 | Automatic lower bridge | Dark green | `#166534` | `rgb(r = 22, g = 101, b = 52)` |
| 31 | Oscillating weight, assembled | Forest | `#15803D` | `rgb(r = 21, g = 128, b = 61)` |
| 31-1 | Oscillating weight | Green | `#22C55E` | `rgb(r = 34, g = 197, b = 94)` |
| 31-2 | Ball bearing | Mint | `#6EE7B7` | `rgb(r = 110, g = 231, b = 183)` |
| 32 | Setting wheel | Cyan | `#0891B2` | `rgb(r = 8, g = 145, b = 178)` |
| 33 | Cannon pinion | Deep cyan | `#0E7490` | `rgb(r = 14, g = 116, b = 144)` |
| 34 | Minute wheel | Light cyan | `#22D3EE` | `rgb(r = 34, g = 211, b = 238)` |
| 35 | Date corrector | Turquoise | `#0D9488` | `rgb(r = 13, g = 148, b = 136)` |
| 36 | Date indicator | Pale cyan | `#67E8F9` | `rgb(r = 103, g = 232, b = 249)` |
| 37 | Hour wheel | Dark teal | `#115E59` | `rgb(r = 17, g = 94, b = 89)` |
| 38 | Date indicator driving wheel | Aqua | `#14B8A6` | `rgb(r = 20, g = 184, b = 166)` |
| 39 | Minute train bridge | Blue teal | `#155E75` | `rgb(r = 21, g = 94, b = 117)` |
| 40 | Date jumper | Bright cyan | `#06B6D4` | `rgb(r = 6, g = 182, b = 212)` |
| 41 | Date jumper maintaining plate | Pale teal | `#5EEAD4` | `rgb(r = 94, g = 234, b = 212)` |
| 42 | Dial support | Indigo | `#4F46E5` | `rgb(r = 79, g = 70, b = 229)` |
| 43 | Key-bolt | Light indigo | `#818CF8` | `rgb(r = 129, g = 140, b = 248)` |
| 900 | Countersunk screw class | Charcoal | `#374151` | `rgb(r = 55, g = 65, b = 81)` |
| 901 | Bridge screw class | Dark gray | `#4B5563` | `rgb(r = 75, g = 85, b = 99)` |
| 902 | Crown-wheel screw | Medium gray | `#6B7280` | `rgb(r = 107, g = 114, b = 128)` |
| 903 | Ratchet-wheel screw | Blue gray | `#475569` | `rgb(r = 71, g = 85, b = 105)` |
| 904 | Automatic-framework screw class | Graphite | `#52525B` | `rgb(r = 82, g = 82, b = 91)` |
| 905 | Automatic-lower-bridge screw | Slate gray | `#64748B` | `rgb(r = 100, g = 116, b = 139)` |
| 906 | Oscillating-weight screw | Steel gray | `#71717A` | `rgb(r = 113, g = 113, b = 122)` |
| 907 | Minute-train-bridge screw | Light steel | `#94A3B8` | `rgb(r = 148, g = 163, b = 184)` |

When one definition is reused, keep one color for every placement. Cade stores
color on the definition for 3MF output and refuses placing the same definition
in two colors. If two visually identical pieces need different diagnostic
colors, give them distinct part definitions and document why.

## Logical assembly of assemblies

This hierarchy follows function and ETA's service order. It is not a claim that
every item can be installed as a preassembled physical module. In CAD, the leaf
parts remain distinct definitions and each subsystem is an assembly of placed
leaves.

```text
eta_2824_2
├── main_plate_assembly
│   ├── main_plate [1]
│   ├── dial_fastener [1-1]
│   └── lower_balance_shock_absorber [1-2]
├── hand_setting_assembly
│   ├── sliding_pinion [2]
│   ├── winding_pinion [3]
│   ├── winding_stem [4]
│   ├── corrector_lever [5]
│   ├── setting_lever [6]
│   ├── yoke [7]
│   ├── setting_lever_jumper [8]
│   └── screws_900
├── going_train_assembly
│   ├── escape_wheel [9]
│   ├── intermediate_wheel [10]
│   ├── third_wheel [11]
│   ├── second_wheel [12]
│   ├── train_wheel_bridge [13]
│   └── screws_901
├── barrel_and_winding_assembly
│   ├── movement_barrel [14]
│   ├── stop_lever [15]
│   ├── barrel_bridge [16]
│   ├── click [17]
│   ├── click_spring [18]
│   ├── crown_wheel [19]
│   ├── ratchet_wheel [20]
│   └── screws_901_902_903
├── escapement_assembly
│   ├── pallet_fork [21]
│   ├── pallet_bridge [22]
│   └── screws_901
├── balance_assembly
│   ├── timed_balance [23]
│   ├── balance_bridge_assembly [24]
│   │   ├── balance_bridge [24-1]
│   │   ├── stud_support [24-2]
│   │   ├── lower_index [24-3]
│   │   ├── upper_index [24-4]
│   │   ├── regulator_corrector [24-5]
│   │   └── upper_balance_shock_absorber [24-6]
│   └── screws_901
├── automatic_winding_assembly
│   ├── automatic_framework [25]
│   ├── ratchet_wheel_driving_wheel [26]
│   ├── auxiliary_reversing_wheel [27]
│   ├── reversing_wheel [28]
│   ├── reduction_wheel [29]
│   ├── automatic_lower_bridge [30]
│   ├── rotor_assembly [31]
│   │   ├── oscillating_weight [31-1]
│   │   └── ball_bearing [31-2]
│   └── screws_904_905_906
└── dial_side_assembly
    ├── motion_works
    │   ├── setting_wheel [32]
    │   ├── cannon_pinion [33]
    │   └── minute_wheel [34]
    ├── calendar_works
    │   ├── date_corrector [35]
    │   ├── date_indicator [36]
    │   ├── hour_wheel [37]
    │   ├── date_indicator_driving_wheel [38]
    │   ├── minute_train_bridge [39]
    │   ├── date_jumper [40]
    │   └── date_jumper_maintaining_plate [41]
    ├── dial_support [42]
    ├── key_bolt [43]
    └── screws_900_907
```

## Cade organization

Use one definition per manufactured part and one file per stable subsystem.
Until measured geometry exists, do not create visually plausible proxy gears
under production names; use an `_envelope` or `_placeholder` suffix so they
cannot be mistaken for verified parts.

```text
eta_2824-2/
├── main_plate.cade
├── hand_setting.cade
├── going_train.cade
├── barrel_and_winding.cade
├── escapement.cade
├── balance.cade
├── automatic_winding.cade
├── dial_side.cade
├── fasteners.cade
└── movement.cade
```

The final Tier 1 shape should follow this pattern once leaf definitions and
frames are measured:

```cade
import "./main_plate.cade" as plate
import "./hand_setting.cade" as setting
import "./going_train.cade" as train
import "./barrel_and_winding.cade" as barrel
import "./escapement.cade" as escapement
import "./balance.cade" as balance
import "./automatic_winding.cade" as automatic
import "./dial_side.cade" as dial

part eta_2824_2() -> Assembly {
  together(
    plate.main() |> place(),
    setting.main() |> place(),
    train.main() |> place(),
    barrel.main() |> place(),
    escapement.main() |> place(),
    balance.main() |> place(),
    automatic.main() |> place(),
    dial.main() |> place(),
  )
}
```

That snippet expresses logical composition only. It will compile after each
imported module exists and supplies a `main() -> Assembly`; it does not establish
any placement without measured frames.

## Measurement backlog

Record every acquired dimension with source, specimen/variant, tool, resolution,
uncertainty, reference temperature, datum, and date. Highest-value interfaces:

1. Main-plate casing seat, flange, and clamp geometry.
2. Stem axis height and radial location in every crown position.
3. Dial seat, dial feet, date window, and dial support heights.
4. Hour, minute, and seconds hand-fitting diameters and axial stack.
5. Rotor swept volume and caseback clearance.
6. Jewel/pivot centers and axial levels for the going train.
7. Bridge locating features, screw axes, and bearing surfaces.
8. Wheel pitch geometry, tooth counts, backlash, and endshake.

Items 6 and 8 are now partly served by the drawing-scaled table above and by the
photographic and documentary work of 2026-09-06. Outside diameters and overall
heights are measured for the whole calibre; the **winding train is fully
resolved** (winding pinion 12, crown wheel 26, ratchet wheel 63 on alternate
teeth, modules 0.2298 and 0.1149); and the plate view gives measured bearing
centres. Still open: every going-train and automatic-train tooth count, the
escape wheel count (15 or 20 - see the note under the resolved winding train),
and every axial level. Pitch geometry below module 0.15 and
every axial level still need a real measurement or a dimensioned drawing.

## Source quality notes

- The ETA technical communication is authoritative for identity, parts list,
  service order, lubrication, and the few published movement-level values.
- The Boley catalogue is useful for cross-reference and purchasing information.
- The Time Connection listing is useful for legacy part names and the stem
  thread lead, but explicitly says its pictures are for reference only.
- [`references/parts/assembly.jpg`](references/parts/assembly.jpg) is explicitly
  labeled ETA 2836-2. It may corroborate the order and identity of base-movement
  and automatic-winding parts shared with the 2824 family, but it is not a
  dimensional source and cannot establish ETA 2824-2 tooth counts.

---

# Photographs of the movement itself (2026-09-06)

The project lead disassembled and reassembled a 2824-2 and photographed every
step, roughly 290 images in two sets with his own written index for each. These
are the first primary source in the project that is not a drawing: a drawing
can be mis-scaled or aliased, a part lying on a bench mat cannot.

The photographs are the project lead's own and are **not** in this repository.
Nothing below reproduces them; each finding cites the image by its file name in
his set so the measurement can be repeated.

Evidence class for everything in this section: **photo_measured** - a count or a
ratio read off a photograph of the part itself. It outranks `drawing_scaled`
for tooth counts, because a count is discrete and either right or wrong, and
ranks below it for dimensions, because these photographs carry no scale bar.

## Crown wheel tooth count from photographs

Four counts on three different photographs:

| image | what it shows | method | teeth |
|---|---|---|---|
| `IMG_9577.JPG` | crown wheel isolated on a bench mat | refined polar fit, score 0.209 | **26** |
| `B (018).JPG` | crown wheel installed, near face-on | refined polar fit, score 0.090 | 25 |
| `IMG_9576.JPG` | crown wheel installed, screw removed | refined polar fit, score 0.096 | 24 |
| `B (017).JPG` | crown wheel isolated, oblique | refined polar fit, score 0.149 | 24 |

The first row is the one to trust. The wheel is isolated, unoccluded and lit
against a plain mat, the fit score is more than twice any of the others, and the
recovered spectrum has clean harmonics at 53 and 78 - two and three times the
fundamental - which a wrong fundamental does not produce. The three lower counts
all come from views where part of the rim is occluded or blown out, and an
occluded tooth is a missed tooth, so they are biased low by exactly the amount
seen.

**26 teeth.** That is the number the page-6 elevation gave, and which this
project overruled as a moire artefact. The photograph vindicates the drawing.

`IMG_9577.JPG` also settles a structural question: the crown wheel is a flat
steel annulus of one thickness with **one** toothing. There is no second, finer
toothing on its underside.

With the measured 6.29-6.41 outside diameter, 26 teeth put the winding module at

    m = 6.35 / (26 + 2) = 0.227

not the 0.12 currently in `datums.cade`. See `ERRORS.md`, E9.

## Ratchet wheel toothing, unresolved

> **SUPERSEDED 2026-09-06.** Resolved in *The winding train, resolved* at the end
> of this document: 63 teeth, engaged by the crown wheel on alternate teeth. The
> section below is kept because it records the measurements, which were right,
> and the inference, which was wrong.

`B (021).JPG` shows the ratchet wheel isolated, nearly face-on, with its screw
resting on it. The same refined polar fit puts its peripheral toothing at
**58-61** teeth (best score 0.133 at 58, contour method 61, and an independent
check from tooth depth against mean radius gives 59). The screw head measures
about a fifth of the wheel's width, which at a 1.4-1.5 mm screw head puts the
wheel at 7.0-7.5 mm - agreeing with the drawing's 7.40-7.54 and confirming the
part's identity.

58-61 teeth on 7.47 mm is module 0.12. The crown wheel is module 0.227. Two
wheels of different pitch cannot mesh, and `B (022).JPG` - the only photograph
with both wheels installed - confirms by eye that the crown wheel's teeth are
about twice the ratchet's.

The teeth themselves say the same thing. The crown wheel's are deep, hooked
wolf teeth, the form used to transmit winding torque. The ratchet wheel's are
shallow, fine and asymmetric - the form used to hold a click. They are not the
same kind of tooth doing the same job.

So the winding drive between them is not the single spur mesh this model has.
This is recorded as open rather than guessed at.

**The photograph that would settle it does not exist in the set**: the barrel
bridge from directly above with the crown wheel *and* the ratchet wheel both
installed. In the assembly sequence the crown wheel goes on at `B (017)`-`B
(020)` and the ratchet at `B (021)`, so `B (022)` is the only frame with both,
and it is a low oblique with the mesh out of focus. In the disassembly sequence
the ratchet was already off before `IMG_9573`.

## Barrel bridge bearing - no jewel

`B (009).JPG` shows the barrel bridge alone, lit from above. The barrel arbor's
upper bearing is a plain brass hole with a turned countersunk oil sink; there is
no jewel anywhere on the part. `B (013).jpg` annotates that same bearing, and
two others on the bridge, with **Moebius HP-1300** - a thick oil. A thick oil is
what a slow, heavily loaded plain bearing gets; a jewelled train bearing gets a
thin oil and never HP-1300.

The barrel arbor turns once per six hours under full mainspring torque, which is
the textbook case for a plain bearing rather than a jewel. The model's
`eta_pos_16_barrel_bridge_jewel` has been removed. The main plate's lower barrel
jewel, which is evidenced, stays.

The same photograph shows the crown wheel's seat as a two-diameter boss turned
into the bridge - a larger lower cylinder with a smaller upper step and a
central screw hole.

## Crown wheel and ratchet wheel do not mesh directly

> **WRONG, AND SUPERSEDED 2026-09-06.** They do mesh. The crown wheel's circular
> pitch is twice the ratchet wheel's *by design* and its teeth drop into
> alternate spaces, so the 1.84 pitch ratio measured below is a correct reading
> of a 2:1 construction rather than proof that a member is missing. See *The
> winding train, resolved*. Kept as the record of a measurement that was sound
> and an inference that was not.

A frame from the TrendWatchLab teardown (youtu.be/IhBtUBl3Chs), taken with the
automatic module lifted off and the movement flat to the camera, puts both
wheels in one image at one scale and in one focal plane. The same refined polar
fit applied to each is therefore directly comparable, which no still in either
photograph set allows:

| wheel | fit score | tip radius (px) | teeth | circular pitch (px) |
|---|---:|---:|---:|---:|
| ratchet | 0.056 | 467 | 63 (cluster 61-65) | 46.6 |
| crown | 0.135 | 341 | 25, second harmonic present at 49-50 | 85.7 |

The crown wheel's circular pitch is **1.84 times** the ratchet wheel's. Wheels of
different pitch cannot mesh. The same fit puts the centre distance at 875 px
against a tip-radius sum of 808, leaving the tooth circles roughly 0.9 mm apart;
the centres there are eyeballed rather than fitted, so that is the weaker of the
two observations, but it agrees.

Three independent measurements now say the same thing - this frame, `B (022)`,
and the pair `B (018)`/`B (021)` - and the tooth forms agree with them. The
crown wheel's teeth are deep hooked wolf teeth, the form that transmits winding
torque. The ratchet wheel's are shallow, fine and asymmetric, the form that
holds a click.

`IMG_9577.JPG` rules out the crown wheel as the place a second toothing could
hide: it is a flat annulus of one thickness with one toothing. So the member
that carries hand-winding torque from the crown wheel to the barrel arbor is
either a second, coarser toothing on the **underside** of the ratchet wheel, or
a separate intermediate wheel. Either way it is a part with two diameters on two
levels - the pattern the project lead noticed across this movement, and which
already corrected the automatic train earlier in the reconstruction.

This is a topology question, not a counting question, and the model will not be
rebuilt until it is answered. What answers it: one photograph of the ratchet
wheel's **underside**, off the movement.

## The ETA parts chart: a fifth confirmation, and one branch closed

> **PARTLY SUPERSEDED 2026-09-06.** The observation stands - the chart does draw
> the two wheels at nearly the same diameter with very different tooth counts -
> but the conclusion drawn from it does not. That is what a 2:1 alternate-tooth
> engagement looks like, not evidence of a missing part. The chart's numbering
> running straight from 19 to 20 with nothing between them is now a *positive*
> result: there is no intermediate because none is needed.

The project lead supplied a dealer's ETA 2824-2 parts chart - a line drawing of
every component, keyed to the same Pos. numbers as the technical communication.
It is third-party artwork and is not in this repository. It is an illustration,
not a dimensioned drawing, so nothing here is promoted above `photo_estimate`.
Two things in it are still worth having.

**It draws the two wheels side by side, and they disagree the same way.** Pos 19
is a thin annulus with a large central bore and a small number of coarse,
hooked teeth. Pos 20 is a solid disc with a **square** central hole - the barrel
arbor square - and a large number of fine teeth. The two are drawn at almost the
same outside diameter. Same diameter, roughly two and a half times the tooth
count: different modules, drawn by ETA's own illustrator.

Checking the chart's scale against known parts confirms it is drawn roughly to
scale rather than cell-by-cell: taking the main plate at 25.60 mm gives the
barrel 12.8 (published 12.29), the second wheel 7.0, Pos 19 about 6.9 and Pos 20
about 7.2 - both within the drawing-scaled measurements already in this
document.

**It closes the "separate intermediate wheel" branch.** The chart runs 1, 1-1,
1-2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
23, 24 with sub-numbers, 25, 26, 27, 28, 29, 30, 31-1, 31-2. **Nothing sits
between 19 and 20**, and no part anywhere in it looks like a small two-level
winding intermediate. The base movement has no such component.

Combined with `IMG_9577.JPG`, which shows the crown wheel is a flat annulus of
one thickness with one toothing, that leaves one place for the missing toothing
to be: **the underside of the ratchet wheel, Pos 20**. The chart draws Pos 20
from above only, so it cannot confirm or deny it.

The prediction is therefore specific and falsifiable: the ratchet wheel carries a
second, coarser toothing on its underside, of the crown wheel's module (about
0.23), with roughly 31 teeth - the count that satisfies the measured 6.72 mm
centre distance against the crown wheel's 26. One photograph of that wheel
turned over confirms or kills it.

## Part-number cross-reference, and what the trade listings do not contain

Dealer listings supplied by the project lead pin the two numbering systems
together. One lists the ratchet wheel as **part 415** with **"Article Number:
20"** - the classical Swiss number and ETA's Pos. number for the same component,
stated side by side. With the parts plate drawing 415 as the square-holed
fine-toothed disc and 420 as the coarse-toothed annulus, the mapping is:

| classical | ETA Pos. | part |
|---|---|---|
| 415 | 20 | ratchet wheel |
| 420 | 19 | crown wheel |

**None of these listings gives a dimension for either wheel.** Every millimetre
figure on them - 25.6, 26.00, 4.60 - is the *movement*: 11.5 lignes is 25.6 mm,
which is the number this project has calibrated on since the first page-6
measurement. A listing that says a ratchet wheel "is designed for a movement
with a total diameter of 25.6 mm" is describing the calibre, not the part, and
reading it as a part dimension would silently corrupt the whole winding train.
Recorded here because it is an easy misread and the numbers look authoritative.

Searched without success for a published crown-wheel diameter or a winding-train
tooth count: the Ranfft caliber database, 17jewels.info, watch-spare, and
several parts dealers. All carry movement-level data only. Ranfft's 2824 entry
gives 11.5 lignes, 26 mm, 4.6 mm height, 25 jewels, 28,800 A/h, 53 degrees lift,
and no gear train at all.

One claim seen in passing: 17jewels.info states the escape wheel "has got 20
teeth". **An earlier note here rejected that on the grounds that 20 teeth would
not give the fourth wheel one turn per minute. That rejection was wrong** and is
withdrawn. Both counts close against 28,800 A/h, with different intermediates:

    15 teeth at 960 escape rev/h  ->  960 x 15 x 2 = 28,800   (the model's train)
    20 teeth at 720 escape rev/h  ->  720 x 20 x 2 = 28,800   (this document's
                                       2026-09-05 derived train, fourth 84 /
                                       escape pinion 7 gives 60 rev/h = 1 rev/min)

The model uses 15, the standard Swiss count. The 17jewels figure is secondary
direct observation of a specimen. The two are not reconciled and the escape
wheel count is still open - it is in the measurement backlog.

**The crown wheel's outside diameter is not published anywhere reachable.** It
has to be measured off the part.

# THE WINDING TRAIN, RESOLVED (2026-09-06)

A 2013 watchuseek post by a watchmaker states the winding train outright:
*"The winding pinion has 12 teeth, the crown wheel has 26 (which only engage
every other tooth on the ratchet wheel) and the ratchet wheel has 63 teeth."*

**Every other tooth.** The crown wheel's circular pitch is twice the ratchet
wheel's by design, and its teeth drop into alternate spaces. That is why this
project spent four rounds hunting a member that does not exist: it applied "two
wheels of different pitch cannot mesh", which governs conventional involute
gearing and not a wolf-tooth winding drive.

## Why this is trusted

One person on a forum is not a source. This is adopted because it is
arithmetically self-confirming and because six independently measured quantities
agree with it.

The author separately states the crown must be turned 2.625 times per ratchet
revolution. From the three tooth counts alone:

    12/26 x 26/(63/2) = 0.380952 ...   1/0.380952 = 2.6250

exactly. Change any one count and it breaks.

| quantity | how this project got it | value | derived from the above |
|---|---|---|---|
| crown wheel teeth | `IMG_9577.JPG`, polar fit score 0.209, harmonics at 53 and 78 | 26 | 26 |
| ratchet wheel teeth | teardown frame, polar fit | 63 | 63 |
| crown : ratchet circular pitch | one frame, one scale | 1.84 | 2.00 |
| crown wheel outside diameter | page 6, drawing-scaled | 6.29 - 6.41 | 6.436 |
| ratchet wheel outside diameter | page 6, drawing-scaled | 7.40 - 7.54 | 7.470 (input) |
| crown-to-barrel centre distance | measured plate layout | 6.72 | 6.608 |

Evidence class: **derived**, resting on `drawing_scaled` diameters and
`photo_measured` counts, with the tooth counts themselves now confirmed three
ways.

## The resolved parameters

Taking the ratchet wheel's measured 7.47 outside diameter as the input:

| | teeth | module | pitch diameter | outside diameter |
|---|---:|---:|---:|---:|
| winding pinion | 12 | 0.2298 | 2.758 | - |
| crown wheel | 26 | 0.2298 | 5.976 | 6.436 |
| ratchet wheel | 63 | 0.1149 | 7.238 | 7.470 |

- The crown wheel engages the ratchet wheel on **alternate teeth**: effective 31.5.
- Crown-to-barrel centre distance **6.608**.
- Crown turns per ratchet turn **2.625**.
- The ratchet wheel's fine teeth are cut for the click; the crown wheel engages
  them two at a time. One toothing, two duties, two effective modules.

## Also from the same post, not yet adopted

Unverified, and recorded only as leads: barrel arbor nominal diameter 3.36;
mainspring 0.125 thick and a little over 400 long; barrel inside diameter about
11; six equidistant bridle notches in the barrel wall; about 22 arbor
revolutions for a full wind. The model currently carries a 12.29 barrel outside
diameter, so an 11 inside diameter is consistent with a 0.6 wall.

# Reading order, 2026-09-06

This document has grown by accretion across several sessions and now contains
superseded material on purpose - the project is the subject of a video, and how
a wrong answer was reached and corrected is part of the record. To read it for
current facts rather than for the history:

1. **Movement-level facts** and the **part ledger** - unchanged throughout, safe.
2. **Drawing-scaled dimensions from the ETA materials page** - the measured
   table, the stepped elevation profiles, the plate layout and bearing centres.
   Still the dimensional backbone.
3. **THE WINDING TRAIN, RESOLVED** at the end - the current answer for the crown
   wheel, ratchet wheel and winding pinion. Overrides everything earlier in the
   document on those three parts.
4. **Photographs of the movement itself** - the barrel bridge having no jewel,
   and the crown wheel's 26 teeth, both stand. The three sections carrying
   SUPERSEDED banners record measurements that were sound and an inference that
   was not; read them for method, not for facts.

The going train, the automatic train and every axial level are still
`expert_estimate` constrained by chains that close. Only the winding train, the
date indicator's 31 teeth and the drawing-scaled diameters are better than that.

## What is still unmeasured

- Every going-train tooth count. The escape wheel is 15 or 20 and unreconciled.
- Every automatic-train tooth count. One lead worth testing: a watchmaker's
  claim that ETA data sheets put a full automatic wind at 1250 rotor rotations.
  This model derives 34.8 rotor turns per ratchet turn, which puts a full wind
  near 260, so if 1250 is right the automatic reduction is out by nearly five
  times.
- Every axial level. The 3.35 base movement height is still an expert estimate
  and is the weakest input in the model.
- The crown wheel's position needs re-solving on the 6.608 centre distance.

# Which execution this model is of (2026-09-06)

**This reconstruction is of the 17-jewel execution.** The specimen in the
teardown is a Hamilton-cased ETA 2824-2 whose caseback reads *17 JEWELS*, and
its rotor is stamped *17 JEWELS SWISS MADE*. The ETA technical communication
this project has used throughout describes a **25-jewel** execution. Both are
the same calibre; ETA built it in several grades.

Recording it explicitly because the two disagree on exactly one thing, and
because leaving it implicit is how a model ends up half one movement and half
another.

## What the difference does and does not touch

A lower jewel count is jewels replaced by plain bearings at the lighter-loaded
pivots. It is not a different calibre, a different plate or a different train.
So almost everything already measured stands:

| Evidence | Still valid? | Why |
|---|---|---|
| Every `drawing_scaled` dimension off page 6 | **Yes** | Part envelopes are shared across executions |
| The measured plate layout and bearing centres | **Yes** | The holes are in the same places; some carry brass instead of ruby |
| Tooth counts, modules, centre distances | **Yes** | The gear trains are identical |
| 25.60 diameter, 4.60 height, 28,800 A/h, 50 degree lift, power reserve | **Yes** | Calibre-level, not execution-level |
| **Jewel count, and which bearings are jewelled** | **No** | This is the one thing that differs |

So the technical communication remains the primary source for identity, parts
list, service order, lubrication and dimensions. It is not the source for
jewels, and this document should not quote its 25 as though it described the
movement being modelled.

## How the jewel map gets built

Not by inference. A jewel is red and unmistakable in a photograph, and the
project lead's stills index has a frame for every part, so each one can simply
be looked at as the walkthrough reaches it. Two data points already:

- **Barrel bridge, position 16: no jewel.** Photographed alone it shows a plain
  brass countersunk oil sink at the barrel arbor, and the lubrication frame
  annotates that bearing with Moebius HP-1300, a thick oil - a plain-bearing
  lubricant. The model's jewel there was removed before this was understood as
  an execution difference; it now looks like the first instance of the pattern.
- **Automatic lower bridge, position 30: jewelled.** The flat frame of the
  module shows three red stones in the steel bridge. So the difference is *not*
  simply "the automatic module loses its jewels", and guessing which eight
  differ would be exactly the kind of inference this project has already been
  burned by twice.

The model currently places four jewel parts. Building the real map is a
walkthrough task, not a derivation.
