#!/usr/bin/env python3
"""Actual gain-arrangement flats, source orders and polynomial chart minors."""

import itertools
import json
from pathlib import Path
import random

import mpmath as mp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import graph_blocks, setup
from audit_actual_general_flow_fusion import normalized_graph
from audit_actual_forced_source_fusion import reduce_source


def actual_core(N, width, word, clocks):
    H = HardyNetwork(N, 1)
    S = setup(H, width, word)
    G = graph_blocks(H, S, clocks)
    scalar, edges, nodes = normalized_graph(H, G)
    factor, edges, charges, moves = reduce_source(H, edges, {v: N-1 for v in nodes})
    assert scalar and factor and edges and len(charges) >= 2
    order = {v: j for j, v in enumerate(sorted(charges))}
    lookup = {pow(H.q, j, H.p): j for j in range(2*N)}
    rows = []
    for number, edge in enumerate(edges):
        assert edge['u'] != edge['v'] and 0 < edge['L'] < N
        exponent = lookup[edge['a']]
        for r in range(edge['L']):
            rows.append((order[edge['u']], order[edge['v']],
                         (exponent+2*r) % (2*N), number))
    q = [charges[v] for v in sorted(charges)]
    assert sum(q) == len(rows)
    return H, rows, q, len(edges), moves


def classify(k, rows, constraints, modulus):
    neighbors = [[] for _ in range(k)]
    marked_zero = set()
    for item in constraints:
        if item < len(rows):
            u, v, exponent, _ = rows[item]
            neighbors[v].append((u, exponent))
            neighbors[u].append((v, -exponent))
        else:
            marked_zero.add(item-len(rows))
    potentials, components, zero = {}, [], set()
    for root in range(k):
        if root in potentials:
            continue
        potentials[root] = 0
        queue, component, bad = [root], [], False
        for v in queue:
            component.append(v)
            for u, step in neighbors[v]:
                value = (potentials[v]+step) % modulus
                if u not in potentials:
                    potentials[u] = value
                    queue.append(u)
                elif potentials[u] != value:
                    bad = True
        if bad or marked_zero.intersection(component):
            zero.update(component)
        else:
            components.append(component)
    index = {v: j for j, C in enumerate(components) for v in C}
    signature = (tuple(sorted(zero)),
                 tuple(tuple((v, potentials[v]) for v in C) for C in components))
    return zero, components, index, potentials, signature


def flat_check(H, rows, charges, blocks, constraints, rng):
    k, modulus = len(charges), 2*H.N
    Z, components, index, potentials, signature = classify(k, rows, constraints, modulus)
    internal, extra, per_block = 0, 0, {}
    containing = []
    for number, (u, v, exponent, block) in enumerate(rows):
        if u in Z and v in Z:
            internal += 1
            containing.append(number)
        elif u not in Z and v not in Z and index[u] == index[v] and (potentials[u]-potentials[v]-exponent) % modulus == 0:
            extra += 1
            per_block[block] = per_block.get(block, 0)+1
            containing.append(number)
    assert max(per_block.values(), default=0) <= 1 and extra <= blocks
    deficit = sum(charges[v] for v in Z)-internal
    residue = extra-deficit
    codimension = k-len(components)
    assert codimension == len(Z)+sum(len(C)-1 for C in components)
    if deficit > blocks:
        assert residue < 0
    if residue == 0 and codimension > len(Z):
        assert residue+codimension-len(Z)-1 >= 0
    if not Z and codimension:
        assert extra > 0 and residue > 0

    # Generic point and generic first normal derivative verify the
    # actual orders, not merely the dimension count.
    for _ in range(200):
        free = [rng.randrange(1, H.p) for C in components]
        point = [0 if v in Z else pow(H.q, potentials[v], H.p)*free[index[v]] % H.p
                 for v in range(k)]
        values = [(point[u]-pow(H.q, exponent, H.p)*point[v]) % H.p
                  for u, v, exponent, block in rows]
        if [j for j, value in enumerate(values) if not value] == containing:
            break
    else:
        raise AssertionError('failed generic flat point')
    for _ in range(200):
        normal = [rng.randrange(1, H.p) for v in range(k)]
        if all((normal[rows[j][0]]-pow(H.q, rows[j][2], H.p)*normal[rows[j][1]]) % H.p
               for j in containing):
            break
    else:
        raise AssertionError('failed generic normal direction')
    actual_numerator_order = sum(value == 0 for value in values)
    assert actual_numerator_order == internal+extra
    assert actual_numerator_order-sum(charges[v] for v in Z) == residue
    return signature, {'zero_coordinates': sorted(Z), 'codimension': codimension,
                       'coordinate_deficit': deficit, 'extra_matching_factors': extra,
                       'phase_residue': residue,
                       'source_form_order': residue+codimension-len(Z)-1,
                       'proper_projective_flat': 0 < codimension < k}


