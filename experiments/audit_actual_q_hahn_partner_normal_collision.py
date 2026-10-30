#!/usr/bin/env python3
"""Actual generic normal versus the transverse collision derivative."""
from __future__ import annotations

import json
import random
from pathlib import Path

import sympy as sp

from audit_high_color_first_normal_r_degree import root_field


def poch(a,Q,k,p):
    v=1
    for r in range(k):v=v*(1-a*pow(Q,r,p))%p
    return v


def poch_b(a,Q,k,p,power):
    v,d=1,0
    for r in range(k):
        z=a*pow(Q,r,p)%p
        v,d=v*(1-z)%p,(d*(1-z)-v*power*z)%p
    return v,d


def phi(m,Q,B,X,T,p):
    value=derivative=0
    for k in range(m+1):
        n,dn=poch_b(B*B*pow(Q,m+1,p)%p,Q,k,p,2)
        den,dd=poch_b(B*Q%p,Q,k,p,1)
        den2=poch(pow(T,-1,p),Q,k,p)*poch(Q,Q,k,p)%p
        ratio=n*pow(den,-1,p)%p
        dr=(dn*den-n*dd)*pow(den*den%p,-1,p)%p
        factor=poch(pow(Q,-m,p),Q,k,p)*poch(X,Q,k,p)*pow(Q,k,p)*pow(den2,-1,p)%p
        value=(value+factor*ratio)%p
        derivative=(derivative+factor*dr)%p
    return value,derivative


