#!/usr/bin/env python3
"""Whole original signed braid as an alias-free charged bridge coefficient."""

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_signed_overbridge_unwinding import (
    conditional, inv, make_network, over_link, over_paths, qbinom)
from audit_actual_two_cut_ports import partial, word_matrix


def setup(H, width, word):
    records, iv, ov, ir, outr = make_network(H, width, word)
    paths = over_paths(records)
    events = []
    selected = set()
    for path in paths:
        first, last = records[path[0]], records[path[-1]]
        events.append({'kind': 'bridge', 'path': path,
                       'input': first['invars'][first['over_in']],
                       'output': last['outvars'][last['over_out']]})
        selected.update(records[j]['outvars'][records[j]['over_out']] for j in path[:-1])
    for i in range(width):
        events.append({'kind': 'closure', 'head': i, 'input': ov[i], 'output': iv[i]})
    under = {}
    roots = dict(zip(iv, ir))
    for j, R in enumerate(records):
        ui, uo = R['invars'][1-R['over_in']], R['outvars'][1-R['over_out']]
        assert ui not in under
        under[ui] = (uo, j)
        for k in (0, 1):
            roots[R['outvars'][k]] = R['out'][k][0][0]
    expected = set(iv) | set(ov) | {v for R in records for v in R['vars']}
    expected -= selected
    return {'records': records, 'iv': iv, 'ov': ov, 'paths': paths, 'events': events,
            'under': under, 'roots': roots, 'expected': expected,
            'width': width, 'word': list(word)}


def segment_coordinates(H, S, clocks):
    p, Q, x = H.p, H.Q, H.x
    mapping, anchor_roots, terminal = {}, [], []
    inputs = {event['input'] for event in S['events']}
    for a, event in enumerate(S['events']):
        v = event['output']
        anchor_roots.append(S['roots'][v])
        zeta, shift = 1, 0
        while True:
            assert v not in mapping
            mapping[v] = (a, zeta, shift)
            assert S['roots'][v]*pow(Q, shift, p) % p == anchor_roots[a]*zeta % p
            if v not in S['under']:
                assert v in inputs
                terminal.append(v)
                break
            v, j = S['under'][v]
            sign, h = S['records'][j]['sign'], clocks[j]
            zeta = zeta*pow(x, sign, p)*pow(Q, -sign*h, p) % p
            shift = (shift-sign*h) % H.N
    assert set(mapping) == S['expected']
    assert set(terminal) == inputs and len(terminal) == len(inputs)
    return mapping, anchor_roots


def segment_q_exponents(H, S, clocks):
    """Exact zeta_v=q^exponent, using q of order2N and x=q^(N-1)."""
    modulus = 2*H.N
    assert H.x == pow(H.q, H.N-1, H.p)
    exponents = {}
    for event in S['events']:
        v, exponent = event['output'], 0
        while True:
            assert v not in exponents
            exponents[v] = exponent % modulus
            if v not in S['under']:
                break
            v, j = S['under'][v]
            sign, h = S['records'][j]['sign'], clocks[j]
            exponent += (H.N-1)*sign-2*sign*h
    return exponents


