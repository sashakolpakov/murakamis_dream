#!/usr/bin/env python3
"""Surviving actual-source bulk curvature and its exact q-binomial fusion."""

import argparse
import json
from pathlib import Path

import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import (
    setup, graph_blocks, exact_cyclotomic_coefficient)


WORD = [1, -2, 1, 1, -2, -2]


def cyclotomic_vector(N, scalar, exponent):
    q = sp.Symbol('q')
    expression = sp.rem(scalar*q**(exponent % (2*N)), sp.cyclotomic_poly(2*N, q), q)
    poly = sp.Poly(expression, q)
    if poly.is_zero:
        return []
    return [int(poly.nth(j)) for j in range(poly.degree()+1)]


def verify_charges(G, flow):
    degree = [0]*G['anchor_count']
    for b, k in zip(G['blocks'], flow):
        assert 0 <= k <= b['length']
        degree[b['tail']] += b['length']-k
        degree[b['head']] += k
    assert degree == [G['N']-1]*G['anchor_count']


def bulk_family(N):
    assert N % 2 and N >= 3
    r, d = (N-1)//2, N-1
    H = HardyNetwork(N, 1)
    S = setup(H, 3, WORD)
    clocks = [0, r, r, r, 0, r]
    G = graph_blocks(H, S, clocks)
    assert G['anchor_count'] == 9
    expected = [(6, 7, d, d), (8, 0, r, -r), (0, 1, r, r),
                (7, 1, r, -r), (1, 2, r, -r), (1, 2, r, r),
                (2, 3, r, -r), (0, 3, d, -d), (3, 4, r, r),
                (4, 5, r, r), (2, 6, d, 0), (5, 7, d, -2),
                (4, 8, d, -2)]
    assert len(G['blocks']) == len(expected)
    for b, (u, v, L, phase) in zip(G['blocks'], expected):
        assert (b['tail'], b['head'], b['length']) == (u, v, L)
        assert b['w_exp'] == phase % (2*N)
    common_alpha = sum(b['alpha_exp']*b['length'] for b in G['blocks']) % (2*N)
    assert common_alpha == 0
    base = [r, 0, 0, 0, 0, 0, 0, r, 0, 0, r, 0, r]
    for t in range(r+1):
        flow = base.copy()
        for edge in (2, 4, 6):
            flow[edge] += t
        flow[7] -= t
        verify_charges(G, flow)
    phase = (G['blocks'][2]['w_exp']+G['blocks'][4]['w_exp']
             +G['blocks'][6]['w_exp']-G['blocks'][7]['w_exp']) % (2*N)
    assert phase == r and phase
    assert not any(G['blocks'][e]['closure'] for e in (2, 4, 6, 7))
    coefficient = exact_cyclotomic_coefficient(G)
    expected_coefficient = cyclotomic_vector(N, N, 2-r*r)
    assert coefficient == expected_coefficient and coefficient

    # Independently check the finite product fusion over the actual
    # cyclotomic finite field. The formula is an identity in q, not a
    # numerical positivity assumption.
    p, q, Q, F = H.p, H.q, H.Q, H.fac
    C = [F[r]*pow(F[j]*F[r-j] % p, -1, p)
         *pow(q, -j*(r-j), p) % p for j in range(r+1)]
    product = [0]*(d+1)
    for a, x in enumerate(C):
        for b, y in enumerate(C):
            product[a+b] = (product[a+b]+x*y*pow(q, 2*r*b, p)) % p
    assert product == [pow(q, r*j, p) for j in range(d+1)]
    for f in range(r+1):
        correlation = sum(C[a]*C[a+f]*pow(q, 2*r*a, p) for a in range(r-f+1)) % p
        assert correlation == pow(q, r*(r-f), p)
    B = sum(C[a]*pow(q, r*a, p) for a in range(r+1)) % p
    assert B == N*pow(F[r], -1, p) % p
    assert pow(q, -2*r+2*r*r, p)*B*B % p == N*pow(q, 2-r*r, p) % p
    return {'N': N, 'clocks': clocks, 'bulk_cycle_edges': [2, 4, 6, -7],
            'feasible_unit_augmentations': r, 'holonomy_q_exponent': phase,
            'exact_cyclotomic_coefficient': coefficient,
            'formula': f'{N}*q^({2-r*r})',
            'all_original_closure_blocks_retained': True,
            'finite_product_and_correlation_fusions_verified': True}


def figure_eight_family(N, h):
    H = HardyNetwork(N, 1)
    S = setup(H, 3, [1, -2, 1, -2])
    G = graph_blocks(H, S, [0, 0, h, N-1])
    coefficient = exact_cyclotomic_coefficient(G)
    assert coefficient == cyclotomic_vector(N, N, 4+h-h*h-N*h)
    return {'N': N, 'H': h, 'exact_nonzero_coefficient': coefficient,
            'source_closure_holonomy_exponent': (N+h+1) % (2*N)}


def topology():
    import snappy
    from spherogram import RationalTangle
    first = snappy.Link(braid_closure=WORD).exterior()
    second = RationalTangle(13, 5).numerator_closure().exterior()
    first_sig = first.triangulation_isosig()
    second_sig = second.triangulation_isosig()
    assert first_sig == second_sig == 'gLLPQccdefffhggaacv_aBBb'
    return {'exact_marked_triangulation_isosig': first_sig,
            'explicit_rational_tangle': '13/5', 'braid_word': WORD}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topology', action='store_true')
    args = parser.parse_args()
    result = {'bulk_curvature_and_fusion': [bulk_family(N) for N in (3, 5, 7, 9)],
              'full_source_closure_curvature': [figure_eight_family(N, h)
                                                for N in (3, 4, 5)
                                                for h in range(1, N-1)],
              'scope': 'Nonflat actual surviving source sectors; explicit polynomial-size fusion, not a volume theorem'}
    if args.topology:
        result['topology'] = topology()
    path = Path(__file__).with_name('anchor_phase_cycles_and_fusion_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS four exact surviving bulk-curvature/fusion families, '
          'six original closure families, capacities and source charges')


if __name__ == '__main__':
    main()
