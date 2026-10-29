#!/usr/bin/env python3
"""Original odd black source: all-node one-leg Chu packet.

Finite-field checks are exact. Complex Barnes factorial and Laplace
checks are high-precision supplementary tests of the written proof.
"""
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_trivalent_complete_circle_vertex_kernel import vertex_formula
from audit_exact_factorial_interpolation import sine_factorial


def factorials(N, q, p):
    Q = q*q % p
    out = [1]
    for r in range(1, N):
        out.append(out[-1]*(1-pow(Q, r, p)) % p)
    return out


def columns(N, q, p):
    d, m, Q = N-1, (N-1)//2, q*q % p
    x = pow(q, d, p)
    E = np.diag([(pow(Q, -a, p)-1) % p for a in range(1, N)], 1)
    F = np.diag([(1-pow(Q, a, p)) % p for a in range(1, N)], -1)
    K = np.diag([x*pow(Q, -a, p) % p for a in range(N)])
    Et, Ft, Kt = coproduct(E, F, K, 2, N, p)
    fac = factorials(N, q, p)
    result = {}
    for j in range(m+1):
        t = d-j
        h = np.zeros(N*N, dtype=np.int64)
        for a in range(t+1):
            h[a*N+t-a] = pow(q, a*a, p)*fac[t]*pow(fac[a]*fac[t-a], -1, p) % p
        assert not np.any(Et@h % p)
        current = h.copy()
        central_lowest = None
        for r in range(1, (d if j == m else j)+1):
            current = Ft@current % p*pow(1-pow(Q, r, p), -1, p) % p
            if r == j:
                result[j] = (h.copy(), current.copy())
            if r == d:
                central_lowest = current.copy()
        if j == 0:
            result[j] = (h.copy(), h.copy())
        if j == m:
            assert central_lowest is not None
            result['lowest'] = central_lowest
    return result, Et, Ft, Kt, fac


def recoupling(N, q, p):
    d = N-1
    x = pow(q, d, p)
    fac = factorials(N, pow(q, -1, p), p)
    J = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        for b in range(N-a):
            J[a, b] = x*pow(-pow(q, -1, p), a+b, p)*fac[a+b]*pow(fac[a]*fac[b], -1, p) % p
    return J


