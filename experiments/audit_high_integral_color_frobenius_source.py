#!/usr/bin/env python3
"""Actual integral Weyl divided powers, normal edges and coherent wall row.

All matrix checks are exact in finite fields with a marked half-root.
The proof is in notes/high_integral_color_frobenius_wall_source.md.
Braiding/closure has an independent root-owned audit; no whole-Q
equality between two different actual colors is inferred here.
"""

import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np

from audit_finite_sum_annihilator import field


def sign(power):
    return 1 if power % 2 == 0 else -1


def integer_and_log_derivative(a, q, prime):
    rho = (q-pow(q, -1, prime)) % prime
    numerator = (pow(q, a, prime)-pow(q, -a, prime)) % prime
    value = numerator*pow(rho, -1, prime) % prime
    derivative = (a*(pow(q, a, prime)+pow(q, -a, prime))*rho
                  -numerator*(q+pow(q, -1, prime))) % prime
    derivative = derivative*pow(rho*rho % prime, -1, prime) % prime
    return value, derivative


def gaussian_Q_factory(Q, prime):
    @lru_cache(None)
    def choose(a, k):
        if k < 0 or k > a:
            return 0
        if k == 0 or k == a:
            return 1
        return (choose(a-1, k)+pow(Q, a-k, prime)*choose(a-1, k-1)) % prime
    return choose


def gaussian_Q_dual_factory(Q, prime):
    """Value and q-log derivative: Q'=2Q, including resonant factors."""
    @lru_cache(None)
    def choose(a, k):
        if k < 0 or k > a:
            return 0, 0
        if k == 0 or k == a:
            return 1, 0
        x0, x1 = choose(a-1, k)
        y0, y1 = choose(a-1, k-1)
        weight = pow(Q, a-k, prime)
        return ((x0+weight*y0) % prime,
                (x1+weight*(y1+2*(a-k)*y0)) % prime)
    return choose


def exponential_nilpotent(matrix, order, prime):
    value = np.eye(len(matrix), dtype=np.int64)
    power = value.copy()
    factorial = 1
    for j in range(1, order+1):
        power = power @ matrix % prime
        factorial = factorial*j % prime
        value = (value+power*pow(factorial, -1, prime)) % prime
    assert not np.any(power @ matrix % prime)
    return value


def exponential_nilpotent_dual(matrix0, matrix1, order, prime):
    value0 = np.eye(len(matrix0), dtype=np.int64)
    value1 = np.zeros_like(value0)
    power0, power1 = value0.copy(), value1.copy()
    factorial = 1
    for j in range(1, order+1):
        power1 = (power1 @ matrix0+power0 @ matrix1) % prime
        power0 = power0 @ matrix0 % prime
        factorial = factorial*j % prime
        inv = pow(factorial, -1, prime)
        value0 = (value0+power0*inv) % prime
        value1 = (value1+power1*inv) % prime
    assert not np.any(power0 @ matrix0 % prime)
    assert not np.any((power1 @ matrix0+power0 @ matrix1) % prime)
    return value0, value1


