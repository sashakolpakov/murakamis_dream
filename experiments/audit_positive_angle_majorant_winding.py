#!/usr/bin/env python3
"""Positive angle norm, exact cyclic projector, and the geometric winding gap."""

import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import acb, acb_poly, arb, ctx
import numpy as np

from audit_finite_sum_annihilator import field


HERE = Path(__file__).parent


def rational_ball(q):
    q = Fraction(q)
    return arb(q.numerator)/q.denominator


def exact_characters():
    X = sp.Symbol('X')
    count = 0
    for N in range(2, 12):
        cyclotomic = sp.Poly(sp.cyclotomic_poly(N, X), X)
        for charge in range(-2*N, 3*N+1):
            polynomial = sum(X**((r*charge) % N) for r in range(N))
            remainder = sp.rem(sp.Poly(polynomial, X), cyclotomic).as_expr()
            assert remainder == (N if charge % N == 0 else 0)
            count += 1
    return {'exact_primitive_character_tests': count,
            'edge_lifts_0_N_2N_are_indistinguishable': True}


def marked_alias_gap():
    data = json.loads((HERE/'positive_alias_volume_counterexample_fixture.json').read_text())
    E = sp.Matrix(data['E'])
    full = sp.Matrix(data['steps'][-1]['gluing_rows'])
    angles = sp.Matrix([sp.Rational(v) for v in data['rational_alias_angles']])
    wind = sp.Matrix(data['winding'])
    assert E == full[:9, :]
    assert sp.kronecker_product(sp.eye(9), sp.ones(1, 3))*angles == sp.ones(9, 1)
    assert E*angles == 2*wind
    assert full[9:, :]*angles == sp.zeros(2, 1)
    assert wind == sp.Matrix([1, 1, 1, 1, 1, 1, 2, 0, 1])
    k20 = 20*angles
    assert all(v.is_Integer and 0 <= v <= 19 for v in k20)
    assert E*k20 != 40*sp.ones(9, 1)
    assert all(int(v) % 20 == 0 for v in E*k20)
    # This is a WEAK sum-N state; even full 2N characters keep it.
    assert all(int(v) % 40 == 0 for v in E*k20)
    assert any(v == 0 for v in k20)
    ctx.prec = 192
    alias = arb(0)
    for a in angles:
        if a:
            alias += (2*arb.pi()*acb(0, 1)*rational_ball(str(a))).exp().polylog(2).imag/2
    root = next(z for z in acb_poly([-1, 3, -2, 1]).roots(tol=1e-48, maxprec=512)
                if z.imag > 0)
    shapes = [sum((rational_ball(c)*root**i for i, c in enumerate(row)), acb(0))
              for row in data['steps'][0]['shape_coefficients']]
    assert all(z.imag > 0 for z in shapes)
    volume = sum((z.polylog(2).imag+(1-z).arg()*abs(z).log() for z in shapes), arb(0))
    gap = alias-volume
    assert gap > arb('.93590')
    assert alias > arb('3.76403') and volume < arb('2.82813')
    return {'tetrahedra': 9, 'integer_angle_state_at_N20': list(map(int, k20)),
            'original_marked_peripheral_rows_zero': True,
            'geometric_projector_rejects_alias': True,
            'cyclic_projector_keeps_alias': True,
            'full_2N_projector_also_keeps_THIS_WEAK_sum_N_alias': True,
            'alias_volume': str(alias), 'complete_volume': str(volume),
            'certified_volume_gap': str(gap),
            'scope': 'positive angle Gram relaxation, not a nonzero original quantum coefficient'}


def strict_and_affine_support():
    # Genuine two-tetrahedron figure-eight angle incidence: each column
    # sums to2 and there are exactly2 edges for2 tetrahedra.
    E = np.array([[2, 1, 0, 2, 1, 0], [0, 1, 2, 0, 1, 2]], dtype=int)
    assert np.all(E.sum(axis=0) == 2)
    strict, affine = 0, 0
    for N in range(2, 13):
        for charge, minimum, kind in ((N, 1, 'strict'), (N-1, 0, 'affine')):
            triples = [(a, b, charge-a-b)
                       for a in range(minimum, charge-2*minimum+1)
                       for b in range(minimum, charge-a-minimum+1)]
            for first in triples:
                for second in triples:
                    k = np.array(first+second)
                    sums = E@k
                    assert int(sum(sums)) == 4*charge
                    target = 0 if kind == 'strict' else 2*charge
                    cyclic = np.all((sums-target) % (2*N) == 0)
                    geometric = np.all(sums == 2*charge)
                    assert cyclic == geometric
                    if kind == 'strict':
                        strict += 1
                    else:
                        affine += 1
        p, _, q = field(N)
        S = np.zeros((N, N), dtype=np.int64)
        for a in range(N):
            S[(a+1) % N, a] = 1
        T = np.diag([pow(q, a, p) for a in range(N)]).astype(np.int64)
        wall = np.zeros_like(S)
        wall[0, -1] = 2
        assert np.array_equal((T@S-q*S@T) % p, wall % p)
        J = S.copy()
        J[:, -1] = 0
        assert not np.any((T@J-q*J@T) % p)
    return {'strict_angle_configurations': strict, 'affine_weak_configurations': affine,
            'strict_full_clock_equals_geometric': True,
            'affine_charge_d_full_clock_equals_geometric_even_at_zero': True,
            'actual_half_clock_wrap_tests': 11,
            'scope': 'angle-support theorem and exact head wall; no original global angle map assumed'}


