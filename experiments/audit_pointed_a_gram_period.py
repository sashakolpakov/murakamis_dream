#!/usr/bin/env python3
"""Exact pointed A-period Gram ratios, including singular jet steps.

The uniform theorem is in notes/pointed_a_gram_period.md. Tests use
symbolic positive Gram polynomials and cyclotomic evaluations modulo
primes. The hyperbolic polynomial block is a calibration, with an
additional original-R comparison only at the explicitly listed levels.
No all-level knot identification or volume estimate is inferred from it.
"""

import json
from math import comb
from pathlib import Path

import numpy as np
import sympy as sp
from flint import nmod_mat

from audit_cyclic_steinberg_lattice import rank
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_peripheral_normal_period import operator_calibration, coefficient_terms


class FiniteFieldGramDegeneracy(ArithmeticError):
    """An isotropic reduction of a positive complex Gram pairing."""


def symbolic_gram(M, b, R):
    lam, z = sp.symbols('lambda z')
    n = M.cols
    nu = n-M.rank()
    assert M.row_join(b).rank() == M.rank()
    assert M.col_join(R).rank() == M.rank()
    P, g = M.T*M, M.T*b
    bottom = (b.T*M).row_join(b.T*b)
    bordered = (P+lam*sp.eye(n)+z*R.T*R).row_join(g).col_join(bottom)
    denominator = sp.Poly((P+lam*sp.eye(n)).det(), lam)
    numerator = sp.Poly(bordered.det(), lam, z)
    assert all(c >= 0 for c in denominator.coeffs())
    assert all(c >= 0 for c in numerator.coeffs())
    ratio = numerator.coeff_monomial(lam**nu*z)/denominator.coeff_monomial(lam**nu)
    solution = M.gauss_jordan_solve(b)[0]
    target = R*solution
    assert not target.free_symbols
    assert ratio == (target.T*target)[0]
    U = sp.Matrix.hstack(*M.T.columnspace())
    Pr, Qr, gr = U.T*P*U, U.T*R.T*R*U, U.T*g
    response = (b.T*b)[0]-(gr.T*(Pr+z*Qr).inv()*gr)[0]
    assert sp.cancel(response.subs(z, 0)) == 0
    assert sp.cancel(sp.diff(response, z).subs(z, 0)-ratio) == 0
    return {'unknowns': n, 'nullity': nu, 'pointed_norm': str(ratio),
            'all_Gram_coefficients_nonnegative': True,
            'same_period_is_the_exact_regularized_energy_derivative': True,
            'source_coefficient_ratio_equals_exact_projected_norm': True}


def symbolic_cases():
    # A free high jet is retained; the observed constant is unique.
    one = symbolic_gram(sp.Matrix([[1, 0, 0], [-2, 1, 0], [0, 0, 0]]),
                        sp.Matrix([1, 0, 0]), sp.Matrix([[1, 0, 0], [0, 1, 0]]))
    two = symbolic_gram(sp.Matrix([[1, 0, 0], [-2, 1, 0], [0, -2, 1]]),
                        sp.Matrix([1, 0, 0]), sp.eye(3))
    # Non-coordinate kernel and a non-diagonal projection exercise the
    # kernel-orthogonal proof, rather than a triangular special case.
    three = symbolic_gram(sp.Matrix([[1, 1, 0], [0, 0, 1], [2, 2, 1]]),
                          sp.Matrix([3, 2, 8]), sp.Matrix([[1, 1, 0], [0, 0, 1]]))
    a, c, x, N = sp.symbols('a c x N')
    for r in range(6):
        expression = sp.prod(a+c*N*x-j for j in range(r))/sp.factorial(r)
        assert sp.expand(expression).coeff(N, r) == (c*x)**r/sp.factorial(r)
    d0, d1, d2, d3 = sp.symbols('d0 d1 d2 d3')
    prolongation = sp.Matrix([[d0, 0, 0, 0], [d1, d0, 0, 0], [d2, d1, d0, 0], [d3, d2, d1, d0]])
    assert prolongation.det() == d0**4
    return [one, two, three]


def binomial_integer(e, r):
    if e >= 0:
        return comb(e, r) if r <= e else 0
    return (-1)**r*comb(r-e-1, r)


def monomial_jet(q, e, B, p):
    value = pow(q, e, p)
    return np.array([value*binomial_integer(e, r) % p for r in range(B+1)], dtype=np.int64)


def mul_jet(a, b, p):
    B = len(a)-1
    return np.array([sum(int(a[j])*int(b[r-j]) for j in range(r+1)) % p for r in range(B+1)], dtype=np.int64)


