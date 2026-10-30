#!/usr/bin/env python3
"""Actual dual measures, completed projector jets and native energy.

Finite algebra audits the identities; the uniform estimates are proved
in the note. The exponential example is a genuine projector norm.
"""
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_matching_edge_completed_projector_block import omega
from audit_actual_q_hahn_physical_generic_jet_bound import (
    Jet, original, matrix, divide_simple_zero,
)
from audit_high_color_first_normal_r_degree import root_field


def product(values, one=1):
    out = one
    for value in values:
        out *= value
    return out


def generic_high_adapter():
    counts = dict(original_full_generic_high_blocks=0,
                  full_generic_chevalley_casimirs=0)
    for p, q in [(1000003, 2), (1000033, 3)]:
        for N in range(2, 8):
            d = N-1
            O = omega(d, q, p)
            C = np.zeros_like(O)
            for u in range(N):
                for v in range(N):
                    C[(d-v)*N+d-u, u*N+v] = pow(q, -N*(u+v), p)
            assert np.array_equal(C@O % p, O@C % p)
            counts['full_generic_chevalley_casimirs'] += 1
            for t in range(d+1):
                lo = [u*N+t-u for u in range(t+1)]
                hi = [(d-t+u)*N+d-u for u in range(t+1)]
                assert np.array_equal(O[np.ix_(lo, lo)], O[np.ix_(hi, hi)])
                counts['original_full_generic_high_blocks'] += 1
    return counts


def extract(A, r):
    return np.array([[v.c[r] for v in row] for row in A], dtype=np.int64)


