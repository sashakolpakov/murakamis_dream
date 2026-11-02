#!/usr/bin/env python3
"""Bounded exact checks for Uniform spectral bounds for local Casimir sources.

Requires SymPy. All source arithmetic is in Q(2 cos(pi/N)); no floating
tolerance decides an identity or coefficient sign. These finite examples
check the formulas, not the all-level estimates or their asymptotic limits.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp
from sympy.polys.rings import ring


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run_level(N):
    d, m = N - 1, N // 2
    J = (N - 1) // 2
    K = sp.QQ.algebraic_field(2 * sp.cos(sp.pi / N))
    R, x, b, c, y, u = ring("x,b,c,y,u", K)
    two_cos = [K.convert(2), K.unit]
    for k in range(1, 2 * N + 1):
        two_cos.append(K.unit * two_cos[k] - two_cos[k - 1])
    a = [K.convert(2) + two_cos[2 * j + 1] for j in range(N)]
    s2 = [K.convert(2) - two_cos[2 * j] for j in range(N)]
    ss = [K.zero] + [
        two_cos[1] - two_cos[2 * j - 1] for j in range(1, N)
    ]
    A, P = x + y, x * y
    zero, one = R.zero, R.one

    # Literal monomial-basis Casimir, not the path sum or cofactor recurrence.
    C = [[zero for _ in range(N)] for _ in range(N)]
    for j in range(N):
        C[j][j] = R(two_cos[2 * j + 1])
        if j:
            C[j - 1][j] = -s2[j] * A
        if j >= 2:
            C[j - 2][j] = -ss[j] * P

    def mmul(U, V):
        out = [[zero for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for k in range(i, N):
                if U[i][k]:
                    for j in range(k, N):
                        if V[k][j]:
                            out[i][j] += U[i][k] * V[k][j]
        return out

    eye = [[one if i == j else zero for j in range(N)] for i in range(N)]
    powers = [eye]
    for _ in range(d):
        powers.append(mmul(powers[-1], C))
    z = sp.Symbol("z")
    chi = sp.Poly(2 * sp.chebyshevt(N, z / 2) + 2, z)
    sigma = -2 - u
    V = [[zero for _ in range(N)] for _ in range(N)]
    for k in range(1, N + 1):
        ck = R(int(chi.nth(k)))
        if ck:
            for r in range(k):
                scalar = ck * sigma ** (k - 1 - r)
                for i in range(N):
                    for j in range(i, N):
                        V[i][j] += scalar * powers[r][i][j]
    matrix_source = (-1) ** d * sum(
        (V[i][j] * b ** i * c ** (d - j)
         for i in range(N) for j in range(i, N)), zero
    )

    # Independent explicit decreasing paths with their actual unused rows.
    sectors = {"C": zero, "L": zero, "R": zero}
    path_count = 0

    def finish(start, end, visited, weight):
        nonlocal path_count
        term = weight * b ** end * c ** (d - start)
        for row in range(N):
            if row not in visited:
                term *= R(a[row]) + u
        central = (end <= m - 1 and start >= m) if N % 2 == 0 else (
            end <= m and start >= m
        )
        label = "C" if central else ("L" if start < m else "R")
        sectors[label] += term
        path_count += 1

    def paths(start, current, visited, weight):
        finish(start, current, visited, weight)
        if current >= 1:
            paths(start, current - 1, visited | {current - 1},
                  weight * s2[current] * A)
        if current >= 2:
            paths(start, current - 2, visited | {current - 2},
                  weight * ss[current] * P)

    for start in range(N):
        paths(start, start, {start}, one)
    require(matrix_source == sum(sectors.values(), zero),
            f"N={N}: full resolvent differs from path partition")
    require(sectors["L"].compose({b: c, c: b}) == sectors["R"],
            f"N={N}: middle reversal fails")
    require(not sectors["L"].compose({c: zero}),
            f"N={N}: protected output does not kill left")
    require(not sectors["R"].compose({b: zero}),
            f"N={N}: protected input does not kill right")

    cofactors = [one]
    for j in range(1, m + 1):
        prod = one
        for r in range(j):
            prod *= R(a[r]) + u
        value = b ** j * prod + s2[j] * A * cofactors[j - 1]
        if j >= 2:
            value += ss[j] * (R(a[j - 1]) + u) * P * cofactors[j - 2]
        cofactors.append(value)
    D = cofactors[m - 1]
    E = (R(a[m - 1]) + u) * cofactors[m - 2] if m >= 2 else zero
    Dc, Ec = D.compose({b: c}), E.compose({b: c})
    if N % 2:
        G = cofactors[m]
        skipping = u * s2[m] * P * D * Dc
        central_formula = G * G.compose({b: c}) + skipping
        require(skipping.diff(u).compose({u: zero}) != zero,
                f"N={N}: odd skipping normal unexpectedly zero")
        require(sectors["C"] != G * G.compose({b: c}),
                f"N={N}: omission of odd skip was not detected")
    else:
        central_formula = s2[m] * A * D * Dc + ss[m] * P * (D * Ec + E * Dc)
    require(central_formula == sectors["C"],
            f"N={N}: exact central factorization fails")

    sign_checks = 0
    interpolation_checks = 0

    def nonnegative(poly, context):
        nonlocal sign_checks
        for value in poly.values():
            # The four test fields have degree at most two. Reduce the
            # sign to a rational squared comparison, not an evalf decision.
            coeffs = list(value.to_list())
            require(len(coeffs) <= 2, "unexpected field degree")
            linear, constant = ([K.dom.zero] + coeffs)[-2:]
            if N == 3:
                rational, radical, radicand = constant, K.dom.zero, 1
            elif N == 5:
                rational = constant + linear / 2
                radical, radicand = linear / 2, 5
            else:
                rational, radical = constant, linear
                radicand = 2 if N == 4 else 3
            if not radical:
                verdict = rational >= 0
            elif not rational or (rational > 0) == (radical > 0):
                verdict = radical > 0
            else:
                comparison = rational * rational - radicand * radical * radical
                verdict = (comparison >= 0) if rational > 0 else (comparison <= 0)
            require(verdict, f"N={N}: negative coefficient in {context}")
            sign_checks += 1

    nodes = [-a[j] for j in range(J + 1)]
    for j in range(J + 1):
        base = cofactors[j].compose({u: zero})
        interpolated = zero
        for ai, node in enumerate(nodes):
            at_node = cofactors[j].compose({u: R(node)})
            nonnegative(at_node, "nodal positivity")
            nonnegative(base - at_node, "zero-spectral comparison")
            cardinal = one
            denominator = K.one
            for bi, other in enumerate(nodes):
                if bi != ai:
                    cardinal *= u - R(other)
                    denominator *= node - other
            interpolated += at_node * cardinal * R(K.one / denominator)
        require(interpolated == cofactors[j],
                f"N={N}: coefficientwise Lagrange interpolation fails")
        interpolation_checks += 1

    return {
        "N": N,
        "parity": "odd" if N % 2 else "even",
        "explicit_paths": path_count,
        "full_resolvent_equals_partition": True,
        "central_factorization": True,
        "odd_skipping_first_normal_retained": bool(N % 2),
        "middle_reversal_and_protected_zeros": True,
        "exact_coefficient_sign_checks": sign_checks,
        "exact_interpolation_identities": interpolation_checks,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent / "build/check.json")
    args = parser.parse_args()
    levels = [run_level(N) for N in (3, 4, 5, 6)]
    here = Path(__file__).resolve().parent
    result = {
        "scope": "Finite exact polynomial identities and signs at the listed levels; "
                 "not a proof of all-level estimates, real-interval uniformity, "
                 "entropy optimization, a source gap, or a volume limit.",
        "arithmetic": "SymPy exact real algebraic fields Q(2 cos(pi/N))",
        "sympy_version": sp.__version__,
        "levels": levels,
        "source_sha256": hashlib.sha256((here / "main.tex").read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {args.output}; {len(levels)} finite levels checked exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
