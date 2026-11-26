#!/usr/bin/env python3
"""Certify the terminal phases for every integer power 4 through 31.

Uses python-flint. Algebraic roots are proved by an explicit Rouche
inequality, and every analytic surface is covered by rigorous intervals.
The shared surface definitions and Taylor bounds are imported from the
three-crossing certificate; no optimizer supplies an acceptance test.
"""
import argparse
import json
from pathlib import Path
from fractions import Fraction as Q
from flint import acb, arb, acb_poly, fmpz_poly, ctx
import certify_terminal_three_central_phase as e

def root_certificate(n):
    """Isolate the selected zero independently by Rouche's theorem.

 The library root finder only proposes a center. The strict polynomial
 inequality below proves that its disk contains exactly one zero.
 """
    ctx.prec = 180
    X = fmpz_poly([0, 1])
    a = fmpz_poly([1])
    b = 2 * X
    for _ in range(2, n):
        a, b = (b, 2 * X * b - a)
    ip = X * b
    p = acb_poly([acb(int(c)) for c in ip.coeffs()]) - acb(0, 1)
    proposed = p.roots(tol=arb(2) ** (-140), maxprec=360)
    candidates = []
    for z in proposed:
        t = 2 * z.acos()
        if t.real > 0 and t.real < 2 * arb.pi() / n and (t.imag < 0):
            candidates.append(z)
    assert len(candidates) == 1
    center = candidates[0].mid()
    rho = arb(2) ** (-100)
    shifted = acb_poly([0])
    variable = acb_poly([center, 1])
    for coefficient in reversed(p.coeffs()):
        shifted = shifted * variable + coefficient
    error = abs(shifted[0]) + sum((abs(shifted[j]) * rho ** j for j in range(2, len(shifted))))
    linear = abs(shifted[1]) * rho
    assert error < linear
    k = acb(center.real + arb(0, rho), center.imag + arb(0, rho))
    t = 2 * k.acos()
    x = k.atan() / arb.pi()
    assert t.real > 0 and t.real < 2 * arb.pi() / n and (t.imag < 0)
    assert x.real > arb(3) / 32 and x.real < arb(13) / 32
    assert -t.imag / (2 * arb.pi()) > x.imag > 0
    return (k, x, t, {'polynomial_real_coefficients': [str(c) for c in ip.coeffs()], 'polynomial_imaginary_constant': '-1', 'root_center': str(center), 'root_center_real_rational': str(center.real.fmpq()), 'root_center_imag_rational': str(center.imag.fmpq()), 'Rouche_radius': '2^-100', 'Rouche_error_upper': str(error.upper()), 'Rouche_linear_lower': str(linear.lower()), 'selected_root': str(k)})

def setup(n):
    k, x, t, rootdata = root_certificate(n)
    e.pi = arb.pi()
    e.I = acb(0, 1)
    e.half = arb(1) / 2
    e.k = k
    e.xs = x
    e.ts = t
    e.hx = x.imag
    e.ht = -t.imag

    def phase(x, t, side):
        pi = e.pi
        I = e.I
        p = e.half + t / (2 * pi)
        m = e.half - t / (2 * pi)
        b = e.Js(p, -1) + e.Js(m, 1) - e.Js(p - x, -1) - e.Js(m - x, 1) - 2 * e.Js(x, side)
        b0 = 2 * e.Js(e.half, 1) - 2 * e.Js(e.half - x, -side) - 2 * e.Js(x, side)
        return b + b0 + n * I * t * t / (4 * pi) - I * t

    def gradient(x, t, side):
        pi = e.pi
        I = e.I
        p = e.half + t / (2 * pi)
        m = e.half - t / (2 * pi)
        gx = e.jp(p - x, -1) + e.jp(m - x, 1) + 2 * e.jp(e.half - x, -side) - 4 * e.jp(x, side)
        gt = (e.jp(p, -1) - e.jp(m, 1) - e.jp(p - x, -1) + e.jp(m - x, 1)) / (2 * pi) + n * I * t / (2 * pi) - I
        return (gx, gt)

    def hessian(x, t):
        pi = e.pi
        I = e.I
        den = (2 * pi * x).cos() + t.cos()
        A = -2 * pi * (2 * pi * x).sin() / den - 4 * pi / (pi * x).tan() - 2 * pi * (2 * pi * x).sin() / ((2 * pi * x).cos() + 1)
        B = -t.sin() / den
        C = -((pi * x + t / 2).tan() + (pi * x - t / 2).tan()) / (4 * pi) + n * I / (2 * pi)
        return (A, B, C)
    e.phase = phase
    e.gradient = gradient
    e.hessian = hessian
    e.M = phase(x, t, 1).real
    xi = int((1000 * x.real).mid().floor().fmpz())
    ri = int((1000 * t.real / (2 * e.pi)).mid().floor().fmpz())
    e.LOCAL = (Q(xi - 3, 1000), Q(xi + 4, 1000), Q(ri - 3, 1000), Q(ri + 4, 1000))
    return rootdata

def certify(n):
    rootdata = setup(n)
    local = e.certify_local(16)
    alpha = arb(3) / 32
    tail = 2 * (e.Js(2 * alpha, 1) - 4 * e.Js(alpha, 1)).real
    assert e.M - tail > arb(19) / 1000
    cases = []
    cases.append(e.certify('central', (Q(3, 32), Q(13, 32), Q(0), Q(1, 3)), Q(1, 10000000)))
    cases.append(e.certify('negative', (Q(3, 32), Q(13, 32), Q(-1, 3), Q(0)), Q(1, 100 * n * n)))
    cases.append(e.certify('lower', (Q(3, 32), Q(13, 32), Q(-1, 3), Q(1, 3)), Q(1, 100 * n ** 3)))
    for sign in ['positive', 'negative']:
        for start in ['outer_', 'outer_lower_']:
            cases.append(e.certify(start + sign, (Q(3, 32), Q(13, 32), Q(0), Q(1)), Q(1, 1000), scale=Q(1, 3)))
    for endpoint in [Q(3, 32), Q(13, 32)]:
        for side in ['upper', 'lower']:
            for start in ['wire_', 'bottom_endpoint_']:
                cases.append(e.certify(start + side, (Q(-1, 3), Q(1, 3), Q(0), Q(1)), Q(1, 1000), endpoint, Q(1, 2)))
            for sign in ['positive', 'negative']:
                cases.append(e.certify('nested_' + side + '_' + sign, (Q(0), Q(1), Q(0), Q(1)), Q(1, 1000), endpoint))
    print('Power', n, 'has all 23 certified surfaces; visited', sum((c['counts']['visited'] for c in cases)), 'rectangles.', flush=True)
    return {'power': n, 'root': rootdata, 'action': str(e.M), 'wire': str(e.xs), 'angle': str(e.ts), 'local': local, 'surfaces': cases}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Save every algebraic-root and rational-box certificate')
    args = parser.parse_args()
    results = [certify(n) for n in range(4, 32)]
    document = {'scope': 'Whole limiting-phase certificate for powers 4 through 31; theorem assembly is in the accompanying note', 'precision_bits': ctx.prec, 'power_range': [4, 31], 'powers': results}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(document, indent=2) + '\n')
        print('Complete certificate:', args.output)
    print('Certified all 28 powers, including their selected-root branches and every required face.')
if __name__ == '__main__':
    main()
