#!/usr/bin/env python3
"""Exact source, Gaussian, and holonomy-complex Markov reductions.

Uniform arguments are in notes/pointed_markov_reduction.md.
The selected global period's geometric norm is not asserted.
"""

import json
from functools import cache
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_cut_density import fixed_point_complex_case
from audit_cyclic_steinberg_lattice import determinant
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices


def equal(a,b):
    if isinstance(a,sp.MatrixBase):
        assert (a-b).applyfunc(sp.cancel) == sp.zeros(*a.shape)
    else:
        assert sp.cancel(a-b)==0


@cache
def gaussian(n,k,Q):
    if k<0 or k>n:
        return sp.Integer(0)
    if k==0 or k==n:
        return sp.Integer(1)
    return sp.expand(gaussian(n-1,k,Q)+Q**(n-k)*gaussian(n-1,k-1,Q))


def newton_certificates():
    Q,t = sp.symbols('Q t',nonzero=True)
    records=[]
    for n in range(9):
        poch=sp.Integer(1);positive=sp.Integer(0);negative=sp.Integer(0)
        for k in range(n+1):
            if k:
                poch *= 1-t*Q**(k-1)
            choose=gaussian(n,k,Q)
            positive += (-1)**k*Q**(k*(k-1)//2+(1-n)*k)*choose*poch
            negative += choose*t**(n-k)*poch
        equal(positive,t**n)
        equal(negative,1)
        records.append({'degree':n,'both_finite_Newton_identities_exact':True})
    return records


def geometric_certificates():
    A,B,C,Y=sp.symbols('A B C Y',nonzero=True)
    D=1+Y-A
    records=[]
    for sign in (1,-1):
        if sign>0:
            H=sp.Matrix([[0,1,1],[1,0,-1],[1,-1,-1]])
            zs=[B,C,Y/A,B*C,Y*C/A]
            vs=[(0,1,0),(0,0,1),(-1,0,0),(0,1,1),(-1,0,1)]
            v=sp.Matrix([0,-1,1]);bp=A/C;cp=A*D/Y
            amp=A*B*(1-B*C)*(1-Y/A)/((1-B)*(1-C)*(1-Y*C/A))/B**2
            stationary=-(1-Y*C/A)*(1-B)/(B*(1-C))
            input_momenta=B*C/Y*(1-Y/A)/(1-Y*C/A)*A/C*(1-B*C)/(1-B)
            meridian=(1-Y*C/A)/(A*(1-Y/A))
        else:
            H=sp.Matrix([[0,-1,0],[-1,0,0],[0,0,0]])
            zs=[A,C,Y/B,A*C,Y*C/B]
            vs=[(1,0,0),(0,0,1),(0,-1,0),(1,0,1),(0,-1,1)]
            v=sp.Matrix([0,1,1]);bp=A*C;cp=Y/(A*D)
            amp=C/(A*B)*(1-A*C)*(1-Y/B)/((1-A)*(1-C)*(1-Y*C/B))*Y**2/B**2
            stationary=(1-A*C)*(1-Y/B)/(A*(1-C))
            input_momenta=Y/(A*B)*(1-A*C)/(1-A)*(1-Y/B)/(1-Y*C/B)
            meridian=A*(1-Y*C/B)/(1-Y/B)
        for z,vec,epsilon in zip(zs,vs,(1,1,1,-1,-1)):
            vec=sp.Matrix(vec);H+=epsilon*z/(1-z)*vec*vec.T
        pull=lambda f:sp.cancel(f.subs(B,bp).subs(C,cp))
        equal(pull(stationary),1)
        equal(pull(input_momenta),1)
        equal(pull(meridian),1)
        equal(bp.subs(C,cp),Y/D)
        hh=pull((v.T*H*v)[0])
        equal(hh,sign*D**2/((A-1)*(A-Y)))
        equal(pull(amp),hh)
        equal(-pull(amp)/hh,-1)
        equal(A*sp.diff(cp,A)/cp,sign*(1+Y-2*A)/D)
        records.append({'crossing_sign':sign,'unique_regular_critical_transfer':str(cp),
                        'trace_Hessian':str(sp.factor(hh)),
                        'cut_and_meridian_characters_one':True,
                        'full_principal_amplitude_squared_equals_trace_Hessian':True})
    h,v1,v2,h11,h12,h22=sp.symbols('h v1 v2 h11 h12 h22')
    old=sp.Matrix([[h11,h12],[h12,h22]])
    vec=sp.Matrix([v1,v2])
    Hnew=(old+h*vec*vec.T).row_join(-h*vec).col_join((-h*vec.T).row_join(sp.Matrix([[h]])))
    U=sp.eye(3);U[2,0]=v1;U[2,1]=v2
    equal(U.T*Hnew*U,sp.diag(old,h))
    equal(Hnew.det(),h*old.det())
    return {'local_principal_reductions':records,'universal_quadratic_chain_map_exact':True}


def original_source_case(N):
    p,generator,q=field(N)
    eye=np.eye(N,dtype=np.int64)
    cases=[]
    for M in (1,generator,pow(generator,2,p),pow(generator,7,p)):
        x=-M*pow(q,-1,p)%p
        positive,negative,pivot,theta=color_matrices(N,p,q,x)
        closing=np.kron(eye,pivot)
        for sign,crossing in ((1,positive),(-1,negative)):
            closed=crossing@closing%p
            partial=np.einsum('abcb->ac',closed.reshape((N,)*4))%p
            want=pow(theta,sign,p)*eye%p
            assert np.array_equal(partial,want)
            cases.append({'M':int(M),'crossing_sign':sign,'original_full_Markov_contraction_exact':True})
    return {'level':N,'prime':p,'whole_meridian_samples':cases}


def chain_equivalence(p,riley,frame,sign):
    old=fixed_point_complex_case(p,riley,frame,include_complex=True)
    new=fixed_point_complex_case(p,riley,frame,sign,include_complex=True)
    o,n=old.pop('complex_data'),new.pop('complex_data')
    a,D,m,A=o['a'],o['D'],o['m'],o['last_meridian']
    dim=D.shape[0]
    Ai=np.array([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]],dtype=np.int64)%p
    K,e=int(A[0,0]),int(A[0,1]);trace=int(np.trace(A))%p
    basis=[np.array([[1,0],[(trace-2*K)*pow(e,-1,p),-1]],dtype=np.int64)%p,
           np.array([[0,1],[-int(A[1,0])*pow(e,-1,p),0]],dtype=np.int64)%p]
    JA=np.array([[int((A@v@Ai%p)[0,k]) for v in basis] for k in (0,1)],dtype=np.int64)
    JAi=np.array([[int((Ai@v@A%p)[0,k]) for v in basis] for k in (0,1)],dtype=np.int64)
    assert determinant(JA,p)==determinant(JAi,p)==1
    domain=np.eye(dim+2,dtype=np.int64)
    domain[dim:,:dim]=(D+np.eye(dim,dtype=np.int64))[-2:,:]%p
    target=np.eye(dim+2,dtype=np.int64)
    target[dim-2:dim,dim:]=JAi
    target_inverse=np.eye(dim+2,dtype=np.int64)
    target_inverse[dim-2:dim,dim:]=-JAi%p
    want=np.zeros((dim+2,dim+2),dtype=np.int64)
    want[:dim,:dim]=D
    want[dim:,dim:]=(-np.eye(2,dtype=np.int64) if sign>0 else -JA)%p
    assert np.array_equal(target@n['D']%p@domain%p,want)
    assert np.array_equal(n['a'],domain@np.vstack([a,np.zeros((2,3),dtype=np.int64)])%p)
    lie=[np.diag([1,-1]),np.array([[0,1],[0,0]]),np.array([[0,0],[1,0]])]
    Ad=np.array([[int((A@v@Ai%p)[i,j]) for v in lie] for i,j in ((0,0),(0,1),(1,0))],dtype=np.int64)
    assert determinant(Ad,p)==1
    assert np.array_equal(n['m']@target_inverse%p,np.column_stack([Ad@m%p,np.zeros((3,2),dtype=np.int64)]))
    assert new['torsion']==old['torsion']
    return {'prime':p,'Riley_root':riley,'frame':list(frame),'stabilization_sign':sign,
            'middle_differential_and_both_end_maps_exact':True,
            'unchanged_torsion':old['torsion']}


def main():
    newton=newton_certificates()
    geometric=geometric_certificates()
    source=[original_source_case(N) for N in range(2,13)]
    chains=[]
    for p in (97,193,601):
        for riley in (u for u in range(p) if (u*u-u+1)%p==0):
            for frame in ((2,3),(3,2),(4,5)):
                for sign in (1,-1):
                    chains.append(chain_equivalence(p,riley,frame,sign))
    result={'scope':'Original finite source and regular geometric Gaussian/holonomy determinant contractions; no selected global volume theorem.',
            'finite_Newton_certificates':newton,'geometric_quadratic_reduction':geometric,
            'original_finite_Markov_contractions':source,'holonomy_chain_equivalences':chains}
    path=Path(__file__).with_name('pointed_markov_reduction_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'results':str(path),'symbolic_Newton_degrees':len(newton),
                      'principal_signs':len(geometric['local_principal_reductions']),
                      'original_root_levels':len(source),
                      'exact_original_source_contractions':sum(len(x['whole_meridian_samples']) for x in source),
                      'full_holonomy_chain_equivalences':len(chains)},indent=2),flush=True)


if __name__=='__main__':
    main()
