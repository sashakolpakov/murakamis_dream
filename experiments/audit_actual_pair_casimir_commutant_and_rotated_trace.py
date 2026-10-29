#!/usr/bin/env python3
"""Original pair E/F/K commutant, actual turn rotation and marked trace.

The commutant audit includes all K-preserving maps, including potential
degree +/-N maps.  The proof eliminates these rather than assuming an
unrolled grading.  Every matrix identity is checked in a root field.
"""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_odd_pretzel_augmented_transfer_source import literal_source


def rank(A, prime):
    A = np.array(A, dtype=np.int64, copy=True) % prime
    row = 0
    for col in range(A.shape[1]):
        pivots = np.flatnonzero(A[row:, col])
        if not len(pivots):
            continue
        pivot = row+int(pivots[0])
        A[[row, pivot]] = A[[pivot, row]]
        A[row, col:] = A[row, col:]*pow(int(A[row, col]), -1, prime) % prime
        if row+1 < A.shape[0]:
            A[row+1:, col:] = (A[row+1:, col:]
                               -A[row+1:, col, None]*A[row, None, col:]) % prime
        row += 1
        if row == min(A.shape):
            break
    return row


def solve(A, b, prime):
    A = np.column_stack((A, b)).astype(np.int64) % prime
    n = A.shape[0]
    for j in range(n):
        pos = next(k for k in range(j, n) if A[k, j])
        A[[j, pos]] = A[[pos, j]]
        A[j] = A[j]*pow(int(A[j, j]), -1, prime) % prime
        for k in range(n):
            if k != j and A[k, j]:
                A[k] = (A[k]-A[k, j]*A[j]) % prime
    return A[:, -1]


def rotated(B, N, x, prime):
    d = N-1
    Z = np.zeros_like(B)
    for a, b, c, e in itertools.product(range(N), repeat=4):
        Z[a*N+b, c*N+e] = (pow(x, c-b-d, prime)
                            *int(B[(d-a)*N+c, b*N+d-e])) % prime
    return Z


def phi(B, N, pivot, prime):
    return (sum(int(pivot[b])*int(B[a*N+b, a*N+b])
                for a, b in itertools.product(range(N), repeat=2))
            *pow(N, -1, prime)) % prime


