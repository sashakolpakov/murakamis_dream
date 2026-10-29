#!/usr/bin/env python3
"""Actual complete-layer closure defect survives the original knot source."""

from collections import defaultdict
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix, partial


def case(n, color):
    H = HardyNetwork(n, color)
    p, Q, x, F, iv = H.p, H.Q, H.x, H.fac, H.inv
    pp = [(-1)**j*pow(Q, j*(j-1)//2, p)*iv[j] % p for j in range(n)]
    pairs = [(i, j) for i in range(n) for j in range(n-i)]
    t0 = 2
    matrices, rows = {}, []
    for sign in (1, -1):
        raw = defaultdict(int)
        for i, j in pairs:
            b0 = F[i+j]*iv[i]*pp[j]*pow(x, -j, p) % p
            for r, k in pairs:
                for h, ell in pairs:
                    a, b = j+r, i
                    if sign > 0:
                        c, e = r+k-h, h+ell
                        power = i+j-k-ell
                        mid = F[r+k]*iv[r]*iv[k]*pow(x, -k, p) % p
                        final = F[h+ell]*iv[h]*pp[ell]*pow(x, -h-2*ell, p) % p
                        value = b0*mid*final % p
                    else:
                        c, e = r+k-ell, h+ell
                        power = i+j-k-h
                        mid = F[r+k]*iv[r]*pp[k]*pow(x, -k, p) % p
                        final = F[h+ell]*iv[h]*iv[ell]*pow(x, -ell, p) % p
                        order = k+h
                        gaussian = ((-1)**order*pow(x, 2*order, p)
                                    *pow(Q, -order*(order-1)//2, p)) % p
                        value = b0*mid*final*gaussian % p
                    assert e >= 0
                    key = power, a, b, c, e
                    raw[key] = (raw[key]+value) % p
        raw = {key: value for key, value in raw.items() if value}
        shifted = defaultdict(int)
        for (power, a, b, c, e), value in raw.items():
            shifted[power, a, b+n, c, e+n] += value
            shifted[power, a, b, c, e+n] -= value*pow(t0, -n, p)
        shifted = {key: value % p for key, value in shifted.items() if value % p}
        assert shifted, 'A times the unprojected actual layer must not be zero'

        def project(poly, orbit):
            out = np.zeros((n*n, n*n), dtype=np.int64)
            for (power, a, b, c, e), value in poly.items():
                if min(a, b, c, e) < 0 or max(a, b, c, e) >= n:
                    continue
                if (power % n if orbit else power) != 0:
                    continue
                multiplier = pow(t0, power, p) if orbit else 1
                row, col = c*n+e, a*n+b
                out[row, col] = (out[row, col]+value*multiplier) % p
            return out

        ct, average = project(raw, False), project(raw, True)
        assert not np.any(project(shifted, False))
        assert not np.any(project(shifted, True))
        # Substitute the adaptive Fermat root radius BEFORE the windows:
        # t0^-N=z1^-N-z7^-N. The only root-average alias is [t^-N]K.
        adaptive_correction = defaultdict(int)
        for (power, a, b, c, e), value in raw.items():
            if power != -n:
                continue
            adaptive_correction[0, a, b+n, c, e] += value
            adaptive_correction[0, a, b, c, e-n] -= value
        adaptive_correction = {key: value % p for key, value in adaptive_correction.items()
                               if value % p}
        assert adaptive_correction, 'The adaptive correction is nonzero before windows'
        assert not np.any(project(adaptive_correction, False))
        scalar = H.kappa if sign > 0 else pow(H.kappa, -1, p)
        literal = H.plus if sign > 0 else H.minus
        assert np.array_equal(scalar*ct % p, literal % p)
        # The D-inserted kernel equals the complete physical kernel at CT
        # and finite-orbit levels, although A*K was nonzero before projection.
        matrices[sign] = scalar*ct % p
        rows.append({'N': n, 'color': color, 'sign': sign,
                     'nonzero_raw_A_inserted_terms': len(shifted),
                     'complete_physical_A_insertion_zero': True,
                     'complete_physical_D_insertion_identity': True,
                     'same_relations_on_finite_root_orbit': True,
                     'adaptive_Fermat_sampling_preserves_physical_matrix_entrywise': True,
                     'adaptive_correction_nonzero_before_windows': len(adaptive_correction)})

    word = [1, -2, 1, -2]
    literal_word = word_matrix(word, H.plus, H.minus, 3, n, p)
    defect_word = word_matrix(word, matrices[1], matrices[-1], 3, n, p)
    literal_cut = partial(literal_word, H.pivot, 3, n, p)
    defect_cut = partial(defect_word, H.pivot, 3, n, p)
    assert np.array_equal(literal_cut % p, defect_cut % p)
    return rows, {'N': n, 'color': color,
                  'original_hyperbolic_word_full_cut_preserved': True,
                  'complete_defect_insertion_cut_nonzero': bool(np.any(defect_cut))}


def main():
    cases, words = [], []
    for n in range(2, 7):
        for color in (1, 3):
            local, word = case(n, color)
            cases.extend(local)
            words.append(word)
    a, b, c, d = sp.symbols('a b c d', nonzero=True)
    T = b*d/(d-b)
    norm_identities = []
    for s in (1, -1):
        first = T*(1/(s*a)-1/d)
        final = d*(1/b-1/(s*c))
        rogers = 1-c/a-c/(s*T)
        assert sp.cancel(rogers+(s*c/T)*first+(c/(s*d))*final) == 0
        assert sp.cancel(first.subs({c: s*b, d: s*a}, simultaneous=True)) == 0
        assert sp.cancel(final.subs({c: s*b, d: s*a}, simultaneous=True)) == 0
        assert sp.cancel(rogers.subs({c: s*b, d: s*a}, simultaneous=True)) == 0
        norm_identities.append({'s': s, 'adaptive_three_norms_generate_two_boundary_relations': True})
    result = {'original_complete_signed_layers': cases,
              'original_pivotal_hyperbolic_words': words,
              'symbolic_adaptive_boundary_norms': norm_identities,
              'scope': 'full finite-source insertion, not a multiplicative A=0 quotient'}
    path = Path(__file__).with_name('actual_orbit_closure_source_obstruction_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(cases)} original signed/color closure-defect and adaptive balanced sampling identities, '
          f'{len(words)} original pivotal whole-word cuts')


if __name__ == '__main__':
    main()
