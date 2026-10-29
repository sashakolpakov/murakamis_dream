#!/usr/bin/env python3
"""Exact checks of the ramified Weyl lattice and its pointed fibre.

Actual cut polynomials test the period functional independently of any
rank hypothesis. The operator tests use the separately certified finite
cyclotomic block; its equality to the actual cut is checked only at the
explicitly indicated levels. No asymptotic assertion is made.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_regularized_kashaev_period import (actual_laurent_period,
                                             multiply_poly, evaluate)
from audit_peripheral_normal_period import (operator_calibration,
    coefficient_terms, cyclotomic_block, matrix_and_derivative)
from audit_actual_peripheral_fusion import inverse_mod
from audit_cyclic_steinberg_lattice import rank


def u_power(exponent, order, prime):
    """Series of ((1+z)/(1-z))^exponent, with the exponent in F_p."""
    result = [1]
    for n in range(1, order+1):
        result.append(2*exponent*sum(result[n-1-j] for j in range(0, n, 2))
                      *pow(n, -1, prime) % prime)
    return result


def reflection(level, prime, q, degree=0, m=1, sign=-1):
    Q = q*q % prime
    result = np.zeros((level, level), dtype=np.int64)
    for r in range(level):
        result[r, (-r-degree) % level] = sign*pow(q, degree*m, prime)*pow(Q, r*m, prime) % prime
    assert np.array_equal(result@result % prime, np.eye(level, dtype=np.int64))
    return result


def eigenframe(J, prime):
    plus, minus, visited = [], [], set()
    size = len(J)
    for r in range(size):
        if r in visited:
            continue
        s = next(j for j in range(size) if J[r, j])
        visited.update((r, s))
        if r == s:
            vector = np.eye(size, dtype=np.int64)[:, r]
            (plus if J[r, r] == 1 else minus).append(vector)
        else:
            for sign, target in ((1, plus), (-1, minus)):
                vector = np.zeros(size, dtype=np.int64)
                vector[r] = 1
                vector[s] = sign*J[s, r] % prime
                target.append(vector)
    frame = np.column_stack(plus+minus)
    inverse = inverse_mod(frame, prime)
    diagonal = np.diag([1]*len(plus)+[-1]*len(minus)) % prime
    assert np.array_equal(inverse@J@frame % prime, diagonal)
    return frame, inverse, len(plus)


def state_series(polynomial, level, prime, q, order):
    Q = q*q % prime
    # v=(Y-1)F, then x=U^(-1/(2N))*v, U=Y^N.
    normal = multiply_poly(polynomial, {1:1, 0:-1}, prime)
    coefficients = [np.zeros(level, dtype=np.int64) for _ in range(order+1)]
    for exponent, coefficient in normal.items():
        series = u_power((2*exponent-1)*pow(2*level, -1, prime) % prime,
                         order, prime)
        for r in range(level):
            value = coefficient*pow(Q, r*exponent, prime) % prime
            for k in range(order+1):
                coefficients[k][r] = (coefficients[k][r]+series[k]*value) % prime
    return coefficients


def transformed_operator_series(terms, level, prime, q, m, order):
    Q = q*q % prime
    result = [np.zeros((level, level), dtype=np.int64) for _ in range(order+1)]
    for j, coefficients in terms.items():
        for coefficient, eY, eQ in coefficients:
            exponent = (2*eY+1-m)*pow(2*level, -1, prime) % prime
            series = u_power(exponent, order, prime)
            for r in range(level):
                value = coefficient*pow(Q, eQ+r*eY, prime) % prime
                for k in range(order+1):
                    result[k][r, (r+j) % level] = (
                        result[k][r, (r+j) % level]+series[k]*value) % prime
    return result


def actual_state_case(level, strands, word):
    prime, _, q = field(level)
    Q = q*q % prime
    F = actual_laurent_period(level, prime, q, strands, word)
    coefficients = state_series(F, level, prime, q, 5)
    J = reflection(level, prime, q)
    for k, vector in enumerate(coefficients):
        assert np.array_equal(J@vector % prime, pow(-1, k, prime)*vector % prime)
    K = evaluate(F, 1, prime)
    assert int(coefficients[0][0]) == 0
    assert level*int(coefficients[1][0])*pow(2, -1, prime) % prime == K
    assert int(coefficients[0][1])*pow(Q-1, -1, prime) % prime == 1
    frame, inverse, nplus = eigenframe(J, prime)
    a0 = (inverse@coefficients[0] % prime)[:nplus]
    b0 = (inverse@coefficients[1] % prime)[nplus:]
    assert np.array_equal(frame[:, :nplus]@a0 % prime, coefficients[0])
    assert np.array_equal(frame[:, nplus:]@b0 % prime, coefficients[1])
    return {'level':level, 'strands':strands, 'crossings':len(word),
            'actual_Weyl_series_through_order_5_exact':True,
            'coarse_fibre_recovers_Kashaev_value_exact':True,
            'ordinary_anchor_is_one':True,
            'plus_dimension':nplus, 'minus_dimension':level-nplus}


def operator_case(level, terms, actual_compared=False):
    prime, _, q = field(level)
    Q = q*q % prime
    F = cyclotomic_block(level, prime, Q)
    if actual_compared:
        assert F == actual_laurent_period(level, prime, q, 3, [(0,1),(1,-1)]*2)
    B = transformed_operator_series(terms, level, prime, q, 8, 5)
    x = state_series(F, level, prime, q, 5)
    J, Jp = reflection(level, prime, q), reflection(level, prime, q, 3, 8, -1)
    C, Ci, np_in = eigenframe(J, prime)
    D, Di, np_out = eigenframe(Jp, prime)
    folded = [Di@matrix@C % prime for matrix in B]
    for k, matrix in enumerate(B):
        assert np.array_equal(matrix@J % prime, pow(-1,k,prime)*Jp@matrix % prime)
        allowed = folded[k].copy()
        if k % 2:
            assert not np.any(allowed[:np_out, :np_in])
            assert not np.any(allowed[np_out:, np_in:])
        else:
            assert not np.any(allowed[:np_out, np_in:])
            assert not np.any(allowed[np_out:, :np_in])
        assert not np.any(sum(B[i]@x[k-i] for i in range(k+1)) % prime)
    coarse = []
    for k in range(3):
        matrix = np.zeros((level, level), dtype=np.int64)
        matrix[:np_out, :np_in] = folded[2*k][:np_out, :np_in]
        if k:
            matrix[:np_out, np_in:] = folded[2*k-1][:np_out, np_in:]
        matrix[np_out:, :np_in] = folded[2*k+1][np_out:, :np_in]
        matrix[np_out:, np_in:] = folded[2*k][np_out:, np_in:]
        coarse.append(matrix)
    state = [np.concatenate(((Ci@x[2*k] % prime)[:np_in],
                             (Ci@x[2*k+1] % prime)[np_in:])) for k in range(3)]
    for k in range(3):
        assert not np.any(sum(coarse[i]@state[k-i] for i in range(k+1)) % prime)
    assert rank(coarse[0], prime) == level-1
    B0, B1 = matrix_and_derivative(terms, level, prime, Q)
    expected_first = (2*B1+(1-8)*pow(level, -1, prime)*B0) % prime
    assert np.array_equal(B[1], expected_first)
    a0, b0 = C[:, :np_in]@state[0][:np_in] % prime, C[:, np_in:]@state[0][np_in:] % prime
    assert not np.any((B0@b0+B[1]@a0) % prime)
    assert level*int(b0[0])*pow(2, -1, prime) % prime == evaluate(F, 1, prime)
    return {'level':level, 'actual_cut_polynomial_compared':actual_compared,
            'operator_reciprocity_through_order_5_exact':True,
            'coarse_kernel_equation_through_order_2_exact':True,
            'coarse_special_rank':level-1,
            'coarse_period_equals_previous_normal_pairing':True}


def elementary_descent_checks():
    z, s, c = sp.symbols('z s c')
    J = sp.diag(1,-1)
    embedding = sp.diag(1,z)
    B = sp.Matrix([[0,0],[z,1]])
    descended = sp.simplify(embedding.inv()*B*embedding)
    assert descended == sp.Matrix([[0,0],[1,1]])
    assert B*sp.Matrix([1,-z]) == sp.zeros(2,1)
    assert descended*sp.Matrix([1,-1]) == sp.zeros(2,1)
    G = sp.Matrix([[1,0],[c*z,1]])
    assert G.subs(z,0) == sp.eye(2)
    assert G*J == J*G.subs(z,-z)
    Gdesc = sp.simplify(embedding.inv()*G*embedding)
    assert Gdesc == sp.Matrix([[1,0],[c,1]])
    assert Gdesc*sp.Matrix([1,-1]) == sp.Matrix([1,c-1])
    # General equivariant morphisms descend functorially, with a preserved
    # negative-weight filtration and a top-right entry divisible by s.
    a,b,d,e,f,g,h,i = sp.symbols('a b d e f g h i')
    G1 = sp.Matrix([[a,z*b],[z*d,e]])
    G2 = sp.Matrix([[f,z*g],[z*h,i]])
    descend = lambda matrix: sp.simplify(embedding.inv()*matrix*embedding).subs(z**2,s)
    assert sp.simplify(descend(G1*G2)-descend(G1)*descend(G2)) == sp.zeros(2)
    return {'specialization_before_descent_discards_normal_coordinate':True,
            'equivariant_gauge_identity_on_naive_fibre_can_change_period':True,
            'coarse_morphism_descent_is_functorial':True}


def parity_dimension_checks():
    records = []
    for level in (2,3,4,5,6,8,10,15,16,18,20):
        prime, _, q = field(level)
        _, _, nplus = eigenframe(reflection(level,prime,q), prime)
        assert level-nplus == (level+1)//2
        for degree in range(1,5):
            for m in range(-2,4):
                for sign in (-1,1):
                    Jp = reflection(level,prime,q,degree,m,sign)
                    _, _, nplus_out = eigenframe(Jp,prime)
                    predicted_trace = sum(sign*(1 if m*((degree+2*r)//level)%2==0 else -1)
                        for r in range(level) if (degree+2*r) % level == 0)
                    assert 2*nplus_out-level == predicted_trace
                    dimension_obstruction = nplus_out > nplus
                    if level % 2 == 0:
                        assert dimension_obstruction == (degree%2==0 and m%2==0 and sign==1)
                    elif level > degree:
                        value = sign*(-1 if degree%2 and m%2 else 1)
                        assert dimension_obstruction == (value == 1)
                    records.append({'level':level,'degree':degree,'m':m,'sign':sign,
                                    'range_trace':predicted_trace,
                                    'sector_injectivity_forbidden_by_dimension':dimension_obstruction})
    return records


def main():
    diagrams = [(2,[(0,1)]*3), (3,[(0,1),(1,-1)]*2),
                (3,[(0,1)]*3+[(1,1)])]
    states = [actual_state_case(n,b,w) for n in (2,3,4,5,6,7) for b,w in diagrams]
    print(f'actual knot-state ramified fibres: {len(states)} cases passed', flush=True)
    _, B, _ = operator_calibration()
    terms = coefficient_terms(B)
    operators = [operator_case(n,terms,n<=8) for n in (2,3,4,5,6,7,8,10,12,15,18)]
    print(f'certified operator/coarse-fibre calibration: {len(operators)} cases passed', flush=True)
    parity = parity_dimension_checks()
    print(f'half-root and parity-dimension signatures: {len(parity)} cases passed', flush=True)
    result = {'scope':'Exact ramified-descent diagnostics; no operator rank or volume theorem is inferred beyond the stated calibration.',
              'actual_knot_states':states, 'certified_operator_calibration':operators,
              'parity_dimension_signatures':parity,
              'elementary_descent':elementary_descent_checks()}
    Path(__file__).with_name('ramified_weyl_fibre_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS', flush=True)


if __name__ == '__main__':
    main()
