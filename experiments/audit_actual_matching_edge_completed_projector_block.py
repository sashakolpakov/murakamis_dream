#!/usr/bin/env python3
"""Actual categorical norm, target gauge, and completed collision jets."""
import json
from pathlib import Path
import numpy as np
from audit_actual_general_four_port_single_racah_kernel import facs,cg,target,seven_factorial_kernel
from audit_actual_trivalent_all_channel_marked_contraction import highest_cup_cap
from audit_actual_q_hahn_physical_generic_jet_bound import Jet,matrix,divide_simple_zero
from audit_actual_supported_racah_common_phase_and_normal_metric import quantum_units,factorials_without,mul,divide
from audit_high_color_first_normal_r_degree import root_field
import math


def omega(d,q,p):
    N=d+1;Q=q*q%p
    E=np.zeros((N,N),dtype=np.int64);F=E.copy()
    K=np.diag([pow(q,d-2*r,p) for r in range(N)]).astype(np.int64)
    Ki=np.diag([pow(q,-d+2*r,p) for r in range(N)]).astype(np.int64)
    I=np.eye(N,dtype=np.int64)
    for r in range(1,N):
        E[r-1,r]=pow(q,-N,p)*(1-pow(Q,N-r,p))%p
        F[r,r-1]=(1-pow(Q,r,p))%p
    Et=(np.kron(E,K)+np.kron(I,E))%p
    Ft=(np.kron(F,I)+np.kron(Ki,F))%p
    return (Ft@Et+q*np.kron(K,K)+pow(q,-1,p)*np.kron(Ki,Ki))%p


