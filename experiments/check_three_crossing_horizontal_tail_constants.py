#!/usr/bin/env python3
"""Exact rational checks for horizontal concavity and two wire tails.

No sampled Hessian or contour assertion is used. The selected heights
are read from the existing outward root certificate, whose hashes are
checked before use.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    pi_lo, pi_hi = F(157, 50), F(22, 7)
    a0 = pi_lo / 10
    sine_lower = a0 - a0**3 / 6
    attenuation = []
    for height, target in [(F(3, 40), F(8, 5)),
                           (F(13, 200), F(3, 2))]:
        t = pi_hi * height
        assert t*t < 6
        sinh_upper = t / (1-t*t/6)
        bound = 1+(sinh_upper/sine_lower)**2
        assert bound < target
        attenuation.append(str(bound))
    assert a0+a0**3/3 > F(8, 25)
    a, b, v = F(8, 5), F(3, 8), F(8, 25)
    assert a*(a-b)*(1+v*v) > F(1469, 1000)**2
    rank_bound = a+(2*a-b)*v*v-2*v*F(1469, 1000)
    assert rank_bound == F(2966, 3125) < F(19, 20)

    # Finite positive exponential sums prove the logarithmic constants.
    for exponent, target, order in [(F(7, 10), F(2), 6),
                                     (F(4), F(25), 9),
                                     (F(5), F(100), 10)]:
        term = F(1)
        total = term
        for j in range(1, order+1):
            term *= exponent/j
            total += term
        assert total > target
    two_b2_bound = 4*F(229, 250)/pi_lo
    assert two_b2_bound < F(146, 125)
    z_tail = F(146, 125)+F(157, 1000)+F(1, 1000)
    p_tail = F(146, 125)+F(67, 4000)+F(1, 3)+F(1, 1000)
    assert z_tail == F(663, 500) < F(153, 100)
    assert p_tail == F(18229, 12000) < F(153, 100)

    certificate = ROOT/'repro/results/research-three-crossing-closing-action.json'
    record = json.loads(certificate.read_text())
    assert record['status'] == 'passed'
    source = ROOT/'experiments/verify_three_crossing_closing_action.py'
    assert record['script_sha256'] == sha(source)
    dependencies = {str(source.relative_to(ROOT)): sha(source)}
    for name, digest in record['dependency_sha256'].items():
        assert sha(ROOT/name) == digest
        dependencies[name] = digest
    for key, bound in [('remaining_color_x', F(3, 40)),
                       ('remaining_color_y', F(13, 200))]:
        lo, hi = map(F, record[key]['imaginary'])
        assert -bound < lo <= hi < bound

    return {
        'status': 'passed',
        'method': 'Exact rational inequalities; no sampled Hessian proof.',
        'attenuation_upper_bounds': attenuation,
        'rank_one_upper_bound': str(rank_bound),
        'small_k_tail_rate_upper_bound': str(z_tail),
        'small_j_minus_k_tail_rate_upper_bound': str(p_tail),
        'selected_height_certificate': str(certificate.relative_to(ROOT)),
        'selected_height_certificate_sha256': sha(certificate),
        'dependency_sha256': dependencies,
        'script_sha256': sha(Path(__file__).resolve()),
        'scope': 'Constants for proved horizontal concavity and real wire tails; no original-cycle transfer.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-three-crossing-horizontal-tail-constants.json')
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('All exact horizontal-concavity and wire-tail constants passed.')
    print(f'Saved {args.output}')
