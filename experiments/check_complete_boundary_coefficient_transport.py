#!/usr/bin/env python3
"""Finite checks of the original complete-boundary coefficient transport.

The reference crossing matrix is built by polynomial multiplication and
division in the original Newton quotient, not by the displayed triangular
matrix formula. The checks are finite diagnostics, not proofs of asymptotic
branch selection or of a volume limit.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


def add(a, b):
    c = [mp.mpc(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return c


def mul(a, b):
    c = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def scale(a, c):
    return [c * x for x in a]


def remainder(a, modulus):
    a = list(a)
    degree = len(modulus) - 1
    for i in range(len(a) - 1, degree - 1, -1):
        coefficient = a[i] / modulus[-1]
        for j in range(degree + 1):
            a[i - degree + j] -= coefficient * modulus[j]
    return (a + [mp.mpc(0)] * degree)[:degree]


def evaluate(a, z):
    total = mp.mpc(0)
    for x in reversed(a):
        total = total * z + x
    return total


def coordinates(a, basis):
    residual = list(a) + [mp.mpc(0)] * (len(basis) - len(a))
    answer = [mp.mpc(0)] * len(basis)
    for j in range(len(basis) - 1, -1, -1):
        answer[j] = residual[j] / basis[j][-1]
        for k, value in enumerate(basis[j]):
            residual[k] -= answer[j] * value
    return mp.matrix(answer)


def max_entry(matrix):
    return max((abs(value) for value in matrix), default=mp.mpf(0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--max-level", type=int, default=12)
    parser.add_argument(
        "--output",
        default="repro/results/research-complete-boundary-coefficient-transport.json",
    )
    args = parser.parse_args()
    if args.dps < 70 or args.max_level < 4:
        parser.error("Use at least 70 digits and include both parities through level 4.")
    mp.mp.dps = args.dps
    tolerance = mp.mpf(10) ** (-(args.dps - 35))
    diagnostics = []

    def check(label, observed, expected, level):
        if isinstance(observed, mp.matrix):
            error = max_entry(observed - expected) / (1 + max_entry(expected))
        else:
            error = abs(observed - expected) / (1 + abs(expected))
        diagnostics.append(
            {"level": level, "identity": label, "relative_error": mp.nstr(error, 12)}
        )
        if error >= tolerance:
            raise AssertionError(f"N={level}, {label}: relative error {error}")

    for N in range(3, args.max_level + 1):
        D = N - 1
        eta = (-1) ** D
        q = mp.exp(mp.pi * 1j / N)
        Q = q * q
        kappa = mp.exp(mp.pi * 1j * D * D / (2 * N))
        roots = [2 * mp.cos(mp.pi * (2 * j + 1) / N) for j in range(N)]
        s = [2 * mp.sin(mp.pi * j / N) for j in range(N)]
        S = [mp.mpf(1)]
        for j in range(1, N):
            S.append(S[-1] * s[j])
        modulus = [mp.mpc(1)]
        for root in roots:
            modulus = mul(modulus, [-root, 1])
        basis = [[mp.mpc(1)]]
        numerator = [mp.mpc(1)]
        for j in range(1, N):
            numerator = mul(numerator, [roots[j - 1], -1])
            basis.append(scale(numerator, 1 / S[j] ** 2))
        crossing = [mp.mpc(0)] * N
        for j in range(N):
            crossing = add(crossing, scale(basis[j], kappa * (-q) ** j))

        def product(a, b):
            return remainder(mul(a, b), modulus)

        def trace(a):
            return eta * N * N * remainder(a, modulus)[D]

        def power(n):
            result = [mp.mpc(1)]
            factor = crossing if n >= 0 else [mp.conj(x) for x in crossing]
            for _ in range(abs(n)):
                result = product(result, factor)
            return result

        M = mp.matrix(N)
        Z = mp.matrix(N)
        J = mp.matrix(N)
        triangular = mp.matrix(N)
        for j in range(N):
            column = coordinates(product(crossing, basis[j]), basis)
            zcolumn = coordinates(product([0, 1], basis[j]), basis)
            for i in range(N):
                M[i, j] = column[i]
                Z[i, j] = zcolumn[i]
            J[j, D - j] = 1
            for k in range(j + 1):
                triangular[j, k] = (
                    kappa
                    * (-1) ** j
                    * q ** (j * (k + 1))
                    * S[j]
                    / (S[k] * S[j - k])
                )
        identity = mp.eye(N)
        pin = mp.matrix(N)
        pin[0, D] = 1
        base_pin = mp.matrix(N)
        base_pin[D, 0] = 1
        conjugate_M = M.apply(mp.conj)
        check("crossing matrix from quotient multiplication", M, triangular, N)
        check("crossing conjugation", conjugate_M * M, identity, N)
        check("Frobenius transpose", M.T * J, J * M, N)
        check("preserved indefinite form", conjugate_M.T * J * M, J, N)
        check("Newton reversal", J * Z * J, Z.T, N)

        L1 = mp.matrix(N)
        for j in range(N):
            L1[j, j] = 4 * q * Q**j - q * (1 + Q) * Q ** (2 * j)
            if j:
                L1[j, j - 1] = L1[j - 1, j] = -(1 - Q**j) ** 2
        check("tridiagonal character conjugation", conjugate_M * Z.T * M, L1, N)
        B = Z.T
        explicit_D3 = (
            q**-2 * (B * B - identity) * L1
            + q**-3 * B * Z
            - 8 * q**-2 * B
            + 8 * q**-1 * identity
        )
        check(
            "power-three banded operator",
            explicit_D3,
            J * M**3 * Z.T * conjugate_M**3 * J,
            N,
        )
        complete_vectors = {}
        for n in (-3, -1, 0, 1, 2, 3):
            Rn = power(n)
            Mn = M**n
            An = J * Mn
            Dn = An * Z.T * An**-1
            check(f"symmetric A_{n}", An.T, An, N)
            for z in (-2, roots[0], mp.mpc("0.37", "0.21")):
                values = mp.matrix([evaluate(e, z) for e in basis])
                kernel = [mp.mpc(0)] * N
                for j in range(N):
                    kernel = add(kernel, scale(basis[j], values[j]))
                weighted = product(Rn, kernel)
                direct_w = mp.matrix([trace(mul(weighted, e)) for e in basis])
                w = An * values
                location = "complete" if z == -2 else ("physical" if z == roots[0] else "complex")
                check(f"direct trace vector n={n} z={location}", w, direct_w, N)
                rhs = mp.matrix(N, 1)
                rhs[0] = -eta * kappa**n * evaluate(modulus, z) / N**2
                check(
                    f"free-boundary forcing n={n} z={location}",
                    (Dn - z * identity) * direct_w,
                    rhs,
                    N,
                )
                check(f"last coordinate n={n} z={location}", direct_w[D], kappa**n, N)
                pinned = Dn-z*identity+pin
                base = Z.T-z*identity+base_pin
                determinant = N**2-eta*evaluate(modulus, z)
                check(f"pinned conjugacy n={n} z={location}",
                      pinned, An*base*An**-1, N)
                check(f"pinned determinant n={n} z={location}",
                      mp.det(pinned), determinant, N)
                pinned_rhs = mp.matrix(N, 1)
                pinned_rhs[0] = kappa**n*determinant/N**2
                check(f"all-parity pinned forcing n={n} z={location}",
                      pinned*direct_w, pinned_rhs, N)
                if abs(determinant) > tolerance:
                    check(f"pinned cap Green response n={n} z={location}",
                          (pinned**-1)[D, 0], N**2/determinant, N)
                if z == -2:
                    complete_rhs = mp.matrix(N, 1)
                    complete_rhs[0] = 2 * (1 - eta) * kappa**n / N**2
                    check(f"complete parity forcing n={n}", (Dn + 2 * identity) * direct_w, complete_rhs, N)
                    check(
                        f"complete indefinite normalization n={n}",
                        (direct_w.apply(mp.conj).T * J * direct_w)[0],
                        mp.mpf(1),
                        N,
                    )
                    complete_vectors[n] = direct_w

        w = complete_vectors[3]
        wminus = complete_vectors[-3]
        check("opposite-power conjugation", wminus, w.apply(mp.conj), N)
        pair = sum(x * x for x in w)
        reflected = sum(w[j] * wminus[j] for j in range(N))
        check("positive reflected pair", reflected, sum(abs(x) ** 2 for x in w), N)
        theta = mp.pi / N
        E = 1 / (4 * mp.sin(theta / 2) ** 2)
        a = 1 / (2 * mp.cos(theta))
        check("last two exact coefficients", w[D - 1] / kappa**3, -q**6 * (E + a) - a, N)

        frequencies = [mp.mpf(j) - mp.mpf(D) / 2 for j in range(N)]

        def fourier_coefficients(vector):
            return [
                sum(vector[j] * mp.exp(-2j * mp.pi * ell * j / N) for j in range(N)) / N
                for ell in frequencies
            ]

        coefficients = fourier_coefficients(w)
        minus_coefficients = fourier_coefficients(wminus)

        def interpolated(coefficients, x):
            return sum(c * mp.exp(2j * mp.pi * ell * x) for c, ell in zip(coefficients, frequencies))

        check(
            "bilinear Fourier constant coefficient",
            N * sum(coefficients[j] * coefficients[D - j] for j in range(N)),
            pair,
            N,
        )
        # The product has integer degree at most D; this trapezoidal
        # integral is exact algebraically on either translated circle.
        count = 2 * N + 1
        for height in (mp.mpf(0), mp.mpf("0.019")):
            points = [mp.mpf("0.173") + mp.mpf(j) / count + 1j * height for j in range(count)]
            integral = N * sum(interpolated(coefficients, x) ** 2 for x in points) / count
            check(f"shifted exact circle height={height}", integral, pair, N)
        points = [mp.mpf(j) / count for j in range(count)]
        positive_integral = N * sum(abs(interpolated(coefficients, x)) ** 2 for x in points) / count
        mixed_integral = N * sum(
            interpolated(coefficients, x) * interpolated(minus_coefficients, x) for x in points
        ) / count
        check("positive real-period integral", positive_integral, reflected, N)
        check("opposite-power Fourier product", mixed_integral, reflected, N)

        # Check the literal shifted adjoint test using the reference
        # quotient multiplication matrix, not a guessed recurrence.
        height = mp.mpf("0.037")
        U = mp.matrix([[mp.exp(-2j*mp.pi*ell*j/N)/mp.sqrt(N)
                        for j in range(N)] for ell in frequencies])
        shift = U.H*mp.diag([mp.exp(-2*mp.pi*ell*height)
                            for ell in frequencies])*U
        A3 = J*M**3
        Q3 = A3*Z.T*A3**-1+2*identity+pin
        shifted_Q = shift*Q3*shift**-1
        f = shift*w
        e0 = mp.matrix(N, 1)
        e0[0] = 1
        forcing = shift*e0
        trial = J*f
        sigma = 1+mp.mpf(2)*(1-eta)/N**2
        check("shifted indefinite adjoint relation",
              shifted_Q.H, J*shifted_Q*J, N)
        check("shifted trial forcing overlap",
              (trial.H*forcing)[0], mp.conj(kappa**3), N)
        check("shifted trial adjoint residual",
              shifted_Q.H*trial, kappa**3*sigma*J*forcing, N)
        check("shifted forcing norm",
              (forcing.H*forcing)[0],
              mp.sinh(2*mp.pi*N*height)/(N*mp.sinh(2*mp.pi*height)), N)

    worst = max(mp.mpf(item["relative_error"]) for item in diagnostics)
    result = {
        "status": "passed",
        "precision_digits": args.dps,
        "levels": list(range(3, args.max_level + 1)),
        "diagnostic_count": len(diagnostics),
        "tolerance": mp.nstr(tolerance, 12),
        "largest_relative_error": mp.nstr(worst, 12),
        "reference": "Polynomial multiplication, division, and Frobenius trace in the original Newton quotient.",
        "scope": "Finite normalization and identity diagnostics only; no asymptotic lower bound or branch-selection claim.",
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
