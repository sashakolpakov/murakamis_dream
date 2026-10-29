#!/usr/bin/env python3
"""Actual marked pair-CD polynomial packet and finite tensor Chebyshev fold."""
import itertools,json
from pathlib import Path
import numpy as np
from audit_actual_two_cut_ports import balanced_data,coproduct
from audit_actual_complete_source_multiplicity_module import apply_pair


def axis_apply(A,v,axis,p):
    moved=np.moveaxis(v,axis,0)
    out=np.tensordot(A,moved,axes=(1,0))%p
    return np.moveaxis(out,0,axis)


def pair_circle(O,N,p):
    u,v=np.eye(N*N,dtype=np.int64),O.copy()
    for _ in range(2,N):u,v=v,(O@v-u)%p
    return (-1)**(N-1)*v%p


def continuant_values(N,q,p,nodes):
    Q=q*q%p;out=np.ones((len(nodes),N),dtype=np.int64)
    for j,c in enumerate(nodes):
        prev,current=0,1
        for a in range(N-1):
            diagonal=(4*q*pow(Q,a,p)-q*(1+Q)*pow(Q,2*a,p))%p
            forward=-(1-pow(Q,a+1,p))**2%p
            backward=-(1-pow(Q,a,p))**2%p
            nxt=((c-diagonal)*current-backward*prev)*pow(forward,-1,p)%p
            out[j,a+1]=nxt;prev,current=current,nxt
    return out


def level(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    d,Q,x=N-1,q*q%p,int(K[0,0]);M=d//2;rho=(q-pow(q,-1,p))%p
    Et,Ft,Kt=coproduct(rho*rho*E%p,F,K,2,N,p)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    L=pair_circle(O,N,p);swap=np.zeros_like(O)
    for a,b in itertools.product(range(N),repeat=2):swap[a*N+b,b*N+a]=1
    C,H=swap@L%p,L@swap%p
    middle=[a*N+d-a for a in range(N)]
    Cd,Hd=C[np.ix_(middle,middle)],H[np.ix_(middle,middle)]
    nodes=[(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p for j in range(M+1)]
    multiplicity=np.array([2]*(M+1),dtype=np.int64)
    if N%2:multiplicity[-1]=1
    V=continuant_values(N,q,p,nodes)
    Vbar=continuant_values(N,pow(q,-1,p),p,nodes)
    assert np.array_equal(Cd,N*(Vbar.T*multiplicity)@V%p)
    assert np.array_equal(Hd,N*(V.T*multiplicity)@Vbar%p)
    assert np.array_equal(V[0],np.array([pow(x,a,p) for a in range(N)],dtype=np.int64))
    cosine=np.ones((M+1,M+1),dtype=np.int64)
    if M:cosine[:,1]=np.array(nodes)*pow(2,-1,p)%p
    for r in range(1,M):cosine[:,r+1]=(np.array(nodes)*cosine[:,r]-cosine[:,r-1])%p
    powers=np.array([1]+[2]*M,dtype=np.int64)
    Dct=(powers[:,None]*cosine.T*multiplicity[None,:]*pow(N,-1,p))%p
    assert np.array_equal(Dct@cosine%p,np.eye(M+1,dtype=np.int64))
    assert int(np.sum(powers*cosine[0]**2)%p)==N*pow(2,-1,p)%p
    rng=np.random.default_rng(2917+N);records=[]
    for k in (1,2,3):
        psi=rng.integers(0,p,size=(N,)*k,dtype=np.int64)
        bra=rng.integers(0,p,size=(N,)*k,dtype=np.int64)
        values,left=psi.copy(),bra.copy();direct=psi.copy()
        for axis in range(k):
            values=axis_apply(Vbar if axis==k-1 else V,values,axis,p)
            left=axis_apply(V if axis==k-1 else Vbar,left,axis,p)
            direct=axis_apply(Hd if axis==k-1 else Cd,direct,axis,p)
        weights=np.ones((M+1,)*k,dtype=np.int64)
        coeff,right_coeff=values.copy(),left.copy()
        for axis in range(k):
            shape=[1]*k;shape[axis]=M+1
            weights=weights*multiplicity.reshape(shape)%p
            coeff=axis_apply(Dct,coeff,axis,p)
            right_coeff=axis_apply(Dct,right_coeff,axis,p)
        energy=int(np.sum(bra*direct)%p)
        grid=int(pow(N,k,p)*np.sum(weights*left%p*values)%p)
        assert energy==grid
        coeff_weights=np.ones((M+1,)*k,dtype=np.int64)
        for axis in range(k):
            shape=[1]*k;shape[axis]=M+1
            coeff_weights=coeff_weights*np.array([1]+[pow(2,-1,p)]*M).reshape(shape)%p
        parseval=int(pow(N,2*k,p)*np.sum(coeff_weights*coeff%p*right_coeff)%p)
        assert parseval==energy
        reconstructed=coeff.copy()
        for axis in range(k):reconstructed=axis_apply(cosine,reconstructed,axis,p)
        assert np.array_equal(reconstructed,values)
        raw=0
        for a in itertools.product(range(N),repeat=k):
            raw+=int(psi[a])*pow(x,sum(a[:-1])+d-a[-1],p)*pow(N,-k-1,p)
        assert raw%p==pow(x,d,p)*pow(N,-k-1,p)*int(values[(0,)*k])%p
        records.append({'pairs':k,'all_input_pair_CD_grid_Parseval_and_marked_corner':True})
    coupled=None
    if N<=5:
        width=6;cup=np.zeros(N*N,dtype=np.int64);ordinary=np.zeros(N*N,dtype=np.int64);marker=np.zeros(N*N,dtype=np.int64)
        for a,b in itertools.product(range(N),repeat=2):
            marker[a*N+b]=pow(x,b,p)*pow(N,-2,p)%p
            if a+b==d:
                cup[a*N+b]=N*pow(x,-b,p)%p
                ordinary[a*N+b]=pow(x,a,p)*pow(N,-1,p)%p
        state=np.kron(np.kron(cup,cup),cup)%p
        word=[2,-4,3,-2,4,1,-5,3]
        for letter in word:state=apply_pair(Rp if letter>0 else Rm,state[:,None],abs(letter)-1,width,N,p)[:,0]
        raw=int(np.kron(np.kron(ordinary,ordinary),marker)@state%p)
        psi=np.zeros((N,N,N),dtype=np.int64)
        for a,b,c in itertools.product(range(N),repeat=3):
            inds=(a,d-a,b,d-b,c,d-c)
            psi[a,b,c]=state[sum(v*N**(5-i) for i,v in enumerate(inds))]
        values=psi.copy()
        for axis in range(3):values=axis_apply(Vbar if axis==2 else V,values,axis,p)
        assert raw==pow(x,d,p)*pow(N,-4,p)*int(values[0,0,0])%p
        coupled={'actual_signed_sixhead_word':word,'unrestricted_original_marker_equal_coherent_corner':True}
    return {'N':N,'original_complete_circle_CD_and_source_phases':True,
            'tensor_all_input_packets':records,'coupled_original_source':coupled}


if __name__=='__main__':
    out={'status':'PASS','all_original_levels':[level(N) for N in range(2,9)],
         'scope':'All-port actual marked CD/DCT/Parseval identities and literal coupled sources. No sharp geometric packet-energy or normal-continuation assertion.'}
    Path(__file__).with_name('actual_marked_multiport_chebyshev_source_packet_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS 7 full physical CD levels/21 all-input tensor packets; 4 literal coupled sixhead marked sources')
