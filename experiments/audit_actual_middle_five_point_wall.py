#!/usr/bin/env python3
"""Literal middle five-point flags, actual R factor, and its retained wall.

All original crossing entries come from the independent E/Cartan evaluator.
All equalities are exact prime-field identities. External original Cartan,
framing, dimension and peripheral lines are retained on both sides.
"""

import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing
from audit_actual_shared_quantum_flags import head, shift, mm, mpow, euler, equal
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def rank(a, p):
    a = a.copy() % p
    n, m = a.shape
    r = 0
    for j in range(m):
        pivot = next((i for i in range(r, n) if a[i, j]), None)
        if pivot is None:
            continue
        a[[r, pivot]] = a[[pivot, r]]
        a[r] = a[r]*pow(int(a[r, j]), -1, p) % p
        for i in range(n):
            if i != r and a[i, j]:
                a[i] = (a[i]-a[i, j]*a[r]) % p
        r += 1
        if r == n:
            break
    return r


def main():
    split_cases, flags_cases, auxiliary_cases = [], [], []
    for N in range(2, 9):
        p, g, q = field(N)
        E = MixedEntries(N, p, q)
        Q, d = E.Q, N-1
        i = np.eye(N, dtype=np.int64)
        i2 = np.eye(N*N, dtype=np.int64)
        zero = np.zeros_like(i2)
        x = -pow(q, -1, p) % p
        lam, kn = pow(x, -1, p), pow(x, N, p)
        flip = np.zeros((N*N, N*N), dtype=np.int64)
        for a in range(N):
            for b in range(N):
                flip[b*N+a, a*N+b] = 1

        for x1, x2 in ((g, pow(g, 2, p)), (x, x)):
            z, k1, e, f = head(E, x1)
            B = crossing(E, x1, x2, 1)
            R0 = mm(flip, B, p)
            D = np.diag([pow(x1, -b, p)*pow(x2, -a, p)*pow(Q, a*b, p) % p
                         for a in range(N) for b in range(N)]).astype(np.int64)
            for mu in (1, g):
                s2 = shift(N, mu)
                n = np.kron(e, s2)
                nminus = -np.kron(e, mm(z, s2, p)) % p
                expected = mm(mm(D, euler(E, nminus), p), euler(E, n), p)
                equal(R0, expected, p)
                split_cases.append({'N': N, 'x1': x1, 'x2': x2, 'wrap': mu,
                                    'original_R_two_nilpotent_factors': True})

        z, k, e, f = head(E, x)
        Z, K, ee, ff = (np.kron(a, i) for a in (z, k, e, f))
        G = np.block([[K, ee], [mm(ff, K, p), (2*lam*i2-Q*K) % p]])
        B = crossing(E, x, x, 1)
        cup = np.zeros(N*N, dtype=np.int64)
        marker = np.zeros_like(cup)
        for a in range(N):
            cup[a*N+d-a] = N*pow(x, a-d, p) % p
            for b in range(N):
                marker[a*N+b] = pow(x, b, p)*pow(N, -2, p) % p
        equal(B@cup, cup, p)

        for mu in (1, g, pow(g, 2, p)):
            S1 = np.kron(shift(N, mu), i)
            S2 = np.kron(i, shift(N, kn*mu % p))
            bflag = (ff+mm(inv(K, p), S2, p)) % p
            Y = -mm(Z, S1, p) % p
            X = x*mm(S2, inv(S1, p), p) % p
            L = np.block([[Y, zero], [-S1 % p, i2]])
            A, BB = np.vstack([i2, S1]), np.vstack([i2, bflag])
            P, S0 = np.vstack([zero, i2]), np.vstack([i2, zero])
            P1, SM = mm(G, P, p), mm(G, S0, p)
            canonical = [np.vstack([i2, zero]), np.vstack([i2, (i2-X) % p]),
                         P, np.vstack([(i2-Z) % p, i2]), np.vstack([i2, i2])]
            originals, tags = [A, BB, P, P1, SM], [Y, Y, i2, lam*i2, mm(Y, K, p)]
            for original, new, tag in zip(originals, canonical, tags):
                equal(mm(L, original, p), mm(new, tag, p), p)
            equal(mm(X, Z, p), Q*mm(Z, X, p), p)
            equal(mpow(X, N, p), i2, p)
            n = mm(ee, S2, p)
            equal(n, mm((Q*i2-inv(Z, p)) % p, X, p), p)
            equal(mpow(n, N, p), zero, p)

            # Explicit group inverse keeps its zero spectral subspace.
            h = np.diag([0 if j == d else pow((1-pow(Q, j+1, p)) % p, -1, p)
                         for j in range(N)]).astype(np.int64)
            U = mm(np.kron(h, i), X, p)
            wall = np.zeros((N, N), dtype=np.int64)
            wall[d, d] = 1
            wall = np.kron(wall, i)
            equal(mm(i2-Q*Z, U, p), X-mm(wall, X, p), p)
            equal(mm(U, Z, p), Q*mm(Z, U, p), p)
            equal(mpow(U, N, p), zero, p)
            gamma = np.diag([pow(-1, j, p)*pow(Q, -j*(j-1)//2, p)*E.F[j]**2 % p
                             for j in range(N)]).astype(np.int64)
            gamma = np.kron(gamma, i)
            equal(mm(mm(gamma, n, p), inv(gamma, p), p), U, p)
            equal(mm(mm(inv(gamma, p), euler(E, U), p), gamma, p), euler(E, n), p)
            equal(mm(X, i2-Z, p)-Q*mm(i2-Z, X, p), (1-Q)*X, p)

            equal(X@cup, pow(Q, -1, p)*cup, p)
            original_weight = int(marker@wall@X@B@cup) % p
            assert original_weight == pow(N*Q, -1, p)
            csource = mm(Y, cup, p)
            cmarker = mm(marker, inv(Y, p), p)
            equal(X@csource, csource, p)
            canonical_weight = int(cmarker@wall@X@csource) % p
            assert canonical_weight == pow(N, -1, p)
            # Full literal source transport under the factorial gauge.
            assert int(mm(marker, inv(gamma, p), p)@mm(gamma, cup, p)) % p == 1
            flags_cases.append({'N': N, 'wrap': mu, 'typed_five_flags': True,
                                'actual_nilpotent_tetrahedron_factor': True,
                                'group_inverse_factorial_gauge': True,
                                'original_wall_weight': original_weight,
                                'typed_wall_weight': canonical_weight})

        # Changing a scalar auxiliary P never removes its determinant wall.
        svalues = [0]+[a for a in range(1, p) if pow(a, N, p) != 1][:2]
        S = shift(N, 1)
        Ki = inv(k, p)
        Dg = (2*lam*i-Q*k) % p
        for s in svalues:
            wedge = (mm(f, k, p)+s*(Dg-k)-s*s*e) % p
            product = mm(mm((S-s*i) % p, (k-lam*i) % p, p),
                         (i-s*inv(S, p)) % p, p)
            equal(wedge, product, p)
            assert rank(wedge, p) == N-1
            auxiliary_cases.append({'N': N, 'scalar_P': [1, s], 'determinant_rank': N-1})

    result = {'actual_crossing_split': split_cases, 'literal_five_flags': flags_cases,
              'generic_scalar_auxiliary_flags': auxiliary_cases,
              'scope': 'exact middle certificate frame and corrected actual R factor; '
                       'no full quantum five-point refactor or volume claim'}
    Path(__file__).with_name('audit_actual_middle_five_point_wall_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(split_cases)} actual R splits; {len(flags_cases)} typed five-flag/gauge '
          f'families; {len(auxiliary_cases)} generic auxiliary determinant walls')


if __name__ == '__main__':
    main()
