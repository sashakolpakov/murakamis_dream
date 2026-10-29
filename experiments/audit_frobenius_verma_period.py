#!/usr/bin/env python3
"""Exact Frobenius block trace of the untruncated Verma braid period.

The full crossing is evaluated using Gaussian polynomials, without
discarding indices >=N. Root block decomposition, both signs, residue
filtration, Alexander normalization, and graded trace identities are
checked independently against the actual finite ADO matrices.
"""

from functools import cache
from itertools import product
import json
from math import comb
from pathlib import Path
from random import Random

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import module
from audit_closed_braid_period_line import burau, permutation_is_knot, t as burau_t, cut_operator
from audit_finite_sum_annihilator import field, cut_matrix_dense
from audit_kashaev_ado_pointing import WORDS, color_matrices
from audit_regular_holonomy_braiding import mm


@cache
def gaussian(a,n,Q,prime):
    if n<0 or n>a:return 0
    if not n or n==a:return 1
    return (gaussian(a-1,n,Q,prime)+pow(Q,a-n,prime)*gaussian(a-1,n-1,Q,prime))%prime


@cache
def pochhammer(start,length,Q,prime):
    result=1
    for j in range(length):result=result*(1-start*pow(Q,j,prime))%prime
    return result


@cache
def coefficient(a,b,n,sign,Q,x,prime):
    if sign>0:
        if not 0<=n<=a:return 0
        return (pow(x,-a-b+n,prime)*pow(Q,(a-n)*b,prime)*gaussian(a,n,Q,prime)
                *pochhammer(pow(x,-2,prime)*pow(Q,a-n,prime)%prime,n,Q,prime))%prime
    if not 0<=n<=b:return 0
    return (pow(x,a+b-n,prime)*pow(Q,-a*b,prime)*gaussian(b,n,Q,prime)
            *pochhammer(x*x%prime*pow(Q,1-b,prime)%prime,n,Q,prime))%prime


@cache
def transitions(a,b,sign,Q,x,prime):
    answer=[]
    for n in range((a if sign>0 else b)+1):
        value=coefficient(a,b,n,sign,Q,x,prime)
        if value:answer.append(((b+n,a-n) if sign>0 else (b-n,a+n),value))
    return answer


def local_case(level):
    prime,generator,q=field(level);Q=q*q%prime;x=generator;k=pow(x,level,prime)
    total=carry=vanishing=0
    for r,s,t in product(range(level),repeat=3):
        for C in (0,1,2):
            for sign in (1,-1):
                A,B=(2,1) if sign>0 else (1,2)
                a,b,n=level*A+r,level*B+s,level*C+t
                full=coefficient(a,b,n,sign,Q,x,prime)
                residual=coefficient(r,s,t,sign,Q,x,prime)
                coarse=(comb(A,C)*pow(k,-A-B+C,prime)*pow(1-pow(k,-2,prime),C,prime)
                        if sign>0 else
                        comb(B,C)*pow(k,A+B-C,prime)*pow(1-k*k,C,prime))%prime
                assert full==residual*coarse%prime
                if full:
                    out=(b+n,a-n) if sign>0 else (b-n,a+n)
                    drop=r+s-sum(v%level for v in out)
                    assert drop in (0,level)
                    carry+=drop==level
                else:vanishing+=1
                total+=1
    actual=color_matrices(level,prime,q,x)
    for sign,finite in ((1,actual[0]),(-1,actual[1])):
        reconstructed=np.zeros_like(finite)
        for a,b in product(range(level),repeat=2):
            for out,value in transitions(a,b,sign,Q,x,prime):
                if max(out)<level:reconstructed[out[0]*level+out[1],a*level+b]=value
        assert np.array_equal(reconstructed,finite)
    # Inverse identities on full homogeneous Verma sectors, including blocks >=N.
    for degree in range(2*level+2):
        pair=[]
        for sign in (1,-1):
            matrix=np.zeros((degree+1,degree+1),dtype=np.int64)
            for a in range(degree+1):
                for out,value in transitions(a,degree-a,sign,Q,x,prime):matrix[out[0],a]=value
            pair.append(matrix)
        assert np.array_equal(mm(prime,*pair),np.eye(degree+1,dtype=np.int64))
    return {'level':level,'coefficient_comparisons':total,'nonzero_carry_terms':carry,
            'zero_coefficients':vanishing,'all_block_factorizations_exact':True,
            'full_Verma_inverse_sectors':2*level+2,'actual_finite_crossings_exact':True}


