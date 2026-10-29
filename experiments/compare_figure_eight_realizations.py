#!/usr/bin/env python3
"""Compare independently integrated two- and three-tetrahedron fiber states.

The exact phase being checked is not used inside either quadrature. Phi is
evaluated through the independently derived real-b remainder and exact shifts.
The real linear quadrature change resolves the complex Gaussian without a
complex contour rotation.
"""

import json
from pathlib import Path

import numpy as np
from scipy.special import roots_hermite

from check_literature_state_volume import Remainder, VOLUME


def log_phi_on_fiber(b, y, remainder):
    Q = b + 1 / b
    Z = Q * np.asarray(y, dtype=complex) / (2 * np.pi)
    # Each horizontal fiber coordinate has one constant imaginary part.
    shift = int(np.floor(float(Z.imag[0]) / b + 0.5))
    assert np.max(np.abs(Z.imag - Z.imag[0])) < 1e-12
    base = Z - 1j * b * shift
    value = np.empty_like(Z)
    for start in range(0, len(Z), 1024):
        block = base[start:start + 1024]
        value[start:start + 1024] = remainder.log_phi_scaled(2 * np.pi * b * block)
    if shift > 0:
        for j in range(1, shift + 1):
            at = base + 1j * b * j
            value -= np.log(1 + np.exp(-1j * np.pi * b**2 + 2 * np.pi * b * at))
    elif shift < 0:
        for j in range(-shift):
            at = base - 1j * b * j
            value += np.log(1 + np.exp(-1j * np.pi * b**2 + 2 * np.pi * b * at))
    return value


def normalized_state(b, x, order, three):
    """Return exp(Vol/(2*pi*h)) times the literal printed fiber integral."""
    h = (b + 1 / b)**(-2)
    nodes, weights = roots_hermite(order)
    if three:
        real_hessian = np.diag([np.sqrt(3), np.sqrt(3) / 2])
        imag_hessian = np.array([[4.0, 1.0], [1.0, -0.5]])
        whitening = np.diag(1 / np.sqrt(np.diag(real_hessian)))
        eigenvalues, eigenvectors = np.linalg.eigh(whitening @ imag_hessian @ whitening)
        radii = np.sqrt(1 + eigenvalues**2)
        transform = np.sqrt(4 * np.pi) * whitening @ eigenvectors @ np.diag(1 / np.sqrt(radii))
        n1, n2 = np.meshgrid(nodes, nodes, indexing="ij")
        w1, w2 = np.meshgrid(weights, weights, indexing="ij")
        coordinates = np.array([n1.ravel(), n2.ravel()])
        offset = np.sqrt(h) * transform @ coordinates
        v = np.log(3) / 2 + 5j * np.pi / 6 + offset[0]
        w = -np.log(3) / 2 + 5j * np.pi / 6 + offset[1]
        y = np.array([v - x, v, w])
        H = np.array([[0.5, 0.5, 1], [0.5, -1, -0.5], [1, -0.5, 0]])
        c = np.pi * np.array([4, -1, 1])
        log_weights = np.log(w1.ravel()) + np.log(w2.ravel())
        compensation = np.sum(coordinates**2, axis=0)
        prefactor = -abs(np.linalg.det(transform)) / ((2 * np.pi)**3 * np.sqrt(h))
    else:
        rate = np.sqrt(3) / (4 * np.pi)
        v = 2j * np.pi / 3 + np.sqrt(h) * nodes / np.sqrt(rate)
        y = np.array([v - x, v])
        H, c = np.diag([0.5, -1.0]), np.pi * np.array([1, -1])
        log_weights, compensation = np.log(weights), nodes**2
        prefactor = 1 / ((2 * np.pi)**2 * np.sqrt(h) * np.sqrt(rate))
    exponent = (1j * np.einsum("ik,ij,jk->k", y, H, y) + c @ y + VOLUME) / (2 * np.pi * h)
    remainder = Remainder(b)
    for row in y:
        exponent += log_phi_on_fiber(b, row, remainder)
    return prefactor * np.sum(np.exp(log_weights + compensation + exponent))


def main():
    records = []
    for b in [0.25, 0.18]:
        h = (b + 1 / b)**(-2)
        expected = -np.exp(-np.pi * 1j / 12 + 11 * np.pi * 1j / (12 * h))
        for x in [0, 0.12 + 0.03j]:
            ratios = [normalized_state(b, x, order, True) / normalized_state(b, -x, order, False)
                      for order in [256, 384]]
            error, refinement = abs(ratios[-1] / expected - 1), abs(ratios[-1] - ratios[0])
            assert error < 2e-8 and refinement < 2e-8
            even_error = abs(normalized_state(b, x, 384, False) / normalized_state(b, -x, 384, False) - 1)
            assert even_error < 2e-10
            records.append({"b": b, "x": str(x), "relative_error": float(error),
                            "quadrature_refinement_difference": float(refinement),
                            "two_tetrahedron_evenness_error": float(even_error)})
    destination = Path(__file__).with_name("figure_eight_state_comparison_results.json")
    destination.write_text(json.dumps({
        "scope": "Numerical checks of independently integrated selected states; not a proof of the move law.",
        "identity": "J3(h,x)=-exp(-pi*i/12+11*pi*i/(12*h))*J2(h,-x)",
        "orders": [256, 384], "records": records}, indent=2) + "\n")
    print(json.dumps({"cases": len(records), "max_relative_error": max(r["relative_error"] for r in records),
                      "max_refinement_difference": max(r["quadrature_refinement_difference"] for r in records),
                      "results": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
