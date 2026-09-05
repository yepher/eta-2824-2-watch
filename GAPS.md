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
- **Binary:** `~/src/cade_research/cade/target/release/cade`
- **Command:** `cade view watch.cade --part fastener_detail_preview --raymarch`
- **Expected:** Visible helical thread geometry on a completed screw model.
- **Actual:** Cade intentionally provides `thread(d, pitch, fit)` as manufacturing metadata and has no helix operator.
- **Impact:** Screw heads, collars, shoulders, shanks, and lead tips can be modeled, but true thread flanks cannot be rendered.
- **Workaround:** Add thread metadata after controlled diameter and pitch values are obtained; retain plain shank solids for the drawing representation.
- **Documentation checked:** `docs/AUTHORING.md` section 5, Threads.
- **Minimal reproduction:** Any screw placed with `thread(...)` retains a cylindrical solid shank; the thread callout is metadata.
- **Evidence:** The compiled `fastener_detail_preview` shows the modeled solid forms without a helix.
- **Resolution:** Intentional language behavior; no model-side fix.

### GAP-2026-09-04-01 - Qualified imported `main` is reported as recursion

- **Status:** open
- **Area:** type checking / diagnostics
- **Found while modeling:** top-level movement assembly
- **Cade revision:** unknown
- **Binary:** `~/src/cade_research/cade/target/release/cade`
- **Command:** `cade check watch.cade --part watch`
- **Expected:** Imported parts named `main` resolve through their aliases.
- **Actual:** At `plate.main()` the compiler reports `` `main` calls itself: main -> main ``.
- **Impact:** Subsystem modules cannot share the conventional `main` entry name.
- **Workaround:** Give every subsystem assembly a unique entry name, such as
  `main_plate_assembly` and `going_train_assembly`.
- **Documentation checked:** `docs/AUTHORING.md` sections 5 and 7; working
  `test/assembly/` examples use unique imported part names.
- **Minimal reproduction:** One file exports `part main() -> Assembly`; a second
  imports it as `a` and calls `a.main()` from its own `part main()`.
- **Evidence:** Compiler diagnostic captured while checking the initial watch
  scaffold.
- **Resolution:** Pending.

## Entry template

Copy this template under **Open gaps** and replace every placeholder.

```markdown
### GAP-YYYY-MM-DD-NN - Short descriptive title

- **Status:** open | needs confirmation | intentional refusal | resolved
- **Area:** syntax | type checking | evaluation | diagnostics | viewer | meshing | import | export | performance | documentation
- **Found while modeling:** ETA position or logical subassembly
- **Cade revision:** commit hash or `unknown`
- **Binary:** `~/src/cade_research/cade/target/release/cade`
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
