#!/usr/bin/env python3
"""Literal central cube/rung normalization and its positive Newton period."""
import json
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_generic_six_head_tetrahedral_source import Generic
from audit_actual_trivalent_complete_circle_vertex_kernel import data,ordered_cube_graph
from audit_actual_trivalent_full_cd_normalization_and_magnetic_growth import physical_columns,ordinary,canonical_three_j
from audit_actual_trivalent_all_channel_marked_contraction import cup_cap,dual_three
from audit_actual_nc_spin_one_flow_order_certificate import spin_graph
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local,graph_case


def turn(A,N,p,pv):
    d=N-1
    B=np.empty_like(A)
    for u in range(N):
        for b in range(N):
            for v in range(N):
                for e in range(N):B[u*N+b,v*N+e]=int(A[(d-u)*N+v,b*N+d-e])*pv[d-e]*pow(pv[d-u],-1,p)%p
    return B


def generic(N,q):
    g=Generic(N,q);p,d=g.p,g.d;m=d//2
    H=turn(g.projector[m],N,p,g.pv)
    mod=ordinary(m,q,p)
    theta=canonical_three_j((m,m,m),[mod]*3,q,p)
    cap=cup_cap(m,q,p)[1];dual=dual_three(theta,[cap]*3,p)
    for a in range(N):
        for b in range(N):
            for c in range(N):assert theta[a,b,c]==int(mod[2][a,a])*int(theta[b,c,a])%p
    Xi=spin_graph(ordered_cube_graph(),theta,dual,p)
    eta=(-1)**m*pow(q,-m*(3*m+1),p)*g.fac[3*m+1]*pow(g.fac[m]*g.fac[2*m+1],-1,p)%p
    anchor=(-1)**m*pow(q,-m*(m+3),p)%p
    coefficient=eta*pow(anchor*anchor,-1,p)%p
    E=g.projector[m].reshape((N,)*4)
    clock=np.diag(g.K)
    clock_inverse=np.array([pow(int(k),-1,p) for k in clock])
    rung0=np.einsum('arb,rcd->bacd',theta,dual)%p
    rung1=np.einsum('abr,drc->abcd',theta,dual)%p
    rung3=np.einsum('bra,cdr->abcd',theta,dual)%p
    assert np.array_equal(rung0,coefficient*(E*clock_inverse[:,None,None,None]%p)%p)
    assert np.array_equal(rung1,coefficient*(E*clock[None,None,None,:]%p)%p)
    assert np.array_equal(rung3,coefficient*(E*clock[None,:,None,None]%p)%p)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for e in range(N):
                    reflected=int(E[d-e,d-c,d-b,d-a])*g.pv[d-b]*g.pv[d-a]
                    reflected=reflected*pow(g.pv[d-e]*g.pv[d-c],-1,p)%p
                    assert E[a,b,c,e]==reflected
    H2=H@H%p;H4=H2@H2%p
    trace=int(np.trace(np.kron(g.K,g.K)@H4%p)%p)
    assert Xi==pow(coefficient,4,p)*trace%p
    # This stronger identity is NOT a premise and is false generically.
    assert not np.array_equal(turn(H2,N,p,g.pv),H2)
    return {'N':N,'generic_parameter':q,'literal_cyclic_clock':True,
            'full_original_rung_normalization':True,'all_three_clocked_rung_entries':True,
            'full_pivotal_projector_self_duality':True,'no_generic_square_turn_invariance_assumed':True}


