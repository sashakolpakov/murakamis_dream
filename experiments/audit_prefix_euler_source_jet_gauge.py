#!/usr/bin/env python3
"""Exact pointed prefix transport to Euler words at fixed normal depth.

The independent jet parameter is Q+1 at N=2, with x fixed. This
is a valid local root-normal coordinate. The proof is all N and
all admissible parameter paths; these checks retain the actual
generic-Q matrices, pivots and non-weight-preserving coupons.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp


P = 1009


def constant(A, J):
    out = np.zeros((J+1, len(A), len(A)), dtype=np.int64)
    out[0] = A
    return out % P


def mul(A, B):
    out = np.zeros_like(A)
    for k in range(len(A)):
        for i in range(k+1):
            out[k] = (out[k]+A[i]@B[k-i]) % P
    return out


def inverse(A):
    out = np.zeros_like(A)
    out[0] = np.array(sp.Matrix(A[0].tolist()).inv_mod(P)).astype(np.int64)
    for k in range(1, len(A)):
        subtotal = sum((A[i]@out[k-i] % P for i in range(1, k+1)), np.zeros_like(A[0])) % P
        out[k] = -out[0]@subtotal % P
    return out


def kron(A, B):
    out = np.zeros((len(A), len(A[0])*len(B[0]), len(A[0])*len(B[0])), dtype=np.int64)
    for k in range(len(A)):
        for i in range(k+1):
            out[k] = (out[k]+np.kron(A[i], B[k-i])) % P
    return out


def embed(A, slot, strands, J):
    left = constant(np.eye(2**slot, dtype=np.int64), J)
    right = constant(np.eye(2**(strands-slot-2), dtype=np.int64), J)
    return kron(kron(left, A), right)


def source(A, D):
    product = mul(D, A)
    return [int(np.trace(coefficient)) % P for coefficient in product]


def case(strands, word, J, x):
    xi = pow(x, -1, P)
    original = np.array([[1, 0, 0, 0], [0, 0, xi, 0],
                         [0, xi, 1-xi*xi, 0], [0, 0, 0, -xi*xi]], dtype=np.int64) % P
    actual = constant(original, J)
    if J:
        actual[1, 3, 3] = xi*xi % P
    completed = constant(original, J)
    completed[0, 3, 0] = -pow(xi, 3, P) % P
    actual_inverse, completed_inverse = inverse(actual), inverse(completed)
    I = constant(np.eye(2**strands, dtype=np.int64), J)
    source_first = constant(np.array([[1, 1], [0, 0]], dtype=np.int64), J)
    pivot = constant(np.diag([xi, -xi]).astype(np.int64), J)
    if J:
        pivot[1, 1, 1] = xi
    D = source_first
    for _ in range(strands-1):
        D = kron(D, pivot)
    prefixes, completed_prefixes, gauges, gauge_inverses = [I.copy()], [I.copy()], [I.copy()], [I.copy()]
    actual_word, completed_word, actual_word_inverse = I.copy(), I.copy(), I.copy()
    L, nilpotence_checks = strands+J, 0
    for letter in word:
        A = embed(actual if letter > 0 else actual_inverse, abs(letter)-1, strands, J)
        Ai = embed(actual_inverse if letter > 0 else actual, abs(letter)-1, strands, J)
        E = embed(completed if letter > 0 else completed_inverse, abs(letter)-1, strands, J)
        actual_word = mul(A, actual_word)
        actual_word_inverse = mul(actual_word_inverse, Ai)
        completed_word = mul(E, completed_word)
        G = mul(completed_word, actual_word_inverse)
        H = (G-I) % P
        term, geometric_inverse = I.copy(), I.copy()
        for degree in range(1, L):
            term = mul(term, H)
            geometric_inverse = (geometric_inverse+(-1)**degree*term) % P
        assert not np.any(mul(term, H))
        assert np.array_equal(mul(G, geometric_inverse), I)
        assert np.array_equal(E, mul(mul(G, A), gauge_inverses[-1]))
        prefixes.append(actual_word.copy())
        completed_prefixes.append(completed_word.copy())
        gauges.append(G)
        gauge_inverses.append(geometric_inverse)
        nilpotence_checks += 1
    D_euler = mul(D, gauge_inverses[-1])
    assert source(actual_word, D) == source(completed_word, D_euler)
    bare_word_mismatch = source(actual_word, D) != source(completed_word, D)

    coupon_checks, exposed_bare_coupons = 0, 0
    for level in sorted(set((0, len(word)//2, len(word)))):
        for slot in range(strands):
            X0 = np.array([[0, 1], [0, 0]], dtype=np.int64)
            X = constant(np.kron(np.kron(np.eye(2**slot, dtype=np.int64), X0),
                                  np.eye(2**(strands-slot-1), dtype=np.int64)), J)
            X_euler = mul(mul(gauges[level], X), gauge_inverses[level])
            A, E, bare = I.copy(), I.copy(), I.copy()
            if level == 0:
                A, E, bare = X.copy(), X_euler.copy(), X.copy()
            for k, letter in enumerate(word, 1):
                RA = embed(actual if letter > 0 else actual_inverse, abs(letter)-1, strands, J)
                RE = embed(completed if letter > 0 else completed_inverse, abs(letter)-1, strands, J)
                A, E, bare = mul(RA, A), mul(RE, E), mul(RE, bare)
                if k == level:
                    A, E, bare = mul(X, A), mul(X_euler, E), mul(X, bare)
            assert np.array_equal(E, mul(gauges[-1], A))
            assert source(A, D) == source(E, D_euler)
            exposed_bare_coupons += int(source(A, D) != source(bare, D))
            coupon_checks += 1
    # A negative-weight matrix coupon does not belong to the carry algebra;
    # its full conjugation is nevertheless finite at the proved depth.
    H = (gauges[-1]-I) % P
    logarithm, power = np.zeros_like(H), I.copy()
    for k in range(1, L):
        power = mul(power, H)
        logarithm = (logarithm+(-1)**(k+1)*pow(k, -1, P)*power) % P
    X = constant(np.eye(2**strands, dtype=np.int64)[::-1].copy(), J)
    for _ in range(2*L-1):
        X = (mul(logarithm, X)-mul(X, logarithm)) % P
    assert not np.any(X)
    return {"N": 2, "strands": strands, "word": list(word), "J": J, "x": x,
            "uniform_nilpotence_bound": L, "prefix_checks": nilpotence_checks,
            "coupon_source_checks": coupon_checks, "exposed_bare_coupons": exposed_bare_coupons,
            "bare_normal_source_mismatch": bare_word_mismatch,
            "all_transported_source_jets_equal": True}


def main():
    words = [(2, (1,)), (2, (-1,)), (3, (1, -2, 1, -2)), (4, (1, -2, 1, -2, 3))]
    q0 = pow(int(sp.primitive_root(P)), (P-1)//4, P)
    rows = [case(b, word, J, x) for b, word in words for J in (0, 1, 2) for x in (3, q0)]
    assert any(r["bare_normal_source_mismatch"] for r in rows)
    assert any(r["exposed_bare_coupons"] for r in rows)
    result = {"status": "PASS", "cases": rows,
              "scope": "Whole actual/Euler prefix gauge and original-source jet transport; arbitrary coupons require their proved conjugation and transported co-source. No geometric survival or norm estimate."}
    Path(__file__).with_name("prefix_euler_source_jet_gauge_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "cases": len(rows),
                      "prefix_checks": sum(r["prefix_checks"] for r in rows),
                      "coupon_source_jet_checks": sum(r["coupon_source_checks"] for r in rows),
                      "exposed_bare_coupon_cases": sum(r["exposed_bare_coupons"] for r in rows),
                      "bare_normal_mismatches": sum(r["bare_normal_source_mismatch"] for r in rows)}))


if __name__ == "__main__":
    main()
