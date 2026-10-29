#!/usr/bin/env python3
"""Original operator-valued Markov boundary quotient and Mellin-normal rays."""

import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_borel_regular_fusion import fusion
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_modular_dilog_circle import psi


def spectator_trace(A, N, pivot, prime):
    out = np.zeros((N*N, N*N), dtype=np.int64)
    for a, c, u, v in itertools.product(range(N), repeat=4):
        out[a*N+u, c*N+v] = sum(int(pivot[b])*int(A[(a*N+b)*N+u, (c*N+b)*N+v])
                                     for b in range(N)) % prime
    return out


def original_operator_case(N):
    H = HardyNetwork(N, 1)
    p, Q, d = H.p, H.Q, N-1
    C, Ci, *_ = fusion(N, p, Q, [H.x, H.x], [0, 0])
    U = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        for k in range(min(d-a, b)+1):
            U[(a+k)*N+b-k, a*N+b] = H.u[k]
    D = np.diag([H.diag[b] for a, b in itertools.product(range(N), repeat=2)])
    I = np.eye(N, dtype=np.int64)
    left = H.kappa*np.kron(C@D % p@U % p, I) % p
    right = np.kron(Ci, I)
    alpha = H.kappa*pow(H.x, -d, p) % p

    # Genuine noncommuting spectator coefficients, with two independent
    # normal Taylor coefficients. No source/intertwiner assumption on them.
    sources = []
    for normal in range(2):
        channels = []
        for k in range(N):
            channels.append(np.array([[(k+1)*(u+2)*(v+3)+(u==v)*(k+normal+2)**2
                                       +(normal+1)*(u==((v+1) % N))
                                       for v in range(N)] for u in range(N)], dtype=np.int64) % p)
        inserted = np.zeros((N**3, N**3), dtype=np.int64)
        for a, b in itertools.product(range(N), repeat=2):
            start = (a*N+b)*N
            inserted[start:start+N, start:start+N] = channels[b]
        actual = spectator_trace(left@inserted % p@right % p, N, H.pivot, p)
        expected = alpha*np.kron(I, channels[0]) % p
        assert np.array_equal(actual, expected)
        zero_pointing = inserted-np.kron(np.eye(N*N, dtype=np.int64), channels[0])
        assert not np.any(spectator_trace(left@zero_pointing % p@right % p, N, H.pivot, p))

        cup = np.zeros(N*N, dtype=np.int64)
        marked = np.zeros(N*N, dtype=np.int64)
        for a, b in itertools.product(range(N), repeat=2):
            if a+b == d:
                cup[a*N+b] = N*pow(H.x, -b, p) % p
            marked[a*N+b] = pow(H.x, b, p)*pow(N*N, -1, p) % p
        for exterior in [H.plus, H.minus, H.plus@H.plus % p]:
            assert int(marked@exterior % p@actual % p@cup % p) == int(marked@exterior % p@expected % p@cup % p)
        sources.append(True)
    return {'N': N, 'noncommuting_spectator_germ_coefficients': len(sources),
            'full_original_marked_exteriors_per_coefficient': 3,
            'zero_pointing_operator_cancellation': True}


def radial_normal(N, R, sigma=0, order=0, dps=50):
    with mp.workdps(dps):
        R, sigma = mp.mpf(R), mp.mpc(sigma)
        Q = mp.exp(2j*mp.pi/N)
        phi = mp.sqrt(N)*mp.exp(mp.j*mp.pi*(mp.mpf(1)/4-(N+mp.mpf(1)/N)/12))
        def integrand(t):
            if not t:
                return mp.mpf(0)
            amplitude = phi/N if t == 1 else psi(N, 1, mp.log(t))/(1-t**N)
            return amplitude*mp.exp(-sigma*mp.log(t))*(-mp.log(t))**order
        value = -N*Q**-1*mp.quad(integrand, [0, R/4, R/2, R])/(2j*mp.pi)
        return +value


def germ_case(N, R):
    mp.mp.dps = 55
    rho = 1/mp.log(mp.e*N)
    values = [radial_normal(N, R, rho*mp.exp(2j*mp.pi*j/4)) for j in range(4)]
    jets = [radial_normal(N, R, order=r) for r in range(3)]
    scale = mp.log(mp.e*N)
    observed = [abs(z)/(math.factorial(r)*scale**r) for r, z in enumerate(jets)]
    assert max(map(abs, values)) < 100
    assert max(observed) < 100
    # Independent work precision, including the singular logarithmic insertion.
    high = radial_normal(N, R, order=1, dps=75)
    assert abs(jets[1]-high)/max(1, abs(high)) < mp.mpf('1e-35')
    return {'N': N, 'R': R, 'normal_disk_radius': mp.nstr(rho, 16),
            'disk_sample_max': mp.nstr(max(map(abs, values)), 16),
            'scaled_logarithmic_jets_0_1_2': [mp.nstr(z, 16) for z in observed],
            'original_ray_pointing': mp.nstr(jets[0], 20)}


def radius_one_normal_coefficients(N):
    mp.mp.dps = 60
    coefficients = [radial_normal(N, '1', order=r, dps=60)/math.factorial(r) for r in range(5)]
    bound = mp.mpf(N)/(2*mp.pi)
    assert all(abs(c) <= bound for c in coefficients)
    Q = mp.exp(2j*mp.pi/N)
    phi = mp.sqrt(N)*mp.exp(mp.j*mp.pi*(mp.mpf(1)/4-(N+mp.mpf(1)/N)/12))
    sigma = 1-mp.mpf('1e-7')
    def remainder(t):
        if not t:
            return mp.mpf(0)
        amplitude = phi/N if t == 1 else psi(N, 1, mp.log(t))/(1-t**N)
        return (amplitude-1)*mp.exp(-sigma*mp.log(t))
    # Analytic subtraction fixes the first Mellin pole without a numerical
    # quadrature of t^(-1+epsilon) at zero.
    scalar = (1/(1-sigma)+mp.quad(remainder, [0, mp.mpf('.25'), mp.mpf('.5'), 1]))/(2j*mp.pi)
    residue = (sigma-1)*scalar
    assert abs(residue+1/(2j*mp.pi)) < mp.mpf('1e-5')
    return {'N': N, 'R': 1,
            'all_orders_0_through_4_below_exact_bound': True,
            'normalized_pointed_coefficient_moduli': [mp.nstr(abs(c), 18) for c in coefficients],
            'exact_uniform_bound': mp.nstr(bound, 18),
            'first_Mellin_residue_approx': mp.nstr(residue, 18)}


if __name__ == '__main__':
    result = {'status': 'PASS',
              'original_operator_valued_source': [original_operator_case(N) for N in range(2, 7)],
              'actual_full_Psi_normal_germs': [germ_case(N, R) for N in [4, 8, 16] for R in ['.25', '.5']],
              'norm_one_seam_and_first_Mellin_residue': [radius_one_normal_coefficients(N) for N in [4, 8]],
              'scope': 'Visible positive normalization cells and their forests, not arbitrary internal alias/cap currents.'}
    Path(__file__).with_name('actual_normalization_boundary_current_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 5 operator-valued original source levels, 30 marked exteriors, 6 full-Psi normal germs')
