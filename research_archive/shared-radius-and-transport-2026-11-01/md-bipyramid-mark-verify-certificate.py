"""Verify explicit original bipyramid source bounds with exact and ball arithmetic.

No optimizer is imported. The certificate proves a finite shared-radius
condition, not a theorem for every equator size.
"""
import argparse
from collections import Counter,defaultdict
from fractions import Fraction as F
import json
from pathlib import Path
from flint import arb,ctx


def verify(case,terms=2048):
    m=case['m'];assert m>=6 and m%2==0
    ports=list(map(tuple,case['ports']))
    expected=[]
    for j in range(m):
        if j%2:expected.append((m,(j-1)%m,(j+1)%m,j))
        else:expected.append((m+1,(j+1)%m,(j-1)%m,j))
    assert ports==expected
    assert case['protected']==[0,1] and case['ordinary']==list(range(2,m+2))
    protected={0,1};ordinary=set(case['ordinary'])
    triangles=[t for x,b,c,y in ports for t in [(x,b,y),(x,c,y)]]
    assert len({tuple(sorted(t)) for t in triangles})==2*m
    original={tuple(sorted((pole,j,(j+1)%m))) for pole in (m,m+1) for j in range(m)}
    assert {tuple(sorted(t)) for t in triangles}==original
    edges=Counter(tuple(sorted((t[j],t[(j+1)%3]))) for t in triangles for j in range(3))
    assert len(edges)==3*m and set(edges.values())=={2}
    matching={tuple(sorted((x,y))) for x,b,c,y in ports}
    assert len(matching)==m and (0,1) not in matching and (0,1) in edges
    row_totals=defaultdict(F);face_totals=defaultdict(F);seen=set()
    for item in case['feasible_triangle_flow']:
        e,s,f=item['port'],item['side'],item['face'];v=F(*item['value'])
        assert 0<=e<m and s in (0,1) and f in ordinary and v>=0
        x,b,c,y=ports[e];assert f in (x,(b,c)[s],y)
        key=(e,s,f);assert key not in seen;seen.add(key)
        row_totals[e,s]+=v;face_totals[f]+=v
    expected_arcs={(e,s,f) for e,(x,b,c,y) in enumerate(ports)
                   for s in (0,1) for f in (x,(b,c)[s],y) if f in ordinary}
    assert seen==expected_arcs
    assert all(row_totals[e,s]==F(1,2) for e in range(m) for s in (0,1))
    assert all(face_totals[f]==1 for f in ordinary)
    expected_anchors={(e,tag) for e,(x,b,c,y) in enumerate(ports)
                      for tag,f in [('L',c),('R',b)] if f in ordinary}
    assert {(b['anchor'],b['label']) for b in case['branches']}==expected_anchors
    assert len(case['branches'])==len(expected_anchors)
    def ab(q):return arb(q.numerator)/q.denominator
    def lob(t):
        v=arb(0)
        for n in range(1,terms+1):v+=(2*n*t).sin()/(2*n*n)
        return v+arb(0,arb(1)/(2*terms))
    entropy_cache={}
    def ent(q):
        if q in (0,F(1,2)):return arb(0)
        if q not in entropy_cache:
            t=arb.pi()*ab(q)
            entropy_cache[q]=(lob(t)+lob(arb.pi()/2-t))/arb.pi()
        return entropy_cache[q]
    lower=sum((ent(F(*row['value'])) for row in case['feasible_triangle_flow']),arb(0))
    def vmax(vals):
        lo=max(v.lower() for v in vals);hi=max(v.upper() for v in vals)
        return (arb(lo)+arb(hi))/2+arb(0,(arb(hi)-arb(lo))/2)
    intervals=[]
    for branch in case['branches']:
        weights={f:arb(0) for f in protected}
        for f,v in branch['radii'].items():
            value=F(*v);assert value>0;weights[int(f)]=ab(value)
        assert set(weights)==set(range(m+2))
        cache={}
        def Q(t):
            key=tuple(sorted(t))
            if key in cache:return cache[key]
            vals=[weights[f] for f in t];pos=[v for v in vals if not v.is_zero()]
            if len(pos)==1:value=pos[0].log()/2
            else:
                disc=(vals[0]*vals[1]+vals[1]*vals[2]+vals[2]*vals[0]).sqrt()
                value=arb(0)
                for v in pos:
                    theta=(v/disc).atan()
                    value+=(lob(theta)+lob(arb.pi()/2-theta)+theta*v.log())/arb.pi()
            cache[key]=value;return value
        upper=arb(0)
        for e,(x,b,c,y) in enumerate(ports):
            qb,qc=Q((x,b,y)),Q((x,c,y))
            if e==branch['anchor']:
                if branch['label']=='L':
                    assert c in ordinary
                    choices=[weights[c].log(),qb+weights[c].log()/2]
                else:
                    assert b in ordinary
                    choices=[weights[b].log(),qc+weights[b].log()/2]
            else:
                choices=[qb+qc]+[weights[f].log() for f in (b,c) if f in ordinary]
            upper+=vmax(choices)
        upper-=sum((weights[f].log() for f in ordinary),arb(0))
        gap=lower-upper
        assert gap>arb('0.3'),(m,branch['anchor'],branch['label'],gap)
        intervals.append({'anchor':branch['anchor'],'label':branch['label'],
                          'upper_bound':str(upper.upper()),'gap_lower_bound':str(gap.lower())})
    return {'m':m,'original_coupons':m,'original_triangles':2*m,
            'feasible_flow_arcs':len(seen),'covered_anchors':len(expected_anchors),
            'volume_rate_lower_bound':str(lower.lower()),
            'minimum_gap_lower_bound':str(min(arb(x['gap_lower_bound']) for x in intervals)),
            'certified_gap':'0.3','branches':intervals}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--certificate',type=Path,default=Path('/private/tmp/md-bipyramid-mark-certificate.json'))
    p.add_argument('--output',type=Path,default=Path('/private/tmp/md-bipyramid-mark-certified-results.json'))
    p.add_argument('--terms',type=int,default=2048)
    args=p.parse_args();ctx.prec=192
    cases=json.loads(args.certificate.read_text())['cases']
    results=[verify(case,args.terms) for case in cases]
    out={'scope':'Exact source incidence and rational feasible flows; rigorous Arb upper/lower bounds for all listed shared-radius anchors. No floating optimizer is part of this verification, and no all-m result is asserted.',
         'precision_bits':192,'lobachevsky_fourier_terms':args.terms,'cases':results}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in r.items() if k!='branches'} for r in results],indent=2))
