#!/usr/bin/env python3
"""Exact finite identities behind the actual source root theorem.

Negative-root counts are separate numerical regressions; the all-N proof
is the Sturm recurrence and sine multiplier, not those regressions.
"""
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct


def symbolic_recurrence():
    q,z=sp.symbols('q z',nonzero=True)
    B={n:sp.Poly(sp.prod(1+q**(n-1-2*r)*z for r in range(n)),z) for n in range(9)}
    count=0
    for u in range(5):
        for v in range(5):
            t=u+v
            Q=[sum(B[u].nth(a)*B[v].nth(j-a)*z**a
                   for a in range(max(0,j-v),min(j,u)+1)) for j in range(t+1)]
            for j in range(2,t+1):
                lhs=(q**j-q**(-j))*Q[j]
                rhs=(z*(q**(u-j+1)-q**(-u+j-1))
                     +q**(v-j+1)-q**(-v+j-1))*Q[j-1]
                rhs+=z*(q**(t-j+2)-q**(-t+j-2))*Q[j-2]
                assert sp.expand(lhs-rhs)==0
                count+=1
    return count


def exact_level(N, physical=False):
    p,eta,q,E,F,K,_,_,_=balanced_data(N)
    d=N-1;imag=pow(eta,N,p)
    sin=lambda r:(pow(q,r,p)-pow(q,-r,p))*pow(2*imag,-1,p)%p
    sf=[1]
    for r in range(1,N):sf.append(sf[-1]*2*sin(r)%p)
    def beta(n,a):
        return 0 if a<0 or a>n else sf[n]*pow(sf[a]*sf[n-a]%p,-1,p)%p
    def Qpoly(u,v,j):return [beta(u,a)*beta(v,j-a)%p for a in range(j+1)]
    multiplier=0
    for j in range(N):
        for a in range(j+1):
            value=sf[j]*pow(N,-1,p)%p
            for r in range(1,d-j+1):value=value*2*sin(a+r)%p
            assert value==beta(j,a)
            multiplier+=1
    recurrence=dualities=peeling=0
    for t in range(N):
        for u in range(t+1):
            v=t-u
            polys=[Qpoly(u,v,j) for j in range(t+1)]
            for j in range(t+1):
                Q=polys[j]
                if j>=2:
                    previous=polys[j-1];older=polys[j-2]
                    for a in range(j+1):
                        at=lambda arr,k:arr[k] if 0<=k<len(arr) else 0
                        rhs=sin(u-j+1)*at(previous,a-1)+sin(v-j+1)*at(previous,a)+sin(t-j+2)*at(older,a-1)
                        assert sin(j)*Q[a]%p==rhs%p
                    recurrence+=1
                R=Qpoly(j,t-j,u)
                for a in range(max(j,u)+1):
                    left=Q[a]*pow(beta(t,j),-1,p)%p if a<len(Q) else 0
                    right=R[a]*pow(beta(t,u),-1,p)%p if a<len(R) else 0
                    assert left==right
                complement=polys[t-j]
                swap=Qpoly(v,u,j)
                for a in range(j+1):
                    b=u-a
                    assert Q[a]==(complement[b] if 0<=b<len(complement) else 0)
                    assert Q[a]==swap[j-a]
                dualities+=1
                # An independent exact test of the Laurent sine peeling.
                Laurent={j-v+k:beta(v,k) for k in range(v+1)}
                high=list(range(N-j,d-u+1)) if j>u else []
                low=list(range(v-j,0,-1)) if j<v else []
                used=set(high+low)
                for r in high+low:
                    Laurent={a:c*sin(a+r)%p for a,c in Laurent.items() if c*sin(a+r)%p}
                a0=max(0,j-v);a1=min(j,u);n=a1-a0
                assert min(Laurent)==a0 and max(Laurent)==a1
                scale=Laurent[a0]
                assert all(Laurent[a0+k]==scale*beta(n,k)%p for k in range(n+1))
                rest=[r for r in range(1,d-u+1) if r not in used]
                assert len(rest)==n+d-t
                assert all(0<r+a0 and r+a0+n<N for r in rest)
                for r in rest:Laurent={a:c*sin(a+r)%p for a,c in Laurent.items()}
                factor=sf[u]*pow(N,-1,p)*pow(2,d-u,p)%p
                assert all(Laurent.get(a,0)*factor%p==Q[a] for a in range(j+1))
                peeling+=1
    entries=0
    if physical:
        rho=(q-pow(q,-1,p))%p
        Et,Ft,Kt=coproduct(rho*rho*E%p,F,K,2,N,p)
        Ki=np.diag([pow(int(k),-1,p) for k in np.diag(Kt)])
        O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
        for t in range(d+1):
            ids=[u*N+t-u for u in range(t+1)];A=O[np.ix_(ids,ids)]
            for j in range(max(0,d-t),min(t,d//2)+1):
                node=(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p
                f=[1]
                for u in range(t):
                    numerator=(node-int(A[u,u]))*f[u]
                    if u:numerator-=int(A[u,u-1])*f[u-1]
                    f.append(numerator*pow(int(A[u,u+1]),-1,p)%p)
                assert np.array_equal(A@np.array(f,dtype=np.int64)%p,node*np.array(f,dtype=np.int64)%p)
                for u in range(t+1):
                    delta=t+j-d;value=0
                    for a in range(max(0,j-(t-u)),min(j,u)+1):
                        coefficient=beta(j,a)*beta(u,a)*beta(t-u,j-a)*pow(beta(t,j),-1,p)%p
                        value=(value+coefficient*pow(q,delta*a,p))%p
                    value=value*pow(-1,u,p)*pow(q,-(j+1)*u,p)%p
                    assert value==f[u]
                    entries+=1
    return dict(N=N,sine_multiplier_coefficients=multiplier,
                exact_recurrences=recurrence,exact_dualities=dualities,
                independent_Laurent_peelings=peeling,original_Casimir_entries=entries)


def numerical_roots():
    rows=polynomials=nontrivial=0
    max_relative_imaginary=0.0
    for N in range(3,26):
        d=N-1;sf=[1.0]
        for r in range(1,N):sf.append(sf[-1]*2*np.sin(np.pi*r/N))
        def beta(n,a):return sf[n]/(sf[a]*sf[n-a]) if 0<=a<=n else 0.0
        for t in range(N):
            for j in range(max(0,d-t),min(t,d//2)+1):
                for u in range(t+1):
                    v=t-u;lo=max(0,j-v);hi=min(j,u)
                    Q=np.array([beta(u,a)*beta(v,j-a) for a in range(lo,hi+1)])
                    P=Q*np.array([beta(j,a)/beta(t,j) for a in range(lo,hi+1)])
                    for coefficients in (Q,P):
                        polynomials+=1
                        if len(coefficients)==1:continue
                        roots=np.roots((coefficients/max(coefficients))[::-1])
                        relative=max(abs(roots.imag))/max(1,max(abs(roots)))
                        max_relative_imaginary=max(max_relative_imaginary,float(relative))
                        assert relative<1e-7
                        assert max(roots.real)<0
                        nontrivial+=1
                    rows+=1
    return dict(physical_complete_support_rows=rows,
                Q_and_actual_P_polynomials=polynomials,
                nonconstant_root_regressions=nontrivial,
                max_relative_imaginary=max_relative_imaginary,
                role='Regression only; the all-N negative-root assertion is proved analytically.')


def main():
    result=dict(status='PASS',generic_symbolic_recurrences=symbolic_recurrence(),
                exact_levels=[exact_level(N,physical=N<=12) for N in range(2,18)],
                numerical=numerical_roots(),
                scope='Actual finite source polynomial, exact forced support, simple negative nonzero roots, and zero-free physical Fourier value. No global source gap or volume claim.')
    Path(__file__).with_name('actual_q_hahn_negative_root_source_polynomial_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',generic_symbolic_recurrences=result['generic_symbolic_recurrences'],
                         exact_recurrences=sum(r['exact_recurrences'] for r in result['exact_levels']),
                         exact_dualities=sum(r['exact_dualities'] for r in result['exact_levels']),
                         independent_peelings=sum(r['independent_Laurent_peelings'] for r in result['exact_levels']),
                         original_Casimir_entries=sum(r['original_Casimir_entries'] for r in result['exact_levels']),
                         numerical=result['numerical']),indent=2))


if __name__=='__main__':main()
