#!/usr/bin/env python3
"""Exact diagnostics for bounded meridian-jet propagation.

The proof is in notes/bounded_meridian_jets.md.  Tests use manufactured
operators with known rational solution spaces, not conjectural knot
operators.  Companion products are computed after clearing their complete
denominators; independent known solutions check every recovered coefficient.
"""

import json
from math import comb
from pathlib import Path

import numpy as np
import sympy as sp


def trim(poly, prime):
    poly = [int(value) % prime for value in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add_poly(a, b, prime, sign=1):
    result = [0]*max(len(a), len(b))
    for j, value in enumerate(a):
        result[j] += value
    for j, value in enumerate(b):
        result[j] += sign*value
    return trim(result, prime)


def mul_poly(a, b, prime):
    result = [0]*(len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            result[j+k] += x*y
    return trim(result, prime)


def shift_poly(poly, q, prime):
    return [value*pow(q, j, prime) % prime
            for j, value in enumerate(poly)]


def power_poly(poly, exponent, prime):
    result = [1]
    for _ in range(exponent):
        result = mul_poly(result, poly, prime)
    return result


def jet(poly, point, order, prime):
    # Coefficients in the coordinate M=point*(1+z).
    return [sum(value*pow(point, j, prime)*comb(j, k)
                for j, value in enumerate(poly) if j >= k) % prime
            for k in range(order+1)]


def mul_series(a, b, order, prime):
    return [sum(a[j]*b[k-j] for j in range(k+1)) % prime
            for k in range(order+1)]


def inv_series(a, order, prime):
    assert a[0] != 0
    inverse = pow(int(a[0]), -1, prime)
    result = [inverse]
    for k in range(1, order+1):
        result.append(-inverse*sum(a[j]*result[k-j]
                                  for j in range(1, k+1)) % prime)
    return result


def mul_matrix_series(a, b, order, prime):
    result = [np.zeros_like(a[0]) for _ in range(order+1)]
    for k in range(order+1):
        for j in range(k+1):
            result[k] = (result[k]+a[j]@b[k-j]) % prime
    return result


def field(level):
    prime = next(4*level*k+1 for k in range(1, 1000)
                 if sp.isprime(4*level*k+1))
    generator = int(sp.primitive_root(prime))
    q = pow(generator, (prime-1)//(2*level), prime)
    assert pow(q, level, prime) == prime-1
    return prime, q, generator


def transfer_row(coefficients, q, level, prime, output_order=0):
    """Return z^S times the transfer row through the Kashaev point.

    Uses polynomial matrices C_j=a_d(M_j(1+z))*B_j, and the full
    product of scalar denominators, rather than Laurent matrix products.
    """
    dimension = len(coefficients)-1
    assert level > dimension
    leading = trim(coefficients[-1], prime)
    nonzero_exponents = [j for j, value in enumerate(leading) if value]
    degree_bound = max(nonzero_exponents)-min(nonzero_exponents)
    steps = []
    for j in range(1, level-dimension+1):
        point = -pow(q, j, prime) % prime
        leading_jet = jet(leading, point, len(leading)-1, prime)
        multiplicity = next(k for k, value in enumerate(leading_jet) if value)
        steps.append((point, multiplicity, leading_jet))
    budget = sum(item[1] for item in steps)
    assert budget <= degree_bound
    order = budget+output_order
    product = [np.eye(dimension, dtype=np.int64)]
    product += [np.zeros((dimension, dimension), dtype=np.int64)
                for _ in range(order)]
    denominator_unit = [1]+[0]*order
    for point, multiplicity, leading_jet in steps:
        jets = [jet(poly, point, order, prime) for poly in coefficients]
        matrices = []
        for k in range(order+1):
            matrix = np.zeros((dimension, dimension), dtype=np.int64)
            for j in range(dimension-1):
                matrix[j, j+1] = jets[-1][k]
            matrix[-1, :] = [-jets[j][k] % prime
                              for j in range(dimension)]
            matrices.append(matrix)
        product = mul_matrix_series(matrices, product, order, prime)
        unit = leading_jet[multiplicity:]+[0]*(order+1)
        denominator_unit = mul_series(denominator_unit, unit[:order+1], order, prime)
    inverse = inv_series(denominator_unit, order, prime)
    row = []
    for k in range(order+1):
        value = np.zeros(dimension, dtype=np.int64)
        for j in range(k+1):
            value = (value+inverse[j]*product[k-j][-1, :]) % prime
        row.append(value)
    return row, budget, degree_bound, [item[1] for item in steps]


def central_unit(level, order, prime):
    u_minus_one = [0]+[comb(2*level, j) % prime
                       if j <= 2*level else 0 for j in range(1, order+1)]
    square = mul_series(u_minus_one, u_minus_one, order, prime)
    return [(int(j == 0)+11*u_minus_one[j]+7*square[j]) % prime
            for j in range(order+1)]


def signal(f, point, order, level, prime, coefficient, include_one=True,
           full=False, eta=1):
    values = [(coefficient*value+int(j == 0 and include_one)) % prime
              for j, value in enumerate(jet(f, point, order, prime))]
    values = mul_series(values, central_unit(level, order, prime), order, prime)
    if full:
        # eta*(M-M^-1)*M^N, retaining its meridian zero and root phase.
        difference = [(point if j <= 1 else 0)
                      -pow(point, -1, prime)*pow(-1, j, prime)
                      for j in range(order+1)]
        monomial = [pow(point, level, prime)*comb(level, j) % prime
                    if j <= level else 0 for j in range(order+1)]
        factor = mul_series(difference, monomial, order, prime)
        values = [eta*value % prime
                  for value in mul_series(values, factor, order, prime)]
    return values


def recover(row, budget, initials, output_order, prime):
    order = budget+output_order
    scaled = [sum(int(row[j][a])*initials[a][k-j]
                  for j in range(k+1) for a in range(len(initials))) % prime
              for k in range(order+1)]
    assert all(value == 0 for value in scaled[:budget])
    return scaled[budget:]


def second_order_data(q, multiplicity, prime):
    f = power_poly(mul_poly([q, 1], [q*q % prime, 1], prime), multiplicity, prime)
    g = add_poly(shift_poly(f, q, prime), f, prime, sign=-1)
    shifted_g = shift_poly(g, q, prime)
    assert g[0] == shifted_g[0] == 0
    coefficients = [shifted_g[1:],
                    [(-x-y) % prime for x, y in zip(g, shifted_g)][1:],
                    g[1:]]
    return f, coefficients


def full_coefficients(coefficients, q, prime):
    dimension = len(coefficients)-1
    factors = [[prime-1, 0, pow(q, 2*j, prime)]
               for j in range(dimension+1)]
    result = []
    for j, poly in enumerate(coefficients):
        value = [coefficient*pow(-q, j, prime) % prime for coefficient in poly]
        for k, factor in enumerate(factors):
            if k != j:
                value = mul_poly(value, factor, prime)
        result.append(value)
    return result


def second_order_check(level, multiplicity):
    prime, q, generator = field(level)
    f, coefficients = second_order_data(q, multiplicity, prime)
    row, budget, degree_bound, multiplicities = transfer_row(
        coefficients, q, level, prime, output_order=1)
    order = budget+1
    coefficient = pow(2, level, prime)
    points = [-pow(q, j, prime) % prime for j in (1, 2)]
    initials = [signal(f, point, order, level, prime, coefficient) for point in points]
    assert initials[0][0] == initials[1][0] == 1
    actual = recover(row, budget, initials, 1, prime)
    expected = signal(f, 1, 1, level, prime, coefficient)
    assert actual == expected

    # The saturated solution lattice has basis (1,f): rows 1 and 3
    # give a unit minor, whereas the initial 2x2 determinant has order m.
    assert jet(f, -pow(q, 3, prime) % prime, 0, prime)[0] != 0
    f1, f2 = [jet(f, point, multiplicity, prime) for point in points]
    initial_minor = [(x-y) % prime for x, y in zip(f2, f1)]
    assert all(value == 0 for value in initial_minor[:multiplicity])
    assert initial_minor[multiplicity] != 0
    assert multiplicity <= degree_bound

    # Full/reduced conjugacy is by the fixed rational shift gauge.
    # A common peripheral zero at the target is kept until its first jet.
    full = full_coefficients(coefficients, q, prime)
    full_row, full_budget, full_degree, _ = transfer_row(
        full, q, level, prime, output_order=1)
    assert full_budget == budget
    full_order = full_budget+1
    eta = pow(pow(generator, (prime-1)//4, prime), level+3, prime)
    full_initials = [signal(f, point, full_order, level, prime, coefficient,
                            full=True, eta=eta) for point in points]
    full_actual = recover(full_row, full_budget, full_initials, 1, prime)
    full_expected = signal(f, 1, 1, level, prime, coefficient, full=True, eta=eta)
    assert full_actual == full_expected
    assert full_actual[0] == 0
    assert full_actual[1] == 2*eta*expected[0] % prime
    assert all(value == 0 for value in full_row[0])
    dropped_highest = [values[:-1]+[0] for values in full_initials]
    assert recover(full_row, full_budget, dropped_highest, 1, prime) == full_actual

    return {"level": level, "finite_field_prime": prime,
            "initial_minor_Smith_exponents": [0, multiplicity],
            "leading_M_span": degree_bound, "orbit_pole_budget": budget,
            "singular_steps": [[j+1, value] for j, value in enumerate(multiplicities) if value],
            "two_output_coefficients_exact": True,
            "full_operator_leading_M_span": full_degree,
            "full_residue_frame_first_jet_exact": True,
            "full_gauge_needs_no_additional_initial_jet": True}


def first_order_sharp(level, degree):
    prime, q, _ = field(level)
    f = power_poly([q, 1], degree, prime)
    coefficients = [[-value % prime for value in shift_poly(f, q, prime)], f]
    row, budget, degree_bound, _ = transfer_row(coefficients, q, level, prime)
    assert budget == degree_bound == degree
    assert int(row[0][0]) != 0
    initial = signal(f, -q % prime, budget, level, prime, 1, include_one=False)
    assert initial[:degree] == [0]*degree and initial[degree] != 0
    actual = recover(row, budget, [initial], 0, prime)
    expected = signal(f, 1, 0, level, prime, 1, include_one=False)
    assert actual == expected and actual[0] != 0
    return {"level": level, "leading_M_span": degree,
            "pole_budget_and_necessary_jet_order": budget, "exact_recovery": True}


def symbolic_checks():
    q, M, z = sp.symbols("q M z")
    f = (M+q)*(M+q**2)
    coefficients = [q**2*(M+1), -((q**2+1)*M+q*(q+1)), M+q]
    assert sp.expand(sum(coefficients)) == 0
    assert sp.expand(sum(coefficient*f.subs(M, q**j*M)
                         for j, coefficient in enumerate(coefficients))) == 0
    determinant = sp.expand(f.subs(M, -q**2*(1+z))-f.subs(M, -q*(1+z)))
    assert determinant.subs(z, 0) == 0
    assert sp.factor(sp.diff(determinant, z).subs(z, 0)-q**2*(q**2-1)) == 0
    jet_difference = sp.diff(determinant, z).subs(z, 0)
    ratio = sp.cancel(f.subs(M, 1)/jet_difference)
    assert sp.cancel(ratio-(1+q)*(1+q**2)/(q**2*(q**2-1))) == 0
    return {"fixed_second_order_operator_annihilates_1_and_f": True,
            "ordinary_initial_values_equal_but_first_jet_free": True,
            "explicit_first_jet_period_formula": str(ratio),
            "arbitrary_c_N_changes_target_without_changing_operator_or_two_values": True}


def main():
    results = {"scope": "Manufactured operator diagnostics, not a knot volume theorem.",
               "symbolic": symbolic_checks(),
               "second_order": [second_order_check(level, multiplicity)
                                for level in (4, 5, 6, 8, 9, 12, 15, 18, 24, 30)
                                for multiplicity in (1, 2, 3) if level > multiplicity],
               "sharp_first_order": [first_order_sharp(level, degree)
                                     for level in (3, 4, 6, 9, 15, 24, 30)
                                     for degree in (1, 2, 3, 5)]}
    path = Path(__file__).with_name("bounded_meridian_jets_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"symbolic": "passed", "second_order_cases": len(results["second_order"]),
                      "sharp_bound_cases": len(results["sharp_first_order"]),
                      "full_state_gauge_checks": "passed", "result_file": str(path)}, indent=2))


if __name__ == "__main__":
    main()
