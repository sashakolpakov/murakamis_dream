#!/usr/bin/env python3
"""Genuine semicyclic holonomy braiding on the common carry lattice.

The uncheck wrap uses phi_2/K_1^N. Checked maps transport their
centers; freezing arbitrary directions is not a braid construction.
The common fixed center line supplies a genuine recoupled braid
action with the original cut period. No geometric norm is asserted.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np

from audit_actual_peripheral_fusion import inverse_mod, module
from audit_carry_recoupling_lattice import carry_crossings, row_matrix, trees
from audit_cyclic_steinberg_lattice import determinant
from audit_factorial_source_torsor import primitive
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_regular_holonomy_braiding import central, embed, holonomy, mm, transformed_centres


def swap(level):
    P=np.zeros((level*level,level*level),dtype=np.int64)
    for a,b in product(range(level),repeat=2):P[b*level+a,a*level+b]=1
    return P


def semicyclic(level,prime,q,x,phi):
    E,F,K=module(level,prime,q,x);F[0,level-1]=phi%prime
    return E,F,K


def positive(level,prime,q,x,u,v):
    return carry_crossings(level,prime,q,x,v*pow(level,-1,prime)%prime)[0]


def negative(level,prime,q,x,u,v):
    k=pow(x,level,prime)
    return carry_crossings(level,prime,q,x,u*pow(k*level,-1,prime)%prime)[1]


def transported(level,prime,q,x,u,v,sign):
    k=pow(x,level,prime);ki=pow(k,-1,prime)
    if sign>0:return (k*v%prime,(k*u+(1-k*k)*v)%prime)
    return (((1-ki*ki)*u+ki*v)%prime,ki*u%prime)


def intertwining_case(level,kind):
    prime,generator,q=field(level);x=generator if kind=='generic' else pow(q,level-1,prime)
    k=pow(x,level,prime);u,v=2,3
    sources=[semicyclic(level,prime,q,x,phi) for phi in (u,v)]
    ca,cb=[central(a,level,prime,q) for a in sources]
    ta,tb,D=transformed_centres(ca,cb,level,prime,q);assert D==1
    targets=[semicyclic(level,prime,q,x,t[2]) for t in (ta,tb)]
    A,B=embed(sources,0),embed(sources,1);Ap,Bp=holonomy(A,B,prime,q)
    corrected=mm(prime,swap(level),positive(level,prime,q,x,0,v*pow(k,-1,prime)%prime))
    target_matrices=embed(targets,0)+embed(targets,1)
    assert all(np.array_equal(mm(prime,old,corrected),mm(prime,corrected,new))
               for old,new in zip(Ap+Bp,target_matrices))
    anchor=np.zeros(level*level,dtype=np.int64);anchor[0]=1
    assert np.array_equal(corrected@anchor%prime,anchor) and determinant(corrected,prime)
    uncorrected=mm(prime,swap(level),positive(level,prime,q,x,u,v))
    assert np.array_equal(uncorrected,corrected)==(k==1)
    return {'level':level,'color':kind,'prime':prime,'retained_k':k,
            'all_six_holonomy_intertwinings_exact':True,'highest_weight_pointing_fixed':True,
            'omitting_wrap_norm_factor_fails':k!=1,'uncheck_wrap_factor':pow(k,-1,prime)}


def word_operator(level,prime,q,x,initial,word):
    centers=list(initial);I=np.eye(level,dtype=np.int64);B=np.eye(level**3,dtype=np.int64)
    for j,sign in word:
        u,v=centers[j:j+2]
        local=(positive if sign>0 else negative)(level,prime,q,x,u,v)
        centers[j:j+2]=transported(level,prime,q,x,u,v,sign)
        B=mm(prime,np.kron(local,I) if j==0 else np.kron(I,local),B)
    return centers,B


def braid_case(level,kind):
    prime,generator,q=field(level);x=generator if kind=='generic' else pow(q,level-1,prime)
    initial=[2,3,5]
    a,A=word_operator(level,prime,q,x,initial,[(0,1),(1,1),(0,1)])
    b,B=word_operator(level,prime,q,x,initial,[(1,1),(0,1),(1,1)])
    assert a==b and np.array_equal(A,B)
    for j in (0,1):
        final,value=word_operator(level,prime,q,x,initial,[(j,1),(j,-1)])
        assert final==initial and np.array_equal(value,np.eye(level**3,dtype=np.int64))
    # Fixing arbitrary parameters instead of updating them need not work.
    I=np.eye(level,dtype=np.int64);frozen=[]
    for word in ([0,1,0],[1,0,1]):
        value=np.eye(level**3,dtype=np.int64)
        for j in word:
            local=positive(level,prime,q,x,initial[j],initial[j+1])
            value=mm(prime,np.kron(local,I) if j==0 else np.kron(I,local),value)
        frozen.append(value)
    return {'level':level,'color':kind,'transported_three_factor_braid_exact':True,
            'positive_negative_centers_and_operators_inverse':True,
            'frozen_arbitrary_parameters_fail':not np.array_equal(*frozen)}


def fixed_line_case(level,kind):
    prime,generator,q=field(level);Q=q*q%prime
    x=generator if kind=='generic' else pow(q,level-1,prime);k=pow(x,level,prime)
    # alpha=1-epsilon gives phi_j=N epsilon k^(1-j)+O(epsilon^2).
    centers=[level*pow(k,-j,prime)%prime for j in range(3)]
    for j in (0,1):
        for sign in (1,-1):
            assert tuple(centers[j:j+2])==transported(level,prime,q,x,*centers[j:j+2],sign)
    a,A=word_operator(level,prime,q,x,centers,[(0,1),(1,1),(0,1)])
    b,B=word_operator(level,prime,q,x,centers,[(1,1),(0,1),(1,1)])
    assert a==b==centers and np.array_equal(A,B)
    states=list(product(range(level),repeat=3));size=len(states)
    S=np.array([pow(x,sum(j*a[j] for j in range(3)),prime) for a in states],dtype=np.int64)
    Si=np.array([pow(int(s),-1,prime) for s in S],dtype=np.int64)
    factorial=primitive(level,Q,1,prime)
    factorial_gauge=np.array([int(factorial[a[0]])*int(factorial[a[1]])*int(factorial[a[2]])%prime for a in states],dtype=np.int64)
    I=np.eye(level,dtype=np.int64);local={}
    for j in (0,1):
        for sign in (1,-1):
            P=(positive if sign>0 else negative)(level,prime,q,x,*centers[j:j+2])
            P=np.kron(P,I) if j==0 else np.kron(I,P)
            local[j,sign]=Si[:,None]*P*S[None,:]%prime
    actual=color_matrices(level,prime,q,x);pivot=np.diag(actual[2])
    cut=np.array([int(a[0]==0)*int(pivot[a[1]])*int(pivot[a[2]])%prime for a in states],dtype=np.int64)
    periods=0
    for tree in trees(0,3):
        M,_,_,_=row_matrix(level,prime,Q,[1,1,1],tree)
        M=M*np.array([pow(int(f),-1,prime) for f in factorial_gauge])[:,None]%prime
        inv=inverse_mod(M,prime)
        rec={key:mm(prime,inv,R,M) for key,R in local.items()}
        left=mm(prime,rec[0,1],rec[1,1],rec[0,1]);right=mm(prime,rec[1,1],rec[0,1],rec[1,1])
        assert np.array_equal(left,right)
        cut_rec=mm(prime,inv,np.diag(cut),M)
        for word in WORDS:
            R=np.eye(size,dtype=np.int64)
            for j,sign in word:R=mm(prime,R,rec[j,sign])
            value=int(np.trace(mm(prime,cut_rec,R)))%prime
            value=value*pow(actual[3],-sum(sign for _,sign in word),prime)%prime
            assert value==reduced_period(level,prime,*actual,word)
            periods+=1
    return {'level':level,'color':kind,'fixed_center_line':centers,
            'endpoint_scaled_center_directions_all_equal':True,
            'genuine_braid_on_both_recoupled_carry_fibers':True,
            'original_cut_pivot_and_writhe_periods':periods}


def full_cut_case(level,kind):
    prime,generator,q=field(level);x=generator if kind=='generic' else pow(q,level-1,prime)
    actual=color_matrices(level,prime,q,x);I=np.eye(level,dtype=np.int64)
    pivot=np.kron(I,np.kron(actual[2],actual[2]))%prime;checks=0
    for word in WORDS:
        _,B=word_operator(level,prime,q,x,[2,3,5],list(reversed(word)))
        closed=mm(prime,B,pivot).reshape((level,)*6)
        cut=np.einsum('abcdbc->ad',closed)%prime
        cut=cut*pow(actual[3],-sum(sign for _,sign in word),prime)%prime
        target=reduced_period(level,prime,*actual,word)
        assert np.array_equal(cut,target*I%prime);checks+=1
    return {'level':level,'color':kind,'entire_cut_matrices_checked':checks,
            'arbitrary_transported_semicyclic_centers_give_original_scalar_cut':True}


def main():
    levels=(2,3,4,5,6,8,9,10,12)
    pairs=[intertwining_case(n,k) for n in levels for k in ('generic','Kashaev')]
    print(f'all-six-generator semicyclic intertwinings: {len(pairs)} passed',flush=True)
    braids=[braid_case(n,k) for n in (2,3,4,5,6) for k in ('generic','Kashaev')]
    print(f'transported braid relations and inverse maps: {len(braids)} passed',flush=True)
    fixed=[fixed_line_case(n,k) for n in (2,3,4,5,6) for k in ('generic','Kashaev')]
    cuts=[full_cut_case(n,k) for n in (2,3,4,5,6) for k in ('generic','Kashaev')]
    result={'scope':'Global pointed semicyclic holonomy braiding and its genuine carry-lattice braid action; original ADO cut period retained; no geometric Bloch-regulator norm theorem.',
            'semicyclic_intertwiners':pairs,'transported_braids':braids,
            'fixed_line_carry_braids_and_periods':fixed,'full_scalar_cut_matrices':cuts}
    Path(__file__).with_name('semicyclic_carry_braiding_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {sum(r["original_cut_pivot_and_writhe_periods"] for r in fixed)} original recoupled periods',flush=True)


if __name__=='__main__':main()
