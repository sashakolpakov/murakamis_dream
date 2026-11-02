#!/usr/bin/env python3
"""Bounded exact checks for strict Newton supports and stationary parameters.

This program does not prove the boundary argument, optimizer theorem,
holomorphic interpolation, or asymptotic estimates. It imports no project
proof checker and uses no floating-point optimization.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
from math import isqrt
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INPUT_FILES = (
    "papers/strict-newton-profiles/main.tex",
    "papers/strict-newton-profiles/syntax.tex",
    "papers/strict-newton-profiles/variation.tex",
    "papers/strict-newton-profiles/profiles.tex",
    "papers/strict-newton-profiles/figures/reduced-tree.tex",
    "papers/strict-newton-profiles/check.py",
)


def hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in INPUT_FILES}


def prime(p):
    return p >= 2 and all(p % r for r in range(2, isqrt(p) + 1))


def prime_divisors(n):
    out = []
    for k in range(2, n + 1):
        if n % k == 0:
            out.append(k)
            while n % k == 0:
                n //= k
        if n == 1:
            break
    return out


def generator(p):
    divisors = prime_divisors(p - 1)
    return next(g for g in range(2, p)
                if all(pow(g, (p - 1) // k, p) != 1 for k in divisors))


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim([x % p for x in c])


def scale(a, t, p):
    return trim([x * t % p for x in a])


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return trim(c)


def remainder(a, monic, p):
    a = trim(a)
    while len(a) >= len(monic):
        k, t = len(a) - len(monic), a[-1]
        for j, x in enumerate(monic):
            a[k + j] = (a[k + j] - t * x) % p
        a = trim(a)
    return a


def newton_coordinates(a, basis, p):
    a = list(a) + [0] * (len(basis) - len(a))
    result = [0] * len(basis)
    for r in range(len(basis) - 1, -1, -1):
        t = a[r] * pow(basis[r][-1], -1, p) % p
        result[r] = t
        for j, x in enumerate(basis[r]):
            a[j] = (a[j] - t * x) % p
    assert not any(a)
    return result


def finite_quotient_checks():
    cases = []
    count = 0
    for n in range(2, 11):
        primes = []
        k = 1
        while len(primes) < 2:
            p = 4 * n * k + 1
            if prime(p):
                primes.append(p)
            k += 1
        for p in primes:
            gen = generator(p)
            q = pow(gen, (p - 1) // (2 * n), p)
            ii = pow(gen, (p - 1) // 4, p)
            assert pow(q, n, p) == p - 1 and ii * ii % p == p - 1
            nodes = [(pow(q, 2 * a + 1, p) +
                      pow(q, -(2 * a + 1), p)) % p for a in range(n)]
            s = [1]
            for a in range(1, n):
                s.append(s[-1] * (pow(q, a, p) - pow(q, -a, p))
                         * pow(ii, -1, p) % p)
            assert all(s)
            # Independent Chebyshev recurrence gives the full monic quotient.
            c0, c1 = [2], [0, 1]
            for _ in range(1, n):
                c0, c1 = c1, add(mul([0, 1], c1, p), scale(c0, -1, p), p)
            quotient = add(c1, [2], p)
            root_product = [1]
            for c in nodes:
                root_product = mul(root_product, [-c % p, 1], p)
            assert quotient == root_product
            # Repeated roots are retained in polynomial division.
            basis, b = [], [1]
            for r in range(n):
                basis.append(scale(b, pow(s[r] * s[r] % p, -1, p), p))
                b = mul(b, [nodes[r], -1 % p], p)
            for i, j in itertools.product(range(n), repeat=2):
                actual = newton_coordinates(
                    remainder(mul(basis[i], basis[j], p), quotient, p),
                    basis, p)
                expected = [0] * n
                if i + j < n:
                    for r in range(max(i, j), i + j + 1):
                        den = s[i] * s[j] * s[r-i] * s[r-j] * s[i+j-r] % p
                        expected[r] = s[i+j] * s[r] * pow(den, -1, p) % p
                assert actual == expected, (n, p, i, j, actual, expected)
                assert actual[-1] == int(i + j == n - 1)
                count += 1
            cases.append({"N": n, "prime": p, "distinct_nodes": len(set(nodes)),
                          "polynomial_degree": len(quotient) - 1})
    return {"cases": cases, "products_and_closing_coefficients": count}


def product_support(a, b, d):
    # Enumerate each original allowed gate, not the interval compiler.
    return {r for i in a for j in b if i+j <= d
            for r in range(max(i, j), i+j+1)}


def support_checks():
    intervals = hubs = boundary_atoms = 0
    parity_examples = []
    for n in range(2, 10):
        d, m = n - 1, (n - 1) // 2
        for lo1 in range(n):
            for hi1 in range(lo1, n):
                for lo2 in range(n):
                    for hi2 in range(lo2, n):
                        actual = product_support(range(lo1, hi1+1),
                                                 range(lo2, hi2+1), d)
                        expected = (set() if lo1+lo2 > d else
                                    set(range(max(lo1, lo2), min(d, hi1+hi2)+1)))
                        assert actual == expected
                        intervals += 1
        high_leaf = range(d-m, d+1)
        boundary = product_support(high_leaf, high_leaf, d)
        assert boundary == (set(range(m, d+1)) if n % 2 else set())
        parity_examples.append({"N": n, "turned_leaf_square_support": sorted(boundary)})
        assert not product_support(range(m+1, n), range(m+1, n), d)
        for inds in itertools.product(range(n), repeat=3):
            left = product_support(product_support({inds[0]}, {inds[1]}, d),
                                   {inds[2]}, d)
            right = product_support({inds[0]},
                                    product_support({inds[1]}, {inds[2]}, d), d)
            good = all(a+b <= d for a, b in itertools.combinations(inds, 2))
            expected = set(range(max(inds), min(d, sum(inds))+1)) if good else set()
            assert left == right == expected
            hubs += 1
    # Exhaustive rational check of the local nonvertex-flat gate classification.
    den = 16
    for xi, yi, zi in itertools.product(range(1, den), repeat=3):
        x, y, z = F(xi, den), F(yi, den), F(zi, den)
        if not max(x, y) <= z <= x+y <= 1:
            continue
        p, q, r, w = z-x, z-y, x+y-z, 1-x-y
        atoms = [(y, x, w), (p, q, 2*r+w), (p+q, r, r+w)]
        assert all(sum(a) == 1 and min(a) >= 0 for a in atoms)
        if min(p, q, r, w) == 0:
            assert any(sum(t > 0 for t in a) == 2 for a in atoms)
            boundary_atoms += 1
    return {"interval_pairs": intervals, "three_input_resolutions": hubs,
            "rational_nonvertex_flat_gate_cases": boundary_atoms,
            "parity_boundary_examples": parity_examples}


def rational_port_checks():
    product_count = harmonic_count = 0
    for x in [F(1, 2), F(3, 4), F(1), F(5, 4)]:
        for b1, b2 in itertools.product([F(k, 4) for k in range(-8, 9)], repeat=2):
            s = b1 + b2
            y1sq, y2sq = 1+b1*b1-x*x, 1+b2*b2-x*x
            if s <= 0 or y1sq <= 0 or y2sq <= 0:
                continue
            bo = (b1*b2+x*x-1)/s
            yosq = y1sq*y2sq/(s*s)
            assert yosq == 1+bo*bo-x*x
            assert y1sq == s*(b1-bo) and y2sq == s*(b2-bo)
            product_count += 1
    for b in [F(1, 3), F(1, 2), F(1), F(2)]:
        for k in range(1, 12):
            u = b * F(k, 12)
            v = u*b/(b-u)
            assert 0 < u < b and 1/u == 1/v+1/b
            assert ((-u)*b+1-1)/(b-u) == -v
            harmonic_count += 1
    return {"product_hyperboloid_identities": product_count,
            "harmonic_responses": harmonic_count}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "build" / "check")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    destination = args.output / "summary.json"
    destination.unlink(missing_ok=True)
    if not __debug__:
        raise SystemExit("Run without -O: this checker requires assertions.")
    before = hashes()
    result = {
        "scope": "Bounded exact finite algebra, support and rational parameter checks.",
        "excluded_claims": [
            "No all-level theorem is inferred from these examples.",
            "No optimizer, analytic interpolation, exponential estimate or volume is numerically certified.",
            "No independent physical crossing or Casimir implementation is claimed here.",
        ],
        "finite_quotient": finite_quotient_checks(),
        "supports": support_checks(),
        "rational_parameters": rational_port_checks(),
    }
    after = hashes()
    assert before == after, "An input changed during the check."
    result["source_hashes"] = before
    result["python"] = sys.version.split()[0]
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"summary": str(destination),
                      "finite_products": result["finite_quotient"]["products_and_closing_coefficients"],
                      "interval_pairs": result["supports"]["interval_pairs"],
                      "three_input_resolutions": result["supports"]["three_input_resolutions"],
                      "rational_parameters": result["rational_parameters"]}, sort_keys=True))


if __name__ == "__main__":
    main()
