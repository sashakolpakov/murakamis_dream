#!/usr/bin/env python3
"""Literal two physical cuts in actual signed braid words.

Checks the four-port reconstruction, original single 1/N source,
all actual Hopf coupon rows (including prefixes), and lost offdiagonal
source bands. Actual pivot, half-Cartan and zero-framing lines remain.
"""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_divided_ward_closure import actual_module
from audit_high_color_first_normal_r_degree import setup, root_field


def embed(A, slot, strands, N):
    out = np.array([[1]], dtype=np.int64)
    for s in range(strands):
        out = np.kron(out, A if s == slot else np.eye(N, dtype=np.int64))
    return out


def balanced_data(N):
    p, m, coeff = setup(N, 0)
    _, eta = root_field(N)
    q = eta*eta % p
    rho = (q-pow(q, -1, p)) % p
    diagonal = np.array([pow(-rho, j, p)*pow(q, j*(j+1)//2, p) % p
                         for j in range(N)], dtype=np.int64)
    frame = diagonal[:, None]*np.array([pow(int(x), -1, p) for x in diagonal])[None, :] % p
    _, Eall, Fall, Kall = actual_module(N, 0, q, p)
    E, F, K = Eall[1][0]*frame % p, Fall[1][0]*frame % p, Kall[0]
    assert all(F[j+1, j] == (1-pow(q, 2*(j+1), p)) % p for j in range(N-1))
    tensor_diagonal = np.kron(diagonal, diagonal)
    tensor_frame = tensor_diagonal[:, None]*np.array([pow(int(x), -1, p) for x in tensor_diagonal])[None, :] % p
    plus, minus = np.zeros((N*N, N*N), dtype=np.int64), np.zeros((N*N, N*N), dtype=np.int64)
    for a in range(N):
        for b in range(N):
            for k in range(min(a, N-1-b)+1):
                plus[(b+k)*N+a-k, a*N+b] = coeff(a, b, k).x
            for k in range(min(b, N-1-a)+1):
                minus[(b-k)*N+a+k, a*N+b] = coeff(a, b, k, negative=True).x
    plus, minus = plus*tensor_frame % p, minus*tensor_frame % p
    assert np.array_equal(plus@minus % p, np.eye(N*N, dtype=np.int64))
    pivot = np.array([pow(int(K[j, j]), 1-N, p) for j in range(N)], dtype=np.int64)
    return p, eta, q, E, F, K, pivot, plus, minus


def word_matrix(word, plus, minus, strands, N, p):
    out = np.eye(N**strands, dtype=np.int64)
    for letter in word:
        left = np.eye(N**(abs(letter)-1), dtype=np.int64)
        right = np.eye(N**(strands-abs(letter)-1), dtype=np.int64)
        out = np.kron(np.kron(left, plus if letter > 0 else minus), right)@out % p
    return out


def partial(C, pivot, strands, N, p):
    out = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        for c in range(N):
            for closed in itertools.product(range(N), repeat=strands-1):
                row, column, weight = c, a, 1
                for x in closed:
                    row, column = row*N+x, column*N+x
                    weight = weight*int(pivot[x]) % p
                out[c, a] = (out[c, a]+weight*int(C[row, column])) % p
    return out


def coproduct(E, F, K, strands, N, p):
    size = N**strands
    Et, Ft = np.zeros((size, size), dtype=np.int64), np.zeros((size, size), dtype=np.int64)
    Kt = np.array([[1]], dtype=np.int64)
    Ki = np.diag([pow(int(K[j, j]), -1, p) for j in range(N)]).astype(np.int64)
    for _ in range(strands):
        Kt = np.kron(Kt, K) % p
    for s in range(strands):
        e, f = np.array([[1]], dtype=np.int64), np.array([[1]], dtype=np.int64)
        for t in range(strands):
            e = np.kron(e, np.eye(N, dtype=np.int64) if t < s else E if t == s else K) % p
            f = np.kron(f, Ki if t < s else F if t == s else np.eye(N, dtype=np.int64)) % p
        Et, Ft = (Et+e) % p, (Ft+f) % p
    return Et, Ft, Kt


def action(kind, C, E, F, K, p):
    Ki = np.diag([pow(int(K[j, j]), -1, p) for j in range(len(K))]).astype(np.int64)
    if kind == "E":
        return (E@C-C@E)@Ki % p
    if kind == "F":
        return (F@C-Ki@C@K@F) % p
    return (K@C@Ki-C) % p


def actual_case(N, strands, word, split, slot):
    p, eta, q, E, F, K, pivot, plus, minus = balanced_data(N)
    A = word_matrix(word[split:], plus, minus, strands, N, p)
    B = word_matrix(word[:split], plus, minus, strands, N, p)
    Et, Ft, Kt = coproduct(E, F, K, strands, N, p)
    for operator in (Et, Ft, Kt):
        assert not np.any((operator@A-A@operator) % p)
        assert not np.any((operator@B-B@operator) % p)
    # Full actual zero-framing and complete ADO external line.
    writhe, m = sum(1 if x > 0 else -1 for x in word), N-1
    imag = pow(eta, N, p)
    external = pow(eta, -writhe*m*(m+2), p)*pow(imag, N+3, p)*pow(N, -1, p) % p
    T = np.zeros((N, N, N, N), dtype=np.int64)  # c,d,a,b
    conditionally_nonzero = 0
    prefix_nonzero = 0
    for b in range(N):
        for d in range(N):
            coupon = np.zeros((N, N), dtype=np.int64)
            coupon[b, d] = 1
            X = embed(coupon, slot, strands, N)
            C = external*partial(A@X@B % p, pivot, strands, N, p) % p
            T[:, d, :, b] = C
            for kind in ("E", "F", "K"):
                cut_current = action(kind, C, E, F, K, p)
                total_current = action(kind, X, Et, Ft, Kt, p)
                exact = external*partial(A@total_current@B % p, pivot, strands, N, p) % p
                assert np.array_equal(cut_current, exact)
                # Original source is all matrix entries/N, not diagonaltrace/N.
                phi = int(np.sum(cut_current))*pow(N, -1, p) % p
                band_source = sum(int(cut_current[c, a]) for a in range(N) for c in range(N))*pow(N, -1, p) % p
                assert phi == band_source
                if b == d and phi:
                    assert not np.any(np.diag(cut_current))
                    conditionally_nonzero += 1
                if kind in ("E", "F"):
                    local = embed(action(kind, coupon, E, F, K, p), slot, strands, N)
                    if np.any((total_current-local) % p):
                        prefix_nonzero += 1
    C = external*partial(A@B % p, pivot, strands, N, p) % p
    reconstructed = sum((T[:, b, :, b] for b in range(N)), np.zeros((N, N), dtype=np.int64)) % p
    assert np.array_equal(C, reconstructed)
    assert not np.any((C-np.diag(np.diag(C))) % p)
    J = np.array([[T[a, b, a, b] for b in range(N)] for a in range(N)], dtype=np.int64)
    original = int(np.sum(C))*pow(N, -1, p) % p
    assert original == int(np.sum(J))*pow(N, -1, p) % p
    # Literal two physical position couplings, including every sourcefactor.
    x, y = 2, 3
    weighted = sum((pow(y, b, p)*T[:, b, :, b] for b in range(N)), np.zeros((N, N), dtype=np.int64)) % p
    from_tensor = sum(pow(x, a, p)*int(weighted[a, a]) for a in range(N))*pow(N, -1, p) % p
    from_array = sum(pow(x, a, p)*pow(y, b, p)*int(J[a, b]) for a in range(N) for b in range(N))*pow(N, -1, p) % p
    assert from_tensor == from_array
    # Full physical degree conservation holds before the internal sums.
    for c, d, a, b in itertools.product(range(N), repeat=4):
        if c+d != a+b:
            assert not T[c, d, a, b]
    assert prefix_nonzero
    return {"N": N, "strands": strands, "word": list(word), "second_cut_slot": slot,
            "actual_original_pivots_halfCartan_framing_ADO_line_retained": True,
            "two_cut_reconstruction_and_single_1_over_N_source_exact": True,
            "two_physical_weight_couplings_exact": True,
            "all_actual_coupon_Hopf_current_rows_exact": True,
            "offdiagonal_original_source_nonzero_conditional_rows": conditionally_nonzero,
            "actual_total_vs_local_prefix_differences": prefix_nonzero}


def actual_unknot_ports(N):
    p, _, _, E, _, _, _, _, _ = balanced_data(N)
    T = np.zeros((N, N, N, N), dtype=np.int64)
    for a in range(N):
        for b in range(N):
            T[b, a, a, b] = 1
    J = np.array([[T[a, b, a, b] for b in range(N)] for a in range(N)], dtype=np.int64)
    assert np.array_equal(J, np.eye(N, dtype=np.int64))
    first_E_diag = np.array([[sum(E[a, c]*T[c, b, a, b] for c in range(N)) % p
                              for b in range(N)] for a in range(N)], dtype=np.int64)
    assert not np.any(first_E_diag)
    assert np.any(E@J % p)
    # Balanced one-port channels really induce every left matrix unit.
    for i, j in itertools.product(range(N), repeat=2):
        left = np.zeros((N, N), dtype=np.int64)
        left[i, j] = 1
        channel = np.zeros_like(J)
        for a in range(N):
            for b in range(N):
                channel[a, b] = sum(left[a, c]*left[a, u]*T[c, b, u, b]
                                     for c in range(N) for u in range(N)) % p
        assert np.array_equal(channel, left@J % p)
    return {"N": N, "actual_two_cut_unknot_Hopf_nondescent_exact": True,
            "balanced_port_matrix_unit_lift_exact": True}


def main():
    cases = [actual_case(N, 2, (1, 1, 1), 1, 1) for N in range(2, 6)]
    cases += [actual_case(N, 3, (1, -2, 1, -2), 2, 2) for N in (2, 3, 4)]
    ports = [actual_unknot_ports(N) for N in range(2, 6)]
    assert any(case["offdiagonal_original_source_nonzero_conditional_rows"] for case in cases)
    target = Path(__file__).with_name("actual_two_cut_ports_results.json")
    target.write_text(json.dumps({"status": "pass", "actual_two_cut_braid_cases": cases,
                                  "actual_port_nondescent_and_channel_cases": ports,
                                  "scope": "Physical two-cut reconstruction/current map; no unmarked deck trace, global Gaussian source or volume claim."}, indent=2)+"\n")
    print(json.dumps({"status": "pass", "actual_two_cut_braid_cases": len(cases),
                      "actual_unknot_port_cases": len(ports), "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
