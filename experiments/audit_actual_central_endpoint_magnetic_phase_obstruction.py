#!/usr/bin/env python3
"""Exact central physical phase obstruction and endpoint local discriminant."""
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_marked_multiport_chebyshev_source_packet import pair_circle


def original_n3():
    I=sp.I;q=(1+I*sp.sqrt(3))/2;Q=sp.simplify(q*q);x=Q
    simple=lambda z:sp.simplify(sp.expand_complex(z))
    F=sp.zeros(3);K=sp.diag(*[simple(x*Q**(-a)) for a in range(3)])
    for a in range(2):F[a+1,a]=simple(1-Q**(a+1))
    Ft=sp.kronecker_product(F,sp.eye(3))+sp.kronecker_product(K.inv(),F)
    W=sp.zeros(9,3);W[1,0]=1;W[3,0]=q
    for r in (1,2):
        column=Ft*W[:,r-1]/(1-Q**r)
        for a in range(9):W[a,r]=simple(column[a])
    triples=[(2,1,0),(1,2,0),(0,2,1),(0,1,2),(1,0,2),(2,0,1)]
    values=[simple(3*x**(-c)*W[3*a+b,2-c]) for a,b,c in triples]
    expected=[3*q,3,-3,3*q*q,-3,3]
    assert all(simple(v-e)==0 for v,e in zip(values,expected))
    ratio=simple(values[0]*values[2]*values[4]/(values[1]*values[3]*values[5]))
    assert simple(ratio-1/q)==0 and sp.im(ratio)!=0
    A=sp.symbols('A0:3',nonzero=True);B=sp.symbols('B0:3',nonzero=True);C=sp.symbols('C0:3',nonzero=True)
    gauges=[A[a]*B[b]*C[c] for a,b,c in triples]
    assert sp.cancel(gauges[0]*gauges[2]*gauges[4]/(gauges[1]*gauges[3]*gauges[5]))==1
    return dict(original_coproduct_entries={str(t):str(v) for t,v in zip(triples,values)},
                gauge_invariant_ratio=str(ratio),nonreal=True)


def endpoint_operators(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    rho=(q-pow(q,-1,p))%p;Et,Ft,Kt=coproduct(rho*rho*E%p,F,K,2,N,p)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    L=pair_circle(O,N,p);projector=L@L%p*pow(N*N,-1,p)%p
    assert np.array_equal(projector@projector%p,projector)
    assert int(np.trace(projector)%p)==N
    m=(N-1)//2;omega=int(Rp[0,0])*pow(-1,m,p)*pow(q,m*(m+1),p)%p
    assert np.array_equal(Rp@projector%p,omega*projector%p)
    assert np.array_equal(Rm@projector%p,pow(omega,-1,p)*projector%p)
    assert np.array_equal(O@projector%p,-2*projector%p)
    return dict(N=N,original_projector_and_both_twist_scalars=True)


def discriminant():
    T,U=sp.symbols('T U');A=U*(T+1)-4*T;B=2*U*(T-1);C=U*(T+1)
    assert sp.expand(B*B-4*A*C-16*T*U*(T+1-U))==0
    phi,psi=sp.symbols('phi psi',real=True)
    original=2+2*sp.cos(phi)-2*sp.cos(psi)-2*sp.cos(phi-psi)
    factored=4*sp.cos(phi/2)*(sp.cos(phi/2)-sp.cos(psi-phi/2))
    assert sp.trigsimp(sp.expand_trig(original-factored))==0
    return dict(discriminant='16*T*U*(T+1-U)',physical_modulus_lower_bound=16,
                trigonometric_factorization=True)


def main():
    result=dict(status='PASS',magnetic_obstruction=original_n3(),
                original_endpoint_operators=[endpoint_operators(N) for N in (3,5,7,9,11)],
                endpoint_discriminant=discriminant(),
                scope='At N=3 no independent-leg gauge makes the actual central tensor entrywise positive. Coherent graph resummation and geometric selection remain open.')
    Path(__file__).with_name('actual_central_endpoint_magnetic_phase_obstruction_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
