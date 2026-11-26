#!/usr/bin/env python3
"""Outward endpoint-gap certificate on 48 full harmonic boundary faces.

This checks closed cells, with an independent rational coverage sweep.
It does not promote parameter samples to a uniform inequality.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, acb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    root = Path(__file__).resolve().parents[1]
    pi, I = arb.pi(), acb(0, 1)
    target = F(1, 10000)

    def q(value):
        value = F(value)
        return arb(value.numerator)/value.denominator

    def interval(a, b):
        return arb(q((a+b)/2), q((b-a)/2))

    def J(z):
        z = acb(z)
        if not (0 < z.real < 1):
            raise ValueError("sine-primitive argument is not in its strip")
        return ((pi*pi/6-(2*pi*I*z).exp().polylog(2))/(2*pi*I)
                + I*pi*z*(1-z)/2)

    def b(x, t):
        return (-J(arb(1)/2-x+t/(2*pi))
                - J(arb(1)/2-x-t/(2*pi))-2*J(x))

    def critical(t, u):
        c, d = t.cos(), u.cos()
        C = (1-c*d)/(2+c+d)
        if not (-1 < C.real < 1):
            raise ValueError("inverse-cosine enclosing box meets its cuts")
        return C.acos()/(2*pi)

    def phase_difference(t, u, endpoint):
        x = critical(t, u)
        return (b(x, t)+b(x, u)-b(endpoint, t)-b(endpoint, u)).real

    def derivative(t, u, endpoint):
        w = (t/2).tan()
        z1 = (pi*endpoint).tan()*w
        z2 = w*(u/2).cos()
        if not ((-1 < z1.real < 1) or not z1.imag.contains(0)):
            raise ValueError("atanh argument enclosure meets a cut")
        if not (-1 < z2.imag < 1):
            raise ValueError("asinh argument enclosure meets a cut")
        return (z1.atanh()-z2.asinh())/pi

    def edge(lo, hi, number, s):
        if number == 0:
            return acb(lo, -q(F(3, 10))+q(F(3, 5))*s), I*q(F(3, 5))
        if number == 1:
            return acb(hi, -q(F(3, 10))+q(F(3, 5))*s), I*q(F(3, 5))
        if number == 2:
            return acb(lo+(hi-lo)*s, -q(F(3, 10))), acb(hi-lo)
        return acb(lo+(hi-lo)*s, q(F(3, 10))), acb(hi-lo)

    def critical_strip_margin(t, u):
        x = critical(t, u)
        zs = [x, arb(1)/2-x+t/(2*pi), arb(1)/2-x-t/(2*pi),
              arb(1)/2-x+u/(2*pi), arb(1)/2-x-u/(2*pi)]
        if not all(0 < z.real < 1 for z in zs):
            raise ValueError("critical factorial strip not certified")
        return min(min(z.real.lower(), (1-z.real).lower()) for z in zs)

    def verify_cover(cells):
        """Independent exact sweep, not merely a sum of cell areas."""
        boxes = [tuple(F(v) for v in cell["box"]) for cell in cells]
        xs = sorted({F(0), F(1)} | {b[i] for b in boxes for i in (0, 1)})
        assert xs[0] == 0 and xs[-1] == 1
        assert sum((B-a)*(d-c) for a, B, c, d in boxes) == 1
        for left, right in zip(xs, xs[1:]):
            mid = (left+right)/2
            ys = sorted((c, d) for a, B, c, d in boxes if a < mid < B)
            assert ys and ys[0][0] == 0
            end = F(0)
            for lower, upper in ys:
                assert lower == end and lower < upper
                end = upper
            assert end == 1

    patches = [
        ("0", q(0), q(F(23, 20)), q(F(3, 10)), "0", "23/20", "3/10"),
        ("1", q(F(11, 10)), q(F(7, 5)), q(F(27, 100)),
         "11/10", "7/5", "27/100"),
        ("2", q(F(27, 20)), pi/2, q(F(49, 200)),
         "27/20", "pi/2", "49/200"),
    ]
    records = []
    total_visited = total_accepted = 0
    for name, lo, hi, endpoint, lotext, hitext, btext in patches:
        assert arb(1)/2-endpoint-hi/(2*pi) > 0
        for first in range(4):
            for second in range(4):
                stack = [(F(0), F(1), F(0), F(1), 0)]
                cells = []
                visited = maxdepth = 0
                while stack:
                    a, B, c, d, depth = stack.pop()
                    visited += 1
                    t, v1 = edge(lo, hi, first, interval(a, B))
                    u, v2 = edge(arb(0), hi, second, interval(c, d))
                    t0, _ = edge(lo, hi, first, q((a+B)/2))
                    u0, _ = edge(arb(0), hi, second, q((c+d)/2))
                    try:
                        margin = critical_strip_margin(t, u)
                        center = phase_difference(t0, u0, endpoint)
                        g1 = (derivative(t, u, endpoint)*v1).real
                        g2 = (derivative(u, t, endpoint)*v2).real
                        enclosure = (center+g1*arb(0, q((B-a)/2))
                                     +g2*arb(0, q((d-c)/2)))
                        if enclosure > q(target):
                            cells.append({
                                "box": list(map(str, (a, B, c, d))),
                                "phase_difference_enclosure": str(enclosure),
                                "lower_bound": str(enclosure.lower()),
                                "critical_strip_margin": str(margin),
                            })
                            maxdepth = max(maxdepth, depth)
                            continue
                    except ValueError:
                        pass
                    assert depth < 28, (name, first, second, a, B, c, d)
                    if B-a >= d-c:
                        mid = (a+B)/2
                        stack.extend([(a, mid, c, d, depth+1),
                                      (mid, B, c, d, depth+1)])
                    else:
                        mid = (c+d)/2
                        stack.extend([(a, B, c, mid, depth+1),
                                      (a, B, mid, d, depth+1)])
                verify_cover(cells)
                total_visited += visited
                total_accepted += len(cells)
                records.append({
                    "patch": name, "t_real_interval": [lotext, hitext],
                    "u_real_interval": ["0", hitext], "wire_endpoint": btext,
                    "parameter_boundary_edges": [first, second],
                    "visited": visited, "accepted": len(cells),
                    "maximum_subdivision_depth": maxdepth,
                    "exact_cover_sweep": "passed", "cells": cells,
                })
    assert len(records) == 48
    # Branch and elementary covering constants used in the proof.
    rational_checks = {
        "C_lower_above_minus_one": 2-F(41, 40)-F(961, 20000),
        "asinh_imaginary_cut_margin": 1-F(11, 100)-F(3, 10)*F(51, 50),
        "low_middle_overlap": F(23, 20)-F(11, 10),
        "middle_high_overlap": F(7, 5)-F(27, 20),
    }
    assert all(v > 0 for v in rational_checks.values())
    branch_checks = {
        "cosh_angular_majorant": q(F(21, 20))-q(F(3, 10)).cosh(),
        "sinh_angular_majorant": q(F(31, 100))-q(F(3, 10)).sinh(),
        "cosine_half_majorant": q(F(51, 50))-q(F(3, 20)).cosh(),
        "cosine_half_imaginary_majorant":
            q(F(11, 100))-(pi/4).sin()*q(F(3, 20)).sinh(),
    }
    assert all(v > 0 for v in branch_checks.values())
    dependencies = [
        "experiments/certify_bare_kernel_wide_endpoint_gaps.py",
        "notes/research_bare_kernel_wide_endpoint_gaps.md",
        "notes/research_path_mixed_trace_currents.md",
        "notes/research_edge_hessian_and_phase_response.md",
    ]
    record = {
        "status": "certified", "precision_bits": ctx.prec,
        "strict_endpoint_gap": str(target), "faces": len(records),
        "visited_boxes": total_visited, "accepted_boxes": total_accepted,
        "scope": (
            "Full harmonic parameter-boundary faces and critical factorial "
            "strips. Separate harmonicity proves the complete complex-box "
            "endpoint gap. No finite-kernel asymptotic is inferred by this "
            "certificate alone."),
        "rational_margins": {k: str(v) for k, v in rational_checks.items()},
        "branch_interval_margins": {k: str(v) for k, v in branch_checks.items()},
        "face_certificates": records,
        "sha256": {p: sha256((root/p).read_bytes()).hexdigest()
                   for p in dependencies},
    }
    output = args.output or root/"repro/results/research-bare-kernel-wide-endpoint-gaps.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Certified {len(records)} complete boundary faces: "
          f"{total_accepted} accepted / {total_visited} visited boxes; "
          f"D > {target}; {args.precision} bits.")
    print(output)


if __name__ == "__main__":
    main()
