#!/usr/bin/env python3
"""Bounded interval attempt for the next-four endpoint majorant.

This tests a new sufficient scalar inequality. It does not evaluate finite
quantum sources or solve critical equations. Unresolved cells are retained.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx

import certify_mixed_endpoint_log_budget as base


RANGES = {
    'e': ('.333', '.363', '-.051', '-.019'),
    'z': ('.246', '.350', '-.078', '-.020'),
    's': ('.240', '.360', '-.102', '-.001'),
    'b': ('.240', '.360', '-.102', '-.001'),
}
MAPS = dict(base.MAPS)
MAPS['b'] = (
    [(1, [-1]), (1, [3, -1]),
     (1, [793, -1375, 2097, -1839, 1283, -597, 179, -29]),
     (1, [985, -2449, 3885, -4085, 2923, -1523, 463, -71])],
    [(8, [1, 1]), (1, [17, -21, 19, -7]),
     (1, [41, -34, 36, -14, 3])],
)
THETAS = ('0', '1/4', '1/2', '3/4', '1')


def clipped_ball(value, lo, hi):
    lower = max(value.lower(), base.rat(lo).lower())
    upper = min(value.upper(), base.rat(hi).upper())
    if lower > upper:
        return None
    return arb((lower+upper)/2, (upper-lower)/2)


def inspect(box):
    pi, ii = arb.pi(), acb(0, 1)
    auxiliary = acb(base.ball(box[0], box[1]), base.ball(box[2], box[3]))
    U = (2*pi*ii*auxiliary).exp()
    shapes = {name: base.rational_enclosure(factors, U)
              for name, factors in MAPS.items()}
    coordinates = {}
    for name, shape in shapes.items():
        coordinate = ii*shape.log()/(2*pi)
        if not coordinate.is_finite():
            return 'split', 'nonfinite '+name+' coordinate', None
        lo, hi, hlo, hhi = map(base.rat, RANGES[name])
        if (coordinate.real.upper() < lo or coordinate.real.lower() > hi
                or coordinate.imag.upper() < hlo
                or coordinate.imag.lower() > hhi):
            return 'excluded', name+' range', None
        coordinates[name] = coordinate
    for name in ('z', 's', 'b'):
        if base.outside_disk(coordinates[name], '.30', '-.052', '.060'):
            return 'excluded', name+' reduced disk', None
    for names, lower in ((('z', 's'), '.545'), (('s', 'b'), '.527')):
        total = sum((coordinates[name].real for name in names), arb(0))
        if total.upper() < base.rat(lower) or total.lower() > base.rat('.77'):
            return 'excluded', '+'.join(names)+' sum', None
    E, Z, S, T = (shapes[name] for name in ('e', 'z', 's', 'b'))
    V = (1-S*T)/(T*(1-S*T)+(1-T)**3)
    if V.is_finite() and V.imag.lower() > 0:
        return 'excluded', 'next external upper half-plane', None
    next_coordinate = ii*V.log()/(2*pi)
    if (next_coordinate.is_finite()
            and base.outside_typed_domain(next_coordinate, 3)
            and base.outside_typed_domain(next_coordinate, 4)):
        return 'excluded', 'next external typed domains', None

    H = base.rat('1/100')
    lam = (2*pi*H).exp()/abs(Z)
    ell = lam.log()
    A = (abs(1-lam*E*Z)/abs(1-E*Z)).log()
    B = (abs(1-lam*S*Z)/abs(1-S*Z)).log()
    C = (abs(1-lam*Z)/abs(1-Z)).log()
    if not all(t.is_finite() for t in (A, B, C, ell)):
        return 'split', 'nonfinite increment', None
    # Actual references have 0<d<ell<1 and .045<q<.21.
    d = clipped_ball(ell-B, '0', '1')
    q = clipped_ball(coordinates['s'].real+coordinates['z'].real-base.rat('.5'),
                     '.045', '.21')
    if d is None or q is None:
        return 'excluded', 'actual scalar ranges', None
    kappa, eta, rho = 10*pi*pi/11, 11*pi*pi/10, base.rat('3/50')
    best = None
    for theta_text in THETAS:
        theta = base.rat(theta_text)
        a = theta*d
        positive = base.positive_upper(q*q-2*a/kappa)
        t_positive = (a*q-kappa*q*q*q/3
                      +kappa*positive*positive.sqrt()/3)
        t_negative = (a*(q+rho)-kappa*q*q*q/3
                      -kappa*rho*q*q/2+eta*rho*rho*rho/6)
        tq_upper = max(t_positive.upper(), t_negative.upper())
        h = 3*C-B-theta*d
        force = A-base.rat('163/298')*h
        majorant = (base.rat('5/8')*(1-theta)**2*d*d
                    +base.rat('45/298')*h*h+force*force/2+pi*tq_upper)
        if not majorant.is_finite():
            continue
        upper = majorant.upper()
        if best is None or upper < best:
            best = upper
        if majorant < pi*pi/384:
            return 'accepted', 'theta='+theta_text, str(upper)
    return 'split', 'majorant not certified', str(best)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--max-cells', type=int, default=6000)
    parser.add_argument('--max-depth', type=int, default=20)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    ctx.prec = args.bits
    started = time.monotonic()
    stack = [('', base.ROOT)]
    leaves, unresolved, counts, visited = [], [], Counter(), 0
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
            children = base.split(box, len(address))
            stack.extend([(address+'1', children[1]),
                          (address+'0', children[0])])
    unresolved.extend({'address': address, 'reason': 'cell budget'}
                      for address, _ in stack)
    proof = Path('notes/research_mixed_first_four_next_four_endpoint_budget.md')
    inputs = [Path(__file__), Path(base.__file__), proof]
    record = {
        'status': 'proved' if not unresolved else 'unresolved',
        'scope': 'Next-four five-trial scalar inequality (30) only',
        'precision_bits': args.bits,
        'initial_auxiliary_rectangle': list(map(str, base.ROOT)),
        'necessary_reference_ranges': RANGES,
        'height': '1/100', 'threshold': 'pi^2/384', 'thetas': THETAS,
        'split_rule': 'bisect real and imaginary axes alternately, real first',
        'visited_cells': visited, 'terminal_counts': dict(counts),
        'unresolved_count': len(unresolved), 'max_cells': args.max_cells,
        'max_depth': args.max_depth, 'elapsed_seconds': time.monotonic()-started,
        'input_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in inputs},
        'leaves': leaves, 'unresolved': unresolved,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in
                     ('status', 'visited_cells', 'terminal_counts',
                      'unresolved_count', 'elapsed_seconds')}))


if __name__ == '__main__':
    main()
