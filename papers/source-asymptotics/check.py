#!/usr/bin/env python3
"""Exact finite algebra checks for the central shared-coefficient paper.

Requires SymPy. The level-dependent source cofactor and the positive-pencil
continuant are constructed separately in Q(2*cos(pi/N)). These finite
identities do not prove the complex packets, uniform phase losses, Gaussian
asymptotics, or any knot-volume statement.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.polys.rings import ring


def require(value, message):
    if not value:
        raise RuntimeError(message)


def check_level(N):
    d, m, J = N - 1, N // 2, (N - 1) // 2
    F = sp.QQ.algebraic_field(2 * sp.cos(sp.pi / N))
    R, x, b, c, y, u = ring("x,b,c,y,u", F)
    C = [F.convert(2), F.unit]
    for _ in range(2 * N + 2):
        C.append(F.unit * C[-1] - C[-2])
    U = [F.one, F.unit]
    for _ in range(2 * N + 2):
        U.append(F.unit * U[-1] - U[-2])
    a = [F.convert(2) + C[2 * j + 1] for j in range(N)]
    s2 = [F.convert(2) - C[2 * j] for j in range(N)]
    ss = [F.zero] + [C[1] - C[2 * j - 1] for j in range(1, N)]
    A, P = x + y, x * y

    # The original row-replaced triangular cofactor, with unused rows.
    cof = [R.one]
    prefix = R.one
    for j in range(1, m + 1):
        prefix *= R(a[j - 1]) + u
        z = b**j * prefix + s2[j] * A * cof[-1]
        if j >= 2:
            z += ss[j] * (R(a[j - 1]) + u) * P * cof[-2]
        cof.append(z)

    # Independent determinant continuants of bI+xH-/2+yH+/2.
    determinants = [R.one]
    s_even = [F.one]
    s_square = [F.one]
    cholesky = []
    for j in range(1, J + 1):
        n = j - 1
        diagonal = F.convert(2) / (C[n] * C[n + 1])
        z = (b + diagonal * A) * determinants[-1]
        if n:
            bn = F.convert(4) * U[n - 1]**2 / (
                C[n]**2 * U[2 * n - 2] * U[2 * n]
            )
            z -= (bn / F.convert(4)) * (A**2 - C[n]**2 * P) * determinants[-2]
        determinants.append(z)
        s_even.append(s_even[-1] * ss[2 * j])
        s_square.append(s_square[-1] * s2[j])
        pivot = F.convert(2) * U[j - 1] / (C[j] * U[2 * j - 2])
        if n:
            require(pivot == F.convert(4) / (C[n] * C[n + 1]) - bn / cholesky[-1],
                    f"N={N}, j={j}: Cholesky pivot identity")
        else:
            require(pivot == F.convert(2) / C[1], f"N={N}: first pivot")
        cholesky.append(pivot)

    node_checks = 0
    binary_checks = 0
    for j in range(J + 1):
        node_value = cof[j].compose({u: R(-a[j])})
        require(node_value == s_even[j] * determinants[j],
                f"N={N}, j={j}: actual node-to-determinant identity")
        # The actual finite eigen-equation, including its scalar.
        def dq(poly):
            out = R.zero
            for monomial, coefficient in poly.items():
                k = monomial[1]
                if k:
                    power = list(monomial)
                    power[1] -= 1
                    # Use [k]=sin(k theta)/sin(theta), avoiding extra fields.
                    out += R.from_dict({tuple(power): coefficient * U[k - 1]})
            return out
        lhs = dq((b*b + A*b + P) * dq(determinants[j]))
        eigen = F.zero if j == 0 else U[j - 1] * U[j]
        require(lhs == eigen * determinants[j], f"N={N}, j={j}: eigenpolynomial")
        node_checks += 1
        beta = s_even[j] / s_square[j]
        binary = R.zero
        for k in range(j + 1):
            coefficient = s_square[j] / (s_square[k] * s_square[j - k])
            binary += coefficient * x**k * y**(j - k)
        require(determinants[j].compose({b: R.zero}) * beta == binary,
                f"N={N}, j={j}: protected-middle sine-binomial expansion")
        binary_checks += 1

    D = cof[m - 1]
    Dc = D.compose({b: c})
    if N % 2:
        G = cof[m]
        source = G * G.compose({b: c}) + u * s2[m] * P * D * Dc
        require((u * s2[m] * P * D * Dc).diff(u).compose({u: R.zero}) != R.zero,
                f"N={N}: skipped-row first normal missing")
    else:
        E = (R(a[m - 1]) + u) * cof[m - 2] if m >= 2 else R.zero
        source = s2[m] * A * D * Dc + ss[m] * P * (
            D * E.compose({b: c}) + E * Dc
        )
    beta = s_even[J] / s_square[J]
    anchor = F.convert(N*N) * beta**2 * determinants[J] * (
        determinants[J].compose({b: c})
    ) * A**(d - 2*J)
    require(source.compose({u: R(-a[J])}) == anchor,
            f"N={N}: maximal-fold parity anchor")
    return {
        "level": N,
        "parity": "odd" if N % 2 else "even",
        "node_and_eigenpolynomial_identities": node_checks,
        "binary_coefficient_identities": binary_checks,
        "cholesky_pivot_identities": len(cholesky),
        "exact_maximal_fold_anchor": True,
        "odd_skipping_normal_checked": bool(N % 2),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent / "build/check.json")
    args = parser.parse_args()
    levels = [check_level(N) for N in (3, 4, 5, 6, 7, 8)]
    here = Path(__file__).resolve().parent
    report = {
        "scope": "Finite exact source, positive-pencil, and parity-anchor identities "
                 "at the listed levels. No sampled asymptotic or positivity test is "
                 "used as a proof of a uniform estimate or a volume theorem.",
        "arithmetic": "Exact algebraic field Q(2*cos(pi/N)); equality is coefficientwise.",
        "sympy_version": sp.__version__,
        "levels": levels,
        "paper_sha256": hashlib.sha256((here / "main.tex").read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {args.output}; six finite levels checked exactly.")


if __name__ == "__main__":
    main()
