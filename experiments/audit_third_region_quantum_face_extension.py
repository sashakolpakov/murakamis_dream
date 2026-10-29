#!/usr/bin/env python3
"""A genuine extra region degree, its original R port, and full pentagon.

All intermediate auxiliary indices are contracted as full matrices BEFORE
vacuum extraction. No product of compressed physical coordinates is used.
"""

import json
from pathlib import Path

import numpy as np

from audit_actual_shared_quantum_flags import head, shift, mm, mpow, euler, equal
from audit_actual_rogers_bridge_transport import crossing
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field
from audit_actual_borel_regular_fusion import inv


def inverse_euler(E, A):
    out = np.zeros_like(A)
    power = np.eye(A.shape[0], dtype=np.int64)
    for h in range(E.N):
        out = (out+pow(E.F[h], -1, E.p)*power) % E.p
        power = mm(power, A, E.p)
    return out


def block(a, N, output, input):
    physical = a.shape[0]//N
    return a.reshape(physical, N, physical, N)[:, output, :, input]


def main():
    results = []
    for N in range(2, 7):
        p, g, q = field(N)
        E = MixedEntries(N, p, q)
        Q, d = E.Q, N-1
        x = -pow(q, -1, p) % p
        kn = pow(x, N, p)
        z, k, e, f = head(E, x)
        i = np.eye(N, dtype=np.int64)
        i2 = np.eye(N*N, dtype=np.int64)
        i3 = np.eye(N**3, dtype=np.int64)
        zero3 = np.zeros_like(i3)
        Z, Z2 = np.kron(z, i), np.kron(i, z)
        W, Wi = z, inv(z, p)
        S, Si = shift(N, kn), inv(shift(N, kn), p)
        Wext = np.kron(i2, W)
        Faux = np.kron(i2, np.diag([pow(E.F[j], -1, p) for j in range(N)]))
        Fauxi = np.kron(i2, np.diag(E.F))
        flip = np.zeros_like(i2)
        for a in range(N):
            for b in range(N):
                flip[b*N+a, a*N+b] = 1
        actual = mm(flip, crossing(E, x, x, 1), p)
        D = np.diag([pow(x, -a-b, p)*pow(Q, a*b, p) % p
                     for a in range(N) for b in range(N)]).astype(np.int64)
        for mu in (1, g):
            S1 = np.kron(shift(N, mu), i)
            S2 = np.kron(i, shift(N, kn*mu % p))
            X = x*mm(S2, inv(S1, p), p) % p
            nR = mm(i2-Z2, X, p)
            R = (i2-nR) % p
            a = mm(Z2, X, p)
            A = np.kron(a, Si)
            B = (np.kron(i2, W)-pow(Q, -1, p)*np.kron(i2, mm(W, S, p))
                 +np.kron(Z, S)) % p
            equal(mm(A, B, p), Q*mm(B, A, p), p)
            equal(mpow(A, N, p), i3, p)
            equal(mpow(B, N, p), i3, p)

            # Periodic quantum Pochhammer controlled transport, U0=I,U1=R.
            PnR, PinR = euler(E, nR), inverse_euler(E, nR)
            U, Ui = np.zeros_like(i3), np.zeros_like(i3)
            for j in range(N):
                Uj = mm(inverse_euler(E, pow(Q, j, p)*nR % p), PnR, p)
                Uji = mm(PinR, euler(E, pow(Q, j, p)*nR % p), p)
                ej = np.zeros_like(i)
                ej[j, j] = 1
                U = (U+np.kron(Uj, ej)) % p
                Ui = (Ui+np.kron(Uji, ej)) % p
            equal(mm(U, Ui, p), i3, p)
            equal(block(U, N, 0, 0), i2, p)
            equal(block(U, N, 1, 1), R, p)
            Atilde, Btilde = mm(mm(U, A, p), Ui, p), mm(mm(U, B, p), Ui, p)
            Xprime = mm(a, inv(R, p), p)
            Zprime = (i2-mm(R, i2-Z, p)) % p
            equal(block(Atilde, N, 0, 1), Xprime, p)
            equal(block(Btilde, N, 0, 0)+block(Btilde, N, 1, 0), Zprime, p)

            # Explicit quantum triangle source C_B, with no vacuum reset.
            L = mm(i3-Q*np.kron(Z, Wi), np.kron(i2, S), p)
            C, Ci = euler(E, L), inverse_euler(E, L)
            equal(mpow(L, N, p), zero3, p)
            equal(mm(mm(C, Wext, p), Ci, p), B, p)
            equal(mm(C, A, p), mm(A, C, p), p)
            equal(block(C, N, 0, 0), i2, p)

            # Actual n_minus is the COMPLETE coherent vacuum port.
            aeff = Q*mm(a, inv(Z, p), p) % p
            eaux = mm(Q*i-Wi, Si, p)
            n0 = np.kron(aeff, eaux)
            P0, Pi0 = euler(E, n0), inverse_euler(E, n0)
            nminus = -mm(Q*i2-inv(Z, p), a, p) % p
            equal(block(mm(P0, C, p), N, 0, 0), euler(E, nminus), p)

            # Full marked pentagon BEFORE all intermediate auxiliary sums.
            H0 = mm(mm(Pi0, Wext, p), P0, p)
            FH = mm(mm(Pi0, Faux, p), P0, p)
            FHi = mm(mm(Pi0, Fauxi, p), P0, p)
            middle = -mm(n0, H0, p) % p
            equal(mm(P0, FHi, p), mm(mm(FHi, P0, p), euler(E, middle), p), p)
            five_source_word = mm(mm(mm(mm(FHi, P0, p), euler(E, middle), p), FH, p), C, p)
            physical = block(mm(mm(U, five_source_word, p), Ui, p), N, 0, 0)
            equal(physical, euler(E, nminus), p)
            n = mm(np.kron(e, i), S2, p)
            equal(mm(mm(D, physical, p), euler(E, n), p), actual, p)
            results.append({'N': N, 'physical_wrap': mu, 'extended_torus': True,
                            'typed_third_region_coordinates': True,
                            'complete_original_R_vacuum_port': True,
                            'full_marked_pentagon_before_all_auxiliary_sums': True,
                            'vacuum_augmentation': 1})
    Path(__file__).with_name('audit_third_region_quantum_face_extension_results.json').write_text(
        json.dumps({'cases': results,
                    'scope': 'actual quantum region extension and exact R-source pentagon port; '
                             'complete geometric third face table not asserted'}, indent=2)+'\n')
    print(f'PASS {len(results)} exact extended region tori, full original R vacuum ports '
          'and marked pentagons with all intermediate auxiliary indices')


if __name__ == '__main__':
    main()
