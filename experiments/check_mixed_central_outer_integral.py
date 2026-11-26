#!/usr/bin/env python3
"""Outward inequalities for the complete central mixed outer integral."""
from __future__ import annotations
import argparse
from hashlib import sha256
from fractions import Fraction
import json
from pathlib import Path
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bits', type=int, default=192)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-central-outer-integral.json')
    args = ap.parse_args()
    ctx.prec = args.bits
    q = lambda a,b=1: arb(a)/b
    pi = arb.pi()
    cot = lambda x: (pi*x).cos()/(pi*x).sin()
    def c(x,y):
        return (2*pi*x).sin()/((2*pi*y).cosh()-(2*pi*x).cos())
    lam=q(19,20)
    rows=[]
    def record(name, bounds, threshold):
        margins=[v-threshold for v in bounds]
        assert all(v>0 for v in margins),(name,margins)
        rows.append({'name':name,'threshold':str(threshold),
                     'endpoint_lower_margins':[str(v) for v in margins]})
    record('inner row: real part .20 to .25',
           [2*pi*c(x,q(3,20))-4*pi*cot(q(9,20))
            for x in [q(1,5),q(1,4)]],lam)
    record('inner row: real part .25 to .44',
           [2*pi*c(x,q(3,20)) for x in [q(1,4),q(11,25)]],lam)
    record('outer row: real part .25 to .30',
           [pi*c(x,q(57,1000))-2*pi*cot(q(9,20))
            for x in [q(1,4),q(3,10)]],lam)
    record('outer row: real part .30 to .40',
           [pi*c(x,q(57,1000)) for x in [q(3,10),q(2,5)]],lam)
    record('reciprocal factorial rate',
           [(-q(57,500)*pi).exp()*(q(4,5)*pi).sin()/(4*pi)],q(3,100))
    # These are additional exact consequences of an already certified
    # root enclosure; the Newton/source certificate is an explicit input.
    source_path=ROOT/'repro/results/research-mixed-central-conditional-rectangles.json'
    source_bytes=source_path.read_bytes()
    source=json.loads(source_bytes)
    assert source['status']=='passed'
    assert source['script_sha256']==sha256((ROOT/
        'experiments/certify_mixed_central_conditional_rectangles.py').read_bytes()).hexdigest()
    assert source['proof_sha256']==sha256((ROOT/
        'notes/research_mixed_central_conditional_rectangles.md').read_bytes()).hexdigest()
    R=Fraction
    def add(a,b): return a[0]+b[0],a[1]+b[1]
    def scale(a,b): return a[0]*b,a[1]*b
    def mul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
    def decode(address):
        box=[R(0),R(1),R(0),R(1)]
        for j,digit in enumerate(address):
            assert digit in '01'
            k=2*(j%2);mid=(box[k]+box[k+1])/2
            box[k+1-int(digit)]=mid
        return box
    pair_minima={}
    accepted=0
    families={(0,('3','3')),(0,('4','3')),(1,('3','4')),(1,('4','4'))}
    assert {(c['eps'],tuple(c['kinds']),tuple(c['parts'])) for c in source['cases']}=={
        (e,k,(a,b)) for e,k in families for a in range(4) for b in range(4)}
    for case in source['cases']:
        codes=set(case['addresses'])
        assert len(codes)==case['accepted']==len(case['witnesses'])
        assert codes=={w['address'] for w in case['witnesses']}
        assert sum((R(1,2**len(v)) for v in codes),R(0))==1
        assert not codes.intersection({v[:j] for v in codes for j in range(len(v))})
        key=str((case['eps'],case['kinds']))
        pair_minima.setdefault(key,[R(10),R(10)])
        for witness in case['witnesses']:
            box=decode(witness['address']);p0=[];vel=[];dt=[]
            for j,(kind,part) in enumerate(zip(case['kinds'],case['parts'])):
                aa,bb,cc,dd=map(R,source['parameter_rectangles'][kind])
                corners=[(aa,cc),(bb,cc),(bb,dd),(aa,dd)]
                speed=add(corners[(part+1)%4],scale(corners[part],-1))
                lo,hi=box[2*j:2*j+2]
                p0.append(add(corners[part],scale(speed,(lo+hi)/2)))
                vel.append(speed);dt.append((hi-lo)/2)
            z0=tuple(map(R,witness['center']))
            deriv=[tuple(map(R,v)) for v in witness['affine_derivatives']]
            radius=R(witness['remainder_radius'])
            assert radius>0
            for side in (0,1):
                lower=z0[0]+p0[side][0]-radius
                for j in (0,1):
                    coefficient=mul(add(deriv[j],(R(j==side),R(0))),vel[j])[0]
                    lower-=abs(coefficient)*dt[j]
                assert lower>R(507,1000),(case['kinds'],witness['address'],side,lower)
                pair_minima[key][side]=min(pair_minima[key][side],lower)
            accepted+=1
    assert accepted==source['accepted_cells']==1103
    assert source_bytes==source_path.read_bytes()
    paths=[
        'notes/research_mixed_central_outer_integral.md',
        'notes/research_mixed_central_conditional_rectangles.md',
        'notes/research_mixed_type_three_window_strip.md',
        'notes/research_mixed_cyclic_critical_height_bounds.md',
        'notes/research_mixed_local_outer_contribution.md',
        'notes/research_mixed_fourier_weight_continuation.md',
        'experiments/certify_mixed_central_conditional_rectangles.py',
        'repro/results/research-mixed-central-conditional-rectangles.json',
    ]
    result={'status':'passed','precision_bits':args.bits,
            'strict_inequality_groups':len(rows),'inequalities':rows,
            'accepted_affine_cells':accepted,
            'pair_sum_threshold':'507/1000',
            'pair_sum_lower_bounds':{k:list(map(str,v)) for k,v in pair_minima.items()},
            'scope':'Whole central unaliased integral and its uniform Hessian bound; no exterior outer-region or full alias bound.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','precision_bits','strict_inequality_groups')}))


if __name__=='__main__':
    main()
