#!/usr/bin/env python3
"""Explicit outer-cap curvature on 32 distinguished-boundary products.

No roots or word samples are proposed. Saved mode verifies the complete
original rational trees without refinements.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time
from flint import acb, arb, ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_cap_outer_contour_reduction.md'
ERECT=tuple(map(F,['.27','.49','-.055','.04']))
ZRECT=[tuple(map(F,['.278','.391','-.072','.021'])),
       tuple(map(F,['.246','.350','-.108','-.020']))]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def point(x,y):return acb(ar(x),ar(y))
def edge(rect,j,v):
    xl,xh,yl,yh=rect
    verts=[point(xl,yl),point(xh,yl),point(xh,yh),point(xl,yh)]
    z0,z1=verts[j],verts[(j+1)%4]
    return z0+v*(z1-z0)

def test(box,eps,je,jz):
    v=[ar(lo).union(ar(hi)) for lo,hi in box]
    e,z=edge(ERECT,je,v[0]),edge(ZRECT[eps],jz,v[1])
    pi,ii=arb.pi(),acb(0,1)
    u=((ii+(1-2*(2*pi*ii*e).exp()).sqrt())/2).atan()/pi
    if not u.is_finite():return None
    cot=lambda s:(pi*s).cot()
    a=pi*(2*(pi*u).tan()+3*cot(u));b=pi*cot(e-u)
    s2=-b+(b+ii*pi)**2/(a+b)
    f2=s2+pi*cot(e+z)-eps*pi*cot(e)+eps*ii*pi
    if not f2.is_finite():return None
    A,B=-f2.real,f2.imag
    if not A>0:return None
    K=A+B**2/A
    if not K<24:return None
    return K.upper(),A.lower()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--input',type=Path)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-cap-outer-alias-curvature.json')
    ap.add_argument('--seconds',type=float,default=120)
    ap.add_argument('--max-visits',type=int,default=50000)
    args=ap.parse_args();ctx.prec=args.precision
    ph,sh=sha(PROOF),sha(__file__)
    old=None;ih=None
    if args.input:
        raw=args.input.read_bytes();ih=hashlib.sha256(raw).hexdigest();old=json.loads(raw)
        assert old['status']=='passed' and old['proof_sha256']==ph and old['script_sha256']==sh
    dependencies={};visited=set()
    def bind(p,h=None):
        actual=sha(ROOT/p)
        if h is not None:assert actual==h,p
        assert p not in dependencies or dependencies[p]==actual,p
        dependencies[p]=actual
        return actual
    def inherit(p):
        bind(p)
        if p in visited:return
        visited.add(p);d=json.loads((ROOT/p).read_text())
        nested={}
        for key in ('dependencies','dependencies_sha256'):
            for name,digest in d.get(key,{}).items():
                assert name not in nested or nested[name]==digest,name
                nested[name]=digest;bind(name,digest)
        for name in nested:
            if name.startswith('repro/results/') and name.endswith('.json'):inherit(name)
    for stem,script in [('mixed_endpoint_cap_rectangle','certify_mixed_endpoint_cap_rectangle'),
                        ('mixed_open_word_endpoint_rectangles','check_mixed_open_word_endpoint_rectangles'),
                        ('mixed_open_word_critical_localization','certify_mixed_open_word_critical_localization')]:
        p='repro/results/research-'+stem.replace('_','-')+'.json';inherit(p)
        d=json.loads((ROOT/p).read_text());assert d['status']=='passed'
        bind('notes/research_'+('mixed_endpoint_cap_rectangle' if stem=='mixed_endpoint_cap_rectangle' else stem)+'.md',d['proof_sha256'])
        bind('experiments/'+script+'.py',d['script_sha256'])
        rp=p[:-5]+'-replay.json'
        if stem!='mixed_open_word_endpoint_rectangles':
            inherit(rp);rd=json.loads((ROOT/rp).read_text())
            assert rd['status']=='passed' and rd['input_sha256']==dependencies[p]
            assert rd['proof_sha256']==d['proof_sha256'] and rd['script_sha256']==d['script_sha256']
    if old:assert old['dependencies_sha256']==dependencies
    pi=arb.pi()
    upper_gap=2*pi*ar('1/25')-12*ar('91/1000')**2
    lower_gap=2*pi*ar('11/200')-12*ar('23/250')**2
    assert upper_gap>ar('3/20') and lower_gap>ar('6/25')
    assert ERECT[0]+min(r[0] for r in ZRECT)>F(1,2)
    assert ERECT[1]+max(r[1] for r in ZRECT)<1
    specs=[(eps,je,jz) for eps in (0,1) for je in range(4) for jz in range(4)]
    if old:assert [tuple(d['case']) for d in old['cases']]==specs
    start=time.monotonic();records=[];leaves=visits=0;global_max=None
    for index,(eps,je,jz) in enumerate(specs):
        todo=[([(F(0),F(1)),(F(0),F(1))],0)];nodes=[];cursor=0;nleaf=0;local_max=None
        while todo:
            assert time.monotonic()-start<args.seconds and visits<args.max_visits
            box,depth=todo.pop();visits+=1
            node=old['cases'][index]['nodes'][cursor] if old else None
            if old:cursor+=1
            if node is None or node==['L']:
                bound=test(box,eps,je,jz)
                if bound is not None:
                    nleaf+=1;nodes.append(['L'])
                    local_max=bound[0] if local_max is None else max(local_max,bound[0])
                    continue
                assert old is None,(index,cursor,'saved leaf failed')
                axis=depth%2
            else:
                assert len(node)==2 and node[0]=='S' and node[1]==depth%2
                axis=node[1]
            assert depth<24
            a,b=box[axis];m=(a+b)/2;nodes.append(['S',axis])
            for interval in ((a,m),(m,b)):
                child=list(box);child[axis]=interval;todo.append((child,depth+1))
        if old:
            assert cursor==len(old['cases'][index]['nodes']) and nleaf==old['cases'][index]['leaves']
        records.append({'case':[eps,je,jz],'leaves':nleaf,'nodes':nodes,'K_upper':str(local_max)})
        leaves+=nleaf;global_max=local_max if global_max is None else max(global_max,local_max)
        print('PASS',eps,je,jz,nleaf,flush=True)
    if old:assert (old['leaves'],old['visits'])==(leaves,visits)
    assert sha(PROOF)==ph and sha(__file__)==sh
    for p,h in dependencies.items():assert sha(ROOT/p)==h,p
    if args.input:assert sha(args.input)==ih
    out={'status':'passed','precision_bits':args.precision,'scope':'Uniform explicit curvature and both complete outer horizontal-alias bounds only; real cut/tail conditions remain separate.',
         'domains':32,'leaves':leaves,'visits':visits,'cases':records,'K_upper':str(global_max),
         'curvature_ceiling':'24','upper_alias_gap':str(upper_gap),'lower_alias_gap':str(lower_gap),
         'proof_sha256':ph,'script_sha256':sh,'dependencies_sha256':dependencies}
    if ih:out['input_sha256']=ih
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS32',leaves,visits,'K',global_max,'seconds',time.monotonic()-start,flush=True)

if __name__=='__main__':main()
