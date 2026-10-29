"""Exact whole-clock endpoint lattices, integral primitives and confluence.

These checks concern the retained function algebra. Actual divided
matrix arrows have a separate audit; no Gaussian/source comparison or
volume estimate is assumed here.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def qinteger(j, Z):
    return sum(Z**k for k in range(j))


def polynomial_zero(expr, *variables):
    return sp.Poly(sp.expand(expr), *variables).is_zero


def lattice_case(L):
    x, Z, c = sp.symbols("x Z c", nonzero=True)
    delta = 1-Z
    basis = [sp.Poly(sp.prod(x-c*Z**r for r in range(j)), x)
             for j in range(L+2)]
    normalized = sp.zeros(L+1)
    checks = 0
    for j in range(L+1):
        assert basis[j].degree() == j and basis[j].LC() == 1
        for r in range(L+1):
            value = basis[j].eval(c*Z**r)
            if r < j:
                assert polynomial_zero(value, Z, c)
                continue
            W = ((-c)**j*Z**(j*(j-1)//2)
                 *sp.prod(qinteger(k,Z) for k in range(r-j+1,r+1)))
            assert polynomial_zero(value-delta**j*W, Z, c)
            normalized[r,j] = sp.expand(W.subs(Z,1))
            assert normalized[r,j] == (-c)**j*sp.factorial(r)/sp.factorial(r-j)
            checks += 1
    expected_det = sp.prod((-c)**j*sp.factorial(j) for j in range(L+1))
    assert sp.expand(normalized.det()-expected_det) == 0

    # The exact clock in the monic Newton basis is bidiagonal; after
    # confluence it retains the whole Jordan jet lattice.
    for j in range(L+1):
        clock_residual = x*basis[j].as_expr()-c*Z**j*basis[j].as_expr()
        assert polynomial_zero(clock_residual-basis[j+1].as_expr(), x, Z, c)

    # Whole Jackson identity, including the integral highest-endpoint
    # correction; no division by a vanishing delta is evaluated.
    for j in range(1,L+2):
        P = basis[j].as_expr()
        jackson_numerator = P-P.subs(x,Z*x)
        exact = delta*qinteger(j,Z)*x*basis[j-1].as_expr()
        assert polynomial_zero(jackson_numerator-exact, x,Z,c)

    # Surjectivity of D:A_L -> A_(L-1): columns x,...,x^L have
    # determinant equal to det(multiplication by x)*product [j]_Z.
    PLm = basis[L].as_expr()
    multiplication_x = sp.zeros(L)
    jackson_nonconstant = sp.zeros(L)
    for j in range(L):
        remainder = sp.Poly(sp.rem(x**(j+1),PLm,x),x)
        for i in range(L):
            multiplication_x[i,j] = remainder.nth(i)
            jackson_nonconstant[i,j] = qinteger(j+1,Z)*remainder.nth(i)
    det_x = c**L*Z**(L*(L-1)//2)
    assert polynomial_zero(multiplication_x.det()-det_x,Z,c)
    expected = det_x*sp.prod(qinteger(j,Z) for j in range(1,L+1))
    assert polynomial_zero(jackson_nonconstant.det()-expected,Z,c)
    assert sp.expand(expected.subs(Z,1)-c**L*sp.factorial(L)) == 0

    # The relative endpoint value includes the full factorial lattice.
    top = basis[L+1].eval(c*Z**(L+1))
    full_product = (c**(L+1)*Z**(L*(L+1)//2)
                    *sp.prod(Z**k-1 for k in range(1,L+2)))
    assert polynomial_zero(top-full_product,Z,c)
    quotient = ((-1)**L*c**(L+1)*Z**(L*(L+1)//2)
                *sp.prod(qinteger(k,Z) for k in range(1,L+2)))
    assert polynomial_zero(-top-delta**(L+1)*quotient,Z,c)
    assert sp.expand(quotient.subs(Z,1)-(-1)**L*c**(L+1)*sp.factorial(L+1)) == 0
    return {
        "L":L,
        "exact_evaluation_entries":checks,
        "smith_normal_valuations":list(range(L+1)),
        "evaluation_index_valuation":L*(L+1)//2,
        "confluent_clock_and_Jackson_primitives":True,
        "endpoint_order_and_full_factorial":True,
    }


def main():
    cases = [lattice_case(L) for L in range(1,9)]
    result = {
        "status":"pass",
        "cases":cases,
        "scope":"Whole function/endpoints and integral source lattices; no network Gaussian map or volume theorem.",
    }
    destination = Path(__file__).with_name("whole_clock_confluent_lattice_results.json")
    destination.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"pass","levels":len(cases),
                      "evaluation_entries":sum(c["exact_evaluation_entries"] for c in cases),
                      "results":str(destination)},indent=2))


if __name__ == "__main__":
    main()
