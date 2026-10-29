#!/usr/bin/env python3
"""90-digit numerical checks of the analytically proved homogeneous face scales."""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_pretzel_port_lift_and_geometric_anchor import gmatrix

mp.mp.dps = 90


def norm_matrix(matrix):
    return max(abs(v) for v in matrix)


def light(z, rho):
    return (2*rho/(abs(z)**2+rho*rho))*mp.matrix([[abs(z)**2, z], [mp.conj(z), 1]])


def anti_white(matrix, rho):
    # Reflection z -> rho^-2/conj(z), in its UNIT Lorentz normalization.
    A = mp.matrix([[0, rho**-2], [1, 0]])
    conjugate = mp.matrix([[mp.conj(matrix[i, j]) for j in range(2)] for i in range(2)])
    return A*conjugate*A.H/rho**-2


def case(s):
    alpha = mp.pi/s
    rho = mp.sqrt(1/mp.cos(alpha)+mp.tan(alpha))
    R, w = mp.exp(2j*alpha), -rho**4
    zz = lambda i: mp.exp((2*i-1)*1j*alpha)/(rho*mp.sin(alpha))
    Z = lambda i: rho*R**i
    Up = lambda i: mp.exp((2*i+1)*1j*alpha)/rho
    Um = lambda i: rho**3*mp.exp((2*i+1)*1j*alpha)
    center = mp.matrix([[rho, 0], [0, 1/rho]])
    Y = (R*w+1)/(w+R)
    maximum = mp.mpf(0)
    total = 0
    for i in range(s):
        c = rho*rho*mp.exp(4j*i*alpha)
        F = mp.matrix([[0, c], [1, 0]])
        assert norm_matrix(F*center*F.H/abs(c)-center) < mp.mpf('1e-75')
        gi, go = gmatrix(w, zz(i)), gmatrix(w, zz(i+1))
        P = gi*go**-1
        J = (mp.eye(2)-Y*P)/(1+Y)
        gp, gm = J*go, J**-1*gi
        maps = [(go, [Z(i), Up(i), Z(i+1), Um(i)],
                       [Z(i), Up(i), Z(i+1), Um(i)]),
                (gp, [Z(i), Um(i), Um(i-1)], [Z(i), Up(i-1), Up(i)]),
                (gm, [Z(i), Up(i-1), Up(i)], [Z(i), Um(i), Um(i-1)])]
        for matrix, sources, targets in maps:
            assert abs(mp.det(matrix)-1) < mp.mpf('1e-75')
            for source, target in zip(sources, targets):
                actual = matrix*anti_white(light(source, rho), rho)*matrix.H
                error = norm_matrix(actual-light(target, rho))
                maximum = max(maximum, error)
                total += 1
                assert error < mp.mpf('1e-70')
        for source, target in ((Up(i-1), Um(i)), (Up(i), Um(i-1)), (Z(i), Z(i))):
            assert norm_matrix(F*light(source, rho)*F.H/abs(c)-light(target, rho)) < mp.mpf('1e-75')
    # Remaining white s-gons, with the actual retained global Cartan map.
    A = mp.matrix([[w, 0], [0, 1/w]])
    for i in range(s):
        for matrix, point in ((mp.eye(2), Up(i)), (-A, Um(i))):
            actual = matrix*anti_white(light(point, rho), rho)*matrix.H
            maximum = max(maximum, norm_matrix(actual-light(point, rho)))
            assert norm_matrix(actual-light(point, rho)) < mp.mpf('1e-70')
            total += 1
    return {'s': s, 'all_labeled_white_and_shaded_homogeneous_vertices': total,
            'actual_center_preserving_half_turns': s,
            'maximum_full_Lorentz_lift_error': str(maximum),
            'no_projective_scalar_discarded': True}


if __name__ == '__main__':
    rows = [case(s) for s in (3, 4, 5, 8, 9, 25)]
    result = {'status': 'PASS', 'literal_homogeneous_face_families': rows,
              'scope': 'Verifies exact Lorentz normalization of the actual complete face maps; universal finite-subdivision and KKT arguments are analytical.'}
    Path(__file__).with_name('actual_pretzel_positive_ideal_angle_certificate_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(rows)} actual homogeneous face-map families, including shaded half twists and even widths')