def generic():
    counts=dict(original_categorical_norms=0,full_projector_operator_entries=0,
                exact_clocked_target_identities=0,original_completed_rows=0)
    for p,q in [(1000003,2),(1000033,3)]:
        Q=q*q%p
        for N in range(2,8):
            d=N-1;F=facs(q,4*N,p)
            sf=lambda k:pow(q,-k*(k-1)//2,p)*F[k]*pow(1-Q,-k,p)%p
            qN=(pow(q,N,p)-pow(q,-N,p))*pow(q-pow(q,-1,p),-1,p)%p
            pV,ell=highest_cup_cap(d,q,p,N*pow(q,-d*d,p)%p)
            P=np.eye(N*N,dtype=np.int64).reshape((N,)*4).transpose(0,1,3,2).reshape(N*N,N*N)
            O=omega(d,q,p);I=np.eye(N*N,dtype=np.int64)
            lams=[(pow(q,2*g+1,p)+pow(q,-2*g-1,p))%p for g in range(N)]
            beta=pow(q,2*d*d+d,p)*pow(N,-2,p)*sf(2*d+1)*pow(qN*sf(d)**2,-1,p)%p
            Ps=[];Ds=[]
            def turn(S):
                S=S.reshape((N,)*4).transpose(3,0,1,2)
                clock=np.array([(-1)**d*pow(q,d-2*u,p)%p for u in range(N)])
                return (clock[:,None,None,None]*S%p).reshape(N*N,N*N)
            def bend(A):return A@np.kron(pV,pV)%p@P%p
            for g in range(N):
                W=cg(d,d,2*g,q,p,F);pg=highest_cup_cap(2*g,q,p)[0]
                dual=pg.T@W.T%p@np.kron(ell.T,ell.T)%p@P%p
                theta=(-1)**(d-g)*pow(q,2*d*d-g*g,p)*pow(N,-2,p)*sf(d+g+1)*pow(sf(d-g)*sf(2*g+1),-1,p)%p
                assert np.array_equal(dual@W%p,theta*np.eye(2*g+1,dtype=np.int64)%p)
                Pr=I.copy()
                for h in range(N):
                    if h!=g:Pr=Pr@(O-lams[h]*I)%p*pow(lams[g]-lams[h],-1,p)%p
                assert np.array_equal(W@dual%p,theta*Pr%p)
                h=(-1)**d*pow(q,g*g+d,p)*sf(g)**2*sf(d-g)**2*sf(2*g+1)*sf(2*d+1)*pow(sf(d)**2*sf(d+g+1)**2,-1,p)%p
                D=(-1)**g*qN*sf(g)**2*sf(d-g)*pow(sf(d+g+1),-1,p)%p
                assert h*theta%p==beta*D%p
                T=target(d,d,d,d,2*g,q,p,F).reshape(N*N,N*N)
                assert np.array_equal(h*T%p,beta*turn(bend(D*Pr%p))%p)
                Ps.append(Pr);Ds.append(D)
                counts['original_categorical_norms']+=1
                counts['full_projector_operator_entries']+=N**4
                counts['exact_clocked_target_identities']+=1
            assert np.array_equal(sum(Ps,np.zeros_like(I))%p,I)
            for a in range(d//2+1):
                Fweights=[];raw=np.zeros_like(I)
                for g in range(N):
                    normalization,S=seven_factorial_kernel(d,d,d,d,2*a,2*g,q,p,F,details=True)
                    G=(-1)**d*S*pow(qN,-1,p)%p
                    Fweights.append(G*Ds[g]%p)
                    raw=(raw+normalization*S*target(d,d,d,d,2*g,q,p,F).reshape(N*N,N*N))%p
                completed=np.zeros_like(I)
                for g in range(N//2):
                    gp=d-g;Cl=(Ps[g]+Ps[gp])%p;M=(O-lams[gp]*I)@Cl%p
                    H=(Fweights[g]-Fweights[gp])*pow(lams[g]-lams[gp],-1,p)%p
                    completed=(completed+Fweights[gp]*Cl+H*M)%p
                if d%2==0:completed=(completed+Fweights[d//2]*Ps[d//2])%p
                rho=pow(q,-a*a-d,p)*sf(d)**2*sf(a)**2*qN*pow(sf(2*a)*sf(2*d+1),-1,p)%p
                assert np.array_equal(raw,rho*beta*turn(bend(completed))%p)
                counts['original_completed_rows']+=1
    return counts


def root_pairs():
    counts=dict(completed_cluster_second_jets=0,cluster_idempotent_first_jets=0,
                nilpotent_and_moving_gap_first_jets=0,weighted_Hermite_second_jets=0,
                original_complete_measure_cancellations=0)
    for N in range(3,8):
        p,eta=root_field(N);q0=eta*eta%p;Jet.p=p;d=N-1
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        diag,up,low=matrix(N,q,d)
        O=np.array([[Jet() for _ in range(N)] for _ in range(N)],dtype=object)
        for r in range(N):
            O[r,r]=diag[r]
            if r<d:O[r,r+1]=up[r];O[r+1,r]=low[r]
        I=np.array([[Jet(int(r==s)) for s in range(N)] for r in range(N)],dtype=object)
        lams=[q**(2*g+1)+q**(-2*g-1) for g in range(N)]
        units=quantum_units(q0,p,2*N,order=4)
        ff=factorials_without(units,p,set());fn=factorials_without(units,p,{N})
        beta0=pow(q0,2*d*d+d,p)*pow(N,-2,p)*fn[2*d+1][0]*pow(ff[d][0]**2,-1,p)%p
        assert beta0==(-1)**d*pow(q0,d+2,p)*pow(N,-2,p)%p
        for a in range(d//2+1):
            k=1 if 2*a==d else 2
            h0=k*N*ff[2*a][0]*pow(ff[a][0]**2,-1,p)%p
            gamma=pow(q0,2-a*a,p)*pow(N,-2,p)%p
            rho0=pow(q0,-a*a-d,p)*ff[d][0]**2*ff[a][0]**2*pow(ff[2*a][0]*fn[2*d+1][0],-1,p)%p
            assert h0*pow(gamma,-1,p)*rho0*beta0%p==k*N%p
            counts['original_complete_measure_cancellations']+=1
        def normalized_num(g,gp):
            out=I.copy();den=Jet(1)
            for h in range(N):
                if h!=g:
                    out=out@(O-I*lams[h])
                    if h!=gp:den*=lams[g]-lams[h]
            return np.array([[v/den for v in row] for row in out],dtype=object)
        def extract(A,k):return np.array([[v.c[k] for v in row] for row in A],dtype=np.int64)
        def divide_matrix(A,gap):return np.array([[Jet(divide_simple_zero(v,gap)) for v in row] for row in A],dtype=object)
        def weight(a,g):
            lo=d+max(a,g);hi=min(2*d,d+a+g);G=[0]*4
            for z in range(lo,hi+1):
                den=[1,0,0,0]
                for k in [z-d-a]*2+[z-d-g]*2+[2*d-z]+[d+a+g-z]*2:den=mul(den,ff[k],p)
                term=divide(fn[z+1],den,p)
                G=[(v+(-1)**(d+z)*w)%p for v,w in zip(G,term)]
            D=divide(mul(mul(ff[g],ff[g],p),ff[d-g],p),fn[d+g+1],p)
            D=[(-1)**g*v%p for v in D]
            assert D[0]==1
            return Jet(mul(G,D,p))
        for g in range(N//2):
            gp=d-g;gap=lams[g]-lams[gp]
            Ag=normalized_num(g,gp);Ap=normalized_num(gp,g)
            Cl=divide_matrix(Ag-Ap,gap);M=(O-I*lams[gp])@Cl
            c0,c1=extract(Cl,0),extract(Cl,1);m0,m1=extract(M,0),extract(M,1)
            assert np.array_equal(c0@c0%p,c0)
            assert np.array_equal((c0@c1+c1@c0)%p,c1)
            assert np.array_equal(m0@m0%p,np.zeros_like(m0))
            assert np.array_equal((m0@m1+m1@m0)%p,gap.c[1]*m0%p)
            counts['completed_cluster_second_jets']+=1
            counts['cluster_idempotent_first_jets']+=1
            counts['nilpotent_and_moving_gap_first_jets']+=1
            for a in range(d//2+1):
                Fg,Fp=weight(a,g),weight(a,gp)
                assert Fg.c[0]==Fp.c[0]
                H=Jet(divide_simple_zero(Fg-Fp,gap))
                lhs=divide_matrix(Ag*Fg-Ap*Fp,gap)
                rhs=Cl*Fp+M*H
                for k in range(3):assert np.array_equal(extract(lhs,k),extract(rhs,k))
                counts['weighted_Hermite_second_jets']+=1
    return counts


def main():
    result=dict(status='PASS',generic=generic(),root_pairs=root_pairs(),
                scope='Actual categorical target norm and gauge; full generic projector recoupling and retained completed Hermite second jets. Native projector norms and coherent source estimates remain open.')
    Path(__file__).with_name('actual_matching_edge_completed_projector_block_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
