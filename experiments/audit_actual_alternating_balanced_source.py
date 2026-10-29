#!/usr/bin/env python3
"""Actual alternating incidence and annihilation of balanced figure-eight clocks."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import setup, graph_blocks, exact_cyclotomic_coefficient
from audit_actual_general_flow_fusion import normalized_graph, contract_edge, graph_coefficient
from audit_whole_fermat_toric_residue_and_wire_source import frame


def physical_successor(S):
    incoming = {}
    for j, R in enumerate(S['records']):
        for p in (0, 1):
            incoming[R['invars'][p]] = (j, p == R['over_in'])
    closure = dict(zip(S['ov'], S['iv']))
    successors, counts = {}, {}
    for j, R in enumerate(S['records']):
        v, unders = R['outvars'][R['over_out']], 0
        for _ in range(len(S['records'])+len(closure)+2):
            if v in incoming:
                k, over = incoming[v]
                if over:
                    successors[j], counts[j] = k, unders
                    break
                underR = S['records'][k]
                v = underR['outvars'][1-underR['over_out']]
                unders += 1
            else:
                v = closure[v]
        else:
            raise AssertionError('Over encounter did not return on its physical component')
    return successors, counts


def close_graph(H, S, clocks):
    G = graph_blocks(H, S, clocks)
    scalar, edges, nodes = normalized_graph(H, G)
    representatives = {i: i for i in nodes}
    for target in [e['id'] for e in edges if e['closure']]:
        selected = next(e for e in edges if e['id'] == target)
        u, v = selected['u'], selected['v']
        factor, edges, nodes = contract_edge(H, edges, nodes, target)
        scalar = scalar*factor % H.p
        representatives = {a: (v if rep == u else rep) for a, rep in representatives.items()}
    return G, scalar, edges, nodes, representatives


def alternating_incidence():
    words = [(2, [1, 1, 1]), (3, [1, -2, 1, -2]),
             (3, [1, -2, 1, 1, -2, -2]),
             (3, [1, -2]*4), (4, [1, -2, 3]*3)]
    rows = []
    for N in (2, 3, 5):
        H = HardyNetwork(N, 1)
        for width, word in words:
            S = setup(H, width, word)
            nxt, undercounts = physical_successor(S)
            assert set(undercounts.values()) == {1}
            assert all(len(path) == 1 for path in S['paths'])
            orbit, j = set(), 0
            while j not in orbit:
                orbit.add(j)
                j = nxt[j]
            assert len(orbit) == len(word)
            count = 0
            for clocks in [(0,)*len(word), (N-1,)*len(word),
                           tuple((2*j+1) % N for j in range(len(word))),
                           tuple((j*j+2) % N for j in range(len(word)))]:
                _, _, edges, nodes, reps = close_graph(H, S, clocks)
                incidence = {v: 0 for v in nodes}
                for edge in edges:
                    incidence[edge['u']] += edge['L']
                    incidence[edge['v']] += edge['L']
                for j in range(len(word)):
                    assert incidence[reps[j]] == 2*(N-1)+clocks[j]-clocks[nxt[j]]
                count += 1
            rows.append({'N': N, 'width': width, 'word': word,
                         'one_under_between_each_physical_over_pair': True,
                         'signed_actual_incidence_assignments': count,
                         'balanced_clock_space_is_one_dimensional': True})
    return rows


def cyclic_local_support():
    rows = []
    for N in range(2, 10):
        H = HardyNetwork(N, 1)
        p = H.p
        _, G0, I0 = frame(H, 1)
        _, G1, I1 = frame(H, H.x)
        G, Gi = np.kron(G0, G1) % p, np.kron(I0, I1) % p
        checks = 0
        for sign, R in ((1, H.plus), (-1, H.minus)):
            M = (G@R % p)@Gi % p
            for a, b, c, e in itertools.product(range(N), repeat=4):
                u, v, t, z = (b-a-1) % N, (a-c) % N, (c-e) % N, (e-b) % N
                allowed = u+v+t+z == N-1
                assert bool(M[c*N+e, a*N+b]) == allowed
                if allowed:
                    h = (b-c-1) % N if sign > 0 else (e-a-1) % N
                    assert h == (u+v if sign > 0 else u+z)
                checks += 1
        rows.append({'N': N, 'both_original_signs_fixed_cyclic_grid_support_checks': checks,
                     'actual_clock_dictionary': True})
    return rows


def figure_eight_blocks(N, hs):
    d = N-1
    u, v, w, t = hs
    # (tail,head,length,starting Q exponent), vertices(A,B,C,D).
    return [(1, 2, d-u, 0), (2, 0, u, 1),
            (3, 0, d-v, v+1), (0, 1, v, -v+w+1),
            (2, 1, d-w, u+w+2), (1, 3, w, -w-t-1),
            (0, 3, d-t, -v), (3, 2, t, 0)]


def check_actual_block_table(H, S, hs):
    G, scalar, edges, nodes, _ = close_graph(H, S, hs)
    actual = {}
    for edge in edges:
        block = G['blocks'][edge['id']]
        actual[block['event'], block['kind']] = edge
    names = {0: 0, 4: 1, 5: 2, 6: 3}
    for j, ((u, v, L, start), key) in enumerate(zip(figure_eight_blocks(H.N, hs),
            [(0,'input'),(0,'output'),(1,'input'),(1,'output'),
             (2,'input'),(2,'output'),(3,'input'),(3,'output')])):
        if not L:
            assert key not in actual
            continue
        edge = actual[key]
        assert (names[edge['u']], names[edge['v']], edge['L']) == (u, v, L)
        scale_u = pow(H.x, -1, H.p) if u in (1, 3) else 1
        scale_v = pow(H.x, -1, H.p) if v in (1, 3) else 1
        root = edge['a']*scale_v*pow(scale_u, -1, H.p) % H.p
        assert root == pow(H.Q, start, H.p)
    return scalar, edges, nodes


def grid_support_checks():
    rows = []
    for N in range(2, 7):
        H = HardyNetwork(N, 1)
        S = setup(H, 3, [1, -2, 1, -2])
        sectors, colorings, diagonal = 0, 0, 0
        nxt, _ = physical_successor(S)
        for hs in itertools.product(range(N), repeat=4):
            table = figure_eight_blocks(N, hs)
            found = 0
            for tail in itertools.product(range(N), repeat=3):
                colors = (0,)+tail
                if all((colors[i]-colors[j]-start) % N >= L for i,j,L,start in table):
                    found += 1
            if found:
                assert hs[0] == 0 and hs[1]+hs[3] >= N-1
                defects = [hs[j]-hs[nxt[j]] for j in range(4)]
                assert sum(abs(x) for x in defects) >= N-1
                assert 2*max(abs(x) for x in defects) >= N-1
                sectors += 1
                colorings += found
            if len(set(hs)) == 1:
                assert not found
                diagonal += 1
        # Symbolic affine table is checked directly on sufficiently many actual assignments.
        for hs in [(0,)*4, (N-1,)*4, tuple(j % N for j in range(4))]:
            check_actual_block_table(H, S, hs)
        rows.append({'N': N, 'all_clock_assignments_examined': N**4,
                     'nonempty_regular_grid_support_sectors': sectors,
                     'source_support_grid_colorings_mod_common_scale': colorings,
                     'all_diagonal_sectors_pointwise_zero': diagonal,
                     'cut_face_and_macroscopic_defect_necessary_on_all_support': True})
    return rows


def diagonal_exact_coefficients():
    rows = []
    for N in range(2, 15):
        H = HardyNetwork(N, 1)
        S = setup(H, 3, [1, -2, 1, -2])
        for h in range(N):
            scalar, edges, nodes = check_actual_block_table(H, S, (h,)*4)
            assert scalar*graph_coefficient(H, edges, nodes) % H.p == 0
            if N <= 5:
                assert exact_cyclotomic_coefficient(graph_blocks(H, S, (h,)*4)) == []
        rows.append({'N': N, 'all_actual_diagonal_coefficients_zero': N,
                     'exact_cyclotomic_zero_independent_of_prime': N <= 5})
    return rows


def main():
    result = {'status': 'PASS', 'general_signed_alternating_incidence': alternating_incidence(),
              'original_cyclic_support_and_clock_dictionary': cyclic_local_support(),
              'full_actual_figure_eight_regular_grid_support': grid_support_checks(),
              'actual_balanced_diagonal_zero_coefficients': diagonal_exact_coefficients(),
              'scope': ('All-N support/incidence proofs in note; actual balanced figure-eight source is zero. '
                        'Sublinear individual anchor defects cannot carry this representation, '
                        'but further exact clustering/fusion is not excluded.')}
    Path(__file__).with_name('actual_alternating_balanced_source_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS signed alternating incidence, both original cyclic supports, full figure-eight '
          'grid support/macrodefect constraints and all diagonal source coefficients')


if __name__ == '__main__':
    main()
