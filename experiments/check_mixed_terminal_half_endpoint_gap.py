#!/usr/bin/env python3
"""A calibrated terminal half-point gap on admitted neighbor rectangles.

Reuse complete old endpoint trees, testing only leaves meeting sixteen
rectangle sides. No endpoint root or parameter subdivision is proposed.
Each extra half-point row has an original-log disk witness; replay accepts
only its saved rational center and radius.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
import certify_mixed_open_word_critical_localization as base
import certify_mixed_endpoint_packet_extension as end

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_terminal_half_endpoint_gap.md'
RECTANGLES = [[(F('.30'),F('.39')),(F('-.03'),F('.02'))],
              [(F('.27'),F('.33')),(F('-.057'),F('-.001'))]]
FLOOR = F(1,100)
ar,cp = base.ar,base.cp


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def g(z):
    return end.J(z)+II*PI*z*(1-z)/2


def gp(z):
    return end.gp(z)+II*PI*(ar('1/2')-z)


def Q(s,a,e,eps):
    return g(s+a)+g(s+e)-(2+eps)*g(s)+2*PI*II*a*s


def action(a,e,t,u,eps):
    return Q(t,a,e,eps)-g(a)-(1+eps)*g(e)+end.J(e)+end.phase(e,u)


def half_equation(s,a,eps):
    return (base.jp(s+a)+base.jp(s+HALF)-(2+eps)*base.jp(s)
            +PI*II*(a-HALF+eps*(s-HALF)))


def half_second(s,a,eps):
    return PI*(base.cot(s+a)+base.cot(s+HALF)-(2+eps)*base.cot(s))+eps*PI*II


def half_proposal(a,eps):
    import numpy as np
    aa=complex(float(a.real.mid()),float(a.imag.mid()))
    p=1/np.tan(np.pi*aa)
    coefficients=([1,p,-1-1j*p] if eps==0 else [1,p+1j,1j*p,2*(p-1j)])
    good=[]
    for r in np.roots(coefficients):
        s=np.log((r+1j)/(r-1j))/(2j*np.pi)
        if s.real<0:s+=1
        center=[format(s.real,'.17g'),format(s.imag,'.17g')]
        ss=cp(center)
        if (ar('.1')<ss.real<ar('.49') and abs(ss.imag)<ar('.17')
                and abs(half_equation(ss,a,eps))<ar('1e-8')):
            good.append(center)
    assert len(good)==1,('half-row proposal',eps,aa,good)
    return good[0]


def half_disk(a,a0,eps,witness=None):
    center=half_proposal(a0,eps) if witness is None else witness['center']
    c=cp(center)
    Y=1/half_second(c,a0,eps)
    assert Y.is_finite() and abs(Y)>0

    def test(radius,parameter):
        assert radius>0
        s=c+acb(arb(0,radius),arb(0,radius))
        if not (ar('.1')<s.real<ar('.49') and abs(s.imag)<ar('.17')):
            return None
        if not all(0<v.real<1 for v in (s,s+parameter,s+HALF)):
            return None
        cotangent=base.cot(s)
        if not (cotangent.real>0 and abs(cotangent.imag)<1):
            return None
        q=abs(1-Y*half_second(s,parameter,eps))
        residual=abs(Y*half_equation(c,parameter,eps))
        if not (q.is_finite() and q<1 and residual+q*radius<radius):
            return None
        return s

    point_radius=ar('1e-10')
    point=test(point_radius,a0)
    assert point is not None,('half-row midpoint',eps,center)
    if witness is None:
        accepted=None
        for k in range(24,2,-1):
            radius=F(1,2**k)
            whole=test(ar(radius),a)
            if whole is not None:
                accepted=dict(center=center,radius=str(radius))
                break
        assert accepted is not None,('half-row whole cell',eps,center)
    else:
        assert set(witness)=={'center','radius'}
        accepted=witness
        whole=test(ar(witness['radius']),a)
        assert whole is not None,('saved half-row whole cell',eps,center)
    return whole,point,accepted


def intersects(box,neighbor):
    cr,ci,r=base.DISKS[neighbor]
    physical=[(c+r*lo,c+r*hi) for c,(lo,hi) in zip((cr,ci),box)]
    rr=RECTANGLES[neighbor]
    sides=[]
    for side in range(4):
        axis=side//2; other=1-axis; fixed=rr[axis][side%2]
        if (physical[axis][0]<=fixed<=physical[axis][1]
                and physical[other][0]<=rr[other][1]
                and rr[other][0]<=physical[other][1]):
            sides.append(side)
    return sides


def test(box,eps,neighbor,witness,half_witness=None):
    a=base.parameter(box,neighbor)
    a0=base.parameter([((lo+hi)/2,)*2 for lo,hi in box],neighbor)
    assert base.test(witness,a,eps) is not None,'original whole-cell endpoint witness'
    point=dict(witness,radius='1/10000000000')
    assert base.test(point,a0,eps) is not None,'original midpoint endpoint witness'
    z0=list(map(cp,witness['centers']))
    rad=ar(witness['radius']); rp=ar(point['radius'])
    e,t,u=[z+acb(arb(0,rad),arb(0,rad)) for z in z0]
    ep,tp,up=[z+acb(arb(0,rp),arb(0,rp)) for z in z0]
    sh,shp,new=half_disk(a,a0,eps,half_witness)
    value=(action(a0,ep,tp,up,eps)-action(a0,HALF,shp,UHALF,eps)).real
    # The responses of e,t,u and sh vanish by their ORIGINAL critical
    # equations. The common derivative -g'(a) cancels exactly.
    derivative=gp(t+a)+2*PI*II*t-gp(sh+a)-2*PI*II*sh
    radii=[ar(base.DISKS[neighbor][2]*(hi-lo)/2) for lo,hi in box]
    lower=value-abs(derivative.real)*radii[0]-abs(derivative.imag)*radii[1]
    assert lower>ar(FLOOR),('terminal half-point gap',eps,neighbor,lower)
    return lower.lower(),new


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-terminal-half-endpoint-gap.json')
    parser.add_argument('--seconds',type=float,default=120)
    args=parser.parse_args()
    assert args.precision>=192 and 0<args.seconds<=300
    ctx.prec=args.precision
    global PI,II,HALF,UHALF
    PI,II=arb.pi(),acb(0,1)
    end.PI,end.II=PI,II
    HALF=acb(ar('1/2'));UHALF=acb(ar('1/4'),arb(3).log()/(4*PI))
    assert abs(end.partials(HALF,UHALF)[1])<ar('1e-40')
    ph,sh=sha(PROOF),sha(__file__)
    ih=sha(args.input) if args.input else None
    old=json.loads(args.input.read_text()) if args.input else None
    deps={};primary={};seen=set()

    def bind(path,expected=None):
        digest=sha(ROOT/path)
        if expected is not None:assert digest==expected,path
        assert path not in deps or deps[path]==digest,path
        deps[path]=digest
        return digest

    def read(path,main=False):
        bind(path)
        r=json.loads((ROOT/path).read_text())
        assert r['status']=='passed',path
        if main:primary[path]=deps[path]
        if path not in seen:
            seen.add(path)
            for field in ('dependencies','dependencies_sha256'):
                for p,digest in r.get(field,{}).items():
                    bind(p,digest)
        return r

    rootpath='repro/results/research-mixed-open-word-critical-localization.json'
    replaypath='repro/results/research-mixed-open-word-critical-localization-replay.json'
    roots,replay=read(rootpath,True),read(replaypath,True)
    assert replay['input_sha256']==deps[rootpath]
    assert roots['domains']==replay['domains']
    for r in (roots,replay):
        bind('notes/research_mixed_open_word_critical_localization.md',r['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',r['script_sha256'])
    for stem,script in [
        ('mixed-terminal-conditional-source','certify_mixed_terminal_conditional_source.py'),
        ('mixed-complete-first-cap-packet','check_mixed_complete_first_cap_packet.py'),
        ('mixed-open-local-gaussian','check_mixed_open_local_gaussian.py'),
    ]:
        p=f'repro/results/research-{stem}.json'
        r=read(p,True)
        bind('experiments/'+script,r['script_sha256'])
    # Bind the actual all-row half-point packet and the ordinary endpoint
    # primitive implementation; their recorded arithmetic inputs are frozen.
    for name in ['mixed_unselected_right_taper_products','mixed_terminal_conditional_packet',
                 'mixed_terminal_right_endpoint_reduction','mixed_open_word_hessian',
                 'mixed_open_local_gaussian','mixed_fourier_weight_continuation',
                 'mixed_complete_boundary_sum']:
        bind('notes/research_'+name+'.md')
    bind('experiments/certify_mixed_endpoint_packet_extension.py')
    square=read('repro/results/research-mixed-right-square-conditional-packets.json',True)
    bind('notes/research_mixed_unselected_right_taper_products.md',square['proof_sha256'])
    bind('experiments/certify_mixed_right_square_conditional_packets.py',square['script_sha256'])
    if old:
        assert old['status']=='passed' and old['proof_sha256']==ph and old['script_sha256']==sh
        assert old['dependencies_sha256']==deps
    start=time.monotonic()
    specs=[(e,n) for e in (0,1) for n in (0,1)]
    assert [(d['epsilon'],d['neighbor_epsilon']) for d in roots['domains']]==specs
    domains=[];total_nodes=total_leaves=total_excluded=0
    for index,domain in enumerate(roots['domains']):
        eps,neighbor=specs[index]
        # Exact corner tests put the entire target rectangle strictly inside
        # the old disk; all its sides are therefore in accepted old leaves.
        cr,ci,r=base.DISKS[neighbor]
        assert all((x-cr)**2+(y-ci)**2<r*r for x in RECTANGLES[neighbor][0] for y in RECTANGLES[neighbor][1])
        pending=[([(F(-1),F(1)),(F(-1),F(1))],0)]
        saved=[];minimum=None;counts=[0]*4;cursor=0;leaves=excluded=0
        for number,node in enumerate(domain['tree']):
            assert time.monotonic()-start<args.seconds,'runtime bound'
            assert pending,'unused old nodes'
            box,depth=pending.pop();total_nodes+=1
            if node[0]=='S':
                assert len(node)==2 and node[1]==depth%2
                left,right=base.split(box,node[1])
                pending.extend([(left,depth+1),(right,depth+1)])
                continue
            if node[0]=='X':
                assert len(node)==1 and base.excluded(box)
                excluded+=1
                continue
            assert node[0]=='L' and len(node)==2 and not base.excluded(box)
            leaves+=1
            sides=intersects(box,neighbor)
            if not sides:continue
            hw=None
            if old:
                prior=old['domains'][index]['witnesses'][cursor]
                assert prior['node']==number and prior['sides']==sides
                hw=prior['half_witness']
            value,hw=test(box,eps,neighbor,node[1],hw)
            saved.append(dict(node=number,sides=sides,half_witness=hw))
            cursor+=1
            for side in sides:counts[side]+=1
            minimum=value if minimum is None else min(minimum,value)
        assert not pending and leaves==domain['leaves'] and excluded==domain['excluded']
        if old:assert cursor==len(old['domains'][index]['witnesses'])
        assert all(counts)
        total_leaves+=leaves;total_excluded+=excluded
        domains.append(dict(epsilon=eps,neighbor_epsilon=neighbor,side_counts=counts,
                            minimum_lower=str(minimum),witnesses=saved))
        print('PASS terminal family',eps,neighbor,'cells',cursor,'sides',counts,'lower',minimum,flush=True)
    assert (total_nodes,total_leaves,total_excluded)==(10978,5258,233)
    assert [d['side_counts'] for d in domains]==[[11,10,33,17],[26,15,30,16],[10,10,20,17],[15,13,16,16]]
    if old:
        assert [[(w['node'],w['sides'],w['half_witness']) for w in d['witnesses']] for d in domains]==[
            [(w['node'],w['sides'],w['half_witness']) for w in d['witnesses']] for d in old['domains']]
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if args.input:assert sha(args.input)==ih
    result=dict(status='passed',precision_bits=args.precision,domains=domains,
        rectangles=[[[str(lo),str(hi)]for lo,hi in r]for r in RECTANGLES],
        gap_floor=str(FLOOR),boundary_sides=16,
        reused_endpoint_leaves=sum(len(d['witnesses'])for d in domains),
        boundary_cell_incidences=sum(sum(d['side_counts'])for d in domains),
        original_nodes=total_nodes,original_leaves=total_leaves,original_exclusions=total_excluded,
        new_endpoint_roots=0,new_parameter_subdivisions=0,
        proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,primary_records=primary,
        input_sha256=ih,elapsed_seconds=time.monotonic()-start,
        scope='Calibrated complete-color terminal half-point gap on two admitted neighbor rectangles; harmonic interior transfer. No full open-word contour bound or wider-height claim.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',result['reused_endpoint_leaves'],'reused leaves;',len(deps),'bindings',flush=True)


if __name__=='__main__':
    main()