def original_column(N,t,m,u,p,q):
    """Independent original R_(m,a) derivative, before root simplification."""
    Q=q*q%p;d=N-1;x=pow(q,d,p)
    fac=[1];harm=[0]
    for k in range(1,N):
        z=pow(Q,k,p)
        fac.append(fac[-1]*(1-z)%p)
        harm.append((harm[-1]-2*k*z*pow(1-z,-1,p))%p)
    def gauss(n,k):return fac[n]*pow(fac[k]*fac[n-k]%p,-1,p)%p
    def hbin(n,k):return (harm[n]-harm[k]-harm[n-k])%p
    v=dv=0
    for a in range(max(0,u-t+m),min(m,u)+1):
        R=pow(Q,a*(a-m),p)*gauss(m,a)%p
        term=pow(-1,a,p)*pow(x,u-2*a,p)*pow(Q,a*(t-u)+a*(a-1)//2,p)*R%p
        term=term*gauss(u,a)*gauss(t-u,m-a)*pow(gauss(t,m),-1,p)%p
        gamma=(d*(u-2*a)+2*a*(t-u)+a*(a-1)
               +harm[N-m+a-1]+harm[N-a-1]-harm[N-m-1]-harm[N-1]
               +hbin(u,a)+hbin(t-u,m-a)-hbin(t,m))%p
        v=(v+term)%p;dv=(dv+term*gamma)%p
    return v,dv


def finite_h(m,Q,B,X,T,p):
    F=[1]
    for k in range(1,m+1):F.append(F[-1]*(1-pow(Q,k,p))%p)
    num=0
    for a in range(m+1):
        gauss=F[m]*pow(F[a]*F[m-a]%p,-1,p)%p
        ratio=poch(B*pow(Q,m-a+1,p)%p,Q,a,p)*pow(poch(B*Q%p,Q,a,p),-1,p)%p
        term=pow(-1,a,p)*pow(B,a,p)*pow(Q,a*(a+1)//2,p)*gauss*ratio%p
        term=term*pow(T,a,p)*poch(X,Q,a,p)%p
        for r in range(m-a):term=term*(T*X-pow(Q,r,p))%p
        num=(num+term)%p
    den=1
    for r in range(m):den=den*(T-pow(Q,r,p))%p
    return num*pow(den,-1,p)%p


def tail_normal(j,l,Q,X,T,Delta,p):
    a,b=pow(Q,-j,p),pow(Q,-l,p)
    def log_poch(y,k):
        return -sum(y*pow(Q,r,p)*pow(1-y*pow(Q,r,p),-1,p) for r in range(k))%p
    total=0
    for k in range(j+1):
        ck=(poch(a,Q,k,p)*poch(b,Q,k,p)*poch(X,Q,k,p)*pow(Q,k,p)
            *pow(poch(Q,Q,k,p)**2*poch(pow(T,-1,p),Q,k,p)%p,-1,p))%p
        total=(total+ck*(log_poch(b,k)-log_poch(a,k)))%p
    for k in range(j+1,l+1):
        term=(poch(a,Q,j,p)*poch(b,Q,k,p)*poch(Q,Q,k-j-1,p)*poch(X,Q,k,p)*pow(Q,k,p)
              *pow(poch(Q,Q,k,p)**2*poch(pow(T,-1,p),Q,k,p)%p,-1,p))%p
        total=(total+term)%p
    return total*pow(Delta,-1,p)%p


def symbolic_transformation():
    Q,B,X,T=sp.symbols('Q B X T')
    def P(a,k):return sp.prod(1-a*Q**r for r in range(k))
    checked=0
    for m in range(3):
        F=[P(Q,k) for k in range(m+1)]
        num=0
        for a in range(m+1):
            term=(-1)**a*B**a*Q**(a*(a+1)//2)*F[m]/F[a]/F[m-a]
            term*=P(B*Q**(m-a+1),a)/P(B*Q,a)*T**a*P(X,a)
            term*=sp.prod(T*X-Q**r for r in range(m-a))
            num+=term
        standard=sum(P(Q**(-m),k)*P(B*B*Q**(m+1),k)*P(X,k)*Q**k
                     /(P(B*Q,k)*P(1/T,k)*P(Q,k)) for k in range(m+1))
        assert sp.cancel(num/sp.prod(T-Q**r for r in range(m))-standard)==0
        checked+=1
    return checked


def main():
    symbolic=symbolic_transformation()
    rng=random.Random(301020269)
    generic=collision=values=normals=poles=tails=0
    # Exact generic transformations, away from every source denominator.
    p=1000003
    for m in range(9):
        for _ in range(12):
            while True:
                Q,B,X,T=[rng.randrange(2,p-1) for i in range(4)]
                try:
                    a=finite_h(m,Q,B,X,T,p)
                    v,_=phi(m,Q,B,X,T,p)
                    break
                except ValueError:pass
            assert a==v;generic+=1
    # Generic collision, NOT at a root of unity.
    for N in range(3,17):
        Q=4;B=-pow(2,-N,p)%p
        assert B*B*pow(Q,N,p)%p==1
        for j in range((N-1)//2):
            l=N-1-j
            X,T=7,11
            vj,_=phi(j,Q,B,X,T,p)
            vl,_=phi(l,Q,B,X,T,p)
            assert vj==vl
            assert vj==finite_h(j,Q,B,X,T,p)==finite_h(l,Q,B,X,T,p)
            collision+=1
    for N in range(3,20):
        p,eta=root_field(N);q=eta*eta%p;Q=q*q%p;x=pow(q,N-1,p)
        for j in range((N-1)//2+1):
            l=N-1-j
            if j>=l:continue
            Delta=(pow(q,2*j+1,p)-pow(q,-2*j-1,p))%p
            # Retain actual tensor eigenvalue derivative, not the root-only one.
            ej=2*N-2*j-1;el=2*N-2*l-1
            actual_gap=(ej*(pow(q,ej,p)-pow(q,-ej,p))-el*(pow(q,el,p)-pow(q,-el,p)))%p
            assert actual_gap==(-2*N*Delta)%p
            for _ in range(5):
                while True:
                    X,T=rng.randrange(2,p-1),rng.randrange(2,p-1)
                    try:
                        _,bj=phi(j,Q,1,X,T,p)
                        _,bl=phi(l,Q,1,X,T,p)
                        break
                    except ValueError:pass
                assert tail_normal(j,l,Q,X,T,Delta,p)==(bj-bl)*pow(2*Delta,-1,p)%p
                tails+=1
            for t in range(l,N):
                T=pow(Q,t,p)
                for u in range(t+1):
                    X=pow(Q,-u,p)
                    fj,bj=phi(j,Q,1,X,T,p)
                    fl,bl=phi(l,Q,1,X,T,p)
                    vj,dj=original_column(N,t,j,u,p,q)
                    vl,dl=original_column(N,t,l,u,p,q)
                    assert vj==vl==pow(x,u,p)*fj%p
                    assert fj==fl;values+=2
                    from_q=(dj-dl)*pow(actual_gap,-1,p)%p
                    from_b=pow(x,u,p)*(bj-bl)*pow(2*Delta,-1,p)%p
                    assert from_q==from_b;normals+=1
            # At every additional T pole, its highest-X residue is nonzero.
            numerator=(pow(-1,l,p)*pow(Q,l*(l+1)//2,p)
                       *poch(pow(Q,-l,p),Q,l,p)*poch(pow(Q,-j,p),Q,j,p)
                       *poch(Q,Q,l-j-1,p))%p
            assert numerator!=0
            for r in range(j,l):
                T=pow(Q,r,p)
                remaining=1
                for k in range(l):
                    if k!=r:remaining=remaining*(1-pow(Q,k-r,p))%p
                # Derivative of 1-Q^r/T at T=Q^r is 1/T.
                residue=numerator*T*pow(Delta*poch(Q,Q,l,p)**2*remaining%p,-1,p)%p
                assert residue!=0;poles+=1
    result=dict(status='PASS',formal_generic_transformations=symbolic,
                exact_generic_transformations=generic,noncyclotomic_collisions=collision,
                original_value_entries=values,original_q_vs_transverse_normal_entries=normals,
                nonphysical_explicit_tail_checks=tails,
                exact_nonzero_extra_pole_residues=poles,
                scope='Actual generic collision and first-normal identity, with genuine individual-column poles. '
                      'No smaller-corridor relative bound, full-coupon pole or global source claim.')
    Path(__file__).with_name('actual_q_hahn_partner_normal_collision_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
