#!/usr/bin/env python3
"""Outward derivative bounds for a moving coordinate between two right neighbors.

Only elementary logarithms occur. The three parameter rectangles are fixed;
every saved binary split and all row/height switches are replayed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import time

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_two_right_neighbor_transport.md'
SOURCE = ROOT/'repro/results/research-mixed-raw-row-stationarity.json'
CASES = ((0, 0, F('-.03'), F('.02')),
         (1, 0, F('-.057'), F('-.02')),
         (1, 1, F(0), F(0)))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    value = F(value)
    return arb(value.numerator)/value.denominator


def gp(z):
    return (1-(-2*arb.pi()*acb(0, 1)*z).exp()).log()


def gpp(z):
    return arb.pi()*(arb.pi()*z).cot()-arb.pi()*acb(0, 1)


def values(box, alpha, selected):
    intervals = [ar(lo).union(ar(hi)) for lo, hi in box]
    middle = [ar((lo+hi)/2) for lo, hi in box]
    ii = acb(0, 1)

    def at(parameters, left, right, chi, q):
        t, c = parameters
        rho = (t-ar('0.1'))/ar('0.12')
        if selected:
            z = acb(t, ar('0.014'))
            velocity, zt, zc, vc = acb(1), acb(1), acb(0), acb(0)
        else:
            z = acb(t, c*rho)
            velocity = 1+ii*chi*c/ar('0.12')
            zt, zc, vc = 1+ii*c/ar('0.12'), ii*rho, ii*chi/ar('0.12')
        coefficient = 2+alpha-q
        K = gp(z+ar(left))+gp(z+ar(right))-coefficient*gp(z) \
            +2*arb.pi()*ii*(ar(right)+selected-q)
        Kz = gpp(z+ar(left))+gpp(z+ar(right))-coefficient*gpp(z)
        return (velocity*K).real, [
            (velocity*Kz*zt).real,
            (vc*K+velocity*Kz*zc).real,
        ]

    lowers, all_grads = [], []
    for left, right in itertools.product((F(1, 5), F(2, 5)), repeat=2):
        for chi in ((0,) if selected else (0, 1)):
            for q in ((0, 1) if selected else (0,)):
                direct, grad = at(intervals, left, right, chi, q)
                center, _ = at(middle, left, right, chi, q)
                if not all(x.is_finite() for x in [direct, center, *grad]):
                    return None, None
                mean = center-sum((abs(d)*ar((hi-lo)/2)
                                   for d, (lo, hi) in zip(grad, box)), arb(0))
                lowers.append(max(direct.lower(), mean.lower()))
                all_grads.append(grad)
    return min(lowers), all_grads


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT/
                    'repro/results/research-mixed-two-right-neighbor-transport.json')
    ap.add_argument('--max-visits', type=int, default=4095)
    ap.add_argument('--seconds', type=float, default=30)
    args = ap.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    source = json.loads(SOURCE.read_text())
    assert source['status'] == 'passed'
    assert source['row_endpoints'] == ['1/5', '2/5']
    assert source['moving_minimum_interval'] == ['3/25', '11/50']
    assert source['physical_branch_count'] == 12
    deps = {str(SOURCE.relative_to(ROOT)): sha(SOURCE)}
    for path, digest in source['dependencies_sha256'].items():
        assert sha(ROOT/path) == digest
        deps[path] = digest
    for path, digest in [
        ('notes/research_mixed_raw_row_stationarity.md', source['proof_sha256']),
        ('experiments/check_mixed_raw_row_stationarity.py', source['script_sha256'])]:
        assert sha(ROOT/path) == digest
        deps[path] = digest
    old, ih = None, None
    if args.input:
        ih = sha(args.input)
        old = json.loads(args.input.read_text())
        assert old['status'] == 'passed'
        assert old['proof_sha256'] == ph and old['script_sha256'] == sh
        assert old['dependencies_sha256'] == deps
        assert len(old['cases']) == len(CASES)
    start = time.monotonic()
    cases = []
    status = 'passed'
    for case_index, (alpha, selected, clo, chi) in enumerate(CASES):
        box0 = [(F('0.12'), F('0.22')), (clo, chi)]
        stack, nodes = [box0], []
        minimum = None
        leaves = visits = cursor = 0
        saved = None if old is None else old['cases'][case_index]
        if saved:
            assert saved['alpha'] == alpha and saved['selected'] == selected
            assert saved['coefficient_interval'] == [str(clo), str(chi)]
        while stack:
            if old is None and (visits >= args.max_visits or time.monotonic()-start > args.seconds):
                status = 'incomplete'
                break
            box = stack.pop()
            visits += 1
            node = None
            if saved:
                node = saved['nodes'][cursor]
                cursor += 1
                if node[0] == 'S':
                    assert node[1] in (0, 1)
                    axis = node[1]
                    lo, hi = box[axis]
                    assert lo < hi
                    mid = (lo+hi)/2
                    for pair in ((lo, mid), (mid, hi)):
                        child = list(box)
                        child[axis] = pair
                        stack.append(child)
                    nodes.append(node)
                    continue
                assert node == ['L']
            lower, gradients = values(box, alpha, selected)
            if lower is not None and lower > ar(F(1, 5)):
                leaves += 1
                minimum = lower if minimum is None else min(minimum, lower)
                nodes.append(['L'])
                continue
            assert saved is None, ('saved leaf failed', case_index, cursor, str(lower))
            if gradients is None:
                axis = max((hi-lo, j) for j, (lo, hi) in enumerate(box))[1]
            else:
                axis = max((max((abs(g[j])*ar(hi-lo)).upper() for g in gradients), j)
                           for j, (lo, hi) in enumerate(box))[1]
            lo, hi = box[axis]
            assert hi-lo > F(1, 2**24)
            mid = (lo+hi)/2
            nodes.append(['S', axis])
            for pair in ((lo, mid), (mid, hi)):
                child = list(box)
                child[axis] = pair
                stack.append(child)
        if saved:
            assert not stack and cursor == len(saved['nodes'])
            assert leaves == saved['accepted_cells'] and visits == saved['visited_cells']
        cases.append(dict(alpha=alpha, selected=selected,
                          coefficient_interval=[str(clo), str(chi)],
                          accepted_cells=leaves, visited_cells=visits,
                          remaining_boxes=len(stack), smooth_functions=8,
                          minimum_lower_bound=str(minimum), nodes=nodes))
        if status != 'passed':
            break
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert ih == sha(args.input)
    result = dict(status=status, precision_bits=args.precision, cases=cases,
                  derivative_lower_bound='1/5', proof_sha256=ph, script_sha256=sh,
                  dependencies_sha256=deps,
                  elapsed_seconds=time.monotonic()-start, critical_root_solves=0,
                  scope='Uniform local minimum-flow derivative between two immediate right neighbors, all center types and selections, .12<=t<=.22. No one-right-neighbor inequality, full mixed flow, finite kernel lower bound, or knot-family consequence.')
    if ih:
        result['input_sha256'] = ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(status.upper(), [(c['alpha'], c['selected'], c['accepted_cells'],
                           c['minimum_lower_bound']) for c in cases], flush=True)


if __name__ == '__main__':
    main()
