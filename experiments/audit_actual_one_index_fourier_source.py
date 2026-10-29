#!/usr/bin/env python3
"""Actual one-exterior-index source reduction and whole balanced Ward rows.

Finite-field assertions are exact. Complex singular values only check the
separately proved root metric estimate; they are not used as proof.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field, cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices


def inverse(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p), dtype=np.int64) % p


def ward(C, Q, p):
    N = len(C)
    K = np.diag([pow(Q, -j, p) for j in range(N)]).astype(np.int64)
    Ki = np.diag([pow(Q, j, p) for j in range(N)]).astype(np.int64)
    F = np.zeros_like(C)
    for k in range(1, N):
        F[k, k-1] = (1-pow(Q, k, p)) % p
    return (K@C@Ki-C) % p, (F@C-Ki@C@K@F) % p


def contract(X, Q, p):
    XK, XF = X
    N = len(XK)
    result = np.zeros_like(XK)
    for i, j in itertools.product(range(N), repeat=2):
        if i != j:
            result[i, j] = int(XK[i, j])*pow((pow(Q, j-i, p)-1) % p, -1, p) % p
    for k in range(1, N):
        d = int(XF[k, k-1])*pow((1-pow(Q, k, p)) % p, -1, p) % p
        for i in range(N):
            step = ((N-k)*pow(N, -1, p)-int(i >= k)) % p
            result[i, i] = (int(result[i, i])+d*step) % p
    return result


def lambda_a(C, a, p):
    return sum(int(C[c, a]) for c in range(len(C))) % p


def phi(C, p):
    return int(np.sum(C))*pow(len(C), -1, p) % p


def contraction_case(N, root):
    p, generator, q = field(N)
    if not root:
        q = generator
    Q = q*q % p
    assert len({pow(Q, j, p) for j in range(N)}) == N
    count = 0
    for i, j in itertools.product(range(N), repeat=2):
        C = np.zeros((N, N), dtype=np.int64)
        C[i, j] = 1
        recovered = contract(ward(C, Q, p), Q, p)
        expected = (C-int(i == j)*pow(N, -1, p)*np.eye(N, dtype=np.int64)) % p
        assert np.array_equal(recovered, expected)
        for a in range(N):
            lhs = (lambda_a(C, a, p)-phi(C, p)) % p
            rhs = (lambda_a(recovered, a, p)-phi(recovered, p)) % p
            assert lhs == rhs
        count += 1
    # Literal two-cut unknot followed by E00: actual inserted-source failure.
    P0 = np.zeros((N, N), dtype=np.int64)
    P0[0, 0] = 1
    assert phi(P0, p) == pow(N, -1, p)
    assert lambda_a(P0, 0, p) == 1
    assert lambda_a(P0, 1, p) == 0
    assert any(np.any(x) for x in ward(P0, Q, p))
    return {"N": N, "primitive_root": root, "matrix_units": count,
            "whole_h_delta_and_all_actual_source_rows": True,
            "actual_unknot_matrix_unit_source_counterexample": True}


def embed(A, position, strands, N):
    value = np.ones((1, 1), dtype=np.int64)
    for s in range(strands):
        value = np.kron(value, A if s == position else np.eye(N, dtype=np.int64))
    return value


def actual_case(N, strands, word, split, slot, M, root=True, include_arrays=False):
    p, generator, qroot = field(N)
    q = qroot if root else generator
    Q = q*q % p
    M %= p
    x = -M*pow(q, -1, p) % p
    positive, negative, pivot, theta = color_matrices(N, p, q, x)
    diagonal = [1]
    for j in range(1, N):
        diagonal.append(diagonal[-1]*(1-pow(Q, j, p)) % p)
    diagonal = np.array(diagonal, dtype=np.int64)
    frame = np.kron(diagonal, diagonal)
    framei = np.array([pow(int(d), -1, p) for d in frame])
    positive = positive*frame[:, None]*framei[None, :] % p
    negative = negative*frame[:, None]*framei[None, :] % p

    def wordmatrix(letters):
        value = np.eye(N**strands, dtype=np.int64)
        for position, sign in reversed(letters):
            op = positive if sign > 0 else negative
            left = np.eye(N**position, dtype=np.int64)
            right = np.eye(N**(strands-position-2), dtype=np.int64)
            value = value@np.kron(np.kron(left, op), right) % p
        return value

    A, B = wordmatrix(word[split:]), wordmatrix(word[:split])
    writhe = sum(sign for _, sign in word)
    eta = pow(-1, N+1, p)*pow(qroot, N*(1-N)//2, p) % p
    S_N = sum(pow(M, 2*j, p) for j in range(N)) % p
    if not S_N:
        return None
    d_N = eta*pow(M, N-1, p)*pow(S_N, -1, p) % p
    external = d_N*pow(theta, -writhe, p) % p

    def close(C):
        result = np.zeros((N, N), dtype=np.int64)
        for c, a in itertools.product(range(N), repeat=2):
            for indices in itertools.product(range(N), repeat=strands-1):
                row, col, weight = c, a, 1
                for j in indices:
                    row, col = row*N+j, col*N+j
                    weight = weight*int(pivot[j, j]) % p
                result[c, a] = (int(result[c, a])+weight*int(C[row, col])*external) % p
        return result

    T = np.zeros((N, N, N, N), dtype=np.int64)
    for b, d in itertools.product(range(N), repeat=2):
        X = np.zeros((N, N), dtype=np.int64)
        X[b, d] = 1
        T[:, d, :, b] = close(A@embed(X, slot, strands, N)@B % p)
    C = sum((T[:, b, :, b] for b in range(N)), np.zeros((N, N), dtype=np.int64)) % p
    assert np.array_equal(C, close(A@B % p))
    discrepancy = contract(ward(C, Q, p), Q, p)
    assert np.array_equal(discrepancy, (C-int(np.trace(C))*pow(N, -1, p)*np.eye(N, dtype=np.int64)) % p)
    is_scalar = np.array_equal(C, int(C[0, 0])*np.eye(N, dtype=np.int64) % p)
    if root:
        assert is_scalar
        assert not any(np.any(z) for z in ward(C, Q, p))
    V = np.array([[pow(Q, j*b, p) for b in range(N)] for j in range(N)], dtype=np.int64)
    bigV = np.kron(np.eye(N, dtype=np.int64), V)
    TV = (bigV@T.reshape(N*N, N*N)@inverse(bigV, p) % p).reshape(N, N, N, N)
    raw = np.array([[sum(int(TV[c, j, a, j]) for c in range(N)) % p
                     for j in range(N)] for a in range(N)], dtype=np.int64)
    original = phi(C, p)
    for a in range(N):
        row_sum = int(np.sum(raw[a, :])) % p
        assert row_sum == lambda_a(C, a, p)
        assert (row_sum-original) % p == (lambda_a(discrepancy, a, p)-phi(discrepancy, p)) % p
        if root:
            assert row_sum == original
    result = {"N": N, "strands": strands, "word": word, "M": M,
            "primitive_root": root, "actual_whole_V_source": True,
            "root_scalar": bool(is_scalar), "original_period": int(original),
            "fixed_column_sums": [int(sum(int(y) for y in raw[a, :]) % p) for a in range(N)],
            "retained_full_d_N": int(d_N),
            "whole_source_difference_is_actual_Ward_row": True}
    if include_arrays:
        result.update({"prime": p, "Q": Q, "raw_fourier_array": raw.tolist(),
                       "raw_two_cut_tensor": T.tolist()})
    return result


def metric_case(N):
    Q = np.exp(2j*np.pi/N)
    hdiag = np.empty((N, N-1), dtype=complex)
    for k in range(1, N):
        hdiag[:, k-1] = ((N-k)/N-(np.arange(N) >= k))/(1-Q**k)
    norm = np.linalg.norm(hdiag, 2)
    assert norm <= 3*N/4+1e-8
    gamma = np.zeros((N, N), dtype=float)
    gamma[0, :] = 1
    gamma -= np.ones((N, N))/N
    assert abs(np.linalg.norm(gamma, 'fro')-np.sqrt(N-1)) < 1e-10
    return {"N": N, "balanced_chain_operator_norm": float(norm),
            "proven_h_bound": 3*N/4,
            "actual_source_difference_norm": float(np.sqrt(N-1))}


def phase_case(pnum, d):
    cases = 0
    for N in range(2, 101):
        a, r = divmod(pnum*N, d)
        assert 0 <= a < N
        # Whole marked Z=Q^N cover, not its frozen root value.
        assert sp.Rational(pnum*N-r, d) == a
        root_lhs = np.exp(2j*np.pi*a/N)
        root_rhs = np.exp(2j*np.pi*pnum/d)*np.exp(-2j*np.pi*r/(d*N))
        assert abs(root_lhs-root_rhs) < 1e-12
        cases += 1
    return {"numerator": pnum, "denominator": d, "levels": cases,
            "root_phase_and_whole_logarithmic_derivative": True}


def actual_symbolic_normal_defect():
    Q, x, M = sp.symbols('Q x M', nonzero=True)
    crossing = sp.Matrix([[1, 0, 0, 0], [0, 0, 1/x, 0],
                          [0, 1/x, 1-1/x**2, 0], [0, 0, 0, Q/x**2]])
    pivot = [1/x, Q/x]
    cut = sp.zeros(2)
    for c, a, b in itertools.product(range(2), repeat=3):
        cut[c, a] += x*pivot[b]*crossing[2*c+b, 2*a+b]
    expected = sp.diag(1, 1+(Q**2-1)/x**2)
    assert (cut-expected).applyfunc(sp.simplify) == sp.zeros(2)
    d = sp.I*M/(1+M**2)
    cut = (cut*d).subs(x**-2, Q/M**2)
    gamma = sp.factor(cut[0, 0]-sp.trace(cut)/2)
    assert sp.simplify(gamma+d*Q*(Q**2-1)/(2*M**2)) == 0
    normal = sp.simplify((Q*sp.diff(gamma, Q)).subs(Q, -1))
    assert sp.simplify(normal-d/M**2) == 0
    assert normal.subs(M, 1) == sp.I/2
    frow = (1-Q)*(cut[0, 0]-cut[1, 1])
    assert sp.simplify(gamma-frow/(2*(1-Q))) == 0
    return {"N": 2, "actual_single_positive_crossing_unknot": True,
            "whole_cut": str(cut), "gamma_0": str(gamma),
            "logQ_normal_at_root": str(normal),
            "complete_normal_value": "I/2", "actual_F_Ward_source_exact": True}


def main():
    contraction = [contraction_case(N, root) for N in range(2, 9) for root in (True, False)]
    actual = []
    for N in range(2, 6):
        p, generator, _ = field(N)
        for M in (1, generator):
            for word in [[(0, 1)], [(0, 1)]*3, [(0, -1)]*3]:
                record = actual_case(N, 2, word, 1, 1, M)
                if record:
                    actual.append(record)
    for N in (2, 3, 4):
        for M in (1, field(N)[1]):
            record = actual_case(N, 3, [(0, 1), (1, -1), (0, 1), (1, -1)], 2, 2, M)
            if record:
                actual.append(record)
    auxiliary = [actual_case(N, 2, [(0, 1)]*3, 1, 1, 3, False) for N in (2, 3, 4)]
    assert any(not a['root_scalar'] for a in auxiliary if a)
    metric = [metric_case(N) for N in (2, 3, 4, 5, 8, 12, 24, 48, 96)]
    phases = [phase_case(pnum, d) for pnum, d in ((1, 3), (2, 5), (3, 7))]
    result = {"status": "PASS", "whole_contraction_cases": contraction,
              "actual_root_signed_braids_and_full_peripheral_source": actual,
              "actual_offroot_auxiliary_Ward_defects": auxiliary,
              "actual_characteristic_zero_normal_source_defect": actual_symbolic_normal_defect(),
              "numerical_metric_checks_of_proved_bound": metric,
              "marked_power_graphs": phases,
              "scope": "Exact root single-index source reduction, whole source Ward defect; no selected geometric-cycle or volume claim."}
    path = Path(__file__).with_name("actual_one_index_fourier_source_results.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "whole_contraction_cases": len(contraction),
                      "actual_root_cases": len(actual), "actual_offroot_cases": len(auxiliary),
                      "matrix_units": sum(a['matrix_units'] for a in contraction),
                      "results": str(path)}, indent=2))


if __name__ == '__main__':
    main()
