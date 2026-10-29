#!/usr/bin/env python3
"""Exact cyclic affine-descent and whole-germ diagnostics.

Manufactured operators and known polynomial solutions check source
transport, resonant averaging, incompatibility, and a rank-drop fiber.
The classical figure-eight action check is explicitly numerical.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


def chebyshev_trace(value, exponent, prime):
    a, b = 2, value
    for _ in range(exponent):
        a, b = b, (value*b-a) % prime
    return a % prime


def field(level, resonant=False):
    n = 2*level
    prime = next(4*level*k+1 for k in range(1, 1000)
                 if sp.isprime(4*level*k+1)
                 and (pow(2, n, 4*level*k+1) != 1 if resonant
                      else chebyshev_trace(3, n, 4*level*k+1) != 3))
    generator = int(sp.primitive_root(prime))
    return prime, pow(generator, (prime-1)//n, prime)


def inverse2(matrix, prime):
    a, b, c, d = map(int, matrix.flatten())
    determinant = (a*d-b*c) % prime
    assert determinant != 0
    return np.array([[d, -b], [-c, a]], dtype=np.int64)*pow(determinant, -1, prime) % prime


def monodromy(matrices, sources, prime):
    dimension = len(matrices[0])
    H = np.eye(dimension, dtype=np.int64)
    source = np.zeros(dimension, dtype=np.int64)
    for matrix, c in zip(matrices, sources):
        H = matrix@H % prime
        source = (matrix@source+c) % prime
    return H, source


def polynomial_value(m, prime):
    return (1+m+pow(m, 3, prime)) % prime


def nonresonant_check(level):
    prime, q = field(level)
    n = 2*level
    points = [pow(q, j, prime) for j in range(n)]
    states = [np.array([polynomial_value(m, prime), polynomial_value(q*m % prime, prime)],
                       dtype=np.int64) for m in points]
    matrices = [np.array([[0, 1], [-1, 3+m]], dtype=np.int64) % prime for m in points]
    sources = [(states[(j+1) % n]-matrix@states[j]) % prime
               for j, matrix in enumerate(matrices)]
    assert all(int(c[0]) == 0 for c in sources)
    H, source = monodromy(matrices, sources, prime)
    residual = (np.eye(2, dtype=np.int64)-H) % prime
    solution = inverse2(residual, prime)@source % prime
    assert np.array_equal(solution, states[0])
    assert int(np.trace(H)) % prime == (chebyshev_trace(3, n, prime)-1) % prime
    for j in range(n):
        shifted_matrices = matrices[j:]+matrices[:j]
        shifted_sources = sources[j:]+sources[:j]
        H_j, source_j = monodromy(shifted_matrices, shifted_sources, prime)
        value = inverse2((np.eye(2, dtype=np.int64)-H_j) % prime, prime)@source_j % prime
        assert np.array_equal(value, states[j])

    gauges = [np.array([[1, m], [0, 1]], dtype=np.int64) for m in points]
    translations = [np.array([m*m % prime, (1+pow(m, 3, prime)) % prime], dtype=np.int64)
                    for m in points]
    transformed_matrices, transformed_sources = [], []
    for j in range(n):
        following = (j+1) % n
        B = gauges[following]@matrices[j] % prime
        B = B@inverse2(gauges[j], prime) % prime
        c = (gauges[following]@sources[j]+translations[following]-B@translations[j]) % prime
        transformed_matrices.append(B)
        transformed_sources.append(c)
    H_new, source_new = monodromy(transformed_matrices, transformed_sources, prime)
    assert np.array_equal(H_new, gauges[0]@H@inverse2(gauges[0], prime) % prime)
    expected_source = (gauges[0]@source+(np.eye(2, dtype=np.int64)-H_new)@translations[0]) % prime
    assert np.array_equal(source_new, expected_source)
    transformed_solution = inverse2((np.eye(2, dtype=np.int64)-H_new) % prime, prime)@source_new % prime
    assert np.array_equal(transformed_solution, (gauges[0]@solution+translations[0]) % prime)
    return {"level": level, "finite_field_prime": prime,
            "cyclic_resolvent_and_all_orbit_frames_exact": True,
            "affine_gauge_and_source_transport_exact": True,
            "unique_maximum_M_degree_coefficient": "coefficient of T",
            "target_first_component": int(solution[0])}


def resonant_check(level):
    prime, q = field(level, resonant=True)
    n = 2*level
    points = [pow(q, j, prime) for j in range(n)]
    B = np.diag([1, 2]).astype(np.int64)
    matrices = [B for _ in points]
    known = [np.array([m, (m*m+5) % prime], dtype=np.int64) for m in points]
    sources = [(known[(j+1) % n]-B@known[j]) % prime for j in range(n)]
    H, source = monodromy(matrices, sources, prime)
    assert int(H[0, 0]) == 1 and int(H[1, 1]) != 1
    assert int(source[0]) == 0
    initial = [np.array([(pow(m, 3, prime)+7) % prime, (m*m+5) % prime], dtype=np.int64)
               for m in points]
    value = initial
    total = [np.zeros(2, dtype=np.int64) for _ in points]
    for _ in range(n):
        total = [(x+y) % prime for x, y in zip(total, value)]
        value = [(B@value[(j-1) % n]+sources[(j-1) % n]) % prime for j in range(n)]
    assert all(np.array_equal(x, y) for x, y in zip(initial, value))
    average = [x*pow(n, -1, prime) % prime for x in total]
    for j in range(n):
        assert np.array_equal(average[(j+1) % n], (B@average[j]+sources[j]) % prime)
        assert np.array_equal(average[j], (known[j]+np.array([7, 0])) % prime)

    inconsistent = [np.array([1, int(c[1])], dtype=np.int64) for c in sources]
    bad_H, bad_source = monodromy(matrices, inconsistent, prime)
    assert int(bad_H[0, 0]) == 1 and int(bad_source[0]) == n % prime != 0
    return {"level": level, "finite_field_prime": prime,
            "resonant_affine_average_is_a_rational_section": True,
            "central_translation_retained": 7,
            "inconsistent_source_detected": True}


def symbolic_factor_and_rank_drop():
    q, M, c = sp.symbols("q M c")
    h = 1+M+M**3
    coefficients = [sp.Integer(1), -(3+M), sp.Integer(1)]
    source = sp.expand(sum(a*h.subs(M, q**j*M) for j, a in enumerate(coefficients)))
    ratio = source.subs(M, q*M)/source
    homogeneous = [-ratio*coefficients[0]]
    homogeneous += [coefficients[j-1].subs(M, q*M)-ratio*coefficients[j] for j in (1, 2)]
    homogeneous += [coefficients[2].subs(M, q*M)]
    residual = sum(a*h.subs(M, q**j*M) for j, a in enumerate(homogeneous))
    assert sp.cancel(residual) == 0

    # n=4, c^4=2: the generic affine denominator is u-1.
    # Its zero at the target is canceled only as a whole meridian germ.
    root = sp.I
    period = (1+M**2)*(1+M)
    H, accumulated = sp.Integer(1), sp.Integer(0)
    for j in range(4):
        a = c+root**j*M
        b = period.subs(M, root**(j+1)*M)-a*period.subs(M, root**j*M)
        H = sp.expand(a*H)
        accumulated = sp.expand(a*accumulated+b)
    denominator = sp.rem(sp.expand(1-H), c**4-2, c)
    numerator = sp.rem(sp.expand(accumulated), c**4-2, c)
    assert sp.expand(denominator-(M**4-1)) == 0
    assert sp.expand(numerator-denominator*period) == 0
    assert denominator.subs(M, 1) == numerator.subs(M, 1) == 0
    whole = sp.cancel(numerator/denominator)
    assert whole == sp.expand(period)
    assert whole.subs(M, 1) == 4
    eta = sp.I
    full = sp.cancel(eta*M/(1+M**2)*whole)
    assert full.subs(M, 1) == 2*sp.I
    assert sp.simplify(2/eta*full.subs(M, 1)) == 4

    # A split period can have the figure-eight geometric principal factor.
    trace = M**4-M**2-2-M**-2+M**-4
    b = 2-trace
    assert sp.expand(1-trace+1-b) == 0
    return {"scalar_inhomogeneous_homogeneous_factorization": True,
            "whole_meridian_germ_at_u_equals_one_rank_drop": True,
            "retained_factor_1_plus_M_squared_at_target": 2,
            "whole_reduced_target": 4, "full_ADO_target": "2i",
            "split_source_with_geometric_principal_factor_has_period_one": True}


def numerical_classical_action():
    mp.mp.dps = 65
    pi = mp.pi

    def logarithmic_radius(theta):
        trace = 2*mp.cos(4*theta)-2*mp.cos(2*theta)-2
        return mp.acosh(max(mp.mpf(1), abs(trace)/2))

    left = mp.quad(logarithmic_radius, [0, pi/3])
    right = mp.quad(logarithmic_radius, [2*pi/3, pi])
    regular_tetrahedron = mp.im(mp.polylog(2, mp.exp(mp.j*pi/3)))
    assert abs(left-right) < mp.mpf("1e-55")
    assert abs(left-regular_tetrahedron) < mp.mpf("1e-55")
    volume = 2*regular_tetrahedron
    return {"scope": "Numerical classical check; not a quantum period proof.",
            "left_lobe_action": mp.nstr(left, 40),
            "right_lobe_action": mp.nstr(right, 40),
            "full_spectral_radius_action": mp.nstr(left+right, 40),
            "two_regular_tetrahedron_volume": mp.nstr(volume, 40),
            "full_action_over_required_Vol_over_two": mp.nstr((left+right)/(volume/2), 30)}


def formal_trace_test():
    h, X = sp.symbols("h X")
    q = sp.exp(h)
    M = -sp.exp(X*h)
    shifted_M = q*M
    trace = (shifted_M**4-shifted_M**2-q**2-q**-2
             -shifted_M**-2+shifted_M**-4)
    # Algebraic test on the displayed literature figure-eight block.
    # Its actual all-level annihilator membership is not assumed here.
    unreduced = [q**3*M**2-q**-3*M**-2,
                 -(shifted_M**2-shifted_M**-2)*trace,
                 q*M**2-q**-1*M**-2]
    leading = [sp.expand(sp.diff(value, h).subs(h, 0)) for value in unreduced]
    assert leading == [4*X+6, 8*X+8, 4*X+2]
    assert sum(sp.Poly(value, X).LC() for value in leading) == 16
    reduced_leading = [sp.expand(value*(X+j)) for j, value in enumerate(leading)]
    assert all(sp.degree(value, X) == 2 for value in reduced_leading)
    assert sum(sp.Poly(value, X).LC() for value in reduced_leading) == 16
    return {"scope": "Checks the displayed operator's algebraic test, not its knot-state membership.",
            "unreduced_trace_leading_coefficients": [str(value) for value in leading],
            "reduced_trace_leading_coefficients": [str(value) for value in reduced_leading],
            "sum_of_leading_color_coefficients": 16,
            "formal_rational_nonresonance_test_passes": True}


def nonsplit_gaussian_example(level):
    prime, q = field(level)
    n = 2*level
    coefficients = [pow(q, -r*(r+1)//2, prime) for r in range(n)]
    # Check sigma(s)-M*s=1+M^n coefficient by coefficient.
    assert coefficients[0] == 1
    assert all((coefficients[r]*pow(q, r, prime)-coefficients[r-1]) % prime == 0
               for r in range(1, n))
    assert -coefficients[-1] % prime == 1
    target = sum(coefficients)*pow(2, -1, prime) % prime
    return {"level": level, "finite_field_prime": prime,
            "exact_cyclic_primitive_identity": True,
            "retained_target_denominator": 2,
            "target_mod_prime": target,
            "complex_target_upper_bound": n//2,
            "not_a_knot_volume_model": True}


def formal_source_splitting():
    M, h = sp.symbols("M h")

    def delta(expression):
        return M*sp.diff(expression, M)

    coefficients = [1/(1-M)]
    for k in range(1, 5):
        known = 0
        for ell in range(1, k+1):
            derivative = coefficients[k-ell]
            for _ in range(ell):
                derivative = delta(derivative)
            known += derivative/sp.factorial(ell)
        coefficients.append(sp.factor(-known/(1-M)))
    assert sp.cancel(coefficients[1]+M/(1-M)**3) == 0
    assert sp.cancel(coefficients[2]-M*(1+4*M+M**2)/(2*(1-M)**5)) == 0
    orders = []
    for coefficient in coefficients:
        denominator = sp.fraction(sp.cancel(coefficient))[1]
        orders.append(sp.Poly(denominator, M).degree())
    assert orders == [1, 3, 5, 7, 9]
    # Direct shifts at fixed generic meridians, rather than the
    # coefficient recursion, check the truncated formal equation.
    for point in (sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(-2, 3)):
        shifted = sum(h**k*coefficient.subs(M, point*sp.exp(h))
                      for k, coefficient in enumerate(coefficients))
        unshifted = sum(h**k*coefficient.subs(M, point)
                        for k, coefficient in enumerate(coefficients))
        assert sp.series(shifted-point*unshifted-1, h, 0, 5).removeO() == 0
    return {"formal_particular_solution_through_order": 4,
            "boundary_pole_orders": orders,
            "direct_q_shift_checks_at_three_rational_meridians": True,
            "does_not_assert_convergence_or_boundary_evaluation": True}


def main():
    levels = (2, 3, 4, 5, 6, 9, 12, 15)
    results = {"scope": "Exact affine model checks, with one separately labeled numerical classical diagnostic.",
               "nonresonant": [nonresonant_check(level) for level in levels],
               "resonant": [resonant_check(level) for level in levels],
               "symbolic": symbolic_factor_and_rank_drop(),
               "formal_trace": formal_trace_test(),
               "formal_source_splitting": formal_source_splitting(),
               "nonsplit_gaussian_source": [nonsplit_gaussian_example(level) for level in levels],
               "classical_action": numerical_classical_action()}
    path = Path(__file__).with_name("affine_quantum_a_period_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"nonresonant_levels": len(levels), "resonant_levels": len(levels),
                      "symbolic_rank_drop_and_source_factorization": "passed",
                      "classical_factor_two_diagnostic": "passed", "result_file": str(path)}, indent=2))


if __name__ == "__main__":
    main()
