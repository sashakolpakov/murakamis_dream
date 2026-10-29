#!/usr/bin/env python3
"""Exact checks of the norm-root transfer, first-normal class, and period."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ

from audit_coherent_cut_and_ward_relative_class import substitute


def equal(a, b):
    # ANP unit multiples can give structurally different fraction normal forms.
    return not (a - b)


def dual_zero(values):
    return all(not a and not b for a, b in values)


def inverse_nilpotent(coefficients, field):
    n = len(coefficients)
    result = [field.one / coefficients[0]]
    for j in range(1, n):
        result.append(-sum((coefficients[i] * result[j - i]
                            for i in range(1, j + 1)), field.zero)
                      / coefficients[0])
    return result


def log_degree_n(coefficients, field):
    """Coefficient z^N log(sum_{j<N} f_j z^j), f_0=1."""
    n = len(coefficients)
    inverse = inverse_nilpotent(coefficients, field)
    return sum((field(j) * coefficients[j] * inverse[n - j]
                for j in range(1, n)), field.zero) / field(n)


def ordinary_product(a, b, field):
    return [sum((a[i] * b[j - i] for i in range(j + 1)), field.zero)
            for j in range(len(a))]


def dual_product(a, b, field, sign):
    """A[e,eps]/(eps^2,e^N-sign*eps), in its free basis."""
    n = len(a)
    result = [(field.zero, field.zero) for _ in range(n)]
    for i, (a0, a1) in enumerate(a):
        for j, (b0, b1) in enumerate(b):
            r = i + j
            if r < n:
                c0, c1 = result[r]
                result[r] = (c0 + a0 * b0, c1 + a0 * b1 + a1 * b0)
            else:
                c0, c1 = result[r - n]
                result[r - n] = (c0, c1 + sign * a0 * b0)
    return result


def dual_subtract(a, b):
    return [(a0 - b0, a1 - b1) for (a0, a1), (b0, b1) in zip(a, b)]


def audit_level(n):
    sign = (-1) ** (n + 1)
    k = QQ.cyclotomic_field(n)
    q = k.from_sympy(k.ext)
    field = k.frac_field("t", "v")
    t, v = field.gens
    qf = field.convert(q, k)
    # Generic exact H90 recursion: v^N=1+kappa_N*t^N.
    delta = sign * (v ** n - 1) / t ** n
    h = [field.one]
    denominator = field.one
    for j in range(1, n):
        denominator *= v * qf ** j - 1
        h.append(t ** j / denominator)
    assert equal(v * h[0], h[0] + t * delta * h[n - 1])
    count = 1
    for j in range(1, n):
        assert equal(v * qf ** j * h[j], h[j] + t * h[j - 1])
        count += 1
    f = [field.one]
    denominator = field.one
    for j in range(1, n):
        denominator *= 1 - qf ** j
        f.append((-t) ** j / denominator)
        assert equal(substitute(h[j], v, 1), f[j])
        count += 1

    # Entire first-normal correction, including constant/norm mark.
    inverse_f = inverse_nilpotent(f, field)
    logarithm_coefficient = log_degree_n(f, field)
    quotient_h = [-sign * logarithm_coefficient]
    for j in range(1, n):
        rhs_j = t ** n / n * qf ** j * inverse_f[j]
        quotient_h.append(rhs_j / (qf ** j - 1))
    correction = ordinary_product(f, quotient_h, field)
    fdual = [(value, field.zero) for value in f]
    gdual = list(zip(f, correction))
    alpha = [(field.one, field.zero), (t, field.zero)] + [
        (field.zero, field.zero) for _ in range(n - 2)]
    normalized = [(field.one, -t ** n / n), (t, -t ** (n + 1) / n)] + [
        (field.zero, field.zero) for _ in range(n - 2)]

    def sigma(coefficients):
        return [(a * qf ** j, b * qf ** j)
                for j, (a, b) in enumerate(coefficients)]

    source = dual_subtract(sigma(fdual), dual_product(alpha, fdual, field, sign))
    expected = [(field.zero, -t ** n / n)] + [
        (field.zero, field.zero) for _ in range(n - 1)]
    assert dual_zero(dual_subtract(source, expected))
    assert dual_zero(dual_subtract(sigma(gdual),
                                  dual_product(normalized, gdual, field, sign)))
    # This is B_0(g)=0, the first-normal norm-one character.
    assert not (n * correction[0] + sign * n * logarithm_coefficient)
    count += 3
    return {"N": n, "exact_H90_and_first_normal_checks": count}


def ghost_cocycle_checks():
    field = QQ.frac_field("t", "u")
    t, u = field.gens
    count = 0
    for n in range(2, 10):
        sign = (-1) ** (n + 1)
        a = [field.one] + [t ** j / (j + 1) for j in range(1, n)]
        b = [field.one] + [
            field(j + 2) * u ** j / (j + 3) for j in range(1, n)]
        a0, b0 = t + 2, u - 3
        wrap = sum((a[i] * b[n - i] for i in range(1, n)), field.zero)
        product0 = a0 + b0 + sign * n * wrap
        product = ordinary_product(a, b, field)
        char_a = a0 + sign * n * log_degree_n(a, field)
        char_b = b0 + sign * n * log_degree_n(b, field)
        char_product = product0 + sign * n * log_degree_n(product, field)
        assert char_product == char_a + char_b
        edge = [field.one, t] + [field.zero] * (n - 2)
        assert sign * n * log_degree_n(edge, field) == t ** n
        count += 2
    return count


def scalar_period_checks():
    meridian, t, b = sp.symbols("M t b", nonzero=True)
    kappa = meridian - 1 / meridian
    count = 0
    for n in range(2, 11):
        kn = meridian ** n - meridian ** -n
        un = sp.cancel(kn / kappa)
        norm = 1 + kn * t ** n
        assert sp.cancel(norm.subs(t, meridian) - meridian ** (2 * n)) == 0
        assert sp.cancel((1 + kappa * meridian) ** n
                         - norm.subs(t, meridian)) == 0
        pullback = sp.diff(norm, t) / (n * kappa * norm)
        assert sp.cancel(pullback - un * t ** (n - 1) / norm) == 0
        power = ((1 + kappa * b) ** n - 1) / kn
        assert sp.cancel(sp.diff(power, b) / (1 + kn * power)
                         - n / un / (1 + kappa * b)) == 0
        # Endpoint period with the identity logarithm: Log(M^{2N})=2N Log M.
        assert sp.cancel((2 * n * sp.log(meridian)) / (n * kappa)
                         - 2 * sp.log(meridian) / kappa) == 0
        # The forbidden regular derivation has nonzero constant RHS 2N sign.
        assert sp.diff((-1) ** (n + 1) * kn, meridian).subs(
            meridian, 1) == 2 * n * (-1) ** (n + 1)
        count += 6
    ell = 2 * sp.log(meridian) / kappa
    assert sp.simplify(sp.diff(ell, meridian)
                       + ell * sp.diff(kappa, meridian) / kappa
                       - 2 / (meridian * kappa)) == 0
    gap = sp.Symbol("kappa")
    assert sp.series(2 * sp.asinh(gap / 2) / gap, gap, 0, 4).removeO() == (
        1 - gap ** 2 / 24)
    return count + 2


def main():
    levels = [audit_level(n) for n in range(2, 11)]
    result = {
        "status": "all exact checks passed",
        "finite_levels": levels,
        "H90_and_first_normal_checks": sum(
            row["exact_H90_and_first_normal_checks"] for row in levels),
        "first_normal_cocycle_checks": ghost_cocycle_checks(),
        "peripheral_period_and_connection_checks": scalar_period_checks(),
        "scope": (
            "Norm-root unit-group transfer, first-normal affine character, "
            "literal factorial H90 gauge and marked peripheral relative "
            "period. No internal knot Gaussian or Bloch-period selection "
            "is inferred."
        ),
    }
    result["total_exact_checks"] = sum(
        value for key, value in result.items()
        if key.endswith("_checks") and isinstance(value, int))
    path = Path(__file__).with_name("cyclic_ward_norm_root_period_results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
