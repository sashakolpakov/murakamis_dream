#!/usr/bin/env python3
"""Exact rational finite checks for the stable alternating-section lemma.

These checks do not test an asymptotic theorem, a geometric capacity, or the
original source normalization. They test the new finite inequalities against
direct products, including both original parity cutoffs and endpoint factors.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def multiply_linear(coeffs, a, b):
    out = [F(0)] * (len(coeffs) + 1)
    for j, c in enumerate(coeffs):
        out[j] += a * c
        out[j + 1] += b * c
    return out


def evaluate(coeffs, t):
    out = F(0)
    for c in reversed(coeffs):
        out = out * t + c
    return out


def main():
    if not __debug__:
        raise SystemExit('Assertions must be enabled; do not run with -O.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('cap_stable_sections_results.json'))
    args = parser.parse_args()
    counts = {'polynomials': 0, 'direct_product_values': 0,
              'section_bounds': 0, 'mode_bounds': 0,
              'far_bounds': 0, 'squared_factor_bounds': 0}
    parities = set()
    T = F(17, 5)
    for N in range(3, 13):
        d, M = N - 1, N // 2 - 1
        parities.add(N % 2)
        cases = [
            [F(1, 2)] * d,
            [F((3 * j + 1) % 11 + 1, 13) for j in range(d)],
            [F(1, 100)] * (d // 2) + [F(9, 10)] * (d - d // 2),
            [F(0)] * (d - M) + [F(2, 3)] * M,
            [F(1)] * (M + 1) + [F(1, 3)] * (d - M - 1),
            [F(0)] * d,
            [F(1)] * d,
        ]
        for roots in cases:
            coeffs = [F(1)]
            for p in roots:
                coeffs = multiply_linear(coeffs, 1 - p, p)
            assert len(coeffs) == d + 1 and sum(coeffs) == 1
            assert all(coeffs[j] ** 2 >= coeffs[j - 1] * coeffs[j + 1]
                       for j in range(1, d))
            nu = sum(roots) / d
            k = sum(p * (1 - p) for p in roots) / d
            a, b = 1 - nu - k, nu - k
            RT = max(a, b, 1 - 4 * k, a / T + b * T - 2 * k)
            pM = coeffs[M]
            K = max(evaluate(coeffs, T) / T ** M, (d + 1) * pM)
            t0 = pM / coeffs[M + 1] if pM and coeffs[M + 1] else None
            grid = {F(0), F(1, 10), F(1, 2), F(1), F(2), T,
                    F(4), F(10), F(100)}
            if t0 is not None:
                grid |= {t0 / 2, t0, 2 * t0}
                assert evaluate(coeffs, t0) <= (d + 1) * pM * t0 ** M
                counts['mode_bounds'] += 1
            for t in sorted(grid):
                direct = F(1)
                for p in roots:
                    direct *= 1 - p - p * t
                assert direct == evaluate(coeffs, -t)
                counts['direct_product_values'] += 1
                section = sum((-1) ** j * coeffs[j] * t ** j
                              for j in range(M + 1))
                if t0 is not None:
                    bound = (abs(direct) if t <= t0 else 0) + pM * t ** M
                    assert abs(section) <= bound
                    counts['section_bounds'] += 1
                if t >= T:
                    assert abs(section) <= (K + pM) * t ** M
                    counts['far_bounds'] += 1
                if t <= 1:
                    assert direct ** 2 <= max(a, 1 - 4 * k) ** d
                    counts['squared_factor_bounds'] += 1
                elif t <= T:
                    assert direct ** 2 <= t ** d * RT ** d
                    counts['squared_factor_bounds'] += 1
            counts['polynomials'] += 1
    assert parities == {0, 1}
    result = {
        'scope': 'Exact finite rational inequalities for stable sections; no sampled asymptotic or geometric claim.',
        'levels': list(range(3, 13)),
        'cutoff': 'M=floor(N/2)-1, d=N-1',
        'tilt': str(T),
        'counts': counts,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_sha256': hashlib.sha256((Path(__file__).resolve().parents[1] / 'notes/research_cap_uniform_spectral_gap.md').read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
