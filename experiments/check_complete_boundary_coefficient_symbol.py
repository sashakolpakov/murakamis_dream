#!/usr/bin/env python3
"""Exact polynomial checks for the power-three coefficient recurrence.

This checks the characteristic discriminant, reciprocal resultant and
endpoint scaling. It does not certify any asymptotic solution or lower
bound for the quantum source.
"""

import sympy as sp


def main():
    X, U, y = sp.symbols("X U y")
    c = X + 1 / X
    b = c - 2
    a = 4 * X - 2 * X**2
    d = -(1 - X) ** 2
    F = ((c + b * U) ** 2 - 1) * (a + d * (U + 1 / U))
    F += (c + b * U) * (c + b / U) - 8 * (c + b * U) + 10
    polynomial = sp.cancel(U * F)
    quintic = 20 * X**5 - 64 * X**4 + 80 * X**3 - 50 * X**2 + 8 * X - 1
    target = 1024 * (X - 1) ** 12 * quintic / X**5
    assert sp.cancel(sp.discriminant(polynomial, U) - target) == 0
    reciprocal = sp.expand(X**5 * quintic.subs(X, 1 / X))
    assert sp.resultant(quintic, reciprocal, X) == -1107908637241
    endpoint = sp.limit(sp.cancel(F.subs(U, y / (X - 1) ** 2)), X, 1)
    assert sp.expand(endpoint + (y - 1) * (y**2 + 3 * y + 4)) == 0
    print("Three exact symbolic identities verified.")


if __name__ == "__main__":
    main()
