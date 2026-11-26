#!/usr/bin/env python3
"""Outward imaginary-gradient bounds for removing a right selected height."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as F
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_right_selected_height_removal.md'
HELPER = ROOT / 'experiments/certify_mixed_minimum_level_half_stencils.py'
spec = importlib.util.spec_from_file_location('selected_height_roots', HELPER)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
ar = core.ar

POLYGONS = {
    0: [('.1','0'),('.22','-.03'),('.45','-.03'),('.5','0'),
        ('.45','.02'),('.22','.02')],
    1: [('.1','0'),('.22','-.057'),('.45','-.057'),('.5','0'),
        ('.45','.014'),('.12','.014')],
}
POLYGONS = {k: [(F(x), F(y)) for x,y in p] for k,p in POLYGONS.items()}
CENTER = [(F('.45'), F('-.057')), (F('.5'), F(0)),
          (F('.45'), F('.014'))]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def polygon(ty, clipped):
    return core.m.clip(POLYGONS[ty], F('.16'), True) if clipped else POLYGONS[ty]


def cases():
    ans = []
    for clipped in (False, True):
        for eta, gamma in itertools.product((0,1), repeat=2):
            for sides in itertools.product(range(len(polygon(eta,clipped))),
                                           range(3),
                                           range(len(polygon(gamma,clipped)))):
                ans.append(dict(clipped=clipped, types=[eta,gamma], sides=list(sides)))
    assert len(ans) == 939
    assert sum(not c['clipped'] for c in ans) == 432
    return ans


def parameters(box, case):
    eta,gamma = case['types']
    shapes = [polygon(eta,case['clipped']), CENTER, polygon(gamma,case['clipped'])]
    values, mids, velocities = [], [], []
    for shape, side, (lo,hi) in zip(shapes,case['sides'],box):
        p,q = shape[side],shape[(side+1)%len(shape)]
        start = acb(ar(p[0]),ar(p[1]))
        v = acb(ar(q[0]-p[0]),ar(q[1]-p[1]))
        values.append(start+v*ar(lo).union(ar(hi)))
        mids.append(start+v*ar((lo+hi)/2))
        velocities.append(v)
    return values,mids,velocities


def test(box, case, witnesses=None):
    z,z0,v = parameters(box,case)
    eta,gamma = case['types']
    edges = [(0,1,eta,1),(1,2,1,gamma)]
    full,mid,saved = [],[],[]
    for j,(a,b,e,d) in enumerate(edges):
        result = core.root_box(z[a],z[b],z0[a],z0[b],d,
                               None if witnesses is None else witnesses[j])
        if result is None:
            return None,None,None
        root,point,witness = result
        full.append(core.gradH(root,z[a],z[b],e,d))
        mid.append(core.gradH(point,z0[a],z0[b],e,d))
        saved.append(witness)
    # The correlated Newton test can be sharper than a direct Schur
    # denominator enclosure. Refine the parameter box if the latter
    # still contains zero; a NaN is neither a bound nor a split weight.
    for G,H in full+mid:
        if not all(v.is_finite() for v in G+[w for row in H for w in row]):
            return None,None,None
    central = (mid[0][0][1]+mid[1][0][0]).imag
    derivative = [full[0][1][1][0],
                  full[0][1][1][1]+full[1][1][0][0],
                  full[1][1][0][1]]
    gradients = [(d*vv).imag for d,vv in zip(derivative,v)]
    lower = central-sum((abs(g)*ar((hi-lo)/2)
                        for g,(lo,hi) in zip(gradients,box)),arb(0))
    direct = (full[0][0][1]+full[1][0][0]).imag
    if direct.lower()>lower.lower():
        lower = direct
    return lower,gradients,saved


def cover(case, saved=None, max_visits=100000):
    supplied = iter(saved['nodes']) if saved else None
    if saved:
        assert saved['case'] == case
    stack = [[(F(0),F(1)) for _ in range(3)]]
    nodes=[]; visits=leaves=0; minimum=None
    threshold = F('-.45') if case['clipped'] else F('-.6')
    while stack:
        box=stack.pop(); visits+=1
        assert visits<=max_visits, (case,'visit cap')
        node=next(supplied) if supplied is not None else None
        if node is not None and node[0]=='S':
            assert len(node)==2 and type(node[1]) is int and 0<=node[1]<3
            axis=node[1]
        else:
            if node is not None:
                assert len(node)==2 and node[0]=='L'
            lower,grads,witnesses=test(box,case,None if node is None else node[1])
            if node is not None:
                assert lower is not None and lower>ar(threshold),(case,visits,lower)
            if lower is not None and lower>ar(threshold):
                leaves+=1
                margin=(lower-ar(threshold)).lower()
                if minimum is None or margin<minimum:
                    minimum=margin
                nodes.append(['L',witnesses])
                continue
            assert supplied is None
            if grads is None:
                _,_,vel=parameters(box,case)
                weights=[abs(v).upper()*ar(hi-lo) for v,(lo,hi) in zip(vel,box)]
            else:
                weights=[abs(g).upper()*ar(hi-lo) for g,(lo,hi) in zip(grads,box)]
            axis=max(range(3),key=lambda j:float(weights[j]))
        lo,hi=box[axis]; assert lo<hi
        middle=(lo+hi)/2
        for interval in ((lo,middle),(middle,hi)):
            child=list(box); child[axis]=interval; stack.append(child)
        nodes.append(['S',axis])
    if supplied is not None:
        assert next(supplied,None) is None
        assert leaves==saved['leaves'] and visits==saved['visits']
    assert visits==2*leaves-1
    return dict(case=case,nodes=nodes,leaves=leaves,visits=visits,
                threshold=str(threshold),minimum_margin=str(minimum))


def dependencies():
    files=[
        'experiments/certify_mixed_minimum_level_half_stencils.py',
        'experiments/certify_mixed_isolated_transition_phase.py',
        'experiments/certify_mixed_real_small_support.py',
    ]
    records=[
        ('mixed_closed_cotangent_roots','check'),
        ('mixed_early_selected_source_cap','certify'),
        ('mixed_transition_pair_source','certify'),
        ('mixed_left_right_interface_source','certify'),
    ]
    deps={p:sha(ROOT/p) for p in files}
    for stem,prefix in records:
        pp=f'notes/research_{stem}.md'
        ss=f'experiments/{prefix}_{stem}.py'
        rr=f'repro/results/research-{stem.replace("_","-")}.json'
        rec=json.loads((ROOT/rr).read_text())
        for p in (pp,ss,rr): deps[p]=sha(ROOT/p)
        assert rec['status']=='passed'
        assert rec['proof_sha256']==deps[pp] and rec['script_sha256']==deps[ss]
        for key in ('dependencies','dependencies_sha256'):
            for p,h in rec.get(key,{}).items():
                assert sha(ROOT/p)==h,p
                if p in deps: assert deps[p]==h
                deps[p]=h
    # The right-square packet has a different proof filename.
    pp='notes/research_mixed_unselected_right_taper_products.md'
    ss='experiments/certify_mixed_right_square_conditional_packets.py'
    rr='repro/results/research-mixed-right-square-conditional-packets.json'
    rec=json.loads((ROOT/rr).read_text())
    for p in (pp,ss,rr): deps[p]=sha(ROOT/p)
    assert rec['status']=='passed' and rec['proof_sha256']==deps[pp]
    assert rec['script_sha256']==deps[ss]
    for key in ('dependencies','dependencies_sha256'):
        for p,h in rec.get(key,{}).items():
            assert sha(ROOT/p)==h,p
            if p in deps: assert deps[p]==h
            deps[p]=h
    return deps


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--input',type=Path)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-right-selected-height-removal.json')
    ap.add_argument('--limit',type=int)
    ap.add_argument('--max-visits',type=int,default=100000)
    ap.add_argument('--max-seconds',type=float,default=1800)
    args=ap.parse_args(); assert args.precision>=160
    core.configure(args.precision)
    ph,sh=sha(PROOF),sha(__file__);deps=dependencies()
    all_cases=cases()
    chosen=all_cases if args.limit is None else all_cases[:args.limit]
    assert chosen
    input_hash=sha(args.input) if args.input else None
    saved=json.loads(args.input.read_text()) if args.input else None
    if saved:
        assert saved['status']=='passed' and saved['products']==939
        assert saved['proof_sha256']==ph and saved['script_sha256']==sh
        assert saved['dependencies_sha256']==deps
        assert [r['case'] for r in saved['cases']]==all_cases
        assert args.limit is None
    pi=arb.pi()
    lam=(2*(ar('.45')*pi).sin()).log()
    kf=ar('.028')*pi-ar('.0426');kg=lam-ar('.639')
    assert kf>0 and kg>0
    assert F(3,5)*(F('.014')+F('.057')/2)*20==F('.51')
    assert F(9,20)*(F('.014')+F('.057'))*20==F('.639')
    rows=[];start=time.time()
    for j,case in enumerate(chosen):
        assert time.time()-start<args.max_seconds,('time cap',j)
        row=cover(case,None if saved is None else saved['cases'][j],args.max_visits)
        rows.append(row)
        if (j+1)%10==0 or j+1==len(chosen):
            print('PRODUCT',j+1,'/',len(chosen),'leaves',sum(r['leaves']for r in rows),
                  'elapsed',round(time.time()-start,2),flush=True)
    assert ph==sha(PROOF) and sh==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if args.input:
        assert sha(args.input)==input_hash
    result=dict(status='passed' if args.limit is None else 'partial',
                precision_bits=args.precision,products=len(rows),
                leaves=sum(r['leaves']for r in rows),visits=sum(r['visits']for r in rows),
                cases=rows,scalar_comparisons=2,exact_budget_identities=2,
                lambda_lower=str(lam),forcing_reserve=str(kf),factorial_reserve=str(kg),
                proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,
                input_sha256=input_hash,
                elapsed_seconds=time.time()-start,
                scope='Imaginary derivative bounds on two complete polygon products and the resulting selected-to-unselected comparison at fixed right-transition angle. No unselected transport or whole-period theorem.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(result['status'].upper(),len(rows),'products',result['leaves'],'leaves',flush=True)


if __name__=='__main__':
    main()
