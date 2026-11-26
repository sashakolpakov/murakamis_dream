"""Search shared-radius witnesses at an equatorial mark; diagnostics only."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.special import spence
from scipy.optimize import minimize


def lob(t):
    if abs(t) < 1e-14 or abs(t-np.pi/2) < 1e-14:
        return 0.0
    return 0.5*spence(1-np.exp(2j*t)).imag


def diagram(m):
    theta=np.pi/m
    s,c=np.sin(theta),np.cos(theta)
    radii=np.r_[c/s**2*(c-np.cos((2*np.arange(m)-1)*theta)),1.,1.]
    radii[:2]=0.
    ports=[(m,(j-1)%m,(j+1)%m,j) if j%2 else
           (m+1,(j+1)%m,(j-1)%m,j) for j in range(m)]
    ordinary=list(range(2,m+2))
    return ports,ordinary,radii


def functions(m):
    ports,ordinary,radii=diagram(m)
    free=ordinary[:-1]
    index={f:i for i,f in enumerate(free)}
    n=len(free)
    def values(h):
        logs={f:float(h[i]) for f,i in index.items()}
        logs[ordinary[-1]]=0.
        weights={f:np.exp(logs[f]) for f in ordinary}
        weights[0]=weights[1]=0.
        def linear(f):
            g=np.zeros(n)
            if f in index:g[index[f]]=1.
            return logs[f],g
        cache={}
        def Q(tri):
            key=tuple(sorted(tri))
            if key in cache:return cache[key]
            w=np.array([weights[f] for f in tri]);pos=np.flatnonzero(w)
            g=np.zeros(n)
            if len(pos)==1:
                f=tri[pos[0]];value,gg=linear(f);answer=(value/2,gg/2)
            else:
                disc=np.sqrt(w[0]*w[1]+w[1]*w[2]+w[2]*w[0])
                value=0.
                for j in pos:
                    f=tri[j];t=np.arctan(w[j]/disc)
                    value+=(lob(t)+lob(np.pi/2-t)+t*logs[f])/np.pi
                    if f in index:g[index[f]]+=t/np.pi
                answer=(value,g)
            cache[key]=answer
            return answer
        rows=[]
        for x,b,c,y in ports:
            qb,gb=Q((x,b,y));qc,gc=Q((x,c,y))
            choices={'C':[(qb+qc,gb+gc)]}
            choices['H']=choices['C'].copy()
            if c in logs:
                v,g=linear(c)
                choices['L']=[(v,g),(qb+v/2,gb+g/2)]
                choices['H'].append((v,g))
            if b in logs:
                v,g=linear(b)
                choices['R']=[(v,g),(qc+v/2,gc+g/2)]
                choices['H'].append((v,g))
            rows.append(choices)
        return rows
    h0=np.log(radii[free]/radii[ordinary[-1]])
    return ports,ordinary,values,h0


def solve(m,anchor,tag):
    ports,ordinary,values,h0=functions(m);n=len(h0)
    tags=['H']*m;tags[anchor]=tag
    def choices(h):
        return [row[t] for row,t in zip(values(h),tags)]
    last=[None,None]
    def cached(h):
        if last[0] is None or not np.array_equal(last[0],h):
            last[:]=[h.copy(),choices(h)]
        return last[1]
    def obj(v):return np.sum(v[n:])-np.sum(v[:n])
    jac=np.r_[-np.ones(n),np.ones(m)]
    def constraints(v):
        return np.array([v[n+e]-a for e,row in enumerate(cached(v[:n])) for a,g in row])
    def cjac(v):
        rows=[]
        for e,row in enumerate(cached(v[:n])):
            for a,g in row:
                vec=np.r_[-g,np.zeros(m)];vec[n+e]=1.;rows.append(vec)
        return np.array(rows)
    start=np.r_[h0,[max(a for a,g in row) for row in choices(h0)]]
    result=minimize(obj,start,jac=lambda v:jac,method='SLSQP',
                    constraints={'type':'ineq','fun':constraints,'jac':cjac},
                    bounds=[(-15,15)]*n+[(-100,100)]*m,
                    options={'maxiter':300,'ftol':1e-11})
    rows=choices(result.x[:n])
    actual=sum(max(a for a,g in row) for row in rows)-np.sum(result.x[:n])
    geom=values(h0)
    phi=sum(row['C'][0][0] for row in geom)-np.sum(h0)
    return {'m':m,'anchor':anchor,'tag':tag,'success':bool(result.success),
            'message':result.message,'phi':phi,'upper_witness':actual,
            'witness_gap':phi-actual,'log_weights':result.x[:n].tolist(),
            'ordinary_order':ordinary,'iterations':int(result.nit)}


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--sizes',default='6,8,10')
    p.add_argument('--output',type=Path,default=Path('/private/tmp/md-bipyramid-mark-capacity-results.json'))
    args=p.parse_args()
    rows=[]
    for m in map(int,args.sizes.split(',')):
        ports,ordinary,values,h0=functions(m)
        for e,row in enumerate(values(h0)):
            for tag in ('L','R'):
                if tag in row:rows.append(solve(m,e,tag))
        here=[x for x in rows if x['m']==m]
        print(json.dumps({'m':m,'anchors':len(here),
                          'minimum_witness_gap':min(x['witness_gap'] for x in here),
                          'failed_strict_gap':[(x['anchor'],x['tag'],x['witness_gap']) for x in here if x['witness_gap']<=0]}),flush=True)
    args.output.write_text(json.dumps({'scope':'Floating-point search only; no certified lower bound on optimum, no asymptotic theorem.','rows':rows},indent=2)+'\n')
