#!/usr/bin/env python3
"""Independent Riley algebra and a certified modulus-only switch for 6_1.

The exact checks use SymPy and Arb.  Optional numerical quadrature is a
classical-curve diagnostic, not a proof of a quantum annihilator or volume.
"""

import argparse
import json
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx


def symbolic_checks():
    M, z, L, Y, t = sp.symbols('M z L Y t')
    A = sp.Matrix([[M, 1], [0, 1/M]])
    B = sp.Matrix([[M, 0], [-z, 1/M]])
    W = sp.simplify((A*B.inv()*A.inv()*B)**2)
    Wr = sp.simplify((B*A.inv()*B.inv()*A)**2)
    R = (z**4+(5-2*t)*z**3+(t**2-6*t+11)*z**2
         +(t**2-7*t+12)*z+5-2*t)
    Rm = sp.cancel(R.subs(t, M**2+M**-2))
    assert (W*A-B*W-sp.Matrix([[0, Rm], [z*Rm, 0]])).applyfunc(sp.cancel) == sp.zeros(2)
    rnum = sp.fraction(Rm)[0]
    longitude = sp.simplify(W*Wr)
    for v in longitude*B-B*longitude:
        assert sp.rem(sp.fraction(sp.cancel(v))[0], rnum, z) == 0
    w12 = -((-M**2+z+1)*(-M**4*z+M**2*z**2+2*M**2*z+2*M**2-z))/M**3
    assert sp.cancel(W[0, 1]-w12) == 0
    assert sp.rem(sp.fraction(sp.cancel(longitude[0, 0]*w12.subs(M, 1/M)+w12))[0], rnum, z) == 0
    P = (L**4*M**8-L**3*M**16+L**3*M**14+3*L**3*M**8
         +3*L**3*M**6-2*L**3*M**4+L**2*M**16-3*L**2*M**14
         -L**2*M**12+3*L**2*M**10+6*L**2*M**8+3*L**2*M**6
         -L**2*M**4-3*L**2*M**2+L**2-2*L*M**12+3*L*M**10
         +3*L*M**8+L*M**2-L+M**8)
    # Use the reduced rational longitude; no table or named polynomial proof.
    relation = sp.fraction(sp.cancel(L+ w12/w12.subs(M, 1/M)))[0]
    resultant = sp.factor(sp.resultant(rnum, relation, z))
    quotient = sp.factor(resultant/P)
    assert not quotient.has(L, z)
    D = 5*t**6-32*t**5+26*t**4+42*t**3-55*t**2+226*t-23
    assert sp.factor(sp.discriminant(R, z)-D) == 0
    a = -Y**4+Y**3+3+3/Y-2/Y**2
    b = Y**4-3*Y**3-Y**2+3*Y+6+3/Y-Y**-2-3*Y**-3+Y**-4
    c = -2*Y**2+3*Y+3+Y**-3-Y**-4
    F = L**4+a*L**3+b*L**2+c*L+1
    assert sp.cancel(F.subs(Y, M**2)-P/M**8) == 0
    for coefficient, expected in ((a, 5), (b, 15), (c, 5)):
        assert sp.rem(sp.fraction(sp.cancel(coefficient-expected))[0], Y**2-Y+1, Y) == 0
    switch = L**4+5*L**3+15*L**2+5*L+1
    assert sp.discriminant(switch, L) != 0
    return {'matrix_relation': 'W A = B W', 'longitude': 'W W_reverse',
            'resultant_extra_factor': str(quotient),
            'riley_discriminant': str(D),
            'switch_longitude_discriminant': str(sp.discriminant(switch, L))}


