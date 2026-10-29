#!/usr/bin/env python3
"""Reproducible algebra and numerical checks for notes/quantum_a_volume.md.

Numerical results support, and do not replace, the proofs in the note. Only
mpmath and sympy are external dependencies. Run from any working directory.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


def figure_eight_target() -> mp.mpf:
    def length_half(alpha: mp.mpf) -> mp.mpf:
        c = 1 + mp.cos(alpha) - mp.cos(2 * alpha)
        return mp.acosh(max(mp.mpf(1), c))

    return mp.quad(length_half, [0, mp.pi / 3, 2 * mp.pi / 3])


def cone_recurrence_rate(n: int, summands: int = 1) -> float:
    """Compute (T/n) log |f_n| without exponentially large intermediate values."""
    total_angle = 2 * math.pi / 3
    step = total_angle / n
    ratio = 1.0
    log_state = 0.0
    for k in range(n):
        log_state += math.log(ratio)
        if k < n - 1:
            alpha = total_angle - k * step
            c = max(1.0, 1 + math.cos(alpha) - math.cos(2 * alpha))
            a = 2 * math.cosh(summands * math.acosh(c))
            ratio = a - 1 / ratio
            if ratio < 1 - 2e-14:
                raise AssertionError("The positive recurrence left its invariant cone")
    return step * log_state


def exact_operator_check() -> dict[str, str]:
    """Evaluate the actual SL(2) Laurent polynomial, not its trigonometric rewrite."""
    n = 31
    total_angle = 2 * mp.pi / 3
    step = total_angle / n
    q = mp.exp(-mp.j * step / 2)
    m0 = mp.exp(mp.j * total_angle / 2)
    f = [mp.mpf(1), mp.mpf(-1)]
    largest_residual = mp.mpf(0)
    for k in range(n - 1):
        alpha = total_angle - k * step
        a = 2 * (1 + mp.cos(alpha) - mp.cos(2 * alpha))
        f.append(-a * f[-1] - f[-2])
        m = m0 * q**k
        t = m**4 - m**2 - 2 - m**-2 + m**-4
        residual = f[k + 2] - t * f[k + 1] + f[k]
        scale = max(mp.mpf(1), abs(f[k + 2]), abs(t * f[k + 1]))
        largest_residual = max(largest_residual, abs(residual) / scale)
    assert largest_residual < mp.mpf("1e-45")

    a, l = sp.symbols("a l")
    matrix = sp.Matrix([[a - 1, a - 2], [1, 1]])
    characteristic = sp.expand((l * sp.eye(2) - matrix).det())
    assert sp.expand(characteristic - (l**2 - a * l + 1)) == 0
    return {
        "relative_laurent_operator_residual": mp.nstr(largest_residual, 8),
        "positive_transfer_characteristic": str(characteristic),
    }


def connected_sum_symbol_check() -> dict[str, object]:
    t, l = sp.symbols("t l")
    companion = sp.Matrix([[t, -1], [1, 0]])
    traces = [sp.Integer(2), t]
    checked = []
    for r in range(1, 7):
        if r >= len(traces):
            traces.append(sp.expand(t * traces[-1] - traces[-2]))
        polynomial = sp.expand((l * sp.eye(2) - companion**r).det())
        assert sp.expand(polynomial - (l**2 - traces[r] * l + 1)) == 0
        checked.append({"summands": r, "trace_polynomial": str(traces[r])})
    return {"characteristic_polynomials_checked": checked}


# Formal quantum-plane computations use the normal order x^a y^b, xy=q yx.
Polynomial = dict[tuple[int, int], Fraction]


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = left.copy()
    for power, coefficient in right.items():
        result[power] = result.get(power, Fraction(0)) + coefficient
        if not result[power]:
            del result[power]
    return result


def scale(poly: Polynomial, value: Fraction) -> Polynomial:
    return {power: coefficient * value for power, coefficient in poly.items() if coefficient * value}


def multiply(left: Polynomial, right: Polynomial, q: Fraction, degree: int) -> Polynomial:
    result: Polynomial = {}
    for (a, b), ca in left.items():
        for (c, d), cb in right.items():
            if a + b + c + d <= degree:
                key = (a + c, b + d)
                value = ca * cb * q ** (-b * c)
                result[key] = result.get(key, Fraction(0)) + value
    return {power: coefficient for power, coefficient in result.items() if coefficient}


def q_series(argument: Polynomial, q: Fraction, degree: int, inverse: bool) -> Polynomial:
    """E_q if inverse=False; Psi_q=(argument;q)_infinity if inverse=True."""
    result: Polynomial = {}
    power: Polynomial = {(0, 0): Fraction(1)}
    denominator = Fraction(1)
    for n in range(degree + 1):
        if n:
            denominator *= 1 - q**n
        coefficient = Fraction(1, 1) / denominator
        if inverse:
            coefficient *= (-1) ** n * q ** (n * (n - 1) // 2)
        result = add(result, scale(power, coefficient))
        power = multiply(power, argument, q, degree)
    return result


def quantum_pentagon_check() -> dict[str, object]:
    q = Fraction(2, 5)
    degree = 8
    x: Polynomial = {(1, 0): Fraction(1)}
    y: Polynomial = {(0, 1): Fraction(1)}
    minus_yx = scale(multiply(y, x, q, degree), Fraction(-1))

    ex = q_series(x, q, degree, False)
    ey = q_series(y, q, degree, False)
    ez = q_series(minus_yx, q, degree, False)
    left = multiply(ex, ey, q, degree)
    right = multiply(multiply(ey, ez, q, degree), ex, q, degree)
    assert left == right, "E_q pentagon failed"

    px = q_series(x, q, degree, True)
    py = q_series(y, q, degree, True)
    pz = q_series(minus_yx, q, degree, True)
    left_inverse = multiply(py, px, q, degree)
    right_inverse = multiply(multiply(px, pz, q, degree), py, q, degree)
    assert left_inverse == right_inverse, "Psi_q pentagon failed"

    shifted = {(a, b): coefficient * q**a for (a, b), coefficient in px.items()}
    one_minus_x: Polynomial = {(0, 0): Fraction(1), (1, 0): Fraction(-1)}
    assert multiply(one_minus_x, shifted, q, degree) == px
    return {"q": str(q), "total_degree": degree, "both_pentagons": True, "local_difference_equation": True}


def log_sine_factorials(n: int) -> list[float]:
    values = [0.0]
    for k in range(1, n):
        values.append(values[-1] + math.log(2 * math.sin(math.pi * k / n)))
    return values


def log_sum_exp(values: list[float]) -> float:
    largest = max(values)
    return largest + math.log(math.fsum(math.exp(value - largest) for value in values))


def figure_eight_angle_sum(n: int) -> dict[str, float | int]:
    """Enumerate the exact positive angle lattice of the two-tetrahedron example.

    Variables (a,b,c,d,e,f) obey a+b+c=d+e+f=N and
    2a+b+2d+e=2N. These equations have the same affine solution
    as Example A.10 of Garoufalidis--Hodgson--Hoffman--Rubinstein,
    https://arxiv.org/abs/1604.02688 .
    """
    factorials = log_sine_factorials(n)
    contributions: list[float] = []
    for a in range(1, n - 1):
        for b in range(1, n - a):
            c = n - a - b
            # e=2N-2a-b-2d, f=-N+2a+b+d.
            lower = max(1, n - 2 * a - b + 1)
            upper = min(n - 2, (2 * n - 2 * a - b - 1) // 2)
            for d in range(lower, upper + 1):
                e = 2 * n - 2 * a - b - 2 * d
                f = -n + 2 * a + b + d
                if min(c, e, f) < 1 or max(c, e, f) >= n:
                    continue
                assert a + b + c == n
                assert d + e + f == n
                assert 2 * a + b + 2 * d + e == 2 * n
                contributions.append(-sum(factorials[k] for k in (a, b, c, d, e, f)))
    log_partition = log_sum_exp(contributions)
    return {"N": n, "states": len(contributions), "pi_over_N_log_Z": math.pi * log_partition / n}


def local_two_three_check() -> dict[str, object]:
    n = 6
    factorials = [sp.Integer(1)]
    for k in range(1, n):
        factorials.append(sp.simplify(factorials[-1] * 2 * sp.sin(sp.pi * k / n)))
    left = sp.simplify(factorials[2] ** -6)
    right = sp.simplify(factorials[4] ** -3 * factorials[1] ** -6)
    assert left == sp.Rational(1, 27)
    assert right == sp.Rational(1, 216)
    assert sp.simplify(left / right) == 8

    table = []
    for size in (6, 12, 24, 48, 96, 192):
        logs = log_sine_factorials(size)
        left_log = -6 * logs[size // 3]
        # The three-tetrahedron fiber has one shared p, not three independent ones.
        right_terms = [
            -3 * (logs[2 * size // 3] + logs[p] + logs[size // 3 - p])
            for p in range(1, size // 3)
        ]
        right_log = log_sum_exp(right_terms)
        table.append({
            "N": size,
            "left_pi_over_N_log": math.pi * left_log / size,
            "right_pi_over_N_log": math.pi * right_log / size,
            "log_left_over_right": left_log - right_log,
        })
    return {"N6_left": str(left), "N6_right": str(right), "N6_ratio": 8, "asymptotic_comparison": table}


def main() -> None:
    mp.mp.dps = 60
    target = figure_eight_target()
    tetrahedra = 2 * mp.im(mp.polylog(2, mp.exp(mp.j * mp.pi / 3)))
    assert abs(target - tetrahedra) < mp.mpf("1e-50")
    rates = []
    for n in (32, 128, 512, 2048, 8192, 32768, 131072, 524288):
        rate = cone_recurrence_rate(n)
        rates.append({"steps": n, "rate": rate, "error": rate - float(target)})

    result = {
        "status": "numerical and algebraic checks; proofs are in the research note",
        "figure_eight_volume": mp.nstr(target, 55),
        "volume_cross_check_error": mp.nstr(abs(target - tetrahedra), 8),
        "quantum_operator": exact_operator_check(),
        "connected_sum_symbols": connected_sum_symbol_check(),
        "cone_recurrence": rates,
        "connected_sum_recurrence": [
            {
                "summands": r,
                "steps": 32768,
                "rate": cone_recurrence_rate(32768, r),
                "target": r * float(target),
            }
            for r in (2, 3, 5)
        ],
        "formal_quantum_identities": quantum_pentagon_check(),
        "angle_state_sums": [figure_eight_angle_sum(n) for n in (12, 24, 48, 96)],
        "local_two_three_move": local_two_three_check(),
    }
    destination = Path(__file__).with_name("results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
