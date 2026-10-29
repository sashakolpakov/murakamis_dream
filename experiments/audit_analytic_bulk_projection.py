#!/usr/bin/env python3
"""Normalization audit for analytic finite-head projection and endpoint forcing."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_crossing_euler_completion import actual_data


def main():
    mp.mp.dps = 90
    exact = []
    for N in range(2, 13):
        data = actual_data(N, 1)
        if data is None:
            continue
        p, q, x, _, pivot, *_ = data
        Q = q*q % p
        F = [1]
        for a in range(1, N):
            F.append(F[-1]*(1-pow(Q, a, p)) % p)
        u = [pow(c, -1, p) for c in F]
        v = [pow(-1, a, p)*pow(Q, a*(a-1)//2, p)*u[a] % p for a in range(N)]
        for a in range(N+1):
            ua = u[a] if a < N else 0
            uprev = u[a-1] if a else 0
            va = v[a] if a < N else 0
            vprev = v[a-1] if a else 0
            rhs = pow(N, -1, p) if a == N else 0
            assert (pow(Q, a, p)*ua-ua+uprev-rhs) % p == 0
            assert (va-pow(Q, a, p)*va+pow(Q, a-1, p)*vprev-rhs) % p == 0
        S = np.zeros((N, N), dtype=np.int64)
        for a in range(N-1):
            S[a+1, a] = 1
        Xm, Xp = np.kron(S.T, S), np.kron(S, S.T)
        wall = Xm@Xp
        expected = np.kron(np.eye(N, dtype=np.int64)-np.diag([int(a == N-1) for a in range(N)]),
                           np.eye(N, dtype=np.int64)-np.diag([int(a == 0) for a in range(N)]))
        assert np.array_equal(wall, expected)
        value = sum(int(wall[a*N+k, a*N+k])*int(pivot[k]) for a in range(N) for k in range(N))*pow(N, -1, p) % p
        assert value == -(N-1)*int(pivot[0])*pow(N, -1, p) % p and value != 0
        exact.append(dict(N=N, field=p, wall_source=value))

    packets = []
    epsilon, s, delta = mp.mpf('0.03'), mp.mpf('0.4'), mp.mpf('0.3')
    for N in (10, 20, 40, 80):
        k = N//2
        # z^k(1+eps*z)^N(1+eps/z)^N: all coefficients positive.
        coeff = {}
        for a in range(N+1):
            for b in range(N+1):
                degree = k+a-b
                coeff[degree] = coeff.get(degree, mp.mpf(0))+mp.binomial(N, a)*mp.binomial(N, b)*epsilon**(a+b)
        envelope = (1+epsilon)**(2*N)
        actual_error = sum(c for degree, c in coeff.items() if degree < 0 or degree >= N)
        inner = mp.exp(-s*k)*(1+epsilon*mp.exp(-s))**N*(1+epsilon*mp.exp(s))**N
        outer = mp.exp(s*k)*(1+epsilon*mp.exp(s))**N*(1+epsilon*mp.exp(-s))**N
        assert inner <= envelope*mp.exp(-delta*N*s)
        assert outer <= envelope*mp.exp((1-delta)*N*s)
        exact_bound = inner/(mp.exp(s)-1)+outer*mp.exp(-N*s)/(1-mp.exp(-s))
        theorem_bound = 2*envelope*mp.exp(-delta*N*s)/(1-mp.exp(-s))
        assert actual_error <= exact_bound <= theorem_bound
        packets.append(dict(N=N, relative_wall_error=float(actual_error/envelope), relative_bound=float(theorem_bound/envelope)))

    factorials, endpoint = [], []
    for N in (30, 60, 120, 240):
        Q = mp.exp(2j*mp.pi/N)
        F = [mp.mpc(1)]
        for a in range(1, N):
            F.append(F[-1]*(1-Q**a))
        t = mp.mpf(1)/3
        k = N//3
        A = -(mp.polylog(2, mp.exp(2j*mp.pi*t))-mp.pi**2/6)/(2j*mp.pi)
        approximation = mp.sqrt(2*N*mp.sin(mp.pi*t))*mp.exp(N*A+mp.pi*1j*t/2)
        relative = abs(F[k]/approximation-1)
        assert relative < mp.mpf(1)/N
        factorials.append(dict(N=N, N_times_relative_error=float(N*relative)))
        z = mp.exp(mp.pi*1j/3)
        u = lambda w: sum(w**a/F[a] for a in range(N))
        pairmax = max(abs(u(z)), abs(u(Q*z)))
        assert pairmax >= (1-mp.mpf('1e-60'))/(2*N)
        endpoint.append(dict(N=N, N_times_pairmax=float(N*pairmax)))
    result = dict(status='PASS', exact_cases=exact, interior_packets=packets,
                  factorial_normalization=factorials, forbidden_homogeneous_chart=endpoint,
                  scope='Actual interior projector estimate and forced endpoint; no knot-cycle comparison.')
    Path(__file__).with_name('analytic_bulk_projection_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', exact_cases=len(exact), interior_packets=len(packets), factorial_cases=len(factorials))))


if __name__ == '__main__':
    main()