def certified_switch():
    ctx.prec = 192
    I = acb(0, 1)
    Y = (1-I*arb(3).sqrt())/2
    a = -Y**4+Y**3+3+3/Y-2/Y**2
    b = Y**4-3*Y**3-Y**2+3*Y+6+3/Y-Y**-2-3*Y**-3+Y**-4
    c = -2*Y**2+3*Y+3+Y**-3-Y**-4
    da = -4*Y**3+3*Y**2-3/Y**2+4/Y**3
    db = 4*Y**3-9*Y**2-2*Y+3-3/Y**2+2/Y**3+9/Y**4-4/Y**5
    dc = -4*Y+3-3/Y**4+4/Y**5
    slopes, rows = [], []
    for sign in (-1, 1):
        w = (-5+sign*I*3*arb(3).sqrt())/2
        l = (w-(w*w-4).sqrt())/2
        if abs(l) < 1:
            l = (w+(w*w-4).sqrt())/2
        assert abs(l) > 3
        residual = l**4+a*l**3+b*l**2+c*l+1
        assert residual.contains(0)
        pl = 4*l**3+3*a*l**2+2*b*l+c
        py = da*l**3+db*l**2+dc*l
        assert not pl.contains(0)
        slope = (-2*arb.pi()*I*Y*py/(l*pl)).real
        slopes.append(slope)
        rows.append({'root': str(l), 'modulus': str(abs(l)),
                     'd_x_log_modulus': str(slope)})
    assert slopes[0] < -7
    assert slopes[1] > 3
    assert slopes[0]-slopes[1] < -10
    return {'x': '5/6', 'expanding_branches': rows,
            'slope_difference': str(slopes[0]-slopes[1]),
            'conclusion': 'transverse modulus switch; no eigenvalue collision'}


def numerical_diagnostic(points):
    import numpy as np
    from scipy.integrate import simpson
    from scipy.optimize import linear_sum_assignment

    xs = np.linspace(.5000001, .9999999, points)
    tracks = []
    prior = None
    for x in xs[::-1]:
        t = 2*np.cos(2*np.pi*x)
        roots = np.roots([1, 5-2*t, t*t-6*t+11, t*t-7*t+12, 5-2*t])
        if prior is None:
            roots = roots[np.argsort(-roots.imag)]
        else:
            _, permutation = linear_sum_assignment(abs(prior[:, None]-roots[None, :]))
            roots = roots[permutation]
        tracks.append(roots)
        prior = roots
    tracks = np.array(tracks[::-1])
    M = -np.exp(1j*np.pi*xs)
    def w12(m, z):
        return -((-m*m+z+1)*(-m**4*z+m*m*z*z+2*m*m*z+2*m*m-z))/m**3
    rates = []
    for k in range(4):
        z = tracks[:, k]
        longitude = -w12(M, z)/w12(1/M, z)
        rate = np.log(np.abs(longitude))
        rate[np.abs(z.imag) < 1e-6] = 0
        rates.append(rate)
    rates = np.array(rates)
    coherent = sorted([float(2*np.pi*simpson(v, x=xs)) for v in rates])
    envelope = float(2*np.pi*simpson(np.max(rates, axis=0), x=xs))
    return {'status': 'uncertified numerical classical-curve diagnostic',
            'points': points, 'coherent_integrals_2pi_scaled': coherent,
            'spectral_envelope_integral_2pi_scaled': envelope,
            'not_claimed': 'actual all-level quantum operator or hyperbolic-volume calibration'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--points', type=int, default=0,
                        help='optional uncertified numerical branch quadrature')
    args = parser.parse_args()
    out = {'exact_algebra': symbolic_checks(), 'certified_switch': certified_switch()}
    if args.points:
        out['numerical_diagnostic'] = numerical_diagnostic(args.points)
    out['scope'] = ('Independent classical Riley/longitude algebra and rigorous modulus-only '
                    'switch. No actual quantum operator or sharp volume bound asserted.')
    Path(__file__).with_name('six_one_spectral_envelope_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS exact Riley/longitude/resultant algebra and Arb transverse modulus switch')
    if args.points:
        print(json.dumps(out['numerical_diagnostic'], indent=2))


if __name__ == '__main__':
    main()
