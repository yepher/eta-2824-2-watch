# ETA 2824-2 Cade reference reconstruction

This project reconstructs an ETA 2824-2 movement and a simplified watch around
it from published references and explicitly labeled engineering estimates. It is
an educational/reference model, not a manufacturing drawing package.

> **Turn it round yourself.** Open
> [`output/watch-raymarch.html`](output/watch-raymarch.html) in a browser —
> nothing to install, no server, no network. Drag to orbit, wheel to zoom,
> shift-drag to pan; hover a part in the list to light it, click to hide it, and
> the slider explodes the assembly. It is 1.6 MB for all 103 placements because
> the page evaluates the model's own field per pixel rather than carrying a
> mesh, so there is no resolution setting and nothing is faceted. It needs
> **WebGPU** — current Chrome or Edge, or Safari 18+.
>
> **`output/watch.html` is the fallback and it is a poor picture.** It draws the
> same model from a *mesh*, so it needs only WebGL, and it is not committed
> because it is 54 MB. At the resolution that keeps it to that size the page
> reports its own damage: **37 of the 83 parts are under two cells across their
> thinnest feature and are bridged**, and the rotor meshes to nothing and is
> **missing from the picture entirely**. That is the drawing, not the model.
> Regenerate it with `cade view watch.cade -o output/watch.html --part watch
> -n 48`; better costs a lot, since the same command at `-n 64` is 95 MB and at
> `-n 128` is 381 MB.
>
> The raymarched page has none of this, because it has no grid: it evaluates
> the field per pixel, so nothing is bridged and nothing is faceted at any zoom.
> Use it if you can.

> **The STEP and Parasolid files are partial, on purpose.** They hold **43 of
> the model's 83 part definitions** — 54 of its 103 placements. The other 40 are
> not missing from the *model*; they are parts whose boundary cade cannot yet
> state as exact surfaces, and exact B-rep export is still being built out.
> Anything derived from that STEP, the `.x_t` included, inherits the same gap.
> **For the complete geometry use the 3MF**, which holds every placement — see
> [`output/EXPORTS-2026-09-07.md`](output/EXPORTS-2026-09-07.md) for what each
> format does and does not carry.

## Session one — watch it being built

[<img src="https://i.ytimg.com/vi/DhmN8472T4A/hqdefault.jpg" width="420" alt="ChatGPT designed this parametric watch movement in Cade. — Yeph Werks"/>](https://www.youtube.com/watch?v=DhmN8472T4A)

**[ChatGPT designed this parametric watch movement in Cade.](https://www.youtube.com/watch?v=DhmN8472T4A)**
— Yeph Werks. The first session, start to finish.

The written record of that session is in this repository as
[`chatgpt_session_one.md`](chatgpt_session_one.md). What the model has become
since is in [`MODEL_STATUS.md`](MODEL_STATUS.md), which grades every ETA
position as `placeholder`, `estimated` or `supported`, and in
[`ASSUMPTIONS.md`](ASSUMPTIONS.md), which says which numbers are published and
which are estimates.

## Renders

Click any thumbnail for the full-resolution image.

|  |  |  |
|:--:|:--:|:--:|
| [<img src="rendered/thumbs/watch_render.jpg" width="250" alt="exploded movement"/>](rendered/watch_render.jpeg)<br>**Exploded movement** | [<img src="rendered/thumbs/dial.jpg" width="250" alt="dial side"/>](rendered/dial.png)<br>**Dial side**<br>hands and date window | [<img src="rendered/thumbs/back.jpg" width="250" alt="caseback"/>](rendered/back.png)<br>**Caseback**<br>closed, from the rotor side |
| [<img src="rendered/thumbs/movement_body.jpg" width="250" alt="movement in the case"/>](rendered/movement_body.png)<br>**Movement in the case**<br>caseback off | [<img src="rendered/thumbs/movement_weight.jpg" width="250" alt="rotor in place"/>](rendered/movement_weight.png)<br>**Rotor in place**<br>the winding weight over the train | [<img src="rendered/thumbs/movement_wo_weight.jpg" width="250" alt="movement without the rotor"/>](rendered/movement_wo_weight.png)<br>**Rotor removed**<br>the automatic framework beneath |
| [<img src="rendered/thumbs/going_train.jpg" width="250" alt="going train"/>](rendered/going_train.png)<br>**Going train**<br>wheels, pivots and jewels alone | [<img src="rendered/thumbs/gears_1.jpg" width="250" alt="barrel and winding wheels"/>](rendered/gears_1.png)<br>**Barrel and winding wheels**<br>under the barrel bridge | [<img src="rendered/thumbs/balance.jpg" width="250" alt="balance and hairspring"/>](rendered/balance.png)<br>**Balance**<br>rim, staff, hairspring and stud |
| [<img src="rendered/thumbs/crown_assembly.jpg" width="250" alt="crown and stem"/>](rendered/crown_assembly.png)<br>**Crown and stem**<br>with the keyless works | [<img src="rendered/thumbs/exploded_view_editor.jpg" width="250" alt="exploded view in the viewer"/>](rendered/exploded_view_editor.png)<br>**Exploded view**<br>the same pose in the viewer | [<img src="rendered/thumbs/list_assemblies.jpg" width="250" alt="the viewer's part picker"/>](rendered/list_assemblies.png)<br>**The viewer**<br>part picker and per-placement list |

`rendered/thumbs/` holds the small copies only; every link above goes to the
original. The thumbnails are **151 KB for all twelve** against 7.1 MB for the
full set, which is the whole reason they exist — a README that inlined the
originals would cost a reader 7 MB to scroll past.
