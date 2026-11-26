#!/usr/bin/env python3
"""Universal five-window height bound for a four followed by a four.

The independent mode evaluates the frozen sine/cotangent primitive on
every saved cell; no author Newton function is imported in that mode.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_four_before_four_height.md'
RECTS=[['3/10','39/100','-3/100','1/50'],
       ['27/100','33/100','-57/1000','-1/50']]
UPPER=Q(-6,125)
INHERITED=[
 ('cyclic_block_localization','research_mixed_cyclic_critical_localization.md'),
 ('cyclic_window_heights','research_mixed_cyclic_critical_height_bounds.md'),
 ('type_three_window_strip','research_mixed_type_three_window_strip.md'),
 ('type_four_height_refinement','research_mixed_type_four_height_refinement.md')]

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def decode(address):
    box=[Q(0),Q(1),Q(0),Q(1)]
    for j,bit in enumerate(address):
        assert bit in '01'
        k=2*(j%2);mid=(box[k]+box[k+1])/2
        box[k+1-int(bit)]=mid
    return box

def verify_cover(addresses):
    codes=sorted(addresses)
    assert len(codes)==len(set(codes))
    assert all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
    assert sum((Q(1,2**len(a))for a in codes),Q(0))==1
    for a in codes:decode(a)

def cases():
    ans=[]
    for a,b,c in itertools.product((0,1),repeat=3):
        word=(a,b,1,1,c)
        for ta,tb,fa,fb in itertools.product(range(2),range(2),range(4),range(4)):
            ans.append((word,ta,tb,fa,fb))
    assert len(ans)==len(set(ans))==512
    return ans

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--independent',action='store_true')
    ap.add_argument('--input',type=Path)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--max-visits',type=int,default=300000)
    args=ap.parse_args();assert args.precision>=160
    if args.independent:assert args.input is not None
    if args.output is None:
        args.output=ROOT/('repro/results/research-mixed-four-before-four-height'+('-replay'if args.independent else'')+'.json')
    ctx.prec=args.precision;ph,sh=sha(PROOF),sha(__file__)
    deps={}
    for stem,proof in INHERITED:
        records=[]
        for prefix,suffix in [('certify',''),('replay','-replay')]:
            script='experiments/'+prefix+'_mixed_'+stem+'.py'
            record='repro/results/research-mixed-'+stem.replace('_','-')+suffix+'.json'
            for p in(script,record,'notes/'+proof):deps[p]=sha(ROOT/p)
            data=json.loads((ROOT/record).read_text());records.append((record,data))
            assert data['status']=='passed'
            assert data['script_sha256']==deps[script]and data['proof_sha256']==deps['notes/'+proof]
            for field in('dependencies','dependencies_sha256'):
                for p,h in data.get(field,{}).items():assert sha(ROOT/p)==h,(stem,p)
        assert records[1][1]['input_sha256']==sha(ROOT/records[0][0])
    primitive=ROOT/('experiments/replay_mixed_cyclic_window_heights.py'if args.independent else'experiments/certify_mixed_cyclic_window_heights.py')
    deps[str(primitive.relative_to(ROOT))]=sha(primitive)
    spec=importlib.util.spec_from_file_location('immutable_five_window',primitive)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.PI=arb.pi()
    faces=[0,0]
    def params(box,ta,tb):
        ans=[]
        for j,t in enumerate((ta,tb)):
            xl,xh,yl,yh=map(Q,RECTS[t]);v=m.ar(box[2*j]).union(m.ar(box[2*j+1]));f=faces[j]
            ans.append(acb(m.ar(xl)+m.ar(xh-xl)*v,m.ar(yl if f==0 else yh))if f in(0,2)
                       else acb(m.ar(xh if f==1 else xl),m.ar(yl)+m.ar(yh-yl)*v))
        return ans
    m.params=params
    inclusions=[]
    for t,row in enumerate(RECTS):
        xl,xh,yl,yh=map(Q,row);cr,ci=m.CENT[t]
        d=max((x-cr)**2+(y-ci)**2 for x in(xl,xh)for y in(yl,yh))
        reserve=m.RAD[t]**2-d;assert reserve>0;inclusions.append(str(reserve))
    expected=cases();saved=None;ih=None
    if args.input:
        ih=sha(args.input);previous=json.loads(args.input.read_text())
        assert previous['status']=='passed'and previous['boundary_products']==512
        assert previous['proof_sha256']==ph and previous['script_sha256']==sh
        assert previous['rectangles']==RECTS and Q(previous['upper_height'])==UPPER
        for p,h in previous['dependencies_sha256'].items():assert sha(ROOT/p)==h,p
        saved={tuple([tuple(r['word']),*r['external_types'],*r['faces']]):r for r in previous['cases']}
        assert len(saved)==len(previous['cases'])==512 and set(saved)==set(expected)
    start=time.time();rows=[];visited=0;upper=None
    for number,case in enumerate(expected):
        word,ta,tb,fa,fb=case;faces[:]=[fa,fb]
        todo=list(reversed(saved[case]['addresses']))if saved else['']
        if saved:verify_cover(todo)
        accepted=[];hull=None
        while todo:
            address=todo.pop();visited+=1;assert visited<=args.max_visits
            box=decode(address)
            result=m.certify(word,ta,tb,box,Q(-3,25))
            if result and result[1].imag<m.ar(UPPER):
                accepted.append(address)
                hull=result[1]if hull is None else acb(hull.real.union(result[1].real),hull.imag.union(result[1].imag))
                continue
            assert saved is None,('saved cell failed',case,address,result)
            if len(address)>=18:
                mid=[(box[0]+box[1])/2,(box[2]+box[3])/2]
                point=m.certify(word,ta,tb,[mid[0],mid[0],mid[1],mid[1]],Q(-3,25))
                assert not point or not point[1].imag>=m.ar(UPPER),('auxiliary-window counterexample',case,mid,str(point[1]))
            assert len(address)<28,('unresolved cell',case,address,str(result))
            todo.extend([address+'1',address+'0'])
        verify_cover(accepted)
        ub=hull.imag.upper();upper=ub if upper is None else max(upper,ub)
        row=dict(word=list(word),external_types=[ta,tb],faces=[fa,fb],addresses=sorted(accepted),accepted=len(accepted),right_leg_hull=[hull.real.str(35,more=True),hull.imag.str(35,more=True)],height_upper=str(ub))
        rows.append(row)
        print('PASS',number+1,'/512','leaves',len(accepted),'visited',visited,'upper',str(ub),'seconds',round(time.time()-start,2),flush=True)
    assert ph==sha(PROOF)and sh==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if args.input:assert ih==sha(args.input)
    out=dict(status='passed',precision_bits=args.precision,boundary_products=512,accepted_cells=sum(r['accepted']for r in rows),visited_cells=visited,
        cases=rows,rectangles=RECTS,upper_height=str(UPPER),rectangle_disk_inclusion_margins=inclusions,maximum_height_upper=str(upper),
        primitive='independent sine/logarithm and cotangent'if args.independent else'original exponential/logarithm',
        elapsed_seconds=time.time()-start,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,
        scope='Every actual type-four right leg followed by type four has height below -.048; existing actual lower bound remains -.057. Geometry only, no finite-source or contour assertion.')
    if args.input:out.update(input_path=str(args.input),input_sha256=ih)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('FULL PASS512',out['accepted_cells'],visited,flush=True)

if __name__=='__main__':main()