def graph_blocks(H, S, clocks):
    """Authoritative grouped polynomial graph and exact positive-binomial phases.

    A block means product_r<length(alpha X_tail-Q^r beta X_head).
    After alpha^length, its k-head-charge coefficient has positive sine
    q-binomial magnitude and phase q^(w_exp*k), where all exponents are
    integers modulo2N. This function does not assert graph flatness.
    """
    N, p, d, modulus = H.N, H.p, H.N-1, 2*H.N
    mapping, roots = segment_coordinates(H, S, clocks)
    exponents = segment_q_exponents(H, S, clocks)
    assert all(pow(H.q, exponents[v], p) == mapping[v][1] for v in mapping)
    blocks = []

    def append(event, kind, length, v, w, beta_exp, predicted_exp):
        if not length:
            return
        alpha = exponents[v] % modulus
        beta = (beta_exp+exponents[w]) % modulus
        phase = (N+beta-alpha+length-1) % modulus
        assert phase == predicted_exp % modulus
        blocks.append({'event': event, 'kind': kind, 'tail': mapping[v][0],
                       'head': mapping[w][0], 'length': length,
                       'tail_port': v, 'head_port': w,
                       'alpha_exp': alpha, 'beta_exp': beta,
                       'w_exp': phase, 'closure': kind == 'closure'})

    for ei, event in enumerate(S['events']):
        Zin, Zout = event['input'], event['output']
        if event['kind'] == 'closure':
            texp = 0 if event['head'] == 0 else -2
            append(ei, 'closure', d, Zin, Zout, 2+texp,
                   texp+exponents[Zout]-exponents[Zin])
            continue
        path = event['path']
        hs = [clocks[j] for j in path]
        signs = [S['records'][j]['sign'] for j in path]
        us = [S['records'][j]['outvars'][1-S['records'][j]['over_out']] for j in path]
        aexps = [(-2*h-(N-1) if sign > 0 else N+1) for h, sign in zip(hs, signs)]
        bexps = [(2*h+2 if sign > 0 else 2) for h, sign in zip(hs, signs)]
        append(ei, 'input', d-hs[0], Zin, us[0], bexps[0],
               signs[0]*hs[0]+exponents[us[0]]-exponents[Zin])
        for j in range(len(path)-1):
            append(ei, 'internal', hs[j]-hs[j+1], us[j], us[j+1],
                   -2+aexps[j]+bexps[j+1],
                   signs[j+1]*hs[j+1]-signs[j]*hs[j]+exponents[us[j+1]]-exponents[us[j]])
        append(ei, 'output', hs[-1], us[-1], Zout, aexps[-1],
               -signs[-1]*hs[-1]+exponents[Zout]-exponents[us[-1]])
    baseline = [0]*len(S['events'])
    for block in blocks:
        baseline[block['tail']] += block['length']
    return {'N': N, 'modulus': modulus, 'anchor_count': len(S['events']),
            'clocks': list(clocks), 'blocks': blocks, 'baseline_outdegree': baseline,
            'required_in_minus_out': [d-value for value in baseline]}


def linear_form(mapping, v, cv, w, cw, p):
    a, za, _ = mapping[v]
    b, zb, _ = mapping[w]
    answer = {a: cv*za % p}
    answer[b] = (answer.get(b, 0)+cw*zb) % p
    return {k: value for k, value in answer.items() if value % p}


