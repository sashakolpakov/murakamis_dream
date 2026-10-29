#!/usr/bin/env python3
"""Source-exact articulation factors and constructive blockwise minimax bound."""

import cmath
import itertools
import json
import math
from pathlib import Path

import networkx as nx
import numpy as np

from audit_actual_anchor_sublevel_radial_transport import cores_from_actual


def coefficient(q, factors):
    vertices = sorted(q)
    index = {v: j for j, v in enumerate(vertices)}
    target = tuple(q[v] for v in vertices)
    terms = {(0,)*len(vertices): 1.+0j}
    for u, v, a, b in factors:
        out = {}
        for powers, value in terms.items():
            for vertex, scalar in ((u, a), (v, -b)):
                j = index[vertex]
                if powers[j] < target[j]:
                    tt = powers[:j]+(powers[j]+1,)+powers[j+1:]
                    out[tt] = out.get(tt, 0)+value*scalar
        terms = out
    return terms.get(target, 0j)


def strict(q, factors):
    vertices = sorted(q)
    assert sum(q.values()) == len(factors)
    for mask in range(1, 2**len(vertices)-1):
        I = {v for j, v in enumerate(vertices) if mask >> j & 1}
        internal = sum(u in I and v in I for u, v, _, _ in factors)
        C = sum((u in I) != (v in I) for u, v, _, _ in factors)
        e = sum(q[i] for i in I)-internal
        assert 1 <= e <= C-1


def split(q, factors):
    G = nx.Graph()
    G.add_nodes_from(q)
    G.add_edges_from((u, v) for u, v, _, _ in factors)
    articulations = sorted(nx.articulation_points(G))
    strict(q, factors)
    if not articulations:
        return [(q, factors)]
    v = articulations[0]
    G.remove_node(v)
    blocks, articulation_charge = [], 0
    for C in nx.connected_components(G):
        V = set(C) | {v}
        FF = [F for F in factors if F[0] in V and F[1] in V]
        qq = {u: q[u] for u in C}
        qq[v] = len(FF)-sum(qq.values())
        articulation_charge += qq[v]
        strict(qq, FF)
        blocks.extend(split(qq, FF))
    assert articulation_charge == q[v]
    return blocks


def is_balanced(q, factors):
    S = {u: 0 for u in q}
    for u, v, _, _ in factors:
        S[u] += 1
        S[v] += 1
    return all(S[u] == 2*q[u] for u in q)


def univariate_data(q, factors):
    u, v = sorted(q)
    roots, gamma = [], 1.+0j
    for i, j, a, b in factors:
        if (i, j) == (u, v):
            gamma *= a
            roots.append(b/a)
        else:
            assert (i, j) == (v, u)
            gamma *= -b
            roots.append(a/b)
    P = gamma*np.poly(roots)
    m, charge = len(roots), q[u]
    derivative = np.polysub(np.polymul([1, 0], np.polyder(P)), charge*P)
    critical = [z for z in np.roots(derivative) if abs(np.polyval(P, z)) > 1e-7]
    values = [np.polyval(P, z)/z**charge for z in critical]
    assert critical
    Mcrit = max(map(abs, values))
    bound = 4*m*m*math.log(m+1)*Mcrit
    assert abs(coefficient(q, factors)) <= bound*(1+1e-10)
    return {'degree': m, 'charge': charge, 'Mcrit': Mcrit,
            'normalized_mass_bound': 4*m*m*math.log(m+1),
            'one_critical_point': critical[0]}


def one_family(q, factors, label):
    decomposition = split(q, factors)
    direct = coefficient(q, factors)
    component_values = [coefficient(qq, FF) for qq, FF in decomposition]
    product = math.prod(component_values)
    residual = abs(direct-product)
    assert residual <= 3e-7*max(1, abs(direct), abs(product))
    allowed = all(len(qq) == 2 or is_balanced(qq, FF)
                  for qq, FF in decomposition)
    row = {'label': label, 'anchors': len(q), 'factors': len(factors),
           'component_sizes': [len(qq) for qq, _ in decomposition],
           'component_charges': [list(qq.values()) for qq, _ in decomposition],
           'source_factorization_error': residual,
           'all_blocks_have_constructive_polynomial_mass': allowed,
           'selected_coefficient_abs': abs(direct)}
    if allowed:
        row['two_anchor_bounds'] = [
            {key: value for key, value in univariate_data(qq, FF).items()
             if key != 'one_critical_point'}
            for qq, FF in decomposition if len(qq) == 2]
    return row


