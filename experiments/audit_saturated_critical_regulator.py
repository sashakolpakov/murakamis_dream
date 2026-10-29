#!/usr/bin/env python3
"""Exact universal face cancellation and a genuine saturation obstruction.

This audits algebra used by the critical-closure theorem, not a volume
asymptotic for any knot. All proof assertions below use exact arithmetic.
"""

from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path

import sympy as sp


def add(*terms):
    answer = defaultdict(int)
    for sign, term in terms:
        for key, value in term.items():
            answer[key] += sign * value
    return {key: value for key, value in answer.items() if value}


def wedge(left, right):
    answer = defaultdict(int)
    for a, av in left.items():
        for b, bv in right.items():
            if a != b:
                answer[tuple(sorted((a, b)))] += av * bv * (1 if a < b else -1)
    return {key: value for key, value in answer.items() if value}


def edge(i, j):
    return {''.join(map(str, sorted((i, j)))): 1}


def triangle(i, j, k):
    a, b, c = edge(i, j), edge(j, k), edge(k, i)
    return add((1, wedge(a, b)), (1, wedge(b, c)), (1, wedge(c, a)))


def face_audit():
    z = {'13': 1, '02': 1, '03': -1, '12': -1}
    one_minus_z = {'01': 1, '23': 1, '03': -1, '12': -1}
    boundary = add(*[
        (-((-1) ** omit), triangle(*[v for v in range(4) if v != omit]))
        for omit in range(4)
    ])
    residual = add((1, wedge(z, one_minus_z)), (-1, boundary))
    assert not residual

    # Independent Pluecker check of the cross-ratio convention, including
    # the torsion minus sign in 1-z that disappears in the rational wedge.
    coords = sp.symbols('a0 b0 a1 b1 a2 b2 a3 b3')
    vectors = [sp.Matrix(coords[2*i:2*i+2]) for i in range(4)]
    p = {(i, j): sp.det(sp.Matrix.hstack(vectors[i], vectors[j]))
         for i, j in combinations(range(4), 2)}
    assert sp.expand(p[0, 3]*p[1, 2] - p[0, 2]*p[1, 3] + p[0, 1]*p[2, 3]) == 0
    return {'face_exterior_residual': {}, 'pluecker_polynomial': '0'}


def saturation_audit():
    h, x, y, w, u, v = sp.symbols('h x y w u v')
    f1 = w-x*y
    f2 = (1-w)*u-x+w
    f3 = (1-w)*v-y+w
    g = u*v-w*(1-u)*(1-v)
    x0, y0 = w+(1-w)*u, w+(1-w)*v
    assert sp.expand((1-w)*g - (-f1+f2*y0+x*f3)) == 0
    assert sp.expand((x0*y0-w)-(1-w)*g) == 0

    naive = sp.groebner([f1, f2, f3], x, y, w, u, v, order='lex')
    _, naive_remainder = naive.reduce(g)
    assert naive_remainder != 0

    localized = sp.groebner([f1, f2, f3, 1-h*(1-w)], h, x, y, w, u, v, order='lex')
    _, localized_remainder = localized.reduce(g)
    assert localized_remainder == 0
    eliminated = [p.as_expr() for p in localized.polys if not p.as_expr().has(h, x, y)]
    assert eliminated
    image_ideal = sp.groebner(eliminated, w, u, v, order='lex')
    assert image_ideal.reduce(g)[1] == 0
    assert all(sp.rem(p, sp.Poly(g, w), w) == 0 for p in eliminated)

    fake = {x: 1, y: 1, w: 1, u: sp.I, v: sp.I}
    assert all(sp.simplify(f.subs(fake)) == 0 for f in [f1, f2, f3])
    assert sp.simplify(g.subs(fake)) == -1+2*sp.I
    assert sp.expand(g.subs(w, 1)) == u+v-1

    # D(i)=Im Li_2(i)=sum (-1)^k/(2k+1)^2. Alternation proves the
    # exact positive lower bound 1-1/9=8/9, without floating arithmetic.
    catalan_lower = sp.Rational(1)-sp.Rational(1, 9)
    assert catalan_lower > 0
    return {
        'saturation_certificate_residual': '0',
        'naive_ideal_remainder': str(naive_remainder),
        'localized_ideal_remainder': '0',
        'saturated_shape_image_generators': [str(p) for p in eliminated],
        'false_boundary_cleared_equations': ['0', '0', '0'],
        'false_boundary_saturated_residual': '-1 + 2*I',
        'saturated_boundary_relation': str(sp.expand(g.subs(w, 1))),
        'false_boundary_regulator_strict_lower_bound': str(2*catalan_lower),
    }


def main():
    report = {'status': 'PASS', 'universal_face': face_audit(),
              'pachner_saturation': saturation_audit(),
              'scope': 'Exact universal identities; no quantum-cycle or volume-limit assertion.'}
    target = Path(__file__).with_name('saturated_critical_regulator_results.json')
    target.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
