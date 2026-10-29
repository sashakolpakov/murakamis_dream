#!/usr/bin/env python3
"""Exact finite-height source contours and actual factorial endpoint marks."""

import json
from pathlib import Path

import mpmath as mp

from audit_exact_factorial_interpolation import factorial


def height(u, ug, hg):
    return min(hg, hg*(1-u)/(1-ug))


def top_integral(f, L, R, N, ug, hg):
    kink = N*ug
    pieces = []
    if L < min(R, kink):
        pieces.append(mp.quad(lambda s: f(s+N*hg*1j), [L, min(R, kink)]))
    if max(L, kink) < R:
        slope = -hg/(1-ug)
        pieces.append(mp.quad(lambda s: f(s+1j*N*height(s/N, ug, hg))*(1+1j*slope),
                              [max(L, kink), R]))
    return mp.fsum(pieces)


def contour_case(N, name, g):
    ug, hg = mp.mpf('0.86919340003238'), mp.mpf('0.09218763788516')
    a = int(mp.ceil(mp.mpf('.51')*N+mp.mpf('.5')))
    b = int(mp.floor(mp.mpf('.99')*N-mp.mpf('.5')))
    L, R = mp.mpf(a)-mp.mpf('.5'), mp.mpf(b)+mp.mpf('.5')
    HL, HR = N*height(L/N, ug, hg), N*height(R/N, ug, hg)
    D = mp.mpf('.1')*N
    plus = lambda z: mp.exp(2j*mp.pi*z)/(1-mp.exp(2j*mp.pi*z))
    minus = lambda z: mp.exp(-2j*mp.pi*z)/(1-mp.exp(-2j*mp.pi*z))
    main = top_integral(g, L, R, N, ug, hg)
    upper = top_integral(lambda z: g(z)*plus(z), L, R, N, ug, hg)
    lower = mp.quad(lambda s: g(s-1j*D)*minus(s-1j*D), [L, R])
    edge = (1j*mp.quad(lambda t: g(L+1j*t)/(1+mp.exp(-2*mp.pi*t)), [0, HL])
            -1j*mp.quad(lambda t: g(R+1j*t)/(1+mp.exp(-2*mp.pi*t)), [0, HR])
            +1j*mp.quad(lambda t: g(L-1j*t)/(1+mp.exp(2*mp.pi*t)), [0, D])
            -1j*mp.quad(lambda t: g(R-1j*t)/(1+mp.exp(2*mp.pi*t)), [0, D]))
    original = mp.fsum(g(n) for n in range(a, b+1))
    residual = abs(original-main-upper-lower-edge)
    assert residual < max(1, abs(original))*mp.mpf('1e-38'), (N, name, residual)
    return dict(N=N, function=name, a=a, b=b, exact_identity_residual=float(residual),
                endpoint_source_retained=True)


def phi(x):
    if not x:
        return mp.mpc(0)
    X = mp.exp(2j*mp.pi*x)
    value = mp.polylog(2, X)
    # The boundary bank is Re(x)->0+; mpmath's value on the positive
    # cut is the other bank when Im(x)<0.
    if mp.re(x) == 0 and mp.im(x) < 0:
        value += 2j*mp.pi*mp.log(X)
    return (mp.polylog(2, 1)-value)/(2j*mp.pi)


def endpoint_factorial_cases():
    rows = []
    for N in (8, 16, 32):
        points = (mp.mpc(0), mp.mpc(mp.mpf('.2')/N), mp.mpc(mp.mpf(1)/(N*N)),
                  mp.mpc(0, '.04'), mp.mpc(0, '-.04'),
                  mp.mpc('.6', '-.1'), mp.mpc('.99', '.05'))
        for x in points:
            logarithmic_ratio = (mp.log(abs(factorial(N, N*x)))-N*mp.re(phi(x))
                                 -mp.log(1+N*abs(x))/2)
            assert abs(logarithmic_ratio) < 8
            rows.append(dict(N=N, x=[float(mp.re(x)), float(mp.im(x))],
                             endpoint_uniform_log_amplitude_ratio=float(logarithmic_ratio)))
    return rows


def actual_integer_interpoland():
    rows = []
    for N, n in ((8, 6), (13, 9)):
        H = 2j*mp.pi/N
        Fn = factorial(N, n)
        count = N-1-n
        constant = Fn**3/N*mp.exp(-H*n*(n+2)-1j*mp.pi*n*(n-N+1)/N)
        for w in (mp.mpc(0), mp.mpc(n), mp.mpc('.3', '.2'), mp.mpc(n-mp.mpf('.2'), '-.1')):
            actual = (mp.exp(H*(-n*(n+2)-w*(n+1)))*Fn**3
                      /(factorial(N, w)*factorial(N, n-w))*mp.exp(2j*mp.pi*w))
            finite = (constant*mp.exp(-1j*mp.pi*w*(w-N+1)/N)
                      *mp.fprod(1-mp.exp(H*(w+r)) for r in range(1, count+1)))
            error = abs(actual/finite-1)
            assert error < mp.mpf('1e-40')
            rows.append(dict(N=N, n=n, w=[float(mp.re(w)), float(mp.im(w))],
                             original_inner_interpoland_error=float(error)))
    return rows


def main():
    with mp.workdps(55):
        contours = []
        for N in (8, 12, 20):
            tests = [('constant', lambda z: mp.mpc(1)), ('cubic', lambda z: z**3),
                     ('exponential', lambda z: mp.exp((mp.mpf('.1')+mp.mpf('.07')*1j)*z)),
                     ('lattice_alias', lambda z: mp.exp(4j*mp.pi*z))]
            contours.extend(contour_case(N, name, f) for name, f in tests)
        endpoint = endpoint_factorial_cases()
        actual = actual_integer_interpoland()
    result = dict(status='PASS', exact_contour_cases=contours, endpoint_factorials=endpoint,
                  actual_inner_interpolands=actual,
                  scope='Exact finite-height outer source formula and uniform endpoint amplitude marks; geometric phase bounds and outer saddle selection are separate.')
    Path(__file__).with_name('outer_finite_height_quadrature_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', contour_cases=len(contours), endpoint_factorial_cases=len(endpoint),
                          actual_interpoland_cases=len(actual))))


if __name__ == '__main__':
    main()
