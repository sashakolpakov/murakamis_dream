#!/usr/bin/env python3
"""Full physical quarter-turn, explicit pretzel base polynomial and jets.

Every comparison is against original finite E/F/R, literal circle, turns
and sole marked source. Nodal and normal coefficients are both retained.
"""

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_crossing_circle_source_and_filling import (
    crossing_circle, ordinary_module, power,
)
from audit_actual_odd_pretzel_augmented_transfer_source import transfer_source
from audit_actual_complete_casimir_hermite_packet import canonical_field_frame


def rotate_box(B, N, x, p):
    d = N-1
    C = np.zeros_like(B)
    for u in range(N):
        for b in range(N):
            for v in range(N):
                e = u+b-v
                if 0 <= e < N:
                    C[u*N+b, v*N+e] = pow(x, u-e, p)*int(B[(d-u)*N+v, b*N+d-e]) % p
    return C


def polyadd(a, b, p):
    out = [0]*max(len(a), len(b))
    for j, c in enumerate(a):
        out[j] += int(c)
    for j, c in enumerate(b):
        out[j] += int(c)
    return [c % p for c in out]


def polymul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for j, c in enumerate(a):
        for k, e in enumerate(b):
            out[j+k] += int(c)*int(e)
    return [c % p for c in out]


def polyvalue(a, z, p):
    out = 0
    for c in reversed(a):
        out = (out*z+int(c)) % p
    return out


def derivative(a, p):
    return [(j*int(c)) % p for j, c in enumerate(a) if j]


def matrix_value(a, A, p):
    value, I = np.zeros_like(A), np.eye(len(A), dtype=np.int64)
    for c in reversed(a):
        value = (value@A+int(c)*I) % p
    return value


def remainder(a, P, p):
    a = list(a)
    n = len(P)-1
    for j in range(len(a)-1, n-1, -1):
        c = a[j] % p
        for k, b in enumerate(P):
            a[j-n+k] = (a[j-n+k]-c*b) % p
    return (a+[0]*n)[:n]


