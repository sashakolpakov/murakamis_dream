#!/usr/bin/env python3
"""Exact nine-atom/actual-crossing regulator calibration and wall-mark identity."""

from collections import defaultdict
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


A, B, z, w = sp.symbols('A B z w', nonzero=True)
VARIABLES = (A, B, z, w)


def rational(q):
    return sp.factor(q)


def atom_graph(sign):
    a, b, p, r = A, B, z, w
    atoms = []
    def diagonal(head, epsilon):
        nonlocal a, b, p, r
        clock = (a, b)[head]
        atoms.append((epsilon, rational(1-clock)))
        if head == 0:
            p = rational(p*(1-clock)**(-epsilon))
        else:
            r = rational(r*(1-clock)**(-epsilon))
    def transfer(plus, epsilon):
        nonlocal a, b, p, r
        argument = rational(-p/r if plus else -r/p)
        atoms.append((epsilon, argument))
        if plus:
            a, b = rational(a*(1-argument)**(-epsilon)), rational(b*(1-argument)**epsilon)
        else:
            a, b = rational(a*(1-argument)**epsilon), rational(b*(1-argument)**(-epsilon))
    diagonal(1, -1)
    transfer(False, 1)
    diagonal(0, -1)
    diagonal(1, 1)
    if sign > 0:
        transfer(True, -1)
        r = rational(-r/b)
    else:
        r = rational(-b*r)
        transfer(True, 1)
    diagonal(1, -1)
    diagonal(0, 1)
    transfer(False, -1)
    diagonal(1, 1)
    assert len(atoms) == 9
    return atoms, (a, b, p, r)


def physical(data):
    a, b, p, r = data
    return tuple(map(rational, (-1/a, (1/a-1)/p, (1-a)*p,
                                -1/b, (1/b-1)/r, (1-b)*r)))


def actual_crossing(sign):
    k, e, f, l, g, h = physical(VARIABLES)
    if sign > 0:
        c = rational(1/(1-e*h))
        d = 1-e*h
        output = (l*d, (d*g+e*(d*l-1/l))/k, k*h/d,
                  k/d, e/(l*d), l*(d*f+h*(d/k-k)))
        five = [(1, B), (1, c), (1, 1/A), (-1, B*c), (-1, c/A)]
    else:
        c = rational(1-(B/A)*g*f)
        output = (l*c, k*g, f+h/k-f/(l*l*c),
                  k/c, l*e+g-k*k*g/c, f/l)
        five = [(1, A), (1, c), (1, 1/B), (-1, A*c), (-1, c/B)]
    return tuple(map(rational, output)), five


def multiplicative_vector(value):
    result = defaultdict(int)
    for polynomial, sign in zip(sp.fraction(rational(value)), [1, -1]):
        constant, factors = sp.factor_list(polynomial, *VARIABLES)
        # Rational constants are retained; only their torsion sign disappears.
        for prime, power in sp.factorint(abs(sp.numer(constant))).items():
            result['constant:'+str(prime)] += sign*power
        for prime, power in sp.factorint(abs(sp.denom(constant))).items():
            result['constant:'+str(prime)] -= sign*power
        for factor, power in factors:
            result[str(factor)] += sign*power
    return {key: exponent for key, exponent in result.items() if exponent}


def bloch_boundary(atoms):
    result = defaultdict(int)
    for epsilon, argument in atoms:
        left, right = multiplicative_vector(argument), multiplicative_vector(1-argument)
        for a, av in left.items():
            for b, bv in right.items():
                if a != b:
                    result[tuple(sorted((a, b)))] += epsilon*av*bv*(1 if a < b else -1)
    return {key: value for key, value in result.items() if value}


def D(value):
    return mp.im(mp.polylog(2, value))+mp.log(abs(value))*mp.arg(1-value)


