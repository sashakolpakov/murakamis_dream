#!/usr/bin/env python3
"""Exact linear and Arb checks of the constrained positive lens chart.

The actual 8_1 field, shapes and gluing rows are those independently
certified by audit_all_radius_angular_chart. Both peripheral markings
are labeled explicitly: the MERIDIAN lens chart has rank B=3; the
LONGITUDE lens chart has rank B=4. No original quantum cycle is inferred.
"""

import argparse
import itertools
import json
from pathlib import Path

from flint import acb, acb_mat, acb_poly, arb, arb_mat, ctx
import sympy as sp

from audit_all_radius_angular_chart import ROWS, geometry, topology


def real_ball(value):
    value = sp.Rational(value)
    return arb(int(value.p))/int(value.q)


def zero_solution(matrix, rhs):
    if rhs.cols == 0:
        return sp.zeros(matrix.cols, 0)
    answer, free = matrix.gauss_jordan_solve(rhs)
    return answer.subs({v: 0 for v in free})


def reduction(A, B, units):
    t, rank = A.rows, B.rank()
    k = t-rank
    assert A.shape == B.shape == (t, t)
    assert A.row_join(B).rank() == t
    assert A*B.T == B*A.T
    basis = B.T.nullspace()
    E = sp.Matrix.vstack(*(v.T for v in basis)) if basis else sp.zeros(0, t)
    D = E*A
    assert E.rows == D.rank() == k
    assert E*B == sp.zeros(k, t)
    assert B*D.T == sp.zeros(t, k)
    assert B.nullspace() == [] or sp.Matrix.hstack(D.T, *B.nullspace()).rank() == k
    lbasis = D.nullspace()
    L = sp.Matrix.hstack(*lbasis) if lbasis else sp.zeros(t, 0)
    assert L.shape == (t, rank) and L.rank() == rank
    assert D*L == sp.zeros(k, rank)
    Y = zero_solution(B, -A*L)
    C = L.T*Y
    assert B*Y == -A*L and C == C.T
    if k and rank:
        variation = sp.Matrix(k, rank, lambda i, j: i+j+1)
        assert L.T*(Y+D.T*variation) == C
    full = zero_solution(A.row_join(B), units)
    x0, y0 = full[:t, :], full[t:, :]
    assert A*x0+B*y0 == units
    tangent = L.row_join(sp.zeros(t, k)).col_join(Y.row_join(D.T))
    assert tangent.rank() == t
    assert A.row_join(B)*tangent == sp.zeros(t, t)
    return {'A': A, 'B': B, 'units': units, 'E': E, 'D': D,
            'L': L, 'Y': Y, 'C': C, 'x0_units': x0, 'y0_units': y0,
            'rank_B': rank, 'constraint_rank': k}


def dot(row, values):
    return sum((real_ball(a)*b for a, b in zip(row, values)), acb(0))


def assert_small(value):
    assert abs(value) < arb('1e-35'), value


