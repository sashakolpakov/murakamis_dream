#!/usr/bin/env python3
"""Exact pure mixed-circle core/alias identities and uniform alias bounds.

Polynomial comparisons retain repeated-root derivatives. Principal-root
inequalities are independently sampled with high precision; their proof
is in the companion note, not inferred from finite-field signs.
"""
from fractions import Fraction
from pathlib import Path
import json

import mpmath as mp
import numpy as np

from audit_actual_positive_newton_multiplication import mul, add_scaled, trim
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_odd_central_cube_reflection_packet import turn
from audit_actual_crossing_circle_source_and_filling import ordinary_module, crossing_circle


def chebyshev_u(count, prime=None):
    values = [[1], [0, 1]]
    while len(values) < count:
        value = [0] + values[-1]
        add_scaled(value, values[-2], -1, prime)
        values.append(trim(value))
    return values[:count]


def generic_cases():
    count = 0
    for q in (Fraction(3, 2), Fraction(5, 3), Fraction(7, 5)):
        fac = [Fraction(1)]
        for n in range(1, 25):
            fac.append(fac[-1] * (q**n-q**(-n))/(q-1/q))
        basis = [[Fraction(1)]]
        for r in range(12):
            basis.append(mul(basis[-1], [q**(2*r+1)+q**(-2*r-1), -1]))
        for j, polynomial in enumerate(chebyshev_u(12), 1):
            candidate = [Fraction(0)] * j
            for r in range(j):
                coefficient = (-1)**r * fac[j+r]/(fac[2*r+1]*fac[j-r-1])
                add_scaled(candidate, basis[r], coefficient)
            assert trim(candidate) == trim(polynomial)
            count += 1
    return count


def root_data(N):
    prime, eta = root_field(N)
    q = eta*eta % prime
    Q = q*q % prime
    imaginary = pow(eta, N, prime)
    sine = [1]
    for r in range(1, N):
        factor = imaginary*pow(q, -r, prime)*(1-pow(Q, r, prime)) % prime
        sine.append(sine[-1]*factor % prime)
    nodes = [(pow(q, 2*r+1, prime)+pow(q, -2*r-1, prime)) % prime for r in range(N)]
    unscaled = [[1]]
    for node in nodes:
        unscaled.append(mul(unscaled[-1], [node, -1], prime))
    basis = [[a*pow(sine[r]**2 % prime, -1, prime) % prime for a in unscaled[r]]
             for r in range(N)]
    return prime, eta, q, sine, nodes, basis


def coordinates(polynomial, basis, prime):
    residual = list(polynomial) + [0]*(len(basis)-len(polynomial))
    answer = [0]*len(basis)
    for r in range(len(basis)-1, -1, -1):
        answer[r] = residual[r]*pow(basis[r][-1], -1, prime) % prime
        for k, entry in enumerate(basis[r]):
            residual[k] = (residual[k]-answer[r]*entry) % prime
    assert not any(residual)
    return answer


def alias_coefficients(N, j, sine, prime):
    answer = [0]*N
    for r in range(j):
        positive = sine[r]**2*sine[j+r]*pow(sine[2*r+1]*sine[j-r-1] % prime, -1, prime) % prime
        answer[N-1-r] = (-1)**(j-1+r)*positive % prime
    return answer


