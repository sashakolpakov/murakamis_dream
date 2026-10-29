#!/usr/bin/env python3
"""Original 4_1 full-channel energy: exact odd-root witness + stable CD numerics.

No dense numerical inverse is used: original negative R is its exact
antiunitary mirror, and V^{-1} is evaluated by its CD blocks.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_casimir_hermite_packet import canonical_field_frame


def exact_odd_source(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    Q, d, m = q*q % prime, N-1, (N-1)//2
    x, rho = int(K[0, 0]), (q-pow(q, -1, prime)) % prime
    factorial = [1]
    for j in range(1, N):
        factorial.append(factorial[-1]*(1-pow(Q, j, prime)) % prime)
    E2, F2, K2 = coproduct(E*rho*rho % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(K2)])
    O2 = (F2@E2+q*K2+pow(q, -1, prime)*Ki) % prime
    ids = [j*N+d-j for j in range(N)]
    A, R, Ri = O2[np.ix_(ids, ids)], Rp[np.ix_(ids, ids)], Rm[np.ix_(ids, ids)]
    V, Vi, metadata, blocks = canonical_field_frame(A, N, d, prime, q)
    J = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N-i):
            binomial = factorial[d-j]*pow(factorial[i]*factorial[d-i-j] % prime, -1, prime) % prime
            J[i, j] = (pow(-x*Q, d-i, prime)*pow(x, j, prime)
                       *pow(Q, i*(i+1)//2-d*(d+1)//2, prime)*binomial) % prime
    assert np.array_equal(J, J.T)
    simple = metadata.index((m, 'value'))
    eigen = V[:, simple]
    y = np.zeros(N, dtype=np.int64)
    positive = []
    for r in range(m+1):
        b = factorial[m]*pow(factorial[r]*factorial[m-r] % prime, -1, prime) % prime
        positive.append(pow(Q, -r*(m-r), prime)*b*b % prime)
        y[m+r] = positive[-1]
    assert np.array_equal(J@eigen % prime, y)
    cup = np.array([N*pow(x, a-d, prime) % prime for a in range(N)], dtype=np.int64)
    kappa = int(Rp[0, 0])
    assert kappa*kappa % prime == pow(x, d, prime)
    first = np.array([kappa*int(cup[a])*factorial[d-a] % prime for a in range(N)], dtype=np.int64)
    v = Ri@first % prime
    Bm = sum(positive) % prime
    nu = pow(-1, m, prime)*pow(q, m*(m+1), prime) % prime
    assert int(y@v) % prime == N*nu*factorial[m]*Bm % prime
    output = R@R % prime@J % prime@v % prime
    channel = Vi@output % prime
    target = N*nu*nu*factorial[m]*Bm % prime
    assert int(channel[simple]) == target
    # The literal cap source remains the complete value-channel sum/N.
    scalar = sum(int(channel[i]) for i, (_, kind) in enumerate(metadata) if kind == 'value')
    scalar = scalar*pow(x, d, prime)*pow(N, -1, prime) % prime
    positive_period = sum(factorial[a]*pow(-1, a, prime)*pow(Q, -a*(a+1)//2, prime)*factorial[a]
                          for a in range(N)) % prime
    assert scalar == positive_period
    return {'N': N, 'literal_original_R_and_inverse_with_kappa': True,
            'complete_Hermite_simple_channel_and_positive_projection': True,
            'exact_original_figure_eight_scalar': True}


def matvec(A, v):
    return [mp.fsum(a*b for a, b in zip(row, v)) for row in A]


def high_precision_energy(N, digits=None):
    mp.mp.dps = digits or 80+N
    q = mp.exp(mp.j*mp.pi/N)
    Q, x, d = q*q, -1/q, N-1
    kappa = q**(mp.mpf(d*d)/2)
    fac = [mp.mpc(1)]
    for j in range(1, N):
        fac.append(fac[-1]*(1-Q**j))
    R = [[mp.mpc(0) for _ in range(N)] for _ in range(N)]
    for a in range(N):
        b = d-a
        for k in range(a+1):
            i = b+k
            R[i][a] = (kappa*x**(-d+k)*Q**(b*(a-k))*fac[i]*fac[a]
                       /fac[k]/fac[b]/fac[a-k])
    Ri = [[mp.conj(R[d-i][d-j]) for j in range(N)] for i in range(N)]
    J = [[mp.mpc(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        phase = (-x*Q)**(d-i)*Q**(i*(i+1)//2-d*(d+1)//2)
        for j in range(N-i):
            J[i][j] = phase*x**j*fac[d-j]/fac[i]/fac[d-i-j]
    # Chronological word [2,-1,2,2]. The first R23/cup contraction
    # is the exact source identity, not an interpolated approximation.
    first = [kappa*N*x**(a-d)*fac[d-a] for a in range(N)]
    v = matvec(Ri, first)
    right = matvec(R, matvec(R, matvec(J, v)))
    diagonal = [q+1/q-q*(1-Q**u)**2-(1-Q**(u+1))**2/q for u in range(N)]
    off = [-(1-Q**(u+1))**2 for u in range(d)]
    channels, values = [], []
    for j in range((N+1)//2):
        c = q**(2*j+1)+q**(-2*j-1)
        nu = (-1)**j*q**(j*(j+1))
        f, derivative = [mp.mpc(1)], [mp.mpc(0)]
        for u in range(d):
            f.append(((c-diagonal[u])*f[u]-(off[u-1]*f[u-1] if u else 0))/off[u])
            derivative.append((f[u]+(c-diagonal[u])*derivative[u]
                               -(off[u-1]*derivative[u-1] if u else 0))/off[u])
        pairing = mp.fsum(f[u]*right[u] for u in range(N))
        if 2*j+1 < N:
            sigma = (-1)**d*x**d*nu/(4-c*c)
            jet = -nu*(d-2*j)/(2*(q**(2*j+1)-q**(-2*j-1)))
            eta = jet/nu+c/(4-c*c)
            value = (mp.fsum(derivative[u]*right[u] for u in range(N))-eta*pairing)/sigma
            channels += [value, pairing/sigma]
            values.append(value)
        else:
            value = pairing/(x**d*nu)
            channels.append(value)
            values.append(value)
    scalar = x**d/N*mp.fsum(values)
    period = mp.fsum(abs(z)**2 for z in fac)
    error = abs(scalar/period-1)
    assert error < mp.mpf(10)**(-min(35, mp.mp.dps//4))
    energy = mp.fsum(abs(z)**2 for z in channels)/N
    row = {'N': N, 'decimal_digits': mp.mp.dps,
           'log_complete_energy_over_N': float(mp.log(energy)/N),
           'log_original_squared_scalar_over_N': float(2*mp.log(period)/N),
           'relative_original_scalar_error': mp.nstr(error, 8),
           'dense_numeric_inverse_used': False}
    if N % 2:
        m = d//2
        Bm = mp.fsum(abs(fac[m]/fac[r]/fac[m-r])**2 for r in range(m+1))
        target = N*Q**(m*(m+1))*fac[m]*Bm
        witness_error = abs(channels[-1]/target-1)
        assert witness_error < mp.mpf(10)**(-min(35, mp.mp.dps//4))
        witness_energy = N*N*Bm*Bm
        assert energy >= witness_energy*(1-mp.mpf('1e-30'))
        row.update({'exact_simple_channel_relative_error': mp.nstr(witness_error, 8),
                    'log_proved_positive_witness_over_N': float(mp.log(witness_energy)/N)})
    return row, energy


if __name__ == '__main__':
    exact = [exact_odd_source(N) for N in range(3, 18, 2)]
    profiles, energies = [], {}
    for N in (8,16,17,32,33,64,65,96,97,129):
        row, energy = high_precision_energy(N)
        profiles.append(row)
        energies[N] = energy
    low, e1 = high_precision_energy(32, 112)
    high, e2 = high_precision_energy(32, 192)
    assert abs(e1/e2-1) < mp.mpf('1e-70')
    refined, highest = high_precision_energy(129, 320)
    assert abs(energies[129]/highest-1) < mp.mpf('1e-100')
    result = {'status': 'PASS', 'exact_original_odd_root_witnesses': exact,
              'high_precision_complete_energies': profiles,
              'precision_doubling_relative_error': mp.nstr(abs(e1/e2-1), 8),
              'highest_level_precision_refinement_relative_error':mp.nstr(abs(energies[129]/highest-1),8),
              'proved_witness_exponential_rate': 'v8/pi = 4*Catalan/pi',
              'scope': 'lower witness disproves sharpness of this fixed Gram; full energy limit not asserted'}
    Path(__file__).with_name('actual_figure_eight_complete_channel_energy_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(exact)} exact full-source odd-root witnesses; {len(profiles)} CD high-precision energies; precision doubling')