def main():
    actual = []
    for N, word, clocks in (
            (3, [1, -2, 1, -2], [0, 0, 1, 2]),
            (4, [1, -2, 1, -2], [0, 1, 1, 2]),
            (5, [1, -2, 1, -2], [0, 2, 2, 3]),
            (3, [1, -2, 1, 1, -2, -2], [0, 1, 1, 1, 0, 1])):
        for j, (q, FF) in enumerate(cores_from_actual(N, 3, word, clocks)):
            actual.append(one_family(dict(enumerate(q)), FF,
                                     {'N': N, 'word': word, 'clocks': clocks, 'core': j}))
    # Arbitrary-width constructive mixed family: unbalanced parallel bundles
    # separated by balanced triangle blocks. The scalar remains nonzero.
    q = {0: 1, 1: 5, 2: 2, 3: 4, 4: 1}
    F = [(0, 1, 1., z) for z in (1., 1., 1j, -1.)]
    F += [(u, v, 1., 1.) for u, v in ((1, 2), (2, 3), (1, 3)) for _ in range(2)]
    F += [(3, 4, 1., z) for z in (1., 1j, -1j)]
    mixed = one_family(q, F, 'five-anchor unbalanced-bundle/balanced-triangle/bundle')
    assert mixed['all_blocks_have_constructive_polynomial_mass']
    assert mixed['selected_coefficient_abs'] > .1
    # Complete critical splitting: the balanced discriminant triangle has
    # maximum 27 at its equilateral unit point; append independent regular
    # critical points of both unbalanced bundles and verify the full gradient.
    blocks = split(q, F)
    assert sorted(map(lambda B: len(B[0]), blocks)) == [2, 2, 3]
    left = univariate_data(*next(B for B in blocks if set(B[0]) == {0, 1}))
    right = univariate_data(*next(B for B in blocks if set(B[0]) == {3, 4}))
    omega = cmath.exp(2j*math.pi/3)
    X = {1: omega, 2: omega**2, 3: 1.+0j}
    X[0] = left['one_critical_point']*X[1]
    X[4] = X[3]/right['one_critical_point']
    gradient = {v: -complex(charge) for v, charge in q.items()}
    value = 1.+0j
    for u, v, a, b in F:
        den = a*X[u]-b*X[v]
        value *= den
        gradient[u] += a*X[u]/den
        gradient[v] -= b*X[v]/den
    value /= math.prod(X[v]**q[v] for v in q)
    assert max(map(abs, gradient.values())) < 1e-7
    Mfull = left['Mcrit']*27*right['Mcrit']
    assert abs(value) <= Mfull*(1+1e-7)
    multiplier = left['normalized_mass_bound']*right['normalized_mass_bound']
    assert mixed['selected_coefficient_abs'] <= multiplier*Mfull
    mixed['full_critical_gradient_residual'] = max(map(abs, gradient.values()))
    mixed['exact_balanced_triangle_Mcrit'] = 27
    mixed['product_full_Mcrit'] = Mfull
    mixed['explicit_polynomial_mass_bound'] = multiplier
    # Wider all-balanced families have the source torus itself as a valid cycle.
    balanced = []
    for triangles in range(1, 5):
        FF, qq = [], {i: 0 for i in range(2*triangles+1)}
        for t in range(triangles):
            vertices = (2*t, 2*t+1, 2*t+2)
            for u, v in itertools.combinations(vertices, 2):
                FF.extend([(u, v, 1., 1.)]*2)
                qq[u] += 1
                qq[v] += 1
        row = one_family(qq, FF, f'{triangles} balanced triangle blocks')
        assert row['all_blocks_have_constructive_polynomial_mass']
        assert abs(row['selected_coefficient_abs']-6**triangles) < 1e-6
        balanced.append(row)
    data = {'status': 'PASS', 'actual_residual_source_cores': actual,
            'constructive_mixed_source': mixed, 'arbitrary_width_balanced_blocks': balanced,
            'scope': 'Blockwise original-source transport only; no general unbalanced biconnected-core mass estimate or full-clock knot bound.'}
    Path(__file__).with_name('actual_blockwise_sublevel_source_transport_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(f'PASS {len(actual)} actual articulation source cores, explicit mixed critical '
          'product and four wider balanced families; unbalanced biconnected scope retained')


if __name__ == '__main__':
    main()
