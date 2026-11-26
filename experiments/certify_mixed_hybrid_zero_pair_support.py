#!/usr/bin/env python3
"""Full five-window endpoint-pair support; bounded outward cover, no target optimizer."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as F
from pathlib import Path
from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_hybrid_zero_pair_support.md'
HELPER=ROOT/'experiments/certify_mixed_paired_right_transition_support.py'
HELPER_SHA=hashlib.sha256(HELPER.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('hybrid_pair_frozen_window',HELPER)
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
assert HELPER_SHA==hashlib.sha256(HELPER.read_bytes()).hexdigest()
ar=p.ar
HEIGHTS={0:[F('-.03'),F('.02')],1:[F('-.057'),F('.014')]}
A={(0,0):F('.360050'),(0,1):F('.447948'),(1,0):F('.485081'),(1,1):F('.551147')}
B={0:F('.347548'),1:F('.515591')}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def configure(bits):
    ctx.prec=bits;p.P=arb.pi();p.I=acb(0,1);p.m.PI=p.P
    p.ns['PI']=p.P;p.core.pi=p.P;p.core.ii=p.I


def decode(address):
    bounds=[F(0),F(1)]*2
    for j,bit in enumerate(address):
        assert bit in '01'
        k=2*(j%2);mid=(bounds[k]+bounds[k+1])/2
        bounds[k+1-int(bit)]=mid
    return bounds


def test(case,bounds):
    word,ta,tb,fa,fb=case;p.faces[:]=[fa,fb]
    w=p.cert(word,ta,tb,bounds,-F(3,25))
    if not w:return None,'reference'
    z=[w['boxes'][j]for j in(3,5,7)];T=p.response(w)
    if T is None:return None,'response'
    rf=p.pair(z,word,w['boxes'][4],w['boxes'][6])
    mid=[(bounds[k]+bounds[k+1])/2 for k in(0,2)]
    wm=p.cert(word,ta,tb,[mid[0],mid[0],mid[1],mid[1]],-F(3,25))
    if not wm:return None,'midpoint'
    z0=[wm['boxes'][j]for j in(3,5,7)]
    r0=p.pair(z0,word,wm['boxes'][4],wm['boxes'][6])
    PL,PR=r0[1][0],r0[1][2]
    C=r0[0]-PL*z0[0]-PR*z0[2]
    fee=ar('7.55')*z0[0].imag**2+ar('5.5')*z0[2].imag**2
    derivatives=[]
    for ell in range(2):
        xl,xh,yl,yh=map(F,p.RECTS[(ta,tb)[ell]])
        vel=acb(ar(xh-xl))if p.faces[ell]in(0,2)else acb(0,ar(yh-yl))
        R=[T[j,ell]*vel for j in(3,5,7)]
        dv=p.matvec(rf[2],R)
        derivatives.append((dv[0],dv[2],R[0],R[2],ar((bounds[2*ell+1]-bounds[2*ell])/2)))
    lower=[]
    targets=list(itertools.product((0,1),HEIGHTS[word[1]],(0,1),HEIGHTS[word[3]]))
    assert len(targets)==len(set(targets))==16
    for x,ha,y,hc in targets:
        a=acb(x,ar(ha));c=acb(y,ar(hc))
        gap=(C+PL*a+PR*c).real-ar(A[word[2],word[1]]+B[word[3]])-fee
        for dPL,dPR,da,dc,radius in derivatives:
            dg=((a-z[0])*dPL+(c-z[2])*dPR).real
            dg-=ar('15.1')*z[0].imag*da.imag+11*z[2].imag*dc.imag
            gap-=abs(dg)*radius
        if not gap>ar('1/4'):return None,'gap'
        lower.append(gap.lower())
    return min(lower),None


def validate_records():
    specs=[
        ('mixed_hybrid_zero_pair_reduction','check'),
        ('mixed_paired_right_transition_support','certify'),
        ('mixed_cyclic_window_heights','certify'),
        ('mixed_oriented_height_reset','certify'),
        ('mixed_selected_reset_plateau_support','certify'),
        ('mixed_selected_plateau_support','certify'),
    ]
    deps={};records={}
    for stem,prefix in specs:
        proof=f'notes/research_{stem}.md'
        if stem=='mixed_cyclic_window_heights':proof='notes/research_mixed_cyclic_critical_height_bounds.md'
        script=f'experiments/{prefix}_{stem}.py';record=f'repro/results/research-{stem.replace("_","-")}.json'
        for path in(proof,script,record):deps[path]=sha(ROOT/path)
        rec=json.loads((ROOT/record).read_text());assert rec['status']=='passed',stem
        assert rec['proof_sha256']==deps[proof] and rec['script_sha256']==deps[script],stem
        for key in('dependencies','dependencies_sha256'):
            for path,digest in rec.get(key,{}).items():
                assert sha(ROOT/path)==digest,(stem,path)
                if path in deps:assert deps[path]==digest
                deps[path]=digest
        records[stem]=rec
    extra='notes/research_mixed_partial_selected_heights.md';deps[extra]=sha(ROOT/extra)
    source=records['mixed_hybrid_zero_pair_reduction']
    assert {tuple(map(int,k)):F(v)for k,v in source['left_endpoint_constants'].items()}==A
    assert {int(k):F(v)for k,v in source['right_endpoint_constants'].items()}==B
    assert F(source['low_cutoff'])==F(1,1000)
    assert arb(source['maximum_pair_collar_cost'])<ar('1/50')
    assert records['mixed_paired_right_transition_support']['boundary_products']==2048
    assert list(map(F,records['mixed_oriented_height_reset']['integrated_one_height_costs']))==[F(11,2),F(151,20)]
    assert F(1,4)-F(1,50)-F(1,100)==F(11,50)>F(1,5)
    return deps,len(specs)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-hybrid-zero-pair-support.json')
    parser.add_argument('--max-seconds',type=float,default=900)
    parser.add_argument('--max-visits',type=int,default=200000)
    args=parser.parse_args();assert args.precision>=160 and args.max_seconds>0
    configure(args.precision);ph,sh=sha(PROOF),sha(__file__)
    deps,record_count=validate_records();assert sha(HELPER)==HELPER_SHA
    cases=[(word,ta,tb,fa,fb)for word in itertools.product((0,1),repeat=5)
           for ta,tb,fa,fb in itertools.product(range(2),range(2),range(4),range(4))]
    assert len(cases)==len(set(cases))==2048
    old=None;ih=None
    if args.input:
        ih=sha(args.input);saved=json.loads(args.input.read_text())
        assert saved['status']=='passed' and saved['proof_sha256']==ph and saved['script_sha256']==sh
        assert saved['dependencies_sha256']==deps
        old={(tuple(r['word']),*r['external_types'],*r['faces']):r for r in saved['cases']}
        assert len(old)==len(saved['cases'])==2048 and set(old)==set(cases)
    rows=[];visits=0;worst=None;start=time.monotonic()
    for case in cases:
        pending=list(reversed(old[case]['addresses']))if old is not None else['']
        accepted=[];minimum=None;reasons={}
        while pending:
            assert time.monotonic()-start<=args.max_seconds,(case,'runtime limit')
            address=pending.pop();visits+=1;assert visits<=args.max_visits,(case,'visit limit')
            value,reason=test(case,decode(address))
            if value is None:
                assert old is None,(case,address,reason,'saved cell failed')
                reasons[reason]=reasons.get(reason,0)+1
                assert len(address)<28,(case,address,reason)
                pending.extend([address+'1',address+'0'])
            else:
                accepted.append(address)
                minimum=value if minimum is None else min(minimum,value)
        codes=sorted(accepted)
        assert len(codes)==len(set(codes)) and all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
        assert sum((F(1,2**len(a))for a in codes),F(0))==1
        worst=minimum if worst is None else min(worst,minimum)
        row=dict(word=case[0],external_types=list(case[1:3]),faces=list(case[3:]),
                 addresses=codes,cells=len(codes),minimum_gap=str(minimum),split_reasons=reasons)
        rows.append(row)
        Path(str(args.output)+'.partial').write_text(json.dumps(dict(status='running',cases=rows),separators=(',',':'))+'\n')
        print('progress',len(rows),2048,case,len(codes),visits,str(minimum),'elapsed',time.monotonic()-start,flush=True)
    assert ph==sha(PROOF) and sh==sha(__file__) and sha(HELPER)==HELPER_SHA
    assert all(sha(ROOT/path)==digest for path,digest in deps.items())
    if args.input:assert ih==sha(args.input)
    out=dict(status='passed',precision_bits=args.precision,boundary_products=2048,
             accepted_cells=sum(r['cells']for r in rows),visited_cells=visits,target_corners_per_cell=16,
             minimum_gap=str(worst),geometric_gap='1/4',finite_pair_gap='1/5',source_records=record_count,
             low_cutoff='1/1000',cases=rows,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,
             elapsed_seconds=time.monotonic()-start,runtime_limit_seconds=args.max_seconds,
             scope='Original near-zero incident pair, full other-angle/physical-height bands and all selections, reserving both oriented outside costs. Exterior interpretation only for the stated isolated plateau star; no global low-region bound.')
    if args.input:out.update(input_path=str(args.input),input_sha256=ih)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
    Path(str(args.output)+'.partial').unlink(missing_ok=True)
    print('PASS',2048,out['accepted_cells'],visits,'elapsed',out['elapsed_seconds'],flush=True)


if __name__=='__main__':main()
