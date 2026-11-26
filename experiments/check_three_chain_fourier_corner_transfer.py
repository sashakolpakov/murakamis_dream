#!/usr/bin/env python3
"""Check the algebra and constants in the Fourier-boundary corner transfer.

The all-level matrix, Fourier, and interpolation estimates are written
proofs. No asymptotic is inferred from a finite-level numerical sample.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    checks = []

    def rational(q):
        q = Q(q)
        return arb(q.numerator)/q.denominator

    def positive(name, margin):
        assert margin > 0, (name, margin)
        checks.append({"name": name, "positive_margin": str(margin)})

    v = sp.symbols("v")
    assert sp.expand(1-v*v-(sp.Rational(5, 4)-v)+(v-sp.Rational(1, 2))**2) == 0

    # Even final index gives an upper alternating partial sum for Catalan.
    catalan_upper = sum(((-1)**j)*Q(1, (2*j+1)**2) for j in range(101))
    positive("Catalan alternating upper sum below 11/12", Q(11, 12)-catalan_upper)
    pi = arb.pi()
    positive("pi exceeds 157/50", pi-rational(Q(157, 50)))
    positive("log 2 below 347/500", rational(Q(347, 500))-arb(2).log())
    c = acb(0, pi/3).exp().polylog(2).imag/pi
    positive("calibrated c below 161533/500000", rational(Q(161533, 500000))-c)
    positive("corner rate below two c", 2*c-rational(Q(3, 25)))
    upper = Q(161533, 250000)+Q(275, 471)+Q(3, 25)+Q(347, 1000)
    positive("mixed Fourier endpoint error below 17/10", Q(17, 10)-upper)
    positive("first-attachment action reserve above 1/5", Q(19113, 10000)-Q(17, 10)-Q(1, 5))
    positive("sigma below 3/25", rational(Q(3, 25))-(arb(100).log()+1)/50)
    positive("larger corner sigma below 27/200", rational(Q(27, 200))-(arb(80).log()+1)/40)
    positive("larger corner sigma below two c", 2*c-rational(Q(27, 200)))
    positive("larger mixed endpoint error below 343/200", Q(343, 200)-(upper-Q(3, 25)+Q(27, 200)))
    positive("larger corner first-attachment reserve above 19/100", Q(19113, 10000)-Q(343, 200)-Q(19, 100))
    gap = Q(3, 25)+Q(1, 15)-Q(27, 200)
    assert gap == Q(31, 600)
    positive("larger corner complete-ended gap above 1/20", gap-Q(1, 20))

    root = Path(__file__).resolve().parents[1]
    paths = [Path(__file__).resolve(),
             root/"notes/research_three_chain_fourier_corner_transfer.md",
             root/"notes/research_traced_three_vertex_endpoint.md",
             root/"notes/research_positive_three_crossing_cycle.md",
             root/"notes/research_three_vertex_global_wire_bound.md",
             root/"notes/research_three_cap_first_attachment.md"]
    record = {
        "status": "passed", "precision_bits": ctx.prec,
        "scope": "Exact axis identity and strict scalar budgets for the written full-period Fourier-boundary corner-error theorem. No full retained-attachment asymptotic is inferred by this check.",
        "exact_axis_identity_count": 1,
        "comparison_count": len(checks), "comparisons": checks,
        "catalan_upper_partial_sum": str(catalan_upper),
        "first_attachment_error_upper": str(upper),
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in paths},
    }
    output = args.output or root/"repro/results/research-three-chain-fourier-corner-transfer.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed one exact axis identity and {len(checks)} strict comparisons.\n{output}")


if __name__ == "__main__":
    main()
