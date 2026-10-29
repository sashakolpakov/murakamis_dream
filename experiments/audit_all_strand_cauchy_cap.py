#!/usr/bin/env python3
"""Exact universal Euler/Cauchy cap after actual tail Borel fusion.

Checks arbitrary braid-index sources without replacing their physical
pivots, word, framing or complete modified dimension. No geometric
cycle selection or volume-growth assertion is made.
"""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import (
    alg_product, fusion, inv, physical_cap, right_regular,
)
from audit_actual_two_cut_ports import balanced_data, word_matrix


def tail_blocks(N, p, Q, xs):
    """Actual tail basis = normalized indecomposable Borel heads."""
    if len(xs) == 1:
        return np.eye(N, dtype=np.int64), list(xs)
    C, _, central, H, f, Ks, tails = fusion(N, p, Q, xs, [0]*len(xs))
    assert central == 0
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    columns, ys = [], []
    product = 1
    for x in xs:
        product = product*x % p
    for copy in range(len(tails)):
        for j in range(N):
            ys.append(product*pow(Q, -j, p) % p)
            for a in range(N):
                columns.append(C[:, copy*N*N+a*N+j]*pow(fac[a], -1, p) % p)
    S = np.column_stack(columns)
    Si = inv(S, p)
    K = H*product % p
    Fhead = np.zeros((N, N), dtype=np.int64)
    for a in range(1, N):
        Fhead[a, a-1] = (1-pow(Q, a, p)) % p
    expected_k = np.concatenate([[y*pow(Q, -a, p) % p for a in range(N)] for y in ys])
    assert np.array_equal(Si@K@S % p, np.diag(expected_k))
    assert np.array_equal(Si@f@S % p, np.kron(np.eye(len(ys), dtype=np.int64), Fhead))
    return S, ys


def audit(N, strands, word):
    p, eta, q, _, _, K, _, plus, minus = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    S, ys = tail_blocks(N, p, Q, [x]*(strands-1))
    T = np.kron(np.eye(N, dtype=np.int64), S)
    Ti = np.kron(np.eye(N, dtype=np.int64), inv(S, p))
    W = word_matrix(word, plus, minus, strands, N, p)
    transformed = Ti@W@T % p
    blocks = transformed.reshape(N, len(ys), N, N, len(ys), N)
    C, Ci, phi, _, _, _, _ = fusion(N, p, Q, [x, ys[0]], [0, 0])
    assert phi == 0
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    one, u, vi = (np.zeros(N*N, dtype=np.int64) for _ in range(3))
    one[:N] = 1
    for a in range(N):
        u[a*N:(a+1)*N] = pow(x, a, p)*pow(fac[a], -1, p) % p
        vi[a*N:(a+1)*N] = (pow(-1, a, p)*pow(Q, a*(a+3)//2, p)
                              *pow(x, a, p)*pow(fac[a], -1, p)) % p
    v0 = np.concatenate([vi[a*N:(a+1)*N]*pow(Q, -2*a, p) % p
                          for a in range(N)])
    exact, cauchy, nonzero, endpoint_source = 0, 0, 0, 0
    gamma0 = N*pow(x, strands*(1-N), p)*Q % p
    for t, y in enumerate(ys):
        block = blocks[:, t, :, :, t, :].reshape(N*N, N*N)
        relative = Ci@block@C % p
        a = relative@one % p
        assert np.array_equal(relative, right_regular(a, N, 0, p))
        Ks = [K, np.diag([y*pow(Q, -b, p) % p for b in range(N)]).astype(np.int64)]
        literal = physical_cap(block, Ks, N, p)
        gamma = N*pow(x*y % p, 1-N, p)*Q % p
        dressed = alg_product(alg_product(vi, a, N, 0, p), u, N, 0, p)
        value = gamma*int(dressed[(N-1)*N]) % p
        assert value == literal
        conjugated = alg_product(alg_product(v0, a, N, 0, p), u, N, 0, p)
        endpoint_difference = sum(int(conjugated[k*N])*pow(x, -k, p)
                                  *(1-pow(Q, -k, p)) for k in range(N)) % p
        endpoint_value = (gamma*pow(x, N-1, p)*pow(1-Q, -1, p)
                          *endpoint_difference) % p
        assert endpoint_value == literal
        endpoint_source = (endpoint_source+gamma*pow(gamma0, -1, p)
                            *endpoint_difference) % p
        exact = (exact+literal) % p
        cauchy = (cauchy+value) % p
        nonzero += int(bool(value))
    physical = physical_cap(W, [K]*strands, N, p)
    assert physical == exact == cauchy
    writhe = sum(1 if letter > 0 else -1 for letter in word)
    imag = pow(eta, N, p)
    external = pow(eta, -writhe*(N-1)*(N+1), p)*pow(imag, N+3, p)*pow(N, -1, p) % p
    assert external*physical % p == external*cauchy % p
    root_unit = pow(x, (strands-1)*(1-N), p)*Q % p
    assert physical == N*root_unit*pow(1-Q, -1, p)*endpoint_source % p
    return {"N": N, "strands": strands, "word": list(word), "field": p,
            "actual_tail_heads": len(ys), "nonzero_diagonal_cap_blocks": nonzero,
            "actual_weighted_endpoint_source": int(endpoint_source),
            "original_complete_period": external*physical % p,
            "original_half_Cartan_pivots_framing_and_d_N_retained": True}


def main():
    records = []
    for N, strands in [(2, 2), (3, 2), (4, 2), (2, 3), (3, 3), (4, 3), (5, 3), (2, 4), (3, 4)]:
        generator = tuple(range(1, strands))
        records.append(audit(N, strands, generator+generator+generator))
        records.append(audit(N, strands, tuple((1 if j % 2 else -1)*j for j in generator)*2))
    result = {"status": "PASS", "case_count": len(records),
              "diagonal_head_blocks": sum(r["actual_tail_heads"] for r in records),
              "scope": "Actual arbitrary-braid-index cap as universal right-Euler/Cauchy coefficients and exact two-point divided differences of their normal forms; no selected geometric-period or volume estimate.",
              "cases": records}
    Path(__file__).with_name("all_strand_cauchy_cap_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in ("status", "case_count", "diagonal_head_blocks")}, indent=2))


if __name__ == "__main__":
    main()
