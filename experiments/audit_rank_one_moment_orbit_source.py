#!/usr/bin/env python3
"""Actual rank-one multiplicative moment and retained Whittaker orbit source."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data
from audit_high_color_first_normal_r_degree import root_field
from audit_highest_whittaker_boundary import actual_head, inverse_diagonal
from audit_identity_cut_orientation_cover import actual_tensor


def matrix_inverse(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p)).astype(np.int64)


def beta_K(X, Q, p):
    return sum(int(X[c, 0])*pow((pow(Q, -c, p)-1) % p, -1, p)
               for c in range(1, len(X))) % p


def moment_case(N, root):
    p, eta = root_field(N)
    q = pow(eta, 2, p) if root else int(sp.primitive_root(p))
    M = 2
    Q, B, _, _, P, delta, kappa, D, F, E = actual_head(N, q, M, p)
    I = np.eye(N, dtype=np.int64)
    Binv = inverse_diagonal(B, p)
    Z = pow(Q, N, p)
    v, w = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
    v[0], w[0] = 1, 1
    e = np.outer(v, w)
    normalized = pow(Q, -1, p)*(B@P@Binv@P.T % p) % p
    a = (pow(Z, -1, p)-1) % p
    assert np.array_equal(normalized, (I+a*e) % p)
    inverse_normalized = Q*(P@B@P.T@Binv % p) % p
    assert np.array_equal(inverse_normalized, (I+(Z-1)*e) % p)
    assert pow(Q, N, p)*(1+a) % p == 1
    assert np.count_nonzero(np.diag((normalized-I) % p)) == (0 if root else 1)
    if not root:
        assert delta
        assert np.array_equal(pow(delta, -1, p)*(normalized-I) % p, pow(Z, -1, p)*e % p)
    else:
        assert Z == 1
    e_top = P.T@e@P % p
    Fcyc, Ecyc = P@(I-Q*B) % p, P.T@D % p
    assert np.array_equal(F, Fcyc@(I-e_top) % p)
    assert np.array_equal(E, Ecyc@(I-e) % p)
    SP = np.zeros_like(P)
    current = I.copy()
    for _ in range(N):
        SP = (SP+current) % p
        current = current@P % p
    ell = np.ones(N, dtype=np.int64)
    assert np.array_equal(w@SP % p, ell)
    assert np.array_equal(e@SP % p, np.outer(v, ell))
    C = np.array([[(3*i+5*j+i*j+2) % p for j in range(N)] for i in range(N)], dtype=np.int64)
    D2 = np.array([[(7*i+2*j+3*i*j+1) % p for j in range(N)] for i in range(N)], dtype=np.int64)
    moment_defect = Q*(normalized-I) % p
    selected_defect = moment_defect@SP % p
    assert np.array_equal(selected_defect, Q*a*np.outer(v, ell) % p)
    lhs = int(ell@C@selected_defect@D2@v) % p
    rhs = Q*a*int(ell@C@v)*int(ell@D2@v) % p
    assert lhs == rhs
    DK = (Binv@C@B-C) % p
    assert (int(ell@C@v)-int(w@C@v)) % p == beta_K(DK, Q, p)
    if root:
        norm_squared = -sum(pow(Q, c, p)*pow((1-pow(Q, c, p)) % p, -2, p)
                            for c in range(1, N)) % p
        assert norm_squared == (N*N-1)*pow(12, -1, p) % p
    else:
        # Naive product moment pairs do not remain rank one under fusion.
        e1, e2 = np.kron(e, I), np.kron(I, e)
        fusion = ((np.eye(N*N, dtype=np.int64)+a*e1)@
                  (np.eye(N*N, dtype=np.int64)+a*e2)-np.eye(N*N, dtype=np.int64)) % p
        assert Z not in (1, p-1)
        assert np.count_nonzero(np.diag(fusion)) == 2*N-1
    return {"N": N, "root": root, "actual_rank_of_Q_normalized_defect": 0 if root else 1,
            "whole_framed_moment_and_inverse": True, "both_endpoint_projector_deletions": True,
            "original_orbit_cosource_and_K_homotopy": True,
            "whole_selected_framed_period_factorization": True,
            "rank_drop_divided_normal_retains_E00": True}


def actual_Fourier_sum_rule(N, strands, word, split, slot):
    p, q, T = actual_tensor(N, strands, word, split, slot)
    Q = q*q % p
    B = np.diag([pow(Q, c, p) for c in range(N)]).astype(np.int64)
    Binv = inverse_diagonal(B, p)
    source = sum(int(T[c, b, 0, b]) for c, b in itertools.product(range(N), repeat=2)) % p
    whitaker, moment, currents = [], [], []
    for j in range(N):
        A = np.zeros((N, N), dtype=np.int64)
        for c, a in itertools.product(range(N), repeat=2):
            A[c, a] = sum(pow(Q, j*(d-b), p)*int(T[c, d, a, b])
                          for b, d in itertools.product(range(N), repeat=2))*pow(N, -1, p) % p
        DK = (Binv@A@B-A) % p
        whit = int(A[:, 0].sum()) % p
        mom = int(A[0, 0])
        residual = beta_K(DK, Q, p)
        assert (whit-mom) % p == residual
        assert mom == source*pow(N, -1, p) % p
        whitaker.append(whit)
        moment.append(mom)
        currents.append(residual)
    assert sum(whitaker) % p == source
    assert sum(moment) % p == source
    assert sum(currents) % p == 0
    return {"N": N, "word": list(word), "original_pivot_framing_peripheral_lines_retained": True,
            "whole_K_row_applied_before_root_scalar_closure": True,
            "moment_partial_j_constant": True,
            "actual_nonconstant_Fourier_dependence_in_retained_Ward_sector": any(currents)}


def actual_R_case(N):
    p, _, _, _, _, _, _, plus, minus = balanced_data(N)
    w00 = np.zeros(N*N, dtype=np.int64)
    w00[0] = 1
    ell = np.ones(N*N, dtype=np.int64)
    S = np.ones((N, N), dtype=np.int64)
    S2 = np.kron(S, S)
    nonzero = 0
    for R in (plus, minus):
        r00 = int(R[0, 0])
        assert np.array_equal(R[:, 0], r00*w00 % p)
        assert np.array_equal(w00@R % p, r00*w00 % p)
        residual = (ell@R-r00*ell) % p
        exact = w00@(S2@R-R@S2) % p
        assert np.array_equal(residual, exact)
        nonzero += bool(np.any(residual))
    assert nonzero
    return {"N": N, "both_actual_signed_R_moment_framings_covariant": True,
            "original_Whittaker_orbit_residual_exact": True, "nonzero_orbit_R_defects": nonzero}


def exact_R_counterexample():
    eta = (1+sp.I)/sp.sqrt(2)
    R = sp.Matrix([[eta, 0, 0, 0], [0, 0, 1/eta, 0],
                   [0, 1/eta, 2*sp.I/eta, 0], [0, 0, 0, eta]])
    w = sp.Matrix([[1, 0, 0, 0]])
    ell = sp.ones(1, 4)
    S = sp.ones(4, 4)
    residual = (ell*R-eta*ell).applyfunc(sp.simplify)
    assert (residual-w*(S*R-R*S)).applyfunc(sp.simplify) == sp.zeros(1, 4)
    assert sp.simplify(residual[1]+sp.sqrt(2)*sp.I) == 0
    return {"N": 2, "literal_positive_R_orbit_residual_input_01": "-sqrt(2)*i",
            "full_half_Cartan_eta_retained": True}


def main():
    moments = [moment_case(N, root) for N in range(2, 9) for root in (False, True)]
    Fourier = [actual_Fourier_sum_rule(N, 2, (1, 1, 1), 1, 1) for N in range(2, 7)]
    Fourier += [actual_Fourier_sum_rule(N, 3, (1, -2, 1, -2), 2, 2) for N in range(2, 5)]
    Rcases = [actual_R_case(N) for N in range(2, 8)]
    result = {"status": "pass", "whole_moment_cases": moments,
              "actual_Fourier_sum_rules": Fourier, "actual_signed_R_cases": Rcases,
              "characteristic_zero_R_counterexample": exact_R_counterexample(),
              "scope": "Actual framed moment plus original orbit cosource/current, not selected geometric survival or a volume limit."}
    output = Path(__file__).with_name("rank_one_moment_orbit_source_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "whole_moment_cases": len(moments),
                      "actual_Fourier_sum_rules": len(Fourier), "actual_signed_R_levels": len(Rcases),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
