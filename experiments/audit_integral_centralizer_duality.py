#!/usr/bin/env python3
"""PBW Frobenius form, projective complete color, and full cut duality.

The special-fiber centralizer is solved directly from E,F,K; no
generic fusion frames are specialized. All scalars are the original
ADO pivot, dimension, and crossing normalization.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np

from audit_actual_peripheral_fusion import inverse_mod, module, tensor_module
from audit_cyclic_steinberg_lattice import determinant, rank
from audit_finite_sum_annihilator import field
from audit_intrinsic_cut_transport import modified_dimension
from audit_kashaev_ado_pointing import color_matrices
from audit_regular_holonomy_braiding import mm


class NilpotentAlgebra:
    def __init__(self, N, p, q, k):
        self.N, self.p, self.q, self.k = N, p, q, k
        self.Q = q*q % p
        self.rho = (q-pow(q, -1, p)) % p
        self.basis = tuple(product(range(N), repeat=3))
        self.index = {v:i for i,v in enumerate(self.basis)}
        self.one = {(0, 0, 0):1}
        self.F = {(1, 0, 0):1}
        self.E = {(0, 0, 1):1}
        self.K = {(0, 1, 0):1}
        self.Ki = {(0, N-1, 0):pow(k, -1, p)}
        self.expansions = {}

    def add(self, *terms):
        out = {}
        for coefficient, term in terms:
            for monomial, value in term.items():
                out[monomial] = (out.get(monomial, 0)+coefficient*value) % self.p
        return {m:v for m,v in out.items() if v}

    def left_E(self, term):
        out = {}
        N, p, q, Q = self.N, self.p, self.q, self.Q
        def add(a, b, c, value):
            carry, residue = divmod(b, N)
            monomial = (a, residue, c)
            out[monomial] = (out.get(monomial, 0)+value*pow(self.k, carry, p)) % p
        for (a, b, c), value in term.items():
            if c+1 < N:
                add(a, b, c+1, value*pow(Q, -b, p))
            if a:
                coefficient = ((pow(q, a, p)-pow(q, -a, p))
                               *pow(self.rho, -2, p)) % p
                add(a-1, b+1, c, value*coefficient*pow(q, 1-a, p))
                add(a-1, b-1, c, -value*coefficient*pow(q, a-1, p))
        return {m:v for m,v in out.items() if v}

    def E_expansion(self, exponent, monomial):
        key = exponent, monomial
        if key not in self.expansions:
            value = {monomial:1}
            for _ in range(exponent):
                value = self.left_E(value)
            self.expansions[key] = value
        return self.expansions[key]

    def monomial_product(self, left, right):
        a, b, c = left
        out = {}
        for (d, e, f), value in self.E_expansion(c, right).items():
            if a+d >= self.N:
                continue
            carry, residue = divmod(b+e, self.N)
            monomial = a+d, residue, f
            value = value*pow(self.Q, -b*d, self.p)*pow(self.k, carry, self.p)
            out[monomial] = (out.get(monomial, 0)+value) % self.p
        return {m:v for m,v in out.items() if v}

    def mul(self, left, right):
        out = {}
        for a, va in left.items():
            for b, vb in right.items():
                for monomial, value in self.monomial_product(a, b).items():
                    out[monomial] = (out.get(monomial, 0)+va*vb*value) % self.p
        return {m:v for m,v in out.items() if v}

    def mu(self, value):
        return value.get((self.N-1, 0, self.N-1), 0)

    def mu_product(self, left, right):
        a, b, c = left
        total = 0
        for (d, e, f), value in self.E_expansion(c, right).items():
            if a+d != self.N-1 or f != self.N-1:
                continue
            carry, residue = divmod(b+e, self.N)
            if not residue:
                total += value*pow(self.Q, -b*d, self.p)*pow(self.k, carry, self.p)
        return total % self.p

    def omega(self):
        return self.add((self.rho*self.rho, self.mul(self.F, self.E)),
                        (self.q, self.K), (pow(self.q, -1, self.p), self.Ki))

    def polynomial(self, coefficients, value):
        out = {}
        for coefficient in reversed(coefficients):
            out = self.add((1, self.mul(value, out)), (coefficient, self.one))
        return out

    def vector(self, value):
        out = np.zeros(len(self.basis), dtype=np.int64)
        for monomial, coefficient in value.items():
            out[self.index[monomial]] = coefficient
        return out

    def regular(self, value):
        return np.column_stack([self.vector(self.mul(value, {m:1})) for m in self.basis])


def chebyshev_coefficients(N, p):
    a, b = [2], [0, 1]
    for _ in range(1, N):
        c = [0]+b
        for j, v in enumerate(a):
            c[j] = (c[j]-v) % p
        a, b = b, c
    return b


def divide_linear(coefficients, root, p):
    quotient = [0]*(len(coefficients)-1)
    quotient[-1] = coefficients[-1]
    for j in range(len(quotient)-1, 0, -1):
        quotient[j-1] = (coefficients[j]+root*quotient[j]) % p
    assert (coefficients[0]+root*quotient[0]) % p == 0
    return quotient


def weight_projector(H, x):
    return {(0, b, 0):pow(H.N, -1, H.p)*pow(x, -b, H.p) % H.p
            for b in range(H.N)}


def pbw_case(N, kind):
    p, generator, q = field(N)
    k = pow(generator, N, p) if kind == 'generic' else (1 if kind == 'plus' else p-1)
    H = NilpotentAlgebra(N, p, q, k)
    for monomial in H.basis:
        h = {monomial:1}
        KE, EK = H.mul(H.K, H.mul(H.E, h)), H.mul(H.E, H.mul(H.K, h))
        KF, FK = H.mul(H.K, H.mul(H.F, h)), H.mul(H.F, H.mul(H.K, h))
        assert KE == H.add((H.Q, EK))
        assert KF == H.add((pow(H.Q, -1, p), FK))
        commutator = H.add((1, H.mul(H.E, H.mul(H.F, h))),
                           (-1, H.mul(H.F, H.mul(H.E, h))))
        assert commutator == H.add((pow(H.rho, -1, p), H.mul(H.K, h)),
                                   (-pow(H.rho, -1, p), H.mul(H.Ki, h)))
        assert not H.E_expansion(N, monomial)
    gram = np.array([[H.mu_product(a, b) for b in H.basis] for a in H.basis], dtype=np.int64)
    assert np.array_equal(gram, gram.T)
    det = determinant(gram, p)
    assert det
    polynomial = chebyshev_coefficients(N, p)
    polynomial[0] = (polynomial[0]+k+pow(k, -1, p)) % p
    assert not H.polynomial(polynomial, H.omega())
    return {'level':N, 'prime':p, 'central_character':kind, 'PBW_rank':N**3,
            'all_left_regular_generator_relations_exact':True,
            'PBW_trace_is_symmetric':True, 'PBW_trace_Gram_determinant':det,
            'nilpotent_Casimir_polynomial_exact':True}


def projective_color_case(N):
    p, _, q = field(N)
    x = pow(q, N-1, p)
    k = pow(x, N, p)
    H = NilpotentAlgebra(N, p, q, k)
    polynomial = chebyshev_coefficients(N, p)
    polynomial[0] = (polynomial[0]+k+pow(k, -1, p)) % p
    quotient = divide_linear(polynomial, -2 % p, p)
    derivative = sum(j*c*pow(-2, j-1, p) for j,c in enumerate(polynomial) if j) % p
    assert derivative
    central = H.polynomial([v*pow(derivative, -1, p) % p for v in quotient], H.omega())
    e = H.mul(central, weight_projector(H, x))
    assert H.mul(e, e) == e and e
    assert not H.mul(H.E, e)
    columns = []
    v = e
    for _ in range(N):
        columns.append(H.vector(v))
        v = H.mul(H.F, v)
    assert not v
    inclusion = np.column_stack(columns)
    assert rank(inclusion, p) == N
    for operator, small in zip((H.E, H.F, H.K), module(N, p, q, x)):
        assert np.array_equal(mm(p, H.regular(operator), inclusion), mm(p, inclusion, small))
    full_ideal = np.column_stack([H.vector(H.mul({a:1}, e)) for a in H.basis])
    assert rank(full_ideal, p) == N
    gamma = N*N*pow(q, N*(1-N)//2, p)*pow(H.rho, -2*N+2, p) % p
    eta = pow(-1, N+1, p)*pow(q, N*(1-N)//2, p) % p
    assert gamma*H.mu(e) % p == eta*pow(N, -1, p) % p
    return {'level':N, 'prime':p, 'regular_primitive_idempotent_exact':True,
            'left_ideal_rank_and_actual_color_dimension':N,
            'all_color_E_F_K_intertwinings_exact':True,
            'PBW_to_ADO_trace_scale_gamma':gamma,
            'complete_ADO_trace_of_primitive_idempotent':gamma*H.mu(e) % p}


def spectral_calibration_case(N):
    p, x, q = field(N)
    H = NilpotentAlgebra(N, p, q, pow(x, N, p))
    O, pi = H.omega(), weight_projector(H, x)
    polynomial = chebyshev_coefficients(N, p)
    polynomial[0] = (polynomial[0]+H.k+pow(H.k, -1, p)) % p
    gamma = N*N*pow(q, N*(1-N)//2, p)*pow(H.rho, -2*N+2, p) % p
    records = []
    for j in range(N):
        z = x*pow(H.Q, -j, p) % p
        c = (q*z+pow(q*z, -1, p)) % p
        quotient = divide_linear(polynomial, c, p)
        derivative = sum(a*v*pow(c, a-1, p) for a,v in enumerate(polynomial) if a) % p
        ej = H.polynomial([v*pow(derivative, -1, p) % p for v in quotient], O)
        actual = gamma*H.mu(H.mul(pi, ej)) % p
        expected = modified_dimension(N, p, q, z)
        assert actual == expected
        records.append(actual)
    return {'level':N, 'prime':p, 'all_primitive_trace_weights_are_actual_ADO_dimensions':records}


def free_tensor_case(N, second_color):
    p, _, q = field(N)
    x = pow(q, N-1, p)
    y = x if second_color == 'complete' else p-1
    k, l = pow(x, N, p), pow(y, N, p)
    H, total_H = NilpotentAlgebra(N, p, q, k), NilpotentAlgebra(N, p, q, k*l % p)
    regular = tuple(H.regular(a) for a in (H.E, H.F, H.K))
    target = tensor_module(regular, module(N, p, q, y), p)
    size = N**4
    seed = np.zeros((size, N), dtype=np.int64)
    for a in range(N):
        seed[a, a] = 1
    blocks = []
    for a, b, c in H.basis:
        value = seed.copy()
        for _ in range(c):value = mm(p, target[0], value)
        for _ in range(b):value = mm(p, target[2], value)
        for _ in range(a):value = mm(p, target[1], value)
        blocks.append(value)
    Phi = np.column_stack(blocks)
    assert rank(Phi, p) == size
    for op, target_op in zip((total_H.E, total_H.F, total_H.K), target):
        domain_op = np.kron(total_H.regular(op), np.eye(N, dtype=np.int64))
        assert np.array_equal(mm(p, Phi, domain_op), mm(p, target_op, Phi))
    return {'level':N, 'prime':p, 'second_color':second_color, 'free_tensor_dimension':size,
            'Hopf_free_tensor_map_is_invertible_and_intertwines_E_F_K':True}


def nullspace(matrix, p):
    work = matrix.copy() % p
    pivots = []
    row = 0
    for column in range(work.shape[1]):
        possible = np.flatnonzero(work[row:, column])
        if not len(possible):continue
        pivot = row+int(possible[0])
        work[[row, pivot]] = work[[pivot, row]]
        work[row, column:] = work[row, column:]*pow(int(work[row, column]), -1, p) % p
        targets = np.flatnonzero(work[row+1:, column])+row+1
        if len(targets):
            work[targets, column:] = (work[targets, column:]
                -work[targets, column, None]*work[row, column:]) % p
        pivots.append(column)
        row += 1
        if row == len(work):break
    free = [j for j in range(work.shape[1]) if j not in set(pivots)]
    result = np.zeros((work.shape[1], len(free)), dtype=np.int64)
    result[free, np.arange(len(free))] = 1
    for r, c in reversed(list(enumerate(pivots))):
        result[c] = -mm(p, work[r:r+1, c+1:], result[c+1:])[0] % p
    assert not np.any(mm(p, matrix, result))
    return result


def complete_centralizer_case(N, strands):
    p, _, q = field(N)
    x = pow(q, N-1, p)
    data = module(N, p, q, x)
    for _ in range(strands-1):data = tensor_module(data, module(N, p, q, x), p)
    E, F, K = data
    size, Q = len(E), q*q % p
    weights = np.diag(K)
    positions = [(a,b) for a,b in product(range(size), repeat=2) if weights[a] == weights[b]]
    pos_index = {v:i for i,v in enumerate(positions)}
    variables = len(positions)
    constraints = np.zeros((2*variables, variables), dtype=np.int64)
    for op_index, (G, ratio) in enumerate(((E,Q),(F,pow(Q,-1,p)))):
        allowed = [(a,b) for a,b in product(range(size),repeat=2)
                   if weights[a] == ratio*weights[b] % p]
        rows = {v:i+op_index*variables for i,v in enumerate(allowed)}
        assert len(allowed) == variables
        row_terms = [np.flatnonzero(G[a]) for a in range(size)]
        col_terms = [np.flatnonzero(G[:,a]) for a in range(size)]
        for column, (a,b) in enumerate(positions):
            for c in row_terms[b]:constraints[rows[a,int(c)],column] += int(G[b,c])
            for c in col_terms[a]:constraints[rows[int(c),b],column] -= int(G[c,a])
    constraints %= p
    basis = nullspace(constraints, p)
    expected = N**(2*strands-3)
    assert basis.shape[1] == expected
    density = np.array([1]+[0]*(N-1), dtype=np.int64)
    pivot = np.diag(color_matrices(N, p, q, x)[2])
    for _ in range(strands-1):density = np.kron(density,pivot) % p
    eta = pow(-1,N+1,p)*pow(q,N*(1-N)//2,p) % p
    d0 = eta*pow(N,-1,p) % p
    active = [j for j,(a,b) in enumerate(positions) if density[a]]
    transpose = [pos_index[positions[j][::-1]] for j in active]
    factors = np.array([density[positions[j][0]]*d0 % p for j in active], dtype=np.int64)
    gram = mm(p, (basis[active]*factors[:,None]).T % p, basis[transpose])
    assert np.array_equal(gram,gram.T)
    gram_det = determinant(gram,p)
    assert gram_det
    # Independently verify every basis element against the full operators.
    for j in range(expected):
        A = np.zeros((size,size),dtype=np.int64)
        for i,(a,b) in enumerate(positions):A[a,b]=basis[i,j]
        for G in (E,F,K):assert np.array_equal(mm(p,A,G),mm(p,G,A))
    return {'level':N,'strands':strands,'prime':p,
            'complete_centralizer_computed_without_fusion_frames':expected,
            'actual_full_ADO_cut_Gram_determinant':gram_det,
            'every_basis_element_checked_against_E_F_K':True,
            'complete_cut_is_symmetric_and_perfect':True}


def main():
    result = {
        'scope':'Exact PBW/projectivity and complete centralizer diagnostics; no geometric regulator or volume theorem.',
        'PBW_Frobenius_forms':[pbw_case(N,kind) for N in (2,3,4,5,6) for kind in ('generic','plus','minus')],
        'projective_complete_color':[projective_color_case(N) for N in (2,3,4,5,6)],
        'actual_dimension_calibration':[spectral_calibration_case(N) for N in (2,3,4,5,6)],
        'free_tensor_intertwiners':[free_tensor_case(N,kind) for N in (2,3,4) for kind in ('complete','shifted')],
        'complete_tensor_centralizers':[complete_centralizer_case(N,b)
            for N,b in ((2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3),(5,2),(6,2))]}
    path=Path(__file__).with_name('integral_centralizer_duality_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':str(path),**{k:len(v) for k,v in result.items() if isinstance(v,list)},
                      'complete_centralizer_basis_elements':sum(r['complete_centralizer_computed_without_fusion_frames']
                          for r in result['complete_tensor_centralizers'])}),flush=True)


if __name__=='__main__':main()
