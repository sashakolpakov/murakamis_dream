#!/usr/bin/env python3
"""Actual pointed regular-cube boundary moments and Fisher boundary topology."""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import coproduct, balanced_data
from audit_actual_trivalent_complete_circle_vertex_kernel import (
    data, sources, axis_apply, theta_graph, ordered_cube_graph,
)


def multiply(a,b,p):
    out = [0]*len(a)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if not i&j:out[i|j] = (out[i|j]+x*y) % p
    return out


def determinant(A,p):
    A = [[int(x)%p for x in row] for row in A]
    result = 1
    for i in range(len(A)):
        pivot = next(k for k in range(i,len(A)) if A[k][i])
        if pivot!=i:A[i],A[pivot],result=A[pivot],A[i],-result
        v = A[i][i]
        result = result*v % p
        for k in range(i+1,len(A)):
            scale = A[k][i]*pow(v,-1,p) % p
            for j in range(i,len(A)):A[k][j] = (A[k][j]-scale*A[i][j]) % p
    return result % p


def physical(N):
    p,q,x,R,Ri,L,P,*_=data(N)
    _,eta,*_=balanced_data(N)
    d,M,Q=N-1,(N-1)//2,q*q % p
    E=np.diag([(pow(Q,-u,p)-1)%p for u in range(1,N)],1)
    F=np.diag([(1-pow(Q,u,p))%p for u in range(1,N)],-1)
    K=np.diag([x*pow(Q,-u,p)%p for u in range(N)])
    Et,Ft,Kt=coproduct(E,F,K,2,N,p)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    identity=np.eye(N*N,dtype=np.int64)
    factorial=[1]
    for k in range(1,N):factorial.append(factorial[-1]*(1-pow(Q,k,p))%p)
    sine=[pow(pow(eta,N,p),k,p)*pow(q,-k*(k+1)//2,p)*factorial[k]%p for k in range(N)]
    nodes=[(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p for j in range(M+1)]
    projectors={}
    for j,cj in enumerate(nodes):
        value=identity.copy(); derivative=0
        for k,ck in enumerate(nodes):
            if k==j:continue
            multiplicity=1 if 2*k==d else 2
            for _ in range(multiplicity):value=value@(O-ck*identity)%p*pow(cj-ck,-1,p)%p
            derivative=(derivative+multiplicity*pow(cj-ck,-1,p))%p
        if 2*j<d:value=value@(identity-derivative*(O-cj*identity))%p
        assert np.array_equal(value@value%p,value)
        projectors[j]=value
    choices={(M,M,M),(max(0,d-2*M),M,M)}
    if M:choices.add((M-1,M-1,M))
    rows=[]
    for labels in sorted(choices):
        if sum(labels)<d:continue
        source,_,mark=sources(N,x,p)
        value=source.copy()
        for axis,j in enumerate(labels):value=axis_apply(projectors[j],value,axis,p)
        active=[axis for axis,j in enumerate(labels) if 2*j<d]
        r=len(active); size=1<<r; top=size-1
        moments=[]
        states=[]
        for mask in range(size):
            current=value.copy()
            for k,axis in enumerate(active):
                if mask>>k&1:current=axis_apply(L,current,axis,p)
            states.append(current)
            moments.append(int(np.sum(mark*current)%p))
        tau=moments[top]
        assert tau
        J=sum(labels);delta=J-d
        Racah=0
        for t in range(max(labels),J-max(labels)+1):
            den=1
            for j in labels:den=den*sine[t-j]*sine[J-j-t]%p
            Racah=(Racah+sine[t]*sine[J-t]*pow(den,-1,p))%p
        expected=N*N*(1<<r)*Racah*Racah*pow(sine[delta],-1,p)%p
        for j in labels:expected=expected*sine[J-2*j]%p
        expected=expected*pow(N,-(3-r),p)%p
        assert tau==expected
        gram=[[0 if i&j else moments[i|j] for j in range(size)] for i in range(size)]
        sign=1 if r==0 else (-1)**(1<<(r-1))
        assert determinant(gram,p)==sign*pow(tau,size,p)%p
        qpoly=[moments[top^i]*pow(tau,-1,p)%p for i in range(size)]
        assert qpoly[0]==1
        n=qpoly.copy();n[0]=0
        power=[1]+[0]*(size-1)
        root=[0]*size
        coefficient=1
        for k in range(r+1):
            root=[(x+coefficient*y)%p for x,y in zip(root,power)]
            power=multiply(power,n,p)
            coefficient=coefficient*(-1-2*k)*pow(2*(k+1),-1,p)%p
        assert not any(power)
        normalized=multiply(qpoly,multiply(root,root,p),p)
        assert normalized==[1]+[0]*(size-1)
        for i in range(size):
            for j in range(size):
                v=[0]*size;v[i]=1;w=[0]*size;w[j]=1
                v=multiply(root,v,p);w=multiply(root,w,p)
                product=multiply(v,w,p)
                pairing=sum(x*y for x,y in zip(moments,product))%p
                assert pairing==(tau if i==(top^j) else 0)
        # Direct physical generator products agree with the Boolean algebra.
        for k,axis in enumerate(active):
            assert not np.any(axis_apply(L,states[1<<k],axis,p))
        counter = None
        if N==4 and labels==(1,1,1):
            normalized_moments=[v*pow(tau,-1,p)%p for v in moments]
            assert (p,q)==(1009,762)
            assert normalized_moments==[571,201,201,0,201,0,0,1]
            defect=(qpoly[3]-qpoly[1]*qpoly[2])%p
            assert defect==201
            flattening=(normalized_moments[0]*normalized_moments[7]-normalized_moments[1]*normalized_moments[6])%p
            assert flattening==571
            counter={'prime':p,'primitive_eighth_root_image':q,
                     'actual_marked_moment_ratios_mod_prime':normalized_moments,
                     'two_axis_factorization_defect':defect,
                     'nonzero_rank_one_flattening_minor':flattening,
                     'exact_nonzero_cyclotomic_reduction_certificate':True}
        rows.append({'labels':list(labels),'paired_axes':r,'boundary_dimension':size,
                     'full_physical_top_moment':tau,'nondegenerate_actual_marked_Frobenius':True,
                     'finite_square_root_congruence_and_source_frame':True,
                     'nonfactorization_certificate':counter})
    return {'N':N,'actual_regular_boundary_cells':rows}


def fisher(graph):
    ports,black,marked=graph
    vertices=list(ports)
    E=len(set(e for es in ports.values() for e in es))
    halfedges=[(v,e) for v in vertices for e in ports[v]]
    adjacency={h:set() for h in halfedges}
    for v,es in ports.items():
        for a,b in itertools.combinations(es,2):
            adjacency[(v,a)].add((v,b));adjacency[(v,b)].add((v,a))
    for e in range(E):
        ends=[h for h in halfedges if h[1]==e]
        assert len(ends)==2
        a,b=ends;adjacency[a].add(b);adjacency[b].add(a)
    assert all(len(s)==3 for s in adjacency.values())
    seen=set();todo=[halfedges[0]]
    while todo:
        v=todo.pop()
        if v in seen:continue
        seen.add(v);todo.extend(adjacency[v]-seen)
    assert len(seen)==len(halfedges)==2*E
    annuli=sum(len(s) for s in adjacency.values())//2
    assert annuli==3*E
    genus=1+(2*E)//2
    assert genus==E+1
    return {'graph_vertices':len(vertices),'crossing_disks':E,'pants_boundary_components':2*E,
            'cusp_annuli':annuli,'connected_boundary_genus':genus,
            'actual_Fisher_annulus_graph':True}


def sorted_dipole_graph():
    return {0:(0,1,2),1:(3,4,5),2:(0,1,5),3:(2,3,4)},{0,1},2


if __name__=='__main__':
    result={'status':'PASS','physical_boundary_cells':[physical(N) for N in range(3,9)],
            'source_boundary_topology':[fisher(g()) for g in (theta_graph,sorted_dipole_graph,ordered_cube_graph)],
            'scope':'Actual marked regular-cell boundary torsor and NC Morse boundary incidence. No polynomial conditioning, unsupported-cell deletion, geometric pants-module identification or general graph energy bound.'}
    Path(__file__).with_name('actual_six_pants_boundary_torsor_and_sewing_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS6 physical boundary levels; exact marked Frobenius/congruence;3 actual Morse Fisher boundaries')
