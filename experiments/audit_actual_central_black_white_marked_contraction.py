#!/usr/bin/env python3
"""Exact original odd central pivotal contractions, not assumed norm squares."""

import json
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_two_cut_ports import balanced_data
from audit_actual_trivalent_steinberg_central_anchor import closed_columns
from audit_actual_trivalent_complete_circle_vertex_kernel import vertex_formula, sources, axis_apply, matrix_power


def dual_vector(value, cap, p):
    result = value.copy()
    for a in range(3):
        result = axis_apply(cap, result, a, p)
    return result.transpose(2, 1, 0)


def level(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    m, d, x = (N-1)//2, N-1, pow(q, N-1, p)
    W, fac = closed_columns(N, q, p)
    Wbar, _ = closed_columns(N, pow(q, -1, p), p)
    cup = np.array([[N*pow(x, -b, p) % p if a+b == d else 0 for b in range(N)] for a in range(N)], dtype=np.int64)
    cap = np.array([[pow(x, a, p)*pow(N, -1, p) % p if a+b == d else 0 for b in range(N)] for a in range(N)], dtype=np.int64)
    P = np.eye(N*N, dtype=np.int64).reshape(N, N, N, N).transpose(1, 0, 2, 3).reshape(N*N, N*N)
    pi = Wbar.T@P % p
    gamma = pow(q, 3*m*m, p)*pow(N, -1, p) % p
    DW = cup.T@W.T % p@np.kron(cap.T, cap.T) % p@P % p
    assert np.array_equal(DW, gamma*pi % p)
    assert np.array_equal(pi@W % p, np.eye(N, dtype=np.int64))
    labels = [(m+r, m) for r in range(N)]
    U, V, Vm = vertex_formula(N, x, p, labels, Wbar)
    _, Vbar, Vmbar = vertex_formula(N, pow(x, -1, p), p, labels, W)
    # Row right-duality is transpose-times-cap^T; tensor contractions below
    # implement the transpose row action, then reverse abstract dual order.
    DU = dual_vector(U, cap, p)
    ordinary = pow(N, -6, p)*Vbar % p
    assert np.array_equal(ordinary, pow(gamma, 3, p)*DU % p)
    assert np.any(ordinary) and np.any(U)
    assert int(np.sum(ordinary*U) % p) == 0
    Theta = (W@cup % p).reshape((N,)*3)
    DTheta = dual_vector(Theta, cap, p)
    T = Theta.reshape(N*N, N).T@DTheta.reshape(N*N, N) % p
    assert np.array_equal(K@T % p, gamma*np.eye(N, dtype=np.int64) % p)
    assert int(np.trace(T) % p) == 0
    for a in range(m+1):
        h = pow(q, a*a, p)*fac[m]*pow(fac[a]*fac[m-a], -1, p) % p
        assert W[d*N+m-a, d-a] == pow(q, m*m, p)*h % p
    Est = W@pi % p
    tensor = Est.reshape((N,)*4)
    weights = np.diag(K)
    inverse_weights = np.array([pow(int(k), -1, p) for k in weights], dtype=np.int64)
    assert np.array_equal(np.einsum('abcb,b->ac', tensor, weights) % p, np.eye(N, dtype=np.int64))
    assert np.array_equal(np.einsum('abad,a->bd', tensor, inverse_weights) % p, np.eye(N, dtype=np.int64))
    imag = pow(eta, N, p)
    sine = [pow(imag, a, p)*pow(q, -a*(a+1)//2, p)*fac[a] % p for a in range(N)]
    S = sum((sine[m]*pow(sine[a]*sine[m-a], -1, p) % p)**4 for a in range(m+1)) % p
    A = pow(q, m*(2-m), p)*S % p
    Abar = pow(q, -m*(2-m), p)*S % p
    s = N*N*pow(q, -m*m, p)*A % p
    assert np.array_equal(U, s*Theta % p)
    assert pow(gamma, 4, p)*s*s % p == A*Abar % p
    actual = pow(N, -4, p)*int(np.sum(U*Vmbar) % p) % p
    assert actual == N**3*A*Abar % p
    direct = []
    if N <= 7:
        J, ell, marked = sources(N, x, p)
        omega = pow(eta, d*d, p)*(-1)**m*pow(q, m*(m+1), p) % p
        for exponents in [(0, 0, 0), (1, -2, 3), (-3, 1, 0)]:
            value = J.copy()
            for axis, exponent in enumerate(exponents):
                box = matrix_power(Rp, exponent, Rm, p)@(N*Est % p) % p
                assert np.array_equal(box, N*pow(omega, exponent, p)*Est % p)
                value = axis_apply(box, value, axis, p)
            scalar = int(np.sum(marked*value) % p)
            assert int(np.sum(ell*value) % p) == 0
            assert scalar == N**3*pow(omega, sum(exponents), p)*A*Abar % p
            direct.append({'signed_full_Cartan_exponents': list(exponents), 'unrestricted_original_marked_scalar': scalar})
    return {'N': N, 'exact_dual_Clebsch_and_nonzero_ordinary_white': True,
            'zero_ordinary_coherent_pairing': True,
            'typed_partial_traces_of_actual_simple_projector': True,
            'exact_marked_central_scalar': int(actual),
            'literal_full_physical_marker_checks': direct}


def profile(N):
    mp.mp.dps = 80
    m = (N-1)//2
    s = [mp.mpf(1)]
    for a in range(1, m+1):
        s.append(s[-1]*2*mp.sin(mp.pi*a/N))
    Aabs = sum((s[m]/s[a]/s[m-a])**4 for a in range(m+1))
    normalized = 16*N**3*Aabs**2*mp.exp(-2*N*4*mp.catalan/mp.pi)
    assert abs(normalized-1) < 7/N
    return {'N': N, 'marked_scalar_normalized_proved_prefactor': float(normalized)}


if __name__ == '__main__':
    levels = [level(N) for N in range(3, 16, 2)]
    profiles = [profile(N) for N in (33, 65, 129, 257)]
    result = {'status': 'PASS', 'exact_original_odd_central_contractions': levels,
              'positive_marked_scalar_profiles': profiles,
              'scope': 'Exact odd central ordinary and original-marked two-vertex contractions. No even/paired or arbitrary-graph survival statement.'}
    Path(__file__).with_name('actual_central_black_white_marked_contraction_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 7 exact central dual/ordinary/marked levels; 9 literal physical signed markers; 4 scalar prefactors')
