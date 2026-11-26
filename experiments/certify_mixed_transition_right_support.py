#!/usr/bin/env python3
"""Full transition-cap/right-half source profiles and actual-window support gaps."""
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
PROOF = ROOT / 'notes/research_mixed_transition_right_support.md'
HELPER = ROOT / 'experiments/certify_mixed_paired_right_transition_support.py'
HELPER_HASH = hashlib.sha256(HELPER.read_bytes()).hexdigest()
sp = importlib.util.spec_from_file_location('partial_right_window', HELPER)
w = importlib.util.module_from_spec(sp)
sp.loader.exec_module(w)
assert HELPER_HASH == hashlib.sha256(HELPER.read_bytes()).hexdigest()
ar = w.ar
GRID = [F(-1, 5)+F(j, 20) for j in range(10)]
LIMIT = -F(1, 1000)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def configure(bits):
    global PI, II, pi, ii
    ctx.prec = bits
    PI, II = arb.pi(), acb(0, 1)
    pi, ii = PI, II
    w.P, w.I, w.m.PI, w.ns['PI'] = PI, II, PI, PI
    w.core.pi, w.core.ii = PI, II


Q = F

def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator

def g(z):return (((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)).real

def gp(z):return (1-(-2*pi*ii*z).exp()).log().real

def ev(u,y,p,k,q):
 e,b,c=p['e'],p['b'],p['c'];h=float(Q(p['h']));H=abs(h);hp=max(h,0);sig=p['sig']
 gg=lambda z:((spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)).real
 lp=lambda z:np.log(abs(1-np.exp(-2j*np.pi*z)))
 cu=2*np.pi*(hp-c*h);co=np.pi*hp*(b-q/2)-b*np.pi*sig*h;kap=float(k)+q*np.pi*hp
 val=gg(.5+u)+gg(y+u-1j*H)-(1+q/2)*gg(y-1j*H)-(2+e)*gg(u)+cu*u+co-kap*y
 du=np.log(2*np.cos(np.pi*u))+lp(y+u-1j*H)-(2+e)*np.log(2*np.sin(np.pi*u))+cu
 dy=lp(y+u-1j*H)-(1+q/2)*lp(y-1j*H)-kap
 return val,np.array([du,dy])

def bound(p,k,q,pt):
 e,b,c=p['e'],p['b'],p['c'];h=Q(p['h']);H=abs(h);hp=max(h,Q(0));sig=p['sig'];lo=Q(p['ylo']);hi=Q(p['yhi']);u,y=map(Q,pt)
 cu=2*pi*ar(hp-c*h);co=pi*ar(hp)*(b-ar(Q(q,2)))-b*pi*ar(sig*h);kap=ar(k)+q*pi*ar(hp);z=acb(ar(y+u),-ar(H));w=acb(ar(y),-ar(H))
 val=g(acb(ar(Q(1,2)+u)))+g(z)-(1+ar(Q(q,2)))*g(w)-(2+e)*g(acb(ar(u)))+cu*ar(u)+co-kap*ar(y)
 du=(2*(pi*ar(u)).cos()).log()+gp(z)-(2+e)*(2*(pi*ar(u)).sin()).log()+cu
 dy=gp(z)-(1+ar(Q(q,2)))*gp(w)-kap
 sup=val+max((du*ar(x-u)).upper()for x in[Q(1,5),Q(1,2)])+max((dy*ar(x-y)).upper()for x in[lo,hi])
 return sup

def endpoint_ev(y,p,k,q):
 e,b,c=p['e'],p['b'],p['c'];h=float(Q(p['h']));hp=max(h,0);H=abs(h);sig=p['sig']
 gg=lambda z:((spence(1-np.exp(-2j*np.pi*z))-np.pi*np.pi/6)/(2j*np.pi)).real
 lp=lambda z:np.log(abs(1-np.exp(-2j*np.pi*z)))
 co=2*np.pi*(hp-c*h)+np.pi*hp*(b-q/2)-b*np.pi*sig*h;kap=float(k)+q*np.pi*hp
 return -q/2*gg(y-1j*H)+co-kap*y,-q/2*lp(y-1j*H)-kap

def endpoint_bound(p,k,q,yt):
 b,c=p['b'],p['c'];h=Q(p['h']);hp=max(h,Q(0));H=abs(h);sig=p['sig'];y=Q(yt);lo=Q(p['ylo']);hi=Q(p['yhi']);z=acb(ar(y),-ar(H))
 co=2*pi*ar(hp-c*h)+pi*ar(hp)*(b-ar(Q(q,2)))-b*pi*ar(sig*h);kap=ar(k)+q*pi*ar(hp)
 val=-ar(Q(q,2))*g(z)+co-kap*ar(y);dy=-ar(Q(q,2))*gp(z)-kap
 return val+max((dy*ar(x-y)).upper()for x in[lo,hi])

def profile_specs():
    rows = []
    intervals = [(F(13,100),F(13,100)),(F(13,100),F(4,25)),
                 (F(4,25),F(19,100)),(F(19,100),F(11,50))]
    for e,b,c in ((0,0,0),(1,1,0),(0,0,1),(0,1,1),(1,0,1),(1,1,1)):
        for sig in range(b+1):
            for j,(lo,hi) in enumerate(intervals):
                rho = (hi-F(1,10))/F(3,25)
                hs = [-F(3,100)*rho,F(1,50)*rho] if not b else ([F(0),F(7,500)] if sig else [-F(57,1000)*rho,F(0)])
                for h in sorted(set(hs)):
                    rows.append(dict(e=e,b=b,c=c,sig=sig,h=str(h),ylo=str(lo),yhi=str(hi),name='small' if j==0 else f'part{j}'))
    assert len(rows)==72
    return rows


def source_grid(saved=None):
    specs=profile_specs()
    if saved is not None:
        assert len(saved)==len(specs)
        assert all(len(row['grid'])==10 for row in saved)
        assert all({k:row[k] for k in p}==p for row,p in zip(saved,specs))
    rows=[]
    for index,p in enumerate(specs):
        lo,hi=F(p['ylo']),F(p['yhi']); vals=[]
        for j,k in enumerate(GRID):
            old=None if saved is None else saved[index]['grid'][j]
            if old is not None:
                assert F(old['k'])==k
                assert [v['q'] for v in old['trials']]==sorted(set((0,p['b'])))
                assert [v['q'] for v in old['endpoint_trials']]==sorted(set((0,p['b'])))
            trials=[]; endpoints=[]; uppers=[]
            for qi,q in enumerate(sorted(set((0,p['b'])))):
                if old is None:
                    opt=minimize(lambda z:(-ev(*z,p,k,q)[0],-ev(*z,p,k,q)[1]),[.28,float((lo+hi)/2)],jac=True,
                                 bounds=[(.20000000001,.49999999999),(float(lo),float(hi))],method='L-BFGS-B',
                                 options=dict(ftol=1e-14,gtol=1e-11,maxiter=200))
                    pt=[str(F(str(float(opt.x[0])))),str(min(max(F(str(float(opt.x[1]))),lo),hi))]
                    opt=minimize(lambda z:(-endpoint_ev(z[0],p,k,q)[0],np.array([-endpoint_ev(z[0],p,k,q)[1]])),
                                 [float((lo+hi)/2)],jac=True,bounds=[(float(lo),float(hi))],method='L-BFGS-B',
                                 options=dict(ftol=1e-14,gtol=1e-11,maxiter=100))
                    yt=str(min(max(F(str(float(opt.x[0]))),lo),hi))
                else:
                    pt=old['trials'][qi]['point'];yt=old['endpoint_trials'][qi]['point']
                u,y=map(F,pt)
                assert F(1,5)<=u<F(1,2) and lo<=y<=hi and lo<=F(yt)<=hi
                bb=bound(p,k,q,pt);ee=endpoint_bound(p,k,q,yt)
                trials.append(dict(q=q,point=pt,upper=str(bb.upper())))
                endpoints.append(dict(q=q,point=yt,upper=str(ee.upper())))
                uppers.extend((bb,ee))
            if old is None:
                ub=max(v.upper() for v in uppers)
                upper=F(int(np.ceil(float(ub)*10**8))+2,10**8)
            else:
                upper=F(old['upper'])
            assert all(v<ar(upper) for v in uppers),(p,k,uppers,upper)
            vals.append(dict(k=str(k),upper=str(upper),trials=trials,endpoint_trials=endpoints))
        rows.append(dict(**p,grid=vals))
    profiles={}
    for p in rows:
        profiles.setdefault((p['e'],p['b'],p['c']),[]).append(p)
    return rows,profiles


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
        for profile in profiles[key]:
            values=[F(row['upper']) for row in profile['grid']]
            A, B = chord(values, kappas[1-side])
            moved=acb(ar(-A),ar(F(profile['h'])))
            x,y=(acb(ar(F(1,2))),moved) if side==0 else (moved,acb(ar(F(1,2))))
            low = (C+gradient[0]*x+gradient[1]*y).real
            for qa, qb, qc, radius in differentials:
                low -= abs((qa*x+qb*y+qc).real)*radius
            defect=ar(B)-low
            if not defect < ar(LIMIT):
                return None,'support gap'
            upper.append(defect.upper())
    return max(upper), None


def validate():
    specs = [
        ('small-angle-high-rows', 'certify_mixed_small_angle_high_rows.py', 'research_mixed_small_angle_high_rows.md'),
        ('small-angle-high-rows-replay', 'replay_mixed_small_angle_high_rows.py', 'research_mixed_small_angle_high_rows.md'),
        ('right-half-concavity', 'check_mixed_right_half_concavity.py', 'research_mixed_right_half_concavity.md'),
        ('partially-reset-right-support', 'certify_mixed_partially_reset_right_support.py', 'research_mixed_partially_reset_right_support.md'),
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
    parser.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-transition-right-support.json')
    parser.add_argument('--max-visits', type=int, default=200000)
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
    source, profiles = source_grid(saved_grid)
    print('source PASS', len(source), 'profiles;',10*len(source), 'outward support values', flush=True)
    seeds = {(tuple(r['word']), *r['external_types'], *r['faces']): r['addresses']
             for r in recs['partially-reset-right-support']['cases']}
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
    out = dict(status='passed', precision_bits=args.precision, source_profiles=72, source_values=720,
               source_grid=source, reference_products=512, reference_cells=sum(r['cells'] for r in rows),
               visited_cells=visits, worst_core_defect_upper=str(worst), strict_core_ceiling=str(LIMIT),
               finite_source_gap='1/2000', moving_real_interval=['1/10', '11/50'],
               source_records=len(recs), cases=rows, proof_sha256=ph, script_sha256=sh,
               previous_completed_author_run={'proof_sha256': '4bda703ca7202281a8638bc4d6794e2d110796903a7f9ab503fc1f342695c096', 'script_sha256': 'df9c192de0a6671d992fbf3302b488b5e49065679b4f2f8b88c07d6d0cbbec71', 'record_sha256': 'e75c183847c10695b56938cc4ac0184df5ebaa4012298f112fa6498cc52a78f3', 'source_profiles': 72, 'source_values': 720, 'reference_products': 512, 'reference_cells': 5180, 'reason': 'Fresh final run after inline math formatting repairs and an additional exact saved-grid length check; no numerical inequality or target domain changed.'},
               dependencies_sha256=deps, elapsed_seconds=time.monotonic()-start,
               replay_scope='Source rational tangent points and exact reference subdivisions are saved; original window root proposals are rechecked by complete interval self-maps.',
               scope='Whole original conditional block between the transition cap y in [.1,.22] and real right half x in [.5,1], all typed slow/fast height bands, selections, rows and parities; finite gap1/2000. No complete mixed-region assembly.')
    if args.input:
        out.update(input_path=str(args.input), input_sha256=ih)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', 72, 720, 512, out['reference_cells'], visits, time.monotonic()-start, flush=True)


if __name__ == '__main__':
    main()
