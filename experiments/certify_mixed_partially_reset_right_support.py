#!/usr/bin/env python3
"""Missing zero-height right-core profiles and actual-window support ceilings."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.special import spence
from flint import arb, acb, acb_mat, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_partially_reset_right_support.md'
HELPER = ROOT / 'experiments/certify_mixed_paired_right_transition_support.py'
HELPER_HASH = hashlib.sha256(HELPER.read_bytes()).hexdigest()
sp = importlib.util.spec_from_file_location('partial_right_window', HELPER)
w = importlib.util.module_from_spec(sp)
sp.loader.exec_module(w)
assert HELPER_HASH == hashlib.sha256(HELPER.read_bytes()).hexdigest()
ar = w.ar
GRID = [F(-1, 5)+F(j, 20) for j in range(10)]
LIMIT = F(1, 200)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def configure(bits):
    global PI, II
    ctx.prec = bits
    PI, II = arb.pi(), acb(0, 1)
    w.P, w.I, w.m.PI, w.ns['PI'] = PI, II, PI, PI
    w.core.pi, w.core.ii = PI, II


def g(z):
    return (((-2*PI*II*z).exp()).polylog(2)-PI*PI/6)/(2*PI*II)


def J(x):
    return g(acb(ar(x))).real


def L(x):
    return (2*(PI*ar(x)).sin()).log()


def propose_support(e, k):
    gd = lambda z: (spence(1-np.exp(-2j*np.pi*np.asarray(z, dtype=complex)))-np.pi**2/6)/(2j*np.pi)
    jd = lambda x: gd(x).real
    ld = lambda x: np.log(2*np.sin(np.pi*x))
    kap = float(k)

    def core(z):
        u, y = z
        value = jd(.5+u)+jd(u+y)-(2+e)*jd(u)-1.5*jd(y)-kap*y
        grad = [np.log(2*np.cos(np.pi*u))+ld(u+y)-(2+e)*ld(u),
                ld(u+y)-1.5*ld(y)-kap]
        return -float(value), -np.array(grad)

    p = minimize(core, [.27, .3], jac=True, method='L-BFGS-B',
                 bounds=[(.2, .499999999), (.22, .45)],
                 options=dict(ftol=1e-14, gtol=1e-11, maxiter=100))
    # Convergence is not used: any rational interior tangent gives an upper bound.
    u = min(max(F(str(float(p.x[0]))), F(1, 5)), F(499999999, 10**9))
    y = min(max(F(str(float(p.x[1]))), F(11, 50)), F(9, 20))

    def endpoint(z):
        yy = z[0]
        return float(jd(yy)/2+kap*yy), np.array([ld(yy)/2+kap])

    q = minimize(endpoint, [.3], jac=True, method='L-BFGS-B',
                 bounds=[(.22, .45)], options=dict(ftol=1e-14, gtol=1e-11, maxiter=100))
    yy = min(max(F(str(float(q.x[0]))), F(11, 50)), F(9, 20))
    return [str(u), str(y)], str(yy)


def support_bounds(e, k, point, endpoint):
    u, y = map(F, point)
    yy = F(endpoint)
    assert F(1, 5) <= u < F(1, 2) and F(11, 50) <= y <= F(9, 20)
    assert F(11, 50) <= yy <= F(9, 20)
    value = J(F(1, 2)+u)+J(u+y)-(2+e)*J(u)-ar(F(3, 2))*J(y)-ar(k*y)
    du = (2*(PI*ar(u)).cos()).log()+L(u+y)-(2+e)*L(u)
    dy = L(u+y)-ar(F(3, 2))*L(y)-ar(k)
    upper = value+max((du*ar(v-u)).upper() for v in (F(1, 5), F(1, 2)))
    upper += max((dy*ar(v-y)).upper() for v in (F(11, 50), F(9, 20)))
    ev = -J(yy)/2-ar(k*yy)
    ed = -L(yy)/2-ar(k)
    ep = ev+max((ed*ar(v-yy)).upper() for v in (F(11, 50), F(9, 20)))
    return upper, ep


def source_grid(old_grid, saved=None):
    rows = []
    by_key = {}
    old = {} if saved is None else {(r['own_type'], F(r['kappa'])): r for r in saved}
    if saved is not None:
        assert len(old) == len(saved) == 20
        assert set(old) == set(itertools.product((0, 1), GRID))
    for e, k in itertools.product((0, 1), GRID):
        if saved is None:
            pt, ep = propose_support(e, k)
        else:
            pt, ep = old[e, k]['point'], old[e, k]['endpoint_point']
        vals = support_bounds(e, k, pt, ep)
        if saved is None:
            high = max(v.upper() for v in vals)
            upper = F(int(np.ceil(float(high)*10**8))+2, 10**8)
        else:
            upper = F(old[e, k]['upper'])
        assert all(v < ar(upper) for v in vals), (e, k, vals, upper)
        rows.append(dict(own_type=e, moving_type=1, kappa=str(k), point=pt,
                         endpoint_point=ep, upper=str(upper)))
        by_key[e, k] = upper
    profiles = {}
    for e, beta, c in ((0, 0, 0), (1, 1, 0), (0, 0, 1),
                       (0, 1, 1), (1, 0, 1), (1, 1, 1)):
        if beta:
            profiles[e, beta, c] = [by_key[e, k] for k in GRID]
        else:
            pp = [p for p in old_grid['profiles'] if (p['e'], p['b'], p['c']) == (e, 0, c)]
            assert len(pp) == 2 and {F(p['h']) for p in pp} == {F(-3, 100), F(1, 50)}
            neg = next(p for p in pp if F(p['h']) < 0)
            pos = next(p for p in pp if F(p['h']) > 0)
            assert all(F(p['grid'][j]['k']) == k for p in pp for j, k in enumerate(GRID))
            profiles[e, beta, c] = [F(2, 5)*F(neg['grid'][j]['upper'])+
                                    F(3, 5)*F(pos['grid'][j]['upper']) for j in range(10)]
    return rows, profiles


def decode(address):
    bounds = [F(0), F(1)]*2
    for j, bit in enumerate(address):
        assert bit in '01'
        k = 2*(j % 2)
        mid = (bounds[k]+bounds[k+1])/2
        bounds[k+1-int(bit)] = mid
    return bounds


def response(box):
    n = 6
    rr = [ar(v) for v in box['rad']]
    ee = box['ee']
    rho = max((sum((abs(ee[i, j])*rr[j] for j in range(n)), arb(0))/rr[i]).upper()
              for i in range(n))
    assert rho < 1
    de = acb_mat(n, 2)
    de[0, 0] = box['diff'](box['zz'][0]+box['p0'][0], box['hz'][0]+box['dp'][0])
    de[n-1, 1] = box['diff'](box['zz'][-1]+box['p0'][1], box['hz'][-1]+box['dp'][1])
    residual = box['Y']*((box['J0']*box['D']+box['E0'])+acb_mat(box['dj'])*box['D']+de)
    cur, total = residual, residual
    for _ in range(4):
        cur = ee*cur
        total = total+cur
    T = box['D']-total
    for j in range(2):
        mu = max((abs(residual[i, j])/rr[i]).upper() for i in range(n))
        tail = mu*rho**5/(1-rho)
        for i in range(n):
            rad = (rr[i]*tail).upper()
            T[i, j] += acb(arb(0, rad), arb(0, rad))
    return T


def chord(values, kappa):
    lo, hi = max(kappa.lower(), ar(GRID[0])), min(kappa.upper(), ar(GRID[-1]))
    assert lo <= hi
    i = max([0]+[j for j in range(10) if ar(GRID[j]) < lo])
    j = min([9]+[j for j in range(10) if ar(GRID[j]) > hi])
    if i == j:
        if j < 9:
            j += 1
        else:
            i -= 1
    A = (values[j]-values[i])/(GRID[j]-GRID[i])
    return A, values[i]-A*GRID[i]


def test(case, bounds, profiles):
    word, ta, tb, fa, fb = case
    w.faces[:] = [fa, fb]
    box = w.cert(word, ta, tb, bounds, -F(3, 25))
    if not box:
        return None, 'window'
    T = response(box)
    a, s, b = [box['boxes'][j] for j in (1, 2, 3)]
    eta, e = word[:2]
    _, _, Hess = w.core.phase(s, a, b, eta, e)
    mids = [(bounds[k]+bounds[k+1])/2 for k in (0, 2)]
    center = w.cert(word, ta, tb, [mids[0], mids[0], mids[1], mids[1]], -F(3, 25))
    if not center:
        return None, 'point window'
    aa, ss, bb = [center['boxes'][j] for j in (1, 2, 3)]
    value, gradient, _ = w.core.phase(ss, aa, bb, eta, e)
    C = value-gradient[0]*aa-gradient[1]*bb
    differentials, kerr = [], [arb(0), arb(0)]
    for ell in range(2):
        qa = Hess[0][0]*T[1, ell]+Hess[0][1]*T[3, ell]
        qb = Hess[1][0]*T[1, ell]+Hess[1][1]*T[3, ell]
        xl, xh, yl, yh = map(F, w.RECTS[(ta, tb)[ell]])
        vel = acb(ar(xh-xl)) if (fa, fb)[ell] in (0, 2) else acb(0, ar(yh-yl))
        qa, qb = qa*vel, qb*vel
        radius = ar((bounds[2*ell+1]-bounds[2*ell])/2)
        differentials.append((qa, qb, -a*qa-b*qb, radius))
        for j, q in enumerate((qa, qb)):
            kerr[j] += abs(q.real)*radius
    kappas = [gradient[j].real+arb(0, kerr[j].upper()) for j in range(2)]
    upper = []
    for side, key in ((0, (e, e, 0)), (1, (e, eta, 1))):
        A, B = chord(profiles[key], kappas[1-side])
        x, y = (acb(ar(F(1, 2))), acb(ar(-A))) if side == 0 else (acb(ar(-A)), acb(ar(F(1, 2))))
        low = (C+gradient[0]*x+gradient[1]*y).real
        for qa, qb, qc, radius in differentials:
            low -= abs((qa*x+qb*y+qc).real)*radius
        defect = ar(B)-low
        if not defect < ar(LIMIT):
            return None, 'support ceiling'
        upper.append(defect.upper())
    return max(upper), None


def validate():
    specs = [
        ('right-core-support-grid', 'certify_mixed_right_core_support_grid.py', 'research_mixed_right_core_support.md'),
        ('right-core-support-reference', 'certify_mixed_right_core_support_reference.py', 'research_mixed_right_core_support.md'),
        ('geometric-support-slopes', 'certify_mixed_geometric_support_slopes.py', 'research_mixed_geometric_support_slopes.md'),
        ('geometric-support-slopes-replay', 'replay_mixed_geometric_support_slopes.py', 'research_mixed_geometric_support_slopes.md'),
        ('all-endpoint-support', 'certify_mixed_all_endpoint_support.py', 'research_mixed_all_endpoint_support.md'),
        ('43-endpoint-support', 'check_mixed_43_endpoint_support.py', 'research_mixed_43_endpoint_support.md'),
        ('high-row-endpoint-reduction', 'certify_mixed_high_row_endpoint_reduction.py', 'research_mixed_high_row_endpoint_reduction.md'),
        ('right-half-source-reduction', 'check_mixed_right_half_source_reduction.py', 'research_mixed_right_half_source_reduction.md'),
        ('paired-right-transition-support', 'certify_mixed_paired_right_transition_support.py', 'research_mixed_paired_right_transition_support.md'),
    ]
    deps, recs = {}, {}
    for stem, script, proof in specs:
        pp, ss, rr = 'notes/'+proof, 'experiments/'+script, 'repro/results/research-mixed-'+stem+'.json'
        for path in (pp, ss, rr):
            deps[path] = sha(ROOT/path)
        rec = json.loads((ROOT/rr).read_text())
        assert rec['status'] == 'passed'
        assert rec['proof_sha256'] == deps[pp] and rec['script_sha256'] == deps[ss]
        for key in ('dependencies', 'dependencies_sha256'):
            for path, digest in rec.get(key, {}).items():
                assert sha(ROOT/path) == digest, (stem, path)
                if path in deps:
                    assert deps[path] == digest
                deps[path] = digest
        recs[stem] = rec
    extra = 'notes/research_mixed_right_half_block_bound.md'
    deps[extra] = sha(ROOT/extra)
    assert recs['right-core-support-grid']['support_values'] == 750
    return deps, recs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-partially-reset-right-support.json')
    parser.add_argument('--max-visits', type=int, default=50000)
    args = parser.parse_args()
    assert args.precision >= 160
    configure(args.precision)
    ph, sh = sha(PROOF), sha(__file__)
    deps, recs = validate()
    cases = [(word, ta, tb, fa, fb) for word in itertools.product((0, 1), repeat=3)
             for ta, tb, fa, fb in itertools.product(range(2), range(2), range(4), range(4))]
    assert len(cases) == len(set(cases)) == 512
    old, ih, saved_grid = None, None, None
    if args.input:
        ih = sha(args.input)
        previous = json.loads(args.input.read_text())
        assert previous['status'] == 'passed'
        assert previous['proof_sha256'] == ph and previous['script_sha256'] == sh
        assert previous['dependencies_sha256'] == deps
        saved_grid = previous['source_grid']
        old = {(tuple(r['word']), *r['external_types'], *r['faces']): r for r in previous['cases']}
        assert len(old) == len(previous['cases']) == 512 and set(old) == set(cases)
    source, profiles = source_grid(recs['right-core-support-grid'], saved_grid)
    print('source PASS', len(source), 'new outward support values', flush=True)
    seeds = {(tuple(r['word']), *r['external_types'], *r['faces']): r['addresses']
             for r in recs['geometric-support-slopes']['cases']}
    assert len(seeds) == 512 and set(seeds) == set(cases)
    rows, visits, start, worst = [], 0, time.monotonic(), None
    for case in cases:
        pending = list(reversed(old[case]['addresses'] if old else seeds[case]))
        accepted, maximum, reasons = [], None, {}
        while pending:
            address = pending.pop()
            visits += 1
            assert visits <= args.max_visits
            value, reason = test(case, decode(address), profiles)
            if value is None:
                assert old is None, (case, address, reason, 'saved cell failed')
                assert len(address) < 24, (case, address, reason)
                reasons[reason] = reasons.get(reason, 0)+1
                pending.extend((address+'1', address+'0'))
            else:
                accepted.append(address)
                maximum = value if maximum is None else max(maximum, value)
        codes = sorted(accepted)
        assert len(codes) == len(set(codes))
        assert all(not b.startswith(a) for a, b in zip(codes, codes[1:]))
        assert sum((F(1, 2**len(a)) for a in codes), F(0)) == 1
        worst = maximum if worst is None else max(worst, maximum)
        rows.append(dict(word=case[0], external_types=list(case[1:3]), faces=list(case[3:]),
                         addresses=codes, cells=len(codes), defect_upper=str(maximum), split_reasons=reasons))
        if len(rows) % 32 == 0:
            print('progress', len(rows), 512, visits, str(worst), 'seconds', time.monotonic()-start, flush=True)
    assert ph == sha(PROOF) and sh == sha(__file__) and sha(HELPER) == HELPER_HASH
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert ih == sha(args.input)
    out = dict(status='passed', precision_bits=args.precision, source_values=20,
               source_grid=source, reference_products=512, reference_cells=sum(r['cells'] for r in rows),
               visited_cells=visits, worst_core_defect_upper=str(worst), strict_core_ceiling=str(LIMIT),
               finite_source_ceiling='1/100', moving_real_interval=['11/50', '9/20'],
               source_records=len(recs), cases=rows, proof_sha256=ph, script_sha256=sh,
               dependencies_sha256=deps, elapsed_seconds=time.monotonic()-start,
               replay_scope='Source rational tangent points and exact reference subdivisions are saved; original window root proposals are rechecked by complete interval self-maps.',
               scope='Whole original right-half block with moving plateau height anywhere between its prescribed selected/unselected height and zero; positive finite defect ceiling1/100, all rows/parities/selections. No general exterior or whole-cycle assertion.')
    if args.input:
        out.update(input_path=str(args.input), input_sha256=ih)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', 20, 512, out['reference_cells'], visits, time.monotonic()-start, flush=True)


if __name__ == '__main__':
    main()