def hermite_monomial(N, q, degree, prime):
    d, total = N-1, 0
    for j in range((d+1)//2):
        c = (pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime
        derivative = degree*pow(c, degree-1, prime) % prime if degree else 0
        total += ((4-c*c)*derivative-c*pow(c, degree, prime))
    total *= pow(-1, d, prime)
    if N % 2:
        total += pow(-2, degree, prime)
    return total % prime


def unrestricted_commutant_dimension(Et, Ft, Kt, prime):
    size = Et.shape[0]
    kval = np.diag(Kt)
    variables = [(a, b) for a in range(size) for b in range(size) if kval[a] == kval[b]]
    positions = {key: index for index, key in enumerate(variables)}
    rows = []
    for A in (Et, Ft):
        nzrow = [np.flatnonzero(A[a]) for a in range(size)]
        nzcol = [np.flatnonzero(A[:, b]) for b in range(size)]
        for a, b in itertools.product(range(size), repeat=2):
            terms = {}
            for k in nzcol[b]:
                key = positions.get((a, int(k)))
                if key is not None:
                    terms[key] = terms.get(key, 0)+int(A[k, b])
            for k in nzrow[a]:
                key = positions.get((int(k), b))
                if key is not None:
                    terms[key] = terms.get(key, 0)-int(A[a, k])
            if terms:
                row = np.zeros(len(variables), dtype=np.int64)
                for key, value in terms.items():
                    row[key] = value % prime
                if np.any(row):
                    rows.append(row)
    actual_rank = rank(np.array(rows), prime)
    return len(variables), len(variables)-actual_rank


def field_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, x = N-1, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    size = N*N
    ids = [[a*N+T-a for a in range(max(0, T-d), min(d, T)+1)]
           for T in range(2*d+1)]
    assert [j for j in range(size) if Kt[j, j] == 1] == ids[d]
    assert np.array_equal(O.T, O)
    for operator in (Et, Ft, Kt):
        assert not np.any((operator@O-O@operator) % prime)
    for T in range(d):
        assert rank(Et[np.ix_(ids[T], ids[T+1])], prime) == T+1
    for T in range(d, 2*d):
        assert rank(Ft[np.ix_(ids[T+1], ids[T])], prime) == 2*d-T
    powers = [np.eye(size, dtype=np.int64)]
    for _ in range(1, N):
        powers.append(O@powers[-1] % prime)
    J = O[np.ix_(ids[d], ids[d])]
    krylov = np.column_stack([B[np.ix_(ids[d], ids[d])][:, 0] for B in powers])
    assert rank(krylov, prime) == N
    if N <= 8:
        variables, dim = unrestricted_commutant_dimension(Et, Ft, Kt, prime)
        assert variables == N**3
        assert dim == N
    else:
        variables, dim = N**3, None
    for r, B in enumerate(powers):
        assert phi(B, N, pivot, prime) == hermite_monomial(N, q, r, prime)
        assert phi(B, N, pivot, prime) == int(B[ids[d][0], ids[d][-1]])
        Z = rotated(B, N, x, prime)
        assert np.array_equal(rotated(Z, N, x, prime), pow(x, -2*d, prime)*B % prime)
        # Actual turn composition, with both original N factors cancelling.
        turn = np.zeros_like(B)
        for a, b, c, e in itertools.product(range(N), repeat=4):
            turn[a*N+b, c*N+e] = (pow(x, a-e-d, prime)
                                   *int(B[b*N+d-e, (d-a)*N+c])) % prime
        assert np.array_equal(Z, turn)
        for operator in (Et, Ft, Kt):
            assert not np.any((operator@Z-Z@operator) % prime)
        coeff = solve(krylov, Z[np.ix_(ids[d], ids[d])][:, 0], prime)
        expected = np.zeros_like(O)
        for value, Bk in zip(coeff, powers):
            expected = (expected+int(value)*Bk) % prime
        assert np.array_equal(Z, expected)
        for h in range(-d, d+1):
            T = d+h
            colors = list(range(max(0, h), min(d, d+h)+1))
            M = np.array([[pow(x, -2*a+h, prime)
                           *int(B[(a-h)*N+d-b+h, a*N+d-b]) % prime
                           for b in colors] for a in colors], dtype=np.int64)
            S = np.diag([pow(x, a, prime) for a in colors])
            Si = np.diag([pow(x, -a, prime) for a in colors])
            P = np.eye(len(colors), dtype=np.int64)[::-1]
            assert np.array_equal(Z[np.ix_(ids[T], ids[T])], P@S@M@Si@P % prime)
    assert np.array_equal(rotated(Rm, N, x, prime), pow(x, -d, prime)*Rp % prime)
    assert phi(Rp, N, pivot, prime) == pow(eta, d*d, prime)*pow(x, -d, prime) % prime
    a, b = np.eye(size, dtype=np.int64), O.copy()
    for _ in range(2, N):
        a, b = b, (O@b-a) % prime
    L = pow(-1, d, prime)*b % prime
    assert phi(L, N, pivot, prime) == N*N % prime
    cup = np.array([N*pow(x, -v, prime) % prime if u+v == d else 0
                    for u, v in itertools.product(range(N), repeat=2)], dtype=np.int64)
    ell = np.array([pow(x, u, prime)*pow(N, -1, prime) % prime if u+v == d else 0
                    for u, v in itertools.product(range(N), repeat=2)], dtype=np.int64)
    Pi = np.outer(cup, ell) % prime
    assert not np.any(Et@cup % prime)
    assert not np.any(Ft@cup % prime)
    assert np.array_equal(Kt@cup % prime, cup)
    assert not np.any(ell@Et % prime)
    assert not np.any(ell@Ft % prime)
    assert np.array_equal(ell@Kt % prime, ell)
    assert np.array_equal(rotated(np.eye(size, dtype=np.int64), N, x, prime),
                          pow(x, -d, prime)*Pi % prime)
    assert phi(Pi, N, pivot, prime) == 1
    return {'N': N, 'field': prime, 'all_K_preserving_unknowns': variables,
            'full_E_F_K_commutant_dimension': dim,
            'middle_unique_K_weight_and_cyclic_generation': True,
            'all_original_Casimir_basis_turn_rotations': True,
            'all_Hermite_values_and_normal_trace_weights': True,
            'literal_crossing_Cartan_and_rank_one_turn_normalizations': True}, (prime, x, pivot, O, Rp, Rm, L)


def source_case(N, s, generic, data):
    prime, x, pivot, O, Rp, Rm, L = data
    if generic:
        rng = np.random.default_rng(9300+N+s)
        boxes = []
        for _ in range(s):
            B = np.zeros_like(O)
            for a, b, c, e in itertools.product(range(N), repeat=4):
                if a+b == c+e:
                    B[a*N+b, c*N+e] = int(rng.integers(0, prime))
            boxes.append(B)
    else:
        alphabet = [Rm@L % prime, Rp, O]
        boxes = [alphabet[i % len(alphabet)] for i in range(s)]
    product = np.eye(N*N, dtype=np.int64)
    for B in boxes:
        product = product@rotated(B, N, x, prime) % prime
    expected = pow(x, s*(N-1), prime)*phi(product, N, pivot, prime) % prime
    assert literal_source(N, x, prime, boxes) == expected
    return {'N': N, 'odd_boxes': s, 'generic_degree_boxes': generic,
            'literal_full_marked_source_equals_rotated_pair_period': True}


if __name__ == '__main__':
    rows, data = [], {}
    for N in range(2, 11):
        row, data[N] = field_case(N)
        rows.append(row)
    sources = [source_case(N, 3, generic, data[N]) for N in (2, 3, 4)
               for generic in (False, True)]
    sources += [source_case(2, 5, generic, data[2]) for generic in (False, True)]
    results = {'status': 'PASS', 'original_pair_commutant_rotation_and_trace': rows,
               'whole_original_marked_product_sources': sources,
               'scope': 'All-N exact pair/rotation/marked Hermite reduction; no geometric growth or positivity theorem.'}
    Path(__file__).with_name('actual_pair_casimir_commutant_and_rotated_trace_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS 9 full original pair levels; 7 unrestricted E/F/K commutants; 8 whole marked rotated-product sources')
