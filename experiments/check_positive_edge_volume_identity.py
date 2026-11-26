#!/usr/bin/env python3
"""Compare original tetrahedron volumes with the normalized edge action.

The written proof is in notes/research_positive_edge_volume_identity.md.
These checks compare three constructions: eight Bloch--Wigner volumes,
an explicit holomorphic dilogarithm primitive, and integration of the
original meridian form. Finite samples do not prove geometric assembly
or a quantum asymptotic.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def f(z):
    return mp.atan(mp.tanh(z))


def integral_f(z):
    exponential = mp.exp(-2*z)
    return (mp.pi*z/4 + 1j*(mp.polylog(2, -1j*exponential)
                            - mp.polylog(2, 1j*exponential))/4
            - mp.catalan/2)


def phase(p, q):
    return (4*mp.catalan - 2*(p+q)*(f(p)+f(q))
            + 4*(integral_f(p)+integral_f(q)))/mp.pi


def coordinates(p, q):
    return (2*(f(p)+f(q)), -2j*(p-q), p+q, 1j*(f(q)-f(p)))


def bloch_wigner(z):
    return mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)


def original_shapes(p, q):
    t, u, rt, ru = coordinates(p, q)
    a = 1j*mp.exp(rt-1j*u/2)
    b = 1j*mp.exp(1j*t/2-ru)
    c = 1j*mp.exp(-rt-1j*u/2)
    d = 1j*mp.exp(1j*t/2+ru)
    return (a, b, -1/a, -1/b, c, d, -1/c, -1/d)


def relative(left, right):
    return abs(left-right)/max(1, abs(left), abs(right))


def integrated_phase(p, q):
    # Straight paths in P,Q stay inside the positive strip product.
    def derivative(s):
        t, u, rt, ru = coordinates(s*p, s*q)
        dt = 2*(p/mp.cosh(2*s*p)+q/mp.cosh(2*s*q))
        du = -2j*(p-q)
        return -(rt*dt+ru*du)/mp.pi
    return 4*mp.catalan/mp.pi+mp.quad(derivative, [0, mp.mpf('.5'), 1])


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    points = [
        ('0', '0'), ('.3', '.2'), ('-.7', '.4'), ('1.2', '-.6'),
        ('-1.4', '-.5'), ('.1', '.77'), ('-.2', '-.76'), ('3', '.1'),
    ]
    strips = [mp.mpc(x, y) for x, y in points]
    rows = []
    for index in range(24):
        p, q = strips[index % 8], strips[(3*index+index//8) % 8]
        t, u, rt, ru = coordinates(p, q)
        shapes = original_shapes(p, q)
        assert all(z.imag > 0 for z in shapes)
        volume = mp.fsum(bloch_wigner(z) for z in shapes)
        action_volume = 2*mp.pi*phase(p, q).real-2*(t.imag*rt.imag+u.imag*ru.imag)
        residual = relative(volume, action_volume)
        assert residual < tolerance
        # Rational cross ratios supply a separate branch/convention check.
        aa, bb = mp.tan(t/2), mp.tan(u/2)
        qq = mp.cosh(rt)/mp.cos(u/2)
        rational = ((qq+aa)/(bb-1j), -(qq-bb)/(aa+1j),
                    (qq-aa)/(bb-1j), -(qq+bb)/(aa+1j))
        rational_residual = max(relative(shapes[k], r)
                                for k, r in zip((0, 1, 4, 5), rational))
        assert rational_residual < tolerance
        row = {'P': str(p), 'Q': str(q),
               'volume': mp.nstr(volume, 35),
               'volume_relative_residual': mp.nstr(residual, 12),
               'cross_ratio_relative_residual': mp.nstr(rational_residual, 12)}
        if index < 8:
            integral_residual = relative(phase(p, q), integrated_phase(p, q))
            assert integral_residual < tolerance
            row['integrated_period_relative_residual'] = mp.nstr(integral_residual, 12)
        rows.append(row)
    # Check the stationary cancellation with nonzero free boundary angles.
    # Independent algebraic data need not satisfy the real part of the
    # stationary equations: only their imaginary part is used here.
    stationary_rows = []
    for p, q, power in zip(strips[1:5], strips[4:8], (-6, -4, 5, 9)):
        t, u, rt, ru = coordinates(p, q)
        charge = (power*t.real/2-rt.imag)/mp.pi
        action = phase(p, q)+1j*power*t*t/(4*mp.pi)-1j*charge*t
        volume = mp.fsum(bloch_wigner(z) for z in original_shapes(p, q))
        residual = relative(volume, 2*mp.pi*action.real-2*u.imag*ru.imag)
        assert residual < tolerance
        stationary_rows.append({'power': power,
                                'charge': mp.nstr(charge, 35),
                                'relative_residual': mp.nstr(residual, 12)})
    return {
        'scope': ('Finite checks of the absolute positive-cell volume and its '
                  'boundary correction; no manifold assembly or quantum estimate.'),
        'precision_decimal_digits': precision,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'edge_checks': rows,
        'stationary_correction_checks': stationary_rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=100)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'edge_checks': len(result['edge_checks']),
        'integrated_period_checks': sum('integrated_period_relative_residual' in r
                                       for r in result['edge_checks']),
        'stationary_correction_checks': len(result['stationary_correction_checks']),
        'output': str(args.output) if args.output else None,
    }))


if __name__ == '__main__':
    main()
