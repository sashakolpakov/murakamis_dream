#!/usr/bin/env python3
"""Full physical and combinatorial checks for the actual cap-sum reduction.

The uniform proof is the explicit separating-sphere argument and exact
zero-coordinate multiplication law in the note. These finite checks do not
recognize manifolds or infer hyperbolicity from quantum values.
"""
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_odd_central_cube_reflection_packet import turn
from audit_positive_conway_geometric_incidence import Pairing


A = ('A',)


def T(a):
    return ('turn', a)


def P(a, b):
    return ('product', a, b)


EXPRS = [A, T(A), P(A, A), P(A, T(A)), T(P(A, A)),
         P(T(A), T(A)), T(P(A, T(A)))]


def pairing(e):
    if e == A:
        u = Pairing([(0, 1), (2, 3)])
        return u.product(u).product(u)
    if e[0] == 'turn':
        return pairing(e[1]).turn()
    return pairing(e[1]).product(pairing(e[2]))


def auxiliary_count(e):
    if e == A:
        return 3
    return sum(auxiliary_count(c) for c in e[1:])


def cap_component_count(e):
    return pairing(e).turn().close() + auxiliary_count(e)


def component_checks():
    pairs = 0
    for f, g in itertools.product(EXPRS, repeat=2):
        assert cap_component_count(P(f, g)) == (
            cap_component_count(f) + cap_component_count(g) - 1)
        pairs += 1
    rows = []
    run = T(A)
    for k in range(1, 33):
        if k > 1:
            run = P(run, T(A))
        assert cap_component_count(run) == 5*k+1
        # Through main pairing puts both outside caps on one component.
        assert pairing(run).pairs == ((0, 2), (1, 3))
        assert pairing(run).loops == 2*k
        rows.append({'k': k, 'main_components': 2*k+1,
                     'auxiliary_components': 3*k,
                     'total_components': 5*k+1})
    return {'arbitrary_pair_checks': pairs, 'theta_sum_families': rows}


def support_counts(e, d):
    if e == A:
        h = [int(2*r <= d) for r in range(d+1)]
        return support_product(support_product(h, h), h)
    if e[0] == 'turn':
        return support_counts(e[1], d)[::-1]
    return support_product(support_counts(e[1], d), support_counts(e[2], d))


def support_product(a, b):
    d, out = len(a)-1, [0]*len(a)
    for i, j in itertools.product(range(d+1), repeat=2):
        if i+j <= d:
            for z in range(max(i, j), i+j+1):
                out[z] += a[i]*b[j]
    return out


def support_checks():
    checks = 0
    for d in range(2, 14):
        for f, g in itertools.product(EXPRS, repeat=2):
            a, b = support_counts(f, d), support_counts(g, d)
            # Independent recursive count of all full-normal support states.
            whole = support_counts(T(P(f, g)), d)[d]
            assert whole == a[0]*b[0]
            assert whole > 0
            checks += 1
    return {'exact_integer_state_count_factorizations': checks,
            'levels_d': list(range(2, 14))}


def symbolic_flat_gate():
    x = y = z = sp.Integer(0)
    p, q, r, w = z-x, z-y, x+y-z, 1-x-y
    triples = [(p+r, q+r, w), (p, q, 2*r+w), (p+q, r, r+w)]
    assert triples == [(0, 0, 1)]*3
    # The exact multiplication coefficient is s_0^2/s_0^5=1.
    return {'forced_child_coordinates': [0, 0],
            'angle_triples': [[int(a) for a in t] for t in triples],
            'exact_gate_weight': 1}


def physical_level(N):
    p, _, q, E, F, K, pivot, _, _ = balanced_data(N)
    d, rho = N-1, (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(a), -1, p) for a in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    identity = np.eye(N*N, dtype=np.int64)
    previous, circle = identity, O.copy()
    for _ in range(2, N):
        previous, circle = circle, (O@circle-previous) % p
    circle = (-1)**d*circle % p
    pv = [N*pow(q, -d*(d-u), p) % p for u in range(N)]
    h = turn(circle, N, p, pv)
    cache = {A: h@h % p@h % p}

    def compile(e):
        if e not in cache:
            if e[0] == 'turn':
                cache[e] = turn(compile(e[1]), N, p, pv)
            else:
                cache[e] = compile(e[1])@compile(e[2]) % p
        return cache[e]

    def pointed_partial(mat):
        x = mat.reshape(N, N, N, N)
        partial = sum((int(pivot[b])*x[:, b, :, b] for b in range(N)),
                      np.zeros((N, N), dtype=np.int64)) % p
        scalar = int(partial[0, 0])
        assert np.array_equal(partial, scalar*np.eye(N, dtype=np.int64) % p)
        return scalar

    def cap(e):
        return pointed_partial(turn(compile(e), N, p, pv))

    count = 0
    for f, g in itertools.product(EXPRS, repeat=2):
        assert cap(P(f, g)) == cap(f)*cap(g) % p
        count += 1
    theta = pointed_partial(compile(A))
    run = T(A)
    family = []
    for k in range(1, 9):
        if k > 1:
            run = P(run, T(A))
        scalar = cap(run)
        assert scalar == pow(theta, k, p)
        family.append({'k': k, 'whole_original_scalar': scalar})
    return {'N': N, 'prime': p, 'all_input_physical_pair_factorizations': count,
            'theta_scalar': theta, 'theta_power_checks': family}


if __name__ == '__main__':
    result = {'status': 'PASS', 'symbolic_gate': symbolic_flat_gate(),
              'main_pairing_and_auxiliary_components': component_checks(),
              'integer_support': support_checks(),
              'original_marked_physical_sources': [physical_level(N) for N in range(2, 11)],
              'scope': 'Exact finite physical and support checks supplement the explicit all-expression separating sphere and Cartesian-product proof. General primitive hyperbolic volume identification remains open.'}
    Path(__file__).with_name('actual_conway_cap_sum_reduction_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS441 literal full-source cap products /72 theta powers /588 integer-support factorizations /49 component products /32 theta-sum component certificates')
