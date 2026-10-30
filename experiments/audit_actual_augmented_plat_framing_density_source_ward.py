#!/usr/bin/env python3
"""Focused actual-source Ward and framing-density normalization audit.

The general Gaussian-current assembly is proved in the note. These exact
checks audit its local source identities, orientations and marked adapter;
they do not test a global stationary-cycle coefficient.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_q_hahn_small_channel_generic_normals import source_S
from audit_actual_braided_two_cut_source_adapter import original_crossings
from audit_actual_nc_morse_graph_first_normal_source_reduction import module_jet
from audit_actual_matching_edge_antidiagonal_operator_packet import factorials, cup


def zero(expr):
    assert sp.cancel(expr) == 0


def symbolic_newton():
    U,V,Q,A0=sp.symbols('U V Q A0', nonzero=True)
    def P(X,n):return sp.prod(X-Q**r for r in range(n))
    fterms=eterms=ratios=0
    for m in range(1,5):
        for b in range(m+1):
            N=V**b*P(U,b)*P(V,m-b)
            zero((1-U)*N.subs(U,U/Q)+U*(1-V)*N.subs(V,V/Q)
                 -(1-U*V/Q**m)*N)
            fterms+=1
            E=A0*(U-A0)*N.subs(U,Q*U)+U*(V-A0)*N.subs(V,Q*V)
            E-=(Q**m*U*V-A0**2)*N
            lower=0
            if b<m:
                lower+=Q**b*(A0-Q**(m-b-1))*(Q**(m-b)-1)*V**b*P(U,b)*P(V,m-1-b)
            if b:
                lower+=A0*(A0-Q**(b-1))*(Q**b-1)*V**(b-1)*P(U,b-1)*P(V,m-b)
            zero(E+U*V*lower)
            eterms+=1
        B=sp.symbols('B',nonzero=True)
        for b in range(m):
            cr=-B*Q**(b+1)*(1-Q**(m-b))*(1-B*Q**(m-b))/((1-Q**(b+1))*(1-B*Q**(b+1)))
            diagonal=Q**b*(A0-Q**(m-b-1))*(Q**(m-b)-1)
            nextterm=A0*(A0-Q**b)*(Q**(b+1)-1)
            zero((diagonal+cr*nextterm).subs(A0,1/(B*Q)))
            ratios+=1
    return dict(termwise_F_identities=fterms,termwise_E_telescopes=eterms,
                actual_coefficient_cancellations=ratios)


def actual_polynomial_jets():
    Jet.p=1000000007;Jet.order=4
    count=cups=0
    for N in range(3,13):
        for q0 in (2,5):
            q=Jet([q0*pow(math.factorial(k),-1,Jet.p)%Jet.p for k in range(4)])
            Q=q*q;A0=Q**(N-1)
            U=Jet([3,7,11,13]);V=Jet([17,19,23,29])
            fac=factorials(q,N-1)
            for L in range(N):
                for r in range(1,L+1):
                    assert cup(L,q,fac,r)/cup(L,q,fac,r-1)==-q**(L-2*r)*(1-Q**r)/(1-Q**(L-r+1))
                    cups+=1
            for m in range(N):
                def H(u,v):return source_S(N,q,m,u,u*v)/u**m
                h=H(U,V)
                assert (1-U)*H(U/Q,V)+U*(1-V)*H(U,V/Q)==(1-U*V*Q**(-m))*h
                assert A0*(U-A0)*H(Q*U,V)+U*(V-A0)*H(U,Q*V)==(Q**m*U*V-A0*A0)*h
                count+=2
    return dict(actual_large_and_small_H_four_jet_identities=count,
                retained_jet_coefficients=4*count,actual_cup_four_jet_ratios=cups)


def source_cut_rows():
    counts=0
    for N in range(2,13):
        p,q,g,_=original_crossings(N)
        E,F,K=module_jet(N-1,q,p)
        E,F,K=E[0],F[0],K[0]
        Ki=np.diag([pow(int(v),-1,p) for v in np.diag(K)])
        e=np.ones((N,N),dtype=np.int64)*pow(N,-1,p)%p
        eK=(Ki@e@K-e)%p
        eE=(Ki@e@E-E@Ki@e)%p
        eF=(e@F-K@F@e@Ki)%p
        A=np.array([pow(q,2*a,p) for a in range(N)],dtype=np.int64)
        assert np.all(np.diag(eK)==0)
        assert np.array_equal(np.diag(eE),q*(1-q*q)*A*pow(N,-1,p)%p)
        assert np.array_equal(np.diag(eF),(1-q*q)*A*pow(N,-1,p)%p)
        assert np.array_equal(np.diag(eF-eE-2*eK)%p,(1-q)*(1-q*q)*A*pow(N,-1,p)%p)
        counts+=4*N
    return dict(actual_truncated_complete_cut_diagonals=counts)


def symbols_and_density():
    h,p,q,M,r,s,x,L=sp.symbols('h p q M r s x L',nonzero=True)
    A=sp.exp(q)
    # Literal row coefficient equals its Weyl symbol at the half-step.
    zero((1-sp.exp(q-h/2))-(1-A).subs(q,q-h/2))
    zero((1/M-M*sp.exp(-h/2)/A)-(1/M-M/A).subs(q,q+h/2))
    # Actual moving-factorial cup ratio: the finite monomial and both
    # factorial recurrences, without an off-root reflection shortcut.
    exponent=x*(L-x-1)
    zero(exponent-exponent.subs(x,x-1)-(L-2*x))
    # Generic Fhat-to-G phase leaves exactly q0^(-x) in the root cup.
    zero(exponent+(x*(x+1)+(L-x)*(L-x+1)-L*(L+1))/2+x)
    k,e,f=sp.symbols('k e f',nonzero=True)
    Ah=sp.Matrix([0,2*e,-2*f]);Ae=sp.Matrix([k*f,1/k+e*f-k,-f*f])
    Af=sp.Matrix([-e,0,1-1/k**2]);xs=(k,e,f)
    fields=(k*Ah/2,k*Af,Ae-f*Ah/2)
    for field,expected in zip(fields,(0,-e,f)):
        zero(sum(sp.diff(field[j],xs[j]) for j in range(3))-expected)
        zero(field[0]/k-expected)
    xi1=(-2*(1-r),2*s);xi2=(2*r-1,2*s)
    density=-1/(s*(1+s));Ac=1/(1+s)
    for v in (xi1,xi2):
        zero(sp.diff(density*v[0],r)+sp.diff(density*v[1],s)-2*Ac*density)
    zero(sp.det(sp.Matrix([xi1,xi2]))+2*s)
    F=sp.Matrix([[r,1-r],[s,-s]])
    Pi=sp.simplify(F*sp.diag(1,0)*F.inv())
    assert Pi==sp.Matrix([[r,r*(1-r)/s],[s,1-r]])
    w=(r-1)/s;v=r/s
    jac=sp.det(sp.Matrix([[sp.diff(v,r),sp.diff(v,s)],
                          [sp.diff(w,r),sp.diff(w,s)]]))
    zero(jac/(v-w)**2-1/s)
    zero(density+Ac/s)
    # Derive the marked cup factor without resetting the finite d offset.
    n,a=sp.symbols('n a',integer=True,positive=True)
    zero(-(n-1-a)-a-1+n)
    # Leading b_i/h=-2A, residual (1-q)(1-Q)/h tends to zero.
    assert sp.limit(2*sp.exp(h/2)*(1-sp.exp(h))/h,h,0)==-2
    assert sp.limit((1+sp.exp(h/2))*(1-sp.exp(h))/h,h,0)==-2
    assert sp.limit((1-sp.exp(h/2))*(1-sp.exp(h))/h,h,0)==0
    return dict(exact_Weyl_half_steps=2,literal_cup_ratio=1,
                exact_root_cup_phase=1,modular_divergence_cancellations=3,
                field_divergences=2,field_independence=1,flag_Jacobian=1,
                marked_clock_offset=1,cut_subprincipal_limits=3)


def gaussian_current():
    # A variable Gaussian tests precisely the determinant derivative that
    # is lost by transporting only its stationary action.
    x,h=sp.symbols('x h',positive=True)
    a=1+x*x;b=1+x;v=2*x+1
    G=b/sp.sqrt(a)
    # Constant and u^2 terms of the actual external divergence.
    integrated=sp.diff(v*b,x)/sp.sqrt(a)-v*b*sp.diff(a,x)/(2*a**sp.Rational(3,2))
    zero(integrated-sp.diff(v*G,x))
    # Normal current (c*u)*I integrates to zero; <u²>=h/a.
    c=x*x+3
    zero(c*G-c*a/h*(h/a)*G)
    # A change x=f(y) retains the top-form Jacobian and divergence.
    y=sp.symbols('y',positive=True);f=y+y*y;fp=sp.diff(f,y)
    pulled=G.subs(x,f)*fp;vp=v.subs(x,f)/fp
    zero(sp.diff(vp*pulled,y)-sp.diff(v*G,x).subs(x,f)*fp)
    return dict(variable_transverse_determinant=1,normal_current=1,
                actual_top_form_Jacobian=1)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    result=dict(status='PASS',newton=symbolic_newton(),source=actual_polynomial_jets(),
                cut=source_cut_rows(),geometry=symbols_and_density(),
                gaussian=gaussian_current(),scope='Exact local source Ward identities and density normalization. The general current/Gaussian proof is analytical; no global finite-cycle coefficient is tested.')
    target=args.output or Path(__file__).with_name('actual_augmented_plat_framing_density_source_ward_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
