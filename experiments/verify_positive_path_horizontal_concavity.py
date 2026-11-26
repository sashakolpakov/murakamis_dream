#!/usr/bin/env python3
"""Exact algebraic steps in the positive-path horizontal-concavity proof.

This checks the polynomial positivity certificate and scalar constants.
It does not replace the written return-angle and period argument.
"""

from fractions import Fraction as F
from math import comb
import hashlib
import json
from pathlib import Path


def add(p, q):
    return [
        (p[i] if i < len(p) else F(0))
        + (q[i] if i < len(q) else F(0))
        for i in range(max(len(p), len(q)))
    ]


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def scale(p, c):
    return [c * x for x in p]


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def main():
    # All lists contain coefficients in increasing degree.
    a = [F(1), F(1)]
    b = [F(1), F(0), F(3)]
    p = mul(mul(a, b), [F(1), F(-1), F(-1), F(2)])
    q = mul(b, [F(1), F(1), F(-1), F(-2)])
    r = list(map(F, [1, -3, -3, 15, 3, -21, 0, 12]))
    lhs = add(scale(mul(p, p), F(2)),
              scale(mul([F(1), F(0), F(-1)], mul(q, q)), F(-1)))
    rhs = mul(mul(a, mul(b, b)), r)
    assert trim(lhs) == trim(rhs), "Factorization (19)"

    # Substitute u=1/3+x/6, then change from powers to Bernstein basis.
    power = [
        sum(r[k] * comb(k, j) * F(1, 3) ** (k - j) * F(1, 6) ** j
            for k in range(j, 8))
        for j in range(8)
    ]
    bernstein = [
        sum(power[j] * F(comb(i, j), comb(7, j)) for j in range(i + 1))
        for i in range(8)
    ]
    expected = [
        F(130, 729), F(547, 3402), F(260, 1701), F(167, 1080),
        F(209, 1260), F(125, 672), F(3, 14), F(1, 4),
    ]
    assert bernstein == expected, "Bernstein expansion (21)--(22)"
    assert all(x > 0 for x in bernstein), "Strict positivity on [1/3,1/2]"

    comparisons = [
        ("kappa upper bound after squaring", F(3 * 97**2), F(2 * 119**2)),
        ("cosine comparison after squaring", F(3 * 83**2), F(144**2)),
        ("positive last factor of P", F(0), 1 - F(1, 2) - F(1, 2)**2),
        ("positive last factor of Q", F(0), 1 - F(1, 2)**2 - 2*F(1, 2)**3),
    ]
    for name, left, right in comparisons:
        assert left < right, name
    assert F(1, 2) + F(11, 144) == F(83, 144)

    script = Path(__file__).resolve()
    root = script.parents[1]
    paths = [
        script,
        root / "notes/research_positive_path_horizontal_concavity.md",
        root / "notes/research_geometric_phase_maximum_principle.md",
    ]
    record = {
        "status": "passed",
        "method": "exact Fraction arithmetic",
        "scope": "Finite algebra and constants; all-path inference has a written proof.",
        "factorization_coefficients": [str(x) for x in trim(lhs)],
        "bernstein_coefficients": [str(x) for x in bernstein],
        "positive_polynomial_lower_bound": str(min(bernstein)),
        "strict_comparisons": [
            {"name": name, "left": str(left), "right": str(right),
             "positive_difference": str(right - left)}
            for name, left, right in comparisons
        ],
        "sha256": {
            str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in paths
        },
    }
    output = root / "repro/results/research-positive-path-horizontal-concavity.json"
    output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({
        "status": "passed", "factorization": True,
        "positive_bernstein_coefficients": 8,
        "strict_scalar_comparisons": len(comparisons),
        "output": str(output.relative_to(root)),
    }))


if __name__ == "__main__":
    main()
