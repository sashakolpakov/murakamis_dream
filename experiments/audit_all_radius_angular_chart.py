#!/usr/bin/env python3
"""Certify the all-radius angular chart and exact 8_1 subunit obstruction."""

import argparse
import itertools
import json
from pathlib import Path

from flint import acb, acb_poly, arb, ctx
import mpmath as mp
import sympy as sp


ROWS = [
    [2,0,0, 1,0,0, 0,0,0, 0,0,0, 0,0,0],
    [0,2,1, 0,0,2, 0,1,0, 0,1,0, 0,0,0],
    [0,0,1, 0,2,0, 0,1,1, 0,1,1, 0,2,1],
    [0,0,0, 1,0,0, 1,0,0, 1,0,0, 0,0,1],
    [0,0,0, 0,0,0, 1,0,1, 1,0,1, 2,0,0],
    [0,0,0, 0,-1,-1, 1,0,0, 1,-1,0, 0,-1,0],
    [0,0,0, 1,-1,-1, 3,0,-1, 0,-3,0, 0,-2,0],
]
GLUINGS = [
    [[0,1,1,0], [[3,2,0,1],[0,1,3,2],[3,2,0,1],[2,3,1,0]]],
    [[0,0,3,2], [[2,3,1,0],[0,1,3,2],[0,1,3,2],[0,1,3,2]]],
    [[3,4,1,4], [[1,2,3,0],[0,1,3,2],[0,1,3,2],[1,2,3,0]]],
    [[4,2,4,1], [[2,3,1,0],[3,0,1,2],[1,2,3,0],[0,1,3,2]]],
    [[2,2,3,3], [[3,0,1,2],[0,1,3,2],[3,2,0,1],[3,0,1,2]]],
]


def geometry():
    ctx.prec = 192
    b = sp.symbols('b')
    P = b**6+b**5+5*b**4+4*b**3+6*b**2+3*b+1

    def red(expr):
        numerator, denominator = sp.fraction(sp.cancel(expr))
        return sp.rem(sp.rem(numerator, P, b)*sp.invert(denominator, P, b), P, b)

    a = -(b*b+b+1)/(b*b+2)
    assert red(a*a-b**3) == 0
    symbolic = [a, a**(-2), b, b, 1/(1-b)]
    triples = [[red(z), red(1/(1-z)), red(1-1/z)] for z in symbolic]
    flat = sum(triples, [])
    for row in ROWS:
        value = sp.Integer(1)
        for z, power in zip(flat, row):
            if power:
                value = red(value*red(z**power))
        assert value == 1

    root = next(z for z in acb_poly([1,3,6,4,5,1,1]).roots(tol=1e-48, maxprec=512)
                if arb('1.77') < z.imag < arb('1.78'))
    assert arb('-.036') < root.real < arb('-.035')
    ar = -(root*root+root+1)/(root*root+2)
    shapes = [ar, ar**(-2), root, root, 1/(1-root)]
    assert all(z.imag > 0 for z in shapes)
    qt = [[z, 1/(1-z), 1-1/z] for z in shapes]
    logs = sum([[z.log() for z in triple] for triple in qt], [])
    for j, row in enumerate(ROWS):
        total = sum((c*v for c, v in zip(row, logs)), acb(0))
        assert abs(total.real) < arb('1e-35')
        target = 2*arb.pi() if j < 5 else arb(0)
        assert abs(total.imag-target) < arb('1e-35')

    options = [[j for j, z in enumerate(triple) if abs(z) < 1] for triple in qt]
    assert options == [[1], [0,1], [1], [1], [0]]
    assert all(abs(z) < 1 or abs(z) > 1 for triple in qt for z in triple)
    witness = sp.Matrix([0,0,1,1,-2])
    obstruction = []
    for rotations in itertools.product(*options):
        B = sp.Matrix([[row[3*j+(2+rotations[j]) % 3]-row[3*j+(1+rotations[j]) % 3]
                        for j in range(5)] for row in ROWS])
        assert B*witness == sp.zeros(7, 1)
        assert B.rank() == 4
        obstruction.append({'quad_rotations': list(rotations), 'full_B_rank': 4,
                            'common_kernel': list(map(int, witness))})

    rotations = [0,1,0,0,0]
    selected = sp.Matrix(ROWS)[[0,1,2,3,5], :]
    A = sp.Matrix([[row[3*j+rotations[j]]-row[3*j+(1+rotations[j]) % 3]
                    for j in range(5)] for row in selected.tolist()])
    B = sp.Matrix([[row[3*j+(2+rotations[j]) % 3]-row[3*j+(1+rotations[j]) % 3]
                    for j in range(5)] for row in selected.tolist()])
    assert B.det() == 1
    C = B.inv()*A
    assert C == C.T
    positive = [qt[j][rotation] for j, rotation in enumerate(rotations)]
    rho = [abs(z).log() for z in positive]
    L = [abs(1-z).log() for z in positive]
    for j in range(5):
        linear = sum(((int(j == k)-int(C[j,k]))*rho[k] for k in range(5)), arb(0))
        # C happens integral in this det-one chart.
        assert abs(linear-L[j]) < arb('1e-35')
    gaps = []
    for z, rlog, ell in zip(positive, rho, L):
        mu = rlog if rlog > 0 else arb(0)
        assert ell < mu or ell > mu
        threshold = mu if ell < mu else ell
        value = z.polylog(2).imag + ell*z.arg()
        gap = value-arb.pi()*threshold
        assert gap > 0
        gaps.append({'radius_log': str(rlog), 'L': str(ell),
                     'lift': '[0,2pi]' if ell < mu else '[-pi,pi]',
                     'positive_endpoint_gap': str(gap)})
    return {'field_polynomial': str(P), 'isolated_upper_root': str(root),
            'positive_complete_geometry_certified': True,
            'all_edge_and_both_peripheral_products_exact': True,
            'all_subunit_polarizations': obstruction,
            'nonsingular_positive_quad_chart': rotations,
            'det_B': 1, 'angular_boundary_gaps': gaps}


