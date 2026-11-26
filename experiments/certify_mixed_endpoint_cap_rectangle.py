#!/usr/bin/env python3
"""Outward endpoint-coefficient certificate on the outer-cap rectangle."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
import certify_mixed_endpoint_packet_extension as base

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_endpoint_cap_rectangle.md"
INITIAL = [
    [(F(27, 100), F(49, 100)), (F(-11, 200), F(0))],
    [(F(27, 100), F(49, 100)), (F(0), F(1, 25))],
]
FLOORS = [F(1, 5), F(1, 50), F(1, 3)]
ar = base.ar


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def test(box, sign):
    r, h = [ar(a).union(ar(b)) for a, b in box]
    rm, hm = [ar((a+b)/2) for a, b in box]
    e, em = acb(r, h), acb(rm, hm)
    u, disc = base.critical(e)
    if not u.is_finite():
        return None
    b = r-ar(F(1, 100))
    regular = (
        disc.real > 1,
        u.real > ar(F(17, 100)), u.real < ar(F(7, 25)),
        u.imag > ar(F(1, 1000)), u.imag < ar(F(1, 10)),
        u.real > ar(F(1, 20)), u.real < b,
        (e-u).real > 0, (e-u).real < ar(F(1, 2)),
    )
    if not all(regular):
        return None
    beta, lift = base.partials(e, u)
    if not (lift.is_finite() and lift.imag > -PI and lift.imag < PI):
        return None
    um, _ = base.critical(em)
    sm = base.phase(em, um)
    aa, bm = ar(F(1, 20)), rm-ar(F(1, 100))
    penalty_coefficient = -2*PI if sign < 0 else PI/2
    values = [
        (sm-base.phase(em, aa)).real,
        (sm-base.phase(em, bm)).real,
        (sm+base.J(em)).real-penalty_coefficient*hm,
    ]
    fa, _ = base.partials(e, acb(aa))
    fb, ub = base.partials(e, acb(b))
    c1, c2, c3 = beta-fa, beta-fb, beta+base.gp(e)
    gradients = [
        (c1.real, -c1.imag),
        ((c2-ub).real, -c2.imag),
        (c3.real, -c3.imag-penalty_coefficient),
    ]
    radii = [ar((hi-lo)/2) for lo, hi in box]
    lows = [(value-sum(abs(g)*radius for g, radius in zip(gs, radii))).lower()
            for value, gs in zip(values, gradients)]
    if not all(value > ar(floor) for value, floor in zip(lows, FLOORS)):
        return None
    return dict(lower=lows, u=u)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--seconds", type=float, default=120)
    ap.add_argument("--max-cells", type=int, default=50000)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-endpoint-cap-rectangle.json")
    args = ap.parse_args()
    assert args.precision >= 192 and 0 < args.seconds <= 900
    ctx.prec = args.precision
    global PI
    PI = arb.pi()
    base.PI, base.II = PI, acb(0, 1)
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, visited = {}, set()

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        bind(path)
        if path in visited:
            return
        visited.add(path)
        record = json.loads((ROOT/path).read_text())
        assert record["status"] == "passed", path
        nested = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                if p in nested:
                    assert nested[p] == digest
                nested[p] = digest
                bind(p, digest)
        for p in nested:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)

    primary = "repro/results/research-mixed-endpoint-packet-extension.json"
    inherit(primary)
    parent = json.loads((ROOT/primary).read_text())
    assert parent["proof_sha256"] == bind(
        "notes/research_mixed_endpoint_packet_extension_criterion.md")
    assert parent["script_sha256"] == bind(
        "experiments/certify_mixed_endpoint_packet_extension.py")
    checks = []

    def check(name, statement):
        assert statement, name
        checks.append(name)

    check("left-row sine lower bound on [.22,.49]",
          (ar(F(11, 50))*PI).sin() > ar(F(1, 2))
          and (ar(F(49, 100))*PI).sin() > ar(F(1, 2)))
    check("left-row cosine, sine and exponential bounds",
          (PI/20).cos()**2 > ar(F(1, 4))
          and (PI/20).sin() < ar(F(1, 6))
          and (-PI/25).exp() > ar(F(1, 2)))
    check("low-row ratio greater than one",
          F(1, 2)*F(1, 4)*6**3*F(1, 2) == F(27, 2) > 1)
    check("short added interval has the stated sine bound",
          (PI/20).sin()**2+(9*PI/100).sinh()**2 < ar(F(1, 9)))
    check("short added interval trigonometric quotient bound",
          (6*PI/25).cos()**2/(6*PI/25).sin()**3 < ar(F(5, 3)))
    check("short added interval exponential bound",
          (9*PI/100).exp() < ar(F(4, 3)))
    check("short added interval row ratio below one",
          F(1, 3)*F(5, 3)*F(4, 3) == F(20, 27) < 1)
    check("old upper interval ratio below one",
          (9*PI/100).exp()*(9*PI/100).cosh() < ar(F(7, 5))
          and (3*PI/10).cos()**2/(3*PI/10).sin()**3 < ar(F(2, 3))
          and F(7, 5)*F(2, 3) == F(14, 15) < 1)
    check("alias coefficient remains positive", 2*(F(1, 2)-F(49, 100)) == F(1, 50))
    check("cuts and reflection interval stay regular",
          F(1, 6) < F(27, 100) < F(49, 100) < F(1, 2)
          and F(49, 100)+F(1, 2) < 1
          and F(27, 100)-F(1, 100) > F(1, 20))
    if old is not None:
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
        assert old["gap_floors"] == list(map(str, FLOORS))
        assert len(old["cases"]) == len(INITIAL)
    start = time.monotonic()
    records, total_leaves, total_visits = [], 0, 0
    for case_index, initial in enumerate(INITIAL):
        sign = -1 if case_index == 0 else 1
        stack = [(initial, 0)]
        saved = old["cases"][case_index] if old else None
        if saved:
            assert saved["initial_box"] == [[str(a), str(b)] for a, b in initial]
        nodes, cursor, leaves, visits, depthmax = [], 0, 0, 0, 0
        minimum, u_hull = [None]*3, None
        while stack:
            assert time.monotonic()-start < args.seconds, "bounded runtime exhausted"
            assert total_visits+visits < args.max_cells, "bounded cell budget exhausted"
            box, depth = stack.pop()
            visits += 1
            depthmax = max(depthmax, depth)
            node = saved["nodes"][cursor] if saved else None
            cursor += saved is not None
            if node is not None and node[0] == "S":
                assert len(node) == 2 and type(node[1]) is int and node[1] in (0, 1)
                axis = node[1]
            else:
                assert node is None or node == ["L"]
                result = test(box, sign)
                if result is not None:
                    leaves += 1
                    nodes.append(["L"])
                    for j, lower in enumerate(result["lower"]):
                        minimum[j] = lower if minimum[j] is None else min(minimum[j], lower)
                    u = result["u"]
                    u_hull = u if u_hull is None else acb(
                        u_hull.real.union(u.real), u_hull.imag.union(u.imag))
                    continue
                assert saved is None, ("saved cell failed", case_index, cursor, box)
                axis = max((hi-lo, j) for j, (lo, hi) in enumerate(box))[1]
            lo, hi = box[axis]
            assert lo < hi and depth < 24
            mid = (lo+hi)/2
            nodes.append(["S", axis])
            for interval in ((lo, mid), (mid, hi)):
                child = list(box)
                child[axis] = interval
                stack.append((child, depth+1))
        if saved:
            assert cursor == len(saved["nodes"])
            assert leaves == saved["accepted_cells"] and visits == saved["visited_cells"]
        records.append(dict(initial_box=[[str(a), str(b)] for a, b in initial],
            nodes=nodes, accepted_cells=leaves, visited_cells=visits,
            maximum_depth=depthmax, remaining_boxes=0,
            minimum_gaps=list(map(str, minimum)),
            critical_image=[str(u_hull.real), str(u_hull.imag)]))
        total_leaves += leaves
        total_visits += visits
        print("case", case_index, "PASS", leaves, visits, list(map(str, minimum)), flush=True)
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    result = dict(status="passed", precision_bits=args.precision,
        parameter_domains=len(INITIAL), accepted_cells=total_leaves, visited_cells=total_visits,
        cases=records, gap_floors=list(map(str, FLOORS)),
        critical_image_rectangle=["17/100", "7/25", "1/1000", "1/10"],
        original_logarithmic_lift="zero, by the inherited exact cubic and imaginary lift in (-pi,pi)",
        exact_and_scalar_checks=len(checks), checks=checks,
        primary_records={primary: deps[primary]}, primary_record_count=1,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        input_sha256=ih, elapsed_seconds=time.monotonic()-start,
        scope="Complete ordinary-endpoint coefficient on E_cap. No outer-cap estimate or open-word noncancellation claim.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", total_leaves, "cells", total_visits, "visits",
          "seconds", result["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
