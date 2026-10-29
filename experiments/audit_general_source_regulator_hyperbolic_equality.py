#!/usr/bin/env python3
"""Focused checks of the new equivariant-map geometry and arbitrary slopes.

No knot asymptotic is inferred. The all-base statement is proved in the note;
these checks catch map-order, frame, positivity and factor-two errors.
"""

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 75


def b3(t):
    r = abs(t)
    if r < 1:
        return mp.mpf(2) / 3 - t*t + r**3/2, -2*t + 3*t*r/2
    if r < 2:
        return (2-r)**3/6, -mp.sign(t)*(2-r)**2/2
    return mp.mpf(0), mp.mpf(0)


def cusp_development(x, y, tau, U, V):
    w = x + tau*y
    q = -1/U
    value, dx, dy, mass = [mp.mpc(0) for _ in range(4)]
    for m in range(int(mp.floor(x))-1, int(mp.floor(x))+3):
        bx, dbx = b3(x-m)
        for n in range(int(mp.floor(y))-1, int(mp.floor(y))+3):
            by, dby = b3(y-n)
            weight = bx*by
            mult = mp.exp(m*U+n*V)
            affine = q+mult*(w-m-n*tau-q)
            value += weight*affine
            dx += dbx*by*affine+weight*mult
            dy += bx*dby*affine+weight*mult*tau
            mass += weight
    assert abs(mass-1) < mp.mpf('1e-65')
    determinant = mp.re(dx)*mp.im(dy)-mp.im(dx)*mp.re(dy)
    return value, dx, dy, determinant


