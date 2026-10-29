#!/usr/bin/env python3
"""Actual source residues sewn through a braid and their charged lift.

All root data are original ADO matrices. The first-order lift is solved
directly from E,F,K. This does not identify a geometric selected period.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as s

from audit_actual_peripheral_fusion import inverse_mod,module,tensor_module
from audit_braided_source_groupoid import projector_zero
from audit_finite_sum_annihilator import field
from audit_integral_centralizer_duality import nullspace,chebyshev_coefficients,divide_linear
from audit_intrinsic_cut_transport import casimir,modified_dimension
from audit_kashaev_ado_pointing import color_matrices,WORDS
from audit_regular_holonomy_braiding import mm


def apply_pair(columns,operator,position,N,strands,prime):
    left=N**position;right=N**(strands-position-2);count=columns.shape[1]
    packed=columns.reshape(left,N*N,right,count).transpose(1,0,2,3).reshape(N*N,-1)
    transformed=mm(prime,operator,packed)
    return transformed.reshape(N*N,left,right,count).transpose(1,0,2,3).reshape(N**strands,count)


def apply_word(columns,word,positive,negative,N,strands,prime,theta):
    value=columns.copy()
    for position,sign in reversed(word):
        value=apply_pair(value,positive if sign>0 else negative,position,N,strands,prime)
    return value*pow(theta,-sum(sign for _,sign in word),prime)%prime


def cut_rows(N,strands,pivot,prime):
    weights=np.array([1],dtype=np.int64)
    for _ in range(strands-1):weights=np.kron(weights,np.diag(pivot))%prime
    return np.arange(N**(strands-1)),weights


def full_cut(matrix,N,strands,pivot,dimension,prime):
    rows,weights=cut_rows(N,strands,pivot,prime)
    return dimension*sum(int(weights[j])*int(matrix[r,r]) for j,r in enumerate(rows))%prime


def full_cut_factor(left,right,N,strands,pivot,dimension,prime):
    rows,weights=cut_rows(N,strands,pivot,prime)
    return dimension*int(np.trace(mm(prime,right[:,rows]*weights[None,:]%prime,left[rows,:])))%prime


def root_data(N):
    prime,_,q=field(N);x=pow(q,N-1,prime)
    positive,negative,pivot,theta=color_matrices(N,prime,q,x)
    duality=np.zeros((N,N),dtype=np.int64)
    for a in range(N):duality[N-1-a,a]=pow(q,a*a,prime)
    cup=inverse_mod(duality,prime).T.reshape(N*N,1)
    cap=mm(prime,pivot,duality).reshape(1,N*N)
    rho=(q-pow(q,-1,prime))%prime
    dimension=pow(-1,N+1,prime)*pow(q,N*(1-N)//2,prime)*pow(N,-1,prime)%prime
    return prime,q,x,positive,negative,pivot,theta,cup,cap,rho,dimension


def sewn_corner_case(N,strands):
    p,q,x,B,Bi,pivot,theta,cup,cap,rho,dimension=root_data(N)
    small=N**(strands-2);identity=np.eye(small,dtype=np.int64)
    inclusion=np.kron(cup,identity);projection=np.kron(cap,identity)
    beta=apply_pair(inclusion,B,1,N,strands,p)*pow(theta,-1,p)%p
    # Compute projection*B_23 by acting on its transpose; no dense full braid.
    alpha=apply_pair(projection.T,B.T,1,N,strands,p).T*pow(theta,-1,p)%p
    assert not np.any(mm(p,projection,inclusion))
    assert np.array_equal(mm(p,projection,beta),identity)
    assert np.array_equal(mm(p,alpha,inclusion),identity)
    negative_curl=mm(p,projection,apply_pair(inclusion,Bi,1,N,strands,p))
    assert np.array_equal(negative_curl,identity*pow(theta,-1,p)%p)
    omega=mm(p,alpha,beta)
    alpha=(alpha-mm(p,omega,projection))%p
    assert np.array_equal(mm(p,alpha,inclusion),identity)
    assert not np.any(mm(p,alpha,beta))
    left=[inclusion,beta];right=[alpha,projection]
    for i,j in product(range(2),repeat=2):
        expected=identity if i==j else np.zeros_like(identity)
        assert np.array_equal(mm(p,right[i],left[j]),expected)
    source_ops=module(N,p,q,x);full_ops=source_ops
    for _ in range(strands-3):source_ops=tensor_module(source_ops,module(N,p,q,x),p)
    for _ in range(strands-1):full_ops=tensor_module(full_ops,module(N,p,q,x),p)
    for big,little in zip(full_ops,source_ops):
        for U in left:assert np.array_equal(mm(p,big,U),mm(p,U,little))
        for V in right:assert np.array_equal(mm(p,V,big),mm(p,little,V))
    probes=[np.eye(small,dtype=np.int64)]
    if strands>3:probes.append(B)
    for probe in probes:
        expected=full_cut(probe,N,strands-2,pivot,dimension,p)
        for i,j in product(range(2),repeat=2):
            actual=full_cut_factor(mm(p,left[i],probe),right[j],N,strands,pivot,dimension,p)
            assert actual==(expected if i==j else 0)
    # Independently construct the original source Casimir residue.
    pair_ops=tensor_module(module(N,p,q,x),module(N,p,q,x),p)
    O=casimir(pair_ops,p,q);c0=(q+pow(q,-1,p))%p
    e0=projector_zero(N,p,q,O)
    J=mm(p,(O-c0*np.eye(N*N,dtype=np.int64))%p,e0)
    assert np.array_equal(J,mm(p,cup,cap)*pow(-1,N,p)*rho*rho%p)
    residue=J*(N*pow(rho,-1,p)%p)%p
    words=[('stabilized_unknot',tuple((j,1) for j in reversed(range(strands-1))))]
    if strands==3:words.extend((name,tuple(word)) for name,word in zip(
        ('figure_eight','positive_test','negative_test'),WORDS))
    else:words.append(('stabilized_figure_eight',tuple(WORDS[0])+((2,1),)))
    rows,weights=cut_rows(N,strands,pivot,p)
    basis=np.zeros((N**strands,len(rows)),dtype=np.int64);basis[rows,np.arange(len(rows))]=1
    source_columns=apply_pair(basis,residue,0,N,strands,p)
    records=[]
    for name,word in words:
        acted=apply_word(inclusion,word,B,Bi,N,strands,p,theta)
        sewn=mm(p,projection,acted)
        lower_cut=full_cut(sewn,N,strands-2,pivot,dimension,p)
        expected=pow(-1,N,p)*N*rho*lower_cut%p
        literal=apply_word(source_columns,word,B,Bi,N,strands,p,theta)
        actual=dimension*sum(int(weights[j])*int(literal[r,j]) for j,r in enumerate(rows))%p
        assert actual==expected
        if name=='stabilized_unknot':assert lower_cut==dimension*pow(theta,-1,p)%p
        records.append({'word':name,'zero_framed_lower_source_cut':lower_cut,
                        'full_sewn_meridian_source_residue':actual,
                        'literal_Casimir_source_and_lower_strand_cut_agree':True})
    return {'level':N,'prime':p,'strands':strands,'source_rank':small,
            'two_copy_source_corner_and_all_original_E_F_K_intertwinings':True,
            'actual_full_cut_corner_pairings_exact':True,
            'positive_and_negative_curl_scalar':[theta,pow(theta,-1,p)],
            'sewn_word_cases':records}


def color_jet(N,p,q,charge):
    x=pow(q,N-1,p);ops=module(N,p,q,x);rho=(q-pow(q,-1,p))%p
    derivative=[np.zeros_like(A) for A in ops]
    for a in range(1,N):
        integer=(pow(q,a,p)-pow(q,-a,p))*pow(rho,-1,p)%p
        derivative[0][a-1,a]=(charge*integer*(x*pow(q,1-a,p)
            +pow(x,-1,p)*pow(q,a-1,p))*pow(rho,-1,p))%p
    derivative[2]=charge*ops[2]%p
    return ops,tuple(derivative)


def tensor_jet(left,right,p):
    A,Ad=left;B,Bd=right;E,F,K=A;e,f,k=B;Ed,Fd,Kd=Ad;ed,fd,kd=Bd
    I,J=np.eye(len(E),dtype=np.int64),np.eye(len(e),dtype=np.int64)
    Ki=np.diag([pow(int(v),-1,p) for v in np.diag(K)]).astype(np.int64)
    Kid=-mm(p,Ki,Kd,Ki)%p
    derivative=((np.kron(Ed,k)+np.kron(E,kd)+np.kron(I,ed))%p,
                (np.kron(Fd,J)+np.kron(Kid,f)+np.kron(Ki,fd))%p,
                (np.kron(Kd,k)+np.kron(K,kd))%p)
    return tensor_module(A,B,p),derivative


def charged_first_jet_case(N):
    p,q,x,B,Bi,pivot,theta,cup,cap,rho,dimension=root_data(N)
    inclusion=np.kron(cup,np.eye(N,dtype=np.int64));size=N**3
    one=color_jet(N,p,q,1)
    W,Wd=tensor_jet(tensor_jet(one,one,p),one,p)
    P,Pd=color_jet(N,p,q,3)
    indices=np.array([(sum(a)+1)%N for a in product(range(N),repeat=3)],dtype=np.int64)
    constraints=np.zeros((2*size,size),dtype=np.int64);rhs=np.zeros(2*size,dtype=np.int64)
    for block,step in ((0,1),(1,-1)):
        Z,Zd,Zp,Zpd=W[block],Wd[block],P[block],Pd[block]
        difference=(mm(p,inclusion,Zpd)-mm(p,Zd,inclusion))%p
        for row in range(size):
            column=(int(indices[row])+step)%N;line=block*size+row
            possible=np.flatnonzero(Z[row])
            possible=possible[indices[possible]==column]
            constraints[line,possible]=Z[row,possible]
            constraints[line,row]=(constraints[line,row]-Zp[indices[row],column])%p
            rhs[line]=difference[row,column]
    solutions=nullspace(np.column_stack((constraints,-rhs)),p)
    possible=np.flatnonzero(solutions[-1]);assert len(possible)
    candidate=solutions[:,possible[0]]*pow(int(solutions[-1,possible[0]]),-1,p)%p
    first=np.zeros_like(inclusion);first[np.arange(size),indices]=candidate[:-1]
    for Z,Zd,Zp,Zpd in zip(W,Wd,P,Pd):
        assert not np.any((mm(p,Z,first)+mm(p,Zd,inclusion)
                          -mm(p,first,Zp)-mm(p,inclusion,Zpd))%p)
    wrong_derivative=one[1][2]
    obstruction=(mm(p,inclusion,wrong_derivative)-mm(p,Wd[2],inclusion))%p
    assert np.any(obstruction[np.arange(size),indices])
    return {'level':N,'prime':p,'weight_restricted_lift_variables':size,
            'source_charge_three_lifts_the_actual_cup_through_first_meridian_order':True,
            'all_E_F_K_first_order_intertwining_equations_checked':True,
            'unchanged_source_charge_one_is_obstructed_at_first_order':True}


def charge_factor_certificate():
    M,U=s.symbols('M U',nonzero=True)
    ratio=(M*M+1+M**-2)/(U+1+U**-1)
    assert s.cancel((M**3-M**-3)/(M-M**-1)-(M*M+1+M**-2))==0
    assert ratio.subs({M:1,U:1})==1
    return {'full_dimension_ratio':'(M^2+1+M^(-2))/(U+1+U^(-1))',
            'whole_complete_ratio':1,'source_meridian_step':'M^3 -> q^3*M^3',
            'both_source_charge_and_central_factors_retained':True}


def rational_source_corner_case(N,meridian_power):
    p,q,x0,B,Bi,pivot0,theta,cup,cap,rho,dimension0=root_data(N)
    I=np.eye(N,dtype=np.int64)
    i0=np.kron(cup,I);c0=np.kron(cap,I)
    beta0=apply_pair(i0,B,1,N,3,p)*pow(theta,-1,p)%p
    alpha0=apply_pair(c0.T,B.T,1,N,3,p).T*pow(theta,-1,p)%p
    alpha0=(alpha0-mm(p,alpha0,beta0,c0))%p
    old_left=[i0,beta0];old_right=[alpha0,c0]
    _,generator,_=field(N)
    M=1 if meridian_power is None else pow(generator,meridian_power,p)
    U=pow(M,2*N,p)
    if M!=1 and ((U-1)%p==0 or (pow(U,3,p)-1)%p==0):
        raise ZeroDivisionError('source or target modified dimension is on another pole')
    x=-M*pow(q,-1,p)%p;z=-pow(M,3,p)*pow(q,-1,p)%p
    small_ops=module(N,p,q,z);big_ops=module(N,p,q,x)
    for _ in range(2):big_ops=tensor_module(big_ops,module(N,p,q,x),p)
    E,F,K=big_ops
    O=casimir(big_ops,p,q)
    k=pow(z,N,p);root=(q*z+pow(q*z,-1,p))%p
    coefficients=chebyshev_coefficients(N,p)
    coefficients[0]=(coefficients[0]+k+pow(k,-1,p))%p
    quotient=divide_linear(coefficients,root,p)
    derivative=sum(j*c*pow(root,j-1,p) for j,c in enumerate(coefficients) if j)%p
    if not derivative:raise ZeroDivisionError('the selected simple block is on its discriminant')
    mask=np.flatnonzero(np.diag(K)==z)
    block=O[np.ix_(mask,mask)];projector=np.zeros_like(block);identity=np.eye(len(mask),dtype=np.int64)
    for coefficient in reversed(quotient):projector=(mm(p,projector,block)+coefficient*identity)%p
    projector=projector*pow(derivative,-1,p)%p
    assert np.array_equal(mm(p,projector,projector),projector)
    left=[];right=[]
    for old_U,old_V in zip(old_left,old_right):
        h=np.zeros(N**3,dtype=np.int64);h[mask]=mm(p,projector,old_U[mask,:1])[:,0]
        columns=[];value=h[:,None]
        for _ in range(N):columns.append(value[:,0]);value=mm(p,F,value)
        target=np.column_stack(columns);left.append(target)
        row=np.zeros((1,N**3),dtype=np.int64)
        row[:,mask]=mm(p,old_V[:1,mask],projector)
        rows=[row[0].copy()]
        for a in range(1,N):
            row=mm(p,row,E)*pow(int(small_ops[0][a-1,a]),-1,p)%p
            rows.append(row[0].copy())
        right.append(np.vstack(rows))
    overlap=np.zeros((2,2),dtype=np.int64)
    for i,j in product(range(2),repeat=2):
        value=mm(p,right[i],left[j]);overlap[i,j]=value[0,0]
        assert np.array_equal(value,int(value[0,0])*I%p)
    if (overlap[0,0]*overlap[1,1]-overlap[0,1]*overlap[1,0])%p==0:
        raise ZeroDivisionError('outside the anchored two-copy source chart')
    inverse=inverse_mod(overlap,p)
    right=[sum(int(inverse[i,j])*right[j] for j in range(2))%p for i in range(2)]
    for i,j in product(range(2),repeat=2):
        assert np.array_equal(mm(p,right[i],left[j]),I if i==j else np.zeros_like(I))
    for big,little in zip(big_ops,small_ops):
        for inclusion in left:assert np.array_equal(mm(p,big,inclusion),mm(p,inclusion,little))
        for projection in right:assert np.array_equal(mm(p,projection,big),mm(p,little,projection))
    pivot=color_matrices(N,p,q,x)[2]
    dimension=dimension0 if M==1 else modified_dimension(N,p,q,x)
    source_dimension=dimension0 if M==1 else modified_dimension(N,p,q,z)
    for i,j in product(range(2),repeat=2):
        actual=full_cut_factor(left[i],right[j],N,3,pivot,dimension,p)
        assert actual==(source_dimension if i==j else 0)
    if M==1:
        assert all(np.array_equal(a,b) for a,b in zip(left,old_left))
        assert all(np.array_equal(a,b) for a,b in zip(right,old_right))
    else:
        ratio=((M*M+1+pow(M,-2,p))*pow((U+1+pow(U,-1,p))%p,-1,p))%p
        assert source_dimension*pow(dimension,-1,p)%p==ratio
    return {'level':N,'prime':p,'meridian_power':meridian_power,
            'complete_source_anchor':M==1,
            'source_highest_root':'-M^3/q',
            'explicit_rational_Steinberg_projection_and_two_copy_retraction':True,
            'all_actual_E_F_K_intertwinings_and_full_cut_weights_checked':True,
            'source_full_dimension':source_dimension,
            'whole_meridian_charge_factor_retained':True}


def main():
    corners=[sewn_corner_case(N,3) for N in (2,3,4,5,6,9)]
    corners.extend(sewn_corner_case(N,4) for N in (2,3))
    rational=[]
    for N in (2,3,4,5,6):
        rational.append(rational_source_corner_case(N,None))
        accepted=0
        for exponent in range(1,50):
            try:record=rational_source_corner_case(N,exponent)
            except ZeroDivisionError:continue
            rational.append(record);accepted+=1
            if accepted==2:break
        assert accepted==2
    result={'scope':'Actual all-word residue sewing and projective source corner with conserved meridian charge; no geometric selected-period or volume theorem.',
            'source_corners_and_sewn_words':corners,
            'actual_charged_source_first_jets':[charged_first_jet_case(N) for N in (2,3,4,5,6)],
            'explicit_rational_charged_corners':rational,
            'charge_and_full_dimension_factor':charge_factor_certificate()}
    output=Path(__file__).with_name('sewn_source_corner_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':str(output),'actual_source_corner_cases':len(corners),
                      'sewn_original_word_cases':sum(len(r['sewn_word_cases']) for r in corners),
                      'direct_charged_first_order_lifts':len(result['actual_charged_source_first_jets']),
                      'explicit_rational_charge_three_corners':len(rational)}),flush=True)


if __name__=='__main__':main()
