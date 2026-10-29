#!/usr/bin/env python3
"""Pointed algebraic pentagons and the actual compressed Verma period.

Individual compact products are never evaluated at roots. Their combined
Fock coefficients are canceled first and independently compared with
the actual finite crossings and the full root Verma trace.
"""

from functools import cache
from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod
from audit_finite_sum_annihilator import field
from audit_frobenius_verma_period import (
    coefficient, compositions, finite_polynomial, classical_matrix,
)
from audit_kashaev_ado_pointing import WORDS, color_matrices

Q=sp.Symbol('Q',nonzero=True)
kappa=sp.Symbol('kappa')


@cache
def euler(n):
    return (-1)**n*Q**(n*(n-1)//2)/sp.prod(1-Q**j for j in range(1,n+1))


def qt_multiply(left,right,cap,triangle=False):
    result={}
    for (a,b),u in left.items():
        for (c,d),v in right.items():
            if a+c>cap or (triangle and a+b+c+d>cap):continue
            key=(a+c,b+d)
            result[key]=result.get(key,0)+u*v*Q**(-b*c)
    return {key:sp.cancel(value) for key,value in result.items() if value!=0}


def compact(a,b,scalar,cap,triangle=False):
    maximum=cap//(a+b) if triangle else cap//a
    return {(a*n,b*n):euler(n)*scalar**n*Q**(-a*b*n*(n-1)//2) for n in range(maximum+1)}


def compact_pentagon(cap=6):
    PX=compact(1,0,1,cap,True);PY=compact(0,1,1,cap,True)
    middle=compact(1,1,-1/Q,cap,True) # -YX in ordered X,Y coordinates
    left=qt_multiply(PY,PX,cap,True)
    right=qt_multiply(qt_multiply(PX,middle,cap,True),PY,cap,True)
    keys=set(left)|set(right)
    assert all(sp.cancel(left.get(key,0)-right.get(key,0))==0 for key in keys)
    return {'total_degree':cap,'ordered_coefficients':len(keys),'scalar_one_pentagon_exact':True}


def tetra_step(states,i,j,weight,degree,Q0,prime,eta=None):
    eta=-Q0%prime if eta is None else eta%prime
    result={}
    for (p,q,n),value in states.items():
        for m in range(degree+1):
            pp,qq=p+weight[0]*m,q+weight[1]*m
            if pp+qq>degree:break
            denominator=1
            for r in range(1,m+1):denominator=denominator*(1-pow(Q0,r,prime))%prime
            factor=pow(eta,m,prime)*pow(Q0,-m*n[j]+m*(m-1)//2,prime)*pow(denominator,-1,prime)%prime
            target=list(n);target[i]+=m;target[j]+=n[i]
            key=(pp,qq,tuple(target))
            result[key]=(result.get(key,0)+value*factor)%prime
    return {key:value for key,value in result.items() if value}


def tetra_case(prime,degree):
    Q0=int(sp.primitive_root(prime))
    total=0;wrong_phase_detected=False
    for initial in product((-1,0,2),repeat=3):
        state={(0,0,initial):1}
        left=tetra_step(tetra_step(tetra_step(state,1,2,(0,1),degree,Q0,prime),
                                  0,2,(1,1),degree,Q0,prime),0,1,(1,0),degree,Q0,prime)
        right=tetra_step(tetra_step(state,0,1,(1,0),degree,Q0,prime),
                        1,2,(0,1),degree,Q0,prime)
        assert left==right
        wrong=tetra_step(tetra_step(tetra_step(state,1,2,(0,1),degree,Q0,prime,eta=-1),
                                   0,2,(1,1),degree,Q0,prime,eta=-1),
                         0,1,(1,0),degree,Q0,prime,eta=-1)
        wrong_right=tetra_step(tetra_step(state,0,1,(1,0),degree,Q0,prime,eta=-1),
                              1,2,(0,1),degree,Q0,prime,eta=-1)
        wrong_phase_detected |= wrong!=wrong_right
        total+=len(set(left)|set(right))
    assert wrong_phase_detected
    return {'prime':prime,'tag_degree':degree,'Laurent_input_vectors':27,
            'coefficient_comparisons':total,'tetrahedral_pentagon_scalar_one_exact':True,
            'omitting_Q_phase_fails':True}


@cache
def symbolic_gaussian(a,n):
    if n<0 or n>a:return sp.Integer(0)
    if n==0 or n==a:return sp.Integer(1)
    return sp.expand(symbolic_gaussian(a-1,n)+Q**(a-n)*symbolic_gaussian(a-1,n-1))


def compressed_crossing(cap=6):
    # A S=Q S A. Each argument has A-degree one.
    arguments=[(1,-1,-Q),(1,0,kappa),(1,0,Q),(1,1,-kappa)]
    series={(0,0):sp.Integer(1)}
    for a,b,scalar in arguments:series=qt_multiply(series,compact(a,b,scalar,cap),cap)
    expressions={};checks=0;annihilated=0
    for a in range(cap+1):
        for n in range(cap+1):
            value=sp.cancel(sum(c*Q**(a*s) for (r,s),c in series.items() if r==n))
            expected=(Q**(-n*(a-n))*symbolic_gaussian(a,n)
                      *sp.prod(1-kappa*Q**(a-n+j) for j in range(n)))
            assert sp.cancel(value-expected)==0,(a,n)
            denominator=sp.denom(value)
            terms=sp.Poly(denominator,Q,kappa).terms()
            assert len(terms)==1 and terms[0][0][1]==0
            if n>a:assert value==0;annihilated+=1
            expressions[a,n]=value
            checks+=1
    return expressions,{'maximum_input_and_transfer':cap,'symbolic_compressions':checks,
                        'forbidden_Fock_transfers_canceled':annihilated,
                        'all_root_poles_canceled_before_specialization':True}


def evaluate_rational(value,Q0,kappa0,prime):
    num,den=sp.fraction(value)
    a=int(num.subs({Q:Q0,kappa:kappa0}))%prime
    b=int(den.subs({Q:Q0,kappa:kappa0}))%prime
    return a*pow(b,-1,prime)%prime


def root_context(expressions,Q0,x,prime,cap):
    theta={(a,n):pow(x,n,prime)*evaluate_rational(value,Q0,pow(x,-2,prime),prime)%prime
           for (a,n),value in expressions.items()}
    sectors={}
    for degree in range(cap+1):
        matrix=np.zeros((degree+1,degree+1),dtype=np.int64)
        for a in range(degree+1):
            b=degree-a
            for n in range(a+1):
                out=(b+n,a-n)
                diagonal=pow(x,-a-b,prime)*pow(Q0,(a-n)*(b+n),prime)%prime
                matrix[out[0],a]=theta[a,n]*diagonal%prime
        sectors[degree]=(matrix,inverse_mod(matrix,prime))
    return theta,sectors


def root_crossing_case(level,expressions,cap):
    prime,generator,q=field(level);Q0=q*q%prime
    checks=0
    for x in (generator,pow(q,level-1,prime)):
        theta,sectors=root_context(expressions,Q0,x,prime,cap)
        for a,b in product(range(cap+1),repeat=2):
            for n in range(a+1):
                value=theta[a,n]*pow(x,-a-b,prime)*pow(Q0,(a-n)*(b+n),prime)%prime
                assert value==coefficient(a,b,n,1,Q0,x,prime)
                checks+=1
        for degree,pair in sectors.items():
            for a in range(degree+1):
                b=degree-a
                for out_a in range(degree+1):
                    n=b-out_a
                    assert int(pair[1][out_a,a])==coefficient(a,b,n,-1,Q0,x,prime)
                    checks+=1
        if level-1<=cap:
            actual=color_matrices(level,prime,q,x)
            for sign in (1,-1):
                reconstructed=np.zeros((level*level,level*level),dtype=np.int64)
                for a,b in product(range(level),repeat=2):
                    if sign>0:
                        for n in range(min(a,level-1-b)+1):
                            value=theta[a,n]*pow(x,-a-b,prime)*pow(Q0,(a-n)*(b+n),prime)%prime
                            reconstructed[(b+n)*level+a-n,a*level+b]=value
                    elif a+b<=cap:
                        for n in range(min(b,level-1-a)+1):
                            reconstructed[(b-n)*level+a+n,a*level+b]=sectors[a+b][1][b-n,a]
                if sign>0:assert np.array_equal(reconstructed,actual[0])
                else:
                    for a,b in product(range(level),repeat=2):
                        if a+b<=cap:assert np.array_equal(reconstructed[:,a*level+b],actual[1][:,a*level+b])
    return {'level':level,'compressed_root_entries_checked':checks,
            'generic_and_Kashaev_colors_exact':True,'finite_ADO_positive_and_inverse_restrictions_exact':True}


def lattice_case(level):
    prime,generator,q=field(level);Q0=q*q%prime;x=generator
    U=pow(x,2*level,prime)
    hs=[1]
    for a in range(1,4*level):hs.append(hs[-1]*pow(1-pow(x,-2,prime)*pow(Q0,a-1,prime),-1,prime)%prime)
    for A,r in product(range(4),range(level)):
        assert hs[level*A+r]==pow(1-pow(U,-1,prime),-A,prime)*hs[r]%prime
    # The ordered monomial -YX has Nth power -X^N Y^N, at every parity.
    scalar=pow(-1,level,prime)*pow(Q0,-level*(level-1)//2,prime)%prime
    assert scalar==prime-1
    x0=pow(q,level-1,prime)
    factors=[(1-pow(x0,-2,prime)*pow(Q0,j,prime))%prime for j in range(level)]
    assert all(factors[:-1]) and factors[-1]==0
    return {'level':level,'Pochhammer_block_lattice_exact':True,'finite_Kashaev_frame_units':level,
            'first_untruncated_frame_pole_retained':True,'middle_monomial_root_sign_exact':True}


def trace_case(level,word,kind,expressions,cap):
    prime,generator,q=field(level);Q0=q*q%prime
    x=pow(q,level-1,prime) if kind=='ideal' else generator
    _,sectors=root_context(expressions,Q0,x,prime,cap)
    def local(a,b,sign):
        matrix=sectors[a+b][0 if sign>0 else 1]
        return [((out,a+b-out),int(matrix[out,a])) for out in range(a+b+1) if matrix[out,a]]
    def diagonal(initial):
        states={initial:1}
        for j,sign in reversed(word):
            after={}
            for state,value in states.items():
                for pair,factor in local(state[j],state[j+1],sign):
                    target=state[:j]+pair+state[j+2:]
                    after[target]=(after.get(target,0)+value*factor)%prime
            states={key:value for key,value in after.items() if value}
        return states.get(initial,0)
    b=3;c=b-1-sum(s for _,s in word)
    polynomial=finite_polynomial(level,b,word,prime,q,x)
    L=classical_matrix(b,word,pow(x,level,prime),False,prime)[1:,1:]
    ds=[1,-int(np.trace(L))%prime,int(L[0,0]*L[1,1]-L[0,1]*L[1,0])%prime]
    hs=[1]
    for n in range(1,cap//level+1):hs.append(-sum(ds[j]*hs[n-j] for j in range(1,min(n,2)+1))%prime)
    for d in range(cap+1):
        value=sum(diagonal((0,)+a) for a in compositions(d,b-1))*pow(x,c,prime)*pow(Q0,-d,prime)%prime
        expected=sum(polynomial[r]*hs[(d-r)//level] for r in range(min(d,len(polynomial)-1)+1) if (d-r)%level==0)%prime
        assert value==expected
    return {'level':level,'word':word,'color':kind,'graded_coefficients':cap+1,
            'four_factor_trace_equals_actual_ADO_Burau_period':True}


def main():
    pentagon=compact_pentagon()
    print('compact formal pentagon: passed',flush=True)
    tetra=[tetra_case(p,4) for p in (101,1009,1013)]
    print('tagged tetrahedral operators: passed',flush=True)
    cap=6
    expressions,compression=compressed_crossing(cap)
    print(f'four-factor symbolic Fock compressions: {compression["symbolic_compressions"]} passed',flush=True)
    roots=[root_crossing_case(n,expressions,cap) for n in (2,3,4,5,6)]
    lattice=[lattice_case(n) for n in (2,3,4,5,6,8,9,10,12)]
    print('root compression and full pole lattices: passed',flush=True)
    traces=[trace_case(n,list(word),kind,expressions,cap) for n in (2,3,4,5,6)
            for word in WORDS for kind in ('generic','ideal')]
    result={'scope':'Formal tetrahedral/pentagon transport of the actual compressed root period; no arbitrary triangulation or regulator-norm comparison.',
            'compact_pentagon':pentagon,'tagged_tetrahedral_pentagons':tetra,
            'four_factor_compression':compression,'root_crossings':roots,
            'relative_pole_lattices':lattice,'transported_traces':traces}
    Path(__file__).with_name('verma_tetrahedral_transport_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(traces)} transported trace cases',flush=True)


if __name__=='__main__':main()
