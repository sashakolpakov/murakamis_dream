#!/usr/bin/env python3
"""Exact support-semigroup certificates and positive whole-source partitions.

The all-level limit is proved in the note. Floating point rates are diagnostics.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np

A = ('A',)


def turn(e):
    return ('turn', e)


def product(a, b):
    return ('product', a, b)


EXPRS = [A, turn(A), product(A, A), product(A, turn(A)),
         turn(product(A, A)), product(turn(A), turn(A)),
         product(turn(product(A, A)), A),
         product(turn(product(A, turn(A))), product(A, A))]


def compile_wires(expr):
    nodes = []

    def add(kind, *children):
        nodes.append((kind, children))
        return len(nodes) - 1

    def visit(e):
        if e[0] == 'A':
            i, j, k = (add('h') for _ in range(3))
            return add('product', add('product', i, j), k)
        return add(e[0], *(visit(c) for c in e[1:]))

    root = visit(expr)
    return nodes, root


def witness(nodes, root, d):
    choices = []
    for kind, children in nodes:
        if kind == 'h':
            opts = {r: () for r in range(d // 2 + 1)}
        elif kind == 'turn':
            opts = {d - r: (r,) for r in choices[children[0]]}
        else:
            opts = {}
            for i in choices[children[0]]:
                for j in choices[children[1]]:
                    if i + j <= d:
                        for r in range(max(i, j), i + j + 1):
                            opts.setdefault(r, (i, j))
        choices.append(opts)
    assert set(choices[root]) == set(range(d + 1))
    out = [None] * len(nodes)

    def fill(k, r):
        out[k] = r
        for child, value in zip(nodes[k][1], choices[k][r]):
            fill(child, value)

    fill(root, d)
    verify(nodes, root, d, out)
    return out


def verify(nodes, root, d, labels):
    assert labels[root] == d
    for (kind, children), r in zip(nodes, labels):
        assert isinstance(r, int) and 0 <= r <= d
        if kind == 'h':
            assert 2 * r <= d
        elif kind == 'turn':
            assert r + labels[children[0]] == d
        else:
            i, j = (labels[c] for c in children)
            assert max(i, j) <= r <= i + j <= d


def semigroup_checks():
    sums = residues = 0
    for expr in EXPRS:
        nodes, root = compile_wires(expr)
        ws = {d: witness(nodes, root, d) for d in range(2, 12)}
        for d, e in itertools.product(ws, repeat=2):
            verify(nodes, root, d + e, [a + b for a, b in zip(ws[d], ws[e])])
            sums += 1
        for D in range(2, 9):
            for d in range(2 * D + 2, 5 * D + 5):
                anchor_d = 2 + (d - 2) % D
                k = (d - anchor_d) // D
                labels = [k * a + b for a, b in zip(ws[D], ws[anchor_d])]
                verify(nodes, root, d, labels)
                # Exact numerator bound for distance from the rational witness.
                assert all(abs(D * x - d * y) <= D * anchor_d
                           for x, y in zip(labels, ws[D]))
                residues += 1
    return {'additive_integer_support_checks': sums,
            'all_residue_approximation_checks': residues,
            'expressions': len(EXPRS)}


def positive_level(N):
    d, M = N - 1, (N - 1) // 2
    ls = np.zeros(N)
    for r in range(1, N):
        ls[r] = ls[r - 1] + math.log(2 * math.sin(math.pi * r / N))
    h = np.full(N, -np.inf)
    for v in range(M + 1):
        h[v] = math.log(N) + np.logaddexp.reduce([
            math.log(1 if 2 * j == d else 2) + ls[j + v] - ls[j - v] - 2 * ls[v]
            for j in range(v, M + 1)])
    table = [(i, j, k, ls[i + j] + ls[k] - ls[i] - ls[j]
              - ls[k - i] - ls[k - j] - ls[i + j - k])
             for i in range(N) for j in range(N - i)
             for k in range(max(i, j), i + j + 1)]

    def mul(a, b):
        out = np.full(N, -np.inf)
        for i, j, k, value in table:
            out[k] = np.logaddexp(out[k], a[i] + b[j] + value)
        return out

    cache = {A: mul(mul(h, h), h)}

    def evaluate(e):
        if e not in cache:
            if e[0] == 'turn':
                cache[e] = evaluate(e[1])[::-1]
            else:
                cache[e] = mul(evaluate(e[1]), evaluate(e[2]))
        return cache[e]

    vals = [float(evaluate(e)[d]) for e in EXPRS]
    assert all(math.isfinite(x) for x in vals)
    assert abs(vals[1] - 6 * math.log(N)) < 2e-11
    assert abs(vals[4] - 12 * math.log(N)) < 2e-11
    theta_error = None
    if N <= 16:
        terms = []
        for a, b, c in itertools.product(range(M + 1), repeat=3):
            J = a + b + c
            if J < d:
                continue
            R = math.log(N) + np.logaddexp.reduce([
                ls[t] - ls[d + t - J]
                - sum(ls[t - j] + ls[J - j - t] for j in (a, b, c))
                for t in range(max(a, b, c, J - d), min(a + b, a + c, b + c, d) + 1)])
            terms.append(2 * math.log(N) + sum(math.log(1 if 2 * j == d else 2)
                         + ls[J - 2 * j] for j in (a, b, c)) - ls[J - d] + 2 * R)
        theta_error = abs(float(np.logaddexp.reduce(terms)) - vals[0])
        assert theta_error < 3e-10
    return {'N': N, 'full_positive_expression_log_values': vals,
            'independent_whole_theta_log_error': theta_error,
            'constant_closure_N6_and_N12': True,
            'volume_scaled_rates_diagnostic_only': [2 * math.pi * x / N for x in vals]}


if __name__ == '__main__':
    result = {'status': 'PASS', 'support': semigroup_checks(),
              'positive_partitions': [positive_level(N) for N in [3, 4, 5, 6, 7, 8, 12, 16, 24, 33]],
              'scope': 'Exact integer support and residue certificates; positive DP and theta comparison use floating point. The all-level variational theorem follows from uniform factorial bounds and the written semigroup proof. Actual manifold-volume identification remains separate.'}
    Path(__file__).with_name('actual_positive_conway_variational_limit_results.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print('PASS', result['support'], '/10 positive partition levels; theta calibration and zero-rate turned closures')
