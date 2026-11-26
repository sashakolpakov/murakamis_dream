"""Outward diagnostic on the OLD complete cover; no refinement or new source grid.

Tests whether the original zero-height supports pay the two-edge reset debit.
Positive upper bounds are inconclusive, not counterexamples. No theorem is claimed.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import ast
import hashlib
import importlib.util
import itertools
import json
import time

from flint import arb, acb

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HELPER = ROOT / 'experiments/certify_mixed_partially_reset_right_support.py'
spec = importlib.util.spec_from_file_location('saved_reset_support', HELPER)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
w, ar = p.w, p.ar


def profiles(old):
    answer = {}
    for e, beta, c in ((0, 0, 0), (1, 1, 0), (0, 0, 1),
                       (0, 1, 1), (1, 0, 1), (1, 1, 1)):
        pp = [r for r in old['profiles'] if (r['e'], r['b'], r['c']) == (e, beta, c)]
        if beta:
            pp = [r for r in pp if r['name'] == 'part4' and F(r['h']) == 0]
            assert len(pp) == 2 and {r['sig'] for r in pp} == {0, 1}
            assert all(F(r['ylo']) == F(2, 5) and F(r['yhi']) == F(1, 2) for r in pp)
            values = [F(z['upper']) for z in pp[0]['grid']]
            assert values == [F(z['upper']) for z in pp[1]['grid']]
        else:
            assert len(pp) == 2 and {F(r['h']) for r in pp} == {F(-3, 100), F(1, 50)}
            neg, pos = sorted(pp, key=lambda r: F(r['h']))
            values = [F(2, 5)*F(a['upper'])+F(3, 5)*F(b['upper'])
                      for a, b in zip(neg['grid'], pos['grid'])]
        assert all([F(z['k']) for z in r['grid']] == p.GRID for r in pp)
        answer[e, beta, c] = values
    return answer


def restricted_profiles(old, zero_type_three=False):
    """The old tangent points, evaluated on the contained real interval [.45,.5]."""
    source = ROOT/'experiments/certify_mixed_right_core_support_grid.py'
    names = {'ar', 'g', 'gp', 'bound', 'endpoint_bound'}
    definitions = [n for n in ast.parse(source.read_text()).body
                   if isinstance(n, ast.FunctionDef) and n.name in names]
    assert len(definitions) == len(names)
    ns = dict(Q=F, arb=arb, acb=acb, pi=arb.pi(), ii=acb(0, 1))
    exec(compile(ast.Module(body=definitions, type_ignores=[]), str(source), 'exec'), ns)
    copied = json.loads(json.dumps(old))
    zero_values = {}
    if zero_type_three:
        row_points = {}
        for e in (0, 1):
            lo, hi = F(1, 5), F(2, 5)
            for _ in range(36):
                u = (lo+hi)/2
                derivative = ((2*(arb.pi()*ar(u)).cos()).log()+
                              (2*(arb.pi()*ar(u+F(9, 20))).sin()).log()-
                              (2+e)*(2*(arb.pi()*ar(u)).sin()).log())
                if derivative > 0:
                    lo = u
                else:
                    assert derivative < 0
                    hi = u
            row_points[e] = str((lo+hi)/2)
        for e, k in itertools.product((0, 1), p.GRID):
            candidates = [r for r in old['profiles'] if r['e'] == e and
                          (r['b'] == 0 or r['name'] == 'part4' and F(r['h']) == 0)]
            points = sorted({v['point'][0] for r in candidates for row in r['grid']
                             if F(row['k']) == k for v in row['trials']} | {row_points[e]})
            assert len(points) <= 8
            pp = dict(e=e, b=0, c=0, h='0', sig=0, ylo='9/20', yhi='1/2')
            values = [ns['bound'](pp, k, 0, [u, '9/20']) for u in points]
            # A minimum of independently valid tangent ceilings remains a ceiling.
            high = min(v.upper() for v in values)
            endpoint = ns['endpoint_bound'](pp, k, 0, '9/20').upper()
            high = max(high, endpoint)
            bound = F(int(float(high)*10**12)+2, 10**12)
            assert high < ar(bound)
            zero_values[e, k] = bound
    relevant = 0
    for row in copied['profiles']:
        if not (row['b'] == 0 or row['name'] == 'part4' and F(row['h']) == 0):
            continue
        assert F(row['ylo']) <= F(9, 20) and F(row['yhi']) == F(1, 2)
        row['ylo'] = '9/20'
        for support in row['grid']:
            k = F(support['k'])
            if zero_type_three and row['b'] == 0:
                support['upper'] = str(zero_values[row['e'], k])
                relevant += 1
                continue
            vals = [ns['bound'](row, k, v['q'], v['point']) for v in support['trials']]
            vals += [ns['endpoint_bound'](row, k, v['q'], v['point']) for v in support['endpoint_trials']]
            high = max(v.upper() for v in vals)
            # Exact rational ceiling, with strict outward confirmation.
            bound = F(int(float(high)*10**12)+2, 10**12)
            assert all(v < ar(bound) for v in vals)
            assert bound <= F(support['upper'])
            support['upper'] = str(bound)
            relevant += 1
    # profiles() also checks the original domains: use a small temporary copy
    # of their labels, after the numerical restriction has already been evaluated.
    for row in copied['profiles']:
        if row['b'] and row['name'] == 'part4':
            row['ylo'] = '2/5'
    assert relevant == 120
    return profiles(copied)


def cover(addresses):
    assert len(addresses) == len(set(addresses))
    leaves = set(addresses)
    nodes = {a[:j] for a in leaves for j in range(len(a))}
    assert not leaves & nodes
    assert all(n+'0' in leaves | nodes and n+'1' in leaves | nodes for n in nodes)
    assert '' in leaves | nodes


def test(case, bounds, supports):
    word, ta, tb, fa, fb = case
    w.faces[:] = [fa, fb]
    box = w.cert(word, ta, tb, bounds, -F(3, 25))
    assert box is not None, ('original root cell', case, bounds)
    T = p.response(box)
    a, s, b = [box['boxes'][j] for j in (1, 2, 3)]
    eta, e = word[:2]
    _, _, Hess = w.core.phase(s, a, b, eta, e)
    mids = [(bounds[k]+bounds[k+1])/2 for k in (0, 2)]
    center = w.cert(word, ta, tb, [mids[0], mids[0], mids[1], mids[1]], -F(3, 25))
    assert center is not None, ('original root midpoint', case, bounds)
    aa, ss, bb = [center['boxes'][j] for j in (1, 2, 3)]
    value, gradient, _ = w.core.phase(ss, aa, bb, eta, e)
    C = value-gradient[0]*aa-gradient[1]*bb
    differentials, velocities, kerr = [], [], [arb(0), arb(0)]
    for ell in range(2):
        qa = Hess[0][0]*T[1, ell]+Hess[0][1]*T[3, ell]
        qb = Hess[1][0]*T[1, ell]+Hess[1][1]*T[3, ell]
        xl, xh, yl, yh = map(F, w.RECTS[(ta, tb)[ell]])
        vel = acb(ar(xh-xl)) if (fa, fb)[ell] in (0, 2) else acb(0, ar(yh-yl))
        qa, qb = qa*vel, qb*vel
        radius = ar((bounds[2*ell+1]-bounds[2*ell])/2)
        differentials.append((qa, qb, -a*qa-b*qb, radius))
        velocities.append(vel)
        for j, q in enumerate((qa, qb)):
            kerr[j] += abs(q.real)*radius
    kappas = [gradient[j].real+arb(0, kerr[j].upper()) for j in range(2)]
    result = []
    for side, key in ((0, (e, e, 0)), (1, (e, eta, 1))):
        A, B = p.chord(supports[key], kappas[1-side])
        x, y = (acb(ar(F(1, 2))), acb(ar(-A))) if side == 0 else (acb(ar(-A)), acb(ar(F(1, 2))))
        low = (C+gradient[0]*x+gradient[1]*y).real
        for qa, qb, qc, radius in differentials:
            low -= abs((qa*x+qb*y+qc).real)*radius
        defect = ar(B)-low
        if side == 1:  # forward P-U-R: pair is U-R, P is its left external reference
            cp, cu = box['pp'][0].imag, a.imag
            cp0, cu0 = center['pp'][0].imag, aa.imag
            tp, tu = ta, eta
            qp, qu = F(11, 2), F(151, 20)
            orientation = 'EPUR'
        else:          # reverse R-U-P-E: pair is R-U, P is the following internal leg
            cp, cu = box['boxes'][5].imag, b.imag
            cp0, cu0 = center['boxes'][5].imag, bb.imag
            tp, tu = word[2], e
            qp, qu = F(151, 20), F(11, 2)
            orientation = 'RUPE'
        kp, ku = (F(0), qu) if tp == tu == 1 else (10-qp, F(10))
        residual = ar(B)-(C+gradient[0]*x+gradient[1]*y).real+ar(kp)*cp0**2+ar(ku)*cu0**2
        for ell, ((qa, qb, qc, radius), vel) in enumerate(zip(differentials, velocities)):
            if side == 1:
                dcp = vel.imag if ell == 0 else arb(0)
                dcu = (T[1, ell]*vel).imag
            else:
                dcp, dcu = (T[5, ell]*vel).imag, (T[3, ell]*vel).imag
            derivative = -(qa*x+qb*y+qc).real+2*ar(kp)*cp*dcp+2*ar(ku)*cu*dcu
            residual += abs(derivative)*radius
        # For the actual P4-U3-R geometry, the existing 100/101 theorem bounds
        # the debit by a constant. Apply the maximum principle ONLY to the raw
        # support defect, then add this constant: no window image is clipped.
        if side == 1 and (tp, tu) == (1, 0):
            hp, hu = (F(51, 1000), F(17, 1000)) if e == 0 else (F(53, 1000), F(25, 1000))
            constant_debit = F(9, 2)*hp**2+10*hu**2
            residual = defect+ar(constant_debit)
        result.append((orientation, tp, tu, defect.upper(), residual.upper()))
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--restrict-U', action='store_true')
    ap.add_argument('--zero-type-three', action='store_true')
    args = ap.parse_args()
    assert not args.zero_type_three or args.restrict_U
    start = time.monotonic()
    p.configure(256)
    paths = [Path(__file__), HELPER, w.HELPER if hasattr(w, 'HELPER') else w.SRC,
             ROOT/'experiments/certify_mixed_paired_right_transition_support.py',
             ROOT/'experiments/certify_mixed_real_small_support.py',
             ROOT/'experiments/certify_mixed_right_core_support_grid.py',
             ROOT/'notes/research_mixed_neighbor_conditioned_critical_boxes.md',
             ROOT/'experiments/certify_mixed_neighbor_conditioned_critical_boxes.py',
             ROOT/'repro/results/research-mixed-neighbor-conditioned-critical-boxes.json',
             ROOT/'repro/results/research-mixed-right-core-support-grid.json',
             ROOT/'repro/results/research-mixed-right-core-support-reference.json']
    bindings = {str(q.relative_to(ROOT)): hashlib.sha256(q.read_bytes()).hexdigest() for q in paths}
    data = json.loads(paths[-1].read_text())
    grid = json.loads(paths[-2].read_text())
    for rec in (data, grid):
        assert rec['status'] == 'passed'
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in rec.get(field, {}).items():
                assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest
                bindings[name] = digest
    cases = [(tuple(r['word']), *r['external'], *r['faces']) for r in data['cases']]
    expected = set(itertools.product(itertools.product((0, 1), repeat=3), range(2), range(2), range(4), range(4)))
    assert len(cases) == len(set(cases)) == 512 and set(cases) == expected
    supports = restricted_profiles(grid, args.zero_type_three) if args.restrict_U else profiles(grid)
    summary = {}
    cells = 0
    for index, (case, row) in enumerate(zip(cases, data['cases'])):
        cover(row['addresses'])
        for address in row['addresses']:
            assert time.monotonic()-start < 300, 'bounded diagnostic time cap'
            ans = test(case, p.decode(address), supports)
            cells += 1
            for orientation, tp, tu, raw, residual in ans:
                key = f'{orientation}:{tp}{tu}'
                rr = summary.setdefault(key, dict(cells=0, raw_upper=None, residual_upper=None, witness=None))
                rr['cells'] += 1
                if rr['raw_upper'] is None or raw > arb(rr['raw_upper']).upper():
                    rr['raw_upper'] = str(raw)
                if rr['residual_upper'] is None or residual > arb(rr['residual_upper']).upper():
                    rr['residual_upper'] = str(residual)
                    rr['witness'] = dict(word=list(case[0]), external=list(case[1:3]), faces=list(case[3:]), address=address)
                # Serialized intervals are outward. On an overlapping comparison
                # retain their upper endpoint, never choose an uncertain max ball.
                rr['raw_upper'] = str(max(raw, arb(rr['raw_upper']).upper()))
                rr['residual_upper'] = str(max(residual, arb(rr['residual_upper']).upper()))
        if (index+1) % 64 == 0:
            print('PROGRESS', index+1, cells, round(time.monotonic()-start, 3), flush=True)
    assert cells == data['accepted_cells'] == 5546
    assert bindings == {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in bindings}
    result = dict(scope='Outward diagnostic only, re-evaluating all OLD 512 domains/5546 cells with original source supports. No refinement, source optimization or new cover. Positive upper residual is inconclusive. Payer debit applies to unselected U height zero, not selected positive U corner.',
                  status='complete', restrict_U=args.restrict_U, zero_type_three=args.zero_type_three,
                  precision_bits=256, products=512, cells=cells, refinements=0,
                  by_typed_orientation=summary, dependencies=bindings, elapsed_seconds=time.monotonic()-start)
    name = ('direct-zero-support.json' if args.zero_type_three else
            'restricted-zero-support.json' if args.restrict_U else 'saved-zero-support.json')
    (HERE/name).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['by_typed_orientation'], indent=2), flush=True)


if __name__ == '__main__':
    main()
