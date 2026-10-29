#!/usr/bin/env python3
"""Exact resonant moment Jacobian, cyclic quotient and source transversality."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

from audit_high_color_first_normal_r_degree import root_field


def rank(A, p):
    A = np.array(A, dtype=np.int64) % p
    row = 0
    for col in range(A.shape[1]):
        candidates = np.flatnonzero(A[row:, col])
        if not len(candidates):
            continue
        pivot = row+int(candidates[0])
        A[[row, pivot], :] = A[[pivot, row], :]
        A[row, :] = A[row, :]*pow(int(A[row, col]), -1, p) % p
        if row+1 < len(A):
            A[row+1:, :] = (A[row+1:, :]-A[row+1:, col:col+1]*A[row:row+1, :]) % p
        row += 1
        if row == min(A.shape):
            break
    return row


def product_dual(A, B, p):
    return A[0]@B[0] % p, (A[1]@B[0]+A[0]@B[1]) % p


def inverse_dual(A, inverse, p):
    return inverse, -inverse@A[1]@inverse % p


def case(N):
    p, eta = root_field(N)
    Q = pow(eta, 4, p)
    B = np.diag([pow(Q, j, p) for j in range(N)]).astype(np.int64)
    Binv = np.diag([pow(Q, -j, p) for j in range(N)]).astype(np.int64)
    P = np.zeros((N, N), dtype=np.int64)
    for j in range(N):
        P[(j+1) % N, j] = 1
    I, zero = np.eye(N, dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    v, w0 = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
    v[0], w0[0] = 1, 1
    e = np.outer(v, w0)
    assert np.array_equal(B@P % p, Q*P@B % p)

    def jac(a, b, dw, epsilon=0):
        return (a-P@a@P.T+B@b@Binv-b-np.outer(v, dw)-epsilon*I) % p

    def right_inverse(H):
        trace = int(np.trace(H)) % p
        T = (H-trace*e) % p
        diagonal, partial = [0], 0
        for i in range(1, N):
            partial = (partial+int(T[i, i])) % p
            diagonal.append(partial)
        a = np.diag(diagonal).astype(np.int64)
        b = zero.copy()
        for i, j in itertools.product(range(N), repeat=2):
            if i != j:
                b[i, j] = int(T[i, j])*pow((pow(Q, i-j, p)-1) % p, -1, p) % p
        return a, b, -trace*w0 % p

    # Every target matrix unit exercises the actual trace and off-diagonal inverses.
    units = 0
    for i, j in itertools.product(range(N), repeat=2):
        H = zero.copy()
        H[i, j] = 1
        a, b, dw = right_inverse(H)
        assert np.array_equal(jac(a, b, dw), H)
        units += 1
    # Independent dual-number differentiation of the actual nonlinear equation.
    a = np.array([[(i*j+2*i+3*j+1) % p for j in range(N)] for i in range(N)], dtype=np.int64)
    b = np.array([[(3*i*j+i+7*j+2) % p for j in range(N)] for i in range(N)], dtype=np.int64)
    dw = np.array([(j*j+5*j+3) % p for j in range(N)], dtype=np.int64)
    epsilon = 3
    X, Y = (B, a@B % p), (P, b@P % p)
    commutator = product_dual(product_dual(product_dual(X, Y, p), inverse_dual(X, Binv, p), p),
                              inverse_dual(Y, P.T, p), p)
    derivative = (pow(Q, -1, p)*(commutator[1]-epsilon*commutator[0])-np.outer(v, dw)) % p
    assert np.array_equal(derivative, jac(a, b, dw, epsilon))
    # The genuine whole quantum-normal tangent, including moment-row derivative.
    Jhead = np.diag(np.arange(N)).astype(np.int64)
    assert not np.any(jac(Jhead, zero, -N*w0 % p, 1))

    # Companion-slice tangent coordinates: delta X, last column delta Y, delta w.
    columns = []
    for i, j in itertools.product(range(N), repeat=2):
        dX = zero.copy()
        dX[i, j] = 1
        columns.append(jac(dX@Binv % p, zero, np.zeros(N, dtype=np.int64)).reshape(-1))
    for i in range(N):
        dY = zero.copy()
        dY[i, N-1] = 1
        columns.append(jac(zero, dY@P.T % p, np.zeros(N, dtype=np.int64)).reshape(-1))
    for j in range(N):
        row = np.zeros(N, dtype=np.int64)
        row[j] = 1
        columns.append(jac(zero, zero, row).reshape(-1))
    matrix = np.column_stack(columns)
    assert rank(matrix, p) == N*N
    dimension = N*N+2*N
    source_X = np.zeros((N, dimension), dtype=np.int64)
    for i in range(N):
        source_X[i, i*N] = 1
    source_Y = np.zeros((N, dimension), dtype=np.int64)
    for i in range(N):
        source_Y[i, N*N+i] = 1
    full_source = np.vstack([matrix, source_X, source_Y])
    assert full_source.shape == (dimension, dimension)
    assert rank(full_source, p) == dimension
    natural_source = np.vstack([matrix, source_X, np.sum(source_Y, axis=0, keepdims=True)])
    assert rank(natural_source, p) == N*N+N+1

    # Stabilizer/common-commutant claim checked from independent matrix entries.
    commutant_columns = []
    for i, j in itertools.product(range(N), repeat=2):
        A = zero.copy()
        A[i, j] = 1
        commutant_columns.append(np.r_[(A@B-B@A).reshape(-1), (A@P-P@A).reshape(-1)] % p)
    assert rank(np.column_stack(commutant_columns), p) == N*N-1
    # A scalar infinitesimal stabilizer is killed by its nonzero marked vector.
    assert np.any(I@v)
    return {"N": N, "prime": p, "all_matrix_target_right_inverse_cases": units,
            "independent_nonlinear_dual_derivative": True,
            "actual_Q_normal_tangent_with_dw_minus_N": True,
            "cyclic_quotient_relative_dimension": 2*N,
            "actual_source_constraints_transverse": True,
            "natural_highest_Whittaker_locus_relative_dimension": N-1,
            "common_commutant_dimension": 1, "vector_pointing_kills_stabilizer": True}


def main():
    cases = [case(N) for N in range(2, 10)]
    result = {"status": "pass", "cases": cases,
              "scope": "Actual resonant framed moment scheme and source-section smoothness; no global word period, geometric endpoint comparison or volume claim."}
    output = Path(__file__).with_name("actual_resonant_moment_smoothness_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "primitive_root_levels": len(cases),
                      "exact_target_matrix_right_inverses": sum(item["all_matrix_target_right_inverse_cases"] for item in cases),
                      "companion_quotient_and_source_Jacobians": len(cases),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
