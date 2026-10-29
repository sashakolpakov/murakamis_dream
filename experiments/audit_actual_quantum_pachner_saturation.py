#!/usr/bin/env python3
"""Actual middle-certificate quantum saturation, its current and whole source.

The boundary projector is kept. The classical cleared relation alone is
tested separately and is source-visible. Exact tests include finite normal
jets without assuming the off-root cyclic q-torus identities.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_shared_quantum_flags import head, shift, mm, euler, equal
from audit_actual_rogers_bridge_transport import crossing
from audit_actual_borel_regular_fusion import inv
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def exact_two_source():
    """The classical relation is not null for the actual original cup."""
    i = sp.I
    eye = sp.eye(2)
    identity = sp.eye(4)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -1], [1, 0]])
    X = i*sp.kronecker_product(s1, s2)
    Z = sp.kronecker_product(sp.diag(1, -1), eye)
    E0 = sp.kronecker_product(sp.diag(1, 0), eye)
    w = (identity-X)*(identity-Z)
    H = identity-w
    u = identity-X*(identity-E0)*H.inv()
    v = identity-Z*H.inv()
    bare = u*v-w*(identity-u)*(identity-v)
    current = (u*w-w*u)*(identity-v)
    cup = sp.Matrix([0, -2*i, 2, 0])
    marker = sp.Matrix([[1, i, 1, i]])/4
    assert sp.simplify((marker*bare*cup)[0]) == 1
    assert sp.simplify((marker*current*cup)[0]) == -1
    return {'N': 2, 'original_bare_relation_source': '1',
            'retained_commutator_current_source': '-1'}


def series_mul(a, b, p):
    order = len(a)
    return [sum((mm(a[j], b[k-j], p) for j in range(k+1)), np.zeros_like(a[0])) % p
            for k in range(order)]


def series_inverse(a, p):
    ai = [inv(a[0], p)]
    for k in range(1, len(a)):
        value = sum((mm(a[j], ai[k-j], p) for j in range(1, k+1)), np.zeros_like(a[0])) % p
        ai.append(-mm(ai[0], value, p) % p)
    return ai


def series_add(*pairs):
    return [sum((sign*value[k] for sign, value in pairs), np.zeros_like(pairs[0][1][0]))
            for k in range(len(pairs[0][1]))]


def normal_jets(X, Z, E0, p, order=5):
    size = X.shape[0]
    eye = np.eye(size, dtype=np.int64)
    zeros = [np.zeros_like(eye) for _ in range(order)]
    ids = [eye]+zeros[1:]
    # General off-torus perturbations are intentional: only E0(1-Z)=0
    # and invertibility of the root H are used in the all-jet theorem.
    perturb = np.diag(np.arange(1, size+1, dtype=np.int64))
    perturb_z = np.diag(np.arange(size, dtype=np.int64))
    perturb_z = (eye-E0)@perturb_z % p
    Xs = [X, perturb]+zeros[2:]
    Zs = [Z, perturb_z]+zeros[2:]
    x, y = series_add((1, ids), (-1, Xs)), series_add((1, ids), (-1, Zs))
    w = series_mul(x, y, p)
    H = series_add((1, ids), (-1, w))
    Hi = series_inverse(H, p)
    K = series_mul(Xs, [eye-E0]+zeros[1:], p)
    u = series_add((1, ids), (-1, series_mul(K, Hi, p)))
    v = series_add((1, ids), (-1, series_mul(Zs, Hi, p)))
    gq = series_add((1, series_mul(u, v, p)),
                    (-1, series_mul(series_mul(u, w, p), v, p)),
                    (1, series_mul(u, w, p)), (1, series_mul(w, v, p)), (-1, w))
    assert all(not np.any(a % p) for a in gq)


def main():
    cases = []
    for N in range(2, 10):
        p, generator, q = field(N)
        E = MixedEntries(N, p, q)
        Q, d = E.Q, N-1
        xc = -pow(q, -1, p) % p
        kn = pow(xc, N, p)
        z, _, _, _ = head(E, xc)
        i = np.eye(N, dtype=np.int64)
        i2 = np.eye(N*N, dtype=np.int64)
        zero = np.zeros_like(i2)
        Z = np.kron(z, i)
        E0 = np.kron(np.diag([1]+[0]*d), i)
        cup = np.zeros(N*N, dtype=np.int64)
        marker = np.zeros_like(cup)
        for a in range(N):
            cup[a*N+d-a] = N*pow(xc, a-d, p) % p
            for b in range(N):
                marker[a*N+b] = pow(xc, b, p)*pow(N, -2, p) % p
        for mu in (1, generator, pow(generator, 2, p)):
            S1 = np.kron(shift(N, mu), i)
            S2 = np.kron(i, shift(N, kn*mu % p))
            X = xc*mm(S2, inv(S1, p), p) % p
            x, y = (i2-X) % p, (i2-Z) % p
            w = mm(x, y, p)
            H = (i2-w) % p
            Hi = inv(H, p)
            K = mm(X, i2-E0, p)
            u, v = (i2-mm(K, Hi, p)) % p, (i2-mm(Z, Hi, p)) % p
            edge = mm(X, E0, p)
            equal(mm(u, H, p)-x+w, edge, p)
            equal(mm(v, H, p)-y+w, zero, p)
            equal(mm(edge, y, p), zero, p)
            gq = (mm(u, v, p)-mm(mm(u, w, p), v, p)+mm(u, w, p)+mm(w, v, p)-w) % p
            classical_order = (mm(u, v, p)-mm(mm(w, i2-u, p), i2-v, p)) % p
            current = (mm(u, w, p)-mm(w, u, p)) % p
            equal(gq, zero, p)
            equal(classical_order+mm(current, i2-v, p), zero, p)
            # Fixed degree in the face variables; no H inverse or projector
            # remains on the right side of the quantum correction relation.
            equal(mm(K, Z, p), Q*mm(Z, K, p), p)
            equal(H, Z+K-mm(K, Z, p), p)
            polynomial_current = (i2-mm(i2-u, H, p)) % p
            for factor in (i2-v, H, i2-u):
                polynomial_current = mm(polynomial_current, factor, p)
            equal(current, (Q-1)*polynomial_current, p)
            equal(classical_order, -(Q-1)*mm(polynomial_current, i2-v, p), p)
            assert np.any(classical_order)
            # The exact derived source presentation, including its co-source.
            descriptor = np.block([[classical_order, current], [-(i2-v) % p, i2]])
            left = np.block([[i2, -current % p], [zero, i2]])
            right = np.block([[i2, zero], [(i2-v) % p, i2]])
            equal(mm(mm(left, descriptor, p), right, p),
                  np.block([[zero, zero], [zero, i2]]), p)
            extended = np.concatenate([cup, (i2-v)@cup % p])
            equal(descriptor@extended, np.zeros(2*N*N, dtype=np.int64), p)
            naive_source = int(marker@classical_order@cup) % p
            current_source = int(marker@current@(i2-v)@cup) % p
            assert (naive_source+current_source) % p == 0
            normal_jets(X, Z, E0, p)
            cases.append({'N': N, 'prime': p, 'wrap': mu, 'ordered_saturated_operator': 0,
                          'bare_relation_source': naive_source, 'retained_current_source': current_source,
                          'fixed_degree_Q_minus_one_divisibility': True,
                          'five_normal_coefficients': 'all zero', 'unimodular_source_extension': True})

        # Whole original figure-eight source, with all original pivots/marker.
        if N <= 5:
            mu = 1
            S1, S2 = np.kron(shift(N, mu), i), np.kron(i, shift(N, kn*mu % p))
            X = xc*mm(S2, inv(S1, p), p) % p
            x, y = i2-X, i2-Z
            w = mm(x, y, p)
            Hi = inv((i2-w) % p, p)
            u = (i2-mm(mm(X, i2-E0, p), Hi, p)) % p
            v = (i2-mm(Z, Hi, p)) % p
            bare = (mm(u, v, p)-mm(mm(w, i2-u, p), i2-v, p)) % p
            correction = mm((mm(u, w, p)-mm(w, u, p)) % p, i2-v, p)
            B, Bi = crossing(E, xc, xc, 1), inv(crossing(E, xc, xc, 1), p)
            factors = [np.kron(B, i), np.kron(i, Bi), np.kron(B, i), np.kron(i, Bi)]
            pivot = np.diag([pow(xc, -d, p)*pow(Q, -a, p) % p for a in range(N)])
            close = np.kron(i, np.kron(pivot, pivot))
            def period(coupon):
                word = factors[0]@np.kron(coupon, i)%p
                for factor in factors[1:]:
                    word = mm(word, factor, p)
                closed = mm(word, close, p)
                cut = np.einsum('abcdbc->ad', closed.reshape((N,)*6)) % p
                return int(cut.sum())*pow(N, -1, p) % p
            first, second = period(bare), period(correction)
            assert (first+second) % p == 0
            cases[-1]['whole_figure_eight_wrap_one_bare_and_current'] = [first, second]
    Path(__file__).with_name('audit_actual_quantum_pachner_saturation_results.json').write_text(
        json.dumps({'cases': cases, 'exact_complex_original_source': exact_two_source(),
                    'scope': 'actual middle-certificate source/current saturation; '
                             'not a raw classical quotient or a global endpoint bound'}, indent=2)+'\n')
    print(f'PASS {len(cases)} actual quantum saturation/current descriptors, all finite normal jets '
          'and four whole original figure-eight source checks')


if __name__ == '__main__':
    main()
