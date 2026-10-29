#!/usr/bin/env python3
"""Original coherent T2 interaction, Ward/current identities and rate calibration."""
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data


def field_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q = N-1, q*q % prime
    kappa = pow(eta, d*d, prime)
    f = [1]
    for i in range(1, N):
        f.append(f[-1]*(1-pow(Q, i, prime)) % prime)
    T = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(i+1):
            nu = (-1)**j*pow(Q, j*(j+1)//2, prime) % prime
            T[i, j] = (kappa*nu*pow(-q, i-j, prime)*f[i]
                       *pow(f[j]*f[i-j] % prime, -1, prime)) % prime
    T2 = T@T % prime
    P = np.eye(N, dtype=np.int64)[::-1].copy()
    actual = T2@P@T2[:, 0] % prime
    h, hb, jv, jb = [1], [1], [0], [0]
    W = []
    for i in range(N):
        value = sum((-1)**j*pow(Q, (3*j*j+j)//2, prime)
                    *pow(f[j]**3*f[i-j] % prime, -1, prime)
                    for j in range(i+1)) % prime
        w = f[i]**2*value % prime
        W.append(w)
        target = pow(kappa, 4, prime)*N*pow(-q, i+d, prime)*w % prime
        assert int(actual[i]) == target
        if i:
            for root, out, second in ((Q, h, jv), (pow(Q, -1, prime), hb, jb)):
                a = (1+root-3*pow(root, i, prime)) % prime
                b = root*pow(1-pow(root, i-1, prime), 3, prime) % prime
                out.append((a*out[-1]-(b*out[-2] if i > 1 else 0)) % prime)
                second.append(1 if i == 1 else (a*second[-1]-b*second[-2]) % prime)
        assert h[i] == f[i]*w % prime
    Pd = N*N*sum(pow(Q, j, prime)*pow(f[j], -2, prime) for j in range(N)) % prime
    assert Pd == sum(f) % prime
    fb = [(-1)**j*pow(Q, -j*(j+1)//2, prime)*f[j] % prime for j in range(N)]
    Pdb = N*N*sum(pow(Q, -j, prime)*pow(fb[j], -2, prime) for j in range(N)) % prime
    assert h[d] == Pdb
    assert pow(fb[1], 3, prime)*h[d-1] % prime == ((1-2*pow(Q, -1, prime))*h[d]+pow(Q, -1, prime)) % prime
    for k in range(N):
        lhs = pow(fb[k], 3, prime)*h[d-k] % prime
        rhs = (h[d]*hb[k]+pow(Q, -1, prime)*jb[k]) % prime
        assert lhs == rhs
    return {"N": N, "all_original_T2_source_coefficients_and_Ward": True,
            "exact_Gaussian_endpoint_and_full_backward_current": True}


def calibration(N, rate):
    mp.mp.dps = N+60
    Q, d = mp.exp(2j*mp.pi/N), N-1
    F, H, J = [mp.mpc(1)], [mp.mpc(1)], [mp.mpc(0)]
    for i in range(1, N):
        F.append(F[-1]*(1-Q**i))
        a, b = 1+Q-3*Q**i, Q*(1-Q**(i-1))**3
        H.append(a*H[-1]-(b*H[-2] if i > 1 else 0))
        J.append(mp.mpc(1) if i == 1 else a*J[-1]-b*J[-2])
    Pd = mp.fsum(F)
    assert abs(H[-1]-mp.conj(Pd)) < mp.mpf('1e-35')*max(1, abs(Pd))
    energy = N*N*mp.fsum(abs(H[i]/F[i])**2 for i in range(N))
    maximum = max(range(N), key=lambda i: abs(H[i]/F[i]))
    ratio_error, j_over_h = mp.mpf(0), mp.mpf(0)
    for i in range(1, int(mp.mpf('.45')*N)+1):
        Y = Q**i
        mu = (2-3*Y-Y*mp.sqrt(4*Y-3))/2
        ratio_error = max(ratio_error, N*abs(H[i]/H[i-1]-mu))
        j_over_h = max(j_over_h, abs(J[i]/H[i]))
    assert abs(mp.log(energy)-N*rate) < 20*mp.log(N)
    return {"N": N, "log_energy_over_N": mp.nstr(mp.log(energy)/N, 20),
            "peak_index_over_N": maximum/N,
            "endpoint_modulus_over_N_3half": mp.nstr(abs(H[-1])/N**mp.mpf('1.5'), 16),
            "gapped_prefix_N_times_ratio_error": mp.nstr(ratio_error, 12),
            "gapped_prefix_second_solution_ratio": mp.nstr(j_over_h, 12),
            "scope": "finite calibration; the written source/endpoints/transfer proof establishes the rate"}


if __name__ == '__main__':
    mp.mp.dps = 60
    z = mp.findroot(lambda z: z**3-4*z*z+3*z-1, mp.mpf('3.2'))
    u = mp.asin(mp.sqrt(z)/2)
    rho = lambda v: abs((2-3*mp.exp(2j*v)-mp.exp(2j*v)*mp.sqrt(4*mp.exp(2j*v)-3))/2)
    integral = mp.quad(lambda v: mp.log(rho(v)), [0, u])
    lob = -mp.quad(lambda v: mp.log(2*mp.sin(v)), [0, u])
    rate = 2*(integral+2*lob)/mp.pi
    exact = [field_case(N) for N in range(2, 15)]
    profiles = [calibration(N, rate) for N in (16, 32, 64, 128, 256)]
    result = {"status": "PASS", "exact_original_root_families": exact,
              "critical_cubic_root": mp.nstr(z, 35),
              "proved_rate_integral_calibration": mp.nstr(rate, 35),
              "coherent_all_index_profiles": profiles,
              "scope": "Entire source vector and its reflected positive norm; no link-volume identification."}
    Path(__file__).with_name('actual_newton_two_twist_interaction_packet_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(exact)} exact original packet/Ward/backward-current levels; '
          f'{len(profiles)} high-precision coherent norm profiles')