def root_jets():
    counts = dict(actual_column_four_jets=0, generic_dual_norm_four_jets=0,
                  actual_residue_four_jets=0, completed_cluster_three_jets=0,
                  simple_projector_four_jets=0, exact_double_rank_one_blocks=0)
    for N in range(3, 10):
        p, eta = root_field(N)
        q0 = eta*eta % p
        Jet.p = p
        q = Jet([q0*pow(math.factorial(k), -1, p) % p for k in range(4)])
        F = [Jet(1)]
        for k in range(1, N):
            F.append(F[-1]*(1-q**(2*k)))
        d = N-1
        for t in range(d+1):
            di, up, low = matrix(N, q, t)
            O = np.array([[Jet(0) for _ in range(t+1)] for _ in range(t+1)], dtype=object)
            I = np.array([[Jet(int(u == v)) for v in range(t+1)] for u in range(t+1)], dtype=object)
            for u in range(t+1):
                O[u, u] = di[u]
                if u < t:
                    O[u, u+1], O[u+1, u] = up[u], low[u]
            lam = [q**(2*N-2*m-1)+q**(-2*N+2*m+1) for m in range(t+1)]
            G = [Jet(1)]
            for a, b in zip(up, low):
                G.append(G[-1]*a/b)
            lowprod = product(low, Jet(1))
            cols = []
            for m in range(t+1):
                f = np.array([original(N, q, t, m, u, F) for u in range(t+1)], dtype=object)
                assert all(v == Jet(0) for v in O@f-f*lam[m])
                norm = sum(f[u]*G[u]*f[u] for u in range(t+1))
                cd = f[-1]*product((lam[m]-lam[h] for h in range(t+1) if h != m), Jet(1))/lowprod
                assert norm == cd
                cols.append(f)
                counts['actual_column_four_jets'] += t+1
                counts['generic_dual_norm_four_jets'] += 1
            for j in range(min(t, d//2)+1):
                l = d-j
                if j == l or t < l:
                    f = cols[j]
                    sigma = f[-1]*product((lam[j]-lam[h] for h in range(t+1) if h != j), Jet(1))/lowprod
                    outer = np.array([[f[u]*f[v]*G[v]/sigma for v in range(t+1)] for u in range(t+1)], dtype=object)
                    proj = I.copy()
                    for h in range(t+1):
                        if h != j:
                            proj = proj@(O-I*lam[h])
                            proj = np.array([[v/(lam[j]-lam[h]) for v in row] for row in proj], dtype=object)
                    for k in range(4):
                        assert np.array_equal(extract(outer, k), extract(proj, k))
                    counts['simple_projector_four_jets'] += 1
                    continue
                residues = []
                for m in (j, l):
                    f = cols[m]
                    b = f[-1]*product((lam[m]-lam[h] for h in range(t+1) if h not in (j, l)), Jet(1))/lowprod
                    R = np.array([[f[u]*f[v]*G[v]/b for v in range(t+1)] for u in range(t+1)], dtype=object)
                    polynomial = I.copy()
                    den = Jet(1)
                    for h in range(t+1):
                        if h != m:
                            polynomial = polynomial@(O-I*lam[h])
                            if h not in (j, l):
                                den *= lam[m]-lam[h]
                    polynomial = np.array([[v/den for v in row] for row in polynomial], dtype=object)
                    for k in range(4):
                        assert np.array_equal(extract(R, k), extract(polynomial, k))
                    residues.append(R)
                    counts['actual_residue_four_jets'] += 1
                Rj, Rl = residues
                delta = lam[j]-lam[l]
                Cl = np.array([[Jet(divide_simple_zero(v, delta)) for v in row] for row in Rj-Rl], dtype=object)
                M = (O-I*lam[j])@Cl
                for k in range(3):
                    assert np.array_equal(extract(M, k), extract(Rl, k))
                    assert np.array_equal(extract(Cl@Cl, k), extract(Cl, k))
                counts['completed_cluster_three_jets'] += 1
                f = cols[j]
                w = [Jet(divide_simple_zero(cols[j][u]-cols[l][u], delta)) for u in range(t+1)]
                sigma0 = sum(f[u].c[0]*w[u].c[0] for u in range(t+1)) % p
                assert sigma0
                exact = np.array([[f[u].c[0]*f[v].c[0]*pow(sigma0, -1, p) % p for v in range(t+1)] for u in range(t+1)], dtype=np.int64)
                assert np.array_equal(extract(M, 0), exact)
                counts['exact_double_rank_one_blocks'] += 1
    return counts


def steinberg_energy():
    mp.mp.dps = 100
    rows = []
    limit = 2*mp.catalan/mp.pi
    for N in (5, 9, 17, 33, 65, 129, 257, 513):
        m = (N-1)//2
        logs = [mp.mpf(0)]
        for r in range(1, m+1):
            logs.append(logs[-1]+mp.log(2*mp.sin(mp.pi*r/N)))
        f_abs = [mp.exp(logs[m]-logs[u]-logs[m-u]) for u in range(m+1)]
        energy = sum(v*v for v in f_abs)
        assert abs(mp.exp(2*logs[m])/N-1) < mp.mpf('1e-90')
        # An independent actual highest vector, including its phase,
        # verifies the bilinear norm and hence the native projector norm.
        if N <= 33:
            q = mp.exp(mp.pi*1j/N); Q = q*q; x = q**(N-1)
            fac = [mp.mpc(1)]
            for r in range(1, N):
                fac.append(fac[-1]*(1-Q**r))
            f = []
            for a in range(m+1):
                actual_ratio = fac[N-m+a-1]*fac[N-a-1]/fac[N-m-1]/fac[N-1]
                f.append((-1)**a*x**(-a)*Q**(a*(m-1)-a*(a-1)//2)*actual_ratio)
            sigma = sum(v*v for v in f)
            assert abs(abs(sigma)-1) < mp.mpf('1e-85')
            native = sum(abs(v)**2 for v in f)/abs(sigma)
            assert abs(native/energy-1) < mp.mpf('1e-85')
        rows.append(dict(N=N, normalized_log=float(mp.log(energy)/N), limit=float(limit)))
    return rows


def main():
    result = dict(status='PASS', generic=generic_high_adapter(), root_jets=root_jets(),
                  steinberg_native_energy=steinberg_energy(),
                  scope='Exact original generic adapter and dual/projector jets; native energy retained. Exponential simple-projector cost precludes a blanket polynomial operator norm; no assembled-source estimate.')
    Path(__file__).with_name('actual_matching_edge_native_projector_energy_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