def exact_case(N):
    p, eta, q, E, F, K, pivot, R, Ri = balanced_data(N)
    d, m, Q, x = N-1, (N-1)//2, q*q % p, pow(q, N-1, p)
    qb, imag = pow(q, -1, p), pow(eta, N, p)
    actual, Et, Ft, Kt, fac = columns(N, q, p)
    bar, Ebt, Fbt, Kbt, facb = columns(N, qb, p)
    J, Jb = recoupling(N, q, p), recoupling(N, qb, p)
    P = np.eye(N, dtype=np.int64)[::-1]
    assert np.array_equal(Jb@P % p@J % p, P)
    sine = [pow(imag, a, p)*pow(q, -a*(a+1)//2, p)*fac[a] % p for a in range(N)]
    ids = [a*N+d-a for a in range(N)]
    Z = {j: np.array([sine[j+k]*pow(sine[j-k]*sine[k]**2, -1, p) % p
                       for k in range(j+1)], dtype=np.int64) for j in range(m+1)}
    for j in range(m+1):
        f = pow(q, j*j, p)*actual[j][1][ids] % p
        fb = pow(qb, j*j, p)*bar[j][1][ids] % p
        expected = np.concatenate((np.zeros(d-j, dtype=np.int64), Z[j][::-1]))
        assert np.array_equal(J@f % p, expected)
        # Literal full-Cartan physical R eigenphase, including kappa.
        kappa = pow(eta, d*d, p)
        omega = kappa*(-1)**j*pow(q, j*(j+1), p) % p
        assert np.array_equal(R@actual[j][1] % p, omega*actual[j][1] % p)
        for k in range(j+1):
            got = sum(int(Z[j][i])*pow(-qb, i, p)*facb[i]*pow(facb[k]*facb[i-k], -1, p) for i in range(k, j+1)) % p
            target = (-1)**j*pow(q, k*k-j*(j+1), p)*int(Z[j][k]) % p
            assert got == target
        # Actual open trivalent kernel, at the specified three physical degrees.
        matrix = np.column_stack((bar['lowest'], bar[j][1], bar[m][0]))
        U, V, Vm = vertex_formula(N, x, p, [(3*m,m),(d,j),(m,m)], matrix)
        B = int(U[0, 1, 2])*pow(N, -3, p) % p
        pos = sum(int(Z[j][k])*int(Z[m][k]) for k in range(j+1)) % p
        assert B == pow(q, m*(2-3*m+2*j), p)*pos % p
        matrix_element = int(fb@(J@(pow(q,m*m,p)*actual[m][1][ids] % p) % p) % p)
        assert B == pow(q, j*j-4*m*m, p)*matrix_element % p
    for j in range(m+1):
        zj = np.pad(Z[j], (0, N-len(Z[j])))
        for ell in range(m+1):
            zl = np.pad(Z[ell], (0, N-len(Z[ell])))
            left = int(zj@(J@zl % p) % p)
            right = x*(-1)**(j+ell)*pow(q, -j*(j+1)-ell*(ell+1), p)
            right *= sum(int(Z[j][k])*int(Z[ell][k]) for k in range(min(j,ell)+1))
            assert left == right % p
    return {'N': N, 'prime': p, 'all_nodes': m+1,
            'literal_black_kernel_and_full_kappa': True,
            'real_tail_and_second_Chu_all_nodes': True,
            'all_bilinear_node_pairings': True,
            'original_white_and_marked_rows_not_identified': True}


def Jfun(t):
    t = mp.mpc(t)
    X = mp.exp(2j*mp.pi*t)
    return ((mp.polylog(2, 1)-mp.polylog(2, X))/(2j*mp.pi)
            -1j*mp.pi*(t*t-t)/2)


def phase(sigma):
    t = mp.atan(mp.cos(mp.pi*sigma))/mp.pi
    lam = mp.mpf('.5')-sigma
    return Jfun(lam+t)-Jfun(lam-t)-4*Jfun(t)-2*Jfun(mp.mpf('.5')-t)


def positive_profile(N):
    m = (N-1)//2
    sine = [mp.mpf(1)]
    for r in range(1, N):
        sine.append(sine[-1]*2*mp.sin(mp.pi*r/N))
    values = []
    previous = mp.mpf(0)
    for j in range(m+1):
        pos = sum(sine[j+k]/(sine[j-k]*sine[k]**2)*N/(sine[k]**2*sine[m-k]**2) for k in range(j+1))
        assert pos >= previous*(1-mp.mpf('1e-40'))
        previous = pos
        if j in {m, m-round(mp.mpf('.05')*N), m-round(mp.mpf('.15')*N)}:
            sigma = mp.mpf(m-j)/N
            scaled = 4*mp.sqrt(mp.cos(mp.pi*sigma))*N**mp.mpf('1.5')*mp.exp(-N*phase(sigma))*pos
            assert abs(scaled-1) < 2/N
            values.append({'deficit': m-j, 'normalized_Laplace_prefactor': float(mp.re(scaled)),
                           'scaled_N_error': float(N*abs(scaled-1))})
    return {'N': N, 'whole_physical_monotonicity': True, 'profiles': values}


def complex_window(N):
    m = (N-1)//2
    sigma = mp.mpc('.025', '.015')
    window = [k for k in range(m+1) if abs(mp.mpf(k)/N-mp.mpf('.25')) <= mp.mpf('.12')]
    sines = [mp.mpf(1)]
    for r in range(1, N):
        sines.append(sines[-1]*2*mp.sin(mp.pi*r/N))
    def packet(z):
        return N*sum(sine_factorial(N,m-N*z+k)/sine_factorial(N,m-N*z-k)/sines[k]**4/sines[m-k]**2 for k in window)
    actual = packet(sigma)
    reflected = packet(-sigma)
    symmetry = abs(actual/reflected-1)
    assert symmetry < mp.mpf('1e-36')
    predicted = N**mp.mpf('-1.5')*mp.exp(N*phase(sigma))/(4*mp.sqrt(mp.cos(mp.pi*sigma)))
    error = abs(actual/predicted-1)
    assert N*error < 4
    return {'N': N, 'exact_Barnes_window_evenness_error': float(symmetry),
            'complex_packet_scaled_N_error': float(N*error)}


def main():
    exact = [exact_case(N) for N in range(3, 22, 2)]
    with mp.workdps(50):
        profiles = [positive_profile(N) for N in (65,129,257)]
        complex_rows = [complex_window(N) for N in (33,65)]
    out = {'status': 'PASS', 'exact_original_all_node_source': exact,
           'positive_profile_calibration': profiles,
           'canonical_complex_factorial_window': complex_rows,
           'scope': 'One actual black magnetic coefficient, two central legs and arbitrary third retained node. No all-three-noncentral, all-magnetic, marked-white or sewn-graph survival theorem.'}
    Path(__file__).with_name('actual_trivalent_one_channel_source_packet_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {len(exact)} exact original all-node black-source families, 3 whole-color/Laplace profiles, 2 canonical complex windows')


if __name__ == '__main__':
    main()
