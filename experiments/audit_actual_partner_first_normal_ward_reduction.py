#!/usr/bin/env python3
"""Exact first-normal Ward interpolation; no higher-normal assertion."""
import itertools
import json
import random
from pathlib import Path

import sympy as sp

from audit_actual_racah_partner_reflection_identity import normalized_metric_jet
from audit_actual_supported_racah_common_phase_and_normal_metric import forms, root_field

PAIRS = ((0, 2), (1, 3), (4, 5))
FACES = ((0, 1, 4), (2, 3, 4), (0, 3, 5), (1, 2, 5))
BITS = list(itertools.product((0, 1), repeat=6))
GRID = list(itertools.product(range(3), repeat=3))


def grid_bits(state, pairs):
    bits = [0] * 6
    for s, (big, small) in zip(state, pairs):
        if s == 1:
            bits[small] = 1
        elif s == 2:
            bits[big] = 1
    return tuple(bits)


def grid_data(delta):
    pairs = [tuple(sorted(pair, key=lambda i: (-delta[i], i))) for pair in PAIRS]
    sums = [delta[a] + delta[b] for a, b in pairs]
    gaps = [delta[a] - delta[b] for a, b in pairs]
    actual = []
    predicted = []
    for state in GRID:
        us = [(-s, -d, d)[v] for v, s, d in zip(state, sums, gaps)]
        if min(us[0] + us[1], us[0] + us[2], us[1] + us[2]) > 0:
            actual.append(state)
        plus = [i for i, v in enumerate(state) if v == 2]
        if len(plus) == 3 and min(gaps[0] + gaps[1], gaps[0] + gaps[2], gaps[1] + gaps[2]) > 0:
            predicted.append(state)
        elif len(plus) == 2:
            r = next(i for i in range(3) if i not in plus)
            magnitude = sums[r] if state[r] == 0 else gaps[r]
            if magnitude < min(gaps[i] for i in plus):
                predicted.append(state)
    assert actual == predicted and len(actual) <= 3
    if sum(d == 0 for d in gaps) >= 2:
        assert not actual
    if len(actual) == 3:
        r = min(range(3), key=lambda i: gaps[i])
        others = [i for i in range(3) if i != r]
        assert sums[r] < min(gaps[i] for i in others)
        dominant = [pairs[i][0] for i in others]
        face = next(face for face in FACES if all(i in face for i in dominant))
        for bits in BITS:
            signed = [(2*bits[i]-1)*delta[i] for i in range(6)]
            us = [sum(signed[i] for i in pair) for pair in PAIRS]
            live = min(us[0]+us[1], us[0]+us[2], us[1]+us[2]) > 0
            assert live == all(bits[i] for i in dominant)
            if live:
                faces = [sum(signed[i] for i in f) for f in FACES]
                assert faces.count(max(faces)) == 1
                assert FACES[faces.index(max(faces))] == face
    return pairs, actual


def interpolate(bits, pairs, values, p):
    choices = []
    for big, small in pairs:
        local = (bits[big], bits[small])
        choices.append({(0, 0): [(0, 1)], (0, 1): [(1, 1)],
                        (1, 0): [(2, 1)], (1, 1): [(1, 1), (2, 1), (0, -1)]}[local])
    total = 0
    count = 0
    for branch in itertools.product(*choices):
        state = tuple(v[0] for v in branch)
        sign = branch[0][1] * branch[1][1] * branch[2][1]
        total += sign * values[grid_bits(state, pairs)][1]
        count += 1
    assert count <= 27
    return total % p