def base_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x, kappa = N-1, q*q % p, int(K[0, 0]), int(Rp[0, 0])
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    U0, U1 = np.eye(N*N, dtype=np.int64), O.copy()
    if d == 0:
        LN = U0
    elif d == 1:
        LN = -U1 % p
    else:
        for _ in range(2, d+1):
            U0, U1 = U1, (O@U1-U0) % p
        LN = pow(-1, d, p)*U1 % p
    if N <= 7:
        target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [d-2*a for a in range(N)]}
        literal = crossing_circle(target, ordinary_module(N, q, p), q, eta, p, N)
        assert np.array_equal(LN, literal)
    assert np.array_equal(rotate_box(Rm, N, x, p), Rp)
    cup = np.array([N*pow(x, -b, p) % p if a+b == d else 0
                    for a in range(N) for b in range(N)], dtype=np.int64)
    ell = np.array([pow(x, a, p)*pow(N, -1, p) % p if a+b == d else 0
                    for a in range(N) for b in range(N)], dtype=np.int64)
    assert np.array_equal(rotate_box(np.eye(N*N, dtype=np.int64), N, x, p),
                          np.outer(cup, ell) % p)
    B, Z = Rm@LN % p, rotate_box(Rm@LN % p, N, x, p)
    assert np.array_equal(Z@O % p, O@Z % p)
    ids = [u*N+d-u for u in range(N)]
    A, middle = O[np.ix_(ids, ids)], Z[np.ix_(ids, ids)]
    f = [[1]]
    if d:
        f.append([(-int(A[0, 0])*pow(int(A[0, 1]), -1, p)) % p,
                  pow(int(A[0, 1]), -1, p)])
    for v in range(1, d):
        numerator = polyadd(polymul([-int(A[v, v]), 1], f[v], p),
                            [-int(A[v, v-1])*c for c in f[v-1]], p)
        f.append([c*pow(int(A[v, v+1]), -1, p) % p for c in numerator])
    for v in range(N):
        row = matrix_value(f[v], A, p)[0]
        assert np.array_equal(row, np.eye(N, dtype=np.int64)[v])
    fac, sine = [1], [1]
    imaginary = pow(eta, N, p)
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
        sine.append(pow(imaginary, a, p)*pow(q, -a*(a+1)//2, p)*fac[a] % p)
    coefficients, bvalues = [0]*N, []
    for v in range(d//2+1):
        length, low = d-2*v, d-v
        cosine = 1
        for r in range(length):
            exponent = 2*r+1-length
            cosine = cosine*(pow(eta, exponent, p)+pow(eta, -exponent, p)) % p
        b = sine[low]**2*cosine*pow(sine[length], -1, p) % p
        # Independent original positive-CD corner sum, as an exact field identity.
        corner = sine[low]**2*sum(pow(sine[a]*sine[length-a] % p, -1, p)
                                    for a in range(length+1)) % p
        assert b == corner
        assert b == N*N*sine[2*v]*pow(sine[v], -4, p) % p
        assert b*pow(x, v, p) % p == N*N*fac[2*v]*pow(fac[v], -4, p) % p
        assert int(middle[0, v]) == pow(kappa, -1, p)*b % p
        bvalues.append(b)
        for k, c in enumerate(f[v]):
            coefficients[k] = (coefficients[k]+pow(kappa, -1, p)*b*c) % p
    assert not np.any(middle[0, d//2+1:])
    assert np.array_equal(matrix_value(coefficients, O, p), Z)
    assert coefficients[d//2] != 0 and all(c == 0 for c in coefficients[d//2+1:])
    if N % 2:
        m = d//2
        assert coefficients[m] == pow(kappa, -1, p)*pow(q, -m*(m+1), p) % p
    V, Vi, meta, blocks = canonical_field_frame(A, N, d, p, q)
    expected = np.zeros_like(A)
    col = 0
    derivative_coeff = derivative(coefficients, p)
    def pochhammer(a, r):
        out = 1
        for k in range(r):
            out = out*(1-a*pow(Q, k, p)) % p
        return out
    products = [[1]]
    for r in range(d//2):
        products.append(polymul(products[-1],
                                [(1+pow(Q, 2*r+1, p)) % p,
                                 -q*pow(Q, r, p) % p], p))
    # Independent finite product-basis formula, not a fit of node values.
    for v in range(d//2+1):
        expansion = [0]*(v+1)
        for r in range(v+1):
            weight = (pow(x, v, p)*pochhammer(pow(Q, -v, p), r)
                      *pow(Q, r, p)*pow(fac[r], -3, p)) % p
            for k, a in enumerate(products[r]):
                expansion[k] = (expansion[k]+weight*a) % p
        assert expansion == f[v]
    for j in range(d//2+1):
        c = (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
        node = 0
        for v in range(d//2+1):
            for r in range(min(v, j)+1):
                term = (pow(Q, r*(r-v-j), p)*fac[2*v]*fac[j+r]
                        *pow(fac[v], -3, p)*pow(fac[v-r], -1, p)
                        *pow(fac[j-r], -1, p)*pow(fac[r], -3, p)) % p
                node += term
        assert pow(kappa, -1, p)*N*N*node % p == polyvalue(coefficients, c, p)
        if 2*j == d:
            continue  # Odd simple node needs no normal condition.
        normal, tail = 0, 0
        for v in range(d//2+1):
            for r in range(v+1):
                A = (fac[2*v]*pow(fac[v], -4, p)
                     *pochhammer(pow(Q, -v, p), r)*pow(Q, r, p)
                     *pow(fac[r], -3, p)) % p
                if r <= j:
                    bj = pochhammer(pow(Q, j+1, p), r)*pochhammer(pow(Q, -j, p), r) % p
                    dj = sum((pow(Q, a-j, p)*pow(1-pow(Q, a-j, p), -1, p)
                              -pow(Q, a+j+1, p)*pow(1-pow(Q, a+j+1, p), -1, p))
                             for a in range(r)) % p
                    normal += A*bj*dj
                else:
                    term = (A*pow(-1, j, p)*pow(Q, -j*(j+1)//2, p)
                            *fac[j+r]*fac[r-j-1]) % p
                    normal += term
                    tail += term
        w = pow(q, 2*j+1, p)
        normal = normal*pow(w-pow(w, -1, p), -1, p) % p
        assert pow(kappa, -1, p)*N*N*normal % p == polyvalue(derivative_coeff, c, p)
    for block in blocks:
        j = block['j']
        c = (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
        value = polyvalue(coefficients, c, p)
        expected[col, col] = value
        if block['multiplicity'] == 2:
            expected[col, col+1] = polyvalue(derivative_coeff, c, p)
            expected[col+1, col+1] = value
            col += 2
        else:
            col += 1
    assert np.array_equal(Vi@middle % p@V % p, expected)
    traceweights = np.array([int(pivot[b]) for a in range(N) for b in range(N)])
    phi = lambda X: int(np.dot(traceweights, np.diag(X)))*pow(N, -1, p) % p
    for v in range(N):
        value = phi(power(O, v, p))
        assert value == (pow(-1, d, p)*N*N % p if v == d else 0)
    T0, T1 = [2], [0, 1]
    for _ in range(2, N+1):
        T0, T1 = T1, polyadd([0]+T1, [-c for c in T0], p)
    PN = polyadd(T1, [2], p)
    source_powers = []
    for s in (1, 3, 5, 7, 9):
        polynomial, unreduced = [1], [1]
        for _ in range(s):
            polynomial = remainder(polymul(polynomial, coefficients, p), PN, p)
            unreduced = polymul(unreduced, coefficients[:d//2+1], p)
        source = phi(power(Z, s, p))
        top_source = pow(-1, d, p)*N*N*polynomial[d] % p
        assert source == top_source
        assert source == transfer_source(N, x, p, [B]*s)
        laurent = {}
        for k, coefficient in enumerate(unreduced):
            for r in range(k+1):
                exponent = k-2*r
                laurent[exponent] = (laurent.get(exponent, 0)
                                     +coefficient*math.comb(k, r)) % p
        winding = sum((-1)**(m-1)*m*(laurent.get(m*N-1, 0)-laurent.get(m*N+1, 0))
                      for m in range(1, (s*(d//2)+1)//N+1))
        assert pow(-1, d, p)*N*N*winding % p == source
        spectral = 0
        for j in range((N-1)//2):
            c = (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
            lam, xi = polyvalue(coefficients, c, p), polyvalue(derivative_coeff, c, p)
            spectral += (4-c*c)*s*xi*pow(lam, s-1, p)-c*pow(lam, s, p)
        # For even N the lower half includes j=N/2-1 as a double node.
        if N % 2 == 0:
            j = N//2-1
            c = (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
            lam, xi = polyvalue(coefficients, c, p), polyvalue(derivative_coeff, c, p)
            spectral += (4-c*c)*s*xi*pow(lam, s-1, p)-c*pow(lam, s, p)
        spectral *= pow(-1, d, p)
        if N % 2:
            spectral += pow(polyvalue(coefficients, -2 % p, p), s, p)
        assert spectral % p == source
        source_powers.append({'odd_boxes': s, 'original_full_source': int(source)})
    return {'N': N, 'base_polynomial_degree': d//2,
            'literal_entire_pair_quarter_turn_and_positive_corner_product': True,
            'all_value_and_normal_Hermite_channels': True,
            'finite_quadratic_factorial_nodes_and_surviving_normal_tail': True,
            'original_phi_all_coefficients': True,
            'all_true_finite_integer_windings': True,
            'all_odd_box_source_checks': source_powers}


def formal_continuant_identity():
    q, V, R = sp.symbols('q V R')
    Q, x = q*q, -1/q
    D = q+1/q-q*(1-V)**2-(1-Q*V)**2/q
    lhs = -(1-Q*V)**2*x*(Q*V-1)/(Q*V-R)
    rhs = (q*R+1/(q*R)-D
           -(1/q)*(Q/R)*V*(1-R)**3/(Q*V-R)
           +(1-V)**2/x*(V-R)/(V-1))
    assert sp.factor(lhs-rhs) == 0
    return {'formal_product_basis_coefficient_recurrence': True,
            'independent_variables': ['q', 'V=Q^v', 'R=Q^r']}


if __name__ == '__main__':
    results = {'status': 'PASS', 'formal_continuant_identity': formal_continuant_identity(),
               'all_level_source_polynomials': [base_case(N) for N in range(2, 11)],
               'scope': 'Exact original augmented-pretzel reduction, not an asymptotic geometric survival proof.'}
    Path(__file__).with_name('actual_pretzel_complete_base_casimir_polynomial_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS 9 full physical base polynomials/complete jets; 45 original odd-box sources and spectral/top-coefficient identities')
