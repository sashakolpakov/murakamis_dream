#!/usr/bin/env python3
"""Finite original-matrix curvature and retained boundary corrections.

Bounds are proved in the note. Sample minima/rates below are diagnostics of
the exact source interfaces, not proofs of a graph rank or stationary point.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_q_hahn_complementary_hard_edge import matrices, det_pair, low_series
from audit_actual_q_hahn_small_channel_generic_normals import gauss
from audit_actual_q_hahn_resonant_hard_edge import boundary_polynomial
from audit_actual_correlated_boundary_band_ratio import model_and_relative, root_cup


def symbolic():
    alpha,beta,u,v=sp.symbols('alpha beta u v',real=True)
    hm=sp.Matrix([[2,1-sp.I],[1+sp.I,3]])
    hp=hm.conjugate()
    X,Y=alpha*hm,beta*hp
    M=sp.eye(2)+X+Y
    R=M.inv()
    direct=sp.trace(R*(u*u*X+v*v*Y)-R*(u*X+v*Y)*R*(u*X+v*Y))
    expected=(u*u*sp.trace(X*R*R)+v*v*sp.trace(Y*R*R)
              +(u-v)**2*sp.trace(X*R*Y*R))
    assert sp.cancel(direct-expected)==0
    x,t=sp.symbols('x t',real=True)
    assert sp.trigsimp(sp.sin(2*x+t)-sp.sin(x)*sp.cos(x+t)
                      -sp.sin(x+t)*sp.cos(x))==0
    A,B=sp.symbols('A B',positive=True)
    assert sp.trigsimp(sp.cot(A)+sp.cot(B)-sp.sin(A+B)/(sp.sin(A)*sp.sin(B)))==0
    # Half-index and physical-log-radius signs in the actual determinant.
    q,Xr,Yr=sp.symbols('q Xr Yr',nonzero=True)
    U,V=Xr/q,Yr/q
    assert sp.cancel(q*q*U*V-Xr*Yr)==0
    assert sp.cancel(1/(q*V)-1/Yr)==0
    return dict(noncommuting_exact_Hessian_identity=1,
                actual_pivot_and_ratio_trigonometric_identities=2,
                original_half_index_and_inverse_clock_identities=2)


def matrix_checks():
    count=pivots=bulk_vectors=cones=0
    min_curvature=float('inf');max_curvature=0.
    min_jensen=float('inf');max_identity=0.
    for N in (16,31,32,63,64,127,128):
        th=np.pi/N
        for a in sorted(set((max(1,N//5),N//3,(N-1)//2))):
            Hp,Hm=matrices(N,a)
            for H in (Hp,Hm):
                reconstructed=np.zeros_like(H)
                for n in range(1,a):
                    p=np.sin(n*th)/(np.cos(n*th)*np.sin((2*n-1)*th))
                    w=np.zeros(a,complex);w[n-1]=1;w[n]=np.conj(H[n-1,n])/p
                    reconstructed+=p*np.outer(w,np.conj(w))
                    pivots+=1
                p=np.sin(a*th)/(np.cos(a*th)*np.sin((2*a-1)*th))
                reconstructed[-1,-1]+=p
                assert np.linalg.norm(H-reconstructed)<=2e-10*max(1,np.linalg.norm(H))
            for alpha,beta in ((.2,.4),(1.1,.7),(2.3,1.6)):
                X,Y=alpha*Hm,beta*Hp
                M=np.eye(a)+X+Y;R=np.linalg.inv(M);R2=R@R
                xx=float(np.trace(X@R2).real)
                yy=float(np.trace(Y@R2).real)
                ab=float(np.trace(X@R@Y@R).real)
                explicit=np.array([[xx+ab,-ab],[-ab,yy+ab]])
                direct=np.array([[np.trace(X@R-X@R@X@R).real,-np.trace(X@R@Y@R).real],
                                 [-np.trace(X@R@Y@R).real,np.trace(Y@R-Y@R@Y@R).real]])
                err=float(np.linalg.norm(direct-explicit))
                max_identity=max(max_identity,err)
                assert err<1e-8*N
                eig=np.linalg.eigvalsh(explicit)/N
                min_curvature=min(min_curvature,float(eig[0]))
                max_curvature=max(max_curvature,float(eig[-1]))
                assert eig[0]>1e-5 and eig[-1]<1
                # Exact one-variable source, including the final folded row.
                M0=np.eye(a)+X;R0=np.linalg.inv(M0)
                one=float(np.trace(X@R0@R0).real)/N
                assert 1e-5<one<1
                count+=1
                # Original disjoint Cholesky rows and their Jensen step.
                for n in range(max(1,int(np.ceil(N*.05))),min(a,int(np.floor(N*.12)))+1,2):
                    if n>=a:continue
                    p=np.sin(n*th)/(np.cos(n*th)*np.sin((2*n-1)*th))
                    w=np.zeros(a,complex);w[n-1]=1;w[n]=np.conj(Hm[n-1,n])/p
                    w/=np.linalg.norm(w)
                    lhs=float(np.vdot(w,R2@w).real)
                    rhs=float(np.vdot(w,M@w).real)**-2
                    assert lhs>=rhs-1e-10
                    min_jensen=min(min_jensen,lhs/rhs)
                    bulk_vectors+=1
                eigM,vec=np.linalg.eigh(M)
                ir=(vec/np.sqrt(eigM))@vec.conj().T
                A=ir@X@ir;B=ir@Y@ir
                for z1,z2 in ((.02+.03j,-.01+.02j),(-.025+.01j,.015-.02j)):
                    e1,e2=np.exp(z1)-1,np.exp(z2)-1
                    E=e1*A+e2*B
                    assert np.linalg.norm(E,2)<=abs(e1)+abs(e2)+1e-10
                    assert np.linalg.norm(E,2)<.2
                    cones+=1
    return dict(original_Hermitian_matrix_Hessians=count,
                original_Cholesky_rows=pivots,bulk_Jensen_vectors=bulk_vectors,
                complex_preconditioned_neighborhoods=cones,
                minimum_Hessian_eigenvalue_over_N=min_curvature,
                maximum_Hessian_eigenvalue_over_N=max_curvature,
                minimum_Jensen_ratio=min_jensen,
                maximum_direct_Hessian_identity_error=max_identity)


def variance_checks():
    weights=ratios=shells=0
    min_var=mp.inf;max_var=mp.mpf(0);min_shell=mp.inf
    for N in (32,33,64,65,128,129,256,257):
        th=mp.pi/N
        for a in sorted(set((N//4,(N-1)//2))):
            for w in map(mp.mpf,('.25','.7','1','2','4')):
                ts=[mp.mpf(1)]
                for k in range(a):
                    rr=w*(mp.sin((a-k)*th)/mp.sin((k+1)*th))**2
                    ts.append(ts[-1]*rr)
                    ratios+=1
                norm=mp.fsum(ts);ps=[x/norm for x in ts]
                mean=mp.fsum(k*x for k,x in enumerate(ps))
                var=mp.fsum((k-mean)**2*x for k,x in enumerate(ps))
                min_var=min(min_var,var/N);max_var=max(max_var,var/N)
                assert mp.mpf('.001')<var/N<1
                mode=max(range(a+1),key=lambda k:ts[k])
                if mode>2*mp.sqrt(N)+2 and a-mode>2*mp.sqrt(N)+2:
                    left=mp.fsum(ps[k] for k in range(a+1) if mp.sqrt(N)<=mode-k<=2*mp.sqrt(N))
                    right=mp.fsum(ps[k] for k in range(a+1) if mp.sqrt(N)<=k-mode<=2*mp.sqrt(N))
                    assert left>0 and right>0
                    min_shell=min(min_shell,left,right);shells+=2
                weights+=1
    derivatives=0;max_error=mp.mpf(0)
    for N in (8,9,16,17):
        q=mp.exp(mp.pi*1j/N)
        for a in sorted(set((N//4,(N-1)//2))):
            w=mp.mpf('1.3')
            f=lambda z:boundary_polynomial(N,a,w*mp.exp(z)/(q*q))
            f0=f(0);f1=mp.diff(f,0,1)/f0;f2=mp.diff(f,0,2)/f0
            ts=[mp.mpf(1)]
            for k in range(a):
                ts.append(ts[-1]*w*(mp.sin((a-k)*mp.pi/N)/mp.sin((k+1)*mp.pi/N))**2)
            norm=mp.fsum(ts)
            mu=mp.fsum(k*x for k,x in enumerate(ts))/norm
            vv=mp.fsum((k-mu)**2*x for k,x in enumerate(ts))/norm
            err=max(abs(f1-mu),abs(f2-f1*f1-vv))
            assert err<mp.mpf('1e-70');max_error=max(max_error,err);derivatives+=2
    return dict(actual_positive_weight_families=weights,exact_sine_weight_ratios=ratios,
                separated_shell_mass_checks=shells,original_phase_polynomial_derivatives=derivatives,
                minimum_variance_over_N=str(min_var),maximum_variance_over_N=str(max_var),
                minimum_tested_shell_probability=str(min_shell),
                maximum_literal_derivative_error=str(max_error))


def logjets(f):
    f0=f(0)
    z=[mp.diff(f,0,k)/f0 for k in (1,2,3)]
    return z[0],z[1]-z[0]**2,z[2]-3*z[1]*z[0]+2*z[0]**3


def derivative_and_correction_checks():
    core=corrections=cups=0;max_core=mp.mpf(0);max_correction=mp.mpf(0)
    for N in (16,17,32,33,64,65):
        q=mp.exp(mp.pi*1j/N)
        for step in (0,1):
            a=(N-1)//2-step;s=N-1-2*a
            # Literal core derivatives, original finite determinant recurrence.
            for beta in (None,mp.mpf('.7')):
                U0=-mp.mpf('1.4')/q
                V0=None if beta is None else -1/(2*beta*q)
                f=lambda z:det_pair(N,a,U0*mp.exp(z),None if V0 is None else V0*mp.exp(-mp.mpf('.4')*z))
                jj=logjets(f)
                for value in jj:
                    max_core=max(max_core,abs(value)/N)
                    assert abs(value)/N<10;core+=1
            # All six retained model corrections, with actual raw half-index.
            fixtures={
                '200':(N*N*mp.mpc('.8','.3'),mp.mpc('.6','.2')),
                '002':(mp.mpc('.6','.2'),mp.mpc('.8','.3')/(N*N)),
                '220':(-mp.mpf('1.4')/q,N*N*mp.mpc('.8','.3')),
                '022':(mp.mpc('.8','.3')/(N*N),-mp.mpf('1.4')/q),
                '202':(N*N*mp.mpc('.8','.3'),mp.mpf('1.3')/(q*q*N*N*mp.mpc('.8','.3'))),
                '222':(-mp.mpf('1.4')/q,-mp.mpf('.8')/q),
            }
            for pattern,(U0,V0) in fixtures.items():
                du,dv=mp.mpf('.6'),mp.mpf('-.4')
                def ff(z):
                    U,V=U0*mp.exp(du*z),V0*mp.exp(dv*z)
                    full=model_and_relative(N,a,pattern,U,V)[0]
                    if pattern=='220':corefactor=det_pair(N,a,U)
                    elif pattern=='022':corefactor=det_pair(N,a,q**(2*(N-1))/V)
                    elif pattern=='202':corefactor=boundary_polynomial(N,a,U*V)
                    elif pattern=='222':corefactor=det_pair(N,a,U,V)
                    else:corefactor=mp.mpc(1)
                    return full/corefactor
                jj=logjets(ff)
                for value in jj[1:]:
                    max_correction=max(max_correction,abs(value)/(s+1))
                    assert abs(value)/(s+1)<100;corrections+=1
            # Interior auxiliary and both logarithmically escaping arguments.
            for X in (mp.mpf('-.8'),N*N*mp.mpc('.8','.3'),mp.mpc('.8','.3')/(N*N)):
                x=N*mp.log(X)/(2j*mp.pi)
                jj=logjets(lambda z:root_cup(N,2*a,x+N*z/(2j*mp.pi)))
                for value in jj[1:]:
                    assert abs(value)/(s+1)<100;cups+=1
    return dict(original_determinant_log_derivatives=core,
                all_six_model_nonlinear_corrections=corrections,
                retained_interior_and_escaping_cup_corrections=cups,
                maximum_core_derivative_over_N=str(max_core),
                maximum_model_correction_over_s_plus_one=str(max_correction))


def independent_source_derivatives():
    """Original finite H sum and its literal leading-V coefficient."""
    full=top=0;worst=mp.mpf(0)
    for N in (3,4,7,8,11,12):
        q=mp.exp(mp.pi*1j/N);Q=q*q
        for a in sorted(set((max(1,(N-1)//2-1),(N-1)//2))):
            Ka=gauss(Q,2*a,a)
            U0,V0=-mp.mpf('1.3')/q,-mp.mpf('.8')/q
            def source(z):
                U,V=U0*mp.exp(z),V0*mp.exp(-mp.mpf('.4')*z)
                return low_series(q,N,a,U,V)/(V**a*Ka)
            determinant=lambda z:det_pair(N,a,U0*mp.exp(z),V0*mp.exp(-mp.mpf('.4')*z))
            for actual,expected in zip(logjets(source),logjets(determinant)):
                err=abs(actual-expected);worst=max(worst,err)
                assert err<mp.mpf('1e-68');full+=1
            def leading(z):
                U=U0*mp.exp(z)
                return mp.fsum((-1)**k*Q**(k*(k+1)//2)*gauss(Q,a,k)**2
                               *mp.fprod(U-Q**j for j in range(k))
                               for k in range(a+1))/Ka
            for actual,expected in zip(logjets(leading),logjets(lambda z:det_pair(N,a,U0*mp.exp(z)))):
                err=abs(actual-expected);worst=max(worst,err)
                assert err<mp.mpf('1e-68');top+=1
    return dict(original_H_sum_log_derivatives=full,
                original_leading_V_coefficient_log_derivatives=top,
                maximum_source_derivative_error=str(worst))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();mp.mp.dps=85
    result=dict(status='PASS',precision_digits=mp.mp.dps,symbolic=symbolic(),
                matrices=matrix_checks(),variance=variance_checks(),
                derivatives=derivative_and_correction_checks(),
                original_source=independent_source_derivatives(),
                scope='Finite local root-source curvature, complex derivative interfaces and retained nonlinear corrections. No graph rank, stationary point, Gaussian reduction or period claim.')
    target=args.output or Path(__file__).with_name('actual_q_hahn_boundary_model_curvature_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
