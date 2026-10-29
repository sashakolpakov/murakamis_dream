#!/usr/bin/env python3
"""Exact two-variable normal density using FLINT polynomial arithmetic.

The coefficient field is Q(s,r)(sqrt(-3)).  The actual coefficient,
Hessian, framing derivatives and cut use the original audit unchanged.
No interpolation or numerical specialization is used.
"""

import json
from pathlib import Path

import sympy as sp
from flint import fmpq_mpoly_ctx

from audit_actual_normal_stationary_period import symbolic_framing_density


CONTEXT = fmpq_mpoly_ctx.get(('s', 'r'))
ZERO = CONTEXT.constant(0)
ONE = CONTEXT.constant(1)


class QuadraticFraction:
    """(a+b sqrt(-3))/c, with a,b,c in Q[s,r]."""

    def __init__(self, a=ZERO, b=ZERO, c=ONE):
        if not c:
            raise ZeroDivisionError
        if not a and not b:
            self.a, self.b, self.c = ZERO, ZERO, ONE
            return
        common = a.gcd(b).gcd(c)
        if not common.is_one():
            a, b, c = a / common, b / common, c / common
        leading = c.leading_coefficient()
        self.a, self.b, self.c = a / leading, b / leading, c / leading

    @staticmethod
    def coerce(value):
        if isinstance(value, QuadraticFraction):
            return value
        return QuadraticFraction(CONTEXT.constant(value))

    def __bool__(self):
        return bool(self.a) or bool(self.b)

    def __neg__(self):
        return QuadraticFraction(-self.a, -self.b, self.c)

    def __add__(self, other):
        other = self.coerce(other)
        return QuadraticFraction(self.a * other.c + other.a * self.c,
                                 self.b * other.c + other.b * self.c,
                                 self.c * other.c)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return QuadraticFraction(self.a * other.a - 3 * self.b * other.b,
                                 self.a * other.b + self.b * other.a,
                                 self.c * other.c)

    __rmul__ = __mul__

    def inverse(self):
        return QuadraticFraction(self.c * self.a, -self.c * self.b,
                                 self.a * self.a + 3 * self.b * self.b)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, exponent):
        exponent = int(exponent)
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result, base = self.coerce(1), self
        while exponent:
            if exponent & 1:
                result = result * base
            exponent >>= 1
            if exponent:
                base = base * base
        return result


class ExactQuadraticField:
    def __init__(self):
        self.zero = QuadraticFraction()
        self.one = QuadraticFraction(ONE)
        self.gens = tuple(QuadraticFraction(g) for g in CONTEXT.gens())
        self.radical = QuadraticFraction(ZERO, ONE)

    def convert(self, value, source=None):
        if source is not None:
            # The sole extension-field conversion in the original audit.
            assert source.to_sympy(value) == sp.sqrt(-3)
            return self.radical
        return QuadraticFraction.coerce(value)

    def to_sympy(self, value):
        value = self.convert(value)
        symbols = dict(zip(('s', 'r'), sp.symbols('s r')))

        def polynomial(poly):
            return sp.sympify(str(poly).replace('^', '**'), locals=symbols)

        return (polynomial(value.a) + sp.sqrt(-3) * polynomial(value.b)) / polynomial(value.c)


def main():
    field = ExactQuadraticField()
    s, r = field.gens
    z = field.radical
    assert not z * z + 3
    f = (s + z * r) / (s * r - z)
    assert not f * ((s * r - z) / (s + z * r)) - 1
    assert not (s + z * r) * (s - z * r) - (s * s + 3 * r * r)
    result = symbolic_framing_density(None, exact_field=field)
    result['arithmetic'] = 'FLINT Q[s,r] polynomial gcds; exact quadratic extension; no interpolation'
    path = Path(__file__).with_name('full_framing_density_results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
