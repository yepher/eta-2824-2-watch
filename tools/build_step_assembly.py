#!/usr/bin/env python3
"""Assemble the per-part STEP files into one openable STEP assembly.

`cade export` writes each solid in its own local frame, so a directory of
per-part STEP files has no positions. The positions live in the Cade sources:
every subsystem assembly is a flat `together(...)` of

    part_name()
      |> place(frame = frame(origin = point(x =, y =, z =), axis =, angle =),
               color = rgb(r =, g =, b =))

This script reads those placements straight out of the .cade files, loads each
part's STEP, and writes a single AP214 assembly with the subsystem hierarchy,
part names, and the Cade colors preserved.

    python3 tools/build_step_assembly.py [-o output/watch_assembly.step]

Requires OpenCASCADE Python bindings:  pip install cadquery-ocp
"""

import argparse
import json
import math
import os
import re
import sys

_TIMESTAMP = "2026-09-05T00:00:00"

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESIGN = os.path.join(HERE, "eta_2824_design")

# The subsystems `watch()` is built from, in the order movement.cade and
# watch.cade compose them.
SUBSYSTEMS = [
    ("main_plate",         "main_plate.cade",         "main_plate_assembly"),
    ("hand_setting",       "hand_setting.cade",       "hand_setting_assembly"),
    ("going_train",        "going_train.cade",        "going_train_assembly"),
    ("barrel_and_winding", "barrel_and_winding.cade", "barrel_and_winding_assembly"),
    ("escapement",         "escapement.cade",         "escapement_assembly"),
    ("balance",            "balance.cade",            "balance_assembly"),
    ("automatic_winding",  "automatic_winding.cade",  "automatic_winding_assembly"),
    ("dial_side",          "dial_side.cade",          "dial_side_assembly"),
    ("fasteners",          "fasteners.cade",          "fasteners_assembly"),
    ("case_and_hands",     "case.cade",               "watch_case_assembly"),
]

NUM = r"(-?[\d.]+)"
ORIGIN = re.compile(
    r"origin\s*=\s*point\(\s*x\s*=\s*%smm\s*,\s*y\s*=\s*%smm\s*,\s*z\s*=\s*%smm\s*,?\s*\)"
    % (NUM, NUM, NUM))
AXIS = re.compile(r"axis\s*=\s*([A-Za-z_]+)")
ANGLE = re.compile(r"angle\s*=\s*%sdeg" % NUM)
COLOR = re.compile(
    r"color\s*=\s*rgba?\(\s*r\s*=\s*(\d+)\s*,\s*g\s*=\s*(\d+)\s*,\s*b\s*=\s*(\d+)\s*"
    r"(?:,\s*a\s*=\s*(\d+)\s*)?,?\s*\)")
PLACE = re.compile(r"(?:(\w+)\.)?(\w+)\(\)\s*\|>\s*place\s*")
SUBCALL = re.compile(r"(?:(\w+)\.)?(\w+_assembly)\(\)")


def _balanced(text, i):
    """text[i] is '('; return the text between it and its matching ')'."""
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "(":
            depth += 1
        elif text[j] == ")":
            depth -= 1
            if depth == 0:
                return text[i + 1:j]
    raise ValueError("unbalanced parentheses")


def _part_body(src, fn):
    m = re.search(r"part\s+%s\s*\(\)\s*->\s*Assembly\s*\{" % re.escape(fn), src)
    if not m:
        return None
    i = m.end() - 1
    depth = 0
    for j in range(i, len(src)):
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                return src[i + 1:j]
    return None


def _placements(body):
    out = []
    for m in PLACE.finditer(body):
        inner = _balanced(body, body.index("(", m.end() - 1))
        origin = ORIGIN.search(inner)
        if not origin:
            continue
        axis = AXIS.search(inner)
        angle = ANGLE.search(inner)
        color = COLOR.search(inner)
        out.append({
            "part": m.group(2),
            "origin": [float(origin.group(i)) for i in (1, 2, 3)],
            "axis": axis.group(1) if axis else "Z",
            "angle": float(angle.group(1)) if angle else 0.0,
            "color": [int(color.group(i)) for i in (1, 2, 3)] if color else [150, 150, 150],
        })
    return out


def read_placements():
    """Every placement in `watch()`, grouped by subsystem.

    Sub-assemblies called without their own `place(...)` (balance_bridge,
    rotor, hand_stack) are inlined: their placements are already absolute.
    """
    sources = {f: open(os.path.join(DESIGN, f)).read()
               for f in os.listdir(DESIGN) if f.endswith(".cade")}

    def collect(fname, fn, seen):
        if (fname, fn) in seen:
            return []
        seen.add((fname, fn))
        body = _part_body(sources[fname], fn) or ""
        out = _placements(body)
        for m in SUBCALL.finditer(body):
            if m.group(2) != fn:
                out += collect(fname, m.group(2), seen)
        return out

    return [{"name": label, "parts": collect(fname, fn, set())}
            for label, fname, fn in SUBSYSTEMS]


