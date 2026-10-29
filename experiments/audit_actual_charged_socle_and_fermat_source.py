#!/usr/bin/env python3
"""Actual charged source: finite-flat residue, nilpotent socle and root orbits."""

import itertools
import json
from pathlib import Path

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import setup, charged_data, charged_coefficient


def lam_monomial(exponents, centers, n, p):
    value = 1
    for exponent, center in zip(exponents, centers):
        power, remainder = divmod(exponent, n)
        if remainder != n-1:
            return 0
        value = value*pow(center, power, p) % p
    return value


def algebra_checks():
    rows = []
    for n in range(2, 10):
        H = HardyNetwork(n, 1)
        p, d = H.p, n-1
        pairs = 0
        for k in (1, 2):
            basis = list(itertools.product(range(n), repeat=k))
            for centers in ([0]*k, list(range(2, 2+k))):
                for a in basis:
                    for b in basis:
                        powers = tuple(x+y for x, y in zip(a, b))
                        assert lam_monomial(powers, centers, n, p) == int(all(t == d for t in powers))
                        pairs += 1
        k, roots = 2, [2, 3]
        centers = [pow(r, n, p) for r in roots]
        monomials = [(d, d), (d+n, d), (2*d, 0), (0, 2*d), (0, 0)]
        for powers in monomials:
            direct = 0
            for labels in itertools.product(range(n), repeat=k):
                values = [r*pow(H.Q, ell, p) % p for r, ell in zip(roots, labels)]
                term = 1
                for value, exponent in zip(values, powers):
                    term = term*pow(value, exponent-d, p) % p
                direct = (direct+term) % p
            direct = direct*pow(n**k, -1, p) % p
            assert direct == lam_monomial(powers, centers, n, p)
        for e in range(2*d+1):
            powers = (e, 2*d-e)
            assert lam_monomial(powers, centers, n, p) == lam_monomial(powers, [0, 0], n, p)
        rows.append({'N': n, 'complete_basis_pairing_checks': pairs,
                     'grid_residue_normalization_and_top_homogeneous_flatness': True})
    return rows


def full_orbit_factor(forms, H):
    """Detect full root orbit on one anchor pair; never infer converse."""
    p, n = H.p, H.N
    grouped = {}
    for form in forms:
        if len(form) != 2:
            continue
        i, j = sorted(form)
        ratio = -int(form[j])*pow(int(form[i]), -1, p) % p
        grouped.setdefault((i, j), set()).add(ratio)
    for pair, ratios in grouped.items():
        for ratio in ratios:
            if all(ratio*pow(H.Q, r, p) % p in ratios for r in range(n)):
                return pair
    return None


def actual_source_checks():
    rows = []
    for n in (2, 3, 4):
        H = HardyNetwork(n, 1)
        for width, word in [(3, [1, -2, 1, -2]), (2, [1, 1]),
                            (3, [1, 1, 1, 2, -1, 2])]:
            S = setup(H, width, word)
            detected = []
            examined = 0
            for clocks in itertools.product(range(n), repeat=len(word)):
                if any(any(clocks[a] < clocks[b] for a, b in zip(path, path[1:])) for path in S['paths']):
                    continue
                forms, _, _, _ = charged_data(H, S, clocks)
                if full_orbit_factor(forms, H) is not None:
                    detected.append(clocks)
                examined += 1
            samples = sorted(set([int(j*(len(detected)-1)/11) for j in range(12)])) if detected else []
            for index in samples:
                forms, _, _, _ = charged_data(H, S, detected[index])
                assert charged_coefficient(forms, len(S['events']), n-1, H.p) == 0
            if word != [1, -2, 1, -2]:
                assert detected and samples
            rows.append({'N': n, 'word': word, 'actual_clock_states': examined,
                         'complete_orbit_sectors_detected': len(detected),
                         'independently_expanded_zero_coefficients': len(samples),
                         'criterion_is_sufficient_only': True})
    return rows


def main():
    result = {'status': 'PASS', 'finite_flat_source_pairings': algebra_checks(),
              'actual_source_orbit_annihilation': actual_source_checks(),
              'scope': 'Canonical fixed-level residue/jet source; no cross-level growth or noncancellation claim.'}
    Path(__file__).with_name('actual_charged_socle_and_fermat_source_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS eight finite-flat source families and actual charged full-orbit annihilation checks')


if __name__ == '__main__':
    main()
