#!/usr/bin/env python3
"""Canonical original nilpotent source and failure of positive closing."""
import json
from pathlib import Path
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import balanced_data,coproduct,partial,word_matrix
from audit_braided_source_groupoid import projector_zero


def ptr(H,T):
    N,p=H.N,H.p
    G=np.kron(np.eye(N,dtype=np.int64),np.diag(H.pivot))
    return np.einsum('abcb->ac',(T@G%p).reshape((N,)*4))%p


def cap_data(H):
    N,p,x,d=H.N,H.p,H.x,H.N-1
    cup=np.zeros((N*N,1),dtype=np.int64);cap=np.zeros((1,N*N),dtype=np.int64)
    for j in range(N):
        i=d-j
        cup[i*N+j,0]=N*pow(x,-j,p)%p
        cap[0,i*N+j]=pow(x,j,p)*int(H.pivot[i])*pow(N,-1,p)%p
    return cup,cap,cup@cap%p


def actual_source_cases():
    rows=[]
    for N in range(2,14):
        H=HardyNetwork(N,1);p,q=H.p,H.q
        cup,cap,Pi=cap_data(H)
        I=np.eye(N,dtype=np.int64);II=np.eye(N*N,dtype=np.int64)
        assert int((cap@cup)[0,0])%p==0 and not np.any(Pi@Pi%p) and np.any(Pi)
        assert not np.any(ptr(H,II)) and np.array_equal(ptr(H,Pi),I)
        assert int(ptr(H,Pi).sum())*pow(N,-1,p)%p==1
        _,_,_,E,F,K,g,R,Ri=balanced_data(N)
        Et,Ft,Kt=coproduct(E,F,K,2,N,p)
        assert not np.any(Et@cup%p) and not np.any(Ft@cup%p)
        assert np.array_equal(Kt@cup%p,cup)
        assert not np.any(cap@Et%p) and not np.any(cap@Ft%p)
        assert np.array_equal(cap@Kt%p,cap)
        for A in (Et,Ft,Kt,R):assert not np.any((A@Pi-Pi@A)%p)
        rho=(q-pow(q,-1,p))%p
        Kti=np.diag([pow(int(k),-1,p) for k in np.diag(Kt)])
        O=(rho*rho*(Ft@Et%p)+q*Kt+pow(q,-1,p)*Kti)%p
        e0=projector_zero(N,p,q,O)
        c0=(q+pow(q,-1,p))%p
        assert np.array_equal((O-c0*II)@e0%p,Pi*pow(-1,N,p)*rho*rho%p)
        B=R*pow(H.kappa,-1,p)%p
        J=e0@(B@B%p-II)%p
        coefficient=pow(-1,N+1,p)*(N-1)*rho%p
        assert np.array_equal(J,Pi*coefficient%p) and np.any(J) and not np.any(J@J%p)
        rows.append({'N':N,'original_pivot_trace_of_identity':0,
                     'original_pivotal_partial_trace_of_nilpotent':'I',
                     'original_marked_source_on_nilpotent':1,
                     'original_Hopf_invariant_cup_cap':True,
                     'retained_full_twist_nilpotent_coefficient':coefficient,
                     'nontrivial_original_crossing_Jordan_block':True})
    return rows


def whole_original_cases():
    rows=[]
    for N,width,word in [(2,3,[1,-2,1,-2]),(3,3,[1,-2,1,-2]),
                         (4,3,[1,-2,1,-2]),(2,2,[1,1,1]),
                         (3,2,[-1,-1,-1]),(3,3,[1,1,1,2,-1,2])]:
        H=HardyNetwork(N,1);p=H.p;I=np.eye(N,dtype=np.int64)
        _,_,Pi=cap_data(H)
        W=word_matrix(word,H.plus,H.minus,width,N,p)
        C=partial(W,H.pivot,width,N,p)
        scalar=int(C[0,0]);assert np.array_equal(C,scalar*I%p)
        restored=ptr(H,np.kron(C,I)@Pi%p)
        assert np.array_equal(restored,C)
        core=int(C.sum())*pow(N,-1,p)%p
        actual=int(restored.sum())*pow(N,-1,p)%p
        assert core==actual
        writhe=sum(1 if j>0 else -1 for j in word)
        external=H.dimension*pow(H.twist,-writhe,p)%p
        rows.append({'N':N,'width':width,'word':word,
                     'same_original_full_cut_matrix':True,
                     'same_original_period_with_full_external_line':external*actual%p})
    return rows


def flat_complex_norms():
    rows=[]
    for N in (2,3,5,12,32,64):
        q=np.exp(np.pi*1j/N);Q=q*q;x=-1/q
        g=np.array([x**(1-N)*Q**(-a) for a in range(N)])
        p=N*np.array([x**(-j) for j in range(N)])
        l=np.array([x**j*g[N-1-j]/N for j in range(N)])
        norm=np.linalg.norm(p)*np.linalg.norm(l)
        assert abs(norm/N-1)<1e-11
        assert abs(g.sum())<1e-10
        rows.append({'N':N,'rank_one_source_operator_norm':float(norm),
                     'exact_predicted_norm':N,'source_extraction_norm':N})
    return rows


def main():
    out={'canonical_original_source':actual_source_cases(),
         'all_original_knot_source_reconstruction':whole_original_cases(),
         'polynomial_source_norms':flat_complex_norms(),
         'scope':'universal actual-source obstruction to positive categorical closing/trace; '
                 'does not exclude emergent geometric positivity or establish a volume lower bound'}
    Path(__file__).with_name('audit_actual_quantum_source_positivity_results.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print('PASS 12 ORIGINAL Hopf cup/cap and Jordan source levels, '
          'six original whole-knot source reconstructions and six tame norm scales')


if __name__=='__main__':main()