def build(step_dir, out_path, placements):
    from OCP.STEPControl import STEPControl_Reader
    from OCP.IFSelect import IFSelect_RetDone
    from OCP.TDocStd import TDocStd_Document
    from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ColorType
    from OCP.STEPCAFControl import STEPCAFControl_Writer
    from OCP.TCollection import TCollection_ExtendedString
    from OCP.TDataStd import TDataStd_Name
    from OCP.gp import gp_Trsf, gp_Ax1, gp_Pnt, gp_Dir, gp_Vec
    from OCP.TopLoc import TopLoc_Location
    from OCP.Quantity import Quantity_Color, Quantity_TOC_sRGB
    from OCP.Interface import Interface_Static

    def load(path):
        reader = STEPControl_Reader()
        if reader.ReadFile(path) != IFSelect_RetDone:
            return None
        reader.TransferRoots()
        shape = reader.OneShape()
        return None if shape.IsNull() else shape

    def location(axis, angle_deg, origin):
        rot = gp_Trsf()
        if abs(angle_deg) > 1e-12:
            direction = {"X": gp_Dir(1, 0, 0), "Y": gp_Dir(0, 1, 0), "Z": gp_Dir(0, 0, 1)}[axis]
            rot.SetRotation(gp_Ax1(gp_Pnt(0, 0, 0), direction), math.radians(angle_deg))
        move = gp_Trsf()
        move.SetTranslation(gp_Vec(*origin))
        return TopLoc_Location(move.Multiplied(rot))

    doc = TDocStd_Document(TCollection_ExtendedString("watch"))
    shapes = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    colors = XCAFDoc_DocumentTool.ColorTool_s(doc.Main())

    def label_name(label, text):
        TDataStd_Name.Set_s(label, TCollection_ExtendedString(text))

    wanted = {p["part"] for sub in placements for p in sub["parts"]}
    available = {f[:-5] for f in os.listdir(step_dir) if f.endswith(".step")}

    definitions = {}
    for part in sorted(wanted & available):
        shape = load(os.path.join(step_dir, part + ".step"))
        if shape is None:
            continue
        label = shapes.AddShape(shape, False)
        label_name(label, part)
        definitions[part] = label

    root = shapes.NewShape()
    label_name(root, "eta_2824_2_watch")

    placed, missing = 0, {}
    for sub in placements:
        sub_label = shapes.NewShape()
        label_name(sub_label, sub["name"])
        count = 0
        for p in sub["parts"]:
            definition = definitions.get(p["part"])
            if definition is None:
                missing[p["part"]] = missing.get(p["part"], 0) + 1
                continue
            component = shapes.AddComponent(
                sub_label, definition, location(p["axis"], p["angle"], p["origin"]))
            label_name(component, p["part"])
            r, g, b = p["color"]
            colors.SetColor(component,
                            Quantity_Color(r / 255.0, g / 255.0, b / 255.0, Quantity_TOC_sRGB),
                            XCAFDoc_ColorType.XCAFDoc_ColorSurf)
            placed += 1
            count += 1
        if count:
            label_name(shapes.AddComponent(root, sub_label, TopLoc_Location()), sub["name"])

    shapes.UpdateAssemblies()

    Interface_Static.SetCVal_s("write.step.schema", "AP214IS")
    Interface_Static.SetCVal_s("write.step.product.name", "eta_2824_2_watch")
    Interface_Static.SetIVal_s("write.step.assembly", 1)
    writer = STEPCAFControl_Writer()
    writer.SetColorMode(True)
    writer.SetNameMode(True)
    writer.Transfer(doc)
    writer.Write(out_path)
    _rewrite_header(out_path, placed, len(definitions))
    return placed, missing, len(definitions)


def _rewrite_header(path, placed, definitions):
    """Replace the generic OpenCASCADE header with one that says what this is."""
    with open(path) as fh:
        text = fh.read()
    start, end = text.index("HEADER;"), text.index("ENDSEC;")
    description = ("ETA 2824-2 reference reconstruction - %d placement(s) of %d part(s), "
                   "positioned from the Cade sources" % (placed, definitions))
    header = ("HEADER;\n"
              "FILE_DESCRIPTION(('%s'),'2;1');\n"
              "FILE_NAME('watch_assembly.step','%s',('cade'),('cade'),"
              "'cade export + OpenCASCADE STEP processor','tools/build_step_assembly.py','');\n"
              "FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'));\n"
              % (description, _TIMESTAMP))
    with open(path, "w") as fh:
        fh.write(text[:start] + header + text[end:])


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-o", "--out", default=os.path.join(HERE, "output", "watch_assembly.step"))
    ap.add_argument("--step-dir", default=os.path.join(HERE, "output", "step"))
    ap.add_argument("--dump-placements", action="store_true",
                    help="print the parsed placements as JSON and exit")
    args = ap.parse_args()

    placements = read_placements()
    total = sum(len(s["parts"]) for s in placements)
    if args.dump_placements:
        json.dump(placements, sys.stdout, indent=1)
        return

    if not os.path.isdir(args.step_dir):
        sys.exit("no per-part STEP in %s — see output/README.md" % args.step_dir)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)

    placed, missing, definitions = build(args.step_dir, args.out, placements)
    print("%s\n  %d of %d placements, %d distinct parts, %.1f MB"
          % (args.out, placed, total, definitions, os.path.getsize(args.out) / 1e6))
    if missing:
        print("  not placed (no STEP export — see output/README.md):")
        for part in sorted(missing):
            n = missing[part]
            print("    %s%s" % (part, " x%d" % n if n > 1 else ""))


if __name__ == "__main__":
    main()
