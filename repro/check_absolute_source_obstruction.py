#!/usr/bin/env python3
"""Check finite algebra and exact load rounding used by the cancellation note.

Finite fields test the actual face operator, not asymptotic rates. Rational
tables test the original incidence constraints. The all-level lower bound
and its entropy limit are written proofs in the linked research note.
"""

import argparse
from collections import Counter, deque
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from check_local_face_fourier import (
    chebyshev_annihilator, evaluate, face_matrix, fields, scale,
)

ROOT = Path(__file__).resolve().parents[1]


def quotient_at(coefficients, sigma, p):
    """(chi(X)-chi(sigma))/(X-sigma), with no spectral division."""
    out = [0] * (len(coefficients) - 1)
    out[-1] = coefficients[-1]
    for j in range(len(out) - 2, -1, -1):
        out[j] = (coefficients[j + 1] + sigma * out[j + 1]) % p
    return out


def cofactor(N, q, p, x, y, m):
    """The separate cleared-cofactor recurrence at spectrum -2."""
    a = [(2 + pow(q, 2*j+1, p) + pow(q, -2*j-1, p)) % p
         for j in range(N)]
    rows, prefix = [[1]], 1
    for j in range(1, m + 1):
        prefix = prefix * a[j-1] % p
        out = [0] * (j + 1)
        out[j] = prefix
        s2 = (2 - pow(q, 2*j, p) - pow(q, -2*j, p)) % p
        pair = -(pow(q, j, p) - pow(q, -j, p)) * (
            pow(q, j-1, p) - pow(q, 1-j, p)) % p
        for i, v in enumerate(rows[-1]):
            out[i] = (out[i] + s2 * (x+y) * v) % p
        if j >= 2:
            for i, v in enumerate(rows[-2]):
                out[i] = (out[i] + pair*a[j-1]*x*y*v) % p
        rows.append(out)
    return rows[-1]


def algebra():
    cap_entries = odd_entries = 0
    cases = []
    for N in range(3, 16):
        m, d = N // 2, N - 1
        for p, q in fields(N):
            chi = chebyshev_annihilator(N, p)
            # Matrix evaluation of the original face operator supplies H_V.
            T = face_matrix(N, q, p, 1, 0)
            V = evaluate(quotient_at(chi, 2, p), scale(T, -1, p), p)
            numerator, denominator = 1, 1
            for j in range(m):
                if j:
                    numerator = numerator * (
                        2-pow(q, 2*j, p)-pow(q, -2*j, p)) % p
                denominator = denominator * (
                    2-pow(q, 2*j+1, p)-pow(q, -2*j-1, p)) % p
                assert denominator != 0
                U = 4 * numerator * pow(denominator, -1, p) % p
                assert V[0][j] == (-1)**j * U % p
                cap_entries += 1
            if N % 2:
                for x, y in [(1, 1), (2, 3), (1, 0), (0, 1)]:
                    T = face_matrix(N, q, p, x, y)
                    V = evaluate(quotient_at(chi, -2, p), scale(T, -1, p), p)
                    G = cofactor(N, q, p, x, y, m)
                    for i in range(N):
                        for h in range(N):
                            expected = G[i]*G[h] % p if i <= m and h <= m else 0
                            assert V[i][d-h] == expected
                            odd_entries += 1
            cases.append({'N': N, 'prime': p})
    return {'cases': cases, 'protected_cap_entries': cap_entries,
            'odd_central_entries': odd_entries}


