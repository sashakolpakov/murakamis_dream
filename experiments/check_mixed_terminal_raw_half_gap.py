#!/usr/bin/env python3
"""Calibrated full-row terminal gap on the existing sixteen boundary sides.

No new endpoint roots or parameter subdivisions. Real raw optimizers are
enclosed by original derivative signs and the analytic slope <= -2*pi.
Saved replay validates the same exact rational row brackets.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
import check_mixed_terminal_half_endpoint_gap as core

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_terminal_raw_half_gap.md'
base,end=core.base,core.end
ar,cp=base.ar,base.cp
FLOOR=F(1,300)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def row(u,a,eps):
    return (end.J(a+u)-end.J(a)+end.J(u+HALF)
            -(2+eps)*end.J(u)+II*PI*a*u).real


def slope(u,a,eps):
    return (base.jp(a+u)+base.jp(u+HALF)
            -(2+eps)*base.jp(acb(u))+II*PI*a).real


def raw_row(a,a0,eps,witness=None):
    assert 0<a.real<ar('1/2')
    assert slope(ar('1/5'),a,eps)>0 and slope(ar('2/5'),a,eps)<0
    if witness is None:
        lo,hi=F(1,5),F(2,5)
        for _ in range(42):
            mid=(lo+hi)/2
            value=slope(ar(mid),a0,eps)
            if value>0:lo=mid
            elif value<0:hi=mid
            else:raise AssertionError('inconclusive scalar bisection sign')
        witness=[str(lo),str(hi)]
    else:
        assert len(witness)==2
        lo,hi=map(F,witness)
    assert F(1,5)<=lo<hi<=F(2,5)
    assert hi-lo<=F(1,2**40)
    assert slope(ar(lo),a0,eps)>0 and slope(ar(hi),a0,eps)<0
    um=ar((lo+hi)/2)
    radius=(abs(slope(um,a,eps))/(2*PI)).upper()
    whole=(um+arb(0,radius)).intersection(ar('1/5').union(ar('2/5')))
    assert whole.is_finite() and ar('1/5')<=whole<=ar('2/5')
    return whole,ar(lo).union(ar(hi)),witness


def test(box,eps,neighbor,witness,row_witness=None):
    a=base.parameter(box,neighbor)
    a0=base.parameter([((lo+hi)/2,)*2 for lo,hi in box],neighbor)
    assert base.test(witness,a,eps) is not None
    point=dict(witness,radius='1/10000000000')
    assert base.test(point,a0,eps) is not None
    z0=list(map(cp,witness['centers']))
    radius=ar(witness['radius']);rp=ar(point['radius'])
    e,t,u=[z+acb(arb(0,radius),arb(0,radius))for z in z0]
    ep,tp,up=[z+acb(arb(0,rp),arb(0,rp))for z in z0]
    v,vm,rw=raw_row(a,a0,eps,row_witness)
    value=core.action(a0,ep,tp,up,eps).real-HHALF-row(vm,a0,eps)
    derivative=core.gp(t+a)+2*PI*II*t-core.gp(a+v)-2*PI*II*v
    radii=[ar(base.DISKS[neighbor][2]*(hi-lo)/2)for lo,hi in box]
    lower=value-abs(derivative.real)*radii[0]-abs(derivative.imag)*radii[1]
    assert lower>ar(FLOOR),('raw terminal gap',eps,neighbor,lower)
    return lower.lower(),rw


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-terminal-raw-half-gap.json')
    parser.add_argument('--seconds',type=float,default=120)
    args=parser.parse_args()
    assert args.precision>=192 and 0<args.seconds<=300
    ctx.prec=args.precision
    global PI,II,HALF,HHALF
    PI,II=arb.pi(),acb(0,1);HALF=acb(ar('1/2'))
    core.PI,core.II,core.HALF=PI,II,HALF
    end.PI,end.II=PI,II
    uh=acb(ar('1/4'),arb(3).log()/(4*PI))
    HHALF=(end.J(HALF)+end.phase(HALF,uh)).real
    ph,sh=sha(PROOF),sha(__file__)
    ih=sha(args.input)if args.input else None
    old=json.loads(args.input.read_text())if args.input else None
    deps={};primary={}

    def bind(p,expected=None):
        digest=sha(ROOT/p)
        if expected is not None:assert digest==expected,p
        assert p not in deps or deps[p]==digest,p
        deps[p]=digest
        return digest

    def read(p):
        bind(p);primary[p]=deps[p]
        r=json.loads((ROOT/p).read_text());assert r['status']=='passed',p
        for field in ('dependencies','dependencies_sha256'):
            for name,digest in r.get(field,{}).items():bind(name,digest)
        return r

    p='repro/results/research-mixed-terminal-half-endpoint-gap.json'
    r='repro/results/research-mixed-terminal-half-endpoint-gap-replay.json'
    coherent,replayed=read(p),read(r)
    assert replayed['input_sha256']==deps[p]
    for data in (coherent,replayed):
        bind('notes/research_mixed_terminal_half_endpoint_gap.md',data['proof_sha256'])
        bind('experiments/check_mixed_terminal_half_endpoint_gap.py',data['script_sha256'])
    assert [[(w['node'],w['sides'],w['half_witness'])for w in d['witnesses']]for d in coherent['domains']]==[
        [(w['node'],w['sides'],w['half_witness'])for w in d['witnesses']]for d in replayed['domains']]
    for stem,script in [('complex-right-row-reduction','check_mixed_complex_right_row_reduction.py'),
                        ('right-boundary-row-bracket','check_mixed_right_boundary_row_bracket.py')]:
        p='repro/results/research-mixed-'+stem+'.json'
        r='repro/results/research-mixed-'+stem+'-replay.json'
        source,replayed_source=read(p),read(r)
        if stem=='complex-right-row-reduction':
            # This older scalar replay independently recomputes its whole
            # finite identity list rather than accepting an input witness.
            assert replayed_source['precision_bits']>=320
            for key in ('exact_identities','height_cases','dependencies'):
                assert replayed_source[key]==source[key]
        else:
            assert replayed_source['input_sha256']==deps[p]
        for data in(source,replayed_source):
            bind('notes/research_mixed_'+stem.replace('-','_')+'.md',data['proof_sha256'])
            bind('experiments/'+script,data['script_sha256'])
    bind('notes/research_mixed_endpoint_polynomial_collar.md')
    bind('notes/research_mixed_terminal_right_endpoint_reduction.md')
    roots=json.loads((ROOT/'repro/results/research-mixed-open-word-critical-localization.json').read_text())
    if old:
        assert old['status']=='passed' and old['proof_sha256']==ph and old['script_sha256']==sh
        assert old['dependencies_sha256']==deps
    start=time.monotonic();domains=[];nodes=leaves=excluded=0
    for index,domain in enumerate(roots['domains']):
        eps,neighbor=domain['epsilon'],domain['neighbor_epsilon']
        pending=[([(F(-1),F(1)),(F(-1),F(1))],0)]
        selected={v['node']:v for v in coherent['domains'][index]['witnesses']}
        rows=[];minimum=None;side_counts=[0]*4
        for number,node in enumerate(domain['tree']):
            assert time.monotonic()-start<args.seconds,'runtime bound'
            assert pending
            box,depth=pending.pop();nodes+=1
            if node[0]=='S':
                assert len(node)==2 and node[1]==depth%2
                left,right=base.split(box,node[1]);pending.extend([(left,depth+1),(right,depth+1)])
                continue
            if node[0]=='X':
                assert len(node)==1 and base.excluded(box);excluded+=1;continue
            assert node[0]=='L' and len(node)==2 and not base.excluded(box);leaves+=1
            sides=core.intersects(box,neighbor)
            if not sides:
                assert number not in selected
                continue
            assert number in selected and selected[number]['sides']==sides
            rw=None
            if old:
                prior=old['domains'][index]['witnesses'][len(rows)]
                assert prior['node']==number and prior['sides']==sides
                rw=prior['row_bracket']
            lower,rw=test(box,eps,neighbor,node[1],rw)
            rows.append(dict(node=number,sides=sides,row_bracket=rw))
            for side in sides:side_counts[side]+=1
            minimum=lower if minimum is None else min(minimum,lower)
        assert not pending and len(rows)==len(selected)
        assert side_counts==coherent['domains'][index]['side_counts']
        if old:assert len(rows)==len(old['domains'][index]['witnesses'])
        domains.append(dict(epsilon=eps,neighbor_epsilon=neighbor,witnesses=rows,
                            side_counts=side_counts,minimum_lower=str(minimum)))
        print('PASS raw terminal family',eps,neighbor,len(rows),'lower',minimum,flush=True)
    assert (nodes,leaves,excluded)==(10978,5258,233)
    if old:assert [[w for w in d['witnesses']]for d in domains]==[[w for w in d['witnesses']]for d in old['domains']]
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==digest for p,digest in deps.items())
    if args.input:assert sha(args.input)==ih
    result=dict(status='passed',precision_bits=args.precision,domains=domains,
        gap_floor=str(FLOOR),boundary_sides=16,reused_endpoint_leaves=258,
        boundary_cell_incidences=275,original_nodes=nodes,original_leaves=leaves,
        original_exclusions=excluded,new_endpoint_roots=0,new_parameter_subdivisions=0,
        proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,primary_records=primary,
        input_sha256=ih,elapsed_seconds=time.monotonic()-start,
        scope='Complete raw terminal half-gap on two admitted direct-neighbor rectangles; superharmonic interior transfer and the full right-angle reduction. No attenuated-neighbor or arbitrary-height sign.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 258 reused endpoint cells;',len(deps),'bindings',flush=True)


if __name__=='__main__':
    main()

