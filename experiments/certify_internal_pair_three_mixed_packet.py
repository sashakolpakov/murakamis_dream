#!/usr/bin/env python3
"""Outward trace-first certificates for the original mixed power-three packet.

Only the fixed internal wire is polarized. The outer wire and complete trace
retain the original nineteen contour surfaces, with a single wire penalty.
The finite-source passage is a separate mathematical proof.
"""

import argparse
import hashlib
import json
import platform
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp
import flint
from flint import acb, acb_poly, arb, ctx

import certify_terminal_three_central_phase as e

ALPHA, BETA, ANGLE = Q(1, 32), Q(15, 32), Q(39, 20)
BASE_PHASE, BASE_GRADIENT, BASE_HESSIAN = e.phase, e.gradient, e.hessian
BASE_BOUND_AFFINE = e.bound_affine


def setup(precision):
    ctx.prec = precision
    mp.mp.dps = 80
    c0 = mp.findroot(lambda c: 4*c**3-4j*c**2-4*c+1j, .82+.34j)
    center = acb(mp.nstr(c0.real, 80), mp.nstr(c0.imag, 80)).mid()
    p = acb_poly([acb(0, 1), -4, acb(0, -4), 4])
    translated = p(acb_poly([center, 1]))
    radius = arb(2)**(-80)
    error = abs(translated[0]) + sum(
        abs(translated[j])*radius**j for j in range(2, len(translated)))
    linear = abs(translated[1])*radius
    assert error < linear
    c = acb(center.real + arb(0, radius), center.imag + arb(0, radius))
    e.pi, e.I, e.half = arb.pi(), acb(0, 1), arb(1)/2
    t = 2*c.acos()
    polarized = (c/arb(2).sqrt()).asin()/e.pi
    e.polarized = polarized
    y = c.atan()/e.pi
    e.xs, e.ts, e.hx, e.ht = y, t, y.imag, -t.imag
    T = e.rat(ANGLE)
    assert 0 < t.real < e.pi/2 < T and t.imag < 0
    assert c.real > 0 and c.imag > 0 and abs(c) < 1
    assert e.rat(ALPHA) < y.real < e.rat(BETA)
    assert 0 < e.hx < e.ht/(2*e.pi)
    assert polarized.real > 0 and polarized.imag > 0
    fixed_bulk = e.half-polarized.real-T/(2*e.pi)
    local_bulk = e.half-y.real-t.real/(2*e.pi)
    assert fixed_bulk > 0 and local_bulk > 0

    def fixed_b(t):
        return (-e.Ju(e.half-polarized+t/(2*e.pi))
                -e.Ju(e.half-polarized-t/(2*e.pi))-2*e.Ju(polarized))

    def phase(y, t, side):
        return BASE_PHASE(y, t, side)+fixed_b(t)

    def gradient(y, t, side):
        gy, gt = BASE_GRADIENT(y, t, side)
        gt += (-e.jp(e.half-polarized+t/(2*e.pi), 1)
               +e.jp(e.half-polarized-t/(2*e.pi), 1))/(2*e.pi)
        return gy, gt

    def hessian(y, t):
        yy, yt, tt = BASE_HESSIAN(y, t)
        tt -= ((e.pi*polarized+t/2).tan()
               +(e.pi*polarized-t/2).tan())/(4*e.pi)
        return yy, yt, tt

    def mapping(p, q, kind, endpoint=None):
        if kind in ("central", "negative", "lower"):
            side = -1 if kind == "lower" else 1
            yy, tt = acb(p, side*e.hx), acb(2*e.pi*q, -e.ht)
            dirs = ((acb(1), acb(0)), (acb(0), 2*e.pi))
            penalty = 2*e.pi*e.hx if side < 0 else arb(0)
            pd = (arb(0), arb(0))
        elif kind.startswith("outer_"):
            side = -1 if kind.startswith("outer_lower_") else 1
            sign = 1 if kind.endswith("positive") else -1
            yy, tt = acb(p, side*e.hx*q), acb(sign*T, -e.ht*q)
            dirs = ((acb(1), acb(0)), (side*e.I*e.hx, -e.I*e.ht))
            coefficient = 2*e.pi*e.hx if side < 0 else arb(0)
            penalty, pd = coefficient*q, (arb(0), coefficient)
        elif kind.startswith("bottom_endpoint_"):
            side = 1 if kind.endswith("upper") else -1
            yy, tt = acb(e.rat(endpoint), side*e.hx*q), acb(2*e.pi*p, -e.ht)
            dirs = ((acb(0), 2*e.pi), (side*e.I*e.hx, acb(0)))
            coefficient = 2*e.pi*e.hx if side < 0 else arb(0)
            penalty, pd = coefficient*q, (arb(0), coefficient)
        else:
            raise ValueError(kind)
        return yy, tt, dirs, side, penalty, pd

    def boundbox(box, kind, endpoint, target):
        if not kind.startswith("nested_"):
            return BASE_BOUND_AFFINE(box, kind, endpoint, target)
        side = 1 if "_upper_" in kind else -1
        sign = 1 if kind.endswith("positive") else -1
        p, q = e.ball(box[0], box[1]), e.ball(box[2], box[3])
        yy = acb(e.rat(endpoint), side*e.hx*p*q)
        tt = acb(sign*T, -e.ht*p)
        penalty = 2*e.pi*e.hx*p*q if side < 0 else arb(0)
        return phase(yy, tt, side).real-penalty, "direct"

    e.phase, e.gradient, e.hessian = phase, gradient, hessian
    e.mapping, e.boundbox = mapping, boundbox
    e.M = phase(y, t, 1).real
    e.LOCAL = (Q(225, 1000), Q(233, 1000), Q(235, 1000), Q(243, 1000))
    gy, gt = gradient(y, t, 1)
    assert abs(gy) < arb(1)/100 and abs(gt) < arb(1)/100
    gx = (e.jp(e.half-polarized+t/(2*e.pi), 1)
          +e.jp(e.half-polarized-t/(2*e.pi), 1)-2*e.jp(polarized, 1))
    assert abs(gx) < arb(1)/100
    yy, yt, tt = hessian(y, t)
    den = (2*e.pi*polarized).cos()+t.cos()
    bxxt = -2*e.pi*(2*e.pi*polarized).sin()/den-2*e.pi/(e.pi*polarized).tan()
    bxt = -t.sin()/den
    reduced_xx = bxxt-bxt*bxt*yy/(yy*tt-yt*yt)
    assert reduced_xx.real < 0
    sine = (t/2).sin()
    E = -(3*e.I*t/2).exp()*c/(1+sine)
    assert E.real > 0
    rsum = sine.asinh()+(sine/c).asinh()
    lift = rsum-e.I*(3*t/2-e.pi)
    assert abs(lift) < arb(1)/100

    g_alpha = (e.Js(2*e.rat(ALPHA), 1)-4*e.Js(e.rat(ALPHA), 1)).real
    wire_tail = fixed_b(acb(0)).real+2*g_alpha
    yT = (T/2).cos().atan()/e.pi
    outer_edge = BASE_PHASE(yT, T, 1)-3*e.I*T*T/(4*e.pi)+e.I*T
    angular_tail = fixed_b(T).real+outer_edge.real
    assert e.M-wire_tail > arb(1)/5
    assert e.M-angular_tail > arb(1)/100
    return {
        "root_polynomial": ["i", "-4", "-4i", "4"],
        "root_variable": "c=cos(t/2)",
        "center_real_rational": str(center.real.fmpq()),
        "center_imag_rational": str(center.imag.fmpq()),
        "Rouche_radius": "2^-80",
        "Rouche_error_upper": str(error.upper()),
        "Rouche_linear_lower": str(linear.lower()),
        "c": str(c), "angle": str(t), "polarized_wire": str(polarized),
        "outer_wire": str(y), "fixed_wire_strip_margin": str(fixed_bulk),
        "local_outer_bulk_margin": str(local_bulk),
        "original_log_lift": str(lift),
        "mixed_gradient": [str(gy), str(gt)],
        "internal_wire_gradient": str(gx),
        "reduced_internal_wire_second_derivative": str(reduced_xx),
        "selected_action": str(phase(y, t, 1)),
        "wire_tail_rate": str(wire_tail), "wire_tail_gap": "1/5",
        "angular_tail_rate": str(angular_tail), "angular_tail_gap": "1/100",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument("--output", type=Path,
                        default=Path("repro/results/research-internal-pair-three-mixed-packet.json"))
    parser.add_argument("--only", type=str)
    args = parser.parse_args()
    if args.precision < 140:
        parser.error("At least 140 bits are required.")
    root = setup(args.precision)
    local = e.certify_local(16)
    cases = []
    # A rational rectangle slightly beyond T/(2pi), still with positive
    # fixed-wire bulk margin; it safely covers every actual horizontal.
    stop = Q(311, 1000)
    assert e.rat(stop)*2*e.pi > e.rat(ANGLE)
    assert arb(1)/2-e.polarized.real-e.rat(stop) > 0
    plan = [
        ("central", (ALPHA, BETA, Q(0), stop), Q(1, 10_000_000), None, Q(1)),
        ("negative", (ALPHA, BETA, -stop, Q(0)), Q(1, 1000), None, Q(1)),
        ("lower", (ALPHA, BETA, -stop, stop), Q(1, 1000), None, Q(1)),
    ]
    for sign in ("positive", "negative"):
        for prefix in ("outer_", "outer_lower_"):
            plan.append((prefix+sign, (ALPHA, BETA, Q(0), Q(1)),
                         Q(1, 1000), None, Q(1, 3)))
    for endpoint in (ALPHA, BETA):
        for side in ("upper", "lower"):
            plan.append(("bottom_endpoint_"+side,
                         (-stop, stop, Q(0), Q(1)),
                         Q(1, 1000), endpoint, Q(1, 2)))
            for sign in ("positive", "negative"):
                plan.append(("nested_"+side+"_"+sign, (Q(0), Q(1), Q(0), Q(1)),
                             Q(1, 1000), endpoint, Q(1)))
    assert len(plan) == 19
    document = {
        "status": "incomplete",
        "scope": "Limiting phase inequalities for the exact mixed packet; finite-source assembly separate.",
        "precision_bits": args.precision,
        "python_version": platform.python_version(),
        "python_flint_version": flint.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest(),
        "outer_wire_interval": [str(ALPHA), str(BETA)],
        "angle_cutoff": str(ANGLE),
        "root": root, "local_Hessian": local, "surfaces": cases,
        "expected_surface_count": 19,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for kind, box, gap, endpoint, scale in plan:
        if args.only and args.only != kind:
            continue
        result = e.certify(kind, box, gap, endpoint, scale)
        cases.append(result)
        args.output.write_text(json.dumps(document, indent=2)+"\n")
        print(f"{kind} endpoint={endpoint}: {result['counts']['visited']} boxes", flush=True)
    document["status"] = "certified" if len(cases) == 19 else "partial"
    args.output.write_text(json.dumps(document, indent=2)+"\n")
    print(f"{document['status']}: {len(cases)} surfaces", flush=True)


if __name__ == "__main__":
    main()
