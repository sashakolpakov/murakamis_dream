#!/usr/bin/env python3
"""Exact actual high-color four/two-word grid Ward contractions.

All scalar divisions are actual root units. Pairs keep the q-log
derivative of every integral Gaussian arrow and coherent source unit.
"""

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_divided_ward_closure import (
    actual_module, add, sub, mul, scale, eye, zero, const, eq,
)
from audit_high_color_first_normal_r_degree import root_field


def inverse_scalar(a, da, p):
    inv = pow(int(a), -1, p)
    return inv, -int(da)*inv*inv % p


def divide_value(a, da, b, db, p):
    inv, dinv = inverse_scalar(b, db, p)
    return int(a)*inv % p, (int(da)*inv+int(a)*dinv) % p


def comm(a, b, p):
    return sub(mul(a, b, p), mul(b, a, p), p)


def trace(a, p):
    return tuple(int(np.trace(x)) % p for x in a)


def source_value(a, c, p):
    return trace(mul(a, c, p), p)


def tree(N, r):
    edges = []
    D = N*(r+1)
    for R in range(r+1):
        for S in range(N-1):
            child = [R*N+U for U in range(S+1, N)]
            edges.append((2, R*N+S, R*N+S+1, child))
    for R in range(r):
        child = list(range((R+1)*N, D))
        edges.append((3, R*N, (R+1)*N, child))
    assert len(edges) == D-1
    return edges


