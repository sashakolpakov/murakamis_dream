#!/usr/bin/env python3
"""Actual highest-spin wall contraction and charged first-normal R source.

Checks the whole-memory complex both at generic Q and its actual root;
the local R check assembles the original integral universal matrix and
its first normal before projecting a charged channel.
"""

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_degree_elevation_actual_head_ward import elev, sl2
from audit_high_color_first_normal_r_degree import setup
from audit_finite_sum_annihilator import field


def modular_inverse(matrix, prime):
    size = len(matrix)
    work = np.column_stack((matrix.copy() % prime, np.eye(size, dtype=np.int64)))
    for j in range(size):
        row = next(i for i in range(j, size) if work[i, j] % prime)
        work[[row, j]] = work[[j, row]]
        work[j] = work[j]*pow(int(work[j, j]), -1, prime) % prime
        factors = work[:, j].copy()
        factors[j] = 0
        work = (work-factors[:, None]*work[j]) % prime
    assert np.array_equal(work[:, :size], np.eye(size, dtype=np.int64))
    return work[:, size:]


def complement_complex_case(N, generic):
    prime, generator, qroot = field(N)
    Q = generator if generic else qroot*qroot % prime
    L, size = 2*N, 2*N+1
    rho = np.diag([pow(Q, N-j, prime) for j in range(size)]).astype(np.int64)
    F = np.zeros((size, size), dtype=np.int64)
    for j in range(L):
        F[j+1, j] = 1
    eye = np.eye(size, dtype=np.int64)
    qi = pow(Q, -1, prime)
    d0 = np.vstack(((rho-eye) % prime, F))
    d1 = np.column_stack((-qi*F % prime, (rho-qi*eye) % prime))
    assert not np.any(d1 @ d0 % prime)
    h1 = np.zeros((size, 2*size), dtype=np.int64)
    h2 = np.zeros((2*size, size), dtype=np.int64)
    for j in range(L):
        h1[j, size+j+1] = 1
        h2[j, j+1] = -Q % prime
    unit = (pow(Q, N, prime)-qi) % prime
    assert unit
    h2[size, 0] = pow(unit, -1, prime)
    p0 = np.zeros_like(eye)
    p0[L, L] = 1
    p1 = np.zeros((2*size, 2*size), dtype=np.int64)
    p1[L, L] = 1
    assert np.array_equal(h1 @ d0 % prime, eye-p0)
    assert np.array_equal((d0 @ h1+h2 @ d1) % prime, (np.eye(2*size, dtype=np.int64)-p1) % prime)
    assert np.array_equal(d1 @ h2 % prime, eye)
    assert int(d0[L, L]) % prime == (pow(Q, -N, prime)-1) % prime
    return {"N": N, "generic_memory": generic, "prime": prime,
            "all_forks_contract_with_unit_top_arrow": True,
            "exact_single_Bockstein_wall_line": True}


def actual_spin_and_source(N):
    e, f, h = [sp.Matrix(a.tolist()) for a in sl2(N)]
    v = (-1)**N*e**N/sp.factorial(2*N)
    chain = [v]
    for _ in range(2*N):
        chain.append(f*chain[-1]-chain[-1]*f)
    assert chain[-1] == f**N
    u, t, m = sp.symbols("u t m")

    def obstruction(C):
        return sp.expand(sum((-1)**j*sp.binomial(N, i)*C[i, j]*u**(N+i-j)
                             for i in range(N+1) for j in range(N+1)))

    for j, C in enumerate(chain):
        assert obstruction(C) == sp.factorial(N)/sp.factorial(2*N-j)*u**j
    for C in chain:
        G = obstruction(C)
        assert sp.expand(obstruction(e*C-C*e)-sp.diff(G, u)) == 0
        assert sp.expand(obstruction(f*C-C*f)-(2*N*u*G-u*u*sp.diff(G, u))) == 0
        assert sp.expand(obstruction(h*C-C*h)-(2*N*G-2*u*sp.diff(G, u))) == 0
    # The unitary HS chain used for the tame contraction has exact norms.
    g = [sp.binomial(N, k) for k in range(N+1)]
    norms = [sp.simplify(sum(C[i, j]**2*g[i]/g[j]
                             for i in range(N+1) for j in range(N+1))) for C in chain]
    for j in range(2*N):
        assert sp.simplify(norms[j+1]/norms[j]-(j+1)*(2*N-j)) == 0
    wall = sp.zeros(N+1)
    wall[N, 0] = 1
    psi = sp.ones(N+1, 1)
    paired = sp.Matrix([[sp.binomial(N, k)*((1+m)/2)**(N-k)*((1-m)/2)**k
                         for k in range(N+1)]])
    response = sp.expand((paired*wall*psi)[0])
    assert sp.expand(response-((1-m)/2)**N) == 0
    assert sp.integrate(response/2, (m, -1, 1)) == sp.Rational(1, N+1)
    assert response.subs(m, 0) == sp.Rational(1, 2**N)
    H = sp.Matrix(N, N, lambda i, j: 1+2*i+3*j)
    correlated_psi = sp.zeros(N*(N+1), 1)
    correlated_lambda = sp.zeros(1, N*(N+1))
    for k in range(N+1):
        index = k*N+k % N
        correlated_psi[index] = 1
        correlated_lambda[index] = sp.Rational(sp.binomial(N, k), 2**N)
    assert (correlated_lambda*sp.kronecker_product(wall, H)*correlated_psi)[0] == sp.Rational(1, 2**N)*H[0, 0]
    # Literal elevated coupons in the actual resonant current example.
    oldP0 = sp.zeros(N)
    oldP0[0, 0] = 1
    oldLow = sp.zeros(N)
    oldLow[N-1, 0] = 1
    # Characteristic-zero version of the explicit elevation formula.
    def elevation(C):
        return sp.Matrix(N+1, N+1, lambda i, j:
                         (sp.Rational(N-i, N)*C[i, j] if i<N and j<N else 0)
                         +(sp.Rational(i, N)*C[i-1, j-1] if i and j else 0))
    X, Y = elevation(oldP0), elevation(oldLow)
    assert f*Y == wall and Y*f == wall
    current = N*sp.kronecker_product(e*X-X*e, wall)
    uniform = sp.ones(1, N+1)/(N+1)
    plus = sp.Matrix([[sp.Rational(sp.binomial(N, k), 2**N) for k in range(N+1)]])
    psi2 = sp.kronecker_product(psi, psi)
    assert (sp.kronecker_product(uniform, uniform)*current*psi2)[0] == -sp.Rational(N-1, N+1)
    assert (sp.kronecker_product(plus, plus)*current*psi2)[0] == -sp.Rational(N*(N-1), 2**(2*N-1))
    return {"N": N, "actual_highest_spin_matrix_chain_exact": True,
            "global_incidence_section_and_current_action_exact": True,
            "unitary_HS_arrow_coefficients_exact": True,
            "uniform_wall_source": str(sp.Rational(1, N+1)),
            "original_coherent_wall_source": str(sp.Rational(1, 2**N)),
            "coupled_head_endpoint_source_exact": True,
            "actual_tail_current_source_weights_exact": True}


