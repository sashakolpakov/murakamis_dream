#!/usr/bin/env python3
"""Original multicomponent Kashaev/quantum/ADO source normalization.

Original Kashaev weights and the finite quantum R are evaluated
separately.  No comparison theorem or polynomial normalization is
assumed.  One genuine cut is used on every link.
"""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_kashaev_crossing import original, quantum_group
from audit_high_color_first_normal_r_degree import root_field


def components(width, word):
    perm = list(range(width))
    for letter in word:
        a = abs(letter)-1
        perm[a], perm[a+1] = perm[a+1], perm[a]
    seen, count = set(), 0
    for a in range(width):
        if a in seen:
            continue
        count += 1
        while a not in seen:
            seen.add(a)
            a = perm[a]
    return count


def normalized_cut(N, width, word, positive, negative, pivot, alpha, prime):
    I = np.eye(N, dtype=np.int64)
    W = np.eye(N**width, dtype=np.int64)
    for letter in word:
        slot = abs(letter)-1
        gate = positive if letter > 0 else negative
        for _ in range(slot):
            gate = np.kron(I, gate) % prime
        for _ in range(width-slot-2):
            gate = np.kron(gate, I) % prime
        W = gate@W % prime
    closing = I.copy()
    for _ in range(width-1):
        closing = np.kron(closing, pivot) % prime
    W = W@closing % prime
    if width == 2:
        C = np.einsum('abcb->ac', W.reshape((N,)*4)) % prime
    elif width == 3:
        C = np.einsum('abcdbc->ad', W.reshape((N,)*6)) % prime
    else:
        raise ValueError('audit widths are2 or3')
    writhe = sum(1 if a > 0 else -1 for a in word)
    C = C*pow(int(alpha), -writhe, prime) % prime
    assert np.array_equal(C, int(C[0, 0])*I % prime)
    # Original rank-one selected source, not division by quantum dimension.
    assert int(np.sum(C))*pow(N, -1, prime) % prime == int(C[0, 0])
    return int(C[0, 0])


def link_cases(N):
    prime, eta = root_field(N)
    q, Q, d = eta*eta % prime, pow(eta, 4, prime), N-1
    Ro, printed, _ = original(N, prime, Q)
    Rq, Rqi = quantum_group(N, prime, eta)
    P = np.zeros((N*N, N*N), dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        P[b*N+a, a*N+b] = 1
    I = np.eye(N*N, dtype=np.int64)
    BK, BKi = P@Ro.T % prime, printed.T@P*pow(Q, -1, prime) % prime
    BD, BDi = P@Rq.T % prime, Rqi.T@P % prime
    BP, BPi = P@Rq % prime, Rqi@P % prime
    for positive, negative in ((BK, BKi), (BD, BDi), (BP, BPi)):
        assert np.array_equal(positive@negative % prime, I)
    shift = np.roll(np.eye(N, dtype=np.int64), 1, axis=0)
    muK = -q*shift % prime
    K = np.diag([pow(q, d-2*a, prime) for a in range(N)]).astype(np.int64)
    Ki = np.diag([pow(int(a), -1, prime) for a in np.diag(K)]).astype(np.int64)
    g = np.diag([pow(int(a), -d, prime) for a in np.diag(K)]).astype(np.int64)
    assert np.array_equal(g, pow(-1, d, prime)*K % prime)
    alphaK, alphaq = -q % prime, pow(eta, N*N-1, prime)
    theta = pow(eta, -d*d, prime)
    assert theta == pow(-1, d, prime)*alphaq % prime
    words = [(2, ()), (2, (1,)), (2, (1, 1)), (2, (1, 1, 1))]
    if N <= 5:
        words += [(3, ()), (3, (1, 2)), (3, (1, 1, 2, 2)),
                  (3, (1, -2, 1, -2, 1, -2)), (3, (1, -2, 1, -2, 1))]
    rows = []
    for width, word in words:
        c = components(width, word)
        kash = normalized_cut(N, width, word, BK, BKi, muK, alphaK, prime)
        dual = normalized_cut(N, width, word, BD, BDi, Ki, alphaq, prime)
        ordinary = normalized_cut(N, width, word, BP, BPi, K, alphaq, prime)
        ado = normalized_cut(N, width, word, BP, BPi, g, theta, prime)
        assert kash == dual == ordinary
        assert ado == pow(-1, d*(c-1), prime)*kash % prime
        rows.append({'N': N, 'width': width, 'word': list(word), 'link_components': c,
                     'literal_original_enhanced_vs_quantum_cut': True,
                     'actual_ADO_pivot_twist_component_sign': True,
                     'selected_one_cut_value_nonzero': bool(kash)})
    return rows


def peripheral_germ(N):
    mp.mp.dps = 90
    q, d = mp.exp(mp.pi*1j/N), N-1
    logq, eta = mp.log(q), mp.j**(N+3)
    prefactor = -mp.exp(logq*N*(1-N)/2)
    def numerator(u):
        alpha = d+u/logq
        return mp.exp(logq*(alpha+1))-mp.exp(-logq*(alpha+1))
    def denominator(u):
        alpha = d+u/logq
        return mp.exp(logq*N*alpha)-mp.exp(-logq*N*alpha)
    at_zero = prefactor*mp.diff(numerator, 0)/mp.diff(denominator, 0)
    assert abs(at_zero-eta/N) < mp.mpf('1e-75')
    for u in (mp.mpf(1)/(10*N), mp.mpc(1, mp.mpf('.2'))/(11*N),
              -mp.mpc(1, mp.mpf('-.1'))/(13*N)):
        actual = prefactor*numerator(u)/denominator(u)
        whole = eta*mp.sinh(u)/mp.sinh(N*u)
        assert abs(actual-whole) < mp.mpf('1e-75')
    kappa = mp.exp(logq*d*d/2)
    theta = mp.exp(logq*(d*d-2*d*d)/2)
    assert abs(theta-1/kappa) < mp.mpf('1e-75')
    assert abs(abs(theta)-1) < mp.mpf('1e-75')
    assert abs(abs(at_zero)-mp.mpf(1)/N) < mp.mpf('1e-75')
    return {'N': N, 'whole_original_meridian_germ': True,
            'single_modified_cut_factor_modulus': f'1/{N}',
            'actual_complete_twist_modulus': 1,
            'reduced_external_factor_exponential_rate_zero': True}


if __name__ == '__main__':
    links = [row for N in range(2, 7) for row in link_cases(N)]
    assert any(row['link_components'] > 1 and row['selected_one_cut_value_nonzero'] for row in links)
    germs = [peripheral_germ(N) for N in list(range(2, 17))+[24, 32, 64]]
    results = {'status': 'PASS', 'original_knot_and_multicomponent_cuts': links,
               'actual_whole_modified_dimension_and_twist': germs,
               'scope': 'Complete one-cut enhanced link normalization only; no generic peripheral-size, q-normal-jet or geometric-volume claim.'}
    Path(__file__).with_name('actual_complete_augmented_source_normalization_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print(f'PASS {len(links)} original knot/link cuts; {len(germs)} whole peripheral germ/twist levels; no external exponential factor')