def regulator_checks(atoms, five):
    functions = [(epsilon, sp.lambdify(VARIABLES, value, 'mpmath')) for epsilon, value in atoms]
    target = [(epsilon, sp.lambdify(VARIABLES, value, 'mpmath')) for epsilon, value in five]
    points = [(mp.mpc('.4', '.3'), mp.mpc('.7', '-.2'), mp.mpc('1.2', '.1'), mp.mpc('.3', '.8')),
              (mp.mpc('-.7', '.2'), mp.mpc('1.3', '.4'), mp.mpc('.8', '-.2'), mp.mpc('-.4', '.9')),
              (mp.mpf('2'), mp.mpf('3'), mp.mpf('5'), mp.mpf('7'))]
    rows = []
    for point in points:
        lhs = mp.fsum(epsilon*D(fun(*point)) for epsilon, fun in functions)
        rhs = mp.fsum(epsilon*D(fun(*point)) for epsilon, fun in target)
        assert abs(lhs-rhs) < mp.mpf('1e-43')
        if all(not mp.im(v) for v in point):
            assert abs(lhs)+abs(rhs) < mp.mpf('1e-43')
        rows.append({'nine_atom_regulator': str(lhs), 'actual_five_term_regulator': str(rhs),
                     'difference': float(abs(lhs-rhs))})
    return rows


def real_quadratic_identity():
    rows = []
    X = [mp.mpc('.3', '.4'), mp.mpc('-.2', '.7'), mp.mpc('.6', '-.5')]
    shape_rows = [[1, 0, -1], [0, 1, 1], [1, -1, 0], [0, 0, 1]]
    epsilon = [1, -1, 1, 1]
    nu = [0, 1, 0, 1]
    C = mp.matrix([[mp.mpf('.4'), mp.mpf('-.2'), 0],
                   [mp.mpf('-.2'), mp.mpf('.7'), mp.mpf('.3')],
                   [0, mp.mpf('.3'), mp.mpf('-.8')]])
    xx = mp.matrix(X)
    for marks in [[0, 0, 0], [1, -2, 1], [3, 4, -1]]:
        kappa = mp.matrix([mp.pi*(j+mp.mpf(1)/3)+2*mp.pi*marks[j] for j in range(3)])
        shapes = [mp.exp(sum(a*x for a, x in zip(row, X))+1j*mp.pi*v)
                  for row, v in zip(shape_rows, nu)]
        value = mp.fsum(e*mp.polylog(2, a) for e, a in zip(epsilon, shapes))
        value += (xx.T*C*xx)[0]/2+1j*(kappa.T*xx)[0]
        gradient = C*xx+1j*kappa
        for j in range(3):
            gradient[j] -= mp.fsum(e*row[j]*mp.log(1-a)
                                    for e, row, a in zip(epsilon, shape_rows, shapes))
        bloch = mp.fsum(e*D(a) for e, a in zip(epsilon, shapes))
        residual = mp.fsum(mp.re(X[j])*mp.im(gradient[j]) for j in range(3))
        assert abs(mp.im(value)-bloch-residual) < mp.mpf('1e-43')
        rows.append({'integer_wall_marks': marks, 'identity_residual': float(abs(mp.im(value)-bloch-residual))})
    return rows


def main():
    mp.mp.dps = 60
    rows = []
    for sign in [1, -1]:
        nine, output = atom_graph(sign)
        actual, five = actual_crossing(sign)
        assert all(rational(a-b) == 0 for a, b in zip(physical(output), actual))
        difference = bloch_boundary(nine+[(-epsilon, value) for epsilon, value in five])
        assert not difference
        rows.append({'crossing_sign': sign, 'all_six_actual_Gauss_coordinates_equal': True,
                     'rational_function_field_Bloch_wedge_difference': {},
                     'nine_rational_shapes': [[epsilon, str(value)] for epsilon, value in nine],
                     'regulator_checks': regulator_checks(nine, five)})
    output = {'status': 'PASS', 'actual_crossing_calibration': rows,
              'real_quadratic_wall_mark_identity': real_quadratic_identity(),
              'scope': 'All regular full interior critical actions equal the actual representation regulator after the recorded fundamental-cycle comparison. No singular/endpoint bound or global selected coefficient.'}
    Path(__file__).with_name('actual_wall_critical_regulator_results.json').write_text(json.dumps(output, indent=2)+'\n')
    print('PASS both actual nine-atom crossing maps, exact rational Bloch wedge equalities, '
          'six regulator checks and three integer-wall off-critical identities')


if __name__ == '__main__':
    main()
