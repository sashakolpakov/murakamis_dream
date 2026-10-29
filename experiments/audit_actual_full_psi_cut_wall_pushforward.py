#!/usr/bin/env python3
"""Full-function Cauchy pushforward and explicit scalar cut-current checks."""

import json
from pathlib import Path

import mpmath as mp

from audit_actual_modular_dilog_circle import psi, original_v


def cauchy_check(N, epsilon, A, radius):
    def angular(theta):
        t = radius*mp.exp(epsilon*1j*theta)
        return psi(N, epsilon, mp.log(radius)+epsilon*1j*theta)/(1-A/t)/(2*mp.pi)
    bulk = mp.quad(angular, [-mp.pi, 0, mp.pi])
    def ray(r):
        if not r:
            return 0
        return psi(N, epsilon, mp.log(r)+epsilon*1j*mp.pi)*(-r)**N/(1+A/r)/r
    current = epsilon*mp.quad(ray, [0, radius])/(2j*mp.pi)
    expected = psi(N, epsilon, mp.log(A))
    error = abs(bulk-current-expected)
    assert error < mp.mpf('1e-32')
    return {'N': N, 'epsilon': epsilon, 'argument': str(A),
            'Cauchy_full_relative_error': float(error),
            'retained_cut_current_modulus': float(abs(current))}


def two_atom_check(N, radius, c):
    d = N-1
    phi = mp.arg(c)
    assert 0 < phi < mp.pi and abs(c)*radius < 1
    second_cut = mp.pi-phi
    def angular(theta):
        logz = mp.log(radius)+1j*theta
        phase2 = phi+theta
        if phase2 > mp.pi:
            phase2 -= 2*mp.pi
        logcz = mp.log(abs(c)*radius)+1j*phase2
        return psi(N, 1, logz)*psi(N, 1, logcz)*mp.exp(-d*logz)/(2*mp.pi)
    bare = mp.quad(angular, [-mp.pi, 0, second_cut, mp.pi])
    def wall1(r):
        if not r:
            return -1
        logz = mp.log(r)+1j*mp.pi
        logcz = mp.log(abs(c)*r)+1j*(phi-mp.pi)
        return (psi(N, 1, logz)*psi(N, 1, logcz)
                *mp.exp((N-d)*logz)/r)
    def wall2(r):
        if not r:
            return c**N*mp.exp(1j*second_cut)
        logz = mp.log(r)+1j*second_cut
        logcz = mp.log(abs(c)*r)+1j*mp.pi
        return (psi(N, 1, logz)*psi(N, 1, logcz)
                *mp.exp(N*logcz-d*logz)/r)
    current1 = mp.quad(wall1, [0, radius])/(2j*mp.pi)
    current2 = mp.quad(wall2, [0, radius])/(2j*mp.pi)
    expected = mp.fsum(original_v(N, 1, a)*original_v(N, 1, d-a)*c**(d-a)
                        for a in range(N))
    error = abs(bare-current1-current2-expected)
    assert error < mp.mpf('1e-30')
    return {'N': N, 'original_finite_low_coefficient': str(expected),
            'bare_product_circle': str(bare), 'two_retained_cut_currents': [str(current1), str(current2)],
            'exact_cut_wall_pushforward_error': float(error),
            'bare_circle_error': float(abs(bare-expected))}


def main():
    mp.mp.dps = 48
    rows = [cauchy_check(N, epsilon, A, mp.mpf('.65'))
            for N in [2, 3, 5] for epsilon in [1, -1]
            for A in [mp.mpc('.2', '.15'), mp.mpc('-.3', '-.12')]]
    coupled = [two_atom_check(N, mp.mpf('.7'), mp.mpf('.43')*mp.exp(mp.mpf('.6')*1j))
               for N in [2, 3, 5]]
    assert any(row['bare_circle_error'] > .001 for row in coupled)
    result = {'status': 'PASS', 'full_relative_Cauchy_checks': rows,
              'coupled_two_atom_cut_wall_sources': coupled,
              'scope': 'Exact scalar full-function pushforward/current checks; no global geometric coefficient or exponential gap.'}
    Path(__file__).with_name('actual_full_psi_cut_wall_pushforward_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(rows)} full relative Cauchy identities and {len(coupled)} coupled two-cut source identities')


if __name__ == '__main__':
    main()
