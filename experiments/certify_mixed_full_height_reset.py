#!/usr/bin/env python3
"""Full matrix height-reset cost with both real coordinates free."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_full_height_reset.md"
HELPER = ROOT/"experiments/certify_mixed_real_small_support.py"
spec = importlib.util.spec_from_file_location("full_reset_arithmetic", HELPER)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
U = {0: [".22", ".50", "-.03", ".02"], 1: [".22", ".50", "-.057", "0"]}
DEPS = [
    "experiments/certify_mixed_real_small_support.py",
    "notes/research_mixed_unselected_right_taper_products.md",
    "experiments/certify_mixed_right_square_conditional_packets.py",
    "repro/results/research-mixed-right-square-conditional-packets.json",
    "notes/research_mixed_fourier_weight_continuation.md",
    "notes/research_mixed_real_one_small_support.md",
    "experiments/certify_mixed_real_one_small_support.py",
    "repro/results/research-mixed-real-one-small-support.json",
    "notes/research_mixed_coupled_outer_graph.md",
    "experiments/check_mixed_coupled_outer_graph.py",
    "repro/results/research-mixed-coupled-outer-graph.json",
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def edge(rect, face, lo, hi):
    xl, xh, yl, yh = map(F, rect)
    t = core.ar(lo).union(core.ar(hi))
    if face in (0, 2):
        return acb(core.ar(xl)+core.ar(xh-xl)*t, core.ar(yl if face == 0 else yh))
    return acb(core.ar(xh if face == 1 else xl), core.ar(yl)+core.ar(yh-yl)*t)


def test(case, address, witness=None):
    eta, eps, fa, fb = case
    al, ah, bl, bh = core.box(address)
    a, b = edge(U[eta], fa, al, ah), edge(U[eps], fb, bl, bh)
    a0 = edge(U[eta], fa, (al+ah)/2, (al+ah)/2)
    b0 = edge(U[eps], fb, (bl+bh)/2, (bl+bh)/2)
    packet = core.root_box(a, b, a0, b0, eps, witness)
    if packet is None:
        return None
    s, _, wit = packet
    _, _, h = core.phase(s, a, b, eta, eps)
    A, C, D = -h[0][0].real, -h[0][1].real, -h[1][1].real
    E, Ff, G = h[0][0].imag, h[0][1].imag, h[1][1].imag
    det = A*D-C*C
    if not (A > 0 and D > 0 and det > 0):
        return None
    k00 = A+(D*E*E-2*C*E*Ff+A*Ff*Ff)/det
    k01 = C+(D*E*Ff-C*(E*G+Ff*Ff)+A*Ff*G)/det
    k11 = D+(D*Ff*Ff-2*C*Ff*G+A*G*G)/det
    r00, r01, r11 = 20-k00, -k01, 20-k11
    rd = r00*r11-r01*r01
    if not (r00 > 0 and r11 > 0 and rd > 0):
        return None
    # Positive determinant/trace gives a lower bound for the least eigenvalue.
    alow = (det/(A+D)).lower()
    rlow = (rd/(r00+r11)).lower()
    return wit, alow, rlow


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-mixed-full-height-reset.json")
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    core.pi, core.ii = arb.pi(), acb(0, 1)
    initial = {p: sha(ROOT/p) for p in DEPS}
    ph, sh = sha(PROOF), sha(__file__)
    for pi, si, ri in ((1, 2, 3), (5, 6, 7), (8, 9, 10)):
        rec = json.loads((ROOT/DEPS[ri]).read_text())
        assert rec["status"] == "passed"
        assert rec["script_sha256"] == initial[DEPS[si]]
        dep = rec.get("dependencies_sha256", rec.get("dependencies", {}))
        assert rec.get("proof_sha256", dep.get(DEPS[pi])) == initial[DEPS[pi]]
        assert all(sha(ROOT/p) == h for p, h in dep.items())
    aa, cc, dd, ee, ff, gg = sp.symbols("aa cc dd ee ff gg", real=True)
    u0, u1, v0, v1 = sp.symbols("u0 u1 v0 v1", real=True)
    Am = sp.Matrix([[aa, cc], [cc, dd]])
    Bm = sp.Matrix([[ee, ff], [ff, gg]])
    uu, vv = sp.Matrix([u0, u1]), sp.Matrix([v0, v1])
    lhs = -(uu.T*Am*uu)[0]-2*(uu.T*Bm*vv)[0]+(vv.T*Am*vv)[0]
    ww = uu+Am.inv()*Bm*vv
    rhs = -(ww.T*Am*ww)[0]+(vv.T*(Am+Bm*Am.inv()*Bm)*vv)[0]
    assert sp.cancel(lhs-rhs) == 0
    margin = F(11, 200)-10*F(57, 1000)**2
    assert margin == F(2251, 100000) > F(9, 400)
    assert F(9, 400)-F(1, 400) == F(1, 50)
    assert 3*F(57, 1000)*20 == F(171, 50)
    assert 1+F(171, 50)**2 < F(18, 5)**2
    patterns = 0
    for m in range(1, 10):
        for low in itertools.product((0, 1), repeat=m):
            if not any(low):
                continue
            reset = [not low[j] and (low[(j-1) % m] or low[(j+1) % m])
                     for j in range(m)]
            nlp = sum(low[j] != low[(j+1) % m] for j in range(m))
            nongapped_cost_count = sum(
                int(reset[j])+int(reset[(j+1) % m])
                for j in range(m) if not low[j] and not low[(j+1) % m])
            assert nongapped_cost_count <= nlp
            patterns += 1
    saved = json.loads(args.input.read_text()) if args.input else None
    expected = list(itertools.product((0, 1), (0, 1), range(4), range(4)))
    if saved:
        assert saved["status"] == "passed"
        assert saved["proof_sha256"] == ph and saved["script_sha256"] == sh
        assert saved["dependencies"] == initial
        assert [tuple(row["case"]) for row in saved["cases"]] == expected
    rows, total, visits = [], 0, 0
    leastA, leastR = None, None
    start = time.time()
    for idx, case in enumerate(expected):
        pending = [("", None)] if saved is None else [
            (x["address"], x["witness"]) for x in saved["cases"][idx]["leaves"]]
        if saved:
            core.cover([a for a, w in pending])
        leaves, visited = [], 0
        while pending:
            address, witness = pending.pop()
            visited += 1
            value = test(case, address, witness)
            if value is None:
                assert saved is None and len(address) < 28, (case, address)
                pending.extend(((address+"0", None), (address+"1", None)))
                continue
            wit, av, rv = value
            leastA = av if leastA is None else min(leastA, av)
            leastR = rv if leastR is None else min(leastR, rv)
            leaves.append({"address": address, "witness": wit})
        leaves.sort(key=lambda x: x["address"])
        core.cover([x["address"] for x in leaves])
        rows.append({"case": list(case), "leaves": leaves, "visited": visited})
        total += len(leaves)
        visits += visited
        print("case", list(case), len(leaves), flush=True)
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in initial.items())
    result = {
        "status": "passed", "precision_bits": args.precision,
        "domains": len(rows), "cells": total, "visits": visits,
        "min_negative_real_hessian_eigenvalue": str(leastA),
        "min_full_cost_reserve_eigenvalue": str(leastR),
        "matrix_cost_upper": 20, "integrated_cost_upper": 10,
        "parameter_rectangles": U, "cases": rows,
        "exact_matrix_identities": 1, "exact_scalar_checks": 4,
        "cyclic_incidence_patterns": patterns,
        "proof_sha256": ph, "script_sha256": sh, "dependencies": initial,
        "elapsed_seconds": time.time()-start,
        "scope": "Full two-coordinate real readjustment and arbitrary unselected height resets; compact low/plateau cluster consequence only. No near-zero uniform source, connecting contour, or selected complex-height bound.",
    }
    if saved:
        result["input_sha256"] = sha(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(rows), "domains", total, "cells; K<20I", flush=True)


if __name__ == "__main__":
    main()
