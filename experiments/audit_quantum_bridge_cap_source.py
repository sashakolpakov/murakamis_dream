#!/usr/bin/env python3
"""Actual balanced turns, nilpotent cut, and all-bridge half-step sources.

Checks independent original cap matrices, actual knot cut evaluations,
symbolic central-character obstruction, and flat source systems with
arbitrary subsets. The general proofs are in quantum_bridge_cap_source.md.
No selected-period/geometric-regulator norm theorem is asserted.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import determinant, rank
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_relative_pivotal_duality import dual_data


def factorials(N, p, Q):
    values = [1]
    for a in range(1, N):
        values.append(values[-1]*(1-pow(Q, a, p)) % p)
    assert values[-1] == N % p
    return values


def cap_case(N, kind):
    p, generator, q = field(N)
    Q = q*q % p
    x = generator if kind == 'generic' else pow(q, N-1, p)
    Fs = factorials(N, p, Q)
    _, _, J, g = dual_data(N, p, q, x, 0)
    cap = np.zeros((N, N), dtype=np.int64)  # dual, primal
    cup = np.zeros_like(cap)               # primal, dual
    for a in range(N):
        b = N-1-a
        assert Fs[a]*Fs[b] % p == N*pow(-1, a, p)*pow(Q, a*(a+1)//2, p) % p
        cap[a, b] = int(J[b, a])*pow(Fs[a]*Fs[b] % p, -1, p) % p
        cup[b, a] = Fs[a]*Fs[b]*pow(int(J[b, a]), -1, p) % p
        assert int(cap[a, b]) == pow(x, a, p)*pow(N, -1, p) % p
        assert int(cup[b, a]) == N*pow(x, -a, p) % p
    assert np.array_equal(cup@cap % p, np.eye(N, dtype=np.int64))
    assert np.array_equal(cap@cup % p, np.eye(N, dtype=np.int64))
    right = g@cap.T % p                    # primal, dual
    gi = np.diag([pow(int(v), -1, p) for v in np.diag(g)])
    right_cup = cup.T@gi % p               # dual, primal
    assert np.array_equal(right@right_cup % p, np.eye(N, dtype=np.int64))
    assert np.array_equal(right_cup@right % p, np.eye(N, dtype=np.int64))

    e = np.full((N, N), pow(N, -1, p), dtype=np.int64)
    D = gi@e % p
    assert rank(D, p) == 1 and not np.any(D@D % p)
    assert np.array_equal(g@D % p, e)
    assert int(np.trace(g@D % p)) % p == 1
    assert np.array_equal(D@g@D % p, D)
    marked = D.T@right % p
    expected = np.array([[pow(x, a, p)*pow(N, -2, p) % p for a in range(N)]
                         for b in range(N)], dtype=np.int64)
    assert np.array_equal(marked, expected)
    assert int(np.sum(marked*cup)) % p == 1
    assert int(np.sum(right*cup)) % p == 0

    corners = 0
    for kappa, lam, epsilon, scalar_power in ((pow(N, -1, p), x, 1, 0),
                       (N, pow(x, -1, p), -1, 0),
                       (Q*pow(x, 1-N, p)*pow(N, -1, p) % p, Q*x % p, 1, 1-N),
                       (N*pow(x, N-1, p)*pow(Q, -1, p) % p, pow(Q*x, -1, p), -1, N-1)):
        v = np.array([kappa*pow(lam, a, p) % p for a in range(N)], dtype=np.int64)
        delta = np.roll(v, -1)-lam*v
        want = np.zeros(N, dtype=np.int64)
        want[-1] = kappa*(1-pow(lam, N, p)) % p
        assert np.array_equal(delta % p, want)
        seed = np.zeros(N, dtype=np.int64); seed[-1] = 1
        reconstructed = np.zeros(N, dtype=np.int64)
        for j in range(N):
            reconstructed = (reconstructed+kappa*pow(lam, N-1-j, p)*np.roll(seed, -j)) % p
        assert np.array_equal(v, reconstructed)
        # The rank-one torsor is the same anchored vector with its cut
        # multiplier included; test both shifts without inverting 1-lambda^N.
        internal_multiplier = np.full(N, lam, dtype=np.int64)
        internal_multiplier[-1] = pow(lam, 1-N, p)
        assert np.array_equal(np.roll(v, -1), internal_multiplier*v % p)
        assert pow(lam, N-1, p)*int(internal_multiplier[-1]) % p == 1
        meridian_multiplier = np.array([pow(q, scalar_power+epsilon*a, p) for a in range(N)], dtype=np.int64)
        advanced_lam = pow(q, epsilon, p)*lam % p
        advanced_internal = np.full(N, advanced_lam, dtype=np.int64)
        advanced_internal[-1] = pow(advanced_lam, 1-N, p)
        assert np.array_equal(np.roll(meridian_multiplier, -1)*internal_multiplier % p,
                              advanced_internal*meridian_multiplier % p)
        H = np.array([pow(q, a, p) for a in range(N)], dtype=np.int64)
        sign_at_cut = np.ones(N, dtype=np.int64); sign_at_cut[-1] = -1
        assert np.array_equal(np.roll(H, -1), q*H*sign_at_cut % p)
        corners += 1
    if kind == 'complete':
        assert (1-pow(x, N, p)) % p == (2 if N % 2 == 0 else 0)
    return {'level': N, 'color': kind, 'prime': p,
            'four_original_balanced_turns_exact': True,
            'rank_one_nilpotent_mark_and_pivotal_trace_one': True,
            'marked_cap_and_unknot_normalization_exact': True,
            'cyclic_turn_source_and_polynomial_resolvent_cases': corners,
            'same_anchored_norm_one_frame_with_full_meridian_half_step': True,
            'whole_left_cap_source_factor': (1-pow(x, N, p)) % p}


def channel_indices(k):
    values = [(0, 0)]
    values.extend((mask, parity) for mask in range(1, 1 << k) for parity in (0, 1))
    assert len(values) == (1 << (k+1))-1
    return values, {key: i for i, key in enumerate(values)}


def internal(N, p, q, x, clocks, signs, offsets, indices, lookup, i):
    r = len(indices)
    mat = np.zeros((r, r), dtype=np.int64)
    for j, (mask, parity) in enumerate(indices):
        if not mask & (1 << i):
            mat[j, j] = 1
            continue
        lam = pow(q, offsets[i]+parity*signs[i], p)*pow(x, signs[i], p) % p
        mat[j, j] = lam
        if clocks[i] == N-1:
            reduced = mask & ~(1 << i)
            dest = (reduced, parity) if reduced else (0, 0)
            mat[j, lookup[dest]] = (1-pow(lam, N, p)) % p
    return mat


def half_step(N, p, q, clocks, signs, scalar_power, indices, lookup):
    Q = q*q % p
    mat = np.zeros((len(indices), len(indices)), dtype=np.int64)
    scalar = pow(q, scalar_power, p)
    mat[0, 0] = scalar
    for j, (mask, parity) in enumerate(indices[1:], start=1):
        if parity == 0:
            mat[j, lookup[(mask, 1)]] = scalar
        else:
            exponent = sum(signs[i]*clocks[i] for i in range(len(clocks)) if mask & (1 << i))
            mat[j, lookup[(mask, 0)]] = scalar*pow(Q, exponent, p) % p
    return mat


def section(N, p, q, x, clocks, signs, offsets, scalar_power, indices):
    kappa = pow(x, scalar_power, p)
    values = []
    for mask, parity in indices:
        v = kappa
        for i in range(len(clocks)):
            if mask & (1 << i):
                lam = pow(q, offsets[i]+parity*signs[i], p)*pow(x, signs[i], p) % p
                v = v*pow(lam, clocks[i], p) % p
        values.append(v)
    return np.array(values, dtype=np.int64)


def flat_cube_case(N, k, kind):
    p, generator, q = field(N)
    x = generator if kind == 'generic' else pow(q, N-1, p)
    signs = [1 if i % 2 == 0 else -1 for i in range(k)]
    offsets = [2*i for i in range(k)]
    scalar_power = 1-N
    indices, lookup = channel_indices(k)
    clock_samples = {tuple([0]*k), tuple([N-1]*k), tuple([N//2]*k)}
    clock_samples.update(tuple(N-1 if i == j else (j+i) % N for i in range(k)) for j in range(k))
    checks = 0
    for clocks in sorted(clock_samples):
        state = section(N, p, q, x, clocks, signs, offsets, scalar_power, indices)
        meridian = half_step(N, p, q, clocks, signs, scalar_power, indices, lookup)
        expected_det = -pow(q, scalar_power*len(indices), p)
        for i in range(k):
            expected_det = expected_det*pow(q*q % p, clocks[i]*signs[i]*(1 << (k-1)), p) % p
        assert determinant(meridian, p) == expected_det % p
        meridian_period = np.eye(len(indices), dtype=np.int64)
        for _ in range(2*N):
            meridian_period = meridian@meridian_period % p
        assert np.array_equal(meridian_period, np.eye(len(indices), dtype=np.int64))
        changed = section(N, p, q, q*x % p, clocks, signs, offsets, scalar_power, indices)
        assert np.array_equal(meridian@state % p, changed)
        for i in range(k):
            advanced = list(clocks); advanced[i] = (advanced[i]+1) % N
            B = internal(N, p, q, x, clocks, signs, offsets, indices, lookup, i)
            B_delta = internal(N, p, q, q*x % p, clocks, signs, offsets, indices, lookup, i)
            lam0 = pow(q, offsets[i], p)*pow(x, signs[i], p) % p
            assert determinant(B, p) == pow(pow(q, signs[i], p)*lam0*lam0 % p, 1 << (k-1), p)
            shifted_meridian = half_step(N, p, q, advanced, signs, scalar_power, indices, lookup)
            assert np.array_equal(shifted_meridian@B % p, B_delta@meridian % p)
            assert np.array_equal(B@state % p,
                                  section(N, p, q, x, advanced, signs, offsets, scalar_power, indices))
            # Other-direction coefficients are unchanged by the i shift.
            for j in range(i):
                C = internal(N, p, q, x, clocks, signs, offsets, indices, lookup, j)
                assert np.array_equal(B@C % p, C@B % p)
            # Inspect the actual internal orbit, including both corner sources.
            H = np.eye(len(indices), dtype=np.int64)
            for step in range(N):
                rotated = list(clocks); rotated[i] = (rotated[i]+step) % N
                H = internal(N, p, q, x, rotated, signs, offsets, indices, lookup, i)@H % p
            expected_diag = []
            for mask, parity in indices:
                if mask & (1 << i):
                    lam = pow(q, offsets[i]+parity*signs[i], p)*pow(x, signs[i], p) % p
                    expected_diag.append(pow(lam, N, p))
                else:
                    expected_diag.append(1)
            assert np.array_equal(np.diag(H), expected_diag)
            assert np.array_equal(H@state % p, state)
            checks += 1
    return {'level': N, 'bridges': k, 'color': kind,
            'source_channels': len(indices), 'mixed_half_step_squares': checks,
            'all_internal_squares_and_selected_sections': True,
            'unit_determinant_characters_and_full_meridian_orbit': True,
            'both_bulk_monodromy_signs_and_corner_divisors_retained': True}


def actual_marked_cut(N, kind):
    p, generator, q = field(N); Q = q*q % p
    x = generator if kind == 'generic' else pow(q, N-1, p)
    Fs = factorials(N, p, Q)
    positive, negative, g, theta = data = color_matrices(N, p, q, x)
    basis = np.array([pow(Fs[a]*Fs[b] % p*Fs[c] % p, -1, p)
                      for a, b, c in product(range(N), repeat=3)], dtype=np.int64)
    basis_inverse = np.array([pow(int(v), -1, p) for v in basis], dtype=np.int64)
    eye = np.eye(N, dtype=np.int64)
    records = []
    for word in WORDS[:2]:
        B = np.eye(N**3, dtype=np.int64)
        for position, sign in word:
            crossing = positive if sign > 0 else negative
            local = np.kron(crossing, eye) if position == 0 else np.kron(eye, crossing)
            B = B@local % p
        balanced = basis_inverse[:, None]*B % p*basis[None, :] % p
        source_e = np.full((N, N), pow(N, -1, p), dtype=np.int64)
        # g D=e exactly, so this is the full pivotal closure with the mark.
        closing = np.kron(source_e, np.kron(g, g))
        value = int(np.sum(closing*balanced.T)) % p
        value = value*pow(theta, -sum(sign for _, sign in word), p) % p
        expected = reduced_period(N, p, *data, word)
        assert value == expected
        ordinary = np.kron(g, np.kron(g, g))
        assert int(np.sum(ordinary*balanced.T)) % p == 0
        records.append({'word': word, 'actual_reduced_value': value,
                        'marked_balanced_closure_equals_original_cut': True,
                        'unmarked_closure_zero': True})
    return {'level': N, 'color': kind, 'original_knots': records}


def symbolic_certificates():
    z, X, k, N = sp.symbols('z X k N')
    obstruction = sp.expand((z-X)*(z-1)-(z+X)*(z-1))
    assert sp.expand(obstruction+2*X*(z-1)) == 0
    assert sp.simplify(k-(k-1)-2) == -1
    assert sp.simplify(sp.Rational(3, 2)*k-sp.Rational(1, 2)*(k-1)-1) == k-sp.Rational(1, 2)
    # Generic one-cap flatness using e A=Q^-1 e as a quotient relation.
    q, A, e, x = sp.symbols('q A e x', nonzero=True)
    BT = sp.Matrix([[x, 0, (1-X)*e], [0, q*x, (1+X)*e], [0, 0, 1]])
    Bdelta = sp.Matrix([[0, 1, 0], [A, 0, 0], [0, 0, 1]])
    shifted = Bdelta.subs(A, q*q*A)
    delta_BT = BT.subs({x: q*x, X: -X}, simultaneous=True)
    diff = sp.expand(shifted*BT-delta_BT*Bdelta)
    for entry in diff:
        assert sp.rem(sp.together(entry).as_numer_denom()[0], q*q*A*e-e, A) == 0
    # Independent physical Borel products of an actual principal cup.
    U, momentum = sp.symbols('U momentum', nonzero=True)
    def borel(color, position, p):
        K = color/position
        ee = (1-color**2/position)*p/color
        f = (1-position)/p
        return sp.Matrix([[K, ee], [0, 1]]), sp.Matrix([[1, 0], [-K*f, K]])
    primal_plus, primal_minus = borel(x, U, momentum)
    dual_plus, dual_minus = borel(1/x, 1/U, momentum/x)
    assert (dual_plus*primal_plus-sp.eye(2)).applyfunc(sp.cancel) == sp.zeros(2)
    assert (dual_minus*primal_minus-sp.eye(2)).applyfunc(sp.cancel) == sp.zeros(2)
    G = primal_minus.inv()*primal_plus
    flag = sp.Matrix([1, 1])
    assert (G.subs(momentum, 1)*flag-flag/x).applyfunc(sp.cancel) == sp.zeros(2, 1)
    u = sp.Symbol('u')
    peripheral = sp.series(N*sp.sinh(u)/sp.sinh(N*u), u, 0, 9).removeO().expand()
    degrees = []
    for j in range(9):
        coeff = sp.cancel(peripheral.coeff(u, j))
        if j % 2:
            assert coeff == 0
        elif coeff:
            degree = int(sp.Poly(coeff, N).degree())
            assert degree <= j
            degrees.append({'jet_order': j, 'degree_in_level_after_multiplication_by_N': degree})
    return {'rank_two_half_step_obstruction_polynomial': str(obstruction),
            'generic_three_channel_flatness_modulo_exact_corner_relation': True,
            'actual_principal_cap_has_both_inverse_Borel_products': True,
            'marked_cap_selects_the_original_inverse_eigenflag': True,
            'arbitrary_bridge_normalization_power': -1,
            'boundary_norm_power': str(k-sp.Rational(1, 2)),
            'whole_peripheral_germ_jet_bounds': degrees}


def main():
    symbolic = symbolic_certificates()
    caps = [cap_case(N, kind) for N in range(2, 17) for kind in ('generic', 'complete')]
    cubes = [flat_cube_case(N, k, kind) for N in range(2, 13)
             for k in range(1, 5) for kind in ('generic', 'complete')]
    cuts = [actual_marked_cut(N, kind) for N in range(2, 7) for kind in ('generic', 'complete')]
    out = {'scope': 'Actual quantum boundary source and half-step transport for arbitrary bridges. Full geometric source comparison and selected volume norm remain unproved.',
           'symbolic_certificates': symbolic, 'original_balanced_caps': caps,
           'simultaneous_bridge_source_systems': cubes, 'original_marked_quantum_closures': cuts}
    path = Path(__file__).with_name('quantum_bridge_cap_source_results.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'results': str(path), 'original_balanced_cap_cases': len(caps),
                      'flat_simultaneous_bridge_cases': len(cubes),
                      'mixed_half_step_squares': sum(r['mixed_half_step_squares'] for r in cubes),
                      'original_marked_knot_closures': sum(len(r['original_knots']) for r in cuts)}, indent=2))


if __name__ == '__main__':
    main()
