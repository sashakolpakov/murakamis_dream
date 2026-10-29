#!/usr/bin/env python3
"""Actual semicyclic turns, pivotal caps, and the dual carry source.

The checks retain the central wrap, double-dual normalization, original
cut functional and torsion linking form. No hyperbolic period or norm
identification is asserted.
"""

from itertools import product
import json
from math import comb
from pathlib import Path

import numpy as np

from audit_actual_peripheral_fusion import inverse_mod, module, tensor_module
from audit_actual_peripheral_fusion import matrix_power
from audit_cyclic_steinberg_lattice import determinant, rank
from audit_finite_sum_annihilator import field
from audit_factorial_source_torsor import matrices, mul
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_regular_holonomy_braiding import mm


def semicyclic(level, prime, q, x, phi):
    E,F,K=module(level,prime,q,x)
    F[0,level-1]=phi%prime
    return E,F,K


def dual_data(level,prime,q,x,phi):
    Q=q*q%prime
    y=pow(x*Q,-1,prime)
    psi=-pow(x,level,prime)*phi%prime
    coefficients=[pow(-x,a,prime)*pow(Q,a*(a+1)//2,prime)%prime for a in range(level)]
    J=np.zeros((level,level),dtype=np.int64)
    for a,c in enumerate(coefficients):J[level-1-a,a]=c
    g=np.diag([pow(x*pow(Q,-a,prime),1-level,prime) for a in range(level)]).astype(np.int64)
    return y,psi,J,g


def turns_case(level,kind,phi):
    prime,generator,q=field(level)
    x=generator if kind=='generic' else pow(q,level-1,prime)
    E,F,K=semicyclic(level,prime,q,x,phi)
    y,psi,J,g=dual_data(level,prime,q,x,phi)
    dual=semicyclic(level,prime,q,y,psi)
    Ki=inverse_mod(K,prime)
    inherited=[-mm(prime,E,Ki).T%prime,-mm(prime,K,F).T%prime,Ki.T]
    assert all(np.array_equal(mm(prime,A,J),mm(prime,J,B)) for A,B in zip(inherited,dual))
    xx,pp,JJ,_=dual_data(level,prime,q,y,psi)
    assert xx==x and pp==phi%prime
    assert np.array_equal(mm(prime,inverse_mod(J.T,prime),JJ),g)
    Ji=inverse_mod(J,prime);gi=inverse_mod(g,prime)
    ev=J.T.reshape(1,level**2)
    coev=Ji.T.reshape(level**2,1)
    right_ev=mm(prime,g,J).reshape(1,level**2)
    right_coev=mm(prime,Ji,gi).reshape(level**2,1)
    eye=np.eye(level,dtype=np.int64)
    assert np.array_equal(mm(prime,np.kron(eye,ev),np.kron(coev,eye)),eye)
    assert np.array_equal(mm(prime,np.kron(ev,eye),np.kron(eye,coev)),eye)
    assert np.array_equal(mm(prime,np.kron(right_ev,eye),np.kron(eye,right_coev)),eye)
    assert np.array_equal(mm(prime,np.kron(eye,right_ev),np.kron(right_coev,eye)),eye)
    for left,right,cap,cup in ((dual,(E,F,K),ev,right_coev),((E,F,K),dual,right_ev,coev)):
        EE,FF,KK=tensor_module(left,right,prime)
        assert not np.any(mm(prime,cap,EE)) and not np.any(mm(prime,cap,FF))
        assert np.array_equal(mm(prime,cap,KK),cap)
        assert not np.any(mm(prime,EE,cup)) and not np.any(mm(prime,FF,cup))
        assert np.array_equal(mm(prime,KK,cup),cup)
        assert not np.any(matrix_power(FF,level,prime))
    assert int(np.trace(g))%prime==0
    assert int(mm(prime,right_ev,coev)[0,0])==0
    return {'level':level,'color':kind,'phi':phi,'prime':prime,'dual_x':y,'dual_phi':psi,
            'all_three_antipode_intertwinings':True,'all_four_snake_identities':True,
            'left_and_right_caps_and_cups_are_Hopf_maps':True,
            'double_dual_is_exact_actual_pivot':True,
            'cap_total_F_N_is_zero':True,'ordinary_pivotal_bubble_is_zero':True}


def cut_case(level,kind):
    prime,generator,q=field(level)
    x=generator if kind=='generic' else pow(q,level-1,prime)
    actual=color_matrices(level,prime,q,x)
    _,_,J,g=dual_data(level,prime,q,x,0)
    # Construct closing weights from the actual cup and right cap.
    cup=inverse_mod(J,prime).T
    cap=mm(prime,g,J)
    weights=np.sum(cup*cap,axis=1)%prime
    assert np.array_equal(weights,np.diag(actual[2]))
    eye=np.eye(level,dtype=np.int64);records=[]
    for word in WORDS:
        B=np.eye(level**3,dtype=np.int64)
        for position,sign in word:
            local=actual[0 if sign>0 else 1]
            B=mm(prime,B,np.kron(local,eye) if position==0 else np.kron(eye,local))
        tensor=B.reshape((level,)*6)
        closed=np.einsum('abcdbc,b,c->ad',tensor,weights,weights)%prime
        closed=closed*pow(actual[3],-sum(sign for _,sign in word),prime)%prime
        target=reduced_period(level,prime,*actual,word)
        assert np.array_equal(closed,target*eye%prime)
        ordinary=np.einsum('abcdbc->ad',tensor)%prime
        ordinary=ordinary*pow(actual[3],-sum(sign for _,sign in word),prime)%prime
        assert int(np.trace(mm(prime,g,closed)))%prime==0
        records.append({'word':word,'actual_cut_value':target,'entire_scalar_cut_from_explicit_turns':True,
                        'omitting_pivotal_turn_changes_cut':not np.array_equal(ordinary,closed),
                        'closing_the_marked_strand_by_an_ordinary_cap_gives_zero':True})
    return {'level':level,'color':kind,'periods':records}


def dual_batch(values,prime):
    return np.stack([inverse_mod(value,prime).T for value in values])


def endpoint_frame(level,prime,Q,x,a,b):
    lam=pow(x,-level,prime)
    X=np.zeros((level,level),dtype=np.int64)
    for j in range(level-1):X[j+1,j]=1
    X[0,level-1]=lam
    Y=mm(prime,(b*np.eye(level,dtype=np.int64)-a*X)%prime,
         np.diag([pow(Q,-j,prime) for j in range(level)]))
    roots=[pow(x,-1,prime)*pow(Q,i,prime)%prime for i in range(level)]
    H=np.array([[pow(r,j,prime) for j in range(level)] for r in roots],dtype=np.int64)
    Hdual=np.array([[pow(r,-j,prime) for j in range(level)] for r in roots],dtype=np.int64)
    d=[1]
    for j in range(1,level):d.append(d[-1]*(b-a*roots[j])%prime)
    A=mm(prime,inverse_mod(H,prime),np.diag(d))
    weights=[pow(a-b*pow(r,-1,prime),-1,prime) for r in roots]
    J=mm(prime,H.T,np.diag(weights),Hdual)*pow(level,-1,prime)%prime
    c=-pow(level*x*Q,-1,prime)
    for s in range(1,level-1):c=c*(b-a*pow(x,-1,prime)*pow(Q,s,prime))%prime
    return X,Y,A,J,c%prime


def endpoint_source_case(level,kind):
    prime,generator,q=field(level);Q=q*q%prime
    x=generator if kind=='generic' else pow(q,level-1,prime)
    a=x;b=generator;phi=(pow(b,level,prime)-1)%prime
    y,psi,Jactual,g=dual_data(level,prime,q,x,phi)
    X,Y,A,J,c=endpoint_frame(level,prime,Q,x,a,b)
    XX,YY,AA,JJ,cc=endpoint_frame(level,prime,Q,y,b,a)
    E,F,K=semicyclic(level,prime,q,x,phi)
    assert np.array_equal(mm(prime,X,A),mm(prime,A,inverse_mod(K,prime)))
    assert np.array_equal(mm(prime,Y,A),mm(prime,A,F))
    vacuum=np.zeros(level,dtype=np.int64);vacuum[0]=1
    transported_unit=mm(prime,inverse_mod(A,prime),vacuum[:,None])
    assert not np.any(mm(prime,(F+a*inverse_mod(K,prime)-b*np.eye(level,dtype=np.int64))%prime,
                         transported_unit))
    assert np.array_equal(mm(prime,inverse_mod(X,prime).T,J),mm(prime,J,XX))
    assert np.array_equal(mm(prime,-mm(prime,inverse_mod(X,prime),Y).T%prime,J),mm(prime,J,YY))
    assert np.array_equal(mm(prime,inverse_mod(J.T,prime),JJ),-inverse_mod(X,prime)%prime)
    assert cc==-pow(x,level,prime)*c%prime
    assert np.array_equal(mm(prime,A.T,J,AA),Jactual*c%prime)
    assert int(J[0,0])==-pow(a,level-1,prime)*pow(x,-level,prime)*pow(phi,-1,prime)%prime
    assert np.array_equal(mm(prime,inverse_mod((J*pow(c,-1,prime)%prime).T,prime),
                              JJ*pow(cc,-1,prime)%prime),matrix_power(X,level-1,prime))
    # Evaluate the canceled whole cap at b=1, without evaluating its singular factors.
    d=[1]
    for j in range(1,level):d.append(d[-1]*(1-pow(Q,j,prime))%prime)
    whole=np.zeros((level,level),dtype=np.int64)
    c0=pow(x*(1-Q),-1,prime)
    assert -pow(x*c0,-1,prime)%prime==(Q-1)%prime
    whole[level-1,0]=c0
    for j in range(1,level):
        value=d[level-1-j]
        for s in range(1,j):value=value*x*(1-pow(Q,s+1,prime))%prime
        whole[level-1-j,j]=value*pow(level,-1,prime)%prime
    assert np.array_equal(whole,Jactual*c0%prime) and determinant(whole,prime)
    dd=[1]
    for j in range(1,level):dd.append(dd[-1]*x*(1-pow(Q,j+1,prime))%prime)
    assert all(dd[:-1]) and dd[-1]==0
    lost=np.diag(dd)
    assert rank(lost,prime)==level-1 and np.any(whole[:,level-1])
    first_normal=-pow(x,level-1,prime)
    for r in range(2,level):first_normal=first_normal*(1-pow(Q,r,prime))%prime
    pole=-pow(x,-1,prime)
    assert first_normal%prime
    assert first_normal*pole*pow(level,-1,prime)%prime==int(whole[0,level-1])
    return {'level':level,'color':kind,'prime':prime,
            'endpoint_trace_dual_intertwines_the_inverse_affine_character':True,
            'finite_factorial_scalar_matches_the_actual_dual_frame':True,
            'endpoint_unit_is_transported_as_the_actual_factorial_vector':True,
            'unit_cap_has_explicit_nonzero_normal_residue':True,
            'source_normalization_fixes_exact_actual_pivot':True,
            'whole_cap_regular_and_full_rank_at_phi_zero':True,
            'dual_endpoint_frame_loses_one_direction_at_the_wall':True,
            'retained_first_normal_coefficient_recovers_that_direction':True}


def endpoint_module(level,prime,Q,lam,a,b):
    X=np.zeros((level,level),dtype=np.int64)
    for j in range(level-1):X[j+1,j]=1
    X[0,level-1]=lam%prime
    Y=mm(prime,(b*np.eye(level,dtype=np.int64)-a*X)%prime,
         np.diag([pow(Q,-j,prime) for j in range(level)]))
    return X,Y


def pointed_fusion(level,prime,Q,left,right):
    X,Y=left;x,y=right;eye=np.eye(level,dtype=np.int64)
    totalX=np.kron(X,x)%prime
    relX=(np.kron(X,eye)+np.kron(Y,inverse_mod(y,prime)))%prime
    unit=np.zeros(level**2,dtype=np.int64);unit[0]=1
    relative=[unit]
    for _ in range(1,level):relative.append(mm(prime,relX,relative[-1][:,None])[:,0])
    columns=[]
    for a in range(level):
        for vector in relative:
            v=vector.copy()
            for _ in range(a):v=mm(prime,totalX,v[:,None])[:,0]
            columns.append(v)
    C=np.column_stack(columns)
    assert determinant(C,prime)
    return C


def triangle_pairing_case(level):
    prime,generator,q=field(level);Q=q*q%prime
    x1,x2=generator,pow(generator,3,prime)
    lam1,lam2=pow(x1,-level,prime),pow(x2,-level,prime)
    a=2
    c=next(v for v in range(3,prime) if (pow(v,level,prime)-lam2*pow(a,level,prime))%prime)
    d=next(v for v in range(4,prime)
           if (pow(v,level,prime)-lam1*pow(c,level,prime))%prime
           and (pow(v,level,prime)-lam1*lam2*pow(a,level,prime))%prime)
    X1,Y1,_,J1,c1=endpoint_frame(level,prime,Q,x1,c,d)
    X2,Y2,_,J2,c2=endpoint_frame(level,prime,Q,x2,a,c)
    _,_,_,JT,ct=endpoint_frame(level,prime,Q,x1*x2%prime,a,d)
    X2d,Y2d,_,_,_=endpoint_frame(level,prime,Q,pow(x2*Q,-1,prime),c,a)
    X1d,Y1d,_,_,_=endpoint_frame(level,prime,Q,pow(x1*Q,-1,prime),d,c)
    C=pointed_fusion(level,prime,Q,(X1,Y1),(X2,Y2))
    Cr=pointed_fusion(level,prime,Q,(X2d,Y2d),(X1d,Y1d))
    flip=np.zeros_like(C)
    for i,j in product(range(level),repeat=2):flip[j*level+i,i*level+j]=1
    J1=J1*pow(c1,-1,prime)%prime;J2=J2*pow(c2,-1,prime)%prime;JT=JT*pow(ct,-1,prime)%prime
    paired=mm(prime,C.T,np.kron(J1,J2),flip,Cr)
    reduced=mm(prime,np.kron(inverse_mod(JT,prime),np.eye(level,dtype=np.int64)),paired)
    face=np.einsum('iaib->ab',reduced.reshape((level,)*4))*pow(level,-1,prime)%prime
    assert determinant(face,prime)
    assert np.array_equal(paired,np.kron(JT,face)%prime)
    mu1=(pow(d,level,prime)-lam1*pow(c,level,prime))%prime
    mu2=(pow(c,level,prime)-lam2*pow(a,level,prime))%prime
    mut=(mu1+lam1*mu2)%prime
    rel_lam=mut*pow(mu2,-1,prime)%prime
    rel_mu=-mu1*lam2*pow(mu2,-1,prime)%prime
    RX,RY=endpoint_module(level,prime,Q,rel_lam,c*pow(a,-1,prime)%prime,d*pow(a,-1,prime)%prime)
    SX,SY=endpoint_module(level,prime,Q,-rel_lam*pow(rel_mu,-1,prime)%prime,
                          c*pow(d,-1,prime)%prime,a*pow(d,-1,prime)%prime)
    A=-mm(prime,inverse_mod(RY,prime),RX)%prime
    B=Q*inverse_mod(RY,prime)%prime
    assert np.array_equal(mm(prime,A.T,face),mm(prime,face,SX))
    assert np.array_equal(mm(prime,B.T,face),mm(prime,face,SY))
    return {'level':level,'prime':prime,'face_pairing_factors_exactly_from_endpoint_and_total_caps':True,
            'face_pairing_is_invertible_with_scalar_fixed':True,
            'face_pairing_intertwines_the_reversed_relative_shape_algebra':True,
            'reversed_unit_transports_to_nonconstant_dual_vector':bool(np.any(face[1:,0]))}


def affine_source_case(level):
    prime,generator,q=field(level);Q=q*q%prime;Y=generator
    U=pow(Y,level,prime)
    theta=next(a for a in range(2,prime) if pow(a,level,prime) not in (1,pow(U,-1,prime)))
    C=pow(theta,level,prime);V=(1-U*C)*pow(1-U,-1,prime)%prime
    eye=np.repeat(np.eye(2,dtype=np.int64)[None,:,:],level,axis=0)
    B,D,_,p=matrices(level,Q,Y,theta,0,prime)
    Bd,_,_,_=matrices(level,Q,Q*Y%prime,theta,0,prime)
    Bs,Ds,Bds=dual_batch(B,prime),dual_batch(D,prime),dual_batch(Bd,prime)
    assert np.array_equal(mul(Bs.transpose(0,2,1),B,prime),eye)
    assert np.array_equal(mul(np.roll(Ds,-1,axis=0),Bs,prime),mul(Bds,Ds,prime))
    expected=eye.copy()
    for j in range(level):
        a,b=int(B[j,0,0]),int(B[j,0,1])
        expected[j,0,0]=pow(a,-1,prime)
        expected[j,1,0]=-b*pow(a,-1,prime)%prime
    assert np.array_equal(Bs,expected) and np.any(Bs[:,1,0])
    wrong=Bs.copy();wrong[:,1,0]=0
    assert not np.array_equal(mul(wrong.transpose(0,2,1),B,prime),eye)
    dual_norm=eye.copy()
    for r in range(level):
        _,Dr,_,_=matrices(level,Q,Y*pow(Q,r,prime)%prime,theta,0,prime)
        dual_norm=mul(dual_batch(Dr,prime),dual_norm,prime)
    assert np.array_equal(dual_norm,eye*pow(V,-1,prime)%prime)
    loop=eye.copy();dual_loop=eye.copy()
    for cut in range(level):
        H=(1-Q*Y*theta*pow(Q,cut,prime))%prime
        J=eye.copy();J[:,1,1]=H;J[cut,0,1]=-U*C%prime
        Js=dual_batch(J,prime)
        loop=mul(J,loop,prime);dual_loop=mul(Js,dual_loop,prime)
    assert np.array_equal(dual_loop,dual_batch(loop,prime))
    assert np.array_equal(mul(dual_loop.transpose(0,2,1),loop,prime),eye)
    assert np.any(dual_loop[:,1,0])
    return {'level':level,'prime':prime,'source_meridian_norm':V,
            'dual_source_meridian_norm':pow(V,-1,prime),
            'dual_two_direction_extension_is_flat':True,
            'off_diagonal_co_source_is_nonzero_and_necessary':True,
            'full_peripheral_norm_cancels_on_an_interior_dual_pair':True,
            'non_scalar_raw_cut_loop_and_dual_loop_pair_exactly':True}


def reversed_triangle_case(level):
    prime,generator,q=field(level);Q=q*q%prime
    x1,x2=generator,pow(generator,3,prime)
    phi1=2
    phi2=next(v for v in range(3,prime) if (phi1+pow(x1,-level,prime)*v)%prime)
    first=semicyclic(level,prime,q,x1,phi1)
    second=semicyclic(level,prime,q,x2,phi2)
    X1,Y1=inverse_mod(first[2],prime),first[1]
    X2,Y2=inverse_mod(second[2],prime),second[1]
    eye=np.eye(level,dtype=np.int64)
    A,B,C,D=np.kron(X1,eye),np.kron(Y1,eye),np.kron(eye,X2),np.kron(eye,Y2)
    relX=(A+mm(prime,B,inverse_mod(D,prime)))%prime
    relY=-mm(prime,B,inverse_mod(D,prime),C)%prime
    dx2,dy2=inverse_mod(X2,prime).T,-mm(prime,inverse_mod(X2,prime),Y2).T%prime
    dx1,dy1=inverse_mod(X1,prime).T,-mm(prime,inverse_mod(X1,prime),Y1).T%prime
    AA,BB,CC,DD=np.kron(dx2,eye),np.kron(dy2,eye),np.kron(eye,dx1),np.kron(eye,dy1)
    reverseX=(AA+mm(prime,BB,inverse_mod(DD,prime)))%prime
    reverseY=-mm(prime,BB,inverse_mod(DD,prime),CC)%prime
    flip=np.zeros((level**2,level**2),dtype=np.int64)
    for a,b in product(range(level),repeat=2):flip[b*level+a,a*level+b]=1
    pulledX=mm(prime,flip,reverseX,flip).T
    pulledY=mm(prime,flip,reverseY,flip).T
    assert np.array_equal(pulledX,-mm(prime,inverse_mod(relY,prime),relX)%prime)
    assert np.array_equal(pulledY,Q*inverse_mod(relY,prime)%prime)
    lam=int(matrix_power(relX,level,prime)[0,0]);mu=int(matrix_power(relY,level,prime)[0,0])
    I=np.eye(level**2,dtype=np.int64)
    assert np.array_equal(matrix_power(reverseX,level,prime),I*(-lam*pow(mu,-1,prime)%prime)%prime)
    assert np.array_equal(matrix_power(reverseY,level,prime),I*pow(mu,-1,prime)%prime)
    return {'level':level,'prime':prime,'reversed_triangle_operators_include_exact_Q_and_transpose':True,
            'central_shape_change_is_minus_lambda_over_mu_and_inverse_mu':True}


def linking_case(level,leaves):
    prime,_,_=field(level)
    states=list(product(range(level),repeat=leaves))
    carries=[sum(state)//level for state in states]
    basis=[(i,a) for i,k in enumerate(carries) for a in range(k)]
    index={label:j for j,label in enumerate(basis)}
    size=len(basis)
    pairing=np.zeros((size,size),dtype=np.int64)
    epsilon=np.zeros_like(pairing)
    for row,(i,a) in enumerate(basis):
        pairing[row,index[i,carries[i]-1-a]]=1
        if a+1<carries[i]:epsilon[index[i,a+1],row]=1
    assert rank(pairing,prime)==size and determinant(pairing,prime)
    assert np.array_equal(mm(prime,epsilon.T,pairing),mm(prime,pairing,epsilon))
    socle=[index[i,k-1] for i,k in enumerate(carries) if k]
    residual=[index[i,0] for i,k in enumerate(carries) if k]
    assert np.array_equal(pairing[np.ix_(socle,residual)],np.eye(len(socle),dtype=np.int64))
    assert size==(leaves-1)*(level-1)*level**(leaves-1)//2
    assert len(socle)==level**leaves-comb(level+leaves-1,leaves)
    return {'level':level,'leaves':leaves,'linking_length':size,'lost_fiber_dimension':len(socle),
            'perfect_R_balanced_residue_linking_form':True,
            'Tor_source_and_dual_residual_fiber_pair_perfectly':True,
            'largest_normal_jet_in_linking_pairing':max(carries)-1}


def main():
    levels=(2,3,4,5,6,8,9,10,12)
    turns=[turns_case(n,kind,phi) for n in levels for kind in ('generic','Kashaev') for phi in (0,2)]
    print(f'{len(turns)} semicyclic duality and turn cases passed',flush=True)
    cuts=[cut_case(n,kind) for n in (2,3,4,5,6) for kind in ('generic','Kashaev')]
    assert any(p['omitting_pivotal_turn_changes_cut'] for case in cuts for p in case['periods'])
    print(f'{sum(len(case["periods"]) for case in cuts)} original scalar cuts from explicit caps passed',flush=True)
    sources=[affine_source_case(n) for n in levels]
    print(f'{len(sources)} flat affine source/co-source pairs passed',flush=True)
    endpoint_caps=[endpoint_source_case(n,kind) for n in levels for kind in ('generic','Kashaev')]
    print(f'{len(endpoint_caps)} pointed cyclic endpoint caps and their retained wall source passed',flush=True)
    triangles=[reversed_triangle_case(n) for n in levels]
    print(f'{len(triangles)} reversed triangle algebra cases passed',flush=True)
    faces=[triangle_pairing_case(n) for n in levels]
    assert any(f['reversed_unit_transports_to_nonconstant_dual_vector'] for f in faces)
    print(f'{len(faces)} actual-source induced triangle face pairings passed',flush=True)
    links=[linking_case(n,b) for n,b in [(2,b) for b in range(2,7)]+[(3,b) for b in range(2,5)]+[(4,2),(4,3)]]
    result={'scope':'Actual oriented duality, forced cap degeneration, and perfect duality of the retained carry source; no full geometric triangulation assignment or regulator-norm theorem.',
            'semicyclic_duality':turns,'actual_cut_closures':cuts,
            'affine_source_duality':sources,'endpoint_source_caps':endpoint_caps,
            'reversed_triangle_algebras':triangles,
            'induced_triangle_face_pairings':faces,
            'source_linking_forms':links}
    Path(__file__).with_name('relative_pivotal_duality_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(links)} perfect source linking forms',flush=True)


if __name__=='__main__':main()
