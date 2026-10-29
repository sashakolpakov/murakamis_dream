#!/usr/bin/env python3
"""Global cut/flag/weighted jets in the ORIGINAL charged source."""

import itertools
import json
import math
from pathlib import Path
import random

import networkx as nx

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import charged_data, setup


def polynomial(factors, charges, p):
    zero = (0,)*len(charges)
    answer = {zero: 1}
    for F in factors:
        new = {}
        for powers, value in answer.items():
            for v, c in F.items():
                if powers[v] >= charges[v]:
                    continue
                target = powers[:v]+(powers[v]+1,)+powers[v+1:]
                new[target] = (new.get(target, 0)+value*c) % p
        answer = {key: val for key, val in new.items() if val}
    return answer


def coefficient(factors, charges, p):
    if min(charges, default=0) < 0 or sum(charges) != len(factors):
        return 0
    return polynomial(factors, charges, p).get(tuple(charges), 0)


def cut_data(factors, charges, I):
    inside, outside, cross = [], [], []
    for F in factors:
        vertices = set(F)
        if vertices <= I:
            inside.append(F)
        elif vertices.isdisjoint(I):
            outside.append(F)
        else:
            assert len(vertices) == 2
            vi = next(v for v in F if v in I)
            vo = next(v for v in F if v not in I)
            cross.append((vi, F[vi], vo, F[vo]))
    return inside, outside, cross, sum(charges[v] for v in I)-len(inside)


def cut_value(factors, charges, I, p):
    inside, outside, cross, e = cut_data(factors, charges, I)
    if not 0 <= e <= len(cross):
        return 0, 0
    total = 0
    for selected in itertools.combinations(range(len(cross)), e):
        S = set(selected)
        qi = [charges[v] if v in I else 0 for v in range(len(charges))]
        qo = [charges[v] if v not in I else 0 for v in range(len(charges))]
        scalar = 1
        for j, (vi, bi, vo, ao) in enumerate(cross):
            if j in S:
                qi[vi] -= 1
                scalar = scalar*bi % p
            else:
                qo[vo] -= 1
                scalar = scalar*ao % p
        total += scalar*coefficient(inside, qi, p)*coefficient(outside, qo, p)
    return total % p, math.comb(len(cross), e)


def feasible_assignment(factors, charges):
    graph = nx.DiGraph()
    for j, F in enumerate(factors):
        graph.add_edge('source', ('factor', j), capacity=1)
        for v in F:
            graph.add_edge(('factor', j), ('vertex', v), capacity=1)
    for v, q in enumerate(charges):
        graph.add_edge(('vertex', v), 'sink', capacity=q)
    value, flow = nx.maximum_flow(graph, 'source', 'sink')
    if value != len(factors):
        return None
    return [next(v for v in F if flow[('factor', j)].get(('vertex', v), 0))
            for j, F in enumerate(factors)]


def hall_and_cores(factors, charges, p):
    n = len(charges)
    all_sets = [set(v for v in range(n) if mask >> v & 1)
                for mask in range(1 << n)]
    feasible = all(cut_data(factors, charges, I)[3] >= 0 for I in all_sets)
    assignment = feasible_assignment(factors, charges)
    assert feasible == (assignment is not None)
    expected = coefficient(factors, charges, p)
    if not feasible:
        assert expected == 0
        return {'feasible': False, 'selected_coefficient': 0}
    residual = nx.DiGraph()
    residual.add_nodes_from(range(n))
    for F, assigned in zip(factors, assignment):
        for other in F:
            residual.add_edge(assigned, other)
    components = list(nx.strongly_connected_components(residual))
    index = {v: j for j, C in enumerate(components) for v in C}
    reduced = list(charges)
    scalar = 1
    core_factors = [[] for C in components]
    for F, assigned in zip(factors, assignment):
        if len({index[v] for v in F}) == 1:
            core_factors[index[assigned]].append(F)
        else:
            reduced[assigned] -= 1
            scalar = scalar*F[assigned] % p
    value = scalar
    for C, FF in zip(components, core_factors):
        q = [reduced[v] if v in C else 0 for v in range(n)]
        value = value*coefficient(FF, q, p) % p
    assert value == expected
    # Tight-set closure and the exact uncrossing count.
    tight = [I for I in all_sets if cut_data(factors, charges, I)[3] == 0]
    for I in tight:
        for J in tight:
            assert cut_data(factors, charges, I | J)[3] == 0
            assert cut_data(factors, charges, I & J)[3] == 0
            assert not any(set(F) & (I-J) and set(F) & (J-I) for F in factors)
    return {'feasible': True, 'selected_coefficient': expected,
            'tight_set_count': len(tight),
            'canonical_component_sizes': sorted(map(len, components)),
            'source_core_factorization': True}


def flagged_value(factors, charges, flag, p):
    deficits = [cut_data(factors, charges, I)[3] for I in flag]
    if min(deficits, default=0) < 0:
        assert coefficient(factors, charges, p) == 0
        return {'negative_deficit_zero': True}
    internal, boundary = [], []
    for F in factors:
        if all(len({v in I for v in F}) == 1 for I in flag):
            internal.append(F)
        else:
            boundary.append(F)
    n, r = len(charges), len(flag)
    answer = {((0,)*n, (0,)*r): (1, 1)}
    for F in boundary:
        next_answer = {}
        for (powers, jets), (coef, count) in answer.items():
            for v, c in F.items():
                increments = tuple(int(v in I and not set(F) <= I) for I in flag)
                tt = tuple(a+b for a, b in zip(jets, increments))
                if any(a > b for a, b in zip(tt, deficits)) or powers[v] >= charges[v]:
                    continue
                xx = powers[:v]+(powers[v]+1,)+powers[v+1:]
                old_coef, old_count = next_answer.get((xx, tt), (0, 0))
                next_answer[(xx, tt)] = ((old_coef+coef*c) % p, old_count+count)
        answer = next_answer
    kernel = {powers: value for (powers, jets), value in answer.items()
              if jets == tuple(deficits)}
    cell_poly = polynomial(internal, charges, p)
    total = 0
    for powers, (coef, count) in kernel.items():
        remaining = tuple(q-a for q, a in zip(charges, powers))
        total += coef*cell_poly.get(remaining, 0)
    assert total % p == coefficient(factors, charges, p)
    choice_count = sum(count for coef, count in kernel.values())
    bound = math.prod(math.comb(len(cut_data(factors, charges, I)[2]), e)
                      for I, e in zip(flag, deficits))
    assert choice_count <= bound
    return {'deficits': deficits, 'compatible_boundary_choices': choice_count,
            'product_binomial_bound': bound, 'exact_joint_jet': True}


