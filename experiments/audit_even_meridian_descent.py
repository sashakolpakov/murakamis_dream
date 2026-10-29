#!/usr/bin/env python3
"""Exact checks for the knot's squared-meridian cyclic descent.

Checks actual cut matrices, the norm of the uniform longitude insertion,
the full-state sign twist, and the relation between N and 2N monodromy.
No root-central/classical-A equality or volume-limit assertion is made.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field, cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices, WORDS


def exact_cut_parities():
    records = []
    diagrams = [(2, [(0, 1)]*3), (3, WORDS[0]), (3, WORDS[1]), (3, WORDS[2])]
    for level in (2, 3, 4, 5, 6):
        prime, generic, root = field(level)
        for actual_root, q in ((False, generic), (True, root)):
            M = generic
            x = -pow(q, -1, prime)*M % prime
            for strands, word in diagrams:
                old = cut_matrix_dense(level, prime, color_matrices(level, prime, q, x), strands, word)
                opposite_M = cut_matrix_dense(level, prime, color_matrices(level, prime, q, -x % prime), strands, word)
                opposite_q = cut_matrix_dense(level, prime, color_matrices(level, prime, -q % prime, -x % prime), strands, word)
                assert np.array_equal(old, opposite_M)
                assert np.array_equal(old, opposite_q)
                records.append({"level": level, "actual_root": actual_root,
                                "strands": strands, "crossings": len(word),
                                "even_meridian_cut_matrix": True,
                                "generic_closed_lift_uses_q_squared": True})
    return records


def norms_and_monodromy(level):
    prime, generator, q = field(level)
    Q = q*q % prime
    Y = generator
    delta = pow(-1, level-1, prime)
    twist = -pow(q, -1, prime) % prime
    assert pow(twist, level, prime) == delta

    def gauge(y):
        return twist*(Q*y-1)*pow(y-1, -1, prime) % prime

    product_g = 1
    H = np.eye(2, dtype=np.int64)
    Hfull = np.eye(2, dtype=np.int64)
    H2 = np.eye(2, dtype=np.int64)
    for r in range(2*level):
        y = Y*pow(Q, r, prime) % prime
        B = np.array([[1+y, y], [1, 1]], dtype=np.int64) % prime
        H2 = H2@B % prime
        if r < level:
            H = H@B % prime
            Hfull = Hfull@(gauge(y)*B % prime) % prime
            product_g = product_g*gauge(y) % prime
    assert product_g == delta
    assert np.array_equal(H2, H@H % prime)
    assert np.array_equal(Hfull, delta*H % prime)

    # Per-state local factors of the longitude observable have norm one.
    local_norms = []
    for a, b, k in ((1 % level, 0, 0), (level-1, 0, level-1),
                    (level-1, 1 % level, 1)):
        A, B, C = pow(Q, a, prime), pow(Q, b, prime), pow(Q, k, prime)
        for sign in (-1, 1):
            norm = 1
            for r in range(level):
                y = Y*pow(Q, r, prime) % prime
                if sign > 0:
                    factor = ((1-y*C*pow(A, -1, prime))*pow(B*C % prime, -1, prime)
                              *pow(1-y*pow(A, -1, prime), -1, prime)) % prime
                else:
                    factor = (A*(1-y*C*pow(B, -1, prime))
                              *pow(1-y*pow(B, -1, prime), -1, prime)) % prime
                norm = norm*factor % prime
            assert norm == 1
            local_norms.append(norm)

    # The full normalization is a section of the retained sign line.
    M = generator
    def d(m):
        return (pow(m, level-1, prime)
                *pow(sum(pow(m, 2*j, prime) for j in range(level)) % prime, -1, prime)) % prime
    assert d(-M % prime) == delta*d(M) % prime
    return {"level": level, "prime": prime, "full_state_cyclic_norm": int(delta),
            "reduced_longitude_local_norms": local_norms,
            "N_to_2N_monodromy_square_checked": True,
            "full_twist_monodromy_checked": True,
            "full_normalization_parity_checked": True}


def spectral_square_identity():
    W, V = sp.symbols("W V")
    records = []
    for rank in (1, 2, 3):
        coeff = sp.symbols("a:"+str(rank))
        P = W**rank+sum(coeff[j]*W**j for j in range(rank))
        H = sp.zeros(rank)
        for j in range(rank-1):
            H[j+1, j] = 1
        for j in range(rank):
            H[j, rank-1] = -coeff[j]
        squared = (V*sp.eye(rank)-H*H).det()
        result = (-1)**rank*sp.resultant(P, W*W-V, W)
        assert sp.expand(squared-result) == 0
        records.append({"rank": rank, "resultant_identity_exact": True})
    return records


def main():
    result = {"scope": "Actual squared-meridian descent and signed cyclic norm data; no selected volume theorem.",
              "actual_cut_parities": exact_cut_parities(),
              "cyclic_norms": [norms_and_monodromy(n) for n in (2, 3, 4, 5, 6, 8, 9, 10, 12, 15)],
              "spectral_square": spectral_square_identity()}
    Path(__file__).with_name("even_meridian_descent_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"actual_cut_parity_cases": len(result["actual_cut_parities"]),
                      "cyclic_levels": [r["level"] for r in result["cyclic_norms"]],
                      "full_even_level_sign_retained": True,
                      "spectral_square_ranks": [r["rank"] for r in result["spectral_square"]],
                      "all_checks_passed": True}), flush=True)


if __name__ == "__main__":
    main()
