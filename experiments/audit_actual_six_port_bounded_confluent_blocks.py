#!/usr/bin/env python3
"""Exact root-gap valuations and bounded joint-confluence lattice checks.

The physical-source proof is analytical. The tensor-Jordan lattice checks
test its saturation argument for every actual admissibility pattern below;
they are not substituted for a physical Clebsch-frame norm estimate.
"""

import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

z, t = sp.symbols('z t')


def gap_poly(a, b):
    p, q = 2*a+1, 2*b+1
    m = max(p, q)
    return sp.Poly(z**(m+p)+z**(m-p)-z**(m+q)-z**(m-q), z, domain=sp.QQ)


def valuation(poly, cyclo):
    order = 0
    while poly and not poly.is_zero:
        quotient, remainder = sp.div(poly, cyclo)
        if not remainder.is_zero:
            break
        order += 1
        poly = quotient
    return order


def actual_gap_case(N):
    d = N-1
    cyclo = sp.Poly(sp.cyclotomic_poly(2*N, z), z, domain=sp.QQ)
    pair_orders = []
    for a in range(N):
        partner = d-a
        if a == partner:
            continue
        order = valuation(gap_poly(a, partner), cyclo)
        assert order == 1
        pair_orders.append(order)
    total_zeros = []
    for a in range(1, 3*d+1):
        order = valuation(gap_poly(0, a), cyclo)
        expected = a % N == 0 or (a+1) % N == 0
        assert order == int(expected)
        if order:
            total_zeros.append(a)
    assert len(total_zeros) == (3 if N == 2 else 4)
    clusters = [tuple(sorted({a, d-a})) for a in range((N+1)//2)]
    ranks = []
    patterns = set()
    for groups in itertools.product(clusters, repeat=3):
        double_slots = [i for i, C in enumerate(groups) if len(C) == 2]
        branch_ids = []
        for bits in itertools.product((0, 1), repeat=len(double_slots)):
            indices = [C[0] for C in groups]
            for slot, bit in zip(double_slots, bits):
                indices[slot] = groups[slot][bit]
            a, b, c = indices
            if abs(a-b) <= c <= a+b:
                branch_ids.append(sum(bit << j for j, bit in enumerate(bits)))
        if branch_ids:
            ranks.append(len(branch_ids))
            patterns.add((len(double_slots), tuple(sorted(branch_ids))))
    assert max(ranks) <= 8
    assert sum(ranks) == (N**3+N)//2
    return ({'N': N, 'pair_gaps_all_simple': True,
             'total_spin_zero_gap_indices': total_zeros,
             'source_joint_rank_sum': sum(ranks),
             'maximum_joint_source_rank': max(ranks)}, patterns)


def jordan_pattern_case(count, branches):
    # Each pair has the regular family A=[[0,1],[0,t]]. Its primitive
    # eigenvectors are (1,0) and (1,t), with projector poles at most1.
    rows = 1 << count
    matrix = sp.Matrix(rows, len(branches),
       lambda row, col: t**int(row).bit_count()
                         if int(row) & ~branches[int(col)] == 0 else 0)
    smith = smith_normal_form(matrix, domain=sp.QQ.poly_ring(t))
    powers = []
    for j in range(len(branches)):
        diag = sp.Poly(smith[j, j], t)
        assert not diag.is_zero
        power = min(mon[0] for mon, coeff in diag.terms() if coeff)
        assert sp.degree(diag) == power
        assert 0 <= power <= count <= 3
        powers.append(power)
    return {'double_pairs': count, 'admissible_branches': list(branches),
            'exact_Smith_exponents': powers}


def denominator_factor_identity():
    for a in range(1, 25):
        gap = z+z**-1-z**(2*a+1)-z**(-2*a-1)
        factor = -z*z**(-2*a-2)*(1-z**(2*a))*(1-z**(2*a+2))
        assert sp.expand(gap-factor) == 0
    return {'exact_Laurent_gap_factorizations': 24}


if __name__ == '__main__':
    factor = denominator_factor_identity()
    gaps, patterns = [], set()
    for N in range(2, 21):
        row, new_patterns = actual_gap_case(N)
        gaps.append(row); patterns |= new_patterns
    lattices = [jordan_pattern_case(count, branches)
                for count, branches in sorted(patterns)]
    full = jordan_pattern_case(3, tuple(range(8)))
    assert full['exact_Smith_exponents'] == [0, 1, 1, 1, 2, 2, 2, 3]
    result = {'status': 'PASS', 'exact_denominator_factorization': factor,
              'physical_spectral_gap_valuation_families': gaps,
              'actual_admissibility_pattern_lattice_tests': lattices,
              'sharp_tensor_Jordan_test': full,
              'scope': 'Exact valuations and saturation-algorithm stress tests; no physical inverse-Gram or asymptotic estimate inferred.'}
    Path(__file__).with_name('actual_six_port_bounded_confluent_blocks_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(gaps)} exact physical root-gap families; '
          f'{len(lattices)} admissibility-pattern Smith tests; sharp three-step example')
