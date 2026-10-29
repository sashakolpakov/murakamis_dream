#!/usr/bin/env python3
"""Certify an oversized integer alias face of a positive 5_2 triangulation.

All angle/lattice identities use exact rational arithmetic. Arb isolates
one cubic root and certifies positive complete geometry at every move,
and the strict volume excess of a rational alias point. The optional
topology check independently replays the moves in Regina.
This does NOT assert a nonzero coefficient of that alias in the original
quantum cycle; its purpose is to refute universal phase-volume domination.
"""

import argparse
import json
from fractions import Fraction
from pathlib import Path

from flint import acb, acb_poly, arb, ctx
import sympy as sp

from audit_degenerate_alias_faces import incidence_from_gluings


ctx.prec = 192
HERE = Path(__file__).parent


def rational(value):
    q = Fraction(value)
    return arb(q.numerator) / q.denominator


def geometry(data):
    a = sp.symbols('a')
    P = a ** 3 - 2 * a ** 2 + 3 * a - 1
    root = next(z for z in acb_poly([-1, 3, -2, 1]).roots(tol=1e-48, maxprec=512)
                if z.imag > 0)
    assert arb('.78') < root.real < arb('.79')
    assert arb('1.30') < root.imag < arb('1.31')
    result = []
    for step in data['steps']:
        symbolic = [sum(sp.Rational(c) * a ** k for k, c in enumerate(coefficients))
                    for coefficients in step['shape_coefficients']]
        shapes = [sum((rational(c) * root ** k for k, c in enumerate(coefficients)), acb(0))
                  for coefficients in step['shape_coefficients']]
        assert all(z.imag > 0 for z in shapes)
        flat = sum([[z, 1 / (1 - z), 1 - 1 / z] for z in symbolic], [])
        logs = sum([[z.log(), (1 / (1 - z)).log(), (1 - 1 / z).log()]
                    for z in shapes], [])
        t = step['tetrahedra']
        assert sorted(incidence_from_gluings(step['gluings'])) == sorted(step['gluing_rows'][:t])
        for j, row in enumerate(step['gluing_rows']):
            product = sp.cancel(sp.prod(z ** power for z, power in zip(flat, row)))
            numerator, _ = sp.fraction(sp.cancel(product - 1))
            assert sp.rem(numerator, P, a) == 0
            total = sum((power * value for power, value in zip(row, logs)), acb(0))
            target = 2 * arb.pi() if j < t else arb(0)
            assert abs(total.imag - target) < arb('1e-30')
            assert abs(total.real) < arb('1e-30')
        bloch = lambda z: z.polylog(2).imag + (1 - z).arg() * abs(z).log()
        volume = sum((bloch(z) for z in shapes), arb(0))
        assert arb('2.82812') < volume < arb('2.82813')
        result.append({'tetrahedra': t, 'all_shapes_positive': True,
                       'exact_edge_and_peripheral_products': True,
                       'marked_edge_angles_2pi_and_peripheral_angles_zero': True,
                       'volume_enclosure': str(volume)})
    return result