def root_level(N):
    p,q,x,R,Ri,L,P,*_=data(N);d=N-1;m=d//2
    W,fac,(Et,Ft,Kt)=physical_columns(N,q,p)
    Wb,*_=physical_columns(N,pow(q,-1,p),p)
    E=W[m]@Wb[m].T%p@P%p
    pv=[N*pow(x,-(d-u),p)%p for u in range(N)]
    H=turn(E,N,p,pv)
    Ki=np.diag([pow(int(k),-1,p) for k in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    eye=np.eye(N*N,dtype=np.int64)
    _,eta,*_=__import__('audit_actual_two_cut_ports').balanced_data(N)
    imag=pow(eta,N,p)
    sine=[pow(imag,k,p)*pow(q,-k*(k+1)//2,p)*fac[k]%p for k in range(N)]
    nodes=[(pow(q,2*k+1,p)+pow(q,-2*k-1,p))%p for k in range(N)]
    z=[sine[m]**2*pow(sine[k]**2*sine[m-k]**2,-1,p)%p for k in range(m+1)]
    basis=[];current=eye.copy();reconstructed=np.zeros_like(eye)
    for k in range(N):
        basis.append(current)
        if k<=m:reconstructed=(reconstructed+z[k]*current)%p
        if k<d:current=(nodes[k]*eye-O)@current%p*pow((sine[k+1]*pow(sine[k],-1,p)%p)**2,-1,p)%p
    assert np.array_equal(H,reconstructed)
    alpha=[0]*N
    for i in range(m+1):
        for j in range(m+1):
            for k in range(max(i,j),i+j+1):
                mu=sine[i+j]*sine[k]*pow(sine[i]*sine[j]*sine[k-i]*sine[k-j]*sine[i+j-k],-1,p)%p
                alpha[k]=(alpha[k]+z[i]*z[j]*mu)%p
    H2=H@H%p
    assert np.array_equal(H2,sum((alpha[k]*basis[k] for k in range(N)),np.zeros_like(eye))%p)
    H4=H2@H2%p
    K=np.diag([x*pow(q*q%p,-u,p)%p for u in range(N)])
    period=pow(N,-1,p)*int(np.trace(np.kron(np.eye(N,dtype=np.int64),K)@H4%p)%p)%p
    assert period==sum(alpha[k]*alpha[d-k] for k in range(N))%p
    ids=[u*N+d-u for u in range(N)];A=O[np.ix_(ids,ids)]
    HM=H[np.ix_(ids,ids)]
    for j in range(m+1):
        vector=[1];prev=0
        for u in range(N-1):
            value=((nodes[j]-int(A[u,u]))*vector[-1]-(int(A[u,u-1])*prev if u else 0))*pow(int(A[u,u+1]),-1,p)%p
            prev=vector[-1];vector.append(value)
        value=int((HM@np.array(vector,dtype=np.int64)%p)[0])
        positive=sum(sine[j+k]*pow(sine[j-k]*sine[k]**2,-1,p)*z[k] for k in range(j+1))%p
        assert value==positive
    original=[]
    if N<=9:
        local=Local(N);S=sum(v*v for v in z)%p
        for powers in ([0]*12,[1,-2,3]+[0]*9):
            row=graph_case(local,'central_cube',ordered_cube_graph(),[m]*12,powers)
            predicted=pow(N,12,p)*pow(S,8,p)*period*pow(local.omega[m],sum(powers),p)%p
            assert row['original_marked_scalar']==predicted
            original.append({'signed_edge_powers':powers,'original_physical_marked_scalar':predicted})
    return {'N':N,'full_physical_half_degree_and_positive_nodes':True,
            'full_normal_Newton_period':period,'actual_central_cube_sources':original}


def profile(N):
    with mp.workdps(max(120,N+60)):
        m=(N-1)//2;sine=[mp.mpf(1)]
        for k in range(1,N):sine.append(sine[-1]*2*mp.sin(mp.pi*k/N))
        z=[(sine[m]/sine[k]/sine[m-k])**2 for k in range(m+1)]+[mp.mpf(0)]*m
        nodes=[2*mp.cos((2*k+1)*mp.pi/N) for k in range(N)]
        steps=[mp.mpf(0)]+[(2*mp.sin(mp.pi*k/N))**2 for k in range(1,N)]
        current=z[:];alpha=[mp.mpf(0)]*N
        for j in range(m+1):
            for k in range(N):alpha[k]+=z[j]*current[k]
            if j<m:current=[((nodes[j]-nodes[k])*current[k]+(steps[k]*current[k-1] if k else 0))/steps[j+1] for k in range(N)]
        assert min(alpha)>0
        value=mp.fsum(alpha[k]*alpha[N-1-k] for k in range(N))
        ang=mp.pi/4
        Lambda=lambda t:mp.im(mp.polylog(2,mp.exp(2j*t)))/2
        action=16/mp.pi*(Lambda(mp.pi/4+ang/2)+Lambda(mp.pi/4-ang/2))
        constant=4**(-3)*mp.sin(ang)*mp.cos(ang)**mp.mpf('-.5')/2
        ratio=value/(constant*N**mp.mpf('-4.5')*mp.exp(N*action))
        assert abs(ratio-1)<4/N
        return {'N':N,'precision':max(120,N+60),'positive_Newton_period_prefactor_calibration':mp.nstr(ratio,25),
                'scaled_N_error':mp.nstr(N*(ratio-1),20),'shared_core_action':mp.nstr(action,25)}


if __name__=='__main__':
    generic_rows=[generic(N,q) for N in (3,5,7) for q in (2,3)]
    roots=[root_level(N) for N in range(3,14,2)]
    profiles=[profile(N) for N in (17,33,65,129,257)]
    result={'status':'PASS','generic_rung_and_clock':generic_rows,'root_original_sources':roots,
            'positive_period_profiles':profiles,
            'scope':'Odd central cube sector only; full original mark/normals. No whole-label/even cube volume-conjecture claim.'}
    Path(__file__).with_name('actual_odd_central_cube_reflection_packet_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS6 generic rung families;6 full-normal odd root kernels/8 physical central cubes;5 sharp positive-period profiles')
