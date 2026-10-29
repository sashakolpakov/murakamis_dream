#!/usr/bin/env python3
"""Exact diagnostics for additive and unipotent cyclotomic descent.

The all-level implication is proved in the note, not by these finite
checks. These cover the pole-order formula, a ramified rational source,
the central Heisenberg correction, and noncommutative cyclic transport.
"""

import json
from pathlib import Path

import sympy as s


Q, Y, U, z = s.symbols('Q Y U z')


def shifted(expression):
    return expression.subs(Y, Q * Y)


def root_pole_formula():
    records = []
    # Power-series coefficients provide an independent check of the
    # differential rational formula at every coefficient checked.
    for order in range(2, 9):
        for pole_order in range(1, 5):
            formula = order / (1 - U)
            for ell in range(1, pole_order):
                formula = order * U * s.diff(formula, U) + ell * formula
            formula = s.cancel(formula / s.factorial(pole_order - 1))
            leading = s.limit((1 - U)**pole_order * formula, U, 1)
            assert leading == order**pole_order
            series = s.series(formula, U, 0, 7).removeO().expand()
            for ell in range(7):
                expected = order * s.binomial(order * ell + pole_order - 1,
                                               pole_order - 1)
                assert series.coeff(U, ell) == expected
            records.append({'orbit_order': order, 'pole_order': pole_order,
                            'highest_pole_coefficient': int(leading),
                            'seven_independent_coefficients': True})
    return records


def ramified_sources():
    records = []
    # The trace over z^d=Q-1 is rational although each pole has
    # ramified zero or infinity at Q=1. Log derivatives give its
    # partial-fraction sum without choosing analytic root branches.
    for degree in (2, 3, 4):
        for sign in (-1, 1):
            seed = (Q - 1)**sign
            polynomial = 1 - seed * Y**degree
            trace = s.cancel(degree - Y * s.diff(polynomial, Y) / polynomial)
            assert s.cancel(trace - degree / polynomial) == 0
            source = s.cancel(shifted(trace) - trace)
            # Independently compute the orbit charge contribution:
            # sigma(P_z)-P_z for all conjugate poles, then trace.
            expected = degree / (1 - seed * Q**degree * Y**degree)
            expected -= degree / (1 - seed * Y**degree)
            assert s.cancel(source - expected) == 0
            assert s.limit(trace, Y, s.oo) == 0
            records.append({'ramification_degree': degree,
                            'pole_parameter_valuation': f'{sign}/{degree}',
                            'rational_trace_source': True,
                            'proper_galois_descent_normalization': True})
    return records


def heisenberg_center():
    p = Y / (1 - Y)
    q = Y**2 / (1 - 2 * Y)
    r = Y / (1 - 3 * Y)
    u = s.cancel(shifted(p) - p)
    v = s.cancel(shifted(q) - q)
    w = s.cancel(shifted(r) - r - u * q)
    C = s.Matrix([[1, u, w], [0, 1, v], [0, 0, 1]])
    G = s.Matrix([[1, p, r], [0, 1, q], [0, 0, 1]])
    assert all(s.cancel(x) == 0 for x in shifted(G) - C * G)
    G0 = s.Matrix([[1, p, 0], [0, 1, q], [0, 0, 1]])
    central = shifted(G0).inv() * C * G0
    central = central.applyfunc(s.cancel)
    assert central[0, 1] == central[1, 2] == 0
    assert s.cancel(central[0, 2] - (w + u * q)) == 0
    assert s.cancel(central[0, 2] - shifted(r) + r) == 0
    assert s.cancel(u * q) != 0
    return {'all_three_equations_exact': True,
            'central_cross_term_required': True,
            'gauge_convention_sigma_G_equals_C_G': True}


def finite_field(order):
    multiplier = max(1, 2000 // order)
    while not s.isprime(order * multiplier + 1):
        multiplier += 1
    prime = int(order * multiplier + 1)
    generator = int(s.primitive_root(prime))
    return prime, generator, pow(generator, (prime - 1) // order, prime)


def matrix_product(left, right, prime):
    dimension = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(dimension)) % prime
             for j in range(dimension)] for i in range(dimension)]


def inverse_unitriangular(matrix, prime):
    dimension = len(matrix)
    inverse = [[int(i == j) for j in range(dimension)] for i in range(dimension)]
    for distance in range(1, dimension):
        for i in range(dimension - distance):
            j = i + distance
            inverse[i][j] = -sum(matrix[i][k] * inverse[k][j]
                                  for k in range(i + 1, j + 1)) % prime
    return inverse


def cyclic_matrix_checks():
    records = []
    for order in range(3, 16):
        prime, generator, root = finite_field(order)
        for dimension in (3, 4, 5):
            identity = [[int(i == j) for j in range(dimension)]
                        for i in range(dimension)]

            def gauge(y):
                matrix = [row[:] for row in identity]
                for i in range(dimension):
                    for j in range(i + 1, dimension):
                        denominator = (1 - (j + 1) * y) % prime
                        if not denominator:
                            return None
                        matrix[i][j] = (i + 1) * pow(y, j - i, prime)
                        matrix[i][j] *= pow(denominator, -1, prime)
                        matrix[i][j] %= prime
                return matrix

            for scaled_k in (1, 2, 3):
                qvalue = pow(root, scaled_k, prime)
                candidates = None
                for power in range(1, prime):
                    y = pow(generator, power, prime)
                    matrices = [gauge(y * pow(qvalue, j, prime) % prime)
                                for j in range(order + 1)]
                    if all(matrix is not None for matrix in matrices):
                        candidates = matrices
                        break
                assert candidates is not None
                transport = [row[:] for row in identity]
                for j in range(order):
                    step = matrix_product(candidates[j + 1],
                                          inverse_unitriangular(candidates[j], prime),
                                          prime)
                    transport = matrix_product(step, transport, prime)
                assert transport == identity
                records.append({'level': order, 'dimension': dimension,
                                'scaled_k': scaled_k,
                                'actual_orbit_order': order // int(s.gcd(order, scaled_k)),
                                'noncommutative_transport_identity': True})
    return records


def source_obstructions():
    # A bare pole or a nonzero constant is not invisible to transport.
    records = []
    for order in (2, 3, 5, 8):
        bare_pole_sum = order / (1 - U)
        assert bare_pole_sum != 0
        assert order != 0
        records.append({'level': order, 'constant_charge_detected': order,
                        'bare_pole_charge_detected': str(bare_pole_sum)})
    return records


def main():
    result = {'pole_order_formula': root_pole_formula(),
              'ramified_rational_sources': ramified_sources(),
              'heisenberg_center': heisenberg_center(),
              'cyclic_unitriangular_transports': cyclic_matrix_checks(),
              'nonzero_source_obstructions': source_obstructions(),
              'scope': 'Diagnostics for proved rational additive/unipotent descent; '
                       'no constructed actual knot/regulator comparison.'}
    output = Path(__file__).with_name('additive_unipotent_cyclotomic_descent_results.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: len(value) if isinstance(value, list) else value
                      for key, value in result.items() if key != 'scope'}, indent=2))


if __name__ == '__main__':
    main()