def evaluate_chart(data, shapes, *, exact_regular_lens=False):
    A, B, L, C = (data[key] for key in ('A', 'B', 'L', 'C'))
    t, rank = A.rows, data['rank_B']
    pi = arb.pi()
    x = [z.log() for z in shapes]
    y = [(1-1/z).log() for z in shapes]
    x0 = [acb(0, pi*real_ball(v)) for v in data['x0_units']]
    y0 = [acb(0, pi*real_ball(v)) for v in data['y0_units']]
    for j in range(t):
        assert_small(dot(A.row(j), x)+dot(B.row(j), y)
                     -acb(0, pi*real_ball(data['units'][j])))
    for j in range(data['constraint_rank']):
        assert_small(dot(data['D'].row(j), x)
                     -acb(0, pi*real_ball((data['E']*data['units'])[j])))
    if rank:
        left_inverse = (L.T*L).inv()*L.T
        xi = [dot(left_inverse.row(a), [x[j]-x0[j] for j in range(t)])
              for a in range(rank)]
    else:
        xi = []
    for j in range(t):
        assert_small(x0[j]+dot(L.row(j), xi)-x[j])
    ell_linear = [dot(L.col(a), y0) for a in range(rank)]
    for a in range(rank):
        assert_small(-dot(L.col(a), y)+dot(C.row(a), xi)+ell_linear[a])

    hessian = [[dot([L[j, a]*L[j, b] for j in range(t)],
                    [1/(1-z) for z in shapes])+real_ball(C[a, b])
                for b in range(rank)] for a in range(rank)]
    positive_minors = []
    for size in range(1, rank+1):
        minor = arb_mat([[hessian[a][b].imag for b in range(size)]
                         for a in range(size)]).det()
        assert minor > 0
        positive_minors.append(str(minor))
    for a in range(rank):
        for b in range(rank):
            direct_positive_form = sum((real_ball(L[j, a]*L[j, b])
                *shapes[j].imag/(abs(1-shapes[j])**2) for j in range(t)), arb(0))
            assert_small(hessian[a][b].imag-direct_positive_form)
    hdet = acb_mat(hessian).det() if rank else acb(1)
    assert abs(hdet) > 0
    W = sum((z.polylog(2)+xx*xx/2-acb(0, pi)*xx
             for z, xx in zip(shapes, x)), acb(0))
    W += sum((xi[a]*real_ball(C[a, b])*xi[b]/2
              for a in range(rank) for b in range(rank)), acb(0))
    W += sum((ell_linear[a]*xi[a] for a in range(rank)), acb(0))
    volume = sum((z.polylog(2).imag+xx.real*(1-z).arg()
                  for z, xx in zip(shapes, x)), arb(0))
    assert_small(W.imag-volume)
    gaps = []
    radii, geometric_angles, ell = [], [], []
    for z in shapes:
        if not exact_regular_lens:
            assert abs(z) < 1 and abs(1-z) < 1
        rr, theta, linear = abs(z), z.arg(), abs(1-z).log()
        gap = z.polylog(2).imag+linear*theta
        assert gap > 0
        assert z.polylog(2).imag/(2*pi)-rr.log() > 0
        gaps.append(gap)
        radii.append(rr); geometric_angles.append(theta); ell.append(linear)
    margin = min(float(gap) for gap in gaps)/2
    margin_ball = arb(str(margin))
    assert all(gap > margin_ball for gap in gaps)

    # Check the fixed-radius separable identity at genuine affine
    # angle points, without asserting that the whole phase is concave
    # on the lower half of the lifted box.
    comparisons = 0
    if rank:
        for turn in range(1, 8):
            shift = [sp.Rational((-1)**(a+turn), 100+turn) for a in range(rank)]
            shifted_xi = [xx+acb(0, real_ball(s)) for xx, s in zip(xi, shift)]
            shifted_x = [x0[j]+dot(L.row(j), shifted_xi) for j in range(t)]
            shifted_W = sum((xx.exp().polylog(2)+xx*xx/2-acb(0, pi)*xx
                             for xx in shifted_x), acb(0))
            shifted_W += sum((shifted_xi[a]*real_ball(C[a, b])*shifted_xi[b]/2
                              for a in range(rank) for b in range(rank)), acb(0))
            shifted_W += sum((ell_linear[a]*shifted_xi[a] for a in range(rank)), acb(0))
            f_difference = sum((xx.exp().polylog(2).imag+linear*xx.imag
                                -(z.polylog(2).imag+linear*angle)
                                for xx, z, linear, angle in
                                zip(shifted_x, shapes, ell, geometric_angles)), arb(0))
            assert_small(shifted_W.imag-W.imag-f_difference)
            assert shifted_W.imag < W.imag
            comparisons += 1
    return {'rank_B': rank, 'constraint_rank': data['constraint_rank'],
            'constraints_D': str(data['D']), 'basis_L': str(L),
            'symmetric_C': str(C), 'x0_in_pi_i_units': str(data['x0_units']),
            'y0_in_pi_i_units': str(data['y0_units']),
            'marked_critical_equations': True, 'entire_affine_relation': True,
            'volume_and_critical_imaginary_action': str(volume),
            'positive_hessian_leading_minors': positive_minors,
            'nonzero_complex_hessian_determinant': str(hdet),
            'coordinate_endpoint_gaps': list(map(str, gaps)),
            'rigorous_common_relative_boundary_gap': str(margin_ball),
            'constrained_separable_phase_checks': comparisons,
            'zero_dimensional_boundary_empty': rank == 0}


