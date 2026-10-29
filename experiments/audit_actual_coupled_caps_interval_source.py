#!/usr/bin/env python3
"""Original cap/cup coefficients, whole sources, and their exact interval form."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_borel_regular_fusion import fusion, inv
from audit_actual_cyclic_hardy_dilog_network import CyclicHardyNetwork
from audit_actual_two_cut_ports import word_matrix
from audit_finite_sum_annihilator import field
from audit_relative_pivotal_duality import dual_data


def pair_data(N, complete):
    p, g, q = field(N)
    Q, d = q*q % p, N-1
    x = pow(q, d, p) if complete else g
    y, _, J, pivot = dual_data(N, p, q, x, 0)
    F = [1]
    for a in range(1, N):
        F.append(F[-1]*(1-pow(Q, a, p)) % p)
    DF = np.diag(F).astype(np.int64)
    defect = inv(DF, p) @ inv(pivot, p) @ np.full((N, N), pow(N, -1, p), dtype=np.int64) @ DF % p
    raw_cup = inv(J, p).T.reshape(N*N)
    raw_cap = (pivot @ J % p).reshape(N*N)
    raw_mark = (defect.T @ pivot @ J % p).reshape(N*N)
    cup, cap, mark = [np.zeros(N*N, dtype=np.int64) for _ in range(3)]
    for a, b in itertools.product(range(N), repeat=2):
        j = a*N+b
        cup[j] = int(raw_cup[j])*F[a]*F[b] % p
        cap[j] = int(raw_cap[j])*pow(F[a]*F[b], -1, p) % p
        mark[j] = int(raw_mark[j])*pow(F[a]*F[b], -1, p) % p
        assert int(cup[j]) == (N*pow(x, a-d, p) % p if a+b == d else 0)
        assert int(cap[j]) == (pow(N, -1, p)*pow(y, a, p) % p if a+b == d else 0)
        assert int(mark[j]) == pow(x, b, p)*pow(N, -2, p) % p
    C, Ci, *_ = fusion(N, p, Q, [x, y], [0, 0])
    assert np.array_equal(C[:, d*N], cup)
    row = cap @ C % p
    assert np.count_nonzero(row) == 1 and int(row[d]) == pow(N, -1, p)
    fused_mark = mark @ C % p
    assert np.array_equal(fused_mark @ Ci % p, mark)
    for r in range(N):
        expected = pow(x, d-r, p)*(-1)**r*pow(Q, -r*(r+1)//2, p)*F[r]**2*pow(N, -2, p) % p
        assert int(fused_mark[r*N+d-r]) == expected
        # Coefficient of b^d after terminal F_d and reciprocal F_0 peeling.
        h = r
        v = (-1)**h*pow(Q, h*(h-1)//2, p)*pow(F[h], -1, p) % p
        coefficient = v*pow(F[d-h], -1, p)*pow(x, -h, p) % p
        assert coefficient == pow(N, -1, p)*pow(y, h, p) % p
    # All N coefficients of (t;Q)_(N-1)=K_N(Q^-1 t), including numerator.
    polynomial = [1]
    for a in range(d):
        nxt = [0]*(len(polynomial)+1)
        for j, c in enumerate(polynomial):
            nxt[j] = (nxt[j]+c) % p
            nxt[j+1] = (nxt[j+1]-c*pow(Q, a, p)) % p
        polynomial = nxt
    assert polynomial == [pow(Q, -a, p) for a in range(N)]
    assert int(mark @ cup) % p == 1
    assert int(cap @ cup) % p == 0
    if complete:
        # Original typed five-flag source mark; no unwrapped center imposed.
        def shift(mu):
            S = np.zeros((N, N), dtype=np.int64)
            for j in range(N-1):
                S[j+1, j] = 1
            S[0, N-1] = mu
            return S
        I = np.eye(N, dtype=np.int64)
        S1 = np.kron(shift(1), I)
        S2 = np.kron(I, shift(pow(x, N, p)))
        X = x*S2 @ inv(S1, p) % p
        assert np.array_equal(X @ cup % p, pow(Q, -1, p)*cup % p)
    return {'N': N, 'color': 'complete' if complete else 'generic',
            'all_original_duality_coefficients': N*N,
            'terminal_factor_peeling_coefficients': N,
            'whole_marked_bubble': 1, 'ordinary_bubble': 0}


def whole_sources(N, letters):
    H = CyclicHardyNetwork(N, 1)
    p, x, d = H.p, H.x, N-1
    # These are the literal physical sources, independent of a Ward corner.
    cup = np.zeros(N*N, dtype=np.int64)
    ordinary = np.zeros_like(cup)
    marked = np.zeros_like(cup)
    restricted = np.zeros_like(cup)
    y = pow(x, -1, p)*pow(H.Q, -1, p) % p
    assert x == y
    for a, b in itertools.product(range(N), repeat=2):
        j = a*N+b
        marked[j] = pow(x, b, p)*pow(N, -2, p) % p
        if a+b == d:
            cup[j] = N*pow(x, a-d, p) % p
            ordinary[j] = pow(N, -1, p)*pow(y, a, p) % p
            restricted[j] = marked[j]
    W = word_matrix(letters, H.plus, H.minus, 4, N, p)
    incoming = np.kron(cup, cup) % p
    image = W @ incoming % p
    assert all(int(value) == 0 or sum(index) == 2*d
               for index, value in zip(itertools.product(range(N), repeat=4), image))
    full_row = np.kron(marked, ordinary) % p
    coupled_row = np.kron(restricted, ordinary) % p
    # Not equal as arbitrary rows; equal on the exact original whole source.
    assert np.any(full_row != coupled_row)
    full = int(full_row @ image) % p
    coupled = int(coupled_row @ image) % p
    assert full == coupled
    return {'N': N, 'word': letters, 'original_full_marked_source': full,
            'coupled_degree_restriction_source': coupled,
            'restriction_not_claimed_on_arbitrary_rows': True}


def interval_checks():
    rows = []
    with mp.workdps(70):
        charts = [mp.mpc('.2', '.3'), mp.mpc('-.5', '.8'), mp.mpc('2', '.4'),
                  mp.mpc('1.0000001', '0.0000002'), mp.mpc('.3', '-.7')]
        for N in [2, 3, 4, 7, 16, 31]:
            for r in charts:
                for deck in [0, -1, 1]:
                    L = mp.log(r)+2j*mp.pi*deck
                    exact = mp.fsum(r**a for a in range(N))
                    interval = N*L/(r-1)*mp.quad(lambda s: mp.exp(N*s*L), [0, 1])
                    assert abs(interval-exact) <= mp.mpf('1e-57')*max(1, abs(exact))
                    rows.append({'N': N, 'deck': deck, 'relative_error': float(abs(interval-exact)/max(1, abs(exact)))})
        # The correct local removable factor is on the L=0 sheet.
        assert mp.limit(lambda r: mp.log(r)/(r-1), 1) == 1
    return rows


def deformed_interval_checks():
    rows = []
    with mp.workdps(70):
        for N in [2, 5, 13]:
            for r in [mp.mpc('.3', '.4'), mp.mpc('1.2', '.1'), mp.mpc('-.4', '-.6')]:
                L = mp.log(r)
                for B in [mp.mpc('.2', '.7'), mp.mpc('2', '-.3'), mp.mpc('3', '0')]:
                    point = mp.log(B)/(2j*mp.pi)
                    def segment(a, b):
                        return (b-a)*mp.quad(lambda t: mp.exp(N*(a+(b-a)*t)*L), [0, 1])
                    bent = segment(0, point)+segment(point, 1)
                    direct = mp.quad(lambda s: mp.exp(N*s*L), [0, 1])
                    assert abs(bent-direct) <= mp.mpf('1e-57')*max(1, abs(direct))
                    assert abs(mp.exp(2j*mp.pi*point)-B) < mp.mpf('1e-65')
                    rows.append({'N': N, 'clock': str(B), 'complex_interval_point': str(point),
                                 'endpoint_fixed_path_relative_error': float(abs(bent-direct)/max(1, abs(direct)))})
    return rows


def classical_cap():
    x, B, z = sp.symbols('x B z', nonzero=True)
    def data(xi, Bi, zi):
        K = xi/Bi
        f = (1-Bi)*zi
        e = (1/xi-xi/Bi)/zi
        Lp = sp.Matrix([[K, e], [0, 1]])
        Lm = sp.Matrix([[1, 0], [-K*f, K]])
        return K, f, e, Lp, Lm, Lm.inv()*Lp
    K1, f1, e1, P1, M1, G1 = data(x, B, z)
    K2, f2, e2, P2, M2, G2 = data(1/x, 1/B, x*z)
    assert sp.simplify(K1*K2-1) == 0
    assert sp.simplify(f1+f2/K1) == 0
    assert sp.simplify(e1*K2+e2) == 0
    assert sp.simplify(P2*P1-sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(M2*M1-sp.eye(2)) == sp.zeros(2)
    H1, H2 = G1, M1.inv()*G2*M1
    assert sp.simplify(H2*H1-sp.eye(2)) == sp.zeros(2)
    # This distinction is substantive, not just a choice of notation.
    assert sp.simplify(G2*G1-sp.eye(2)) != sp.zeros(2)
    assert sp.simplify(G1.subs(x, -1).trace()+2) == 0
    assert sp.simplify(G1.det()-1) == 0
    assert sp.simplify(G1.subs({x: -1, B: 1})+sp.eye(2)) == sp.zeros(2)
    return {'general_dual_color_coproduct_e_f_zero_K_one': True,
            'actual_framed_H2_H1_identity': True,
            'raw_G2_G1_not_claimed_identity': True,
            'regular_complete_parabolic_chart': True,
            'regular_interval_endpoint_has_central_meridian': True,
            'interval_clock_source_charge': 'p1+p2=2*pi*i; D+1=N'}


def main():
    pairs = [pair_data(N, complete) for N in range(2, 11) for complete in [False, True]]
    words = [[], [1], [-1, 2, 1, -3], [2, -1, 3, 2, -2, 1]]
    whole = [whole_sources(N, word) for N in [2, 3, 4] for word in words]
    intervals = interval_checks()
    deformations = deformed_interval_checks()
    result = {'scope': 'Exact original coupled sources and regular actual cap relation; no geometric cycle selection.',
              'pairs': pairs, 'whole_original_words': whole,
              'interval_log_chart_checks': intervals, 'exact_complex_clock_path_deformations': deformations,
              'classical_cap': classical_cap()}
    path = Path(__file__).with_name('actual_coupled_caps_interval_source_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(pairs)} literal duality/fusion families, {len(whole)} whole original marked words, '
          f'{len(intervals)} interval/deck identities, {len(deformations)} complex-clock path deformations, '
          'and symbolic actual framed cap holonomy')


if __name__ == '__main__':
    main()
