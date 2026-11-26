#!/usr/bin/env python3
"""Bounded interval cover of correlated next-four endpoint budget (15).

Uses only the original rational reference maps and elementary scalar costs.
No root solve or finite quantum-source evaluation is performed. A proof
requires a complete cover; unresolved boxes are not word counterexamples.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx

import certify_mixed_next_four_endpoint_budget as frozen


base = frozen.base
THETAS = frozen.THETAS
CEILINGS = ('2/5', '81/200', '41/100', '83/200', '21/50')
PROOF = Path('notes/research_mixed_next_four_correlated_endpoint_budget.md')
FROZEN_PROOF = Path('notes/research_mixed_first_four_next_four_endpoint_budget.md')


def interval_record(value):
    return {'ball': str(value), 'lower': str(value.lower()),
            'upper': str(value.upper())}


def box_record(box):
    return list(map(str, box))


def inspect(box):
    pi, ii = arb.pi(), acb(0, 1)
    auxiliary = acb(base.ball(box[0], box[1]), base.ball(box[2], box[3]))
    U = (2*pi*ii*auxiliary).exp()
    shapes = {name: base.rational_enclosure(factors, U)
              for name, factors in frozen.MAPS.items()}
    coordinates = {}
    for name, shape in shapes.items():
        coordinate = ii*shape.log()/(2*pi)
        if not coordinate.is_finite():
            return 'split', 'nonfinite '+name+' coordinate', None
        lo, hi, hlo, hhi = map(base.rat, frozen.RANGES[name])
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
    E, Z, S, B_out = (shapes[name] for name in ('e', 'z', 's', 'b'))
    next_shape = ((1-S*B_out)
                  / (B_out*(1-S*B_out)+(1-B_out)**3))
    if next_shape.is_finite() and next_shape.imag.lower() > 0:
        return 'excluded', 'next external upper half-plane', None
    next_coordinate = ii*next_shape.log()/(2*pi)
    if (next_coordinate.is_finite()
            and base.outside_typed_domain(next_coordinate, 3)
            and base.outside_typed_domain(next_coordinate, 4)):
        return 'excluded', 'next external typed domains', None

    H = base.rat('1/100')
    R = (2*pi*H).exp()
    lam = R/abs(Z)
    ell = lam.log()
    A = (abs(1-lam*E*Z)/abs(1-E*Z)).log()
    B = (abs(1-lam*S*Z)/abs(1-S*Z)).log()
    C = (abs(1-lam*Z)/abs(1-Z)).log()
    a_star = (ii*(1+S)/(1-S)).real
    if not all(v.is_finite() for v in (A, B, C, ell, a_star)):
        return 'split', 'nonfinite scalar', None
    d = frozen.clipped_ball(ell-B, '0', '1')
    q = frozen.clipped_ball(coordinates['s'].real+coordinates['z'].real
                            -base.rat('1/2'), '.045', '.21')
    c = frozen.clipped_ball(coordinates['z'].imag, '-.078', '-.020')
    hs = frozen.clipped_ball(coordinates['s'].imag, '-.102', '-.001')
    if any(v is None for v in (d, q, c, hs)):
        return 'excluded', 'actual scalar ranges', None
    if a_star.upper() < base.rat('2/5'):
        return 'excluded', 'actual ordinary curvature', None

    # The exact gamma is decreasing in a_star>0. Use its same-box lower
    # endpoint, intersected with the proved actual-reference a_star>2/5.
    a_lower = max(a_star.lower(), base.rat('2/5').lower())
    mu_lower = min(a_lower, base.rat('7/16').lower())
    gamma_upper = (1/(2*(2*a_lower+mu_lower))).upper()
    vertical = base.rat('19/10')*pi*pi*(H-c)**2
    factorial_threshold = 2*pi*pi*H-pi/500

    # The uniform .42 ceiling is already proved for every retained actual
    # reference, so its coarse credit is always available. Other ceilings
    # require a strict whole-box ratio test, retaining the actual hs.
    forced_threshold = pi*(base.rat('27/500')+pi/1250)-pi/500
    ceiling_witness = 'uniform .42, coarse credit'
    ceiling_tests = []
    T, re = (-2*pi*hs).exp(), base.rat('8/9')
    for t_text in CEILINGS:
        t = base.rat(t_text)
        ae = -(2*pi*(base.rat('.306')+t)).cos()
        ass = -(2*pi*(base.rat('.22')+t)).cos()
        az = -(2*pi*t).cos()
        numerator = ((1+2*re*ae*R+re*re*R*R)
                     * (T*T+2*T*ass*R+R*R))
        denominator = (1+2*az*R+R*R)**2
        eligible = numerator < denominator
        test = {'t': t_text, 'eligible': bool(eligible),
                'denominator_minus_numerator':
                    interval_record(denominator-numerator)}
        if eligible:
            credit = ((base.rat('1/2')-t)/2
                      *((2*(pi*t).sin()).log()+arb(2).log())
                      +pi*H*(base.rat('1/2')-t))
            threshold = pi*credit-pi/500
            test['forced_threshold'] = interval_record(threshold)
            if threshold.lower() > forced_threshold.lower():
                forced_threshold = threshold
                ceiling_witness = t_text
        ceiling_tests.append(test)

    kappa, eta, rho = 10*pi*pi/11, 11*pi*pi/10, base.rat('3/50')
    trials, chosen, best_upper = [], None, None
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
        m = A-base.rat('163/298')*h
        horizontal = (gamma_upper*(1-theta)**2*d*d
                      +base.rat('45/298')*h*h+m*m/2+pi*tq_upper)
        budget = vertical+horizontal
        if not budget.is_finite():
            trials.append({'theta': theta_text, 'finite': False})
            continue
        accepted = (budget < factorial_threshold and budget < forced_threshold)
        trial = {'theta': theta_text, 'finite': True,
                 'horizontal_upper_enclosure': interval_record(horizontal),
                 'total_budget_upper_enclosure': interval_record(budget),
                 'factorial_slack': interval_record(factorial_threshold-budget),
                 'forced_slack': interval_record(forced_threshold-budget),
                 'accepted': bool(accepted)}
        trials.append(trial)
        if best_upper is None or budget.upper() < best_upper:
            best_upper = budget.upper()
            chosen = trial

    details = {
        'reference_scalar_enclosures': {
            name: interval_record(value) for name, value in
            (('c', c), ('h_s', hs), ('a_star', a_star), ('gamma_upper', gamma_upper),
             ('A', A), ('B', B), ('C', C), ('ell', ell), ('d', d), ('q', q))},
        'vertical': interval_record(vertical),
        'factorial_threshold': interval_record(factorial_threshold),
        'forced_threshold': interval_record(forced_threshold),
        'ceiling_witness': ceiling_witness, 'ceiling_tests': ceiling_tests,
        'best_trial': chosen, 'trials': trials,
    }
    accepted_trials = [trial for trial in trials if trial.get('accepted')]
    if accepted_trials:
        witness = accepted_trials[0]
        details['acceptance_theta'] = witness['theta']
        return 'accepted', 'both credits', details
    return 'split', 'combined budget not certified', details


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--max-cells', type=int, default=6000)
    parser.add_argument('--max-depth', type=int, default=20)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not (1 <= args.max_cells <= 6000 and 0 <= args.max_depth <= 24):
        parser.error('this bounded attempt permits at most 6000 cells and depth 24')
    ctx.prec = args.bits
    inputs = [Path(__file__), Path(frozen.__file__), Path(base.__file__),
              PROOF, FROZEN_PROOF]
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    started = time.monotonic()
    stack = [('', base.ROOT)]
    leaves, unresolved, counts, visited = [], [], Counter(), 0
    while stack and visited < args.max_cells:
        address, box = stack.pop()
        kind, reason, details = inspect(box)
        visited += 1
        if kind in ('accepted', 'excluded'):
            counts[kind] += 1
            leaf = {'address': address, 'status': kind, 'reason': reason}
            if kind == 'accepted':
                leaf['certificate'] = details
            leaves.append(leaf)
        elif len(address) >= args.max_depth:
            unresolved.append({'address': address, 'box': box_record(box),
                               'reason': reason, 'enclosures': details})
        else:
            children = base.split(box, len(address))
            stack.extend([(address+'1', children[1]),
                          (address+'0', children[0])])
    unresolved.extend({'address': address, 'box': box_record(box),
                       'reason': 'cell budget; box not inspected',
                       'enclosures': None} for address, box in stack)
    for p in inputs:
        if hashlib.sha256(p.read_bytes()).hexdigest() != hashes[str(p)]:
            raise RuntimeError('input changed during run: '+str(p))
    record = {
        'status': 'proved' if not unresolved else 'unresolved',
        'scope': 'Correlated next-four scalar budget (15), actual-reference superset only',
        'rational_evaluation': 'frozen Horner jets and whole-box complex mean value',
        'precision_bits': args.bits,
        'initial_auxiliary_rectangle': box_record(base.ROOT),
        'necessary_reference_ranges': frozen.RANGES,
        'necessary_filters': ['z,s,b reduced disks',
                              'z+s in [.545,.77], s+b in [.527,.77]',
                              'next external in K3 union K4',
                              'actual d,q ranges and a_star>2/5'],
        'height': '1/100', 'thetas': THETAS, 'ceiling_grid': CEILINGS,
        'gamma': '1/[2(2*a_star+min(a_star,7/16))], a_star=Re[i(1+S)/(1-S)]',
        'acceptance': 'one theta: 19*pi^2*(H-c)^2/10+Nhat_theta below both credits minus pi/500',
        'fallback_forced_credit': '27/500+pi/1250, established uniform .42 ceiling',
        'split_rule': 'bisect real and imaginary axes alternately, real first',
        'visited_cells': visited, 'terminal_counts': dict(counts),
        'unresolved_count': len(unresolved), 'max_cells': args.max_cells,
        'max_depth': args.max_depth, 'elapsed_seconds': time.monotonic()-started,
        'input_sha256': hashes, 'leaves': leaves, 'unresolved': unresolved,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k: record[k] for k in
                     ('status', 'visited_cells', 'terminal_counts',
                      'unresolved_count', 'elapsed_seconds')}))


if __name__ == '__main__':
    main()
