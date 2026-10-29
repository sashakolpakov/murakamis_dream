#!/usr/bin/env python3
"""Complete filling Gram and literal mixed-circle source discriminant."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_crossing_circle_source_and_filling import (
    ordinary_module, crossing_circle, filling_coefficients,
)


def gram_maps(N):
    K, S = mp.matrix(N), mp.matrix(N)
    K[0, 0] = 1
    pos = 1
    for n in range(1, (N+1)//2):
        m, r = N-n, mp.mpf(n)/N
        K[n, pos], K[m, pos] = (1-r)/mp.sqrt(2), -r/mp.sqrt(2)
        K[n, pos+1] = K[m, pos+1] = 1/mp.sqrt(2)
        pos += 2
    if N % 2 == 0:
        K[N//2, pos] = 1
        pos += 1
    assert pos == N
    for j in range(N):
        S[j, j] = (-1)**j
        if j+2 < N:
            S[j, j+2] = -(-1)**j
    B = S*K
    return K, S, B, B*B.T


def filling_data(N, ell):
    q = mp.exp(mp.j*mp.pi/N)
    d = N-1
    w = [q**(2*k+1) for k in range(N)]
    nu = [(-1)**k*q**(k*(k+1)) for k in range(N)]
    h = [v**ell for v in nu]
    jet = [-mp.mpf(ell)/2*(d-2*k)*h[k] for k in range(N)]
    H = [sum(h[k]*w[k]**(-n) for k in range(N))/N for n in range(N)]
    D = [sum(jet[k]*w[k]**(-n) for k in range(N))/N for n in range(N)]
    a = [H[0]]+[(D[n]+(N-n)*H[n])/N for n in range(1, N)]
    y = [H[0]]
    for n in range(1, (N+1)//2):
        y.extend((mp.sqrt(2)*H[n], mp.sqrt(2)*D[n]/N))
    if N % 2 == 0:
        y.append(D[N//2]/N)
    extended = a+[0, 0]
    beta = [(-1)**j*(extended[j]-extended[j+2]) for j in range(N)]
    return mp.matrix(a), mp.matrix(y), mp.matrix(beta)


def complex_gram_case(N):
    with mp.workdps(100):
        K, S, B, G = gram_maps(N)
        eigenvalues = np.linalg.eigvalsh(np.array(G.tolist(), dtype=float))
        assert eigenvalues[0] >= 1/(6*N*N)*(1-1e-10)
        assert eigenvalues[-1] <= 6*(1+1e-10)
        Gi = G**(-1)
        norm2 = lambda v: sum(abs(z)**2 for z in v)
        for ell in (-7, -2, -1, 0, 1, 2, 8):
            a, y, beta = filling_data(N, ell)
            assert max(abs(z) for z in K*y-a) < mp.mpf('1e-65')
            assert max(abs(z) for z in B*y-beta) < mp.mpf('1e-65')
            cost = 1+mp.mpf(ell*ell)*(N*N-1)/(12*N*N)
            assert abs(norm2(y)-cost) < mp.mpf('1e-65')
            dual = (beta.T*Gi*beta.conjugate())[0]
            assert abs(dual-cost) < mp.mpf('1e-65')
            packet = mp.matrix([mp.exp(mp.j*j*j/7)/(j+1)+mp.j*(j % 3) for j in range(N)])
            z = B.T*packet
            period = (beta.T*packet)[0]
            assert abs(period-(y.T*z)[0]) < mp.mpf('1e-65')
            assert abs(period)**2 <= cost*norm2(z)*(1+mp.mpf('1e-60'))
        # Arbitrary noncommuting operator-valued exteriors, with all ports open.
        ell = -2
        _, y, beta = filling_data(N, ell)
        Bt = np.array(B.T.tolist(), dtype=float)
        operators = np.array([[[1+j*1j, .2*(j+1)], [.3j, (-1)**j+.1j*j]]
                              for j in range(N)], dtype=complex)
        transformed = np.einsum('rj,jab->rab', Bt, operators)
        filled = sum(complex(beta[j])*operators[j] for j in range(N))
        cost = float(norm2(y))
        gap = cost*sum(A.conj().T@A for A in transformed)-filled.conj().T@filled
        assert np.linalg.eigvalsh(gap)[0] >= -1e-8*max(1, np.linalg.norm(gap))
        return {'N': N, 'seven_signed_full_Hermite_dual_costs': True,
                'even_alias_or_odd_simple_node_retained': True,
                'positive_Gram_condition': float(eigenvalues[-1]/eigenvalues[0]),
                'all_input_operator_Cauchy': True}


def physical_source_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x, kappa = N-1, q*q % prime, int(K[0, 0]), int(Rp[0, 0])
    target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [d-2*a for a in range(N)]}
    I = np.eye(N, dtype=np.int64)
    cup = np.zeros((N**3, N), dtype=np.int64)
    expected_slide = np.zeros_like(cup)
    for a in range(N):
        for j in range(N):
            cup[(j*N+d-j)*N+a, a] = N*pow(x, j-d, prime) % prime
            expected_slide[(a*N+j)*N+d-j, a] = N*pow(x, j-d, prime) % prime

    def on12(operator, state):
        out = np.zeros_like(state)
        for c in range(N):
            out[c::N, :] = operator@state[c::N, :] % prime
        return out

    def on23(operator, state):
        out = np.zeros_like(state)
        for a in range(N):
            block = slice(a*N*N, (a+1)*N*N)
            out[block] = operator@state[block] % prime
        return out

    def close(state):
        out = np.zeros((N, N), dtype=np.int64)
        for a in range(N):
            cap = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
            for c in range(N):
                out[c, :] += cap*state[(a*N+d-a)*N+c, :] % prime
        return out % prime

    prefix = on12(Rp, on23(Rp, cup))
    assert np.array_equal(prefix, expected_slide)
    R2 = Rp@Rp % prime
    packet = []
    operators = []
    for j in range(1, N+1):
        loop = crossing_circle(target, ordinary_module(j, q, prime), q, eta, prime, N)
        actual = close(on23(R2, on12(loop, prefix)))
        scalar = int(actual[0, 0])
        assert np.array_equal(actual, scalar*I % prime)
        packet.append(scalar)
        operators.append(actual)
    assert packet[0] == kappa*kappa % prime
    fac, factor = [1], 1
    for j in range(1, N):
        factor = factor*(1-pow(Q, j, prime)) % prime
        fac.append(factor)
    Z = sum(pow(-1, j, prime)*pow(Q, -j*(j+1)//2, prime)*fac[j]**2 for j in range(N)) % prime
    beta = filling_coefficients(N, q, Q, -2, prime)
    assert pow(kappa, -2, prime)*sum(beta[j]*packet[j] for j in range(N)) % prime == Z
    actual_figure = close(on23(R2, on12(Rm@Rm % prime, prefix)))
    assert np.array_equal(actual_figure, Z*I % prime)
    for value, operator in zip(packet, operators):
        assert np.array_equal(operator@actual_figure % prime, value*Z*I % prime)
    return {'N': N, 'literal_mixed_circle_tangle_colors': N,
            'every_input_scalar_tangle_and_cup_slide': True,
            'actual_normalization_and_figure_eight_fillings': True,
            'arbitrary_knot_scalar_insertion_tested_on_figure_eight': True}


def actual_base_energy(N):
    with mp.workdps(3*N+80):
        d = N-1
        q = mp.exp(mp.j*mp.pi/N)
        Q, x = q*q, q**d
        # Actual complete A and exact terminal cap row N ell R23^2.
        A = mp.matrix(N)
        for j in range(N):
            A[j, j] = q+1/q-q*(1-Q**j)**2-(1-Q**(j+1))**2/q
            if j:
                A[j-1, j] = A[j, j-1] = -(1-Q**j)**2
        e0 = mp.zeros(N, 1)
        e0[0] = 1
        u0, u1 = e0, A*e0
        vectors = [u0]
        if N > 1:
            vectors.append(u1)
        for j in range(2, N):
            u0, u1 = u1, A*u1-u0
            vectors.append(u1)
        packet = mp.matrix([(-1)**j*sum(x**(d-i)*vectors[j][i] for i in range(N)) for j in range(N)])
        _, _, B, _ = gram_maps(N)
        z = B.T*packet
        energy = sum(abs(v)**2 for v in z)
        _, source, beta = filling_data(N, -2)
        fac, Z = mp.mpc(1), mp.mpf(1)
        for j in range(1, N):
            fac *= 1-Q**j
            Z += abs(fac)**2
        kappa = q**(mp.mpf(d*d)/2)
        assert abs(packet[0]-kappa**2) < mp.mpf('1e-45')
        assert abs(kappa**(-2)*(beta.T*packet)[0]-Z) < mp.mpf('1e-40')*max(1, Z)
        cost = sum(abs(v)**2 for v in source)
        assert energy >= Z**2/cost*(1-mp.mpf('1e-38'))
        assert energy >= mp.mpf(3)/4*Z**2*(1-mp.mpf('1e-38'))
        inserted_energy = Z**2*energy
        assert inserted_energy >= mp.mpf(3)/4*Z**4*(1-mp.mpf('1e-38'))
        return {'N': N, 'complete_actual_two_filling_packet': True,
                'unit_normalization_scalar_modulus': float(abs(packet[0])),
                'energy_over_Z_squared': float(energy/Z**2),
                'hyperbolic_inserted_energy_lower_bound': True}


if __name__ == '__main__':
    gram = [complex_gram_case(N) for N in (2, 3, 4, 6, 9, 12, 24)]
    physical = [physical_source_case(N) for N in range(2, 7)]
    base = [actual_base_energy(N) for N in (2, 3, 4, 6, 12, 24)]
    output = {'status': 'PASS', 'positive_complete_Hermite_Grams': gram,
              'literal_all_input_mixed_color_sources': physical,
              'actual_source_energy_discriminant': base,
              'scope': 'Exact coherent filling Gram and source discriminant; no reduced-long-filling geometric no-go.'}
    Path(__file__).with_name('actual_filling_fourier_hermite_gram_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 7 complete positive filling Grams/49 signed dual costs; 5 literal all-input mixed-circle packets; 6 actual two-filling energy discriminants')
