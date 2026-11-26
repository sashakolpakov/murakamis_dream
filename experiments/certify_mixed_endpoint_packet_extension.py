#!/usr/bin/env python3
"""Bounded outward check of the explicit ordinary-endpoint packet criterion.

Only two real parameters are covered. No source-row or contour-current
cover is used: those reductions are proved in the bound proof. Saved
replays exhaust the original split trees and cannot refine them.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_endpoint_packet_extension_criterion.md"
INITIAL = [
    [(F(33, 100), F(47, 100)), (F(-9, 100), F(0))],
    [(F(33, 100), F(47, 100)), (F(0), F(2, 25))],
]
FLOORS = [F(1, 5), F(1, 20), F(1, 5)]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(x):
    x = F(x)
    return arb(x.numerator) / x.denominator


def J(z):
    return ((PI*PI/6-(2*PI*II*z).exp().polylog(2))/(2*PI*II)
            +II*PI*z*(1-z)/2)


def gp(z):
    return (2*(PI*z).sin()).log()


def critical(e):
    disc = 1-2*(2*PI*II*e).exp()
    u = ((II+disc.sqrt())/2).atan()/PI
    return u, disc


def phase(e, u):
    return -2*J(ar(F(1, 2))-u)-3*J(u)-J(e-u)+II*PI*e*u


def partials(e, u):
    fe = -gp(e-u)+II*PI*u
    fu = (2*(PI*u).cos().log()+(PI*(e-u)).sin().log()
          -3*(PI*u).sin().log()+II*PI*e)
    return fe, fu


def test(box, sign):
    r, h = [ar(a).union(ar(b)) for a, b in box]
    rm, hm = [ar((a+b)/2) for a, b in box]
    e, em = acb(r, h), acb(rm, hm)
    u, disc = critical(e)
    if not u.is_finite():
        return None
    b = r-ar(F(1, 100))
    # The explicit branch stays regular. The cubic identity plus the
    # original logarithmic lift interval below proves Fu=0 exactly.
    regular = (
        disc.real > 1,
        u.real > ar(F(19, 100)), u.real < ar(F(7, 25)),
        u.imag > ar(F(1, 100)), u.imag < ar(F(1, 10)),
        u.real > ar(F(1, 20)), u.real < b,
        (e-u).real > 0, (e-u).real < ar(F(1, 2)),
    )
    if not all(regular):
        return None
    beta, lift = partials(e, u)
    if not (lift.is_finite() and lift.imag > -PI and lift.imag < PI):
        return None
    um, _ = critical(em)
    sm = phase(em, um)
    aa, bm = ar(F(1, 20)), rm-ar(F(1, 100))
    d1 = (sm-phase(em, aa)).real
    d2 = (sm-phase(em, bm)).real
    penalty_coefficient = -2*PI if sign < 0 else PI/2
    d3 = (sm+J(em)).real-penalty_coefficient*hm
    fa, _ = partials(e, acb(aa))
    fb, ub = partials(e, acb(b))
    c1, c2, c3 = beta-fa, beta-fb, beta+gp(e)
    gradients = [
        (c1.real, -c1.imag),
        ((c2-ub).real, -c2.imag),
        (c3.real, -c3.imag-penalty_coefficient),
    ]
    radii = [ar((hi-lo)/2) for lo, hi in box]
    lows = [(value-sum(abs(g)*radius for g, radius in zip(gs, radii))).lower()
            for value, gs in zip((d1, d2, d3), gradients)]
    if not all(value > ar(floor) for value, floor in zip(lows, FLOORS)):
        return None
    return dict(lower=lows, u=u, disc=disc, lift=lift)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--seconds", type=float, default=120)
    ap.add_argument("--max-cells", type=int, default=50000)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-endpoint-packet-extension.json")
    args = ap.parse_args()
    assert args.precision >= 192 and 0 < args.seconds <= 900
    ctx.prec = args.precision
    global PI, II
    PI, II = arb.pi(), acb(0, 1)
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, visited, primary = {}, set(), {}

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

    for stem in ("complete_boundary_coefficient_asymptotic",
                 "complete_boundary_complex_index",
                 "complete_boundary_full_index_interval"):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        inherit(path)
        record = json.loads((ROOT/path).read_text())
        assert record["status"] == "passed"
        assert record["script_sha256"] == bind("experiments/check_"+stem+".py")
        bind("notes/research_"+stem+".md")
        primary[path] = deps[path]
    for name in ("research_uniform_factorial_and_boundary_decay",
                 "research_free_boundary_cardinal_factorial_comparison",
                 "research_internal_pair_three_full_boundary_packet",
                 "research_finite_two_boundary_kernel_closure",
                 "research_mixed_complete_boundary_sum"):
        bind("notes/"+name+".md")
    checks = []

    def check(name, statement):
        assert statement, name
        checks.append(name)

    z, X = sp.symbols("z X")
    check("original critical cubic factors through the selected quadratic",
          sp.expand((z+sp.I)*(2*z*z-2*sp.I*z+X-1)
                    -(2*z**3+(X+1)*z+sp.I*(X-1))) == 0)
    s = sp.symbols("s")
    check("explicit square root satisfies the critical quadratic",
          sp.rem(sp.expand((2*z*z-2*sp.I*z+X-1).subs(z, (sp.I+s)/2)),
                 s*s-(1-2*X), s) == 0)
    check("low-row ratio has the claimed elementary lower bound",
          F(1, 2)*F(1, 4)*6**3*F(1, 2) == F(27, 2))
    check("pentagon quotient is below two thirds",
          (3*PI/10).cos()**2/(3*PI/10).sin()**3 < ar(F(2, 3)))
    check("upper-row exponential factor is below seven fifths",
          (ar(F(9, 100))*PI).exp()*(ar(F(9, 100))*PI).cosh() < ar(F(7, 5)))
    check("upper-row ratio below one", F(7, 5)*F(2, 3) == F(14, 15) < 1)
    check("left elementary sine and exponential bounds",
          (ar(F(7, 25))*PI).sin() > ar(F(1, 2))
          and (PI/20).sin() < ar(F(1, 6))
          and (PI/20).cos()**2 > ar(F(1, 4))
          and (-ar(F(2, 25))*PI).exp() > ar(F(1, 2)))
    check("lower-alias positive uniform coefficient",
          2*(F(1, 2)-F(47, 100)) == F(3, 50))
    check("Gaussian power is exact", 1-2-F(1, 2) == -F(3, 2))
    if old is not None:
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
        assert old["gap_floors"] == list(map(str, FLOORS))
        assert len(old["cases"]) == 2
    start = time.monotonic()
    records, total_leaves, total_visits = [], 0, 0
    for case_index, initial in enumerate(INITIAL):
        sign = -1 if case_index == 0 else 1
        stack = [(initial, 0)]
        saved = old["cases"][case_index] if old else None
        if saved:
            assert saved["initial_box"] == [[str(a), str(b)] for a, b in initial]
        nodes, cursor, leaves, visits, depthmax = [], 0, 0, 0, 0
        minimum = [None]*3
        u_hull = None
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
                axis = max(((hi-lo)/F(1, 1), j) for j, (lo, hi) in enumerate(box))[1]
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
        parameter_domains=2, accepted_cells=total_leaves, visited_cells=total_visits,
        cases=records, gap_floors=list(map(str, FLOORS)),
        critical_image_rectangle=["19/100", "7/25", "1/100", "1/10"],
        original_logarithmic_lift="zero, by exact cubic and imaginary lift in (-pi,pi)",
        exact_and_scalar_checks=len(checks), checks=checks,
        primary_records=primary, primary_record_count=len(primary),
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        input_sha256=ih, elapsed_seconds=time.monotonic()-start,
        scope="Outward scalar-gap and explicit-root image certificate on the full private-index rectangle. No source-row cover, no open-word critical-map theorem or noncancellation claim.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", total_leaves, "cells", total_visits, "visits",
          "seconds", result["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
