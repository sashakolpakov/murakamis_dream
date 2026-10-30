#!/usr/bin/env python3
"""Focused large-imaginary-head checks of the actual moving Gamma factor.

Estimates are proved in the note. Numerical checks retain the exact
marked product, compare independent tail lengths, and take genuine
period derivatives at fixed logarithmically escaping indices.
"""
import argparse
import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp
from audit_actual_moving_period_factorial_normals import factorial, log_factorial, period


def symbolic():
    z=sp.symbols('z')
    b=lambda a:-a*a/2+a/2-sp.Rational(1,12)
    assert sp.expand(b(z+1)-b(-z))==0
    assert sp.expand((z+1-sp.Rational(1,2))-(-z-sp.Rational(1,2))-(2*z+1))==0
    return dict(digamma_first_coefficient=1,digamma_second_coefficient_cancellation=1)


def numeric():
    count=disks=normal=recurrences=gauges=0
    maximum_error=mp.mpf(0);maximum_ratio=mp.mpf(1);maximum_derivative=mp.mpf(0)
    for N in (9,24,61):
        L=1+mp.log(N);scale=N*N*L*L;rho=mp.mpf('.001')/scale
        for real,sign in ((mp.mpf('.31'),1),(mp.mpf('.67'),-1),
                          (mp.mpf('-.34'),1),(mp.mpf('1.32'),-1)):
            z=N*(real+sign*mp.mpf('.6')*L*1j)
            length=max(96,int(mp.ceil(24*(1+abs(z)/N))))
            def value(e,shift=None,extra=0):
                return factorial(period(N,e),z,N,shift=shift,count=length+extra,order=30)
            root=value(0)
            stable=abs(value(0,extra=48)/root-1)
            assert stable<mp.mpf('1e-48'),(N,z,stable)
            maximum_error=max(maximum_error,stable);count+=1
            for direction in (1,-1,1j,-1j):
                ratio=value(rho*direction)/root
                assert mp.mpf('.5')<abs(ratio)<2
                maximum_ratio=max(maximum_ratio,abs(ratio),1/abs(ratio));disks+=1
            first=mp.diff(lambda e:value(e),0)/root
            scaled=abs(first)/scale
            assert scaled<20
            maximum_derivative=max(maximum_derivative,scaled);normal+=1
            eps=rho*(1+1j)/2;P=period(N,eps)
            nxt=factorial(P,z+1,N,count=length,order=30)
            target=(1-mp.exp(2*mp.pi*1j*(z+1)/P))*value(eps)
            error=abs(nxt/target-1)
            assert error<mp.mpf('1e-48'),(N,error)
            maximum_error=max(maximum_error,error);recurrences+=1
            # Actual fixed-L cup gauge with both large opposite imaginary heads.
            d=N-1
            def cup(e):
                Pe=period(N,e);zeta=mp.exp(mp.pi*1j/N+e)
                F=lambda w:factorial(Pe,w,N,count=length,order=30)
                return mp.exp(mp.pi*1j*z)*zeta**(z*(d-z-1))*F(z)*F(d-z)/F(d)
            c0=cup(0);ce=cup(eps)
            assert mp.mpf('.5')<abs(ce/c0)<2
            gauges+=1
    return dict(independent_Gamma_tail_lengths=count,relative_disk_checks=disks,
                genuine_fixed_index_normals=normal,exact_marked_unit_recurrences=recurrences,
                actual_opposite_head_cup_gauges=gauges,
                maximum_relative_identity_error=str(maximum_error),
                maximum_two_sided_relative_ratio=str(maximum_ratio),
                maximum_scaled_first_normal=str(maximum_derivative))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    mp.mp.dps=85
    result=dict(status='PASS',precision_digits=mp.mp.dps,symbolic=symbolic(),numeric=numeric(),
                scope='Actual factorials and cup factors at logarithmically escaping complex heads. No polynomial turning packet, real divisor crossing or selected global period.')
    target=args.output or Path(__file__).with_name('actual_moving_period_factorial_logarithmic_escape_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
