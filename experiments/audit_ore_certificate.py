#!/usr/bin/env python3
"""Check the explicit arXiv:1711.11522v3 figure-eight Ore certificate.

Normal form: Q1^a Q2^b E1^c E2^d; Ei Qi = q Qi Ei.
The parameter s is q^(1/2). All checks are exact polynomial calculations.
"""

import json
from pathlib import Path

import sympy as sp

s = sp.Symbol("s")
q = s**2


class Ore:
    def __init__(self, value=0):
        if isinstance(value, dict):
            self.terms = {m: sp.expand(c) for m, c in value.items() if c != 0}
            self.terms = {m: c for m, c in self.terms.items() if c != 0}
        else:
            self.terms = {(0, 0, 0, 0): sp.sympify(value)} if value != 0 else {}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Ore) else Ore(value)

    def __add__(self, other):
        other = self.coerce(other)
        out = self.terms.copy()
        for m, c in other.terms.items():
            out[m] = out.get(m, 0) + c
        return Ore(out)

    __radd__ = __add__

    def __neg__(self):
        return Ore({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for a, ca in self.terms.items():
            for b, cb in other.terms.items():
                m = tuple(x + y for x, y in zip(a, b))
                out[m] = out.get(m, 0) + ca * cb * q ** (a[2] * b[0] + a[3] * b[1])
        return Ore(out)

    __rmul__ = __mul__

    def __pow__(self, degree):
        assert isinstance(degree, int) and degree >= 0
        out = Ore(1)
        for _ in range(degree):
            out = out * self
        return out


Q1, Q2, E1, E2 = [Ore({tuple(int(i == j) for i in range(4)): 1}) for j in range(4)]


def main():
    assert not (E1 * Q1 - q * Q1 * E1).terms
    assert not (E2 * Q2 - q * Q2 * E2).terms
    assert not (E1 * Q2 - Q2 * E1).terms

    g1 = E1 * Q2**2 - s * Q1 * Q2 - q * Q1**2
    g2 = E2 * Q1 * Q2**2 + s * (E2 * Q1**2 + E2 * Q1 - q) * Q2 + q * E2 * Q1**2
    P = (
        q**3 * E2**2 * (q * E2 * Q1**2 - 1) * Q1**2 * E1**2
        - (q**2 * E2 * Q1**2 - 1)
        * (q**4 * E2**2 * Q1**4 - q**3 * E2**2 * Q1**3 - q * (q**2 + 1) * E2 * Q1**2 - q * E2 * Q1 + 1)
        * E1
        + q * E2 * (q**3 * E2 * Q1**2 - 1) * Q1**2
    )
    a1 = (
        E2 * Q1
        * ((q * E2 * Q1**2 - 1) * (q**3 * E2 * Q1**2 + q * E2 * Q1 - 1) * E1
           + q**2 * E2 * (q**3 * E2 * Q1**2 - 1) * Q1**2)
        * Q2
        + s * (q * E2 * Q1**2 - 1)
        * (q**5 * E2**2 * Q1**4 + q**3 * E2**2 * Q1**3 + q * E2**2 * Q1**2
           - q**2 * (q + 1) * E2 * Q1**2 - (q + 1) * E2 * Q1 + 1)
        * E1
        + s**5 * E2 * (E2 * Q1 - q) * (q**3 * E2 * Q1**2 - 1) * Q1**2
    )
    a2 = (
        ((q * E2 * Q1**2 - 1) * (q**3 * E2 * Q1**2 + q * E2 * Q1 - 1) * E1**2
         + q**3 * E2 * (q**3 * E2 * Q1**2 - 1) * Q1**2 * E1)
        * Q2
        - s**5 * E2 * (q * E2 * Q1**2 - 1) * Q1**2 * E1**2
        - s**3
        * (q**4 * (q + 1) * E2**2 * Q1**4 + q**2 * E2**2 * Q1**3
           - q * (q**2 + q + 1) * E2 * Q1**2 - q * E2 * Q1 + 1)
        * Q1 * E1
        - s**7 * E2 * (q**3 * E2 * Q1**2 - 1) * Q1**3
    )
    residual = s**9 * Q1**2 * P - q * a1 * g1 + a2 * g2
    result = {
        "source": "arXiv:1711.11522v3 TeX lines 1257-1290",
        "normal_order": "Q1^a Q2^b E1^c E2^d; Ei Qi=q Qi Ei; q=s^2",
        "certificate_exact": not residual.terms,
        "residual_terms": {str(m): str(sp.factor(c)) for m, c in residual.terms.items()},
        "scope": "Algebraic certificate only; integrand equations, contours and minimality are separate obligations.",
    }
    Path(__file__).with_name("ore_certificate_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
