#!/usr/bin/env python3
"""Parameterized outward certificates for isolated-vertex trace-first contours.

Only explicitly requested (degree,power) pairs are checked. No inference
is made for untested pairs. The original 19 surfaces and all penalties
are inherited from the separately audited degree-two procedure.
"""

import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path

import mpmath as mp
from flint import acb, acb_poly, arb, ctx

import certify_internal_degree_two_contours as c

e = c.e


def gaussian_coefficients(degree, power):
    """Exact coefficients of (-i)^d(w+i)^d+w^n(w-i)^d."""
    coefficients = [[0, 0] for _ in range(degree + power + 1)]
    units = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for j in range(degree + 1):
        first, second = units[-j % 4], units[-(degree - j) % 4]
        for component in (0, 1):
            coefficients[j][component] += comb(degree, j) * first[component]
            coefficients[j + power][component] += comb(degree, j) * second[component]
    return coefficients


def root_certificate(power, precision):
    degree = c.DEGREE
    mp.mp.dps = max(100, degree + 30)

    def equations(a, b):
        return (mp.sin(a) - mp.cosh(b) * mp.tanh(power * b / degree),
                power * a + degree * mp.atan(mp.sinh(b) / mp.cos(a)) - mp.pi)

    denominator = degree**2 + power**2
    a, b = mp.findroot(
        equations, (mp.pi * power / denominator, mp.pi * degree / denominator),
        tol=mp.mpf("1e-90"), maxsteps=100)
    proposed = mp.exp(1j * (a - 1j * b))
    coefficients = gaussian_coefficients(degree, power)
    ctx.prec = max(precision, 2 * degree + 100)
    p = acb_poly([acb(real, imag) for real, imag in coefficients])
    center = acb(mp.nstr(proposed.real, mp.mp.dps),
                 mp.nstr(proposed.imag, mp.mp.dps)).mid()
    radius = arb(2) ** (-100)
    shifted = acb_poly([0])
    variable = acb_poly([center, 1])
    for coefficient in reversed(p.coeffs()):
        shifted = shifted * variable + coefficient
    error = abs(shifted[0]) + sum(
        abs(shifted[j]) * radius**j for j in range(2, len(shifted)))
    linear = abs(shifted[1]) * radius
    assert error < linear
    w = acb(center.real + arb(0, radius),
            center.imag + arb(0, radius))
    t = -2 * acb(0, 1) * w.log()
    x = (t / 2).cos().atan() / arb.pi()
    assert 0 < t.real < arb.pi() / 2
    assert t.real < 2 * arb.pi() / power
    assert t.imag < 0
    assert e.rat(c.ALPHA) < x.real < e.rat(c.BETA)
    assert -t.imag / (2 * arb.pi()) > x.imag > 0
    margin = arb(1) / 2 - x.real - t.real / (2 * arb.pi())
    assert margin > 0
    y = -acb(0, 1) * (w + acb(0, 1)) / (w - acb(0, 1))
    assert y.real > 0 and y.imag < 0
    geometric_residual = (degree * y.log()
                          - acb(0, 1) * power * t / 2
                          + acb(0, 1) * arb.pi())
    # The exact polynomial makes exp(geometric_residual)=1. This
    # enclosure excludes every nonzero logarithmic winding, so it
    # certifies the original unit-charge cone equation itself.
    assert abs(geometric_residual) < arb(1) / 100
    return x, t, {
        "variable": "w=exp(i*t/2)",
        "polynomial": "(-i)^d*(w+i)^d+w^n*(w-i)^d",
        "gaussian_integer_coefficients": coefficients,
        "center_real_rational": str(center.real.fmpq()),
        "center_imag_rational": str(center.imag.fmpq()),
        "Rouche_disk_radius": "2^-100",
        "Rouche_error_upper": str(error.upper()),
        "Rouche_linear_lower": str(linear.lower()),
        "root_enclosure": str(w),
        "selected_wire": str(x), "selected_angle": str(t),
        "selected_factorial_bulk_margin": str(margin),
        "original_cone_equation_residual": str(geometric_residual),
        "precision_bits": ctx.prec,
        "branch_rule": (
            "Polynomial gives exp(2*pi*Psi_t)=1 and tan(pi*x)=cos(t/2) "
            "gives exp(Psi_x/d)=1; certified |Psi_x|,|Psi_t|<1/100 "
            "then forces both literal logarithmic derivatives to vanish."
        ),
    }