def extended_gcd(a, b):
    if b == 0:
        return (1 if a > 0 else -1), 0
    r, s = extended_gcd(b, a % b)
    return s, r-(a//b)*s


def cusp_case(a, b, epsilon, tau):
    assert math.gcd(a, b) == 1
    U = 2j*mp.pi*epsilon/(a+b*tau)
    V = tau*U
    q = -1/U
    assert abs(a*U+b*V-2j*mp.pi*epsilon) < mp.mpf('1e-65')
    minimum = mp.inf
    maximum_equivariance = mp.mpf(0)
    maximum_height_error = mp.mpf(0)
    for x in (mp.mpf('.13'), mp.mpf('.47'), mp.mpf('.91')):
        for y in (mp.mpf('.19'), mp.mpf('.62'), mp.mpf('.88')):
            val, dx, dy, jac = cusp_development(x, y, tau, U, V)
            minimum = min(minimum, jac)
            assert jac > 0
            # Full hyperbolic tail determinant is exp(t+chi)*jac.
            chi = x*mp.re(U)+y*mp.re(V)
            assert mp.exp(mp.mpf('1.3')+chi)*jac > 0
            for r, s in ((1, 0), (0, 1), (2, -1), (-1, 2)):
                shifted = cusp_development(x+r, y+s, tau, U, V)[0]
                expected = q+mp.exp(r*U+s*V)*(val-q)
                maximum_equivariance = max(maximum_equivariance,
                                           abs(shifted-expected))
                actual_log = mp.log((shifted-q)/(val-q))
                assert abs(actual_log-r*U-s*V) < mp.mpf('1e-60')
                height_ratio = mp.exp((x+r)*mp.re(U)+(y+s)*mp.re(V)-chi)
                maximum_height_error = max(maximum_height_error,
                         abs(height_ratio-abs(mp.exp(r*U+s*V))))
    assert maximum_equivariance < mp.mpf('1e-60')
    assert maximum_height_error < mp.mpf('1e-65')
    r, s = extended_gcd(a, b)
    assert a*r+b*s == 1
    c, d = -s, r
    core = c*U+d*V
    assert a*d-b*c == 1
    assert abs(mp.re(core)) > 0
    assert mp.im(mp.conj(U)*V) > 0
    assert mp.sign(mp.re(core)) == -epsilon
    return {'primitive_slope': [a, b], 'epsilon': epsilon,
            'minimum_link_jacobian': float(minimum),
            'maximum_affine_equivariance_error': float(maximum_equivariance),
            'maximum_height_equivariance_error': float(maximum_height_error),
            'actual_small_logs_checked': True,
            'complementary_core_real_period': float(mp.re(core))}


def point(w, height):
    rr = abs(w)**2+height**2
    return mp.matrix([(rr+1)/(2*height), mp.re(w)/height,
                      mp.im(w)/height, (rr-1)/(2*height)])


def inner(a, b):
    return -a[0]*b[0]+sum(a[i]*b[i] for i in (1, 2, 3))


def action(matrix, x):
    h = mp.matrix([[x[0]+x[3], x[1]+1j*x[2]],
                   [x[1]-1j*x[2], x[0]-x[3]]])
    result = matrix*h*matrix.H
    return mp.matrix([mp.re(result[0, 0]+result[1, 1])/2,
                      mp.re(result[0, 1]+result[1, 0])/2,
                      mp.re((result[0, 1]-result[1, 0])/(2j)),
                      mp.re(result[0, 0]-result[1, 1])/2])


def sl(a, b, c):
    return mp.matrix([[mp.exp(a)+b*c*mp.exp(-a), b*mp.exp(-a)],
                      [c*mp.exp(-a), mp.exp(-a)]])


def normalize_sum(weights, vectors):
    result = mp.matrix([mp.fsum(weights[j]*vectors[j][i]
                    for j in range(len(weights))) for i in range(4)])
    assert result[0] > 0 and inner(result, result) <= -1+mp.mpf('1e-60')
    result /= mp.sqrt(-inner(result, result))
    assert abs(inner(result, result)+1) < mp.mpf('1e-60')
    return result


def lorentz_case(index):
    x = point(mp.mpc(index/10, -.23), mp.mpf('.9')+index/20)
    eps = mp.mpf('0.0001')*(index+1)
    originals = [sl(mp.mpc('.1', '.03')*j, mp.mpc('.2', '.1')*j,
                    mp.mpc('-.1', '.07')*j) for j in range(4)]
    deformed = [sl(eps*j, eps*mp.mpc(j, -j/3), -eps*j)*originals[j]
                for j in range(4)]
    weights = [mp.mpf(1)/10, mp.mpf(2)/10, mp.mpf(3)/10, mp.mpf(4)/10]
    vectors = [action(deformed[j]*originals[j]**-1, x) for j in range(4)]
    average = normalize_sum(weights, vectors)
    old_delta = sl(mp.mpc('.13', '.02'), mp.mpc('.1', '.12'),
                   mp.mpc('-.2', '.01'))
    new_delta = sl(eps, eps/2, -eps/3)*old_delta
    shifted_x = action(old_delta, x)
    shifted_vectors = [action((new_delta*deformed[j]) *
                       (old_delta*originals[j])**-1, shifted_x)
                       for j in range(4)]
    shifted_average = normalize_sum(weights, shifted_vectors)
    error = mp.norm(shifted_average-action(new_delta, average))
    assert error < mp.mpf('1e-60')
    return {'case': index, 'future_timelike_normalization': True,
            'exact_reindexing_equivariance_error': float(error)}


def symbolic_action():
    a, b, epsilon, x, y = sp.symbols('a b epsilon x y', real=True,
                                     nonzero=True)
    U = x+sp.I*y
    V = (2*sp.pi*sp.I*epsilon-a*U)/b
    correction = a*U**2/(4*b)-sp.pi*sp.I*epsilon*U/b
    assert sp.simplify(sp.im(correction)+sp.re(U)*sp.im(V)/2) == 0
    derivative = sp.diff(a*sp.Symbol('U')**2/(4*b)
                         -sp.pi*sp.I*epsilon*sp.Symbol('U')/b,
                         sp.Symbol('U'))
    assert sp.simplify(derivative-(a*sp.Symbol('U')
                         -2*sp.pi*sp.I*epsilon)/(2*b)) == 0
    return {'arbitrary_primitive_filling_correction_exact': True,
            'squared_log_half_factor_retained': True}


if __name__ == '__main__':
    symbolic = symbolic_action()
    lorentz = [lorentz_case(j) for j in range(8)]
    cusp = [cusp_case(a, b, epsilon, tau)
            for a, b in ((1, 101), (1, -101), (37, 52), (43, -59))
            for epsilon in (-1, 1)
            for tau in (mp.mpc('.3', '1.1'), mp.mpc('-.4', '.8'))]
    result = {'status': 'PASS', 'symbolic_action': symbolic,
              'Lorentz_average_families': lorentz,
              'affine_cusp_and_arbitrary_slope_families': cusp,
              'scope': 'General geometric construction and action algebra only; no additional knot-source asymptotic inferred.'}
    Path(__file__).with_name('general_source_regulator_hyperbolic_equality_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS arbitrary-slope action algebra; {len(lorentz)} Lorentz equivariance families; '
          f'{len(cusp)} positive affine-cusp/primitive-slope families')
