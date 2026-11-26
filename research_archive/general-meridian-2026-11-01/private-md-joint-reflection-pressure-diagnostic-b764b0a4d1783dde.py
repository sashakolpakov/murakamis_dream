#!/usr/bin/env python3
"""Exploratory concave optimization; no numerical output is a proof."""
import json
import numpy as np
from scipy.optimize import linprog, minimize, LinearConstraint
from scipy.special import spence


def J(x):
    a=np.asarray(x)
    a=np.clip(a,0.,1.)
    return -np.imag(spence(1-np.exp(2j*np.pi*a)))/(2*np.pi)


def jp(x):
    return np.log(2*np.sin(np.pi*np.clip(x,1e-14,1-1e-14)))


def pressure(z):
    z=np.asarray(z,dtype=float); m=len(z); k=m+1
    # variables: m-1 physical internal edges, then left/right g leaves.
    pairs=[]
    for v in range(m):
        pairs.append((m-1 if v==0 else v-1,m if v==m-1 else v))
    rows=[]; bounds=[]
    for p,(a,b) in zip(z,pairs):
        q=np.zeros(k);q[a]=q[b]=1
        rows.extend([q,-q]);bounds.extend([1.,p-1.])
        for i in (a,b):
            q=np.zeros(k);q[i]=1;rows.append(q);bounds.append(1-p)
    A=np.array(rows); ub=np.array(bounds)
    # Strict feasible seed maximizes a common slack in all gate/leaf faces.
    hi=np.ones(k);hi[-2:]=.5
    AA=np.vstack([np.c_[A,np.ones(len(A))],np.c_[-np.eye(k),np.ones(k)],np.c_[np.eye(k),np.ones(k)]])
    bb=np.r_[ub,np.zeros(k),hi]
    lp=linprog(np.r_[np.zeros(k),-1.],A_ub=AA,b_ub=bb,bounds=[(None,None)]*k+[(0,None)],method='highs')
    if not lp.success:return {'feasible':False,'message':lp.message}
    def fun(x):
        val=0.; grad=np.zeros(k)
        for p,(a,b) in zip(z,pairs):
            u,v=x[a],x[b];s=p+u+v-1
            val+=J(p+u)+J(p+v)+J(u+v)-J(p)-J(u)-J(v)-J(s)
            grad[a]+=jp(p+u)+jp(u+v)-jp(u)-jp(s)
            grad[b]+=jp(p+v)+jp(u+v)-jp(v)-jp(s)
        for i in (k-2,k-1):
            val+=J(2*x[i])-4*J(x[i]);grad[i]+=2*jp(2*x[i])-4*jp(x[i])
        return -float(val),-grad
    out=minimize(fun,lp.x[:k],jac=True,method='SLSQP',constraints=[LinearConstraint(A,-np.inf,ub)],bounds=[(0,h) for h in hi],options={'ftol':1e-11,'maxiter':600})
    return {'feasible':True,'value':-out.fun,'state':out.x.tolist(),'success':bool(out.success),'slack':float(lp.x[-1]),'violation':float(max(0.,np.max(A@out.x-ub)))}


def run():
    rng=np.random.default_rng(7234); records=[]
    for m in range(2,9):
        probes=[np.full(m,a) for a in (.55,.7,.85,.97,.999)]
        probes.extend(.5+.499*rng.random(m) for _ in range(15))
        for z in probes:
            hi=pressure(z);lo=pressure(1-z)
            records.append({'marks':z.tolist(),'high':hi,'reflected':lo,'gap':lo.get('value',np.nan)-hi.get('value',np.nan)})
    records.sort(key=lambda x:x['gap'])
    return records


if __name__=='__main__':
    data=run()
    with open('/private/tmp/md-joint-reflection-pressure-diagnostic-results.json','w') as f:json.dump(data,f,indent=2)
    for d in data[:12]:print(json.dumps(d))
