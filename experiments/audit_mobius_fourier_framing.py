#!/usr/bin/env python3
"""Test the prefix Möbius theorem against raw 2x2 conjugation and cyclic traces."""

from itertools import product
import json
from pathlib import Path
import sympy as sp

from audit_actual_fourier_polarized_normal_block import (
    PRIME, mm, inv, add, mul, local_data,
)


def finite_field_audit():
    count = inverse_cases = pole_cases = infinite_cases = 0
    for vi, ui in product(range(3), repeat=2):
        va, vb, vc = vi+2, vi+1, vi+2
        V = (va, vb, vc, (1+vb*vc)*pow(va, -1, PRIME) % PRIME)
        x, y = ui+1, ui+2
        mer = ((1+x*y) % PRIME, -x*x % PRIME,
               y*y % PRIME, (1-x*y) % PRIME)
        U = mm(mer, V)
        # mer-I=(x,y)^t (y,-x), so the actual difference is u*(wV).
        w = (y, -x % PRIME)
        a = (w[0]*V[0]+w[1]*V[2]) % PRIME
        b = (w[0]*V[1]+w[1]*V[3]) % PRIME
        c, d = w
        assert add(U, mul(-1, V)) == tuple(
            z % PRIME for z in (x*a, x*b, y*a, y*b))
        for r, s, sigma in product(range(2, 10), range(1, 5), (-1, 1)):
            raw = local_data(U, V, r, s, sigma)
            den = (a*r+b*s) % PRIME
            if raw is None or not den:
                continue
            _, p, _, _, _, pp = raw
            expected = sigma*(c*(1-r)-d*s)*pow(den, -1, PRIME) % PRIME
            assert p == expected
            delta = sigma*(s*(a*d-b*c)-a*c) % PRIME
            pd = (a*p+sigma*c) % PRIME
            if not delta or not pd:
                continue
            rr = (sigma*(c-d*s)-b*s*p)*pow(pd, -1, PRIME) % PRIME
            rp = delta*pow(pd, -2, PRIME) % PRIME
            assert rr == r and rp*pp % PRIME == 1
            count += 1
            inverse_cases += 1
            if a and y:
                lam = -sigma*c*pow(a, -1, PRIME) % PRIME
                lam_prefix = -sigma*mer[2]*pow((U[2]-V[2]) % PRIME,
                                              -1, PRIME) % PRIME
                assert lam == lam_prefix
                pole_cases += 1

    # A genuine nonconstant infinite-pole chart, constructed independently.
    V = (1, 0, -1 % PRIME, 1)
    mer = (2, 1, -1 % PRIME, 0)
    U = mm(mer, V)
    for r, s, sigma in product(range(2, 8), range(1, 4), (-1, 1)):
        raw = local_data(U, V, r, s, sigma)
        if raw is None:
            continue
        _, p, _, _, _, pp = raw
        assert p == sigma*(1-r-s)*pow(s, -1, PRIME) % PRIME
        assert pp == -sigma*pow(s, -1, PRIME) % PRIME
        infinite_cases += 1
    assert count and pole_cases and infinite_cases
    return {"raw_prefix_cases": count, "inverse_cases": inverse_cases,
            "intrinsic_pole_cases": pole_cases,
            "pole_at_infinity_cases": infinite_cases, "prime": PRIME}


def figure_eight_audit():
    u, r, s, p = sp.symbols("u r s p")
    modulus = u*u+u+1

    def red(value):
        num, den = sp.fraction(sp.cancel(value))
        nr = sp.rem(num, modulus, u)
        dr = sp.rem(den, modulus, u)
        return sp.cancel(nr*sp.invert(dr, modulus, u)).expand().collect(u)

    V = sp.Matrix([[1, 1], [-u, 1-u]])
    U = sp.Matrix([[u+1, 2*u+1], [1-u, 3-u]])
    F = sp.Matrix([[r, 1-r], [s, -s]])
    vp = F.inv()*V*F
    up = F.inv()*U*F
    k = up[0, 0]/vp[0, 0]
    praw = -(up[0, 1]-k*vp[0, 1])/(k-1)
    pexpected = (s-(1+u)*(1-r))/(r+2*s)
    assert red(praw-pexpected) == 0
    rinverse = (s-(1+u)-2*s*p)/(p-(1+u))
    assert red(rinverse.subs(p, pexpected)-r) == 0
    assert red(sp.diff(rinverse, p)
               -((1+u)+(1+2*u)*s)/(p-(1+u))**2) == 0
    lam = 1+u
    assert red(lam**6-1) == 0
    assert all(red(lam**n-1) != 0 for n in (1, 2, 3))
    return {"raw_symbolic_momentum": True, "inverse_and_density": True,
            "intrinsic_pole_order": 6}


def cyclic_trace_audit():
    count = 0
    for n, lam in product(range(2, 10), (sp.Rational(2, 3), sp.Integer(2),
                                      sp.Integer(0), -sp.Rational(1, 3))):
        P = sp.zeros(n)
        for j in range(n):
            P[(j+1) % n, j] = 1
        R = (P-lam*sp.eye(n)).inv()
        actual = sp.trace(R*R*P)/n
        expected = n*lam**(n-1)/(1-lam**n)**2
        assert sp.cancel(actual-expected) == 0
        count += 1
    return {"independent_companion_trace_cases": count}


def main():
    report = {"status": "pass", "finite_field": finite_field_audit(),
              "figure_eight": figure_eight_audit(),
              "cyclic_norm": cyclic_trace_audit()}
    target = Path(__file__).with_name("mobius_fourier_framing_results.json")
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