def calibration_color(j, q, B, p):
    term = np.zeros(B+1, dtype=np.int64); term[0] = 1
    total = term.copy()
    for r in range(1, j):
        factor = (monomial_jet(q, 2*j, B, p)+monomial_jet(q, -2*j, B, p)
                  -monomial_jet(q, 2*r, B, p)-monomial_jet(q, -2*r, B, p)) % p
        term = mul_jet(term, factor, p)
        total = (total+term) % p
    return total


def recurrence_matrix(terms, j0, N, B, q, p, colors):
    d = max(terms)
    block = B+1
    n = (N-j0+1)*block
    M = np.zeros((n, n), dtype=np.int64)
    b = np.zeros(n, dtype=np.int64)
    values = []
    for j in range(j0, N+1):
        jet = colors(j, q, B, p)
        values.extend(map(int, jet))
        if j < j0+d:
            start = (j-j0)*block
            M[start:start+block, start:start+block] = np.eye(block, dtype=np.int64)
            b[start:start+block] = jet
    for j in range(j0, N-d+1):
        row = (j+d-j0)*block
        for i, coeffs in terms.items():
            coeff = np.zeros(block, dtype=np.int64)
            for c, eM, eq in coeffs:
                coeff = (coeff+c*pow(-1, eM, p)*monomial_jet(q, eq+j*eM, B, p)) % p
            col = (j+i-j0)*block
            for r in range(block):
                for s in range(r+1):
                    M[row+r, col+s] = (M[row+r, col+s]+coeff[r-s]) % p
    values = np.array(values, dtype=np.int64)
    assert np.array_equal(M@values % p, b)
    observed = list(range(0, n, block))
    R = np.eye(n, dtype=np.int64)[observed]
    return M, b, R, values[observed]


def det_shift_coefficient(A, exponent, p):
    n = len(A)
    if exponent < 0 or exponent > n:
        return 0
    if n == 0:
        return int(exponent == 0)
    coefficients = nmod_mat(A.tolist(), p).charpoly()
    return pow(-1, n+exponent, p)*int(coefficients[exponent]) % p


def gram_ratio(M, b, Mstar, bstar, R, p):
    n = len(M)
    nu = n-rank(M, p)
    assert n-rank(Mstar, p) == nu
    assert rank(np.vstack((M, R)), p) == rank(M, p)
    P = Mstar.T@M % p
    if rank(P, p) != n-nu:
        raise FiniteFieldGramDegeneracy(p)
    g, h = Mstar.T@b % p, bstar@M % p
    bordered = np.zeros((n+1, n+1), dtype=np.int64)
    bordered[:n, :n] = P
    bordered[:n, n], bordered[n, :n] = g, h
    bordered[n, n] = int(bstar@b) % p
    denominator = det_shift_coefficient(P, nu, p)
    if not denominator:
        raise FiniteFieldGramDegeneracy(p)
    numerator = 0
    # Differentiate the z diagonal. The lambda identity excludes the last
    # bordered entry, so remove its spurious lambda term as well.
    observed = [int(np.flatnonzero(row)[0]) for row in R]
    for j in observed:
        rows = [i for i in range(n+1) if i != j]
        cols = [i for i in range(n) if i != j]
        numerator += det_shift_coefficient(bordered[np.ix_(rows, rows)], nu, p)
        numerator -= det_shift_coefficient(P[np.ix_(cols, cols)], nu-1, p)
    return numerator % p*pow(denominator, -1, p) % p, nu


def one_case_at_field(N, terms, B, colors, label, actual, p, q):
    M, b, R, f = recurrence_matrix(terms, 1, N, B, q, p, colors)
    # This second evaluation is the conjugate cyclotomic embedding. It is
    # not claimed to be a field automorphism of the prime field itself.
    Ms, bs, Rs, fs = recurrence_matrix(terms, 1, N, B, pow(q, -1, p), p, colors)
    assert np.array_equal(R, Rs)
    value, nu = gram_ratio(M, b, Ms, bs, R, p)
    assert value == int(fs@f) % p
    assert nu <= B
    scaling = np.array([pow(N, -(j % (B+1)), p) for j in range(len(M))], dtype=np.int64)
    inverse = np.array([pow(int(v), -1, p) for v in scaling], dtype=np.int64)
    scaled = scaling[:, None]*M % p*inverse[None, :] % p
    scaled_star = scaling[:, None]*Ms % p*inverse[None, :] % p
    alternate, alternate_nullity = gram_ratio(scaled, scaling*b % p, scaled_star, scaling*bs % p, R, p)
    assert (alternate, alternate_nullity) == (value, nu)
    original = False
    if actual:
        total = 0
        for j in range(1, N+1):
            # M=-q^j, so the actual x=-M/q is +q^(j-1).
            xp = pow(q, j-1, p)
            xm = pow(pow(q, -1, p), j-1, p)
            plus = reduced_period(N, p, *color_matrices(N, p, q, xp), WORDS[0])
            minus = reduced_period(N, p, *color_matrices(N, p, pow(q, -1, p), xm), WORDS[0])
            assert plus == int(f[j-1]) and minus == int(fs[j-1])
            total = (total+plus*minus) % p
        assert total == value
        original = True
    return {'level': N, 'model': label, 'jet_budget': B, 'unknowns': len(M),
            'nullity': nu, 'prime': p, 'positive_period_mod_prime': value,
            'Gram_coefficient_ratio_equals_all_root_color_norms': True,
            'rescaled_jet_lattice_has_exactly_the_same_pointed_period': True,
            'original_quantum_cut_all_colors_checked_at_this_level': original}


