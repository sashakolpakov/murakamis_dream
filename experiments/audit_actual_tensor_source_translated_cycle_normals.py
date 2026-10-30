#!/usr/bin/env python3
"""Adjoint source residues and actual moving-cup translated finite parts."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_moving_period_factorial_normals import log_factorial, period


def adjoint_residues():
    Y = sp.symbols('Y')
    g = Y/(1-Y)
    # Constant factors 2*pi*i and -pi*i occur identically on both sides.
    W = (1+Y)/(1-Y)
    D = lambda f: sp.cancel(Y*sp.diff(f,Y))
    checks = 0
    for f in (sp.Integer(1),Y,1/Y,(Y-1)**2,1/(Y-2)):
        lhs = sp.cancel(f/g)
        rhs = sp.cancel(W*g)
        for order in range(4):
            for point in (0,1,2):
                left = sp.residue(sp.cancel(W*g*lhs/Y),Y,point)
                right = sp.residue(sp.cancel((-1)**order*rhs*f/g/Y),Y,point)
                assert sp.simplify(left-right)==0,(f,order,point)
                checks += 1
            lhs = D(lhs)
            rhs = D(rhs)
    x,A,B = sp.symbols('x A B')
    # Actual local cotangent and cup-gauge Laurent coefficients.
    w = 1/x-sp.pi**2*x/3
    logarithmic_g = -1/x+sp.pi*sp.I+sp.pi**2*x/3
    density = sp.diff(w,x)+w*logarithmic_g
    residue = sp.residue(density*(A+B*x),x,0)
    assert sp.expand(residue-(sp.pi*sp.I*A-2*B))==0
    return dict(meromorphic_adjoint_residues=checks,actual_cotangent_double_pole=1)


def finite_product(zeta,n):
    return mp.fprod(1-zeta**(2*j) for j in range(1,n+1))


def cup_periods(N,eps,n,g0):
    """Original physical cup value, translated cotangent finite part.

    The latter is evaluated independently from the original moving-Gamma
    Laurent coefficients, not by the transport identity being tested.
    """
    d=N-1; k=n+1
    zeta=mp.exp(mp.pi*1j/N+eps); lam=2*mp.log(zeta)
    Fd=finite_product(zeta,d)
    base=mp.exp(mp.pi*1j*n)*zeta**(n*(d-n-1))*finite_product(zeta,n)*finite_product(zeta,d-n)/Fd
    R=-1/(lam*mp.fprod(1-zeta**(-2*j) for j in range(1,k)))
    c=g0-lam/2+lam*mp.fsum(zeta**(-2*j)/(1-zeta**(-2*j)) for j in range(1,k))
    M=mp.exp(-mp.pi*1j*k)*zeta**(-k*(d+k-1))
    m=d+k
    factors=[1-zeta**(2*j) for j in range(1,m+1)]
    B=mp.fprod(factors)
    Bprime=B*g0-lam*mp.fsum(zeta**(2*j)*mp.fprod(factors[:j-1]+factors[j:]) for j in range(1,m+1))
    residue=R*M*B/Fd
    finite=R*M/Fd*((c+mp.pi*1j+mp.log(zeta)*(d+2*k-1))*B-Bprime)
    # x'=n+N+y; the reversed cup argument is -k-y.
    turn=(-1)**d*zeta**(d-2*(n+N))
    translated=turn*(finite-(2*mp.pi*1j-2*mp.log(zeta))*residue)
    return base,translated


def original_cup_normals():
    checks=0; worst=mp.mpf(0); rows=[]
    step=mp.mpf('1e-20')
    for N in (3,4,5,7):
        d=N-1; values={}
        for sign in (-1,1):
            eps=sign*step; P=period(N,eps)
            g0=mp.diff(lambda z:log_factorial(P,z,N,shift=0),0)
            values[sign]={n:cup_periods(N,eps,n,g0) for n in sorted({0,d//2,d})}
        for n in sorted({0,d//2,d}):
            plus=values[1][n];minus=values[-1][n]
            actual=((plus[1]-(-1)**d*plus[0])-(minus[1]-(-1)**d*minus[0]))/(2*step)
            expected=(-1)**d*N*(N-2)*mp.exp(mp.pi*1j*d*n/N)
            err=abs(actual-expected)/(1+abs(expected))
            assert err<mp.mpf('1e-27'),(N,n,err)
            worst=max(worst,err); checks+=1
            rows.append(dict(N=N,head=n,relative_error=str(err)))
    return dict(original_moving_cup_translated_first_normal_finite_parts=checks,
                maximum_relative_error=str(worst),cases=rows)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();mp.mp.dps=100
    result=dict(status='PASS',adjoint=adjoint_residues(),original_cups=original_cup_normals(),
                scope='Original cotangent adjoint finite jets and actual cup finite parts. No cycle-to-saddle deformation or periodic physical-basis extension.')
    out=args.output or Path(__file__).with_name('actual_tensor_source_translated_cycle_normals_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