def source_case(N, r):
    prime, _, q = field(N)
    Q = q*q % prime
    rho = (q-pow(q, -1, prime)) % prime
    dimension = N*(r+1)
    m = dimension-1
    choose = gaussian_Q_factory(Q, prime)
    choose_dual = gaussian_Q_dual_factory(Q, prime)
    beta = [sign(N*k*(k-1)//2+k*s) for k in range(r+1) for s in range(N)]
    E = np.zeros((dimension, dimension), dtype=np.int64)
    F = np.zeros_like(E)
    Ediv = np.zeros_like(E)
    Fdiv = np.zeros_like(E)
    Ediv1 = np.zeros_like(E)
    Fdiv1 = np.zeros_like(E)
    E_cross_derivative = np.zeros_like(E)
    F_cross_derivative = np.zeros_like(E)
    for j in range(dimension):
        if j:
            E[j-1, j] = beta[j]*beta[j-1]*integer_and_log_derivative(m-j+1, q, prime)[0] % prime
            if j % N == 0:
                E_cross_derivative[j-1, j] = beta[j]*beta[j-1]*integer_and_log_derivative(m-j+1, q, prime)[1] % prime
        if j < m:
            F[j+1, j] = beta[j]*beta[j+1]*integer_and_log_derivative(j+1, q, prime)[0] % prime
            if j % N == N-1:
                F_cross_derivative[j+1, j] = beta[j]*beta[j+1]*integer_and_log_derivative(j+1, q, prime)[1] % prime
        if j >= N:
            upper = m-j+N
            coefficient = pow(q, -N*(upper-N), prime)*choose(upper, N) % prime
            Ediv[j-N, j] = beta[j]*beta[j-N]*coefficient % prime
            g0, g1 = choose_dual(upper, N)
            assert g0 == choose(upper, N)
            coefficient1 = pow(q, -N*(upper-N), prime)*(g1-N*(upper-N)*g0) % prime
            Ediv1[j-N, j] = beta[j]*beta[j-N]*coefficient1 % prime
        if j+N < dimension:
            upper = j+N
            coefficient = pow(q, -N*(upper-N), prime)*choose(upper, N) % prime
            Fdiv[j+N, j] = beta[j]*beta[j+N]*coefficient % prime
            g0, g1 = choose_dual(upper, N)
            assert g0 == choose(upper, N)
            coefficient1 = pow(q, -N*(upper-N), prime)*(g1-N*(upper-N)*g0) % prime
            Fdiv1[j+N, j] = beta[j]*beta[j+N]*coefficient1 % prime

    Est = np.zeros((N, N), dtype=np.int64)
    Fst = np.zeros_like(Est)
    for s in range(1, N):
        Est[s-1, s] = integer_and_log_derivative(N-s, q, prime)[0]
        Fst[s, s-1] = integer_and_log_derivative(s, q, prime)[0]
    Kst = np.diag([pow(q, N-1-2*s, prime) for s in range(N)]).astype(np.int64)
    K = np.diag([pow(q, m-2*j, prime) for j in range(dimension)]).astype(np.int64)
    assert np.array_equal(E, np.kron(np.eye(r+1, dtype=np.int64), sign(r)*Est) % prime)
    assert np.array_equal(F, np.kron(np.eye(r+1, dtype=np.int64), Fst) % prime)
    assert np.array_equal(K, np.kron(np.eye(r+1, dtype=np.int64), sign(r)*Kst) % prime)

    ecl = np.zeros((r+1, r+1), dtype=np.int64)
    fcl = np.zeros_like(ecl)
    for k in range(1, r+1):
        ecl[k-1, k] = r-k+1
        fcl[k, k-1] = k
    tau = sign(N*r-1)
    assert np.array_equal(tau*Ediv % prime, np.kron(ecl, np.eye(N, dtype=np.int64)) % prime)
    assert np.array_equal(Fdiv, np.kron(fcl, np.eye(N, dtype=np.int64)) % prime)
    hcl = np.diag([r-2*k for k in range(r+1)]).astype(np.int64)
    assert np.array_equal((ecl @ fcl-fcl @ ecl) % prime, hcl % prime)
    assert np.array_equal((hcl @ ecl-ecl @ hcl) % prime, 2*ecl % prime)
    assert np.array_equal((hcl @ fcl-fcl @ hcl) % prime, -2*fcl % prime)
    for generator in (E, F, K):
        for divided in (Ediv, Fdiv):
            assert not np.any((generator @ divided-divided @ generator) % prime)

    # Independent actual q-log derivatives of integral entries, then
    # division by delta'=d(1-q^(2N))/dlogq=-2N.
    inv_delta_prime = pow(-2*N % prime, -1, prime)
    E_normal = E_cross_derivative*inv_delta_prime % prime
    F_normal = F_cross_derivative*inv_delta_prime % prime
    ewrap = np.zeros((N, N), dtype=np.int64)
    fwrap = np.zeros_like(ewrap)
    ewrap[N-1, 0] = 1
    fwrap[0, N-1] = 1
    assert np.array_equal(E_normal, sign(r+1)*pow(rho, -1, prime)*np.kron(ecl, ewrap) % prime)
    assert np.array_equal(F_normal, pow(rho, -1, prime)*np.kron(fcl, fwrap) % prime)

    # Coherent source is constructed from the literal divided action.
    expF = exponential_nilpotent(fcl, r, prime)
    expE = exponential_nilpotent(ecl, r, prime)
    source = expF[:, 0]
    row = expE[0, :]*pow(pow(2, r, prime), -1, prime) % prime
    assert np.array_equal(source, np.ones(r+1, dtype=np.int64))
    assert list(map(int, row)) == [math.comb(r, k)*pow(pow(2, r, prime), -1, prime) % prime
                                   for k in range(r+1)]
    assert int(row @ source) % prime == 1
    coupon = source[:, None]*row[None, :] % prime
    assert np.array_equal(coupon @ coupon % prime, coupon)
    assert int(np.trace(coupon)) % prime == 1

    entries = np.array([k*k+3*k+2 for k in range(r+1)], dtype=np.int64) % prime
    head_projector = np.zeros((N, N), dtype=np.int64)
    head_projector[N//2, N//2] = 1
    insertion = np.kron(np.diag(entries), np.eye(N, dtype=np.int64))
    marked_coupon = np.kron(coupon, head_projector)
    wall = (r+1)*int(np.trace(marked_coupon @ insertion % prime))*pow(dimension, -1, prime) % prime
    expected = sum(math.comb(r, k)*int(entries[k]) for k in range(r+1))
    expected = expected*pow(N*pow(2, r, prime) % prime, -1, prime) % prime
    assert wall == expected
    normalization = (r+1)*int(np.trace(marked_coupon))*pow(dimension, -1, prime) % prime
    assert normalization == pow(N, -1, prime)
    assert sign(r*(N-1)) == (1 if r == N else sign(r*(N-1)))
    # Canonical whole source/cosource from actual generic divided matrices.
    # The unit u_s is differentiated before its normalization is canceled.
    nonzero_source_jets = 0
    for s in range(N):
        indices = [k*N+s for k in range(r+1)]
        localE0 = tau*Ediv[np.ix_(indices, indices)] % prime
        localE1 = tau*Ediv1[np.ix_(indices, indices)] % prime
        localF0 = Fdiv[np.ix_(indices, indices)]
        localF1 = Fdiv1[np.ix_(indices, indices)]
        e0, e1 = exponential_nilpotent_dual(localE0, localE1, r, prime)
        f0, f1 = exponential_nilpotent_dual(localF0, localF1, r, prime)
        psi0, psi1 = f0[:, 0], f1[:, 0]
        scale = pow(pow(2, r, prime), -1, prime)
        lambda0, lambda1 = e0[0, :]*scale % prime, e1[0, :]*scale % prime
        u0 = int(lambda0 @ psi0) % prime
        u1 = int(lambda1 @ psi0+lambda0 @ psi1) % prime
        assert u0 == 1
        normalized1 = (lambda1-u1*lambda0) % prime
        coupon0 = psi0[:, None]*lambda0[None, :] % prime
        coupon1 = (psi1[:, None]*lambda0[None, :]
                   +psi0[:, None]*normalized1[None, :]) % prime
        assert np.array_equal(coupon0, coupon)
        assert not np.any((coupon0 @ coupon1+coupon1 @ coupon0-coupon1) % prime)
        assert int(np.trace(coupon1)) % prime == 0
        weight1 = (lambda0*psi1+normalized1*psi0) % prime
        assert int(np.sum(weight1)) % prime == 0
        if np.any(weight1):
            nonzero_source_jets += 1
    return {"N": N, "r": r, "dimension": dimension, "prime": prime,
            "tau": tau, "ordinary_Steinberg_blocks_exact": True,
            "integral_divided_power_and_classical_action_exact": True,
            "actual_normal_block_edges_exact": True,
            "divided_coherent_source_and_wall_row_exact": True,
            "whole_actual_divided_source_idempotent_first_jet_exact": True,
            "nonzero_coherent_wall_weight_first_jets": nonzero_source_jets,
            "degree_N_wall_source": r == N}


def main():
    cases = [source_case(N, r) for N in range(2, 9) for r in sorted({0, 1, 2, N})]
    result = {"actual_high_integral_color_cases": cases,
              "scope": "Actual module/divided/first-normal source and wall row; separate braiding audit, no low/high whole-color jet equality or second-current comparison."}
    target = Path(__file__).with_name("high_integral_color_frobenius_source_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"actual_color_cases": len(cases),
                      "all_parity_level_range": [2, 8],
                      "degree_N_wall_sources": sum(row["degree_N_wall_source"] for row in cases),
                      "whole_highcolor_source_first_jet_cases": len(cases),
                      "output": str(target)}, indent=2))


if __name__ == "__main__":
    main()
