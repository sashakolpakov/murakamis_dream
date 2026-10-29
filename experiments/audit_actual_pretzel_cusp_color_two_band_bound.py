#!/usr/bin/env python3
"""All-input cusp-color two-band source and its retained normal remainder."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pretzel_complete_base_casimir_polynomial import (
    rotate_box, polyadd, polymul, matrix_value,
)
from diagnose_pretzel_coherent_radial_capacity import evaluate


def continuants(A, p):
    n = len(A)
    f = [[1]]
    if n > 1:
        f.append([-int(A[0, 0])*pow(int(A[0, 1]), -1, p) % p,
                  pow(int(A[0, 1]), -1, p)])
    for u in range(1, n-1):
        numerator = polyadd(polymul([-int(A[u, u]), 1], f[u], p),
                            [-int(A[u, u-1])*z for z in f[u-1]], p)
        f.append([z*pow(int(A[u, u+1]), -1, p) % p for z in numerator])
    return f


def gaussians(n, Q, p):
    row = [1]
    for m in range(n):
        row = [(row[k] if k < len(row) else 0)
               +(pow(Q, m+1-k, p)*row[k-1] if k else 0)
               for k in range(m+2)]
        row = [z % p for z in row]
    return row


def field_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x, kappa = N-1, q*q % p, int(K[0, 0]), int(Rp[0, 0])
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    ids = [u*N+d-u for u in range(N)]
    A = O[np.ix_(ids, ids)]
    f, backward = continuants(A, p), continuants(A[::-1, ::-1], p)
    fd = matrix_value(f[-1], O, p)
    assert np.array_equal(fd, pow(x, d, p)*pow(kappa, -1, p)*Rp % p)
    for l in range(N):
        assert np.array_equal(fd@matrix_value(backward[l], O, p) % p,
                              matrix_value(f[d-l], O, p))
    imaginary, fac, sine = pow(eta, N, p), [1], [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
        sine.append(pow(imaginary, a, p)*pow(q, -a*(a+1)//2, p)*fac[a] % p)
    Us = [np.eye(N*N, dtype=np.int64), O.copy()]
    for n in range(2, N):
        Us.append((O@Us[-1]-Us[-2]) % p)
    rows = []
    for r in range(d//2+1):
        j = N-r
        Lj = pow(-1, j-1, p)*Us[j-1] % p
        actual = rotate_box(Rm@Lj % p, N, x, p)
        middle = actual[np.ix_(ids, ids)]
        direct_coeff = []
        for v in range(N):
            k = v-r
            gaussian = gaussians(2*v, Q, p)[k] if 0 <= k <= 2*v else 0
            coefficient = sine[d-v]**2*pow(q, r*r-v*v, p)*gaussian % p
            direct_coeff.append(coefficient)
            assert int(middle[0, v]) == pow(kappa, -1, p)*coefficient % p
        core = [0]*N
        for v in range(r, d//2+1):
            coefficient = (sine[d-v]**2*sine[2*v]
                           *pow(sine[v-r]*sine[v+r] % p, -1, p)) % p
            assert coefficient == direct_coeff[v]
            for k, z in enumerate(f[v]):
                core[k] = (core[k]+pow(kappa, -1, p)*coefficient*z) % p
        short = [0]*max(1, r)
        for t in range(1, r+1):
            coefficient = (pow(-1, N-t-r, p)*sine[t-1]**2*sine[t+r-1]
                           *pow(sine[2*t-1]*sine[r-t] % p, -1, p)) % p
            assert coefficient == direct_coeff[N-t]
            for k, z in enumerate(backward[t-1]):
                short[k] = (short[k]+coefficient*z) % p
        for v in range(N):
            if not (r <= v <= d//2 or N-r <= v <= d):
                assert direct_coeff[v] == 0
        expected = (matrix_value(core, O, p)+Rp@matrix_value(short, O, p)) % p
        assert np.array_equal(actual, expected)
        if r == 1:
            assert np.array_equal(Rp@matrix_value(short, O, p) % p,
                                  pow(-1, N, p)*Rp % p)
        rows.append({'cusp_distance': r, 'actual_auxiliary_color': j,
                     'full_physical_two_band_and_original_R_remainder': True})
    return {'N': N, 'all_cusp_colors': rows,
            'entire_reflected_continuant_identity_with_all_normal_coefficients': True}


def complex_norm_case(N):
    mp.mp.dps = 85
    d, q = N-1, mp.exp(mp.pi*1j/N)
    Q, x = q*q, q**d
    sine = [mp.mpf(1)]
    for a in range(1, N):
        sine.append(sine[-1]*2*mp.sin(mp.pi*a/N))
    # These are MONIC reversed continuants: denominators are cancelled
    # before bounding/evaluating the cusp remainder.
    D = [mp.conj(q+1/q-q*(1-Q**u)**2-(1-Q**(u+1))**2/q) for u in range(N)]
    off = [mp.conj(-(1-Q**(u+1))**2) for u in range(N)]
    polynomials = [[mp.mpc(1)]]
    if d:
        polynomials.append([-D[0], mp.mpc(1)])
    for l in range(1, d):
        out = [mp.mpc(0)]*(l+2)
        for k, a in enumerate(polynomials[l]):
            out[k] -= D[l]*a
            out[k+1] += a
        for k, a in enumerate(polynomials[l-1]):
            out[k] -= off[l-1]**2*a
        polynomials.append(out)
    norms = []
    for r in range(1, d//2+1):
        short = [mp.mpc(0)]*r
        for t in range(1, r+1):
            B = mp.fprod(off[:t-1])
            coefficient = ((-1)**(N-t-r)*sine[t-1]**2*sine[t+r-1]
                           /(sine[2*t-1]*sine[r-t]))
            ratio = sine[t+r-1]/(sine[2*t-1]*sine[r-t])
            assert ratio <= 4**r*(1+mp.mpf('1e-60'))
            for k, z in enumerate(polynomials[t-1]):
                short[k] += coefficient*z/B
        norm = mp.mpf(0)
        for j in range((d+2)//2):
            c = q**(2*j+1)+q**(-2*j-1)
            P, Pprime = evaluate(short, c)
            nu = (-1)**j*q**(j*(j+1))
            if 2*j == d:
                value = abs(P)
            else:
                logarithmic = -(d-2*j)/(2*(q**(2*j+1)-q**(-2*j-1)))
                value = abs(P)+abs(Pprime+logarithmic*P)/(N*N)
            norm = max(norm, value)
        assert norm <= 56**r
        norms.append({'r': r, 'actual_remainder_Hermite_norm': float(norm),
                      'proved_uniform_upper': str(56**r)})
    return {'N': N, 'all_retained_normal_source_norms': norms}


if __name__ == '__main__':
    results = {'status': 'PASS', 'entire_physical_source_identities': [field_case(N) for N in range(2, 11)],
               'uniform_normal_source_norm_checks': [complex_norm_case(N) for N in (4, 5, 8, 9, 12, 16, 24)],
               'scope': 'Exact actual cusp-source split and C^r remainder; no claim of negligible whole-period error or geometric survival.'}
    Path(__file__).with_name('actual_pretzel_cusp_color_two_band_bound_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS 9 complete physical cusp-corridor splits with all normal data; 7 uniform Hermite source-norm families')
