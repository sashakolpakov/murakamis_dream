#!/usr/bin/env python3
"""Original full crossing-circle reflection, positive CD weights and cap cost.

The complex test constructs every physical degree block from the literal
coproduct entries and compares a polynomial L_N with its positive CD sum.
The finite-field test independently retains the original mixed universal
crossings/pivot. No global augmented-source positivity is inferred.
"""

import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_crossing_circle_source_and_filling import (
    crossing_circle, ordinary_module,
)
from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_half_clock_source_dilation import original_factorial_R


def maxabs(A):
    return max((abs(z) for z in A), default=mp.mpf(0))


def omega_block(N, T):
    q = mp.exp(mp.pi*1j/N)
    Q, x = q*q, q**(N-1)
    O = mp.matrix(T+1)
    for u in range(T+1):
        v = T-u
        O[u, u] = ((Q**(-u)-1)*x*Q**(-v)*(1-Q**u)
                   +(Q**(-v)-1)/x*Q**u*(1-Q**v)
                   +q*x*x*Q**(-T)+q**(-1)*x**(-2)*Q**T)
        if u < T:
            O[u, u+1] = O[u+1, u] = Q**(-v)*(1-Q**v)*(1-Q**(u+1))
    return O


def circle_polynomial(O, j):
    a = mp.eye(O.rows)
    if j == 1:
        return a
    b = O.copy()
    for _ in range(2, j):
        a, b = b, O*b-a
    return (-1)**(j-1)*b


def canonical_value(O, c):
    v = mp.matrix(O.rows, 1)
    v[0] = 1
    if O.rows > 1:
        v[1] = (c-O[0, 0])/O[0, 1]
    for u in range(1, O.rows-1):
        v[u+1] = ((c-O[u, u])*v[u]-O[u, u-1]*v[u-1])/O[u, u+1]
    return v


