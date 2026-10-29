#!/usr/bin/env python3
"""Exact audit of the actual-source Newton/canonical-transform identities.

This verifies algebra, interpolation, boundaries, and source obstruction.
It does not infer an asymptotic or geometric branch selection from tests.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ

from audit_whole_source_newton_transport import (
    ONE, add, mon, mul, qa, qm, qs, scale, shift,
)


def qmon(q=0, u=0, e=0, c=1):
    return {(q, u, e): c} if c else {}


def generic_coefficient_checks():
    # Normal order Q^q u^a E^b; E u=Q u E.
    u = qmon(u=1)
    de = qa(qmon(q=-2, u=-2), qmon(c=-1),
            qmon(q=1, c=-1), qmon(q=3, u=2))
    x = qa(qmon(e=-1), qmon(q=1, u=1), qmon(q=-1, u=-1))
    s = qa(qmon(q=1, u=1), qmon(u=-1), qm(de, qmon(e=1)))
    z = qa(qmon(u=1, e=-1), qmon(q=1, u=2),
           qmon(q=2, u=2), qm(qmon(q=1, u=1), qm(de, qmon(e=1))))
    assert qm(u, qa(x, qs(s, q=1))) == qa(
        z, qmon(q=1), qmon(q=-1))
    assert qa(x, qmon(q=1, u=1, c=-1),
              qmon(q=-1, u=-1, c=-1)) == qmon(e=-1)
    checks = 2

    def on_delta(operator, m):
        # A coefficient at input index m gives output index n=m-b.
        out = {}
        for (a, b, step), c in operator.items():
            n = m - step
            out = add(out, mon(q=a + b * n, y=n, c=c))
        return out

    def difference(poly, power):
        return shift(poly, power)

    def generating_action(which, poly):
        if which == "x":
            return add(mul(mon(y=1), poly),
                       mul(mon(q=1), difference(poly, 1)),
                       mul(mon(q=-1), difference(poly, -1)))
        if which == "s":
            bracket = add(
                difference(poly, -2), scale(poly, -1),
                mul(mon(q=1, c=-1), poly),
                mul(mon(q=1), difference(poly, 2)))
            return add(mul(mon(q=1), difference(poly, 1)),
                       difference(poly, -1),
                       mul(mon(y=-1), bracket))
        bracket = add(
            difference(poly, -1), scale(difference(poly, 1), -1),
            mul(mon(q=1, c=-1), difference(poly, 1)),
            mul(mon(q=1), difference(poly, 3)))
        return add(
            mul(mon(q=1, y=1), difference(poly, 1)),
            mul(add(mon(q=1), mon(q=2)), difference(poly, 2)),
            mul(mon(y=-1), bracket))

    for n in range(13):
        de_n = add(mon(q=-2 * n), mon(c=-1), mon(q=1, c=-1),
                   mon(q=2 * n + 1))
        expected = {
            "x": add(mon(y=n + 1), mon(q=n + 1, y=n),
                     mon(q=-n - 1, y=n)),
            "s": add(mon(q=n + 1, y=n), mon(q=-n, y=n),
                     mul(de_n, mon(y=n - 1))),
            "z": add(mon(q=n + 1, y=n + 1),
                     mon(q=2 * n + 1, y=n), mon(q=2 * n + 2, y=n),
                     mul(de_n, mon(q=n, y=n - 1))),
        }
        for which, operator in (("x", x), ("s", s), ("z", z)):
            assert on_delta(operator, n) == expected[which]
            assert generating_action(which, mon(y=n)) == expected[which]
            assert all(power >= 0 for _, power in expected[which])
            checks += 3
    return checks


def interpolation_checks():
    field = QQ.frac_field("Q")
    q = field.gens[0]
    # Arbitrary exact rational coefficient sequence. This tests the algebraic
    # interpolation theorem, not an asserted knot formula.
    coeff = [
        field.one, q + q ** -1, (1 - q) / (1 + q),
        -q ** 3, (1 + q ** 2) / (1 - q ** 3), q ** -4,
        q ** 2 - q + 3,
    ]
    nodes = [q ** j + q ** (-j) for j in range(1, 10)]

    def kernel(n, x):
        out = field.one
        for a in nodes[:n]:
            out *= x - a
        return out

    values = [
        sum((coeff[n] * kernel(n, x) for n in range(min(j + 1, len(coeff)))),
            field.zero)
        for j, x in enumerate(nodes)
    ]
    checks = 0
    extracted = []
    for n in range(len(coeff)):
        residual = values[n] - sum(
            (extracted[j] * kernel(j, nodes[n]) for j in range(n)), field.zero)
        extracted.append(residual / kernel(n, nodes[n]))
        assert extracted[-1] == coeff[n]
        checks += 1
        if n <= 4:
            divided = field.zero
            for j in range(n + 1):
                denominator = field.one
                for r in range(n + 1):
                    if r != j:
                        denominator *= nodes[j] - nodes[r]
                divided += values[j] / denominator
            assert divided == coeff[n]
            checks += 1

    # Confluent extraction when nodes repeat, by the residue formula.
    x = sp.Symbol("x")
    repeated_nodes = [sp.Integer(3), sp.Integer(-1), sp.Integer(-1),
                      sp.Integer(2), sp.Integer(3)]
    polynomial = x ** 6 - 2 * x ** 3 + 7 * x + 2
    basis = [sp.Integer(1)]
    for a in repeated_nodes:
        basis.append(sp.expand(basis[-1] * (x - a)))
    remaining = polynomial
    confluent = []
    for n in range(6, -1, -1):
        # Extend the monic basis arbitrarily beyond the repeated nodes.
        while len(basis) <= n:
            basis.append(sp.expand(basis[-1] * (x - (len(basis) + 1))))
        c = sp.Poly(remaining, x).nth(n)
        confluent.insert(0, c)
        remaining = sp.expand(remaining - c * basis[n])
    assert remaining == 0
    for m in range(5):
        quotient = polynomial / basis[m + 1]
        total = sum(sp.residue(quotient, x, a)
                    for a in set(repeated_nodes[:m + 1]))
        assert sp.simplify(total - confluent[m]) == 0
        checks += 1
    return checks


def canonical_checks():
    u, e, y, ell = sp.symbols("u e Y L", nonzero=True)
    x = e ** -1 + u + u ** -1
    s = u + u ** -1 + (u - u ** -1) ** 2 * e
    z = u * (x + s) - 2
    hm = e * (u - 1) ** 2 + u
    hp = e * (u + 1) ** 2 + u
    checks = 0
    for expression in (
        x ** 2 + s ** 2 + z ** 2 - x * s * z - 4,
        (z + 2) / (x + s) - u,
        1 / (x - u - 1 / u) - e,
        x + s - hm * hp / (e * u ** 2),
        s - (x * x - x - 4) - (e - 1) * hm * hp / (e ** 2 * u ** 2),
    ):
        assert sp.factor(expression) == 0
        checks += 1
    for sub, point in (
        ({e: -u / (u - 1) ** 2}, (2, -2, -2)),
        ({e: -u / (u + 1) ** 2}, (-2, 2, -2)),
    ):
        for coordinate, value in zip((x, s, z), point):
            assert sp.factor(coordinate.subs(sub) - value) == 0
            checks += 1

    uu = (y * ell + 1) / (y + ell)
    ee = y * (y + ell) * (y * ell + 1) / (ell * (y * y - 1) ** 2)
    full_coordinates = (y + 1 / y, ell + 1 / ell,
                        y * ell + 1 / (y * ell))
    for transformed, original in zip((x, s, z), full_coordinates):
        assert sp.factor(transformed.subs({u: uu, e: ee}) - original) == 0
        checks += 1
    for invariant in (uu, ee):
        reflected = invariant.subs({y: 1 / y, ell: 1 / ell}, simultaneous=True)
        assert sp.factor(reflected - invariant) == 0
        checks += 1
    bracket = (
        ell * sp.diff(ee, ell) * y * sp.diff(uu, y)
        - y * sp.diff(ee, y) * ell * sp.diff(uu, ell)
    ) / (ee * uu)
    assert sp.factor(bracket - 1) == 0
    checks += 1

    # Rational identities underlying the dilogarithmic logarithm derivatives.
    longitude = (u * y - 1) / (y - u)
    assert sp.factor(-((1 - u * y) * (1 - u / y)) / u
                     - (y + 1 / y - u - 1 / u)) == 0
    assert sp.factor((1 - 1 / y) * (1 - u * y)
                     / ((1 - y) * (1 - u / y)) - longitude) == 0
    checks += 2

    # First-order signed-complete branch, with the retained second-order
    # numerator/denominator in e.
    lam, eps = sp.symbols("lambda eps")
    near = {y: 1 + eps, ell: -1 + lam * eps}
    assert sp.simplify(sp.limit(uu.subs(near), eps, 0)
                       - (lam - 1) / (lam + 1)) == 0
    assert sp.simplify(sp.limit(ee.subs(near), eps, 0)
                       - (1 - lam ** 2) / 4) == 0
    checks += 2
    return checks


def root_source_obstruction_checks():
    checks = 0
    for n in range(2, 13):
        field = QQ.cyclotomic_field(n)
        q = field.from_sympy(field.ext)
        # f0 and f1 coefficient dictionaries in the actual Laurent Y.
        f0 = {0: field.one, 1: -field.one}
        f1 = {n: field.one, 1 - n: -field.one}
        for f in (f0, f1):
            assert {-exponent + 1: -value for exponent, value in f.items()} == f
            assert all(
                value * (q ** exponent + q ** (1 - exponent) - 1 - q)
                == field.zero for exponent, value in f.items())
            checks += 2
        # F1 is the exact Laurent quotient f1/(1-Y).
        quotient = {exponent: -field.one for exponent in range(1 - n, n)}
        for j in range(1, n):
            value = sum((c * q ** (j * exponent)
                         for exponent, c in quotient.items()), field.zero)
            assert value == field.one
            checks += 1
        at_one = sum(quotient.values(), field.zero)
        cut = -sum((field(exponent) * value for exponent, value in f1.items()),
                   field.zero)
        assert at_one == cut == field(1 - 2 * n)
        checks += 1
    return checks


def main():
    result = {
        "status": "all exact checks passed",
        "generic_coefficient_and_power_series_checks": generic_coefficient_checks(),
        "interpolation_and_confluent_checks": interpolation_checks(),
        "classical_canonical_and_kernel_checks": canonical_checks(),
        "root_source_obstruction_checks": root_source_obstruction_checks(),
        "scope": (
            "Exact transform, boundary, and actual-source selection identities. "
            "No geometric support, coefficient WKB selection, or volume "
            "asymptotic is inferred."
        ),
    }
    result["total_exact_checks"] = sum(
        value for key, value in result.items() if key.endswith("_checks"))
    path = Path(__file__).with_name("newton_actual_source_canonical_transform_results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
