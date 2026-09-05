# ETA 2824-2 Cade reference reconstruction

This project reconstructs an ETA 2824-2 movement and a simplified watch around
it from published references and explicitly labeled engineering estimates. It is
an educational/reference model, not a manufacturing drawing package.

Start with [CLAUDE.md](CLAUDE.md), [MODEL_STATUS.md](MODEL_STATUS.md),
[ASSUMPTIONS.md](ASSUMPTIONS.md), and [eta_2824-2_info.md](eta_2824-2_info.md).
The top-level Cade entry point is `watch` in `watch.cade`.

Run the live raymarch view from the Cade repository:

```sh
cargo run --release -- view watch.cade --raymarch -p 7879 --part watch --watch
```

`watch.cade` is intentionally a minimal, compiling starting point. The CAD agent
will establish the assembly structure and add rough envelopes there before
deciding whether real complexity justifies additional Cade files. Part names
ending in `_envelope` are provisional and must not be interpreted as production
geometry.
