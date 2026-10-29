#!/usr/bin/env python3
"""Full physical alias, monic spectral ellipse, all-color gap constants."""

import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pretzel_complete_base_casimir_polynomial import rotate_box, matrix_value
from audit_actual_pretzel_cusp_color_two_band_bound import continuants
from diagnose_pretzel_coherent_radial_capacity import lobachevsky


def monic_polynomials(q, N, p):
    Q = q*q % p
    ps = [[1]]
    previous = [0]
    for l in range((N-1)//2):
        D = (4*q*pow(Q, l, p)-q*(1+Q)*pow(Q, 2*l, p)) % p
        a = -(1-pow(Q, l, p))**2 % p
        out = [0]*(l+2)
        for k, value in enumerate(ps[-1]):
            out[k] = (out[k]-D*value) % p
            out[k+1] = (out[k+1]+value) % p
        for k, value in enumerate(previous):
            out[k] = (out[k]-a*a*value) % p
        previous = ps[-1]
        ps.append(out)
    return ps


def field_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x = N-1, q*q % p, int(K[0, 0])
    qi, Qi = pow(q, -1, p), pow(Q, -1, p)
    M = d//2
    imaginary = pow(eta, N, p)
    fac, sine = [1], [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
        sine.append(pow(imaginary, a, p)*pow(q, -a*(a+1)//2, p)*fac[a] % p)
    Abar = np.diag([(4*qi*pow(Qi, u, p)-qi*(1+Qi)*pow(Qi, 2*u, p)) % p
                    for u in range(N)]).astype(np.int64)
    for u in range(N-1):
        Abar[u, u+1] = Abar[u+1, u] = -(1-pow(Qi, u+1, p))**2 % p
    fsbar = continuants(Abar, p)
    psbar = monic_polynomials(qi, N, p)
    rho = (q-qi) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+qi*Ki) % p
    Us = [np.eye(N*N, dtype=np.int64), O.copy()]
    for n in range(2, N):
        Us.append((O@Us[-1]-Us[-2]) % p)
    count = 0
    for h in range(1, N//2+1):
        literal = [0]*h
        monic = [0]*h
        for t in range(1, h+1):
            beta = (pow(-1, N-t-h, p)*sine[t-1]**2*sine[t+h-1]
                    *pow(sine[2*t-1]*sine[h-t] % p, -1, p)) % p
            for k, value in enumerate(fsbar[t-1]):
                literal[k] = (literal[k]+beta*value) % p
        for l in range(h):
            gaussian = fac[h+l]*pow(fac[2*l+1]*fac[h-l-1] % p, -1, p) % p
            phase = (pow(-1, l, p)*pow(q, 3*l*l+4*l+1-2*h*l-h, p)*gaussian) % p
            for k, value in enumerate(psbar[l]):
                monic[k] = (monic[k]+phase*value) % p
        assert monic == [pow(-1, N+h-1, p)*v % p for v in literal]
        Lj = pow(-1, h-1, p)*Us[h-1] % p
        actual = rotate_box(Rm@Lj % p, N, x, p)
        expected = pow(-1, N, p)*Rp@matrix_value(literal, O, p) % p
        assert np.array_equal(actual, expected)
        count += 1
    return {'N': N, 'all_input_small_color_alias_and_monic_phase_cases': count,
            'even_middle_color_included': N % 2 == 0}


def exact_ellipse_certificate():
    y = sp.symbols('y', real=True)
    slack = sp.expand((81-y**4)**2-36*(9-y*y)**2-36*(2*y-y*y)*(9+y*y)**2)
    p1 = y**4+12*y*y-36*y+27
    p2 = y**4+24*y*y-36*y+135
    assert sp.factor(slack-p1*p2) == 0
    assert sp.expand(p1-((y-1)**2*(y*y+2*y+3)
                         +12*(y-sp.Rational(4, 3))**2+sp.Rational(8, 3))) == 0
    assert sp.expand(p2-(y**4+24*(y-sp.Rational(3, 4))**2+sp.Rational(243, 2))) == 0
    return {'radius_six_ellipse_slack': True, 'strict_positive_squares': True}


def opnorm(A):
    B = A.H*A
    tr = mp.re(B[0, 0]+B[1, 1])
    det = mp.re(B[0, 0]*B[1, 1]-B[0, 1]*B[1, 0])
    return mp.sqrt((tr+mp.sqrt(max(0, tr*tr-4*det)))/2)


def frozen_cases():
    mp.mp.dps = 80
    count, maximum = 0, mp.mpf(0)
    for t in (mp.mpf(0), mp.mpf('.01'), mp.mpf('.1'), mp.mpf('.2'), mp.mpf('.25'),
              mp.mpf('.3'), mp.mpf('.4'), mp.mpf('.49'), mp.mpf('.5')):
        u, V = mp.pi*t, mp.exp(2j*mp.pi*t)
        a = 4*mp.sin(u)**2
        for z in (-2, mp.mpf('-1.5'), -1, 0, 1, 2):
            d = z/V-4+2*V
            root = mp.sqrt(d*d-4*a*a)
            radius = max(abs((d+root)/2), abs((d-root)/2))
            assert radius < 6
            maximum = max(maximum, radius)
            A = mp.matrix([[z-4*V+2*V*V, -V*V*a*a], [1, 0]])/6
            for L in (1, 4, 16):
                assert opnorm(A**L) <= L*opnorm(A)+L-1+mp.mpf('1e-55')
            count += 1
    return {'frozen_parameter_and_Cayley_Hamilton_cases': count,
            'largest_sampled_root_modulus': mp.nstr(maximum, 25),
            'proof_is_the_exact_ellipse_certificate_not_the_grid': True}


def exact_binomial_and_width_threshold():
    values = [1, 8]
    for n in range(2, 45):
        values.append(8*values[-1]-values[-2])
    for h in range(1, 45):
        assert sum(math.comb(h+l, 2*l+1)*6**l for l in range(h)) == values[h-1]
    G = sum((Fraction((-1)**k, (2*k+1)**2) for k in range(6)), Fraction(0))
    pi_upper = Fraction(22, 7)
    cos_lower = 1-(pi_upper/25)**2/2
    margin = 4*G/pi_upper-Fraction(31, 30)-pi_upper/(25*cos_lower)
    assert margin > 0
    exp_lower = sum((Fraction(31, 15)**k/math.factorial(k) for k in range(10)), Fraction(0))
    assert exp_lower > 4 and (exp_lower-4)**2 > 15
    mp.mp.dps = 65
    B = mp.log(4+mp.sqrt(15))/2
    j0 = 8*lobachevsky(mp.pi/4)/mp.pi
    widths = []
    for s in (25, 27, 29, 35, 51, 101):
        A = 4*s/mp.pi*(lobachevsky(mp.pi/4+mp.pi/(2*s))
                       +lobachevsky(mp.pi/4-mp.pi/(2*s)))
        gap = A-(s-1)*j0-B
        assert gap > 0
        widths.append({'s': s, 'complete_geometric_rate': float(A),
                       'global_alias_source_gap': float(gap)})
    return {'exact_binomial_Chebyshev_identities': 44,
            'B': float(B), 'j0': float(j0),
            'rigorous_rational_lower_margin_for_all_s_ge_25': str(margin),
            'width_rate_diagnostics': widths}


def alias_norm_diagnostic(N):
    mp.mp.dps = max(160, 2*N)
    d, h = N-1, (N-1)//2
    q, Q = mp.exp(mp.pi*1j/N), mp.exp(2*mp.pi*1j/N)
    sine = [mp.mpf(1)]
    for a in range(1, N):
        sine.append(sine[-1]*2*mp.sin(mp.pi*a/N))
    beta = [(-1)**(N-t-h)*sine[t-1]**2*sine[t+h-1]
            /(sine[2*t-1]*sine[h-t]) for t in range(1, h+1)]
    diag = [mp.conj(4*q*Q**u-q*(1+Q)*Q**(2*u)) for u in range(h)]
    off = [mp.conj(-(1-Q**(u+1))**2) for u in range(h)]
    norm, best = mp.mpf(0), None
    for j in range(N//2+N % 2):
        c = 2*mp.cos((2*j+1)*mp.pi/N)
        old, value, old_prime, derivative = mp.mpc(0), mp.mpc(1), mp.mpc(0), mp.mpc(0)
        P, Pprime = mp.mpc(0), mp.mpc(0)
        for l in range(h):
            P += beta[l]*value
            Pprime += beta[l]*derivative
            nxt = ((c-diag[l])*value-(off[l-1]*old if l else 0))/off[l]
            nxt_prime = (value+(c-diag[l])*derivative
                         -(off[l-1]*old_prime if l else 0))/off[l]
            old, value, old_prime, derivative = value, nxt, derivative, nxt_prime
        if 2*j == d:
            candidate = abs(P)
        else:
            w = q**(2*j+1)
            Rlogprime = -(d-2*j)/(2*(w-1/w))
            candidate = abs(P)+abs(Pprime+Rlogprime*P)/(N*N)
        if candidate > norm:
            norm, best = candidate, j
    return {'N': N, 'h': h, 'dps': mp.mp.dps,
            'exact_full_normal_alias_log_norm_over_N': float(mp.log(norm)/N),
            'largest_node_index': best,
            'proved_uniform_asymptotic_upper': float(mp.log(4+mp.sqrt(15))/2),
            'scope': 'Finite diagnostic; no sharp alias limit inferred.'}


if __name__ == '__main__':
    fields = [field_case(N) for N in range(2, 11)]
    ellipse = exact_ellipse_certificate()
    frozen = frozen_cases()
    widths = exact_binomial_and_width_threshold()
    norms = [alias_norm_diagnostic(N) for N in (32, 33, 64, 65, 128, 129)]
    Path(__file__).with_name('actual_pretzel_global_alias_and_colored_source_gap_results.json').write_text(
        json.dumps({'status': 'PASS', 'literal_physical_alias_and_monic_identities': fields,
                    'exact_ellipse': ellipse, 'frozen_block_cases': frozen,
                    'exact_Chebyshev_and_global_width_threshold': widths,
                    'actual_retained_normal_alias_norms': norms,
                    'scope': 'Global full-normal alias upper and entire original color-cube off-cusp gap for odd s>=25. No fixed-filling survival or peripheral identification inferred.'}, indent=2)+'\n')
    print('PASS 9 full physical alias/monic families including every even middle color; exact radius-6 ellipse; 54 frozen-block families; 44 exact binomial identities; rational all-width gap; 6 actual full-normal alias diagnostics')
