#!/usr/bin/env python3
"""Literal middle-wall Euler packet, original sources and exact Plancherel."""

import itertools,json
from pathlib import Path

import numpy as np

from audit_actual_shared_quantum_flags import head,shift,mm,euler,mpow,equal
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field
from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing


def local_data(N,mu=None):
    p,g,q=field(N);E=MixedEntries(N,p,q);Q,d=E.Q,N-1
    x=-pow(q,-1,p)%p;k=pow(x,N,p)
    if mu is None:mu=1
    Z,K,e,f=head(E,x);I=np.eye(N,dtype=np.int64);I2=np.eye(N*N,dtype=np.int64)
    S1=np.kron(shift(N,mu),I);S2=np.kron(I,shift(N,k*mu%p))
    X=x*mm(S2,inv(S1,p),p)%p
    Ed=np.kron(np.diag([0]*d+[1]),I)
    W=Ed@X%p
    n=np.kron(e,I)@S2%p
    nm=-np.kron(e,Z)@S2%p
    P=euler(E,n);A=euler(E,nm);Pi=inv(P,p)
    D=np.diag([pow(x,-a-b,p)*pow(Q,a*b,p)%p
               for a,b in itertools.product(range(N),repeat=2)]).astype(np.int64)
    Flip=np.zeros_like(I2)
    for a,b in itertools.product(range(N),repeat=2):Flip[b*N+a,a*N+b]=1
    L=mm(mm(mm(mm(Flip,D,p),A,p),W,p),P,p)
    B=crossing(E,x,x,1)
    equal(mm(mm(mm(Flip,D,p),A,p),P,p),B,p)
    return locals()


