#!/usr/bin/env python3
"""Exact algebra and rational constants for the retained-vertex global bound.

The continuous entropy classification, finite-product upper bounds, and
Gaussian consequences are proved in the note. This script does not infer
an asymptotic theorem from sampled finite levels or sampled wire phases.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import factorial
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--precision", type=int, default=192)
    args = parser.parse_args()
    ctx.prec = args.precision
    identities = []
    comparisons = []

    def zero(name, expression):
        reduced = sp.simplify(expression)
        assert reduced == 0, (name, reduced)
        identities.append({"name": name, "difference": "0"})

    def positive(name, expression):
        reduced = sp.factor(expression)
        assert reduced.is_Rational and reduced > 0, (name, reduced)
        comparisons.append({"name": name, "positive_margin": str(reduced)})

    q = sp.Rational
    v = sp.Symbol("v", real=True)
    cubic = 8*v**3 + 4*v**2 - 6*v - 5
    polynomial = 16*v**4 - 16*v**2 - 4*v + 5
    zero("stationary polynomial factorization", polynomial - (2*v-1)*cubic)
    zero("squared stationarity difference",
         4*v**2*(1-v**2) - (q(5, 4)-v) + polynomial/4)
    zero("axis monotonicity square",
         (1-v**2) - (q(5, 4)-v) + (v-q(1, 2))**2)
    zero("cubic derivative", sp.diff(cubic, v) - (24*v**2+8*v-6))
    zero("cubic derivative discriminant", 8**2 - 4*24*(-6) - 640)
    critical = (sp.sqrt(10)-1)/6
    zero("positive cubic critical point", sp.diff(cubic, v).subs(v, critical))
    positive("positive critical point: sqrt(10)>1", sp.Integer(10)-1)
    positive("critical point below 1/2: sqrt(10)<4", sp.Integer(16)-10)
    positive("cubic negative at zero", -cubic.subs(v, 0))
    positive("cubic negative at one half", -cubic.subs(v, q(1, 2)))
    positive("cubic positive at one", cubic.subs(v, 1))
    positive("cubic derivative strictly increasing on nonnegative axis", sp.Integer(8))

    # c=3 sqrt(3) D3/(4 pi), with all omitted D3 blocks positive.
    d3_three = sum(q(1, (3*j+1)**2)-q(1, (3*j+2)**2) for j in range(3))
    positive("sqrt(3)>19/11", 3-q(19, 11)**2)
    c_lower = 3*q(19, 11)*d3_three/(4*q(22, 7))
    positive("three positive D3 blocks imply c>8/25", c_lower-q(8, 25))

    exp_seven_tenths_lower = sum(q(7, 10)**k/factorial(k) for k in range(5))
    positive("exp(7/10)>2 from first five terms", exp_seven_tenths_lower-2)
    # log 2 = 2 sum_{j>=0}(1/3)^(2j+1)/(2j+1).
    zero("first atanh term for log 2", 2*q(1, 3)-q(2, 3))
    positive("next atanh term makes log 2>2/3", 2*q(1, 3)**3/3)

    # For k>=3, 1/k^2<=1/9; sum_{k>=3}2^-k=1/4.
    li2_upper = q(1, 2)+q(1, 16)+q(1, 36)
    positive("Li2(1/2)<3/5", q(3, 5)-li2_upper)
    zero("top-edge coarse upper rate", -q(2, 3)+q(6, 15)+q(4, 15))
    positive("top-edge rate below -3/50", q(4, 15)-q(3, 50))
    zero("central entropy coarse lower rate", 2*q(8, 25)-q(7, 10)+q(3, 50))

    # e^2: after k=7 the ratio of consecutive terms is at most 1/4.
    e2_upper = sum(q(2)**k/factorial(k) for k in range(7))
    e2_upper += (q(2)**7/factorial(7))/(1-q(1, 4))
    positive("positive series with geometric tail gives exp(2)<15/2", q(15, 2)-e2_upper)
    positive("pi exp(2)<25 from rational bounds", 25-q(22, 7)*q(15, 2))
    positive("cut-face derivative ratio 2 pi/25<1", 1-2*q(22, 7)/25)
    positive("corner threshold below central indices", q(1, 3)-q(1, 50))

    # The polynomial derivative has one positive critical point, and
    # the sign comparisons above establish exactly one cubic root in
    # (1/2,1); that stationary point is a diagonal minimum.
    root_intervals = sp.polys.polytools.intervals(cubic, eps=q(1, 10**8))
    assert len(root_intervals) == 1 and root_intervals[0][1] == 1, root_intervals
    left, right = root_intervals[0][0]
    assert q(1, 2) < left < right < 1

    # Unequal-radius Hessians. Divide every Hessian by pi, so all
    # identities are exact in Q(sqrt(3)); no sampled height is used.
    sqrt3 = sp.sqrt(3)
    index_core = sp.Matrix([[2, 1], [1, 2]])
    ss = -index_core/sqrt3
    sv = -2*sp.eye(2)
    vv = 4*sp.eye(2)/sqrt3
    envelope_hessian = vv-sv.T*ss.inv()*sv
    for i in range(2):
        for j in range(2):
            zero(f"unequal-radius maximum Hessian entry {i}{j}",
                 envelope_hessian[i, j]-
                 (4*sp.Matrix([[3, -1], [-1, 3]])/sqrt3)[i, j])
    alpha, beta = 8*sqrt3/21, q(4, 7)
    zero("actual critical phase slope beta/alpha", beta/alpha-sqrt3/2)
    zero("actual height rate coefficient",
         (alpha**2+beta**2)/(2*alpha)-1/sqrt3)
    actual_hessian = (alpha+beta**2/alpha)*sp.Matrix([[5, -2], [-2, 5]])
    for i in range(2):
        for j in range(2):
            zero(f"positive modulus excess Hessian entry {i}{j}",
                 envelope_hessian[i, j]-actual_hessian[i, j]
                 -2*sp.eye(2)[i, j]/sqrt3)

    # The quantitative one-height bound reduces its full parameter
    # range analytically to these scalar endpoint comparisons.
    outward = []

    def ar(value):
        rational = sp.Rational(value)
        return arb(int(rational.p))/int(rational.q)

    def arb_positive(name, expression):
        assert expression > 0, (name, expression)
        outward.append({"name": name, "positive_margin": str(expression)})

    pi = arb.pi()
    d3_forty = sum(q(1, (3*j+1)**2)-q(1, (3*j+2)**2) for j in range(40))
    arb_positive("forty positive D3 blocks give c>323/1000",
                 3*arb(3).sqrt()*ar(d3_forty)/(4*pi)-ar(q(323, 1000)))
    arb_positive("log 2 below 347/500", ar(q(347, 500))-arb(2).log())
    positive("maximum g derivative below 2/5",
             q(2, 5)-(-1/(6*q(53, 100))+1/(3*(1-q(53, 100)))))
    zero("low-p global envelope bound", q(347, 500)-q(3, 50)+q(3, 100)*q(2, 5)-q(323, 500))
    arb_positive("height shift 9/1000 keeps radius below 53/100",
                 ar(q(53, 50)).log()-9*pi/500)
    arb_positive("lower square face derivative",
                 (ar(q(67, 100))*pi).sin()**2
                 -(ar(q(5, 4))-(ar(q(3, 10))*pi).cos()))
    arb_positive("upper square face derivative",
                 1+ar(q(53, 100))**2
                 -ar(q(106, 100))*(ar(q(37, 100))*pi).cos()
                 -ar(q(106, 100))**2*(ar(q(67, 100))*pi).sin()**2)
    arb_positive("cosine threshold for monotonic d and q",
                 ar(q(3, 5))-(ar(q(3, 10))*pi).cos())

    def dq(index, radius):
        angle, rad = ar(index)*pi, ar(radius)
        denominator = 1+rad*rad-2*rad*angle.cos()
        return pi*rad*angle.sin()/denominator, 2*pi*(1-rad*angle.cos())/denominator

    arb_positive("minimum d above 5/3", dq(q(37, 100), q(1, 2))[0]-ar(q(5, 3)))
    arb_positive("maximum d below 21/10", ar(q(21, 10))-dq(q(3, 10), q(53, 100))[0])
    arb_positive("maximum q below 27/4", ar(q(27, 4))-dq(q(3, 10), q(1, 2))[1])
    arb_positive("minimum k above one", -pi/(3*pi/5).tan()-1)
    c_exact = (acb(0, pi/3).exp().polylog(2).imag)/pi
    arb_positive("complete scalar upper c<161533/500000",
                 ar(q(161533, 500000))-c_exact)
    zero("Schur inverse upper budget",
         1/(q(5, 3)+q(5, 3)/(q(5, 3)+1))-q(24, 55))
    zero("height Hessian upper budget", q(42, 5)+q(27, 4)**2*q(24, 55)-q(3111, 110))
    positive("height Hessian below 29", 29-q(3111, 110))
    zero("quantitative envelope numerator",
         2*q(161533, 500000)+q(29, 2)*q(9, 1000)**2-q(1294613, 2000000))
    positive("uniform envelope below .6474", q(6474, 10000)-q(1294613, 2000000))
    zero("vertical-join comparison budget", q(19113, 10000)-q(6319, 5000)-q(6474, 10000)-q(1, 10000))
    arb_positive("certified attachment height within 9/1000",
                 ar(q(9, 1000))-
                 (arb(2).log()/(2*pi)-ar(q("0.101358689576302370861575311618"))+ar(q(1, 10**8))))

    root = Path(__file__).resolve().parents[1]
    paths = [Path(__file__).resolve(),
             root / "notes/research_three_vertex_global_wire_bound.md",
             root / "notes/research_traced_three_vertex_endpoint.md",
             root / "notes/research_three_vertex_local_composition.md",
             root / "notes/research_positive_three_crossing_cycle.md",
             root / "notes/research_three_cap_first_attachment.md"]
    record = {
        "status": "passed",
        "scope": "Exact polynomial identities and rational margins for the written global entropy proof; no sampled asymptotic or global source claim.",
        "exact_identity_count": len(identities),
        "exact_identities": identities,
        "rational_comparison_count": len(comparisons),
        "rational_comparisons": comparisons,
        "precision_bits": ctx.prec,
        "outward_scalar_comparison_count": len(outward),
        "outward_scalar_comparisons": outward,
        "exact_cubic_real_root_isolation": {
            "lower": str(left), "upper": str(right), "multiplicity": 1,
            "other_real_roots": 0},
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in paths},
    }
    output = args.output or root / "repro/results/research-three-vertex-global-wire-bound.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {len(identities)} exact identities, {len(comparisons)} rational comparisons, "
          f"{len(outward)} outward scalar comparisons, and exact cubic isolation.\n{output}")


if __name__ == "__main__":
    main()
