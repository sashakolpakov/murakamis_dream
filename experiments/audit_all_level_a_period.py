#!/usr/bin/env python3
"""Check the exact all-level A-period formula on known polynomial traces.

The q-variable moves with the color point M=-q^j.  This is distinct
from a meridian jet at fixed q.  Tests compare cleared companion
products to independent fixed polynomial solutions and include an
incoherent root-only family excluded by the theorem's hypotheses.
"""

import json
from math import comb
from pathlib import Path

import numpy as np
import sympy as sp

from audit_bounded_meridian_jets import (
    add_poly, jet, mul_matrix_series, mul_poly, mul_series, inv_series,
    recover, shift_poly, signal, transfer_row,
)


Q, M = sp.symbols("q M")


def terms(expression):
    return {tuple(exponents): int(coefficient)
            for exponents, coefficient in sp.Poly(sp.expand(expression), Q, M).terms()}


def binomial_integer(exponent, order):
    if exponent >= 0:
        return comb(exponent, order) if order <= exponent else 0
    return (-1)**order*comb(-exponent+order-1, order)


def curve_terms(polynomial, color):
    result = {}
    for (a, b), coefficient in polynomial.items():
        exponent = a+b*color
        result[exponent] = result.get(exponent, 0)+coefficient*(-1)**b
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def curve_jet(polynomial, color, q, order, prime):
    substituted = curve_terms(polynomial, color)
    return [sum(coefficient*pow(q, exponent, prime)*binomial_integer(exponent, k)
                for exponent, coefficient in substituted.items()) % prime
            for k in range(order+1)]


