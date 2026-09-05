# Working commands

Run Cargo commands from `~/src/cade_research/cade/`.

## Live views

```sh
cargo run --release -- view ~/src/watch/watch.cade --raymarch -p 7879 --part watch --watch
cargo run --release -- view ~/src/watch/watch.cade --cell 0.05mm -p 7880 --part watch --watch
```

## Format and validate syntax

```sh
cargo run --release -- fmt ~/src/watch/watch.cade --check
cargo run --release -- view ~/src/watch/watch.cade --raymarch -o /tmp/watch-check.html --part watch
cargo run --release -- check ~/src/watch/watch.cade --part movement_envelope
```

`check` requires one solid and intentionally refuses the `watch` assembly. Use
the one-shot `view` command to compile the whole assembly graph and `check` or
`validate` on the individual solid currently being refined.

## Clearance diagnostics

Add focused diagnostic solids to `watch.cade` as interfaces are created, then
run `mesh watch.cade --part <diagnostic_name>`. Each should report zero volume.
A bounded intersection that canonicalizes to an empty solid may instead exit
with `this program denotes an empty or unbounded solid`; explicit emptiness is
also a pass. The CAD agent may move mature diagnostics to another file later.

## Export a review mesh

```sh
cargo run --release -- build ~/src/watch/watch.cade -o ~/src/watch/watch.3mf --part watch --cell 0.05mm
```
