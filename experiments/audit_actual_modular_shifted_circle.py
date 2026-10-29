#!/usr/bin/env python3
"""Independent shifted-circle/negative-ray moment checks for full Psi."""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_modular_dilog_circle import psi, original_v


def check(N, R):
    rows = []
    # Inside R<1 the anchored closed formula is directly evaluable on
    # the whole shifted strip; no principal-factor exterior reset is used.
    for a in sorted({0, N-1}):
        circle = mp.quad(lambda theta: psi(N, 1, mp.log(R)+1j*theta)
                         * (R*mp.exp(1j*theta))**(-a)/(2*mp.pi),
                         [-mp.pi, 0, mp.pi])
        def ray(t):
            if not t:
                return mp.mpf(1) if a == N-1 else mp.mpf(0)
            return psi(N, 1, mp.log(t)+1j*mp.pi)*t**(N-a-1)
        correction = (-1)**(N-a)*mp.quad(ray, [0, R/2, R])/(2j*mp.pi)
        residual = abs(circle-correction-original_v(N, 1, a))
        assert residual < mp.mpf('1e-27')
        bound = mp.sqrt(1+R)*R**(N-a)/(2*mp.pi*(N-a))
        assert abs(correction) <= bound+mp.mpf('1e-30')
        for t in [R/3, R]:
            upper = psi(N, 1, mp.log(t)+1j*mp.pi)
            lower = psi(N, 1, mp.log(t)-1j*mp.pi)
            assert abs(abs(upper)**2-(1+t)) < mp.mpf('1e-30')
            assert abs(lower-(1-(-t)**N)*upper) < mp.mpf('1e-30')
        rows.append({'N': N, 'a': a, 'R': str(R),
                     'exact_relative_moment_error': float(residual),
                     'radial_modulus': float(abs(correction)),
                     'radial_bound': float(bound)})
    return rows


def main():
    mp.mp.dps = 42
    rows = [row for N in (2,3) for R in (mp.mpf('.55'),mp.mpf('.85'))
            for row in check(N, R)]
    result = {'status': 'PASS', 'shifted_moments': rows,
              'scope': 'Exact original shifted coefficient source; exterior theorem is proved analytically, not tested using reset principal factors.'}
    Path(__file__).with_name('actual_modular_shifted_circle_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'shifted_original_coefficients': len(rows),
                      'levels': 2, 'radii': 2}))


if __name__ == '__main__':
    main()