def field(level):
    # Keep all sparse exponents below the characteristic in these tests.
    prime = next(4*level*k+1 for k in range(100, 1000)
                 if sp.isprime(4*level*k+1))
    generator = int(sp.primitive_root(prime))
    q = pow(generator, (prime-1)//(2*level), prime)
    assert pow(q, level, prime) == prime-1
    return prime, q


def data(multiplicity):
    common = sp.lcm_list([Q**(2*k+1)-1 for k in range(multiplicity+1)])
    f = sp.expand(sum(comb(multiplicity, k)*Q**(2*k)
                      *sp.cancel(common/(Q**(2*k+1)-1))*M**(2*k+1)
                      for k in range(multiplicity+1)))
    leading = (1+Q**2*M**2)**multiplicity
    trailing = Q*(1+Q**4*M**2)**multiplicity
    coefficients = [trailing, -leading-trailing, leading]
    assert sp.expand(f.subs(M, Q*M)-f-common*M*leading) == 0
    assert sp.expand(sum(coefficients)) == 0
    assert sp.expand(sum(coefficient*f.subs(M, Q**j*M)
                         for j, coefficient in enumerate(coefficients))) == 0
    known = 1+(Q**2+3)*(f-f.subs(M, -Q))
    assert sp.expand(known.subs(M, -Q)-1) == 0
    return [terms(coefficient) for coefficient in coefficients], terms(known)


def q_transfer(coefficients, level, q, prime, output_order=1):
    dimension = len(coefficients)-1
    leading = coefficients[-1]
    q_span = max(a for a, _ in leading)-min(a for a, _ in leading)
    M_span = max(b for _, b in leading)-min(b for _, b in leading)
    support_size = len(leading)
    start = q_span+1
    assert level > start+dimension-1
    steps = []
    for color in range(start, level-dimension+1):
        sparse = curve_terms(leading, color)
        assert sparse
        leading_jet = curve_jet(leading, color, q, support_size-1, prime)
        multiplicity = next(k for k, value in enumerate(leading_jet) if value)
        steps.append((color, multiplicity))
    budget = sum(multiplicity for _, multiplicity in steps)
    singular_steps = sum(multiplicity != 0 for _, multiplicity in steps)
    assert singular_steps <= M_span
    assert budget <= M_span*(support_size-1)
    order = budget+output_order
    product = [np.eye(dimension, dtype=np.int64)]
    product += [np.zeros((dimension, dimension), dtype=np.int64)
                for _ in range(order)]
    denominator_unit = [1]+[0]*order
    for color, multiplicity in steps:
        jets = [curve_jet(poly, color, q, order, prime) for poly in coefficients]
        matrices = []
        for k in range(order+1):
            matrix = np.zeros((dimension, dimension), dtype=np.int64)
            for j in range(dimension-1):
                matrix[j, j+1] = jets[-1][k]
            matrix[-1, :] = [-jets[j][k] % prime for j in range(dimension)]
            matrices.append(matrix)
        product = mul_matrix_series(matrices, product, order, prime)
        complete_leading = curve_jet(leading, color, q, order+multiplicity, prime)
        unit = complete_leading[multiplicity:]
        denominator_unit = mul_series(denominator_unit, unit, order, prime)
    inverse = inv_series(denominator_unit, order, prime)
    row = []
    for k in range(order+1):
        value = np.zeros(dimension, dtype=np.int64)
        for j in range(k+1):
            value = (value+inverse[j]*product[k-j][-1, :]) % prime
        row.append(value)
    return row, budget, start, M_span*(support_size-1), steps


def moving_q_check(level, multiplicity, operator, known):
    prime, q = field(level)
    row, budget, start, bound, steps = q_transfer(operator, level, q, prime)
    initials = [curve_jet(known, color, q, budget+1, prime)
                for color in range(start, start+len(operator)-1)]
    actual = recover(row, budget, initials, 1, prime)
    expected = curve_jet(known, level, q, 1, prime)
    assert actual == expected
    for color in range(start, level-1):
        # Check the full moving-q recurrence, including its first jet,
        # independently of the companion product.
        residual = [0, 0]
        for shift, polynomial in enumerate(operator):
            a = curve_jet(polynomial, color, q, 1, prime)
            y = curve_jet(known, color+shift, q, 1, prime)
            value = mul_series(a, y, 1, prime)
            residual = [(x+y) % prime for x, y in zip(residual, value)]
        assert residual == [0, 0]
    expected_budget = multiplicity if level % 2 == 0 and level//2-1 >= start else 0
    assert budget == expected_budget
    return {"level": level, "finite_field_prime": prime,
            "leading_root_multiplicity": multiplicity,
            "fixed_initial_color_start": start,
            "uniform_q_jet_bound": bound, "actual_q_pole_budget": budget,
            "singular_steps": [[color, order] for color, order in steps if order],
            "whole_q_germ_value_and_first_coefficient_exact": True,
            "independent_recurrence_jet_check": True}


def root_only_counterexample(level):
    assert level % 2 == 0 and level >= 8
    prime, q = field(level)
    f = [1]
    for r in range(level//2, level):
        f = mul_poly(f, [1, 0, -pow(q, 2*r, prime) % prime], prime)
    left = mul_poly([1, 0, 1], shift_poly(f, q, prime), prime)
    right = mul_poly([1, 0, prime-1], f, prime)
    assert add_poly(left, right, prime, sign=-1) == [0]
    assert all(jet(f, -pow(q, j, prime) % prime, 0, prime)[0] == 0
               for j in range(1, level//2+1))
    assert jet(f, 1, 0, prime)[0] != 0
    assert jet(f, -pow(q, level//2+1, prime) % prime, 0, prime)[0] != 0

    # It is an honest root solution, but generic trace recurrence with
    # the same first two values gives the constant sequence instead.
    operator = [[q*q % prime, 0, -q*q % prime],
                [-(1+q*q) % prime], [1, 0, q*q % prime]]
    row, budget, _, _ = transfer_row(operator, q, level, prime)
    coefficient = pow(2, level, prime)
    initials = [signal(f, -pow(q, j, prime) % prime, budget,
                       level, prime, coefficient) for j in (1, 2)]
    assert all(values[0] == 1 for values in initials)
    target = recover(row, budget, initials, 0, prime)[0]
    assert target == (1+coefficient*jet(f, 1, 0, prime)[0]) % prime
    assert target != 1
    return {"level": level, "finite_field_prime": prime,
            "first_half_color_values_all_one": True,
            "root_only_polynomial_solution_exact": True,
            "meridian_jets_recover_nonconstant_target": True,
            "generic_coherent_sequence_with_same_initial_values_is_constant": True,
            "not_an_actual_knot_family": True}


def main():
    moving = []
    for multiplicity in (1, 2, 3):
        operator, known = data(multiplicity)
        for level in (8, 9, 12, 15, 16, 18, 24, 30, 36):
            if level > 2*multiplicity+2:
                moving.append(moving_q_check(level, multiplicity, operator, known))
    results = {"scope": "Exact model checks; no knot holonomicity or volume theorem is assumed.",
               "moving_q_germs": moving,
               "incoherent_root_family": [root_only_counterexample(level)
                                           for level in (8, 12, 18, 24, 30)]}
    path = Path(__file__).with_name("all_level_a_period_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"moving_q_cases": len(moving),
                      "singular_moving_q_cases": sum(case["actual_q_pole_budget"] > 0
                                                      for case in moving),
                      "root_only_coherence_counterexamples": 5,
                      "all_exact_checks": "passed", "result_file": str(path)}, indent=2))


if __name__ == "__main__":
    main()
