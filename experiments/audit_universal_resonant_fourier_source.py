#!/usr/bin/env python3
"""Exact original-matrix audit of the first-slot resonant Fourier source.

The literal two-cut tensor includes every original pivot, twist and d_N.
No geometric principal density is substituted for this finite tensor.
"""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_one_index_fourier_source import actual_case


def evaluate(T, X, p):
    return np.einsum('cdab,bd->ca', T, X) % p


def check_case(N, strands, braid, M):
    # P is an actual negative first crossing, with its positive inverse.
    word = [(0, -1), (0, 1)] + braid
    rec = actual_case(N, strands, word, 1, 0, M,
                      root=True, include_arrays=True)
    if rec is None:
        return None
    p, Q = rec['prime'], rec['Q']
    T = np.array(rec['raw_two_cut_tensor'], dtype=np.int64)
    raw = np.array(rec['raw_fourier_array'], dtype=np.int64)
    B = np.diag([pow(Q, a, p) for a in range(N)]).astype(np.int64)
    Bi = np.diag([pow(Q, -a, p) for a in range(N)]).astype(np.int64)
    E, F = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    for a in range(1, N):
        E[a-1, a] = (M*pow(Q, -a, p)-pow(M, -1, p)) % p
        F[a, a-1] = (1-pow(Q, a, p)) % p
    # Scaling K by x only scales ad_E, so use K=B^-1 here.
    operations = [lambda X: Bi@X@B % p,
                  lambda X: (E@X-X@E)@B % p,
                  lambda X: (F@X-B@X@Bi@F) % p]
    units = 0
    for b, d in itertools.product(range(N), repeat=2):
        X = np.zeros((N, N), dtype=np.int64)
        X[b, d] = 1
        for op in operations:
            assert np.array_equal(evaluate(T, op(X), p), op(evaluate(T, X, p)))
        units += 1
    period = rec['original_period']
    kappa = (M-pow(M, -1, p)) % p
    wrap = np.zeros((N, N), dtype=np.int64)
    wrap[N-1, 0] = 1
    currents = []
    for j in range(N):
        eta = pow(Q, j, p)
        X = np.array([[pow(Q, j*(d-b), p)*pow(N, -1, p) % p
                       for d in range(N)] for b in range(N)], dtype=np.int64)
        Y = evaluate(T, X, p)
        assert np.array_equal(np.sum(Y, axis=0) % p, raw[:, j])
        assert int(Y[0, 0]) == period*pow(N, -1, p) % p
        if M*M % p == 1:
            assert np.array_equal(Y, period*X % p)
        R = evaluate(T, (wrap@X-X@wrap)@B % p, p)
        wrap_row = int(np.sum(R[:, 0])) % p
        lhs = (M*(eta-pow(Q, -1, p))*int(raw[0, (j+1) % N])
               +(M-pow(M, -1, p)*eta)*int(raw[0, j])) % p
        rhs = kappa*eta*(period*pow(N, -1, p)-wrap_row) % p
        assert lhs == rhs
        for a in range(N):
            lhs_f = (1-eta)*int(raw[a, j]) % p
            rhs_f = (pow(Q, a+1, p)-pow(Q, -1, p)*eta)*int(raw[a, (j-1) % N])
            if a+1 < N:
                rhs_f += (1-pow(Q, a+1, p))*int(raw[a+1, (j-1) % N])
            assert lhs_f == rhs_f % p
        currents.append(int(wrap_row))
    if M*M % p == 1:
        expected = np.zeros_like(raw)
        expected[:, 0] = period
        assert np.array_equal(raw, expected)
    return {'N': N, 'strands': strands, 'braid': braid, 'M': M,
            'prime': p, 'Q': Q, 'full_period': int(period),
            'all_generator_equivariance_units': units,
            'actual_full_d_N': rec['retained_full_d_N'],
            'actual_fourier_array': raw.tolist(),
            'highest_wrap_current': currents,
            'complete_delta_array': bool(M*M % p == 1),
            'complete_matrix_projector_identity': bool(M*M % p == 1)}


def main():
    records = []
    for N in range(2, 7):
        for M in (1, 3):
            for braid in [[(0, 1)], [(0, 1)]*3, [(0, -1)]*3]:
                rec = check_case(N, 2, braid, M)
                if rec is not None:
                    records.append(rec)
    for N in range(2, 5):
        for M in (1, 3):
            rec = check_case(N, 3, [(0, 1), (1, -1), (0, 1), (1, -1)], M)
            if rec is not None:
                records.append(rec)
    # A concrete retained word-dependent meridian wrap/source witness.
    witnesses = []
    for left, right in itertools.combinations(records, 2):
        if (left['N'], left['M'], left['prime']) != (right['N'], right['M'], right['prime']):
            continue
        if left['M'] == 1 or not left['full_period'] or not right['full_period']:
            continue
        p = left['prime']
        lrow = [v*pow(left['full_period'], -1, p) % p for v in left['actual_fourier_array'][0]]
        rrow = [v*pow(right['full_period'], -1, p) % p for v in right['actual_fourier_array'][0]]
        if lrow != rrow:
            witnesses.append({'N': left['N'], 'M': left['M'], 'prime': p,
                              'left_braid': left['braid'], 'right_braid': right['braid'],
                              'left_normalized_highest_row': lrow,
                              'right_normalized_highest_row': rrow})
            break
    assert witnesses, 'Need an actual word-dependent meridian profile witness'
    result = {'status': 'PASS',
              'scope': 'Original first-slot finite Fourier source, Hopf rows and complete delta localization; no selected geometric-period or volume assertion.',
              'cases': records,
              'case_count': len(records),
              'generator_equivariance_matrix_units': sum(r['all_generator_equivariance_units'] for r in records),
              'word_dependent_off_complete_profile_witness': witnesses[0]}
    target = Path(__file__).with_name('universal_resonant_fourier_source_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status', 'case_count', 'generator_equivariance_matrix_units',
                                          'word_dependent_off_complete_profile_witness')}, indent=2))


if __name__ == '__main__':
    main()
