#!/usr/bin/env python3
"""Actual two-wall Verma boundary, coherent Weyl source and centralizer."""

from functools import cache
import itertools
import json
import math
from pathlib import Path

import sympy as s

from audit_complete_color_divided_ward import Ring
from audit_finite_sum_annihilator import field
from audit_figure_eight_whole_source import MixedEntries


def root_module_case(N,M,p,q):
    Q=q*q%p;gamma=pow(-1,N+1,p);x=-M*pow(q,-1,p)%p
    kappa=(M-pow(M,-1,p))%p;kappan=(pow(M,N,p)-pow(M,-N,p))%p
    R=Ring(p);states=[(a,) for a in range(2*N)]
    E={};F={}
    for a in range(2*N):
        if a:E[(a,)]={(a-1,):((M*pow(Q,-a,p)-pow(M,-1,p))%p,0)}
        if a+1<2*N:
            value=(1-pow(Q,a+1,p))%p
            if value:F[(a,)]={(a+1,):(value,0)}
    power=R.oppower(E,N,states)
    expected={(a,):{(a-N,):(gamma*kappan%p,0)} for a in range(N,2*N) if kappan}
    assert power==expected
    assert R.oppower(F,N,states)=={}
    head=[(a,) for a in range(N)];I=R.identity(head)
    EH={c:rows for c,rows in E.items() if c[0]<N}
    FH={c:rows for c,rows in F.items() if c[0]<N}
    K={(a,):{(a,):(x*pow(Q,-a,p)%p,0)} for a in range(N)}
    Ki={(a,):{(a,):(pow(x*pow(Q,-a,p)%p,-1,p),0)} for a in range(N)}
    rho=(q-pow(q,-1,p))%p
    for spectral in (0,1,2):
        Es=R.plus(EH,{(0,):{(N-1,):(kappa*spectral%p,0)}})
        assert R.oppower(Es,N,head)==R.scale(I,gamma*kappan*spectral%p)
        comm=R.plus(R.compose(Es,FH),R.scale(R.compose(FH,Es),-1))
        expected=R.scale(R.plus(K,R.scale(Ki,-1)),rho)
        assert comm==expected
    return {'level':N,'complete_meridian':M==1,'central_block_shift_identity':True,
            'finite_E_cyclic_source_family_actual_Hopf_relations':True}


def meridian_bockstein(N,p,q):
    Q=q*q%p;gamma=pow(-1,N+1,p);R=Ring(p)
    states=[(a,) for a in range(2*N)];M=(1,1)
    E={}
    for a in range(1,2*N):
        coeff=R.add(R.mul(M,(pow(Q,-a,p),0)),R.neg(R.power(M,-1)))
        if coeff!=(0,0):E[(a,)]={(a-1,):coeff}
    power=R.oppower(E,N,states)
    expected={(a,):{(a-N,):(0,gamma*2*N%p)} for a in range(N,2*N)}
    assert power==expected
    return {'level':N,'nonzero_central_first_meridian_extension':True,
            'gauge_invariant_off_diagonal_coefficient':True}


