#!/usr/bin/env python3
"""Numerically check an independently derived Faddeev remainder and AK state.

These are numerical diagnostics for the proofs in literature_state_volume.md,
not a replacement for bounds or contour arguments. The quantum dilogarithm is
evaluated through the convergent remainder integral derived from its defining
integral. No published asymptotic formula is an input.
"""

import json
from pathlib import Path

import numpy as np
from scipy.special import roots_hermite, roots_legendre, spence

PI = np.pi
ETA = 2 * PI / 3
VOLUME = 2 * spence(1 - np.exp(1j * PI / 3)).imag


def dilog_minus_exp(z):
    return spence(1 + np.exp(np.asarray(z, dtype=complex)))


class Remainder:
    def __init__(self, b, order=800, cutoff=80.0):
        self.b = b
        nodes, weights = roots_legendre(order)
        self.t = (nodes + 1) * cutoff / 2
        weights = weights * cutoff / 2
        v = b**2 * self.t
        small = np.abs(v) < 0.03
        difference = np.empty_like(v)
        vs = v[small]
        difference[small] = (
            -vs / 6 + 7 * vs**3 / 360 - 31 * vs**5 / 15120
            + 127 * vs**7 / 604800 - 73 * vs**9 / 3421440
        )
        difference[~small] = 1 / np.sinh(v[~small]) - 1 / v[~small]
        self.residue = -b**2 / 24
        kernel = difference / (4 * self.t * np.sinh(self.t))
        regular_kernel = kernel - self.residue * np.exp(-self.t) / self.t
        self.weighted_kernel = weights * regular_kernel

    def sine_integral(self, z):
        z = np.asarray(z, dtype=complex)
        return np.sin(z[..., None] * self.t / PI) @ self.weighted_kernel + self.residue * np.arctan(z / PI)

    def __call__(self, z):
        return -2j * self.sine_integral(z) - 1j * PI * self.residue

    def log_phi_scaled(self, z):
        return dilog_minus_exp(z) / (2j * PI * self.b**2) + self(z)


def normalized_state(b, order, X=0):
    """Return J_b(X/(2*pi*b)) exp(V/(2*pi*b^2))."""
    nodes, weights = roots_hermite(order)
    gaussian_rate = np.sqrt(3) / (4 * PI)
    u = b * nodes / np.sqrt(gaussian_rate) - 1j * ETA
    phase = (dilog_minus_exp(X - u) - dilog_minus_exp(u) - X * (2 * u - X)) / 1j
    remainder = Remainder(b)
    quantum_correction = remainder(X - u) - remainder(u)
    exponent = (phase + VOLUME) / (2 * PI * b**2) + nodes**2 + quantum_correction
    summands = np.exp(np.log(weights) + exponent)
    return np.exp(-(1 + b**(-2)) * X) * np.sum(summands) / (2 * PI * np.sqrt(gaussian_rate))


def main():
    probes = np.array([x + 1j * y for x in [-8, -2, 0, 2, 8] for y in [-ETA, 0, ETA]])
    diagnostics = []
    volume_checks = []
    operator_checks = []
    for b in [0.5, 0.35, 0.25, 0.18, 0.12]:
        remainder = Remainder(b)
        center_exact = 1j * PI * b**2 / 24
        assert abs(remainder(0) - center_exact) < 1e-13
        functional_residuals = []
        for z in [-2 + 0.4j, 0, 1 - 0.3j]:
            delta = remainder.log_phi_scaled(z - 1j * PI * b**2) - remainder.log_phi_scaled(z + 1j * PI * b**2)
            functional_residuals.append(abs(np.exp(delta) / (1 + np.exp(z)) - 1))
        max_residual = max(functional_residuals)
        assert max_residual < 2e-10
        diagnostics.append({
            "b": b,
            "sampled_max_abs_R_over_b_squared": float(np.max(np.abs(remainder(probes))) / b**2),
            "max_functional_equation_relative_residual": float(max_residual),
        })
        z128 = normalized_state(b, 128)
        z256 = normalized_state(b, 256)
        assert abs(z128 - z256) < 2e-9
        assert abs(z256.imag) < 1e-10
        effective_volume = VOLUME - 2 * PI * b**2 * np.log(abs(z256))
        volume_checks.append({
            "b": b,
            "normalized_state_real": float(z256.real),
            "normalized_state_imaginary": float(z256.imag),
            "quadrature_order_difference": float(abs(z128 - z256)),
            "minus_2pi_b_squared_log_abs_state": float(effective_volume),
        })
    for b in [0.18, 0.12]:
        q = np.exp(2j * PI * b**2)
        for X in [0.04, 0.03 + 0.02j]:
            Q = np.exp(-X)
            R = q**4 * Q**4 - q**3 * Q**3 - q * (q**2 + 1) * Q**2 - q * Q + 1
            coefficients = [
                q**2 * Q**2 * (q**3 * Q**2 - 1),
                -(q**2 * Q**2 - 1) * R,
                q**2 * Q**2 * (q * Q**2 - 1),
            ]
            values = [normalized_state(b, 256, X - 2j * PI * b**2 * j) for j in range(3)]
            terms = np.array(coefficients) * values
            relative_residual = abs(np.sum(terms)) / np.sum(np.abs(terms))
            assert relative_residual < 2e-9
            operator_checks.append({
                "b": b,
                "X": str(X),
                "Q": str(Q),
                "relative_annihilator_residual": float(relative_residual),
            })
    result = {
        "literature_state": "Andersen--Kashaev arXiv:1109.6295v2 equation (38), x=0",
        "target_volume": float(VOLUME),
        "predicted_normalized_state_limit": float(3**(-0.25)),
        "remainder_diagnostics": diagnostics,
        "state_volume_diagnostics": volume_checks,
        "generic_peripheral_operator_diagnostics": operator_checks,
        "scope": "Numerical checks only; the uniform strip bound and saddle proof are in the companion note.",
    }
    Path(__file__).with_name("literature_state_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
