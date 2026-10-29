#!/usr/bin/env python3
"""Exact symbolic and actual-matrix checks of the divided source orbit."""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_divided_ward_factorial_fusion import field, ident, mm, powers, eq


def symbolic_checks():
    a,b=sp.symbols('a b', nonzero=True)
    z=a+b
    g=sp.Matrix([[a+1/z,a],[b-1/z,b]])
    assert sp.cancel(g.det()-1)==0
    phi=sp.Matrix([[1,1]])
    assert (phi*g-z*phi).applyfunc(sp.cancel)==sp.zeros(1,2)
    j=z*g.inv().T
    F0=sp.Matrix([[0,1],[1,-1]])
    F=(F0*j.inv()).applyfunc(sp.cancel)
    r,s=a/z,z**-2
    assert (F-sp.Matrix([[r,1-r],[s,-s]])).applyfunc(sp.cancel)==sp.zeros(2)
    jac=sp.diff(r,a)*sp.diff(s,b)-sp.diff(r,b)*sp.diff(s,a)
    density=sp.cancel(-jac/(s*(1+s)))
    assert sp.cancel(density-2/(1+z*z))==0
    A=z*z/(1+z*z)
    fields=[(-a-2*b,b),(-b,-a)]
    targets=[(-2*(1-r),2*s),(2*r-1,2*s)]
    for (va,vb),(vr,vs) in zip(fields,targets):
        assert sp.cancel(va*sp.diff(r,a)+vb*sp.diff(r,b)-vr)==0
        assert sp.cancel(va*sp.diff(s,a)+vb*sp.diff(s,b)-vs)==0
        div=sp.cancel((sp.diff(density*va,a)+sp.diff(density*vb,b))/density)
        assert sp.cancel(div-2*A)==0
    tau=a*z
    V=lambda f:sp.cancel((sp.diff(f,a)-sp.diff(f,b))/z)
    assert V(tau)==1 and V(A)==0
    assert sp.cancel(density/z-sp.diff(sp.log(A),a))==0
    assert sp.cancel(density/z-sp.diff(sp.log(A),b))==0
    return {'source_orbit':True,'equivariant_frame_coordinates':True,
            'canonical_density_pullback':True,'both_actual_source_divergences':True,
            'vertical_transgression':True}


def matrix_case(n):
    p,q=field(n)
    Q=q*q%p
    e=np.zeros((n,n),dtype=np.int64)
    f=e.copy()
    W=e.copy()
    U=e.copy()
    K=np.diag([pow(-q,-1,p)*pow(Q,-a,p)%p for a in range(n)])
    for j in range(1,n):
        e[j-1,j]=(pow(Q,-j,p)-1)%p
        f[j,j-1]=(1-pow(Q,j,p))%p
        U[j-1,j]=pow(n-1,-1,p)
    W[n-1,0]=1
    a,b=3,5
    z=(a+b)%p
    c=a*pow(n-1,-1,p)%p
    v=(a*U+b*W)%p
    eq(mm(K,v,p),Q*mm(v,K,p),p)
    central=b*pow(c,n-1,p)%p
    eq(powers(v,n,p)[n],central*ident(n),p)
    original=np.ones((n,n),dtype=np.int64)*pow(n,-1,p)%p
    coupon=mm(v,original,p)*(n*pow(z,-1,p)%p)%p
    eq(mm(coupon,coupon,p),coupon,p)
    assert int(coupon.trace())%p==1
    r=a*pow(z,-1,p)%p
    expected=np.ones((n,n),dtype=np.int64)
    expected[:-1,:]=r*pow(n-1,-1,p)%p
    expected[-1,:]=(1-r)%p
    eq(coupon,expected,p)
    # The whole normalized coupon, not just its diagonal, loses scale z.
    v2=(2*a*U+2*b*W)%p
    eq(mm(v2,original,p)*(n*pow(2*z,-1,p)%p),coupon,p)
    # Exact original-cut anchor r=(N-1)/N, valid on every matrix.
    anchor=((n-1)*U+W)%p
    eq(mm(anchor,original,p),original,p)
    P=[1]
    for j in range(1,n):P.append(P[-1]*(pow(Q,-j,p)-1)%p)
    assert P[-1]==pow(-1,n-1,p)*n%p
    mu=central*pow(P[-1],-1,p)%p
    E_mu=(e+mu*W)%p
    diagonal=[P[j]*pow(c,-j,p)%p for j in range(n)]
    D=np.diag(diagonal)
    Di=np.diag([pow(vv,-1,p) for vv in diagonal])
    eq(mm(mm(D,E_mu,p),Di,p),v,p)
    Fv=mm(mm(D,f,p),Di,p)
    Ki=np.diag([pow(int(K[j,j]),-1,p) for j in range(n)])
    casimir=(-2*ident(n)-q*K-pow(q,-1,p)*Ki)%p
    eq(mm(Fv,v,p),casimir,p)
    eq(powers(Fv,n,p)[n],np.zeros_like(Fv),p)
    return {'level':n,'literal_clock_shift_relation':True,
            'cyclic_power_and_regular_companion_gauge':True,
            'whole_coupon_scale_collapse':True,'exact_original_cut_anchor':True,
            'actual_transformed_Casimir':True}


def main():
    result={'symbolic':symbolic_checks(),'actual_matrices':[matrix_case(n) for n in range(2,10)],
            'scope':'Actual divided-normal source orbit and density; no internal Gaussian source map.'}
    path=Path(__file__).with_name('divided_source_framing_orbit_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'symbolic':result['symbolic'],'matrix_levels':len(result['actual_matrices']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
