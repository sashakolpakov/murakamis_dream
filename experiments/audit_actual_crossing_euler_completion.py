#!/usr/bin/env python3
"""Actual R = Euler/Gaussian completion modulo a source-null weight ideal.

Full one-cut matrices, original pivots and external factors are retained.
The comparison is at the actual root and whole meridian parameter, not
an off-root quantum-normal or arbitrary-coupon equivalence.
"""

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_borel_regular_fusion import fusion, right_regular, alg_product, physical_cap
from audit_actual_two_cut_ports import balanced_data, word_matrix, partial
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices


def actual_data(N, M):
    if M == 1:
        p, eta, q, _, _, K, pivot, positive, negative = balanced_data(N)
        x = int(K[0, 0])
        twist = pow(eta, (N-1)*(N+1), p)
        dimension = pow(pow(eta, N, p), N+3, p)*pow(N, -1, p) % p
        return p, q, x, K, pivot, positive, negative, twist, dimension, 'original_full_complete_Cartan'
    p, _, q = field(N)
    x = -M*pow(q, -1, p) % p
    positive, negative, pivotal, twist = color_matrices(N, p, q, x)
    Q = q*q % p
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, p)) % p)
    gauge = np.kron(np.array(fac, dtype=np.int64), np.array(fac, dtype=np.int64))
    gauge_i = np.array([pow(int(t), -1, p) for t in gauge], dtype=np.int64)
    positive = positive*gauge[:, None]*gauge_i[None, :] % p
    negative = negative*gauge[:, None]*gauge_i[None, :] % p
    K = np.diag([x*pow(Q, -a, p) % p for a in range(N)]).astype(np.int64)
    norm = sum(pow(M, 2*j, p) for j in range(N)) % p
    if not norm:
        return None
    eta = pow(-1, N+1, p)*pow(q, N*(1-N)//2, p) % p
    dimension = eta*pow(M, N-1, p)*pow(norm, -1, p) % p
    return p, q, x, K, np.diag(pivotal).copy(), positive, negative, twist, dimension, 'original_generic_ADO_normalization'


def completion(N, p, Q, x, positive, negative):
    C, Ci, central, _, _, _, _ = fusion(N, p, Q, [x, x], [0, 0])
    assert central == 0
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    scalar = int(positive[0, 0])
    exact, completed, euler, diagonal = (np.zeros(N*N, dtype=np.int64) for _ in range(4))
    for a, k in itertools.product(range(N), repeat=2):
        value = (scalar*pow(-1, k, p)*pow(Q, k*(k-1)//2, p)
                 *pow(x, -a-2*k, p)*pow(fac[a], -1, p)) % p
        completed[a*N+k] = value
        if a+k < N:
            exact[a*N+k] = value
        euler[a*N+k] = pow(x, -a, p)*pow(fac[a], -1, p) % p
    for k in range(N):
        diagonal[k] = pow(-1, k, p)*pow(Q, k*(k-1)//2, p)*pow(x, -2*k, p) % p
    assert np.array_equal(completed, scalar*alg_product(euler, diagonal, N, 0, p) % p)
    assert np.array_equal(C@right_regular(exact, N, 0, p)@Ci % p, positive)
    tilde = C@right_regular(completed, N, 0, p)@Ci % p
    error = (tilde-positive) % p
    degree = np.array([a+b for a, b in itertools.product(range(N), repeat=2)])
    for row, column in zip(*np.nonzero(error)):
        assert degree[row]-degree[column] == N
    assert not np.any(error@negative@error % p)
    inverse = (negative-negative@error@negative) % p
    assert np.array_equal(tilde@inverse % p, np.eye(N*N, dtype=np.int64))
    assert np.array_equal(inverse@tilde % p, np.eye(N*N, dtype=np.int64))
    for row, column in zip(*np.nonzero((inverse-negative) % p)):
        assert degree[row]-degree[column] == N
    return tilde, inverse


def case(N, strands, M):
    data = actual_data(N, M)
    if data is None:
        return None
    p, q, x, K, pivot, plus, minus, twist, dimension, normalization = data
    Q = q*q % p
    completed_plus, completed_minus = completion(N, p, Q, x, plus, minus)
    if strands == 2:
        words = [(1,), (1, 1, 1), (1, -1), (-1, -1, -1)]
    elif strands == 3:
        words = [(1, -2, 1, -2), (1, 2, -1, 2, 1, -2), (2, -1, 2, -1)]
    else:
        words = [(1, 2, 3, -2, -1, 3), (1, -2, 3, 1, -2, 3)]
    degree = np.array([sum(state) for state in itertools.product(range(N), repeat=strands)])
    nonzero_word_errors = 0
    periods = []
    for word in words:
        actual = word_matrix(word, plus, minus, strands, N, p)
        softened = word_matrix(word, completed_plus, completed_minus, strands, N, p)
        error = (softened-actual) % p
        nonzero_word_errors += int(bool(np.any(error)))
        for row, column in zip(*np.nonzero(error)):
            delta = int(degree[row]-degree[column])
            assert delta >= N and delta % N == 0
        exact_cut = partial(actual, pivot, strands, N, p)
        completed_cut = partial(softened, pivot, strands, N, p)
        assert np.array_equal(exact_cut, completed_cut)
        writhe = sum(1 if letter > 0 else -1 for letter in word)
        external = dimension*pow(twist, -writhe, p) % p
        assert np.array_equal(external*exact_cut % p, external*completed_cut % p)
        periods.append(int(external*exact_cut[0, 0]) % p)
    braid_defect_nonzero = None
    if strands == 3:
        left = word_matrix((1, 2, 1), completed_plus, completed_minus, 3, N, p)
        right = word_matrix((2, 1, 2), completed_plus, completed_minus, 3, N, p)
        defect = (left-right) % p
        braid_defect_nonzero = bool(np.any(defect))
        for row, column in zip(*np.nonzero(defect)):
            delta = int(degree[row]-degree[column])
            assert delta >= N and delta % N == 0
        assert not np.any(partial(defect, pivot, 3, N, p))
    return {'N': N, 'strands': strands, 'M': M, 'field': p,
            'normalization': normalization, 'word_count': len(words),
            'nonzero_word_errors_in_positive_weight_ideal': nonzero_word_errors,
            'completed_braid_defect_nonzero': braid_defect_nonzero,
            'original_full_periods': periods,
            'full_first_cut_matrix_retained': True,
            'all_original_pivots_dimension_twist_and_Cartan_retained': True}


def mixed_case(N):
    p, _, q = field(N)
    Q, x1, x2, scalar = q*q % p, 3, 7, 2
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    actual = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        poch = 1
        for k in range(min(a, N-1-b)+1):
            if k:
                poch = poch*(1-x1*x1*pow(Q, k-a, p)) % p
            gaussian = fac[b+k]*pow(fac[b]*fac[k], -1, p) % p
            coefficient = (scalar*pow(-1, k, p)*pow(x1, -b-2*k, p)
                           *pow(x2, -a+k, p)*pow(Q, a*b+(a-b)*k-k*(k+1)//2, p)
                           *gaussian*poch) % p
            actual[(b+k)*N+a-k, a*N+b] = coefficient
    C_in, Ci_in, *_ = fusion(N, p, Q, [x1, x2], [0, 0])
    C_out, _, *_ = fusion(N, p, Q, [x2, x1], [0, 0])
    exact, completed = (np.zeros(N*N, dtype=np.int64) for _ in range(2))
    for a, k in itertools.product(range(N), repeat=2):
        value = (scalar*pow(-1, k, p)*pow(Q, k*(k-1)//2, p)
                 *pow(x1, -a, p)*pow(x1*x2, -k, p)*pow(fac[a], -1, p)) % p
        completed[a*N+k] = value
        if a+k < N:
            exact[a*N+k] = value
    assert np.array_equal(C_out@right_regular(exact, N, 0, p)@Ci_in % p, actual)
    softened = C_out@right_regular(completed, N, 0, p)@Ci_in % p
    error = (softened-actual) % p
    degree = np.array([a+b for a, b in itertools.product(range(N), repeat=2)])
    for row, column in zip(*np.nonzero(error)):
        assert degree[row]-degree[column] == N
    return {'N': N, 'field': p, 'colors': [x1, x2],
            'retained_common_Cartan_scalar': scalar,
            'exact_mixed_color_relative_formula': True}


def counterexamples():
    data = actual_data(2, 1)
    p, q, x, K, _, positive, negative, *_ = data
    completed, _ = completion(2, p, q*q % p, x, positive, negative)
    error = (completed-positive) % p
    E = np.array([[0, -2], [0, 0]], dtype=np.int64) % p
    coupon_value = physical_cap(np.kron(np.eye(2, dtype=np.int64), E)@error % p,
                                 [K, K], 2, p)
    assert coupon_value == 2*int(positive[0, 0]) % p != 0

    Z, h = sp.symbols('Q x', nonzero=True)
    R = sp.Matrix([[1, 0, 0, 0], [0, 0, 1/h, 0],
                   [0, 1/h, 1-h**-2, 0], [0, 0, 0, Z*h**-2]])
    softened = sp.Matrix([[1, 0, 0, 0], [0, 0, 1/h, 0],
                          [0, 1/h, 1-h**-2, 0], [-h**-3, 0, 0, -h**-2]])
    def symbolic_word(local):
        out = sp.eye(8)
        inverse = local.inv()
        for letter in (1, -2, 1, -2):
            factor = local if letter > 0 else inverse
            operator = (sp.kronecker_product(factor, sp.eye(2)) if abs(letter) == 1
                        else sp.kronecker_product(sp.eye(2), factor))
            out = operator*out
        return out
    actual_word, completed_word = symbolic_word(R), symbolic_word(softened)
    pivot = [1/h, Z/h]
    defect = sp.factor(sum(pivot[a]*pivot[b]
                          *(completed_word[2*a+b, 2*a+b]-actual_word[2*a+b, 2*a+b])
                          for a, b in itertools.product(range(2), repeat=2)))
    assert sp.simplify(defect-Z*(Z+1)*(h*h-1)/(h*h)) == 0
    normal = sp.factor((Z*sp.diff(defect, Z)).subs(Z, -1))
    assert sp.simplify(normal-(h*h-1)/(h*h)) == 0
    assert sp.simplify(normal.subs(h, sp.I)) == 2
    return {'negative_weight_coupon_N2_value': int(coupon_value),
            'negative_weight_coupon_exact': '2*eta',
            'natural_offroot_figure_eight_cut_defect': str(defect),
            'offroot_Q_normal_at_root': str(normal),
            'complete_Q_normal_defect': 2}


def meridian_transport_case(N):
    p, _, q = field(N)
    Q, M, strands = q*q % p, 3, 3
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    gauge = np.kron(np.array(fac, dtype=np.int64), np.array(fac, dtype=np.int64))
    gauge_i = np.array([pow(int(t), -1, p) for t in gauge], dtype=np.int64)
    fibers = []
    for point in (M, q*M % p):
        x = -point*pow(q, -1, p) % p
        plus, minus, pivotal, _ = color_matrices(N, p, q, x)
        plus = plus*gauge[:, None]*gauge_i[None, :] % p
        minus = minus*gauge[:, None]*gauge_i[None, :] % p
        softened_plus, softened_minus = completion(N, p, Q, x, plus, minus)
        fibers.append((plus, minus, softened_plus, softened_minus, np.diag(pivotal).copy()))
    word = (1, -2, 1, -2)
    inverse_word = tuple(-letter for letter in reversed(word))
    plus, minus, softened_plus, softened_minus, pivot = fibers[0]
    actual_inverse = word_matrix(inverse_word, plus, minus, strands, N, p)
    softened_inverse = word_matrix(inverse_word, softened_plus, softened_minus, strands, N, p)
    plus1, minus1, softened_plus1, softened_minus1, _ = fibers[1]
    actual = word_matrix(word, plus1, minus1, strands, N, p)@actual_inverse % p
    softened = word_matrix(word, softened_plus1, softened_minus1, strands, N, p)@softened_inverse % p
    error = (softened-actual) % p
    degree = np.array([sum(state) for state in itertools.product(range(N), repeat=strands)])
    for row, column in zip(*np.nonzero(error)):
        delta = int(degree[row]-degree[column])
        assert delta >= N and delta % N == 0
    assert np.array_equal(partial(actual, pivot, strands, N, p),
                          partial(softened, pivot, strands, N, p))
    return {'N': N, 'field': p, 'word': list(word),
            'two_fiber_meridian_matrix_projection': True,
            'entire_original_cut_preserved': True}


def main():
    rows = []
    for N, strands in ([(n, 2) for n in range(2, 9)]
                       +[(n, 3) for n in range(2, 6)]+[(2, 4), (3, 4)]):
        for M in (1, 3):
            row = case(N, strands, M)
            if row is not None:
                rows.append(row)
    mixed = [mixed_case(N) for N in range(2, 8)]
    boundaries = counterexamples()
    transports = [meridian_transport_case(N) for N in range(2, 6)]
    result = {'status': 'PASS', 'cases': rows, 'mixed_color_cases': mixed,
              'verified_scope_boundaries': boundaries,
              'matrix_meridian_transports': transports,
              'scope': 'Actual arbitrary signed braid root-meridian family, Euler/Gaussian completion and bounded positive-weight null ideal. Not a generic-q or arbitrary-coupon equivalence.'}
    Path(__file__).with_name('actual_crossing_euler_completion_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'case_count': len(rows),
                      'whole_words': sum(r['word_count'] for r in rows),
                      'mixed_color_cases': len(mixed),
                      'matrix_meridian_transports': len(transports),
                      'nonzero_word_errors': sum(r['nonzero_word_errors_in_positive_weight_ideal'] for r in rows)}))


if __name__ == '__main__':
    main()
