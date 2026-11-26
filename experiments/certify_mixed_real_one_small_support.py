#!/usr/bin/env python3
"""Finite real tangents for one-small original conditional sources.

Uses the frozen both-small checker's original-log Newton and Schur routines,
with separate target geometry, accepted cover, proof and provenance.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_real_one_small_support.md"
HELPER = ROOT / "experiments/certify_mixed_real_small_support.py"
spec = importlib.util.spec_from_file_location("one_small_original_log_helpers", HELPER)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
ar = core.ar
DEPS = core.DEPS + [
    "notes/research_mixed_real_small_support.md",
    "experiments/certify_mixed_real_small_support.py",
    "repro/results/research-mixed-real-small-support.json",
]
INTERVALS = [(F(j, 20), F(j+1, 20)) for j in range(10)]
DELTA = F(1, 10)
PHASE_GAP = F(11, 200)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def validate_record(record_path, proof, script):
    rec = json.loads((ROOT/record_path).read_text())
    assert rec["status"] == "passed"
    assert rec["proof_sha256"] == sha(ROOT/proof)
    assert rec["script_sha256"] == sha(ROOT/script)
    bound = {}
    for key in ("dependencies", "dependencies_sha256"):
        for p, digest in rec.get(key, {}).items():
            if p in bound:
                assert bound[p] == digest
            assert sha(ROOT/p) == digest, p
            bound[p] = digest


def tangent_data(source=None):
    tangent, roots = {}, []
    old = {} if source is None else {tuple(v["key"]): v["center"] for v in source["real_roots"]}
    keys = list(itertools.product((0, 1), (0, 1), range(10)))
    if source:
        assert set(old) == set(keys) and len(source["real_roots"]) == len(keys)
    for eps, side, j in keys:
        lo, hi = INTERVALS[j]
        mid = (lo+hi)/2
        c = (acb(ar(DELTA)), acb(ar(mid))) if side == 0 else (acb(ar(mid)), acb(ar(DELTA)))
        root = core.point_root(*c, eps, old.get((eps, side, j)))
        assert root is not None, (eps, side, j)
        s, center = root
        roots.append({"key": [eps, side, j], "center": center})
        corners = list(itertools.product((F(0), DELTA), (lo, hi))) if side == 0 else list(itertools.product((lo, hi), (F(0), DELTA)))
        for eta in (0, 1):
            value, grad, _ = core.phase(s, *c, eta, eps)
            tangent[eta, eps, side, j] = [
                (t, (value+sum((grad[k]*(ar(t[k])-c[k]) for k in (0, 1)), acb(0))).real)
                for t in corners]
    return tangent, roots


def test(case, address, tangent, witness=None):
    eta, eps, fa, fb = case
    al, ah, bl, bh = core.box(address)
    a, b = core.edge(eta, fa, al, ah), core.edge(eps, fb, bl, bh)
    a0 = core.edge(eta, fa, (al+ah)/2, (al+ah)/2)
    b0 = core.edge(eps, fb, (bl+bh)/2, (bl+bh)/2)
    roots = core.root_box(a, b, a0, b0, eps, witness)
    if roots is None:
        return None
    s, s0, wit = roots
    value, grad, _ = core.phase(s0, a0, b0, eta, eps)
    _, _, H = core.phase(s, a, b, eta, eps)
    velocities = [core.velocity(eta, fa), core.velocity(eps, fb)]
    radii = [ar((ah-al)/2), ar((bh-bl)/2)]
    worst = None
    for side, j in itertools.product((0, 1), range(10)):
        for target, tang in tangent[eta, eps, side, j]:
            t = [ar(x) for x in target]
            plane = value+grad[0]*(t[0]-a0)+grad[1]*(t[1]-b0)
            upper = tang-plane.real
            for k in (0, 1):
                derivative = H[0][k]*(t[0]-a)+H[1][k]*(t[1]-b)
                upper += abs((derivative*velocities[k]).real)*radii[k]
            if not upper < -ar(PHASE_GAP):
                return None
            worst = upper.upper() if worst is None else max(worst, upper.upper())
    return wit, worst


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT/"repro/results/research-mixed-real-one-small-support.json")
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    core.pi, core.ii = arb.pi(), acb(0, 1)
    initial = {p: sha(ROOT/p) for p in DEPS}
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    for j in (0, 3, 8):
        validate_record(core.DEPS[j+2], core.DEPS[j], core.DEPS[j+1])
    validate_record(DEPS[-1], DEPS[-3], DEPS[-2])
    for rect in core.RECTS.values():
        xl, xh, yl, yh = rect
        cot = (core.pi*acb(ar(xl).union(ar(xh)), ar(yl).union(ar(yh)))).cot()
        assert cot.real > 0 and abs(cot.imag) < ar("1/2")
    input_hash = sha(args.input) if args.input else None
    source = json.loads(args.input.read_text()) if args.input else None
    if source:
        assert source["status"] == "passed"
        assert source["rectangles"] == {str(k): v for k, v in core.RECTS.items()}
        assert source["target_intervals"] == [[str(a), str(b)] for a, b in INTERVALS]
        assert source["cutoff"] == str(DELTA) and source["phase_gap"] == str(PHASE_GAP)
        assert source["proof_sha256"] == proof_hash and source["script_sha256"] == script_hash
        assert source["dependencies"] == initial
    tangent, real_roots = tangent_data(source)
    expected = list(itertools.product((0, 1), (0, 1), range(4), range(4)))
    if source:
        assert [tuple(x["case"]) for x in source["cases"]] == expected
    cases, cell_count, visit_count, worst = [], 0, 0, None
    for idx, case in enumerate(expected):
        leaves = []
        pending = [("", None)] if source is None else [(v["address"], v["witness"]) for v in source["cases"][idx]["leaves"]]
        if source:
            core.cover([a for a, _ in pending])
        while pending:
            address, witness = pending.pop()
            visit_count += 1
            result = test(case, address, tangent, witness)
            if result is None:
                assert source is None and len(address) < 28, (case, address)
                pending.extend([(address+"0", None), (address+"1", None)])
                continue
            wit, upper = result
            worst = upper if worst is None else max(worst, upper)
            leaves.append({"address": address, "witness": wit})
        leaves.sort(key=lambda v: v["address"])
        core.cover([v["address"] for v in leaves])
        cell_count += len(leaves)
        cases.append({"case": list(case), "leaves": leaves})
    assert initial == {p: sha(ROOT/p) for p in DEPS}
    assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
    if args.input:
        assert input_hash == sha(args.input)
    record = {
        "status": "passed", "precision_bits": args.precision,
        "scope": "Real one-small targets only; compact finite-source bounds away from zero and the half endpoints. No complex-taper or reset-star assembly claim.",
        "rectangles": core.RECTS, "cutoff": str(DELTA), "phase_gap": str(PHASE_GAP),
        "target_intervals": [[str(a), str(b)] for a, b in INTERVALS],
        "reference_products": len(cases), "orientations": 2,
        "tangent_planes_per_type_and_orientation": len(INTERVALS),
        "cells": cell_count, "visits": visit_count,
        "affine_corner_tests": 80*cell_count,
        "worst_defect_upper": str(worst), "real_roots": real_roots, "cases": cases,
        "proof_sha256": proof_hash, "script_sha256": script_hash, "dependencies": initial}
    if input_hash:
        record["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print("PASS", len(cases), "reference products", cell_count, "cells", visit_count, "visits; worst", worst)


if __name__ == "__main__":
    main()
