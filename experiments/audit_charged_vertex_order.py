#!/usr/bin/env python3
"""Diagnostic: root charges versus the actual face-order adapters.

This searches the finite root translates of the literal basic kernel.
It is not an invariance proof. Each comparison keeps the actual face
metrics and corrected cyclic adapters. Scalar charged prefactors do
not affect this projective diagnostic, but are not deleted from any
actual period.
"""

from functools import cache
from itertools import permutations,product
import json
from pathlib import Path

import numpy as np

from audit_actual_peripheral_fusion import inverse_mod
from audit_oriented_tetrahedron_source import axis_action,scalar_ratio
from audit_regular_holonomy_braiding import mm
from audit_standard_face_gluing import configuration,FaceFrames
from audit_standard_matrix_dilog_comparison import basic_kernel


def tensor_of(cfg,t,R,raw_cyclic=False):
    i,j,k,l=t;N=cfg.N;p=cfg.p
    A,B,C,D=(i,k,l),(i,j,k),(i,j,l),(j,k,l)
    sign=(-1)**sum(t[a]>t[b] for a in range(4) for b in range(a+1,4))
    if sign==1:
        matrix=mm(p,R,np.kron(inverse_mod(cfg.face(A),p).T,inverse_mod(cfg.face(B),p).T))
        value=np.transpose(matrix.reshape((N,)*4),(1,2,0,3));faces=[D,A[::-1],C,B[::-1]]
    else:
        matrix=mm(p,inverse_mod(R,p),np.kron(inverse_mod(cfg.face(C),p).T,inverse_mod(cfg.face(D),p).T))
        value=np.transpose(matrix.reshape((N,)*4),(3,0,2,1));faces=[D[::-1],A,C[::-1],B]
    canonical=[(1,2,3),(3,2,0),(0,1,3),(2,1,0)]
    for axis,face in enumerate(faces):
        target=canonical[t[axis]]
        if raw_cyclic:
            S=np.eye(N,dtype=np.int64);current=face
            for _ in range(3):
                if current==target:break
                S=mm(p,cfg.rotation(current),S)
                current=current[1:]+current[:1]
            assert current==target
        else:S=cfg.face_alignment(face,target)
        value=axis_action(value,S,axis,p)
    return np.transpose(value,tuple(t.index(v) for v in range(4)))


def projective_key(value,p):
    flat=value.reshape(-1)
    lead=int(flat[np.flatnonzero(flat)[0]])
    return tuple(int(x) for x in flat*pow(lead,-1,p)%p)


