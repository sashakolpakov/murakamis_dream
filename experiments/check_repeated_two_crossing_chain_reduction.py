#!/usr/bin/env python3
"""Check exact quantum and marked affine reductions of same-sign 2-chains.

The affine checks use the integer parameter k=4r+j, rather than
extrapolating a finite list of lengths. Matrix comparisons supplement
the written all-level quantum proof. No asymptotic estimate is tested.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from check_twist_period_insertion import original_matrices


def affine_checks():
    r = sp.symbols('r', integer=True, nonnegative=True)
    turn = sp.Matrix([[0, -1, 0], [1, 0, sp.Rational(1, 2)], [0, 0, 1]])

    def crossing(n):
        return sp.Matrix([[1, n, n/2], [0, 1, 0], [0, 0, 1]])

    def power(k, sigma, parity):
        if sigma == 1:
            return sp.Matrix([
                [1-k, -k, -sp.Rational(3, 4)*k*(k-1)],
                [k, 1+k, sp.Rational(3, 4)*k*(k+1)], [0, 0, 1]])
        return sp.Matrix([
            [parity*(1-k), parity*k, ((2*k-1)*parity+1)/8],
            [-parity*k, parity*(1+k), ((2*k+1)*parity-1)/8],
            [0, 0, 1]])

    def zero_matrix(matrix):
        if any(sp.simplify(x) != 0 for x in matrix):
            raise AssertionError(matrix)

    def integer_polynomial(expr):
        poly = sp.Poly(sp.expand(expr), r)
        if not all(coefficient.is_Integer for coefficient in poly.all_coeffs()):
            raise AssertionError((expr, poly.all_coeffs()))
        return str(poly.as_expr())

    rows = []
    expected = [(1, 1), (1, 0), (0, 0), (0, 1)]
    for sigma in (-1, 1):
        sigma = sp.Integer(sigma)
        step = turn*crossing(2*sigma)
        zero_matrix(power(sp.Integer(0), sigma, sp.Integer(1))-sp.eye(3))
        for residue in range(4):
            k = 4*r+residue
            parity = sp.Integer((-1)**residue)
            current = power(k, sigma, parity)
            # The closed form is proved by its initial value and this recurrence.
            zero_matrix(power(k+1, sigma, -parity)-current*step)
            target = crossing(-sigma)*turn*crossing(-sigma*(k+1))*turn*crossing(-sigma)
            relative = sp.simplify(target.inv()*current*turn)
            sign = sp.simplify(relative[0, 0])
            if sign not in (sp.Integer(1), sp.Integer(-1)):
                raise AssertionError(sign)
            zero_matrix(relative[:2, :2]-sign*sp.eye(2))
            coordinates = []
            for axis in range(2):
                delta = sign*relative[axis, 2]-sp.Rational(expected[residue][axis], 2)
                coordinates.append(integer_polynomial(delta))

            pendant_target = crossing(-sigma)*turn*crossing(-sigma*(k+1))
            stabilizer = crossing(sigma)*turn*crossing(sigma)
            difference = sp.simplify(pendant_target.inv()*current*stabilizer.inv())
            sign2 = sp.simplify(difference[0, 0])
            if sign2 not in (sp.Integer(1), sp.Integer(-1)):
                raise AssertionError(sign2)
            zero_matrix(difference[:2, :2]-sign2*sp.eye(2))
            half_coordinates = [integer_polynomial(2*sign2*difference[axis, 2])
                                for axis in range(2)]
            rows.append({'sign': int(sigma), 'length': f'4r+{residue}',
                         'spectator_half_translation': expected[residue],
                         'integer_translation_remainders': coordinates,
                         'pendant_half_translation_coordinates': half_coordinates})
    return rows


def quantum_checks(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []

    def error(left, right):
        return mp.norm(left-right)/max(1, mp.norm(left), mp.norm(right))

    for level in range(2, 9):
        matrix, _, _ = original_matrices(level)
        turn = mp.matrix([[int(i+j == level-1) for j in range(level)]
                          for i in range(level)])
        unit = mp.eye(level)[:, 0]
        kappa = mp.exp(mp.pi*1j*(level-1)**2/(2*level))
        for sigma in (-1, 1):
            for length in range(7):
                chain = (turn*matrix**(2*sigma))**length
                operator = (kappa**(sigma*length)*matrix**(-sigma)*turn
                            *matrix**(-sigma*length)*turn*matrix**sigma)
                turned = (kappa**(sigma*(length+1))*matrix**(-sigma)*turn
                          *matrix**(-sigma*(length+1))*turn*matrix**(-sigma))
                pendant = (kappa**(sigma*length)*matrix**(-sigma)*turn
                           *matrix**(-sigma*(length+1))*unit)
                errors = {'operator': error(chain, operator),
                          'two_boundary_word': error(chain*turn, turned),
                          'pendant': error(chain*unit, pendant)}
                if max(errors.values()) > tolerance:
                    raise ArithmeticError((level, sigma, length, errors))
                rows.append({'N': level, 'sign': sigma, 'length': length,
                             'relative_errors': {name: mp.nstr(value, 35)
                                                 for name, value in errors.items()}})
        print(f'Full original chain identities checked at N={level}.', flush=True)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=120)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = {'scope': 'All-length affine mapping-class calculation and finite original-matrix normalization checks; no volume asymptotic is inferred.',
              'decimal_precision': args.precision,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'symbolic_affine_checks': affine_checks(),
              'quantum_checks': quantum_checks(args.precision)}
    output = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
        print(f'Saved {args.output}.')
    else:
        print(output)


if __name__ == '__main__':
    main()
