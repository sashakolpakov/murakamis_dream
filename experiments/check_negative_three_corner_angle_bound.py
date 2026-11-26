#!/usr/bin/env python3
"""Exact polynomial identity for the magnitude-three corner angle bound."""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp


def verify():
    a, z = sp.symbols("a z")
    def cosine_polynomial(n):
        return sum((-1)**j * sp.binomial(n, 2*j) * a**(2*j)
                   for j in range(n//2 + 1))
    def sine_polynomial(n):
        return sum((-1)**j * sp.binomial(n, 2*j+1) * a**(2*j+1)
                   for j in range((n+1)//2))
    c = {j: cosine_polynomial(j) for j in (4, 5, 6)}
    s = {j: sine_polynomial(j) for j in (4, 5, 6)}
    P = (z**12 - 75*z**11 + 1841*z**10 - 26525*z**9
         + 188184*z**8 - 674158*z**7 + 1223346*z**6
         - 1195674*z**5 + 652257*z**4 - 197015*z**3
         + 32461*z**2 - 2681*z + 86)
    # Multiply by 4*c4^4*c5^2*c6^2 before expanding.
    lhs = (4*s[4]**2*c[4]**2*c[5]**2*c[6]**2
           + s[6]**2*(c[4]**2+s[4]**2)**2*c[5]**2
           - 4*s[5]**2*c[4]**4*c[6]**2)
    rhs = 4*a**4*(3-a**2)*(1+a**2)**4*P.subs(z, a**2)
    assert sp.expand(lhs-rhs) == 0
    grouped = (z**12 + z**10*(1841-75*z)
               + z**8*(188184-26525*z)
               + z**6*(1223346-674158*z)
               + z**4*(652257-1195674*z)
               + z**2*(32461-197015*z) - 2681*z + 86)
    assert sp.expand(P-grouped) == 0
    end = F(1, 25)
    pairs = [(1841, 75), (188184, 26525),
             (1223346, 674158), (652257, 1195674)]
    assert all(F(p)-q*end > 0 for p, q in pairs)
    assert F(32461)-197015*end > 24580
    assert -2681+2*24580*end < 0
    lower = F(86)-2681*end+24580*end**2
    assert lower == F(11305, 625) and lower > 18
    return {
        "claim": "The exact tangent identity and P(z)>18 on 0<=z<=1/25.",
        "identity_residual": "0",
        "polynomial_coefficients_low_to_high":
            [int(P.coeff(z, j)) for j in range(13)],
        "quadratic_lower_bound": "86-2681*z+24580*z^2",
        "minimum_quadratic_lower_bound": str(lower),
        "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text)
