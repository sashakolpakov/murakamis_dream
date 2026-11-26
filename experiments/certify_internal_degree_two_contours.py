#!/usr/bin/env python3
"""Outward certificates for the trace-first degree-two filling contours.

This proves limiting-phase inequalities, not the finite-source theorem.
The reusable terminal engine supplies rigorous primitive enclosures,
Taylor bounds, and rational-box coverings. This file supplies a new
algebraic saddle, the degree-two phase, correctly scaled wire penalties,
and precisely the 19 surfaces required by the trace-first ordering.
"""

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp
from flint import acb, acb_poly, arb, ctx, fmpz_poly

import certify_terminal_three_central_phase as e


BASE_MAPPING = e.mapping
BASE_BOUNDBOX = e.boundbox
DEGREE = 2
ALPHA, BETA = Q(1, 32), Q(15, 32)


def root_certificate(n, precision):
    """A numerical proposal is accepted only by an exact Rouché bound."""
    mp.mp.dps = 100

    def equations(a, b):
        return (mp.sin(a) - mp.cosh(b) * mp.tanh(n * b / DEGREE),
                n * a + DEGREE * mp.atan(mp.sinh(b) / mp.cos(a)) - mp.pi)

    a, b = mp.findroot(equations, (mp.pi / (n + DEGREE), DEGREE / n**2),
                       tol=mp.mpf("1e-90"), maxsteps=100)
    proposed = mp.exp(1j * (2 * a - 2j * b) / 4)
    X = fmpz_poly([0, 1])
    polynomial = (2 * X**n * (X**4 - 1)
                  - (X**4 + 1) * (X**(2 * n) + 1))
    ctx.prec = precision
    p = acb_poly([int(c) for c in polynomial.coeffs()])
    center = acb(mp.nstr(proposed.real, 100),
                 mp.nstr(proposed.imag, 100)).mid()
    radius = arb(2) ** (-100)
    shifted = acb_poly([0])
    variable = acb_poly([center, 1])
    for coefficient in reversed(p.coeffs()):
        shifted = shifted * variable + coefficient
    error = abs(shifted[0]) + sum(
        abs(shifted[j]) * radius**j for j in range(2, len(shifted)))
    linear = abs(shifted[1]) * radius
    assert error < linear
    r = acb(center.real + arb(0, radius),
            center.imag + arb(0, radius))
    t = -4 * acb(0, 1) * r.log()
    x = (t / 2).cos().atan() / arb.pi()
    assert 0 < t.real < 2 * arb.pi() / n
    assert t.real < arb.pi() / 2
    assert t.imag < 0
    assert e.rat(ALPHA) < x.real < e.rat(BETA)
    assert -t.imag / (2 * arb.pi()) > x.imag > 0
    bulk_margin = arb(1) / 2 - x.real - t.real / (2 * arb.pi())
    assert bulk_margin > 0
    # The polynomial gives tan(t/2)=-i cos(nt/4). The checked strip
    # 0<Re t<2pi/n and Im t<0 selects the principal asinh equation
    # asinh(tan(t/2))=i(nt/4-pi/2), rather than its other sinh branches.
    return x, t, {
        "variable": "r=exp(i*t/4)",
        "polynomial_coefficients": [str(c) for c in polynomial.coeffs()],
        "center_real_rational": str(center.real.fmpq()),
        "center_imag_rational": str(center.imag.fmpq()),
        "Rouche_disk_radius": "2^-100",
        "Rouche_error_upper": str(error.upper()),
        "Rouche_linear_lower": str(linear.lower()),
        "root_enclosure": str(r),
        "selected_wire": str(x), "selected_angle": str(t),
        "selected_factorial_bulk_margin": str(bulk_margin),
    }


