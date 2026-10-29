#!/usr/bin/env python3
"""Exact degenerate-alias obstruction and geometric star-bound checks.

The arithmetic and incidence checks do not import SnapPy or Regina.
Arb isolates the explicit complete geometric root and proves all bounds.
Optional --topology compares the saved gluing fixture with their knot label.
No quantum wall/source identification is asserted.
"""

import argparse
import json
from itertools import combinations
from pathlib import Path

from flint import acb, acb_poly, arb, ctx
import sympy as sp

from twist_family_certificates import UnionFind, combinatorial_data, twist_faces


ctx.prec = 192
HERE = Path(__file__).parent


def incidence_from_gluings(gluings):
    t = len(gluings)
    vertices = UnionFind((j, v) for j in range(t) for v in range(4))
    edges = UnionFind((j, a, b) for j in range(t) for a, b in combinations(range(4), 2))
    corners = UnionFind((j, v, w) for j in range(t) for v in range(4)
                        for w in range(4) if v != w)
    for j, (neighbors, maps) in enumerate(gluings):
        for face, (k, permutation) in enumerate(zip(neighbors, maps)):
            other_face = permutation[face]
            assert gluings[k][0][other_face] == j
            reverse = gluings[k][1][other_face]
            assert all(reverse[permutation[v]] == v for v in range(4))
            vs = [v for v in range(4) if v != face]
            for v in vs:
                vertices.union((j, v), (k, permutation[v]))
            for a, b in combinations(vs, 2):
                c, d = sorted([permutation[a], permutation[b]])
                edges.union((j, a, b), (k, c, d))
                corners.union((j, a, b), (k, permutation[a], permutation[b]))
                corners.union((j, b, a), (k, permutation[b], permutation[a]))
    classes = {}
    for edge in edges.parent:
        classes.setdefault(edges.find(edge), []).append(edge)
    index = {(0, 1): 0, (2, 3): 0, (0, 2): 1,
             (1, 3): 1, (0, 3): 2, (1, 2): 2}
    rows = []
    for group in classes.values():
        row = [0] * (3 * t)
        for j, a, b in group:
            row[3 * j + index[a, b]] += 1
        rows.append(row)
    assert len({vertices.find(v) for v in vertices.parent}) == 1
    assert len({corners.find(v) for v in corners.parent}) - 2 * t == 0
    return rows


