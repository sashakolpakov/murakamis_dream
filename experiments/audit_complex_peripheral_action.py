#!/usr/bin/env python3
"""Complex action/regulator constants and logarithmic path audit.

The integration chart beta=[z], M=sqrt(z), ell=(1-z)^(-1) tests
delta beta=-2M wedge ell. It is not asserted to be a knot curve.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def symbolic_checks():
    a, b, theta, phi, da, dt, dp = sp.symbols('a b theta phi da dt dp', real=True)
    imaginary_action = 2*(b*dt+phi*da)
    regulator = 2*(b*dt-a*dp)
    boundary = 2*(phi*da+a*dp)
    assert sp.expand(imaginary_action-regulator-boundary) == 0
    aa, tt, x = sp.symbols('aa tt x', positive=True)
    collision = sp.Rational(1, 2)+sp.I*tt/(2*aa)
    s1 = aa*(x*x-x)/2
    s2 = -s1+sp.I*tt*x
    mismatch = sp.simplify((s2-s1).subs(x, collision))
    assert sp.simplify(mismatch-(aa/4-tt**2/(4*aa)+sp.I*tt/2)) == 0
    assert sp.simplify((sp.diff(s2, x)-sp.diff(s1, x)).subs(x, collision)) == 0
    return {'differential_identity': True, 'exact_gaussian_node_mismatch': str(mismatch)}


def bloch(z):
    return mp.im(mp.polylog(2, z))+mp.log(abs(z))*mp.arg(1-z)


def open_path(radial_bulge, end_radius):
    l0 = mp.pi*1j
    l1 = mp.log(end_radius)+mp.pi*1j/3
    def logz(t):
        return l0*(1-t)+l1*t+radial_bulge*mp.sin(mp.pi*t)
    def dlogz(t):
        return l1-l0+radial_bulge*mp.pi*mp.cos(mp.pi*t)
    def integrand(t):
        z = mp.exp(logz(t))
        return -mp.log(1-z)*dlogz(t)
    action = mp.quad(integrand, [0, mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75'), 1])
    start, end = mp.exp(l0), mp.exp(l1)
    deltaR = bloch(end)-bloch(start)
    longitude_argument = mp.im(-mp.log(1-end))
    endpoint = mp.log(abs(end))*longitude_argument
    error = abs(mp.im(action)-deltaR-endpoint)
    assert error < mp.mpf('1e-60'), error
    # The same correction written in the actual M coordinate has a 2.
    assert abs(endpoint-2*(mp.log(abs(end))/2)*longitude_argument) < mp.mpf('1e-65')
    # A longitude-log deck shift must retain its complete endpoint term.
    for n in [-2, 3]:
        shifted = action+2*mp.pi*1j*n*(l1-l0)
        expected = 2*mp.pi*n*mp.re(l1-l0)
        assert abs(mp.im(shifted-action)-expected) < mp.mpf('1e-60')
    return {'radial_bulge': str(radial_bulge), 'end_radius': str(end_radius),
            'imaginary_action': mp.nstr(mp.im(action), 25),
            'regulator_difference': mp.nstr(deltaR, 25),
            'retained_endpoint_term': mp.nstr(endpoint, 25),
            'error': mp.nstr(error, 8)}


def winding_loop(radius):
    # z(t)=1-radius*exp(2pi i t), with a continuous longitude log.
    # Both z and 1-z wind once; the latter gives longitude winding -1.
    def z(t):
        return 1-radius*mp.exp(2*mp.pi*1j*t)
    def derivative(t):
        return -2*mp.pi*1j*radius*mp.exp(2*mp.pi*1j*t)
    def v(t):
        return -mp.log(radius)-2*mp.pi*1j*t
    action = mp.quad(lambda t: v(t)*derivative(t)/z(t),
                     [0, mp.mpf('.25'), mp.mpf('.5'), mp.mpf('.75'), 1])
    log_abs_M = mp.log(radius-1)/2
    predicted = 4*mp.pi*(-1)*log_abs_M
    error = abs(mp.im(action)-predicted)
    assert error < mp.mpf('1e-60'), error
    return {'loop_radius': str(radius), 'unit_meridian_base': radius == 2,
            'longitude_log_winding': -1,
            'imaginary_action': mp.nstr(mp.im(action), 25),
            'predicted_retained_boundary': mp.nstr(predicted, 25),
            'error': mp.nstr(error, 8)}


def main():
    mp.mp.dps = 80
    data = {'status': 'PASS', 'symbolic': symbolic_checks(),
            'open_complex_paths': [open_path(mp.mpf(r), mp.mpf(s))
                                   for r in ['-.4', '.3', '.7']
                                   for s in ['1', '.73']],
            'winding_loops': [winding_loop(mp.mpf(2)), winding_loop(mp.mpf(3))],
            'scope': ('Identity and branch-normalization checks in a one-shape Bloch chart; '
                      'not a new knot quantum/source or volume theorem.')}
    Path(__file__).with_name('complex_peripheral_action_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
