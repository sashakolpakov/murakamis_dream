#!/usr/bin/env python3
"""Actual semicyclic cap carry, literal integer degree, and full source tests."""

from itertools import product
import json
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field
from audit_relative_pivotal_duality import dual_data,semicyclic


def power(A,n,p):
    out=np.eye(len(A),dtype=np.int64)
    for _ in range(n):out=out@A%p
    return out


def case(N,kind,phi_kind):
    p,g,q=field(N);Q=q*q%p;d=N-1
    x=g if kind=='generic' else pow(q,d,p)
    phi=g if phi_kind==0 else pow(g,3,p)
    y,psi,J,pivot=dual_data(N,p,q,x,phi)
    _,F1,K1=semicyclic(N,p,q,x,phi)
    _,F2,K2=semicyclic(N,p,q,y,psi)
    A=np.kron(inv(F1,p),F2)%p
    low=np.zeros((N,N),dtype=np.int64);up=np.zeros_like(low)
    for a in range(1,N):low[a-1,a]=1;up[a,a-1]=1
    T=np.kron(low,up)%p
    D=np.diag([a+b for a,b in product(range(N),repeat=2)]).astype(np.int64)
    e0=np.zeros((N,N),dtype=np.int64);e0[0,0]=1
    ed=np.zeros_like(e0);ed[d,d]=1
    P1=np.kron(e0,np.eye(N,dtype=np.int64))
    P2=np.kron(np.eye(N,dtype=np.int64),ed)
    assert np.array_equal((D@A-A@D)%p,N*A@(P1-P2)%p)
    fiber=[a*N+d-a for a in range(N)]
    Ktotal=np.kron(K1,K2)%p
    invariant_indices=[j for j in range(N*N) if int(Ktotal[j,j])==1]
    assert invariant_indices==fiber
    assert all(int(D[j,j])+1==N for j in invariant_indices)
    restricted=A[np.ix_(fiber,fiber)]
    bare=low.copy();bare[d,0]=-pow(x,N,p)%p
    assert np.array_equal(restricted,bare)
    assert np.array_equal(D[np.ix_(fiber,fiber)],d*np.eye(N,dtype=np.int64))
    assert np.array_equal(P1[np.ix_(fiber,fiber)],P2[np.ix_(fiber,fiber)])
    assert np.array_equal(power(restricted,N,p),(-pow(x,N,p))*np.eye(N,dtype=np.int64)%p)

    # Original unbalanced cap and cup, from the actual pivotal duality matrices.
    Fs=[1]
    for a in range(1,N):Fs.append(Fs[-1]*(1-pow(Q,a,p))%p)
    diagF=np.diag(Fs).astype(np.int64)
    e=np.full((N,N),pow(N,-1,p),dtype=np.int64)
    Dmark=inv(diagF,p)@inv(pivot,p)@e@diagF%p
    marked=(Dmark.T@pivot@J%p).reshape(N*N)
    cup=inv(J,p).T.reshape(N*N)
    def source(O):return int(marked@O@cup)%p
    assert int(marked@cup)%p==1
    assert source(P1)==source(P2)==pow(N,-1,p)
    assert source(P1-P2)==0
    value=source(A-T)
    assert value==-x*pow(N,-1,p)%p
    C1=np.diag([pow(Q,a,p) for a,b in product(range(N),repeat=2)]).astype(np.int64)
    Cis=(inv(C1,p),np.eye(N*N,dtype=np.int64),np.eye(N*N,dtype=np.int64),C1)
    cs=(-Q*x,pow(x,-1,p),Q*x,-pow(x,-1,p))
    monomials=[];wall_values=[]
    for c,C in zip(cs,Cis):
        m=c*A@C%p;mt=c*T@C%p
        assert np.array_equal((D@m-m@D)%p,N*m@(P1-P2)%p)
        monomials.append(m)
        wall_values.append(source(m-mt))
    Y=Q*x*x%p
    assert wall_values==[Y*pow(N,-1,p)%p,-pow(N,-1,p)%p,
                        -Y*pow(N,-1,p)%p,pow(N,-1,p)%p]
    assert np.array_equal(monomials[0]@monomials[1]%p,
                          Q*monomials[1]@monomials[0]%p)
    bare_centers=[pow(x,2*N,p),-1%p,-pow(x,2*N,p)%p,1]
    for m,center in zip(monomials,bare_centers):
        assert np.array_equal(power(m[np.ix_(fiber,fiber)],N,p),
                              center*np.eye(N,dtype=np.int64)%p)

    # FULL original crossing/cup source, using independent original E coefficients.
    entries=MixedEntries(N,p,q)
    R=crossing(entries,x,y,1)
    cup_bal=np.array([int(cup[a*N+b])*Fs[a]*Fs[b]%p
                     for a,b in product(range(N),repeat=2)],dtype=np.int64)
    output=np.zeros(N*N,dtype=np.int64)
    for a in range(N):output[a*N+d-a]=N*pow(y,a-d,p)%p
    assert np.array_equal(R@cup_bal%p,output)
    output_mark=np.array([pow(y,b,p)*pow(N,-2,p)%p
                         for a,b in product(range(N),repeat=2)],dtype=np.int64)
    assert int(output_mark@R@cup_bal)%p==1
    # R00 common Cartan is retained externally; at completeness it is explicit.
    complete_normalization=None
    if kind=='complete':
        halfq=pow(g,(p-1)//(4*N),p)
        assert halfq*halfq%p==q
        kappa=pow(halfq,d*d,p)
        theta=kappa*pow(x,-d,p)%p
        assert kappa*theta%p==1
        assert wall_values==[pow(N,-1,p),-pow(N,-1,p)%p,
                            -pow(N,-1,p)%p,pow(N,-1,p)]
        complete_normalization={'actual_common_Cartan':kappa,'actual_twist':theta,
                                'zero_framed_marked_plat':kappa*theta%p}
    return {'N':N,'color':kind,'phi':int(phi),'dual_phi':int(psi),
            'total_degree_current_zero_on_actual_cup':True,
            'actual_charged_degree_D_plus_one_equals_N':True,
            'individual_marked_wall_charge':pow(N,-1,p),
            'marked_cyclic_minus_nilpotent_transfer':int(value),
            'four_common_frame_wall_coupon_values':wall_values,
            'bare_monomial_centers_on_dual_cup':bare_centers,
            'full_original_crossing_source_without_external_Cartan':1,
            'complete_normalization':complete_normalization}


def norm_table(N):
    p,g,q=field(N);k=pow(q,N*(N-1),p)
    assert k*k%p==1
    checks=[]
    for epsilon in (g,pow(g,2,p),pow(g,3,p)):
        r=(-k+epsilon)%p
        D1=(1+k*r)%p
        D2=(1-r*pow(k*D1%p,-1,p))%p
        centers=[-k*r%p,r*pow(k*D1%p,-1,p)%p,
                 k*r*pow(D1,-1,p)%p,-r*pow(k*D1*D2%p,-1,p)%p]
        expected=[(1-k*epsilon)%p,(1-k*pow(epsilon,-1,p))%p]*2
        expected=[expected[0],expected[1],expected[1],expected[0]]
        assert centers==expected
        assert [D1,D2,pow(D1,-1,p),pow(D2,-1,p)]==[
            k*epsilon%p,pow(k*epsilon%p,-1,p),pow(k*epsilon%p,-1,p),k*epsilon%p]
        checks.append({'epsilon':int(epsilon),'centers':centers})
    return {'N':N,'three_exact_four_atom_norm_charts':checks}


def paired_case(N):
    p,g,q=field(N);Q=q*q%p;d=N-1
    deltas=[]
    for e in range(1,40):
        delta=pow(g,e,p)
        if pow(delta,N,p) not in (1,p-1):deltas.append(delta)
        if len(deltas)==3:break
    T=np.zeros((N,N),dtype=np.int64)
    for j in range(N):T[j,(j+1)%N]=1
    A=np.diag([pow(Q,j,p) for j in range(N)]).astype(np.int64)
    Ai=inv(A,p);Ti=T.T
    I=np.eye(N,dtype=np.int64)
    def poch(z,n):
        out=1
        for h in range(n):out=out*(1-z*pow(Q,h,p))%p
        return out
    for delta in deltas:
        epsilon=(1-pow(delta,N,p))%p
        V=np.array([epsilon*pow((1-Q)*poch(Q*Q*delta%p,j)
                    *poch(Q*delta%p,d-j)%p,-1,p)%p for j in range(N)],dtype=np.int64)
        W=np.array([poch(Q*delta%p,j)*poch(delta,d-j)*pow(N,-1,p)%p
                    for j in range(N)],dtype=np.int64)
        LV=(I-delta*Q*Q*A)@T-(I-delta*pow(Q,-1,p)*Ai)
        LW=(I-delta*pow(Q,-1,p)*Ai)@Ti-(I-delta*Q*A)
        assert not np.any(LV@V%p)
        assert not np.any(W@LW%p)
        for j in range(N):
            assert V[(j+1)%N]*(1-delta*pow(Q,j+2,p))%p\
                ==V[j]*(1-delta*pow(Q,-j-1,p))%p
            assert W[(j+1)%N]*(1-delta*pow(Q,-j-2,p))%p\
                ==W[j]*(1-delta*pow(Q,j+1,p))%p
        G=int(W@V)%p
        expected=int(V[d])*(2-epsilon)*pow(1+delta,-1,p)%p
        assert G==expected and G
        pi=W*V*pow(G,-1,p)%p
        assert int(sum(pi))%p==1
        for j in range(N):
            formula=epsilon*(1-delta*delta)*pow(N*(2-epsilon)
                *(1-delta*pow(Q,j+1,p))*(1-delta*pow(Q,-j-1,p))%p,-1,p)%p
            assert int(pi[j])==formula
        for m in range(N+1):
            moment=sum(int(pi[j])*pow(Q,m*(j+1),p) for j in range(N))%p
            expected=(pow(delta,m,p)+pow(delta,N-m,p))*pow(1+pow(delta,N,p),-1,p)%p
            assert moment==expected
    return {'N':N,'exact_paired_Fermat_parameters':len(deltas),
            'both_cyclic_wraps_and_row_operator':True,
            'exact_scalar_Poisson_weights_and_all_clock_moments':True}


def positive_pair_diagnostics():
    mp.mp.dps=50;out=[]
    for N in (2,3,4,8,16,32):
        Q=mp.exp(2j*mp.pi/N)
        for epsilon in (mp.mpf('.01'),mp.mpf('.1'),mp.mpf('.5')):
            delta=(1-epsilon)**(mp.mpf(1)/N)
            def poch(z,n):return mp.fprod(1-z*Q**r for r in range(n))
            V=[epsilon/((1-Q)*poch(Q*Q*delta,j)*poch(Q*delta,N-1-j))
               for j in range(N)]
            W=[poch(Q*delta,j)*poch(delta,N-1-j)/N for j in range(N)]
            scalar=epsilon/(N*(1-delta));R=V[-1]
            error=max(abs(W[j]-scalar/mp.conj(R)*mp.conj(V[j])) for j in range(N))
            assert error<mp.mpf('1e-38')
            norm2=mp.fsum(abs(v)**2 for v in V)
            expected=abs(R)**2*(2-epsilon)/((1+delta)*scalar)
            assert abs(norm2-expected)<mp.mpf('1e-38')
            pi=[epsilon*(1-delta**2)/(N*(2-epsilon)*abs(1-delta*Q**(j+1))**2)
                for j in range(N)]
            assert min(pi)>0
            assert abs(mp.fsum(pi)-1)<mp.mpf('1e-40')
            out.append({'N':N,'epsilon':float(epsilon),'minimum_weight':float(min(pi)),
                        'corner_weight':float(pi[-1]),'sum':float(mp.fsum(pi)),
                        'selected_vector_norm_squared':float(norm2),
                        'co_source_is_normalized_Hermitian_dual':True})
    return out


if __name__=='__main__':
    result={'scope':'actual cap carry versus total degree; no last geometric Pachner-edge identification',
            'source_cases':[case(N,kind,ph) for N in range(2,13)
                            for kind in ('generic','complete') for ph in (0,1)],
            'four_atom_norm_charts':[norm_table(N) for N in range(2,13)],
            'paired_sources':[paired_case(N) for N in range(2,13)],
            'positive_diagonal_diagnostics':positive_pair_diagnostics()}
    path=Path(__file__).with_name('actual_degree_cap_winding_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(result['source_cases']),'original dual-cap families;',
          len(result['four_atom_norm_charts'])*3,'exact actual four-atom norm charts;',
          sum(c['exact_paired_Fermat_parameters'] for c in result['paired_sources']),
          'paired cyclic sources;',len(result['positive_diagonal_diagnostics']),'positive measures')
