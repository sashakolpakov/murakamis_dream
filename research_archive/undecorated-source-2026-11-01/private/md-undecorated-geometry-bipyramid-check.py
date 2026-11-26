#!/usr/bin/env python3
"""Finite checks accompanying the symbolic all-m proof.

These check the generic local curvature identities and literal finite
incidences. They do not replace the proof for every m or establish an
asymptotic statement for the original invariant.
"""
import json
from pathlib import Path
from fractions import Fraction
import sympy as sp

t = sp.symbols('t', positive=True, real=True)
c = (1-t*t)/(1+t*t)
s = 2*t/(1+t*t)
a = 1/s
z = c+sp.I*s

def norm2(w):
    return sp.expand(w*sp.conjugate(w))

def curvature(center, radius, p):
    return sp.cancel((norm2(center-p)-radius*radius)/radius)

checks = []
def exact(name, lhs, rhs=0):
    difference = sp.factor(sp.cancel(lhs-rhs))
    assert difference == 0, (name, difference)
    checks.append(name)

for sign, label in [(-1, 'north'), (1, 'south')]:
    p = a+sign
    for j in [-1, 0, 1, 2]:
        sinj = (z**j-z**(-j))/(2*sp.I)
        exact(f'{label}: rim {j}', curvature(a*z**(2*j), 1, p),
              4*a*(a+sign)*sinj*sinj)
    exact(f'{label}: ratio', curvature(a*z**4, 1, p),
          4*c*c*curvature(a*z**2, 1, p))
exact('north apex at north mark', curvature(0, a-1, a-1))
exact('south apex at south mark', -curvature(0, a+1, a+1))
exact('south normalized at north mark',
      -curvature(0, a+1, a-1)/curvature(a*z**2, 1, a-1), 1/c**2)

p = a*c*z
exact('equator north apex', curvature(0, a-1, p), 2)
exact('equator south apex', -curvature(0, a+1, p), 2)
for j in [-1, 0, 1, 2]:
    expected = 0 if j in [0, 1] else 8*c*c
    exact(f'equator rim {j}', curvature(a*z**(2*j), 1, p), expected)

incidence_cases = 0
marks_checked = 0
for m in range(6, 52, 2):
    rim = [f'v{j}' for j in range(m)]
    for alpha in [0, 1]:
        for beta in [0, 1]:
            matched = {}
            for apex, parity in [('N', alpha), ('S', beta)]:
                used = []
                for j in range(m):
                    if j % 2 == parity:
                        used.extend([(j-1) % m, j])
                        if apex == 'N':
                            q = (apex, rim[(j-1) % m], rim[(j+1) % m], rim[j])
                        else:
                            q = (apex, rim[(j+1) % m], rim[(j-1) % m], rim[j])
                        matched[(apex, j)] = q
                assert sorted(used) == list(range(m))
            assert len(matched) == m
            incidence_cases += 1
            for apex, parity in [('N', alpha), ('S', beta)]:
                for j in range(m):
                    if j % 2 != parity:
                        q = matched[(apex, (j+1) % m)]
                        protected = {apex, rim[j]}
                        assert len(protected & {q[0], q[3]}) == 1
                        assert len(protected & {q[1], q[2]}) == 1
                        marks_checked += 1
            for j in range(m):
                k = j if j % 2 == alpha else (j+1) % m
                q = matched[('N', k)]
                protected = {rim[j], rim[(j+1) % m]}
                assert len(protected & {q[0], q[3]}) == 1
                assert len(protected & {q[1], q[2]}) == 1
                marks_checked += 1

assert Fraction(1, 2)-Fraction(2, 5) == Fraction(1, 10)
sqrt3 = sp.sqrt(3)
figure_p = sp.Rational(3, 2)+sp.I*sqrt3/2
figure_alpha = sqrt3+sp.I
figure_checks = []
for name, center, radius, expected_center, expected_radius in [
    ('N', 0, 1, -sqrt3+sp.I, 1),
    ('S', 0, 3, 1/sqrt3+sp.I, 1),
    ('v2', -1+sp.I*sqrt3, 1, -1/sqrt3+sp.I/3, sp.Rational(1, 3)),
    ('v5', 1-sp.I*sqrt3, 1, -1/sqrt3+5*sp.I/3, sp.Rational(1, 3)),
    ('v3', -2, 1, -1/sqrt3+5*sp.I/6, sp.Rational(1, 6)),
    ('v4', -1-sp.I*sqrt3, 1, -1/sqrt3+7*sp.I/6, sp.Rational(1, 6)),
]:
    denominator = sp.simplify(norm2(center-figure_p)-radius*radius)
    image_center = sp.simplify(sp.I+figure_alpha*sp.conjugate(center-figure_p)/denominator)
    image_radius = sp.simplify(2*radius/sp.Abs(denominator))
    assert sp.simplify(image_center-expected_center) == 0, name
    assert sp.simplify(image_radius-expected_radius) == 0, name
    figure_checks.extend([name+': center', name+': radius'])
X, Y = sp.symbols('X Y', real=True)
w = X+sp.I*Y
for name, center, height in [('v0', 2, 2), ('v1', 1+sp.I*sqrt3, 0)]:
    equation = sp.simplify(norm2(figure_alpha+(figure_p-center)*(w-sp.I))-norm2(w-sp.I))
    assert sp.simplify(equation.subs(Y, height)) == 0
    assert sp.diff(equation, X) == 0
    assert sp.diff(equation, Y) != 0
    figure_checks.append(name+': line')
report = {
    'symbolic_curvature_identities': len(checks),
    'identity_names': checks,
    'tested_even_sizes': list(range(6, 52, 2)),
    'matching_offset_cases': incidence_cases,
    'permissible_marks_checked': marks_checked,
    'rational_negative_margin': str(Fraction(1, 10)),
    'figure_coordinate_identities': len(figure_checks),
    'figure_coordinate_names': figure_checks,
    'scope': 'Generic local identities and finite incidences; the all-size proof is separate.'
}
output = Path('/private/tmp/md-undecorated-geometry-bipyramid-check-results.json')
output.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