def case(N,keep_actual_relative_mark,raw_cyclic=False):
    cfg,B=configuration(N);p=cfg.p;Q=cfg.Q;frames=FaceFrames(cfg,B)
    rootlogs={pow(Q,r,p):r for r in range(N)}
    @cache
    def raw_map(t,a,b):
        i,j,k,l=t
        A,Bf,C,D=(i,k,l),(i,j,k),(i,j,l),(j,k,l)
        GA,eta,aA,_=frames.data(A);GB,rhoB,aB,_=frames.data(Bf)
        GC,alpha,aC,_=frames.data(C);GD,beta,aD,_=frames.data(D)
        gamma=aA*pow(aD,-1,p)%p;u=alpha*pow(gamma,-1,p)%p;v=aC*pow(aA,-1,p)%p
        L=basic_kernel(N,p,Q,u*pow(Q,a,p)%p,v*pow(Q,b,p)%p)
        if keep_actual_relative_mark:
            e=rootlogs[gamma*pow(rhoB,-1,p)%p]
            d=rootlogs[cfg.q*gamma*beta*v*pow(aB,-1,p)%p]
            W=np.zeros((N,N),dtype=np.int64)
            for r in range(N):W[(r-e)%N,r]=pow(Q,d*((r-e)%N),p)
            L=mm(p,L,np.kron(W,np.eye(N,dtype=np.int64)))
        return mm(p,np.kron(inverse_mod(GC,p),inverse_mod(GD,p)),L,cfg.flip,np.kron(GA,GB))

    reference=(0,1,2,3)
    choices={}
    for a,b in product(range(N),repeat=2):
        value=tensor_of(cfg,reference,raw_map(reference,a,b),raw_cyclic)
        choices[projective_key(value,p)]=(a,b,value)
    survivors=set(choices)
    orderings=[(1,2,0,3),(1,0,2,3),(0,2,1,3),(0,1,3,2)]
    orderings +=[t for t in permutations(range(4)) if t not in orderings and t!=reference]
    records=[]
    for t in orderings:
        by_key={}
        for a,b in product(range(N),repeat=2):
            value=tensor_of(cfg,t,raw_map(t,a,b),raw_cyclic)
            by_key[projective_key(value,p)]=(a,b,value)
        common=survivors&set(by_key)
        records.append({'ordering':list(t),'reference_root_choices_surviving':len(common)})
        if not common:
            result={'level':N,'prime':p,'actual_relative_input_mark_retained':keep_actual_relative_mark,'raw_cyclic_map':raw_cyclic,
                    'checked_orderings':records,'all_orders_share_a_projective_root_translate':False}
            if N==3 and keep_actual_relative_mark and not raw_cyclic:
                certificates=[]
                for a,b,c,d in product(range(N),repeat=4):
                    first=tensor_of(cfg,reference,raw_map(reference,a,b)).reshape(-1)
                    second=tensor_of(cfg,t,raw_map(t,c,d)).reshape(-1)
                    i=int(np.flatnonzero(first)[0])
                    j=next(j for j in range(len(first))
                           if (int(second[j])*int(first[i])-int(first[j])*int(second[i]))%p)
                    minor=(int(second[j])*int(first[i])-int(first[j])*int(second[i]))%p
                    certificates.append({'reference_shifts':[a,b],'changed_shifts':[c,d],
                                         'indices':[i,j],'reference_values':[int(first[i]),int(first[j])],
                                         'changed_values':[int(second[i]),int(second[j])],
                                         'nonzero_proportionality_minor':minor})
                result['complete_odd_level_regular_reduction_certificate']={
                    'q':cfg.q,'Q':cfg.Q,'flag_roots':cfg.flags,'flag_points':cfg.points,
                    'edge_difference_roots':[
                        {'edge':[i,j],'root':B[i,j]} for i,j in product(range(4),repeat=2) if i<j],
                    'all_81_pairs_have_nonzero_minors':certificates}
            return result
        survivors=common
    key=next(iter(survivors));a0,b0,reference_value=choices[key]
    witnesses=[]
    for t in (reference,*orderings):
        for a,b in product(range(N),repeat=2):
            value=tensor_of(cfg,t,raw_map(t,a,b),raw_cyclic)
            if projective_key(value,p)==key:
                witnesses.append({'ordering':list(t),'root_shifts':[a,b],
                                  'actual_projective_scalar':scalar_ratio(value,reference_value,p)})
                break
        else:raise AssertionError('lost selected root witness')
    return {'level':N,'prime':p,'actual_relative_input_mark_retained':keep_actual_relative_mark,'raw_cyclic_map':raw_cyclic,
            'checked_orderings':records,'all_orders_share_a_projective_root_translate':True,
            'reference_root_shifts':[a0,b0],'witnesses':witnesses}


def main():
    records=[]
    for N in (2,3,5):
        for retain,raw in product((True,False),repeat=2):
            result=case(N,retain,raw);records.append(result)
            print(f'N={N}, relative mark={retain}, raw cyclic={raw}: S4 root-translate orbit test {result["all_orders_share_a_projective_root_translate"]}',flush=True)
    result={'scope':'Projective diagnostic using the existing actual face-order prescription and finite kernel root charges. This neither assumes nor disproves the published decorated tensor symmetries.',
            'cases':records}
    Path(__file__).with_name('charged_vertex_order_results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