def actual_words(N, r, q, p):
    m, E, F, K = actual_module(N, r, q, p)
    beta = np.array([(-1)**(N*R*(R-1)//2+R*S)
                     for R in range(r+1) for S in range(N)], dtype=np.int64)
    frame = beta[:, None]*beta[None, :]
    E = [tuple(X*frame % p for X in pair) for pair in E]
    F = [tuple(X*frame % p for X in pair) for pair in F]
    H = scale(comm(E[N], F[N], p), (-1)**(N*r-1), 0, p)
    return (K, H, F[1], F[N]), E, F


def valid_units(words, N, r, p):
    K, H, F, L = words
    D = N*(r+1)
    for i in range(D):
        for j in range(D):
            if i == j:
                continue
            selected = K if i % N != j % N else H
            if not (int(selected[0][i, i])-int(selected[0][j, j])) % p:
                return False
            # Optional two-word presentation uses its own simple spectrum.
            two = (2*int(H[0][i, i])+int(K[0][i, i])
                   -2*int(H[0][j, j])-int(K[0][j, j])) % p
            if not two:
                return False
    return all(words[t][0][v, u] for t, u, v, _ in tree(N, r))


def grid_h(X, words, N, r, p):
    D = N*(r+1)
    out = zero(D)
    K, H = words[:2]
    for i in range(D):
        for j in range(D):
            if i == j:
                continue
            index, generator = (0, K) if i % N != j % N else (1, H)
            value = divide_value(X[index][0][i, j], X[index][1][i, j],
                                 generator[0][i, i]-generator[0][j, j],
                                 generator[1][i, i]-generator[1][j, j], p)
            out[0][i, j], out[1][i, j] = value
    invD = pow(D, -1, p)
    for index, u, v, subtree in tree(N, r):
        value = divide_value(X[index][0][v, u], X[index][1][v, u],
                             words[index][0][v, u], words[index][1][v, u], p)
        weight = np.full(D, len(subtree)*invD % p, dtype=np.int64)
        weight[subtree] = (weight[subtree]-1) % p
        for k in range(2):
            out[k][np.diag_indices(D)] = (out[k].diagonal()+value[k]*weight) % p
    return out


def two_word_h(C, words, N, r, p):
    D = N*(r+1)
    A = add(words[1], scale(words[0], pow(2, -1, p), 0, p), p)
    B = add(words[2], words[3], p)
    X, Y = comm(A, C, p), comm(B, C, p)
    off = zero(D)
    for i in range(D):
        for j in range(D):
            if i != j:
                value = divide_value(X[0][i, j], X[1][i, j],
                                     A[0][i, i]-A[0][j, j], A[1][i, i]-A[1][j, j], p)
                off[0][i, j], off[1][i, j] = value
    Y = sub(Y, comm(B, off, p), p)
    # The diagonal tree operator only reads its last two arguments.
    diagonal = grid_h((zero(D), zero(D), Y, Y), words, N, r, p)
    return add(off, diagonal, p)


def actual_controlled_source(E, F, N, r, p):
    D = N*(r+1)
    f = F[N]
    e = scale(E[N], (-1)**(N*r-1), 0, p)
    expf, expe = eye(D), eye(D)
    powerf, powere = eye(D), eye(D)
    fac = 1
    for j in range(1, r+1):
        fac = fac*j % p
        powerf, powere = mul(powerf, f, p), mul(powere, e, p)
        expf = add(expf, scale(powerf, pow(fac, -1, p), 0, p), p)
        expe = add(expe, scale(powere, pow(fac, -1, p), 0, p), p)
    psi = tuple(X[:, 0].copy() for X in expf)
    lam = tuple(X[0, :]*pow(pow(2, r, p), -1, p) % p for X in expe)
    raw = (np.outer(psi[0], lam[0]) % p,
           (np.outer(psi[1], lam[0])+np.outer(psi[0], lam[1])) % p)
    unit, dunit = trace(raw, p)
    if not unit:
        return None, None
    inv, dinv = inverse_scalar(unit, dunit, p)
    normalized = scale(raw, inv, dinv, p)
    # Literal controlled head shift G on the actual high-color space.
    permutation = [(j//N)*N+(j % N+j//N) % N for j in range(D)]
    G = np.zeros((D, D), dtype=np.int64)
    for j, i in enumerate(permutation):
        G[i, j] = 1
    return mul(mul(const(G), normalized, p), const(G.T), p), (unit, dunit)


def exact_case(N, r, generic):
    p, eta = root_field(N)
    root = eta*eta % p
    if generic:
        generator = int(sp.primitive_root(p))
        for exponent in range(1, p-1):
            q = pow(generator, exponent, p)
            if q*q % p == 1:
                continue
            words, E, F = actual_words(N, r, q, p)
            if valid_units(words, N, r, p):
                source, unit = actual_controlled_source(E, F, N, r, p)
                if source is not None:
                    break
        else:
            raise AssertionError("No finite-field point in the actual whole unit chart")
    else:
        q = root
        words, E, F = actual_words(N, r, q, p)
        assert valid_units(words, N, r, p)
        source, unit = actual_controlled_source(E, F, N, r, p)
        assert unit[0] == 1
        selected_source, selected_row = np.zeros(N*(r+1), dtype=np.int64), np.zeros(N*(r+1), dtype=np.int64)
        for R in range(r+1):
            index = R*N+R % N
            selected_source[index] = 1
            selected_row[index] = math.comb(r, R)*pow(pow(2, r, p), -1, p) % p
        assert np.array_equal(source[0], np.outer(selected_source, selected_row) % p)
    D = N*(r+1)
    C = (np.array([[(2*i+3*j+i*j+7) % p for j in range(D)] for i in range(D)], dtype=np.int64),
         np.array([[(5*i+11*j+2*i*j+1) % p for j in range(D)] for i in range(D)], dtype=np.int64))
    dC = tuple(comm(A, C, p) for A in words)
    mean = tuple(int(np.trace(a))*pow(D, -1, p) % p for a in C)
    expected = sub(C, scale(eye(D), mean[0], mean[1], p), p)
    reconstructed = grid_h(dC, words, N, r, p)
    eq(reconstructed, expected)
    assert trace(reconstructed, p) == (0, 0)
    for a, b in zip(dC, (comm(A, reconstructed, p) for A in words)):
        eq(a, b)
    # Strong projection identity on an arbitrary unrestricted four-row input.
    X = tuple(scale(C, t+2, t+1, p) for t in range(4))
    hX = grid_h(X, words, N, r, p)
    projection = tuple(comm(A, hX, p) for A in words)
    eq(grid_h(projection, words, N, r, p), hX)
    eq(two_word_h(C, words, N, r, p), expected)
    # Actual whole source, including its normalization derivative.
    assert trace(source, p) == (1, 0)
    lhs = tuple((x-y) % p for x, y in zip(source_value(source, C, p), mean))
    assert lhs == source_value(source, reconstructed, p)
    return {"N": N, "r": r, "generic_q": generic, "dimension": D,
            "actual_q_point": q, "prime": p,
            "whole_four_row_grid_contraction_and_first_normal_exact": True,
            "actual_image_projection_and_two_word_contraction_exact": True,
            "actual_controlled_coherent_source_unit": list(unit),
            "whole_original_source_homotopy_exact": True}


def root_metric_case(N):
    r, D = N, N*(N+1)
    root = np.exp(2j*np.pi/N)
    gap = max(1/abs(root**(-S)-root**(-U))
              for S in range(N) for U in range(N) if S != U)
    assert abs(gap-1/(2*np.sin(np.pi/N))) < 1e-10
    incidence = np.zeros((D, D-1))
    for j, (kind, u, v, subtree) in enumerate(tree(N, r)):
        if kind == 2:
            S = u % N
            weight = np.sin(np.pi*(S+1)/N)/np.sin(np.pi/N)
        else:
            R = u//N
            weight = np.sqrt((R+1)*(r-R))
        incidence[:, j] = len(subtree)/D
        incidence[subtree, j] -= 1
        incidence[:, j] /= weight
    actual_tree_norm = np.linalg.svd(incidence, compute_uv=False)[0]
    bound = np.sqrt(D*(r+N-1)/2)
    assert actual_tree_norm <= bound*(1+1e-12)
    # The literal correlated coupon is orthogonal in the actual hybrid metric.
    psi, lam = np.zeros(D), np.zeros(D)
    metric = np.array([math.comb(r, R) for R in range(r+1) for S in range(N)], dtype=float)
    for R in range(r+1):
        index = R*N+R % N
        psi[index], lam[index] = 1, math.comb(r, R)/2**r
    A = np.outer(psi, lam)
    transformed = np.sqrt(metric)[:, None]*A/np.sqrt(metric)[None, :]
    assert abs(np.linalg.norm(transformed)-1) < 1e-12
    assert np.linalg.norm(transformed-transformed.T) < 1e-12
    assert np.linalg.norm(transformed@transformed-transformed) < 1e-12
    return {"N": N, "dimension": D, "tree_operator_norm": float(actual_tree_norm),
            "polynomial_root_bound": float(bound), "original_correlated_source_norm": 1,
            "root_hybrid_bound_exact_formula_checked": True}


def main():
    exact = [exact_case(N, r, generic) for N, r in ((2, 1), (2, 2), (3, 3), (4, 4), (5, 5))
             for generic in (False, True)]
    metrics = [root_metric_case(N) for N in range(2, 13)]
    target = Path(__file__).with_name("whole_high_color_ward_grid_results.json")
    target.write_text(json.dumps({"status": "pass", "actual_whole_grid_cases": exact,
                                  "root_hybrid_source_bounds": metrics,
                                  "scope": "Actual finite Ward/source contraction; no Gaussian comparison or low/high normal-jet equality."}, indent=2)+"\n")
    print(json.dumps({"status": "pass", "actual_whole_grid_cases": len(exact),
                      "root_metric_source_cases": len(metrics), "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
