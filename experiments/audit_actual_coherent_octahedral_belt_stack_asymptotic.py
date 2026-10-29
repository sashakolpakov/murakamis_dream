#!/usr/bin/env python3
"""Exact physical stack sources and supplementary coherent-Gaussian checks."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pair_casimir_commutant_and_rotated_trace import phi, rotated
from diagnose_pretzel_coherent_radial_capacity import evaluate, source_polynomial


def physical_level(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Et, Ft, Kt = coproduct(rho*rho*E % prime, F, K, 2, N, prime)
    Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, prime)*Ki) % prime
    I = np.eye(N*N, dtype=np.int64)
    prev, current = I.copy(), O.copy()
    for _ in range(2, d+1):
        prev, current = current, (O@current-prev) % prime
    L = (-1)**d*current % prime

    def turn(A):
        return pow(x, d, prime)*rotated(A, N, x, prime) % prime

    z, zs = turn(Rm@L % prime), turn(Rp@L % prime)
    fp, fm = zs@Rm % prime, Rp@z % prime

    def power(A, n):
        out = I.copy()
        for _ in range(n):
            out = out@A % prime
        return out

    def Rpower(n):
        return power(Rp if n >= 0 else Rm, abs(n))

    # Recover actual Newton coefficients from the literal endpoint source;
    # this tests the complete full matrices before the retained belt kills jets.
    nodes = [(pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime for j in range(N)]
    packets, sine2 = [I.copy()], [1]
    for r in range(1, N):
        f = 1-pow(Q, r, prime)
        sine2.append(sine2[-1]*(-pow(Q, -r, prime))*f*f % prime)
        packets.append((nodes[r-1]*I-O)@packets[-1]*int(sine2[r-1])
                       *pow(int(sine2[r]), -1, prime) % prime)
    ids = [u*N+d-u for u in range(N)]

    def coefficients(A):
        middle = A[np.ix_(ids, ids)]
        return [int((middle@B[np.ix_(ids, ids)] % prime)[0, d]) for B in reversed(packets)]

    az, ash, ar = coefficients(z), coefficients(zs), coefficients(Rp)
    assert not any(az[d//2+1:]) and not any(ash[d//2+1:])

    def ev(alpha, c):
        b, value = 1, 0
        for r in range(N):
            value = (value+alpha[r]*b) % prime
            if r < d:
                b = b*(nodes[r]-c)*int(sine2[r])*pow(int(sine2[r+1]), -1, prime) % prime
        return value

    kappa = pow(eta, d*d, prime)
    assert all(ev(ar, nodes[j]) == kappa*(-1)**j*pow(q, j*(j+1), prime) % prime for j in range(N))
    zvalues, svalues = [ev(az, c) for c in nodes], [ev(ash, c) for c in nodes]
    rvalues = [ev(ar, c) for c in nodes]
    full_words = 0
    outer_rows = []
    for n in range(1, 5):
        for word in itertools.product('+-', repeat=n):
            p, qcount = word.count('+'), word.count('-')
            e = qcount-p
            product = I.copy()
            for sign in word:
                product = product@(fp if sign == '+' else fm) % prime
            reduced = Rpower(e)@power(zs, p)@power(z, qcount) % prime
            assert np.array_equal(product, reduced)
            full_words += 1
        # One word for every count, including both completely unbalanced ends;
        # all orders above have already been checked as FULL operators.
        for p in range(n+1):
            qcount, e = n-p, n-2*p
            for a in (-3, -1, 0, 2, 5):
                product = Rpower(e+a)@power(zs, p)@power(z, qcount) % prime
                actual = phi(L@product % prime, N, pivot, prime)
                expected = N*sum(pow(r, e+a, prime)*pow(s, p, prime)*pow(v, qcount, prime)
                                 for r, s, v in zip(rvalues, svalues, zvalues)) % prime
                assert actual == expected
                outer_rows.append({'plus': p, 'minus': qcount, 'outer_a': a,
                                   'literal_original_source_mod_prime': int(actual)})
    return {'N': N, 'full_original_word_operators': full_words,
            'all_nodal_crossing_eigenvalues_and_original_kappa': True,
            'full_normal_word_and_outer_twist_sources': outer_rows}


def high_precision_complex_phases():
    mp.mp.dps = 100
    count, maximum = 0, mp.mpf(0)
    for N in range(2, 42):
        d = N-1
        kappa = mp.exp(mp.j*mp.pi*d*d/(2*N))
        root = mp.exp(mp.j*mp.pi/N)
        square_root = mp.exp(mp.j*mp.pi*d*d/(4*N))
        for j in range(N):
            theta = (2*j-d)*mp.pi/N
            actual = kappa*(-1)**j*root**(j*(j+1))
            predicted = square_root*mp.exp(mp.j*N*theta*theta/(4*mp.pi))
            maximum = max(maximum, abs(actual-predicted))
            assert abs(actual-predicted) < mp.mpf('1e-94')
            count += 1
        for e in range(-4, 5):
            for a in (-3, 0, 2):
                raw = (mp.exp(mp.j*mp.pi*d*d*(e+a)/(4*N))
                       *mp.exp(-mp.j*e*mp.pi*d/4+mp.j*e*mp.pi/8))
                reduced = (mp.exp(mp.j*mp.pi*d*d*a/(4*N))
                           *mp.exp(-mp.j*e*mp.pi/8+mp.j*e*mp.pi/(4*N)))
                assert abs(raw-reduced) < mp.mpf('1e-94')
    return {'high_precision_physical_nodal_phase_checks': count,
            'decimal_precision': 100,
            'method': 'High-precision numerical checks of the algebraically proved phase identities.',
            'maximum_absolute_error': float(maximum),
            'parity_safe_kappa_square_root_and_imbalance_phase': True}


def gaussian_calibrations():
    cases = [(0, 1, 0), (1, 0, 0), (0, 2, 0), (1, 2, 0), (3, 1, 0),
             (2, 2, 0), (0, 1, 3), (2, 1, -2), (1, 3, 5)]
    rows, errors = [], {}
    for N in (32, 33, 64, 65, 128, 129):
        root, coefficients = source_polynomial(N, max(180, N+80))
        d, j0 = N-1, 4*mp.catalan/mp.pi
        values, crossings = [], []
        for j in range(N):
            c = root**(2*j+1)+root**(-2*j-1)
            values.append(evaluate(coefficients, c)[0])
            crossings.append(mp.exp(mp.j*mp.pi*d*d/(2*N))*(-1)**j*root**(j*(j+1)))
        level_rows = []
        for index, (p, q, a) in enumerate(cases):
            n, e = p+q, q-p
            actual = N*mp.fsum(r**(e+a)*mp.conj(z)**p*z**q for r, z in zip(crossings, values))
            predicted = (mp.mpf(N)**mp.mpf('1.5')*2**(-mp.mpf(9*n)/4)
                         *mp.exp(mp.j*mp.pi*d*d*a/(4*N))
                         *mp.exp(-mp.j*e*mp.pi/8+mp.j*e*mp.pi/(4*N))
                         /mp.sqrt(n-mp.j*(e+a))*mp.exp(n*N*j0))
            ratio = actual/predicted
            errors[N, index] = abs(ratio-1)
            assert N*abs(ratio-1) < 40
            level_rows.append({'plus': p, 'minus': q, 'outer_a': a,
                               'complete_original_source_over_prediction': [float(mp.re(ratio)), float(mp.im(ratio))]})
        rows.append({'N': N, 'all_sign_and_fixed_outer_twist_profiles': level_rows})
        print(f'N={N} oneplus={mp.nstr(level_rows[1]["complete_original_source_over_prediction"], 10)} '
              f'outera5={mp.nstr(level_rows[-1]["complete_original_source_over_prediction"], 10)}', flush=True)
    for parity in (0, 1):
        for index in range(len(cases)):
            assert errors[128+parity, index] < errors[64+parity, index] < errors[32+parity, index]
    return rows


if __name__ == '__main__':
    results = {'status': 'PASS',
               'full_physical_original_sources': [physical_level(N) for N in range(2, 9)],
               'high_precision_complex_nodal_and_source_phase_checks': high_precision_complex_phases(),
               'supplementary_complete_gaussian_calibrations': gaussian_calibrations(),
               'scope': 'Original complete-belt operators, normal directions, signed words, outer powers '
                        'and high-precision all-parity nodal phase checks. Finite large-N profiles supplement the written '
                        'boundary-packet/Gaussian proof. Outer-twist topology requires its collar certificate.'}
    Path(__file__).with_name('actual_coherent_octahedral_belt_stack_asymptotic_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS: seven full physical levels/210 all-sign words/490 outer-twist sources; '
          '860 high-precision nodal phase checks; six complete all-parity Gaussian profile families.')