def integer_round(rows, faces, table):
    """Floor/ceiling cycle rounding; both integer margin sets stay fixed."""
    rounded = {key: F(value.numerator // value.denominator)
               for key, value in table.items()}
    fraction = {key: table[key] - value for key, value in rounded.items()}
    cycles = 0
    while True:
        graph = {}
        for key, value in fraction.items():
            if 0 < value < 1:
                row, face = key
                a, b = ('r', row), ('f', face)
                graph.setdefault(a, []).append((b, key))
                graph.setdefault(b, []).append((a, key))
        if not graph:
            break
        parent, edge_to, found = {}, {}, None

        def visit(v, previous):
            nonlocal found
            for w, edge in graph[v]:
                if w == previous:
                    continue
                if w not in parent:
                    parent[w], edge_to[w] = v, edge
                    if visit(w, v):
                        return True
                else:
                    # In undirected depth-first search the first back edge
                    # joins the current vertex to an ancestor.
                    cycle, z = [edge], v
                    while z != w:
                        cycle.append(edge_to[z])
                        z = parent[z]
                    found = cycle
                    return True
            return False

        for start in graph:
            if start not in parent:
                parent[start] = None
                if visit(start, None):
                    break
        assert found is not None and len(found) % 2 == 0
        step = min(1-fraction[e] if k % 2 == 0 else fraction[e]
                   for k, e in enumerate(found))
        assert step > 0
        for k, edge in enumerate(found):
            fraction[edge] += step if k % 2 == 0 else -step
            assert 0 <= fraction[edge] <= 1
        cycles += 1
    result = {key: int(rounded[key]+fraction[key]) for key in table}
    for row in rows:
        assert sum(result[row, f] for f in rows[row]) == sum(table[row, f] for f in rows[row])
    for face in faces:
        assert sum(value for (row, f), value in result.items() if f == face) == sum(
            value for (row, f), value in table.items() if f == face)
    assert all(abs(result[key]-table[key]) < 1 for key in table)
    return result, cycles


def loads():
    data = json.loads((ROOT/'experiments/actual_singleton_sector_obstruction_certificate.json').read_text())
    ports, anchor = data['source']['ports'], data['anchor']
    protected, ordinary = set(data['source']['protected']), data['ordinary']
    x, b, z, y = ports[anchor]
    assert {b, y} == protected and x not in protected and z not in protected
    values = [F(*v['value']) for v in data['variables']]
    lam = values[data['lambda_variable']]
    source_rows = [r for r in data['rows'] if r['crossing'] != anchor]
    rows = {i: r['faces'] for i, r in enumerate(source_rows)}
    alpha = {(i, f): values[k] for i, r in enumerate(source_rows)
             for f, k in zip(r['faces'], r['variables'])}
    assert min(alpha.values()) > 0 and 0 < lam < 1
    for i in rows:
        assert sum(alpha[i, f] for f in rows[i]) == F(1, 2)
    for f in ordinary:
        assert sum(v for (i, g), v in alpha.items() if g == f) + (
            lam/2 if f == x else 1-lam/2 if f == z else 0) == 1
    graph = {f: [] for f in ordinary}
    for i, fs in rows.items():
        for f in fs:
            graph[f].extend((g, i) for g in fs if g != f)
    parent, order, queue = {ordinary[0]: None}, [], deque([ordinary[0]])
    while queue:
        f = queue.popleft(); order.append(f)
        for g, row in graph[f]:
            if g not in parent:
                parent[g] = (f, row); queue.append(g)
    assert set(parent) == set(ordinary)
    selected = {e: next(f for f in (port[0], port[3]) if f not in protected)
                for e, port in enumerate(ports) if e != anchor}
    outputs = []
    for N in [20000000, 20000001, 20000002, 20000003]:
        d, m = N-1, N//2
        degree = m if N % 2 else m-1
        j = (degree*lam).numerator // (degree*lam).denominator
        assert 0 <= j < m
        outer = Counter(selected.values()) if N % 2 == 0 else Counter()
        target = {f: F(d-outer[f]-(j if f == x else d-j if f == z else 0))
                  for f in ordinary}
        table = {key: 2*degree*v for key, v in alpha.items()}
        delta = {f: target[f]-sum(v for (i, g), v in table.items() if g == f)
                 for f in ordinary}
        eps = degree*lam-j
        if N % 2:
            assert delta == {f: eps if f == x else -eps if f == z else 0 for f in ordinary}
        assert sum(delta.values()) == 0
        for f in reversed(order[1:]):
            g, row = parent[f]
            table[row, f] += delta[f]
            table[row, g] -= delta[f]
            delta[g] += delta[f]
        assert min(table.values()) >= 0
        integers, cycles = integer_round(rows, ordinary, table)
        for f in ordinary:
            assert sum(v for (i, g), v in integers.items() if g == f) == target[f]
        outputs.append({'N': N, 'triangle_degree': degree, 'anchor_outer_degree': j,
                        'rounded_corners': len(integers), 'rounding_cycles': cycles})
    return outputs


def main():
    if not __debug__:
        raise SystemExit('Assertions are required; do not run with -O.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'repro/results/absolute-source-obstruction.json')
    args = parser.parse_args()
    result = {'scope': __doc__, 'finite_algebra': algebra(), 'rational_rounding': loads()}
    sources = ['repro/check_absolute_source_obstruction.py', 'repro/check_local_face_fourier.py',
               'experiments/actual_singleton_sector_obstruction_certificate.json',
               'notes/research_absolute_source_cancellation_obstruction.md']
    result['source_sha256'] = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                              for name in sources}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'protected_cap_entries': result['finite_algebra']['protected_cap_entries'],
                      'odd_central_entries': result['finite_algebra']['odd_central_entries'],
                      'rounded_tables': len(result['rational_rounding']), 'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
