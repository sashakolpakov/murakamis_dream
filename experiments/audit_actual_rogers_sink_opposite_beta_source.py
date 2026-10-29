#!/usr/bin/env python3
"""Actual U/U/F polynomial, opposite-root source, and retained norm current."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_beta_current_connection_and_monodromy import log_full_psi


def factorials(N):
    Q = mp.exp(2j*mp.pi/N)
    F = [mp.mpc(1)]
    for a in range(1, N):
        F.append(F[-1]*(1-Q**a))
    return F


def Rogers(N, u, v):
    F = factorials(N)
    return sum(F[i+j]/(F[i]*F[j])*u**i*v**j
               for i in range(N) for j in range(N-i))


def Bminus(N, a, b):
    q = mp.exp(-2j*mp.pi/N)
    p = mp.mpc(1)
    total = p
    for k in range(N-1):
        p *= a-q**k*b
        total += p
    return total


def phi(N):
    return mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf(1)/4-(N+mp.mpf(1)/N)/12))


def log_minus(N, z):
    return mp.conj(log_full_psi(N, mp.conj(z)))


def T(N, u, v):
    h = 2j*mp.pi/N
    l, m = mp.log(u), mp.log(v)
    return phi(N)*mp.exp(-l*m/h+log_minus(N, l-h)+log_minus(N, m-h))


def finite_identities(N):
    Q = mp.exp(2j*mp.pi/N)
    u, v = mp.mpc('.7', '-.4'), mp.mpc('.4', '-.7')
    R = Rogers(N, u, v)
    reverse = v**(N-1)*Bminus(N, 1/v, u/(Q*v))
    D = 1-u**N-v**N
    errs = [R-reverse,
            (1-u)*R-v*Rogers(N, Q*u, v)-D,
            (1-v)*R-u*Rogers(N, u, Q*v)-D]
    F = factorials(N)
    pp = [mp.mpc(1)]
    mm = [mp.mpc(1)]
    for k in range(1, N):
        pp.append(pp[-1]*(-Q**(k-1))/(1-Q**k))
        mm.append(mm[-1]*Q/(1-Q**k))
    U, V = mp.mpc('-.3', '-.7'), mp.mpc('-.2', '-.8')
    C = sum(mm[i]*mm[j]*pp[N-1-i-j]*U**i*V**j
            for i in range(N) for j in range(N-i))
    errs.append(N*Q**(N-1)*C-Rogers(N, Q**2*U, Q**2*V))
    # Exact current-aware opposite-face pair, independent finite kernels.
    aa, cc, ww = mp.mpc('.6', '-.2'), mp.mpc('.5', '-.3'), mp.mpc('.8', '.1')
    def bp(a, b):
        product = mp.mpc(1)
        total = product
        for k in range(N-1):
            product *= a-Q**k*b
            total += product
        return total
    DB, DR = 1-aa**N+(aa*ww)**N, 1-cc**N-ww**N
    pair = bp(aa, aa*ww)*Rogers(N, cc, ww)
    shifted_pair = bp(aa, Q*aa*ww)*Rogers(N, cc, Q*ww)
    errs.append(pair-aa*cc*shifted_pair
                -DB*Rogers(N, cc, ww)-aa*DR*bp(aa, Q*aa*ww))
    assert max(abs(e) for e in errs) < mp.mpf('1e-45'), (N, errs)
    return {'N': N, 'order_reversal_error': float(abs(errs[0])),
            'two_original_Ward_errors': [float(abs(e)) for e in errs[1:3]],
            'two_minus_full_field_actual_tag_error': float(abs(errs[3])),
            'paired_current_sewing_Ward_error': float(abs(errs[4]))}


def barnes_plus(N, l, c):
    h = 2j*mp.pi/N
    eps = mp.mpf('.13')
    lp0 = log_full_psi(N, c)

    def integrand(y):
        a = -eps+1j*y
        if y >= 0:
            lh = 2j*mp.pi*a-mp.log(1-mp.exp(2j*mp.pi*a))
        else:
            lh = -mp.log(mp.exp(-2j*mp.pi*a)-1)
        return 1j*mp.exp(a*l+lp0-log_full_psi(N, c+h*a)+lh)

    return mp.quad(integrand, [-55, -16, -5, -1, 0, 1, 5, 16, 55])


def actual_opposite_current(N):
    h = 2j*mp.pi/N
    u, v = mp.mpc('.7', '-.4'), mp.mpc('.4', '-.7')
    l, m = mp.log(u), mp.log(v)
    # Conjugate of the ACTUAL downward opposite-root current, not a new contour.
    Ia = barnes_plus(N, mp.conj(-m), mp.conj(l-h))
    J = -mp.conj(Ia)/v
    RR = Rogers(N, u, v)
    TT = T(N, u, v)
    D = 1-u**N-v**N
    error = abs(RR-TT-D*J)
    assert error < mp.mpf('1e-30'), error
    plusform = (phi(N)*(1-u**N)*(1-v**N)
                *mp.exp(-l*m/h-log_full_psi(N, l)-log_full_psi(N, m)))
    normerr = abs(plusform/TT-1)
    assert normerr < mp.mpf('1e-45'), normerr
    return {'N': N, 'actual_conjugate_Barnes_current': str(J),
            'exact_source_decomposition_error': float(error),
            'retained_two_norm_factors_error': float(normerr)}


def balanced_fourier(N):
    Q = mp.exp(2j*mp.pi/N)
    u = mp.mpc('.6', '-.4')
    v = mp.exp(mp.log(1-u**N)/N-2j*mp.pi/N)
    RR = Rogers(N, u, v)
    pp = mp.mpc(1)
    bb = pp
    for k in range(N-1):
        pp *= 1/v-Q**k*u/v
        bb += pp
    expected = N*u**N/(1-v)
    e1, e2 = abs(RR*bb-expected), abs(T(N, u, v)/RR-1)
    assert max(e1, e2) < mp.mpf('1e-42'), (e1, e2)
    return {'N': N, 'balanced_Fourier_error': float(e1),
            'balanced_full_Psi_normalizer_error': float(e2)}


def symbolic_current():
    u, v = sp.symbols('u v')
    L = 1-u-v
    J0, J1 = 1/L, u*v/L**3
    assert sp.factor((1-u)*J0-v*J0-1) == 0
    assert sp.factor((1-u)*J1-v*(J1+u*sp.diff(J0, u))) == 0
    assert sp.factor((1-v)*J1-u*(J1+v*sp.diff(J0, v))) == 0
    return {'two_principal_symbol_orders': True, 'both_Ward_equations_compatible': True}


def main():
    mp.mp.dps = 65
    result = {'status': 'PASS',
              'original_finite_kernels': [finite_identities(N) for N in range(2, 13)],
              'actual_opposite_source_currents': [actual_opposite_current(N) for N in [3, 5]],
              'balanced_Fourier_sources': [balanced_fourier(N) for N in [3, 5, 9]],
              'rational_current_symbols': symbolic_current(),
              'scope': ('Exact ORIGINAL Rogers source and opposite-root Newton relative cycle; '
                        'no independent-sector or full-knot noncancellation assumed.')}
    Path(__file__).with_name('actual_rogers_sink_opposite_beta_source_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS eleven actual Rogers/order-reversal/tag families, two opposite Barnes '
          'source cycles, three balanced Fourier sources and both current Ward symbols')


if __name__ == '__main__':
    main()
