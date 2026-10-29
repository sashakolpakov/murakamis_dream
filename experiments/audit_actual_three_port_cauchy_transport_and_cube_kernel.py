#!/usr/bin/env python3
"""Literal cube boundary transfer and original projected-chain sources."""
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_nc_morse_graph_first_normal_source_reduction import Local,graph_case
from audit_actual_odd_central_cube_reflection_packet import turn
from audit_actual_trivalent_complete_circle_vertex_kernel import ordered_cube_graph,theta_graph
from audit_actual_nc_spin_one_flow_order_certificate import insert_cube


def chain_graph(k):
    graph=theta_graph();fixed={0,2};vertex=0
    for _ in range(k):
        graph,new=insert_cube(graph,vertex)
        fixed={0 if e==0 else 10 if e==1 else 11 if e==2 else e+9 for e in fixed}
        fixed|={2,3,5,6,8,9}
        vertex=new[0]
        assert graph[0][vertex]==(0,1,2)
    E=3+9*k
    assert len(fixed)==2+6*k
    return graph,fixed,[e for e in range(E) if e not in fixed]


def kernel_level(N):
    local=Local(N);p,d=local.p,N-1;m=d//2
    pv=[int(local.cup[0][u,d-u]) for u in range(N)]
    I=np.eye(N*N,dtype=np.int64)
    Est=local.W[m][0]@local.pi[m][0]%p
    H={};P={};F=np.zeros_like(I)
    for j in range(m+1):
        circle=local.h0[j]*local.W[j][0]%p@local.pi[j][0]%p
        mult=1 if j==m else 2
        H[j]=turn(circle,N,p,pv)*pow(N*mult,-1,p)%p
        P[j]=int(np.trace(Est@H[j]%p)%p)*pow(N,-1,p)%p
        F=(F+mult*P[j]**2*H[j])%p
    F2=F@F%p
    pivot=np.kron(np.eye(N,dtype=np.int64),local.ordinary[m][2][0])
    theta=[N**3*(1 if j==m else 2)*P[j]**2%p for j in range(m+1)]
    B=np.zeros((m+1,m+1),dtype=np.int64)
    for j,l in itertools.product(range(m+1),repeat=2):
        product=H[j]@H[l]%p@F2%p
        period=int(np.trace(pivot@product%p)%p)*pow(N,-1,p)%p
        expected=pow(N,12,p)*(1 if j==m else 2)*(1 if l==m else 2)*P[j]**2*P[l]**2*period%p
        actual=0
        for a,b in itertools.product(range(m+1),repeat=2):
            labels=[m]*12
            for edge,value in ((10,j),(1,l),(4,a),(7,b)):labels[edge]=value
            actual+=graph_case(local,'two_boundary_cube',ordered_cube_graph(),labels,[0]*12)['original_marked_scalar']
        assert actual%p==expected
        B[j,l]=expected
    assert np.array_equal(B,B.T)
    M=np.array([pow(int(t),-1,p) for t in theta])[:,None]*B%p
    # Actual source recursion, using the weighted packet without requiring
    # a square root choice in the finite field.
    chain=[]
    for k in (0,1,2) if N==3 else (0,1):
        graph,fixed,rungs=chain_graph(k)
        actual=0
        for js in itertools.product(range(m+1),repeat=len(rungs)):
            labels=[m]*(3+9*k)
            for edge,j in zip(rungs,js):labels[edge]=j
            actual+=graph_case(local,'projected_chain',graph,labels,[0]*len(labels))['original_marked_scalar']
        vector=np.ones(m+1,dtype=np.int64)
        for _ in range(k):vector=M@vector%p
        predicted=int(np.array(theta,dtype=np.int64)@vector%p)
        assert actual%p==predicted
        chain.append({'cube_insertions':k,'vertices':2+6*k,'fixed_cycle_edges':len(fixed),
            'fully_summed_rung_edges':len(rungs),'actual_original_marked_scalar':predicted})
    return {'N':N,'prime':p,'two_boundary_kernel_entries':(m+1)**2,
        'independent_original_four_rung_contractions':(m+1)**4,
        'actual_weighted_kernel_symmetry':True,'whole_projected_sources':chain}


def exact_three_level():
    # At N=3: h0=1,h1=1+B1 and B1²=B1+B2; all products with
    # index sum >=3 vanish in the FULL repeated-root algebra.
    def mul(a,b):
        out=[sp.S.Zero]*3
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if not i:out[j]+=x*y
                elif not j:out[i]+=x*y
                elif i==j==1:out[1]+=x*y;out[2]+=x*y
        return out
    h=[[1,0,0],[1,1,0]];f=[6,4,0];f2=mul(f,f)
    phi=lambda a,b:sum(a[i]*b[2-i] for i in range(3))
    Q=sp.Matrix([[phi(mul(a,b),f2) for b in h] for a in h])
    assert Q==sp.Matrix([[16,80],[80,244]]) and Q.det()==-2496
    D=sp.diag(sp.sqrt(2),2)
    A=3**9*D*Q*D
    assert A.det()==-19968*3**18
    return {'exact_phi_matrix':str(Q),'phi_determinant':int(Q.det()),
        'normalized_transfer_determinant':int(A.det()),'positive_entries_do_not_imply_PSD':True}


if __name__=='__main__':
    small=exact_three_level()
    rows=[kernel_level(N) for N in (3,5,7)]
    out={'status':'PASS','exact_non_PSD_certificate':small,'physical_kernels':rows,
        'scope':'Actual odd projected cycle sources and full rung sums, original exposed mark. Norm/rate proof uses positive Newton inequalities; no full cube/all-parity invariant equality.'}
    Path(__file__).with_name('actual_three_port_cauchy_transport_and_cube_kernel_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS exact non-PSD certificate;3 full two-boundary physical kernels/353 rung contractions;7 whole projected chain sources')