def actual_lens_charts():
    # The existing audit checks the polynomial-field gluing products
    # exactly, all complete logarithmic marks, and subunit obstructions.
    old_certificate = geometry()
    root = next(z for z in acb_poly([1, 3, 6, 4, 5, 1, 1]).roots(tol=1e-48, maxprec=512)
                if arb('1.77') < z.imag < arb('1.78'))
    a = -(root*root+root+1)/(root*root+2)
    original = [a, a**(-2), root, root, 1/(1-root)]
    triples = [[z, 1/(1-z), 1-1/z] for z in original]
    lens = [[j for j, z in enumerate(triple) if abs(z) < 1 and abs(1-z) < 1]
            for triple in triples]
    assert lens == [[1], [1], [1], [1], [0]]
    rotations = [choices[0] for choices in lens]
    shapes = [triple[j] for triple, j in zip(triples, rotations)]
    original_volume = sum((z.polylog(2).imag+abs(z).log()*(1-z).arg()
                           for z in original), arb(0))
    lens_volume = sum((z.polylog(2).imag+abs(z).log()*(1-z).arg()
                       for z in shapes), arb(0))
    assert_small(lens_volume-original_volume)
    output = []
    for peripheral, label, expected_rank in ((5, 'original_meridian', 3), (6, 'longitude', 4)):
        selected = [0, 1, 2, 3, peripheral]
        rows = [ROWS[j] for j in selected]
        A = sp.Matrix([[row[3*j+rotations[j]]-row[3*j+(rotations[j]+1) % 3]
                        for j in range(5)] for row in rows])
        B = sp.Matrix([[row[3*j+(rotations[j]+2) % 3]-row[3*j+(rotations[j]+1) % 3]
                        for j in range(5)] for row in rows])
        units = sp.Matrix([(2 if index < 5 else 0)
                            -sum(row[3*j+(rotations[j]+1) % 3] for j in range(5))
                            for index, row in zip(selected, rows)])
        assert B.rank() == expected_rank
        data = reduction(A, B, units)
        certificate = evaluate_chart(data, shapes)
        certificate.update({'peripheral_mark': label, 'selected_rows': selected,
                            'lens_rotations': rotations})
        output.append(certificate)
    return {'exact_field_and_complete_gluings': old_certificate,
            'unique_lens_rotation': rotations,
            'volume_original_positive_triangulation': str(original_volume),
            'cyclic_quad_regulator_calibration': True, 'charts': output}


def all_rank_linear_models():
    t = 5
    coordinate = sp.eye(t)
    row_change = sp.eye(t)
    for i in range(t):
        for j in range(i+1, t):
            coordinate[i, j] = j-i
            row_change[j, i] = 1
    assert coordinate.det() == row_change.det() == 1
    z = acb(arb(1)/2, arb(3).sqrt()/2)
    shapes = [z]*t
    results = []
    for rank in range(t+1):
        S = sp.Matrix(rank, rank, lambda i, j: (i+j) % 3-1)
        A0 = sp.diag(S, sp.eye(t-rank)) if rank else sp.eye(t)
        B0 = sp.diag(sp.eye(rank), sp.zeros(t-rank)) if rank else sp.zeros(t)
        A = row_change*A0*coordinate.inv()
        B = row_change*B0*coordinate.T
        units = (A+B)*sp.ones(t, 1)/3
        assert B.rank() == rank
        data = reduction(A, B, units)
        certificate = evaluate_chart(data, shapes, exact_regular_lens=True)
        certificate['scope'] = 'Synthetic rational Lagrangian data, not an asserted knot triangulation.'
        results.append(certificate)
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topology', action='store_true')
    args = parser.parse_args()
    ctx.prec = 192
    result = {'status': 'PASS', 'actual_lens_geometry': actual_lens_charts(),
              'synthetic_all_rank_models': all_rank_linear_models(),
              'scope': 'Constrained classical reference chart and Gaussian; original quantum/source cycle not identified.'}
    if args.topology:
        result['topology'] = topology()
    Path(__file__).with_name('constrained_lens_geometric_chart_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS exact 8_1 lens charts: original-meridian rank B=3, longitude rank B=4; '
          'six synthetic ranks 0..5; critical/volume/Hessian/gap certificates')


if __name__ == '__main__':
    main()
