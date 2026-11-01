#!/usr/bin/env python3
"""Check the finite identities used in the moving-meridian source bounds.

The trace is computed in two ways: ordinary polynomial division in a
cyclotomic field, and the Fourier formula. Separate integer calculations
check the interval-tail inequality and the adjacent-level path map.
These finite checks do not prove the uniform analytic or geometric bounds.
Requires SymPy and mpmath.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from itertools import combinations_with_replacement
import json
from math import comb
from pathlib import Path

import mpmath as mp
import sympy as sp


def chebyshev_monic(n, z):
    previous, current = sp.Integer(2), z
    for _ in range(1, n):
        previous, current = current, sp.expand(z * current - previous)
    return current


def multiply(a, b, zero):
    out = [zero] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def exact_level(n):
    z, delta, root = sp.symbols("z delta root")
    field = sp.QQ.algebraic_field(sp.CRootOf(sp.cyclotomic_poly(2 * n, root), 0))
    q, zero, one = field.unit, field.zero, field.one
    m = (n - 1) // 2
    basis = [[one]]
    for k in range(m):
        node = q ** (2 * k + 1) + q ** (-2 * k - 1)
        denominator = 2 - q ** (2 * k + 2) - q ** (-2 * k - 2)
        basis.append(multiply(basis[-1], [node / denominator, -one / denominator], zero))
    modulus = sp.Poly(chebyshev_monic(n, z) + 2 + delta, z, delta, domain=field)

    patterns = set()
    for count in range(2, 9):
        patterns.add((m,) * count)
        patterns.add(tuple(sorted([max(0, m - 1)] + [m] * (count - 1))))
        patterns.add(tuple(sorted([k % (m + 1) for k in range(count)])))
    checked = aliases = returns = 0
    for indices in sorted(patterns):
        coefficients = [one]
        for k in indices:
            coefficients = multiply(coefficients, basis[k], zero)
        degree = len(coefficients) - 1
        polynomial = sp.Poly.from_dict({(i, 0): a for i, a in enumerate(coefficients) if a},
                                      (z, delta), domain=field)
        remainder = polynomial.rem(modulus)
        direct = {power[1]: value * ((-1) ** (n - 1) * n * n)
                  for power, value in remainder.rep.to_dict().items() if power[0] == n - 1}
        direct = {k: v for k, v in direct.items() if v}

        # Expand the actual polynomial after z=-(u+u^-1), independently
        # of the closed q-binomial formula for individual Newton factors.
        laurent = {k: zero for k in range(-degree, degree + 1)}
        for power, value in enumerate(coefficients):
            for k in range(power + 1):
                laurent[power - 2 * k] += value * ((-1) ** power * comb(power, k))
        assert all(laurent[k] == laurent[-k] for k in laurent)
        count_aliases = (degree + 1) // n
        formula = {}
        for ell in range(1, count_aliases + 1):
            difference = laurent.get(ell * n - 1, zero) - laurent.get(ell * n + 1, zero)
            weight = sp.Poly(sp.chebyshevu(ell - 1, 1 + delta / 2), delta, domain=sp.QQ)
            factor = n * n * (-1) ** ((n - 1) * (ell + 1)) * difference
            for (k,), value in weight.rep.to_dict().items():
                formula[k] = formula.get(k, zero) + factor * field.convert(value)
        formula = {k: v for k, v in formula.items() if v}
        assert direct == formula, ("Fourier trace", n, indices)
        checked += 1
        aliases += count_aliases > 1
        returns += any(k > 0 for k in direct)
    return {"N": n, "exact_trace_identities": checked,
            "identities_with_multiple_aliases": aliases,
            "identities_with_nonconstant_deformation": returns}


def interval_tail_checks():
    cases = comparisons = 0
    for m in range(4):
        for count in range(1, 6):
            for radii in combinations_with_replacement(range(m + 1), count):
                sequence = {0: 1}
                for radius in radii:
                    following = Counter()
                    for k, value in sequence.items():
                        for shift in range(-radius, radius + 1):
                            following[k + shift] += value
                    sequence = following
                for k in range(m, sum(radii) + 2):
                    value = sequence.get(k, 0)
                    difference = value - sequence.get(k + 2, 0)
                    assert value <= (2 * m + 1) ** count * difference, (m, radii, k)
                    comparisons += 1
                cases += 1
    return {"interval_convolutions": cases, "tail_inequalities": comparisons}


def paths(indices, level):
    partial = [(indices[0],)]
    for leaf in indices[1:]:
        following = []
        for path in partial:
            incoming = path[-1]
            if incoming + leaf < level:
                following.extend(path + (out,) for out in range(max(incoming, leaf), incoming + leaf + 1))
        partial = following
    return [p for p in partial if p[-1] == level - 1]


def adjacent_path_checks():
    total = families = 0
    for n in (4, 6, 8):
        m = (n - 2) // 2
        for count in range(3, 6):
            for indices in combinations_with_replacement(range(m + 1), count):
                if sum(indices) < n - 1:
                    continue
                images = Counter()
                for path in paths(indices, n - 1):
                    first = next(j for j in range(1, count) if path[j - 1] + indices[j] > path[j])
                    image = tuple(value + (j >= first) for j, value in enumerate(path))
                    assert image[0] == indices[0] and image[-1] == n - 1
                    for j in range(1, count):
                        incoming, leaf, out = image[j - 1], indices[j], image[j]
                        assert incoming + leaf < n
                        assert max(incoming, leaf) <= out <= incoming + leaf
                    images[image] += 1
                    total += 1
                assert max(images.values(), default=0) <= count - 1
                families += 1
    return {"input_families": families, "mapped_positive_paths": total}


def factorial_checks():
    comparisons = 0
    for n in range(4, 34, 2):
        ratio = mp.mpf(1)
        for r in range(n - 1):
            if r:
                ratio *= mp.sin(mp.pi * r / (n - 1)) / mp.sin(mp.pi * r / n)
            assert ratio >= mp.mpf(1) / (n - 1)
            assert ratio <= mp.sqrt(2)
            comparisons += 1
    return {"even_levels": list(range(4, 34, 2)), "ratio_bounds": comparisons}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("main_meridian_source_bounds_results.json"))
    args = parser.parse_args()
    mp.mp.dps = 80
    result = {
        "scope": "Finite exact identities and combinatorial checks; not a proof of uniform source bounds or geometric identification.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {"sympy": sp.__version__, "mpmath": mp.__version__},
        "trace_identities": [exact_level(n) for n in range(2, 9)],
        "integer_interval_tail": interval_tail_checks(),
        "integer_adjacent_path_map": adjacent_path_checks(),
        "factorial_ratios_80_digits": factorial_checks(),
        "result": "all checks passed",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"result": str(args.output),
                      "exact_trace_identities": sum(r["exact_trace_identities"] for r in result["trace_identities"]),
                      "mapped_positive_paths": result["integer_adjacent_path_map"]["mapped_positive_paths"]}, indent=2))


if __name__ == "__main__":
    main()
