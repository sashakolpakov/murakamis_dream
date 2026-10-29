#!/usr/bin/env python3
"""Audit the exact tensor-to-fiber phase and its balanced-angle reduction.

The generic Gaussian identity is symbolic. Twist checks rebuild the matrices
from the face pairings and test the entire affine balanced angle space.
The numerical identity is pointwise; it does not replace a contour proof.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from check_literature_state_volume import Remainder
from twist_family_certificates import (
    combinatorial_data, edge_and_peripheral_matrices, positive_angles, twist_faces,
)
from twist_topology_audit import source_longitude_holonomy


def generic_phase_certificate():
    n = 3
    Q = sp.symbols("Q", positive=True)
    a, c, z = [sp.Matrix(sp.symbols(f"{letter}0:3")) for letter in ["a", "c", "z"]]
    epsilon = sp.Matrix([1, -1, 1])
    plus = [1, 0, 1]
    entries = sp.symbols("f0:6")
    F = sp.Matrix([[entries[0], entries[1], entries[2]],
                   [entries[1], entries[3], entries[4]],
                   [entries[2], entries[4], entries[5]]])
    d = sp.ones(n, 1) - a
    C = sp.diag(*epsilon) * c
    t, u = Q * (-z + sp.I * d) / 2, Q * z / 2
    H, W = F - sp.diag(*plus) / 2, 2 * F * d - C
    tensor_constant = sum(epsilon[j] * (-sp.Rational(1, 12) + Q**2 * (
        a[j] * c[j] / 4 + (a[j] - c[j]) / 12 - sp.Rational(1, 24))) for j in range(n))
    original = (2 * (t.T * F * t)[0] - sp.I * Q * (C.T * t)[0]
                - sum(plus[j] * u[j]**2 for j in range(n))
                - (Q**2 - 2) * sum(plus) / 12 + tensor_constant)
    K = (sum(epsilon[j] * (a[j] * c[j] / 4 + (a[j] - c[j]) / 12 - sp.Rational(1, 24))
             for j in range(n)) - sp.Rational(sum(plus), 12)
         + ((C.T * d)[0] - (d.T * F * d)[0]) / 2)
    transformed = sp.Rational(n, 12) + Q**2 * K + Q**2 * (
        (z.T * H * z)[0] - sp.I * (W.T * z)[0]) / 2
    assert sp.expand(original - transformed) == 0
    return {"mixed_sign_generic_gaussian_identity": True,
            "all_symmetric_gaussian_entries_indeterminate": True,
            "constant_root_of_unity": "exp(pi*i*N/12)"}


def selectors(n):
    a = sp.zeros(n, 3 * n)
    c = sp.zeros(n, 3 * n)
    for j in range(n):
        a[j, 3 * j], c[j, 3 * j + 2] = 1, 1
    return a, c


def balanced_certificate(p, parity):
    faces, signs = twist_faces(p, parity)
    data = combinatorial_data(faces, signs)
    n = len(faces)
    A, B, _, _, omitted = edge_and_peripheral_matrices(data["incidence"], signs, parity)
    F = data["Qf"]
    G = B.inv() * A
    pvector = 2 * B.inv()[:, -1]
    epsilon = sp.Matrix(signs)
    plus_count = sum(sign == 1 for sign in signs)
    aq, cq = selectors(n)
    Cq = sp.diag(*signs) * cq
    Wlinear = -2 * F * aq - Cq
    # Construct the exact branch constants, not a fitted linear term.
    Gp = sp.zeros(n, n)
    for j, sign in enumerate(signs):
        Gp[:, j] = data["incidence"][:, 3 * j + (2 if sign == 1 else 1)]
    selected = [j for j in range(n) if j != omitted]
    nu = sp.Matrix([2 - sum(Gp[j, k] for k in range(n)) for j in selected] + [2])
    c0 = B.inv() * nu - G * sp.ones(n, 1)
    theta0 = positive_angles(p, parity)
    constraints = sp.Matrix(n, 3 * n, lambda i, j: int(j // 3 == i)).col_join(data["incidence"])
    tangent = sp.Matrix.hstack(*constraints.nullspace())
    longitude = source_longitude_holonomy(p, parity).T
    meridian = sp.zeros(1, 3 * n)
    meridian[0, 3 * p], meridian[0, 3 * (p + 1)] = 1, -1
    discrepancy = Wlinear - pvector * longitude / 2
    assert discrepancy * tangent == sp.zeros(n, tangent.cols)
    assert discrepancy * theta0 + 2 * F * sp.ones(n, 1) - c0 == sp.zeros(n, 1)
    assert sp.Matrix.vstack(meridian, longitude) * tangent != sp.zeros(2, tangent.cols)
    assert (sp.Matrix.vstack(meridian, longitude) * tangent).rank() == 2

    # K/pi = theta^T Hessian theta/2 + linear^T theta + constant.
    Hessian = -aq.T * F * aq - (aq.T * sp.diag(*signs) * cq + cq.T * sp.diag(*signs) * aq) / 4
    linear = aq.T * (epsilon / 12 + F * sp.ones(n, 1)) + cq.T * (5 * epsilon / 12)
    constant = -sum(signs) / sp.Integer(24) - sp.Rational(plus_count, 12) - sum(F) / 2
    rhs_linear = aq.T * (epsilon / 12 + c0 / 4) + cq.T * (epsilon / 6)
    rhs_constant = -sp.Rational(n, 24) - sum(signs) / sp.Integer(12) - sum(c0) / 4
    defect_hessian = Hessian + (meridian.T * longitude + longitude.T * meridian) / 8
    assert tangent.T * defect_hessian * tangent == sp.zeros(tangent.cols, tangent.cols)
    gradient = defect_hessian * theta0 + linear - rhs_linear
    assert tangent.T * gradient == sp.zeros(tangent.cols, 1)
    defect_value = ((theta0.T * defect_hessian * theta0)[0] / 2
                    + ((linear - rhs_linear).T * theta0)[0] + constant - rhs_constant)
    assert defect_value == 0
    fixed_boundary = sp.Matrix.hstack(*constraints.col_join(meridian).col_join(longitude).nullspace())
    gauge_derivative = fixed_boundary.T * (Hessian * theta0 + linear)
    chosen = next(j for j in range(n) if pvector[j] != 0)
    sigma = sp.sign(data["face_A"].det() * pvector[chosen])
    return {"p": p, "parity": parity, "angle_space_dimension": tangent.cols,
            "peripheral_rank": 2, "balanced_W_identity_on_entire_angle_space": True,
            "phase_is_affine_after_adding_mu_lambda_over_8pi": True,
            "raw_phase_varies_at_fixed_peripherals": any(x != 0 for x in gauge_derivative),
            "coarea_orientation_sign": int(sigma),
            "chosen_nonzero_p_coefficient": str(pvector[chosen])}


def numerical_phase_checks():
    quantum_b = 0.6
    quantum_Q = quantum_b + 1 / quantum_b
    hbar = quantum_Q**(-2)
    remainder = Remainder(quantum_b)

    def log_phi(Z):
        Z = complex(Z)
        shift = int(np.floor(Z.imag / quantum_b + 0.5))
        base = Z - 1j * quantum_b * shift
        value = complex(remainder.log_phi_scaled(2 * np.pi * quantum_b * base))
        if shift > 0:
            for j in range(1, shift + 1):
                at = base + 1j * quantum_b * j
                value -= np.log(1 + np.exp(-1j * np.pi * quantum_b**2 + 2 * np.pi * quantum_b * at))
        elif shift < 0:
            for j in range(-shift):
                at = base - 1j * quantum_b * j
                value += np.log(1 + np.exp(-1j * np.pi * quantum_b**2 + 2 * np.pi * quantum_b * at))
        return value

    errors = []
    for p, parity in [(0, "odd"), (0, "even"), (2, "odd"), (2, "even")]:
        faces, signs = twist_faces(p, parity)
        F = np.array(combinatorial_data(faces, signs)["Qf"], dtype=float)
        angles = np.array(positive_angles(p, parity), dtype=float).reshape(-1, 3) * np.pi
        av, cv = angles[:, 0], angles[:, 2]
        epsilon = np.array(signs)
        positive = (epsilon + 1) / 2
        d, C = np.pi - av, epsilon * cv
        t = np.linspace(-0.27, 0.31, len(faces))
        u = -t + 1j * quantum_Q * d / (2 * np.pi)
        y = 2 * np.pi * u / quantum_Q
        log_original = 2j * np.pi * t @ F @ t
        for j, sign in enumerate(signs):
            log_original += quantum_Q * cv[j] * sign * t[j]
            log_original -= sign * log_phi(sign * (t[j] - 1j * quantum_Q * d[j] / (2 * np.pi)))
            log_original += sign * (-np.pi * 1j / 12 + 1j / hbar * (
                av[j] * cv[j] / (4 * np.pi) + (av[j] - cv[j]) / 12 - np.pi / 24))
        W = 2 * F @ d - C
        H = F - np.diag(positive) / 2
        K = (np.sum(epsilon * (av * cv / (4 * np.pi) + (av - cv) / 12 - np.pi / 24))
             - np.pi * sum(positive) / 12 + (C @ d - d @ F @ d) / (2 * np.pi))
        log_transformed = (np.pi * 1j * len(faces) / 12 + 1j * K / hbar
                           + (1j * y @ H @ y + W @ y) / (2 * np.pi * hbar)
                           + sum(log_phi(z) for z in u))
        error = abs(np.exp(log_original - log_transformed) - 1)
        assert error < 2e-10
        errors.append({"p": p, "parity": parity, "pointwise_relative_error": float(error)})
    return errors


def main():
    generic = generic_phase_certificate()
    records = [balanced_certificate(p, parity) for parity in ["odd", "even"] for p in range(9)]
    numeric = numerical_phase_checks()
    payload = {"scope": "Exact symbolic identities and finite diagnostics for the independent phase and fiber proof.",
               "generic_certificate": generic, "twist_angle_space_certificates": records,
               "pointwise_quantum_checks": numeric}
    destination = Path(__file__).with_name("peripheral_phase_results.json")
    destination.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"generic_phase_passed": True, "entire_angle_spaces_checked": len(records),
                      "max_pointwise_relative_error": max(r["pointwise_relative_error"] for r in numeric),
                      "results": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