def actual_packets():
    rows=[]
    for N in range(2,11):
        p,g,q=field(N)
        for mu in (1,g,g*g%p):
            D=local_data(N,mu);p,Q,x,k,d=D['p'],D['Q'],D['x'],D['k'],N-1
            X,W,P,A,L=D['X'],D['W'],D['P'],D['A'],D['L']
            summed=np.zeros_like(X);power=np.eye(N*N,dtype=np.int64)
            for j in range(N):summed=(summed+power)%p;power=mm(X,power,p)
            equal(power,np.eye(N*N,dtype=np.int64),p)
            Z1=np.kron(D['Z'],D['I'])
            rhs=pow(x,2,p)*mm(inv(Z1,p),summed,p)%p
            equal(L,rhs,p)
            E0=summed*pow(N,-1,p)%p
            equal(mm(E0,E0,p),E0,p)
            # Explicit FULL entry formula, with every wrap exponent.
            for a,b,u,v in itertools.product(range(N),repeat=4):
                r=(a+b)%N
                value=0
                if (u+v)%N==r:
                    ei=(a+b-r)//N;eo=(u+v-r)//N
                    value=pow(x,a+u+2,p)*pow(k*mu,ei-eo,p)%p
                assert int(L[u*N+v,a*N+b])==value
            WH=mm(mm(D['Pi'],W,p),P,p)
            equal(mm(D['B'],WH,p),L,p)
            FZ=np.kron(np.diag([pow(F,-1,p) for F in D['E'].F]),D['I'])
            FH=mm(mm(D['Pi'],FZ,p),P,p)
            equal(mm(mm(FZ,W,p),inv(FZ,p),p),W*pow(N,-1,p)%p,p)
            equal(mm(mm(FH,WH,p),inv(FH,p),p),WH*pow(N,-1,p)%p,p)
            Gamma=np.kron(np.diag([pow(-1,j,p)*pow(Q,-j*(j-1)//2,p)*F*F%p
                                   for j,F in enumerate(D['E'].F)]),D['I'])
            equal(mm(mm(Gamma,W,p),inv(Gamma,p),p),N*N*pow(Q,-1,p)*W%p,p)
            cup=np.zeros(N*N,dtype=np.int64);marker=np.zeros_like(cup)
            for a,b in itertools.product(range(N),repeat=2):
                if a+b==d:cup[a*N+b]=N*pow(x,a-d,p)%p
                marker[a*N+b]=pow(x,b,p)*pow(N,-2,p)%p
            equal(X@cup,pow(Q,-1,p)*cup,p)
            assert not np.any(L@cup%p)
            assert int(marker@W@cup)%p==pow(N*Q,-1,p)
            # The bare and transported walls deliberately have different sources.
            assert int(marker@L@cup)%p==0
            # Original positive affine cap charge and nilpotent source.
            Pd=np.diag([int(a+b==d) for a,b in itertools.product(range(N),repeat=2)])
            Pcap=mm(Pd,E0,p)
            ghead=np.diag([pow(x,1-N,p)*pow(Q,-a,p)%p for a in range(N)])
            g1=np.kron(ghead,D['I'])
            ordinary=np.zeros(N*N,dtype=np.int64)
            for a in range(N):
                b=d-a
                ordinary[a*N+b]=pow(x,b,p)*int(ghead[a,a])*pow(N,-1,p)%p
            source=np.outer(cup,ordinary)%p
            equal(source,N*mm(g1,Pcap,p)%p,p)
            equal(mm(Pd,L,p),pow(x,N+1,p)*source%p,p)
            assert not np.any(source@source%p)
            # Non-scalar C checks the source identity before Schur reduction.
            Ctest=np.diag([pow(Q,a,p) for a in range(N)]).astype(np.int64)
            Ctest[d,0]=(int(Ctest[d,0])+1)%p
            opened=mm(np.kron(Ctest,D['I']),source,p)
            closed=mm(opened,np.kron(D['I'],ghead),p).reshape((N,)*4)
            equal(np.einsum('abcb->ac',closed)%p,Ctest,p)
            rows.append({'N':N,'wrap':mu,'full_operator_Fourier_identity':True,
                         'all_full_wrap_entries_compared':N**4,
                         'original_transported_input_wall_identity':True,
                         'marked_Phi_conjugation_factor':'1/N',
                         'factorial_Gamma_conjugation_factor':'N^2 Q^-1',
                         'actual_affine_charge_joint_Fourier_source':True,
                         'entire_nonscalar_cut_reproduced_before_scalar_reduction':True,
                         'original_cup_packet_zero_bare_wall_nonzero':True})
    return rows


def full_word_sources():
    rows=[]
    for N in range(2,7):
        D=local_data(N);p,Q,x=D['p'],D['Q'],D['x'];I=D['I']
        positive=D['B'];negative=inv(positive,p)
        WH=mm(mm(D['Pi'],D['W'],p),D['P'],p)
        L=D['L'];pivot=np.diag([pow(x,1-N,p)*pow(Q,-a,p)%p
                                for a in range(N)]).astype(np.int64)
        closer=np.kron(I,np.kron(pivot,pivot))
        factors=[np.kron(positive,I),np.kron(I,negative),
                 np.kron(positive,I),np.kron(I,negative)]
        for position in (0,2):
            left=right=np.eye(N**3,dtype=np.int64)
            for j,B in enumerate(factors):
                if j==position:
                    left=mm(left,np.kron(mm(positive,WH,p),I),p)
                    right=mm(right,np.kron(L,I),p)
                else:
                    left=mm(left,B,p);right=mm(right,B,p)
            equal(left,right,p)
            def cap(M):
                R=mm(M,closer,p).reshape((N,)*6)
                cut=np.einsum('abcdbc->ad',R)%p
                return int(cut.sum())*pow(N,-1,p)%p,cut
            a,C=cap(left);b,Dcut=cap(right)
            assert a==b and np.array_equal(C,Dcut)
            rows.append({'N':N,'word':[1,-2,1,-2],'positive_crossing_slot':position,
                         'entire_original_averaged_cut_preserved':True,
                         'specified_wall_period':a,'no_scalar_cut_replacement_after_insertion':True})
    return rows


def cshift(N,mu):
    S=np.zeros((N,N),complex)
    for a in range(N-1):S[a+1,a]=1
    S[0,N-1]=mu
    return S


def complex_plancherel():
    rows=[]
    rng=np.random.default_rng(2418)
    for N in range(2,14):
        Q=np.exp(2j*np.pi/N);x=-np.exp(-1j*np.pi/N);k=x**N
        for mu in (1.,np.exp(.37j)):
            X=x*np.kron(np.linalg.inv(cshift(N,mu)),cshift(N,k*mu))
            Z=np.kron(np.diag([Q**a for a in range(N)]),np.eye(N))
            U=np.zeros((N*N,N),complex)
            for r in range(N):
                for a in range(N):
                    b=(r-a)%N;eps=(a+b-r)//N
                    U[a*N+b,r]=x**(-a)*(k*mu)**(-eps)/np.sqrt(N)
            assert np.linalg.norm(U.conj().T@U-np.eye(N))<1e-11
            assert np.linalg.norm(X@U-U)<1e-10
            E=sum(np.linalg.matrix_power(X,j) for j in range(N))/N
            L=N*x*x*np.linalg.inv(Z)@E
            assert np.linalg.norm(E-U@U.conj().T)<1e-10
            assert abs(np.linalg.norm(L,2)-N)<1e-9
            assert np.linalg.norm(L.conj().T@L-N*N*E)<1e-8
            a=rng.normal(size=N*N)+1j*rng.normal(size=N*N)
            b=rng.normal(size=N*N)+1j*rng.normal(size=N*N)
            alpha=U.conj().T@Z@a;beta=U.conj().T@b
            assert abs(np.vdot(a,L@b)-N*x*x*np.vdot(alpha,beta))<1e-8
            F=np.array([[Q**(i*j)/np.sqrt(N) for j in range(N)] for i in range(N)])
            assert abs(np.vdot(F@alpha,F@beta)-np.vdot(alpha,beta))<1e-9
            Pd=np.diag([int(a+b==N-1) for a,b in itertools.product(range(N),repeat=2)])
            Pcap=Pd@E
            ghead=np.diag([x**(1-N)*Q**(-a) for a in range(N)])
            source=N*np.kron(ghead,np.eye(N))@Pcap
            assert np.linalg.norm(source@source)<1e-8
            assert np.linalg.norm(source.conj().T@source-N*N*Pcap)<1e-8
            C=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
            opened=np.kron(C,np.eye(N))@source
            assert abs(np.linalg.norm(opened,'fro')**2-N*np.linalg.norm(C,'fro')**2)<1e-7
            mode_sum=np.zeros_like(Pcap)
            mode_norm_sum=0.
            g1=np.kron(ghead,np.eye(N))
            for j in range(N):
                Zj=np.linalg.matrix_power(Z,j)
                Pj=Zj@Pcap@Zj.conj().T
                assert np.linalg.norm(Pj@Pj-Pj)<1e-10
                assert np.linalg.norm(np.einsum('abcb->ac',Pj.reshape((N,)*4))
                                      -np.eye(N)/N)<1e-10
                mode_source=N*g1@Pj
                closed=(mode_source@np.kron(np.eye(N),ghead)).reshape((N,)*4)
                assert np.linalg.norm(np.einsum('abcb->ac',closed)-np.eye(N))<1e-9
                assert abs(np.linalg.norm(np.kron(C,np.eye(N))@mode_source,'fro')**2
                           -N*np.linalg.norm(C,'fro')**2)<1e-7
                mode_norm_sum+=np.linalg.norm(np.kron(C,np.eye(N))@g1@Pj,'fro')**2
                mode_sum+=Pj
            assert np.linalg.norm(mode_sum-Pd)<1e-9
            assert abs(mode_norm_sum-np.linalg.norm(C,'fro')**2)<1e-8
            rows.append({'N':N,'unit_wrap_real_and_nonreal':True,'rank':N,
                         'exact_norm_formula':N,'one_channel_isometry_and_double_layer_verified':True,
                         'original_cap_Choi_Hilbert_Schmidt_identity_before_Schur':True,
                         'all_terminal_Fourier_modes_and_positive_average_verified':True})
    return rows


def main():
    result={'status':'PASS','literal_actual_wall_packets':actual_packets(),
            'whole_original_source_placement':full_word_sources(),
            'independent_complex_Fourier_Plancherel':complex_plancherel(),
            'scope':'Exact specified Euler-wall packet and matched transported source; not an arbitrary bare-wall relocation, global positive invariant or volume bound.'}
    Path(__file__).with_name('actual_middle_wall_fourier_packet_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact original middle-wall Fourier packet, matched full sources, Phi factors and Plancherel')


if __name__=='__main__':main()
