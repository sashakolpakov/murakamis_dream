#!/usr/bin/env python3
"""Stronger middle-four height on the saved four-before-four window cells."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_three_consecutive_four_height.md'
PRIMITIVE=ROOT/'experiments/replay_mixed_cyclic_window_heights.py'
RECTS=[['3/10','39/100','-3/100','1/50'],
       ['27/100','33/100','-57/1000','-1/50']]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def decode(address):
    box=[Q(0),Q(1),Q(0),Q(1)]
    for j,bit in enumerate(address):
        assert bit in '01'
        k=2*(j%2);mid=(box[k]+box[k+1])/2
        box[k+1-int(bit)]=mid
    return box

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=320)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-three-consecutive-four-height.json')
    args=ap.parse_args();assert args.precision>=256;ctx.prec=args.precision
    ph,sh=sha(PROOF),sha(__file__);deps={}
    source_paths=['repro/results/research-mixed-four-before-four-height.json',
                  'repro/results/research-mixed-four-before-four-height-replay.json']
    inherited=[]
    for path in source_paths:
        deps[path]=sha(ROOT/path);r=json.loads((ROOT/path).read_text());inherited.append(r)
        assert r['status']=='passed'and r['boundary_products']==512
        for name,digest in r['dependencies_sha256'].items():
            assert sha(ROOT/name)==digest,name
            deps[name]=digest
        for key,name in [('proof_sha256','notes/research_mixed_four_before_four_height.md'),
                         ('script_sha256','experiments/certify_mixed_four_before_four_height.py')]:
            assert r[key]==sha(ROOT/name);deps[name]=r[key]
        assert r['rectangles']==RECTS
    assert inherited[1]['input_sha256']==deps[source_paths[0]]
    deps[str(PRIMITIVE.relative_to(ROOT))]=sha(PRIMITIVE)
    sp=importlib.util.spec_from_file_location('independent_window',PRIMITIVE)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);m.PI=arb.pi()
    faces=[0,0]
    def params(box,ta,tb):
        out=[]
        for j,t in enumerate((ta,tb)):
            xl,xh,yl,yh=map(Q,RECTS[t]);v=m.ar(box[2*j]).union(m.ar(box[2*j+1]));f=faces[j]
            out.append(acb(m.ar(xl)+m.ar(xh-xl)*v,m.ar(yl if f==0 else yh))if f in(0,2)
                       else acb(m.ar(xh if f==1 else xl),m.ar(yl)+m.ar(yh-yl)*v))
        return out
    m.params=params
    rows={tuple([tuple(r['word']),*r['external_types'],*r['faces']]):r for r in inherited[0]['cases']}
    expected=[((a,1,1,1,c),ta,tb,fa,fb)for a,c,ta,tb,fa,fb in itertools.product(range(2),range(2),range(2),range(2),range(4),range(4))]
    assert len(expected)==len(set(expected))==256
    assert {k for k in rows if k[0][1]==1}==set(expected)
    start=time.time();results=[];maximum=None;count=0
    for case in expected:
        word,ta,tb,fa,fb=case;faces[:]=[fa,fb];codes=sorted(rows[case]['addresses'])
        assert len(codes)==len(set(codes))and all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
        assert sum((Q(1,2**len(a))for a in codes),Q(0))==1
        upper=None
        for address in codes:
            value=m.certify(word,ta,tb,decode(address),Q(-3,25))
            assert value and value[1].imag<m.ar(Q(-53,1000)),(case,address,str(value))
            ub=value[1].imag.upper();upper=ub if upper is None else max(upper,ub);count+=1
        maximum=upper if maximum is None else max(maximum,upper)
        results.append(dict(word=list(word),external_types=[ta,tb],faces=[fa,fb],accepted_cells=len(codes),height_upper=str(upper)))
    assert ph==sha(PROOF)and sh==sha(__file__)
    for p,h in deps.items():assert sha(ROOT/p)==h,p
    result=dict(status='passed',precision_bits=args.precision,boundary_products=256,accepted_cells=count,
                maximum_height_upper=str(maximum),cases=results,proof_sha256=ph,script_sha256=sh,
                dependencies_sha256=deps,elapsed_seconds=time.time()-start,
                scope='Actual middle right leg of three consecutive type-four vertices has height below-.053, with inherited lower bound-.057. Independent sine/cotangent recheck of the complete saved five-window subset; geometry only.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS256',count,'cells','upper',str(maximum),flush=True)

if __name__=='__main__':main()