def weighted_value(factors, charges, weights, p):
    low = sum(min(weights[v] for v in F) for F in factors)
    e = sum(q*w for q, w in zip(charges, weights))-low
    flags = [{v for v, w in enumerate(weights) if w >= r}
             for r in range(1, max(weights)+1)]
    assert e == sum(cut_data(factors, charges, I)[3] for I in flags)
    if e < 0:
        assert coefficient(factors, charges, p) == 0
        return {'negative_weighted_deficit_zero': True}
    internal, boundary = [], []
    for F in factors:
        (internal if len({weights[v] for v in F}) == 1 else boundary).append(F)
    # Endpoint-expanded finite jet, with equal-level products retained.
    n = len(charges)
    states = {((0,)*n, 0): (1, 1)}
    for F in boundary:
        minimum = min(weights[v] for v in F)
        new = {}
        for (powers, jet), (coef, count) in states.items():
            for v, c in F.items():
                t = jet+weights[v]-minimum
                if t > e or powers[v] >= charges[v]:
                    continue
                xx = powers[:v]+(powers[v]+1,)+powers[v+1:]
                a, b = new.get((xx, t), (0, 0))
                new[(xx, t)] = ((a+coef*c) % p, b+count)
        states = new
    pp = polynomial(internal, charges, p)
    total = count_total = 0
    for (powers, jet), (coef, count) in states.items():
        if jet == e:
            total += coef*pp.get(tuple(q-a for q, a in zip(charges, powers)), 0)
            count_total += count
    assert total % p == coefficient(factors, charges, p)
    bound = sum(math.comb(len(boundary), j) for j in range(min(e, len(boundary))+1))
    assert count_total <= bound
    return {'weights': weights, 'weighted_deficit': e,
            'compatible_boundary_choices': count_total,
            'binomial_sum_bound': bound, 'exact_weighted_jet': True}


def one_family(factors, charges, p, label):
    assert sum(charges) == len(factors) and all(F for F in factors)
    hall = hall_and_cores(factors, charges, p)
    candidates = []
    n = len(charges)
    for mask in range(1, (1 << n)-1):
        I = {v for v in range(n) if mask >> v & 1}
        _, _, cross, e = cut_data(factors, charges, I)
        if e < 0 or 0 <= e <= min(2, len(cross)):
            candidates.append((e, I))
    chosen = sorted(candidates, key=lambda x: (abs(x[0]), len(x[1])))[:8]
    expected = coefficient(factors, charges, p)
    for e, I in chosen:
        value, count = cut_value(factors, charges, I, p)
        assert value == expected
    flag = [set(range(1)), set(range(max(2, n//2)))] if n > 2 else [{0}]
    return {'label': label, 'anchors': n, 'factors': len(factors),
            'Hall_and_residual_cores': hall, 'audited_cuts': len(chosen),
            'nested_flag': flagged_value(factors, charges, flag, p),
            'weighted_ray': weighted_value(factors, charges,
                                            [j % 3 for j in range(n)], p)}


def main():
    actual = []
    for N, word, clocks in (
            (3, [1, -2, 1, -2], [0, 0, 1, 2]),
            (4, [1, -2, 1, -2], [0, 1, 1, 2]),
            (3, [1, -2, 1, 1, -2, -2], [0, 1, 1, 1, 0, 1])):
        H = HardyNetwork(N, 1)
        S = setup(H, 3, word)
        factors, W, _, _ = charged_data(H, S, clocks)
        assert W
        actual.append(one_family(factors, [N-1]*len(S['events']), H.p,
                                 {'N': N, 'word': word, 'original_clocks': clocks}))
    rng = random.Random(28471)
    synthetic = []
    for trial in range(24):
        n, M, p = 2+trial % 3, 3+trial % 6, 1009
        charges = [0]*n
        for j in range(M):
            charges[rng.randrange(n)] += 1
        factors = []
        for j in range(M):
            a, b = rng.randrange(n), rng.randrange(n)
            factors.append({a: 1} if a == b else {a: 1, b: rng.choice((1, p-1, 2))})
        synthetic.append(one_family(factors, charges, p, trial))
    # Feasible support is explicitly weaker than nonzero coefficient.
    cancellation = hall_and_cores([{0: 1, 1: 1008}, {0: 1, 1: 1}], [1, 1], 1009)
    assert cancellation['feasible'] and cancellation['selected_coefficient'] == 0
    path = Path(__file__).with_name('charged_source_cut_jets_results.json')
    path.write_text(json.dumps({'actual_original_source_families': actual,
                                'general_loops_and_multiple_factor_families': synthetic,
                                'Hall_feasible_phase_cancellation': cancellation}, indent=2)+'\n')
    print('PASS actual whole-source cut/flag/weighted jets; Hall support with loops; '
          'canonical residual-core factorization; phase cancellation retained')


if __name__ == '__main__':
    main()
