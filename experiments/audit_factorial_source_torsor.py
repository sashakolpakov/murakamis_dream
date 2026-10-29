#!/usr/bin/env python3
"""Flat factorial sources, cut-root transport and the actual ADO boundary.

Exact finite-field diagnostics at every tested parity. The generic cut
family is not declared to be a new knot invariant. No global geometric
source comparison or volume asymptotic is asserted.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np

from audit_actual_peripheral_fusion import inverse_mod
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_pointed_tetrahedron_gluing import shape_field, shape_module


def mul(left,right,prime):
    return np.matmul(left,right)%prime


def primitive(level,Q,h,prime):
    values=[1]
    for a in range(1,level):values.append(values[-1]*(1-pow(Q,a,prime)*h)%prime)
    return np.array(values,dtype=np.int64)


def matrices(level,Q,Y,theta,cut,prime):
    root=theta*pow(Q,cut,prime)%prime;h=Y*root%prime
    p=primitive(level,Q,h,prime)[[(a-cut)%level for a in range(level)]]
    U=pow(Y,level,prime);C=pow(theta,level,prime)
    internal=np.repeat(np.eye(2,dtype=np.int64)[None,:,:],level,axis=0)
    meridian=internal.copy();den=pow(1-Q*Y,-1,prime)
    for a in range(level):
        t=theta*pow(Q,a,prime)%prime
        internal[a,0,0]=(1-Q*Y*t)%prime
        internal[a,0,1]=U*C%prime if a==(cut-1)%level else 0
        meridian[a,0,0]=(1-Q*Y*t)*den%prime
        meridian[a,1,1]=(1-Q*Y*root)*den%prime
    G=np.repeat(np.eye(2,dtype=np.int64)[None,:,:],level,axis=0);G[:,0,1]=p
    return internal,meridian,G,p


def inverse_shear(G,prime):
    out=G.copy();out[:,0,1]=-out[:,0,1]%prime
    return out


def root_case(level):
    prime,q,(h,nu)=shape_field(level);Q=q*q%prime
    theta=next(a for a in range(2,prime) if pow(a,level,prime) not in (1,pow(h,level,prime)))
    Y=h*pow(theta,-1,prime)%prime;U=pow(Y,level,prime);C=pow(theta,level,prime)
    a0=1-U*C;V=a0*pow(1-U,-1,prime)%prime
    Id=np.repeat(np.eye(2,dtype=np.int64)[None,:,:],level,axis=0)
    B,D,G,p=matrices(level,Q,Y,theta,0,prime)
    Bd,Dd,_,_=matrices(level,Q,Q*Y%prime,theta,0,prime)
    assert np.array_equal(mul(np.roll(D,-1,axis=0),B,prime),mul(Bd,D,prime))
    vector=np.column_stack((p,np.ones(level,dtype=np.int64))).reshape(level,2,1)
    assert np.array_equal(np.roll(vector,-1,axis=0),mul(B,vector,prime))
    # The source quotient has its own meridian line; p is a relative section.
    _,_,_,pd=matrices(level,Q,Q*Y%prime,theta,0,prime)
    d=int(D[0,1,1]);vd=np.column_stack((pd,np.ones(level,dtype=np.int64))).reshape(level,2,1)
    assert np.array_equal(mul(D,vector,prime),vd*d%prime)
    mono=Id.copy();meridian_mono=Id.copy()
    for r in range(level):
        mono=mul(np.roll(B,-r,axis=0),mono,prime)
        _,Dr,_,_=matrices(level,Q,Y*pow(Q,r,prime)%prime,theta,0,prime)
        meridian_mono=mul(Dr,meridian_mono,prime)
    expected=Id.copy();expected[:,0,0]=a0%prime;expected[:,0,1]=U*C*p%prime
    assert np.array_equal(mono,expected)
    assert np.array_equal(meridian_mono,Id*V%prime) and V!=1
    raw_loop=Id.copy();strict_loop=Id.copy()
    wrong_scalar_loop=Id.copy()
    for cut in range(level):
        oldB,oldD,oldG,oldp=matrices(level,Q,Y,theta,cut,prime)
        newB,newD,newG,newp=matrices(level,Q,Y,theta,cut+1,prime)
        hr=(1-Q*Y*theta*pow(Q,cut,prime))%prime
        raw=Id.copy();raw[:,1,1]=hr;raw[cut,0,1]=-U*C%prime
        diagonal=Id.copy();diagonal[:,1,1]=hr*pow(nu,-1,prime)%prime
        strict=mul(mul(newG,diagonal,prime),inverse_shear(oldG,prime),prime)
        oldv=np.column_stack((oldp,np.ones(level,dtype=np.int64))).reshape(level,2,1)
        newv=np.column_stack((newp,np.ones(level,dtype=np.int64))).reshape(level,2,1)
        assert np.array_equal(mul(raw,oldv,prime),newv*hr%prime)
        assert np.array_equal(mul(strict,oldv,prime),newv*(hr*pow(nu,-1,prime)%prime)%prime)
        for J in (raw,strict):
            assert np.array_equal(mul(np.roll(J,-1,axis=0),oldB,prime),mul(newB,J,prime))
        _,_,oldGd,_=matrices(level,Q,Q*Y%prime,theta,cut,prime)
        _,_,newGd,_=matrices(level,Q,Q*Y%prime,theta,cut+1,prime)
        hrd=(1-Q*Q*Y*theta*pow(Q,cut,prime))%prime
        rawd=Id.copy();rawd[:,1,1]=hrd;rawd[cut,0,1]=-U*C%prime
        diagonald=Id.copy();diagonald[:,1,1]=hrd*pow(nu,-1,prime)%prime
        strictd=mul(mul(newGd,diagonald,prime),inverse_shear(oldGd,prime),prime)
        for J,Jd in ((raw,rawd),(strict,strictd)):
            assert np.array_equal(mul(Jd,oldD,prime),mul(newD,J,prime))
        raw_loop=mul(raw,raw_loop,prime);strict_loop=mul(strict,strict_loop,prime)
        wrong_scalar_loop=mul(raw*pow(nu,-1,prime)%prime,wrong_scalar_loop,prime)
    raw_expected=Id.copy();raw_expected[:,1,1]=a0%prime;raw_expected[:,0,1]=-U*C*p%prime
    assert np.array_equal(raw_loop,raw_expected)
    assert np.array_equal(strict_loop,Id)
    assert not np.array_equal(wrong_scalar_loop,Id)
    phi=np.array([int(p[a])*pow(nu,-a,prime)%prime for a in range(level)],dtype=np.int64)
    for a in range(level):
        assert int(phi[(a+1)%level])==(1-Q*h*pow(Q,a,prime))*pow(nu,-1,prime)*int(phi[a])%prime
    # Comparison with the independently implemented pointed tetrahedron kernel.
    _,_,kernel=shape_module(level,prime,Q*h%prime,nu,pow(q,-1,prime))
    assert np.array_equal(kernel,phi[[(-a)%level for a in range(level)]])
    def dilog_power(x):
        value=1
        for j in range(1,level):value=value*pow(1-pow(Q,j,prime)*x,j,prime)%prime
        return value
    for a in range(level):
        assert pow(int(phi[a]),level,prime)==dilog_power(h*pow(Q,a+1,prime)%prime)*pow(dilog_power(Q*h%prime),-1,prime)%prime
    # The primitive boundary limit is evaluated after its nu^a rescaling.
    endpoint=primitive(level,Q,1,prime)
    assert int(endpoint[-1])==level%prime and all(endpoint)
    return {'level':level,'prime':prime,'retained_internal_center':C,
            'meridian_norm_with_internal_center_retained':int(V),
            'two_direction_flatness_and_affine_monodromy_exact':True,
            'raw_cut_loop_is_non_scalar_affine_matrix':True,
            'normalizing_entire_raw_adapter_by_one_scalar_fails':True,
            'source_channel_normalized_cut_loop_is_identity':True,
            'pointed_cyclic_dilog_and_tetrahedron_kernel_match':True,
            'rescaled_boundary_factorials_and_endpoint_N_exact':True}


def tensor_walls(level,count):
    prime,_,q=field(level);Q=q*q%prime
    values=primitive(level,Q,1,prime)
    defects=0
    for indices in product(range(level),repeat=count):
        top=1;after=1;bulk=1
        for a in indices:
            ai=(1-pow(Q,a+1,prime))%prime;bi=int(a==level-1)
            top=top*(ai*int(values[a])+bi)%prime
            after=after*int(values[(a+1)%level])%prime
            bulk=bulk*ai*int(values[a])%prime
        assert top==after
        if all(a==level-1 for a in indices):
            assert top==1 and bulk==0;defects+=1
    assert defects==1
    return {'level':level,'tensor_factors':count,'all_wall_corners_retained':True,
            'omitting_the_full_corner_source_fails':True}


def actual_case(level):
    prime,generator,q=field(level);Q=q*q%prime;F=primitive(level,Q,1,prime)
    checks=0;periods=0
    for kind,x in [('generic',generator),('Kashaev',pow(q,level-1,prime))]:
        actual=color_matrices(level,prime,q,x);Y=Q*x*x%prime
        H=primitive(level,pow(Q,-1,prime),Y,prime)
        pos=np.zeros((level*level,level*level),dtype=np.int64);neg=np.zeros_like(pos)
        for a,b in product(range(level),repeat=2):
            for k in range(min(a,level-1-b)+1):
                gaussian=int(F[a])*pow(int(F[k])*int(F[a-k]),-1,prime)%prime
                color=int(H[a])*pow(int(H[a-k]),-1,prime)%prime
                value=(pow(-1,k,prime)*pow(x,-a-b-k,prime)
                       *pow(Q,a*b+(a-b)*k-k*(k+1)//2,prime)*gaussian*color)%prime
                pos[(b+k)*level+a-k,a*level+b]=value;checks+=1
            for k in range(min(b,level-1-a)+1):
                gaussian=int(F[b])*pow(int(F[k])*int(F[b-k]),-1,prime)%prime
                color=int(H[b])*pow(int(H[b-k]),-1,prime)%prime
                neg[(b-k)*level+a+k,a*level+b]=(pow(x,a+b-k,prime)*pow(Q,-a*b,prime)*gaussian*color)%prime
                checks+=1
        assert np.array_equal(pos,actual[0]) and np.array_equal(neg,actual[1])
        if level<=4:
            for word in WORDS:
                assert reduced_period(level,prime,pos,neg,actual[2],actual[3],word)==reduced_period(level,prime,*actual,word)
                periods+=1
        M=-q*x%prime;endpoint=int(primitive(level,Q,M*M%prime,prime)[-1])
        if kind=='generic':
            eta=pow(-1,level+1,prime)*pow(q,level*(1-level)//2,prime)%prime
            dimension=eta*pow(M,level-1,prime)*pow(endpoint,-1,prime)%prime
            wall=pow(q,-1,prime)*(pow(x,-1,prime)-Q*x)%prime
            original=pow(q,level*(1-level)//2,prime)*wall*pow(pow(x,level,prime)-pow(x,-level,prime),-1,prime)%prime
            assert dimension==original
    return {'level':level,'actual_crossing_entries':checks,'closed_cut_periods':periods,
            'full_dimension_is_inverse_raw_endpoint_transport':True,
            'generic_and_Kashaev_colors_exact':True}


def main():
    levels=(2,3,4,5,6,8,9,10,12)
    roots=[root_case(n) for n in levels]
    print(f'flat source and coherent cut-root transport: {len(roots)} levels passed',flush=True)
    corners=[tensor_walls(n,m) for n in (2,3,4,5) for m in (2,3)]
    actual=[actual_case(n) for n in levels]
    print(f'actual crossing entries: {sum(r["actual_crossing_entries"] for r in actual)} passed',flush=True)
    result={'scope':'Local literature cyclic-dilogarithm/source equivalence with full meridian and cut factors; no arbitrary geometric triangulation or selected regulator-norm theorem.',
            'flat_source_and_cut_torsor':roots,'tensor_wall_corners':corners,
            'actual_ADO_boundary':actual}
    Path(__file__).with_name('factorial_source_torsor_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
