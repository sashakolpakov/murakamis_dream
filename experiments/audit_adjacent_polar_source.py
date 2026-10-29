#!/usr/bin/env python3
"""Entire adjacent polar projectors on their charged two-channel source.

Checks use actual tensor matrices, original projector cuts and root phases.
No selected geometric-period or volume statement is asserted.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as s

from audit_actual_peripheral_fusion import inverse_mod,module,tensor_module
from audit_braided_source_groupoid import projector_zero
from audit_cyclic_steinberg_lattice import rank
from audit_finite_sum_annihilator import field
from audit_integral_centralizer_duality import chebyshev_coefficients,divide_linear
from audit_intrinsic_cut_transport import casimir,fusion_frame,modified_dimension
from audit_kashaev_ado_pointing import color_matrices,WORDS
from audit_regular_holonomy_braiding import mm
from audit_sewn_source_corner import root_data,apply_word,cut_rows,full_cut


def symbolic_certificates():
    a,c,t,z,Q=s.symbols('a c t z Q',nonzero=True);v=c/a
    ratio=-v*(z-Q*t)*(1-a*z)/((1-Q*z)*(1-c*z))
    G=lambda w:-Q*t*(1-w)*(1-c*w/Q)/(w*(1-Q*t)*(1-c*t))
    difference=1-(1-v*t)*(1-Q*t/z)/((1-Q*t)*(1-c*t))
    assert s.cancel(ratio*G(Q*z)-G(z)-difference)==0
    delta,A=s.symbols('delta A',nonzero=True)
    T1=s.Matrix([[delta,A],[0,0]]);T2=s.Matrix([[0,0],[A,delta]])
    assert T1*T1==delta*T1 and T2*T2==delta*T2
    assert T1*T2*T1==A*A*T1 and T2*T1*T2==A*A*T2
    E11=s.Matrix([[1,0],[0,0]]);E22=s.eye(2)-E11
    assert T1*T2-delta*T1==(A*A-delta*delta)*E11
    assert T2*T1-delta*T2==(A*A-delta*delta)*E22
    E1=T1/delta;E2=T2/delta
    assert s.trace(E1*E2)==A*A/(delta*delta)
    D=s.diag(1/delta,1)
    assert D.inv()*E1*D==s.Matrix([[1,A],[0,0]])
    assert D.inv()*E2*D==s.Matrix([[0,0],[A/delta**2,1]])
    q,M,V,epsilon=s.symbols('q M V epsilon',nonzero=True)
    rho=q-q**-1;wall=q*M*M-q**-1*M**-2
    overlap=epsilon*rho*(M+M**-1)*wall/(V+V**-1)
    full_source=(1+V**-2)*overlap/(rho*(M*M-M**-2))
    assert s.cancel(full_source-epsilon*M*wall/(V*(M*M-1)))==0
    return {'terminating_finite_sum_telescoper_exact':True,
            'both_projector_relations_and_matrix_units_exact':True,
            'simultaneous_finite_integral_lattice_obstructed_by_trace_pole':True,
            'single_projector_lattice_change_makes_adjacent_pole_order_two':True,
            'full_affine_source_cancels_one_plus_U_and_retains_only_Y_minus_one_pole':True,
            'ordered_source_pair_comparison_group':'G_m',
            'selected_global_period_not_identified':True}


def block_product(A,B,masks,p):
    out=np.zeros_like(A)
    for mask in masks:out[np.ix_(mask,mask)]=mm(p,A[np.ix_(mask,mask)],B[np.ix_(mask,mask)])
    return out


def steinberg_projection(N,p,q,z,ops):
    E,F,K=ops;rho=(q-pow(q,-1,p))%p
    masks=[np.flatnonzero(np.diag(K)==z*pow(q,-2*a,p)%p) for a in range(N)]
    assert all(len(mask)==N*N for mask in masks)
    first,last=masks[0],masks[-1]
    root=(q*z+pow(q*z,-1,p))%p
    O=(rho*rho*mm(p,F[np.ix_(first,last)],E[np.ix_(last,first)])
       +root*np.eye(N*N,dtype=np.int64))%p
    k=pow(z,N,p);coefficients=chebyshev_coefficients(N,p)
    coefficients[0]=(coefficients[0]+k+pow(k,-1,p))%p
    quotient=divide_linear(coefficients,root,p)
    derivative=sum(j*c*pow(root,j-1,p) for j,c in enumerate(coefficients) if j)%p
    if not derivative:raise ZeroDivisionError('on the chosen block discriminant')
    block=np.zeros_like(O);identity=np.eye(N*N,dtype=np.int64)
    for coefficient in reversed(quotient):block=(mm(p,block,O)+coefficient*identity)%p
    block=block*pow(derivative,-1,p)%p
    S=np.zeros_like(E);S[np.ix_(first,first)]=block
    little=module(N,p,q,z)
    for a in range(1,N):
        previous,current=masks[a-1],masks[a]
        block=mm(p,F[np.ix_(current,previous)],block,E[np.ix_(previous,current)])
        block=block*pow(int(little[0][a-1,a]),-1,p)%p
        S[np.ix_(current,current)]=block
    assert np.array_equal(block_product(S,S,masks,p),S)
    return S,masks


def actual_case(N,exponent):
    p,q,x0,B0,Bi0,pivot0,theta0,cup,cap,rho,dimension0=root_data(N)
    _,generator,_=field(N);M=1 if exponent is None else pow(generator,exponent,p)
    U=pow(M,2*N,p)
    if M!=1 and ((U*U-1)%p==0 or (pow(U,3,p)-1)%p==0):
        raise ZeroDivisionError('on a noncomplete fusion wall')
    x=-M*pow(q,-1,p)%p;z=-pow(M,3,p)*pow(q,-1,p)%p
    color=module(N,p,q,x);pair=tensor_module(color,color,p);ops=tensor_module(pair,color,p)
    E,F,K=ops;S,masks=steinberg_projection(N,p,q,z,ops)
    I=np.eye(N,dtype=np.int64);size=N**3
    pair_E=color[0];h=[1]
    for a in range(N-1):
        coefficient=-int(pair_E[N-2-a,N-1-a])*pow(q,2*(N-a-2),p)
        denominator=int(pair_E[a,a+1])*x%p
        h.append(h[-1]*coefficient*pow(denominator,-1,p)%p)
    highest=np.zeros(N*N,dtype=np.int64)
    for a,value in enumerate(h):highest[a*N+N-1-a]=theta0*value%p
    v0=I[:,0];seeds=[np.kron(highest,v0),np.kron(v0,highest)]
    inclusions=[]
    for seed in seeds:
        columns=[];value=seed[:,None]
        for _ in range(N):columns.append(value[:,0]);value=mm(p,F,value)
        inclusions.append(np.column_stack(columns))
    little=module(N,p,q,z)
    for big,small in zip(ops,little):
        for inclusion in inclusions:assert np.array_equal(mm(p,big,inclusion),mm(p,inclusion,small))
    delta=rho*(M*M-pow(M,-2,p))%p
    coupling=(pow(-1,N,p)*rho*(M+pow(M,-1,p))
              *(q*M*M-pow(q,-1,p)*pow(M,-2,p))
              *pow((pow(M,N,p)+pow(M,-N,p))%p,-1,p))%p
    if (coupling*coupling-delta*delta)%p==0:
        raise ZeroDivisionError('outside the joint source corner')
    if M==1:
        O=casimir(pair,p,q);c0=(q+pow(q,-1,p))%p
        cluster=projector_zero(N,p,q,O)
        T=mm(p,(O-c0*np.eye(N*N,dtype=np.int64))%p,cluster)
        assert np.array_equal(T,mm(p,cup,cap)*pow(-1,N,p)*rho*rho%p)
        projector=None
    else:
        H,Hi,_=fusion_frame(N,p,q,x,x)
        projector=mm(p,H[:,-N:],Hi[-N:,:]);T=projector*delta%p
        # Independent terminating norm from the actual highest vector.
        lam=[pow(-1,a,p)*pow(x,-a,p)*pow(q,a*(a-1),p)%p for a in range(N)]
        norm=sum(a*b for a,b in zip(lam,h))%p
        r=pow(x,-2,p);Q=q*q%p
        expected=(1+pow(r,N,p))*(1-r*pow(Q,-1,p))*pow((1-r*r*pow(Q,-3,p))%p,-1,p)%p
        assert norm==expected and coupling==delta*lam[-1]*pow(norm,-1,p)%p
    Ts=[np.kron(T,I),np.kron(I,T)]
    # The constant opposite caps are regular coordinate left inverses.
    opposite=[np.kron(I,cap),np.kron(cap,I)]
    rows=[]
    for j in range(2):
        determinant=mm(p,opposite[j],inclusions[j])
        try:coordinate=inverse_mod(determinant,p)
        except StopIteration:raise ZeroDivisionError('outside an anchored image chart')
        coordinate=mm(p,coordinate,opposite[j])
        row=mm(p,coordinate,block_product(Ts[j],S,masks,p));rows.append(row)
        assert np.array_equal(mm(p,inclusions[j],row),block_product(Ts[j],S,masks,p))
    C=np.array([[delta,coupling],[coupling,delta]],dtype=np.int64)
    Ci=inverse_mod(C,p)
    retractions=[sum(int(Ci[i,j])*rows[j] for j in range(2))%p for i in range(2)]
    for i,j in product(range(2),repeat=2):
        assert np.array_equal(mm(p,retractions[i],inclusions[j]),I if i==j else np.zeros_like(I))
    for big,small in zip(ops,little):
        for retraction in retractions:
            assert np.array_equal(mm(p,retraction,big),mm(p,small,retraction))
    included=np.column_stack(inclusions);retracted=np.vstack(retractions)
    corner=mm(p,included,retracted)
    canonical=[np.array([[delta,coupling],[0,0]],dtype=np.int64),
               np.array([[0,0],[coupling,delta]],dtype=np.int64)]
    for j in range(2):
        assert np.array_equal(block_product(Ts[j],S,masks,p),mm(p,included,np.kron(canonical[j],I),retracted))
    record={'level':N,'prime':p,'meridian_power':exponent,'complete_anchor':M==1,
            'source_charge_three':True,'exact_overlap_equals_actual_pivotal_moment':True,
            'entire_adjacent_projectors_have_the_stated_joint_two_channel_form':True}
    if M==1:
        nu=pow(-1,N,p)*rho*rho%p
        assert coupling==nu
        i0,i1=np.kron(cup,I),np.kron(I,cup)
        c0,c1=np.kron(cap,I),np.kron(I,cap)
        assert np.array_equal(inclusions[0],i0) and np.array_equal(inclusions[1],i1)
        assert np.array_equal(retractions[0],c1) and np.array_equal(retractions[1],c0)
        assert np.array_equal(mm(p,c0,i1),I) and np.array_equal(mm(p,c1,i0),I)
        assert not np.any(mm(p,c0,i0)) and not np.any(mm(p,c1,i1))
        for j in range(2):
            assert not np.any(block_product(Ts[j],np.eye(size,dtype=np.int64)-S,masks,p))
        record['regular_remainder_numerators_vanish_at_completeness']=True
        record['nonzero_double_pole_trace_coefficient']=N*rho*rho*pow(16,-1,p)%p
    else:
        actual=[np.kron(projector,I),np.kron(I,projector)]
        background=[];dimension=modified_dimension(N,p,q,x)
        source_dimension=modified_dimension(N,p,q,z)
        positive,negative,pivot,theta=color_matrices(N,p,q,x)
        for j in range(2):
            regular=(actual[j]-block_product(actual[j],S,masks,p))%p;background.append(regular)
            assert np.array_equal(block_product(regular,regular,masks,p),regular)
            assert sum(rank(regular[np.ix_(mask,mask)],p) for mask in masks)==N*(N-1)
            assert full_cut(regular,N,3,pivot,dimension,p)==-source_dimension%p
            assert np.array_equal(actual[j],(mm(p,included,np.kron(canonical[j]*pow(delta,-1,p)%p,I),retracted)+regular)%p)
        cut_indices,weights=cut_rows(N,3,pivot,p);word_checks=[]
        for name,word in (('identity',()),('figure_eight',tuple(WORDS[0]))):
            acted=apply_word(included,word,positive,negative,N,3,p,theta)
            blocks=[[mm(p,retractions[i],acted[:,j*N:(j+1)*N]) for j in range(2)] for i in range(2)]
            for j in range(2):
                literal=apply_word(actual[j][:,cut_indices],word,positive,negative,N,3,p,theta)
                lhs=dimension*sum(int(weights[k])*int(literal[r,k]) for k,r in enumerate(cut_indices))%p
                regular=apply_word(background[j][:,cut_indices],word,positive,negative,N,3,p,theta)
                rest=dimension*sum(int(weights[k])*int(regular[r,k]) for k,r in enumerate(cut_indices))%p
                diagonal=blocks[0][0] if j==0 else blocks[1][1]
                off_diagonal=blocks[1][0] if j==0 else blocks[0][1]
                rhs=(source_dimension*(int(diagonal[0,0])+coupling*pow(delta,-1,p)*int(off_diagonal[0,0]))+rest)%p
                assert lhs==rhs
                word_checks.append({'word':name,'projector_position':j,'whole_full_cut':lhs})
        record['regular_remainder_rank']=N*(N-1)
        record['whole_source_cut_decompositions']=word_checks
    return record


def main():
    complete=[];generic=[]
    for N in (2,3,4,5,6,9):
        complete.append(actual_case(N,None));accepted=0
        for exponent in range(1,50):
            try:record=actual_case(N,exponent)
            except ZeroDivisionError:continue
            generic.append(record);accepted+=1
            if accepted==2:break
        assert accepted==2
    result={'scope':'Exact full local adjacent-source normal form and obstruction to a common integral lattice; no geometric selected-period or volume theorem.',
            'uniform_symbolic_certificates':symbolic_certificates(),
            'complete_original_source_corners':complete,'generic_original_polar_projectors':generic}
    output=Path(__file__).with_name('adjacent_polar_source_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':str(output),'complete_adjacent_corners':len(complete),
                      'generic_entire_projector_pairs':len(generic),
                      'whole_actual_tensor_cut_decompositions':sum(len(r['whole_source_cut_decompositions']) for r in generic),
                      'universal_telescoping_and_lattice_obstruction_checked':True}),flush=True)


if __name__=='__main__':main()
