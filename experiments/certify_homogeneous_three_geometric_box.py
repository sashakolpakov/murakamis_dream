#!/usr/bin/env python3
"""Enclose derivatives of the original power-three geometric neighbor map.

The map solves one original logarithmic period equation. This program
checks a compact parameter box by outward arithmetic; it makes no
statement about quantum coefficients or integration contours.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx


def rat(value):
    value = Q(value)
    return arb(value.numerator) / value.denominator


def interval(left, right):
    return rat((left + right) / 2) + arb(0, rat((right - left) / 2))


def angle(box):
    a, b, c, d = box
    return acb(interval(a, b), -interval(c, d))


def split(box):
    a, b, c, d = box
    if (b - a) / Q(13, 25) >= (d - c) / Q(39, 100):
        mid = (a + b) / 2
        return [(a, mid, c, d), (mid, b, c, d)]
    mid = (c + d) / 2
    return [(a, b, c, mid), (a, b, mid, d)]


def parts(t, u):
    v = (t / 2).tan()
    cu = (u / 2).cos()
    root = (1 + v*v*cu*cu).sqrt()
    return (
        cu*(1+v*v)/(2*root),
        -v*(u/2).sin()/(2*root),
        (v*cu).asinh(),
    )

def enclosed_parts(t, u):
    """First-order holomorphic mean-value enclosures on a product rectangle."""
    tm = acb(t.real.mid(), t.imag.mid())
    um = acb(u.real.mid(), u.imag.mid())
    dt, du = t-tm, u-um
    rt0, ru0, r0 = parts(tm, um)
    rt, ru, _ = parts(t, u)
    v = (t/2).tan()
    cu, su = (u/2).cos(), (u/2).sin()
    s = (1+v*v*cu*cu).sqrt()
    rtt = cu*v*(1+v*v)/(2*s)-cu**3*v*(1+v*v)**2/(4*s**3)
    rtu = -su*(1+v*v)/(4*s**3)
    ruu = -v*cu*(1+v*v)/(4*s**3)
    return (
        rt0+rtt*dt+rtu*du,
        ru0+rtu*dt+ruu*du,
        r0+rt*dt+ru*du,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=128)
    parser.add_argument("--mesh", type=int, default=16)
    parser.add_argument("--max-boxes", type=int, default=10000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    domain = (Q(13,10), Q(91,50), Q(41,50), Q(121,100))
    a, b, c, d = domain
    mesh = args.mesh
    neighbors = [
        (a+(b-a)*i/mesh, a+(b-a)*(i+1)/mesh,
         c+(d-c)*j/mesh, c+(d-c)*(j+1)/mesh)
        for i in range(mesh) for j in range(mesh)
    ]
    queue = [domain]
    accepted = []
    started = time.monotonic()
    visits = 0
    ii = acb(0, 1)
    while queue:
        box = queue.pop()
        t = angle(box)
        rt_hull = None
        local_parts = []
        for ub in neighbors:
            rt, ru, ret = enclosed_parts(t, angle(ub))
            local_parts.append((rt, ru, ret))
            rt_hull = rt if rt_hull is None else acb(
                rt_hull.real.union(rt.real), rt_hull.imag.union(rt.imag))
        rt_complete, _, complete_return = enclosed_parts(t, acb(0))
        margin = None
        passed = True
        for rt, ru, ret in local_parts:
            checks = [
                ret.real,
                rat(Q(3,5)) + ret.imag,
                -ret.imag,
            ]
            for other in (rt_hull, rt_complete):
                denominator = 3 + 2*ii*(rt+other)
                derivative = -2*ii*ru/denominator
                checks.extend([
                    denominator.real,
                    derivative.real,
                    rat(Q(1,4))-derivative.real,
                    rat(Q(1,16))-derivative.imag,
                    rat(Q(1,16))+derivative.imag,
                ])
            if not all(v > 0 for v in checks):
                passed = False
                break
            lower = min(v.lower() for v in checks)
            margin = lower if margin is None else min(margin, lower)
        visits += 1
        if passed:
            accepted.append({
                "box": [str(v) for v in box],
                "positive_margin": str(margin),
                "other_neighbor_t_derivative": str(rt_hull),
            })
        else:
            queue.extend(split(box))
        if visits % 100 == 0:
            print(f"visited {visits}, accepted {len(accepted)}, pending {len(queue)}, seconds {time.monotonic()-started:.1f}", flush=True)
        if visits >= args.max_boxes:
            raise RuntimeError(f"Unfinished certificate: {len(queue)} boxes pending")
    result = {
        "status": "passed",
        "precision_bits": args.precision,
        "domain_real_angle_height": [str(v) for v in domain],
        "neighbor_mesh": mesh,
        "scope": "Original one-vertex implicit derivatives: 0<Re T_u<1/4, |Im T_u|<1/16 for a finite neighbor, with the other neighbor finite or complete; selected-selected returns have -3/5<Im r<0 and Re r>0. No global fixed point or quantum conclusion is asserted by this record alone.",
        "visited": visits,
        "accepted": accepted,
        "sha256": {str(Path(__file__).name): hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    output = args.output or Path(__file__).resolve().parents[1]/"repro/results/research-homogeneous-three-geometric-box.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Passed {len(accepted)} boxes in {time.monotonic()-started:.1f}s. {output}", flush=True)


if __name__ == "__main__":
    main()
