#!/usr/bin/env python3
"""Check the entire Fourier realization of the actual coefficient equation.

Laurent-polynomial operators are applied without an alias projection or
truncation. Their band preservation is checked on every basis monomial.
The source is constructed separately from the original Newton matrices.
These finite checks do not establish an asymptotic connection coefficient.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def plus(*polynomials):
    result = {}
    for polynomial in polynomials:
        for k, value in polynomial.items():
            result[k] = result.get(k, mp.mpc(0)) + value
    return result


def times(a, b):
    result = {}
    for i, x in a.items():
        for j, y in b.items():
            result[i + j] = result.get(i + j, mp.mpc(0)) + x * y
    return result


def scale(p, factor):
    return {k: factor * value for k, value in p.items()}


def shift(p, factor):
    return {k: factor**k * value for k, value in p.items()}


def evaluate(p, X):
    return sum(value * X**k for k, value in p.items())


def norm(p):
    return max((abs(value) for value in p.values()), default=mp.mpf(0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--max-level", type=int, default=14)
    parser.add_argument(
        "--output",
        default="repro/results/research-complete-boundary-fourier-equation.json",
    )
    args = parser.parse_args()
    if args.dps < 70 or args.max_level < 4:
        parser.error("Use at least 70 digits and include both parities through level 4.")
    mp.mp.dps = args.dps
    tolerance = mp.mpf(10) ** (-(args.dps - 35))
    diagnostics = []

    def check(label, error, denominator, N):
        relative = abs(error) / (1 + denominator)
        diagnostics.append(
            {"level": N, "identity": label, "relative_error": mp.nstr(relative, 12)}
        )
        if relative >= tolerance:
            raise AssertionError(f"N={N}, {label}: relative error {relative}")

    for N in range(2, args.max_level + 1):
        D = N - 1
        eta = (-1) ** D
        q = mp.exp(mp.pi * 1j / N)
        Q = q * q
        kappa = mp.exp(mp.pi * 1j * D * D / (2 * N))
        c = {1: q, -1: q**-1}
        b = {1: 1, -1: 1, 0: -2}
        d = {0: -1, 1: 2, 2: -1}
        a = {1: 4 * q, 2: -q * (1 + Q)}

        def Zop(p):
            return plus(times(c, p), scale(times(b, shift(p, Q**-1)), -q**-1))

        def Bop(p):
            return plus(times(c, p), scale(times(shift(b, Q), shift(p, Q)), -q))

        def Lop(p):
            return plus(
                times(a, p),
                scale(times(d, shift(p, Q**-1)), -q**-1),
                scale(times(shift(d, Q), shift(p, Q)), -q),
            )

        def Dop(p):
            lp = Lop(p)
            return plus(
                scale(plus(Bop(Bop(lp)), scale(lp, -1)), q**-2),
                scale(Bop(Zop(p)), q**-3),
                scale(Bop(p), -8 * q**-2),
                scale(p, 8 * q**-1),
            )

        Z = mp.matrix(N)
        L = mp.matrix(N)
        M = mp.matrix(N)
        J = mp.matrix(N)
        S = [mp.mpf(1)]
        for j in range(1, N):
            S.append(S[-1] * 2 * mp.sin(mp.pi * j / N))
        for j in range(N):
            Z[j, j] = q * Q**j + q**-1 * Q**-j
            L[j, j] = 4 * q * Q**j - q * (1 + Q) * Q ** (2 * j)
            J[j, D - j] = 1
            if j:
                Z[j, j - 1] = Q**j + Q**-j - 2
                L[j, j - 1] = L[j - 1, j] = -(1 - Q**j) ** 2
            for k in range(j + 1):
                M[j, k] = kappa * (-1) ** j * q ** (j * (k + 1)) * S[j] / (S[k] * S[j - k])

        def sample(p):
            return mp.matrix(
                [
                    mp.exp(-mp.pi * 1j * D * j / N) * evaluate(p, Q**j)
                    for j in range(N)
                ]
            )

        for k in range(N):
            monomial = {k: mp.mpc(1)}
            for name, operator, matrix in (("Z", Zop, Z), ("B", Bop, Z.T), ("L1", Lop, L)):
                output = operator(monomial)
                outside = {j: value for j, value in output.items() if j < 0 or j > D}
                check(f"{name} preserves polynomial band on X^{k}", norm(outside), norm(output), N)
                difference = sample(output) - matrix * sample(monomial)
                check(
                    f"{name} sampling intertwiner on X^{k}",
                    max(abs(value) for value in difference),
                    max(abs(value) for value in matrix * sample(monomial)),
                    N,
                )

        values = mp.matrix([mp.mpf(1)] + [mp.mpf(0)] * D)
        for j in range(1, N):
            values[j] = values[j - 1] * (Z[j - 1, j - 1] + 2) / (4 * mp.sin(mp.pi * j / N) ** 2)
        w = J * M**3 * values
        polynomial = {
            k: sum(
                w[j] * mp.exp(-2j * mp.pi * (mp.mpf(k) - mp.mpf(D) / 2) * j / N)
                for j in range(N)
            ) / N
            for k in range(N)
        }
        forcing = {
            k: 2 * (1 - eta) * kappa**3 / N**3 for k in range(N)
        }
        output = plus(Dop(polynomial), scale(polynomial, 2))
        residual = plus(output, scale(forcing, -1))
        check("entire forced polynomial equation", norm(residual), norm(polynomial), N)
        check(
            "ordinary polynomial normalization",
            evaluate(polynomial, Q**-1) - kappa**5,
            mp.mpf(1),
            N,
        )
        check(
            "original source interpolation",
            max(abs(value) for value in sample(polynomial) - w),
            max(abs(value) for value in w),
            N,
        )
        for x in (mp.mpc("0.173", "0.091"), mp.mpc("0.417", "-0.027")):
            X = mp.exp(2j * mp.pi * x)
            lhs = mp.exp(-mp.pi * 1j * D * x) * evaluate(output, X)
            cardinal = mp.sin(mp.pi * N * x) / (N * mp.sin(mp.pi * x))
            rhs = 2 * (1 - eta) * kappa**3 * cardinal / N**2
            check(f"entire equation at x={x}", lhs - rhs, abs(lhs) + abs(rhs) + norm(polynomial), N)

    worst = max(mp.mpf(item["relative_error"]) for item in diagnostics)
    result = {
        "status": "passed",
        "precision_digits": args.dps,
        "levels": list(range(2, args.max_level + 1)),
        "diagnostic_count": len(diagnostics),
        "tolerance": mp.nstr(tolerance, 12),
        "largest_relative_error": mp.nstr(worst, 12),
        "scope": "Finite operator, interpolation, parity-forcing and normalization checks; no asymptotic branch-selection claim.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "diagnostics": diagnostics,
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Passed {len(diagnostics)} finite diagnostics at {args.dps} digits.")
    print(f"Largest relative error: {mp.nstr(worst, 12)}")
    print(f"Saved {path}")


if __name__ == "__main__":
    main()
