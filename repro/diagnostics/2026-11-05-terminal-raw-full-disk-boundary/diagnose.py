#!/usr/bin/env python3
"""Bounded test of complete smaller-disk circles on old endpoint cells."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys,time
from flint import acb,arb,ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'experiments'))
import check_mixed_terminal_raw_half_gap as raw
core,base,end=raw.core,raw.base,raw.end
ar,cp=raw.ar,raw.cp


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def meets(box,neighbor):
    radius=F(83,90)if neighbor==0 else F(15,16)
    minimum=sum(min(lo*lo,hi*hi)if lo*hi>0 else F(0)for lo,hi in box)
    maximum=sum(max(lo*lo,hi*hi)for lo,hi in box)
    return minimum<=radius*radius<=maximum


def test(box,eps,neighbor,witness):
    a=base.parameter(box,neighbor)
    a0=base.parameter([((lo+hi)/2,)*2 for lo,hi in box],neighbor)
    assert base.test(witness,a,eps)is not None
    point=dict(witness,radius='1/10000000000')
    assert base.test(point,a0,eps)is not None
    centers=list(map(cp,witness['centers']))
    radius=ar(witness['radius']);rp=ar(point['radius'])
    e,t,u=[z+acb(arb(0,radius),arb(0,radius))for z in centers]
    ep,tp,up=[z+acb(arb(0,rp),arb(0,rp))for z in centers]
    v,vm,rw=raw.raw_row(a,a0,eps)
    P0=core.action(a0,ep,tp,up,eps).real
    Pprime=core.gp(t+a)+2*PI*II*t-core.gp(a)
    values=[P0-HHALF-raw.row(vm,a0,eps),
            P0-HHALF+2*PI*a0.imag,
            P0-HHALF-B2/2,
            P0-HHALF-B2/2+PI*a0.imag]
    derivatives=[core.gp(t+a)+2*PI*II*t-core.gp(a+v)-2*PI*II*v,
                 Pprime-2*PI*II,Pprime,Pprime-PI*II]
    radii=[ar(base.DISKS[neighbor][2]*(hi-lo)/2)for lo,hi in box]
    lows=[value-abs(d.real)*radii[0]-abs(d.imag)*radii[1]
          for value,d in zip(values,derivatives)]
    return dict(lower_endpoints=[str(v.lower())for v in lows],
                upper_endpoints=[str(v.upper())for v in lows],
                positive=[bool(v>0)for v in lows],
                midpoint_gaps=[str(v)for v in values],row_bracket=rw),lows


def main():
    ctx.prec=256
    global PI,II,HHALF,B2
    PI,II=arb.pi(),acb(0,1)
    raw.PI,raw.II,raw.HALF=PI,II,acb(ar('1/2'))
    core.PI,core.II,core.HALF=PI,II,raw.HALF
    end.PI,end.II=PI,II
    uh=acb(ar('1/4'),arb(3).log()/(4*PI))
    HHALF=(end.J(raw.HALF)+end.phase(raw.HALF,uh)).real
    B2=-4*end.J(acb(ar('1/4'))).real
    deps={}
    def bind(p,h=None):
        hh=sha(ROOT/p)
        if h is not None:assert hh==h,p
        assert p not in deps or deps[p]==hh
        deps[p]=hh
    rp='repro/results/research-mixed-open-word-critical-localization.json'
    rr='repro/results/research-mixed-open-word-critical-localization-replay.json'
    bind(rp);bind(rr)
    roots=json.loads((ROOT/rp).read_text());replay=json.loads((ROOT/rr).read_text())
    assert roots['status']==replay['status']=='passed'
    assert replay['input_sha256']==deps[rp]and replay['domains']==roots['domains']
    for r in(roots,replay):
        bind('notes/research_mixed_open_word_critical_localization.md',r['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',r['script_sha256'])
        for p,h in r['dependencies_sha256'].items():bind(p,h)
    for p in ['experiments/check_mixed_terminal_raw_half_gap.py',
              'experiments/check_mixed_terminal_half_endpoint_gap.py',
              'experiments/certify_mixed_endpoint_packet_extension.py',
              'notes/research_mixed_terminal_half_endpoint_gap.md',
              'notes/research_mixed_terminal_half_row_envelope.md',
              'notes/research_mixed_terminal_raw_half_gap.md']:
        bind(p)
    start=time.monotonic();domains=[];nodes=leaves=excluded=0
    for domain in roots['domains']:
        eps,n=domain['epsilon'],domain['neighbor_epsilon']
        pending=[([(F(-1),F(1)),(F(-1),F(1))],0)]
        rows=[];minima=[None]*4;failures=[]
        for ni,node in enumerate(domain['tree']):
            assert time.monotonic()-start<120
            assert pending
            box,depth=pending.pop();nodes+=1
            if node[0]=='S':
                assert node[1]==depth%2
                left,right=base.split(box,node[1]);pending.extend([(left,depth+1),(right,depth+1)])
                continue
            if node[0]=='X':
                assert base.excluded(box)and not meets(box,n)
                excluded+=1;continue
            assert node[0]=='L';leaves+=1
            if not meets(box,n):continue
            result,lows=test(box,eps,n,node[1])
            rows.append(dict(node=ni,box=[[str(v)for v in side]for side in box],**result))
            if not all(result['positive']):failures.append(ni)
            for j,low in enumerate(lows):
                if minima[j]is None or low.lower()<minima[j]:minima[j]=low.lower()
        assert not pending
        domains.append(dict(epsilon=eps,neighbor_epsilon=n,cells=len(rows),
                            failures=failures,minima=[str(v)for v in minima],rows=rows))
        print(eps,n,'cells',len(rows),'failed',len(failures),'minima',[float(v)for v in minima],flush=True)
    assert(nodes,leaves,excluded)==(10978,5258,233)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    out=dict(status='bounded_fixed_tree_test',precision_bits=ctx.prec,domains=domains,
             scope='All old endpoint cells meeting the two smaller-disk boundaries; four complete raw majorant branches. This first pass records interval failures without proposing new cells or roots. A positive point sample is not substituted for a whole-cell inequality.',
             original_nodes=nodes,original_leaves=leaves,original_exclusions=excluded,
             dependencies_sha256=deps,script_sha256=sha(__file__),
             new_endpoint_roots=0,new_parameter_subdivisions=0,
             elapsed_seconds=time.monotonic()-start)
    (HERE/'result.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()

