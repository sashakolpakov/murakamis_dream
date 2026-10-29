#!/usr/bin/env python3
"""Actual Casimir-projector interval products and their sharp entropy barrier."""

import json
from pathlib import Path

import numpy as np
from scipy.special import spence


def J(x):
    return -np.imag(spence(1 - np.exp(2j * np.pi * np.asarray(x)))) / (2 * np.pi)


def profile(T, r, s, k):
    return (J(s) - J(r) + J(T-r) - J(T-s)
            - J(k-r) - J(s-k) - J(k+s) + J(k+r))


def continuous_checks():
    rng = np.random.default_rng(28102026)
    l = rng.uniform(0, 1, 12000)
    r = rng.uniform(0, 1, len(l)) * (1-l)
    s = r+l
    k = r+rng.uniform(0, 1, len(l))*l
    T = s+rng.uniform(0, 1, len(l))*(1-l)
    p = profile(T, r, s, k)
    envelope = -4*(J(l/2)+J((1-l)/2))
    barrier = float(-8*J(.25))
    assert np.max(p-envelope) < 2e-12
    assert np.max(envelope-barrier) < 2e-12
    # Both extrema of a periodic interval, including wrap through an integer.
    starts = rng.uniform(-2, 3, len(l))
    intervals = J(starts+l)-J(starts)
    assert np.min(intervals-2*J(l/2)) > -2e-12
    assert np.max(intervals+2*J((1-l)/2)) < 2e-12
    assert abs(profile(1., .25, .75, .5)-barrier) < 2e-13
    return {'physical_profiles': len(l), 'sharp_projector_rate': barrier,
            'max_profile_minus_envelope': float(np.max(p-envelope))}


def exact_root_products():
    rng = np.random.default_rng(88271)
    rows = []
    for N in (3, 4, 7, 8, 16, 31, 64, 127, 256):
        d = N-1
        logs = np.r_[0., np.log(2*np.sin(np.pi*np.arange(1, N)/N))]
        F = np.cumsum(logs)
        worst = 0.
        collisions = 0
        for _ in range(300):
            T = int(rng.integers(0, 2*d+1))
            lo, hi = max(0, T-d), min(T, d)
            r = int(rng.integers(lo, hi+1))
            s = int(rng.integers(r, hi+1))
            k = int(rng.integers(r, s+1))
            # These are the two literal numerator products in the physical frame.
            numerator = F[s]-F[r]+F[T-r]-F[T-s]
            denominator_one = F[k-r]+F[s-k]
            second_indices = [k+j+1 for j in range(r, s+1) if j != k]
            assert all(1 <= m <= 2*N-1 for m in second_indices)
            zero_count = sum(m == N for m in second_indices)
            assert zero_count <= 1
            collisions += zero_count
            denominator_two = sum(logs[m % N] for m in second_indices if m != N)
            exact_regular_log = numerator-denominator_one-denominator_two
            leading = N*profile(T/N, r/N, s/N, k/N)
            error = abs(exact_regular_log-leading)
            worst = max(worst, float(error))
            # Supplementary endpoint-uniform check; the analytic proof gives O(log N).
            assert error <= 20*np.log(N)
        rows.append({'N': N, 'physical_intervals': 300,
                     'single_collision_cases': collisions,
                     'max_regular_product_log_error': worst,
                     'error_over_log_N': worst/np.log(N)})
    return rows


def maximizing_profiles():
    rows = []
    barrier = float(-8*J(.25))
    for N in (16, 32, 64, 128, 256, 512, 1024):
        T, r, s, k = N, N//4, 3*N//4, N//2
        logs = np.r_[0., np.log(2*np.sin(np.pi*np.arange(1, N)/N))]
        F = np.cumsum(logs)
        indices = [k+j+1 for j in range(r, s+1) if j != k]
        regular = (F[s]-F[r]+F[T-r]-F[T-s]-F[k-r]-F[s-k]
                   -sum(logs[m % N] for m in indices if m != N))
        assert abs(regular-N*barrier) <= 20*np.log(N)
        rows.append({'N': N, 'regular_projector_log_rate': float(regular/N),
                     'sharp_profile_rate': barrier})
    return rows


def main():
    out = {'continuous': continuous_checks(),
           'literal_root_products': exact_root_products(),
           'maximizing_profile': maximizing_profiles(),
           'scope': 'sharp physical projector profile; coarse full-source twist bound, '
                    'not a sharp hyperbolic-volume theorem'}
    Path(__file__).with_name('actual_twist_block_projector_barrier_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS 12000 physical profiles, 2700 literal root intervals, '
          'wrap/collision endpoints and sharp projector barrier')


if __name__ == '__main__':
    main()
