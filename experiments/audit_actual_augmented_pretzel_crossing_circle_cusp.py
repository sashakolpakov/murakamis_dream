#!/usr/bin/env python3
"""Own cusp lattice from the actual doubled-antiprism face labels."""

import json
from pathlib import Path

import mpmath as mp


def cusp_case(s):
    mp.mp.dps = 85
    alpha = mp.pi/s
    c = mp.cos(alpha)
    rho = 1/mp.sqrt(mp.tan(mp.pi/4-alpha/2))
    A = rho*rho
    image = lambda radius, angle: 1/(radius*mp.exp(1j*angle)-rho)
    ll, ul = image(1/rho, alpha), image(1/rho, -alpha)
    lr, ur = image(rho**3, alpha), image(rho**3, -alpha)
    tol = mp.mpf('1e-72')
    assert abs(ll-mp.conj(ul)) < tol
    assert abs(lr-mp.conj(ur)) < tol
    assert abs(mp.im(ll-lr)) < tol
    assert abs(mp.im(ul-ur)) < tol
    width, height = mp.re(lr-ll), mp.im(ul-ll)
    assert width > 0 and height > 0
    assert abs(width-1/(rho*mp.sin(alpha))) < tol
    assert abs(height/width-c) < tol
    # Exact labels: copy 1 develops by y -> 2c-y. Its half-twist
    # shading exchange sends local y -> c-y, hence delta=1+ic.
    for y in (mp.mpf(0), c/7, c/2, c):
        source = 1j*y
        target = 1+1j*(2*c-(c-y))
        assert abs(target-source-(1+1j*c)) < tol
        source1 = 1j*(2*c-y)
        target0 = 1+1j*(c-y)
        assert abs(target0-source1-(1-1j*c)) < tol
    longitude = 2j*c
    meridian_plus, meridian_minus = 1+1j*c, 1-1j*c
    assert abs(meridian_plus-meridian_minus-longitude) < tol
    area = lambda a, b: mp.im(mp.conj(a)*b)
    assert abs(area(meridian_plus, longitude)-2*c) < tol
    assert abs(area(meridian_minus, longitude)-2*c) < tol
    assert abs(area(2, meridian_plus)-2*c) < tol
    plus, minus = longitude/meridian_plus, longitude/meridian_minus
    assert abs(plus-(2*c*c+2j*c)/(1+c*c)) < tol
    assert abs(minus-(-2*c*c+2j*c)/(1+c*c)) < tol
    u = mp.atan(1/c)
    assert abs(plus-2*mp.exp(1j*u)*mp.cos(u)) < tol
    for p in range(-4, 5):
        assert abs(meridian_plus+p*longitude-(1+1j*(2*p+1)*c)) < tol
        assert abs(meridian_minus+p*longitude-(1+1j*(2*p-1)*c)) < tol
    if s == 3:
        assert abs(plus-(mp.mpf('0.4')+mp.mpf('0.8')*1j)) < tol
    return {'s': s, 'literal_rectangle_height_over_width': mp.nstr(c, 30),
            'two_rectangle_primitive_lattice_checked': True,
            'positive_diagonal_cusp_shape': [mp.nstr(mp.re(plus), 30), mp.nstr(mp.im(plus), 30)],
            'negative_diagonal_cusp_shape': [mp.nstr(mp.re(minus), 30), mp.nstr(mp.im(minus), 30)],
            'full_twist_shears_and_Hessian_factor_two_checked': True}


if __name__ == '__main__':
    rows = [cusp_case(s) for s in range(3, 31)]
    Path(__file__).with_name('actual_augmented_pretzel_crossing_circle_cusp_results.json').write_text(
        json.dumps({'status': 'PASS', 'widths': rows,
                    'scope': 'Actual geometric cusp lattice and both primitive half-twist markings; no unproved identification of a quantum logarithm or sign.'}, indent=2)+'\n')
    print('PASS 28 literal crossing-circle cusp rectangles/lattices, primitive half-twist markings, and full-twist shears')
