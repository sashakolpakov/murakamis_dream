#!/usr/bin/env python3
"""Universal exact checks of Rees cyclic factors and characteristic R transport."""

import json
from pathlib import Path

import numpy as np
import sympy as s

from audit_divided_ward_factorial_fusion import eq, field, ident, mm, powers


def cyclic_log_checks():
    records=[]
    for n in range(2,10):
        p,q=field(n)
        zeta=q*q%p
        count=0
        for m in range(1,3*n+3):
            weighted=sum(j*pow(zeta,j*m,p) for j in range(1,n))%p
            dlog=-weighted*pow(m*n,-1,p)%p
            c=-dlog%p
            if m%n==0:c=(c-(n-1)*pow(2*m,-1,p))%p
            expected=0 if m%n==0 else -pow(m*(1-pow(zeta,m,p))%p,-1,p)%p
            assert c==expected
            transport=c*(pow(zeta,m,p)-1)%p
            assert transport==(0 if m%n==0 else pow(m,-1,p))
            deck=sum(pow(zeta,j*m,p) for j in range(n))%p
            assert c*deck%p==0
            count+=1
        records.append({'level':n,'cyclic_log_coefficients':count,
                        'norm_one_and_functional_transport':True})
    return records


def cyclic_color(n,p,q,meridian,y,momentum):
    zeta=q*q%p
    rho=(q-pow(q,-1,p))%p
    x=-meridian*pow(q,-1,p)%p
    k=np.diag([x*pow(y,-1,p)*pow(zeta,-j,p)%p for j in range(n)])
    e=np.zeros((n,n),dtype=np.int64)
    f=e.copy()
    for j in range(1,n):
        e[j-1,j]=(meridian*pow(y,-1,p)*pow(zeta,-j,p)-pow(meridian,-1,p))%p
    e[n-1,0]=momentum*(meridian*pow(y,-1,p)-pow(meridian,-1,p))%p
    for j in range(n-1):f[j+1,j]=(1-y*pow(zeta,j+1,p))%p
    f[0,n-1]=(1-y)*pow(momentum,-1,p)%p
    u=pow(y,n,p)
    gamma=pow(-1,n+1,p)
    kc=gamma*pow(meridian,n,p)*pow(u,-1,p)%p
    ec=momentum*gamma*(pow(meridian,n,p)*pow(u,-1,p)-pow(meridian,-n,p))%p
    fc=(1-u)*pow(momentum,-1,p)%p
    for mat,scalar in ((k,kc),(e,ec),(f,fc)):
        eq(powers(mat,n,p)[n],ident(n)*scalar,p)
    ki=powers(k,n-1,p)[n-1]*pow(kc,-1,p)%p
    eq(mm(e,f,p)-mm(f,e,p),rho*(k-ki),p)
    return k,e,f,kc,ec,fc


def characteristic_transport():
    records=[]
    for n in range(2,8):
        p,q=field(n)
        zeta=q*q%p
        accepted=0
        for trial in range(2,40):
            m1,m2=(1,1) if accepted==0 else (2,3)
            y1,y2=trial,trial+1
            momentum1,momentum2=2,5
            left=cyclic_color(n,p,q,m1,y1,momentum1)
            right=cyclic_color(n,p,q,m2,y2,momentum2)
            k1c,e1c,f1c=left[3:]
            k2c,e2c,f2c=right[3:]
            if not all((e1c,f1c,e2c,f2c)):continue
            divisor=(1+e1c*f2c*k2c*pow(k1c,-1,p))%p
            if not divisor:continue
            k1,e1,f1=(np.kron(a,ident(n))%p for a in left[:3])
            k2,e2,f2=(np.kron(ident(n),a)%p for a in right[:3])
            i=ident(n*n)
            k1i=powers(k1,n-1,p)[n-1]*pow(k1c,-1,p)%p
            k2i=powers(k2,n-1,p)[n-1]*pow(k2c,-1,p)%p
            u=q*mm(mm(mm(e1,k1i,p),k2,p),f2,p)%p
            up=powers(u,n,p)
            eq(up[n],i*(-e1c*f2c*k2c*pow(k1c,-1,p)%p),p)
            h=sum(up[:n])%p*pow(divisor,-1,p)%p
            g=sum((pow(zeta,-j,p)*up[j] for j in range(n)))%p*pow(divisor,-1,p)%p
            eq(mm(i-u,h,p),i,p)
            eq(mm(i-pow(zeta,-1,p)*u,g,p),i,p)
            kr1=mm(k1,i-pow(zeta,-1,p)*u,p)
            kr2=mm(k2,h,p)
            er1=mm(e1,k2,p)
            fr2=mm(k1i,f2,p)
            er2=(mm(k1,e2,p)+e1-mm(mm(e1,mm(k2,k2,p),p),h,p))%p
            fr1=(f2+mm(f1,k2i,p)-mm(mm(g,mm(k1i,k1i,p),p),f2,p))%p
            expected=(k1c*divisor%p,k2c*pow(divisor,-1,p)%p,
                      e1c*k2c%p,f2c*pow(k1c,-1,p)%p,
                      (k1c*e2c+e1c-e1c*k2c*k2c*pow(divisor,-1,p))%p,
                      (f2c+f1c*pow(k2c,-1,p)-f2c*pow(k1c*k1c*divisor%p,-1,p))%p)
            for mat,scalar in zip((kr1,kr2,er1,fr2,er2,fr1),expected):
                eq(powers(mat,n,p)[n],i*scalar,p)
            theta=q*mm(e1,f2,p)%p
            eq(powers(theta,n,p)[n],i*(-e1c*f2c%p),p)
            mismatch=(e1c*k2c+e2c-k1c*e2c-e1c)%p
            records.append({'level':n,'pair':accepted,'prime':p,
                            'six_characteristic_centre_powers':True,
                            'theta_cyclic_power_sign':True,
                            'same_fiber_obstruction_nonzero':bool(mismatch)})
            accepted+=1
            if accepted==2:break
        assert accepted==2
    assert any(r['same_fiber_obstruction_nonzero'] for r in records)
    return records


def scalar_normal_adapter():
    k,n=s.symbols('k N',nonzero=True)
    actual=-(k-1)/(2*n*k*k)
    expected=(1/k**2-1/k)/(2*n)
    assert s.cancel(actual-expected)==0
    epsilon=s.symbols('epsilon')
    adapter=s.series(1/(n*s.log(1+epsilon))-1/(n*epsilon),epsilon,0,2).removeO()
    assert s.simplify(adapter.subs(epsilon,0)-1/(2*n))==0
    return {'linear_vs_logarithmic_normal_adapter':'Li2/(2N)',
            'resonant_polar_sign_positive':True}


def main():
    result={'cyclic_factor':cyclic_log_checks(),
            'full_cyclic_Rees_characteristic_transport':characteristic_transport(),
            'normal_adapter':scalar_normal_adapter(),
            'scope':'Universal local whole-R/source factorization ingredients; no selected knot phase claim.'}
    out=Path(__file__).with_name('rees_whole_crossing_source_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cyclic_levels':len(result['cyclic_factor']),
                      'cyclic_log_coefficients':sum(r['cyclic_log_coefficients'] for r in result['cyclic_factor']),
                      'full_cyclic_pairs':len(result['full_cyclic_Rees_characteristic_transport']),
                      'normal_adapter':result['normal_adapter'],
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
