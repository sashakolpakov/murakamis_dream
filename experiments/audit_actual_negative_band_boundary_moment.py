#!/usr/bin/env python3
"""Actual finite negative-band moment, its K-Ward row and norm-zero atom.

Retains the existing actual tensor source.  The geometric eta parameter is
never substituted for the independent Fourier-band variable in these tests.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data
from audit_identity_cut_orientation_cover import actual_tensor, kernel


def coupon_cut(T, X, p):
    N = T.shape[0]
    out = np.zeros((N, N), dtype=np.int64)
    for c, a in itertools.product(range(N), repeat=2):
        out[c, a] = sum(int(T[c, d, a, b])*int(X[b, d])
                        for b, d in itertools.product(range(N), repeat=2)) % p
    return out


def actual_ward_case(N, word, split):
    p, Q, T = actual_tensor(N, 2, word, split, 1)
    _, _, q, _, _, K, *_ = balanced_data(N)
    assert Q == q  # actual_tensor returns the q retained by its construction.
    Q = q*q % p  # physical head clock is Q=q^2.
    X, H = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    for b in range(N):
        for d in range(b):
            m = b-d
            X[b, d] = m
            H[b, d] = m*pow((pow(Q, -m, p)-1) % p, -1, p) % p
    diagonal = np.diag(K)
    inverses = np.array([pow(int(k), -1, p) for k in diagonal], dtype=np.int64)
    ward_coupon = (diagonal[:, None]*H*inverses[None, :]-H) % p
    assert np.array_equal(ward_coupon, X)
    CX, CH = coupon_cut(T, X, p), coupon_cut(T, H, p)
    cut_ward = (diagonal[:, None]*CH*inverses[None, :]-CH) % p
    assert np.array_equal(CX, cut_ward)
    poly = kernel(T, p)
    raw = sum(-j*value for j, value in poly.items() if j < 0) % p
    moment = raw*pow(N, -1, p) % p
    assert moment == int(CX.sum())*pow(N, -1, p) % p
    source = poly.get(0, 0)*pow(N, -1, p) % p
    dual_row = sum((pow(Q, a-c, p)-1)*int(CH[c, a])
                   for c, a in itertools.product(range(N), repeat=2))*pow(N, -1, p) % p
    assert dual_row == moment
    return {"N": N, "word": list(word), "split": split, "prime": p,
            "original_source": source, "weighted_moment_with_single_1_over_N": moment,
            "literal_coupon_and_true_K_Ward_source_row": True,
            "all_original_pivotal_framing_peripheral_lines_retained": True}


def ptr_sym(M, g):
    return sp.Matrix(2, 2, lambda c, a: sum(g[t]*M[c*2+t, a*2+t] for t in range(2)))


def symbolic_tensor_kernel(A, B, g, external):
    out = {}
    for b, d in itertools.product(range(2), repeat=2):
        X = sp.zeros(2)
        X[b, d] = 1
        C = external*ptr_sym(A*sp.kronecker_product(sp.eye(2), X)*B, g)
        out[d-b] = sp.simplify(out.get(d-b, 0)+sum(C))
    return {j: sp.simplify(value) for j, value in out.items()}


def exact_characteristic_zero():
    I = sp.I
    eta = (1+I)/sp.sqrt(2)
    R = sp.Matrix([[eta, 0, 0, 0], [0, 0, 1/eta, 0],
                   [0, 1/eta, 2*I/eta, 0], [0, 0, 0, eta]])
    g = [-I, I]
    inverse = sp.simplify(R.inv())
    assert sp.simplify(R*inverse) == sp.eye(4)
    pair = symbolic_tensor_kernel(inverse, R, g, I/2)
    outside = symbolic_tensor_kernel(sp.eye(4), sp.eye(4), g, I/2)
    assert pair == {-1: I, 0: 0, 1: -I}
    assert all(value == 0 for value in outside.values())
    knot_rows = []
    for writhe in (1, 3):
        # The same literal second cut: immediately after the first crossing.
        F = symbolic_tensor_kernel(R**(writhe-1), R, g, I*eta**(-3*writhe)/2)
        assert F[-1] == sp.Rational(1, 2)
        assert F[0]/2 == (-I/2 if writhe == 1 else 3*I/2)
        knot_rows.append({"word": [1]*writhe, "source": str(F[0]/2),
                          "negative_band_weight": str(F[-1])})
    # Exact whole K-Ward coupon on the actual generic D_1 R coefficient.
    half = sp.symbols("eta_half", nonzero=True)
    q, rho = half**2, half**2-half**-2
    generic_R = sp.Matrix([[half, 0, 0, 0], [0, 0, 1/half, 0],
                           [0, 1/half, rho/half, 0], [0, 0, 0, half]])
    generic_g = [1/q, q]
    U = sp.Matrix([[0, 0], [1, 0]])
    H = U/(q**-2-1)
    CH = ptr_sym(generic_R.inv()*sp.kronecker_product(sp.eye(2), H)*generic_R, generic_g)
    CX = ptr_sym(generic_R.inv()*sp.kronecker_product(sp.eye(2), U)*generic_R, generic_g)
    K = sp.diag(q, 1/q)
    assert (K*CH*K.inv()-CH-CX).applyfunc(sp.cancel) == sp.zeros(2)
    return {"exact_inverse_R_pair_F": "i(eta_F^-1-eta_F)",
            "outside_pair_F": "0", "same_cut_knot_counterexample": knot_rows,
            "actual_generic_q_D1_K_Ward_identity": True}


def original_atom_cases():
    # Exact polynomial norm and its moving divisor, tested independently of F.
    cases = []
    for N in range(2, 9):
        p, _, q, *_ = balanced_data(N)
        Q = q*q % p
        V_at_corner = 1
        for r in range(1, N):
            V_at_corner = V_at_corner*(1-pow(Q, r, p)) % p
        assert V_at_corner == N
        for B in (2, 3, 5):
            product = 1
            for r in range(N):
                product = product*(1-B*pow(Q, r, p)) % p
            assert product == (1-pow(B, N, p)) % p
        cases.append({"N": N, "primitive_norm_polynomial_exact": True,
                      "whole_moving_divisor": "B=Q^N", "corner_unit_value": N})
    eta, c, s = sp.symbols("eta_geo c s", nonzero=True)
    k = 1-c*eta/(s*(1-eta)**2)
    B = 1/k
    residues = []
    for N in range(2, 8):
        amplitude = 1/(1-B**N)
        polar = sp.limit(eta*amplitude, eta, 0)
        assert sp.simplify(polar+s/(N*c)) == 0
        density = 1/(s*(1-eta)**2)
        residue = sp.residue(amplitude*density, eta, 0)
        assert sp.simplify(residue+1/(N*c)) == 0
        residues.append({"N": N, "simple_atom_coefficient": "-s/(N*c)",
                         "geometric_residue_if_this_actual_atom_inserted": "-1/(N*c)"})
    return {"norm_and_unit_cases": cases, "symbolic_simple_atom_residues": residues,
            "scope": "Original negative N-step Ward atom, not an asserted factor in the selected full knot state."}


def main():
    exact = exact_characteristic_zero()
    cases = []
    for N in range(2, 8):
        for word, split in [((1,), 1), ((1, 1, 1), 1), ((1, -1), 1), ((1, -1), 0)]:
            cases.append(actual_ward_case(N, word, split))
    assert any(row["original_source"] == 0 and row["weighted_moment_with_single_1_over_N"] != 0
               for row in cases if row["split"] == 1)
    atoms = original_atom_cases()
    result = {"status": "pass", "characteristic_zero": exact,
              "actual_signed_tensor_Ward_cases": cases, "original_Ward_atom": atoms,
              "scope": "Exact independent physical B and Fourier eta_F source/current model; no automatic cap-to-geometric cycle map or volume claim."}
    output = Path(__file__).with_name("actual_negative_band_boundary_moment_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "actual_signed_tensor_Ward_cases": len(cases),
                      "actual_characteristic_zero_counterexamples": True,
                      "root_norm_unit_levels": len(atoms["norm_and_unit_cases"]),
                      "exact_simple_atom_residues": len(atoms["symbolic_simple_atom_residues"]),
                      "results": str(output)}, indent=2))


if __name__ == "__main__":
    main()
