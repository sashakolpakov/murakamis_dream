#!/usr/bin/env python3
"""Whole original source: physical bridge continuation and charged full fusion."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import (
    setup, graph_blocks, charged_data, charged_coefficient)
from audit_actual_general_flow_fusion import normalized_graph, one_cycle_permutation
from audit_actual_signed_overbridge_unwinding import inv, polynomial, over_link
from audit_whole_fermat_toric_residue_and_wire_source import frame
from audit_actual_two_cut_ports import partial, word_matrix
from audit_original_source_cyclic_variation_peeling import supported


def coefficient(H, edges, charges):
    if any(q < 0 for q in charges.values()):
        return 0
    order = {v: i for i, v in enumerate(sorted(charges))}
    target = tuple(charges[v] for v in sorted(charges))
    P = {(0,)*len(order): 1}
    for e in edges:
        for r in range(e['L']):
            f = {order[e['u']]: 1}
            j = order[e['v']]
            f[j] = (f.get(j, 0)-e['a']*pow(H.Q, r, H.p)) % H.p
            nxt = {}
            for powers, c in P.items():
                for j, a in f.items():
                    if not a or powers[j] >= target[j]:
                        continue
                    new = powers[:j]+(powers[j]+1,)+powers[j+1:]
                    nxt[new] = (nxt.get(new, 0)+c*a) % H.p
            P = {k: v for k, v in nxt.items() if v}
            if not P:
                return 0
    return P.get(target, 0)


def fuse_full(H, edges, charges, identifier):
    """Any relative charges 0<=q<=d; exact arbitrary-exterior identity."""
    e = next(e for e in edges if e['id'] == identifier)
    assert e['L'] == H.N-1 and e['u'] != e['v']
    u, v, d, p = e['u'], e['v'], H.N-1, H.p
    q = charges[u]+charges[v]-d
    if q < 0:
        return 0, [], {}
    s = e['a']*inv(H.Q, p) % p
    scalar = pow(s, d-charges[u], p)
    out = []
    for old in edges:
        if old['id'] == identifier:
            continue
        new = old.copy()
        if new['u'] == u:
            scalar = scalar*pow(s, new['L'], p) % p
            new['u'], new['a'] = v, new['a']*inv(s, p) % p
        if new['v'] == u:
            new['v'], new['a'] = v, new['a']*s % p
        out.append(new)
    remaining = {a: b for a, b in charges.items() if a != u}
    remaining[v] = q
    return scalar, out, remaining


def reduce_source(H, edges, charges):
    """Extract loops/zero-charge vertices and contract every full block."""
    p, d, scalar = H.p, H.N-1, 1
    edges, charges, moves = [e.copy() for e in edges if e['L']], dict(charges), []
    while True:
        if any(q < 0 for q in charges.values()):
            return 0, [], {}, moves+['negative-charge-zero']
        loop = next((e for e in edges if e['u'] == e['v']), None)
        if loop is not None:
            v = loop['u']
            factor = 1
            for r in range(loop['L']):
                factor = factor*(1-loop['a']*pow(H.Q, r, p)) % p
            scalar = scalar*factor % p
            charges[v] -= loop['L']
            edges = [e for e in edges if e['id'] != loop['id']]
            moves.append('loop-charge-extraction')
            if not scalar:
                return 0, [], {}, moves+['exact-loop-zero']
            continue
        zero = next((v for v, q in charges.items() if q == 0), None)
        if zero is not None:
            out = []
            for e in edges:
                if e['u'] == zero:
                    scalar = (scalar*pow(-e['a'], e['L'], p)
                              *pow(H.Q, e['L']*(e['L']-1)//2, p)) % p
                    charges[e['v']] -= e['L']
                elif e['v'] == zero:
                    charges[e['u']] -= e['L']
                else:
                    out.append(e)
            edges = out
            del charges[zero]
            moves.append('zero-charge-boundary-push')
            continue
        full = next((e for e in edges if e['L'] == d), None)
        if full is None:
            return scalar, edges, charges, moves
        factor, edges, charges = fuse_full(H, edges, charges, full['id'])
        scalar = scalar*factor % p
        moves.append('charged-full-fusion')
        if not scalar:
            return 0, [], {}, moves+['saturated-cut-zero']


def physical_overbridges(S):
    """Join actual over encounters across identity and original closure wires."""
    rec = S['records']
    incoming = {v: (j, p == R['over_in'])
                for j, R in enumerate(rec) for p, v in enumerate(R['invars'])}
    closure = {v: (S['iv'][i], i) for i, v in enumerate(S['ov'])}
    following, coupons = {}, {}
    for j, R in enumerate(rec):
        v, cs = R['outvars'][R['over_out']], []
        for _ in range(len(rec)+S['width']+1):
            if v in incoming:
                nxt, over = incoming[v]
                if over:
                    following[j], coupons[j] = nxt, cs
                break
            v, head = closure[v]
            cs.append(head)
        else:
            raise AssertionError('All-over or untouched closed component')
    prev = set(following.values())
    paths = []
    for j in range(len(rec)):
        if j in prev:
            continue
        path = [j]
        while path[-1] in following:
            path.append(following[path[-1]])
        paths.append(path)
    assert sorted(j for path in paths for j in path) == list(range(len(rec)))
    return paths, coupons


def continued_wire_checks():
    rows = []
    for N in range(2, 11):
        H = HardyNetwork(N, 1)
        p, d = H.p, N-1
        gin, G, _ = frame(H, 2)
        gout, _, I = frame(H, 3)
        count = 0
        for t, eta in ((1, 1), (inv(H.Q, p), pow(H.x, 1-N, p))):
            adapter = G@np.diag([eta*pow(t, a, p) % p for a in range(N)])@I % p
            for L, s in itertools.product(range(N), repeat=2):
                a, b = 5, 7
                A, B = polynomial(H, a, L), polynomial(H, b, d-s)
                pout = np.array([sum(c*pow(z, j, p) for j, c in enumerate(A)) % p
                                 for z in gout], dtype=np.int64)
                pin = np.array([pow(z, -s, p)*sum(c*pow(z, -j, p)
                                  for j, c in enumerate(B)) % p for z in gin], dtype=np.int64)
                old = int(pin@(adapter@pout % p)) % p
                new = N*eta*over_link(H, L, s, a*t % p, b) % p
                assert old == new, (N, L, s, t)
                count += 1
        rows.append({'N': N, 'different_frame_original_identity_and_pivot_contractions': count})
    return rows


def relative_charge_checks():
    rows = []
    for N in range(2, 11):
        H = HardyNetwork(N, 1)
        p, d, a = H.p, N-1, 3
        B = polynomial(H, a, d)
        checks = 0
        for qx, qy, ex, ey in itertools.product(range(N), range(N), range(N+2), range(N+2)):
            k = d-qx+ex
            old = B[k] if 0 <= k <= d and ey+k == qy else 0
            q = qx+qy-d
            new = pow(a*inv(H.Q, p) % p, d-qx+ex, p) if q >= 0 and ex+ey == q else 0
            assert old == new
            checks += 1
        rows.append({'N': N, 'all_relative_charge_arbitrary_exterior_monomials': checks})
    return rows


def supported_clock_sets(N, width, word):
    """Exact original cyclic support, retaining actual propagated overclock h."""
    local = supported(N)
    answer = set()
    for tail in itertools.product(range(N), repeat=width-1):
        states = {((0,)+tuple((a+1) % N for a in tail), ())}
        for letter in word:
            pos, sign = abs(letter)-1, 1 if letter > 0 else -1
            nxt = set()
            for state, hs in states:
                for c, e, ks in local[state[pos], state[pos+1]]:
                    u, v, t, z = ks
                    h = u+v if sign > 0 else u+z
                    nxt.add((state[:pos]+(c, e)+state[pos+2:], hs+(h,)))
            states = nxt
        answer.update(hs for state, hs in states if state == (0,)+tail)
    return answer


def forced_bridge_checks():
    words = [(3, [1, -2, 1, -2]), (3, [1, 2, -1, -2]),
             (3, [1, 1, 2, 2, -1, 2]), (3, [-1, -2, -1, -2]),
             (4, [1, 2, -1, 3, 2]), (4, [1, -2, 3, -1, 2])]
    rows = []
    for N in (2, 3):
        H = HardyNetwork(N, 1)
        for width, word in words:
            assert one_cycle_permutation(width, word)
            S = setup(H, width, word)
            paths, coupons = physical_overbridges(S)
            oldpaths = S['paths']
            first = next(j for j, letter in enumerate(word) if abs(letter) == 1)
            last = max(j for j, letter in enumerate(word) if abs(letter) == 1)
            hs_set = supported_clock_sets(N, width, word)
            retained = 0
            for hs in hs_set:
                # Propagation is a whole overbridge SUM identity. Individual
                # supported cyclic paths need not have monotone overclocks.
                if any(hs[a] < hs[b] for path in paths for a, b in zip(path, path[1:])):
                    continue
                retained += 1
                if word[first] > 0:
                    path = next(path for path in paths if first in path)
                    mark = path.index(first)
                    assert all(hs[j] == N-1 for j in path[:mark])
                    assert all(hs[j] == 0 for j in path[mark:])
                else:
                    assert word[last] < 0
                    path = next(path for path in paths if last in path)
                    mark = path.index(last)
                    assert all(hs[j] == N-1 for j in path[:mark+1])
                    assert all(hs[j] == 0 for j in path[mark+1:])
                lengths = [N-1-hs[path[0]]] + [hs[a]-hs[b] for a, b in zip(path, path[1:])] + [hs[path[-1]]]
                assert lengths.count(N-1) == 1 and set(lengths) <= {0, N-1}
            rows.append({'N': N, 'width': width, 'word': word,
                         'open_bridge_count': len(oldpaths), 'physical_bridge_count': len(paths),
                         'cross_closure_over_links': sum(bool(cs) for cs in coupons.values()),
                         'supported_actual_clock_assignments': len(hs_set),
                         'after_exact_closed_overbridge_monotonicity': retained,
                         'source_bridge_has_exactly_one_full_block': True})
    return rows


def whole_source_checks():
    rows = []
    words = [(3, [1, -2, 1, -2]), (3, [1, 1, 1, 2, -1, 2]),
             (3, [-1, -2, -1, -2]), (4, [1, 2, -1, 3, 2])]
    for N in (2, 3):
        H = HardyNetwork(N, 1)
        p, d = H.p, N-1
        for width, word in words:
            S = setup(H, width, word)
            physical_paths, _ = physical_overbridges(S)
            total = 0
            count, moves, lowered, zeros = 0, 0, 0, 0
            for hs in itertools.product(range(N), repeat=len(word)):
                if any(any(hs[a] < hs[b] for a, b in zip(path, path[1:])) for path in S['paths']):
                    continue
                forms, weight, _, _ = charged_data(H, S, hs)
                old = charged_coefficient(forms, len(S['events']), d, p)
                if any(hs[a] < hs[b] for path in physical_paths for a, b in zip(path, path[1:])):
                    assert old == 0, (N, word, hs, 'closure bridge monotonicity')
                scalar, edges, nodes = normalized_graph(H, graph_blocks(H, S, hs))
                factor, reduced, charges, report = reduce_source(H, edges, {v: d for v in nodes})
                new = scalar*factor*coefficient(H, reduced, charges) % p
                assert old == new, (N, width, word, hs, old, new, report)
                total = (total+weight*new) % p
                count += 1
                moves += len(report)
                lowered += any(0 < q < d for q in charges.values())
                zeros += not new
            core = total*inv(N, p) % p
            W = word_matrix(word, H.plus, H.minus, width, N, p)
            expected = int(partial(W, H.pivot, width, N, p).sum())*inv(N, p) % p
            assert core == expected
            rows.append({'N': N, 'width': width, 'word': word, 'original_clock_sectors': count,
                         'exact_saturation_operations': moves, 'sectors_with_lower_relative_charges': lowered,
                         'exact_zero_sectors': zeros, 'original_complete_source_period': core,
                         'all_original_clock_feedback_normalizers_and_pivots_retained': True})
    return rows


def main():
    result = {'status': 'PASS', 'continued_original_source_wires': continued_wire_checks(),
              'arbitrary_relative_charge_kernel': relative_charge_checks(),
              'arbitrary_sign_physical_cut_bridge': forced_bridge_checks(),
              'whole_original_source_saturation_reduction': whole_source_checks(),
              'scope': ('Exact physical bridge continuation and full-block reduction of original source. '
                        'Residual charges and macrodefects remain; no global positive source, '
                        'geometric cycle coefficient or volume limit is asserted.')}
    Path(__file__).with_name('actual_forced_source_fusion_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS continued source wires, relative-charge kernels, forced physical bridges and whole-source fusion')


if __name__ == '__main__':
    main()
