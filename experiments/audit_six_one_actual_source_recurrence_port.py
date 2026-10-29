#!/usr/bin/env python3
"""Actual six-crossing plat -> proved triple source; Newton target unproved."""

import json
from pathlib import Path

import sympy as sp

from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field
from audit_actual_multichannel_newton_green import gaussian_rows


ACTION = [(1, 1)]+[(0, -1)]*3+[(1, 1)]*2


def framing_and_topology():
    T = sp.Matrix([[1, 1], [0, 1]])
    U = sp.Matrix([[1, 0], [1, 1]])
    assert T**2*U**3*T*sp.Matrix([0, 1]) == sp.Matrix([9, 4])
    A, d = sp.symbols('A d')
    B = 2*d-A
    colors, orientations = [A, B, B, A], [1, -1, -1, 1]
    cartan, writhe = 0, 0
    for position, sign in ACTION:
        cartan += sign*colors[position]*colors[position+1]/2
        writhe += sign*orientations[position]*orientations[position+1]
        colors[position], colors[position+1] = colors[position+1], colors[position]
        orientations[position], orientations[position+1] = orientations[position+1], orientations[position]
    assert colors == [B, A, B, A]
    assert writhe == 2
    assert sp.expand(cartan-writhe*(A*A-2*d*A)/2-d*B) == 0
    return {'slope': [9, 4], 'handedness': 'mirror of 9/5 Riley note',
            'oriented_writhe': 2, 'full_Cartan_minus_framing': 'd*alpha_dual'}


def literal(E, x):
    N, p, Q, d = E.N, E.p, E.Q, E.N-1
    xv = pow(x, -1, p)*pow(Q, -1, p) % p
    Y = Q*x*x % p
    total, count = 0, 0
    for a in range(N):
        states = [((a, d-a, d, 0), (), N*N*pow(x, a-2*d, p) % p)]
        colors = [x, xv, xv, x]
        for position, sign in ACTION:
            following = []
            x1, x2 = colors[position:position+2]
            for state, route, value in states:
                aa, bb = state[position:position+2]
                bound = min(aa, d-bb) if sign > 0 else min(bb, d-aa)
                for h in range(bound+1):
                    coefficient = E.direct(x1, x2, aa, bb, h, sign)
                    if not coefficient:
                        continue
                    pair = (bb+h, aa-h) if sign > 0 else (bb-h, aa+h)
                    following.append((state[:position]+pair+state[position+2:],
                                      route+(h,), value*coefficient % p))
            states = following
            colors[position], colors[position+1] = colors[position+1], colors[position]
        assert colors == [xv, x, xv, x]
        for state, route, value in states:
            if state[0]+state[1] != d or state[2]+state[3] != d:
                continue
            assert route[0] == 0 and route[4] == a and route[5] == 0
            k, l, r = route[1:4]
            assert a+k <= d and 0 <= l <= k and 0 <= r <= d-a-k+l
            assert state == (d-k+l-r, k-l+r, d, 0)
            # Two ORIGINAL ev_L caps and full Cartan/framing factor.
            actual = value*pow(x, state[0]+state[2], p)*pow(N, -2, p)*pow(xv, d, p) % p
            phase = 1+a+2*k*(a+k+1)-l*(a+2*k)+l*l
            predicted = (pow(Y, d-2*a-k+r, p)*pow(Q, phase, p)
                         *E.gaussian(a+k, k)*E.gaussian(d-k+l, l)
                         *E.gaussian(a+k-l+r, r)) % p
            for z, length in ((Q*pow(Y, -1, p), k), (Y*pow(Q, -a-k, p), l),
                              (pow(Q, k-l+1, p)*pow(Y, -1, p), r),
                              (Y*pow(Q, -a-k+l-r, p), a)):
                predicted = predicted*E.pochhammer(z % p, length) % p
            assert actual == predicted, (N, a, k, l, r)
            total = (total+actual) % p
            count += 1
    return total, count


def inverted_intermediate(E, Y):
    N, p, Q, d = E.N, E.p, E.Q, E.N-1
    total = 0
    for m in range(N):
        for b in range(m+1):
            for a in range(b+1):
                for n in range(b, N):
                    exponent = 1+n+b+2*b*b+a*(a-3)//2-a*(2*b+m)
                    v = (pow(-1, a, p)*pow(Y, d+m-2*b, p)*pow(Q, exponent, p)
                         *E.gaussian(n, b)*E.gaussian(m, b)*E.gaussian(b, a)) % p
                    for z, length in ((Q*pow(Y, -1, p), m),
                                      (pow(Q, b-a+1, p)*pow(Y, -1, p), n-b),
                                      (pow(Q, b+1, p)*pow(Y, -1, p), n-b)):
                        v = v*E.pochhammer(z % p, length) % p
                    total = (total+v) % p
    return total


