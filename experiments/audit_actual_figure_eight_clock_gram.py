#!/usr/bin/env python3
"""Complete ORIGINAL 4_1 clock sector, its coherent phase and Gram rate.

The exact tests use the literal original closure-contracted table, not an
isolated expanded coefficient. The uniform proof is in the companion note.
"""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_alternating_balanced_source import (
    figure_eight_blocks, check_actual_block_table)
from audit_actual_general_flow_fusion import graph_coefficient
from audit_actual_global_charged_bridge_flow import (
    setup, charged_data, charged_coefficient)
from audit_actual_signed_overbridge_unwinding import qbinom


def exact_checks():
    rows = []
    for k in (1, 2, 3):
        N, hs = 3*k+1, (0, 2*k, k, 2*k)
        H = HardyNetwork(N, 1)
        p, q, Q, d = H.p, H.q, H.Q, N-1
        S = setup(H, 3, [1, -2, 1, -2])
        scalar, actual_edges, nodes = check_actual_block_table(H, S, hs)
        edges = [{'u': u, 'v': v, 'L': L, 'a': pow(Q, start, p)}
                 for u, v, L, start in figure_eight_blocks(N, hs)]
        actual = graph_coefficient(H, edges, set(range(4)))

        # q^{-r(L-r)} [L r]_Q is the principal-embedding positive
        # sine-binomial, represented EXACTLY in the same root field.
        beta = lambda L, r: pow(q, -r*(L-r), p)*qbinom(H, L, r) % p
        positive_sum = sum(beta(2*k, r)*beta(2*k, k-r)
                           for r in range(k+1)) % p
        expected = N*pow(q, 3*k*k-2*k, p)*positive_sum*pow(H.fac[k], -1, p) % p
        assert actual == expected and actual, (N, actual, expected)

        # Reproduce every original closure/rescaling factor, rather than
        # comparing an unrelated polynomial with the same lengths.
        names = {0: 0, 4: 1, 5: 2, 6: 3}
        scales = {v: (pow(H.x, -1, p) if names[v] in (1, 3) else 1)
                  for v in nodes}
        scale_factor = 1
        for edge in actual_edges:
            scale_factor = scale_factor*pow(scales[edge['u']], edge['L'], p) % p
        for value in scales.values():
            scale_factor = scale_factor*pow(value, -d, p) % p
        old_coefficient = graph_coefficient(H, actual_edges, nodes)
        assert old_coefficient == scale_factor*actual % p
        forms, weight, *_ = charged_data(H, S, hs)
        root_factor = weight*scalar*scale_factor % p
        # This word has writhe zero, so both common Cartan copies cancel.
        assert pow(root_factor, 2*N, p) == 1
        if k == 1:
            full_original = weight*charged_coefficient(forms, len(S['events']), d, p) % p
            assert full_original == root_factor*actual % p

        # Exact normalizers cancel pairwise in the eight-block table.
        lengths = [L for _, _, L, _ in figure_eight_blocks(N, hs)]
        assert lengths == [d, 0, k, 2*k, 2*k, k, k, 2*k]
        rows.append({'N': N, 'clocks': hs, 'finite_prime': p,
                     'literal_table_coefficient': actual, 'formula_coefficient': expected,
                     'original_closure_and_unit_source_factors_checked': True,
                     'original_full_seven_anchor_coefficient_checked': k == 1})
    return rows


def positive_and_growth_checks():
    mp.mp.dps = 90
    V = 2*mp.im(mp.polylog(2, mp.e**(mp.j*mp.pi/3)))
    rows = []
    for k in (1, 2, 4, 8, 16, 32, 64, 128):
        N = 3*k+1
        q = mp.e**(mp.j*mp.pi/N)
        Q = q*q
        logs = [mp.mpf(0)]
        F = [mp.mpc(1)]
        for j in range(1, N):
            logs.append(logs[-1]+mp.log(2*mp.sin(mp.pi*j/N)))
            F.append(F[-1]*(1-Q**j))
        beta = lambda r: mp.exp(logs[2*k]-logs[r]-logs[2*k-r])
        terms = [beta(r)*beta(k-r) for r in range(k+1)]
        S = mp.fsum(terms)
        maximum = max(terms)
        assert maximum <= S <= (k+1)*maximum*(1+mp.mpf('1e-80'))
        maximizers = [r for r, val in enumerate(terms)
                      if abs(val/maximum-1) < mp.mpf('1e-70')]
        assert set(maximizers).issubset({k//2, (k+1)//2})
        # Direct complex coefficients independently verify common phase.
        if k <= 16:
            coeff = lambda r: (-1)**r*Q**(r*(r+1)//2)*F[2*k]/(F[r]*F[2*k-r])
            actual = mp.fsum(coeff(r)*coeff(k-r) for r in range(k+1))
            expected = (-q**(2*k+1))**k*S
            assert abs(actual/expected-1) < mp.mpf('1e-70')
        rate = 2*mp.pi*(mp.log(S)-logs[k])/N
        rows.append({'N': N, 'positive_terms': k+1,
                     'common_phase_tested': k <= 16,
                     'sector_2pi_log_rate': float(rate),
                     'limiting_twice_volume': float(2*V)})
    assert abs(rows[-1]['sector_2pi_log_rate']-float(2*V)) < .16
    return rows


def diagonal_metric_checks():
    mp.mp.dps = 70
    f = [mp.mpc(2, 3), mp.mpc(-4, 1), mp.mpc(1, -2)]
    a = [mp.mpc(1, 1), mp.mpc(2, -1), mp.mpc(-3, 2)]
    optimum = mp.fsum(abs(x*y) for x, y in zip(a, f))**2
    g = [abs(x)/abs(y) for x, y in zip(a, f)]
    budget = mp.fsum(z*abs(y)**2 for z, y in zip(g, f))*mp.fsum(
        abs(x)**2/z for x, z in zip(a, g))
    assert abs(budget/optimum-1) < mp.mpf('1e-65')
    return {'exact_optimized_diagonal_budget': True}


if __name__ == '__main__':
    result = {'status': 'PASS', 'exact_original_sectors': exact_checks(),
              'positive_sum_and_growth': positive_and_growth_checks(),
              'diagonal_metric': diagonal_metric_checks()}
    target = Path(__file__).with_name('actual_figure_eight_clock_gram_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: 3 exact complete original sectors, 8 positive-sum profiles, diagonal optimum')
