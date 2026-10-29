#!/usr/bin/env python3
"""Root-cyclic pentagons with transported centers and full norm roots.

Raw finite matrices retain their scalar. Their determinant equations
specify the normalization line; the uniform proof fixes its phase on
the component anchored by zero coefficient tags.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod, matrix_power
from audit_cyclic_steinberg_lattice import determinant
from audit_four_cyclic_atoms import cyclic_atom
from audit_regular_holonomy_braiding import mm


def root_field(level,kind):
    for multiple in range(20,700):
        prime=4*level*multiple+1
        if not sp.isprime(prime):continue
        generator=int(sp.primitive_root(prime));q=pow(generator,(prime-1)//(2*level),prime)
        roots={pow(a,level,prime):a for a in range(1,prime)}
        for A,u in roots.items():
            first=(1-A if kind=='primitive' else 1+A)%prime
            if not first or first not in roots:continue
            for B,v in roots.items():
                second=(1-B if kind=='primitive' else 1+B)%prime
                third=(1-A+A*B if kind=='primitive' else 1+A+A*B)%prime
                if second and third and second in roots and third in roots:
                    return prime,q,u,v,roots[first],roots[second],roots[third]
    raise AssertionError('no nondegenerate diagnostic pentagon cover')


def scalar_ratio(left,right,prime):
    row,col=next(zip(*np.nonzero(right)))
    value=int(left[row,col])*pow(int(right[row,col]),-1,prime)%prime
    assert value and np.array_equal(left,right*value%prime)
    return value


def primitive_case(level):
    prime,q,x,y,nuA,nuB,nuH=root_field(level,'primitive');Q=q*q%prime
    X=np.diag([x*pow(Q,j,prime)%prime for j in range(level)]).astype(np.int64)
    Y=np.zeros_like(X)
    for j in range(level):Y[(j+1)%level,j]=y
    left1,Fb=cyclic_atom(level,prime,Q,Y,y,nuB)
    left2,Fh=cyclic_atom(level,prime,Q,X*nuB%prime,x*nuB%prime,nuH)
    right1,Fa=cyclic_atom(level,prime,Q,X,x,nuA)
    middle=-mm(prime,Y,X)*pow(nuA,-1,prime)%prime
    right2,Fm=cyclic_atom(level,prime,Q,middle,q*x*y*pow(nuA,-1,prime)%prime,nuH*pow(nuA,-1,prime)%prime)
    right3,Fl=cyclic_atom(level,prime,Q,Y*pow(nuH,-1,prime)%prime,
                          y*pow(nuH,-1,prime)%prime,nuA*nuB*pow(nuH,-1,prime)%prime)
    left=mm(prime,left1,left2);right=mm(prime,right1,right2,right3)
    scalar=scalar_ratio(left,right,prime)
    quotient=Fb*Fh*pow(Fa*Fm*Fl,-1,prime)%prime
    assert pow(scalar,level,prime)==quotient
    return {'level':level,'prime':prime,'raw_pentagon_scalar':scalar,
            'exact_cycle_determinant_ratio':quotient,
            'transported_rank_N_pentagon_exact_up_to_recorded_scalar':True,
            'negative_middle_monomial_uses_q_to_retain_all_parities':True}


def full_torus(level,prime,Q,z,s):
    shift=np.zeros((level,level),dtype=np.int64)
    for a in range(level):shift[(a+1)%level,a]=1
    clock=np.diag([pow(Q,a,prime) for a in range(level)]).astype(np.int64)
    eye=np.eye(level,dtype=np.int64);Z=[];S=[]
    for j in range(3):
        zz=np.array([[1]],dtype=np.int64);ss=zz.copy()
        for k in range(3):
            zz=np.kron(zz,z[j]*shift%prime if j==k else eye)%prime
            ss=np.kron(ss,s[j]*clock%prime if j==k else eye)%prime
        Z.append(zz);S.append(ss)
    return Z,S


def shear(level,i,j):
    states=list(product(range(level),repeat=3));index={state:k for k,state in enumerate(states)}
    C=np.zeros((level**3,level**3),dtype=np.int64)
    for col,state in enumerate(states):
        target=list(state);target[j]=(target[j]+target[i])%level
        C[index[tuple(target)],col]=1
    return C


def tetra_step(level,prime,q,z,s,i,j,tag,nu):
    Q=q*q%prime;beforeZ,beforeS=full_torus(level,prime,Q,z,s);C=shear(level,i,j)
    zz=z.copy();ss=s.copy();zz[i]=zz[i]*zz[j]%prime;ss[j]=ss[j]*pow(ss[i],-1,prime)%prime
    Z,S=full_torus(level,prime,Q,zz,ss)
    # Verify the shear in its actual transported clock/shift modules.
    for k in range(3):
        imageZ=mm(prime,beforeZ[i],beforeZ[j]) if k==i else beforeZ[k]
        imageS=mm(prime,inverse_mod(beforeS[i],prime),beforeS[j]) if k==j else beforeS[k]
        assert np.array_equal(mm(prime,imageZ,C),mm(prime,C,Z[k]))
        assert np.array_equal(mm(prime,imageS,C),mm(prime,C,S[k]))
    m=mm(prime,Z[i],inverse_mod(Z[j],prime),inverse_mod(S[j],prime))*(-Q*tag)%prime
    mu=q*tag*z[i]*s[i]*pow(s[j],-1,prime)%prime
    D,F=cyclic_atom(level,prime,Q,m,mu,nu)
    zz[j]=zz[j]*pow(nu,-1,prime)%prime
    ss[i]=ss[i]*pow(nu,-1,prime)%prime;ss[j]=ss[j]*nu%prime
    return mm(prime,C,inverse_mod(D,prime)),zz,ss,F


def tetra_case(level):
    prime,q,ua,vb,nuA,nuB,nuH=root_field(level,'tetra');Q=q*q%prime
    z=[2,3,5];s=[7,11,13]
    u=ua*s[1]*pow(z[0]*s[0],-1,prime)%prime
    v=vb*s[2]*pow(z[1]*s[1],-1,prime)%prime
    def run(word):
        zz=z.copy();ss=s.copy();value=np.eye(level**3,dtype=np.int64);factors=[]
        for i,j,tag,nu in word:
            T,zz,ss,F=tetra_step(level,prime,q,zz,ss,i,j,tag,nu)
            value=mm(prime,value,T);factors.append(F)
        return value,zz,ss,factors
    left,zl,sl,fl=run([(0,1,u,nuA),(0,2,u*v%prime,nuH*pow(nuA,-1,prime)%prime),
                       (1,2,v,nuA*nuB*pow(nuH,-1,prime)%prime)])
    right,zr,sr,fr=run([(1,2,v,nuB),(0,1,u,nuH)])
    assert zl==zr and sl==sr
    expected_z=[z[0]*z[1]*z[2]%prime,z[1]*z[2]*pow(nuH,-1,prime)%prime,z[2]*pow(nuB,-1,prime)%prime]
    expected_s=[s[0]*pow(nuH,-1,prime)%prime,s[1]*nuH*pow(s[0]*nuB,-1,prime)%prime,
                s[2]*nuB*pow(s[1],-1,prime)%prime]
    assert zl==expected_z and sl==expected_s
    scalar=scalar_ratio(left,right,prime)
    factor=1
    for F in fr:factor=factor*F%prime
    for F in fl:factor=factor*pow(F,-1,prime)%prime
    assert pow(scalar,level**3,prime)==pow(factor,level**2,prime)
    bare_left=mm(prime,shear(level,0,1),shear(level,0,2),shear(level,1,2))
    bare_right=mm(prime,shear(level,1,2),shear(level,0,1))
    assert np.array_equal(bare_left,bare_right)
    return {'level':level,'prime':prime,'raw_tetrahedral_scalar':scalar,
            'full_rank_N_cubed_determinant_identity':True,
            'stronger_single_cycle_determinant_identity':pow(scalar,level,prime)==factor,
            'same_final_shift_and_clock_roots':True,
            'all_five_shears_intertwine_their_transported_modules':True,
            'raw_three_to_two_matrix_identity_with_recorded_scalar':True,
            'source_coordinate_roots':[z,s],'final_coordinate_roots':[zl,sl]}


def main():
    primitive=[primitive_case(n) for n in (2,3,4,5,6,8,9,10,12)]
    print(f'transported primitive cyclic pentagons: {len(primitive)} passed',flush=True)
    tetra=[]
    for n in (2,3,4,5,6):
        tetra.append(tetra_case(n));print(f'N={n}: full tetrahedral three-to-two identity passed',flush=True)
    result={'scope':'Root-cyclic and shear/tetrahedral pentagons on compatible anchored root covers; no arbitrary global gluing or selected regulator-norm theorem.',
            'primitive_cyclic_pentagons':primitive,'tetrahedral_pentagons':tetra}
    Path(__file__).with_name('cyclic_tetrahedron_pentagon_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
