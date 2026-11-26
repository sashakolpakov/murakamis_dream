#!/usr/bin/env python3
"""Sixteen bounded outward cardinal checks; no disk-wide/source conclusion."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from flint import acb, arb, ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'experiments'))
import check_mixed_terminal_raw_half_gap as raw
core,base,end=raw.core,raw.base,raw.end
ar,cp=raw.ar,raw.cp


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ctx.prec=256
    pi,ii=arb.pi(),acb(0,1)
    raw.PI,raw.II,raw.HALF=pi,ii,acb(ar('1/2'))
    core.PI,core.II,core.HALF=raw.PI,raw.II,raw.HALF
    end.PI,end.II=pi,ii
    uh=acb(ar('1/4'),arb(3).log()/(4*pi))
    hhalf=(end.J(raw.HALF)+end.phase(raw.HALF,uh)).real
    b2=-4*end.J(acb(ar('1/4'))).real
    deps={}
    def bind(p,h=None):
        hh=sha(ROOT/p)
        if h is not None:assert hh==h,p
        assert p not in deps or deps[p]==hh
        deps[p]=hh
    rp='repro/results/research-mixed-open-word-critical-localization.json'
    rr='repro/results/research-mixed-open-word-critical-localization-replay.json'
    bind(rp);bind(rr)
    roots=json.loads((ROOT/rp).read_text())
    replay=json.loads((ROOT/rr).read_text())
    assert roots['status']==replay['status']=='passed'
    assert replay['input_sha256']==deps[rp] and replay['domains']==roots['domains']
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
    rows=[]
    for di,domain in enumerate(roots['domains']):
        eps,neighbor=domain['epsilon'],domain['neighbor_epsilon']
        cr,ci,r=base.DISKS[neighbor]
        rad=F('.083') if neighbor==0 else F('.060')
        targets=[(cr+rad,ci),(cr,ci+rad),(cr-rad,ci),(cr,ci-rad)]
        found=[[]for _ in targets]
        pending=[([(F(-1),F(1)),(F(-1),F(1))],0)]
        for ni,node in enumerate(domain['tree']):
            assert pending
            box,depth=pending.pop()
            if node[0]=='S':
                assert node[1]==depth%2
                left,right=base.split(box,node[1]);pending.extend([(left,depth+1),(right,depth+1)])
                continue
            if node[0]=='X':
                assert base.excluded(box)
                continue
            assert node[0]=='L'
            for side,(x,y)in enumerate(targets):
                normalized=[(x-cr)/r,(y-ci)/r]
                if all(lo<=v<=hi for v,(lo,hi)in zip(normalized,box)):
                    found[side].append((F(node[1]['radius']),ni,box,node[1]))
        assert not pending
        for side,point in enumerate(targets):
            assert found[side]
            radius,ni,box,witness=min(found[side],key=lambda item:(item[0],item[1]))
            a=acb(ar(point[0]),ar(point[1]))
            assert base.test(witness,base.parameter(box,neighbor),eps) is not None
            assert base.test(witness,a,eps) is not None
            rradius=ar(radius)
            center=list(map(cp,witness['centers']))
            whole=[z+acb(arb(0,rradius),arb(0,rradius))for z in center]
            value=core.action(a,*center,eps)
            gradient=base.equation(center,a,eps)
            H=base.jacobian(whole,a,eps)
            error=rradius*sum(abs(gradient[j,0])for j in range(3))
            error+=rradius**2*sum(abs(H[j,k])for j in range(3)for k in range(3))/2
            actual=value.real+arb(0,error.upper())
            v,vm,row_witness=raw.raw_row(a,a,eps)
            lower_max=raw.row(vm,a,eps)
            negheight=max(F(0),-point[1])
            upper_zero=2*pi*ar(negheight)
            upper_half=b2/2+pi*ar(negheight)
            gaps=[actual-hhalf-c for c in(lower_max,upper_zero,upper_half)]
            classifications=[]
            for gap in gaps:
                classifications.append('positive_lower' if gap>0 else
                                       'negative_upper' if gap<0 else 'inconclusive')
            row=dict(epsilon=eps,neighbor_epsilon=neighbor,cardinal=side,
                     external=[str(v)for v in point],original_node=ni,
                     endpoint_radius=str(radius),containing_leaves=len(found[side]),
                     row_bracket=row_witness,endpoint_action=str(actual),
                     row_lower_max=str(lower_max),upper_zero=str(upper_zero),
                     upper_half=str(upper_half),
                     gaps=[str(g)for g in gaps],
                     gap_lower_endpoints=[str(g.lower())for g in gaps],
                     gap_upper_endpoints=[str(g.upper())for g in gaps],
                     classifications=classifications)
            rows.append(row)
            print(eps,neighbor,side,'a',row['external'],
                  'gaps',[float(g.mid())for g in gaps],classifications,flush=True)
    assert len(rows)==16
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    out=dict(status='bounded_point_diagnostic',precision_bits=ctx.prec,
             scope='16 fixed cardinal points of smaller attached disks. Outward whole-witness action and raw-row enclosures; no full circle bound, no actual-word counterexample, no finite-kernel lower estimate.',
             rows=rows,dependencies_sha256=deps,
             script_sha256=sha(__file__),new_endpoint_roots=0,new_parameter_subdivisions=0)
    (HERE/'result.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()

