#!/usr/bin/env python3
"""Exact cyclotomic audits of intrinsic monodromy and norm descent."""

import json
from pathlib import Path

import sympy as sp


def audit(n):
    q = sp.Symbol("q")
    phi = sp.Poly(sp.cyclotomic_poly(n, q), q, domain=sp.QQ)

    def red(value):
        p = value if isinstance(value, sp.Poly) else sp.Poly(value, q, domain=sp.QQ)
        return p.rem(phi)

    zero, one = red(0), red(1)
    scale, c = sp.Rational(2, 3), sp.S.One
    xs = [red(scale*q**j) for j in range(n)]
    cs = [[[zero, -one], [one, red(c)-x]] for x in xs]
    inverses = [[[red(c)-x, one], [-one, zero]] for x in xs]

    def mul(a, b):
        return [[red(sum((a[i][k]*b[k][j] for k in range(2)), zero))
                 for j in range(2)] for i in range(2)]

    identity = [[one, zero], [zero, one]]
    h = identity
    for matrix in cs:
        h = mul(h, matrix)
    s0, s1 = sp.Integer(2), c
    for _ in range(n):
        s0, s1 = s1, c*s1-s0
    trace = red(s0-scale**n)
    assert red(h[0][0]+h[1][1]) == trace
    assert red(h[0][0]*h[1][1]-h[0][1]*h[1][0]) == one

    # On the simple central component, v^2=trace*v-1.
    def eigen_mul(a, b):
        return (red(a[0]*b[0]-a[1]*b[1]),
                red(a[0]*b[1]+a[1]*b[0]+trace*a[1]*b[1]))

    numerator, denominator, current = (one, zero), one, h
    for matrix, inverse in zip(cs, inverses):
        following = mul(mul(inverse, current), matrix)
        # e=(H_12,v-H_11); T e=a e with a=(sigma(H_11)-v)/H_12.
        numerator = eigen_mul(numerator, (following[0][0], -one))
        denominator = red(denominator*current[0][1])
        current = following
    assert current == h
    assert not denominator.is_zero
    assert numerator == (zero, denominator)

    # Hilbert 90 in the same etale orbit, without assuming n is prime.
    fs = [one-x for x in xs]
    ratios = [red(fs[j]*sp.invert(fs[(j+1) % n], phi)) for j in range(n)]
    norm = one
    for ratio in ratios:
        norm = red(norm*ratio)
    assert norm == one
    averages = []
    for start in (0, 1):
        prefix, average = one, zero
        for j in range(n):
            average = red(average+prefix)
            prefix = red(prefix*ratios[(start+j) % n])
        averages.append(average)
        assert average == red(fs[start]*n/(1-scale**n))
    assert red(ratios[0]*averages[1]) == averages[0]

    # The cyclic lattice removes a pole above u=1 but retains 1/n at x=1.
    p0 = red(sum(scale**j for j in range(n)))
    p1 = red(sum((xs[1]**j for j in range(n)), zero))
    assert red((red(scale)-one)*p0-(xs[1]-one)*p1) == zero
    for k in range(n):
        at_root = red(sum(q**(k*j) for j in range(n)))
        assert at_root == red(n if k == 0 else 0)
    return {"level": n, "cyclotomic_degree": phi.degree(),
            "central_trace_constant": str(s0),
            "central_polynomial_exact": True, "eigenline_norm_exact": True,
            "hilbert_90_exact": True, "pole_lattice_extension_exact": True}


def main():
    records = [audit(n) for n in (3, 5, 9, 15)]
    result = {"scope": "Exact algebraic diagnostics; no knot-state identification asserted.",
              "records": records}
    Path(__file__).with_name("intrinsic_norm_torsor_results.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