def setup(n, precision):
    x, t, rootdata = root_certificate(n, precision)
    e.pi, e.I, e.half = arb.pi(), acb(0, 1), arb(1) / 2
    e.xs, e.ts, e.hx, e.ht = x, t, x.imag, -t.imag

    def phase(x, t, side):
        p, m = e.half + t / (2 * e.pi), e.half - t / (2 * e.pi)
        block = (e.Js(p, -1) + e.Js(m, 1)
                 - e.Js(p - x, -1) - e.Js(m - x, 1)
                 + 2 * e.Js(e.half, 1)
                 - 2 * e.Js(e.half - x, -side)
                 - 4 * e.Js(x, side))
        return DEGREE * block + n * e.I * t * t / (4 * e.pi) - e.I * t

    def gradient(x, t, side):
        p, m = e.half + t / (2 * e.pi), e.half - t / (2 * e.pi)
        gx = DEGREE * (e.jp(p - x, -1) + e.jp(m - x, 1)
                       + 2 * e.jp(e.half - x, -side) - 4 * e.jp(x, side))
        gt = (DEGREE * (e.jp(p, -1) - e.jp(m, 1)
                        - e.jp(p - x, -1) + e.jp(m - x, 1))
              / (2 * e.pi) + n * e.I * t / (2 * e.pi) - e.I)
        return gx, gt

    def hessian(x, t):
        den = (2 * e.pi * x).cos() + t.cos()
        xx = DEGREE * (
            -2 * e.pi * (2 * e.pi * x).sin() / den
            -4 * e.pi / (e.pi * x).tan()
            -2 * e.pi * (2 * e.pi * x).sin() / ((2 * e.pi * x).cos() + 1))
        xt = -DEGREE * t.sin() / den
        tt = (-DEGREE * ((e.pi * x + t / 2).tan()
                         + (e.pi * x - t / 2).tan()) / (4 * e.pi)
              + n * e.I / (2 * e.pi))
        return xx, xt, tt

    def mapping(p, q, kind, endpoint=None):
        x, t, directions, side, penalty, penalty_gradient = BASE_MAPPING(
            p, q, kind, endpoint)
        return (x, t, directions, side, DEGREE * penalty,
                tuple(DEGREE * value for value in penalty_gradient))

    def boundbox(box, kind, endpoint, target):
        if not kind.startswith("nested_"):
            return BASE_BOUNDBOX(box, kind, endpoint, target)
        # On the angular connector, p is the angular depth fraction
        # and q is the independent wire-endpoint depth fraction.
        # Direct interval evaluation retains the product p*q, so no
        # mixed chain-rule or mixed penalty term is omitted.
        side = 1 if "_upper_" in kind else -1
        sign = 1 if kind.endswith("positive") else -1
        p, q = e.ball(box[0], box[1]), e.ball(box[2], box[3])
        xx = acb(e.rat(endpoint), side * e.hx * p * q)
        tt = acb(sign * 2 * e.pi / 3, -e.ht * p)
        penalty = DEGREE * 2 * e.pi * e.hx * p * q if side < 0 else 0
        return phase(xx, tt, side).real - penalty, "direct"

    e.phase, e.gradient, e.hessian = phase, gradient, hessian
    e.mapping, e.boundbox = mapping, boundbox
    e.M = phase(x, t, 1).real
    xi = int((1000 * x.real).mid().floor().fmpz())
    ti = int((1000 * t.real / (2 * e.pi)).mid().floor().fmpz())
    e.LOCAL = (Q(xi - 3, 1000), Q(xi + 4, 1000),
               Q(ti - 3, 1000), Q(ti + 4, 1000))
    gx, gt = gradient(x, t, 1)
    assert abs(gx) < arb(1) / 100
    assert abs(gt) < arb(1) / 100
    rootdata["logarithmic_gradient_enclosures"] = [str(gx), str(gt)]
    return rootdata


def certify(n, precision):
    rootdata = setup(n, precision)
    local = e.certify_local(24)
    alpha = e.rat(ALPHA)
    g_alpha = (e.Js(2 * alpha, 1) - 4 * e.Js(alpha, 1)).real
    m_infinity = 2 * (e.Js(e.half, 1) - 4 * e.Js(e.half / 2, 1)).real
    wire_tail = (DEGREE - 1) * m_infinity + 2 * g_alpha
    assert e.M - wire_tail > arb(1) / 4
    assert e.M > arb(9) / 5
    cases = []

    def add(kind, rectangle, gap, endpoint=None, scale=Q(1)):
        result = e.certify(kind, rectangle, gap, endpoint, scale)
        cases.append(result)
        print(f"d=2, n={n}: certified {kind}, endpoint={endpoint}; "
              f"{result['counts']['visited']} boxes", flush=True)

    add("central", (ALPHA, BETA, Q(0), Q(1, 3)), Q(1, 10_000_000))
    add("negative", (ALPHA, BETA, Q(-1, 3), Q(0)), Q(1, 100 * n**2))
    add("lower", (ALPHA, BETA, Q(-1, 3), Q(1, 3)), Q(1, 100 * n**3))
    for sign in ("positive", "negative"):
        for prefix in ("outer_", "outer_lower_"):
            add(prefix + sign, (ALPHA, BETA, Q(0), Q(1)),
                Q(1, 1000), scale=Q(1, 3))
    for endpoint in (ALPHA, BETA):
        for side in ("upper", "lower"):
            add("bottom_endpoint_" + side,
                (Q(-1, 3), Q(1, 3), Q(0), Q(1)),
                Q(1, 1000), endpoint, Q(1, 2))
            for sign in ("positive", "negative"):
                add("nested_" + side + "_" + sign,
                    (Q(0), Q(1), Q(0), Q(1)),
                    Q(1, 1000), endpoint)
    assert len(cases) == 19
    return {
        "degree": DEGREE, "power": n, "root": rootdata,
        "selected_rate": str(e.M), "wire_tail_rate": str(wire_tail),
        "wire_tail_gap_lower_bound": "1/4",
        "angular_tail_comparison": "M>9/5>2*(4/5); finite real-angle lemma supplies the upper rate",
        "local_Hessian": local, "surfaces": cases,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--powers", type=int, nargs="+", default=[3])
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if min(args.powers) < 3 or max(args.powers) > 31:
        parser.error("This procedure is scoped to degree two and powers 3 through 31")
    if args.precision < 140:
        parser.error("At least 140 bits are required for the fixed root disk")
    document = {
        "scope": "Certified scaled limiting-phase inequalities; finite-source assembly is separate.",
        "precision_bits": args.precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest(),
        "degree": DEGREE, "wire_interval": [str(ALPHA), str(BETA)],
        "angular_interval_over_2pi": ["-1/3", "1/3"],
        "lower_wire_penalty_multiplier": DEGREE,
        "powers": [],
    }
    for n in args.powers:
        document["powers"].append(certify(n, args.precision))
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(document, indent=2) + "\n")
    print("All requested parameter cases were certified.", flush=True)


if __name__ == "__main__":
    main()
