#!/usr/bin/env python3
"""Exact odd edge words and literal knot-parity compiler.

Uses cyclic physical ports and independently follows stack/closure wires.
The complete metric itself is the previously audited Conway polyhedron.
"""
import json
from pathlib import Path

import sympy as sp

from audit_actual_conway_bowtie_projection_cut import expression_cases
from audit_actual_conway_marked_peripheral_deformation import (
    white, equal_projectively, at,
)


def matrices():
    E = sp.symbols('E', nonzero=True)
    R = (1+E)**2/(4*E)
    ws = white(E, R)
    cross = sp.Matrix([[R, -R], [1, E*R-1-E]])
    other = cross.subs(E, 1/E).adjugate()
    zeta = (1+E)/2
    assert sp.cancel(at(cross, zeta)-zeta/E) == 0
    assert sp.cancel(at(cross, None)-R) == 0
    assert sp.cancel(at(cross, 1)) == 0
    for i, j in [(0, 2), (2, 0), (1, 3)]:
        word = ws[i].adjugate()*other*ws[j].adjugate()*cross
        assert equal_projectively(word, sp.eye(2))
    b0 = sp.Matrix([[-1, E+1], [0, E]])
    b2 = sp.Matrix([[-1, -E-1], [0, E]])
    t0 = sp.Matrix([[-1, E-1], [0, E]])
    t1 = sp.Matrix([[-1, 1-E], [0, E]])
    for matrix, shift in [(b2.adjugate()*b0, -2*(E+1)),
                          (b0.adjugate()*t0, 2),
                          (b0.adjugate()*t1, 2*E)]:
        assert equal_projectively(matrix, sp.Matrix([[1, shift], [0, 1]]))
    lam, mu0, mup, mum = -2*(E+1), E-1, -2, 2*E
    assert sp.expand(mup-mum-lam) == 0
    assert sp.expand(mup-mu0-lam/2) == 0
    assert sp.expand(mum-mu0+lam/2) == 0
    assert sp.cancel(lam/mup-(1+E)) == 0
    assert sp.cancel(lam/mum+1+1/E) == 0
    # Directed area Im(conjugate(mu)*lambda), with E on the unit circle.
    def bar(v): return sp.sympify(v).subs(E, 1/E)
    def area(mu): return sp.cancel((bar(mu)*lam-mu*bar(lam))/(2*sp.I))
    assert sp.cancel(area(mup)-area(mu0)) == 0
    assert sp.cancel(area(mum)-area(mu0)) == 0
    return {'generic_odd_edge_words': 3,
            'original_chart_white_shaded_paths': 3,
            'primitive_two_rectangle_area_and_both_markings': 'PASS'}


PAIR = {'I': ((0, 3), (1, 2)), 'U': ((0, 1), (2, 3)),
        'X': ((0, 2), (1, 3))}


def canonical(pairs):
    return tuple(sorted(tuple(sorted(p)) for p in pairs))


NAME = {canonical(p): name for name, p in PAIR.items()}


def turn(name):
    return NAME[canonical([((a-1) % 4, (b-1) % 4) for a, b in PAIR[name]])]


def stack(a, b):
    parent = list(range(8))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def join(x, y): parent[find(x)] = find(y)
    for x, y in PAIR[a]: join(x, y)
    for x, y in PAIR[b]: join(x+4, y+4)
    join(2, 5); join(3, 4)
    exposed = [0, 1, 6, 7]
    groups = {}
    for x in range(8): groups.setdefault(find(x), []).append(x)
    loops = sum(not any(x in exposed for x in group) for group in groups.values())
    pairs = [tuple(exposed.index(x) for x in group if x in exposed)
             for group in groups.values() if any(x in exposed for x in group)]
    return NAME[canonical(pairs)], loops


def close(name):
    graph = {i: [] for i in range(4)}
    for a, b in PAIR[name]+PAIR['I']:
        graph[a].append(b); graph[b].append(a)
    seen, count = set(), 0
    for a in range(4):
        if a in seen: continue
        count += 1; todo = [a]
        while todo:
            v = todo.pop()
            if v in seen: continue
            seen.add(v); todo.extend(graph[v])
    return count


def compile_actual(e, pattern):
    if e[0] == 'A':
        names = ['X' if next(pattern) else 'U' for _ in range(3)]
        first, n1 = stack(names[0], names[1])
        last, n2 = stack(first, names[2])
        return last, n1+n2
    if e[0] == 'turn':
        name, loops = compile_actual(e[1], pattern)
        return turn(name), loops
    a, n1 = compile_actual(e[1], pattern)
    b, n2 = compile_actual(e[2], pattern)
    result, n3 = stack(a, b)
    return result, n1+n2+n3


def witnesses(e):
    if e[0] == 'A': return {'X': [1, 1, 1], 'U': [0, 1, 1]}
    if e[0] == 'turn': return {turn(k): p for k, p in witnesses(e[1]).items()}
    result = {}
    for a, pa in witnesses(e[1]).items():
        for b, pb in witnesses(e[2]).items():
            name, loops = stack(a, b)
            if loops == 0: result.setdefault(name, pa+pb)
    assert len(result) >= 2
    return result


def connectivity():
    assert [close(n) for n in ['I', 'U', 'X']] == [2, 1, 1]
    for a in PAIR:
        for b in PAIR:
            _, loops = stack(a, b)
            assert loops == int(a == b == 'U')
    subsets = [('I', 'U'), ('I', 'X'), ('U', 'X')]
    for left in subsets:
        for right in subsets:
            outcomes = {stack(a, b)[0] for a in left for b in right
                        if stack(a, b)[1] == 0}
            assert len(outcomes) >= 2
    rows = []
    for e in expression_cases():
        choices = witnesses(e)
        for name, pattern in choices.items():
            assert compile_actual(e, iter(pattern)) == (name, 0)
        chosen = next(name for name in ['U', 'X'] if name in choices)
        pattern = choices[chosen]
        assert close(chosen) == 1
        # Every signed even full twist leaves each leaf's parity fixed.
        for shift in range(7):
            powers = [(-1 if (i+shift) % 2 else 1)*(i+shift+1)
                      for i in range(len(pattern))]
            filled = [(epsilon-2*p) % 2 for epsilon, p in zip(pattern, powers)]
            assert filled == pattern
            assert compile_actual(e, iter(filled)) == (chosen, 0)
        rows.append({'leaves': len(pattern), 'feasible_no_loop_types': sorted(choices),
                     'chosen_type': chosen, 'odd_pattern': pattern,
                     'filled_main_components': 1})
    return {'set_product_cases': 9, 'expressions': len(rows),
            'signed_full_twist_checks': 7*len(rows), 'witnesses': rows}


if __name__ == '__main__':
    result = {'status': 'PASS', 'geometry': matrices(),
              'literal_connectivity': connectivity()}
    Path(__file__).with_name('actual_conway_half_twist_partner_geometry_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS: 3 generic odd edge words; primitive cusp markings; '
          f"{result['literal_connectivity']['expressions']} knot patterns / "
          f"{result['literal_connectivity']['signed_full_twist_checks']} signed fillings")
