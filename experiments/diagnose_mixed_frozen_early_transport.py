#!/usr/bin/env python3
"""Bounded diagnostic for frozen-early transport; no proof or certificate.

The default deterministic run tests48,600 points across243 local states.
Its output records observations only; no pass status certifies an inequality.
"""
import importlib.util
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('diagnostic_phase',ROOT/'experiments/certify_mixed_selected_reset_plateau_support.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
def phi(a,b,eta,eps):
    value,gradient=helper.float_phase(a,b,eta,eps)
    return value,gradient[0],gradient[1]
import itertools,json,time
rng=np.random.default_rng(18421);start=time.time();rows=[]
slow=lambda x:min(1,max(0,(x-.1)/.12))
fast=lambda x:min(1,max(0,(x-.1)/.02))
for core_states in itertools.product(range(3),repeat=5):
    best=None
    for k in range(200):
        states=[int(rng.integers(3)),*core_states,int(rng.integers(3))]
        early=[bool(rng.random()<.3) for j in range(7)];early[3]=False
        if early[2] and early[4]:early[4]=False
        if not any(early):early[0]=True
        t=.12 if k<10 else .22 if k<20 else rng.uniform(.12,.22)
        xs=[rng.uniform(.1,.12) if early[j] else rng.uniform(t,.45) for j in range(7)];xs[3]=t
        cs=[rng.uniform(-.03,.02) if s==0 else rng.uniform(-.057,-.02) for s in states]
        hs=[];coeff=[]
        for j in range(7):
            near=[(j-1)%7,j,(j+1)%7]
            hs.append(.014*min(fast(xs[l]) for l in near) if states[j]==2 else cs[j]*min(slow(xs[l]) for l in near))
            coeff.append(0 if states[j]==2 or any(early[l] for l in near) else cs[j])
        z=[xs[j]+1j*hs[j] for j in range(7)]
        grads=[]
        for j in (2,3,4):
            grads.append(phi(z[j-1],z[j],int(states[j-1]>0),int(states[j]>0))[2]+phi(z[j],z[j+1],int(states[j]>0),int(states[j+1]>0))[1])
        D=grads[1].real+sum(min(-coeff[j]/.12*grads[j-2].imag,0) for j in (2,3,4))
        ans=dict(minimum=float(D),states=states,early=early,reals=xs,heights=hs,coefficients=coeff,reference_heights=cs)
        if best is None or D<best['minimum']:best=ans
    rows.append(best)
rows.sort(key=lambda r:r['minimum'])
out=dict(scope='Independent height boxes and actual frozen-early cutoff; random diagnostic only, no geometric-point or theorem claim',elapsed=time.time()-start,cases=rows)
destination=ROOT/'repro/results/diagnostic-mixed-frozen-early-transport.json'
destination.parent.mkdir(parents=True,exist_ok=True)
with destination.open('w') as stream:json.dump(out,stream,indent=2)
for r in rows[:8]:print(json.dumps(r),flush=True)
print('elapsed',time.time()-start)
