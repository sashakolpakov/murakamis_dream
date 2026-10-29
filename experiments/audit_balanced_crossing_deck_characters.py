#!/usr/bin/env python3
"""Full-turn characters checked from full Psi's finite-product definition."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def psi(z, n):
    """Convergent Re(z)<0 formula, continued in its explicit log coordinate."""
    q = mp.exp(2j*mp.pi/n)
    w = mp.exp(z)
    assert abs(w) < 1
    log_v = (mp.mpf(n-1)/(2*n))*mp.log(1-w**n)
    log_v -= sum(mp.mpf(k)/n*mp.log(1-q**k*w) for k in range(1, n))
    extra = (mp.mpf(n+1)/(2*n)+1j*z/(2*mp.pi))*mp.log(1-w**n)
    extra += 1j*mp.polylog(2, w**n)/(2*mp.pi*n)
    return mp.exp(log_v+extra)


def kernel(logs, n):
    a, b, c, d = logs
    h, t = 2j*mp.pi/n, 2j*mp.pi
    xlog = 1j*mp.pi-h/2
    beta, f, rho = b-a-xlog, d-c-xlog, c-a
    lam = d-b+t
    g, hh = d-a-xlog, b-c+xlog
    ee = n*f+(n+1)*lam/2+(g*hh+lam**2/2)/h
    rc = mp.exp(n*rho)
    return rc*(1-rc)**2*mp.exp(ee)*psi(beta, n)*psi(h-f, n)*psi(lam+t+h, n)/psi(rho, n)


def characters(logs, n):
    a, b, c, d = [mp.exp(n*z) for z in logs]
    s = (-1)**(n+1)
    return [s*c*(a-s*b)/(b*(a-c)), s*(d-b)/(a-s*b),
            s*(a-c)/(d-s*c), s*b*(d-s*c)/(c*(d-b))]


def symbolic_check():
    a, b, c, d = sp.symbols('A B C D', nonzero=True)
    for s in [-1, 1]:
        mus = [s*c*(a-s*b)/(b*(a-c)), s*(d-b)/(a-s*b),
               s*(a-c)/(d-s*c), s*b*(d-s*c)/(c*(d-b))]
        defects = [a*(s*c-b)/(b*(a-c)), (s*d-a)/(a-s*b),
                   (s*a-d)/(d-s*c), d*(s*b-c)/(c*(d-b))]
        assert all(sp.cancel(mu-1-defect) == 0 for mu, defect in zip(mus, defects))
        assert sp.cancel(sp.prod(mus)-1) == 0
        assert all(sp.cancel(mu.subs({c:s*b, d:s*a})-1) == 0 for mu in mus)
    return {'both_parities': True, 'four_defects': True,
            'product_one': True, 'balanced_specialization_one': True}


def main():
    mp.mp.dps = 90
    cases = []
    for n in [2, 3, 4, 5, 8, 11, 12]:
        for offset in [mp.mpf('0.0'), mp.mpf('0.17')]:
            logs = [mp.log(2)+0.1j, mp.log(mp.mpf('0.7'))+(0.3+offset)*1j,
                    mp.log(mp.mpf('0.1'))+(1.4-offset)*1j,
                    mp.log(mp.mpf('0.3'))+1.0j]
            base = kernel(logs, n)
            expected = characters(logs, n)
            errors = []
            for port in range(4):
                shifted = logs.copy()
                shifted[port] += 2j*mp.pi
                actual = kernel(shifted, n)/base
                error = abs(actual-expected[port])/max(1, abs(expected[port]))
                assert error < mp.mpf('1e-70'), (n, port, error)
                errors.append(float(error))
            cases.append({'N': n, 'offset': str(offset), 'four_port_max_relative_error': max(errors)})
    result = {'status': 'PASS', 'symbolic': symbolic_check(),
              'independent_finite_product_checks': cases,
              'scope': 'Exact marked full-turn characters; no cycle selection or volume estimate.'}
    Path(__file__).with_name('balanced_crossing_deck_characters_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 56 independent full-Psi deck shifts, both-parity rational defects and balanced unit characters')


if __name__ == '__main__':
    main()