def one_case(N, terms, B, colors, label, actual=False):
    p, _, q = field(N)
    excluded = []
    for _ in range(20):
        try:
            result = one_case_at_field(N, terms, B, colors, label, actual, p, q)
            result['excluded_isotropic_reduction_primes'] = excluded
            return result
        except FiniteFieldGramDegeneracy:
            excluded.append(p)
            multiplier = p//(4*N)+1
            p = next(4*N*r+1 for r in range(multiplier, multiplier+1000) if sp.isprime(4*N*r+1))
            generator = int(sp.primitive_root(p))
            q = pow(generator, (p-1)//(2*N), p)
    raise AssertionError(('too many isotropic Gram reductions', N, excluded))


def missing_jet_test(N):
    p, _, q = field(N)
    # An actual unknot annihilator multiplied by a vanishing left factor.
    terms = {0: [(-1, 0, 0), (1, 2, 2)], 1: [(1, 0, 0), (-1, 2, 2)]}
    def colors(j, q, B, p):
        result = np.zeros(B+1, dtype=np.int64); result[0] = 1
        return result
    M0, _, R0, _ = recurrence_matrix(terms, 1, N, 0, q, p, colors)
    M1, _, R1, _ = recurrence_matrix(terms, 1, N, 1, q, p, colors)
    assert rank(np.vstack((M0, R0)), p) > rank(M0, p)
    assert rank(np.vstack((M1, R1)), p) == rank(M1, p)
    record = one_case(N, terms, 1, colors, 'actual_unknot_operator_with_singular_left_factor')
    assert record['positive_period_mod_prime'] == N % p
    record['zero_jet_system_rejected_and_first_jet_repairs_pointing'] = True
    return record


def main():
    symbolic = symbolic_cases()
    regular_terms = {0: [(-2, 0, 0)], 1: [(1, 0, 0)]}
    def exponential(j, q, B, p):
        return np.array([pow(2, j, p)]+[0]*B, dtype=np.int64)
    regular = [one_case(N, regular_terms, 0, exponential, 'constant_coefficient_growth_diagnostic')
               for N in range(4, 13)]
    singular = [missing_jet_test(N) for N in range(3, 13)]
    P, _, _ = operator_calibration()
    # Q=q^2, Y=M^2, with the original meridian q-step.
    calibration = {i: [(c, 2*eY, 2*eQ) for c, eY, eQ in row]
                   for i, row in coefficient_terms(P).items()}
    # Its factored leading coefficient gives exactly two root zeros,
    # counted with multiplicity, on j=1,...,N-3 for every N>=4.
    blocks = [one_case(N, calibration, 2, calibration_color,
                       'telescoping_polynomial_calibration', actual=N in (4, 5, 6))
              for N in range(4, 13)]
    result = {'scope': 'Uniform positive pointed Gram-period identity. The volume growth of the actual knot period remains unproved. Calibration is not an all-level knot-state proof.',
              'symbolic_positive_Gram_certificates': symbolic,
              'regular_growth_models': regular, 'singular_actual_unknot_models': singular,
              'telescoping_block_and_listed_original_cut_checks': blocks}
    path = Path(__file__).with_name('pointed_a_gram_period_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'results': str(path), 'symbolic_positive_Gram_cases': len(symbolic),
                      'regular_recurrence_cases': len(regular), 'singular_jet_repairs': len(singular),
                      'cyclotomic_calibration_cases': len(blocks),
                      'original_knot_root_color_levels': [r['level'] for r in blocks if r['original_quantum_cut_all_colors_checked_at_this_level']]}, indent=2))


if __name__ == '__main__':
    main()
