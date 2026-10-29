#!/usr/bin/env python3
"""Original cut source, one-crossing wall, and actual figure-eight insertions.

The balanced original crossings/pivots and the FULL averaged marked cut are
fixed throughout. Highest-entry values are reported separately, never used
as a replacement for that source after a nonintertwining coupon insertion.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing
from audit_actual_shared_quantum_flags import head, shift, mm, equal
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def symbolic_two():
    i = sp.I
    B = sp.Matrix([[1, 0, 0, 0], [0, 0, -i, 0],
                   [0, -i, 2, 0], [0, 0, 0, 1]])
    eye = sp.eye(2)
    pivot = sp.diag(-i, i)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -1], [1, 0]])
    wallproj = sp.diag(0, 1)
    W = sp.kronecker_product(wallproj, eye)*i*sp.kronecker_product(s1, s2)
    cup = sp.Matrix([0, -2*i, 2, 0])
    marker = sp.Matrix([[1, i, 1, i]])/4
    assert (marker*W*B*cup)[0] == -sp.Rational(1, 2)
    assert (marker*B*W*cup)[0] == -sp.Rational(3, 2)
    slots = [sp.kronecker_product(B, eye), sp.kronecker_product(eye, B.inv()),
             sp.kronecker_product(B, eye), sp.kronecker_product(eye, B.inv())]
    closer = sp.kronecker_product(eye, pivot, pivot)

    def cap(a):
        a = a*closer
        c = sp.zeros(2)
        for u in range(2):
            for v in range(2):
                c[u, v] = sum(a[u*4+b*2+c0, v*4+b*2+c0]
                              for b in range(2) for c0 in range(2))
        return sp.simplify(sum(c)/2), c

    unmarked = sp.eye(8)
    for a in slots:
        unmarked *= a
    scalar, cut = cap(unmarked)
    assert scalar == 5 and cut == 5*eye
    values = []
    for gap in range(5):
        a = sp.eye(8)
        for index in range(5):
            if index == gap:
                a *= sp.kronecker_product(W, eye)
            if index < 4:
                a *= slots[index]
        values.append(cap(a)[0])
    assert values == [-sp.Rational(5, 2), -sp.Rational(3, 2),
                      -sp.Rational(5, 2), sp.Rational(5, 2), sp.Rational(5, 2)]
    return {'original_scalar': '5', 'one_crossing_before': '-1/2',
            'one_crossing_after': '-3/2', 'figure_eight_gaps': list(map(str, values))}


def main():
    currents, one_crossing, figure_eight = [], [], []
    word = [(0, 1), (1, -1), (0, 1), (1, -1)]
    for N in range(2, 8):
        p, g, q = field(N)
        E = MixedEntries(N, p, q)
        Q, d = E.Q, N-1
        x = -pow(q, -1, p) % p
        kn = pow(x, N, p)
        z, k, e, f = head(E, x)
        i = np.eye(N, dtype=np.int64)
        i2 = np.eye(N*N, dtype=np.int64)
        B = crossing(E, x, x, 1)
        Bi = inv(B, p)
        cup = np.zeros(N*N, dtype=np.int64)
        marker = np.zeros_like(cup)
        for a in range(N):
            cup[a*N+d-a] = N*pow(x, a-d, p) % p
            for b in range(N):
                marker[a*N+b] = pow(x, b, p)*pow(N, -2, p) % p
        ed = np.zeros((N, N), dtype=np.int64)
        ed[d, d] = 1
        bd0 = np.zeros_like(ed)
        bd0[d, 0] = 1
        ftot = (np.kron(f, i)+np.kron(inv(k, p), f)) % p
        pivot = np.diag([pow(x, 1-N, p)*pow(Q, -a, p) % p
                         for a in range(N)]).astype(np.int64)
        for mu in (1, g):
            s1, s2 = shift(N, mu), shift(N, kn*mu % p)
            X = x*np.kron(inv(s1, p), s2) % p
            W = mm(np.kron(ed, i), X, p)
            current = (pow(Q, -1, p)-1)*pow(mu, -1, p)*np.kron(bd0, mm(s2, s2, p)) % p
            equal(mm(ftot, W, p)-mm(W, ftot, p), current, p)
            assert np.any(current)
            # Both ordinary pivotal partial traces vanish, despite marked coupling.
            w2 = mm(W, np.kron(i, pivot), p).reshape((N,)*4)
            equal(np.einsum('abcb->ac', w2), np.zeros_like(i), p)
            w1 = mm(W, np.kron(pivot, i), p).reshape((N,)*4)
            equal(np.einsum('abad->bd', w1), np.zeros_like(i), p)
            before = int(marker@W@B@cup) % p
            after = int(marker@B@W@cup) % p
            euler_at_one = sum(pow(F, -1, p) for F in E.F) % p
            assert before == pow(N*Q, -1, p)
            assert after == pow(Q, -1, p)*euler_at_one % p
            currents.append({'N': N, 'wrap': mu, 'F_Ward_defect_nonzero': True,
                             'both_ordinary_partial_traces': 0})
            one_crossing.append({'N': N, 'wrap': mu, 'before': before,
                                 'after': after, 'Euler_at_one': euler_at_one})

        # Original 3-braid figure-eight cut, all words use this SAME full marker.
        eye3 = np.eye(N**3, dtype=np.int64)
        factors = [(np.kron(B if sign > 0 else Bi, i) if position == 0
                    else np.kron(i, B if sign > 0 else Bi)) for position, sign in word]
        closer = np.kron(i, np.kron(pivot, pivot))

        def close(a):
            a = mm(a, closer, p)
            cut = np.einsum('abcdbc->ad', a.reshape((N,)*6)) % p
            return int(cut.sum())*pow(N, -1, p) % p, int(cut[0, 0]), cut

        original = eye3.copy()
        for factor in factors:
            original = mm(original, factor, p)
        scalar, highest, cut = close(original)
        equal(cut, scalar*i, p)
        assert scalar == highest
        wraps = [pow(kn, j, p) for j in range(3)]
        for position in (0, 1):
            X = x*np.kron(inv(shift(N, wraps[position]), p),
                           shift(N, wraps[position+1])) % p
            W = mm(np.kron(ed, i), X, p)
            W = np.kron(W, i) if position == 0 else np.kron(i, W)
            gaps = []
            for gap in range(5):
                a = eye3.copy()
                for index in range(5):
                    if index == gap:
                        a = mm(a, W, p)
                    if index < 4:
                        a = mm(a, factors[index], p)
                value, high, inserted = close(a)
                gaps.append({'full_marked_source': value, 'highest_entry_diagnostic': high,
                             'cut_remains_scalar': bool(np.array_equal(inserted, high*i % p))})
            assert len({item['full_marked_source'] for item in gaps}) > 1
            figure_eight.append({'N': N, 'prime': p, 'local_pair': position,
                                 'original_scalar': scalar, 'global_wraps': wraps, 'gaps': gaps})
    result = {'symbolic_N2': symbolic_two(), 'actual_Ward_currents': currents,
              'one_crossing': one_crossing, 'figure_eight': figure_eight,
              'scope': 'raw interior cut relocation fails; no claim against Ward-completed transport'}
    Path(__file__).with_name('audit_actual_interior_wall_cut_relocation_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(currents)} all-current families; {len(one_crossing)} one-crossing '
          f'identities; {len(figure_eight)} actual figure-eight gap families; exact symbolic N2')


if __name__ == '__main__':
    main()
