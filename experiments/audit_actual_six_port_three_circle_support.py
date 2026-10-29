#!/usr/bin/env python3
"""Exact folded-source incidence and truncated-cube rank checks.

The physical support proof is the cleared generic-projector argument in
the companion note. These checks do not assume or prove nonvanishing of
every surviving actual source block.
"""
import itertools
import json
from math import comb
from pathlib import Path

import sympy as s


def admissible(a, b, c):
    return abs(a-b) <= c <= a+b


def folded_case(N):
    d, M = N-1, (N-1)//2
    source_rank, observed_blocks = 0, []
    cluster_rank_counts = {}
    for js in itertools.product(range(M+1), repeat=3):
        axes = [sorted({j, d-j}) for j in js]
        corners = list(itertools.product(*axes))
        allowed = [a for a in corners if admissible(*a)]
        count = len(allowed)
        source_rank += count
        cluster_rank_counts[count] = cluster_rank_counts.get(count, 0)+1
        full = len(allowed) == len(corners)
        assert full == (sum(js) >= d)
        if not full:
            # Every one-high/others-low corner is an explicit witness
            # whenever sum(js)<d; no unknown frame is involved.
            for axis in range(3):
                witness = list(js)
                witness[axis] = d-js[axis]
                assert tuple(witness) in corners
                assert not admissible(*witness)
        else:
            observed_blocks.append(js)
    assert source_rank == (N**3+N)//2
    K = 3*M-d
    expected = comb(K+3, 3) if K >= 0 else 0
    assert len(observed_blocks) == expected
    for js in observed_blocks:
        hs = tuple(M-j for j in js)
        e = K-sum(hs)
        assert all(h >= 0 for h in hs) and e >= 0
    if N % 2:
        edges = {js for js in observed_blocks if sum(j == M for j in js) >= 2}
        assert len(edges) == 3*M+1
    return {'N': N, 'actual_generic_source_rank': source_rank,
            'folded_cluster_rank_counts': cluster_rank_counts,
            'proved_three_circle_rank_upper': expected,
            'simplex_K': K,
            'odd_verified_reduction_edge_channels': 3*M+1 if N % 2 else None}


def cube_case(r):
    masks = range(1 << r)
    operators = []
    for i in range(r):
        A = s.zeros(1 << r)
        for m in masks:
            if not (m >> i) & 1:
                A[m | (1 << i), m] = 1
        operators.append(A)
    product = s.eye(1 << r)
    for A in operators:
        assert A*A == s.zeros(1 << r)
        product *= A
    assert product.rank() == 1
    # Simultaneous kernel is exactly the top monomial; the socle
    # argument in the note upgrades nonzero top action on a module
    # of this dimension to this regular representation.
    stacked = s.Matrix.vstack(*operators) if operators else s.zeros(0, 1)
    assert (1 << r)-stacked.rank() == 1
    return {'double_axes': r, 'regular_cube_dimension': 1 << r,
            'top_rank': 1, 'socle_dimension': 1,
            'scope': 'Regular algebra model; actual source nonvanishing is not inferred.'}


if __name__ == '__main__':
    levels = [folded_case(N) for N in range(2, 41)]
    cubes = [cube_case(r) for r in range(4)]
    result = {'status': 'PASS', 'folded_original_incidence': levels,
              'truncated_polynomial_rank_lemma': cubes,
              'scope': 'Exact incidence/rank upper bound and regular-cube algebra; no missing actual CG top coefficient or metric bound is assumed.'}
    Path(__file__).with_name('actual_six_port_three_circle_support_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 39 exact folded-source channel counts/simplex bounds; '
          '4 truncated-cube rank/socle models; no interior nonvanishing extrapolated')
