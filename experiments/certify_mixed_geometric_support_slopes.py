#!/usr/bin/env python3
"""Outward bounds on both supporting slopes in three-vertex windows."""
import argparse
import ast
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "experiments/certify_mixed_cyclic_window_heights.py"
PROOF = ROOT / "notes/research_mixed_geometric_support_slopes.md"
RECTS = [["3/10", "39/100", "-3/100", "1/50"],
         ["27/100", "33/100", "-57/1000", "-1/50"]]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decode(address):
    box = [Q(0), Q(1), Q(0), Q(1)]
    for j, bit in enumerate(address):
        assert bit in "01"
        k = 2*(j % 2)
        midpoint = (box[k]+box[k+1])/2
        box[k+1-int(bit)] = midpoint
    return box


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--max-visits", type=int, default=60000)
    parser.add_argument("--case", nargs=3)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-geometric-support-slopes.json")
    args = parser.parse_args()
    assert args.precision >= 128
    dependencies = [
        str(SOURCE.relative_to(ROOT)),
        "notes/research_mixed_cyclic_critical_localization.md",
        "notes/research_mixed_cyclic_critical_height_bounds.md",
        "notes/research_mixed_type_three_window_strip.md",
        "notes/research_mixed_type_four_height_refinement.md",
        "repro/results/research-mixed-cyclic-block-localization.json",
        "repro/results/research-mixed-cyclic-block-localization-replay.json",
        "repro/results/research-mixed-type-three-window-strip.json",
        "repro/results/research-mixed-type-three-window-strip-replay.json",
        "repro/results/research-mixed-type-four-height-refinement.json",
        "repro/results/research-mixed-type-four-height-refinement-replay.json",
        "notes/research_mixed_central_conditional_rectangles.md",
    ]
    initial = {p: sha(ROOT / p) for p in dependencies}
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    for path in dependencies:
        if path.endswith(".json"):
            data = json.loads((ROOT / path).read_text())
            assert data["status"] == "passed"
            for key in ("dependencies", "dependencies_sha256"):
                for name, digest in data.get(key, {}).items():
                    assert sha(ROOT / name) == digest, (path, name)
    for stem, slug, proof in [
        ("mixed_cyclic_block_localization", "mixed-cyclic-block-localization",
         "research_mixed_cyclic_critical_localization.md"),
        ("mixed_type_three_window_strip", "mixed-type-three-window-strip",
         "research_mixed_type_three_window_strip.md"),
        ("mixed_type_four_height_refinement", "mixed-type-four-height-refinement",
         "research_mixed_type_four_height_refinement.md"),
    ]:
        prior_path = ROOT / f"repro/results/research-{slug}.json"
        prior = json.loads(prior_path.read_text())
        replay = json.loads((ROOT / f"repro/results/research-{slug}-replay.json").read_text())
        assert prior["script_sha256"] == sha(ROOT / f"experiments/certify_{stem}.py")
        assert replay["script_sha256"] == sha(ROOT / f"experiments/replay_{stem}.py")
        assert prior["proof_sha256"] == replay["proof_sha256"] == sha(ROOT / "notes" / proof)
        assert replay["input_sha256"] == sha(prior_path)
    spec = importlib.util.spec_from_file_location("unchanged_window", SOURCE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    ctx.prec = args.precision
    m.PI = arb.pi()
    pi, imaginary, ar = m.PI, acb(0, 1), m.ar
    for t, rectangle in enumerate(RECTS):
        xl, xh, yl, yh = map(Q, rectangle)
        cx, cy = m.CENT[t]
        assert max((x-cx)**2+(y-cy)**2
                   for x in (xl, xh) for y in (yl, yh)) < m.RAD[t]**2
    tree = ast.parse(SOURCE.read_text())
    function = next(n for n in tree.body
                    if isinstance(n, ast.FunctionDef) and n.name == "certify")

    class Capture(ast.NodeTransformer):
        def visit_Return(self, node):
            if isinstance(node.value, ast.List):
                return ast.copy_location(
                    ast.Return(ast.Call(ast.Name("locals", ast.Load()), [], [])), node)
            return node

    function = Capture().visit(function)
    ast.fix_missing_locations(function)
    active_faces = [0, 0]

    def edge(t, face, lo, hi):
        xl, xh, yl, yh = map(Q, RECTS[t])
        parameter = ar(lo).union(ar(hi))
        if face in (0, 2):
            return acb(ar(xl)+ar(xh-xl)*parameter, ar(yl if face == 0 else yh))
        assert face in (1, 3)
        return acb(ar(xh if face == 1 else xl), ar(yl)+ar(yh-yl)*parameter)

    def params(box, ta, tb):
        return [edge(t, active_faces[j], box[2*j], box[2*j+1])
                for j, t in enumerate((ta, tb))]

    namespace = dict(m.__dict__)
    namespace["params"] = params
    exec(compile(ast.Module(body=[function], type_ignores=[]),
                 str(SOURCE)+"[rectangle slopes]", "exec"), namespace)
    certify = namespace["certify"]

    def gp(z):
        return (1-(-2*pi*imaginary*z).exp()).log()

    families = [(word, ta, tb) for word in itertools.product((0, 1), repeat=3)
                for ta, tb in itertools.product((0, 1), repeat=2)]
    if args.case:
        families = [(tuple(map(int, args.case[0])),
                     int(args.case[1]), int(args.case[2]))]
        assert len(families[0][0]) == 3
        assert all(v in (0, 1) for v in (*families[0][0], *families[0][1:]))
    start = time.time()
    cases, visits = [], 0
    for word, ta, tb in families:
        for faces in itertools.product(range(4), repeat=2):
            active_faces[:] = faces
            pending, leaves = [""], []
            lower, upper = None, None
            while pending:
                address = pending.pop()
                visits += 1
                assert visits <= args.max_visits, "bounded cover exhausted"
                assert len(address) <= 26, (word, ta, tb, faces, address)
                try:
                    witness = certify(word, ta, tb, decode(address), -Q(3, 25))
                except (ValueError, ZeroDivisionError, OverflowError):
                    witness = False
                accepted = False
                if witness:
                    a, s, b = [witness["boxes"][j] for j in (1, 2, 3)]
                    left, own = word[:2]
                    pa = gp(s+a)+2*pi*imaginary*s-ar(1+Q(left, 2))*gp(a)
                    pb = gp(s+b)-ar(1+Q(own, 2))*gp(b)
                    values = [pa.real, pb.real]
                    accepted = all(-ar("1/5") < v < ar("1/4") for v in values)
                if accepted:
                    leaves.append(address)
                    lo, hi = min(v.lower() for v in values), max(v.upper() for v in values)
                    lower = lo if lower is None else min(lower, lo)
                    upper = hi if upper is None else max(upper, hi)
                else:
                    pending.extend([address+"1", address+"0"])
            addresses = sorted(leaves)
            assert len(addresses) == len(set(addresses))
            assert all(not b.startswith(a) for a, b in zip(addresses, addresses[1:]))
            assert sum((Q(1, 2**len(a)) for a in addresses), Q(0)) == 1
            row = {"word": list(word), "external_types": [ta, tb],
                   "faces": list(faces), "addresses": addresses,
                   "accepted": len(addresses), "lower": str(lower), "upper": str(upper)}
            cases.append(row)
            print(json.dumps({k: v for k, v in row.items() if k != "addresses"}), flush=True)
    expected = {(*word, ta, tb, fa, fb) for word, ta, tb in families
                for fa, fb in itertools.product(range(4), repeat=2)}
    assert {(*c["word"], *c["external_types"], *c["faces"])
            for c in cases} == expected
    assert len(cases) == len(expected) == 16*len(families)
    assert initial == {p: sha(ROOT / p) for p in dependencies}
    assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
    data = {
        "status": "passed", "precision_bits": args.precision,
        "rectangles": RECTS, "slope_bounds": ["-1/5", "1/4"],
        "cases": cases, "case_count": len(cases),
        "accepted_cells": sum(c["accepted"] for c in cases),
        "visited_cells": visits, "elapsed_seconds": time.time()-start,
        "full_family": not bool(args.case),
        "script_sha256": script_hash, "proof_sha256": proof_hash,
        "dependencies": initial,
        "scope": "Both real supporting slopes of a central conditional block "
                 "in every three-vertex reference window; no source dominance bound.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+"\n")
    print("completed", len(cases), "boundary products,", data["accepted_cells"], "cells")


if __name__ == "__main__":
    main()
