#!/usr/bin/env python3
"""Trace the oversized weak alias through its last actual Pachner move.

Exact face permutations identify the bipyramid. Exact linear angle and
rational five-term maps locate the missing preimage, norm divisors, and
directional blow-up. This does not compute an original quantum coefficient.
"""

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).parent


def actual_bipyramid(data):
    old = data['steps'][-2]['gluings']
    new = data['steps'][-1]['gluings']
    assert data['moves'][-1] == [1, 0]
    assert old[1][0][0] == 0 and old[1][1][0] == [1, 3, 0, 2]
    old_labels = {1: ['D', 'A', 'B', 'C'], 0: ['B', 'E', 'C', 'A']}
    labels = []
    for j in range(3):
        found = {}
        for face, neighbor in enumerate(new[j][0]):
            if neighbor < 3:
                continue
            # Unaffected old tetrahedron k is final tetrahedron k+1.
            k = neighbor - 1
            p = new[j][1][face]
            outside_face = p[face]
            removed = old[k][0][outside_face]
            r = old[k][1][outside_face]
            assert removed in old_labels
            for v in range(4):
                if v == face:
                    continue
                label = old_labels[removed][r[p[v]]]
                assert v not in found or found[v] == label
                found[v] = label
        assert len(found) == 4
        labels.append([found[v] for v in range(4)])
    assert labels == [['E', 'D', 'C', 'B'], ['E', 'D', 'B', 'A'], ['E', 'D', 'A', 'C']]
    for j in range(3):
        for face, neighbor in enumerate(new[j][0]):
            if neighbor >= 3:
                continue
            p = new[j][1][face]
            assert all(labels[j][v] == labels[neighbor][p[v]]
                       for v in range(4) if v != face)
    E = sp.Matrix(data['E'])
    assert list(E[7, :]) == [1, 0, 0] * 3 + [0] * 18
    for j, equatorial_edge in enumerate([8, 6, 3]):
        assert E[7, 3 * j] == E[equatorial_edge, 3 * j] == 1
    return {'old_tetrahedra_in_shape_order_x_y': [1, 0],
            'old_vertex_labels_x_y': [old_labels[1], old_labels[0]],
            'new_vertex_labels_u_v_w': labels,
            'new_edge_zero_based': 7, 'new_edge_local_vertices_in_each_new_tet': [0, 1],
            'equatorial_opposite_global_edges_zero_based': [8, 6, 3]}


def angle_preimage(data):
    beta = sp.Matrix(sp.symbols('b0:3'))
    gamma = sp.Matrix(sp.symbols('c0:3'))
    alpha = sp.ones(3, 1) - beta - gamma
    x = sp.Matrix([beta[1] + gamma[2], beta[0] + gamma[1], gamma[0] + beta[2]])
    y = sp.Matrix([gamma[0] + beta[1], gamma[1] + beta[2], beta[0] + gamma[2]])
    total = sum(beta) + sum(gamma)
    assert sp.expand(sum(x) - total) == sp.expand(sum(y) - total) == 0
    equator = sp.Matrix([x[0] + y[1], x[2] + y[2], x[1] + y[0]])
    assert all(sp.expand(equator[j] - alpha[j] - total + 1) == 0 for j in range(3))
    q = sp.Matrix([sp.Rational(v) for v in data['rational_alias_angles']])
    flat = q[:9, :]
    values = {beta[j]: flat[3 * j + 1] for j in range(3)}
    values.update({gamma[j]: flat[3 * j + 2] for j in range(3)})
    assert [alpha[j].subs(values) for j in range(3)] == [0, 0, 0]
    forced_x, forced_y = x.subs(values), y.subs(values)
    assert forced_x == sp.Matrix([sp.Rational(13, 10), sp.Rational(13, 20), sp.Rational(21, 20)])
    assert forced_y == sp.Matrix([sp.Rational(27, 20), sp.Rational(7, 10), sp.Rational(19, 20)])
    assert sum(forced_x) == sum(forced_y) == 3
    # The three equator equations sum to the two old local sums.
    equator_old = sp.Matrix([[1, 0, 0, 0, 1, 0],
                             [0, 0, 1, 0, 0, 1],
                             [0, 1, 0, 1, 0, 0]])
    assert sp.ones(1, 3) * equator_old == sp.ones(1, 6)
    return {'universal_angle_preimage_criterion': 'new internal angle sum exactly 2pi',
            'criterion_necessary_and_sufficient_for_boundary_preserving_nonnegative_angle_replacement': True,
            'oversized_alias_internal_angle_sum_units_pi': 0,
            'positive_preimage_exists': False,
            'formal_boundary_forced_old_x_angles_units_pi': list(map(str, forced_x)),
            'formal_boundary_forced_old_y_angles_units_pi': list(map(str, forced_y)),
            'each_forced_old_local_sum_units_pi': 3}


