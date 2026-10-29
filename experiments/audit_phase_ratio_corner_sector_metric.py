#!/usr/bin/env python3
"""Actual normalized cap: reflected sector metric and exact projector norms."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_phase_ratio_bell_weights import source


def cap_case(N, j, epsilon, matrices=False):
    Q = mp.exp(2*mp.pi*mp.j/N)
    delta = mp.exp(mp.log(1-epsilon)/N)
    u = Q**(-j)*delta
    v = mp.exp(mp.log(epsilon)/N)
    P, L, _ = source(N, 1, u, v)
    h = [abs(L[a])/abs(P[a]) for a in range(N)]
    F = [mp.mpc(1)]
    for a in range(1, N):
        F.append(F[-1]*(1-Q**a))
    gp = gl = mp.mpc(1)
    if j:
        alpha, beta = F[N-j], N/F[N-1-j]
        assert abs(alpha*beta/(N*(1-Q**(-j)))-1) < mp.mpf('1e-75')
        gp, gl = v**(N-j)/alpha, v**j/beta
    Ph, Lh = [gp*p for p in P], [gl*l for l in L]
    hh = [abs(Lh[a])/abs(Ph[a]) for a in range(N)]
    for a in range(N):
        assert abs(hh[a]/h[a]/abs(gl/gp)-1) < mp.mpf('1e-75')
        step = abs(1-u*Q**a)*abs(1-u*Q**(a+1))/abs(v)**2
        assert abs(h[(a+1) % N]/h[a]/step-1) < mp.mpf('1e-65')
    cost = mp.fsum(abs(Ph[a]*Lh[a]) for a in range(N))
    base = abs(1-u)*mp.fsum(1/abs(1-u*Q**a) for a in range(N))
    exact_cost = base if not j else abs(epsilon)/(N*abs(1-Q**(-j)))*base
    assert abs(cost/exact_cost-1) < mp.mpf('1e-65')
    assert abs(mp.fsum(abs(Ph[a])**2*hh[a] for a in range(N))/cost-1) < mp.mpf('1e-75')
    assert cost <= 8*(1+abs(epsilon)*(1+mp.log(N)))

    s = (2*j) % N
    g = [h[a]*h[(s-a) % N] for a in range(N)]
    gh = [hh[a]*hh[(s-a) % N] for a in range(N)]
    for a in range(N):
        assert abs(gh[a]/gh[j]/(g[a]/g[j])-1) < mp.mpf('1e-75')
    z = lambda k: abs(1-delta*Q**k)
    reflected = mp.mpf(1)
    for ell in range(1, N):
        if ell > 1:
            reflected *= (z(ell-1)/z(-(ell-1)))**2
        predicted = reflected*z(ell)/z(-ell)
        actual = g[(j+ell) % N]/g[j]
        assert abs(actual/predicted-1) < mp.mpf('1e-65')
    B = 8*abs(epsilon)*(1+mp.log(N))
    spread = max(abs(mp.log(x/g[j])) for x in g)
    assert spread <= B*(1+mp.mpf('1e-50'))
    rank_one = mp.sqrt(mp.fsum(x/g[j] for x in g)*mp.fsum(g[j]/x for x in g))/N
    assert rank_one <= mp.exp(B)
    if not mp.im(epsilon):
        assert spread < mp.mpf('1e-65')
        assert abs(rank_one-1) < mp.mpf('1e-65')

    direct_checks = 0
    if matrices:
        normalized_g = np.array([float(x/g[j]) for x in g])
        indices = np.arange(N)
        fourier = np.exp(2j*np.pi*np.outer(indices, indices)/N)/np.sqrt(N)
        for r in range(N):
            w = fourier[:, r]
            Pi = np.outer(w, np.conj(w))
            weighted = np.sqrt(normalized_g)[:, None]*Pi/np.sqrt(normalized_g)[None, :]
            norm = np.linalg.svd(weighted, compute_uv=False)[0]
            assert abs(norm-float(rank_one)) < 2e-12
            direct_checks += 1
        chosen = fourier[:, :max(1, N//2)]
        Pi = chosen@chosen.conj().T
        weighted = np.sqrt(normalized_g)[:, None]*Pi/np.sqrt(normalized_g)[None, :]
        norm = np.linalg.svd(weighted, compute_uv=False)[0]
        assert norm <= float(mp.exp(B))*(1+2e-12)
        if not mp.im(epsilon):
            assert abs(norm-1) < 2e-12
        direct_checks += 1
    return {'N': N, 'cap_index': j, 'epsilon': str(epsilon),
            'source_cost': mp.nstr(cost, 16),
            'sector_metric_log_spread': mp.nstr(spread, 10),
            'exact_character_projector_norm': mp.nstr(rank_one, 16),
            'proved_projector_bound': mp.nstr(mp.exp(B), 16),
            'direct_projector_checks': direct_checks}


def opposite_orientation_case(N, j, epsilon):
    Q = mp.exp(-2*mp.pi*mp.j/N)
    delta = mp.exp(mp.log(1-epsilon)/N)
    u, v = Q**(-j)*delta, mp.exp(mp.log(epsilon)/N)
    P, L, _ = source(N, -1, u, v)
    h = [abs(l)/abs(p) for l, p in zip(L, P)]
    s = 2*j % N
    g = [h[a]*h[(s-a) % N] for a in range(N)]
    B = 8*abs(epsilon)*(1+mp.log(N))
    assert max(abs(mp.log(x/g[j])) for x in g) <= B


def main():
    mp.mp.dps = 130
    records = []
    for N in range(2, 19):
        for j in range(N):
            for epsilon in [mp.mpf('.03'), mp.mpf('-.03'),
                            mp.mpc('.03', '.02'), mp.exp(-N)*(1+mp.j/3)/10]:
                records.append(cap_case(N, j, epsilon, matrices=N <= 7))
    for N in [31, 64]:
        for j in [0, 1, N//2, N-2, N-1]:
            for epsilon in [mp.mpf('.04'), mp.mpc('-.02', '.03'),
                            mp.exp(-N)*(1+mp.j/3)]:
                records.append(cap_case(N, j, epsilon))
    opposite = 0
    for N in [2, 5, 11, 23]:
        for j in [0, 1, N-1]:
            opposite_orientation_case(N, j, mp.mpc('.02', '.03'))
            opposite += 1
    result = {'status': 'PASS', 'actual_normalized_cap_cases': len(records),
              'direct_character_and_sum_projector_checks': sum(x['direct_projector_checks'] for x in records),
              'opposite_orientation_cases': opposite,
              'records': records,
              'scope': ('Selected doubled corner sector only. Full regularized cap has other sectors; '
                        'interior sector propagation and triangulation edge identification are not asserted.')}
    Path(__file__).with_name('phase_ratio_corner_sector_metric_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS', len(records), 'actual normalized cap sectors;',
          result['direct_character_and_sum_projector_checks'], 'direct weighted projector checks;',
          opposite, 'opposite-root cases')


if __name__ == '__main__':
    main()
