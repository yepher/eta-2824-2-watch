# Cade gaps discovered by the ETA 2824-2 watch project

This file is the persistent issue ledger for limitations or defects encountered
while modeling the watch in Cade. It is not a wishlist and it is not a ledger of
missing ETA dimensions. A model error becomes a Cade gap only after the current
documentation and compiler diagnostic have been checked.

## Status values

- `open`: reproduced against the current release binary.
- `needs confirmation`: evidence is incomplete or the minimal reproduction is
  not yet isolated.
- `intentional refusal`: Cade deliberately does not support the operation; record
  the documented reason and its impact on this model.
- `resolved`: fixed or documented sufficiently; retain the entry and validation.

## Open gaps

### GAP-2026-09-05-01 - Helical screw threads are metadata, not solid geometry

- **Status:** intentional refusal
- **Area:** syntax
- **Found while modeling:** ETA fastener positions 900-907
- **Cade revision:** unknown
- **Binary:** `$CADE`
- **Command:** `cade view watch.cade --part fastener_detail_preview --raymarch`
- **Expected:** Visible helical thread geometry on a completed screw model.
- **Actual:** Cade intentionally provides `thread(d, pitch, fit)` as manufacturing metadata and has no helix operator.
- **Impact:** Screw heads, collars, shoulders, shanks, and lead tips can be modeled, but true thread flanks cannot be rendered.
- **Workaround:** Add thread metadata after controlled diameter and pitch values are obtained; retain plain shank solids for the drawing representation.
- **Documentation checked:** `docs/AUTHORING.md` section 5, Threads.
- **Minimal reproduction:** Any screw placed with `thread(...)` retains a cylindrical solid shank; the thread callout is metadata.
- **Evidence:** The compiled `fastener_detail_preview` shows the modeled solid forms without a helix.
- **Resolution:** Intentional language behavior; no model-side fix.

### GAP-2026-09-04-01 - A qualified imported call is reported as recursion when the names match

- **Status:** open
- **Area:** type checking / diagnostics
- **Found while modeling:** top-level movement assembly
- **Cade revision:** unknown
- **Binary:** `$CADE`
- **Command:** `cade check watch.cade --part watch`
- **Expected:** An imported part resolves through its alias regardless of what
  the calling part is called.
- **Actual:** At `plate.main()` the compiler reports `` `main` calls itself: main -> main ``.
- **Impact:** No part may call an imported part of the same name, so a module
  cannot expose an entry under the name its caller would naturally use. First
  seen with `main`; re-hit on 2026-09-05 with
  `part datum_stack_preview() { datums.datum_stack_preview() }`, which is the
  same shape and has nothing to do with `main`. The trigger is name equality.
- **Workaround:** Give every subsystem assembly a unique entry name, such as
  `main_plate_assembly` and `going_train_assembly`, and rename the caller when
  it collides (`datum_budget_preview` calls `datums.datum_stack_preview()`).
- **Documentation checked:** `docs/AUTHORING.md` sections 5 and 7; working
  `test/assembly/` examples use unique imported part names.
- **Minimal reproduction:** One file exports `part main() -> Assembly`; a second
  imports it as `a` and calls `a.main()` from its own `part main()`.
- **Evidence:** Compiler diagnostic captured while checking the initial watch
  scaffold.
- **Resolution:** Pending.

### GAP-2026-09-05-04 - No whole-assembly interference check

- **Status:** open
- **Area:** evaluation / diagnostics
- **Found while modeling:** whole `watch` assembly, refinement-phase audit
- **Cade revision:** unknown
- **Binary:** release `cade` (`$CADE`)
- **Command:** `cade check`, `cade validate`, `cade view` on `--part watch`
- **Expected:** Some command that reports when two placed bodies of one
  assembly occupy the same volume, or a way to ask for it.