def shape_maps_and_norms(data):
    x, y, a = sp.symbols('x y a')
    e = x * y / (x + y - 1)
    vertices = {'D': sp.Matrix([1, 0]), 'A': sp.Matrix([0, 1]),
                'B': sp.Matrix([1, 1]), 'C': sp.Matrix([x, 1]), 'E': sp.Matrix([e, 1])}
    def bracket(p, q):
        return sp.det(sp.Matrix.hstack(vertices[p], vertices[q]))
    def cross(labels):
        p, q, r, s = labels
        return sp.cancel(bracket(p, r) * bracket(q, s) / (bracket(p, s) * bracket(q, r)))
    assert cross(['D', 'A', 'B', 'C']) == x
    assert sp.cancel(cross(['B', 'E', 'C', 'A']) - y) == 0
    forward = [x / (1 - y), (1 - x) * (1 - y) / (x * y), y / (1 - x)]
    for labels, value in zip([['E', 'D', 'C', 'B'], ['E', 'D', 'B', 'A'], ['E', 'D', 'A', 'C']], forward):
        assert sp.cancel(cross(labels) - value) == 0
    assert sp.cancel(sp.prod(forward) - 1) == 0
    P = a ** 3 - 2 * a ** 2 + 3 * a - 1
    shape = lambda step, j: sum(sp.Rational(c) * a ** k for k, c in enumerate(step['shape_coefficients'][j]))
    actual_x = shape(data['steps'][-2], 1)
    actual_y = shape(data['steps'][-2], 0)
    for j, value in enumerate(forward):
        difference = sp.cancel(value.subs({x: actual_x, y: actual_y}) - shape(data['steps'][-1], j))
        numerator, _ = sp.fraction(difference)
        assert sp.rem(numerator, P, a) == 0
    u, w, t, eps, direction_a, direction_b = sp.symbols('u w t eps A B', nonzero=True)
    inverse_x = u * (1 - w) / (1 - u * w)
    inverse_y = w * (1 - u) / (1 - u * w)
    assert sp.cancel(inverse_x.subs({u: forward[0], w: forward[2]}, simultaneous=True) - x) == 0
    assert sp.cancel(inverse_y.subs({u: forward[0], w: forward[2]}, simultaneous=True) - y) == 0
    residues = []
    for value in [inverse_x, inverse_y]:
        local = sp.cancel(value.subs(w, (1 - t) / u))
        residue = sp.limit(t * sp.diff(local, t) / local, t, 0)
        assert residue == -1
        residues.append(int(residue))
    blowup = {u: 1 + eps * direction_a, w: 1 + eps * direction_b}
    x0 = sp.limit(inverse_x.subs(blowup, simultaneous=True), eps, 0)
    y0 = sp.limit(inverse_y.subs(blowup, simultaneous=True), eps, 0)
    assert sp.cancel(x0 - direction_b / (direction_a + direction_b)) == 0
    assert sp.cancel(y0 - direction_a / (direction_a + direction_b)) == 0
    assert sp.cancel(x0 + y0 - 1) == 0
    # The exact primitive cyclic pentagon centers of the existing note.
    U, V = forward[2], x
    H = sp.cancel(1 - U + U * V)
    assert H == 1 - y
    assert sp.cancel((1 - V) * U - y) == 0
    assert sp.cancel(V / H - forward[0]) == 0
    assert sp.cancel(-U * V / (1 - U) - 1 / (1 - forward[1])) == 0
    # The simultaneous corner has zero, pole, zero norm ratios.
    norm_values = [1 - w, (1 - inverse_y) / (1 - w),
                   (1 - w) * (1 - inverse_x) / (1 - inverse_y)]
    leading = [sp.limit(norm_values[0].subs(blowup, simultaneous=True) / eps, eps, 0),
               sp.limit(eps * norm_values[1].subs(blowup, simultaneous=True), eps, 0),
               sp.limit(norm_values[2].subs(blowup, simultaneous=True) / eps, eps, 0)]
    expected = [-direction_b, -1 / (direction_a + direction_b), -direction_a]
    assert all(sp.cancel(v - z) == 0 for v, z in zip(leading, expected))
    return {'actual_five_term_map': list(map(str, forward)),
            'inverse_five_term_map': list(map(str, [inverse_x, inverse_y])),
            'inverse_norm_divisor': '1-u*w=0',
            'generic_dlog_x_dlog_y_residues_at_divisor': residues,
            'simultaneous_corner_blowup_x_y': list(map(str, [x0, y0])),
            'blowup_old_shapes_sum_exactly_one': True,
            'cyclic_pentagon_substitution': 'U=w, V=x, H=1-y',
            'cyclic_right_centers': ['w', '1/(1-v)', 'u'],
            'right_norm_ratio_leading_terms': list(map(str, leading)),
            'norm_root_valuations': ['+1/N', '-1/N', '+1/N'],
            'compatible_right_root_frame_monodromy': ['Q', 'Q^-1', 'Q']}


def normalized_cyclic_atom_wall_orders():
    for N in range(2, 33):
        orders = [sp.Rational(N - 1, 2 * N)] + [sp.Rational(2 * j - N - 1, 2 * N) for j in range(1, N)]
        assert sum(orders) == 0
        assert min(orders) < 0 < max(orders)
    return {'uniform_formula': 'ord D_0=(N-1)/(2N), ord D_j=(2j-N-1)/(2N), 1<=j<N',
            'parameter': 't=1-center, spectral root mu=(1-t)^(1/N)',
            'both_zeros_and_poles_for_every_N_ge_2': True,
            'determinant_valuation_zero': True,
            'norm_root_zero_does_not_imply_source_or_operator_vanishing': True}


def main():
    data = json.loads((HERE / 'positive_alias_volume_counterexample_fixture.json').read_text())
    result = {'status': 'PASS', 'actual_last_move_bipyramid': actual_bipyramid(data),
              'universal_angular_preimage_and_concrete_obstruction': angle_preimage(data),
              'actual_shape_map_norm_divisor_and_direction': shape_maps_and_norms(data),
              'normalized_cyclic_atom_wall_orders': normalized_cyclic_atom_wall_orders(),
              'scope': 'Exact classical/angular/norm trace of first failed inverse move. No original quantum source coefficient or cancellation inferred.'}
    (HERE / 'oversized_alias_last_pachner_wall_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
