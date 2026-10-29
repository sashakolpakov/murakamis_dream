#!/usr/bin/env python3
"""Exact checks of meridian anchors and pointed cyclic-kernel periods.

Full N-dimensional colors and their j-dimensional quotients are evaluated
independently. The cofactor test uses a manufactured second-order operator
with a known one-dimensional generic kernel and a larger special kernel.
No claim about a knot's volume or its actual operator rank is made.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import determinant, rank
from audit_kashaev_ado_pointing import color_matrices, reduced_period, WORDS


def field(N, exclude_two=False):
    p = next(4*N*k+1 for k in range(1, 1000)
             if sp.isprime(4*N*k+1)
             and (not exclude_two or pow(2, 2*N, 4*N*k+1) != 1))
    g = int(sp.primitive_root(p))
    q = pow(g, (p-1)//(2*N), p)
    return p, q


def two_strand_period(dimension, prime, positive, negative, pivotal, theta, writhe):
    matrix = np.eye(dimension*dimension, dtype=np.int64)
    crossing = positive if writhe > 0 else negative
    for j in range(abs(writhe)):
        matrix = matrix@crossing % prime
    matrix = matrix@np.kron(np.eye(dimension, dtype=np.int64), pivotal) % prime
    cut = np.einsum('abcb->ac', matrix.reshape((dimension,)*4)) % prime
    cut = cut*pow(theta, -writhe, prime) % prime
    assert np.array_equal(cut, int(cut[0, 0])*np.eye(dimension, dtype=np.int64) % prime)
    return int(cut[0, 0])


def color_anchors(N):
    prime, q = field(N)
    comparisons = triples = 0
    anchor_values = []
    for j in range(1, N+1):
        x = pow(q, j-1, prime)
        full = color_matrices(N, prime, q, x)
        quotient = color_matrices(j, prime, q, x)
        standard_pivotal = np.diag([x*pow(q, -2*a, prime) % prime
                                    for a in range(j)]).astype(np.int64)
        standard = (quotient[0], quotient[1], standard_pivotal, x)
        for writhe in (1, 3, -3):
            actual = two_strand_period(N, prime, *full, writhe)
            expected = two_strand_period(j, prime, *standard, writhe)
            assert actual == expected
            if j == 1:
                assert actual == 1
                anchor_values.append(actual)
            comparisons += 1
        if N <= 6:
            actual = reduced_period(N, prime, *full, WORDS[0])
            expected = reduced_period(j, prime, *standard, WORDS[0])
            assert actual == expected
            if j == 1:
                assert actual == 1
                anchor_values.append(actual)
            triples += 1
    mstar = -q % prime
    assert mstar*pow(q, N-1, prime) % prime == 1
    assert pow(mstar, 2*N, prime) == 1
    eta = pow(-1, N+1, prime)*pow(q, N*(1-N)//2, prime) % prime
    residue = (eta*(mstar-pow(mstar, -1, prime))*pow(mstar, N, prime)) % prime
    expected_residue = eta*pow(-1, N, prime)*(q-pow(q, -1, prime)) % prime
    assert residue == expected_residue and residue != 0
    return {"level": N, "finite_field_prime": prime,
            "all_integer_colors_checked": N, "two_strand_cut_comparisons": comparisons,
            "three_strand_cut_comparisons": triples,
            "trivial_quotient_anchor_values": anchor_values,
            "same_central_fiber_and_orbit": True,
            "full_state_central_residue_exact": True}


def polynomial_matrix(coefficients, X, prime):
    value = np.zeros_like(X)
    eye = np.eye(len(X), dtype=np.int64)
    for coefficient in reversed(coefficients):
        value = (value@X+int(coefficient)*eye) % prime
    return value


def polynomial_matrix_derivative(coefficients, X, derivative, prime):
    value = np.zeros_like(X)
    differentiated = np.zeros_like(X)
    eye = np.eye(len(X), dtype=np.int64)
    for coefficient in reversed(coefficients):
        differentiated = (differentiated@X+value@derivative) % prime
        value = (value@X+int(coefficient)*eye) % prime
    return differentiated


def adjugate_derivative_column(A0, A1, column, prime):
    n = len(A0)
    values = []
    for row in range(n):
        minor = np.delete(np.delete(A0, column, axis=0), row, axis=1)
        derivative = np.delete(np.delete(A1, column, axis=0), row, axis=1)
        coefficient = 0
        for j in range(n-1):
            replaced = minor.copy()
            replaced[:, j] = derivative[:, j]
            coefficient += determinant(replaced, prime)
        values.append(pow(-1, row+column, prime)*coefficient % prime)
    return np.array(values, dtype=np.int64)


def monodromy_hilbert90(N):
    prime, q = field(N, exclude_two=True)
    n = 2*N
    generator = int(sp.primitive_root(prime))
    points = [generator*pow(q, j, prime) % prime for j in range(n)]
    denominator = 2*q*q*(1+q*q) % prime

    def actual_f(m):
        return (m-q)*(m-pow(q, 3, prime))*pow(denominator, -1, prime) % prime

    values = [actual_f(m) for m in points]
    assert all(values) and pow(points[0], n, prime) != 1
    matrices = []
    inverses = []
    for j in range(n):
        coefficient = (values[(j+2) % n]+2*values[j])*pow(values[(j+1) % n], -1, prime) % prime
        matrix = np.array([[0, -2], [1, coefficient]], dtype=np.int64) % prime
        inverse = np.array([[coefficient, 2], [-1, 0]], dtype=np.int64)*pow(2, -1, prime) % prime
        matrices.append(matrix)
        inverses.append(inverse)
    H = np.eye(2, dtype=np.int64)
    for matrix in matrices:
        H = H@matrix % prime
    orbit = [H]
    for j in range(n):
        following = inverses[j]@orbit[-1] % prime
        following = following@matrices[j] % prime
        orbit.append(following)
    assert np.array_equal(orbit[0], orbit[-1])
    adjugates = []
    for monodromy in orbit[:-1]:
        residual = (monodromy-np.eye(2, dtype=np.int64)) % prime
        assert rank(residual, prime) == 1
        adjugates.append(np.array([[residual[1, 1], -residual[0, 1]],
                                  [-residual[1, 0], residual[0, 0]]], dtype=np.int64) % prime)
    for parameter in range(prime):
        rows = [(a[0]+parameter*a[1]) % prime for a in adjugates]
        if all(int(row[0]) for row in rows):
            break
    else:
        raise AssertionError("No common nonzero row frame on the finite etale orbit")
    ratios = []
    for j in range(n):
        transformed = rows[(j+1) % n]@inverses[j] % prime
        ratio = int(transformed[0])*pow(int(rows[j][0]), -1, prime) % prime
        assert np.array_equal(transformed, ratio*rows[j] % prime)
        ratios.append(ratio)
    norm = 1
    for value in ratios:
        norm = norm*value % prime
    assert norm == 1
    for degree in range(n):
        averaged = []
        for start in range(n):
            prefix = 1
            total = 0
            for j in range(n):
                total += prefix*pow(points[(start+j) % n], degree, prime)
                prefix = prefix*ratios[(start+j) % n] % prime
            averaged.append(total % prime)
        if averaged[0]:
            break
    else:
        raise AssertionError("Hilbert-90 averaging vanished on a basis")
    assert all(averaged)
    for j in range(n):
        assert ratios[j]*averaged[(j+1) % n] % prime == averaged[j]
    pairings = [averaged[j]*rows[j] % prime for j in range(n)]
    for j in range(n):
        assert np.array_equal(pairings[j]@matrices[j] % prime, pairings[(j+1) % n])
    solution = [int(row[0]) for row in pairings]
    central_scalar = solution[0]*pow(values[0], -1, prime) % prime
    assert all(value == central_scalar*known % prime for value, known in zip(solution, values))
    return {"level": N, "finite_field_prime": prime,
            "monodromy_row_line_and_cyclic_conjugacy_exact": True,
            "norm_one_cocycle": norm, "Hilbert90_seed_degree": degree,
            "constructed_scalar_period_exact": True}


def higher_rank_anchor_counterexample(N):
    assert N % 2 == 0
    prime, q = field(N)
    n = 2*N
    S = np.diag([pow(q, j, prime) for j in range(n)]).astype(np.int64)
    operator = (S@S-np.eye(n, dtype=np.int64)) % prime
    assert rank(operator, prime) == n-2
    first = np.zeros(n, dtype=np.int64)
    first[0] = 1
    second = first.copy()
    second[0] = 4
    second[N] = 3
    assert not np.any(operator@first % prime) and not np.any(operator@second % prime)
    mstar = -q % prime
    anchor = np.array([pow(mstar, j, prime) for j in range(n)], dtype=np.int64)
    assert int(anchor@first) % prime == int(anchor@second) % prime == 1
    assert int(np.sum(first)) % prime != int(np.sum(second)) % prime
    return {"level": N, "rational_kernel_dimension": 2,
            "equal_reference_values": [1, 1], "different_target_values": [1, 7],
            "scope": "The line-rank hypothesis is essential; no knot-conjecture counterexample."}


def singular_cofactor_period(N):
    prime, q = field(N, exclude_two=True)
    n = 2*N
    eye = np.eye(n, dtype=np.int64)
    X = np.roll(eye, 1, axis=0)
    X1 = np.zeros_like(X)
    X1[0, n-1] = 1
    S = np.diag([pow(q, j, prime) for j in range(n)]).astype(np.int64)
    # f(M)=((M-q)(M-q^3))/(2 q^2(1+q^2)); f(-q)=1.
    denominator = 2*q*q*(1+q*q) % prime
    inverse = pow(denominator, -1, prime)
    coefficients = [pow(q, 4, prime)*inverse % prime,
                    -(q+pow(q, 3, prime))*inverse % prime, inverse]
    vector = np.array(coefficients+[0]*(n-3), dtype=np.int64)
    shifted_coefficients = [c*pow(q, j, prime) % prime for j, c in enumerate(coefficients)]
    f0 = polynomial_matrix(coefficients, X, prime)
    fq0 = polynomial_matrix(shifted_coefficients, X, prime)
    f1 = polynomial_matrix_derivative(coefficients, X, X1, prime)
    fq1 = polynomial_matrix_derivative(shifted_coefficients, X, X1, prime)
    D0, D1 = (f0@S-fq0) % prime, (f1@S-fq1) % prime
    A0, A1 = (S-2*eye)@D0 % prime, (S-2*eye)@D1 % prime
    # Independently build P=(T-2)(f(M)T-f(qM)) from its three coefficients.
    p2 = shifted_coefficients
    p1 = [(-c*pow(q, 2*j, prime)-2*c) % prime for j, c in enumerate(coefficients)]
    p0 = [2*c % prime for c in shifted_coefficients]
    direct = (polynomial_matrix(p2, X, prime)@S@S
              +polynomial_matrix(p1, X, prime)@S+polynomial_matrix(p0, X, prime)) % prime
    assert np.array_equal(direct, A0)
    assert not np.any(A0@vector % prime) and not np.any(A1@vector % prime)
    assert rank(A0+A1, prime) == n-1
    assert rank(A0, prime) == n-2
    mstar = -q % prime
    anchor = np.array([pow(mstar, j, prime) for j in range(n)], dtype=np.int64)
    assert int(anchor@vector) % prime == 1
    expected = int(np.sum(vector)) % prime
    checked = 0
    columns_used = []
    for column in range(n):
        w = adjugate_derivative_column(A0, A1, column, prime)
        if not np.any(w):
            continue
        scale = int(w[0])*pow(int(vector[0]), -1, prime) % prime
        assert np.array_equal(w, scale*vector % prime)
        reconstructed = int(np.sum(w))*pow(int(anchor@w) % prime, -1, prime) % prime
        assert reconstructed == expected
        checked += 1
        columns_used.append(column)
        if checked == 2:
            break
    assert checked == 2
    # Independently build the primitive full-state numerator
    # (u-1) h_full = eta (M^(N+1)-M^(N-1)) f(M).
    eta = pow(-1, N+1, prime)*pow(q, N*(1-N)//2, prime) % prime
    numerator0 = np.zeros(n, dtype=np.int64)
    numerator1 = np.zeros(n, dtype=np.int64)
    for j, coefficient in enumerate(coefficients):
        for shift, sign in ((N+1, 1), (N-1, -1)):
            power, residue = divmod(j+shift, n)
            value = eta*sign*coefficient % prime
            numerator0[residue] = (numerator0[residue]+value) % prime
            numerator1[residue] = (numerator1[residue]+power*value) % prime
    assert int(np.sum(numerator0)) % prime == 0
    rho = (q-pow(q, -1, prime)) % prime
    marked_residue = int(anchor@numerator0) % prime
    assert marked_residue == eta*pow(-1, N, prime)*rho % prime
    jet = (int(np.sum(numerator1))+sum(j*int(value)*pow(n, -1, prime)
                                     for j, value in enumerate(numerator0))) % prime
    assert jet == eta*pow(N, -1, prime)*expected % prime
    reconstructed_full = N*pow(-1, N, prime)*rho*jet*pow(marked_residue, -1, prime) % prime
    assert reconstructed_full == expected
    return {"level": N, "root_order": n, "finite_field_prime": prime,
            "generic_kernel_dimension": 1, "special_kernel_dimension": 2,
            "cofactor_common_valuation": 1, "primitive_cofactor_columns": columns_used,
            "operator_period_ratio_exact": True,
            "full_state_residue_and_meridian_jet_exact": True,
            "scope": "A manufactured operator diagnoses the lattice prescription; no knot-operator rank claim."}


def main():
    results = {"scope": "Exact root-orbit pointing and operator-period diagnostics; no volume-growth theorem.",
               "literature_color_anchors": [color_anchors(N) for N in (2, 3, 4, 5, 6, 9, 15)],
               "monodromy_descent": [monodromy_hilbert90(N) for N in (3, 4, 5, 6, 9, 15)],
               "higher_rank_anchor_counterexamples": [higher_rank_anchor_counterexample(N) for N in (2, 4, 6)],
               "singular_kernel_periods": [singular_cofactor_period(N) for N in (3, 4, 5, 6, 9, 15)]}
    Path(__file__).with_name("root_orbit_pointing_results.json").write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps(results), flush=True)


if __name__ == "__main__":
    main()