def gaussian_angle_identity():
    mp.mp.dps = 90
    count, worst = 0, mp.mpf(0)
    for N in range(3, 18):
        s = [mp.mpf(1)]
        for a in range(1, N):
            s.append(s[-1]*2*mp.sin(mp.pi*a/N))
        for L in range(1, N):
            for a in range(L+1):
                coefficient = s[L]/(s[a]*s[L-a])
                angle_weight = 1/(s[a]*s[L-a]*s[N-L])
                rhs = 2*N*mp.sin(mp.pi*L/N)*angle_weight
                error = abs(coefficient-rhs)/max(1, abs(coefficient), abs(rhs))
                worst = max(worst, error)
                assert error < mp.mpf('1e-80')
                count += 1
    return {'local_exact_angle_reflection_tests': count,
            'worst_relative_error': str(worst),
            'zero_angle_endpoints_included': True}


def pointed_half_period_charge():
    rows = []
    for N in range(2, 13):
        p, _, q = field(N)
        Q = q*q % p
        X = np.diag([pow(Q, -a, p) for a in range(N)]).astype(np.int64)
        Y = np.zeros((N, N), dtype=np.int64)
        for a in range(N):
            Y[(a+1) % N, a] = 1
        Xi = np.diag([pow(Q, a, p) for a in range(N)]).astype(np.int64)
        Yi = Y.T
        Z = (X, Yi, -Xi@Y % p)
        assert np.array_equal(Z[0]@Z[1]@Z[2] % p,
                              (-Q*np.eye(N, dtype=np.int64)) % p)
        qi = pow(q, -1, p)
        zeta = tuple(qi*v % p for v in Z)
        assert np.array_equal(zeta[0]@zeta[1]@zeta[2] % p,
                              (pow(q, N-1, p)*np.eye(N, dtype=np.int64)) % p)
        for a, b in zip(Z, zeta):
            # Matrix powers are exact in the finite field.
            pa = np.eye(N, dtype=np.int64)
            pb = pa.copy()
            for _ in range(N):
                pa = pa@a % p
                pb = pb@b % p
            assert np.array_equal(pb, -pa % p)
        rows.append({'N': N, 'ordered_rescaled_triad_character_q_to_d': True,
                     'Frobenius_central_sign_flips': True})
    data = json.loads((HERE/'positive_alias_volume_counterexample_fixture.json').read_text())
    valences = [sum(row) for row in data['steps'][0]['gluing_rows'][:3]]
    assert valences == [7, 6, 5]
    for N in (3, 5, 7, 9):
        assert all((N*(N-1)//2) % N == 0 for _ in (0,))
        assert [(-1)**(v-2) for v in valences] == [-1, 1, -1]
    return {'literal_pointed_triad_checks': rows, 'actual_initial_edge_valences': valences,
            'same_geometric_center_candidate_character_fails_at_odd_valences_for_odd_N': True,
            'scope': 'a transported half-period/central-sign normalization may repair it; '
                     'actual original global edge character is not computed here'}


def main():
    out = {'status': 'PASS', 'positive_Fourier_projection': exact_characters(),
           'constructive_full_clock_support': strict_and_affine_support(),
           'marked_geometric_alias_norm_gap': marked_alias_gap(),
           'Gaussian_to_positive_angle_weight': gaussian_angle_identity(),
           'original_pointed_half_period_charge': pointed_half_period_charge(),
           'scope': 'Full-clock strict/affine angle support has sharp geometric upper rate; '
                    'weak sum-N cyclic relaxation can have an exponential gap. '
                    'No original full-source angle comparison or knot-volume counterexample.'}
    Path(__file__).with_name('positive_angle_majorant_winding_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS strict/affine full-clock support, exact half-clock wall, weak marked angle norm gap and Gaussian angle identities')


if __name__ == '__main__':
    main()
