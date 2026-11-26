#!/usr/bin/env python3
"""Check the exact Gaussian-window formulas for the full Newton crossing.

The matrix is built from the defining sine-factorial entries, independently
of the Pochhammer feature formula. These are finite identity diagnostics;
they do not certify an asymptotic or a geometric source coefficient.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=65)
    parser.add_argument("--max-level", type=int, default=10)
    parser.add_argument(
        "--output",
        default="repro/results/research-gaussian-frame-newton-transport.json",
    )
    args = parser.parse_args()
    if args.dps < 50 or args.max_level < 3:
        parser.error("Use at least 50 digits and include both level parities.")
    mp.mp.dps = args.dps
    tolerance = mp.mpf(10) ** (-(args.dps - 8))
    worst = mp.mpf(0)
    counts = {"positive_crossing": 0, "negative_crossing": 0, "turn": 0}

    def check(label, actual, expected):
        nonlocal worst
        error = abs(actual - expected) / max(1, abs(actual), abs(expected))
        worst = max(worst, error)
        counts[label] += 1
        if error >= tolerance:
            raise AssertionError(f"{label}: relative error {error}")

    sigma = mp.mpf("0.7")
    centers = [mp.mpf("-.2"), mp.mpf(".31"), mp.mpf("1.1")]
    parameters = [mp.exp(mp.mpf(".4") * 1j), mp.mpc(".8", ".2")]
    for N in range(2, args.max_level + 1):
        D = N - 1
        q = mp.exp(mp.pi * 1j / N)
        Q = q * q
        kappa = mp.exp(mp.pi * 1j * D * D / (2 * N))
        factorials = [mp.mpf(1)]
        for j in range(1, N):
            factorials.append(factorials[-1] * 2 * mp.sin(mp.pi * j / N))
        matrix = mp.matrix(N)
        for j in range(N):
            for k in range(j + 1):
                matrix[j, k] = (
                    kappa * (-1) ** j * q ** (j * (k + 1))
                    * factorials[j] / (factorials[k] * factorials[j - k])
                )

        for xi in centers:
            for z in parameters:
                c = (N / (mp.pi * sigma)) ** mp.mpf(".25")
                window = mp.matrix([
                    c * mp.exp(-(k - N * xi) ** 2 / (2 * sigma * N))
                    * (z / q) ** k
                    for k in range(N)
                ])
                for sign in (1, -1):
                    base = Q ** sign
                    parameter = z if sign == 1 else z / Q
                    polynomial = [mp.mpc(1)]
                    expected = []
                    for j in range(N):
                        heated = sum(
                            polynomial[k] * parameter ** k
                            * mp.exp(-(k - N * xi) ** 2 / (2 * sigma * N))
                            for k in range(j + 1)
                        )
                        expected.append(
                            c * kappa ** sign * (-q ** sign) ** j * heated
                        )
                        polynomial = (
                            [polynomial[0]]
                            + [
                                polynomial[k] + base ** j * polynomial[k - 1]
                                for k in range(1, len(polynomial))
                            ]
                            + [base ** j * polynomial[-1]]
                        )
                    operator = matrix if sign == 1 else matrix.conjugate()
                    actual = operator * window
                    label = "positive_crossing" if sign == 1 else "negative_crossing"
                    for j in range(N):
                        check(label, actual[j], expected[j])

                reflected_center = mp.mpf(D) / N - xi
                reflected_parameter = Q / z
                for k in range(N):
                    expected = (
                        (z / q) ** D * c
                        * mp.exp(-(k - N * reflected_center) ** 2 / (2 * sigma * N))
                        * (reflected_parameter / q) ** k
                    )
                    check("turn", window[D - k], expected)

    script = Path(__file__).resolve()
    result = {
        "passed": True,
        "script": str(script.relative_to(script.parents[1])),
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "precision_digits": args.dps,
        "levels": [2, args.max_level],
        "diagnostics": sum(counts.values()),
        "counts": counts,
        "worst_relative_error": mp.nstr(worst, 16),
        "tolerance": mp.nstr(tolerance, 8),
        "matrix_construction": "Original defining sine-factorial entries; negative crossing is their conjugate.",
        "feature_construction": "Independent finite Pochhammer coefficient multiplication followed by Gaussian monomial multipliers.",
        "scope": "Exact finite crossing and turn identities only; no asymptotic or source-survival claim.",
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
