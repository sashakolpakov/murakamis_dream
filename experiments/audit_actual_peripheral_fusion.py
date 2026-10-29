#!/usr/bin/env python3
"""Independent finite-matrix checks of ADO peripheral fusion and its wall.

The coproduct, Casimir, heterogeneous double crossing, and cabled knot
are constructed from actual quantum-group matrices. Compare these with
the derived fusion formulas, including the nonsplit ideal-color limit.
This audit makes no regulator or asymptotic assertion.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field, scalar_data, cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices
from audit_cyclic_steinberg_lattice import rank
from audit_regularized_kashaev_period import actual_laurent_period, evaluate


def inverse_mod(matrix, prime):
    size = len(matrix)
    work = np.concatenate((matrix.copy() % prime,
                           np.eye(size, dtype=np.int64)), axis=1)
    for column in range(size):
        pivot = next(row for row in range(column, size) if work[row, column] % prime)
        work[[column, pivot]] = work[[pivot, column]]
        work[column] = work[column] * pow(int(work[column, column]), -1, prime) % prime
        for row in range(size):
            if row != column and work[row, column]:
                work[row] = (work[row] - work[row, column] * work[column]) % prime
    return work[:, size:]


def module(level, prime, q, x):
    e, _, _ = scalar_data(level, prime, q, x)
    E = np.zeros((level, level), dtype=np.int64)
    F = np.zeros_like(E)
    for j in range(1, level):
        E[j-1, j] = e[j]
        F[j, j-1] = 1
    K = np.diag([x * pow(q, -2*j, prime) % prime for j in range(level)])
    return E, F, K


def fundamental(prime, q):
    E = np.array([[0, 1], [0, 0]], dtype=np.int64)
    F = E.T.copy()
    K = np.diag([q, pow(q, -1, prime)]).astype(np.int64)
    return E, F, K


def tensor_module(left, right, prime):
    E, F, K = left
    e, f, k = right
    A, B = np.eye(len(E), dtype=np.int64), np.eye(len(e), dtype=np.int64)
    return ((np.kron(E, k) + np.kron(A, e)) % prime,
            (np.kron(F, B) + np.kron(inverse_mod(K, prime), f)) % prime,
            np.kron(K, k) % prime)


def casimir(data, prime, q):
    E, F, K = data
    rho = (q-pow(q, -1, prime)) % prime
    return (F @ E + (q*K + pow(q, -1, prime)*inverse_mod(K, prime))
            * pow(rho, -2, prime)) % prime


def left_trace_fundamental(matrix, level, prime, q):
    # Left closure of the first factor uses g_W^(-1), not g_W.
    weights = [-pow(q, -1, prime), -q]
    return sum(weights[a] * matrix[a*level:(a+1)*level,
                                   a*level:(a+1)*level] for a in range(2)) % prime


def partial_trace_right(matrix, pivotal, prime):
    size = len(pivotal)
    return np.einsum('abcb,b->ac', matrix.reshape((size,)*4),
                     np.diag(pivotal)) % prime


def fusion_case(level, kind):
    prime, generator, q = field(level)
    x = (pow(q, level-1, prime) if kind == 'ideal'
         else pow(generator, 2 if kind == 'generic1' else 6, prime))
    rho = (q-pow(q, -1, prime)) % prime
    bracket = lambda exponent: (x*pow(q, exponent, prime)
                                - pow(x, -1, prime)*pow(q, -exponent, prime)) \
                               * pow(rho, -1, prime) % prime
    delta = bracket(1)
    W, V = fundamental(prime, q), module(level, prime, q, x)
    U = tensor_module(W, V, prime)
    E, F, K = U
    size = 2*level
    eye = np.eye(size, dtype=np.int64)
    c_minus = (x + pow(x, -1, prime)) * pow(rho, -2, prime) % prime
    A = (casimir(U, prime, q)-c_minus*eye) % prime
    assert np.array_equal(A@A % prime, delta*A % prime)
    assert not np.any(np.linalg.matrix_power(E.astype(object), level) % prime)
    assert not np.any(np.linalg.matrix_power(F.astype(object), level) % prime)
    for G in U:
        assert not np.any((A@G-G@A) % prime)

    if kind == 'ideal':
        assert delta == 0
        assert rank(A, prime) == level-1
        assert not np.any(A@A % prime)
        assert np.array_equal(left_trace_fundamental(A, level, prime, q),
                              np.eye(level, dtype=np.int64))
        return {'level':level, 'color':kind, 'square_zero_rank':level-1,
                'nonzero_wall_extension_exact':True, 'left_trace_residue_is_identity':True}

    assert delta != 0, (level, kind, 'unexpected fusion wall')
    basis = np.zeros((size, size), dtype=np.int64)
    hp = np.zeros(size, dtype=np.int64)
    hm = hp.copy()
    hp[0] = 1
    hm[level] = bracket(0)
    hm[1] = -x % prime
    for j in range(level):
        basis[:, j] = hp
        basis[:, level+j] = hm
        hp, hm = F@hp % prime, F@hm % prime
    basis_inverse = inverse_mod(basis, prime)
    plus = module(level, prime, q, q*x % prime)
    minus = module(level, prime, q, pow(q, -1, prime)*x % prime)
    for index, G in enumerate(U):
        target = np.zeros_like(G)
        target[:level, :level] = plus[index]
        target[level:, level:] = minus[index]
        assert np.array_equal(G@basis % prime, basis@target % prime)
    Pplus = A * pow(delta, -1, prime) % prime
    diagonal = np.diag([1]*level+[0]*level).astype(np.int64)
    assert np.array_equal(Pplus, basis@diagonal@basis_inverse % prime)
    Pminus = (eye-Pplus) % prime
    lp = -bracket(2)*pow(delta, -1, prime) % prime
    lm = -bracket(0)*pow(delta, -1, prime) % prime
    assert np.array_equal(left_trace_fundamental(Pplus, level, prime, q),
                          lp*np.eye(level, dtype=np.int64) % prime)
    assert np.array_equal(left_trace_fundamental(Pminus, level, prime, q),
                          lm*np.eye(level, dtype=np.int64) % prime)
    M = -q*x % prime
    f = lambda point: (point-pow(point, -1, prime)) % prime
    assert lp == -f(q*M % prime)*pow(f(M), -1, prime) % prime
    assert lm == -f(pow(q, -1, prime)*M % prime)*pow(f(M), -1, prime) % prime

    # Full modified dimensions give exactly the same coefficients.
    def dimension(m):
        return f(m)*pow((pow(m, level, prime)-pow(m, -level, prime)) % prime,
                         -1, prime) % prime
    assert (pow(M, level, prime)-pow(M, -level, prime)) % prime != 0
    assert lp == dimension(q*M % prime)*pow(dimension(M), -1, prime) % prime
    assert lm == dimension(pow(q, -1, prime)*M % prime)*pow(dimension(M), -1, prime) % prime
    return {'level':level, 'color':kind, 'coproduct_intertwiner_exact':True,
            'Casimir_projectors_exact':True, 'both_partial_trace_weights_exact':True,
            'full_modified_dimension_ratios_exact':True}


def hopf_case(level, color):
    prime, generator, q = field(level)
    qhalf = pow(generator, (prime-1)//(4*level), prime)
    root_x = pow(qhalf, level-1, prime) if color == 'ideal' else generator
    x = root_x*root_x % prime
    E, F, _ = module(level, prime, q, x)
    e, f, _ = fundamental(prime, q)
    rho = (q-pow(q, -1, prime)) % prime
    eye = np.eye(2*level, dtype=np.int64)
    diagonal = np.diag([pow(root_x, 1-2*b, prime)*pow(q, -a*(1-2*b), prime) % prime
                        for a, b in product(range(level), range(2))])
    R = diagonal@(eye+rho*np.kron(E, f)) % prime
    R21 = diagonal@(eye+rho*np.kron(F, e)) % prime
    double = R21@R % prime
    value = np.zeros((level, level), dtype=np.int64)
    weights = [-q, -pow(q, -1, prime)]
    for b in range(2):
        value += weights[b]*double[b::2, b::2]
    M = -q*x % prime
    expected = (M+pow(M, -1, prime)) % prime
    assert np.array_equal(value % prime, expected*np.eye(level, dtype=np.int64) % prime)
    return {'level':level, 'color':color, 'heterogeneous_double_crossing_exact':True,
            'marked_meridian_action':'M+M^(-1)'}


def fundamental_skein_case(level):
    prime, generator, q = field(level)
    a = pow(generator, (prime-1)//(4*level), prime)
    assert a*a % prime == q
    # Invariant cup and cap are constructed independently of the crossing.
    cup = np.array([0, 1, -pow(q, -1, prime), 0], dtype=np.int64).reshape(4, 1) % prime
    cap = np.array([0, -q, 1, 0], dtype=np.int64).reshape(1, 4) % prime
    eye = np.eye(2, dtype=np.int64)
    assert np.array_equal(np.kron(eye, cap)@np.kron(cup, eye) % prime, eye)
    assert np.array_equal(np.kron(cap, eye)@np.kron(eye, cup) % prime, eye)
    W = fundamental(prime, q)
    WW = tensor_module(W, W, prime)
    assert not np.any(WW[0]@cup % prime)
    assert not np.any(WW[1]@cup % prime)
    assert np.array_equal(WW[2]@cup % prime, cup)
    contraction = cup@cap % prime
    delta = (-q-pow(q, -1, prime)) % prime
    assert int((cap@cup)[0, 0]) % prime == delta
    assert np.array_equal(contraction@contraction % prime, delta*contraction % prime)
    rho = (q-pow(q, -1, prime)) % prime
    diagonal = np.diag([a, pow(a, -1, prime), pow(a, -1, prime), a])
    raw_R = diagonal@(np.eye(4, dtype=np.int64)+rho*np.kron(W[0], W[1])) % prime
    swap = [0, 2, 1, 3]
    crossing = raw_R[swap, :]
    expected = (a*np.eye(4, dtype=np.int64)+pow(a, -1, prime)*contraction) % prime
    assert np.array_equal(crossing, expected)
    pivotal = np.diag([-q, -pow(q, -1, prime)]).astype(np.int64) % prime
    curl = partial_trace_right(crossing, pivotal, prime)
    assert np.array_equal(curl, -pow(a, 3, prime)*eye % prime)
    return {'level':level, 'actual_fundamental_Kauffman_relation_exact':True,
            'both_zigzags_and_loop_exact':True, 'twist':'-q^(3/2)'}


def actual_color_crossing(level, prime, q, data, x_top, heights):
    E, F, K = data
    size = len(E)
    rho = (q-pow(q, -1, prime)) % prime
    nilpotent = np.kron(E, F) % prime
    term = np.eye(size*size, dtype=np.int64)
    theta, theta_inverse = np.zeros_like(term), np.zeros_like(term)
    factorial = 1
    for j in range(level):
        if j:
            factorial = factorial*(pow(q, j, prime)-pow(q, -j, prime)) \
                         *pow(rho, -1, prime) % prime
        coefficient = pow(rho, j, prime)*pow(factorial, -1, prime) % prime
        theta = (theta+coefficient*pow(q, j*(j-1)//2, prime)*term) % prime
        theta_inverse = (theta_inverse+coefficient*pow(-1, j, prime)
                         *pow(q, -j*(j-1)//2, prime)*term) % prime
        term = term@nilpotent % prime
    assert not np.any(term)
    eye = np.eye(size*size, dtype=np.int64)
    assert np.array_equal(theta@theta_inverse % prime, eye)
    diagonal = [pow(x_top, -a-b, prime)*pow(q, 2*a*b, prime) % prime
                for a, b in product(heights, repeat=2)]
    raw = np.array(diagonal, dtype=np.int64)[:, None]*theta % prime
    swap = [b*size+a for a, b in product(range(size), repeat=2)]
    crossing = raw[swap, :]
    pivotal = np.diag([pow(int(K[a, a]), 1-level, prime)
                       for a in range(size)]).astype(np.int64)
    curl = partial_trace_right(crossing, pivotal, prime)
    return crossing, pivotal, curl


def raw_mixed_R(level, prime, q, left, x_left, h_left,
                right, x_right, h_right):
    """Actual unflipped R, removing only its common Cartan scalar."""
    rho = (q-pow(q, -1, prime)) % prime
    nilpotent = np.kron(left[0], right[1]) % prime
    size = len(nilpotent)
    term = np.eye(size, dtype=np.int64)
    theta = np.zeros_like(term)
    factorial = 1
    for j in range(level):
        if j:
            factorial = factorial*(pow(q, j, prime)-pow(q, -j, prime)) \
                         *pow(rho, -1, prime) % prime
        coefficient = pow(q, j*(j-1)//2, prime)*pow(rho, j, prime) \
                      *pow(factorial, -1, prime) % prime
        theta = (theta+coefficient*term) % prime
        term = term@nilpotent % prime
    assert not np.any(term)
    diagonal = [pow(x_left, -b, prime)*pow(x_right, -a, prime)*pow(q, 2*a*b, prime) % prime
                for a, b in product(h_left, h_right)]
    return np.array(diagonal, dtype=np.int64)[:, None]*theta % prime


def tensor_crossing_case(level):
    prime, generator, q = field(level)
    x = pow(generator, 2, prime)
    W, V = fundamental(prime, q), module(level, prime, q, x)
    U = tensor_module(W, V, prime)
    hW, hV = [0, 1], list(range(level))
    hU = [b+j for b, j in product(range(2), range(level))]
    R = lambda L, xL, hL, R, xR, hR: raw_mixed_R(
        level, prime, q, L, xL, hL, R, xR, hR)
    RVV = R(V, x, hV, V, x, hV)
    RWV = R(W, q, hW, V, x, hV)
    RVW = R(V, x, hV, W, q, hW)
    RUV = R(U, q*x % prime, hU, V, x, hV)
    RVU = R(V, x, hV, U, q*x % prime, hU)
    eyeV, eyeW = np.eye(level, dtype=np.int64), np.eye(2, dtype=np.int64)
    permutation = [(b*level+k)*level+j
                   for b, j, k in product(range(2), range(level), range(level))]
    R13 = np.kron(RWV, eyeV)[np.ix_(permutation, permutation)]
    R23 = np.kron(eyeW, RVV)
    assert np.array_equal(RUV, R13@R23 % prime)
    permutation = [(i*level+k)*2+b
                   for i, b, k in product(range(level), range(2), range(level))]
    R13 = np.kron(RVV, eyeW)[np.ix_(permutation, permutation)]
    R12 = np.kron(RVW, eyeV)
    assert np.array_equal(RVU, R13@R12 % prime)
    return {'level':level, 'actual_tensor_color_equals_parallel_crossings_both_sides':True,
            'common_Cartan_scalar_matches_exactly':True}


def cabled_case(level, kind, writhe):
    prime, generator, q = field(level)
    x = pow(q, level-1, prime) if kind == 'ideal' else pow(generator, 2, prime)
    U = tensor_module(fundamental(prime, q), module(level, prime, q, x), prime)
    crossing, pivotal, curl = actual_color_crossing(
        level, prime, q, U, q*x % prime,
        [j+b for b, j in product(range(2), range(level))])
    power = lambda matrix, exponent: matrix_power(matrix, exponent, prime)
    cut = partial_trace_right(power(crossing, writhe), pivotal, prime)
    cut = cut@power(curl, -writhe) % prime
    rho = (q-pow(q, -1, prime)) % prime
    delta = (q*x-pow(q*x, -1, prime))*pow(rho, -1, prime) % prime
    c_minus = (x+pow(x, -1, prime))*pow(rho, -2, prime) % prime
    eye = np.eye(2*level, dtype=np.int64)
    A = (casimir(U, prime, q)-c_minus*eye) % prime
    word = [(0, 1 if writhe > 0 else -1)]*abs(writhe)
    if kind == 'ideal':
        F = actual_laurent_period(level, prime, q, 2, word)
        Q = q*q % prime
        assert evaluate(F, Q, prime) == 1
        tau = -2*rho*Q*evaluate(F, Q, prime, derivative=True) % prime
        expected = (eye+tau*A) % prime
        assert np.array_equal(cut, expected)
        satellite = left_trace_fundamental(cut, level, prime, q)
        assert np.array_equal(satellite, (tau-q-pow(q, -1, prime))
                              *np.eye(level, dtype=np.int64) % prime)
        return {'level':level, 'color':kind, 'two_strand_writhe':writhe,
                'actual_cabled_knot_nilpotent_coefficient_exact':True,
                'wall_satellite_derivative_exact':True}

    Pplus = A*pow(delta, -1, prime) % prime
    Pminus = (eye-Pplus) % prime
    values = []
    for shift in (1, -1):
        shifted = color_matrices(level, prime, q, pow(q, shift, prime)*x % prime)
        ordinary_cut = cut_matrix_dense(level, prime, shifted, 2, word)
        values.append(int(ordinary_cut[0, 0]))
    assert np.array_equal(cut, (values[0]*Pplus+values[1]*Pminus) % prime)
    return {'level':level, 'color':kind, 'two_strand_writhe':writhe,
            'actual_cabled_knot_fusion_exact':True}


def matrix_power(matrix, exponent, prime):
    if exponent < 0:
        matrix, exponent = inverse_mod(matrix, prime), -exponent
    result = np.eye(len(matrix), dtype=np.int64)
    while exponent:
        if exponent % 2:
            result = result@matrix % prime
        matrix = matrix@matrix % prime
        exponent //= 2
    return result


def generic_identities():
    q, x, M = sp.symbols('q x M', nonzero=True)
    rho = q-1/q
    bracket = lambda r: (x*q**r-x**(-1)*q**(-r))/rho
    f = lambda m: m-1/m
    checks = []
    for j in range(1, 9):
        integer = (q**j-q**(-j))/rho
        assert sp.cancel(q**(-j)*bracket(1-j)+x*q**(1-j)*integer-bracket(1)) == 0
    for direction in (1, -1):
        weight = (-bracket(direction+1)/bracket(1)).subs(x, -M/q)
        assert sp.cancel(weight+f(q**direction*M)/f(M)) == 0
    # Gauge of the normal v=(M^2-1)F versus the odd w=f(M)F.
    for direction in (1, -1):
        assert sp.cancel(-(q**(2*direction)*M**2-1)*q**(-direction)
                         /(M**2-1)+f(q**direction*M)/f(M)) == 0
    checks.append({'generic_projector_weight_and_both_shift_gauges_exact':True})
    return checks


def main():
    levels = (2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18, 20, 24)
    local = [fusion_case(n, kind) for n in levels
             for kind in ('generic1', 'generic2', 'ideal')]
    print(f'local coproduct, projectors, and wall: {len(local)} cases passed', flush=True)
    hopf = [hopf_case(n, kind) for n in levels for kind in ('generic', 'ideal')]
    print(f'actual heterogeneous Hopf: {len(hopf)} cases passed', flush=True)
    skein = [fundamental_skein_case(n) for n in levels]
    print(f'actual fundamental skein and duality: {len(skein)} cases passed', flush=True)
    parallel = [tensor_crossing_case(n) for n in (2, 3, 4, 5, 6, 8)]
    print(f'actual tensor color versus parallel crossings: {len(parallel)} cases passed', flush=True)
    cables = [cabled_case(n, kind, writhe) for n in (2, 3, 4, 5)
              for kind in ('generic', 'ideal') for writhe in (3, -5)]
    print(f'actual cabled knots, including ideal wall: {len(cables)} cases passed', flush=True)
    result = {'scope':'Finite algebraic diagnostics for the uniform peripheral-fusion proof; no asymptotic assertion.',
              'generic_identities':generic_identities(), 'local_fusion':local,
              'actual_meridian_encircling':hopf, 'fundamental_skein':skein,
              'tensor_color_parallel_crossings':parallel, 'actual_cabled_knots':cables}
    Path(__file__).with_name('actual_peripheral_fusion_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS', flush=True)


if __name__ == '__main__':
    main()
