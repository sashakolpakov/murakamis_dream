#!/usr/bin/env python3
"""Actual highest/Whittaker source, moving walls and finite Fourier tail.

No endpoint-to-geometric Gaussian/source map is assumed in this audit.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field
from audit_identity_cut_orientation_cover import actual_tensor


def inverse_diagonal(A, p):
    return np.diag([pow(int(value), -1, p) for value in np.diag(A)]).astype(np.int64)


def power(A, n, p):
    out = np.eye(len(A), dtype=np.int64)
    for _ in range(n):
        out = out@A % p
    return out


def actual_head(N, q, M, p):
    Q = q*q % p
    B = np.diag([pow(Q, j, p) for j in range(N)]).astype(np.int64)
    U = np.zeros((N, N), dtype=np.int64)
    for j in range(N-1):
        U[j+1, j] = 1
    W = np.zeros_like(U)
    W[0, N-1] = 1
    P = U+W
    delta, kappa = (1-pow(Q, N, p)) % p, (M-pow(M, -1, p)) % p
    I = np.eye(N, dtype=np.int64)
    D = (M*inverse_diagonal(B, p)-pow(M, -1, p)*I) % p
    F = U@(I-Q*B) % p
    E = U.T@D % p
    return Q, B, U, W, P, delta, kappa, D, F, E


def whole_boundary_case(N, root, M):
    p, eta = root_field(N)
    q = pow(eta, 2, p) if root else int(sp.primitive_root(p))
    Q, B, U, W, P, delta, kappa, D, F, E = actual_head(N, q, M, p)
    I = np.eye(N, dtype=np.int64)
    assert np.array_equal(power(P, N, p), I)
    assert np.array_equal((B@P-Q*P@B) % p, delta*W % p)
    Fcyc, Ecyc = P@(I-Q*B) % p, P.T@D % p
    assert np.array_equal(F, (Fcyc-delta*W) % p)
    assert np.array_equal(E, (Ecyc-kappa*W.T) % p)
    ell = np.ones(N, dtype=np.int64)
    psi = np.zeros(N, dtype=np.int64)
    psi[0] = 1
    assert np.array_equal(B@psi % p, psi)
    assert not np.any(E@psi % p)
    assert np.array_equal(ell@P % p, ell)
    top, bottom = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
    top[-1], bottom[0] = 1, 1
    assert np.array_equal(ell@F % p, (ell@(I-Q*B)-delta*top) % p)
    assert np.array_equal(ell@E % p, (ell@D-kappa*bottom) % p)
    assert int(ell@Ecyc@psi) % p == kappa
    assert not np.any(power(F, N, p))
    normF = 1
    normE = 1
    for j in range(N):
        normF = normF*(1-pow(Q, j+1, p)) % p
        normE = normE*(M*pow(Q, -j, p)-pow(M, -1, p)) % p
    assert np.array_equal(power(Fcyc, N, p), normF*I % p)
    assert np.array_equal(power(Ecyc, N, p), normE*I % p)
    if root:
        unit = 1
        for j in range(1, N):
            unit = unit*(1-pow(Q, j, p)) % p
        assert unit == N
        expected = (-1)**(N-1)*(pow(M, N, p)-pow(M, -N, p)) % p
        assert normE == expected
    # Literal paired-source eigenline with commuting left/right operators.
    Q0 = np.outer(psi, ell)
    assert np.array_equal(B@Q0 % p, Q0)
    assert np.array_equal(Q0@P % p, Q0)
    assert int(np.trace(Q0)) == 1
    # Exact finite polynomial/source realization, including degree overflow.
    coefficients = np.array([(j*j+3*j+2) % p for j in range(N)], dtype=np.int64)
    bare_F = np.zeros(N+1, dtype=np.int64)
    for j, value in enumerate(coefficients):
        bare_F[j+1] = int(value)*(1-pow(Q, j+1, p)) % p
    bare_F[N] = (bare_F[N]-delta*int(coefficients[-1])) % p
    assert bare_F[N] == 0
    assert np.array_equal(bare_F[:N], F@coefficients % p)
    numerator = (D@coefficients) % p
    numerator[0] = (numerator[0]-kappa*int(coefficients[0])) % p
    assert numerator[0] == 0
    polynomial_E = np.r_[numerator[1:], 0]
    assert np.array_equal(polynomial_E, E@coefficients % p)
    return {"N": N, "root": root, "M": M, "whole_two_endpoint_source_equations": True,
            "cyclic_q_torus_defect_delta_W": True, "actual_F_nilpotent": True,
            "cyclic_F_norm": int(normF), "cyclic_E_norm": int(normE),
            "selected_divided_F_wrap_at_root": N if root else None,
            "strict_polynomial_and_Serre_source_realization": True}


def actual_highest_fourier_case(N, strands, word, split, slot):
    p, q, T = actual_tensor(N, strands, word, split, slot)
    Q = q*q % p
    coeff = {}
    for b, c, d in itertools.product(range(N), repeat=3):
        value = int(T[c, d, 0, b])
        if value:
            nu = d-b
            coeff[nu] = (coeff.get(nu, 0)+value) % p
            assert c == -nu
    coeff = {nu: v for nu, v in coeff.items() if v % p}
    assert all(-(N-1) <= nu <= 0 for nu in coeff)
    partial = [sum(value*pow(Q, j*nu, p) for nu, value in coeff.items())*pow(N, -1, p) % p
               for j in range(N)]
    fixed_source = coeff.get(0, 0)
    assert sum(partial) % p == fixed_source
    original_average = sum(int(T[c, b, a, b]) for c, a, b in itertools.product(range(N), repeat=3))*pow(N, -1, p) % p
    assert original_average == fixed_source
    return {"N": N, "word": list(word), "actual_original_source": fixed_source,
            "first_input_0_only_output_row_retained": True,
            "uninserted_negative_bands_and_single_final_j_sum": True,
            "original_all_pivots_and_external_lines_retained": True}


def positive_current_tail(N):
    p, eta = root_field(N)
    q = pow(eta, 2, p)
    Q, _, _, _, _, _, _, _, F, _ = actual_head(N, q, 1, p)
    flip = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        flip[b*N+a, a*N+b] = 1
    current = np.kron(np.eye(N, dtype=np.int64), F)@flip % p
    coeff = {}
    for b, c, d in itertools.product(range(N), repeat=3):
        value = int(current[c*N+d, b])
        if value:
            coeff[d-b] = (coeff.get(d-b, 0)+value) % p
    assert coeff.get(1, 0) == (1-Q) % p
    assert coeff[1]
    return {"N": N, "literal_second_output_F_positive_tail": "(1-Q) eta_F",
            "one_sided_uninserted_space_not_current_stable": True}


def symbolic_springer_boundary():
    r, s = sp.symbols("r s", nonzero=True)
    eta, a = -s, 1-r
    jacobian = sp.det(sp.Matrix([[sp.diff(eta, r), sp.diff(eta, s)],
                                [sp.diff(a, r), sp.diff(a, s)]]))
    density = -jacobian/(eta*(1-eta))
    assert sp.simplify(density+1/(s*(1+s))) == 0
    # Actual figure-eight third signed prefix, not an arbitrary matrix pair.
    shape = (-1+sp.sqrt(3)*sp.I)/2
    A = sp.Matrix([[1, 1], [0, 1]])
    Bword = sp.Matrix([[1, 0], [-shape, 1]])
    Cword = Bword*A.inv()*Bword*A*Bword.inv()
    V, Uword = Bword*A, Cword*Bword*A
    k0 = sp.simplify(Uword[1, 0]/V[1, 0])
    C0 = (Uword-k0*V).applyfunc(sp.simplify)
    gamma0 = sp.simplify(C0[1, 1]/(k0-1))  # j=3, so -(-1)^j=1.
    assert sp.simplify(k0-2-shape) == 0
    assert C0[0, 0] == -1
    assert sp.simplify(C0[1, 1]+shape) == 0
    assert sp.simplify(gamma0-shape**2) == 0
    momentum = sp.symbols("p_e")
    r_boundary = gamma0/(momentum+gamma0)
    assert sp.simplify(sp.diff(r_boundary, momentum)+gamma0/(momentum+gamma0)**2) == 0
    return {"candidate_classical_resolved_fiber": "v=1, eta_S=-s, a_B=1-r",
            "normal_residue": "-da_B=dr", "actual_figure_eight_exceptional_momentum": "p_e=u^2(1-r)/r",
            "scope": "Geometric boundary map, not constructed internal quantum-source transform."}


def main():
    whole = [whole_boundary_case(N, root, M) for N in range(2, 9)
             for root in (False, True) for M in (1, 2)]
    tensors = [actual_highest_fourier_case(N, 2, word, 1, 1) for N in range(2, 7)
               for word in ((1,), (1, 1, 1))]
    tensors += [actual_highest_fourier_case(N, 3, (1, -2, 1, -2), 2, 2) for N in range(2, 5)]
    tails = [positive_current_tail(N) for N in range(2, 9)]
    result = {"status": "pass", "whole_endpoint_and_norm_cases": whole,
              "literal_actual_signed_tensor_sources": tensors, "literal_current_tail_cases": tails,
              "classical_boundary_map": symbolic_springer_boundary(),
              "scope": "Exact highest-input source and two moving walls; no internal R/Gaussian source map or selected volume claim."}
    output = Path(__file__).with_name("highest_whittaker_boundary_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "whole_endpoint_cases": len(whole),
                      "actual_signed_tensor_cases": len(tensors), "positive_current_tail_levels": len(tails),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
