#!/usr/bin/env python3
"""Exact Bell one-power weights and canonical actual-source Grams."""

import json
from itertools import product
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_half_clock_source_dilation import original_factorial_R


def source(N, sigma, u, v):
    Q = mp.exp(2*mp.pi*1j*sigma/N)
    P, L, F = [], [], mp.mpc(1)
    numerator = mp.mpc(1)
    for a in range(N):
        if a:
            F *= 1-u*Q**a
            numerator *= 1-u*Q**(a-1)
        P.append(v**a/F)
        L.append(v**(-a)*numerator)
    return P, L, F


def coefficient(P, s, r):
    N = len(P)
    Q = mp.exp(2*mp.pi*1j/N)
    return mp.fsum(Q**(-r*a)*P[a]*mp.conj(P[(s-a) % N])
                   for a in range(N))/mp.sqrt(N)


def metric_check(N, sigma, u, v):
    P, L, _ = source(N, sigma, u, v)
    Q = mp.exp(2*mp.pi*1j*sigma/N)
    H = [abs(L[a])/abs(P[a]) for a in range(N)]
    S = mp.fsum(abs(L[a]*P[a]) for a in range(N))
    exact = abs(1-u)*mp.fsum(1/abs(1-u*Q**a) for a in range(N))
    assert abs(S-exact)/max(1, S) < mp.mpf('1e-60')
    assert abs(mp.fsum(abs(P[a])**2*H[a] for a in range(N))-S)/max(1, S) < mp.mpf('1e-60')
    assert abs(mp.fsum(abs(L[a])**2/H[a] for a in range(N))-S)/max(1, S) < mp.mpf('1e-60')
    bound = 2*N*N*max(1, abs(u)**N)/abs(1-u**N)
    assert S <= bound
    qs = mp.exp(mp.pi*1j*sigma/N)
    Pp, Lp, _ = source(N, sigma, 1/mp.conj(u), qs**-1*mp.conj(v)/mp.conj(u))
    for a in range(N):
        assert abs((abs(Lp[a])/abs(Pp[a]))/H[a]-1) < mp.mpf('1e-60')
    return S


