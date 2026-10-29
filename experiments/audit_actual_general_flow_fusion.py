#!/usr/bin/env python3
"""Arbitrary-exterior reproducing kernels and exact balanced graph star fusion."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import (
    setup, charged_data, charged_coefficient, graph_blocks, exact_cyclotomic_coefficient)
from audit_actual_signed_overbridge_unwinding import inv, polynomial, qbinom
from audit_actual_two_cut_ports import partial, word_matrix


def reproducing_checks():
    rows = []
    for N in range(2, 11):
        H = HardyNetwork(N, 1)
        p, d, Q = H.p, N-1, H.Q
        count = 0
        for a in (2, 5):
            # Product coefficients of B_d(X,Y;a) against the exact sum.
            coefficients = polynomial(H, a, d)
            assert all(coefficients[j] == pow(a*inv(Q, p) % p, j, p) for j in range(N))
            s = a*inv(Q, p) % p
            for power_x in range(2*N+1):
                for power_y in range(N+2):
                    left = (coefficients[power_x] if power_x < N and power_x+power_y < N else 0)
                    right = pow(s, power_x, p) if power_x+power_y < N else 0
                    assert left == right
                    # Reversed source contraction, with its scalar s^d.
                    reverse_left = coefficients[d-power_y] if power_y < N and power_x+power_y < N else 0
                    reverse_right = pow(s, d-power_y, p) if power_x+power_y < N else 0
                    assert reverse_left == reverse_right
                    count += 2
        for exponent in range(2*N):
            s = pow(H.q, exponent, p)
            actual = sum(pow(s, j, p) for j in range(N)) % p
            expected = N % p if not exponent else (0 if exponent % 2 == 0 else 2*inv(1-s, p) % p)
            assert actual == expected
        rows.append({'N': N, 'all_arbitrary_degree_monomial_kernel_checks': count,
                     'reverse_scalar_retained': True, 'all_saturated_cycle_characters': 2*N})
    return rows


def multiply(P, R, p):
    answer = {}
    for a, ca in P.items():
        for b, cb in R.items():
            e = tuple(x+y for x, y in zip(a, b))
            answer[e] = (answer.get(e, 0)+ca*cb) % p
    return {e: c for e, c in answer.items() if c}


def outer_block(H, i, j, L, a):
    P = {(0, 0, 0): 1}
    for r in range(L):
        u, v = [0]*3, [0]*3
        u[i], v[j] = 1, 1
        P = multiply(P, {tuple(u): 1, tuple(v): -a*pow(H.Q, r, H.p) % H.p}, H.p)
    return P


def star_coefficients(H, lengths, a):
    p, d, Q = H.p, H.N-1, H.Q
    P = {}
    for r1 in range(lengths[0]+1):
        for r2 in range(lengths[1]+1):
            r3 = d-r1-r2
            if not 0 <= r3 <= lengths[2]:
                continue
            rs = (r1, r2, r3)
            exponents = tuple(L-r for L, r in zip(lengths, rs))
            coefficient = 1
            for L, r, c in zip(lengths, rs, a):
                coefficient = (coefficient*pow(-c, r, p)*pow(Q, r*(r-1)//2, p)*qbinom(H, L, r)) % p
            P[exponents] = (P.get(exponents, 0)+coefficient) % p
    return {e: c for e, c in P.items() if c}


def triangle_data(H, ks, a):
    p, Q, d = H.p, H.Q, H.N-1
    k1, k2, k3 = ks
    scalar = (pow(-1, k1+k3, p)*pow(Q, k1*(k1-1)//2+k3*(k3-1)//2-k2, p)
              *qbinom(H, d-k2, k3)*pow(a[0], k2, p)*pow(a[1], k3, p)*pow(a[2], k1, p)) % p
    assert scalar
    edges = [(0, 1, k3, pow(Q, k2+1, p)*a[0]*inv(a[1], p) % p),
             (1, 2, k1, pow(Q, k3+1, p)*a[1]*inv(a[2], p) % p),
             (2, 0, k2, pow(Q, k1+1, p)*a[2]*inv(a[0], p) % p)]
    return scalar, edges


def star_triangle_checks():
    rows = []
    for N in range(2, 13):
        H = HardyNetwork(N, 1)
        p, d = H.p, N-1
        triples = 0
        for k1 in range(N):
            for k2 in range(N-k1):
                ks = (k1, k2, d-k1-k2)
                lengths = tuple(d-k for k in ks)
                for a in ((1, 1, 1), (2, 3, 5)):
                    lhs = star_coefficients(H, lengths, a)
                    scalar, edges = triangle_data(H, ks, a)
                    rhs = {(0, 0, 0): scalar}
                    for edge in edges:
                        rhs = multiply(rhs, outer_block(H, *edge), p)
                    assert lhs == rhs, (N, ks, a)
                    oldw = [-a[i]*pow(H.q, lengths[i]-1, p) % p for i in range(3)]
                    for i, j, L, root in edges:
                        neww = -root*pow(H.q, L-1, p) % p
                        assert neww == oldw[i]*inv(oldw[j], p) % p
                    triples += 1
        rows.append({'N': N, 'all_balanced_generic_coefficient_star_triangles': triples,
                     'full_polynomial_coefficients_compared': True,
                     'exact_nonzero_scalar_and_connection_ratios': True})
    return rows


def normalized_graph(H, G):
    p, q = H.p, H.q
    scalar = 1
    edges = []
    for i, block in enumerate(G['blocks']):
        scalar = scalar*pow(q, block['alpha_exp']*block['length'], p) % p
        edges.append({'u': block['tail'], 'v': block['head'], 'L': block['length'],
                      'a': pow(q, block['beta_exp']-block['alpha_exp'], p),
                      'closure': block['closure'], 'id': i})
    return scalar, edges, set(range(G['anchor_count']))


def graph_coefficient(H, edges, nodes):
    p, d = H.p, H.N-1
    order = {a: i for i, a in enumerate(sorted(nodes))}
    forms = []
    for e in edges:
        for r in range(e['L']):
            form = {order[e['u']]: 1}
            b = order[e['v']]
            form[b] = (form.get(b, 0)-e['a']*pow(H.Q, r, p)) % p
            forms.append({a: c for a, c in form.items() if c})
    return charged_coefficient(forms, len(nodes), d, p)


def contract_edge(H, edges, nodes, target_id):
    """Normalized arbitrary-valency fullblock contraction, eliminating tail."""
    p, Q = H.p, H.Q
    selected = next(e for e in edges if e['id'] == target_id)
    assert selected['L'] == H.N-1
    u, v = selected['u'], selected['v']
    assert u != v
    s = selected['a']*inv(Q, p) % p
    scalar, answer = 1, []
    for edge in edges:
        if edge['id'] == target_id:
            continue
        edge = edge.copy()
        if edge['u'] == u:
            edge['u'] = v
            edge['a'] = edge['a']*inv(s, p) % p
            scalar = scalar*pow(s, edge['L'], p) % p
        if edge['v'] == u:
            edge['v'] = v
            edge['a'] = edge['a']*s % p
        answer.append(edge)
    return scalar, answer, nodes-{u}


def balanced_star_vertex(H, edges, nodes, nondegenerate=False):
    d = H.N-1
    for v in sorted(nodes):
        incident = [e for e in edges if e['u'] == v or e['v'] == v]
        if len(incident) != 3 or any(e['u'] == e['v'] for e in incident):
            continue
        if sum(e['L'] for e in incident) != 2*d:
            continue
        if nondegenerate and (any(e['L'] == d for e in incident)
                              or len({e['u'] if e['v'] == v else e['v'] for e in incident}) != 3):
            continue
        return v
    return None


def star_move(H, edges, nodes, center):
    p, d, Q = H.p, H.N-1, H.Q
    incident = [e for e in edges if e['u'] == center or e['v'] == center]
    assert len(incident) == 3 and all(e['u'] != e['v'] for e in incident)
    assert sum(e['L'] for e in incident) == 2*d
    outer, roots, lengths, scalar = [], [], [], 1
    for e in incident:
        lengths.append(e['L'])
        if e['v'] == center:
            outer.append(e['u'])
            roots.append(e['a'])
        else:
            outer.append(e['v'])
            roots.append(inv(e['a'], p)*pow(Q, 1-e['L'], p) % p)
            scalar = scalar*pow(-e['a'], e['L'], p)*pow(Q, e['L']*(e['L']-1)//2, p) % p
    ks = [d-L for L in lengths]
    pref, new_edges = triangle_data(H, ks, roots)
    scalar = scalar*pref % p
    removed = {e['id'] for e in incident}
    answer = [e.copy() for e in edges if e['id'] not in removed]
    counter = min([e['id'] for e in edges]+[0])-1
    for i, j, L, a in new_edges:
        if L:
            answer.append({'u': outer[i], 'v': outer[j], 'L': L, 'a': a,
                           'id': counter, 'closure': False})
            counter -= 1
    return scalar, answer, nodes-{center}, ks


def original_nondegenerate_inverse_star():
    """An actual nonzero source sector with a genuine positive-length inverse move."""
    H = HardyNetwork(4, 1)
    p, Q, d = H.p, H.Q, H.N-1
    word, clocks = [1, -2, 1, -2], (0, 1, 1, 2)
    S = setup(H, 3, word)
    G = graph_blocks(H, S, clocks)
    scalar, edges, nodes = normalized_graph(H, G)
    coefficient = scalar*graph_coefficient(H, edges, nodes) % p
    exact = exact_cyclotomic_coefficient(G)
    assert exact == [-4, 0, 4]  # 4(q^2-1), certified nonzero over Q(q).
    chosen = [next(e for e, b in zip(edges, G['blocks']) if b['event'] == event and b['kind'] == kind)
              for event, kind in ((1, 'output'), (2, 'output'), (3, 'input'))]
    A, B, C = chosen[0]['u'], chosen[0]['v'], chosen[1]['v']
    assert (chosen[1]['u'], chosen[2]['u'], chosen[2]['v']) == (B, A, C)
    # Reverse the closing diagonal A->C to C->A, retaining its exact scalar.
    last = chosen[2].copy()
    reverse = pow(-last['a'], last['L'], p)*pow(Q, last['L']*(last['L']-1)//2, p) % p
    last['u'], last['v'] = C, A
    last['a'] = inv(last['a'], p)*pow(Q, 1-last['L'], p) % p
    triangle = [chosen[0], chosen[1], last]
    k3, k1, k2 = [e['L'] for e in triangle]
    assert k1 == k2 == k3 == 1 and k1+k2+k3 == d
    assert np.prod([e['a'] for e in triangle], dtype=object) % p == Q*Q % p
    a1 = 1
    a2 = pow(Q, k2+1, p)*inv(triangle[0]['a'], p) % p
    a3 = pow(Q, k3+1, p)*a2*inv(triangle[1]['a'], p) % p
    pref, reconstructed = triangle_data(H, (k1, k2, k3), (a1, a2, a3))
    assert [e[3] for e in reconstructed] == [e['a'] for e in triangle]
    removed = {e['id'] for e in chosen}
    replacement = [e.copy() for e in edges if e['id'] not in removed]
    center = max(nodes)+1
    for index, (outer, a, k) in enumerate(zip((A, B, C), (a1, a2, a3), (k1, k2, k3))):
        replacement.append({'u': outer, 'v': center, 'L': d-k,
                            'a': a, 'id': -index-1, 'closure': False})
    moved_coefficient = (scalar*reverse*inv(pref, p)
                         *graph_coefficient(H, replacement, nodes | {center})) % p
    assert moved_coefficient == coefficient and coefficient != 0
    return {'N': 4, 'word': word, 'original_clocks': clocks,
            'exact_original_source_coefficient': '4(q^2-1)',
            'triangle_lengths': [k3, k1, k2],
            'new_balanced_star_lengths': [d-k1, d-k2, d-k3],
            'all_new_lengths_positive': True,
            'original_exterior_and_inverse_scalar_retained': True}


def one_cycle_permutation(width, word):
    labels = list(range(width))
    for letter in word:
        i = abs(letter)-1
        labels[i], labels[i+1] = labels[i+1], labels[i]
    visited = set()
    i = 0
    while i not in visited:
        visited.add(i)
        i = labels[i]
    return len(visited) == width


def original_closure_case(N, width, word):
    assert one_cycle_permutation(width, word)
    H = HardyNetwork(N, 1)
    p, d = H.p, N-1
    S = setup(H, width, word)
    k, B = len(S['events']), len(S['paths'])
    total, states, moves, stars = 0, 0, 0, 0
    for clocks in itertools.product(range(N), repeat=len(word)):
        if any(any(clocks[a] < clocks[b] for a, b in zip(path, path[1:])) for path in S['paths']):
            continue
        forms, weight, _, _ = charged_data(H, S, clocks)
        old = charged_coefficient(forms, k, d, p)
        scalar, edges, nodes = normalized_graph(H, graph_blocks(H, S, clocks))
        ids = [edge['id'] for edge in edges if edge['closure']]
        assert len(ids) == width
        for target in ids:
            factor, edges, nodes = contract_edge(H, edges, nodes, target)
            scalar = scalar*factor % p
            moves += 1
        assert len(nodes) == B and not any(edge['closure'] for edge in edges)
        new = scalar*graph_coefficient(H, edges, nodes) % p
        assert new == old, (N, word, clocks, old, new)
        center = balanced_star_vertex(H, edges, nodes)
        if center is not None:
            factor, moved, remaining, _ = star_move(H, edges, nodes, center)
            after_star = scalar*factor*graph_coefficient(H, moved, remaining) % p
            assert after_star == old
            new = after_star
            stars += 1
        total = (total+weight*new) % p
        states += 1
    core = total*inv(N, p) % p
    W = word_matrix(word, H.plus, H.minus, width, N, p)
    cut = partial(W, H.pivot, width, N, p)
    expected = int(cut.sum())*inv(N, p) % p
    assert core == expected
    external = H.dimension*pow(H.twist, -sum(1 if j > 0 else -1 for j in word), p) % p
    return {'N': N, 'width': width, 'word': word, 'clock_sectors': states,
            'arbitrary_valency_original_closure_contractions': moves,
            'remaining_overbridge_anchors': B,
            'original_boundary_adapters_removed': width,
            'actual_exterior_balanced_star_insertions_checked': stars,
            'actual_core_period': core, 'actual_normalized_period': core*external % p,
            'all_original_pivot_substitutions_and_scalars_retained': True}


def main():
    whole = []
    for N in (2, 3):
        for width, word in [(3, [1, -2, 1, -2]),
                            (3, [1, 1, 1, 2, -1, 2]),
                            (3, [1, -2, 1, 1, -2, -2]),
                            (4, [1, 2, -1, 3, 2])]:
            whole.append(original_closure_case(N, width, word))
    results = {'status': 'PASS', 'arbitrary_exterior_fullblock_kernel': reproducing_checks(),
               'balanced_star_triangle_polynomial_identities': star_triangle_checks(),
               'whole_original_closure_removal': whole,
               'nonzero_original_source_nondegenerate_inverse_star': original_nondegenerate_inverse_star(),
               'scope': ('Exact original socle-source fusion and boundary gluing. '
                         'No assertion that all graph stars balance, no unretained scalar '
                         'and no general volume/noncancellation conclusion.')}
    Path(__file__).with_name('actual_general_flow_fusion_results.json').write_text(json.dumps(results, indent=2)+'\n')
    print('PASS nine arbitrary-exterior kernel families, eleven all-triple star-triangle '
          'families, eight whole original closure-removal sources')


if __name__ == '__main__':
    main()
