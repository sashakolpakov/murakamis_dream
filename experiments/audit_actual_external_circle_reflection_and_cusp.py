#!/usr/bin/env python3
"""Actual external-color reflection, genuine first normals, and cusp scale.

Matrix checks use exact cyclotomic finite fields and dual numbers.
The mixed braid trace is built from the original typed word, separately
from the Casimir-polynomial calculation. No asymptotic is inferred.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import sympy as sp
import mpmath as mp

from audit_actual_nc_morse_graph_first_normal_source_reduction import (
    Local, add, const, inv, kron, mm, mul,
)
from audit_actual_two_cut_ports import balanced_data


def scale(A, scalar, p):
    return (A[0]*scalar[0] % p,
            (A[1]*scalar[0]+A[0]*scalar[1]) % p)


def subtract(A, B, p):
    return tuple((a-b) % p for a, b in zip(A, B))


def inverse_diagonal(K, p):
    K0 = np.diag([pow(int(x), -1, p) for x in np.diag(K[0])])
    return K0, -K0@K[1]@K0 % p


def polynomials(O, N, p):
    I = const(np.eye(len(O[0]), dtype=np.int64))
    C, P = [scale(I, (2, 0), p), O], [I, O]
    for n in range(2, N+1):
        C.append(subtract(mm(O, C[-1], p), C[-2], p))
        P.append(subtract(mm(O, P[-1], p), P[-2], p))
    Z = const(np.zeros_like(O[0]))
    L = [Z]+[scale(P[j-1], ((-1)**(j-1), 0), p)
             for j in range(1, N+1)]
    return C, L


def root_and_polynomial_jets(counts):
    for N in range(2, 11):
        loc = Local(N)
        p, q = loc.p, loc.q
        K, Ki = loc.Kpair, inverse_diagonal(loc.Kpair, p)
        O = add(mm(loc.Fpair, loc.Epair, p), scale(K, (q, q), p), p)
        qi = pow(q, -1, p)
        O = add(O, scale(Ki, (qi, -qi), p), p)
        C, L = polynomials(O, N, p)
        I = np.eye(N*N, dtype=np.int64)
        Z = np.zeros_like(I)
        Delta = ((C[N][0]+2*I) % p, C[N][1])
        assert not np.any(Delta[0])
        assert np.any(Delta[1])
        sectors = {a: loc.h0[a]*(loc.W[a][0]@loc.pi[a][0] % p) % p
                   for a in loc.W}
        assert np.array_equal(sum(sectors.values(), Z.copy()) % p, L[N][0])
        predicted = Z.copy()
        for a, sector in sectors.items():
            w, s = pow(q, 2*a+1, p), loc.d-2*a
            weight = (-1)**N*N*s*(w-pow(w, -1, p)) % p
            predicted = (predicted+weight*sector) % p
        assert np.array_equal(predicted, Delta[1])
        counts['full_generic_relation_defects'] += 1
        for h in range(N):
            T = scale(C[h], (pow(2, -1, p), 0), p)
            lead = mm(T, L[N], p)
            rhs = add(scale(lead, ((-1)**h, 0), p),
                      scale(L[h], ((-1)**N, 0), p), p)
            assert np.array_equal(rhs[0], L[N-h][0])
            counts['full_root_reflections'] += 1
            defect = scale(mm(Delta, L[h], p),
                           ((-1)**(N+1)*pow(2, -1, p) % p, 0), p)
            assert all(np.array_equal(x, y)
                       for x, y in zip(add(rhs, defect, p), L[N-h]))
            counts['polynomial_first_jet_reflections'] += 1
            for a, sector in sectors.items():
                s = loc.d-2*a
                weight = (pow(q, h*s, p)+pow(q, -h*s, p))*pow(2, -1, p) % p
                assert np.array_equal((-1)**h*T[0]@sector % p,
                                      weight*sector % p)
                counts['actual_complete_sector_weights'] += 1


def ordinary_module(n, q, p):
    L = n-1
    qp = lambda k: (pow(q, k, p), k*pow(q, k, p) % p)
    rho = tuple((a-b) % p for a, b in zip(qp(1), qp(-1)))
    def number(k):
        numerator = tuple((a-b) % p for a, b in zip(qp(k), qp(-k)))
        return mul(numerator, inv(rho, p), p)
    E = [np.zeros((n, n), dtype=np.int64) for _ in range(2)]
    F = [np.zeros((n, n), dtype=np.int64) for _ in range(2)]
    K = [np.zeros((n, n), dtype=np.int64) for _ in range(2)]
    H = [L-2*r for r in range(n)]
    for r, h in enumerate(H):
        K[0][r, r], K[1][r, r] = qp(h)
    for r in range(1, n):
        E[0][r-1, r], E[1][r-1, r] = mul(number(r), number(n-r), p)
        F[0][r, r-1] = 1
    return {'n': n, 'E': tuple(E), 'F': tuple(F), 'K': tuple(K),
            'H': H, 'rho': rho, 'number': number}


def mixed_crossing(A, B, q, eta, p):
    a, b = A['n'], B['n']
    total = const(np.eye(a*b, dtype=np.int64))
    ep = const(np.eye(a, dtype=np.int64))
    fp = const(np.eye(b, dtype=np.int64))
    coefficient = (1, 0)
    for k in range(1, min(a, b)):
        ep, fp = mm(ep, A['E'], p), mm(B['F'], fp, p)
        qpower = (pow(q, k-1, p), (k-1)*pow(q, k-1, p) % p)
        coefficient = mul(coefficient, qpower, p)
        coefficient = mul(coefficient, A['rho'], p)
        coefficient = mul(coefficient, inv(A['number'](k), p), p)
        total = add(total, scale(kron(ep, fp, p), coefficient, p), p)
    cartan0 = np.array([pow(eta, ha*hb, p)
                       for ha in A['H'] for hb in B['H']], dtype=np.int64)
    cartan1 = np.array([ha*hb*pow(2, -1, p)*v % p
                       for (ha, hb), v in zip(
                           ((ha, hb) for ha in A['H'] for hb in B['H']),
                           cartan0)], dtype=np.int64)
    uncheck = (cartan0[:, None]*total[0] % p,
               (cartan1[:, None]*total[0]+cartan0[:, None]*total[1]) % p)
    order = [u*b+v for v in range(b) for u in range(a)]
    return tuple(matrix[order, :] for matrix in uncheck)


def literal_circle(target, auxiliary, q, eta, p, N):
    modules = [target, target, auxiliary]
    size = target['n']**2*auxiliary['n']
    M = const(np.eye(size, dtype=np.int64))
    for position in (1, 0, 0, 1):
        R = mixed_crossing(modules[position], modules[position+1], q, eta, p)
        left = int(np.prod([x['n'] for x in modules[:position]]))
        right = int(np.prod([x['n'] for x in modules[position+2:]]))
        embedded = kron(const(np.eye(left, dtype=np.int64)),
                        kron(R, const(np.eye(right, dtype=np.int64)), p), p)
        M = mm(embedded, M, p)
        modules[position], modules[position+1] = modules[position+1], modules[position]
    j = auxiliary['n']
    standard = [np.zeros((N*N, N*N), dtype=np.int64) for _ in range(2)]
    literal = [np.zeros_like(standard[0]) for _ in range(2)]
    B = np.zeros_like(standard[0])
    for r, h in enumerate(auxiliary['H']):
        root = M[0][r::j, r::j]
        normal = M[1][r::j, r::j]
        k = pow(q, h, p)
        g = pow(q, (1-N)*h, p)
        standard[0] = (standard[0]+k*root) % p
        standard[1] = (standard[1]+k*(normal+h*root)) % p
        literal[0] = (literal[0]+g*root) % p
        literal[1] = (literal[1]+g*(normal+(1-N)*h*root)) % p
        B = (B+(-1)**(j-1)*k*h*root) % p
    return tuple(standard), tuple(literal), B


def literal_pivot_checks(counts):
    for N in range(2, 6):
        p, eta, q, *_ = balanced_data(N)
        target = ordinary_module(N, q, p)
        I = const(np.eye(N, dtype=np.int64))
        Et = add(kron(target['E'], target['K'], p), kron(I, target['E'], p), p)
        Ft = add(kron(target['F'], I, p), kron(inverse_diagonal(target['K'], p), target['F'], p), p)
        Kt = kron(target['K'], target['K'], p)
        O = scale(mm(Ft, Et, p), mul(target['rho'], target['rho'], p), p)
        O = add(O, scale(Kt, (q, q), p), p)
        qi = pow(q, -1, p)
        O = add(O, scale(inverse_diagonal(Kt, p), (qi, -qi), p), p)
        C, Lt = polynomials(O, N, p)
        Z = const(np.zeros((N*N, N*N), dtype=np.int64))
        L, B = [Z], [Z[0].copy()]
        for j in range(1, N+1):
            standard, literal, insertion = literal_circle(
                target, ordinary_module(j, q, p), q, eta, p, N)
            signed = scale(standard, ((-1)**(j-1), 0), p)
            assert all(np.array_equal(x, y) for x, y in zip(signed, Lt[j]))
            assert np.array_equal(literal[0], signed[0])
            assert np.array_equal(literal[1], (signed[1]-N*insertion) % p)
            L.append(literal)
            B.append(insertion)
            counts['literal_typed_circle_pivot_jets'] += 1
        Delta1 = C[N][1]
        for h in range(N):
            T = scale(C[h], (pow(2, -1, p), 0), p)
            rhs = (-1)**h*(T[1]@L[N][0]+T[0]@L[N][1])
            rhs = (rhs+(-1)**N*L[h][1]) % p
            rhs = (rhs+(-1)**(N+1)*pow(2, -1, p)*(Delta1@L[h][0] % p)) % p
            rhs = (rhs+N*((-1)**h*T[0]@B[N]+(-1)**N*B[h]-B[N-h])) % p
            assert np.array_equal(rhs, L[N-h][1])
            counts['literal_first_normal_reflections'] += 1


def symbolic_checks(counts):
    z = sp.symbols('z')
    for N in range(2, 14):
        for h in range(1, N):
            difference = (sp.chebyshevu(N-h-1, z/2)
                          -sp.chebyshevt(h, z/2)*sp.chebyshevu(N-1, z/2)
                          +sp.chebyshevt(N, z/2)*sp.chebyshevu(h-1, z/2))
            assert sp.expand(difference) == 0
            counts['formal_polynomial_identities'] += 1
    x, y, b, c = sp.symbols('x y b c', positive=True)
    A = x+y
    Tb, Tc = sp.sqrt(b*A+x*y), sp.sqrt(c*A+x*y)
    ux, uy = (x-y)/(b*A), 2*Tb/(b*A)
    identities = [
        (ux-1/x)**2+uy**2-(1/b+1/x)**2,
        (ux+1/y)**2+uy**2-(1/b+1/y)**2,
        ux**2+uy**2-1/b**2-4/(b*A),
        ux/(4/(b*A))-(x-y)/4,
        -uy/(4/(b*A))+Tb/2,
        (1/b)/(4/(b*A))-A/4,
    ]
    for expression in identities:
        assert sp.simplify(expression) == 0
        counts['inversion_circle_identities'] += 1
    W, H = A/2, (Tb+Tc)/2
    C = sp.pi*(Tb+Tc)/A
    tau0 = 2*sp.I*W/H
    for epsilon in (-1, 0, 1):
        Z = C-sp.pi*sp.I*epsilon
        tau = tau0/(1-epsilon*tau0/2)
        assert sp.simplify(tau-2*sp.pi*sp.I/Z) == 0
        assert sp.simplify(-2*sp.pi**2/Z-sp.pi*sp.I*tau) == 0
        assert sp.simplify(-2*sp.pi**2/Z-2*sp.pi*sp.I*(tau/2)) == 0
        counts['primitive_and_packet_hessian_conventions'] += 3


def folded_gaussian_checks(counts):
    mp.mp.dps = 75
    worst = mp.mpf(0)
    for N in (64, 65, 128, 129):
        d, M = N-1, (N-1)//2
        s0 = d-2*M
        for C in (mp.pi, mp.pi*mp.sqrt(3)):
            for epsilon in (-1, 0, 1):
                Z = C-mp.pi*1j*epsilon
                weights = [(1 if s0 == 0 and t == 0 else 2)
                           *mp.exp(-Z*t*(t+s0)/N) for t in range(M+1)]
                denominator = sum(weights)
                for z in (mp.mpc(0), mp.mpc('.3', '.2'), mp.mpc('-.4', '.25')):
                    gaussian = mp.exp(-mp.pi**2*z*z/Z)
                    targets = (gaussian, -2*mp.pi**2*z/Z*gaussian,
                               (4*mp.pi**4*z*z/Z**2-2*mp.pi**2/Z)*gaussian)
                    actual = [mp.mpc(0), mp.mpc(0), mp.mpc(0)]
                    for t, weight in enumerate(weights):
                        frequency = mp.pi*(2*t+s0)/mp.sqrt(N)
                        c, s = mp.cos(frequency*z), mp.sin(frequency*z)
                        actual[0] += weight*c
                        actual[1] -= weight*frequency*s
                        actual[2] -= weight*frequency**2*c
                    for value, target in zip(actual, targets):
                        error = abs(value/denominator-target)/max(1, abs(target))
                        worst = max(worst, error)
                        assert error < mp.mpf('1e-12'), (N, epsilon, z, error)
                        counts['both_parity_complex_gaussian_checks'] += 1
    return str(worst)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
        default=Path(__file__).with_name('actual_external_circle_reflection_and_cusp_results.json'))
    args = parser.parse_args()
    counts = {key: 0 for key in (
        'formal_polynomial_identities', 'full_root_reflections',
        'actual_complete_sector_weights', 'polynomial_first_jet_reflections',
        'full_generic_relation_defects', 'literal_typed_circle_pivot_jets',
        'literal_first_normal_reflections', 'inversion_circle_identities',
        'primitive_and_packet_hessian_conventions',
        'both_parity_complex_gaussian_checks')}
    symbolic_checks(counts)
    root_and_polynomial_jets(counts)
    literal_pivot_checks(counts)
    gaussian_error = folded_gaussian_checks(counts)
    result = {'status': 'PASS', 'counts': counts,
              'finite_gaussian_comparison_max_error': gaussian_error,
              'scope': 'Full physical root matrices and actual complete sectors, regular polynomial jets, independent literal mixed-braid/pivot first normals, exact inversion rectangle and cusp factor. No external packet or source gap is inferred.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
