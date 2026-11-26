#!/usr/bin/env python3
"""Bound the new endpoint logarithmic majorant; no source or root evaluation.

This is a bounded interval-cover attempt. Only a complete cover proves the
claimed inequality. An unresolved cell is not an actual-word counterexample.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx


ROOT = (Fraction(217, 1000), Fraction(234, 1000),
        Fraction(27, 1000), Fraction(45, 1000))
RANGES = {
    'e': ('.333', '.363', '-.051', '-.019'),
    'z': ('.246', '.350', '-.070', '-.020'),
    's': ('.267', '.433', '-.065', '.068'),
    'b': ('.267', '.433', '-.065', '.068'),
}

# Descending integer coefficients; these are the original rational maps
# expanded or factored before interval evaluation. In particular the outgoing
# leg is not evaluated by successively widening E, Z and S.
MAPS = {
    'e': ([(1, [1, 2, 1])], [(1, [5, -2, 1])]),
    'z': ([(1, [29, -36, 38, -20, 5])],
          [(2, [1, 1]), (1, [5, -2, 1])]),
    's': ([(1, [1, -1]), (6, [1, 1])],
          [(1, [17, -21, 19, -7]), (1, [41, -34, 36, -14, 3])]),
    'b': ([(1, [-1]), (1, [167, -289, 294, -194, 67, -13]),
           (1, [121, -191, 290, -222, 141, -51, 8])],
          [(8, [1, 1]), (1, [3, -1]), (1, [2, -1, 1])]),
}


def rat(value):
    q = Fraction(value)
    return arb(q.numerator) / q.denominator


def ball(lo, hi):
    return arb(rat((lo + hi) / 2), rat((hi - lo) / 2))


def split(box, depth):
    out = []
    axis = 2 * (depth % 2)
    midpoint = (box[axis] + box[axis + 1]) / 2
    for branch in (0, 1):
        child = list(box)
        child[axis + (0 if branch else 1)] = midpoint
        out.append(tuple(child))
    return out


def positive_upper(value):
    return max(arb(0), value.upper())


def polynomial_jet(coefficients, z):
    value, derivative = acb(0), acb(0)
    for coefficient in coefficients:
        derivative = derivative*z + value
        value = value*z + coefficient
    return value, derivative


def product_jet(factors, z):
    value, derivative = acb(1), acb(0)
    for power, coefficients in factors:
        p, dp = polynomial_jet(coefficients, z)
        derivative = derivative*p**power + value*power*p**(power-1)*dp
        value = value*p**power
    return value, derivative


def rational_enclosure(factors, z):
    """First-order complex mean-value enclosure on the entire input box."""
    numerator, denominator = factors
    center = acb(z.real.mid(), z.imag.mid())
    n0, _ = product_jet(numerator, center)
    d0, _ = product_jet(denominator, center)
    n, dn = product_jet(numerator, z)
    d, dd = product_jet(denominator, z)
    derivative = (dn*d-n*dd)/(d*d)
    return n0/d0 + derivative*(z-center)


def inspect(box):
    pi, ii = arb.pi(), acb(0, 1)
    auxiliary = acb(ball(box[0], box[1]), ball(box[2], box[3]))
    U = (2 * pi * ii * auxiliary).exp()
    shapes = {name: rational_enclosure(factors, U)
              for name, factors in MAPS.items()}
    E, Z, S = (shapes[name] for name in ('e', 'z', 's'))
    for name, shape in shapes.items():
        coordinate = ii * shape.log() / (2*pi)
        if not coordinate.is_finite():
            return 'split', 'nonfinite '+name+' coordinate', None
        lo, hi, hlo, hhi = map(rat, RANGES[name])
        if (coordinate.real.upper() < lo or coordinate.real.lower() > hi
                or coordinate.imag.upper() < hlo
                or coordinate.imag.lower() > hhi):
            return 'excluded', name, None

    H = rat('7/625')
    lam = (2*pi*H).exp() / abs(Z)
    ell = lam.log()
    A = (abs(1-lam*E*Z) / abs(1-E*Z)).log()
    B_log = (abs(1-lam*S*Z) / abs(1-S*Z)).log()
    C = (abs(1-lam*Z) / abs(1-Z)).log()
    d = ell-B_log
    h = 3*C-(B_log+ell)/2
    centered_force = A-rat('163/298')*h
    if not all(v.is_finite() for v in (A, B_log, C, d, h, centered_force)):
        return 'split', 'nonfinite increment', None
    # The proved actual-reference sign d>0 permits replacing its lower
    # interval endpoint by zero; only its upper bound enters these costs.
    dp = positive_upper(d)
    majorant = (rat('45/298')*h*h + centered_force*centered_force/2
                + rat('175/768')*dp*dp
                + rat('2/3')*rat('15/14').sqrt()*(dp/2)*(dp/2).sqrt()
                + rat('2/3')*rat('6/5').sqrt()*(dp/8)*(dp/8).sqrt())
    threshold = pi*pi/128
    if majorant.is_finite() and majorant < threshold:
        return 'accepted', 'majorant', str(majorant.upper())
    return 'split', 'majorant not certified', str(majorant)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--max-cells', type=int, default=6000)
    parser.add_argument('--max-depth', type=int, default=16)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    ctx.prec = args.bits
    started = time.monotonic()
    stack = [('', ROOT)]
    leaves, unresolved = [], []
    counts = Counter()
    visited = 0
    while stack and visited < args.max_cells:
        address, box = stack.pop()
        kind, reason, bound = inspect(box)
        visited += 1
        if kind in ('accepted', 'excluded'):
            counts[kind] += 1
            leaves.append({'address': address, 'status': kind,
                           'reason': reason, 'upper': bound})
        elif len(address) >= args.max_depth:
            unresolved.append({'address': address, 'reason': reason,
                               'enclosure': bound})
        else:
            children = split(box, len(address))
            stack.extend([(address+'1', children[1]),
                          (address+'0', children[0])])
    unresolved.extend({'address': address, 'reason': 'cell budget'}
                      for address, _ in stack)
    status = 'proved' if not unresolved else 'unresolved'
    proof = Path('notes/research_mixed_centered_endpoint_scalar_costs.md')
    record = {
        'status': status,
        'scope': 'centered scalar majorant (26) on the reference superset only',
        'rational_evaluation': 'Horner jets and whole-box complex mean value',
        'precision_bits': args.bits,
        'initial_auxiliary_rectangle': list(map(str, ROOT)),
        'necessary_reference_ranges': RANGES,
        'height': '7/625', 'threshold': 'pi^2/128',
        'split_rule': 'bisect real and imaginary axes alternately, real first',
        'visited_cells': visited, 'terminal_counts': dict(counts),
        'unresolved_count': len(unresolved),
        'max_cells': args.max_cells, 'max_depth': args.max_depth,
        'elapsed_seconds': time.monotonic()-started,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_sha256': hashlib.sha256(proof.read_bytes()).hexdigest(),
        'leaves': leaves, 'unresolved': unresolved,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in
                     ('status', 'visited_cells', 'terminal_counts',
                      'unresolved_count', 'elapsed_seconds')}))


if __name__ == '__main__':
    main()