def profile_case(N, kind):
    if kind == 'fixed_center':
        U = mp.mpc('.3', '.8')
    else:
        radius = mp.mpf('.55') if kind == 'small_fixed_radius' else mp.mpf('1.7')
        U = radius**N*mp.exp(mp.mpf('.7')*1j)
    u, v = mp.exp(mp.log(U)/N), mp.exp(mp.log(1-U)/N)
    P, L, _ = source(N, -1, u, v)
    Q = mp.exp(2*mp.pi*1j/N)
    t, aa = v/mp.conj(v), mp.conj(u)/u
    A = lambda j: abs(1-t*Q**(-j))
    B = lambda j: abs(1-aa*Q**j)
    C = lambda j: abs(1-aa*t*Q**j)
    Ap, Bp, Cp = [mp.mpf(1)], [mp.mpf(1)], {0: mp.mpf(1)}
    for j in range(1, N):
        Ap.append(Ap[-1]*A(j-1))
        Bp.append(Bp[-1]*B(j))
        Cp[j] = Cp[j-1]*C(j)
        Cp[-j] = Cp[-j+1]/C(-j+1)
    f = [[abs(u)**(-r)*abs(v)**s*Ap[r]*Cp[s-r]/Bp[s]
          for r in range(N)] for s in range(N)]
    normP2 = mp.fsum(abs(p)**2 for p in P)
    kappa = normP2/mp.sqrt(mp.fsum(x*x for row in f for x in row))
    c00 = coefficient(P, 0, 0)
    assert mp.re(c00) > 0 and abs(mp.im(c00)) < mp.mpf('1e-60')*max(1, abs(c00))
    assert abs(kappa-c00)/max(1, kappa) < mp.mpf('1e-60')
    alpha, beta = mp.arg(U)/mp.pi, -mp.arg(1-U)/mp.pi
    gamma = alpha+beta
    assert 0 < alpha < 1 and 0 < beta < 1 and 0 < gamma < 1
    shifts = [-beta, -alpha, gamma-1]
    T = []
    for shift in shifts:
        values = [mp.mpf(1)]
        for j in range(1, N+1):
            values.append(values[-1]*2*mp.sin(mp.pi*(j+shift)/N))
        T.append(values)
    Afull, Cfull = abs(1-t**N), abs(1-(aa*t)**N)
    worst = mp.mpf(0)
    for s, r in product(range(N), repeat=2):
        third = r-s if r > s else N-s+r
        factor = Afull if r > s else Afull*Cfull
        shifted = factor*abs(u)**(-r)*abs(v)**s/(T[0][N-r]*T[1][s]*T[2][third])
        err = abs(shifted/f[s][r]-1)
        worst = max(worst, err)
        assert err < mp.mpf('1e-60')
    selected = {(0, 0), (N-1, 0), (0, N-1), (N-1, N-1), (N//3, 2*N//3)}
    for s, r in selected:
        actual = abs(coefficient(P, s, r))
        assert abs(actual-kappa*f[s][r])/max(1, actual) < mp.mpf('1e-60')
    S = metric_check(N, -1, u, v)
    return {'N': N, 'regime': kind, 'clock_radius': mp.nstr(abs(u), 12),
            'Frobenius_center_modulus': mp.nstr(abs(U), 12),
            'exact_kappa': mp.nstr(kappa, 20),
            'maximum_shifted_factorization_error': mp.nstr(worst, 8),
            'balanced_source_norm_squared': mp.nstr(S, 20)}


def cap(N, j, epsilon):
    q, Q = mp.exp(mp.pi*1j/N), mp.exp(2*mp.pi*1j/N)
    u = Q**(-j)*mp.exp(mp.log(1-epsilon)/N)
    v = mp.exp(mp.log(epsilon)/N)
    P, L, _ = source(N, 1, u, v)
    roots = [mp.mpc(1)]
    for a in range(1, N):
        roots.append(roots[-1]*(1-Q**a))
    gp = v**(N-j)/roots[N-j] if j else 1
    gl = v**j/(N/roots[N-1-j]) if j else 1
    Ph, Lh = [gp*p for p in P], [gl*l for l in L]
    H = [abs(Lh[a])/abs(Ph[a]) for a in range(N)]
    cost = mp.fsum(abs(Ph[a]*Lh[a]) for a in range(N))
    assert cost <= 8*(1+abs(epsilon)*(1+mp.log(N)))
    return Ph, Lh, H, cost


def actual_crossing_cauchy(N, sign):
    epsilon1, epsilon2 = mp.mpc('.03', '.01'), mp.mpc('.017', '-.007')
    inputs = [cap(N, j, epsilon1) for j in [N-1, 0]]
    outputs = [cap(N, j, epsilon2) for j in [0, N-1]]
    P = np.kron(*[np.array([complex(x) for x in item[0]]) for item in inputs])
    L = np.kron(*[np.array([complex(x) for x in item[1]]) for item in outputs])
    Hi = np.kron(*[np.array([float(x) for x in item[2]]) for item in inputs])
    Ho = np.kron(*[np.array([float(x) for x in item[2]]) for item in outputs])
    R = original_factorial_R(N)
    if sign < 0:
        R = np.linalg.inv(R)
    weighted = np.sqrt(Ho)[:, None]*R/np.sqrt(Hi)[None, :]
    operator = np.linalg.svd(weighted, compute_uv=False)[0]
    source_cost = np.sqrt(float(mp.fprod(item[3] for item in inputs+outputs)))
    amplitude = abs(L@R@P)
    assert amplitude <= source_cost*operator*(1+1e-9)
    return {'N': N, 'sign': sign, 'literal_original_Cartan_crossing': True,
            'actual_cap_source_cost': source_cost,
            'weighted_interior_operator_norm': float(operator),
            'amplitude': float(amplitude)}


def current_case(N):
    Q = mp.exp(2*mp.pi*1j/N)
    u, v = mp.mpf('.81')*mp.exp(mp.mpf('.23')*1j), mp.mpf('1.07')*mp.exp(-mp.mpf('.17')*1j)
    P, _, Fd = source(N, -1, u, v)
    Delta = 1-u**N-v**N
    c = [[coefficient(P, s, r) for r in range(N)] for s in range(N)]
    t = v/mp.conj(v)
    for s, r in product(range(N), repeat=2):
        h = Delta/Fd*mp.conj(P[s])/mp.sqrt(N)
        k = mp.conj(Delta/Fd)*Q**(-r*s)*P[s]/mp.sqrt(N)
        left1 = c[s][r]-u*c[s][(r+1) % N]-v*Q**(-r)*c[(s-1) % N][r]
        left2 = c[s][r]-mp.conj(u)*Q**s*c[s][(r+1) % N]-mp.conj(v)*c[(s-1) % N][r]
        assert abs(left1-h)/max(1, abs(h)) < mp.mpf('1e-60')
        assert abs(left2-k)/max(1, abs(k)) < mp.mpf('1e-60')
        elimination = ((u-t*mp.conj(u)*Q**(s-r))*c[s][(r+1) % N]
                       -(1-t*Q**(-r))*c[s][r]+h-t*Q**(-r)*k)
        assert abs(elimination)/max(1, abs(h), abs(k)) < mp.mpf('1e-60')
    metric_check(N, -1, u, v)
    return {'N': N, 'both_off_Fermat_source_currents_retained': True}


def main():
    mp.mp.dps = 180
    cap_count = 0
    for N in range(2, 21):
        for j in range(N):
            for epsilon in [mp.mpc('.03', '.01'), mp.exp(-N)*(1+mp.j/5)]:
                _, _, _, value = cap(N, j, epsilon)
                if abs(epsilon) < mp.mpf('1e-6'):
                    assert abs(value-1) < 10*abs(epsilon)*(1+mp.log(N))
                cap_count += 1
    data = {'status': 'PASS',
            'Bell_weight_profiles': [profile_case(N, kind) for N in [3, 7, 16, 32, 64]
                                     for kind in ['fixed_center', 'small_fixed_radius', 'large_fixed_radius']],
            'actual_normalized_cap_cases': cap_count,
            'original_crossing_Cauchy': [actual_crossing_cauchy(N, sign) for N in [2, 3, 4, 5]
                                        for sign in [1, -1]],
            'off_Fermat_currents': [current_case(N) for N in range(2, 9)],
            'scope': ('Exact local weights and actual boundary source costs; '
                      'no sharp bound for the interior original word or global angle projector.')}
    Path(__file__).with_name('phase_ratio_bell_weights_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print('PASS',len(data['Bell_weight_profiles']),'exact Bell weight profiles;',cap_count,
          'actual cap source Grams;',len(data['original_crossing_Cauchy']),
          'original signed crossing Cauchy bounds;',len(data['off_Fermat_currents']),'full currents')


if __name__ == '__main__':
    main()
