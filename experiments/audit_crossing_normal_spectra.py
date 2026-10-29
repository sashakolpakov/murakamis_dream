#!/usr/bin/env python3
"""Exact actual-crossing spectra and first-normal diagnostics.

The general nonconjugacy proof is in the associated note.  These tests
assemble literal balanced crossing entries independently of the predicted
highest-weight spectra, over finite fields and their dual numbers.
The common Cartan line is factored explicitly; x**(N-1) retains the
same-auxiliary-twist normalization.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_divided_ward_factorial_fusion import field


class J:
    p = 0

    def __init__(self, x=0, dx=0):
        self.x, self.dx = int(x) % self.p, int(dx) % self.p

    def __add__(self, other):
        other = other if isinstance(other, J) else J(other)
        return J(self.x + other.x, self.dx + other.dx)

    __radd__ = __add__

    def __neg__(self):
        return J(-self.x, -self.dx)

    def __sub__(self, other):
        return self + (-other if isinstance(other, J) else -int(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, J) else J(other)
        return J(self.x * other.x, self.x * other.dx + self.dx * other.x)

    __rmul__ = __mul__

    def inv(self):
        ix = pow(self.x, -1, self.p)
        return J(ix, -self.dx * ix * ix)

    def __truediv__(self, other):
        other = other if isinstance(other, J) else J(other)
        return self * other.inv()

    def __pow__(self, k):
        if k < 0:
            return self.inv() ** (-k)
        out, base = J(1), self
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k //= 2
        return out

    def __eq__(self, other):
        other = other if isinstance(other, J) else J(other)
        return self.x == other.x and self.dx == other.dx

    def data(self):
        return [self.x, self.dx]


def actual_blocks(n, q, meridian, auxiliary_twist=True):
    """Literal positive checked balanced crossing, common Cartan removed."""
    Q, x = q**2, -meridian / q
    blocks = []
    for total in range(2*n-1):
        states = [(a, total-a) for a in range(n) if 0 <= total-a < n]
        index = {state: i for i, state in enumerate(states)}
        out = [[J() for _ in states] for _ in states]
        for col, (a, d) in enumerate(states):
            for k in range(min(a, n-1-d)+1):
                gaussian, pochhammer = J(1), J(1)
                for r in range(1, k+1):
                    gaussian *= (1-Q**(d+r)) / (1-Q**r)
                    pochhammer *= 1-meridian**2 * Q**(-a+r-1)
                power = a*d+(a-d)*k-k*(k+1)//2
                value = (-1)**k * x**(-a-d-k) * Q**power
                value *= gaussian * pochhammer
                if auxiliary_twist:
                    value *= x**(n-1)
                row = index[(d+k, a-k)]
                out[row][col] += value
        blocks.append((
            np.array([[v.x for v in row] for row in out], dtype=np.int64),
            np.array([[v.dx for v in row] for row in out], dtype=np.int64),
        ))
    return blocks


def traces(blocks, degree, p):
    powers = [(np.eye(len(a), dtype=np.int64), np.zeros_like(a))
              for a, _ in blocks]
    result = []
    for _ in range(degree):
        tr0, tr1 = 0, 0
        updated = []
        for (a, da), (b, db) in zip(powers, blocks):
            c = a @ b % p
            dc = (da @ b+a @ db) % p
            updated.append((c, dc))
            tr0 += int(np.trace(c))
            tr1 += int(np.trace(dc))
        powers = updated
        result.append(J(tr0, tr1))
    return result


def charpoly_from_traces(power_traces):
    coeff = [J(1)]
    for k in range(1, len(power_traces)+1):
        value = sum((coeff[k-i] * power_traces[i-1]
                     for i in range(1, k+1)), J())
        coeff.append(-value/J(k))
    return coeff


def predicted(n, q, meridian, integral):
    highest = n-1
    x = -meridian/q
    eigenvalues = []
    for j in range(n):
        value = x**highest * (-1)**j
        value *= q**(-j*(2*highest-j+1))
        if not integral:
            value *= meridian**(-2*j)
        multiplicity = 2*(highest-j)+1 if integral else n
        eigenvalues.append((value, multiplicity))
    coeff = [J(1)]
    for value, multiplicity in eigenvalues:
        for _ in range(multiplicity):
            new = [J() for _ in range(len(coeff)+1)]
            for k, old in enumerate(coeff):
                new[k] += old
                new[k+1] -= value*old
            coeff = new
    return coeff, eigenvalues


def main():
    records, coefficient_checks = [], 0
    for n in range(2, 9):
        p, q0 = field(n)
        J.p = p
        gen = int(sp.primitive_root(p))
        cases = [
            ("generic_integral", J(gen), -J(gen)**n, True),
            ("generic_root_meridian", J(q0), J(gen), False),
            ("first_normal_integral", J(q0, q0*pow(n, -1, p)), None, True),
            ("first_normal_root_meridian", J(q0), J(1, 1), False),
        ]
        normal_traces = {}
        for name, q, meridian, integral in cases:
            if meridian is None:
                meridian = -q**n
            actual_traces = traces(actual_blocks(n, q, meridian), n*n, p)
            actual = charpoly_from_traces(actual_traces)
            expected, eigenvalues = predicted(n, q, meridian, integral)
            assert actual == expected, (n, name)
            coefficient_checks += len(actual)
            if name.startswith("generic"):
                assert len({v.x for v, _ in eigenvalues}) == n
            if name.startswith("first_normal"):
                normal_traces[name] = actual_traces[0].data()
        # A second independent module invariant: the first normal trace K**N.
        q = J(q0, q0*pow(n, -1, p))
        trace_integral = sum((q**(n*(n-1-2*j)) for j in range(n)), J())
        meridian = J(1, 1)
        trace_root = sum(((-meridian/J(q0)*(J(q0)**2)**(-j))**n
                          for j in range(n)), J())
        assert trace_integral.dx == 0
        assert trace_root.dx == ((-1)**(n-1)*n*n) % p
        if n == 2:
            assert normal_traces["first_normal_integral"] == J(4*q0, q0).data()
            assert normal_traces["first_normal_root_meridian"] == J(4*q0, 0).data()
        records.append({
            "N": n, "prime": p, "q_root": q0,
            "integral_multiplicities": [2*(n-1-j)+1 for j in range(n)],
            "root_typical_multiplicities": [n]*n,
            "normal_auxiliary_twist_traces": normal_traces,
            "normal_trace_K_power": {
                "integral": trace_integral.data(), "root": trace_root.data()},
        })
    result = {
        "normal_parameter": "q=q0*(1+epsilon/N), M_root=1+epsilon",
        "normalization": "full Cartan factored; R multiplied by x**(N-1)",
        "coefficient_checks": coefficient_checks,
        "records": records,
    }
    output = Path(__file__).with_name("crossing_normal_spectra_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "passed", "coefficient_checks": coefficient_checks,
                      "N": [2, 8], "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
