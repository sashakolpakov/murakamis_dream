#!/usr/bin/env python3
"""Actual charged flag mark and full-Phi/nilpotent pentagon at physical roots.

Prime-field tests keep the common full-Phi scalar symbolic. Independent
complex-product tests audit its exact value and every marked unit-root value.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_borel_regular_fusion import inv
from audit_actual_shared_quantum_flags import head, shift, mm, mpow, euler, equal
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def complex_marks():
    mp.mp.dps = 90
    out = []
    for N in (2, 3, 4, 5, 6, 8, 12, 20):
        r = 1-mp.mpf('1e-35')
        for eps in (-1, 1):
            Q = mp.exp(eps*2*mp.pi*1j/N)
            phi = mp.sqrt(N)*mp.exp(eps*mp.pi*1j*(mp.mpf(1)/4-(N+mp.mpf(1)/N)/12))
            F = [mp.mpc(1)]
            for j in range(1, N):
                F.append(F[-1]*(1-Q**j))
            errors = []
            for j in range(1, N+1):
                lift = mp.log(r)+eps*2*mp.pi*1j*j/N
                logpsi = ((1+eps*1j*lift/(2*mp.pi))*mp.log(1-r**N)
                          -sum(mp.mpf(k)/N*mp.log(1-r*Q**(k+j)) for k in range(1, N))
                          +eps*1j*mp.polylog(2, r**N)/(2*mp.pi*N))
                actual = mp.exp(logpsi)
                expected = phi/F[j-1]
                errors.append(abs(actual/expected-1))
            maximum = max(errors)
            assert maximum < mp.mpf('1e-29'), (N, eps, maximum)
            out.append({'N': N, 'orientation': eps,
                        'max_relative_error': str(maximum), 'source_modulus': str(abs(phi))})
    return out


def main():
    cases, factorials = [], []
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
        K1, Ki1 = np.kron(k, i), np.kron(inv(k, p), i)
        e2, Z2 = np.kron(i, e), np.kron(i, z)
        Jplus = np.zeros((N, N), dtype=np.int64)
        for j in range(d):
            Jplus[j+1, j] = 1
        J0 = np.kron(i, np.diag([N-j for j in range(N)]))
        cup = np.zeros(N*N, dtype=np.int64)
        marker = np.zeros_like(cup)
        for a in range(N):
            cup[a*N+d-a] = N*pow(x, a-d, p) % p
            for b in range(N):
                marker[a*N+b] = pow(x, b, p)*pow(N, -2, p) % p
        corner = np.zeros_like(cup)
        corner[d] = 1  # |0,d>
        for mu in (1, g, pow(g, 2, p)):
            S1 = np.kron(shift(N, mu), i)
            S2 = np.kron(i, shift(N, kn*mu % p))
            delta = (np.kron(f, i)+mm(Ki1, S2, p)-S1) % p
            v = (np.kron(i, inv(z, p))+mm(S1, e2, p)) % p
            gamma = -mm(e2, K1, p) % p
            A = -mm(mm(S1, e2, p), Z2, p) % p
            C, Ci = euler(E, A), inv(euler(E, A), p)
            HA = np.kron(i, np.diag([pow(lam, -b, p)*pow(E.F[b], -1, p) % p
                                    for b in range(N)]))
            equal(mm(mm(HA, np.kron(shift(N, mu), Jplus.T), p), inv(HA, p), p), A, p)
            equal(mpow(A, N, p), zero, p)
            equal(mm(mm(C, np.kron(i, inv(z, p)), p), Ci, p), v, p)
            equal(mm(mm(C, np.kron(inv(k, p), Jplus), p), Ci, p), delta, p)
            equal(mm(C, gamma, p), mm(gamma, C, p), p)
            equal(N*pow(x, -d, p)*(C@corner), cup, p)
            Jv = mm(mm(C, J0, p), Ci, p)
            equal(mm(Jv, delta, p)-mm(delta, Jv, p), -delta, p)
            equal(Jv@cup, cup, p)
            # Marked full Phi divided by its SAME retained scalar phi_N.
            Fdiag = np.kron(i, np.diag([pow(E.F[d-b], -1, p) for b in range(N)]))
            Finvdiag = np.kron(i, np.diag([E.F[d-b] for b in range(N)]))
            Fmarked = mm(mm(C, Fdiag, p), Ci, p)
            Finverse = mm(mm(C, Finvdiag, p), Ci, p)
            equal(mm(Fmarked, Finverse, p), i2, p)
            equal(Fmarked@cup, cup, p)
            equal(mm(mm(Fmarked, delta, p), Finverse, p),
                  mm(delta, i2-pow(Q, -1, p)*v, p), p)
            for alpha in (1, g):
                lhs = mm(Fmarked, euler(E, alpha*delta % p), p)
                rhs = mm(mm(euler(E, alpha*delta % p),
                            euler(E, -alpha*pow(Q, -1, p)*mm(delta, v, p) % p), p),
                         Fmarked, p)
                equal(lhs, rhs, p)
                assert int(marker@lhs@cup) % p == 1
                cases.append({'N': N, 'wrap': mu, 'alpha': alpha,
                              'actual_source_unit_after_common_phi_factor': 1,
                              'marked_full_Phi_pentagon': True})

        # The literal middle-five-point factorial frames use the SAME moments.
        Fminus = [1]
        Qminus = pow(Q, -1, p)
        for j in range(1, N):
            Fminus.append(Fminus[-1]*(1-pow(Qminus, j, p)) % p)
        cplus = [pow(-1, j, p)*pow(Q, j*(j-1)//2, p)*pow(E.F[j], -1, p) % p
                 for j in range(N)]
        cminus = [pow(-1, j, p)*pow(Qminus, j*(j-1)//2, p)*pow(Fminus[j], -1, p) % p
                  for j in range(N)]
        Hn = np.diag([pow(lam, j, p)*cplus[j] % p for j in range(N)]).astype(np.int64)
        HU = np.diag([pow(lam, j, p)*E.F[j] % p for j in range(N)]).astype(np.int64)
        reverse = np.fliplr(i)
        equal(HU, N*pow(lam, -d, p)*pow(Q, -1, p)*mm(mm(reverse, Hn, p), reverse, p), p)
        for j in range(N):
            G = pow(-1, j, p)*pow(Q, -j*(j-1)//2, p)*E.F[j]**2 % p
            assert G == N*N*pow(Q, j, p)*cplus[d-j]*cminus[d-j] % p
            assert pow(G, -1, p) == pow(Q, -j, p)*cplus[j]*cminus[j] % p
        factorials.append({'N': N, 'both_full_Phi_moment_gauges': True,
                           'exact_degree_reflection_scalar': N*pow(lam, -d, p)*pow(Q, -1, p) % p})
    result = {'actual_marked_pentagons': cases, 'literal_five_point_factorial_frames': factorials,
              'independent_complex_full_Phi_marks': complex_marks(),
              'scope': 'actual cap-compatible physical-root mixed pentagon; '
                       'not the complete three five-point certificate refactor'}
    Path(__file__).with_name('audit_actual_marked_full_phi_flag_pentagon_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(cases)} actual marked-root pentagons; {len(factorials)} literal '
          f'five-point moment gauges; {len(result["independent_complex_full_Phi_marks"])} complex lifts')


if __name__ == '__main__':
    main()
