#!/usr/bin/env python3
"""Finite checks of the physical root chirp and exact contour identity.

The polynomial side constructs the original canonical crossing, multiplies
and divides polynomials, and applies the top-coefficient trace.  At s=0 it
uses the full complete Newton crossing, including Hermite normals.  The
contour side uses the independently derived paired-grid kernel.

This checks finite identities, not the uniform Gaussian estimate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp


def add(a, b):
    result = [mp.mpc(0) for _ in range(max(len(a), len(b)))]
    for i, x in enumerate(a):
        result[i] += x
    for i, x in enumerate(b):
        result[i] += x
    return result


def scale(a, c):
    return [c * x for x in a]


def multiply(a, b):
    result = [mp.mpc(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def evaluate(a, z):
    result = mp.mpc(0)
    for x in reversed(a):
        result = result * z + x
    return result


def remainder(a, p):
    result = list(a)
    degree = len(p) - 1
    for k in range(len(result) - 1, degree - 1, -1):
        factor = result[k] / p[-1]
        for j in range(degree + 1):
            result[k - degree + j] -= factor * p[j]
    return result[:degree] + [mp.mpc(0)] * max(0, degree - len(result))


def chebyshev_relation(n, s):
    prev, curr = [mp.mpc(2)], [mp.mpc(0), mp.mpc(1)]
    for _ in range(1, n):
        prev, curr = curr, add([mp.mpc(0)] + curr, scale(prev, -1))
    result = list(curr)
    result[0] += 2 * mp.cos(2 * mp.pi * s)
    return result


def ordinary_character(j):
    if j == 1:
        return [mp.mpc(1)]
    prev, curr = [mp.mpc(1)], [mp.mpc(0), mp.mpc(1)]
    for _ in range(1, j - 1):
        prev, curr = curr, add([mp.mpc(0)] + curr, scale(prev, -1))
    return scale(curr, (-1) ** (j - 1))


def complete_crossing(n):
    d = n - 1
    q = mp.exp(mp.j * mp.pi / n)
    basis = [mp.mpc(1)]
    result = list(basis)
    for k in range(1, n):
        node = 2 * mp.cos((2 * k - 1) * mp.pi / n)
        factor = 4 * mp.sin(k * mp.pi / n) ** 2
        basis = scale(multiply(basis, [node, -1]), 1 / factor)
        result = add(result, scale(basis, (-q) ** k))
    return scale(result, mp.exp(mp.j * mp.pi * d * d / (2 * n)))


def physical_crossing(n, s):
    if s == 0:
        return complete_crossing(n)
    d = n - 1
    nodes, values = [], []
    kappa = mp.exp(mp.j * mp.pi * (d + s) ** 2 / (2 * n))
    for r in range(n):
        theta = (-2 * r - 1 + 2 * s) * mp.pi / n
        nodes.append(2 * mp.cos(theta))
        values.append(kappa * (-1) ** r *
                      mp.exp(mp.j * mp.pi * (r * (r + 1) - 2 * s * r) / n))
    matrix = mp.matrix([[z ** k for k in range(n)] for z in nodes])
    return list(mp.lu_solve(matrix, mp.matrix(values)))


def inverse_mod(a, p):
    n = len(p) - 1
    matrix = mp.matrix(n)
    for k in range(n):
        column = remainder([mp.mpc(0)] * k + a, p)
        for r in range(n):
            matrix[r, k] = column[r]
    return list(mp.lu_solve(matrix, mp.matrix([1] + [0] * (n - 1))))


def raw_test_polynomial(n):
    result = [mp.mpc(0) for _ in range(2 * n + 2)]
    result[0] = 1 + mp.j / 5
    result[1] = mp.mpf(2) / 7 - mp.j / 11
    result[n - 1] += -mp.mpf(3) / 13
    result[n + 2] += mp.mpf(1) / 17 + mp.j / 19
    result[2 * n + 1] = -mp.mpf(1) / 23
    return result


def polynomial_trace(n, s, crossing, character, raw):
    p = chebyshev_relation(n, s)
    product = multiply(multiply(crossing, character), raw)
    return (-1) ** (n - 1) * n * n * remainder(product, p)[n - 1]


def contour_trace(n, s, epsilon, j, raw, height, quadrature):
    d = n - 1
    eta = (-1) ** (n + 1)
    zeta_plus = eta * mp.exp(2 * mp.pi * mp.j * s)
    zeta_minus = eta * mp.exp(-2 * mp.pi * mp.j * s)
    phase = mp.exp(mp.j * mp.pi * epsilon *
                   (mp.mpf(d * d) / 4 - s * s / 2) / n)

    def integrand(tau):
        u = mp.exp(mp.j * n * tau)
        kernel = u / ((u - zeta_plus) * (u - zeta_minus))
        chirp = mp.exp(mp.j * epsilon * n * tau * tau / (4 * mp.pi))
        return mp.sin(j * tau) * chirp * evaluate(raw, -2 * mp.cos(tau)) * kernel

    corners = [-mp.pi - mp.j * height, mp.pi - mp.j * height,
               mp.pi + mp.j * height, -mp.pi + mp.j * height,
               -mp.pi - mp.j * height]
    total = mp.mpc(0)
    nodes, weights = quadrature
    for start, end in zip(corners, corners[1:]):
        for segment in range(4):
            left = start + (end - start) * mp.mpf(segment) / 4
            right = start + (end - start) * mp.mpf(segment + 1) / 4
            middle, half_width = (left + right) / 2, (right - left) / 2
            total += half_width * mp.fsum(
                weight * integrand(middle + half_width * node)
                for node, weight in zip(nodes, weights))
    return -n * n * phase * total / (2 * mp.pi * mp.j)


def scaled_error(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def run(levels, digits):
    mp.mp.dps = digits
    params = [("0", mp.mpc(0)),
              ("1/4+i/8", mp.mpc(mp.mpf(1) / 4, mp.mpf(1) / 8))]
    height = mp.mpf(9) / 10
    tolerance = mp.mpf("1e-35")
    quadrature = mp.gauss_quadrature(80, "legendre")
    cases = []
    maxima = {name: mp.mpf(0) for name in
              ("crossing_inverse", "physical_chirp", "character_pivot", "contour")}
    for n in levels:
        d = n - 1
        raw = raw_test_polynomial(n)
        for name, s in params:
            p = chebyshev_relation(n, s)
            cross = physical_crossing(n, s)
            inverse = inverse_mod(cross, p)
            product = remainder(multiply(cross, inverse), p)
            inverse_error = max(abs(x - (1 if k == 0 else 0))
                                for k, x in enumerate(product))
            maxima["crossing_inverse"] = max(maxima["crossing_inverse"], inverse_error)
            for epsilon in (-1, 0, 1):
                power = inverse if epsilon == -1 else cross if epsilon == 1 else [1]
                phase = mp.exp(mp.j * mp.pi * epsilon *
                               (mp.mpf(d * d) / 4 - s * s / 2) / n)
                for r in range(n):
                    tau = 2 * mp.pi * (mp.mpf(d) / 2 + s - r) / n
                    exact = phase * mp.exp(mp.j * epsilon * n * tau * tau / (4 * mp.pi))
                    maxima["physical_chirp"] = max(
                        maxima["physical_chirp"],
                        scaled_error(evaluate(power, -2 * mp.cos(tau)), exact))
                for j in (1, n):
                    character = ordinary_character(j)
                    tau_test = mp.mpf(2) / 7 + mp.j / 9
                    pivot_error = scaled_error(
                        evaluate(character, -2 * mp.cos(tau_test)),
                        mp.sin(j * tau_test) / mp.sin(tau_test))
                    maxima["character_pivot"] = max(maxima["character_pivot"], pivot_error)
                    direct = polynomial_trace(n, s, power, character, raw)
                    integral = contour_trace(n, s, epsilon, j, raw, height, quadrature)
                    error = scaled_error(direct, integral)
                    maxima["contour"] = max(maxima["contour"], error)
                    assert error < tolerance, (n, name, epsilon, j, mp.nstr(error, 20))
                    cases.append({"N": n, "s": name, "epsilon": epsilon, "j": j,
                                  "scaled_error": mp.nstr(error, 12)})
        print(f"completed N={n}", flush=True)
    assert all(value < tolerance for value in maxima.values())
    return {"precision_decimal_digits": digits,
            "levels": levels, "parameter_values": [name for name, _ in params],
            "root_half_twists": [-1, 0, 1],
            "raw_polynomial_degree": "2N+1",
            "contour_height": "9/10",
            "quadrature": "80-point Gauss-Legendre, four segments per side",
            "scaled_error_tolerance": "1e-35",
            "contour_identities_checked": len(cases),
            "maximum_errors": {name: mp.nstr(value, 12) for name, value in maxima.items()},
            "scope": "Finite physical crossing, pivot, full quotient trace, and contour identities only; no uniform analytic estimate is inferred.",
            "cases": cases}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--levels", default="2,3")
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "main_meridian_auxiliary_color_gap_results.json"))
    args = parser.parse_args()
    result = run([int(n) for n in args.levels.split(",")], args.digits)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: result[key] for key in
                      ("contour_identities_checked", "maximum_errors")}, sort_keys=True))


if __name__ == "__main__":
    main()