def exact_flat_repair_obstruction(data):
    E = sp.Matrix(data['E'])
    t = E.rows
    L = sp.kronecker_product(sp.eye(t), sp.ones(1, 3))
    A = L.col_join(E)
    q = sp.Matrix([sp.Rational(v) for v in data['interior_angles']])
    k = sp.Matrix(data['k'])
    assert A * q == sp.ones(t, 1).col_join(2 * k)
    flat = [j for j in range(t) if any(q[3 * j + a] == 0 for a in range(3))]
    assert flat == data['flat']
    keep = [i for i in range(3 * t) if i // 3 not in flat]
    variable = [i for i in range(3 * t) if i // 3 in flat]
    assert all(q[i] > 0 for i in keep)
    rhs = sp.ones(t, 1).col_join(2 * sp.ones(t, 1)) - A[:, keep] * q[keep, :]
    y = sp.Matrix([sp.Rational(v) for v in data['farkas']])
    coefficients = A[:, variable].T * y
    assert all(v >= 0 for v in coefficients)
    assert (y.T * rhs)[0] == -sp.Rational(1, 5)
    # A short projection inequality, independently checked as a row identity.
    projection = sp.zeros(3 * t, 1)
    for i, value in [(3, 3), (15, 3), (4, 1), (16, 2),
                     (2, -1), (10, -1), (11, -2), (13, -1)]:
        projection[i] = value
    combination = sp.Matrix([1, 3, 0, 0, 0, 3, 0, -2, 0, 1, -1, 0])
    assert A.T * combination == projection
    original_rhs = sp.ones(t, 1).col_join(2 * sp.ones(t, 1))
    assert (combination.T * original_rhs)[0] == 3
    assert 3 * (q[3] + q[15]) + q[4] + 2 * q[16] - 3 == -sp.Rational(3, 10)
    assert sorted(incidence_from_gluings(data['gluings'])) == sorted(data['E'])
    assert all(sum(E[:, j]) == 2 for j in range(E.cols))
    assert all(sum(E[edge, 3 * j + a] for j in range(t) for a in range(3)) > 0
               for edge in range(t))
    return {'tetrahedra': t, 'winding': list(k), 'flat_tetrahedra_zero_based': flat,
            'nonflat_tetrahedra_zero_based': [j for j in range(t) if j not in flat],
            'Farkas_dot_product': '-1/5',
            'nonnegative_Farkas_coefficients': list(map(str, coefficients)),
            'edge_matrix_reconstructed_from_face_gluings': True}


def complete_geometry_and_star_bound(data):
    a = sp.symbols('a')
    P = a ** 3 + 2 * a - 1
    symbolic = [(1 + a - a * a) / 2, a, (1 + a) / 2,
                2 + a + a * a, 3 + a + a * a, a]
    triple = lambda z: [z, 1 / (1 - z), 1 - 1 / z]
    flat = sum([triple(z) for z in symbolic], [])
    root = next(z for z in acb_poly([-1, 2, 0, 1]).roots(tol=1e-48, maxprec=512)
                if z.imag > 0)
    assert arb('-0.227') < root.real < arb('-0.226')
    assert arb('1.467') < root.imag < arb('1.469')
    shapes = [(1 + root - root * root) / 2, root, (1 + root) / 2,
              2 + root + root * root, 3 + root + root * root, root]
    assert all(z.imag > 0 for z in shapes)
    marked_logs = sum([[z.log(), (1 / (1 - z)).log(), (1 - 1 / z).log()]
                       for z in shapes], [])
    for j, row in enumerate(data['gluing_rows']):
        product = sp.cancel(sp.prod(z ** power for z, power in zip(flat, row)))
        numerator, _ = sp.fraction(sp.cancel(product - 1))
        assert sp.rem(numerator, P, a) == 0
        total = sum((coefficient * value for coefficient, value in zip(row, marked_logs)), acb(0))
        target = 2 * arb.pi() if j < len(shapes) else arb(0)
        # Exact product 1 and this enclosure choose the required logarithmic lift.
        assert abs(total.imag - target) < arb('1e-30')
        assert abs(total.real) < arb('1e-30')
    bloch = lambda z: z.polylog(2).imag + (1 - z).arg() * abs(z).log()
    volume = sum((bloch(z) for z in shapes), arb(0))
    v3 = bloch((arb.pi() * acb(0, 1) / 3).exp())
    E = data['E']
    t = len(E)
    stars = [sum(any(row[3 * j + a] for a in range(3)) for j in range(t)) for row in E]
    bound = (t - min(stars)) * v3
    assert volume > arb('5.13')
    assert bound < arb('2.030')
    assert bound < volume
    return {'complete_root_polynomial': 'a^3+2a-1',
            'root_upper_half_plane': str(root),
            'all_geometric_shapes_positive': True,
            'exact_edge_and_both_peripheral_products': True,
            'marked_edge_angles_2pi_and_peripheral_angles_zero': True,
            'distinct_tetrahedron_star_sizes': stars,
            'volume_enclosure': str(volume),
            'all_wrong_edge_face_volume_bound_enclosure': str(bound),
            'strict_global_wrong_edge_face_gap': True}


def multiplier_sign_obstruction():
    E = combinatorial_data(*twist_faces(0, 'odd'))['incidence']
    L = sp.kronecker_product(sp.eye(3), sp.ones(1, 3))
    A = L.col_join(E)
    b, c = sp.symbols('b c')
    g = sp.Matrix([(2 * b + c) / 3, b, c] * 2 + [b, c, (2 * b + c) / 3])
    dual = sp.Matrix([c, -b / 3 + 4 * c / 3, -b / 3 + 4 * c / 3,
                      (b - c) / 3, b - c, 0])
    assert A.T * dual == g
    q = sp.Matrix([0, 0, 1, 1, 0, 0, 0, 0, 1])
    k = sp.Matrix([0, 1, 2])
    assert L * q == sp.ones(3, 1) and E * q == 2 * k
    assert (dual[3:, :].T * (k - sp.ones(3, 1)))[0] == (c - b) / 3
    v = next(z for z in acb_poly([1, 0, -1, 1]).roots(tol=1e-48, maxprec=512)
             if z.imag > 0)
    theta = v.arg()
    assert theta > 0 and theta < arb.pi() / 3
    sign_gap = (2 * theta.cos()).log() / 3
    assert sign_gap > 0
    return {'actual_chart': 'audited three-tetrahedron 5_2',
            'wrong_edge_winding': [0, 1, 2],
            'multiplier_defect_exact': 'log(2cos(theta))/3 > 0',
            'positive_multiplier_defect_enclosure': str(sign_gap),
            'the_alias_face_is_flat_and_is_not_a_volume_counterexample': True}


def topology(data):
    import regina
    import snappy
    from layered_two_bridge import regina_triangulation
    M = snappy.Manifold(data['name'])
    assert M.triangulation_isosig(decorated=False) == data['isosig']
    R = regina_triangulation(data['gluings'])
    assert R.isValid() and R.isOrientable() and R.countVertices() == 1
    assert str(R.vertex(0).linkType()) == 'Link.Torus'
    assert R.isIsomorphicTo(regina_triangulation(M._get_tetrahedra_gluing_data())) is not None
    return {'optional_package_knot_label_comparison': data['name'], 'isosig': R.isoSig(),
            'valid_orientable_one_cusp_triangulation': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topology', action='store_true')
    args = parser.parse_args()
    data = json.loads((HERE / 'degenerate_alias_face_fixture.json').read_text())
    result = {'status': 'PASS', 'exact_flat_repair_obstruction': exact_flat_repair_obstruction(data),
              'complete_geometric_fixture_and_global_star_bound': complete_geometry_and_star_bound(data),
              'complete_multiplier_sign_obstruction': multiplier_sign_obstruction(),
              'scope': 'Classical degenerate alias faces and exact repair/sign obstructions; no original quantum wall/period identification.'}
    if args.topology:
        result['optional_topology_comparison'] = topology(data)
    (HERE / 'degenerate_alias_face_results.json').write_text(json.dumps(result, indent=2, default=str) + '\n')
    print(json.dumps(result, indent=2, default=str))


if __name__ == '__main__':
    main()
