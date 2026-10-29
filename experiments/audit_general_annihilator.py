#!/usr/bin/env python3
"""Diagnostics for the general annihilator proof and peripheral conversions.

The proof itself is a degree count and a moment identity, not a finite
numerical search. These checks cover the vanishing-specialization step,
descent from fractional coefficients, actual contour moments, and the exact
figure-eight conversion between two literature state normalizations.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.special import roots_hermite

from check_literature_state_volume import ETA, PI, VOLUME, Remainder, dilog_minus_exp


def audit_field_descent():
    q, Q = sp.symbols("q Q")
    zero = (sp.Integer(0),) * 4
    one = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
    root_Q = (sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(0))
    # Basis 1,s,U,sU, with s^2=q, U^2=Q; sigma(U)=sU.
    def add(a, b):
        return tuple(sp.expand(x + y) for x, y in zip(a, b))

    def multiply(a, b):
        result = [sp.Integer(0)] * 4
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                s_degree = i % 2 + j % 2
                u_degree = i // 2 + j // 2
                k = s_degree % 2 + 2 * (u_degree % 2)
                result[k] += x * y * q ** (s_degree // 2) * Q ** (u_degree // 2)
        return tuple(sp.expand(x) for x in result)

    def sigma(a):
        a = [x.subs(Q, q * Q) for x in a]
        return a[0], a[1], q * a[3], a[2]

    def shift(vector):
        c, d = vector  # c f+d E f, with E^2 f=U E f-f.
        sd = sigma(d)
        return tuple(-x for x in sd), add(sigma(c), multiply(root_Q, sd))

    vector = one, zero
    columns = []
    for _ in range(9):
        columns.append(sp.Matrix(vector[0] + vector[1]))
        vector = shift(vector)
    matrix = sp.Matrix.hstack(*columns)
    coefficients = [
        q**6, 0, q**3 * (q + 1) * (q**2 + 1), 0,
        -q * (Q**2 * q**8 - q**4 - q**3 - 2 * q**2 - q - 1), 0,
        (q + 1) * (q**2 + 1), 0, 1,
    ]
    assert all(sp.expand(x) == 0 for x in matrix * sp.Matrix(coefficients))
    assert matrix[:, :8].rank() == 8
    return {
        "input_equation": "E^2 f-U E f+f=0; U^2=Q; sigma(U)=sU; s^2=q",
        "base_field": "Q(q,Q)",
        "descended_operator_coefficients_by_E_degree": [str(sp.factor(x)) for x in coefficients],
        "exact_residual_zero": True,
        "first_eight_shifts_independent_over_base_field": True,
    }


def audit_formal_moment_extraction():
    q, Q, T = sp.symbols("q Q T")
    P = [
        q * T * (q**3 * T * Q**2 - 1) * Q**2,
        -(q**2 * T * Q**2 - 1)
        * (q**4 * T**2 * Q**4 - q**3 * T**2 * Q**3 - q * (q**2 + 1) * T * Q**2 - q * T * Q + 1),
        q**3 * T**2 * (q * T * Q**2 - 1) * Q**2,
    ]
    inflated = [(T - 1)**2 * a for a in P]
    assert all(a.subs(T, 1) == 0 for a in inflated)
    recovered = [sp.diff(a, T, 2).subs(T, 1) / 2 for a in inflated]
    assert all(sp.expand(a - b.subs(T, 1)) == 0 for a, b in zip(recovered, P))
    assert any(a != 0 for a in recovered)
    return {"direct_specialization_zero": True, "second_moment_recovers_nonzero_boundary_operator": True}


def audit_figure_eight_matrices():
    x0 = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0]])
    x1 = sp.Matrix([[0, 0, 0, 1], [1, 0, 0, 0]])
    x2 = sp.Matrix([[0, 0, 1, 0], [0, 1, 0, 0]])
    x3 = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1]])
    face_A = (x0 - x1 + x2).col_join(x2 - x3)
    face_B = sp.zeros(2, 2).col_join(sp.diag(1, -1))
    r = x0 * face_A.inv() * face_B
    Qf = -(r + r.T) / 2
    G = -2 * Qf + sp.diag(1, 0)
    edge_A = sp.Matrix([[1, -2], [0, 4]])
    edge_B = sp.Matrix([[-1, -1], [0, 2]])
    assert G == edge_B.inv() * edge_A
    assert Qf == sp.diag(1, -1)
    c = edge_B.inv() * sp.Matrix([-1, 2]) - G * sp.ones(2, 1)
    p = 2 * edge_B.inv() * sp.Matrix([0, 1])
    assert c == sp.Matrix([1, -1])
    assert p == sp.Matrix([-1, 1])
    assert (edge_A + edge_B) * sp.ones(2, 1) == 3 * sp.Matrix([-1, 2])
    return {"face_determinant": int(face_A.det()), "FAMED_matrix_identity_exact": True,
            "c_over_pi": list(c), "p": list(p)}


def normalized_am_summands(b, X, order=256):
    nodes, weights = roots_hermite(order)
    gaussian_rate = np.sqrt(3) / (4 * PI)
    u = b * nodes / np.sqrt(gaussian_rate) - 1j * ETA
    phase = (dilog_minus_exp(X - u) - dilog_minus_exp(u) - X * (2 * u - X)) / 1j
    remainder = Remainder(b)
    exponent = (phase + VOLUME) / (2 * PI * b**2) + nodes**2 + remainder(X - u) - remainder(u)
    summands = np.exp(np.log(weights) + exponent - (1 + b**(-2)) * X)
    summands /= 2 * PI * np.sqrt(gaussian_rate)
    return u, summands


def normalized_famed_state(b, X, order=256):
    nodes, weights = roots_hermite(order)
    gaussian_rate = np.sqrt(3) / (4 * PI)
    U = b * nodes / np.sqrt(gaussian_rate) + 1j * ETA
    S = dilog_minus_exp(U) + dilog_minus_exp(U - X) + U**2 / 2 + X * U - X**2 / 2
    remainder = Remainder(b)
    exponent = (S / 1j + VOLUME) / (2 * PI * b**2) + nodes**2 + remainder(U) + remainder(U - X)
    integral = np.sum(np.exp(np.log(weights) + exponent)) / (2 * PI * np.sqrt(gaussian_rate))
    sqrt_hbar = b / (1 + b**2)
    return integral * np.exp(-(1 + b**(-2)) * X / 2) / (2 * PI * sqrt_hbar)


def audit_contour_moments_and_state_conversion():
    records = []
    for b in [0.18, 0.12]:
        q = np.exp(2j * PI * b**2)
        s = np.exp(1j * PI * b**2)
        delta = 2j * PI * b**2
        for X in [0, 0.03 + 0.01j]:
            u, summands = normalized_am_summands(b, X)
            state = np.sum(summands)
            Q, Y = np.exp(-X), np.exp(-u)
            r1 = Q**(-2) / ((1 + s * Y / Q) * (1 + 1 / (s * Y)))
            r_next = Q**(-2) / ((1 + s * q * Y / Q) * (1 + 1 / (s * q * Y)))
            first = np.sum(summands * u * (r1 - 1))
            second = np.sum(summands * u**2 * (r1 * r_next - 2 * r1 + 1))
            first_error = abs(first / (delta * state) - 1)
            second_error = abs(second / (2 * delta**2 * state) - 1)
            assert first_error < 2e-10
            assert second_error < 2e-10
            zeta = np.exp(1j * PI * (b**2 + b**(-2)) / 12)
            sqrt_hbar = b / (1 + b**2)
            predicted = zeta / (2 * PI * sqrt_hbar) * np.exp((1 + b**(-2)) * X / 2) * state
            direct = normalized_famed_state(b, X)
            conversion_error = abs(direct / predicted - 1)
            assert conversion_error < 2e-10
            # This gauge contributes a minus sign in the classical longitude.
            gauge_shift = np.exp(-1j * PI * (b**2 + 1))
            assert abs(gauge_shift + 1 / s) < 1e-14
            records.append({
                "b": b, "X": str(X),
                "first_moment_relative_error": float(first_error),
                "second_moment_relative_error": float(second_error),
                "exact_state_conversion_relative_error": float(conversion_error),
            })
    return records


def main():
    result = {
        "field_descent": audit_field_descent(),
        "vanishing_specialization": audit_formal_moment_extraction(),
        "figure_eight_matrices": audit_figure_eight_matrices(),
        "contour_moments_and_state_conversion": audit_contour_moments_and_state_conversion(),
        "scope": "Exact algebra plus numerical diagnostics; general existence follows from the written degree-count and moment proof, not from these examples.",
    }
    # Convert exact SymPy integer entries in the matrix certificate to JSON.
    result["figure_eight_matrices"]["c_over_pi"] = [int(x) for x in result["figure_eight_matrices"]["c_over_pi"]]
    result["figure_eight_matrices"]["p"] = [int(x) for x in result["figure_eight_matrices"]["p"]]
    Path(__file__).with_name("general_annihilator_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
