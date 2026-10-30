#!/usr/bin/env python3
"""Exact source head transport; finite checks do not transport a period cycle."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_matching_edge_generic_deficient_operator_lift import (
    continued, factorials, white,
)
from audit_actual_moving_period_factorial_normals import factorial, period


def algebra():
    eta, Y, R, V, L = sp.symbols('eta Y R V L', nonzero=True)
    A = lambda y: (1-y)/(1/eta-y)
    B = lambda y: (1-y)/(eta-y)
    g = lambda y: y/(1-y)
    assert sp.cancel(g(eta*Y)/g(Y)-A(Y)) == 0
    count = 1
    for n in range(-3, 4):
        mu = (1-Y)/(eta**(-n)-Y)
        assert sp.cancel(g(eta**n*Y)/g(Y)-mu) == 0
        for m in range(-3, 4):
            mm = (1-eta**n*Y)/(eta**(-m)-eta**n*Y)
            target = (1-Y)/(eta**(-m-n)-Y)
            assert sp.cancel(mu*mm-target) == 0
            count += 1
    G = R*(1-V)*(1-L)/(V*L*(1-R))
    maps = ({R: eta*R}, {R: R/eta, V: eta*V, L: L/eta}, {L: eta*L})
    C = (A(R), B(R)/(A(V)*B(L)), 1/A(L))
    shifts = normals = commutators = 0
    for i in range(3):
        assert sp.cancel(G.subs(maps[i], simultaneous=True)/G-C[i]) == 0
        shifts += 1
        for j in range(3):
            left = C[i].subs(maps[j], simultaneous=True)*C[j]
            right = C[j].subs(maps[i], simultaneous=True)*C[i]
            assert sp.cancel(left-right) == 0
            commutators += 1
    fields = ((1, 0, 0), (-1, 1, -1), (0, 0, 1))
    variables = (R, V, L)
    def deriv(i, f):
        return sum(c*x*sp.diff(f, x) for c, x in zip(fields[i], variables))
    connection = [sp.cancel(deriv(i, G)/G) for i in range(3)]
    for i in range(3):
        # Both sides are divided by the common factor 2 pi i P'(0).
        assert sp.cancel(sp.diff(C[i], eta).subs(eta, 1)-connection[i]) == 0
        normals += 1
        for j in range(3):
            assert sp.cancel(deriv(i, connection[j])-deriv(j, connection[i])) == 0
    # An integral primitive head chart with an actual white and cap:
    # i=x, j=y, r=x+y-m, cap arguments z and L0-z.
    # The complete multiplier is tested after substituting shared variables.
    X, Z = sp.symbols('X Z', nonzero=True)
    network_G = g(X*Y)/(g(X)*g(Z**-1))
    chart = {X: eta*X, Y: Y/eta, Z: eta**2*Z}
    network_C = 1/(A(X)*((1-Z**-1)/(eta**2-Z**-1)))
    assert sp.cancel(network_G.subs(chart, simultaneous=True)/network_G-network_C) == 0
    return dict(exact_local_gauge_and_integer_cocycles=count,
                exact_full_operator_gauges=shifts,
                exact_full_operator_cocycles=commutators,
                exact_first_normal_connections=normals,
                exact_flat_connection_pairs=9,
                shared_integral_head_chart=1)


def numeric():
    mp.mp.dps = 85
    whites = cups = kernels = jets = 0
    worst = mp.mpf(0)
    def check(left, right, tolerance='1e-60'):
        nonlocal worst
        error = abs(left-right)/max(abs(left), abs(right), mp.mpf('1e-70'))
        assert error < mp.mpf(tolerance), error
        worst = max(worst, error)
    for N in (4, 5, 6):
        eps = mp.mpc('.013', '.009')/N**3
        q = mp.exp(mp.pi*1j/N+eps); P = period(N, eps)
        F = factorials(q, N-1)
        sigma = N*mp.mpc('.21', '.07'); i = N*mp.mpc('.08', '.13')
        for a in (0, (N-1)//2):
            base = white(N, a, q, sigma, i, F)
            for p, r in ((1, 0), (0, 1), (1, -1), (-1, 0)):
                shifted = white(N, a, q, sigma+P*(p+r), i+P*p, F)
                check(shifted, (-1)**((N-1)*r)*base)
                whites += 1
    def cup(N, L, eps, x):
        q = mp.exp(mp.pi*1j/N+eps); P = period(N, eps)
        F = factorials(q, L)
        return (mp.exp(mp.pi*1j*x)*q**(x*(L-x-1))
                *factorial(P, x, N)*factorial(P, L-x, N)/F[L])
    for N, L in ((5, 2), (6, 5)):
        eps = mp.mpc('.011', '.007')/N**3
        P = period(N, eps); eta = mp.exp(2*mp.pi*1j*P)
        x = N*mp.mpc('.27', '.09'); Y = mp.exp(2*mp.pi*1j*x)
        base = cup(N, L, eps, x)
        for n in (-1, 1, 2):
            mu = (-1)**(L*n)*(1-Y)/(eta**(-n)-Y)
            check(cup(N, L, eps, x+n*P), mu*base)
            cups += 1
    for N in (5, 6):
        a = (N-1)//2; s = N-1-2*a
        eps = mp.mpc('.009', '.005')/N**3
        P = period(N, eps); eta = mp.exp(2*mp.pi*1j*P)
        t, u, v = (N*mp.mpc('.72', '.04'), N*mp.mpc('.14', '.11'),
                   N*mp.mpc('.38', '.03'))
        A = lambda y: (1-y)/(1/eta-y)
        B = lambda y: (1-y)/(eta-y)
        yr = mp.exp(2*mp.pi*1j*(a-v+u))
        yv = mp.exp(2*mp.pi*1j*v); yl = mp.exp(2*mp.pi*1j*(t-v))
        multipliers = (1/A(yl), (-1)**s*A(yr), (-1)**s*B(yr)/(A(yv)*B(yl)))
        base = continued(N, a, eps, t, u, v, completed=True)
        coordinates = [t, u, v]
        for j, multiplier in enumerate(multipliers):
            shifted = coordinates.copy(); shifted[j] += P
            check(continued(N, a, eps, *shifted, completed=True), multiplier*base)
            kernels += 1
    # Genuine fixed-N transport, with the source endpoint L fixed as P moves.
    N, L = 5, 2
    x = N*mp.mpc('.23', '.12')
    g = lambda z: mp.exp(2*mp.pi*1j*z)/(1-mp.exp(2*mp.pi*1j*z))
    def transported(eps):
        delta = N-period(N, eps)
        return (-1)**L*g(x)*cup(N, L, eps, x+delta)/g(x+delta)
    for order in (0, 1, 2):
        check(mp.diff(lambda eps: cup(N, L, eps, x+N), 0, order),
              mp.diff(transported, 0, order), '1e-50')
        jets += 1
    return dict(precision_digits=mp.mp.dps,
                literal_large_white_moving_period_shifts=whites,
                literal_cup_positive_and_negative_shifts=cups,
                actual_generic_completed_kernel_shifts=kernels,
                genuine_fixed_N_normal_transports=jets,
                maximum_relative_error=mp.nstr(worst, 35))


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = dict(status='PASS', exact=algebra(), numeric=numeric(),
                  scope='Specified actual tensor summands on integral affine head charts; rational gauges and finite quantum jets. No support-domain or residue-cycle transport inferred.')
    path = args.output or Path(__file__).with_name('actual_tensor_source_finite_jet_connection_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
