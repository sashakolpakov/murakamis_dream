#!/usr/bin/env python3
"""Actual finite crossing ratios, aligned units, bulk normal insertion."""

import json
from pathlib import Path

import mpmath as mp
import sympy as s

mp.mp.dps = 70
c = 2*mp.pi*1j


def J(z):
    return 1 if z == 0 else 2*mp.sinh(z/2)/z


def P(H, x):
    return -mp.expm1(H*x)


def parameters(N, b):
    H0 = c/N
    H = H0/(1-b/N)
    return H0, H


def coefficient(sign, H, b, i, j, k):
    logx = c/2+H*(b-1)/2
    if sign == 1:
        ans = (-1)**k*mp.exp(-(i+j+k)*logx
            +H*(i*j+(i-j)*k-mp.mpf(k*(k+1))/2))
        top, start = j, b-i
    else:
        ans = mp.exp((i+j-k)*logx-H*i*j)
        top, start = i, b-j
    return ans*mp.fprod(P(H, top+r)/P(H, r) for r in range(1, k+1)) \
        *mp.fprod(P(H, start+r) for r in range(k))


def direct_positive(H, b, i, j, k):
    q, rho, M = mp.exp(H/2), 2*mp.sinh(H/2), mp.exp(H*b/2)
    logx = c/2+H*(b-1)/2
    qfac = mp.fprod(mp.sinh(H*r/2)/mp.sinh(H/2) for r in range(1, k+1))
    cartan = mp.exp(-(i+j)*logx+H*(i-k)*(j+k))
    coeff = mp.exp(H*k*(k-1)/4)/(rho**k*qfac)
    eprod = mp.fprod(M*mp.exp(-H*(i-r))-1/M for r in range(k))
    fprod = mp.fprod(P(H, j+r) for r in range(1, k+1))
    return cartan*coeff*eprod*fprod


def logU(H0, H, x):
    return mp.log(H/H0)+(H-H0)*x/2+mp.log(J(H*x))-mp.log(J(H0*x))


def log_ratio(sign, N, b, i, j, k):
    H0, H = parameters(N, b)
    if sign == 1:
        A = i*j+(i-j)*k-mp.mpf(k*(k+1))/2-(b-1)*(i+j+k)/2
        top, start = j, b-i
    else:
        A = -i*j+(b-1)*(i+j-k)/2
        top, start = i, b-j
    ans = (H-H0)*A
    ans += sum(logU(H0, H, top+r)-logU(H0, H, r) for r in range(1, k+1))
    ans += sum(logU(H0, H, start+r) for r in range(k))
    return ans