def charged_data(H, S, clocks):
    N, p, Q, x, d = H.N, H.p, H.Q, H.x, H.N-1
    mapping, anchor_roots = segment_coordinates(H, S, clocks)
    forms, weight = [], 1
    for event in S['events']:
        Zin, Zout = event['input'], event['output']
        weight = weight*pow(mapping[Zin][1], -d, p) % p
        before = len(forms)
        if event['kind'] == 'closure':
            eta, t = (1, 1) if event['head'] == 0 else (x*inv(pow(x, N, p), p) % p, inv(Q, p))
            assert all(int(H.pivot[a]) == x*inv(pow(x, N, p), p)*pow(Q, -a, p) % p
                       for a in range(N))
            weight = weight*eta % p
            for r in range(1, N):
                forms.append(linear_form(mapping, Zin, 1, Zout, -pow(Q, r, p)*t, p))
        else:
            path = event['path']
            hs = [clocks[j] for j in path]
            assert all(a >= b for a, b in zip(hs, hs[1:]))
            alpha, beta, u = [], [], []
            for j, h in zip(path, hs):
                R = S['records'][j]
                sign = R['sign']
                alpha.append((pow(Q, -h, p)*inv(x, p) if sign > 0 else Q*x) % p)
                beta.append(pow(Q, h+1, p) if sign > 0 else Q)
                u.append(R['outvars'][1-R['over_out']])
                weight = (weight*pow(H.kappa, sign, p)*pow(-1, h, p)
                          *pow(Q, sign*h*(h+1)//2, p)) % p
            for k in range(len(path)-1):
                h, hn = hs[k], hs[k+1]
                weight = (weight*pow(-alpha[k], hn, p)*pow(Q, hn*(hn-1)//2, p)
                          *qbinom(H, h, hn)) % p
            for r in range(d-hs[0]):
                forms.append(linear_form(mapping, Zin, 1, u[0], -pow(Q, r, p)*beta[0], p))
            for k in range(len(path)-1):
                for r in range(hs[k]-hs[k+1]):
                    forms.append(linear_form(mapping, u[k], 1, u[k+1],
                                             -pow(Q, r-1, p)*alpha[k]*beta[k+1], p))
            for r in range(hs[-1]):
                forms.append(linear_form(mapping, u[-1], 1, Zout, -pow(Q, r, p)*alpha[-1], p))
        assert len(forms)-before == d
    assert len(forms) == len(S['events'])*d
    return forms, weight, mapping, anchor_roots


def charged_coefficient(forms, anchors, d, p):
    zero = (0,)*anchors
    terms = {zero: 1}
    for form in forms:
        new = {}
        for powers, value in terms.items():
            for a, c in form.items():
                if powers[a] == d:
                    continue
                target = powers[:a]+(powers[a]+1,)+powers[a+1:]
                new[target] = (new.get(target, 0)+value*c) % p
        terms = {key: value for key, value in new.items() if value}
        if not terms:
            return 0
    return terms.get((d,)*anchors, 0)


def evaluate_forms(forms, values, p):
    answer = 1
    for form in forms:
        answer = answer*sum(coef*values[a] for a, coef in form.items()) % p
    return answer


def dehomogenized_coefficient(forms, anchors, d, p):
    terms = {(0,)*(anchors-1): 1}
    for form in forms:
        new = {}
        for powers, value in terms.items():
            for a, c in form.items():
                if a == anchors-1:
                    target = powers
                else:
                    if powers[a] == d:
                        continue
                    target = powers[:a]+(powers[a]+1,)+powers[a+1:]
                new[target] = (new.get(target, 0)+value*c) % p
        terms = {key: value for key, value in new.items() if value}
        if not terms:
            return 0
    return terms.get((d,)*(anchors-1), 0)


def coefficient_from_positive_phase_blocks(H, graph):
    """Same exact coefficient, with the sine-binomial phase extracted."""
    N, p, k, d = H.N, H.p, graph['anchor_count'], H.N-1
    terms = {(0,)*k: 1}
    for block in graph['blocks']:
        L, a, b = block['length'], block['tail'], block['head']
        pref = pow(H.q, block['alpha_exp']*L, p)
        choices = []
        for r in range(L+1):
            sine_binomial = qbinom(H, L, r)*pow(H.q, -r*(L-r), p) % p
            value = pref*sine_binomial*pow(H.q, block['w_exp']*r, p) % p
            choices.append((r, value))
        new = {}
        for powers, value in terms.items():
            for r, c in choices:
                target = list(powers)
                target[a] += L-r
                target[b] += r
                if max(target) > d:
                    continue
                target = tuple(target)
                new[target] = (new.get(target, 0)+value*c) % p
        terms = {key: value for key, value in new.items() if value}
        if not terms:
            return 0
    return terms.get((d,)*k, 0)


def exact_cyclotomic_coefficient(graph):
    """Exact Z[q]/Phi_(2N) coefficient, for a candidate actual graph sector.

    This is independent of any finite prime and distinguishes a truly
    vanishing grouped source from a merely feasible nonflat flow graph.
    It is an exact certificate helper, not a polynomial-time algorithm.
    """
    N, k, d = graph['N'], graph['anchor_count'], graph['N']-1
    linear = []
    for block in graph['blocks']:
        for r in range(block['length']):
            linear.append(((block['tail'], block['alpha_exp']),
                           (block['head'], block['beta_exp']+2*r+N)))
    dtype = np.int64 if len(linear) < 61 else object
    start = np.zeros(N, dtype=dtype)
    start[0] = 1
    terms = {(0,)*k: start}

    def shifted(poly, exponent):
        exponent %= 2*N
        amount, sign = exponent % N, 1 if exponent < N else -1
        result = np.empty(N, dtype=dtype)
        if not amount:
            result[:] = sign*poly
        else:
            result[amount:] = sign*poly[:N-amount]
            result[:amount] = -sign*poly[N-amount:]
        return result

    for choices in linear:
        new = {}
        for powers, value in terms.items():
            for a, exponent in choices:
                if powers[a] == d:
                    continue
                target = powers[:a]+(powers[a]+1,)+powers[a+1:]
                term = shifted(value, exponent)
                if target in new:
                    new[target] += term
                else:
                    new[target] = term
        terms = {key: value for key, value in new.items() if np.any(value)}
        if not terms:
            return []
    value = terms.get((d,)*k)
    if value is None:
        return []
    qvar = sp.Symbol('q')
    polynomial = sp.Poly(sum(int(c)*qvar**j for j, c in enumerate(value)), qvar, domain=sp.ZZ)
    cyclotomic = sp.Poly(sp.cyclotomic_poly(2*N, qvar), qvar, domain=sp.ZZ)
    reduced = polynomial.rem(cyclotomic)
    if reduced.is_zero:
        return []
    return [int(reduced.nth(j)) for j in range(reduced.degree()+1)]


def original_reduced_grid_value(H, S, clocks, mapping, anchor_labels):
    N, p, Q, d = H.N, H.p, H.Q, H.N-1
    labels = {v: (anchor_labels[a]+shift) % N for v, (a, _, shift) in mapping.items()}
    values = {v: S['roots'][v]*pow(Q, labels[v], p) % p for v in mapping}
    total = 1
    for event in S['events']:
        if event['kind'] == 'closure':
            i = event['head']
            eta, t = (1, 1) if i == 0 else (H.x*inv(pow(H.x, N, p), p) % p, inv(Q, p))
            ratio = t*values[event['output']]*inv(values[event['input']], p) % p
            total = total*eta*inv(N, p)*sum(pow(ratio, a, p) for a in range(N)) % p
            continue
        entries = []
        for j in event['path']:
            R = S['records'][j]
            si, so = R['invars'][1-R['over_in']], R['outvars'][1-R['over_out']]
            E = conditional(H, R, 'over', labels[si], labels[so])
            assert E['h'] == clocks[j]
            entries.append(E)
        val = (int(entries[0]['pin'][labels[event['input']]])
               *int(entries[-1]['pout'][labels[event['output']]])) % p
        for E in entries:
            val = val*E['c'] % p
        for A, B in zip(entries, entries[1:]):
            val = val*N*over_link(H, A['h'], B['h'], A['a'], B['b']) % p
        total = total*val % p
    return total


def whole_case(N, width, word, verify_grid=False):
    H = HardyNetwork(N, 1)
    p, d = H.p, N-1
    S = setup(H, width, word)
    k = len(S['events'])
    contribution = 0
    clocks_checked = 0
    pointwise = 0
    aliases = 0
    exact_coefficients = 0
    for clocks in itertools.product(range(N), repeat=len(word)):
        if any(any(clocks[a] < clocks[b] for a, b in zip(path, path[1:])) for path in S['paths']):
            continue
        forms, weight, mapping, roots = charged_data(H, S, clocks)
        coefficient = charged_coefficient(forms, k, d, p)
        assert coefficient == dehomogenized_coefficient(forms, k, d, p)
        graph = graph_blocks(H, S, clocks)
        assert coefficient == coefficient_from_positive_phase_blocks(H, graph)
        if exact_coefficients < 3:
            exact = exact_cyclotomic_coefficient(graph)
            assert sum(c*pow(H.q, j, p) for j, c in enumerate(exact)) % p == coefficient
            exact_coefficients += 1
        contribution = (contribution+weight*coefficient) % p
        # Verify both the homogeneous bridge formula and signed clock bijection
        # directly against original crossing tables, with no new boundary vectors.
        for sample in range(2):
            labels = [(a+sample) % N for a in range(k)]
            values = [r*pow(H.Q, ell, p) % p for r, ell in zip(roots, labels)]
            new = (weight*inv(pow(N, k, p), p)*evaluate_forms(forms, values, p)
                   *np.prod([pow(value, -d, p) for value in values], dtype=object)) % p
            old = original_reduced_grid_value(H, S, clocks, mapping, labels)
            assert int(new) == old, (N, width, word, clocks, labels, new, old)
            pointwise += 1
        if verify_grid and aliases < 3:
            # Both the original propagated grids and a wholly different
            # set of anchor centers give the SAME charged coefficient.
            for chosen_roots in (roots, list(range(11, 11+k))):
                actual = 0
                for labels in itertools.product(range(N), repeat=k):
                    values = [r*pow(H.Q, ell, p) % p for r, ell in zip(chosen_roots, labels)]
                    monomial = 1
                    for value in values:
                        monomial = monomial*pow(value, -d, p) % p
                    actual = (actual+monomial*evaluate_forms(forms, values, p)) % p
                assert actual == pow(N, k, p)*coefficient % p
            aliases += 1
        clocks_checked += 1
    core = contribution*inv(N, p) % p
    W = word_matrix(word, H.plus, H.minus, width, N, p)
    cut = partial(W, H.pivot, width, N, p)
    assert np.array_equal(cut, np.diag(np.diag(cut)))
    expected = int(cut.sum())*inv(N, p) % p
    assert core == expected, (N, width, word, core, expected)
    external = H.dimension*pow(H.twist, -sum(1 if x > 0 else -1 for x in word), p) % p
    return {'N': N, 'width': width, 'word': list(word), 'overbridge_events': len(S['paths']),
            'closure_events': width, 'anchor_variables_eliminated': k,
            'clock_assignments_checked': clocks_checked,
            'original_grid_vs_homogeneous_pointwise_checks': pointwise,
            'full_alias_free_grid_coefficient_checks': aliases,
            'original_core_period': core, 'original_normalized_period': core*external % p,
            'original_full_source_before_diagonal_restriction_verified': True,
            'all_anchor_aliases_removed_by_nonnegative_degree': True,
            'exact_grouped_graph_phases_and_charged_coefficient_verified': True}


def alias_degree_proof_audit():
    rows = []
    for N in range(2, 8):
        d = N-1
        for k in range(1, 6):
            kept = []
            # Test all possible alias charges, even for single degrees much>N.
            for charges in itertools.product(range(-k, k+1), repeat=k):
                degrees = [d+N*q for q in charges]
                if min(degrees) >= 0 and sum(degrees) == k*d:
                    kept.append(charges)
            assert kept == [(0,)*k]
        rows.append({'N': N, 'arbitrary_high_positive_alias_requires_forbidden_negative_alias': True})
    return rows


def main():
    cases = []
    for N in (2, 3):
        for width, word in [(3, [1, -2, 1, -2]),
                            (3, [1, 2, 1, -2, -1]),
                            (3, [-1, -2, 1, 2]),
                            (4, [1, 2, -1, 3, 2])]:
            cases.append(whole_case(N, width, word, verify_grid=True))
    graph_samples = []
    for N, word, clocks in [(5, [1, -2, 1, -2], (1, 2, 3, 1)),
                             (7, [1, 1, 1, 2, -1, 2], (3, 3, 3, 3, 3, 3))]:
        H = HardyNetwork(N, 1)
        S = setup(H, 3, word)
        G = graph_blocks(H, S, clocks)
        G['word'] = word
        G['scope'] = 'Exact grouped graph metadata; feasible-phase flatness is not asserted.'
        graph_samples.append(G)
    result = {'status': 'PASS', 'whole_original_global_charged_states': cases,
              'global_alias_degree_argument': alias_degree_proof_audit(),
              'exact_grouped_graph_metadata_samples': graph_samples,
              'scope': ('Original complete averaged pivotal scalar, all closure adapters retained. '
                        'Exact charged flow coefficient; no positivity or geometric noncancellation assertion.')}
    Path(__file__).with_name('actual_global_charged_bridge_flow_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS eight whole original signed charged-flow states, signed undertransport/event bijections, '
          'pointwise homogeneous forms and alias-free anchor coefficients')


if __name__ == '__main__':
    main()