def predicted(N, j, sine, prime):
    if j <= N//2:
        return alias_coefficients(N, j, sine, prime)
    h = N-j
    answer = [0]*N if h == 0 else [(-1)**N*a % prime for a in alias_coefficients(N, h, sine, prime)]
    for v in range(h, (N-1)//2+1):
        answer[v] = N*N*sine[2*v]*pow(sine[v]**2*sine[v-h]*sine[v+h] % prime, -1, prime) % prime
    return answer


def root_case(N):
    prime, eta, q, sine, nodes, basis = root_data(N)
    count, alias_count, core_count = 0, 0, 0
    for j, polynomial in enumerate(chebyshev_u(N, prime), 1):
        source = [(-1)**(j-1)*a % prime for a in polynomial]
        actual = coordinates(source, basis, prime)[::-1]
        expected = predicted(N, j, sine, prime)
        assert actual == expected
        count += 1
        if j <= N//2:
            alias_count += j
        else:
            h = N-j
            core_count += (N-1)//2-h+1
            alias_count += h
    # The new one-factorial formula also equals the older positive sum.
    M = (N-1)//2
    for v in range(M+1):
        old = N*sum((1 if 2*k == N-1 else 2)*sine[k+v]
                    *pow(sine[k-v]*sine[v]**2 % prime, -1, prime)
                    for k in range(v, M+1)) % prime
        new = N*N*sine[2*v]*pow(sine[v]**4 % prime, -1, prime) % prime
        assert old == new
    return {'N': N, 'full_polynomial_color_identities': count,
            'alias_coefficients': alias_count, 'positive_core_coefficients': core_count}


def physical_case(N):
    prime, eta, q, E, F, K, pivot, _, _ = balanced_data(N)
    p2, eta2, q2, sine, nodes, _ = root_data(N)
    assert (prime, eta, q) == (p2, eta2, q2)
    rho = (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(a), -1, prime) for a in np.diag(Kt)])
    omega = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    identity = np.eye(N*N, dtype=np.int64)
    hats = [identity]
    for r in range(1, N):
        factor = pow((sine[r]*pow(sine[r-1], -1, prime))**2 % prime, -1, prime)
        hats.append(((nodes[r-1]*identity-omega)@hats[-1] % prime)*factor % prime)
    pv = [N*pow(q, -(N-1)*(N-1-u), prime) % prime for u in range(N)]
    polynomials = [identity, omega]
    for _ in range(2, N):
        polynomials.append((omega@polynomials[-1]-polynomials[-2]) % prime)
    target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [N-1-2*a for a in range(N)]}
    literal_loops = 0
    for j in range(1, N+1):
        loop = (-1)**(j-1)*polynomials[j-1] % prime
        if N <= 5:
            actual_loop = crossing_circle(target, ordinary_module(j, q, prime), q, eta, prime, N)
            assert np.array_equal(actual_loop, loop)
            literal_loops += 1
        turned = turn(loop, N, prime, pv)
        coefficients = predicted(N, j, sine, prime)
        expected = sum((a*hat for a, hat in zip(coefficients, hats)), np.zeros_like(identity)) % prime
        assert np.array_equal(turned, expected)
    return {'N': N, 'full_physical_turns': N, 'literal_mixed_crossing_loops': literal_loops}


def real_bounds():
    mp.mp.dps = 70
    alias_count = core_count = 0
    max_ratio = mp.mpf(0)
    for N in range(2, 151):
        theta = mp.pi/N
        logs = [mp.mpf(0)]
        for r in range(1, N):
            logs.append(logs[-1]+mp.log(2*mp.sin(r*theta)))
        for j in range(1, N//2+1):
            total = mp.mpf(0)
            for r in range(j):
                value = mp.exp(2*logs[r]+logs[j+r]-logs[2*r+1]-logs[j-r-1])
                ratio = value/(mp.mpf(N)/2)
                assert ratio <= 1+mp.mpf('1e-60')
                max_ratio = max(max_ratio, ratio)
                total += value
                alias_count += 1
            assert total <= mp.mpf(j*N)/2+mp.mpf('1e-55')
        for v in range((N-1)//2+1):
            for h in range(v+1):
                log_ratio = 2*logs[v]-logs[v-h]-logs[v+h]
                assert log_ratio <= mp.mpf('1e-60')
                if h > 0 and 2*v+1 < N:
                    assert log_ratio < 0
                if 2*v+1 == N:
                    assert abs(log_ratio) < mp.mpf('1e-60')
                core_count += 1
    return {'levels': 149, 'alias_bounds': alias_count,
            'core_domination_bounds': core_count,
            'maximum_alias_to_N_over_2_ratio': str(max_ratio)}


if __name__ == '__main__':
    generic = generic_cases()
    root = [root_case(N) for N in range(2, 65)]
    physical = [physical_case(N) for N in range(2, 11)]
    real = real_bounds()
    result = {'status': 'PASS', 'generic_chebyshev_newton_identities': generic,
              'root_full_polynomial_cases': root, 'literal_physical_cases': physical,
              'real_bounds': real,
              'scope': 'Exact pure Rturn(L_j) auxiliary-color leaves, all root normals retained; no global alias gap or long-filling theorem.'}
    Path(__file__).with_name('actual_pure_conway_auxiliary_color_leaf_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {generic} generic identities, {sum(x["full_polynomial_color_identities"] for x in root)} full root polynomials, '
          f'{sum(x["full_physical_turns"] for x in physical)} physical turns, '
          f'{sum(x["literal_mixed_crossing_loops"] for x in physical)} literal mixed loops, '
          f'{real["alias_bounds"]} alias and {real["core_domination_bounds"]} core inequalities')