def finite_ratio_checks():
    records = []
    for N in (12, 17, 24):
        for b in (mp.mpf('.4'), mp.mpc('.3', '.2'), mp.mpf(2)):
            H0, H = parameters(N, b)
            flows = ((1, N//2, N//8, N//4),
                     (-1, N//8, N//2, N//4),
                     (1, 5, 2, 4), (-1, 2, 5, 4))
            for sign, i, j, k in flows:
                left = coefficient(sign, H, b, i, j, k)
                old = coefficient(sign, H0, b, i, j, k)
                unit = mp.exp(log_ratio(sign, N, b, i, j, k))
                assert abs(left-unit*old) < mp.mpf('1e-55')*(1+abs(left))
                assert abs(unit) > mp.mpf('1e-8')
                if sign == 1:
                    direct = direct_positive(H, b, i, j, k)
                    assert abs(left-direct) < mp.mpf('1e-55')*(1+abs(left))
                records.append({'level': N, 'normal_parameter': str(b),
                                'sign': sign, 'finite_actual_ratio': True,
                                'aligned_zero_continued_by_unit': True})
    return records


def scalar_and_obstruction_checks():
    N, b, H0 = s.symbols('N b H0', nonzero=True)
    n, H = N-1, H0*N/(N-b)
    dc = (H*n*n-H0*(n+b)**2)/4
    dt = (-H*n*n-H0*(b*b-n*n))/4
    dx = (H-H0)*(b-1)/2
    assert s.cancel(dc-dt-n*dx) == 0
    records = []
    for NN in (8, 9, 16):
        bb = mp.mpf('.4')
        h0, hh = parameters(NN, bb)
        nn = NN-1
        i1, i2 = NN//4, NN//2
        ratio1 = coefficient(1, hh, bb, i1, i1, 0)/coefficient(1, h0, bb, i1, i1, 0)
        ratio2 = coefficient(1, hh, bb, i2, i2, 0)/coefficient(1, h0, bb, i2, i2, 0)
        expected = mp.exp((hh-h0)*(i1-i2)*(i1+i2-bb+1))
        assert abs(ratio1/ratio2-expected) < mp.mpf('1e-60')
        assert abs(expected-1) > mp.mpf('.01')
        # Periodic boundary zero: no removable unit comparison here.
        bb = mp.mpf(-1)
        h0, hh = parameters(NN, bb)
        moving = coefficient(1, hh, bb, nn, 0, 1)
        fixed = coefficient(1, h0, bb, nn, 0, 1)
        assert abs(fixed) < mp.mpf('1e-60')
        assert abs(moving) > mp.mpf('.01')
        rankA = sum(abs(P(hh, bb-i)) > mp.mpf('1e-55') for i in range(1, NN))
        rankB = sum(abs(P(h0, bb-i)) > mp.mpf('1e-55') for i in range(1, NN))
        assert (rankA, rankB) == (NN-1, NN-2)
        # The full moving-q Frobenius power retains the actual bulk clock.
        bb = mp.mpc('.3', '.2')
        h0, hh = parameters(NN, bb)
        for i in (0, NN//3, nn):
            lhs = mp.exp(NN*(c/2+hh*(bb-1)/2-hh*i))
            rhs = (-1)**nn*mp.exp(hh*bb*(mp.mpf(nn)/2-i))
            assert abs(lhs-rhs) < mp.mpf('1e-60')*(1+abs(rhs))
        records.append({'level': NN, 'diagonal_scalar_coboundary_obstructed': True,
                        'periodic_zero_and_E_rank_mismatch': True,
                        'Frobenius_clock_residual': True})
    return records


def hfun(x):
    return 1 if x == 0 else c*x/(-mp.expm1(-c*x))


def bulk_insertion(sign, u, v, t):
    if sign == 1:
        base = c*(u*v+(u-v)*t-t*t/2)
        return base+mp.quad(lambda x: hfun(v+x)-hfun(x)+hfun(-u+x), [0, t])
    base = -c*u*v
    return base+mp.quad(lambda x: hfun(u+x)-hfun(x)+hfun(-v+x), [0, t])


def bulk_checks():
    records = []
    for N in (32, 64, 128):
        worst = mp.mpf(0)
        for b in (mp.mpf('.4'), mp.mpc('.3', '.2')):
            for sign, ii, jj, kk in ((1, .45, .15, .2), (-1, .15, .45, .2),
                                     (1, .5, .1, .5), (-1, .1, .5, .5)):
                i, j, k = int(ii*N), int(jj*N), int(kk*N)
                u, v, t = mp.mpf(i)/N, mp.mpf(j)/N, mp.mpf(k)/N
                actual = log_ratio(sign, N, b, i, j, k)
                target = b*bulk_insertion(sign, u, v, t)
                worst = max(worst, N*abs(actual-target))
        assert worst < 100
        records.append({'level': N, 'N_times_bulk_log_error': float(worst)})
    return records


def main():
    result = {'finite_actual_coefficients_and_units': finite_ratio_checks(),
              'full_scalar_and_finite_obstructions': scalar_and_obstruction_checks(),
              'uniform_bulk_normal_insertion': bulk_checks(),
              'precision_decimal_digits': mp.mp.dps,
              'scope': 'Actual crossing normal comparison and explicit residuals; no selected knot-period or norm assertion.'}
    target = Path(__file__).with_name('actual_crossing_q_normal_meridian_ratio_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'finite_coefficient_cases': len(result['finite_actual_coefficients_and_units']),
                      'obstruction_levels': len(result['full_scalar_and_finite_obstructions']),
                      'bulk_response_levels': len(result['uniform_bulk_normal_insertion'])}))


if __name__ == '__main__':
    main()