def determinant_mod(A, p):
    A = [[a % p for a in row] for row in A]
    answer = 1
    for j in range(len(A)):
        pivot = next((i for i in range(j, len(A)) if A[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            answer = -answer
        a = A[j][j]
        answer = answer*a % p
        for i in range(j+1, len(A)):
            ratio = A[i][j]*pow(a, -1, p) % p
            for col in range(j, len(A)):
                A[i][col] = (A[i][col]-ratio*A[j][col]) % p
    return answer % p


def minor_checks(H, rows, k, rng):
    field_rows, complex_rows = [], []
    for u, v, exponent, block in rows:
        field = [0]*k
        field[u], field[v] = 1, -pow(H.q, exponent, H.p) % H.p
        comp = [mp.mpc(0)]*k
        comp[u], comp[v] = 1, -mp.e**(mp.j*mp.pi*exponent/H.N)
        field_rows.append(field)
        complex_rows.append(comp)
    for v in range(k):
        field = [0]*k
        field[v] = 1
        field_rows.append(field)
        complex_rows.append(list(map(mp.mpc, field)))
    nonzero = 0

    def sparse_determinant(matrix):
        if not matrix:
            return mp.mpc(1)
        return mp.fsum(((-1)**j)*a*sparse_determinant(
            [row[:j]+row[j+1:] for row in matrix[1:]])
            for j, a in enumerate(matrix[0]) if a)

    for trial in range(180):
        s = 1+trial % k
        rr, cc = rng.sample(range(len(field_rows)), s), rng.sample(range(k), s)
        field = [[field_rows[i][j] for j in cc] for i in rr]
        exact = determinant_mod(field, H.p)
        value = sparse_determinant([[complex_rows[i][j] for j in cc] for i in rr])
        if exact:
            nonzero += 1
            assert abs(value)+mp.mpf('1e-65') >= (mp.mpf(2)/H.N)**s
            assert abs(value) <= mp.mpf(2)**s+mp.mpf('1e-65')
        else:
            assert abs(value) < mp.mpf('1e-65')
    return {'minors_checked': 180, 'nonzero_minors': nonzero,
            'root_of_unity_lower_bound': '(2/N)^s',
            'uniform_fixed_dimensional_polynomial_inverse': True}


def main():
    mp.mp.dps = 90
    rng = random.Random(294793)
    result = []
    families = ((5, 3, [1, -2, 1, -2], [0, 1, 2, 3]),
                (7, 3, [1, -2, 1, 1, -2, -2], [0, 3, 3, 3, 0, 3]),
                (5, 4, [1, -2, 3]*3, [0]+[2]*8))
    for number, (N, width, word, clocks) in enumerate(families):
        H, rows, charges, blocks, moves = actual_core(N, width, word, clocks)
        k = len(charges)
        all_flats = {}
        if number == 0:
            # Every flat is generated by at most k independent rows.
            choices = itertools.chain.from_iterable(itertools.combinations(range(len(rows)+k), s)
                                                    for s in range(k+1))
        else:
            choices = [rng.sample(range(len(rows)+k), rng.randrange(k+1)) for _ in range(220)]
        for constraints in choices:
            signature, row = flat_check(H, rows, charges, blocks, constraints, rng)
            all_flats[signature] = row
        resonant = [row for row in all_flats.values()
                    if row['proper_projective_flat'] and row['phase_residue'] == 0]
        assert all(row['coordinate_deficit'] <= blocks for row in resonant)
        result.append({'N': N, 'width': width, 'word': word, 'original_clocks': clocks,
                       'source_reduction_moves': moves, 'remaining_charges': charges,
                       'remaining_block_slots': blocks, 'linear_factor_count': len(rows),
                       'distinct_flats_checked': len(all_flats),
                       'all_flats_checked': number == 0,
                       'resonant_proper_flats': resonant,
                       'minor_checks': minor_checks(H, rows, k, rng)})
    Path(__file__).with_name('charged_arrangement_boundary_orders_results.json').write_text(
        json.dumps({'actual_source_gain_arrangements': result,
                    'scope': 'Exact boundary orders and linear chart conditioning; no global Morse/source-regulator theorem claimed.'}, indent=2)+'\n')
    print('PASS actual flat/zero-class orders, bounded block multiplicity, '
          'source-form pole orders and root-of-unity minor conditioning')


if __name__ == '__main__':
    main()