def complex_case(N):
    mp.mp.dps = 90
    d = N-1
    q = mp.exp(mp.pi*1j/N)
    Q, x, rho = q*q, q**d, q-1/q
    s = [mp.mpf(1)]
    for a in range(1, N):
        s.append(s[-1]*abs(1-Q**a))
    R = original_factorial_R(N)
    block_rows, total_rank = [], 0
    for T in range(d+1):
        O = omega_block(N, T)
        P = mp.matrix(T+1)
        for u in range(T+1):
            P[u, T-u] = 1
        assert maxabs(P*O.conjugate()-O*P) < mp.mpf('1e-65')
        L = circle_polynomial(O, N)
        H, C = L*P, P*L
        assert maxabs(H-H.H) < mp.mpf('1e-55')*max(1, maxabs(H))
        resolution = mp.matrix(T+1)
        rank = 0
        for j in range(T+1):
            partner = d-j
            if j > partner or partner > T:
                continue
            c = q**(2*j+1)+q**(-2*j-1)
            v = canonical_value(O, c)
            nu = (-1)**j*q**(j*(j+1))
            assert maxabs(O*v-c*v) < mp.mpf('1e-60')*max(1, maxabs(v))
            assert abs(v[T]-x**T*nu) < mp.mpf('1e-60')*max(1, maxabs(v))
            assert maxabs(P*v.conjugate()-mp.conj(v[T])*v) < mp.mpf('1e-60')*max(1, maxabs(v))
            if j < partner:
                h = 2*s[T]**2/(s[T-j]*s[T+j-d])
                four = 2*N*N/(s[T-j]*s[T+j-d]*s[d-T]**2)
            else:
                h = s[T]**2/s[T-j]**2
                four = N*N/(s[T-j]**2*s[d-T]**2)
            assert h > 0
            assert abs(h-four) < mp.mpf('1e-60')*max(1, h)
            resolution += h*v*v.H
            rank += 1
        scale = max(1, maxabs(H))
        assert maxabs(H-resolution) < mp.mpf('1e-55')*scale
        corner = (s[T]**2*sum(1/(s[a]*s[2*T-d-a]) for a in range(2*T-d+1))
                  if 2*T >= d else mp.mpf(0))
        assert abs(H[0, 0]-corner) < mp.mpf('1e-55')*scale
        ids = [u*N+T-u for u in range(T+1)]
        ids_hi = [(d-T+u)*N+d-u for u in range(T+1)]
        # The original factorial R supplies BOTH signed same-pair twists.
        rb = R[np.ix_(ids, ids)]
        cb = np.array(C.tolist(), dtype=complex)
        for operator in (rb, np.linalg.inv(rb)):
            error = np.linalg.norm(operator.conj().T@cb@operator-cb)
            assert error < 3e-6*max(1., np.linalg.norm(cb))
        assert np.allclose(R[np.ix_(ids_hi, ids_hi)], rb, atol=1e-7, rtol=1e-7)
        for j in range(1, N+1):
            Lj = circle_polynomial(O, j)
            difference = j*j*C-Lj.H*C*Lj
            ndifference = np.array(difference.tolist(), dtype=complex)
            eig = np.linalg.eigvalsh((ndifference+ndifference.conj().T)/2)
            assert np.min(eig) > -1e-8*max(1., j*j*np.linalg.norm(cb))
            if math.gcd(j, N) == 1:
                lower = Lj.H*C*Lj-mp.mpf(4)/(N*N)*C
                nlower = np.array(lower.tolist(), dtype=complex)
                eig = np.linalg.eigvalsh((nlower+nlower.conj().T)/2)
                assert np.min(eig) > -1e-8*max(1., j*j*np.linalg.norm(cb))
        total_rank += rank*(1 if T == d else 2)
        if T == d:
            cup = mp.matrix([N*x**(u-d) for u in range(N)])
            ell = mp.matrix([[x**u/N for u in range(N)]])
            marked = mp.matrix([[x**(d-u)/N**2 for u in range(N)]])
            harmonic = [mp.mpc(0)]
            for a in range(1, N):
                harmonic.append(harmonic[-1]+1/(1-Q**a))
            mean = sum(harmonic)/N
            normal = mp.matrix([(-1)**(N+1)*N*rho*x**(u-d)*(harmonic[u]-mean)
                                for u in range(N)])
            assert abs((ell*normal)[0]-1) < mp.mpf('1e-65')
            assert abs((marked*cup)[0]-1) < mp.mpf('1e-65')
            assert maxabs(L*normal-2*N*cup) < mp.mpf('1e-60')
            assert maxabs(C*normal-2*N**3*ell.H) < mp.mpf('1e-60')
            assert maxabs(C*cup) < mp.mpf('1e-60')
            assert abs((normal.H*C*normal)[0]-2*N**3) < mp.mpf('1e-55')
            cap_remainder = np.array((C/(2*N**3)-ell.H*ell).tolist(), dtype=complex)
            eigen = np.linalg.eigvalsh((cap_remainder+cap_remainder.conj().T)/2)
            assert np.min(eigen) > -1e-8*max(1., np.linalg.norm(cap_remainder))
            # Positivity is isolated at complete color; every ordinary j<N
            # has the exact nonzero reflected cross-entry on the source plane.
            for j in range(1, N):
                Lj = circle_polynomial(O, j)
                lam = (-1)**(j-1)*mp.sin(mp.pi*j/N)/mp.sin(mp.pi/N)
                entry = (cup.H*P*Lj*normal)[0]
                assert abs(entry-N*N*lam) < mp.mpf('1e-55')*max(1, abs(entry))
                assert abs((cup.H*P*Lj*cup)[0]) < mp.mpf('1e-55')
        block_rows.append({'T': T, 'positive_rank': rank,
                           'complete_CD_positive_resolution': True,
                           'exact_positive_corner': str(mp.re(corner))})
    assert total_rank == ((N+1)//2)**2
    return {'N': N, 'full_physical_positive_rank': total_rank,
            'every_total_degree_including_high_mirror': block_rows,
            'original_cap_exact_dual_cost': f'1/{2*N**3}',
            'both_literal_signed_twist_isometries': True,
            'all_color_quotient_transmission_and_coprime_inverse': True,
            'ordinary_color_reflection_indefinite': True}


def literal_field_circle(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, rho = N-1, (q-pow(q, -1, p)) % p
    target = {'dim': N, 'E': E, 'F': F, 'K': K,
              'H': [d-2*a for a in range(N)]}
    actual = crossing_circle(target, ordinary_module(N, q, p), q, eta, p, N)
    Ec = rho*rho*E % p
    Et, Ft, Kt = coproduct(Ec, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    a, b = np.eye(N*N, dtype=np.int64), O.copy()
    if d == 0:
        expected = a
    elif d == 1:
        expected = -b % p
    else:
        for _ in range(2, d+1):
            a, b = b, (O@b-a) % p
        expected = pow(-1, d, p)*b % p
    assert np.array_equal(actual, expected)
    return {'N': N, 'literal_full_mixed_Cartan_and_pivotal_circle': True}


def lobachevsky(t):
    return mp.im(mp.polylog(2, mp.exp(2j*t)))/2


def profile_case(N):
    mp.mp.dps = 70
    d = N-1
    s = [mp.mpf(1)]
    for a in range(1, N):
        s.append(s[-1]*2*mp.sin(mp.pi*a/N))
    best, worst = -mp.inf, 0
    for T in range((d+1)//2, N):
        length = 2*T-d
        corner = s[T]**2*sum(1/(s[a]*s[length-a]) for a in range(length+1))
        tau = mp.mpf(T)/N
        predicted = N/mp.pi*(-2*lobachevsky(mp.pi*tau)
                              +2*lobachevsky(mp.pi*(tau-mp.mpf('.5'))))
        worst = max(worst, abs(mp.log(corner)-predicted)/mp.log(N))
        best = max(best, mp.log(corner))
    v8 = 8*lobachevsky(mp.pi/4)
    assert worst < 12
    assert abs(best-N*v8/(2*mp.pi)) < 12*mp.log(N)
    return {'N': N, 'uniform_corner_profile_log_error_ratio': float(worst),
            'maximum_corner_log': float(best),
            'calibrated_octahedral_rate': float(v8/(2*mp.pi))}


if __name__ == '__main__':
    results = {'status': 'PASS',
               'literal_mixed_circle': [literal_field_circle(N) for N in range(2, 8)],
               'complete_positive_CD_and_source': [complex_case(N) for N in range(2, 13)],
               'positive_corner_profiles': [profile_case(N) for N in (16, 32, 64, 128)],
               'scope': 'All-level local positive reflected circle/cap theorem; global FAL source identification and open color survival are not claimed.'}
    Path(__file__).with_name('actual_complete_circle_reflection_positive_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS 6 literal mixed circles; 11 all-degree reflected PSD/source/twist families; 4 positive corner profiles')
