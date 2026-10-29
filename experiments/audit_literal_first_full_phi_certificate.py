#!/usr/bin/env python3
"""The FIRST actual five-point certificate, with its full strict cut.

The common marked full-Psi scalar phi_N^-1 is retained symbolically:
F0=diag(F_j) below equals phi_N F. Every equation is homogeneous in
that scalar, and the note records its uncanceled source power.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing
from audit_actual_shared_quantum_flags import head, shift, mm, mpow, euler, equal
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def cross_ratio(points):
    a, b, c, d = points
    det = lambda u, v: sp.det(sp.Matrix.hstack(u, v))
    return sp.factor(det(d, b)*det(c, a)/(det(d, a)*det(c, b)))


def face_table():
    X, Z, T = sp.symbols('X Z T')
    n = -X*(1-Z)/Z
    G = 1-n+n*T
    points = [sp.Matrix([1, 1-X]), sp.Matrix([0, 1]),
              sp.Matrix([1-Z, 1]), sp.Matrix([1, 1]),
              sp.Matrix([1, 1-(1-T)*X])]
    expected = [G, G/T, 1/T, (1-1/n)/T, 1-1/n]
    rows = []
    for j, value in enumerate(expected):
        actual = cross_ratio(points[:j]+points[j+1:])
        assert sp.factor(actual-value) == 0
        rows.append({'omitted_vertex': j, 'cross_ratio': str(actual),
                     'minus_boundary_sign': (-1)**(j+1)})
    return rows


def main():
    cases, whole_colors = [], []
    for N in range(2, 11):
        p, g, q = field(N)
        E = MixedEntries(N, p, q)
        Q, d = E.Q, N-1
        x = -pow(q, -1, p) % p
        kn = pow(x, N, p)
        z, k, e, f = head(E, x)
        i = np.eye(N, dtype=np.int64)
        i2 = np.eye(N*N, dtype=np.int64)
        zero = np.zeros_like(i2)
        T = np.kron(i, z)
        Ed = np.kron(i, np.diag([0]*d+[1]))
        F0 = np.kron(i, np.diag(E.F))
        F0i = inv(F0, p)
        atom = np.kron(e, f)
        cartan = np.diag([pow(x, -a-b, p)*pow(Q, a*b, p) % p
                          for a in range(N) for b in range(N)]).astype(np.int64)
        flip = np.zeros_like(i2)
        cup = np.zeros(N*N, dtype=np.int64)
        marker = np.zeros_like(cup)
        for a in range(N):
            cup[a*N+d-a] = N*pow(x, a-d, p) % p
            for b in range(N):
                flip[b*N+a, a*N+b] = 1
                marker[a*N+b] = pow(x, b, p)*pow(N, -2, p) % p
        original = mm(flip, crossing(E, x, x, 1), p)
        original_negative = crossing(E, x, x, -1)
        corner = np.zeros_like(cup)
        corner[d*N] = N
        for mu in (1, g, pow(g, 2, p)):
            S1 = np.kron(shift(N, mu), i)
            S2 = np.kron(i, shift(N, kn*mu % p))
            Z = np.kron(z, i)
            X = x*mm(S2, inv(S1, p), p) % p
            Yframe = -mm(Z, S1, p) % p
            K1, K2 = np.kron(k, i), np.kron(i, k)
            Ftotal = (np.kron(f, i)+np.kron(inv(k, p), f)) % p
            Ktotal = mm(K2, K1, p)
            region = (i2-mm(i2-T, X, p)) % p
            # Literal s_R=(K_total,F_total K_total)^t in the SAME
            # bounded homogeneous frame as the actual middle flags.
            equal(mm(Ftotal-S1, Ktotal, p),
                  mm(region, mm(Yframe, Ktotal, p), p), p)
            n = mm(np.kron(e, i), S2, p)
            c = mm(n, i2-Ed, p)
            P, Pi = euler(E, c), inv(euler(E, c), p)
            H = mm(mm(Pi, T, p), P, p)
            FH0 = mm(mm(Pi, F0, p), P, p)
            y = -Q*mm(c, H, p) % p
            Y, Yi = euler(E, y), inv(euler(E, y), p)
            J = mm(mm(Yi, H, p), Y, p)
            equal(mm(c, T, p), pow(Q, -1, p)*mm(T, c, p), p)
            equal(mm(F0, mm(c, F0i, p), p), atom, p)
            equal(atom, mm(c, i2-Q*T, p), p)
            equal(mpow(c, N, p), zero, p)
            equal(mpow(y, N, p), zero, p)
            equal(mpow(H, N, p), i2, p)
            equal(mpow(J, N, p), i2, p)
            equal(mm(i2-c, H, p), T, p)
            equal(mm(mm(FH0, c, p), inv(FH0, p), p), mm(c, i2-Q*H, p), p)
            equal(mm(FH0, P, p), mm(mm(Y, P, p), FH0, p), p)
            equal(mm(P, FH0, p), mm(mm(Yi, FH0, p), P, p), p)
            equal(J, mm(H, inv(i2+mm(c, H, p), p), p), p)
            Gfirst = (i2-atom) % p
            equal(J, mm(inv(Gfirst, p), T, p), p)
            rfirst = mm(J, c, p)
            equal(rfirst, -mm(y, inv(i2-y, p), p), p)
            equal(i2-rfirst, mm(inv(Gfirst, p), i2-c, p), p)
            final_argument = mm(mm(mm(mm(Yi, FH0, p), c, p), inv(FH0, p), p), Y, p)
            equal(final_argument, atom, p)
            rewritten = mm(mm(mm(mm(cartan, Yi, p), FH0, p), P, p), F0i, p)
            equal(rewritten, original, p)
            equal(inv(mm(flip, rewritten, p), p), original_negative, p)
            # Full wall current is retained; no sectorwise Ward claim.
            wall = mm(n, Ed, p)
            e0d = np.zeros_like(i); e0d[0, d] = 1
            e1d = np.zeros_like(i); e1d[1, d] = 1
            e0dm = np.zeros_like(i); e0dm[0, d-1] = 1
            wall_current = (kn*mu % p)*(
                np.kron(mm(f, e, p)-mm(e, f, p), e0d)
                +(1-Q)*np.kron(mm(inv(k, p), e, p), e1d)
                -(1-pow(Q, -1, p))*np.kron(mm(e, inv(k, p), p), e0dm))
            equal(mm(Ftotal, wall, p)-mm(wall, Ftotal, p), wall_current, p)
            # Every strict wall power is retained, although the WHOLE cup
            # degree d makes these particular source differences vanish.
            for h in range(N):
                cutoff = np.kron(i, np.diag([int(j < N-h) for j in range(N)]))
                equal(mpow(c, h, p), mm(mpow(n, h, p), cutoff, p), p)
                equal(mpow(c, h, p)@cup, mpow(n, h, p)@cup, p)
                assert int(marker@mpow(c, h, p)@cup) % p == 1
            equal(P@cup, corner, p)
            equal(H@cup, cup, p)
            equal(FH0@cup, cup, p)
            assert int(marker@mm(P, FH0, p)@cup) % p == pow(N, -1, p)
            assert int(marker@mm(mm(Yi, FH0, p), P, p)@cup) % p == pow(N, -1, p)
            equal(mm(flip, rewritten, p)@cup, cup, p)
            assert int(marker@mm(flip, rewritten, p)@cup) % p == 1
            cases.append({'N': N, 'wrap': mu, 'first_two_to_three_word': True,
                          'original_positive_and_negative_crossings': True,
                          'all_strict_cut_powers': N,
                          'source_after_same_phi_inverse': f'1/{N}',
                          'whole_original_cup_source': 1})
        # The operator identity is a WHOLE color identity at the fixed
        # physical q root; only the literal complete face/source table
        # above uses x=-q^-1.
        for x1, x2 in ((g, pow(g, 2, p)), (x, g)):
            _, _, e1, _ = head(E, x1)
            jplus = shift(N, 1)
            jplus[0, d] = 0
            c = np.kron(e1, jplus)
            P, Pi = euler(E, c), inv(euler(E, c), p)
            H = mm(mm(Pi, T, p), P, p)
            FH0 = mm(mm(Pi, F0, p), P, p)
            y = -Q*mm(c, H, p) % p
            Yi = inv(euler(E, y), p)
            Dmixed = np.diag([pow(x1, -b, p)*pow(x2, -a, p)*pow(Q, a*b, p) % p
                             for a in range(N) for b in range(N)]).astype(np.int64)
            rewritten = mm(mm(mm(mm(Dmixed, Yi, p), FH0, p), P, p), F0i, p)
            equal(mm(flip, rewritten, p), crossing(E, x1, x2, 1), p)
            whole_colors.append({'N': N, 'x1': x1, 'x2': x2, 'whole_color_operator_identity': True})
    result = {'status': 'PASS', 'literal_first_face_table': face_table(),
              'cases': cases, 'whole_color_operator_cases': whole_colors,
              'scope': 'FIRST literal five-point operator word with exact actual R embedding, '
                       'all finite cuts and marked full-Psi source; no positive atlas or cycle-degree claim.'}
    Path(__file__).with_name('literal_first_full_phi_certificate_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS five literal first faces, {len(cases)} all-cut first-certificate words, '
          f'full original +/- R and original cup/marked source, {len(whole_colors)} whole-color cases')


if __name__ == '__main__':
    main()
