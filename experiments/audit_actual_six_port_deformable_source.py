#!/usr/bin/env python3
"""Literal six-head source spans and finite generic Clebsch invariant frames."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import (
    inverse_mod, matrix_polynomial, apply_pair, rank_mod)


def generic_module(m, zeta, prime):
    Q = zeta*zeta % prime
    E, F = np.zeros((m+1, m+1), dtype=np.int64), np.zeros((m+1, m+1), dtype=np.int64)
    for a in range(1, m+1):
        E[a-1, a] = pow(zeta, -m-1, prime)*(1-pow(Q, m+1-a, prime)) % prime
    for a in range(m):
        F[a+1, a] = (1-pow(Q, a+1, prime)) % prime
    K = np.diag([pow(zeta, m, prime)*pow(Q, -a, prime) % prime for a in range(m+1)])
    return E, F, K


def generic_cup(m, zeta, prime, p0=1):
    Q, x = zeta*zeta % prime, pow(zeta, m, prime)
    fac = [1]
    for r in range(1, m+1):
        fac.append(fac[-1]*(1-pow(Q, r, prime)) % prime)
    result = np.zeros((m+1)**2, dtype=np.int64)
    for a in range(m+1):
        result[a*(m+1)+m-a] = (p0*pow(-x, a, prime)*pow(Q, -a*(a+1)//2, prime)
                         *fac[a]*fac[m-a]*pow(fac[m], -1, prime)) % prime
    return result


def clebsch(m, n, c, zeta, prime):
    assert (m+n-c) % 2 == 0 and abs(m-n) <= c <= m+n
    k = (m+n-c)//2
    Q = zeta*zeta % prime
    E1, F1, K1 = generic_module(m, zeta, prime)
    E2, F2, K2 = generic_module(n, zeta, prime)
    Epair = (np.kron(E1, K2)+np.kron(np.eye(m+1, dtype=np.int64), E2)) % prime
    K1i = np.diag([pow(int(v), -1, prime) for v in np.diag(K1)])
    Fpair = (np.kron(F1, np.eye(n+1, dtype=np.int64))+np.kron(K1i, F2)) % prime
    highest = np.zeros((m+1)*(n+1), dtype=np.int64)
    coeff = 1
    for r in range(k+1):
        highest[r*(n+1)+k-r] = coeff
        if r < k:
            coeff = (-coeff*int(E2[k-r-1, k-r])
                     *pow(int(E1[r, r+1])*int(K2[k-r-1, k-r-1]) % prime, -1, prime)) % prime
    assert not np.any(Epair@highest % prime)
    columns, power, fac = [], highest, 1
    for r in range(c+1):
        if r:
            fac = fac*(1-pow(Q, r, prime)) % prime
        columns.append(power*pow(fac, -1, prime) % prime)
        power = Fpair@power % prime
    frame = np.column_stack(columns)
    Ec, Fc, Kc = generic_module(c, zeta, prime)
    assert np.array_equal(Epair@frame % prime, frame@Ec % prime)
    assert np.array_equal(Fpair@frame % prime, frame@Fc % prime)
    assert np.array_equal(np.kron(K1, K2)@frame % prime, frame@Kc % prime)
    return frame


def generic_six_frame(N):
    prime, zeta, d = 1009, 4, N-1
    pair = [clebsch(d, d, 2*a, zeta, prime) for a in range(N)]
    columns, labels = [], []
    for a, b, c in itertools.product(range(N), repeat=3):
        if not abs(a-b) <= c <= a+b:
            continue
        vertex = np.kron(clebsch(2*a, 2*b, 2*c, zeta, prime),
                         np.eye(2*c+1, dtype=np.int64)) @ generic_cup(2*c, zeta, prime) % prime
        tensor = vertex.reshape(2*a+1, 2*b+1, 2*c+1)
        physical = np.einsum('ia,jb,kc,abc->ijk', pair[a], pair[b], pair[c], tensor,
                             optimize=True).reshape(-1) % prime
        columns.append(physical)
        labels.append((a, b, c))
    frame = np.column_stack(columns)
    assert len(labels) == (N**3+N)//2
    assert rank_mod(frame, prime) == len(labels)
    E, F, K = generic_module(d, zeta, prime)
    states = list(itertools.product(range(N), repeat=6))
    eout, fout = np.zeros_like(frame), np.zeros_like(frame)
    for j, state in enumerate(states):
        if np.any(frame[j]):
            assert sum(state) == 3*d
        for slot, a in enumerate(state):
            if a:
                dest = list(state); dest[slot] -= 1
                row = sum(dest[t]*N**(5-t) for t in range(6))
                coef = int(E[a-1, a])
                for t in range(slot+1, 6):
                    coef = coef*int(K[state[t], state[t]]) % prime
                eout[row] = (eout[row]+coef*frame[j]) % prime
            if a < d:
                dest = list(state); dest[slot] += 1
                row = sum(dest[t]*N**(5-t) for t in range(6))
                coef = int(F[a+1, a])
                for t in range(slot):
                    coef = coef*pow(int(K[state[t], state[t]]), -1, prime) % prime
                fout[row] = (fout[row]+coef*frame[j]) % prime
    assert not np.any(eout) and not np.any(fout)
    return {'N': N, 'generic_six_port_triangular_frame_rank': len(labels),
            'all_literal_E_F_H_invariant_columns': True}


def root_source(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Ec = rho*rho*E % prime
    states = [v for v in itertools.product(range(N), repeat=4) if sum(v) == 2*d]
    indices = [sum(v[j]*N**(3-j) for j in range(4)) for v in states]
    dim = len(states)
    octa = {(d-b-c, d-a-c, d-a-b) for a, b, c, e in states}
    expected_octa = {v for v in itertools.product(range(-d, d+1), repeat=3)
                     if sum(map(abs, v)) <= d and (sum(v)-d) % 2 == 0}
    assert octa == expected_octa and dim == (2*N**3+N)//3
    seed = np.zeros((N**4, dim), dtype=np.int64)
    seed[indices, np.arange(dim)] = 1
    pair_ids = [a*N+d-a for a in range(N)]
    E2, F2, K2 = coproduct(Ec, F, K, 2, N, prime)
    Ki2 = np.diag([pow(int(z), -1, prime) for z in np.diag(K2)])
    O2 = (F2@E2+q*K2+pow(q, -1, prime)*Ki2) % prime
    A = O2[np.ix_(pair_ids, pair_ids)]
    R = Rp[np.ix_(pair_ids, pair_ids)]
    vector = np.eye(N, dtype=np.int64)[:, d]
    columns = []
    for _ in range(N):
        columns.append(vector); vector = A@vector % prime
    kappa = int(Rp[0, 0])
    coeffs = inverse_mod(np.column_stack(columns), prime)@R[:, d]*pow(kappa, -1, prime) % prime
    E3, _, _ = coproduct(Ec, F, K, 3, N, prime)
    E4, F4, K4 = coproduct(Ec, F, K, 4, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(K)])
    boundary = (q*x*np.kron(np.eye(N**3, dtype=np.int64), K)
             +pow(q, -1, prime)*pow(x, -1, prime)*np.kron(np.eye(N**3, dtype=np.int64), Ki)
             -x*np.kron(E3, F@K)) % prime
    boundary = boundary[np.ix_(indices, indices)]
    K4i = np.diag([pow(int(z), -1, prime) for z in np.diag(K4)])
    total = (F4@E4+q*K4+pow(q, -1, prime)*K4i) % prime
    total = total[np.ix_(indices, indices)]
    plus = [apply_pair(Rp, seed, slot, 4, N, prime)[indices] for slot in range(3)]
    plus += [kappa*matrix_polynomial(coeffs, boundary, prime) % prime,
             kappa*matrix_polynomial(coeffs, total, prime) % prime]
    minus = [inverse_mod(matrix, prime) for matrix in plus]
    cup = np.zeros(N*N, dtype=np.int64)
    ordinary, marked = np.zeros(N*N, dtype=np.int64), np.zeros(N*N, dtype=np.int64)
    for a in range(N):
        cup[a*N+d-a] = N*pow(x, a-d, prime) % prime
        ordinary[a*N+d-a] = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
        for b in range(N):
            marked[a*N+b] = pow(x, b, prime)*pow(N, -2, prime) % prime
    generic_at_root = generic_cup(d, q, prime, N*pow(x, -d, prime) % prime)
    assert np.array_equal(generic_at_root, cup)
    initial = np.kron(cup, cup)[indices]
    lam = np.kron(ordinary, ordinary)[indices]
    basis, pivots, queue = [], [], []

    def add(v):
        v = v.copy() % prime
        for row, pivot_col in zip(basis, pivots):
            if v[pivot_col]:
                v = (v-int(v[pivot_col])*row) % prime
        nonzero = np.flatnonzero(v)
        if not len(nonzero):
            return
        pivot_col = int(nonzero[0])
        v = v*pow(int(v[pivot_col]), -1, prime) % prime
        basis.append(v); pivots.append(pivot_col); queue.append(v)

    add(initial)
    j = 0
    while j < len(queue):
        v = queue[j]; j += 1
        for matrix in plus:
            add(matrix@v % prime)
    assert len(basis) == (N**3+N)//2
    physical = np.kron(np.kron(cup, cup), cup)[:, None]
    reduced = initial.copy()
    for letter in (1, -4, 2, 5, -3, 4):
        physical = apply_pair(Rp if letter > 0 else Rm, physical, abs(letter)-1, 6, N, prime)
        reduced = (plus if letter > 0 else minus)[abs(letter)-1]@reduced % prime
    full_row = np.kron(np.kron(ordinary, ordinary), marked)
    assert int(full_row@physical[:, 0]) % prime == int(lam@reduced) % prime
    return {'N': N, 'root_invariant_dimension': dim,
            'actual_original_source_cyclic_rank': len(basis),
            'proved_generic_source_rank': (N**3+N)//2,
            'extra_root_invariant_dimension': (N**3-N)//6,
            'literal_marked_word_and_regular_generic_cup': True,
            'octahedral_parity_lattice_exact': True}


if __name__ == '__main__':
    generic = [generic_six_frame(N) for N in range(2, 5)]
    roots = [root_source(N) for N in range(2, 6)]
    result = {'status': 'PASS', 'generic_complete_triangular_Clebsch_frames': generic,
              'root_original_source_families': roots,
              'scope': 'Source saturation/rank and exact six-port coordinates; cyclic-rank equality sampled only, no large-N kernel bound asserted.'}
    Path(__file__).with_name('actual_six_port_deformable_source_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(generic)} generic six-port frames; {len(roots)} complete literal root source/cyclic families')