def triple(E, Y):
    N, p, Q, d = E.N, E.p, E.Q, E.N-1
    total = 0
    for m in range(N):
        for b in range(m+1):
            for r in range(N-b):
                v = (pow(Y, m-b, p)*pow(Q, b*b, p)*E.gaussian(m, b)
                     *E.gaussian(d-b, r)*E.pochhammer(Q*pow(Y, -1, p) % p, m)
                     *E.pochhammer(pow(Q, b+1, p)*pow(Y, -1, p) % p, r)
                     *E.pochhammer(pow(Q, -2*b-m-r-1, p), b)) % p
                total = (total+v) % p
    return total


def unproved_newton_target(E, Y):
    N, p, Q = E.N, E.p, E.Q
    total = basis = 1
    for n in range(1, N):
        basis = basis*(Y+pow(Y, -1, p)-pow(Q, n, p)-pow(Q, -n, p)) % p
        coefficient = sum(E.gaussian(n, j)*pow(Q, -j*(n+1), p) for j in range(n+1)) % p
        total = (total+coefficient*basis) % p
    return total


def rogers_and_classical_checks():
    Q, u, Y, L = sp.symbols('Q u Y L')
    rows = gaussian_rows(Q, 7)
    J = [sp.expand(sum(c*Q**(j*(j+1)) for j, c in enumerate(row))) for row in rows]
    for n in range(2, 8):
        assert sp.expand(J[n]-(1+Q-Q**n+Q**(2*n))*J[n-1]
                         +Q*(1-Q**(n-1))*J[n-2]) == 0
    U = (Y*L+1)/(Y+L)
    V = Y+1/Y-U-1/U
    coefficient_curve = 1-(2-U+U**2)*V+(1-U)*V**2
    a = -Y**4+Y**3+3+3/Y-2/Y**2
    b = Y**4-3*Y**3-Y**2+3*Y+6+3/Y-Y**-2-3*Y**-3+Y**-4
    c = -2*Y**2+3*Y+3+Y**-3-Y**-4
    F = L**4+a*L**3+b*L**2+c*L+1
    assert sp.cancel(coefficient_curve-Y**2*F/((Y+L)**2*(Y*L+1)**2)) == 0
    return {'generic_Rogers_indices': list(range(8)),
            'mirrored_candidate_forward_operator':
                'E^2-(1+Q-Q^2*u+Q^4*u^2)*E+Q*(1-Q*u)',
            'exact_classical_longitude_quartic_match': True,
            'operator_scope': 'Rogers sequence only until the source identity is proved'}


def main():
    cases = []
    for N in range(2, 10):
        p, g, q = field(N)
        E = MixedEntries(N, p, q)
        for M in (1, pow(g, 2, p), pow(g, 3, p)):
            x = -M*pow(q, -1, p) % p
            Y = M*M % p
            actual, routes = literal(E, x)
            intermediate = inverted_intermediate(E, Y)
            reduced = triple(E, Y)
            assert actual == intermediate == reduced
            # This test is explicitly NOT a proof of the remaining identity.
            target = unproved_newton_target(E, Y)
            assert target == actual
            cases.append({'N': N, 'meridian': M, 'surviving_routes': routes,
                          'proved_three_index_value': reduced,
                          'unproved_Newton_target_test_agrees': True})
    out = {'status': 'PASS', 'topology_and_full_source': framing_and_topology(),
           'actual_source_and_finite_transforms': cases,
           'generic_Rogers_and_classical_port': rogers_and_classical_checks(),
           'remaining_identity': 'Equation(10) in the companion note is UNPROVED.',
           'scope': 'Actual whole source reduced to three indices. No actual6_1 quantum color operator or volume bound.'}
    Path(__file__).with_name('six_one_actual_source_recurrence_port_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS 24 original whole-source families, route and triple reductions, '
          'generic Rogers recurrence and classical quartic port; Newton source identity UNPROVED')


if __name__ == '__main__':
    main()
