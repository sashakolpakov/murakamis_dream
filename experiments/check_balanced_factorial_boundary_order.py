#!/usr/bin/env python3
"""Diagnostics for the signed-slope boundary-order theorem.

The translation multiplier is computed independently by iterating the
original sine recurrence. The second check uses the unsimplified finite
factorial formula. These are numerical diagnostics, not interval proofs.
"""

import argparse
import json
from pathlib import Path

import mpmath as mp

from check_exact_cyclotomic_factorial import exact_log


def factorial_log(n, z):
    if z.imag < 0:
        return exact_log(n, z)
    return mp.conj(exact_log(n, mp.conj(z)))


def recurrence_ratio(n, z, shift):
    if shift > 0:
        return mp.fprod(2 * mp.sin(mp.pi * (z + r) / n)
                        for r in range(1, shift + 1))
    return 1 / mp.fprod(2 * mp.sin(mp.pi * (z - r) / n)
                       for r in range(-shift))


def one_case(n, order):
    x = mp.mpc("0.23", "-0.81")
    y = mp.mpc("0.19", "0.12")
    shifts = (y, mp.mpf(1) / 2 - mp.mpf(1) / (2 * n) - y,
              -y / 2, mp.mpc(mp.mpf(1) / 3, mp.mpf(1) / 7))
    slopes, powers = (2, -1, 1, -3), (1, -2, -1, 1)
    factors = list(zip(slopes, powers, shifts))
    degree = -1
    quadratic = -sum(v * a * abs(a) for a, v, b in factors)
    linear = (
        n + degree - order
        - mp.mpf(n) / 2 * mp.fsum(v * abs(a) * b for a, v, b in factors)
        + mp.mpf(n - 1) / 4 * sum(v * abs(a) for a, v, b in factors)
    )
    w, Q = mp.exp(-2j * mp.pi * x), mp.exp(2j * mp.pi / n)
    actual_multiplier = mp.exp(
        1j * mp.pi * n * quadratic * (2 * x + 1) / 2
        + 2j * mp.pi * linear)
    for a, v, b in factors:
        actual_multiplier *= recurrence_ratio(n, n * (a * x + b), n * a) ** v

    logarithm, phi, log_coefficient = mp.mpc(0), mp.mpc(0), mp.mpc(0)
    for a, v, b in factors:
        sign = 1 if a > 0 else -1
        zeta = mp.exp(-2j * mp.pi * sign * b) * w ** abs(a)
        assert abs(zeta) < 1
        term = mp.log(1 - zeta**n)
        logarithm += v * a * term
        phi += v * (
            b * term
            - mp.fsum(mp.mpf(k) / n
                      * mp.log(1 - zeta * Q ** (sign * k))
                      for k in range(n))
            + 1j * sign * mp.polylog(2, zeta**n) / (2 * mp.pi * n))
        constant = (
            mp.log(n) / 2
            + 1j * mp.pi * sign
            * (mp.mpf(n) / 12 - mp.mpf(1) / 4 + mp.mpf(1) / (12 * n)))
        log_coefficient += v * (
            1j * mp.pi * sign * n * b**2 / 2
            - 1j * mp.pi * sign * (n - 1) * b / 2 + constant)

    raw_log = (
        degree * mp.log(w)
        + 1j * mp.pi * n * quadratic * x**2 / 2
        + 2j * mp.pi * linear * x
        + mp.fsum(v * factorial_log(n, n * (a * x + b))
                  for a, v, b in factors))
    normalized_log = raw_log + n * mp.log(w) - x * logarithm
    predicted_log = log_coefficient + order * mp.log(w) + phi
    translation_error = abs(actual_multiplier / mp.exp(logarithm) - 1)
    normalization_error = abs(mp.exp(normalized_log - predicted_log) - 1)
    return {
        "N": n,
        "order": order,
        "quadratic_balance": quadratic
            + sum(v * a * abs(a) for a, v, b in factors),
        "translation_relative_error": mp.nstr(translation_error, 30),
        "normalization_relative_error": mp.nstr(normalization_error, 30),
    }, max(translation_error, normalization_error)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1]
        / "repro/results/research-balanced-factorial-boundary-order.json")
    args = parser.parse_args()
    mp.mp.dps = args.dps
    tolerance = mp.mpf(10) ** (15 - args.dps)
    cases = []
    for n in (2, 3, 7, 11):
        for order in (-2, 0, 1, 3):
            row, error = one_case(n, order)
            assert error < tolerance, (row, tolerance)
            cases.append(row)
    result = {
        "status": "passed",
        "precision_decimal_digits": args.dps,
        "scope": (
            "Finite-precision diagnostics, not interval certificates. "
            "Both slope signs, slopes of magnitude greater than one, "
            "half-integer shifts, both level parities, and positive/zero/"
            "negative boundary orders are retained."),
        "cases": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Saved {len(cases)} signed-slope diagnostics to {args.output}.")


if __name__ == "__main__":
    main()
