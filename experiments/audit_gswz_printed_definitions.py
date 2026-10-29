#!/usr/bin/env python3
"""Exact diagnostics for the printed definitions in arXiv:2412.04241v2.

Uniform counterexample proofs, precise scope, and primary-source locations
are in notes/gswz_printed_definition_audit.md. Finite checks here supplement
those proofs; they do not establish infinite-level claims by sampling.
"""

from fractions import Fraction
from math import comb, gcd
import json
from pathlib import Path

import sympy as sp


def sign_collection(m):
    return -1 if m == 2 else 1


def global_sign_checks():
    tested = 0
    for gamma in range(1, 121):
        for m in range(1, 241):
            if gcd(m, gamma) == 1:
                assert sign_collection(m)**(gamma+1) == 1
                tested += 1
    for p in (5, 7, 11, 13, 17, 19):
        for m in range(1, 241):
            if gcd(m, p) == 1:
                value = sign_collection(m)
                assert Fraction(value, value**p) == 1
    assert sign_collection(2) != sign_collection(10)
    assert (sign_collection(2)-sign_collection(10)) % 5 != 0
    h2, h10 = 1+sign_collection(2), 1+sign_collection(10)
    assert (h2*h2-h10*h10) % 5 != 0
    assert all(sign_collection(m) == 1 for m in range(1, 241) if gcd(m, 6) == 1)
    return {"gamma_order_pairs_checked": tested,
            "local_constant_Frobenius_quotients_equal_one": True,
            "all_sampled_global_tests_equal_one": True,
            "Habiro_gluing_failure": {"p": 5, "orders": [2, 10], "values": [-1, 1]},
            "sum_gamma_one_gluing_failure": {"orders": [2, 10], "squared_values": [h2*h2, h10*h10]},
            "restriction_to_orders_prime_to_six_is_one": True}


def multiply(a, b, order):
    return [sum((a[j]*b[k-j] for j in range(k+1)), Fraction(0))
            for k in range(order+1)]


def power(a, exponent, order):
    result = [Fraction(1)]+[Fraction(0)]*order
    for j in range(exponent):
        result = multiply(result, a, order)
    return result


def binomial_series(beta, order):
    result = [Fraction(1)]
    for j in range(1, order+1):
        result.append(result[-1]*(beta-j+1)/j)
    return result


def compose(a, b, order):
    result = [Fraction(0)]*(order+1)
    term = [Fraction(1)]+[Fraction(0)]*order
    for coefficient in a:
        result = [x+coefficient*y for x, y in zip(result, term)]
        term = multiply(term, b, order)
    return result


def local_slope_checks():
    p, order = 5, 10
    substitution = [Fraction(0)]+[Fraction(comb(p, j)) if j <= p else Fraction(0)
                                   for j in range(1, order+1)]
    rows = []
    for a in range(1, 7):
        beta = Fraction(1, p**a)
        series = binomial_series(beta, order)
        assert compose(series, substitution, order) == power(series, p, order)
        assert series[0] == 1 and series[1] == beta
        rows.append({"a": a, "linear_coefficient": str(beta), "five_adic_valuation": -a,
                     "Frobenius_identity_exact_through_degree": order})
    return {"p": p, "rows": rows,
            "uniform_proof": "(q^p)^beta=(q^beta)^p in the formal germ at q=1"}


def gaussian_checks():
    h, w, z = sp.symbols("h w z")
    z_order = 7
    # Derive the polar and constant terms directly from the defining
    # logarithm -sum (q*z*exp(w))^n/[n*(1-q^n)].
    polar = sp.Integer(0)
    constant = sp.Integer(0)
    for n in range(1, z_order+1):
        ratio = sp.series(-sp.exp(n*h)/(n*(1-sp.exp(n*h))), h, 0, 1).removeO().expand()
        polar += sp.expand(h*ratio).subs(h, 0)*z**n*sp.exp(n*w)
        constant += ratio.coeff(h, 0)*z**n*sp.exp(n*w)
    li2 = sum(z**n/sp.Integer(n*n) for n in range(1, z_order+1))
    li1 = sum(z**n/sp.Integer(n) for n in range(1, z_order+1))
    li0 = sum(z**n for n in range(1, z_order+1))
    printed_polar = sp.series(polar-li2-li1*w-li0*w*w, w, 0, 3).removeO().expand()
    assert printed_polar.coeff(w, 0) == 0
    assert printed_polar.coeff(w, 1) == 0
    assert sp.expand(printed_polar.coeff(w, 2)+li0/2) == 0
    # The printed exponential adds -(1/2)log(1-z), i.e. +(1/2)Li1.
    printed_regular_log_at_zero = sp.expand(constant.subs(w, 0)+li1/2)
    assert sp.expand(printed_regular_log_at_zero-li1) == 0
    normalized_value = sp.series(sp.exp(printed_regular_log_at_zero), z, 0, z_order+1).removeO().expand()
    assert sp.expand(normalized_value-sum(z**j for j in range(z_order+1))) == 0
    assert not any(a+3*b == 2 and c-b == -1
                   for a in range(3) for b in range(2) for c in range(3))
    # With A=0, Lambda=-Li0. Every term shown is a nonzero h^0
    # contribution under the printed quadratic normalization.
    contractions = [str(Fraction(comb(2*n, n), 4**n)) for n in range(10)]
    return {"m": 1, "k": 0, "z_degrees_checked": z_order,
            "unwanted_polar_term": "-Li_0(z)*w^2/(2h)",
            "printed_psi_at_w_zero_h_zero": "1/(1-z)",
            "w2_over_h_outside_stated_semigroup_domain": True,
            "A_zero_constant_order_contributions": contractions}


def recurrence_checks():
    q = sp.symbols("q")

    def coefficient(A, m, k, j):
        n = k+m*j
        denominator = sp.prod(1-q**r for r in range(k+1, n+1))
        exponent = A*(n*(n+1)-k*(k+1))//2
        return sp.cancel((-1)**(A*(n-k))*q**exponent/denominator)

    records = []
    for A, m, k in ((1, 2, 0), (1, 3, 1), (1, 4, 2), (2, 3, 1), (0, 2, 1)):
        for j in range(1, 4):
            n = k+m*j
            lhs = sp.cancel(sp.prod(1-q**(n-r) for r in range(m))*coefficient(A, m, k, j))
            corrected = sp.cancel((-1)**(A*m)*q**(A*m*(m+1)//2+A*m*(n-m))
                                  *coefficient(A, m, k, j-1))
            assert sp.cancel(lhs-corrected) == 0
        records.append({"A": A, "m": m, "k": k, "nonzero_coefficients_checked": 3,
                        "corrected_recurrence_exact": True})
    first = sp.cancel(coefficient(1, 2, 0, 1))
    lhs = sp.cancel((1-q*q)*(1-q)*first)
    assert lhs == q**3
    printed = -q**3
    assert sp.cancel(lhs-printed) == 2*q**3
    return {"printed_counterexample": {"A": 1, "m": 2, "k": 0,
                                       "H_t_squared_coefficient": str(first),
                                       "lhs_t_squared": str(lhs), "printed_rhs_t_squared": str(printed)},
            "corrected_sign": "(-1)^(A*m)", "records": records}


def main():
    result = {"source": "arXiv:2412.04241v2, 27 August 2025",
              "scope": "Printed-definition and formula audit; no claim to refute restricted Theorem 5.",
              "global_sign": global_sign_checks(), "local_slopes": local_slope_checks(),
              "Gaussian": gaussian_checks(), "recurrence": recurrence_checks()}
    Path(__file__).with_name("gswz_printed_definition_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