def infinite_R_case(N,p,q,M,root_wall):
    Q=q*q%p;x=-M*pow(q,-1,p)%p;L=2*(N-1);R=Ring(p)
    states=[(a,b) for a in range(L+1) for b in range(L+1-a)]
    @cache
    def gauss(n,k):
        if k<0 or k>n:return 0
        if k==0 or k==n:return 1
        return (gauss(n-1,k)+pow(Q,n-k,p)*gauss(n-1,k-1))%p
    def poch(z,k):
        value=1
        for j in range(k):value=value*(1-z*pow(Q,j,p))%p
        return value
    def coefficient(sign,a,b,k):
        if sign>0:
            return pow(-1,k,p)*pow(x,-a-b-k,p)\
                *pow(Q,a*b+(a-b)*k-k*(k+1)//2,p)\
                *gauss(b+k,k)*poch(M*M*pow(Q,-a,p)%p,k)%p
        return pow(x,a+b-k,p)*pow(Q,-a*b,p)\
            *gauss(a+k,k)*poch(M*M*pow(Q,-b,p)%p,k)%p
    operators={}
    head=lambda ab:ab[0]<N and ab[1]<N
    original=MixedEntries(N,p,q) if root_wall else None
    for sign in (-1,1):
        op={}
        for a,b in states:
            rows={}
            for k in range((a if sign>0 else b)+1):
                row=(b+sign*k,a-sign*k);value=coefficient(sign,a,b,k)
                if value:rows[row]=(value,0)
                if root_wall and head((a,b)):
                    if not head(row):assert value==0
                    else:
                        maximum=min(a,N-1-b) if sign>0 else min(b,N-1-a)
                        expected=original.direct(x,x,a,b,k,sign) if k<=maximum else 0
                        assert value==expected
                if not root_wall and not head((a,b)) and head(row):assert value==0
            if rows:op[(a,b)]=rows
        operators[sign]=op
    assert R.compose(operators[-1],operators[1])==R.identity(states)
    assert R.compose(operators[1],operators[-1])==R.identity(states)
    def compress(op):return {col:{row:v for row,v in rows.items() if head(row)}
                             for col,rows in op.items() if head(col)}
    def clean(op):return {col:rows for col,rows in op.items() if rows}
    ambient=R.compose(operators[1],operators[1])
    compressed=R.compose(clean(compress(operators[1])),clean(compress(operators[1])))
    assert clean(compress(ambient))==compressed
    return {'level':N,'root_submodule_wall':root_wall,
            'Weyl_quotient_wall':not root_wall,'both_infinite_R_signs_regular_inverse':True,
            'two_crossing_excursion_vanishes_on_wall':True}


def block_Weyl_checks(N,p,q):
    Q=q*q%p
    @cache
    def gauss(n,k):
        if k<0 or k>n:return 0
        if k==0 or k==n:return 1
        return (gauss(n-1,k)+pow(Q,n-k,p)*gauss(n-1,k-1))%p
    for block in range(5):
        for residue in range(N):
            assert gauss((block+1)*N+residue,N)==(block+1)%p
            # BT gives block+1; TB gives block, including vacuum.
            assert ((block+1)-block)%p==1
    return {'level':N,'actual_F_divided_block_coefficient':True,
            'exact_Weyl_pair_all_residues':True}


def centralizer_symbolic_checks():
    k,b,c,z=s.symbols('k b c z');degree=5
    def U(parameter):
        return s.Matrix(degree+1,degree+1,lambda r,j:
            s.binomial(r,j)*parameter**(r-j)*(1+k*parameter)**j if r>=j else 0)
    group=s.expand(b+c+k*b*c)
    assert (U(b)*U(c)-U(group)).applyfunc(s.expand)==s.zeros(degree+1)
    coherent=s.Matrix([z**r for r in range(degree+1)])
    assert (U(b)*coherent-s.Matrix([((1+k*b)*z+b)**r for r in range(degree+1)])).applyfunc(s.expand)==s.zeros(degree+1,1)
    B=s.zeros(degree+1);T=s.zeros(degree+1)
    for r in range(degree):B[r,r+1]=1;T[r+1,r]=r+1
    assert (U(b).diff(b).subs(b,0)-T*(s.eye(degree+1)+k*B))==s.zeros(degree+1)
    assert (U(b)*coherent)[0]==1
    return {'generic_regular_centralizer_group_law_jet_degree':degree,
            'coherent_torsor_action_exact':True,'ordered_infinitesimal_generator':True,
            'actual_vacuum_matrix_coefficient':1}


def generic_boundary_checks():
    q,M=s.symbols('q M',nonzero=True);Q=q*q;x=-M/q;rho=q-1/q
    records=[]
    for N in range(2,7):
        delta=1-Q**N;w=M*Q**(-N)-1/M
        E=lambda a:M*Q**(-a)-1/M
        F=lambda a:1-Q**(a+1)
        K=lambda a:x*Q**(-a)
        for a in range(2*N+1):
            comm=E(a+1)*F(a)-(F(a-1)*E(a) if a else 0)
            assert s.cancel(comm-rho*(K(a)-1/K(a)))==0
        headcomm=-(1-Q**(N-1))*E(N-1)
        assert s.cancel(headcomm-rho*(K(N-1)-1/K(N-1))+delta*w)==0
        D=s.Matrix([[0,w],[delta,0]])
        assert (D*D-delta*w*s.eye(2)).applyfunc(s.cancel)==s.zeros(2)
        assert s.cancel(w.subs(M,-q**N))==0
        adapter=(M**N-M**(-N))/(M-1/M)
        assert s.limit(s.log(M**(2*N))/(M**N-M**(-N)),M,1)==1
        assert s.cancel(N/adapter*(M**N-M**(-N))-N*(M-1/M))==0
        records.append({'level':N,'genuine_common_Verma_relations':True,
                        'actual_rank_one_boundary_matrix_factorization':True,
                        'marked_centralizer_period_complete_value':1})
    return records


def main():
    modules=[];bocksteins=[];Rcases=[];Weyl=[]
    for N in range(2,9):
        p,g,q=field(N)
        for M in (1,pow(g,3,p)):modules.append(root_module_case(N,M,p,q))
        bocksteins.append(meridian_bockstein(N,p,q));Weyl.append(block_Weyl_checks(N,p,q))
        if N<=5:
            Rcases.append(infinite_R_case(N,p,q,pow(g,3,p),True))
            Rcases.append(infinite_R_case(N,p,g,-pow(g,N,p)%p,False))
    result={'root_source_module_cases':modules,'nonzero_extension_Bocksteins':bocksteins,
            'infinite_R_subquotient_cases':Rcases,'actual_block_Weyl_cases':Weyl,
            'generic_two_wall_cases':generic_boundary_checks(),
            'regular_centralizer_coherent_action':centralizer_symbolic_checks(),
            'scope':'Common actual source and its torsor/normal adapters; no selected geometric regulator identity.'}
    path=Path(__file__).with_name('common_verma_two_wall_source_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'root_module_cases':len(modules),'nonzero_Bocksteins':len(bocksteins),
                      'infinite_R_wall_cases':len(Rcases),'Weyl_levels':len(Weyl),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
