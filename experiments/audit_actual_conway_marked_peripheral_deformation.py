#!/usr/bin/env python3
"""Exact rational-function certificates for the marked Conway deformation.

The prism phase variables are independent indeterminates. These checks
are identities, not numerical sampling or manifold recognition. Global
topology is separately certified by the literal closed bowtie audit.
"""
import json
from pathlib import Path

import sympy as sp


def equal_projectively(a, b):
    aa, bb = list(a), list(b)
    return all(sp.cancel(aa[i]*bb[j]-aa[j]*bb[i]) == 0
               for i in range(4) for j in range(i))


def matrix_cancel(matrix):
    return matrix.applyfunc(sp.cancel)


def chart(a, b, c):
    """Projective matrix taking ordered a,b,c to 0,infinity,1."""
    if a is None:
        return sp.Matrix([[0, c-b], [1, -b]])
    if b is None:
        return sp.Matrix([[1, -a], [0, c-a]])
    if c is None:
        return sp.Matrix([[1, -a], [1, -b]])
    return sp.Matrix([[c-b, -a*(c-b)], [c-a, -b*(c-a)]])


def at(matrix, z):
    if z is None:
        return sp.cancel(matrix[0, 0]/matrix[1, 0])
    return sp.cancel((matrix[0, 0]*z+matrix[0, 1]) /
                     (matrix[1, 0]*z+matrix[1, 1]))


def derivative(matrix, z):
    return sp.cancel(matrix.det()/(matrix[1, 0]*z+matrix[1, 1])**2)


def white(e, r):
    return [sp.Matrix([[1, 0], [0, e]]),
            sp.Matrix([[1, e-1], [0, e]]),
            sp.Matrix([[e-r, r*(1-e)], [e-1, 1-e*r]]),
            sp.Matrix([[r, 0], [1-e, e*r]])]


def local_identities():
    E, R, H = sp.symbols('E R H', nonzero=True)
    ws = white(E, R)
    shaded = sp.Matrix([[0, -E*R], [1, -1-E]])
    reflected = shaded.subs(E, 1/E)
    for i, j in [(0, 0), (2, 2), (3, 1)]:
        assert equal_projectively(ws[i]*shaded, reflected*ws[j])

    turn = sp.Matrix([[0, R-1], [1, -1]])
    closure = sp.Matrix([[1, -R], [1, -1]])
    for j in range(4):
        assert equal_projectively(turn*ws[(j+1) % 4],
                                  white(1/E, 1-R)[j]*turn)
        assert equal_projectively(closure*white(1/E, R)[j],
                                  ws[(2-j) % 4]*closure)

    # Every actual main meridian is unipotent projectively, at the
    # corresponding common main flag. No norm or trace inequality.
    corners = [0, None, 1, R]
    expected_derivatives = [1/E, E, 1/E, E]
    for j, corner in enumerate(corners):
        first, second = ws[(j-1) % 4], ws[j]
        meridian = first.adjugate()*second
        assert sp.cancel(sp.trace(meridian)**2-4*meridian.det()) == 0
        for matrix in [first, second]:
            if corner is None:
                assert matrix[1, 0] == 0
                local_derivative = matrix[1, 1]/matrix[0, 0]
            else:
                assert sp.cancel(at(matrix, corner)-corner) == 0
                local_derivative = derivative(matrix, corner)
            assert sp.cancel(local_derivative-expected_derivatives[j]) == 0

    r = H*(1+E)**2/(E*(1+H)**2)
    zeta = (1+E)/(1+H)
    assert sp.cancel(zeta**2-(1+E)*zeta+E*r) == 0
    assert sp.cancel((H*zeta)**2-(1+E)*H*zeta+E*r) == 0
    mixed_white = white(E, r)
    mixed_shaded = shaded.subs(R, r)
    for j in [0, 2]:
        assert sp.cancel(at(mixed_white[j], zeta)-zeta/E) == 0
    assert sp.cancel(at(mixed_shaded, zeta)-zeta) == 0
    assert sp.cancel(at(mixed_shaded, H*zeta)-H*zeta) == 0
    assert sp.cancel(sp.trace(mixed_shaded)**2/mixed_shaded.det()
                     -(1+H)**2/H) == 0
    meridian = mixed_shaded.adjugate()
    assert sp.cancel(1/derivative(meridian, zeta)-1/H) == 0
    longitude = mixed_white[2].adjugate()*mixed_white[0]
    assert sp.cancel(at(longitude, zeta)-zeta) == 0
    assert sp.cancel(1/derivative(longitude, zeta)
                     -((1-E*H)/(E-H))**2) == 0
    assert equal_projectively(longitude*mixed_shaded,
                              mixed_shaded*longitude)
    return {'shaded_pointwise_edge_relations': 3,
            'turn_relations': 4, 'cylindrical_closure_relations': 4,
            'main_meridian_unipotence_and_flags': 4,
            'mixed_leaf_flags_and_primitive_peripheral_logs': 'PASS'}


def prism_identities():
    A, B, C = sp.symbols('A B C', nonzero=True)
    substitutions = {A: 1/A, B: 1/B, C: 1/C}

    def reflected(value):
        if isinstance(value, sp.MatrixBase):
            return value.applyfunc(reflected)
        return sp.sympify(value).xreplace(substitutions)

    p = sp.cancel(1+A-A*(A*B*(1+C)-1-A)/(A*A*B*B*C-A))
    coords = [None, p, 1, A, A*B, A*B*C]
    # Literal lower, upper, output orders, not independently permuted.
    ports = [(2, 3, 1, 0), (0, 1, 4, 5), (2, 3, 4, 5)]
    phases = [B*C, A*B, A*B*C]
    world = []
    for port, e in zip(ports, phases):
        values = [coords[j] for j in port]
        t = chart(*values[:3])
        r = at(t, values[3])
        world.append([matrix_cancel(reflected(t).adjugate()*w*t)
                      for w in white(e, r)])
    triangles = []
    for ids in [(1, 3, 4), (0, 2, 5)]:
        source = [coords[j] for j in ids]
        target = [reflected(z) if z is not None else None for z in source]
        triangles.append(matrix_cancel(chart(*target).adjugate()*chart(*source)))
    top, bottom = triangles
    checks = [(world[0][1], top), (world[1][1], top),
              (world[0][3], bottom), (world[1][3], bottom),
              (world[0][2], world[1][0]),
              (world[2][0], world[0][0]), (world[2][2], world[1][2]),
              (world[2][1], top), (world[2][3], bottom)]
    for a, b in checks:
        assert equal_projectively(a, b)
    return {'generic_prism_rational_function_relations': len(checks),
            'independent_phase_indeterminates': ['A', 'B', 'C'],
            'sampled_parameters_used': False}


if __name__ == '__main__':
    result = {'status': 'PASS', 'local': local_identities(),
              'prism': prism_identities()}
    destination = Path(__file__).with_name(
        'actual_conway_marked_peripheral_deformation_results.json')
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
