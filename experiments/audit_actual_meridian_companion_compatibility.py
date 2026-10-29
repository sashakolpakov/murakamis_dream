#!/usr/bin/env python3
"""Actual meridian orbit, highest residual, full line and source-rank audit.

No replacement states: all Laurent inputs are literal actual trefoil or
figure-eight cut sums. The affine-source construction is the existing
regular-period theorem, with the known zero-complete interpolation.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field
from audit_regularized_kashaev_period import actual_laurent_period, add_poly, evaluate, multiply_poly


def inverse(A, p):
    return np.array(sp.Matrix(A.tolist()).inv_mod(p), dtype=np.int64) % p


def divide_laurent_S(polynomial, N, p):
    low = min([0]+list(polynomial))
    dividend = {e-low: c for e, c in polynomial.items()}
    quotient = {}
    while dividend and max(dividend) >= N-1:
        exponent = max(dividend)-(N-1)
        scalar = dividend[max(dividend)]
        add_poly(quotient, {exponent+low: scalar}, p)
        add_poly(dividend, {r: 1 for r in range(N)}, p, exponent, -scalar)
    assert not dividend
    return quotient


def actual_case(N, strands, word):
    p, eta = root_field(N)
    q, Q = pow(eta, 2, p), pow(eta, 4, p)
    F = actual_laurent_period(N, p, q, strands, word)
    roots = [pow(Q, j, p) for j in range(N)]
    f0 = np.array([evaluate(F, y, p) for y in roots], dtype=np.int64)
    assert f0[1] == 1
    B = np.diag(roots)
    assert int(((B-np.eye(N, dtype=np.int64))@f0 % p)[1]) == (Q-1) % p
    P = np.zeros((N, N), dtype=np.int64)
    for j in range(N):
        P[(j+1) % N, j] = 1
    e0row = np.eye(N, dtype=np.int64)[0, :]
    assert not np.array_equal(e0row@P % p, e0row)
    # Existing P_N ordinary interpolant; c_N additionally vanishes at1.
    PN = {}
    invN = pow(N, -1, p)
    for j in range(1, N):
        z, value = roots[j], int(f0[j])
        for r in range(N-1):
            add_poly(PN, {r: value*(pow(z, -r, p)-z)*invN}, p)
    P1 = evaluate(PN, 1, p)
    c = PN.copy()
    add_poly(c, {r: 1 for r in range(N)}, p, multiplier=-P1*invN)
    residual = F.copy()
    add_poly(residual, c, p, multiplier=-1)
    H = divide_laurent_S(residual, N, p)
    assert evaluate(c, 1, p) == 0
    assert N*evaluate(H, 1, p) % p == int(f0[0])
    for j, root in enumerate(roots):
        target = int(f0[0]) if j == 0 else 0
        assert evaluate(residual, root, p) == target
        assert evaluate(c, root, p) == (0 if j == 0 else int(f0[j]))
    # Generic orbit: ratio line has norm1 and its horizontal source is fixed,
    # so the state is not a rank-N cyclic source for that transport.
    chosen = None
    for M in range(2, p):
        y = M*M % p
        U = pow(y, N, p)
        values = np.array([evaluate(F, pow(Q, j, p)*y % p, p) for j in range(N)], dtype=np.int64)
        if U != 1 and all(int(v) for v in values):
            chosen = M, y, U, values
            break
    assert chosen is not None
    M, y, U, values = chosen
    ratios = [int(values[(j+1) % N])*pow(int(values[j]), -1, p) % p for j in range(N)]
    norm = 1
    for a in ratios:
        norm = norm*a % p
    assert norm == 1
    forward = P.T
    D = np.diag(values)
    horizontal = D@forward@inverse(D, p) % p
    assert np.array_equal(horizontal@values % p, values)
    power = np.eye(N, dtype=np.int64)
    for _ in range(N):
        power = horizontal@power % p
    assert np.array_equal(power, np.eye(N, dtype=np.int64))
    # Same complete full line and anchor residue, never reset to1/N.
    epsilon = pow(pow(eta, N, p), N+3, p)
    regular_normal = epsilon*int(f0[0])*invN % p
    # Residual derivative is not the full normal; keep the actual zero
    # of (y-1)F until differentiating y=U^(1/N).
    full_regular_numerator = multiply_poly(F, {0: -1, 1: 1}, p)
    assert evaluate(full_regular_numerator, 1, p) == 0
    assert epsilon*evaluate(full_regular_numerator, 1, p, derivative=True)*invN % p == regular_normal
    anchorM = -q % p
    anchor_residue = epsilon*pow(anchorM, N-1, p)*(Q-1) % p
    assert anchor_residue == epsilon*pow(-1, N, p)*(q-pow(q, -1, p)) % p
    full_values = []
    for j in range(N+1):
        pointM = pow(q, j, p)*M % p
        pointy = pointM*pointM % p
        S = sum(pow(pointy, r, p) for r in range(N)) % p
        full_values.append(epsilon*pow(pointM, N-1, p)*evaluate(F, pointy, p)*pow(S, -1, p) % p)
    fullnorm = 1
    for j in range(N):
        fullnorm = fullnorm*full_values[j+1]*pow(full_values[j], -1, p) % p
    assert fullnorm == pow(-1, N-1, p)
    return {'N': N, 'strands': strands, 'word': word,
            'actual_highest_clock_failure_at_anchor': int((Q-1) % p),
            'actual_delta_residual_pairing': int(f0[0]),
            'whole_F_equals_c_plus_S_H_and_K_equals_N_H1': True,
            'generic_actual_ratio_norm_one': True,
            'ratio_horizontal_vector_orbit_dimension': 1,
            'full_parity_norm_and_anchor_residue_retained': True,
            'full_complete_U_normal': int(regular_normal)}


def figure_eight_nonresonance(N):
    p, eta = root_field(N)
    Q = pow(eta, 4, p)

    def coefficients(y):
        middle = (Q*Q*y*y-Q*y**4+Q*y**3+Q*y-Q+y*y) % p
        return (y*y*(Q-y)*(Q*y*y-1) % p,
                -(y-1)**2*(y+1)*middle % p,
                y*y*(Q*y-1)*(Q-y*y) % p,
                y*(y+1)*(Q-y*y)*(Q*y*y-1) % p)

    for y in range(2, p):
        H, Uaug = np.eye(2, dtype=np.int64), np.eye(3, dtype=np.int64)
        U = pow(y, N, p)
        gamma = (3-U-pow(U, -1, p)) % p
        if U == 1 or gamma == 0:
            continue
        okay = True
        for j in range(N):
            point = pow(Q, j+1, p)*y % p
            cm, c0, cp, D = coefficients(point)
            if not cp:
                okay = False
                break
            C = np.array([[0, 1], [-cm*pow(cp, -1, p) % p,
                                   -c0*pow(cp, -1, p) % p]], dtype=np.int64)
            aug = np.eye(3, dtype=np.int64)
            aug[:2, :2] = C
            aug[1, 2] = D*gamma*pow(cp, -1, p) % p
            H, Uaug = C@H % p, aug@Uaug % p
        if not okay or int(sp.Matrix((np.eye(2, dtype=np.int64)-H).tolist()).det()) % p == 0:
            continue
        # The source eigen1 is simple; no assertion at the specialU1.
        z = sp.symbols('z')
        value = sp.Poly(sp.Matrix(Uaug.tolist()).charpoly(z).as_expr(), z, modulus=p)
        assert value.eval(1) % p == 0 and value.diff().eval(1) % p != 0
        return {'N': N, 'generic_U': int(U), 'actual_source_factor': int(gamma),
                'rank_two_homogeneous_nonresonance': True,
                'rank_three_augmented_simple_one': True,
                'complete_U1_nondegeneracy_not_assumed': True}
    raise AssertionError(('no generic point', N))


def main():
    actual = [actual_case(N, strands, word) for N in range(2, 6)
              for strands, word in ((2, [(0, 1)]*3),
                                    (3, [(0, 1), (1, -1)]*2))]
    prototype = [figure_eight_nonresonance(N) for N in range(2, 8)]
    result = {'status': 'PASS', 'actual_states': actual,
              'actual_figure_eight_generic_source_monodromy': prototype,
              'scope': 'Actual meridian/source compatibility and existing regularization; gates C,D,E remain open.'}
    path = Path(__file__).with_name('actual_meridian_companion_compatibility_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'actual_states': len(actual),
                      'actual_source_monodromy_levels': len(prototype),
                      'results': str(path)}, indent=2))


if __name__ == '__main__':
    main()
