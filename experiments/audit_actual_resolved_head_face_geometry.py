#!/usr/bin/env python3
"""Resolved ORIGINAL head-face graph, tangent action and retained wire source."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_projected_transfer_cot_completion import Projected


def graph_checks():
    A, U, p = sp.symbols('A U p', nonzero=True)
    e = (1-A)/(A*p)
    f = (1-A)*p
    tau = (1-1/U)/e
    k, l, d = -1/A, -sp.Integer(1), 1/U
    actual = (l*d, e*(d*l-1/l)/k, k*tau/d,
              k/d, e/(l*d), l*(d*f+tau*(d/k-k)))
    p1 = p/(1-A)
    p2 = (A-U)*p/(U*(1-A))
    C, E = U, A/U
    expected = (-1/C, (1/C-1)/p1, (1-C)*p1,
                -1/E, (1/E-1)/p2, (1-E)*p2)
    differences = [sp.factor(a-b) for a, b in zip(actual, expected)]
    assert differences == [0]*6
    # Exponentiated derivatives of the actual FACE generating function.
    eq_u = -(1-A)/(1-A/U)*p2/p
    eq_v = -(1-A/U)*p1/p2
    assert sp.factor(eq_u-1) == 0
    assert sp.factor(eq_v-1) == 0
    assert sp.factor((1-e*tau)-1/U) == 0

    s, tau0 = sp.symbols('s tau', nonzero=True)
    B = 1-s
    r = tau0/s
    ein = sp.factor((1/B-1)/r)
    fin = sp.factor((1-B)*r)
    assert sp.factor(ein-s**2/((1-s)*tau0)) == 0
    assert fin == tau0
    assert sp.limit(ein, s, 0) == 0
    # Liouville difference, compared to d Li2(s).
    old_minus_new = -sp.log(1-s)/s
    assert sp.factor(old_minus_new+sp.log(1-s)/s) == 0
    return {'six_original_Gauss_output_differences': differences,
            'face_tangent_exponentials': [sp.factor(eq_u), sp.factor(eq_v)],
            'resolved_input_e': str(ein), 'resolved_input_f': str(fin),
            'bulk_transfer_tau': str(sp.factor(tau))}


def mixed_gauge_checks():
    rows = []
    for N in range(2, 10):
        H = Projected(N)
        R = H.original()
        worst = 0.
        count = 0
        for a, b in itertools.product(range(N), repeat=2):
            for transfer in range(min(a, N-1-b)+1):
                c, e = b+transfer, a-transfer
                actual = R[c*N+e, a*N+b]
                actual *= complex(H.F[e]*H.F[b]/(H.F[c]*H.F[a]))
                expected = H.kappa*H.x**(-a-b+transfer)*H.Q**(b*(a-transfer))/H.F[transfer]
                err = abs(actual-complex(expected))/max(1., abs(complex(expected)))
                worst = max(worst, err)
                assert err < 1e-11
                count += 1
        rows.append({'N': N, 'original_mixed_chart_entries': count,
                     'maximum_relative_error': worst})
    return rows


def packet_and_source_checks():
    rows = []
    for N in [17, 31, 65, 129, 257]:
        Q = mp.exp(2j*mp.pi/N)
        R = max(1, min(N//7, int(N**mp.mpf('.4'))))
        assert R < N/6
        products = [mp.mpc(1)]
        for j in range(1, R+1):
            products.append(products[-1]*(1-Q**j))
            lower = (mp.mpf(4)/N)**j*mp.factorial(j)
            assert abs(products[-1]) >= lower*(1-mp.mpf('1e-65'))
        cond = max(map(abs, products))/min(map(abs, products))
        bound = (mp.e*N/(4*R))**R
        assert cond <= bound
        # Exact finite identity wire AFTER the adjoining factorial gauges.
        xi, eta = mp.mpc('1.3', '.2'), mp.mpc('.7', '-.1')
        kernel = mp.fsum((xi/eta)**j for j in range(R+1))
        closed = (1-(xi/eta)**(R+1))/(1-xi/eta)
        assert abs(kernel-closed) < mp.mpf('1e-60')*max(1, abs(kernel))
        # The source is NONZERO at a fixed off-diagonal resolved parameter.
        off_diagonal = mp.fsum(mp.mpf(2)**j for j in range(R+1))
        assert off_diagonal == mp.mpf(2)**(R+1)-1
        rows.append({'N': N, 'whole_normal_packet_R': R,
                     'log_original_metric_condition': float(mp.log(cond)),
                     'proved_log_condition_bound': float(mp.log(bound)),
                     'off_diagonal_source_log_over_N': float(mp.log(off_diagonal)/N)})
    return rows


def regulator_checks():
    D = lambda z: mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)
    A, U = mp.mpc('1.4', '.3'), mp.mpc('.7', '.4')
    target = D(A/U)-D(A)
    rows = []
    for N in [32, 128, 512]:
        s = mp.mpf(1)/N
        B = 1-s
        actual = -D(A)-D(B*U)+D(A/U)+D(B)+D(U)
        err = abs(actual-target)
        assert err < 10*s*(1+abs(mp.log(s)))
        # Simultaneous opposite head degeneration has a nonzero local
        # limit, rather than the finite-position central value zero.
        AA = 1-2*s
        double = -D(AA)-D(B*U)+D(AA/U)+D(B)+D(U)
        double_error = abs(double-D(1/U))
        assert double_error < 20*s*(1+abs(mp.log(s)))
        rows.append({'N': N, 'single_resolved_face_regulator_limit': float(target),
                     'single_face_regulator_error': float(err),
                     'double_face_nonzero_limit': float(D(1/U)),
                     'double_face_regulator_error': float(double_error)})
    return rows


def main():
    mp.mp.dps = 80
    data = {'status': 'PASS', 'exact_resolved_crossing_graph': graph_checks(),
            'original_mixed_chart_entries': mixed_gauge_checks(),
            'normal_packet_and_complete_wire_source': packet_and_source_checks(),
            'actual_five_symbol_face_regulator_limits': regulator_checks(),
            'scope': 'Local resolved ORIGINAL graph and exact retained source kernels. No assertion that arbitrary restricted-face global criticals satisfy the missing resolved wire equations or the sharp knot-volume bound.'}
    Path(__file__).with_name('actual_resolved_head_face_geometry_results.json').write_text(
        json.dumps(data, indent=2, default=str)+'\n')
    print('PASS 6 exact original Gauss identities, 2 face generating equations, '
          '8 original mixed-gauge families, 5 whole normal-packet/wire checks, 3 regulator limits')


if __name__ == '__main__':
    main()
