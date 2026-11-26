#!/usr/bin/env python3
"""Check full physical jets and record off-grid cardinal/factorial errors.

The original Newton products and cardinal sum are evaluated directly.
The factorial expression uses the independently proved finite
cyclotomic formula. These are numerical diagnostics, not a proof of
the uniform exponential projection estimate.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_exact_cyclotomic_factorial import exact_log, finite_derivative


def factorial_log(level, value):
    if mp.im(value) < 0:
        return exact_log(level, value)
    return mp.conj(exact_log(level, mp.conj(value)))


def factorial_jet(level, index, angle):
    top = level - 1
    plus = mp.mpf(top) / 2 - level * index + level * angle / (2 * mp.pi)
    minus = mp.mpf(top) / 2 - level * index - level * angle / (2 * mp.pi)
    value = mp.exp(
        mp.log(level) - factorial_log(level, plus)
        - factorial_log(level, minus) - 2 * factorial_log(level, level * index)
    )
    derivative = (
        -level / (2 * mp.pi) * value
        * (finite_derivative(level, plus) - finite_derivative(level, minus))
    )
    return value, derivative


def original_cardinal_jet(level, index, angle):
    value = mp.mpc(1)
    derivative = mp.mpc(0)
    result = mp.mpc(0)
    result_derivative = mp.mpc(0)
    for j in range(level):
        distance = index - mp.mpf(j) / level
        cardinal = mp.sin(mp.pi * level * distance) / (
            level * mp.sin(mp.pi * distance)
        )
        result += cardinal * value
        result_derivative += cardinal * derivative
        if j + 1 < level:
            denominator = 4 * mp.sin(mp.pi * (j + 1) / level) ** 2
            ratio = (
                2 * mp.cos(mp.pi * (2 * j + 1) / level)
                + 2 * mp.cos(angle)
            ) / denominator
            derivative = (
                ratio * derivative - 2 * mp.sin(angle) * value / denominator
            )
            value *= ratio
    return result, result_derivative


def number(value):
    return mp.nstr(value, 40)


def complex_number(value):
    return {"real": number(mp.re(value)), "imaginary": number(mp.im(value))}


def relative_difference(left, right):
    return abs(left - right) / max(1, abs(left), abs(right))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1]
        / "repro/results/research-free-boundary-cardinal-factorial.json",
    )
    args = parser.parse_args()
    mp.mp.dps = args.dps
    tolerance = mp.power(10, -args.dps // 2)
    indices = (mp.mpc(".27", ".07"), mp.mpc(".39", "-.05"))
    exact_rows = []
    for level in range(2, 10):
        for index in indices:
            # Only distinct roots are needed; the odd last root is simple.
            for j in range((level - 1) // 2 + 1):
                angle = mp.pi * (level - 1 - 2 * j) / level
                original = original_cardinal_jet(level, index, angle)
                continued = factorial_jet(level, index, angle)
                value_error = relative_difference(original[0], continued[0])
                double_root = (level - 1 - 2 * j) != 0
                normal_error = None
                if double_root:
                    # The angular derivative divided by 2 sin(angle)
                    # is the actual first normal in the spectral variable.
                    divisor = 2 * mp.sin(angle)
                    normal_error = relative_difference(
                        original[1] / divisor, continued[1] / divisor
                    )
                worst = max(value_error, normal_error or mp.mpf(0))
                if worst > tolerance:
                    raise ArithmeticError((level, index, j, worst))
                exact_rows.append({
                    "N": level, "index": complex_number(index),
                    "physical_node": j, "double_root": double_root,
                    "value_relative_error": number(value_error),
                    "normal_relative_error":
                        number(normal_error) if double_root else None,
                })
        print(f"Full physical jets checked at N={level}.", flush=True)

    off_grid = []
    for level in (16, 17, 32, 33, 64, 65):
        for index in indices:
            for angle in (mp.mpf(0), mp.mpc(".08", ".03")):
                original = original_cardinal_jet(level, index, angle)
                continued = factorial_jet(level, index, angle)
                ratio_error = original[0] / continued[0] - 1
                # Dividing the derivative defect by the nonzero value
                # avoids a spurious division by the derivative at zero.
                derivative_error = (original[1] - continued[1]) / continued[0]
                off_grid.append({
                    "N": level, "index": complex_number(index),
                    "boundary_angle": complex_number(angle),
                    "cardinal_over_factorial_minus_one": complex_number(ratio_error),
                    "absolute_relative_error": number(abs(ratio_error)),
                    "log_relative_error_over_N":
                        number(mp.log(abs(ratio_error)) / level),
                    "derivative_defect_over_factorial": complex_number(derivative_error),
                })
        print(f"Off-grid errors recorded at N={level}.", flush=True)

    source = Path(__file__).resolve()
    dependency = source.parent / "check_exact_cyclotomic_factorial.py"
    result = {
        "status": "passed",
        "precision_decimal_digits": args.dps,
        "scope": (
            "Full distinct-root values and all required first spectral normals "
            "are checked against direct original Newton products. Off-grid "
            "finite-level errors are diagnostics, not interval certificates or "
            "proofs of an exponential asymptotic."
        ),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "factorial_dependency_sha256":
            hashlib.sha256(dependency.read_bytes()).hexdigest(),
        "physical_jet_cases": exact_rows,
        "off_grid_diagnostics": off_grid,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Saved {len(exact_rows)} jet checks and {len(off_grid)} diagnostics "
          f"to {args.output}.")


if __name__ == "__main__":
    main()
