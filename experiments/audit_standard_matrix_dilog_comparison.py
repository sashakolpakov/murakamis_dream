#!/usr/bin/env python3
"""Pointed fusion versus the literature basic and charged matrix kernel.

All four face frames, the input flip, the pointing scalar and the
Heisenberg phase of root translations are retained. No global charged
invariant, actual geometric cycle or volume estimate is asserted.
"""

from itertools import product
from functools import cache
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod
from audit_cyclic_steinberg_lattice import determinant
from audit_regular_holonomy_braiding import mm
from audit_relative_pivotal_duality import endpoint_module,pointed_fusion


def parameters(N):
    for multiple in range(10,500):
        p=12*N*multiple+1
        if not sp.isprime(p):continue
        generator=int(sp.primitive_root(p));Q=pow(generator,(p-1)//N,p)
        roots={pow(a,N,p):a for a in range(1,p)}
        for s,alpha in roots.items():
            if s==1 or (1-s)%p not in roots:continue
            for t,beta in roots.items():
                if t==1 or s*t%p==1:continue
                if (1-t)%p not in roots or (1-s*t)%p not in roots:continue
                a_s=roots[(1-s)%p];a_t=roots[(1-t)%p];a_st=roots[(1-s*t)%p]
                gamma=a_st*pow(a_t,-1,p)%p;v=a_s*pow(a_st,-1,p)%p
                return p,Q,s,t,alpha,beta,gamma,a_s,a_t,a_st,v
    raise AssertionError('no nondegenerate compatible Fermat chart')


def primitive(N,p,Q,z,a):
    values=[1]
    for j in range(1,N):values.append(values[-1]*(1-z*pow(Q,j,p))*pow(a,-1,p)%p)
    assert values[-1]*(1-z)*pow(a,-1,p)%p==1
    return np.array(values,dtype=np.int64)


def omega(N,p,Q,u,v):
    values=[1]
    for j in range(1,N):values.append(values[-1]*v*pow(1-u*pow(Q,j,p),-1,p)%p)
    assert values[-1]*v*pow(1-u,-1,p)%p==1
    return np.array(values,dtype=np.int64)


@cache
def gauss_root(N,p,Q):
    value=-pow(int(sp.primitive_root(p)),(p-1)//(2*N),p)%p
    assert value*value%p==Q and pow(value,N,p)==pow(-1,N-1,p)
    return value


def basic_kernel(N,p,Q,u,v):
    assert (pow(u,N,p)+pow(v,N,p))%p==1
    W=omega(N,p,Q,u,v);root=gauss_root(N,p,Q)
    L=np.zeros((N*N,N*N),dtype=np.int64)
    for i,j,k in product(range(N),repeat=3):
        ell=(i+j)%N
        L[i*N+j,k*N+ell]=pow(Q,k*j,p)*pow(root,k*k,p)*int(W[(i-k)%N])%p
    return L


def evaluation(N,p,Q,z):
    return np.array([[pow(z*pow(Q,i,p)%p,j,p) for j in range(N)] for i in range(N)],dtype=np.int64)


def weyl_apply(matrix,N,p,Q,a,b):
    i,j,k,ell=np.indices((N,)*4)
    tensor=matrix.reshape((N,)*4)
    permuted=tensor[(i+a)%N,(j-a)%N,k,ell]
    phases=np.array([pow(Q,r,p) for r in range(N)],dtype=np.int64)
    return (permuted*phases[(b*i+(a-b)*k)%N]%p).reshape(N*N,N*N)


def normal_chart(N,p,Q,u,v):
    z=pow(u,N,p);a=(1-z)%p;b=z;gamma=pow(u,-1,p)
    kappa=(1-z)*pow(N*(1-u),-1,p)%p
    factorial=[1]
    for i in range(1,N):factorial.append(factorial[-1]*(1-pow(Q,i,p))%p)
    W=omega(N,p,Q,u,v)
    D=primitive(N,p,pow(Q,-1,p),u,v)
    D=np.array([pow(int(value),-1,p) for value in D],dtype=np.int64)
    predicted=np.zeros((N*N,N*N),dtype=np.int64)
    direct=np.zeros_like(predicted)
    for i,j in product(range(N),repeat=2):
        ell=(i+j)%N;carry=(i+j)//N
        row_factor=(kappa*factorial[i]*factorial[j]*pow(factorial[ell],-1,p)
                    *pow(gamma,ell-i,p)*pow(v,-i,p))%p
        terms=[];value=1;valuation=0
        for degree in range(N):
            if degree:
                pn=pow(Q,i+j+degree,p);pd=pow(Q,j+degree,p)
                un=(a+b)%p if pn==1 else (1-pn)%p
                ud=b if pd==1 else (1-pd)%p
                value=value*un*pow(ud,-1,p)%p
                valuation+=int(pn==1)-int(pd==1)
            assert valuation+carry>=0
            terms.append(value if valuation+carry==0 else 0)
        for k in range(N):
            predicted[i*N+j,ell*N+k]=(row_factor*int(D[k])*pow(Q,j*k,p)*int(W[(i-k)%N]))%p
            direct[i*N+j,ell*N+k]=(pow(N*b,carry,p)*pow(N,-1,p)
                *sum(terms[d]*pow(gamma,-d,p)*pow(Q,-k*d,p) for d in range(N)))%p
    assert np.array_equal(predicted,direct)
    determinant_phase=1 if N%2 else pow(-1,N//2,p)
    assert determinant(direct,p)==determinant_phase
    image=direct@np.ones(N*N,dtype=np.int64)%p
    assert np.array_equal(image,np.array([int(i+j<N) for i,j in product(range(N),repeat=2)]))
    return {'normal_shape':z,'normal_kernel_regular_and_nondegenerate':True,
            'fractional_face_poles_cancel_to_exact_integer_carry':True,
            'independent_valuation_and_standard_kernel_constructions_match':True,
            'row_scaled_source_frame_has_exact_nonzero_determinant':True,
            'row_scaled_determinant_phase':determinant_phase}


def case(N):
    p,Q,s,t,alpha,beta,gamma,a_s,a_t,a_st,v=parameters(N)
    u=alpha*pow(gamma,-1,p)%p;eta=alpha*beta%p;half=(N+1)//2
    gauss=gauss_root(N,p,Q);determinant_phase=1 if N%2 else pow(-1,N//2,p)
    phi_s=primitive(N,p,Q,alpha,a_s);phi_t=primitive(N,p,Q,beta,a_t)
    phi_st=primitive(N,p,Q,eta,a_st)
    D=primitive(N,p,pow(Q,-1,p),pow(gamma,-1,p),beta*v%p)
    D=np.array([pow(int(a),-1,p) for a in D],dtype=np.int64)
    source_rel=D*np.array([pow(gauss,-k*k,p) for k in range(N)],dtype=np.int64)%p
    C=pointed_fusion(N,p,Q,endpoint_module(N,p,Q,s,1,1),endpoint_module(N,p,Q,t,1,1))
    Hout=np.kron(evaluation(N,p,Q,alpha),evaluation(N,p,Q,beta))%p
    Hin=np.kron(evaluation(N,p,Q,eta),evaluation(N,p,Q,gamma))%p
    Ceval=mm(p,Hout,C,inverse_mod(Hin,p))
    W=omega(N,p,Q,u,v);L=basic_kernel(N,p,Q,u,v)
    assert determinant(L,p)
    flip=np.zeros_like(L)
    for ell,k in product(range(N),repeat=2):flip[k*N+ell,ell*N+k]=1
    outer=np.kron(phi_s,phi_t)%p
    source=np.kron(source_rel,np.array([pow(int(a),-1,p) for a in phi_st],dtype=np.int64))%p
    ratio=1;terms=[1]
    for b in range(1,N):
        ratio=ratio*pow(gamma,-1,p)*(1-eta*pow(Q,b,p))*pow(1-beta*pow(Q,b,p),-1,p)%p
        terms.append(ratio)
    kappa=sum(terms)*pow(N,-1,p)%p
    assert kappa
    proposed=mm(p,outer[:,None]*L%p,source[:,None]*flip%p)*kappa%p
    assert np.array_equal(Ceval,proposed)
    # Both the constant source and its actual transformed pointing are checked.
    ones=np.ones(N*N,dtype=np.int64)
    assert np.array_equal(Ceval@ones%p,ones)
    pointed=source.copy()
    assert np.array_equal(L@pointed%p*kappa%p,np.array([pow(int(a),-1,p) for a in outer],dtype=np.int64))
    # The Gaussian-circulant proof of invertibility is independent of the fusion map.
    gaussian=np.array([pow(gauss,n*n,p)*int(W[n])%p for n in range(N)],dtype=np.int64)
    transform=np.array([sum(int(gaussian[n])*pow(Q,-r*n,p) for n in range(N))%p for r in range(N)],dtype=np.int64)
    assert all(transform)
    for r in range(N):
        assert int(transform[r])==(u+v*pow(gauss,-1,p)*pow(Q,1-r,p))*int(transform[(r-1)%N])%p
    root_checks=0
    for a,b in product(range(N),repeat=2):
        changed=basic_kernel(N,p,Q,u*pow(Q,a,p)%p,v*pow(Q,b,p)%p)
        assert np.array_equal(changed*int(W[a])%p,weyl_apply(L,N,p,Q,a,b))
        root_checks+=1
    # The g(u) normalization is checked on its Nth-power cover, with roots retained.
    def g_power(z):
        value=1
        for r in range(1,N):value=value*pow(1-z*pow(Q,-r,p),r,p)%p
        return value
    for a in range(N):
        assert g_power(u*pow(Q,a,p)%p)*pow(g_power(u),-1,p)%p==pow(int(W[a]),N,p)
    h_power=g_power(u)*pow(g_power(1),-1,p)%p
    assert determinant(L,p)*pow(h_power,N,p)%p==determinant_phase
    S=N*(N-1)//2
    assert determinant(Ceval,p)==determinant_phase*pow(t*pow(1-t,-1,p)%p,S,p)%p
    Fs,Ft,Fst,FD=(int(np.prod(array,dtype=object))%p for array in (phi_s,phi_t,phi_st,D))
    scalar_power=pow(kappa,N*N,p)*pow(h_power,-N,p)%p
    comparison_phase=pow(-1,(N-1)//2,p) if N%2 else 1
    expected_power=(comparison_phase*pow(t*pow(1-t,-1,p)%p,S,p)
                    *pow(Fst*pow(Fs*Ft*FD,-1,p)%p,N,p))%p
    assert scalar_power==expected_power
    normal=normal_chart(N,p,Q,u,v)
    AB=weyl_apply(weyl_apply(L,N,p,Q,0,1),N,p,Q,1,0)
    BA=weyl_apply(weyl_apply(L,N,p,Q,1,0),N,p,Q,0,1)
    assert np.array_equal(AB,BA*Q%p)
    charged_checks=0
    for epsilon,c0,c1 in (product((1,-1),range(3),range(3)) if N%2 else []):
        a=(-epsilon*half*c0)%N;b=(epsilon*half*c1)%N
        uc=u*pow(Q,a,p)%p;vc=v*pow(Q,b,p)%p
        scalar=pow(uc,-((N-1)//2)*c1,p)*pow(vc,-((N-1)//2)*c0,p)%p
        shifted=basic_kernel(N,p,Q,uc,vc)*int(W[a])%p
        literal=shifted if epsilon==1 else inverse_mod(shifted,p)
        transported=weyl_apply(L,N,p,Q,a,b)
        transported=transported if epsilon==1 else inverse_mod(transported,p)
        assert np.array_equal(literal*scalar%p,transported*scalar%p)
        for r0,r1 in ((1,0),(0,1),(-1,2)):
            lifted=pow(uc,-((N-1)//2)*(c1+N*r1),p)*pow(vc,-((N-1)//2)*(c0+N*r0),p)%p
            central=(pow(pow(u,N,p),-((N-1)//2)*r1,p)
                     *pow(pow(v,N,p),-((N-1)//2)*r0,p))%p
            assert lifted==scalar*central%p
        charged_checks+=1
    return {'level':N,'prime':p,'s':s,'t':t,'pointing_scalar_kappa':kappa,
            'actual_pointed_fusion_equals_four_face_kernel':True,
            'kernel_is_the_literal_literature_definition_at_odd_level':bool(N%2),
            'input_relative_total_flip_and_quadratic_phase_retained':True,
            'standard_source_vector_is_transported_exactly':True,
            'resetting_the_standard_source_to_the_unit_changes_it':not np.array_equal(pointed,ones),
            'gaussian_fourier_recurrence_proves_kernel_invertible':True,
            'root_weyl_translations':root_checks,'heisenberg_generator_commutator_is_Q':True,
            'cyclic_g_normalization_Nth_powers_match_the_compatible_root_cover':True,
            'normalized_kernel_has_exact_determinant_phase':determinant_phase,
            'pointing_scalar_normalization_N_squared_power_is_explicit':True,
            'integer_charge_lifts_retain_their_full_central_multiplier':True,
            'normal_source_chart':normal,
            'charged_positive_and_negative_definitions_checked':charged_checks}


def main():
    records=[]
    for N in (2,3,4,5,6,7,8,9,10,11,12,15):
        records.append(case(N));print(f'N={N}: exact fusion/kernel comparison and root transport passed'+(' (literature charges checked)' if N%2 else ' (even Gaussian phase retained)'),flush=True)
    assert all(r['resetting_the_standard_source_to_the_unit_changes_it'] for r in records)
    result={'scope':'All-level exact expression for the existing fusion map; at odd levels it is the literal literature basic/charged kernel. Even levels retain their Gaussian/determinant phase without asserting an even charged definition. No global charged move/source or regulator-norm theorem.',
            'comparisons':records}
    Path(__file__).with_name('standard_matrix_dilog_comparison_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
