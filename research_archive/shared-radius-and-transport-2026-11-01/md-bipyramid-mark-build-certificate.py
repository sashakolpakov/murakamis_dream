"""Build rational data from a numerical search; verification is separate."""
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict, deque
import numpy as np

path=Path('/private/tmp/md-bipyramid-mark-capacity-diagnostic.py')
spec=importlib.util.spec_from_file_location('search',path)
search=importlib.util.module_from_spec(spec);spec.loader.exec_module(search)


def rational_flow(m,denominator=1000000):
    ports,ordinary,weights=search.diagram(m)
    arcs=[];incident=defaultdict(list);target={}
    for f in ordinary:target[('f',f)]=F(-1)
    for e,(x,b,c,y) in enumerate(ports):
        for side,t in enumerate(((x,b,y),(x,c,y))):
            row=('t',2*e+side);target[row]=F(1,2)
            w=weights[list(t)];disc=np.sqrt(w[0]*w[1]+w[1]*w[2]+w[2]*w[0])
            positive=[f for f in t if f in ordinary]
            for f in positive:
                value=.5 if len(positive)==1 else np.arctan(weights[f]/disc)/np.pi
                k=len(arcs);arcs.append((row,('f',f),value,e,side,f))
                incident[row].append(k);incident[('f',f)].append(k)
    tree=set();seen=set();stack=[next(iter(target))]
    seen.add(stack[0])
    while stack:
        node=stack.pop()
        for k in incident[node]:
            a,b,*_=arcs[k];other=b if a==node else a
            if other not in seen:seen.add(other);tree.add(k);stack.append(other)
    assert seen==set(target)
    flow={};remaining=dict(target)
    for k,(a,b,value,*_) in enumerate(arcs):
        if k not in tree:
            v=F(round(value*denominator),denominator);flow[k]=v
            remaining[a]-=v;remaining[b]+=v
    neighbors={v:set(k for k in incident[v] if k in tree) for v in target}
    queue=deque(v for v in target if len(neighbors[v])==1)
    while queue:
        v=queue.popleft()
        if not neighbors[v]:continue
        k=next(iter(neighbors[v]));a,b,*_=arcs[k];other=b if a==v else a
        sign=1 if a==v else -1
        value=remaining[v]/sign
        assert 0<=value<=F(1,2),(m,k,value)
        flow[k]=value;remaining[v]-=sign*value;remaining[other]+=sign*value
        neighbors[v].remove(k);neighbors[other].remove(k)
        if len(neighbors[other])==1:queue.append(other)
    assert all(v==0 for v in remaining.values())
    return [{'port':e,'side':side,'face':f,'value':[flow[k].numerator,flow[k].denominator]}
            for k,(_,_,_,e,side,f) in enumerate(arcs)]


if __name__=='__main__':
    data=json.loads(Path('/private/tmp/md-bipyramid-mark-capacity-results.json').read_text())
    out=[]
    for m in sorted({r['m'] for r in data['rows']}):
        ports,ordinary,weights=search.diagram(m)
        branches=[]
        for row in data['rows']:
            if row['m']!=m:continue
            radii={f:F(round(float(np.exp(v))*1000000),1000000)
                   for f,v in zip(ordinary[:-1],row['log_weights'])}
            radii[ordinary[-1]]=F(1)
            branches.append({'anchor':row['anchor'],'label':row['tag'],
                             'radii':{str(k):[v.numerator,v.denominator] for k,v in radii.items()}})
        out.append({'m':m,'ports':ports,'protected':[0,1],'ordinary':ordinary,
                    'feasible_triangle_flow':rational_flow(m),'branches':branches})
    dest=Path('/private/tmp/md-bipyramid-mark-certificate.json')
    dest.write_text(json.dumps({'scope':'Finite original Morse sources; rational data only.','cases':out},indent=2)+'\n')
    print(dest)
