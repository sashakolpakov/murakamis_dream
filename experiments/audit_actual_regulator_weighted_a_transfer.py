#!/usr/bin/env python3
"""Actual affine figure-eight channel connection with retained source."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def exact_checks():
    Q, Y, L, a, pd = sp.symbols('Q Y L a pd', nonzero=True)
    g = Q**2*Y**2-Q*Y**4+Q*Y**3+Q*Y-Q+Y**2
    cm = Y**2*(Q-Y)*(Q*Y**2-1)
    c0 = -(Y-1)**2*(Y+1)*g
    cp = Y**2*(Q*Y-1)*(Q-Y**2)
    D = Y*(Y+1)*(Q-Y**2)*(Q*Y**2-1)
    T = sp.Matrix([[-c0/cp, -cm/cp], [1, 0]])
    P = Y**2+Y**-2-Y-Y**-1-2
    aa = Y/(Y**2-1)
    assert all(sp.factor(x) == 0 for x in T.subs(Q, 1)-sp.Matrix([[P, -1], [1, 0]]))
    assert all(sp.factor(x) == 0 for x in T.diff(Q).subs(Q, 1)-sp.Matrix([[-aa*P, 2*aa], [0, 0]]))
    assert sp.factor((D/cp).subs(Q, 1)-(Y+1)**2/Y) == 0
    V = sp.Matrix([[L, 1/L], [1, 1]])
    Ldot = pd*L**2/(L**2-1)
    Vdot = sp.Matrix([[Ldot, -Ldot/L**2], [0, 0]])
    B = V.inv()*sp.Matrix([[-a*(L+1/L), 2*a], [0, 0]])*V-V.inv()*Vdot*sp.diag(L, 1/L)
    assert sp.factor(B[0, 1]-(a/L+pd/(L**2-1)**2)) == 0
    assert sp.factor(B[1, 0]-(a*L+pd*L**4/(L**2-1)**2)) == 0
    at = {a: -sp.I/2, pd: -2*sp.I, L: -2-sp.sqrt(3)}
    assert sp.simplify(B[0, 1].subs(at)-sp.I*(sp.sqrt(3)-1)/6) == 0
    assert sp.simplify(B[1, 0].subs(at)+sp.I*(sp.sqrt(3)+1)/6) == 0
    return {'actual_quantum_coefficient_expansion': True,
            'both_connection_entries_exact': True,
            'B12_at_Y_i': 'i*(sqrt(3)-1)/6', 'B21_at_Y_i': '-i*(sqrt(3)+1)/6',
            'actual_affine_source_at_Y_i': [2, 0]}


def coeff(Q, Y):
    g = Q**2*Y**2-Q*Y**4+Q*Y**3+Q*Y-Q+Y**2
    cm = Y**2*(Q-Y)*(Q*Y**2-1)
    c0 = -(Y-1)**2*(Y+1)*g
    cp = Y**2*(Q*Y-1)*(Q-Y**2)
    D = Y*(Y+1)*(Q-Y**2)*(Q*Y**2-1)
    return mp.matrix([[-c0/cp, -cm/cp], [1, 0]]), mp.matrix([D/cp, 0])


def eig(Y):
    P = Y**2+Y**-2-Y-Y**-1-2
    L = (P-mp.sqrt(P*P-4))/2
    return L, mp.matrix([[L, 1/L], [1, 1]])


def finite_checks():
    rows = []
    Y = mp.j
    L, V = eig(Y)
    B12 = mp.j*(mp.sqrt(3)-1)/6
    B21 = -mp.j*(mp.sqrt(3)+1)/6
    for N in [32, 64, 128, 256, 512]:
        h = 2j*mp.pi/N
        Q = mp.exp(h)
        T, f = coeff(Q, Y)
        _, Vnext = eig(Q*Y)
        step = Vnext**-1*T*V
        e12 = abs(step[0, 1]/h-B12)
        e21 = abs(step[1, 0]/h-B21)
        assert N*max(e12, e21) < 50
        sf = Vnext**-1*f
        assert abs(sf[0]) > mp.mpf('.1') and abs(sf[1]) > mp.mpf('.1')
        rows.append({'N': N, 'actual_orbit_sample_j': N//4,
                     'connection_entry_max_error': float(max(e12, e21)),
                     'actual_affine_source_both_channels_nonzero': True})
    return rows


def main():
    mp.mp.dps = 70
    data = {'status': 'PASS', 'exact_actual_formula': exact_checks(),
            'finite_actual_root_transfer': finite_checks(),
            'scope': 'Actual one-step connection and affine source. Does not bound the selected complete invariant or exclude better exact Green/weighted Gram estimates.'}
    Path(__file__).with_name('actual_regulator_weighted_a_transfer_results.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS exact actual affine transfer/source, both radical connection entries and 5 actual root-orbit limits')


if __name__ == '__main__':
    main()