def classical_matrix(strands,word,k,symbolic=True,prime=None):
    result=sp.eye(strands) if symbolic else np.eye(strands,dtype=np.int64)
    for j,sign in word:
        if symbolic:
            step=sp.eye(strands)
            step[j:j+2,j:j+2]=(sp.Matrix([[1-k**-2,k**-1],[k**-1,0]]) if sign>0
                               else sp.Matrix([[0,k],[k,1-k*k]]))
            result=result*step
        else:
            step=np.eye(strands,dtype=np.int64)
            step[j:j+2,j:j+2]=(np.array([[1-pow(k,-2,prime),pow(k,-1,prime)],[pow(k,-1,prime),0]]) if sign>0
                               else np.array([[0,k],[k,1-k*k]]))
            result=mm(prime,result,step%prime)
    return result.applyfunc(sp.expand) if symbolic else result


def classical_cases():
    k=sp.Symbol('k',nonzero=True)
    rng=Random(271814)
    words=[(3,list(w)) for w in WORDS]+[(2,[(0,1)]*3),(2,[(0,-1)]*3)]
    while len(words)<16:
        b=rng.randrange(2,5)
        w=[(rng.randrange(b-1),rng.choice((-1,1))) for _ in range(rng.randrange(3,10))]
        if permutation_is_knot(b,w):words.append((b,w))
    records=[]
    for b,word in words:
        L=classical_matrix(b,word,k)
        D=sp.expand((sp.eye(b)-L)[1:,1:].det())
        c=b-1-sum(sign for _,sign in word)
        Delta=sp.expand(k**(-c)*D)
        assert c%2==0 and sp.cancel(Delta.subs(k,-k)-Delta)==0
        assert sp.cancel(Delta.subs(k,1/k)-Delta)==0
        assert Delta.subs(k,1)==1 and Delta.subs(k,-1)==1
        B=burau(b,word).subs(burau_t,k*k)
        assert sp.cancel(D-(sp.eye(b)-B)[1:,1:].det())==0
        H=sp.eye(b)
        for i in range(b):
            for j in range(i+1,b):H[i,j]=(1-k*k)*k**(i-j)
        assert (L.subs(k,1/k).T*H*L-H).applyfunc(sp.cancel)==sp.zeros(b)
        if b<=3:
            for sign in (1,-1):
                stabilized=word+[(b-1,sign)]
                bigger=classical_matrix(b+1,stabilized,k)
                cc=b-sum(s for _,s in stabilized)
                other=sp.expand(k**(-cc)*(sp.eye(b+1)-bigger)[1:,1:].det())
                assert sp.cancel(other-Delta)==0
            gamma=[(0,1),(b-2,-1)]
            inverse=[(j,-s) for j,s in reversed(gamma)]
            conjugate=classical_matrix(b,gamma+word+inverse,k)
            assert sp.cancel((sp.eye(b)-conjugate)[1:,1:].det()-D)==0
        records.append({'strands':b,'word':word,'normalized_Alexander':str(Delta),
                        'duality_reciprocity_and_Fox_minor_exact':True,
                        'Markov_and_conjugation_checked':b<=3})
    return records


def compositions(total,length):
    if length==1:
        yield (total,);return
    for a in range(total+1):
        for rest in compositions(total-a,length-1):yield (a,)+rest


def verma_diagonal(initial,word,Q,x,prime):
    states={initial:1}
    for j,sign in reversed(word):
        after={}
        for state,weight in states.items():
            for pair,value in transitions(state[j],state[j+1],sign,Q,x,prime):
                target=state[:j]+pair+state[j+2:]
                after[target]=(after.get(target,0)+weight*value)%prime
        states={s:v for s,v in after.items() if v}
    return states.get(initial,0)