def angular_samples():
    mp.mp.dps = 65
    count = 0
    for r in map(mp.mpf, ['.15','.7','1','1.4','3']):
        for star in map(mp.mpf, ['.2','.7','1.4','2.4','2.9']):
            ell = mp.log(abs(1-r*mp.exp(1j*star)))
            mu = max(mp.mpf(0), mp.log(r))
            left, right = (mp.mpf(0),2*mp.pi) if ell <= mu else (-mp.pi,mp.pi)
            def value(theta):
                if abs(theta) < mp.mpf('1e-55'):
                    return mp.pi*mu
                ans = mp.im(mp.polylog(2, r*mp.exp(1j*theta)))+ell*theta
                if r > 1 and theta < 0:
                    ans += 2*mp.pi*mp.log(r)
                return ans
            peak = value(star)
            gap = peak-mp.pi*max(ell,mu)
            assert gap > 0
            for j in range(1, 160):
                theta = left+(right-left)*j/160
                assert value(theta) <= peak+mp.mpf('1e-55')
            count += 1
    return {'radii_and_angles': count, 'samples_per_interval': 159,
            'scope': 'supplementary diagnostics; theorem proved by derivative and endpoint formulas'}


def topology():
    import snappy
    M, knot = snappy.Manifold('m074'), snappy.Manifold('8_1')
    assert [list(map(int, row)) for row in M.gluing_equations()] == ROWS
    raw = [[list(adj), [list(p) for p in permutations]]
           for adj, permutations in M._get_tetrahedra_gluing_data()]
    assert raw == GLUINGS
    iso = M.isomorphisms_to(knot)
    assert iso
    maps = [f.cusp_maps()[0] for f in iso]
    assert any(int(A[0,0]) in (-1,1) and int(A[1,0]) == 0 for A in maps)
    return {'combinatorial_isomorphism_to_8_1': True,
            'meridian_preserved_up_to_sign': True,
            'isosig': M.triangulation_isosig(decorated=False)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topology', action='store_true')
    args = parser.parse_args()
    result = {'status': 'PASS', 'geometry_and_polarization': geometry(),
              'angular_samples': angular_samples(),
              'scope': 'Reference lifted angular geometric cycle and exact polarization obstruction; original selected cycle not identified.'}
    if args.topology:
        result['topology'] = topology()
    Path(__file__).with_name('all_radius_angular_chart_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'exact_complete_knots': 1,
                      'subunit_polarization_obstructions': 2,
                      'certified_positive_angular_gaps': 5,
                      'angular_sample_cases': 25, 'topology': args.topology}))


if __name__ == '__main__':
    main()