def angle_cell_and_lattice(data):
    t = 9
    E = sp.Matrix(data['E'])
    full_rows = sp.Matrix(data['steps'][-1]['gluing_rows'])
    assert E == full_rows[:t, :]
    q = sp.Matrix([sp.Rational(v) for v in data['rational_alias_angles']])
    L = sp.kronecker_product(sp.eye(t), sp.ones(1, 3))
    k = sp.Matrix(data['winding'])
    assert all(v >= 0 for v in q)
    assert L * q == sp.ones(t, 1)
    assert E * q == 2 * k
    assert (full_rows[t, :] * q)[0] == 0  # Complete marked meridian retained.
    assert full_rows[t:, :] * q == sp.zeros(2, 1)  # Both peripheral rows retained.
    assert k == sp.Matrix([1, 1, 1, 1, 1, 1, 2, 0, 1])
    flat = [j for j in range(t) if any(q[3 * j + a] == 0 for a in range(3))]
    assert flat == [0, 1, 2]
    assert all(q[3 * j + a] > 0 for j in range(3, 9) for a in range(3))
    chart = data['alias_chart']
    rows = chart['selected_rows']
    assert rows == [0, 1, 2, 3, 5, 6, 7, 8, 9]
    selected = full_rows[rows, :]
    A, B = sp.zeros(t), sp.zeros(t)
    theta, gamma = [], []
    middle = sp.zeros(t, 1)
    for j, rotation in enumerate(chart['quad_rotations']):
        i0, i1, i2 = [3 * j + (rotation + a) % 3 for a in range(3)]
        A[:, j] = selected[:, i0] - selected[:, i1]
        B[:, j] = selected[:, i2] - selected[:, i1]
        middle += selected[:, i1]
        theta.append(q[i0])
        gamma.append(q[i2])
    assert A == sp.Matrix(chart['A']) and B == sp.Matrix(chart['B'])
    assert B.det() == -2
    assert A * B.T == B * A.T
    m = sp.Matrix([sp.Integer(v) for v in chart['m']])
    defect = (k - sp.ones(t, 1)).col_join(sp.zeros(1, 1))[rows, :]
    assert B * m == defect
    assert m == sp.Matrix([0, 1, 0, 0, 0, 0, -1, -1, 1])
    C = B.inv() * A
    assert C == C.T
    nu = sp.Matrix([2] * 8 + [0]) - middle
    kappa = B.inv() * nu
    assert sp.Matrix(gamma) == kappa - C * sp.Matrix(theta) + 2 * m
    volume = arb(0)
    for v in q:
        if v == 0 or v == 1:
            continue
        angle = arb.pi() * rational(str(v))
        volume += (2 * acb(0, 1) * angle).exp().polylog(2).imag / 2
    assert arb('3.76403') < volume < arb('3.76404')
    assert volume > arb('2.82813')
    regular = (arb.pi() * acb(0, 1) / 3).exp()
    v3 = regular.polylog(2).imag + (1 - regular).arg() * abs(regular).log()
    assert volume > 3 * v3
    return {'angle_equations_exact': True, 'winding': list(map(int, k)),
            'marked_meridian_angle_exactly_zero': True,
            'both_marked_peripheral_angle_rows_exactly_zero': True,
            'quad_rotations': chart['quad_rotations'], 'omitted_edge_zero_based': 4,
            'det_B': -2, 'integer_alias_m': list(map(int, m)),
            'B_m_equals_full_marked_defect_exactly': True,
            'weak_nonnegative_alias_equation_exact': 'gamma=kappa-C theta+2m, angles in units pi',
            'strictly_positive_alias_locus_empty_zero_edge_forces_flat_tets': True,
            'flat_tetrahedra_zero_based': flat,
            'alias_volume_enclosure': str(volume),
            'exceeds_three_regular_tetrahedron_volumes': True,
            'exceeds_complete_hyperbolic_volume': True}


def topology(data):
    import regina
    from layered_two_bridge import regina_triangulation
    from twist_family_certificates import twist_faces
    from twist_topology_audit import pairings
    steps = data['steps']
    family, _ = twist_faces(0, 'odd')
    original = regina.Triangulation3()
    for _ in family:
        original.newTetrahedron()
    _, adjacency = pairings(family)
    for (t, f), (u, _, p, _, sign) in adjacency.items():
        if sign == 1:
            original.tetrahedron(t).join(f, original.tetrahedron(u), regina.Perm4(*[p[v] for v in range(4)]))
    assert original.isIsomorphicTo(regina_triangulation(steps[0]['gluings'])) is not None
    for j, move in enumerate(data['moves']):
        R = regina_triangulation(steps[j]['gluings'])
        assert R.isValid() and R.isOrientable() and R.countVertices() == 1
        assert str(R.vertex(0).linkType()) == 'Link.Torus'
        assert R.pachner(R.tetrahedron(move[0]).triangle(move[1]))
        assert R.isIsomorphicTo(regina_triangulation(steps[j + 1]['gluings'])) is not None
    final = regina_triangulation(steps[-1]['gluings'])
    assert final.isValid() and final.isOrientable() and final.countVertices() == 1
    assert str(final.vertex(0).linkType()) == 'Link.Torus'
    assert final.isoSig() == data['final_isosig']
    return {'initial_isomorphic_to_previously_audited_three_tetrahedron_5_2': True,
            'each_of_six_2_to_3_moves_legal_independently_in_Regina': True,
            'all_intermediate_triangulations_isomorphic_to_recorded_moves': True,
            'each_vertex_link_explicitly_checked_Torus_in_Regina': True,
            'final_isosig': final.isoSig()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topology', action='store_true')
    args = parser.parse_args()
    data = json.loads((HERE / 'positive_alias_volume_counterexample_fixture.json').read_text())
    result = {'status': 'PASS', 'complete_positive_geometries': geometry(data),
              'exact_marked_alias_and_strict_volume_excess': angle_cell_and_lattice(data),
              'scope': 'Actual positive complete 5_2 triangulation with an oversized integer-alias face. No nonzero original quantum source coefficient asserted.'}
    if args.topology:
        result['independent_topology_move_audit'] = topology(data)
    (HERE / 'positive_alias_volume_counterexample_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