def finite_polynomial(level,strands,word,prime,q,x):
    positive,negative,_,_=color_matrices(level,prime,q,x)
    result=np.eye(level**strands,dtype=np.int64)
    for j,sign in word:
        full=np.kron(np.kron(np.eye(level**j,dtype=np.int64),positive if sign>0 else negative),
                     np.eye(level**(strands-j-2),dtype=np.int64))
        result=mm(prime,result,full)
    Q=q*q%prime;c=strands-1-sum(s for _,s in word)
    polynomial=[0]*((strands-1)*(level-1)+1)
    for r in product(range(level),repeat=strands-1):
        index=sum(a*level**(strands-2-j) for j,a in enumerate(r))
        d=sum(r)
        polynomial[d]=(polynomial[d]+int(result[index,index])*pow(x,c,prime)*pow(Q,-d,prime))%prime
    return polynomial


def trace_case(level,strands,word,kind):
    prime,generator,q=field(level);Q=q*q%prime
    x=pow(q,level-1,prime) if kind=='ideal' else generator
    k=pow(x,level,prime);c=strands-1-sum(s for _,s in word)
    polynomial=finite_polynomial(level,strands,word,prime,q,x)
    L=classical_matrix(strands,word,k,False,prime)
    A=sp.Matrix(L[1:,1:].tolist());z=sp.Symbol('z')
    denominator=sp.Poly((sp.eye(strands-1)-z*A).det(),z)
    ds=[int(denominator.nth(j))%prime for j in range(strands)]
    maximum=len(polynomial)-1+2*level
    h=[1]
    for n in range(1,maximum//level+1):
        h.append(-sum(ds[j]*h[n-j] for j in range(1,min(n,strands-1)+1))%prime)
    for degree in range(maximum+1):
        direct=sum(verma_diagonal((0,)+a,word,Q,x,prime) for a in compositions(degree,strands-1))%prime
        direct=direct*pow(x,c,prime)*pow(Q,-degree,prime)%prime
        predicted=sum(polynomial[r]*h[(degree-r)//level] for r in range(min(degree,len(polynomial)-1)+1)
                      if (degree-r)%level==0)%prime
        assert direct==predicted,(level,strands,kind,word,degree,direct,predicted)
    D=sum(ds)%prime
    Delta=pow(k,-c,prime)*D%prime
    data=color_matrices(level,prime,q,x)
    if strands<=3:
        actual=cut_matrix_dense(level,prime,data,strands,word)
    else:
        V=module(level,prime,q,x)
        actual=cut_operator([V]*strands,[data[0]]*(strands-1),word,level,prime)
        actual=actual*pow(data[3],-sum(s for _,s in word),prime)%prime
    assert sum(polynomial)%prime==pow(k,c,prime)*int(actual[0,0])%prime
    if kind=='ideal':assert Delta==1 and D==1 and pow(k,c,prime)==1
    return {'level':level,'strands':strands,'word':word,'color':kind,
            'graded_coefficients_checked':maximum+1,'root_trace_factorization_exact':True,
            'retained_block_denominator':ds,'normalized_Alexander_value':Delta,
            'finite_ADO_normalization_power':c,'finite_ADO_numerator_exact':True,
            'polar_block_specialization':D==0,'polar_numerator_nonzero':D==0 and sum(polynomial)%prime!=0,
            'ideal_point_comparison_exact':kind=='ideal'}


def main():
    local=[local_case(n) for n in (2,3,4,5,6,8,9,10,12)]
    print(f'full root crossing block factorizations: {sum(r["coefficient_comparisons"] for r in local)} passed',flush=True)
    classical=classical_cases()
    print(f'Alexander, duality and braid normalizations: {len(classical)} passed',flush=True)
    cases=[(n,3,list(w),kind) for n in (2,3,4,5) for w in WORDS for kind in ('generic','ideal')]
    cases += [(n,2,[(0,s)]*3,kind) for n in (6,8) for s in (1,-1) for kind in ('generic','ideal')]
    cases += [(3,4,[(0,1)]*3+[(1,1),(2,-1)],kind) for kind in ('generic','ideal')]
    traces=[]
    for args in cases:
        traces.append(trace_case(*args))
        if len(traces)%8==0:print(f'graded Verma traces: {len(traces)} passed',flush=True)
    result={'scope':'Exact graded Verma/root ADO-Alexander factorization; no generic completion comparison or volume theorem.',
            'local_block_factorizations':local,'classical_Alexander':classical,'graded_trace_cases':traces}
    Path(__file__).with_name('frobenius_verma_period_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(traces)} full graded trace cases',flush=True)


if __name__=='__main__':main()
