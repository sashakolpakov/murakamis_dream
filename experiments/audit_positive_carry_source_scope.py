#!/usr/bin/env python3
"""Independent source-scope audit of the positive-N crossing completion.

Tests the full root meridian family and the full first-cut matrix,
then exhibits a local E coupon which detects a completion error.
This is not a moving-q or geometric-period comparison.
"""

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_borel_regular_fusion import fusion, right_regular
from audit_actual_two_cut_ports import partial, word_matrix
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices


def inverse(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p)).astype(np.int64)


def crossing(N, M):
    p, _, q = field(N)
    Q, M = q*q % p, M % p
    x = -M*pow(q, -1, p) % p
    plus, minus, pivot, theta = color_matrices(N, p, q, x)
    factorial = [1]
    for a in range(1, N):
        factorial.append(factorial[-1]*(1-pow(Q, a, p)) % p)
    diagonal = np.array([factorial[a]*factorial[b] % p
                         for a in range(N) for b in range(N)], dtype=np.int64)
    diagonali = np.array([pow(int(a), -1, p) for a in diagonal], dtype=np.int64)
    plus = plus*diagonal[:, None]*diagonali[None, :] % p
    minus = minus*diagonal[:, None]*diagonali[None, :] % p
    C, Ci, _, _, _, _, _ = fusion(N, p, Q, [x, x], [0, 0])
    completed_coefficient = np.zeros(N*N, dtype=np.int64)
    nonwrapped = np.zeros_like(completed_coefficient)
    for a, k in itertools.product(range(N), repeat=2):
        coefficient = (pow(-1, k, p)*pow(x, -a-2*k, p)
                       *pow(Q, k*(k-1)//2, p)*pow(factorial[a], -1, p)) % p
        completed_coefficient[a*N+k] = coefficient
        if a+k < N:
            nonwrapped[a*N+k] = coefficient
    assert np.array_equal(C@right_regular(nonwrapped, N, 0, p)@Ci % p, plus)
    complete = C@right_regular(completed_coefficient, N, 0, p)@Ci % p
    complete_inverse = inverse(complete, p)
    degree = np.array([a+b for a in range(N) for b in range(N)])
    error = (complete-plus) % p
    support = np.argwhere(error)
    assert len(support)
    assert all(degree[row]-degree[column] == N for row, column in support)
    inverse_error = (complete_inverse-minus) % p
    assert all(degree[row]-degree[column] == N for row, column in np.argwhere(inverse_error))
    assert not np.any(error@error % p)
    pivot = np.diag(pivot).copy()
    assert not np.any(partial(error, pivot, 2, N, p))
    assert not np.any(partial(inverse_error, pivot, 2, N, p))
    return p, q, Q, x, plus, minus, complete, complete_inverse, pivot, theta


def word_case(N, strands, M, word):
    p, q, Q, x, plus, minus, complete, complete_inverse, pivot, theta = crossing(N, M)
    W = word_matrix(word, plus, minus, strands, N, p)
    Wc = word_matrix(word, complete, complete_inverse, strands, N, p)
    degree = np.array([sum(a) for a in itertools.product(range(N), repeat=strands)])
    error = (Wc-W) % p
    for row, column in np.argwhere(error):
        difference = degree[row]-degree[column]
        assert difference >= N and difference % N == 0
    ordinary_cut, completed_cut = partial(W, pivot, strands, N, p), partial(Wc, pivot, strands, N, p)
    assert np.array_equal(ordinary_cut, completed_cut)
    # Retain the original framing line and dimension whenever regular.
    eta = pow(-1, N+1, p)*pow(q, N*(1-N)//2, p) % p
    norm = sum(pow(M, 2*j, p) for j in range(N)) % p
    d = eta*pow(M, N-1, p)*pow(norm, -1, p) % p if norm else None
    external = pow(theta, -sum(1 if a > 0 else -1 for a in word), p)
    if d is not None:
        external = external*d % p
    assert np.array_equal(external*ordinary_cut % p, external*completed_cut % p)
    return {"N": N, "strands": strands, "M": M, "word": list(word),
            "field": p, "full_cut_matrix_preserved": True,
            "original_full_d_N_when_regular": d,
            "nonzero_completion_error_entries": int(np.count_nonzero(error))}


def coupon_witness():
    N, M = 2, 1
    p, _, Q, x, plus, _, complete, _, pivot, _ = crossing(N, M)
    Ecal = np.zeros((N, N), dtype=np.int64)
    Ecal[0, 1] = (pow(Q, -1, p)-1) % p
    error = (complete-plus) % p
    inserted = np.kron(np.eye(N, dtype=np.int64), Ecal)@error % p
    cut = partial(inserted, pivot, 2, N, p)
    value = int(cut[:, 0].sum()) % p
    assert value != 0
    # Normalized positive crossing has error=-i |11><00|.
    assert int(error[3, 0]) == pow(x, -1, p)
    assert value == -2*pow(x, -2, p) % p == 2
    return {"N": N, "field": p, "local_closed_wire_Ecal_detects_error": value,
            "uninserted_cut_is_zero": True,
            "scope": "Local coupons of degree -1 are outside the nonnegative N-graded source quotient."}


def moving_Q_counterexample():
    Q, x = sp.symbols('Q x', nonzero=True)
    C = sp.Matrix([[1, 0, 0, 0], [0, 1, (1-Q)/x, 0],
                   [0, 0, 1-Q, 0], [0, 0, 0, 1-Q]])
    relative = sp.Matrix([[1, 0, 0, 0], [0, -x**-2, 0, 0],
                          [0, x**-1/(1-Q), 1, 0],
                          [-x**-3/(1-Q), 0, 0, -x**-2]])
    euler = (C*relative*C.inv()).applyfunc(sp.simplify)
    actual = sp.Matrix([[1, 0, 0, 0], [0, 0, x**-1, 0],
                        [0, x**-1, 1-x**-2, 0], [0, 0, 0, Q*x**-2]])
    expected = sp.zeros(4)
    expected[3, 0], expected[3, 3] = -x**-3, -(Q+1)*x**-2
    assert (euler-actual-expected).applyfunc(sp.simplify) == sp.zeros(4)
    cut = sp.zeros(2)
    for c, a, b in itertools.product(range(2), repeat=3):
        cut[c, a] += (x**-1 if b == 0 else Q/x)*expected[2*c+b, 2*a+b]
    assert sp.simplify(cut[1, 1]+Q*(Q+1)/x**3) == 0
    source = sp.simplify(sum(cut)/2)
    normal = sp.simplify((Q*sp.diff(source, Q)).subs(Q, -1))
    assert sp.simplify(normal+1/(2*x**3)) == 0
    repair = sp.zeros(4)
    repair[3, 3] = (Q+1)*x**-2
    repaired = euler+repair
    assert (repaired-actual).applyfunc(sp.simplify)[3, 3] == 0
    return {"N": 2, "generic_Euler_minus_actual": "-x^-3 E_(11,00) -(Q+1)x^-2 E_(11,11)",
            "full_cut_difference": "-Q(Q+1)x^-3 E_(1,1)",
            "averaged_source_first_Q_normal": str(normal),
            "explicit_retained_normal_repair": "+(Q+1)x^-2 E_(11,11)"}


def main():
    cases = []
    for N in range(2, 6):
        for M in (1, 3):
            cases.append(word_case(N, 2, M, (1, -1, 1)))
            cases.append(word_case(N, 3, M, (1, -2, 1, -2)))
            cases.append(word_case(N, 3, M, (1, 1, 1, 2)))
    for M in (1, 3):
        cases.append(word_case(2, 4, M, (1, -2, 3, -1, 2)))
    result = {"status": "PASS", "word_cases": cases,
              "local_coupon_witness": coupon_witness(),
              "moving_Q_counterexample_and_repair": moving_Q_counterexample(),
              "scope": "Root-family positive-N completion: full uninserted cut, inverse and local-coupon limitation. No moving-q or geometric-source assertion."}
    Path(__file__).with_name("positive_carry_source_scope_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "word_cases": len(cases),
                      "local_coupon_witness": result["local_coupon_witness"],
                      "moving_Q_counterexample_and_repair": result["moving_Q_counterexample_and_repair"]}, indent=2))


if __name__ == "__main__":
    main()
