#!/usr/bin/env python3
"""Finite-precision diagnostics for the exact canonical factorial formula.

The defining gamma product is evaluated independently of the finite
dilogarithm formula. Its truncation errors are recorded, not treated as
certified enclosures. The mathematical proof is in
notes/research_exact_cyclotomic_factorial.md.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def primitive(t):
    w = mp.exp(-2 * mp.pi * 1j * t)
    return (
        1j * mp.pi * t**2 / 2
        + t * mp.log(1 - w)
        + 1j * mp.polylog(2, w) / (2 * mp.pi)
    )


def exact_log(n, z):
    x = z / n
    return mp.log(n) / 2 - 1j * mp.pi * n / 12 + mp.fsum(
        primitive(x - mp.mpf(k) / n) for k in range(n)
    )


def finite_derivative(n, z):
    return mp.pi / n**2 * mp.fsum(
        (z - k) * mp.cot(mp.pi * (z - k) / n) for k in range(n)
    )


def disk_remainder(n, x):
    w = mp.exp(-2 * mp.pi * 1j * x)
    return (
        x * mp.log(1 - w**n)
        - mp.fsum(
            mp.mpf(k) / n * mp.log(1 - w * mp.exp(2j * mp.pi * k / n))
            for k in range(n)
        )
        + 1j * mp.polylog(2, w**n) / (2 * mp.pi * n)
    )


def quadratic(n, x):
    return (
        1j * mp.pi * n * x**2 / 2
        - 1j * mp.pi * (n - 1) * x / 2
        + mp.log(n) / 2
        + 1j * mp.pi * (mp.mpf(n) / 12 - mp.mpf(1) / 4 + mp.mpf(1) / (12 * n))
    )


def remainder_bound(n, x):
    r = mp.exp(2 * mp.pi * x.imag)
    return (
        (abs(x) + 1 / (2 * mp.pi * n)) * r**n / (1 - r**n)
        + mp.mpf(n - 1) / 2 * r / (1 - r)
    )


def original_truncations(n, z, cutoffs):
    """Raw gamma products and digamma derivatives, with no finite-sum input."""
    value = z * mp.log(2 * mp.pi / n) + mp.loggamma(z + 1)
    derivative = mp.log(2 * mp.pi / n) + mp.digamma(z + 1)
    answer = []
    for m in range(1, max(cutoffs) + 1):
        value += (
            mp.loggamma(n * m + z + 1)
            - mp.loggamma(n * m - z)
            - (2 * z + 1) * mp.log(n * m)
        )
        derivative += (
            mp.digamma(n * m + z + 1)
            + mp.digamma(n * m - z)
            - 2 * mp.log(n * m)
        )
        if m in cutoffs:
            # Sum of the explicit m^(-2) term in the original product.
            tail = mp.polygamma(1, m + 1)
            corrected_value = value - z * (z + 1) * (2 * z + 1) / (6 * n**2) * tail
            corrected_derivative = derivative - (6 * z**2 + 6 * z + 1) / (6 * n**2) * tail
            answer.append((m, value, derivative, corrected_value, corrected_derivative))
    return answer


def number(value):
    return mp.nstr(value, 45)


def run(dps):
    mp.mp.dps = dps
    tol = mp.mpf(10) ** (-(dps - 15))
    rows = []
    for n in (2, 3, 7):
        z = mp.mpc("0.21", "-0.37")
        x = z / n
        value = exact_log(n, z)
        derivative = finite_derivative(n, z)
        residuals = {
            "derivative_of_primitive": abs(mp.diff(lambda zz: exact_log(n, zz), z) - derivative),
            "disk_expression": abs(value - quadratic(n, x) - disk_remainder(n, x)),
            "shift": abs(mp.exp(exact_log(n, z + 1) - value) - 2 * mp.sin(mp.pi * (z + 1) / n)),
            # The upper-half-plane value is given by conjugation of the
            # original gamma product, which has real coefficients.
            "reflection": abs(mp.exp(value + mp.conj(exact_log(n, n - 1 - mp.conj(z)))) - n),
        }
        for name, residual in residuals.items():
            assert residual < tol, (n, name, residual)

        boundary_height = mp.mpf(10) ** (-(dps // 2))
        lattice_errors = []
        sine_product = mp.mpf(1)
        for k in range(n):
            if k:
                sine_product *= 2 * mp.sin(mp.pi * k / n)
            lattice_errors.append(abs(mp.exp(exact_log(n, k - 1j * boundary_height)) - sine_product))
        assert max(lattice_errors) < mp.sqrt(boundary_height)

        product_rows = []
        previous_errors = None
        for cutoff, v, der, vc, dc in original_truncations(n, z, (64, 256, 1024)):
            errors = (
                abs(v - value), abs(der - derivative),
                abs(vc - value), abs(dc - derivative),
            )
            if previous_errors is not None:
                assert all(a < b / 3 for a, b in zip(errors, previous_errors))
            previous_errors = errors
            product_rows.append({
                "cutoff": cutoff,
                "log_product_error": number(errors[0]),
                "log_derivative_error": number(errors[1]),
                "corrected_log_product_error": number(errors[2]),
                "corrected_log_derivative_error": number(errors[3]),
            })

        lower_rows = []
        for height in ("0.2", "1", "3"):
            xx = mp.mpc("0.23", "-" + height)
            err = abs(exact_log(n, n * xx) - quadratic(n, xx))
            bound = remainder_bound(n, xx)
            assert err < bound
            lower_rows.append({
                "imaginary_height": height,
                "exact_remainder_modulus": number(err),
                "explicit_bound": number(bound),
            })
        rows.append({
            "N": n,
            "z": {"real": "0.21", "imag": "-0.37"},
            "exact_formula_residuals": {k: number(v) for k, v in residuals.items()},
            "maximum_lattice_boundary_error": number(max(lattice_errors)),
            "gamma_product_truncations": product_rows,
            "lower_end_remainder_checks": lower_rows,
        })
    return {
        "description": "Numerical diagnostics for the proved exact factorial identity; not interval certificates.",
        "precision_decimal_digits": dps,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.dps)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        print(f"Saved {len(result['cases'])} factorial diagnostics to {args.output}.")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
