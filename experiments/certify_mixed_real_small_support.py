#!/usr/bin/env python3
"""Real both-small conditional sources versus complex reference planes.

Rational root proposals carry no acceptance authority.  All 64 distinguished
boundary products and all four affine target corners are checked outward.
"""
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_real_small_support.md"
RECTS = {0: [".30", ".39", "-.03", ".02"],
         1: [".27", ".33", "-.057", "-.02"]}
DEPS = [
    "notes/research_mixed_real_outer_support.md",
    "experiments/check_mixed_real_outer_support.py",
    "repro/results/research-mixed-real-outer-support.json",
    "notes/research_mixed_central_conditional_rectangles.md",
    "experiments/certify_mixed_central_conditional_rectangles.py",
    "repro/results/research-mixed-central-conditional-rectangles.json",
    "notes/research_mixed_type_four_height_refinement.md",
    "notes/research_mixed_type_three_window_strip.md",
    "notes/research_mixed_global_cotangent_roots.md",
    "experiments/check_mixed_global_cotangent_roots.py",
    "repro/results/research-mixed-global-cotangent-roots.json",
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ar(q):
    q = F(q)
    return arb(q.numerator) / q.denominator


def g(z):
    return ((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)


def gp(z):
    return (1-(-2*pi*ii*z).exp()).log()


def gpp(z):
    return pi*(pi*z).cot()-pi*ii


def equation(s, a, b, eps):
    return gp(s+a)+gp(s+b)-(2+eps)*gp(s)+2*pi*ii*a


def second(s, a, b, eps):
    return gpp(s+a)+gpp(s+b)-(2+eps)*gpp(s)


def point(z):
    return acb(ar(str(z.real)), ar(str(z.imag)))


def proposal(a, b, eps):
    a, b = complex(float(a.real.mid()), float(a.imag.mid())), complex(float(b.real.mid()), float(b.imag.mid()))
    p, q = 1/np.tan(np.pi*a), 1/np.tan(np.pi*b)
    coeffs = [1, p+q, -1+1j*(q-p)] if eps == 0 else [1, p+q+1j, p*q+1j*(p+q), 1j*p*q-2j*(p-1j)*(q+1j)]
    roots = [z for z in np.roots(coeffs) if z.real > 0 and abs(z.imag) < 1]
    if len(roots) != 1:
        return None
    z = np.log((roots[0]+1j)/(roots[0]-1j))/(2j*np.pi)
    return [str(z.real), str(z.imag)]


def point_root(a, b, eps, center=None):
    center = proposal(a, b, eps) if center is None else center
    if center is None:
        return None
    c = acb(ar(center[0]), ar(center[1]))
    Y = 1/second(c, a, b, eps)
    r = ar("1e-12")
    z = c+acb(arb(0, r), arb(0, r))
    if not abs(Y*equation(c, a, b, eps))+abs(1-Y*second(z, a, b, eps))*r < r:
        return None
    S = (pi*z).cot()
    if not (S.real > 0 and abs(S.imag) < 1):
        return None
    if not all(0 < w.real < 1 for w in (z, z+a, z+b)):
        return None
    return z, center


def root_box(a, b, a0, b0, eps, witness=None):
    center = proposal(a0, b0, eps) if witness is None else witness["center"]
    if center is None:
        return None
    z0 = acb(ar(center[0]), ar(center[1]))
    H0 = second(z0, a0, b0, eps)
    Y = 1/H0
    E = [gpp(z0+a0)+2*pi*ii, gpp(z0+b0)]
    dp = [a-a0, b-b0]
    if witness is None:
        dd = [[str(float((-Y*e).real.mid())), str(float((-Y*e).imag.mid()))] for e in E]
    else:
        dd = witness["derivatives"]
    deriv = [acb(ar(v[0]), ar(v[1])) for v in dd]
    dz = sum((deriv[j]*dp[j] for j in (0, 1)), acb(0))
    lin = equation(z0, a0, b0, eps)+sum(((H0*deriv[j]+E[j])*dp[j] for j in (0, 1)), acb(0))

    def rem(base, delta):
        w = base+acb(arb(0, abs(delta.real).upper()), arb(0, abs(delta.imag).upper()))
        if not 0 < w.real < 1:
            return arb.pos_inf()
        return pi*pi*abs(1/(pi*w).sin()**2)*abs(delta)**2/2

    err = abs(Y)*(abs(lin)+rem(z0+a0, dz+dp[0])+rem(z0+b0, dz+dp[1])+(2+eps)*rem(z0, dz))
    if not err.is_finite():
        return None
    radius = F(witness["radius"]) if witness is not None else F(max(1, math.ceil(float(err.upper())*1.5*2**42)), 2**42)
    if radius > F(1, 20):
        return None
    delta = dz+acb(arb(0, ar(radius)), arb(0, ar(radius)))
    z = z0+delta
    if not (ar(".2") < z.real < ar(".46") and abs(z.imag) < ar(".17")):
        return None
    if not all(0 < w.real < 1 for w in (z, z+a, z+b)):
        return None

    def dc(base, move):
        return -pi*(pi*move).sin()/((pi*base).sin()*(pi*(base+move)).sin())

    defect = 1-Y*H0-Y*(dc(z0+a0, delta+dp[0])+dc(z0+b0, delta+dp[1])-(2+eps)*dc(z0, delta))
    if not err+abs(defect)*ar(radius) < ar(radius):
        return None
    pr = point_root(a0, b0, eps, center)
    if pr is None:
        return None
    return z, pr[0], {"center": center, "derivatives": dd, "radius": str(radius)}


def phase(z, a, b, eta, eps):
    ca, cb = 1+ar(F(eta, 2)), 1+ar(F(eps, 2))
    value = g(z+a)+g(z+b)-(2+eps)*g(z)+2*pi*ii*a*z-ca*g(a)-cb*g(b)
    grad = [gp(z+a)+2*pi*ii*z-ca*gp(a), gp(z+b)-cb*gp(b)]
    sa, sb, ss = gpp(z+a)+2*pi*ii, gpp(z+b), second(z, a, b, eps)
    Hess = [[gpp(z+a)-ca*gpp(a)-sa*sa/ss, -sa*sb/ss],
            [-sa*sb/ss, gpp(z+b)-cb*gpp(b)-sb*sb/ss]]
    return value, grad, Hess


def box(address):
    result = [F(0), F(1), F(0), F(1)]
    for j, digit in enumerate(address):
        assert digit in "01"
        k = 2*(j % 2)
        midpoint = (result[k]+result[k+1])/2
        result[k+1-int(digit)] = midpoint
    return result


def cover(addresses):
    a = sorted(addresses)
    assert len(set(a)) == len(a)
    assert all(not y.startswith(x) for x, y in zip(a, a[1:]))
    assert sum((F(1, 2**len(x)) for x in a), F(0)) == 1


def edge(kind, face, lo, hi):
    xl, xh, yl, yh = map(F, RECTS[kind])
    t = ar(lo).union(ar(hi))
    if face in (0, 2):
        return acb(ar(xl)+ar(xh-xl)*t, ar(yl if face == 0 else yh))
    return acb(ar(xh if face == 1 else xl), ar(yl)+ar(yh-yl)*t)


def velocity(kind, face):
    xl, xh, yl, yh = map(F, RECTS[kind])
    return acb(ar(xh-xl)) if face in (0, 2) else ii*ar(yh-yl)


def test(case, address, tangents, witness=None):
    eta, eps, fa, fb = case
    al, ah, bl, bh = box(address)
    a, b = edge(eta, fa, al, ah), edge(eps, fb, bl, bh)
    a0, b0 = edge(eta, fa, (al+ah)/2, (al+ah)/2), edge(eps, fb, (bl+bh)/2, (bl+bh)/2)
    rb = root_box(a, b, a0, b0, eps, witness)
    if rb is None:
        return None
    z, z0, wit = rb
    v0, d0, _ = phase(z0, a0, b0, eta, eps)
    _, _, H = phase(z, a, b, eta, eps)
    rad = [ar((ah-al)/2), ar((bh-bl)/2)]
    vel = [velocity(eta, fa), velocity(eps, fb)]
    worst = None
    for target in itertools.product((F(0), F(3, 20)), repeat=2):
        t = list(map(ar, target))
        plane = v0+d0[0]*(t[0]-a0)+d0[1]*(t[1]-b0)
        upper = tangents[eta, eps][target]-plane.real
        for k in (0, 1):
            derivative = H[0][k]*(t[0]-a)+H[1][k]*(t[1]-b)
            upper += abs((derivative*vel[k]).real)*rad[k]
        if not upper < ar("-1/25"):
            return None
        worst = upper.upper() if worst is None else max(worst, upper.upper())
    return wit, worst


def main():
    global pi, ii
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT/"repro/results/research-mixed-real-small-support.json")
    args = parser.parse_args()
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)
    initial = {p: sha(ROOT/p) for p in DEPS}
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    for j in (0, 3, 8):
        rec = json.loads((ROOT/DEPS[j+2]).read_text())
        assert rec["status"] == "passed"
        assert rec["proof_sha256"] == initial[DEPS[j]] and rec["script_sha256"] == initial[DEPS[j+1]]
        for key in ("dependencies", "dependencies_sha256"):
            for path, digest in rec.get(key, {}).items():
                assert sha(ROOT/path) == digest, path
    for rect in RECTS.values():
        xl, xh, yl, yh = rect
        z = acb(ar(xl).union(ar(xh)), ar(yl).union(ar(yh)))
        cot = (pi*z).cot()
        assert cot.real > 0 and abs(cot.imag) < ar("1/2")
    source = json.loads(args.input.read_text()) if args.input else None
    if source:
        assert source["status"] == "passed" and source["rectangles"] == {str(k): v for k, v in RECTS.items()}
        assert source["proof_sha256"] == proof_hash and source["script_sha256"] == script_hash
        assert source["dependencies"] == initial
    tangents, real_roots = {}, []
    c = acb(ar("3/20"))
    for eps in (0, 1):
        r = point_root(c, c, eps, None if source is None else source["real_roots"][eps])
        assert r is not None
        z, center = r
        real_roots.append(center)
        for eta in (0, 1):
            val, grad, _ = phase(z, c, c, eta, eps)
            tangents[eta, eps] = {t: (val+sum((grad[k]*(ar(t[k])-c) for k in (0, 1)), acb(0))).real
                                 for t in itertools.product((F(0), F(3, 20)), repeat=2)}
    cases, counts, worst = [], 0, None
    expected = list(itertools.product((0, 1), (0, 1), range(4), range(4)))
    if source:
        assert [tuple(x["case"]) for x in source["cases"]] == expected
    for idx, case in enumerate(expected):
        leaves, visited = [], 0
        pending = [("", None)] if source is None else [(x["address"], x["witness"]) for x in source["cases"][idx]["leaves"]]
        if source:
            cover([x[0] for x in pending])
        while pending:
            address, witness = pending.pop()
            visited += 1
            result = test(case, address, tangents, witness)
            if result is None:
                assert source is None and len(address) < 28, (case, address)
                pending.extend([(address+"0", None), (address+"1", None)])
                continue
            wit, upper = result
            leaves.append({"address": address, "witness": wit})
            worst = upper if worst is None else max(worst, upper)
        leaves.sort(key=lambda x: x["address"])
        cover([x["address"] for x in leaves])
        counts += len(leaves)
        cases.append({"case": list(case), "visited": visited, "leaves": leaves})
    assert initial == {p: sha(ROOT/p) for p in DEPS}
    assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
    record = {"status": "passed", "precision_bits": args.precision,
              "scope": "Real target arguments in (0,.15]^2 only; compact-away-zero finite-source bounds. No complex-taper or whole-word conclusion.",
              "rectangles": RECTS, "domains": len(cases), "cells": counts,
              "target_corner_tests": 4*counts, "worst_defect_upper": str(worst),
              "real_roots": real_roots, "cases": cases,
              "proof_sha256": proof_hash, "script_sha256": script_hash, "dependencies": initial}
    if source:
        record["input_sha256"] = sha(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print("PASS", len(cases), "domains", counts, "cells", "worst", worst)


if __name__ == "__main__":
    main()
