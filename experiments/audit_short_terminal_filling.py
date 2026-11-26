#!/usr/bin/env python3
"""Check exact terminal identities and sample their proved asymptotic.

The exact checks compare Newton polynomials with the original crossing
eigenvalues and first normal derivatives. The asymptotic samples are
diagnostics, not a substitute for the contour proof in
notes/research_two_crossing_terminal_filling.md.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp


def root_data(level):
    q = mp.exp(mp.j * mp.pi / level)
    d = level - 1
    kappa = mp.exp(mp.j * mp.pi * d * d / (2 * level))
    sine = [mp.mpf(1)]
    for k in range(1, level):
        sine.append(sine[-1] * 2 * mp.sin(mp.pi * k / level))
    nodes = [2 * mp.cos((2 * j + 1) * mp.pi / level) for j in range(level)]
    return q, kappa, sine, nodes


def evaluate_newton(coefficients, argument, level, nodes):
    value = mp.mpc(0)
    derivative = mp.mpc(0)
    basis = mp.mpc(1)
    basis_derivative = mp.mpc(0)
    for k, coefficient in enumerate(coefficients):
        value += coefficient * basis
        derivative += coefficient * basis_derivative
        if k + 1 < level:
            denominator = (2 * mp.sin(mp.pi * (k + 1) / level)) ** 2
            basis_derivative = ((nodes[k] - argument) * basis_derivative - basis) / denominator
            basis *= (nodes[k] - argument) / denominator
    return value, derivative


def terminal_two(level, parent):
    """Evaluate the complete sum through its exact consecutive-term ratio."""
    q = mp.exp(mp.j * mp.pi / level)
    term = mp.mpc(level)
    value = term
    for k in range(level - 1):
        numerator = 2 * mp.cos((2 * k + 1) * mp.pi / level) + 2 * mp.cos(parent)
        term *= mp.j * q**k * numerator / (2 * mp.sin((k + 1) * mp.pi / level)) ** 3
        value += term
    return value


def selected_action(parent):
    integral = parent * mp.quad(lambda t: mp.asinh(mp.tan(parent * t / 2)), [0, 1])
    return 2 * mp.catalan / mp.pi - integral / (2 * mp.pi) + mp.j * mp.pi / 8 - mp.j * parent**2 / (8 * mp.pi)


def selected_amplitude(parent):
    return mp.exp(-mp.j * mp.pi / 4) / (2 * mp.sqrt(mp.cos(parent / 2)))


def complex_record(value):
    return {"real": mp.nstr(mp.re(value), 32), "imaginary": mp.nstr(mp.im(value), 32)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--max-level", type=int, default=20)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.precision < 70 or args.max_level < 3:
        parser.error("use at least 70 digits and a maximum level of at least 3")
    mp.mp.dps = args.precision
    comparisons = 0
    largest_relative_error = mp.mpf(0)

    for level in range(3, args.max_level + 1):
        q, kappa, sine, nodes = root_data(level)
        d = level - 1
        h_two = [level * mp.j**k * mp.exp(mp.j * mp.pi * k * (k - 1) / (2 * level)) / sine[k]
                 for k in range(level)]
        # Turning H_2 back must recover R^2, including its first normals.
        r_two = list(reversed(h_two))
        h_one = list(reversed([kappa * (-q)**k for k in range(level)]))
        for j in range((level + 1) // 2):
            eigenvalue = kappa * (-1)**j * q**(j * (j + 1))
            simple = level % 2 == 1 and j == d // 2
            relative_normal = None if simple else -(d - 2 * j) / (2 * (q**(2 * j + 1) - q**(-2 * j - 1)))
            for coefficients, power in ((r_two, 2), (h_one, -1)):
                actual, actual_derivative = evaluate_newton(coefficients, nodes[j], level, nodes)
                expected = eigenvalue**power
                error = abs(actual - expected) / max(1, abs(expected))
                largest_relative_error = max(largest_relative_error, error)
                comparisons += 1
                if not simple:
                    expected_derivative = power * expected * relative_normal
                    error = abs(actual_derivative - expected_derivative) / max(1, abs(expected_derivative))
                    largest_relative_error = max(largest_relative_error, error)
                    comparisons += 1

    tolerance = mp.power(10, -args.precision + 25)
    if largest_relative_error >= tolerance:
        raise AssertionError(f"exact identity residual {largest_relative_error} exceeds {tolerance}")

    samples = []
    for parent in (mp.mpc(0), mp.mpc("0.05"), mp.mpc(0, "0.05"), mp.mpc("0.05", "0.03")):
        action = selected_action(parent)
        amplitude = selected_amplitude(parent)
        for level in (20, 21, 40, 41, 80, 81, 160, 161, 320, 321):
            ratio = terminal_two(level, parent) / (amplitude * mp.exp(level * action))
            samples.append({"level": level, "parent": complex_record(parent),
                            "normalized_value": complex_record(ratio),
                            "level_times_relative_error": complex_record(level * (ratio - 1))})

    result = {
        "scope": "Exact finite identities and numerical diagnostics for the two-crossing terminal polynomial; no general volume theorem is tested.",
        "precision_digits": args.precision,
        "exact_checks": {"first_level": 3, "last_level": args.max_level,
                         "comparisons": comparisons,
                         "largest_relative_error": mp.nstr(largest_relative_error, 12),
                         "tolerance": mp.nstr(tolerance, 12)},
        "asymptotic_samples": samples,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Exact identities: {comparisons} value/normal comparisons; maximum relative error {mp.nstr(largest_relative_error, 6)}.")
    print(f"Recorded {len(samples)} complete-sum asymptotic samples at real and complex parent values.")
    if args.output:
        print(f"Results: {args.output}")


if __name__ == "__main__":
    main()