- **Actual:** Every command reports success. `check` and `validate` refuse an
  assembly and want `--part`; `view` renders it; an assembly deliberately has
  no total volume (`docs/AUTHORING.md` section 5), so there is no sum to
  compare against the parts either. An assembly with 52 interpenetrating pairs
  passes everything.
- **Impact:** The single most important correctness property of a mechanism -
  that no two manufactured bodies share a volume - is invisible to the tool.
  `CLAUDE.md` Phase 4 asks for it on every iteration.
- **Workaround:** `tools/interference.py` in this project. It flattens the
  assembly, finds pairs whose world bounds overlap, generates one
  `intersect(a, b)` diagnostic per pair and meshes each, so the volume still
  comes from Cade. 232 pairs on this model take about 45 seconds. This is the
  `docs/AUTHORING.md` section 9 technique, applied exhaustively rather than by
  hand.
- **Documentation checked:** `docs/AUTHORING.md` sections 5, 9; `docs/cli.md`
  `check`, `validate`, `mesh`.
- **Minimal reproduction:** two `place` calls of the same `cylinder(r = 1mm,
  h = 1mm)` at `x = 0mm` and `x = 0.5mm`; every command succeeds.
- **Evidence:** `tools/interference_report.json` and `ERRORS.md` in this
  project.
- **Resolution:** Pending. A `cade interference <file> --part <assembly>` that
  did the pairwise walk internally would remove roughly 200 lines of generated
  program per audit.

### GAP-2026-09-05-03 - Outward `offset` is refused when it would close a small internal void

- **Status:** open
- **Area:** evaluation
- **Found while modeling:** clearance probes between watch parts
- **Cade revision:** unknown
- **Binary:** release `cade` (`$CADE`)
- **Command:** `cade mesh a.cade --part grown`
- **Expected:** Growing a solid outward by 0.2 mm closes a 0.14 mm bore and
  returns the solid without the bore.
- **Actual:** `offset by -0.2mm consumes the cylinder it is applied to: its
  radius would be -0.06mm, which is not a solid`. The offset is distributed
  over the CSG tree, the subtracted cylinder receives the negative offset, and
  a void that shrinks past zero is refused instead of vanishing.
- **Impact:** Blocks the clearance-probe technique of `docs/AUTHORING.md`
  section 9 - `intersect(a, offset(b, d))` to bracket a gap - for any watch
  part with a jewel hole or pivot bore, which is most of them. Probe distances
  are capped at the part's smallest internal radius.
- **Workaround:** Probe with the simpler body of the pair, or bracket the gap
  analytically from centre distances. `tools/clearance.py` does the former and
  records which pairs it cannot answer.
- **Documentation checked:** `docs/AUTHORING.md` sections 3 (Booleans and
  rewrites), 9.
- **Minimal reproduction:**

```cade
part ring() -> Solid<Exact> {
  cut(cylinder(r = 0.5mm, h = 0.3mm), cylinder(r = 0.14mm, h = 0.5mm))
}
part grown() -> Solid<Exact> { offset(ring(), d = 0.2mm, corners = extended) }
```

- **Evidence:** Refusal reproduced with both `corners = extended` and
  `corners = round`.
- **Resolution:** Pending.
- **Related:** `corners = round` additionally refuses at the polar tooth
  vertices of every wheel in this model (`round refuses at the vertex ... no
  ball fits`), which is the documented v0.1 absence of a vertex blend rather
  than a separate defect, but it means `extended` - which moves a corner by
  `d * sqrt(2)` - is the only usable probe here, and its brackets are therefore
  lower bounds.

### GAP-2026-09-05-02 - `cade lower --part <name>` is ignored

- **Status:** open
- **Area:** diagnostics / CLI
- **Found while modeling:** inspecting the lowered form of the `watch` assembly
- **Cade revision:** unknown
- **Binary:** release `cade` (`$CADE`)
- **Command:** `cade lower a.cade --part ring -o /tmp/a.cade0`
- **Expected:** The usage line reads
  `cade lower <file.cade> [-o out.cade0] [--part <name>] [--canonical]`, so
  `--part` selects the part to lower.