def actual_family(N, base):
    D = N - 1
    p, eta = root_field(N)
    q = eta * eta % p
    pairs, exceptions = grid_data([D - 2 * v for v in base])
    values = {}
    cache = {}
    live = 0
    for bits in BITS:
        spins = tuple(D - v if b else v for b, v in zip(bits, base))
        if spins not in cache:
            cache[spins] = normalized_metric_jet(N, spins, q, p)[0]
        values[bits] = cache[spins]
        live += min(forms(spins)[2]) > 2 * D
    assert len({v[0] for v in values.values()}) == 1
    checks = 0
    for a, b in PAIRS:
        others = [i for i in range(6) if i not in (a, b)]
        for other_bits in itertools.product((0, 1), repeat=4):
            fixed = dict(zip(others, other_bits))
            total = 0
            for u, v in itertools.product((0, 1), repeat=2):
                bits = tuple(u if i == a else v if i == b else fixed[i] for i in range(6))
                total += (-1) ** (u + v) * values[bits][1]
            assert total % p == 0
            checks += 1
    for bits in BITS:
        assert interpolate(bits, pairs, values, p) == values[bits][1]
    return dict(N=N, folded=base, prime=p, unique_generic_germs=len(cache),
                exact_Ward_squares=checks, exact_interpolated_first_normals=64,
                grid_exception_count=len(exceptions), live_tail_bit_branches=live)


def rank_defect():
    delta = (5, 19, 3, 9, 4, 16)
    supports = [tuple(i for i in vals if i >= 0)
                for vals in itertools.product((-1, 0, 2), (-1, 1, 3), (-1, 4, 5))]
    rows = []
    combined = []
    vector = lambda bits: [int(all(bits[i] for i in support)) for support in supports]
    for bits in BITS:
        us = [sum((2 * bits[i] - 1) * delta[i] for i in pair) for pair in PAIRS]
        if min(us[0] + us[1], us[0] + us[2], us[1] + us[2]) <= 0:
            rows.append(vector(bits))
            combined.append(vector(bits))
            assert not bits[1] or not bits[5]
        else:
            signed = [(2*bits[i]-1)*delta[i] for i in range(6)]
            faces = [sum(signed[i] for i in face) for face in FACES]
            assert faces.count(max(faces)) == 1
            face = FACES[faces.index(max(faces))]
            assert face == (1, 2, 5)
            dual = tuple(bit if i in face else 1-bit for i, bit in enumerate(bits))
            combined.append([x-y for x,y in zip(vector(bits),vector(dual))])
            assert bits[1]*bits[5] == dual[1]*dual[5]
            assert bits[1]*bits[2]*bits[5] == dual[1]*dual[2]*dual[5]
    matrix = sp.Matrix(rows)
    assert matrix.shape == (48, 27) and matrix.rank() == 24
    assert sp.Matrix(combined).rank() == 25
    assert min(forms((35, 21, 37, 31, 36, 24))[1]) >= 80
    return dict(D=80, folded=(35, 21, 37, 31, 36, 24),
                tail_free_vertices=48, first_normal_function_space_dimension=27,
                exact_rational_constraint_rank=24, remaining_dimension=3,
                combined_Fourier_partner_constraint_rank=25,
                combined_remaining_dimension=2,
                explicit_surviving_Boolean_functions=['b*f','b*c*f'])


def main():
    rng = random.Random(4817)
    for _ in range(3000):
        grid_data([rng.randrange(41) for _ in range(6)])
    families = []
    for N in range(3, 11):
        D = N - 1
        supported = [x for x in itertools.product(range(D // 2 + 1), repeat=6)
                     if min(forms(x)[1]) >= D]
        selected = sorted({supported[i] for i in (0, len(supported)//4, len(supported)//2, len(supported)-1)})
        families.extend(actual_family(N, x) for x in selected)
    live_balanced = [actual_family(3*m+1, (m,) * 6) for m in range(1, 5)]
    assert all(row['grid_exception_count'] == 0 and row['live_tail_bit_branches'] > 0
               for row in live_balanced)
    result = dict(status='PASS', exact_source_families=families,
                  genuinely_live_tail_opposite_equal_families=live_balanced,
                  independently_sampled_deficit_classifications=3000,
                  interpolation_obstruction=rank_defect(),
                  scope='Exact first-normal source Ward equations and all64 interpolation. At most3 exceptional currents, reduced to at most2 using Fourier partner differences by the uniform cylinder proof. The combined rank25 example proves two is sharp for these relations. Higher normals and positive physical transport are not asserted.')
    Path(__file__).with_name('actual_partner_first_normal_ward_reduction_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(families)+len(live_balanced), 'actual source families; all64 first-normal interpolation; exact ranks24/25 and two-current sharpness')


if __name__ == '__main__':
    main()