def actual_normal_R_case(N):
    r = N
    prime, highest, coefficient = setup(N, r)
    color = highest+1
    size = color*color
    R0 = np.zeros((size, size), dtype=np.int64)
    R1 = np.zeros_like(R0)
    for i in range(color):
        for j in range(color):
            column = i*color+j
            for transfer in range(min(i, highest-j)+1):
                value = coefficient(i, j, transfer)
                row = (i-transfer)*color+j+transfer
                R0[row, column], R1[row, column] = value.x, value.dx
    interaction = modular_inverse(R0, prime) @ R1 % prime
    # Isolate the genuine first resonant Fr charge, leaving EVERY head entry.
    e, f, _ = sl2(N)
    expected_tail = N*np.kron(np.kron(e, np.eye(N, dtype=np.int64)),
                              np.kron(f, np.eye(N, dtype=np.int64))) % prime
    charged = np.zeros_like(interaction)
    for row in range(size):
        oi, oj = divmod(row, color)
        oa, ob = oi//N, oj//N
        for column in range(size):
            ii, ij = divmod(column, color)
            a, b = ii//N, ij//N
            if (oa-a, ob-b) == (-1, 1):
                charged[row, column] = interaction[row, column]
    assert np.array_equal(charged, expected_tail)
    oldP0, oldLow = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    oldP0[0, 0], oldLow[N-1, 0] = 1, 1
    X, Y = elev(oldP0, prime), elev(oldLow, prime)
    insertion = np.kron(np.kron(X, np.eye(N, dtype=np.int64)),
                         np.kron(Y, np.eye(N, dtype=np.int64))) % prime
    commutator = (interaction @ insertion-insertion @ interaction) % prime
    wall = np.zeros((N+1, N+1), dtype=np.int64)
    wall[N, 0] = 1
    expected_current = N*np.kron(np.kron((e @ X-X @ e) % prime, np.eye(N, dtype=np.int64)),
                                 np.kron(wall, np.eye(N, dtype=np.int64))) % prime
    projected = np.zeros_like(commutator)
    for row in range(size):
        oi, oj = divmod(row, color)
        oa, ob = oi//N, oj//N
        for column in range(size):
            ii, ij = divmod(column, color)
            a, b = ii//N, ij//N
            if (oa-a, ob-b) == (-1, N):
                projected[row, column] = commutator[row, column]
    assert np.array_equal(projected, expected_current)
    assert np.any(projected)
    return {"N": N, "prime": prime, "actual_R_matrix_dimension": size,
            "full_actual_normal_charged_tail_exact": True,
            "full_actual_adjoint_wall_current_channel_exact": True}


def main():
    complexes = [complement_complex_case(N, generic) for N in range(2, 8) for generic in (False, True)]
    sources = [actual_spin_and_source(N) for N in range(2, 7)]
    actual_R = [actual_normal_R_case(N) for N in (2, 3)]
    result = {"whole_memory_complexes": complexes,
              "actual_spin_and_original_source": sources,
              "actual_universal_R_first_normals": actual_R,
              "scope": "One complement Bockstein line and actual charged source residual; original coherent and uniform sources remain distinct."}
    target = Path(__file__).with_name("degree_elevation_complement_wall_results.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "whole_memory_complex_cases": len(complexes),
                      "actual_spin_source_cases": len(sources), "actual_R_cases": len(actual_R),
                      "results": str(target)}, indent=2))


if __name__ == "__main__":
    main()
