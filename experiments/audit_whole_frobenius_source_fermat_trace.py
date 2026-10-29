"""Actual divided-kN source, exact Kummer trace/norm and normal flag law.

Generic-q and marked-root tests use exact finite fields. Norm/trace
products are evaluated independently of the Gaussian recursion.
No large-level asymptotic or geometric-period equality is assumed.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import root_field


def gaussian_table(m,q,p):
    Q=q*q%p
    values=[[1]]
    derivatives=[[0]]
    for n in range(1,m+1):
        v=[1]+[0]*(n-1)+[1]
        d=[0]*(n+1)
        for k in range(1,n):
            weight=pow(Q,n-k,p)
            v[k]=(values[-1][k]+weight*values[-1][k-1])%p
            d[k]=(derivatives[-1][k]+weight*(derivatives[-1][k-1]
                         +2*(n-k)*values[-1][k-1]))%p
        values.append(v)
        derivatives.append(d)
    return values,derivatives


def symmetric(table,derivative,n,k,q,p):
    power=-k*(n-k)
    factor=pow(q,power,p)
    value=factor*table[n][k]%p
    logarithmic=factor*(derivative[n][k]+power*table[n][k])%p
    return value,logarithmic


def beta(N,k,s):
    return (-1)**(N*k*(k-1)//2+k*s)


def exp_nilpotent_jet(M0,M1,p):
    size=len(M0)
    power0=np.eye(size,dtype=np.int64)
    power1=np.zeros_like(power0)
    out0=power0.copy()
    out1=power1.copy()
    factorial=1
    for k in range(1,size):
        power1=(power1@M0+power0@M1)%p
        power0=power0@M0%p
        factorial=factorial*k%p
        inv=pow(factorial,-1,p)
        out0=(out0+inv*power0)%p
        out1=(out1+inv*power1)%p
    assert not np.any(power0@M0%p)
    return out0,out1


def actual_pair_gauge_jet(N,s,q,p,table,derivative,new0,new1):
    m=N*(N+1)-1
    size=N+1
    E0,E1,F0,F1=[np.zeros((size,size),dtype=np.int64) for _ in range(4)]
    tau=(-1)**(N*N-1)
    normal=-pow(2*N,-1,p)%p
    for k in range(size):
        if k:
            val,log=symmetric(table,derivative,m-(k*N+s)+N,N,q,p)
            sign=tau*beta(N,k,s)*beta(N,k-1,s)
            E0[k-1,k]=sign*val%p
            E1[k-1,k]=sign*log*normal%p
        if k<N:
            val,log=symmetric(table,derivative,k*N+s+N,N,q,p)
            sign=beta(N,k,s)*beta(N,k+1,s)
            F0[k+1,k]=sign*val%p
            F1[k+1,k]=sign*log*normal%p
    ef0,ef1=exp_nilpotent_jet(F0,F1,p)
    ee0,ee1=exp_nilpotent_jet(E0,E1,p)
    psi0,psi1=ef0[:,0:1],ef1[:,0:1]
    raw0,raw1=ee0[0:1,:],ee1[0:1,:]
    U0=int((raw0@psi0)[0,0])%p
    U1=int((raw1@psi0+raw0@psi1)[0,0])%p
    old0=raw0*pow(U0,-1,p)%p
    old1=(raw1*pow(U0,-1,p)-raw0*U1*pow(U0,-2,p))%p
    assert np.array_equal(psi0,np.ones((size,1),dtype=np.int64))
    assert np.array_equal(old0,new0)
    P0=psi0@old0%p
    Pc1=(psi1@old0+psi0@old1)%p
    Pf1=psi0@new1%p
    eye=np.eye(size,dtype=np.int64)
    G1=(psi0@old1-Pf1@(eye-P0)-(eye-P0)@Pc1)%p
    assert not np.any((G1@psi0+psi1)%p)
    assert np.array_equal((new1+new0@G1)%p,old1)
    H=np.diag([N-2*k for k in range(size)]).astype(np.int64)
    T0=(E0+F0+H@H)%p
    T1=(E1+F1)%p
    transported=(T1+G1@T0-T0@G1)%p
    oldvalue=(old1@T0@psi0+old0@T1@psi0+old0@T0@psi1)%p
    newvalue=(new1@T0@psi0+new0@transported@psi0)%p
    assert np.array_equal(oldvalue,newvalue)


def case(N):
    p,eta=root_field(N)
    qroot=pow(eta,2,p)
    generator=int(sp.primitive_root(p))
    zeta=pow(generator,(p-1)//N,p)
    m=N*(N+1)-1
    assert p>2*m+1
    tables={}
    for label,q in [('root',qroot),('generic',generator)]:
        tables[label]=(q,*gaussian_table(m,q,p))
    dual_tables={label:gaussian_table(m,-pow(q,N,p)%p,p)[0]
                 for label,(q,_,_) in tables.items()}
    trace_checks=norm_checks=source_jet_checks=gauge_checks=0
    dual_checks=norm_jet_checks=0
    generic_q=generator
    rho=(generic_q-pow(generic_q,-1,p))%p
    factorials=[1]
    for a in range(1,m+1):
        integer=(pow(generic_q,a,p)-pow(generic_q,-a,p))*pow(rho,-1,p)%p
        factorials.append(factorials[-1]*integer%p)
    for s in range(N):
        L=m-s
        epsilon=(-1)**(N-1+s)
        for label,(q,table,derivative) in tables.items():
            Z=pow(q,2*N,p)
            A=[]
            for k in range(N+1):
                ge,_=symmetric(table,derivative,L,k*N,q,p)
                A.append(epsilon**k*ge%p)
                gf,_=symmetric(table,derivative,s+k*N,k*N,q,p)
                assert gf
                if label=='generic':
                    # Independent ordinary-power/[r]! coefficients of
                    # the ACTUAL E,F module, away from the root zeros.
                    r=k*N
                    actual_f=factorials[s+r]*pow(factorials[s]*factorials[r],-1,p)%p
                    actual_e=factorials[L]*pow(factorials[L-r]*factorials[r],-1,p)%p
                    assert gf==actual_f
                    assert ge==actual_e
                if label=='root':
                    assert gf==(-1)**(k*s)%p
                    assert A[-1]==math.comb(N,k)%p
            def pairing(t):
                return sum(a*pow(t,k,p) for k,a in enumerate(A))%p
            for x in (2,3,5):
                t=epsilon*pow(x,N,p)%p
                products=[]
                for deck in range(N):
                    y=x*pow(zeta,deck,p)%p
                    product=1
                    for r in range(L):
                        product=product*(1+pow(q,L-1-2*r,p)*y)%p
                    products.append(product)
                assert sum(products)*pow(N,-1,p)%p==pairing(t)
                trace_checks+=1
                norm=math.prod(products)%p
                theta=(-1)**s*pow(q,N*(L-1),p)%p
                slow=1
                for r in range(L):
                    slow=slow*(1+theta*pow(Z,-r,p)*t)%p
                assert norm==slow
                norm_checks+=1
                qhat=-pow(q,N,p)%p
                dual=sum(pow(qhat,-j*(L-j),p)*dual_tables[label][L][j]*pow(t,j,p)
                         for j in range(L+1))%p
                assert slow==dual
                dual_checks+=1
                if label=='root':
                    assert slow==pow(1+t,L,p)
                    assert pairing(t)==pow(1+t,N,p)
                # The exact cap generating function, without division at
                # a zero of the source pairing.
                cap=sum(a*pow(t,k,p)*pow(Z,k*N+s,p) for k,a in enumerate(A))%p
                assert cap==pow(Z,s,p)*pairing(t*pow(Z,N,p)%p)%p
        q,table,derivative=tables['root']
        # The symmetric POWER-parameter norm has zero first log-Z
        # derivative and a specified second derivative, while its
        # selected trace below retains the actual nonzero head slope.
        for t in (1,2,3):
            n0,n1,n2=1,0,0
            for r in range(L):
                a=((L-1)*pow(2,-1,p)-r)%p
                f0=(1+t)%p
                f1=t*a%p
                f2=t*a*a*pow(2,-1,p)%p
                n0,n1,n2=(n0*f0%p,(n1*f0+n0*f1)%p,
                           (n2*f0+n1*f1+n0*f2)%p)
            assert n1==0
            expected=t*L*(L*L-1)*pow(24*(1+t)**2,-1,p)%p
            assert n2*pow(n0,-1,p)%p==expected
            norm_jet_checks+=1
        ell=0
        for a in range(1,s+1):
            den=(pow(q,a,p)-pow(q,-a,p))%p
            ell=(ell-(pow(q,a,p)+pow(q,-a,p))*pow(2*den,-1,p))%p
        raw0=[]
        raw1=[]
        for k in range(N+1):
            value,log=symmetric(table,derivative,L,k*N,q,p)
            value=epsilon**k*value%p
            normal=-epsilon**k*log*pow(2*N,-1,p)%p
            assert normal==value*k*ell%p
            raw0.append(value)
            raw1.append(normal)
            source_jet_checks+=1
        U0=sum(raw0)%p
        U1=sum(raw1)%p
        new0=np.array([[a*pow(U0,-1,p)%p for a in raw0]],dtype=np.int64)
        new1=np.array([[(b*pow(U0,-1,p)-a*U1*pow(U0,-2,p))%p
                        for a,b in zip(raw0,raw1)]],dtype=np.int64)
        for k in range(N+1):
            expected=int(new0[0,k])*ell*(k-N*pow(2,-1,p))%p
            assert int(new1[0,k])==expected
        actual_pair_gauge_jet(N,s,q,p,table,derivative,new0,new1)
        gauge_checks+=1
    return {'N':N,'residue_strings':N,'whole_trace_checks':trace_checks,
            'whole_norm_checks':norm_checks,'actual_normal_source_coefficients':source_jet_checks,
            'actual_divided_exponential_pair_gauges':gauge_checks,
            'power_parameter_duality_checks':dual_checks,
            'independent_norm_log_jet_checks':norm_jet_checks}


def main():
    cases=[case(N) for N in range(2,13)]
    result={'status':'pass','cases':cases,
            'scope':'Actual whole integral divided source, finite cover trace/norm, cap character and source-pair normal gauge; no volume estimate.'}
    path=Path(__file__).with_name('whole_frobenius_source_fermat_trace_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','levels':len(cases),
                      'whole_trace_norm_checks':sum(c['whole_trace_checks']+c['whole_norm_checks'] for c in cases),
                      'actual_source_normal_coefficients':sum(c['actual_normal_source_coefficients'] for c in cases),
                      'source_pair_gauges':sum(c['actual_divided_exponential_pair_gauges'] for c in cases),
                      'power_parameter_checks':sum(c['power_parameter_duality_checks'] for c in cases),
                      'norm_log_jet_checks':sum(c['independent_norm_log_jet_checks'] for c in cases),
                      'results':str(path)},indent=2))


if __name__=='__main__':
    main()
