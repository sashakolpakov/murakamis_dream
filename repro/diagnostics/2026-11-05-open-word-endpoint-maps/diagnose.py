#!/usr/bin/env python3
"""Bounded floating proposals for original open-word endpoint maps; not a proof."""
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import root

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DISKS = [(complex(.35, -.01), .09), (complex(.30, -.052), .064)]
DEPENDENCIES = [
    'notes/research_mixed_complete_boundary_sum.md',
    'notes/research_complete_boundary_full_index_interval.md',
    'notes/research_mixed_first_cap_critical.md',
    'notes/research_mixed_cyclic_critical_localization.md',
]

def jp(z):
    return np.log(2*np.sin(np.pi*z))

def endpoint_eq(z, b, eps):
    e,t,u=z
    return np.array([
        -jp(e-u)+jp(e+t)-eps*jp(e)+1j*np.pi*(u-t+eps*(e-.5)),
        jp(e+t)+jp(t+b)-(2+eps)*jp(t)+1j*np.pi*(b-e+eps*(t-.5)),
        2*np.log(np.cos(np.pi*u))+np.log(np.sin(np.pi*(e-u)))
        -3*np.log(np.sin(np.pi*u))+1j*np.pi*e,
    ])

def solve(fun, initial):
    initial=np.asarray(initial, dtype=complex)
    def realfun(v):
        f=fun(v[:len(initial)]+1j*v[len(initial):])
        return np.r_[f.real,f.imag]
    rr=root(realfun,np.r_[initial.real,initial.imag],tol=1e-11)
    z=rr.x[:len(initial)]+1j*rr.x[len(initial):]
    residual=float(np.max(np.abs(fun(z))))
    if residual>1e-8:
        raise RuntimeError((rr.message,residual))
    return z,residual

def pair(z):
    return [float(z.real),float(z.imag)]

def main():
    output={'status':'diagnostic_only', 'scope':'132 fixed external disk proposals and two symmetric one-vertex proposals; no interval validation, no existence or source theorem.', 'cases':[]}
    for eps in range(2):
        for neighbor in range(2):
            center,rad=DISKS[neighbor]
            inputs=[center]+[center+rad*r*np.exp(2j*np.pi*k/16) for r in (.5,1.) for k in range(16)]
            initial=[.42+.01j if eps==0 else .37-.04j,DISKS[eps][0],.23+.05j]
            rows=[]
            for b in inputs:
                z,residual=solve(lambda z:endpoint_eq(z,b,eps),initial)
                e,t,u=z
                margins={
                    'private_real_lower':e.real-.33,'private_real_upper':.47-e.real,
                    'private_imag_lower':e.imag+.09,'private_imag_upper':.08-e.imag,
                    'aux_real_lower':u.real-.21,'aux_real_upper':.25-u.real,
                    'aux_imag_lower':u.imag-.01,'aux_imag_upper':.10-u.imag,
                    'attached_typed_disk':DISKS[eps][1]-abs(t-DISKS[eps][0]),
                }
                rows.append({'external':pair(b),'root':[pair(v) for v in z], 'residual':residual,'margins':{k:float(v) for k,v in margins.items()}})
            output['cases'].append({'epsilon':eps,'neighbor_epsilon':neighbor,'rows':rows,'minimum_margins':{k:min(x['margins'][k] for x in rows) for k in rows[0]['margins']},'ranges':{name:[[min(x['root'][i][j] for x in rows),max(x['root'][i][j] for x in rows)] for j in range(2)] for i,name in enumerate(('e','t','u'))}})
    output['one_vertex']=[]
    for eps in range(2):
        def fun(z):
            e,u=z
            return np.array([-jp(e-u)+jp(2*e)-eps*jp(e)+1j*np.pi*(u-e+eps*(e-.5)),
                2*np.log(np.cos(np.pi*u))+np.log(np.sin(np.pi*(e-u)))-3*np.log(np.sin(np.pi*u))+1j*np.pi*e])
        z,residual=solve(fun,[.4 if eps==0 else .35-.04j,.23+.06j])
        output['one_vertex'].append({'epsilon':eps,'private_e':pair(z[0]),'aux_u':pair(z[1]),'residual':residual})
    output['dependencies_sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPENDENCIES}
    output['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/'result.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'cases':[{k:v for k,v in c.items() if k!='rows'} for c in output['cases']],'one_vertex':output['one_vertex']},indent=2))

if __name__=='__main__':
    main()
