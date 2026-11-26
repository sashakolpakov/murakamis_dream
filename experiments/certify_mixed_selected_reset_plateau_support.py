#!/usr/bin/env python3
"""One real reset and one selected plateau argument, with both forcing branches.

Optimizers propose rational target points only. Acceptance uses original-log
Newton maps, full source bindings, strong target concavity and exact covers.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.special import spence
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_selected_reset_plateau_support.md"
HELPER = ROOT/"experiments/certify_mixed_real_small_support.py"
spec = importlib.util.spec_from_file_location("reset_selected_original_log", HELPER)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
ar = core.ar
PATTERNS = [(0, 1, 1), (1, 1, 1), (1, 0, 0), (1, 1, 0)]
LOW, HIGH, HEIGHT = F(11, 50), F(9, 20), F(7, 500)
DEPS = [
    "experiments/certify_mixed_real_small_support.py",
    "notes/research_mixed_selected_right_taper_support.md",
    "experiments/certify_mixed_selected_right_taper_support.py",
    "repro/results/research-mixed-selected-right-taper-support.json",
    "notes/research_mixed_unselected_right_taper_products.md",
    "experiments/certify_mixed_right_square_conditional_packets.py",
    "repro/results/research-mixed-right-square-conditional-packets.json",
    "notes/research_mixed_fourier_weight_continuation.md",
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def float_phase(a, b, eta, eps):
    p, q = 1/np.tan(np.pi*a), 1/np.tan(np.pi*b)
    co = [1, p+q, -1+1j*(q-p)] if not eps else [1, p+q+1j, p*q+1j*(p+q), 1j*p*q-2j*(p-1j)*(q+1j)]
    roots = [z for z in np.roots(co) if z.real > 0 and abs(z.imag) < 1]
    if len(roots) != 1:
        raise ValueError("root proposal")
    s = np.log((roots[0]+1j)/(roots[0]-1j))/(2j*np.pi)
    g = lambda z: (spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)
    gp = lambda z: np.log(1-np.exp(-2j*np.pi*z))
    val = g(s+a)+g(s+b)-(2+eps)*g(s)+2j*np.pi*a*s-(1+eta/2)*g(a)-(1+eps/2)*g(b)
    grad = np.array([gp(s+a)+2j*np.pi*s-(1+eta/2)*gp(a), gp(s+b)-(1+eps/2)*gp(b)])
    return val, grad


def target_proposal(a0, b0, eta, eps, selected, forcing):
    refs = np.array([complex(float(w.real.mid()), float(w.imag.mid())) for w in (a0, b0)])
    value, grad = float_phase(*refs, eta, eps)
    g = lambda z: (spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)
    gp = lambda z: np.log(1-np.exp(-2j*np.pi*z))

    def objective(x):
        z = np.array(x, dtype=complex)
        z[selected] += .014j
        val, der = float_phase(*z, eta, eps)
        val += forcing*g(z[selected])/2+1j*np.pi*(1-forcing)*z[selected]
        der[selected] += forcing*gp(z[selected])/2+1j*np.pi*(1-forcing)
        return -(val-value-grad@(z-refs)).real, -(der-grad).real

    opt = minimize(objective, np.clip(refs.real, float(LOW), float(HIGH)),
                   jac=True, bounds=[(float(LOW), float(HIGH))]*2,
                   method="L-BFGS-B", options={"ftol": 1e-14, "gtol": 1e-10, "maxiter": 60})
    return [str(float(x)) for x in opt.x]


def quadratic_upper(gradient, lo, hi):
    """Upper bound for max_{d in [lo,hi]} gd-(5/8)d^2, 0 in interval."""
    lam = ar("5/4")
    vals = [arb(0)]
    for g in (gradient.lower(), gradient.upper()):
        if g < lam*ar(lo):
            value = g*ar(lo)-lam*ar(lo)**2/2
        elif g > lam*ar(hi):
            value = g*ar(hi)-lam*ar(hi)**2/2
        else:
            value = g*g/(2*lam)
        vals.append(value.upper())
    return max(vals)


def test(case, address, witness=None):
    eta, eps, selected, forcing, fa, fb = case
    al, ah, bl, bh = core.box(address)
    a, b = core.edge(eta, fa, al, ah), core.edge(eps, fb, bl, bh)
    a0 = core.edge(eta, fa, (al+ah)/2, (al+ah)/2)
    b0 = core.edge(eps, fb, (bl+bh)/2, (bl+bh)/2)
    root = core.root_box(a, b, a0, b0, eps, None if witness is None else witness["reference_root"])
    if root is None:
        return None
    s, s0, ref_witness = root
    try:
        cc = target_proposal(a0, b0, eta, eps, selected, forcing) if witness is None else witness["target_point"]
    except ValueError:
        return None
    c = list(map(F, cc))
    assert all(LOW <= x <= HIGH for x in c)
    target = [acb(ar(x)) for x in c]
    target[selected] += core.ii*ar(HEIGHT)
    target_root = core.point_root(*target, eps, None if witness is None else witness["target_root"])
    if target_root is None:
        return None
    st, target_witness = target_root
    if not (ar(".1") < st.real < ar(".49") and abs(st.imag) < ar(".17")):
        return None
    tv, tg, _ = core.phase(st, *target, eta, eps)
    tv += ar(F(forcing, 2))*core.g(target[selected])+core.pi*core.ii*(1-forcing)*target[selected]
    tg[selected] += ar(F(forcing, 2))*core.gp(target[selected])+core.pi*core.ii*(1-forcing)
    rv0, rg0, _ = core.phase(s0, a0, b0, eta, eps)
    _, rg, Hess = core.phase(s, a, b, eta, eps)
    center = (tv-rv0-rg0[0]*(target[0]-a0)-rg0[1]*(target[1]-b0)).real
    cost = arb(0)
    for k, (kind, face, radius) in enumerate(((eta, fa, (ah-al)/2), (eps, fb, (bh-bl)/2))):
        derivative = Hess[0][k]*(target[0]-a)+Hess[1][k]*(target[1]-b)
        cost += abs((derivative*core.velocity(kind, face)).real)*ar(radius)
    support = sum((quadratic_upper((tg[j]-rg[j]).real, LOW-c[j], HIGH-c[j]) for j in (0, 1)), arb(0))
    upper = center+cost+support
    if not upper < ar("-1/100"):
        return None
    return {"reference_root": ref_witness, "target_point": list(map(str, c)), "target_root": target_witness}, upper.upper()


def validate(record, proof, script):
    rec = json.loads((ROOT/record).read_text())
    assert rec["status"] == "passed"
    assert rec["proof_sha256"] == sha(ROOT/proof) and rec["script_sha256"] == sha(ROOT/script)
    seen = {}
    for key in ("dependencies", "dependencies_sha256"):
        for p, h in rec.get(key, {}).items():
            if p in seen:
                assert seen[p] == h
            assert sha(ROOT/p) == h, p
            seen[p] = h


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT/"repro/results/research-mixed-selected-reset-plateau-support.json")
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    core.pi, core.ii = arb.pi(), acb(0, 1)
    initial = {p: sha(ROOT/p) for p in DEPS}
    ph, sh = sha(PROOF), sha(__file__)
    validate(DEPS[3], DEPS[1], DEPS[2])
    validate(DEPS[6], DEPS[4], DEPS[5])
    input_hash = sha(args.input) if args.input else None
    saved = json.loads(args.input.read_text()) if args.input else None
    expected = [tuple(pattern)+(forcing, fa, fb) for pattern in PATTERNS
                for forcing, fa, fb in itertools.product((0, 1), range(4), range(4))]
    if saved:
        assert saved["status"] == "passed"
        assert saved["proof_sha256"] == ph and saved["script_sha256"] == sh
        assert saved["dependencies"] == initial
        assert [tuple(row["case"]) for row in saved["cases"]] == expected
    rows, cells, visits, worst = [], 0, 0, None
    for idx, case in enumerate(expected):
        pending = [("", None)] if saved is None else [(v["address"], v["witness"]) for v in saved["cases"][idx]["leaves"]]
        if saved:
            core.cover([a for a, _ in pending])
        leaves = []
        while pending:
            address, witness = pending.pop()
            visits += 1
            value = test(case, address, witness)
            if value is None:
                assert saved is None and len(address) < 26, (case, address)
                pending.extend([(address+"0", None), (address+"1", None)])
                continue
            wit, upper = value
            leaves.append({"address": address, "witness": wit})
            worst = upper if worst is None else max(worst, upper)
        leaves.sort(key=lambda v: v["address"])
        core.cover([v["address"] for v in leaves])
        cells += len(leaves)
        rows.append({"case": list(case), "leaves": leaves})
    assert initial == {p: sha(ROOT/p) for p in DEPS}
    assert ph == sha(PROOF) and sh == sha(__file__)
    if args.input:
        assert input_hash == sha(args.input)
    result = {"status": "passed", "precision_bits": args.precision,
              "domains": len(rows), "cells": cells, "visits": visits,
              "patterns": PATTERNS, "forcing_branches_per_pattern": 2,
              "target_interval": [str(LOW), str(HIGH)], "selected_height": str(HEIGHT),
              "target_concavity": "5/4", "phase_gap": "1/100", "finite_source_gap": "1/200",
              "worst_defect_upper": str(worst), "cases": rows,
              "proof_sha256": ph, "script_sha256": sh, "dependencies": initial,
              "scope": "One real-reset plateau leg and one selected+.014 plateau leg, all typed orientations and both true Fourier branches. No full selected-cluster assembly claimed."}
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(rows), "products", cells, "cells", visits, "visits; worst", worst)


if __name__ == "__main__":
    main()
