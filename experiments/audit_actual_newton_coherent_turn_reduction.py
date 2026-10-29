#!/usr/bin/env python3
"""Exact original Newton modular reduction and complete reflected sources."""
import itertools
import json
from fractions import Fraction
from math import prod
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct


def generic_binomial_identity():
    Q = Fraction(2, 3)
    f = lambda n: prod((1-Q**j for j in range(1, n+1)), start=Fraction(1))
    b = lambda n, k: f(n)/(f(k)*f(n-k)) if 0 <= k <= n else Fraction(0)
    count = 0
    for i, j in itertools.product(range(7), repeat=2):
        actual = sum(((-1)**k*Q**(k*(k-1)//2-j*k)*b(i, k)*b(j+k, j)
                      for k in range(i+1)), Fraction(0))
        target = (-1)**i*Q**(i*(i-1)//2-i*j)*b(j, i)
        assert actual == target
        count += 1
    return count


def case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, x, Q = N-1, int(K[0, 0]), q*q % prime
    rho = (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    c = [(pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime
         for j in range(N)]
    kappa = pow(eta, d*d, prime)
    theta = pow(kappa, 3, prime)*pow(-q, d, prime) % prime
    eye = np.eye(N, dtype=np.int64)
    P = eye[::-1].copy()
    Z = np.diag(c).astype(np.int64)
    for j in range(1, N):
        Z[j, j-1] = (pow(Q, j, prime)+pow(Q, -j, prime)-2) % prime
    physical = [np.eye(N*N, dtype=np.int64)]
    packets = [eye]
    Fq, s2 = [1], [1]
    for r in range(1, N):
        Fq.append(Fq[-1]*(1-pow(Q, r, prime)) % prime)
        s2.append((-1)**r*pow(Q, -r*(r+1)//2, prime)*Fq[-1]**2 % prime)
        ratio = int(s2[r-1])*pow(int(s2[r]), -1, prime) % prime
        physical.append(ratio*((c[r-1]*np.eye(N*N, dtype=np.int64)-O)
                               @physical[-1] % prime) % prime)
        packets.append(ratio*((c[r-1]*eye-Z)@packets[-1] % prime) % prime)
    T = kappa*sum((pow(-q, r, prime)*B for r, B in enumerate(packets)),
                  np.zeros_like(eye)) % prime
    Ti = pow(kappa, -1, prime)*sum((pow(-q, -r, prime)*B for r, B in enumerate(packets)),
                                  np.zeros_like(eye)) % prime
    assert np.array_equal(kappa*sum((pow(-q, r, prime)*B for r, B in enumerate(physical)),
                                   np.zeros_like(O)) % prime, Rp)
    assert np.array_equal(pow(kappa, -1, prime)*sum(
        (pow(-q, -r, prime)*B for r, B in enumerate(physical)), np.zeros_like(O)) % prime, Rm)
    assert np.array_equal(T@P@T % prime, theta*(P@Ti@P % prime) % prime)
    C, Ci = T@P % prime, P@Ti % prime
    assert np.array_equal(C@C@C % prime, theta*eye % prime)
    B = T@T@P % prime
    assert np.array_equal(B, theta*(C@Ti@Ci % prime) % prime)
    # Exact FULL marked row, with no local degree replacement.
    cup = np.array([N*pow(x, -b, prime) % prime if a+b == d else 0
                    for a, b in itertools.product(range(N), repeat=2)], dtype=np.int64)
    marked = np.array([pow(x, b, prime)*pow(N*N, -1, prime) % prime
                       for a, b in itertools.product(range(N), repeat=2)], dtype=np.int64)
    A, Abar = eye.copy(), eye.copy()
    sources = 0
    for m in range(10):
        expected = N if m % 3 == 2 else 1
        v = A[:, 0]
        assert int(Abar[:, 0]@v % prime) == expected
        final = Abar.T@v % prime
        operator = sum((int(a)*M for a, M in zip(final, physical)), np.zeros_like(O)) % prime
        assert int(marked@(operator@cup % prime) % prime) == expected
        A, Abar = C@A % prime, (Ti@P % prime)@Abar % prime
        sources += 1
    for m in range(7):
        lhs = np.linalg.matrix_power(B.astype(object), m) % prime
        rhs = pow(theta, m, prime)*(C@np.linalg.matrix_power(Ti.astype(object), m)@Ci % prime) % prime
        assert np.array_equal(lhs, rhs)
    return {"N": N, "full_original_T_and_inverse": True,
            "all_input_modular_and_parabolic_run_relations": True,
            "literal_original_reflected_sources": sources}


if __name__ == '__main__':
    generic = generic_binomial_identity()
    rows = [case(N) for N in range(2, 11)]
    result = {"status": "PASS", "exact_generic_double_binomial_checks": generic,
              "original_root_families": rows,
              "scope": "Exact coherent source reduction and periodic reflected source rate; no new hyperbolic identification."}
    Path(__file__).with_name('actual_newton_coherent_turn_reduction_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {generic} generic finite identities; {len(rows)} full original alphabets; '
          f'{sum(r["literal_original_reflected_sources"] for r in rows)} complete reflected sources')
