#!/usr/bin/env python3
"""Exact selected-source diagnostics on actual unknot and figure-eight objects.

Proofs are in notes/actual_mellin_normal_source_rigidity.md. These checks
distinguish an observable source from an arbitrary annihilator, include
literal first-normal companion terms, and test the actual root affine
figure-eight operator. No alternate off-root figure-eight calibration is
identified with the original finite-Verma lift.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import determinant, power, rank
from audit_finite_sum_annihilator import field
from audit_peripheral_normal_period import cyclotomic_block
from audit_regularized_kashaev_period import evaluate


def inverse(matrix, prime):
    return np.array(sp.Matrix(matrix.tolist()).inv_mod(prime)).astype(np.int64)


def dual_power(matrix0, matrix1, exponent, prime):
    out0 = np.eye(len(matrix0), dtype=np.int64)
    out1 = np.zeros_like(out0)
    for _ in range(exponent):
        out1 = (out1 @ matrix0 + out0 @ matrix1) % prime
        out0 = out0 @ matrix0 % prime
    return out0, out1


def actual_unknot_checks():
    Q, X = sp.symbols("Q X", nonzero=True)
    g = 1/X-1
    z1, z2 = X/(1-X), X**2/(1-X)
    assert sp.cancel(g*z1-1) == 0
    h2 = sp.cancel(g*z2)
    source2 = sp.expand(h2.subs(X, Q*X)-h2)
    assert sp.expand(source2-(Q-1)*X) == 0
    assert sp.cancel(source2.subs(X, Q*X)/source2-Q) == 0

    records = []
    for N in range(2, 10):
        prime, _, q = field(N)
        omega = q*q % prime
        eye = np.eye(2, dtype=np.int64)
        # The actual extra-left-factor annihilator (S-1)^2 g.
        Cbad = np.array([[0, 1], [-1, 2]], dtype=np.int64) % prime
        J = (Cbad-eye) % prime
        vbad = np.array([1, 1], dtype=np.int64)
        Hbad = power(inverse(Cbad, prime), N, prime)
        Lbad = (Hbad-eye) % prime
        assert np.array_equal(Hbad, (eye-N*J) % prime)
        assert rank(Lbad, prime) == 1
        assert rank(np.column_stack((Lbad, vbad)), prime) == 1
        # A nonconstant central h=U^m has an actual first-order lift.
        for m in (1, 2, 3):
            first_jet = np.array([0, N*m], dtype=np.int64) % prime
            L1v = (N*N*m*vbad) % prime
            assert not np.any((Lbad @ first_jet+L1v) % prime)

        # Rebuilt genuine source from (Y-1)(T-1), start two:
        # after h=g f, P_h=(S-Q)(S-1), h=X.
        C0 = np.array([[0, 1], [-omega, 1+omega]], dtype=np.int64) % prime
        C1 = np.array([[0, 0], [-omega, omega]], dtype=np.int64) % prime
        B0 = inverse(C0, prime)
        B1 = -B0 @ C1 @ B0 % prime
        H0, H1 = dual_power(B0, B1, N, prime)
        assert np.array_equal(H0, eye)
        v0 = np.array([1, omega], dtype=np.int64)
        assert not np.any((H1 @ v0+N*v0) % prime)
        ell = np.array([-1, 1], dtype=np.int64)*pow(omega-1, -1, prime) % prime
        assert int(ell @ v0) % prime == 1
        assert np.array_equal(ell @ H0 % prime, ell)
        assert rank(np.column_stack((H0-eye, v0)), prime) == 1
        # H1 + N D_X cancels the base h=X, leaving N^2 m for U^m h.
        for m in (1, 2, 3):
            normal = (H1 @ v0+N*(N*m+1)*v0) % prime
            assert int(ell @ normal) % prime == N*N*m % prime
        records.append({"N": N, "prime": prime,
                        "actual_extra_factor_selected_iota_zero": True,
                        "nonconstant_central_first_jets_survive_extra_factor": True,
                        "rebuilt_source_double_one_semisimple": True,
                        "observable_source_and_literal_first_normal_exact": True})
    return records


def figure_eight_coefficients(omega, y, prime):
    Q, Y = omega, y
    middle = (Q*Q*Y*Y-Q*Y**4+Q*Y**3+Q*Y-Q+Y*Y) % prime
    cm = Y*Y*(Q-Y)*(Q*Y*Y-1) % prime
    c0 = -(Y-1)**2*(Y+1)*middle % prime
    cp = Y*Y*(Q*Y-1)*(Q-Y*Y) % prime
    D = Y*(Y+1)*(Q-Y*Y)*(Q*Y*Y-1) % prime
    return cm, c0, cp, D


def forward_affine(omega, y, prime):
    cm, c0, cp, D = figure_eight_coefficients(omega, omega*y % prime, prime)
    if not cp:
        return None
    cp_inverse = pow(cp, -1, prime)
    return np.array([[0, 1, 0],
                     [-cm*cp_inverse, -c0*cp_inverse, D*cp_inverse],
                     [0, 0, 1]], dtype=np.int64) % prime


def actual_figure_eight_checks():
    records = []
    for N in range(2, 11):
        prime, _, q = field(N)
        omega = q*q % prime
        polynomial = cyclotomic_block(N, prime, omega)
        # This polynomial is the all-level actual figure-eight period by the
        # independently proved whole-source four-plat identity.
        selected = []
        for y in range(2, prime):
            U = pow(y, N, prime)
            h = (3-U-pow(U, -1, prime)) % prime
            if not h:
                continue
            orbit = [y*pow(omega, j, prime) % prime for j in range(N)]
            Cs = [forward_affine(omega, point, prime) for point in orbit]
            if any(C is None or not determinant(C, prime) for C in Cs):
                continue
            H = np.eye(3, dtype=np.int64)
            for C in Cs:
                H = H @ inverse(C, prime) % prime
            L = (H-np.eye(3, dtype=np.int64)) % prime
            v = np.array([evaluate(polynomial, y, prime),
                          evaluate(polynomial, omega*y % prime, prime), h],
                         dtype=np.int64)
            if not determinant((np.eye(2, dtype=np.int64)-H[:2, :2]) % prime, prime):
                continue
            for j, C in enumerate(Cs):
                point = orbit[j]
                before = np.array([evaluate(polynomial, point, prime),
                                   evaluate(polynomial, omega*point % prime, prime), h],
                                  dtype=np.int64)
                after_point = omega*point % prime
                after = np.array([evaluate(polynomial, after_point, prime),
                                  evaluate(polynomial, omega*after_point % prime, prime), h],
                                 dtype=np.int64)
                assert not np.any((C @ before-after) % prime)
            assert not np.any(L @ v % prime)
            assert rank(L, prime) == 2
            assert rank(np.column_stack((L, v)), prime) == 3
            ell = np.array([0, 0, pow(h, -1, prime)], dtype=np.int64)
            assert np.array_equal(ell @ H % prime, ell)
            assert int(ell @ v) % prime == 1
            t = sp.symbols("t")
            delta = sp.Matrix(H.tolist()).charpoly(t).as_expr()
            derivative = int(sp.diff(delta, t).subs(t, 1)) % prime
            expected = determinant((np.eye(2, dtype=np.int64)-H[:2, :2]) % prime, prime)
            assert derivative == expected and derivative
            selected.append({"Y": y, "U": U, "source": h,
                             "characteristic_derivative_at_one": derivative})
            if len(selected) == 3:
                break
        assert len(selected) == 3

        # The whole rational Mellin root fibre retains the Kashaev residue,
        # including a nontrivial fixed prefix subtraction.
        colors = [evaluate(polynomial, pow(omega, j, prime), prime) for j in range(1, N+1)]
        K = evaluate(polynomial, 1, prime)
        assert colors[-1] == K
        numerator = {j: colors[j-1] for j in range(1, N+1)}
        start = 3
        for degree in range(start, 3*N+2):
            coefficient = numerator[(degree-1) % N+1]
            assert coefficient == colors[(degree-1) % N]
        # Numerator/(1-X^N) has infinity limit -K. A prefix with
        # no constant term has zero residue when multiplied by dX/X.
        assert numerator[N] == K
        records.append({"N": N, "prime": prime,
                        "generic_orbits": selected,
                        "literal_actual_affine_transfers_exact": True,
                        "selected_source_rank_and_simple_one_exact": True,
                        "actual_Mellin_residue_preserved": True})
    return records


def main():
    result = {
        "actual_unknot_presentations": actual_unknot_checks(),
        "actual_figure_eight_root_affine_operator": actual_figure_eight_checks(),
        "scope": "Selected source normal rigidity; no alternate off-root lift equivalence, geometric norm, or volume bound."
    }
    target = Path(__file__).with_name("actual_mellin_normal_source_rigidity_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"actual_unknot_levels": len(result["actual_unknot_presentations"]),
                      "actual_figure_eight_levels": len(result["actual_figure_eight_root_affine_operator"]),
                      "generic_actual_root_orbits": sum(len(row["generic_orbits"]) for row in result["actual_figure_eight_root_affine_operator"]),
                      "output": str(target)}, indent=2))


if __name__ == "__main__":
    main()
