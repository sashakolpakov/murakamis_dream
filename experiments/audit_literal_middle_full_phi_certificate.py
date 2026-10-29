#!/usr/bin/env python3
"""Actual literal middle five-point operator sequence and all finite walls.

The full-Phi scalar phi_N is retained symbolically: F_H/phi_N is used in
homogeneous matrix identities, and the note restores its exact power.
Original R coefficients, cup, marker and fixed global wrap types are used.
"""

import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing
from audit_actual_shared_quantum_flags import head, shift, mm, mpow, euler, equal
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def main():
    cases = []
    for N in range(2, 11):
        p, g, q = field(N)
        E = MixedEntries(N, p, q)
        Q, d = E.Q, N-1
        x = -pow(q, -1, p) % p
        lam, kn = pow(x, -1, p), pow(x, N, p)
        z, k, e, f = head(E, x)
        i = np.eye(N, dtype=np.int64)
        i2 = np.eye(N*N, dtype=np.int64)
        zero = np.zeros_like(i2)
        Z = np.kron(z, i)
        E0 = np.kron(np.diag([1]+[0]*d), i)
        FZ = np.kron(np.diag([pow(E.F[j], -1, p) for j in range(N)]), i)
        FZi = inv(FZ, p)
        flip = np.zeros_like(i2)
        for a in range(N):
            for b in range(N):
                flip[b*N+a, a*N+b] = 1
        original = mm(flip, crossing(E, x, x, 1), p)
        cartan = np.diag([pow(x, -a-b, p)*pow(Q, a*b, p) % p
                          for a in range(N) for b in range(N)]).astype(np.int64)
        cup = np.zeros(N*N, dtype=np.int64)
        marker = np.zeros_like(cup)
        for a in range(N):
            cup[a*N+d-a] = N*pow(x, a-d, p) % p
            for b in range(N):
                marker[a*N+b] = pow(x, b, p)*pow(N, -2, p) % p
        corner = np.zeros_like(cup)
        corner[d*N] = N
        for mu in (1, g, pow(g, 2, p)):
            S1 = np.kron(shift(N, mu), i)
            S2 = np.kron(i, shift(N, kn*mu % p))
            X = x*mm(S2, inv(S1, p), p) % p
            n = mm(np.kron(e, i), S2, p)
            P, Pi = euler(E, n), inv(euler(E, n), p)
            H = mm(mm(Pi, Z, p), P, p)
            equal(H, mm(Z, i2-n, p), p)
            equal(H, Z+mm(i2-Q*Z, X, p), p)
            equal(mpow(H, N, p), i2, p)
            equal(mm(n, H, p), Q*mm(H, n, p), p)
            FH, FHi = mm(mm(Pi, FZ, p), P, p), mm(mm(Pi, FZi, p), P, p)
            middle = -mm(n, H, p) % p
            rhs3 = mm(mm(FHi, P, p), euler(E, middle), p)
            equal(mm(P, FHi, p), rhs3, p)
            # Exact developed arguments on the two sides.
            equal(mm(mm(P, H, p), Pi, p), Z, p)
            u = mm(mm(FHi, n, p), FH, p)
            w = -mm(mm(FHi, mm(n, Z, p), p), FH, p) % p
            cut = mm(X, i2-E0, p)
            equal(w, Q*cut, p)
            uZ = -mm(inv(Z, p), cut, p) % p
            equal(mm(mm(FZi, n, p), FZ, p), uZ, p)
            equal(u, mm(mm(Pi, uZ, p), P, p), p)
            equal(euler(E, n), mm(euler(E, uZ), euler(E, w), p), p)
            r = mm(w, inv(H, p), p)
            equal(r, -mm(u, inv(i2-pow(Q, -1, p)*u % p, p), p), p)
            equal(mpow(u, N, p), zero, p)
            equal(mpow(w, N, p), zero, p)
            # Entire actual R word, not just its local pair of factors.
            nminus = -mm(mm(np.kron(e, i), np.kron(i, z), p), S2, p) % p
            rewritten = mm(mm(mm(mm(mm(cartan, euler(E, nminus), p), FHi, p), P, p),
                              euler(E, middle), p), FH, p)
            equal(rewritten, original, p)
            # The actual cup selects the TOP marked H endpoint.
            equal(P@cup, corner, p)
            equal(H@cup, pow(Q, -1, p)*cup, p)
            equal(FH@cup, pow(N, -1, p)*cup, p)
            assert int(marker@mm(P, FHi, p)@cup) % p == 1
            for degree in range(N):
                cutoff = np.kron(np.diag([int(j >= degree) for j in range(N)]), i)
                equal(mpow(w, degree, p), pow(Q, degree, p)*mm(mpow(X, degree, p), cutoff, p), p)
                assert int(marker@mpow(w, degree, p)@cup) % p == (N-degree)*pow(N, -1, p) % p
            cases.append({'N': N, 'wrap': mu, 'literal_two_to_three': True,
                          'actual_R_word': True, 'all_projector_moments': N,
                          'source_after_same_phi_inverse': 1})
    path = Path(__file__).with_name('audit_literal_middle_full_phi_certificate_results.json')
    path.write_text(json.dumps({'cases': cases,
                               'scope': 'literal finite five-point relative operator identity; '
                                        'not a positive geometric face or global cycle theorem'}, indent=2)+'\n')
    print(f'PASS {len(cases)} literal middle-certificate words, original R factorizations '
          'and all finite wall/source moments')


if __name__ == '__main__':
    main()
