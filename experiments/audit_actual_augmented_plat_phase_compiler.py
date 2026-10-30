#!/usr/bin/env python3
"""Original complete augmented-plat kernels and their reduced q-Hahn phase."""
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import apply_pair
from audit_actual_marked_multiport_chebyshev_source_packet import pair_circle


def symbolic_phase():
    T,j,u,a=sp.symbols('T j u a')
    original=(-u+2*a+a*(a-1)+2*a*(T-j-u+a)
              +a*(j-a)+a*(u-a)+(j-a)*(T-u-j+a)-j*(T-j))
    assert sp.expand(original-(a*(T+j+1)-(j+1)*u))==0
    TT,JJ,UU,Z=sp.symbols('T J U Z')
    numerator=sp.expand(TT*(JJ-Z)**2*(UU-Z)+(Z-1)**2*(TT*Z-UU*JJ))
    assert sp.degree(numerator,Z)==2
    expected=(2*JJ*TT-JJ*UU+TT*UU-2*TT)*Z**2 \
        +(-JJ**2*TT-2*JJ*TT*UU+2*JJ*UU+TT)*Z+JJ**2*TT*UU-JJ*UU
    assert sp.expand(numerator-expected)==0
    return dict(internal_quadratic_phase_cancels=True,
                local_stationarity_degree=2, polynomial=str(expected))


def level(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    d=N-1;Q=q*q%p;x=pow(q,d,p);imag=pow(eta,N,p)
    assert imag*imag%p==p-1
    sf=[1]
    for n in range(1,N):
        sine=(pow(q,n,p)-pow(q,-n,p))*pow(imag,-1,p)%p
        sf.append(sf[-1]*sine%p)
    def beta(n,r):
        if min(r,n-r)<0:return 0
        return sf[n]*pow(sf[r]*sf[n-r]%p,-1,p)%p
    def value(T,j,u):
        total=0
        for a in range(max(0,u-(T-j)),min(j,u)+1):
            total+=pow(-1,a,p)*pow(q,a*(T+j+1),p)*beta(j,a)*beta(u,a)*beta(T-u,j-a)
        return pow(-1,u,p)*pow(q,-(j+1)*u,p)*total*pow(beta(T,j),-1,p)%p
    rho=(q-pow(q,-1,p))%p
    Et,Ft,Kt=coproduct(rho*rho*E%p,F,K,2,N,p)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    L=pair_circle(O,N,p)
    kappa=int(Rp[0,0])
    built={eps:np.zeros_like(L) for eps in (-1,0,1)}
    column_count=0;blocks=0
    for total in range(2*d+1):
        T=min(total,2*d-total);shift=max(0,total-d)
        ids=[(shift+u)*N+total-shift-u for u in range(T+1)]
        small=O[np.ix_(ids,ids)]
        for j in range((d//2)+1):
            if d-j>T:continue
            multiplicity=1 if 2*j==d else 2
            assert multiplicity==1 or j<d-j<=T
            v=np.array([value(T,j,u) for u in range(T+1)],dtype=np.int64)
            node=(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p
            assert np.array_equal(small@v%p,node*v%p)
            assert int(v[0])==1
            nu=pow(-1,j,p)*pow(q,j*(j+1),p)%p
            assert int(v[-1])==pow(x,T,p)*nu%p
            h=multiplicity*sf[T]**2*pow(sf[T-j]*sf[T+j-d]%p,-1,p)%p
            rankone=np.outer(v,v)%p
            for eps in (-1,0,1):
                coefficient=pow(kappa,eps,p)*pow(x,-T,p)*pow(nu,eps-1,p)*h%p
                built[eps][np.ix_(ids,ids)]=(built[eps][np.ix_(ids,ids)]+coefficient*rankone)%p
            column_count+=len(v)
        blocks+=1
    assert np.array_equal(built[0],L)
    assert np.array_equal(built[1],Rp@L%p)
    assert np.array_equal(built[-1],Rm@L%p)
    records=[]
    if N<=4:
        for k in (2,3,4):
            if k==4 and N==4:continue
            width=2*k
            cup=np.zeros(N*N,dtype=np.int64)
            ordinary=np.zeros(N*N,dtype=np.int64)
            marker=np.zeros(N*N,dtype=np.int64)
            for a,b in itertools.product(range(N),repeat=2):
                marker[a*N+b]=pow(x,b,p)*pow(N,-2,p)%p
                if a+b==d:
                    cup[a*N+b]=N*pow(x,-b,p)%p
                    ordinary[a*N+b]=pow(x,a,p)*pow(N,-1,p)%p
            state=np.array([1],dtype=np.int64);cap=np.array([1],dtype=np.int64)
            for pair in range(k):
                state=np.kron(state,cup)%p
                cap=np.kron(cap,marker if pair==k-1 else ordinary)%p
            direct=state.copy();compiled=state.copy()
            word=[(i,0) for i in range(2,2*k,2)]
            word += [(i,-1 if i%4==3 else 1) for i in range(1,2*k-1,2)]
            word += [(i,1 if i%4==0 else -1) for i in range(2,2*k,2)]
            for index,eps in word:
                literal=L if not eps else ((Rp if eps>0 else Rm)@L%p)
                direct=apply_pair(literal,direct[:,None],index-1,width,N,p)[:,0]
                compiled=apply_pair(built[eps],compiled[:,None],index-1,width,N,p)[:,0]
            assert np.array_equal(direct,compiled)
            raw=int(cap@direct%p)
            assert raw==int(cap@compiled%p)
            records.append(dict(k=k,augmented_word=word,whole_unrestricted_marked_source=raw))
    return dict(N=N,physical_blocks=blocks,canonical_column_entries=column_count,
                complete_signed_operator_identities=3,whole_plats=records)


def main():
    result=dict(status='PASS',phase=symbolic_phase(),levels=[level(N) for N in range(2,11)],
                scope='Exact complete-color operator and marked scalar compiler at every width. No selected complex saddle, mixed-color corridor, or volume equality is inferred.')
    Path(__file__).with_name('actual_augmented_plat_phase_compiler_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',levels=len(result['levels']),
                         physical_blocks=sum(v['physical_blocks'] for v in result['levels']),
                         canonical_column_entries=sum(v['canonical_column_entries'] for v in result['levels']),
                         original_marked_plats=sum(len(v['whole_plats']) for v in result['levels']),
                         stationary_polynomial_degree=2),indent=2))


if __name__=='__main__':
    main()
