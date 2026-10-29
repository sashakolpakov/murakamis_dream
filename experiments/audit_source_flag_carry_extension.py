#!/usr/bin/env python3
"""Extend source flags through the common carry lattice, with actual cuts.

Finite source kernels are checked against independently constructed
pointed fusion trees in the physical endpoint frames. Infinity uses
valuation/leading-coefficient carry data, with its full grading sign.
No global geometric quantum-A or volume theorem is asserted.
"""

from functools import cache
from itertools import product
import json
from math import comb
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod
from audit_carry_recoupling_lattice import trees,leaves,nodes,row_matrix,carry_crossings
from audit_cyclic_steinberg_lattice import determinant
from audit_kashaev_ado_pointing import WORDS,color_matrices,reduced_period
from audit_regular_holonomy_braiding import mm
from audit_relative_pivotal_duality import endpoint_module,pointed_fusion
from audit_standard_matrix_dilog_comparison import evaluation


@cache
def chart(N,b):
    for multiple in range(10,1000):
        p=12*N*multiple+1
        if not sp.isprime(p):continue
        roots={pow(x,N,p):x for x in range(1,p)}
        candidates=sorted(x for x in roots if x!=1 and (x-1)%p in roots)
        if len(candidates)<b+1:continue
        delta=tuple(candidates[:b+1])
        generator=int(sp.primitive_root(p))
        q=pow(generator,(p-1)//(2*N),p)
        return p,generator,q,delta,tuple(roots[x] for x in delta),tuple(roots[(x-1)%p] for x in delta)
    raise AssertionError('no source chart')


def tensor(values,prime):
    out=np.ones((1,1),dtype=np.int64)
    for value in values:out=np.kron(out,value)%prime
    return out


def factorials(N,p,Q,a,b):
    values=[1]
    for j in range(1,N):values.append(values[-1]*(a-b*pow(Q,j,p))%p)
    assert all(values)
    return values


def raw_tree(N,p,Q,C,tree):
    if isinstance(tree,int):return np.eye(N,dtype=np.int64)
    L,R=tree;il=leaves(L);ir=leaves(R);size=len(il)+len(ir)
    a,k,z=il[0],ir[0],ir[-1]+1
    left=endpoint_module(N,p,Q,1,C[k],C[a])
    right=endpoint_module(N,p,Q,1,C[z],C[k])
    local=pointed_fusion(N,p,Q,left,right)
    work=np.kron(local,np.eye(N**(size-2),dtype=np.int64))
    permutation=[0,*range(2,1+len(il)),1,*range(1+len(il),size)]
    work=work.reshape((N,)*(2*size)).transpose((*permutation,*range(size,2*size))).reshape(N**size,N**size)
    return mm(p,np.kron(raw_tree(N,p,Q,C,L),raw_tree(N,p,Q,C,R)),work)


def actual_tree(N,p,Q,C,tree):
    b=len(leaves(tree));H=evaluation(N,p,Q,1);Hi=inverse_mod(H,p)
    ds=[factorials(N,p,Q,C[j],C[j+1]) for j in range(b)]
    leafinverse=tensor([np.array([pow(int(x),-1,p) for x in d],dtype=np.int64)[:,None]*H%p for d in ds],p)
    dt=factorials(N,p,Q,C[0],C[-1])
    total=Hi*np.array(dt,dtype=np.int64)[None,:]%p
    return mm(p,leafinverse,raw_tree(N,p,Q,C,tree),
              np.kron(total,np.eye(N**(b-1),dtype=np.int64)))


def finite_kernel(N,p,Q,C,tree):
    b=len(leaves(tree));states=list(product(range(N),repeat=b));internal=nodes(tree)
    dleaf=[factorials(N,p,Q,C[j],C[j+1]) for j in range(b)]
    dtotal=factorials(N,p,Q,C[0],C[-1])
    result=np.zeros((N**b,N**b),dtype=np.int64)
    for row,state in enumerate(states):
        r=sum(state)%N
        scale=dtotal[r]
        for j,i in enumerate(state):scale=scale*pow(dleaf[j][i],-1,p)%p
        values=np.array([scale],dtype=np.int64)
        for L,R in internal:
            I=L+R;a,k,z=I[0],R[0],I[-1]+1
            alpha=C[z]*pow(C[a],-1,p)%p
            beta=C[z]*pow(C[k],-1,p)%p
            rootfactor=C[a]*pow(C[k],-1,p)%p
            ri=sum(state[j] for j in I)%N;rr=sum(state[j] for j in R)%N
            coeff=[1];value=1
            for d in range(1,N):
                value=value*rootfactor*(1-alpha*pow(Q,d+ri,p))*pow(1-beta*pow(Q,d+rr,p),-1,p)%p
                coeff.append(value)
            values=np.kron(values,np.array(coeff,dtype=np.int64))%p
        result[row,r*N**(b-1):(r+1)*N**(b-1)]=values
    assert determinant(result,p)
    return result


def infinity_kernel(N,p,Q,delta,tree):
    b=len(leaves(tree));directions=[(delta[j+1]-delta[j])*pow(N,-1,p)%p for j in range(b)]
    leading,carries,_,_=row_matrix(N,p,Q,directions,tree)
    H=evaluation(N,p,Q,1)
    d=factorials(N,p,Q,1,1)
    scales=[]
    for state,kappa in zip(product(range(N),repeat=b),carries):
        value=pow(-1,int(kappa),p)*d[sum(state)%N]%p
        for i in state:value=value*pow(d[i],-1,p)%p
        scales.append(value)
    matrix=mm(p,np.array(scales,dtype=np.int64)[:,None]*leading%p,
              np.kron(inverse_mod(H,p),np.eye(N**(b-1),dtype=np.int64)))
    assert determinant(matrix,p)
    return matrix


def branch_infinity_kernel(N,p,Q,delta,tree,marks):
    """Leading t^w M at a general relative-root branch over infinity."""
    b=len(leaves(tree));states=list(product(range(N),repeat=b));internal=nodes(tree)
    increments=[(marks[j+1]-marks[j])%N for j in range(b)]
    total_increment=(marks[-1]-marks[0])%N
    winding=(sum(increments)-total_increment)//N
    assert 0<=winding<=b-1

    def poch(shift,direction):
        values=[1];orders=[0]
        for j in range(1,N):
            phase=pow(Q,shift+j,p)
            value=direction if phase==1 else (1-phase)%p
            assert value
            values.append(values[-1]*value%p)
            orders.append(orders[-1]+int(phase==1))
        return values,orders

    def ds(a,z):
        values,orders=poch(marks[z]-marks[a],(delta[z]-delta[a])*pow(N,-1,p)%p)
        return [value*pow(Q,marks[a]*j,p)%p for j,value in enumerate(values)],orders

    leaf=[ds(j,j+1) for j in range(b)];dt,vt=ds(0,b)
    result=np.zeros((N**b,N**b),dtype=np.int64)
    for row,state in enumerate(states):
        r=sum(state)%N;kappa=sum(state)//N
        coefficient=pow(-1,kappa,p)*dt[r]%p
        valuation=winding+kappa+vt[r]
        for j,i in enumerate(state):
            coefficient=coefficient*pow(leaf[j][0][i],-1,p)%p
            valuation-=leaf[j][1][i]
        coeff=np.array([coefficient],dtype=np.int64);orders=np.array([valuation],dtype=np.int64)
        for L,R in internal:
            I=L+R;a,k,z=I[0],R[0],I[-1]+1
            ri=sum(state[j] for j in I)%N;rr=sum(state[j] for j in R)%N
            num,vn=poch(ri+marks[z]-marks[a],(delta[z]-delta[a])*pow(N,-1,p)%p)
            den,vd=poch(rr+marks[z]-marks[k],(delta[z]-delta[k])*pow(N,-1,p)%p)
            values=[num[d]*pow(den[d],-1,p)*pow(Q,(marks[a]-marks[k])*d,p)%p for d in range(N)]
            coeff=np.kron(coeff,np.array(values,dtype=np.int64))%p
            orders=(orders[:,None]+np.array(vn)[None,:]-np.array(vd)[None,:]).reshape(-1)
        assert np.all(orders>=0)
        result[row,r*N**(b-1):(r+1)*N**(b-1)]=np.where(orders==0,coeff,0)
    assert determinant(result,p)
    return result,winding


def relative_generators(N,p,Q,delta):
    d1=(delta[0]-delta[1])%p;d2=(delta[1]-delta[2])%p
    D=np.zeros((N*N,N*N),dtype=np.int64);Y=np.zeros_like(D);total=np.zeros_like(D)
    for a,b in product(range(N),repeat=2):
        source=a*N+b;k=(a+b)//N
        D[source,source]=(D[source,source]+pow(Q,a,p))%p
        target=((a+1)%N)*N+(b-1)%N
        coefficient=(d1 if a==N-1 else 1)*pow(d2,-int(b==0),p)%p
        D[target,source]=(D[target,source]+coefficient)%p
        Y[target,source]=(Y[target,source]-coefficient*pow(Q,b,p))%p
        for first in (True,False):
            aa,bb=((a+1)%N,b) if first else (a,(b+1)%N)
            wrap=int((a if first else b)==N-1)
            valuation=wrap+(aa+bb)//N-k
            assert valuation>=0
            if valuation:continue
            coefficient=((d1 if first else d2) if wrap else 1)
            if not first:coefficient=coefficient*pow(Q,a,p)%p
            total[aa*N+bb,source]=(total[aa*N+bb,source]+coefficient)%p
    return D,Y,total


def period_checks(N,p,generator,q,delta,matrices):
    if len(delta)!=4:return []
    Q=q*q%p;eye=np.eye(N,dtype=np.int64)
    directions=[(delta[j]-delta[j+1])*pow(N,-1,p)%p for j in range(3)]
    records=[]
    for kind,x in [('generic',generator),('Kashaev',pow(q,N-1,p))]:
        actual=color_matrices(N,p,q,x)
        pairs=[carry_crossings(N,p,q,x,directions[j+1]) for j in range(2)]
        local={(j,sign):np.kron(pairs[j][0 if sign>0 else 1],eye) if j==0
               else np.kron(eye,pairs[j][0 if sign>0 else 1])
               for j,sign in product(range(2),(1,-1))}
        pivot=np.diag(actual[2])
        states=list(product(range(N),repeat=3))
        cut=np.array([int(a==0)*int(pivot[b])*int(pivot[c])%p for a,b,c in states],dtype=np.int64)
        for word in WORDS:
            B=np.eye(N**3,dtype=np.int64)
            for j,sign in word:B=mm(p,B,local[j,sign])
            twist=pow(actual[3],-sum(sign for _,sign in word),p)
            target=reduced_period(N,p,*actual,word)
            closed=np.einsum('abcdbc,b,c->ad',B.reshape((N,)*6),pivot,pivot)%p
            assert np.array_equal(closed*twist%p,target*eye%p)
            for label,M in matrices.items():
                inverse=inverse_mod(M,p)
                transported=mm(p,inverse,cut[:,None]*B%p,M)
                assert int(np.trace(transported))*twist%p==target
            sectors={int(k):int(np.dot(cut*np.array([sum(s)//N==k for s in states]),np.diag(B)))*twist%p
                     for k in range(3*(N-1)//N+1)}
            records.append({'color':kind,'word':word,'actual_cut_value':target,
                            'whole_cut_operator_is_original_scalar':True,
                            'all_finite_and_infinite_source_tree_frames_preserve_period':True,
                            'carry_sector_contributions':sectors})
    return records


def case(N,b):
    p,generator,q,delta,C0,C1=chart(N,b);Q=q*q%p
    alltrees=trees(0,b)
    selected=alltrees if b<=5 else (alltrees[0],alltrees[-1])
    states=list(product(range(N),repeat=b));carry=np.array([sum(s)//N for s in states],dtype=np.int64)
    records=[];matrices={}
    for tree in selected:
        values={}
        for source,C in [('0',C0),('1',C1)]:
            M=finite_kernel(N,p,Q,C,tree)
            for u in (1,2):
                scaled=tuple(u*x%p for x in C)
                physical=actual_tree(N,p,Q,scaled,tree)
                epsilon=pow(u,N,p)
                expected=np.array([pow(epsilon,int(k),p) for k in carry],dtype=np.int64)[:,None]*physical%p
                assert np.array_equal(expected,M)
            values[source]=M;matrices[(str(tree),source)]=M
        Minf=infinity_kernel(N,p,Q,delta,tree)
        values['infinity']=Minf;matrices[(str(tree),'infinity')]=Minf
        mark_patterns=list(product(range(N),repeat=b)) if b==2 else sorted({(0,)*b,tuple(j%N for j in range(1,b+1)),tuple((-j)%N for j in range(1,b+1))})
        branch_records=[]
        for pattern in mark_patterns:
            marks=(0,*pattern)
            branch,winding=branch_infinity_kernel(N,p,Q,delta,tree,marks)
            if not any(marks):assert np.array_equal(branch,Minf)
            if b==2:
                D,Y,T=relative_generators(N,p,Q,delta)
                lam=(delta[0]-delta[2])*pow(delta[1]-delta[2],-1,p)%p
                Xr,Yr=endpoint_module(N,p,Q,lam,pow(Q,marks[1]-marks[2],p),pow(Q,marks[0]-marks[2],p))
                F=np.zeros((N,N),dtype=np.int64)
                for i in range(N-1):F[i+1,i]=1
                assert np.array_equal(mm(p,D,branch),mm(p,branch,np.kron(np.eye(N,dtype=np.int64),Xr)))
                assert np.array_equal(mm(p,Y,branch),mm(p,branch,np.kron(np.eye(N,dtype=np.int64),Yr)))
                assert np.array_equal(mm(p,T,branch),mm(p,branch,np.kron(F,np.eye(N,dtype=np.int64))))
            elif winding:
                matrices[(str(tree),'root_branch_'+str(pattern))]=branch
            branch_records.append({'relative_root_marks':list(marks),'retained_source_line_order':winding,
                                   'twisted_infinity_frame_is_invertible':True})
        if b==2:
            D,Y,T=relative_generators(N,p,Q,delta)
            lam=(delta[0]-delta[2])*pow(delta[1]-delta[2],-1,p)%p
            F=np.zeros((N,N),dtype=np.int64)
            for i in range(N-1):F[i+1,i]=1
            for source,M in values.items():
                C=None if source=='infinity' else (C0 if source=='0' else C1)
                a,beta=(1,1) if C is None else (C[1]*pow(C[2],-1,p)%p,C[0]*pow(C[2],-1,p)%p)
                Xr,Yr=endpoint_module(N,p,Q,lam,a,beta)
                assert np.array_equal(mm(p,D,M),mm(p,M,np.kron(np.eye(N,dtype=np.int64),Xr)))
                assert np.array_equal(mm(p,Y,M),mm(p,M,np.kron(np.eye(N,dtype=np.int64),Yr)))
                assert np.array_equal(mm(p,T,M),mm(p,M,np.kron(F,np.eye(N,dtype=np.int64))))
            # The total standard source is fixed: the infinity adapter
            # is identity on it, with its entire face scalar retained.
            normal_adapter=mm(p,inverse_mod(Minf,p),values['0'])
            face=np.einsum('iaib->ab',normal_adapter.reshape((N,)*4))*pow(N,-1,p)%p
            assert determinant(face,p)
            assert np.array_equal(normal_adapter,np.kron(np.eye(N,dtype=np.int64),face)%p)
        # Retain the actual source image, not only the basic carry fiber.
        A0=inverse_mod(values['0'],p)*(carry==0)[None,:]%p
        Ainf=inverse_mod(Minf,p)*(carry==0)[None,:]%p
        comparison=mm(p,inverse_mod(Minf,p),values['0'])
        assert np.array_equal(mm(p,comparison,A0),Ainf)
        records.append({'tree':str(tree),'all_three_source_frames_invertible':True,
                        'both_ramified_parameter_evaluations_match_actual_fusion':True,
                        'root_branches_at_source_infinity':branch_records,
                        'ordinary_source_image_rank':comb(N+b-1,b),
                        'retained_Tor_source_dimension':N**b-comb(N+b-1,b),
                        'source_image_naturality_through_infinity':True})
    periods=period_checks(N,p,generator,q,delta,matrices)
    return {'level':N,'leaves':b,'prime':p,'normal_flags':delta,'trees':records,
            'two_factor_full_relative_and_total_algebras_at_infinity':b==2,
            'actual_period_checks':periods}


def main():
    records=[]
    cases=[(2,b) for b in range(2,7)]+[(3,b) for b in range(2,5)]
    cases +=[(4,2),(4,3),(5,2),(5,3),(6,2),(6,3),(9,2)]
    for N,b in cases:
        records.append(case(N,b))
        print(f'N={N}, b={b}: {len(records[-1]["trees"])} source/carry frames through infinity passed',flush=True)
    result={'scope':'Actual pointed fusion in the endpoint frames, common full carry/source lattice through the auxiliary source infinity, and the original whole cut. Global geometric quantum-A/source identification and regulator norm remain unproved.',
            'configurations':records}
    Path(__file__).with_name('source_flag_carry_extension_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
