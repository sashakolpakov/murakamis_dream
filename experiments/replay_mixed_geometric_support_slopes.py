#!/usr/bin/env python3
"""Independent sine/cotangent replay of the geometric supporting slopes."""
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
PRIMITIVE = ROOT / "experiments/replay_mixed_cyclic_window_heights.py"
AUTHOR = ROOT / "experiments/certify_mixed_geometric_support_slopes.py"
PROOF = ROOT / "notes/research_mixed_geometric_support_slopes.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path, default=ROOT /
                        "repro/results/research-mixed-geometric-support-slopes.json")
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-geometric-support-slopes-replay.json")
    args = parser.parse_args()
    assert args.precision >= 160
    source_hash = sha(args.input)
    data = json.loads(args.input.read_text())
    assert data["status"] == "passed" and data["full_family"]
    assert data["script_sha256"] == sha(AUTHOR)
    assert data["proof_sha256"] == sha(PROOF)
    assert data["slope_bounds"] == ["-1/5", "1/4"]
    rectangles = [["3/10", "39/100", "-3/100", "1/50"],
                  ["27/100", "33/100", "-57/1000", "-1/50"]]
    assert data["rectangles"] == rectangles
    dependencies = {**data["dependencies"],
                    str(PRIMITIVE.relative_to(ROOT)): sha(PRIMITIVE),
                    str(AUTHOR.relative_to(ROOT)): sha(AUTHOR),
                    str(PROOF.relative_to(ROOT)): sha(PROOF)}
    for name, digest in dependencies.items():
        assert sha(ROOT / name) == digest, name
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    spec = importlib.util.spec_from_file_location("independent_sine_window", PRIMITIVE)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    ctx.prec = args.precision
    m.PI = arb.pi()
    pi, imaginary, ar = m.PI, acb(0, 1), m.ar
    function = next(n for n in ast.parse(PRIMITIVE.read_text()).body
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

    def params(box, ta, tb):
        result = []
        for j, kind in enumerate((ta, tb)):
            xl, xh, yl, yh = map(Q, rectangles[kind])
            t = ar(box[2*j]).union(ar(box[2*j+1]))
            face = active_faces[j]
            if face in (0, 2):
                result.append(acb(ar(xl)+ar(xh-xl)*t, ar(yl if face == 0 else yh)))
            else:
                assert face in (1, 3)
                result.append(acb(ar(xh if face == 1 else xl), ar(yl)+ar(yh-yl)*t))
        return result

    namespace = dict(m.__dict__)
    namespace["params"] = params
    exec(compile(ast.Module(body=[function], type_ignores=[]),
                 str(PRIMITIVE)+"[rectangle slopes]", "exec"), namespace)
    certify = namespace["certify"]

    def gp(z):
        # Original logarithm expressed using the independent sine lift.
        return (2*(pi*z).sin()).log()+imaginary*pi*(ar("1/2")-z)

    expected = {(*word, ta, tb, fa, fb)
                for word in itertools.product((0, 1), repeat=3)
                for ta, tb, fa, fb in itertools.product((0, 1), (0, 1), range(4), range(4))}
    actual = {(*c["word"], *c["external_types"], *c["faces"]) for c in data["cases"]}
    assert actual == expected and len(actual) == data["case_count"] == len(data["cases"]) == 512
    assert sum(c["accepted"] for c in data["cases"]) == data["accepted_cells"]
    results, total_refinements = [], 0
    started = time.time()
    for case in data["cases"]:
        addresses = sorted(case["addresses"])
        assert len(addresses) == len(set(addresses)) == case["accepted"]
        assert all(not b.startswith(a) for a, b in zip(addresses, addresses[1:]))
        assert sum((Q(1, 2**len(a)) for a in addresses), Q(0)) == 1
        word = tuple(case["word"])
        ta, tb = case["external_types"]
        active_faces[:] = case["faces"]
        leaves, refinements = [], 0
        for original in addresses:
            pending = [original]
            while pending:
                address = pending.pop()
                witness = certify(word, ta, tb, m.decode(address), -Q(3, 25))
                accepted = False
                if witness:
                    a, s, b = [witness["boxes"][j] for j in (1, 2, 3)]
                    left, own = word[:2]
                    pa = gp(s+a)+2*pi*imaginary*s-ar(1+Q(left, 2))*gp(a)
                    pb = gp(s+b)-ar(1+Q(own, 2))*gp(b)
                    accepted = all(-ar("1/5") < v < ar("1/4")
                                   for v in (pa.real, pb.real))
                if accepted:
                    leaves.append(address)
                else:
                    assert len(address) < len(original)+12
                    pending.extend([address+"1", address+"0"])
                    refinements += 1
        assert sum((Q(1, 2**len(a)) for a in leaves), Q(0)) == 1
        row = {"word": list(word), "external_types": [ta, tb],
               "faces": list(active_faces), "author_cells": len(addresses),
               "replay_cells": len(leaves), "refinements": refinements}
        results.append(row)
        total_refinements += refinements
    assert source_hash == sha(args.input)
    assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
    for name, digest in dependencies.items():
        assert sha(ROOT / name) == digest, name
    result = {"status": "passed", "precision_bits": args.precision,
              "case_count": len(results), "cases": results,
              "replay_cells": sum(r["replay_cells"] for r in results),
              "refinements": total_refinements, "elapsed_seconds": time.time()-started,
              "input_sha256": source_hash, "script_sha256": script_hash,
              "proof_sha256": proof_hash, "dependencies": dependencies,
              "scope": data["scope"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("replayed", len(results), "boundary products,", result["replay_cells"],
          "cells,", total_refinements, "refinements")


if __name__ == "__main__":
    main()
