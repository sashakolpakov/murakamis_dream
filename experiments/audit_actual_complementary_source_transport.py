#!/usr/bin/env python3
"""Actual complementary arcs: normalized grid source and full forest residues."""

import itertools
import json
from pathlib import Path

import networkx as nx
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import charged_data, graph_blocks, setup
from audit_actual_general_flow_fusion import contract_edge, graph_coefficient, normalized_graph
from audit_actual_two_cut_ports import partial, word_matrix


def inv(x, p):
    return pow(int(x) % p, -1, p)


def block(H, edge, values, start=0, length=None):
    if length is None:
        length = edge['L']
    out = 1
    for r in range(start, start+length):
        out = out*(values[edge['u']]-edge['a']*pow(H.Q, r, H.p)*values[edge['v']]) % H.p
    return out


def prepare(H, width, word, clocks):
    S = setup(H, width, word)
    G = graph_blocks(H, S, clocks)
    _, weight, _, _ = charged_data(H, S, clocks)
    scalar, edges, nodes = normalized_graph(H, G)
    for identity in [e['id'] for e in edges if e['closure']]:
        factor, edges, nodes = contract_edge(H, edges, nodes, identity)
        scalar = scalar*factor % H.p
    expected = scalar*weight*graph_coefficient(H, edges, nodes) % H.p
    order = {v: j for j, v in enumerate(sorted(nodes))}
    edges = [dict(e, u=order[e['u']], v=order[e['v']]) for e in edges]
    return edges, len(nodes), scalar*weight % H.p, expected


