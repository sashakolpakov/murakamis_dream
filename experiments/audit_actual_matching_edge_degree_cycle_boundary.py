#!/usr/bin/env python3
"""Actual source-null grid residues, marked cup Laurent terms, and wall normals."""
import argparse,json,math
from pathlib import Path
import mpmath as mp
import sympy as sp
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_q_hahn_small_channel_generic_normals import source_S
from audit_actual_moving_period_factorial_normals import factorial,log_factorial,period


def source_zeros():
    checks=0;early=late=0
    Jet.order=3
    for N in range(3,13):
        d=N-1
        for generic in (False,True):
            p,eta=root_field(N)
            Jet.p=1000000007 if generic else p
            qval=2 if generic else eta*eta%p
            q=Jet([qval*pow(math.factorial(j),-1,Jet.p)%Jet.p for j in range(3)])
            Q=q*q
            for a in range(1,d//2+1):
                m=d-a;s=d-2*a
                for k in range(1,m+1):
                    h=a+k;sigma=d-h
                    for i1 in sorted({0,sigma//2,sigma}):
                        for ell in sorted({0,i1}):
                            # i1=d-v and ell=t_target-v are the literal rows.
                            assert source_S(N,q,m,Q**i1,Q**sigma)==0
                            assert source_S(N,q,m,Q**ell,Q**sigma)==0
                            checks+=2
                    if not generic:
                        T=Q**sigma
                        factor=Jet(1)
                        for j in range(a,m):factor*=T-Q**j
                        if k<=s:
                            assert factor.c[0]==0;early+=1
                        else:
                            assert factor.c[0]!=0;late+=1
    return dict(actual_large_numerator_three_jet_zeros=checks,
                early_collision_factor_zeros=early,late_collision_factor_units=late)


def cotangents():
    x=sp.symbols('x');Ar,Br=sp.symbols('Ar Br')
    rows=0
    for step in (1,2,-3):
        for center in range(1,5):
            offset=1
            x0=sp.Rational(center-offset,step)
            weight=sp.pi/step*sp.cot(sp.pi*(x+center-offset)/step)
            actual=sp.residue(weight*(Ar/x+Br),x,0)
            expected=Br if x0.q==1 else sp.pi/step*sp.cot(sp.pi*x0)*Ar
            assert sp.simplify(actual-expected)==0
            rows+=1
    # The actual local numerator ideal is quadratic. Test all degree-two
    # generators against the ordered diagonal-wall Laurent expansion.
    y=sp.symbols('y');checks=0
    for step in (1,2,-3):
        inverse=sum((-y)**n/(step*x)**(n+1) for n in range(7))
        for numerator in (x*x,x*y,y*y):
            for regular in (1,1+x+y):
                expr=sp.expand(numerator*regular*inverse*(1/x-sp.pi**2*x/3)*(1/y-sp.pi**2*y/3))
                assert sp.expand(expr).coeff(x,-1).coeff(y,-1)==0
                checks+=1
    return dict(actual_step_cotangent_residues=rows,ordered_diagonal_wall_ideal_checks=checks)


def finite_product(zeta,n):return mp.fprod(1-zeta**(2*j) for j in range(1,n+1))
def cup(N,L,eps,r):
    zeta=mp.exp(mp.pi*1j/N+eps);P=period(N,eps)
    return mp.exp(mp.pi*1j*r)*zeta**(r*(L-r-1))*factorial(P,r,N)*factorial(P,L-r,N)/finite_product(zeta,L)


def cup_laurent():
    checks=0;worst=mp.mpf(0)
    for N,L,k in [(7,4,1),(7,4,3),(8,6,1),(8,4,4)]:
        eps=mp.mpc('.013','.007')/N**3
        zeta=mp.exp(mp.pi*1j/N+eps);P=period(N,eps);lam=2*mp.log(zeta)
        g0=mp.diff(lambda z:log_factorial(P,z,N,shift=0),0)
        R=-1/(lam*mp.fprod(1-zeta**(-2*j) for j in range(1,k)))
        c=g0-lam/2+lam*mp.fsum(zeta**(-2*j)/(1-zeta**(-2*j)) for j in range(1,k))
        M=mp.exp(-mp.pi*1j*k)*zeta**(-k*(L+k-1))
        B=finite_product(zeta,L+k)
        Bprime=B*(g0-lam*mp.fsum(zeta**(2*j)/(1-zeta**(2*j)) for j in range(1,L+k+1)))
        residue=R*M*B/finite_product(zeta,L)
        finite=R*M/finite_product(zeta,L)*((c+mp.pi*1j+mp.log(zeta)*(L+2*k-1))*B-Bprime)
        delta=mp.mpf('1e-18')
        plus=cup(N,L,eps,-k+delta);minus=cup(N,L,eps,-k-delta)
        for actual,expected in [(delta*(plus-minus)/2,residue),((plus+minus)/2,finite)]:
            err=abs(actual-expected)/(1+abs(expected))
            assert err<mp.mpf('1e-29'),(N,L,k,err)
            worst=max(worst,err);checks+=1
    return dict(original_moving_cup_pole_and_finite_parts=checks,maximum_error=str(worst))


def root_normals():
    checks=0;normalizations=0;worst=mp.mpf(0)
    for N in range(4,17):
        d=N-1;q=mp.exp(mp.pi*1j/N);lam=2*mp.pi*1j/N
        Pprime=-N*N/(mp.pi*1j)
        nu=2*N*(-1)**N/(q-1/q)
        assert abs(Pprime/nu-(-1)**(N+1)*N*mp.sin(mp.pi/N)/mp.pi)<mp.mpf('1e-75')
        normalizations+=1
        for a in range(1,d//2+1):
            L=2*a;s=d-2*a;m=d-a
            for k in range(s+1,m+1):
                n=L+k
                R=-1/(lam*mp.fprod(1-q**(-2*j) for j in range(1,k)))
                M=(-1)**k*q**(-k*(L+k-1))
                rootfinite=2*mp.pi*1j*R*M*finite_product(q,n-N)/finite_product(q,L)
                normalres=-2*N*N*R*M*finite_product(q,n-N)/finite_product(q,L)
                # Independent original root cup normalization (lift (11)).
                h=a+k
                V=mp.fprod(2*mp.sin(mp.pi*(h+j)/N) for j in range(a+1,m+1))
                literal=N*q**(-2*a*k-s*h)/(finite_product(q,L)*V)
                for actual,expected in [(rootfinite,literal),(normalres,Pprime*literal)]:
                    err=abs(actual-expected)/(1+abs(expected));assert err<mp.mpf('1e-72')
                    worst=max(worst,err);checks+=1
    return dict(actual_late_wall_root_cup_and_normal_checks=checks,
                original_exposed_normal_scalars=normalizations,maximum_error=str(worst))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    mp.mp.dps=90
    result=dict(status='PASS',source=source_zeros(),cycles=cotangents(),
                laurent=cup_laurent(),normals=root_normals(),
                scope='Original source-null ordered grid periods and explicit isolated boundary densities. No global cycle deformation or contributing saddle.')
    out=args.output or Path(__file__).with_name('actual_matching_edge_degree_cycle_boundary_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
