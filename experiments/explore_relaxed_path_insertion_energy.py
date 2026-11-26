#!/usr/bin/env python3
"""Exploratory relaxed insertion energies; not an interval certificate.

Solve the original positive filling equations at their unit endpoints.
Evaluate the convex square energy by two independent Gauss quadratures.
Only converged solutions with positive original edge matrices are retained.
"""

import argparse
from functools import lru_cache
import json
from pathlib import Path

import numpy as np
from scipy.optimize import root
from scipy.special import roots_legendre


PI = np.pi


def _equations(t, powers, charges=None):
    extended = np.r_[0j, t, 0j]
    tangent = np.tan(extended / 2)
    returns = np.arcsinh(tangent[1:-1] * np.cos(extended[:-2] / 2))
    returns += np.arcsinh(tangent[1:-1] * np.cos(extended[2:] / 2))
    if charges is None:
        charges = np.ones(len(t))
    return returns - 0.5j * np.asarray(powers) * t + 1j * PI * charges


def _jacobian(t, powers):
    extended = np.r_[0j, t, 0j]
    tangent = np.tan(extended / 2)
    q = np.sqrt(1 + tangent[:-1] ** 2 + tangent[1:] ** 2)
    diagonal = (1 + tangent[1:-1] ** 2) * (1 / q[:-1] + 1 / q[1:]) / 2
    diagonal -= 0.5j * np.asarray(powers)
    cross = -tangent[1:-2] * tangent[2:-1] / (2 * q[1:-1])
    return np.diag(diagonal) + np.diag(cross, 1) + np.diag(cross, -1)


def solve(powers, charges=None, initial=None):
    powers = np.asarray(powers, dtype=float)
    if not len(powers):
        return np.empty(0, dtype=complex), 0.0, 1.0
    if initial is None:
        initial = (2 * PI / powers) / (1 + 2j / powers)

    def fun(raw):
        n = len(powers)
        values = _equations(raw[:n] + 1j * raw[n:], powers, charges)
        return np.r_[values.real, values.imag]

    def jac(raw):
        n = len(powers)
        j = _jacobian(raw[:n] + 1j * raw[n:], powers)
        return np.block([[j.real, -j.imag], [j.imag, j.real]])

    result = root(fun, np.r_[initial.real, initial.imag], jac=jac,
                  method="hybr", options={"xtol": 1e-11})
    n = len(powers)
    t = result.x[:n] + 1j * result.x[n:]
    residual = float(np.max(np.abs(_equations(t, powers, charges))))
    extended = np.r_[0j, t, 0j]
    tangent = np.tan(extended / 2)
    q = np.sqrt(1 + tangent[:-1] ** 2 + tangent[1:] ** 2)
    margin = np.min(q.real - np.hypot(tangent[:-1].real, tangent[1:].real))
    assert residual < 1e-9, (powers.tolist(), result.message, residual)
    assert np.min(t.real) > 0 and np.max(t.real) < PI
    assert np.max(t.imag) < 0 and np.min(t.imag) > -23 / 20
    assert margin > 0, (powers.tolist(), margin)
    return t, residual, float(margin)


@lru_cache(maxsize=None)
def quadrature(order):
    nodes, weights = roots_legendre(order)
    return (nodes + 1) / 2, weights / 2


def square_energy(a, y, order):
    # Evenness allows every integral to be taken in the positive quadrant.
    a, y = np.abs(a), np.abs(y)
    nodes, weights = quadrature(order)
    first = np.sum(weights * np.arcsinh(np.tan(2 * a * nodes))) * a / 2
    second = np.sum(weights * np.arcsinh(np.tan(2 * y * nodes)
                                         * np.cos(2 * a))) * y / 2
    return first + second


@lru_cache(maxsize=None)
def minimum(powers):
    if not powers:
        return {"energy": 0.0, "residual": 0.0, "quadrature_error": 0.0,
                "positive_margin": 1.0}
    t, residual, margin = solve(powers)
    t = np.r_[0j, t, 0j]
    energy = []
    for order in (64, 128):
        value = 0.0
        for v, w in zip(t[:-1], t[1:]):
            gv = np.arcsinh(np.tan(v / 2) * np.cos(w / 2)).imag
            gw = np.arcsinh(np.tan(w / 2) * np.cos(v / 2)).imag
            a, b = v.real / 4, w.real / 4
            value += 4 * square_energy(a - gw / 2, gv / 2 + b, order)
            value += 4 * square_energy(a + gw / 2, gv / 2 - b, order)
        energy.append(float(value))
    return {"energy": energy[-1], "residual": residual,
            "quadrature_error": abs(energy[1] - energy[0]),
            "positive_margin": margin}


def insertion(left, right):
    left, right = tuple(left), tuple(right)
    full = minimum(left + (3, 3) + right)
    first, second = minimum(left), minimum(right)
    return {"left": left, "right": right,
            "cost": full["energy"] - first["energy"] - second["energy"],
            "maximum_residual": max(x["residual"] for x in (full, first, second)),
            "maximum_quadrature_difference": max(
                x["quadrature_error"] for x in (full, first, second)),
            "minimum_positive_margin": min(
                x["positive_margin"] for x in (full, first, second))}


def pair_activation_profile(half_length):
    """Sample a continued positive branch; this does not prove its existence."""
    old = solve((3,) * half_length)[0]
    t = np.r_[old, 0j, 0j, old]
    powers = (3,) * len(t)
    maximum = {"charge": 0.0, "height_over_charge": 0.0}
    residual, margin = 0.0, 1.0
    for charge in np.linspace(0.01, 1, 100):
        charges = np.ones(len(t))
        charges[half_length:half_length + 2] = charge
        t, error, positivity = solve(powers, charges, t)
        ratio = float(np.max(-t[half_length:half_length + 2].imag) / charge)
        residual, margin = max(residual, error), min(margin, positivity)
        if ratio > maximum["height_over_charge"]:
            maximum = {"charge": float(charge), "height_over_charge": ratio}
    return {"half_length": half_length, "maximum_observed_ratio": maximum,
            "maximum_residual": residual, "minimum_positive_margin": margin}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1]
                        / "repro/results/exploratory-relaxed-path-insertion-energy.json")
    args = parser.parse_args()
    records = []
    for length in (0, 1, 2, 4, 8, 16, 32):
        records.append(insertion([3] * length, [3] * length))
    # Fixed representative environments; this is not an exhaustive search.
    for old_power in (4, 5, 8, 64):
        records.append(insertion([old_power] * 8, [old_power] * 8))
        records.append(insertion([3, old_power] * 4, [old_power, 3] * 4))
        records.append(insertion([old_power, 3] * 4, [3, old_power] * 4))
    for left_power, right_power in ((3, 4), (3, 8), (3, 64), (4, 8)):
        records.append(insertion([left_power] * 8, [right_power] * 8))

    profiles = [pair_activation_profile(m) for m in (0, 1, 4, 16)]
    result = {"status": "exploratory, not a proof",
              "scope": "fully relaxed unit endpoints and sampled simultaneous-pair activation",
              "records": records,
              "pair_activation_profiles": profiles,
              "largest_observed_cost": max(x["cost"] for x in records),
              "largest_residual": max(x["maximum_residual"] for x in records),
              "largest_quadrature_difference": max(
                  x["maximum_quadrature_difference"] for x in records)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "records"}, indent=2))
    for record in records:
        print(len(record["left"]), len(record["right"]),
              record["left"][:4], record["right"][:4], record["cost"])


if __name__ == "__main__":
    main()