def certify_pair(degree, power, precision, alpha):
    c.DEGREE, c.ALPHA, c.BETA = degree, alpha, Q(1, 2) - alpha
    c.root_certificate = root_certificate
    rootdata = c.setup(power, precision)
    # Resolve the tiny positive trace angle at high degree. A fixed
    # millesimal rectangle would cross zero and would not be a local
    # rectangle strictly inside the positive main contour.
    denominator = 2**24
    angular_midpoint = e.ts.real / (2 * e.pi)
    center_integer = int((denominator * angular_midpoint).mid().floor().fmpz())
    center = Q(center_integer, denominator)
    width = min(Q(3, 1000), Q(max(4, center_integer // 8), denominator))
    left, right = center - width, center + width + Q(1, denominator)
    assert 0 < left < right < Q(1, 3)
    e.LOCAL = (e.LOCAL[0], e.LOCAL[1], left, right)
    assert alpha < e.LOCAL[0] < e.LOCAL[1] < c.BETA
    local = e.certify_local(24)

    alpha_ball = e.rat(alpha)
    g_alpha = (e.Js(2 * alpha_ball, 1) - 4 * e.Js(alpha_ball, 1)).real
    m_infinity = 2 * (e.Js(e.half, 1) - 4 * e.Js(e.half / 2, 1)).real
    tail = (degree - 1) * m_infinity + 2 * g_alpha
    tail_gap = e.M - tail
    assert tail_gap > 0
    assert e.M > 5 * arb(degree) / 6
    cases = []

    def add(kind, rectangle, gap, endpoint=None, scale=Q(1)):
        item = e.certify(kind, rectangle, gap, endpoint, scale)
        cases.append(item)
        print(f"d={degree}, n={power}: certified {kind}, endpoint={endpoint}; "
              f"{item['counts']['visited']} boxes", flush=True)

    small_gap = Q(1, 100 * (degree + power)**4)
    main_gap = Q(1, 1_000_000 * (degree + power)**4)
    add("central", (alpha, c.BETA, Q(0), Q(1, 3)), main_gap)
    add("negative", (alpha, c.BETA, Q(-1, 3), Q(0)), small_gap)
    add("lower", (alpha, c.BETA, Q(-1, 3), Q(1, 3)), small_gap)
    for sign in ("positive", "negative"):
        for prefix in ("outer_", "outer_lower_"):
            add(prefix + sign, (alpha, c.BETA, Q(0), Q(1)),
                Q(1, 1000), scale=Q(1, 3))
    for endpoint in (alpha, c.BETA):
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
        "degree": degree, "power": power, "root": rootdata,
        "selected_rate": str(e.M), "wire_interval": [str(alpha), str(c.BETA)],
        "wire_tail_rate": str(tail), "wire_tail_gap": str(tail_gap),
        "outer_angle_comparison": "M>5*d/6>d*(4/5)>d*psi(2*pi/3,0)",
        "local_Hessian": local, "surfaces": cases,
    }


def pair(value):
    try:
        degree, power = map(int, value.split(","))
        if degree < 2 or power < 1:
            raise ValueError
        return degree, power
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use degree,power with degree>=2,power>=1") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pairs", type=pair, nargs="+", required=True)
    parser.add_argument("--alpha-denominator", type=int, default=128)
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.alpha_denominator < 8 or args.precision < 140:
        parser.error("Require alpha denominator>=8 and precision>=140")
    report = {
        "scope": "Outward limiting-phase certificates for the explicitly requested pairs only.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "degree_two_engine_sha256": hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest(),
        "primitive_engine_sha256": hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest(),
        "pairs": [],
    }
    for degree, power in args.pairs:
        result = certify_pair(degree, power, args.precision,
                              Q(1, args.alpha_denominator))
        report["pairs"].append(result)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print("All explicitly requested pairs were certified.", flush=True)


if __name__ == "__main__":
    main()