- **Actual:** `this file has 4 parts, so a build has to name one`, followed by
  a help line listing the exact name that was passed. The flag is parsed by the
  usage text and by nothing else. Reproduced with `--part` before and after the
  file argument, and for both a `Solid` part and an `Assembly` part.
- **Impact:** The lowered form of a multi-part file cannot be inspected at all,
  which is the one documented way to see what a Tier 1 program actually means.
- **Workaround:** Copy the part into a single-part file.
- **Documentation checked:** `docs/cli.md` `lower`; `cade` usage output.
- **Minimal reproduction:** any `.cade` file with more than one `part`.
- **Evidence:** Same diagnostic from a four-part scratch file and from
  `watch.cade`.
- **Resolution:** Pending. Compare with `mesh`/`view`, where `--part` works.

### GAP-2026-09-05-05 - Two BOM positions with identical geometry become one product

- **Status:** needs confirmation
- **Area:** export / documentation
- **Found while modeling:** ETA positions 27 and 28 (reversing wheels), 1 and
  13 (jewels), 1-2 and 24-6 (shock absorbers)
- **Cade revision:** unknown
- **Binary:** release `cade` (`$CADE`)
- **Command:** `cade view watch.cade --part watch -o /tmp/watch.html`
- **Expected:** Positions that are separate line items in the ETA parts list
  stay separate in the output, since `CLAUDE.md` asks for one named part per
  physical component with its own BOM identity.
- **Actual:** Identical definitions are grouped by content hash
  (`docs/AUTHORING.md` section 5), so `eta_pos_28_reversing_wheel_envelope`
  reports `def: eta_pos_27_aux_reversing_wheel_envelope`. The placement keeps
  its own spelled name in the viewer table; the definition, and therefore the
  3MF object and the STEP product, is shared. Six of this model's 84
  placements are affected today.
- **Impact:** A BOM taken from the export undercounts distinct positions
  whenever two of them are geometrically identical at envelope stage. It
  resolves itself as the parts diverge, so it matters most for exactly the
  rough phase where the export is most useful for review.
- **Workaround:** Treat the placement name, not the definition name, as the BOM
  key while parts remain envelopes; keep `eta_2824-2_info.md` as the authority.
- **Documentation checked:** `docs/AUTHORING.md` section 5 (nesting and
  grouping); `docs/colour-decision.md` is referenced there for the related
  colour rule.
- **Minimal reproduction:** two parts with identical bodies and different
  names, placed once each.
- **Evidence:** `subtitle: both - 1 definition(s) placed 2 time(s)` on a
  two-part scratch file.
- **Resolution:** Pending - may be intended, in which case the note belongs in
  the authoring guide next to the grouping rule.

## Entry template

Copy this template under **Open gaps** and replace every placeholder.

```markdown
### GAP-YYYY-MM-DD-NN - Short descriptive title

- **Status:** open | needs confirmation | intentional refusal | resolved
- **Area:** syntax | type checking | evaluation | diagnostics | viewer | meshing | import | export | performance | documentation
- **Found while modeling:** ETA position or logical subassembly
- **Cade revision:** commit hash or `unknown`
- **Binary:** `$CADE`
- **Command:** exact command line
- **Expected:** observable expected behavior
- **Actual:** observable behavior and exact diagnostic
- **Impact:** what this prevents or compromises in the watch model
- **Workaround:** safe temporary approach, or `none`
- **Documentation checked:** exact files and sections
- **Minimal reproduction:** path to a small `.cade` file or a fenced Cade block
- **Evidence:** output, generated artifact, screenshot, or measurement
- **Resolution:** fix/documentation revision and validation command, when resolved
```

## Resolved gaps

Move resolved entries here without deleting their reproduction or evidence.
