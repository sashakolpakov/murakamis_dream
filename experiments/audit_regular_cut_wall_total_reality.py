#!/usr/bin/env python3
"""Exact radial implicit identities and complex Jacobians for actual cut walls."""

import json
from pathlib import Path

import sympy as sp
import mpmath as mp


def simple_wall(n):
    tau = sp.symbols('tau', real=True)
    a = sp.Matrix([[1]+[(-1)**j*(j+1) for j in range(1, n)]])
    initial = sp.Matrix([sp.Rational(j+1, 7)+sp.Rational((-1)**j, j+2)*tau
                         for j in range(n)])
    target = sp.Matrix([sp.Rational(2*j+3, 5) for j in range(n)])
    ell = sp.Rational(2, 9)
    denominator = (a*(target-initial))[0]
    assert denominator != 0
    root = sp.factor((tau-ell-(a*initial)[0])/denominator)
    rho = (1-root)*initial+root*target
    assert sp.factor((a*rho)[0]+ell-tau) == 0
    assert sp.factor((a*rho.diff(tau))[0]-1) == 0
    # u=a.Z, Y=(Z_2,...,Z_n): kernel basis has complementary projection I.
    V = sp.zeros(n, max(0, n-1))
    for j in range(1, n):
        V[j, j-1] = 1
        V[0, j-1] = -a[j]
    assert a*V == sp.zeros(1, max(0, n-1))
    columns = [rho.diff(tau)]+[sp.I*V[:, j] for j in range(n-1)]
    Zjac = sp.Matrix.hstack(*columns)
    coordinate_change = sp.eye(n)
    coordinate_change[0, :] = a
    jacobian = coordinate_change*Zjac
    determinant = sp.factor(jacobian.det())
    assert determinant == sp.I**(n-1)
    return {'head_dimension': n, 'primitive_wall_row': [int(v) for v in a],
            'implicit_radial_constraint_exact': True,
            'free_radial_derivative_exactly_one': True,
            'complex_jacobian_determinant': str(determinant)}


def independent_wall(k, n, extra):
    # General real left-inverse and kernel blocks in adapted coordinates.
    lower = sp.Matrix(n-k, k, lambda i, j: sp.Rational((i+1)*(j+2), 11))
    J = sp.zeros(n+extra)
    for i in range(k):
        J[i, i] = 1
    for i in range(extra):
        J[k+i, k+i] = sp.Rational(i+2, 3)+sp.I*sp.Rational(i+1, 5)
    for i in range(n-k):
        row = k+extra+i
        for j in range(k):
            J[row, j] = lower[i, j]
        for j in range(extra):
            J[row, k+j] = (i+1)*(j+1)*(1+sp.I)
        J[row, k+extra+i] = sp.I
    determinant = sp.factor(J.det())
    assert determinant != 0
    expected = sp.I**(n-k)
    for i in range(extra):
        expected *= sp.Rational(i+2, 3)+sp.I*sp.Rational(i+1, 5)
    assert sp.factor(determinant-expected) == 0
    return {'independent_free_wall_radii': k, 'head_dimension': n,
            'additional_moment_Gaussian_cap_blocks': extra,
            'complex_jacobian_determinant': str(determinant)}


def one_parameter_corner():
    s, t1, t2 = sp.symbols('s t1 t2', real=True)
    equations = [t1-s, t2-2*s]
    solution = sp.solve(equations, (t1, t2), dict=True)[0]
    assert solution[t2] == 2*solution[t1]
    return {'independent_wall_rows': 2, 'homotopy_parameters': 1,
            'free_radial_parameters': 1, 'retained_radial_relation': 'tau_2=2*tau_1',
            'not_claimed_free_multiwall_chart': True}


def transverse_pole_growth():
    rows = []
    with mp.workdps(50):
        a, c = mp.mpf('1'), mp.mpf('.1')
        for N in [2, 5, 11]:
            radial = 2j*mp.pi*mp.exp(N*c)*mp.quad(
                lambda r: mp.exp(-N*r*r)*mp.besselj(1, N*a*r), [0, 1, mp.inf])
            exact = 2j*mp.pi*mp.exp(N*c)*(1-mp.exp(-N*a*a/4))/(N*a)
            assert abs(radial-exact) < mp.mpf('1e-40')
            rows.append({'N': N, 'absolute_integral_error': float(abs(radial-exact)),
                         'pole_exponential_rate': str(c),
                         'regular_holomorphic_critical_rate': str(c-a*a/4),
                         'no_complex_critical_point_on_divisor': True})
    return rows


def main():
    rows = [simple_wall(n) for n in range(1, 8)]
    multiple = [independent_wall(k, n, extra) for n in range(2, 7)
                for k in range(1, n+1) for extra in [0, 2]]
    result = {'status': 'PASS', 'actual_simple_wall_radial_charts': rows,
              'free_independent_wall_block_jacobians': multiple,
              'one_parameter_corner_scope_check': one_parameter_corner(),
              'transverse_L1_pole_growth_countermodel': transverse_pole_growth(),
              'scope': 'Restricted complex stationarity is full on regular simple/all-pole charts. No thimble coefficient or unresolved corner claim.'}
    Path(__file__).with_name('regular_cut_wall_total_reality_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(rows)} exact implicit simple-wall charts, {len(multiple)} block Jacobians, '
          'the one-parameter corner countercheck and three transverse pole growth identities')


if __name__ == '__main__':
    main()
