#!/usr/bin/env python3
"""Validate a positive (7,3) period solution and a zero below its wire ray.

The numerical solve supplies a candidate only. A rectangular interval
contraction proves existence and uniqueness in the recorded box. This
does not test a volume identity or claim cancellation in a knot invariant.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json

import mpmath as mp
from flint import acb, arb, ctx


def main():
    root = Path(__file__).resolve().parents[1]
    ctx.prec = 256
    mp.mp.dps = 90
    n, p = 7, 3
    candidate = mp.findroot(
        lambda t, u: (
            n*t+2j*(mp.asinh(mp.tan(t/2))
                     +mp.asinh(mp.tan(t/2)*mp.cos(u/2)))-2*mp.pi,
            p*u+2j*(mp.asinh(mp.tan(u/2))
                     +mp.asinh(mp.tan(u/2)*mp.cos(t/2)))-2*mp.pi,
        ), (2*mp.pi/(n+2j), 2*mp.pi/(p+2j)), tol=mp.mpf('1e-85'))
    centers = [acb(mp.nstr(z.real, 85), mp.nstr(z.imag, 85)).mid()
               for z in candidate]
    radius = arb(2)**(-100)
    error_box = acb(arb(0, radius), arb(0, radius))
    box = [z+error_box for z in centers]
    I = acb(0, 1)
    pi = arb.pi()

    def equations(t, u):
        return [n*t+2*I*((t/2).tan().asinh()
                        +((t/2).tan()*(u/2).cos()).asinh())-2*pi,
                p*u+2*I*((u/2).tan().asinh()
                        +((u/2).tan()*(t/2).cos()).asinh())-2*pi]

    def jacobian(t, u):
        ct, cu = (t/2).cos(), (u/2).cos()
        st, su = (t/2).sin(), (u/2).sin()
        tt, tu = (t/2).tan(), (u/2).tan()
        dt, du = (1+(tt*cu)**2).sqrt(), (1+(tu*ct)**2).sqrt()
        return [[n+I*(1/ct+cu/(ct**2*dt)), -I*tt*su/dt],
                [-I*tu*st/du, p+I*(1/cu+ct/(cu**2*du))]]

    jac0 = jacobian(*centers)
    det = jac0[0][0]*jac0[1][1]-jac0[0][1]*jac0[1][0]
    inverse = [[(jac0[1][1]/det).mid(), (-jac0[0][1]/det).mid()],
               [(-jac0[1][0]/det).mid(), (jac0[0][0]/det).mid()]]
    jac = jacobian(*box)
    defect = [[acb(int(i == j))-sum(inverse[i][k]*jac[k][j]
                                  for k in range(2))
               for j in range(2)] for i in range(2)]
    residual = equations(*centers)
    images = [centers[i]-sum(inverse[i][j]*residual[j] for j in range(2))
              +sum(defect[i][j]*error_box for j in range(2))
              for i in range(2)]
    assert all(box[i].contains_interior(images[i]) for i in range(2))
    contraction = max(sum(abs(v) for v in row).upper() for row in defect)
    assert contraction < arb(1)/2

    t, u = box
    for v, neighbor in ((t, u), (u, t)):
        assert 0 < v.real < pi/2 and v.imag < 0
        assert abs((v/2).cos()) < 1
        assert (v/2).tan().real > 0
        arg = (v/2).tan()*(neighbor/2).cos()
        assert arg.real > 0
        assert arg.asinh().real > 0
    # Positive real returns alone do not certify positive original
    # tetrahedra. Check the exact positive-edge criterion on every
    # original edge, including both complete outside incidences.
    positive_edges = []
    for left, right in ((t, acb(0)), (t, u), (u, acb(0))):
        aa, bb = (left/2).tan(), (right/2).tan()
        qq = (1+aa*aa+bb*bb).sqrt()
        margin = qq.real-(aa.real**2+bb.real**2).sqrt()
        assert margin > 0
        shapes = [(qq+aa)/(bb-I), (qq-aa)/(bb-I),
                  -(qq-bb)/(aa+I), -(qq+bb)/(aa+I)]
        assert all(shape.imag > 0 for shape in shapes)
        # Fix the return-square-root sign as well as the shapes.
        for first, second in ((left, right), (right, left)):
            rr = ((first/2).tan()*(second/2).cos()).asinh()
            assert (qq*(second/2).cos()).real > 0
            assert (rr.cosh()-qq*(second/2).cos()).contains(0)
        positive_edges.append({
            'positive_matrix_margin': str(margin),
            'four_original_shapes': list(map(str, shapes)),
        })
    A, B = (t/2).cos()**2, (u/2).cos()**2
    W = (A*B/(A+B-A*B)).sqrt()
    assert W.real > 0 and W.imag > 0
    gamma_tangent = W.imag/W.real
    assert 0 < gamma_tangent < arb(1)/2
    a, H = t.real, -t.imag
    zero_x = arb(1)/2-a/(2*pi)
    zero_height = H/(2*pi)
    ray_height = (gamma_tangent*a.sin()).asinh()/(2*pi)
    gap = zero_height-ray_height
    assert arb(1)/50 < zero_x < arb(12)/25
    assert zero_height > 0 and gap < -arb(3)/1000
    assert zero_x < arb(12)/25-arb(1)/200
    assert -u.imag > H

    # This is the zero of the limiting sine argument. The exact
    # reciprocal-factorial zero is shifted by +1/(2N): its argument
    # N*(1/2-x-t/(2*pi))-1/2 is then -1, where G_N has a simple pole.
    zero = acb(arb(1)/2)-t/(2*pi)
    assert ((pi*zero).tan()-1/(t/2).tan()).contains(0)
    # For every N>=100, |h'|<=tan(gamma)<1/2 makes the height loss
    # from this shift at most 1/(4N)<=1/400. The original gap>3/1000
    # therefore leaves a strict finite-zero gap>1/2000. The other
    # three factorial arguments in the pair have nonzero imaginary
    # parts (H_u>H_t), so no pole can cancel the reciprocal zero.
    assert Fraction(3, 1000)-Fraction(1, 400) == Fraction(1, 2000)
    record = {
        'status': 'certified', 'precision_bits': ctx.prec,
        'powers': [n, p], 'box_radius': str(radius),
        'center': list(map(str, centers)), 'root_box': list(map(str, box)),
        'contraction_upper': str(contraction),
        'fixed_point_image': list(map(str, images)),
        'positive_original_edges': positive_edges,
        'wire_tangent_W': str(W), 'zero_real_part': str(zero_x),
        'ray_slope_modulus_upper': '1/2',
        'zero_height': str(zero_height), 'ray_height_at_zero_real_part': str(ray_height),
        'zero_minus_ray_height': str(gap),
        'finite_reciprocal_zero': {
            'location': 'x_N=1/2-t/(2*pi)+1/(2*N)',
            'all_levels_at_least': 100,
            'height_gap_lower': '1/2000',
            'factorial_argument': '-1',
        },
        'scope': 'The selected positive (7,3) period solution has a limiting sine-argument zero strictly below the proposed W-ray, inside (1/50,12/25). The exact reciprocal-factorial zero x_N=x_0+1/(2N) is also strictly below the ray for every N>=100. This refutes only the unchanged zero-free deformation; it is not a counterexample to a volume conjecture.',
        'sha256': {
            str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in [Path(__file__).resolve(),
                         root/'notes/research_pair_truncated_ray_obstruction.md',
                         root/'notes/research_positive_edge_global_monotonicity.md',
                         root/'notes/research_radical_path_sector_gap.md',
                         root/'notes/exact_factorial_interpolation_and_complex_contours.md']
        },
    }
    output = root/'repro/results/research-pair-truncated-ray-obstruction.json'
    output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in (
        'status', 'powers', 'contraction_upper', 'zero_real_part',
        'zero_height', 'ray_height_at_zero_real_part', 'zero_minus_ray_height')}, indent=2))


if __name__ == '__main__':
    main()
