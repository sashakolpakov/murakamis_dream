#!/usr/bin/env python3
"""Four root-cyclic tetrahedron atoms for the actual holonomy crossing.

Each atom changes the splitting center, so its matrix is evaluated in
the transported frame. Raw scalar and determinant data are kept exactly;
normalization roots are specified by the accompanying uniform proof.
No geometric knot character or volume asymptotic is asserted.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod, matrix_power
from audit_carry_recoupling_lattice import carry_crossings
from audit_cyclic_steinberg_lattice import determinant
from audit_regular_holonomy_braiding import mm


def parameters(level,kind):
    for multiple in range(20,600):
        prime=4*level*multiple+1
        if not sp.isprime(prime):continue
        generator=int(sp.primitive_root(prime))
        q=pow(generator,(prime-1)//(2*level),prime)
        roots={pow(a,level,prime):a for a in range(1,prime)}
        colors=[pow(q,level-1,prime)] if kind=='Kashaev' else [pow(generator,j,prime) for j in range(1,30)]
        for x in colors:
            k=pow(x,level,prime)
            if kind=='generic' and k*k%prime==1:continue
            for r,a in roots.items():
                d1=(1+k*r)%prime
                if not d1 or d1 not in roots:continue
                d2=(1-r*pow(k*d1,-1,prime))%prime
                if not d2 or d2 not in roots:continue
                nu1=roots[d1]
                nu2=pow(nu1,-1,prime) if kind=='Kashaev' else roots[d2]
                assert pow(nu2,level,prime)==d2
                return prime,q,x,a,nu1,nu2
    raise AssertionError('no diagnostic root cover found')


def torus(level,prime,Q,s1,s2,z1,z2):
    clock=np.diag([pow(Q,a,prime) for a in range(level)]).astype(np.int64)
    shift=np.zeros((level,level),dtype=np.int64)
    for a in range(level):shift[(a+1)%level,a]=1
    I=np.eye(level,dtype=np.int64)
    return [np.kron(s1*clock%prime,I)%prime,np.kron(I,s2*clock%prime)%prime,
            np.kron(z1*shift%prime,I)%prime,np.kron(I,z2*shift%prime)%prime]


def cyclic_atom(level,prime,Q,m,mu,nu):
    size=len(m);I=np.eye(size,dtype=np.int64)
    assert np.array_equal(matrix_power(m,level,prime),I*pow(mu,level,prime)%prime)
    assert (pow(mu,level,prime)+pow(nu,level,prime))%prime==1
    values=[1]
    for j in range(1,level):
        values.append(values[-1]*nu*pow(1-mu*pow(Q,j-1,prime),-1,prime)%prime)
    assert values[-1]*nu*pow(1-mu*pow(Q,level-1,prime),-1,prime)%prime==1
    C=np.zeros_like(I);power=I.copy()
    for ell in range(level):
        coefficient=sum(values[j]*pow(Q,-j*ell,prime) for j in range(level))%prime
        C=(C+coefficient*power)%prime
        power=mm(prime,power,m*pow(mu,-1,prime)%prime)
    C=C*pow(level,-1,prime)%prime
    F=1
    for value in values:F=F*value%prime
    assert size%level==0
    assert determinant(C,prime)==pow(F,size//level,prime)
    return C,F


def case(level,kind):
    prime,q,x,a,nu1,nu2=parameters(level,kind);Q=q*q%prime;k=pow(x,level,prime);r=pow(a,level,prime)
    I=np.eye(level*level,dtype=np.int64)
    cartan=np.diag([pow(Q,i*j,prime) for i,j in product(range(level),repeat=2)]).astype(np.int64)
    source_roots=(1,1,1,a);roots=[1,1,pow(x,-1,prime),a*pow(x,-1,prime)%prime]
    raw=cartan.copy();records=[];Fs=[]
    nus=[nu1,nu2,pow(nu1,-1,prime),pow(nu2,-1,prime)]
    mus=[q*x*a%prime,a*pow(x*nu1,-1,prime)%prime,
         Q*x*a*pow(nu1,-1,prime)%prime,q*a*pow(x*nu1*nu2,-1,prime)%prime]
    arguments=[(-1,-Q*x%prime),(0,pow(x,-1,prime)),(0,Q*x%prime),(1,-pow(x,-1,prime)%prime)]
    for index,((b,c),mu,nu) in enumerate(zip(arguments,mus,nus)):
        S1,S2,Z1,Z2=torus(level,prime,Q,*roots)
        A=mm(prime,inverse_mod(Z1,prime),Z2)
        m=mm(prime,A,matrix_power(S1,b%level,prime)*pow(roots[0],b-b%level,prime)%prime)*c%prime
        # The exponent correction above retains S1^N when b=-1.
        C,F=cyclic_atom(level,prime,Q,m,mu,nu);Fs.append(F)
        updated=[roots[0]*pow(nu,-1,prime)%prime,roots[1]*nu%prime,
                 roots[2]*pow(nu,-b,prime)%prime,roots[3]]
        target=torus(level,prime,Q,*updated)
        for G,T,commutation in zip((S1,S2,Z1,Z2),target,(1,-1,b,0)):
            if commutation==1:transformed=mm(prime,G,inverse_mod((I-m)%prime,prime))
            elif commutation==-1:transformed=mm(prime,G,(I-pow(Q,-1,prime)*m)%prime)
            else:transformed=G
            assert np.array_equal(mm(prime,transformed,C),mm(prime,C,T))
        raw=mm(prime,raw,C);roots=updated
        records.append({'atom':index+1,'central_shape':pow(mu,level,prime),
                        'retained_norm_factor':pow(nu,level,prime),
                        'all_four_torus_generator_intertwinings_exact':True,
                        'raw_cycle_determinant':F})
    assert roots[0]==roots[1]==1
    assert roots[2]==nu1*nu2*pow(x,-1,prime)%prime and roots[3]==a*pow(x,-1,prime)%prime
    expected_phi1=(pow(k,-1,prime)+(1-pow(k,-2,prime))*r)%prime
    expected_phi2=r*pow(k,-1,prime)%prime
    assert pow(roots[2],level,prime)==expected_phi1 and pow(roots[3],level,prime)==expected_phi2
    Bs=np.array([pow(a,j,prime) for i,j in product(range(level),repeat=2)],dtype=np.int64)
    Bt=np.array([pow(roots[2],i,prime)*pow(roots[3],j,prime)%prime for i,j in product(range(level),repeat=2)],dtype=np.int64)
    standard=raw*np.array([pow(int(v),-1,prime) for v in Bs])[:,None]*Bt[None,:]%prime
    swap=np.zeros_like(I)
    for i,j in product(range(level),repeat=2):swap[j*level+i,i*level+j]=1
    checked=carry_crossings(level,prime,q,x,r*pow(k*level,-1,prime)%prime)[0]
    R=mm(prime,swap,checked);scalar=int(standard[0,0]);assert scalar
    assert np.array_equal(standard,R*scalar%prime)
    rhs=pow(nu1*nu2,level*level*(level-1)//2,prime)
    for F in Fs:rhs=rhs*pow(F,level,prime)%prime
    assert pow(scalar,level*level,prime)==rhs
    factors=[record['retained_norm_factor'] for record in records]
    assert factors[0]*factors[2]%prime==1 and factors[1]*factors[3]%prime==1
    return {'level':level,'color':kind,'prime':prime,'source_k':k,'source_ratio':r,
            'atoms':records,'raw_four_atom_crossing_scalar':scalar,
            'full_actual_semicyclic_crossing_matches_up_to_recorded_scalar':True,
            'exact_normalization_determinant_identity':True,
            'compatible_reciprocal_roots_restore_clock_centers':True,
            'final_F_centers':[expected_phi1,expected_phi2]}


def main():
    k,r,U=sp.symbols('k r U',nonzero=True)
    d1=1+k*r;d2=1-r/(k*d1)
    assert sp.cancel(d1*d2-(1+k*r-r/k))==0
    peripheral=[sp.cancel(d.subs(r,k)) for d in (d1,d2,1/d1,1/d2)]
    expected=[1+U,U/(1+U),1/(1+U),(1+U)/U]
    assert all(sp.cancel(a-b.subs(U,k*k))==0 for a,b in zip(peripheral,expected))
    complete_shapes=[sp.simplify(1-d.subs(U,1)) for d in expected]
    assert complete_shapes==[-1,sp.Rational(1,2),sp.Rational(1,2),-1]
    cases=[]
    for level in (2,3,4,5,6,8,9,10,12):
        for kind in ('generic','Kashaev'):
            cases.append(case(level,kind))
        print(f'N={level}: four transported cyclic atoms passed',flush=True)
    result={'scope':'Exact four cyclic-dilogarithm atom factorization with all root/normalization data retained; no geometric selected-period norm theorem.',
            'four_atom_cases':cases,
            'symbolic_peripheral_factors':[str(d) for d in expected],
            'complete_fixed_center_shapes':[str(z) for z in complete_shapes]}
    Path(__file__).with_name('four_cyclic_atoms_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(cases)} crossings, {4*len(cases)} atom intertwiners',flush=True)


if __name__=='__main__':main()
