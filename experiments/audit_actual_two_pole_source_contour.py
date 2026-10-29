#!/usr/bin/env python3
"""Exact actual-word endpoint pairs and the two-pole source contour.

The endpoint polynomial is built from the original matrices, tail fusion
and Euler conjugation. Tests do not assume a geometric-cycle comparison.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_all_strand_cauchy_cap import tail_blocks
from audit_actual_borel_regular_fusion import alg_product, fusion, inv, physical_cap
from audit_actual_two_cut_ports import balanced_data, word_matrix


def actual_polynomial(N, strands, word):
    p, _, q, _, _, K, _, plus, minus = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    tail, ys = tail_blocks(N, p, Q, [x]*(strands-1))
    frame = np.kron(np.eye(N, dtype=np.int64), tail)
    frame_i = np.kron(np.eye(N, dtype=np.int64), inv(tail, p))
    W = word_matrix(word, plus, minus, strands, N, p)
    blocks = (frame_i@W@frame % p).reshape(N, len(ys), N, N, len(ys), N)
    C, Ci, _, _, _, _, _ = fusion(N, p, Q, [x, ys[0]], [0, 0])
    fac = [1]
    for k in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, k, p)) % p)
    one, u, v = (np.zeros(N*N, dtype=np.int64) for _ in range(3))
    one[:N] = u[:N] = v[:N] = 1
    for k in range(1, N):
        u[k*N:(k+1)*N] = pow(x, k, p)*pow(fac[k], -1, p) % p
        v[k*N:(k+1)*N] = (pow(-1, k, p)*pow(Q, k*(k-1)//2, p)
                             *pow(x, k, p)*pow(fac[k], -1, p)) % p
    coefficients = [0]*N
    gamma0 = N*pow(x, strands*(1-N), p)*Q % p
    for index, y in enumerate(ys):
        block = blocks[:, index, :, :, index, :].reshape(N*N, N*N)
        a = Ci@block@C % p@one % p
        b = alg_product(alg_product(v, a, N, 0, p), u, N, 0, p)
        gamma = N*pow(x*y % p, 1-N, p)*Q % p
        weight = gamma*pow(gamma0, -1, p) % p
        for k in range(N):
            coefficients[k] = (coefficients[k]+weight*int(b[k*N])*pow(x, -k, p)) % p
    first = sum(coefficients) % p
    second = sum(c*pow(Q, -k, p) for k, c in enumerate(coefficients)) % p
    contour = sum(c*(1-pow(Q, -k, p))*pow(1-Q, -1, p)
                  for k, c in enumerate(coefficients)) % p
    assert contour == (first-second)*pow(1-Q, -1, p) % p
    physical = physical_cap(W, [K]*strands, N, p)
    assert physical == N*pow(x, (strands-1)*(1-N), p)*Q*contour % p
    # Naively merging Q=1 first makes the source of the constant one N.
    constant_actual = (1-pow(Q, N, p))*pow(1-Q, -1, p) % p
    assert constant_actual == 0 and N % p != 0
    return {"N": N, "strands": strands, "word": list(word), "field": p, "Q": Q,
            "normal_form_polynomial": coefficients, "endpoint_pair": [first, second],
            "endpoint_difference": (first-second) % p,
            "exact_contour_period": int(contour), "original_physical_cap": int(physical)}


def characteristic_zero_conjugacy():
    I = sp.I
    eta = (1+I)/sp.sqrt(2)
    R = sp.Matrix([[eta, 0, 0, 0], [0, 0, 1/eta, 0],
                   [0, 1/eta, 2*I/eta, 0], [0, 0, 0, eta]])
    F, K = sp.Matrix([[0, 0], [2, 0]]), sp.diag(I, -I)
    total = sp.kronecker_product(F, sp.eye(2))+sp.kronecker_product(K.inv(), F)
    seeds = [sp.eye(4)[:, 0], sp.eye(4)[:, 1]]
    C = sp.Matrix.hstack(seeds[0], seeds[1], total*seeds[0], total*seeds[1])
    tail = sp.Matrix.hstack(seeds[0], total*seeds[0]/2, seeds[1], total*seeds[1]/2)
    full = sp.kronecker_product(sp.eye(2), tail)
    fac = [sp.Integer(1), sp.Integer(2)]
    one, u, v = sp.Matrix([1, 1, 0, 0]), sp.Matrix([1, 1, I/2, I/2]), sp.Matrix([1, 1, -I/2, -I/2])

    def multiply(a, b):
        out = sp.zeros(4, 1)
        for degree in range(2):
            for j in range(2):
                for other in range(2-degree):
                    k = (j-other) % 2
                    out[(degree+other)*2+k] += a[degree*2+j]*b[other*2+k]
        return out

    def polynomial(word):
        W = sp.eye(8)
        for letter in word:
            local = R if letter > 0 else R.inv()
            op = sp.kronecker_product(local, sp.eye(2)) if abs(letter) == 1 else sp.kronecker_product(sp.eye(2), local)
            W = op*W
        transformed = (full.inv()*W*full).applyfunc(sp.simplify)
        coeff = sp.zeros(2, 1)
        for head in range(2):
            inds = [a*4+head*2+b for a in range(2) for b in range(2)]
            block = transformed.extract(inds, inds)
            a = (C.inv()*block*C*one).applyfunc(sp.simplify)
            b = multiply(multiply(v, a), u)
            coeff[0] += (-1)**head*b[0]
            coeff[1] += (-1)**head*b[2]/I
        return coeff.applyfunc(sp.simplify)

    original = polynomial((1, -2, 1, -2))
    conjugate = polynomial((1, 1, -2, 1, -2, -1))
    assert original == sp.Matrix([-1, sp.Rational(5, 2)])
    assert conjugate == sp.Matrix([2, sp.Rational(5, 2)])
    return {"original_normal_form": "-1+(5/2)Z", "conjugate_normal_form": "2+(5/2)Z",
            "original_endpoint_pair": ["3/2", "-7/2"],
            "conjugate_endpoint_pair": ["9/2", "-1/2"], "same_difference": "5"}


def main():
    cases = []
    for N in range(2, 7):
        for strands, word in ((2, (1,)), (2, (1, 1, 1)), (3, (1, -2, 1, -2))):
            cases.append(actual_polynomial(N, strands, word))
    witness = []
    for N in (2, 3, 4):
        original = actual_polynomial(N, 3, (1, -2, 1, -2))
        conjugate = actual_polynomial(N, 3, (1, 1, -2, 1, -2, -1))
        assert original["endpoint_difference"] == conjugate["endpoint_difference"]
        assert original["original_physical_cap"] == conjugate["original_physical_cap"]
        if original["endpoint_pair"] != conjugate["endpoint_pair"]:
            witness.append({"N": N, "field": original["field"],
                            "original_pair": original["endpoint_pair"],
                            "conjugate_pair": conjugate["endpoint_pair"],
                            "same_difference": original["endpoint_difference"]})
    assert witness
    characteristic_zero = characteristic_zero_conjugacy()
    result = {"status": "PASS", "actual_word_cases": cases,
              "conjugate_endpoint_noninvariance": witness,
              "characteristic_zero_conjugacy": characteristic_zero,
              "scope": "Original two-pole coefficient source and endpoint-pair transport; no geometric cycle or volume claim."}
    Path(__file__).with_name("actual_two_pole_source_contour_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "actual_word_cases": len(cases),
                      "conjugacy_witness": witness[0],
                      "characteristic_zero": characteristic_zero}, indent=2))


if __name__ == "__main__":
    main()