def orient_forest(H, edges, count):
    graph = nx.Graph()
    graph.add_nodes_from(range(count))
    for edge in edges:
        if edge['L'] and edge['u'] != edge['v']:
            u, v = edge['u'], edge['v']
            if not graph.has_edge(u, v) or graph[u][v]['L'] < edge['L']:
                graph.add_edge(u, v, L=edge['L'], edge_id=edge['id'])
    forest = nx.maximum_spanning_tree(graph, weight='L')
    parents, selected, roots, traversal = {}, {}, [], []
    for component in nx.connected_components(forest):
        root = min(component)
        roots.append(root)
        traversal.append(root)
        for parent, child in nx.bfs_edges(forest, root):
            parents[child] = parent
            selected[child] = forest[parent][child]['edge_id']
            traversal.append(child)
    scalar, out = 1, []
    selected_ids = set(selected.values())
    by_id = {edge['id']: edge for edge in edges}
    oriented = {}
    for child, identity in selected.items():
        edge = by_id[identity].copy()
        parent = parents[child]
        if (edge['u'], edge['v']) == (parent, child):
            scalar = scalar*pow(-edge['a'], edge['L'], H.p)*pow(H.Q, edge['L']*(edge['L']-1)//2, H.p) % H.p
            edge['u'], edge['v'] = child, parent
            edge['a'] = inv(edge['a'], H.p)*pow(H.Q, 1-edge['L'], H.p) % H.p
        assert (edge['u'], edge['v']) == (child, parent)
        oriented[child] = edge
    outside = [edge for edge in edges if edge['id'] not in selected_ids]
    return scalar, oriented, roots, traversal, outside


def generic_centers(H, count):
    roots, centers, seen = [], [], set()
    for candidate in range(1, H.p):
        central = pow(candidate, H.N, H.p)
        if central and central not in seen and -central % H.p not in seen:
            roots.append(candidate)
            centers.append(central)
            seen.add(central)
            if len(roots) == count:
                return roots, centers
    raise AssertionError('insufficient generic root centers')


def forest_case(H, edges, count, scalar, expected):
    phase, selected, roots, traversal, outside = orient_forest(H, edges, count)
    scalar = scalar*phase % H.p
    if not selected:
        return {'no_nonempty_forest': True, 'original_coefficient': expected}
    rr, centers = generic_centers(H, count)
    norms, norm_product = {}, 1
    for child, edge in selected.items():
        assert pow(edge['a'], H.N, H.p) in (1, H.p-1)
        K = (centers[child]-pow(edge['a'], H.N, H.p)*centers[edge['v']]) % H.p
        assert K
        norms[child] = K
        norm_product = norm_product*K % H.p
    numerator_degree = sum(edge['L'] for edge in outside)
    denominator_threshold = count*(H.N-1)+sum(H.N-edge['L'] for edge in selected.values())
    assert numerator_degree == count*(H.N-1)-sum(edge['L'] for edge in selected.values())
    assert denominator_threshold-numerator_degree == len(selected)*H.N

    values, short_choices = {}, {}
    by_subset = {}
    zero_count = 0

    def visit(position):
        nonlocal zero_count
        if position == len(traversal):
            zero_count += 1
            numerator = scalar*norm_product % H.p
            for edge in outside:
                numerator = numerator*block(H, edge, values) % H.p
            jacobian = 1
            for vertex in traversal:
                x = values[vertex]
                if vertex not in selected:
                    jacobian = jacobian*H.N*pow(x, H.N-1, H.p) % H.p
                else:
                    edge = selected[vertex]
                    m = H.N-edge['L']
                    if vertex not in short_choices:
                        jacobian = jacobian*H.N*pow(x, H.N-1, H.p)*block(H, edge, values, edge['L'], m) % H.p
                    else:
                        r = short_choices[vertex]
                        derivative = 1
                        for s in range(m):
                            if s != r:
                                derivative = derivative*(x-edge['a']*pow(H.Q, edge['L']+s, H.p)*values[edge['v']]) % H.p
                        explicit = (pow(edge['a']*pow(H.Q, edge['L'], H.p)*values[edge['v']], m-1, H.p)
                                    *pow(-1, r, H.p)*pow(H.Q, r*(m-1)-r*(r+1)//2, H.p)
                                    *H.fac[r]*H.fac[m-1-r]) % H.p
                        assert derivative == explicit
                        F = (pow(x, H.N, H.p)-centers[vertex]) % H.p
                        assert F and derivative
                        jacobian = jacobian*F*derivative % H.p
            assert jacobian
            key = tuple(sorted(short_choices))
            by_subset[key] = (by_subset.get(key, 0)+numerator*inv(jacobian, H.p)) % H.p
            return
        vertex = traversal[position]
        # Fi roots. Selected arc roots are disjoint by all-path genericity.
        for label in range(H.N):
            values[vertex] = rr[vertex]*pow(H.Q, label, H.p) % H.p
            if vertex in selected:
                edge = selected[vertex]
                assert block(H, edge, values, edge['L'], H.N-edge['L'])
            visit(position+1)
        if vertex in selected:
            edge = selected[vertex]
            for r in range(H.N-edge['L']):
                values[vertex] = edge['a']*pow(H.Q, edge['L']+r, H.p)*values[edge['v']] % H.p
                assert pow(values[vertex], H.N, H.p) != centers[vertex]
                short_choices[vertex] = r
                visit(position+1)
            del short_choices[vertex]

    visit(0)
    assert zero_count == H.N**len(roots)*math_product(H.N+H.N-edge['L'] for edge in selected.values())
    assert by_subset.get((), 0) == expected
    assert sum(by_subset.values()) % H.p == 0
    assert (-sum(value for key, value in by_subset.items() if key)) % H.p == expected

    # Closed all-short factorial channel when the selected forest spans
    # one connected component. The root-label sum cancels its N exactly.
    full_channel = None
    if len(roots) == 1:
        root = roots[0]
        computed = 0
        vertices = [v for v in traversal if v in selected]
        for rs in itertools.product(*(range(H.N-selected[v]['L']) for v in vertices)):
            tags = dict(zip(vertices, rs))
            beta = {root: 1}
            for child in traversal[1:]:
                edge = selected[child]
                beta[child] = edge['a']*pow(H.Q, edge['L']+tags[child], H.p)*beta[edge['v']] % H.p
            numerator = scalar*norm_product % H.p
            for edge in outside:
                numerator = numerator*block(H, edge, beta) % H.p
            denominator = 1
            for child, edge in selected.items():
                r, m = tags[child], H.N-edge['L']
                path_norm = (pow(beta[child], H.N, H.p)*centers[root]-centers[child]) % H.p
                derivative_unit = (pow(edge['a']*pow(H.Q, edge['L'], H.p)*beta[edge['v']], m-1, H.p)
                                   *pow(-1, r, H.p)*pow(H.Q, r*(m-1)-r*(r+1)//2, H.p)
                                   *H.fac[r]*H.fac[m-1-r]) % H.p
                denominator = denominator*path_norm*derivative_unit % H.p
            assert denominator
            computed = (computed+numerator*inv(denominator, H.p)) % H.p
        full_channel = by_subset.get(tuple(sorted(selected)), 0)
        assert computed == full_channel
    return {'original_coefficient': expected, 'forest_edge_count': len(selected),
            'all_triangular_zero_count': zero_count, 'generic_all_path_norms_nonzero': True,
            'empty_short_subset_original_source': by_subset.get((), 0),
            'sum_all_zero_residues': 0, 'sum_nonempty_short_subsets': (-expected) % H.p,
            'nonzero_short_subsets': sum(bool(v) for key, v in by_subset.items() if key),
            'full_short_factorial_channel': full_channel,
            'all_norms_and_original_clock_weight_retained': True}


def math_product(values):
    out = 1
    for value in values:
        out *= value
    return out


def actual_cases():
    result = []
    for N, word, h in ((3, [1, -2, 1, -2], [0, 0, 1, 2]),
                       (4, [1, -2, 1, -2], [0, 1, 1, 2]),
                       (5, [1, -2, 1, -2], [0, 0, 2, 4]),
                       (3, [1, -2, 1, 1, -2, -2], [0, 1, 1, 1, 0, 1])):
        H = HardyNetwork(N, 1)
        edges, count, scalar, expected = prepare(H, 3, word, h)
        assert expected
        row = forest_case(H, edges, count, scalar, expected)
        row.update(N=N, word=word, original_clocks=h)
        result.append(row)
    return result


def whole_original_word():
    H, word, width = HardyNetwork(2, 1), [1, -2, 1, -2], 3
    total, corrected, rows = 0, 0, []
    for h in itertools.product(range(H.N), repeat=len(word)):
        edges, count, scalar, expected = prepare(H, width, word, h)
        row = forest_case(H, edges, count, scalar, expected)
        total = (total+expected) % H.p
        corrected = (corrected-row.get('sum_nonempty_short_subsets', -expected)) % H.p
        rows.append(row)
    W = word_matrix(word, H.plus, H.minus, width, H.N, H.p)
    cut = partial(W, H.pivot, width, H.N, H.p)
    direct = int(cut.sum())*inv(H.N, H.p) % H.p
    chi = H.dimension*pow(H.twist, -sum(1 if a > 0 else -1 for a in word), H.p) % H.p
    assert chi*inv(H.N, H.p)*total % H.p == chi*direct % H.p
    assert corrected == total
    return {'N': H.N, 'word': word, 'original_clock_states': len(rows),
            'all_original_external_and_1_over_N_normalizers_retained': True,
            'original_pivotal_scalar': chi*direct % H.p,
            'forest_source_scalar': chi*inv(H.N, H.p)*corrected % H.p}


def bare_unit_cell():
    rows = []
    for N in (2, 3, 5):
        Q = np.exp(2j*np.pi/N)
        d = N-1
        z = np.exp(2j*np.pi*np.arange(128)/128)
        X, Y = 3*z[:, None], 5*z[None, :]
        FX, FY = X**N-1, Y**N-2
        for t in (1, Q**-1):
            long = np.ones((128, 128), dtype=complex)
            for r in range(d):
                long *= X-Q**(r+1)*t*Y
            D, K, E = X-t*Y, 1-t**N*2, Y**d
            poly = np.mean(long*E/(FX*FY)*X*Y)
            comp = np.mean(K*E/(D*FX*FY)*X*Y)
            current = np.mean(E/D*(1/FY-t**N/FX)*X*Y)
            assert abs(poly-1) < 1e-11
            assert abs(comp) < 1e-11
            assert abs(current-1) < 1e-11
            rows.append({'N': N, 'actual_pivot_t': '1' if t == 1 else 'Q^-1',
                         'original_unit_source': str(poly),
                         'bare_complemented_torus': str(comp),
                         'retained_relative_current': str(current)})
    return rows


def arbitrary_block_checks():
    rows = []
    for N in range(2, 8):
        H = HardyNetwork(N, 1)
        d, p = N-1, H.p
        for L in range(N):
            a, m = 3, N-L
            b = [a*pow(H.Q, L+r, p) % p for r in range(m)]
            weights = [inv(math_product((b[r]-b[s]) % p for s in range(m) if s != r), p)
                       for r in range(m)]
            exterior = {}
            degree = 3*d-L
            for i in range(degree+1):
                for j in range(degree-i+1):
                    k = degree-i-j
                    exterior[i, j, k] = (1+3*i+7*j+11*k+i*j) % p
            lhs = 0
            for k in range(L+1):
                binomial = H.fac[L]*inv(H.fac[k]*H.fac[L-k], p) % p
                coefficient = pow(-a, k, p)*pow(H.Q, k*(k-1)//2, p)*binomial % p
                lhs += coefficient*exterior.get((d-L+k, d-k, d), 0)
            rhs = sum(weights[r]*sum(coef*pow(b[r], i, p)
                                      for (i, j, k), coef in exterior.items()
                                      if i+j == 2*d-L and k == d)
                      for r in range(m)) % p
            assert lhs % p == rhs
            rows.append({'N': N, 'L': L, 'short_root_channels': m,
                         'ordinary_parent_charge': 2*d-L,
                         'arbitrary_exterior_source_identity': True})
    H = HardyNetwork(3, 1)
    b = pow(H.Q, 2, H.p)
    assert pow(b, 3, H.p) != 0
    return {'all_original_charge_blocks': rows,
            'larger_parent_charge_cannot_reuse_bare_short_root_rule':
                {'N': 3, 'L': 2, 'exterior': 'Xi^3', 'charges': [2, 3],
                 'original_coefficient': 0, 'incorrect_bare_evaluation': pow(b, 3, H.p)}}


def main():
    result = {'actual_fixed_clock_forest_residues': actual_cases(),
              'whole_original_source': whole_original_word(),
              'literal_actual_closure_unit_cells': bare_unit_cell(),
              'arbitrary_block_source_contraction': arbitrary_block_checks(),
              'scope': 'Exact source forest decomposition with all norms; no geometric-sector deletion.'}
    Path(__file__).with_name('actual_complementary_source_transport_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS actual complementary source forests/all path norms/factorial Jacobians; '
          'whole original pivotal period; zero bare torus and retained unit current')


if __name__ == '__main__':
    main()
