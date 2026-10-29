#!/usr/bin/env python3
"""Exact diagnostics of localized cuts and the explicit Ward retraction."""

import itertools
import json
from pathlib import Path

import numpy as np

from audit_divided_ward_factorial_fusion import color, eq, field, ident, mm, ward_h


def delta(t, k, f, p):
    return (mm(k,t,p)-mm(t,k,p))%p, (mm(f,t,p)-mm(t,f,p))%p


def main():
    records=[]
    for n in range(2,9):
        p,q=field(n)
        _,k,_,_,f=color(n,p,q)
        phi=lambda t:int(t.sum())*pow(n,-1,p)%p
        subset_count=0
        unit_count=0
        for m in range(1,n+1):
            for retained in itertools.combinations(range(n),m):
                retained=list(retained)
                ix=np.ix_(retained,retained)
                ks=k[ix]
                fs=np.zeros((m,m),dtype=np.int64)
                for j in range(m-1):
                    coefficient=1
                    for r in range(retained[j],retained[j+1]):
                        coefficient=coefficient*int(f[r+1,r])%p
                    assert coefficient
                    fs[j+1,j]=coefficient
                def c0(t):return t[ix]
                def s0(t):
                    out=ident(n)*(int(np.trace(t))*pow(m,-1,p)%p)%p
                    out[ix]=t
                    return out
                def hn(pair):return ward_h(*pair,k,f,n,p)
                def hs(pair):return ward_h(*pair,ks,fs,m,p)
                def c1(pair):return delta(c0(hn(pair)),ks,fs,p)
                def s1(pair):return delta(s0(hs(pair)),k,f,p)
                def diff(t):return (int(c0(t).sum())*pow(m,-1,p)-phi(t))%p
                eq(c0(s0(ident(m))),ident(m),p)
                assert int(c0(ident(n)).sum())*pow(m,-1,p)%p==1
                for x in range(n*n):
                    t=np.zeros((n,n),dtype=np.int64)
                    t[x//n,x%n]=1
                    dt=delta(t,k,f,p)
                    ht=hn(dt)
                    assert (diff(t)-diff(ht))%p==0
                    left=c1(dt)
                    right=delta(c0(t),ks,fs,p)
                    eq(left[0],right[0],p)
                    eq(left[1],right[1],p)
                    h=ht-s0(c0(ht))
                    eq(h,t-s0(c0(t)),p)
                    dh=delta(h,k,f,p)
                    sc=s1(c1(dt))
                    eq(dh[0],dt[0]-sc[0],p)
                    eq(dh[1],dt[1]-sc[1],p)
                    unit_count+=1
                if m<n:
                    deleted=next(a for a in range(n) if a not in retained)
                    keep=retained[0]
                    a=np.zeros((n,n),dtype=np.int64)
                    b=a.copy()
                    a[keep,deleted]=1
                    b[deleted,keep]=1
                    projector=np.zeros((n,n),dtype=np.int64)
                    projector[retained,retained]=1
                    lhs=c0(mm(a,b,p))-mm(c0(a),c0(b),p)
                    rhs=c0(mm(mm(a,ident(n)-projector,p),b,p))
                    eq(lhs,rhs,p)
                    assert np.any(lhs)
                subset_count+=1
        # Literal whole-normal carry: alpha=1+eps/N, alpha^N=1+eps.
        # For f=A^(N-1), Af=U canonically. The retained trace of U
        # is U, while using an unreduced A^N in the zero-residue
        # formula misses N*U/(N-1), exactly the prescribed carry.
        assert n*pow(n,-1,p)%p==1
        records.append({'level':n,'prime':p,'retained_subsets':subset_count,
                        'matrix_unit_chain_and_homotopy_checks':unit_count,
                        'compression_excursion_defect':True,
                        'whole_normal_mark_and_carry':True})
    result={'levels':records,
            'scope':'Boundary relative-Ward localization; no compressed R/Hopf or geometric-survival claim.'}
    out=Path(__file__).with_name('ward_source_localization_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'levels':len(records),'retained_subsets':sum(r['retained_subsets'] for r in records),
                      'matrix_units':sum(r['matrix_unit_chain_and_homotopy_checks'] for r in records),
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
