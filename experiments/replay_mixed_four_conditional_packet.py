#!/usr/bin/env python3
"""Independent replay of the full physical type-four conditional certificate.

Uses the negative-frequency sine primitive, a rational exponential Hessian,
and an exact horizontal sweep of the parameter cover. No author code or
root solver is imported. Stored rational centers only propose self-maps.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time

from flint import arb, acb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=320)
    parser.add_argument('--output', type=Path, default=ROOT/
                        'repro/results/research-mixed-four-conditional-packet-replay.json')
    args = parser.parse_args()
    ctx.prec = args.precision
    start = time.monotonic()
    record_path = 'repro/results/research-mixed-four-conditional-packet.json'
    author_script = 'experiments/certify_mixed_four_conditional_packet.py'
    original_hash = digest(ROOT/record_path)
    record = json.loads((ROOT/record_path).read_text())
    assert record['status'] == 'passed'
    assert record['script_sha256'] == digest(ROOT/author_script)
    for path, value in record['dependencies_sha256'].items():
        assert digest(ROOT/path) == value, path
    assert record['parameter_domain'] == ['1/5', '9/20', '1/5', '9/20']
    assert record['root_box'] == ['6/25', '17/50', '-17/100', '1/100']
    assert record['endpoint_gap'] == '1/50'

    def ar(x):
        x = Q(x)
        return arb(x.numerator)/x.denominator

    def interval(l, u):
        return ar(l).union(ar(u))

    def square(z, radius):
        return acb(z.real+arb(0, ar(radius)), z.imag+arb(0, ar(radius)))

    pi, ii = arb.pi(), acb(0, 1)

    def jsine(z):
        # Opposite to the author's positive-frequency Li_2 expression.
        return ((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii) \
            -ii*pi*z*(1-z)/2

    def log_sine(z):
        return (2*(pi*z).sin()).log()

    def phase(s, alpha, beta):
        return (jsine(s+alpha)+jsine(s+beta)-3*jsine(s)
                +ii*pi*(s*(alpha-beta)+(s*s-s)/2))

    def gradient(s, alpha, beta):
        return (log_sine(s+alpha)+log_sine(s+beta)-3*log_sine(s)
                +ii*pi*(alpha-beta+s-ar('1/2')))

    def hessian(s, alpha, beta):
        U = (-2*pi*ii*s).exp()
        AU = (-2*pi*ii*(s+alpha)).exp()
        BU = (-2*pi*ii*(s+beta)).exp()
        return 2*pi*ii*(AU/(1-AU)+BU/(1-BU)-3*U/(1-U))

    def hessian_derivatives(s, alpha, beta):
        U = (-2*pi*ii*s).exp()
        AU = (-2*pi*ii*(s+alpha)).exp()
        BU = (-2*pi*ii*(s+beta)).exp()
        au, bu, uu = AU/(1-AU)**2, BU/(1-BU)**2, U/(1-U)**2
        return 4*pi*pi*(au+bu-3*uu), 4*pi*pi*au, 4*pi*pi*bu

    def supnorm(z):
        return max(abs(z.real).upper(), abs(z.imag).upper())

    def rows(z):
        return abs(z.real)+abs(z.imag)

    def contraction_cover(inv, box):
        """Exact subdivision of the root-square/parameter product rectangle."""
        pending = [(box, 0)]
        accepted = visited = 0
        maximum = None
        while pending:
            cell, depth = pending.pop()
            mids = [(lo+hi)/2 for lo, hi in cell]
            widths = [(hi-lo)/2 for lo, hi in cell]
            sc = acb(ar(mids[0]), ar(mids[1]))
            aa, bb = acb(ar(mids[2])), acb(ar(mids[3]))
            sb = acb(interval(*cell[0]), interval(*cell[1]))
            ab, bblock = acb(interval(*cell[2])), acb(interval(*cell[3]))
            ds, da, db = hessian_derivatives(sb, ab, bblock)
            enclosure = (hessian(sc, aa, bb)
                         +ds*acb(arb(0, ar(widths[0])), arb(0, ar(widths[1])))
                         +da*acb(arb(0, ar(widths[2])))
                         +db*acb(arb(0, ar(widths[3]))))
            bound = rows(1-inv*enclosure)
            visited += 1
            if bound < ar('1/2'):
                accepted += 1
                maximum = bound.upper() if maximum is None else max(maximum, bound.upper())
                continue
            assert depth < 18, ('Hessian product cover unresolved', cell, str(bound))
            axis = max(range(4), key=lambda axis: widths[axis])
            lo, hi = cell[axis]
            for ends in ((lo, mids[axis]), (mids[axis], hi)):
                child = list(cell)
                child[axis] = ends
                pending.append((tuple(child), depth+1))
        return maximum, accepted, visited

    exact = []
    A, B, U = sp.symbols('A B U')
    assert sp.expand((1-A*U)*(1-B*U)-A*(1-U)**3
                     -(1-A+(2*A-B)*U+A*(B-3)*U*U+A*U**3)) == 0
    exact.append('original exponential conditional cubic')
    rational = 2*U*(A/(1-A*U)+B/(1-B*U)-3/(1-U))
    cotangent = ((1+A*U)/(1-A*U)+(1+B*U)/(1-B*U)
                 -3*(1+U)/(1-U)+1)
    assert sp.factor(rational-cotangent) == 0
    exact.append('independent rational Hessian equals original cotangent derivative')
    r0 = rational/2
    assert sp.factor(U*sp.diff(r0, U)
                     -(A*U/(1-A*U)**2+B*U/(1-B*U)**2-3*U/(1-U)**2)) == 0
    exact.append('rational s-derivative for the mean-value Hessian cover')
    assert sp.factor(A*sp.diff(r0, A)-A*U/(1-A*U)**2) == 0
    exact.append('rational alpha-derivative for the mean-value Hessian cover')
    assert sp.factor(B*sp.diff(r0, B)-B*U/(1-B*U)**2) == 0
    exact.append('rational beta-derivative for the mean-value Hessian cover')

    leaves = record['leaves']
    assert len(leaves) == record['accepted_cells']
    codes = set()
    events = {}
    for index, leaf in enumerate(leaves):
        code = leaf['address']
        assert code not in codes and set(code) <= {'0', '1'}
        codes.add(code)
        box = [Q(1, 5), Q(9, 20), Q(1, 5), Q(9, 20)]
        for depth, bit in enumerate(code):
            axis = depth % 2
            low = 2*axis
            mid = (box[low]+box[low+1])/2
            box[low+1-int(bit)] = mid
        stored = list(map(Q, leaf['bounds']))
        assert box == stored, (code, box, stored)
        left, right, bottom, top = stored
        assert left < right and bottom < top
        events.setdefault(left, []).append((1, index, bottom, top))
        events.setdefault(right, []).append((-1, index, bottom, top))
    for code in codes:
        assert all(code[:j] not in codes for j in range(len(code)))
    # Independent exact horizontal sweep, not the author's recursive tree walk.
    active = {}
    cuts = sorted(events)
    assert cuts[0] == Q(1, 5) and cuts[-1] == Q(9, 20)
    slabs = 0
    for cut_index, cut in enumerate(cuts):
        for sign, index, bottom, top in sorted(events[cut]):
            if sign == -1:
                assert active.pop(index) == (bottom, top)
            else:
                assert index not in active
                active[index] = (bottom, top)
        if cut_index+1 == len(cuts):
            assert not active
            break
        running = Q(1, 5)
        for bottom, top in sorted(active.values()):
            assert bottom == running, (cut, running, bottom)
            running = top
        assert running == Q(9, 20)
        slabs += 1

    scalar_margins = []

    def positive(name, value):
        assert value > 0, (name, str(value))
        scalar_margins.append({'name': name, 'strict_margin': str(value)})

    positive('uniform cotangent comparison',
             (pi/5).cos()-(2*pi/5).cos()*(2*pi/5).cosh())
    positive('uniform negative real Hessian',
             pi*(pi/10).sin()/((2*pi/5).cosh()+(pi/10).cos())-ar('1/3'))
    positive('uniform Hessian modulus', 56-pi*(5*(pi/10).cot()+1))
    positive('left original real tail',
             (pi/5).sin()**2-2*(pi/10).sin()**3)
    positive('right original real tail below half',
             2*(9*pi/20).sin()**3-1)
    positive('right original real tail above half', 2*(pi/5).sin()-1)
    eps = ar('1/100000')
    positive('both horizontal aliases', pi*eps/2-4732*eps**2-ar('1/100000'))
    positive('entire vertical endpoint side',
             ar('11/100')**2/6-56*eps*ar('11/100')-28*eps**2-ar('1/600'))
    positive('adaptive contour height', ar('1/5')-ar('17/100')-eps)

    replay_rows = []
    min_gap = None
    max_contraction = None
    hessian_cover_accepted = hessian_cover_visited = 0
    for index, leaf in enumerate(leaves):
        al, ah, bl, bh = map(Q, leaf['bounds'])
        am, bm = (al+ah)/2, (bl+bh)/2
        alpha0, beta0 = acb(ar(am)), acb(ar(bm))
        alpha, beta = acb(interval(al, ah)), acb(interval(bl, bh))
        z = acb(ar(Q(leaf['center'][0])), ar(Q(leaf['center'][1])))
        radius, point_radius = Q(leaf['radius']), Q(leaf['point_radius'])
        assert point_radius == Q(1, 10**40)
        inv = 1/hessian(z, alpha0, beta0)
        zp = square(z, point_radius)
        point_contraction = rows(1-inv*hessian(zp, alpha0, beta0))
        point_error = supnorm(inv*gradient(z, alpha0, beta0))
        assert point_contraction < ar('1/2')
        assert point_error+point_contraction*ar(point_radius) < ar(point_radius)
        zs = square(z, radius)
        zr, zi = map(Q, leaf['center'])
        contraction, haccepted, hvisited = contraction_cover(inv, (
            (zr-radius, zr+radius), (zi-radius, zi+radius), (al, ah), (bl, bh)))
        hessian_cover_accepted += haccepted
        hessian_cover_visited += hvisited
        residual = supnorm(inv*gradient(z, alpha, beta))
        assert contraction < ar('1/2'), (index, leaf['address'], str(contraction))
        assert residual+contraction*ar(radius) < ar(radius), (index, str(contraction))
        assert zs.real > ar('6/25') and zs.real < ar('17/50')
        assert zs.imag > -ar('17/100') and zs.imag < ar('1/100')
        for argument in (zs, zs+alpha, zs+beta):
            assert argument.real > 0 and argument.real < 1
        gaps = []
        for cut in (Q(1, 10), Q(9, 20)):
            c = acb(ar(cut))
            base = (phase(zp, alpha0, beta0)-phase(c, alpha0, beta0)).real
            da = (log_sine(zs+alpha)-log_sine(c+alpha)+ii*pi*(zs-c)).real
            db = (log_sine(zs+beta)-log_sine(c+beta)-ii*pi*(zs-c)).real
            gap = base-abs(da)*ar((ah-al)/2)-abs(db)*ar((bh-bl)/2)
            assert gap > ar('1/50'), (index, leaf['address'], str(gap))
            gaps.append(str(gap))
            min_gap = gap.lower() if min_gap is None else min(min_gap, gap.lower())
        max_contraction = (contraction.upper() if max_contraction is None
                           else max(max_contraction, contraction.upper()))
        replay_rows.append({'address': leaf['address'],
                            'newton_contraction': str(contraction),
                            'newton_residual': str(residual),
                            'hessian_cover_accepted': haccepted,
                            'hessian_cover_visited': hvisited,
                            'endpoint_gaps': gaps})
        if (index+1) % 500 == 0:
            print(json.dumps({'replayed_cells': index+1}), flush=True)

    assert digest(ROOT/record_path) == original_hash, 'author artifact changed during replay'
    assert record['script_sha256'] == digest(ROOT/author_script)
    for path, value in record['dependencies_sha256'].items():
        assert digest(ROOT/path) == value, path
    dependencies = [record_path, author_script, *record['dependencies_sha256']]
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'replayed_parameter_cells': len(replay_rows),
        'exact_horizontal_cover_slabs': slabs,
        'point_and_parameter_newton_count': 2*len(replay_rows),
        'endpoint_gap_count': 2*len(replay_rows),
        'hessian_cover_accepted': hessian_cover_accepted,
        'hessian_cover_visited': hessian_cover_visited,
        'strict_scalar_count': len(scalar_margins), 'scalars': scalar_margins,
        'exact_identity_count': len(exact), 'exact_identities': exact,
        'minimum_endpoint_gap_lower_bound': str(min_gap),
        'maximum_newton_contraction_upper_bound': str(max_contraction),
        'replayed_cells': replay_rows, 'elapsed_seconds': time.monotonic()-start,
        'independence': ('No author imports or numerical root solver. Negative-frequency '
                         'Li_2 primitive; rational-exponential Hessian; exact address '
                         'reconstruction plus an independent horizontal rectangle sweep.'),
        'scope': ('Full real-neighbor parameter certificate and original branch/root/gap '
                  'inputs. The written contour proof supplies the all-level physical '
                  'conditional packet; no complex-neighbor or mixed-word source claim.'),
        'author_artifact_sha256': original_hash,
        'script_sha256': digest(Path(__file__)),
        'dependencies_sha256': {path: digest(ROOT/path) for path in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'status', 'replayed_parameter_cells', 'exact_horizontal_cover_slabs',
        'strict_scalar_count', 'exact_identity_count',
        'minimum_endpoint_gap_lower_bound', 'maximum_newton_contraction_upper_bound')}))


if __name__ == '__main__':
    main()
