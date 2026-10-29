#!/usr/bin/env python3
"""Finite-dimensional majorization/pointed-energy algebra audit.

Model matrices test the proved identities; no actual knot channel is
asserted here.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np


def unitary(rng, d):
    z = rng.normal(size=(d, d))+1j*rng.normal(size=(d, d))
    q, r = np.linalg.qr(z)
    phase = np.diag(r)/abs(np.diag(r))
    return q@np.diag(phase.conjugate())


def majorization_tests():
    rng = np.random.default_rng(918237)
    for _ in range(24):
        d = 4
        P = np.eye(d, dtype=complex)
        upper = np.zeros(d)
        for _ in range(7):
            A = unitary(rng, d)@np.diag(np.exp(rng.uniform(-.6, .6, d)))@unitary(rng, d)
            upper += np.log(np.linalg.svd(A, compute_uv=False))
            P = A@P
        actual = np.log(np.linalg.svd(P, compute_uv=False))
        assert np.max(np.cumsum(actual)-np.cumsum(upper)) < 1e-11
        assert abs(sum(actual)-sum(upper)) < 1e-11
        for power in [.5, 1, 2]:
            assert sum(np.exp(power*actual)) <= sum(np.exp(power*upper))+1e-10
    return 24


def channel_tests():
    rng = np.random.default_rng(12841)
    for index in range(20):
        R = np.diag([-.3, -.3, .2, .2])
        U = np.zeros((4, 4), complex)
        U[:2, :2], U[2:, 2:] = unitary(rng, 2), unitary(rng, 2)
        if index % 2:
            U = unitary(rng, 4)
        V = unitary(rng, 4)
        Ks = [np.sqrt(.37)*U, np.sqrt(.63)*V]
        phiR = sum(K@R@K.conjugate().T for K in Ks)
        lhs = sum(np.linalg.norm(R@K-K@R)**2 for K in Ks)
        rhs = 2*np.trace(R@(R-phiR)).real
        assert abs(lhs-rhs) < 1e-12
        C = abs(U)**2
        r = np.diag(R)
        variance = sum(C[i, j]*(r[i]-r[j])**2 for i in range(4) for j in range(4))
        assert abs(variance-2*r@(r-C@r)) < 1e-12
        if index % 2 == 0:
            assert np.linalg.norm(C@r-r) < 1e-12
            assert np.linalg.norm(U@R-R@U) < 1e-12
    return 20


def pointed_telescoping():
    mp.mp.dps = 80
    # Marked potential tie blocks change at each stage. Every U_j
    # commutes with the local potential, not necessarily other stages.
    N = 32
    potentials = [[0, 0, 0, 0], [-.2, -.2, .1, .1],
                  [.15, -.1, .15, -.1], [.2, .2, -.15, -.15],
                  [.11, .27, -.08, .03]]
    vectors = [list(map(lambda x: mp.mpf(str(x)), r)) for r in potentials]
    G = [mp.diag([mp.exp(N*x) for x in r]) for r in vectors]
    U = []
    for r in vectors[:-1]:
        groups = [[i for i in range(4) if r[i] == value] for value in sorted(set(r))]
        A = mp.eye(4)
        for group in groups:
            if len(group) >= 2:
                i, j = group[:2]
                A[i, i] = A[j, j] = mp.cos(mp.mpf('.37'))
                A[i, j], A[j, i] = mp.sin(mp.mpf('.37')), -mp.sin(mp.mpf('.37'))
        U.append(A)
    P, product_U = mp.eye(4), mp.eye(4)
    for j in range(len(U)):
        D = G[j+1]*(G[j]**-1)
        P = D*U[j]*P
        product_U = U[j]*product_U
    expected = G[-1]*product_U
    assert mp.norm(P-expected)/mp.norm(expected) < mp.mpf('1e-65')
    s = mp.matrix([1, 2j, mp.mpf('.3'), -1])
    ell = mp.matrix([1j, mp.mpf('.5'), -1, 2])
    value = (ell.H*P*s)[0]
    bound = mp.norm(G[-1]*ell)*mp.norm(s)
    assert abs(value) <= bound
    return {'exact_matrix_error': mp.nstr(mp.norm(P-expected), 8),
            'source_amplitude': mp.nstr(abs(value), 18),
            'source_bound': mp.nstr(bound, 18)}


def phase_energy():
    mp.mp.dps = 80
    out = []
    for N in [16, 32, 64]:
        a, b = mp.mpf(2), mp.mpf(1)/N
        weights = [mp.exp(a*k*(N-k)/N) for k in range(N)]
        sampled = mp.fsum(abs(b*mp.fsum(weights[k]*mp.exp(2j*mp.pi*ell*k/N)
                                        for k in range(N)))**2 for ell in range(N))/N
        exact = b*b*mp.fsum(w*w for w in weights)
        assert abs(sampled-exact)/exact < mp.mpf('1e-65')
        fixed = b*mp.fsum(weights[k]*mp.exp(1j*k) for k in range(N))
        out.append({'N': N, 'sqrt_phase_energy_rate': mp.nstr(mp.log(exact)/(2*N), 18),
                    'fixed_theta_one_rate': mp.nstr(mp.log(abs(fixed))/N, 18),
                    'envelope_limit': '.5', 'fixed_theta_limit': '.375'})
    return out


def main():
    data = {'status': 'PASS', 'log_majorization_families': majorization_tests(),
            'bistochastic_variance_families': channel_tests(),
            'exact_source_telescoping': pointed_telescoping(),
            'phase_plancherel': phase_energy(),
            'scope': ('General matrix/source algebra and analytic-model energy only; '
                      'the actual knot connection fixed-point premise is not asserted.')}
    Path(__file__).with_name('regulator_majorization_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
