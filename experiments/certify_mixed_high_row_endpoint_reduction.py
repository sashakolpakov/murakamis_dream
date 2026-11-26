#!/usr/bin/env python3
"""Certify the upper-row endpoint reduction for the mixed finite source."""
import argparse
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_high_row_endpoint_reduction.md'
BOX = tuple(map(Fraction, ('13/100', '1/2', '0', '57/1000', '0', '1')))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    if isinstance(value, Fraction):
        return arb(value.numerator) / value.denominator
    return arb(value)


def interval(lo, hi):
    return ar(lo).union(ar(hi))


def exact_algebra():
    t, R = sp.symbols('t R', positive=True)
    C, S, a, b, d = sp.symbols('C S a b d', real=True)
    identities = []

    def check(name, expression):
        assert sp.cancel(sp.expand(expression)) == 0, name
        identities.append(name)

    P = (R + 1/R - 2*C)*t*t - 4*S*t + R + 1/R + 2*C
    modulus = 1 + R**2 - 2*R*(C*(t*t-1) + 2*S*t)/(1+t*t)
    check('shifted squared modulus', modulus - R*P/(1+t*t))
    for epsilon in (0, 1):
        for orientation in (0, 1):
            original = (4*t*t/(1+t*t) * modulus * R**(-2*orientation)
                        * (1+t*t)**(2+epsilon) / 2**(4+2*epsilon))
            reduced = (t*t*P*(1+t*t)**epsilon
                       / (2**(2+2*epsilon)*R**(2*orientation-1)))
            check(f'row derivative eps={epsilon} orientation={orientation}',
                  original-reduced)
    P0 = a*t*t - b*t + d
    B0 = 2*a*t*t - sp.Rational(3, 2)*b*t + d
    for epsilon, B in ((0, B0), (1, B0*(1+t*t)+t*t*P0)):
        check(f'polynomial derivative eps={epsilon}',
              sp.diff(t*t*P0*(1+t*t)**epsilon, t)-2*t*B)
    s, c, K = sp.symbols('s c K', real=True)
    polynomial = (2*K-2*(c*c-s*s))*t*t - 8*s*c*t + 2*K+2*(c*c-s*s)
    positive_form = (2*K-2)*(1+t*t)+4*(s*t-c)**2
    check('nonnegative quadratic factorization',
          polynomial-positive_form-2*(1-s*s-c*c)*(t*t+1))
    return identities


def criterion(box, epsilon):
    yl, yh, hl, hh, wl, wh = box
    y = interval(yl, yh)
    height = interval(hl, hh)
    w = interval(wl, wh)
    pi = arb.pi()
    t = w*(pi*y).cos()/(pi*y).sin()
    t2 = t*t
    K = 2*(2*pi*height).cosh()
    C = 2*(2*pi*y).cos()
    b = 4*(2*pi*y).sin()
    a, d = K-C, K+C
    P = a*t2-b*t+d
    Q = t2*P*(1+t2)**epsilon
    threshold = 2**(2+2*epsilon)*(-2*pi*height).exp()
    if Q < threshold:
        return 0
    B = 2*a*t2-ar(Fraction(3, 2))*b*t+d
    if epsilon:
        B = B*(1+t2)+t2*P
    if B > 0:
        return 1
    return None


def verify_partition(addresses):
    ordered = sorted(addresses)
    assert len(set(ordered)) == len(ordered)
    assert all(not right.startswith(left)
               for left, right in zip(ordered, ordered[1:]))
    assert sum((Fraction(1, 2**len(a)) for a in ordered), Fraction(0)) == 1
    return ordered


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=192)
    parser.add_argument('--output', type=Path, default=ROOT /
                        'repro/results/research-mixed-high-row-endpoint-reduction.json')
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    script_hash, proof_hash = sha(__file__), sha(PROOF)
    dependencies = {
        p: sha(ROOT/p) for p in (
            'notes/research_mixed_right_half_source_reduction.md',
            'notes/research_mixed_boundary_strip_bounds.md')
    }
    identities = exact_algebra()
    start = time.time()
    cases = []
    for epsilon in (0, 1):
        stack = [('', list(BOX))]
        addresses = []
        counts = [0, 0]
        visited = 0
        while stack:
            address, box = stack.pop()
            visited += 1
            result = criterion(box, epsilon)
            if result is not None:
                addresses.append(address)
                counts[result] += 1
            else:
                assert len(address) < 36, (epsilon, address)
                k = 2*(len(address) % 3)
                middle = (box[k]+box[k+1])/2
                first, second = box[:], box[:]
                first[k+1] = middle
                second[k] = middle
                stack.extend(((address+'1', second), (address+'0', first)))
            assert visited < 200000
        addresses = verify_partition(addresses)
        case = {'epsilon': epsilon, 'addresses': addresses,
                'accepted_cells': len(addresses), 'visited_cells': visited,
                'below_threshold_cells': counts[0],
                'positive_derivative_cells': counts[1]}
        cases.append(case)
        print(json.dumps({k: v for k, v in case.items() if k != 'addresses'}), flush=True)
    assert sha(__file__) == script_hash and sha(PROOF) == proof_hash
    assert dependencies == {p: sha(ROOT/p) for p in dependencies}
    output = {
        'status': 'passed', 'precision_bits': args.precision,
        'exact_identity_count': len(identities), 'exact_identities': identities,
        'domain': {'y': ['13/100', '1/2'], 'absolute_height': ['0', '57/1000'],
                   'w': ['0', '1'], 'upper_rows': ['1/2', '1']},
        'cases': cases, 'case_count': len(cases),
        'accepted_cells': sum(c['accepted_cells'] for c in cases),
        'visited_cells': sum(c['visited_cells'] for c in cases),
        'elapsed_seconds': time.time()-start,
        'script_sha256': script_hash, 'proof_sha256': proof_hash,
        'dependencies': dependencies,
        'scope': ('Upper row maximum attained at u=1/2 or u=1, at right angle '
                  '1/2 and y in [13/100,1/2], for both original block types '
                  'and orientations. No small-angle or geometric gap claim.')
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+'\n')
    print('Certified', output['accepted_cells'], 'complete parameter boxes.', flush=True)


if __name__ == '__main__':
    main()
