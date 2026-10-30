#!/usr/bin/env python3
"""The specified Gamma-product factorial at a moving complex period.

Numerical products use a convergent Gamma prefix with its Bernoulli
tail. Doubling that prefix checks the evaluation independently. The
uniform estimates themselves are proved in the accompanying note.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp

from audit_exact_factorial_interpolation import factorial as root_barnes_factorial


_tails = {}


def log_sine_product(P, z, count=48, order=24):
    P, z = mp.mpc(P), mp.mpc(z)
    value = z*(mp.log(2*mp.pi)-mp.log(P))+mp.loggamma(z+1)
    for k in range(1,count+1):
        w=P*k
        value += mp.loggamma(w+z+1)-mp.loggamma(w-z)-(2*z+1)*mp.log(w)
    key=(count,order,mp.mp.dps)
    if key not in _tails:
        _tails[key]=[mp.zeta(2*j,count+1) for j in range(1,order+1)]
    for j,tail in enumerate(_tails[key],1):
        value -= mp.bernpoly(2*j+1,z+1)*tail/(j*(2*j+1)*P**(2*j))
    return value


def _log_marked_factor(P, w, N):
    f=1-mp.exp(2*mp.pi*1j*w/P)
    root=1-mp.exp(2*mp.pi*1j*w/N)
    # Keep the root logarithmic mark even at a negative-real factor.
    return mp.log(root)+mp.log(f/root)


def log_factorial(P, z, N, shift=None, count=48, order=24):
    """N fixes the shift/mark only; P is the moving analytic period."""
    P,z=mp.mpc(P),mp.mpc(z)
    if shift is None:
        shift=0 if 0<=mp.re(z)<N-mp.mpf('.25') else int(mp.nint(N/2-mp.re(z)))
    w=z+shift
    assert mp.re(w)>-1 and mp.re(w)<mp.re(P)
    value=(mp.pi*1j*w*(w+1)/(2*P)-mp.pi*1j*w/2
           +log_sine_product(P,w,count,order))
    if shift>0:
        value-=mp.fsum(_log_marked_factor(P,z+j,N) for j in range(1,shift+1))
    elif shift<0:
        value+=mp.fsum(_log_marked_factor(P,w+j,N) for j in range(1,-shift+1))
    return value


def factorial(P,z,N,**kwargs):
    return mp.exp(log_factorial(P,z,N,**kwargs))


def period(N,epsilon):
    return mp.pi*1j/(mp.pi*1j/N+epsilon)


def literal(N,epsilon,n):
    zeta=mp.exp(mp.pi*1j/N+epsilon)
    return mp.fprod(1-zeta**(2*j) for j in range(1,n+1))


def exact_evaluations():
    integer=recurrence=shifts=prefixes=barnes=0
    worst=mp.mpf(0)
    for N in (3,5,8,13):
        eps=mp.mpc('.003','.002')/N**3
        P=period(N,eps)
        for n in sorted(set((0,1,N//2,N-1))):
            err=abs(factorial(P,n,N)/literal(N,eps,n)-1)
            assert err<mp.mpf('1e-50'),(N,n,err)
            worst=max(worst,err);integer+=1
        for x in (mp.mpc('.31','.17'),mp.mpc('-.34','.13'),mp.mpc('1.32','-.16')):
            z=N*x
            fp=factorial(P,z,N)
            ratio=factorial(P,z+1,N)/fp
            err=abs(ratio/(1-mp.exp(2*mp.pi*1j*(z+1)/P))-1)
            assert err<mp.mpf('1e-50'),(N,x,err)
            worst=max(worst,err);recurrence+=1
            k=int(mp.nint(N/2-mp.re(z)))
            # Two nearby fixed strip shifts specify the same function.
            err=abs(factorial(P,z,N,shift=k)/factorial(P,z,N,shift=k+1)-1)
            assert err<mp.mpf('1e-50')
            worst=max(worst,err);shifts+=1
            err=abs(factorial(P,z,N,count=64,order=28)/fp-1)
            assert err<mp.mpf('1e-50')
            worst=max(worst,err);prefixes+=1
        z=N*mp.mpc('.37','.11')
        err=abs(factorial(N,z,N)/root_barnes_factorial(N,z)-1)
        assert err<mp.mpf('1e-50')
        worst=max(worst,err);barnes+=1
    return dict(genuine_integer_factorials=integer,
                moving_period_exact_recurrences=recurrence,
                independent_fixed_shift_comparisons=shifts,
                Gamma_prefix_tail_stability_checks=prefixes,
                independent_root_Barnes_checks=barnes,
                maximum_relative_error=str(worst))


def relative_disks():
    ratios=jets=endpoints=gauges=root_gauges=0
    maxratio=mp.mpf(1);maxjet=mp.mpf(0)
    for N in (5,12,25,48):
        scale=N*N*(1+mp.log(N))
        rho=mp.mpf('.002')/scale
        indices=(mp.mpf(N-1),N*mp.mpc('.28','.19'),
                 N*mp.mpc('-.33','.14'),N*mp.mpc('1.31','-.14'))
        for z in indices:
            root=factorial(N,z,N)
            for direction in (1,-1,1j,-1j):
                val=factorial(period(N,rho*direction),z,N)/root
                assert mp.mpf('.5')<abs(val)<2
                maxratio=max(maxratio,abs(val),1/abs(val));ratios+=1
            derivative=mp.diff(lambda e:factorial(period(N,e),z,N),0)
            normalized=abs(derivative/root)/scale
            assert normalized<10
            maxjet=max(maxjet,normalized);jets+=1
        # Exact FIXED d=N-1 generic first and second derivatives.
        for order in (1,2):
            analytic=mp.diff(lambda e:factorial(period(N,e),N-1,N),0,order)
            finite=mp.diff(lambda e:literal(N,e,N-1),0,order)
            assert abs((analytic-finite)/literal(N,0,N-1))<mp.mpf('1e-45')
            endpoints+=1
        L=N-2;z=N*mp.mpc('-.31','.13')
        def b(e,w):
            P=period(N,e);zeta=mp.exp(mp.pi*1j/N+e)
            return zeta**(w*(L-w))*factorial(P,w,N)*factorial(P,L-w,N)/literal(N,e,L)
        for direction in (1,1j):
            eps=rho*direction
            ratio=b(eps,z)/b(0,z)
            assert mp.mpf('.5')<abs(ratio)<2
            assert abs(b(eps,z)/b(eps,L-z)-1)<mp.mpf('1e-50')
            gauges+=1
        def physical_b(e):
            P=period(N,e);zeta=mp.exp(mp.pi*1j/N+e)
            return (zeta**(z*(N-1-z))*factorial(P,z,N)
                    *factorial(P,N-1-z,N)/literal(N,e,N-1))
        assert abs(physical_b(0)-1)<mp.mpf('1e-50')
        # The fixed-root reflection is NOT a moving-q constant.
        assert abs(mp.diff(physical_b,0))>mp.mpf('1e-6')
        root_gauges+=1
    return dict(relative_disk_factor_checks=ratios,
                genuine_complex_factor_first_derivatives=jets,
                fixed_endpoint_first_and_second_derivative_checks=endpoints,
                specified_exterior_gauge_checks=gauges,
                fixed_root_gauge_and_nonzero_moving_normal_checks=root_gauges,
                maximum_two_sided_ratio=str(maxratio),
                maximum_normalized_first_derivative=str(maxjet))


def period_transports():
    shifts=reflections=endpoints=corrections=normals=0
    worst=mp.mpf(0)
    for N in (4,7,12):
        eps=mp.mpc('.002','-.003')/N**3
        P=period(N,eps)
        z=mp.mpc('-.37','.23')
        error=abs(factorial(P,z+P,N)
                  /((1-mp.exp(2*mp.pi*1j*z))*factorial(P,z,N))-1)
        assert error<mp.mpf('1e-48');worst=max(worst,error);shifts+=1
        z=N*mp.mpc('.31','.13')
        target=P*mp.exp(mp.pi*1j*z*(z-P+1)/P)
        error=abs(factorial(P,z,N)*factorial(P,P-1-z,N)/target-1)
        assert error<mp.mpf('1e-48');worst=max(worst,error);reflections+=1
        error=abs(factorial(P,P-1,N)/P-1)
        assert error<mp.mpf('1e-48');worst=max(worst,error);endpoints+=1
        z=N*mp.mpc('-.31','.13');d=N-1
        zeta=mp.exp(mp.pi*1j/N+eps)
        actual=zeta**(z*(d-z))*factorial(P,z,N)*factorial(P,d-z,N)/literal(N,eps,d)
        corrected=(P/literal(N,eps,d)*mp.exp(mp.pi*1j*z*(N-P)/P)
                   *factorial(P,d-z,N)/factorial(P,P-1-z,N))
        error=abs(actual/corrected-1)
        assert error<mp.mpf('1e-48');worst=max(worst,error);corrections+=1
    for N in (3,5):
        z=mp.mpc('.23','.19')
        def left(e):
            return factorial(period(N,e),z+N,N)
        def right(e):
            P=period(N,e);Delta=N-P
            return ((1-mp.exp(2*mp.pi*1j*(z+Delta)))
                    *factorial(P,z+Delta,N))
        base=factorial(N,z+N,N)
        for order in (1,2):
            error=abs((mp.diff(left,0,order)-mp.diff(right,0,order))/base)
            assert error<mp.mpf('1e-44');worst=max(worst,error);normals+=1
    return dict(exact_moving_second_period_checks=shifts,
                exact_complex_period_reflection_checks=reflections,
                moving_endpoint_value_checks=endpoints,
                fixed_source_endpoint_correction_checks=corrections,
                genuine_fixed_N_shift_first_and_second_normals=normals,
                maximum_relative_error=str(worst))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name(
        'actual_moving_period_factorial_normals_results.json'))
    args=parser.parse_args()
    mp.mp.dps=85
    result=dict(status='PASS',precision_digits=mp.mp.dps,
                exact=exact_evaluations(),relative=relative_disks(),
                transport=period_transports(),
                scope='The specified moving-period Gamma interpolant, fixed endpoint and marked nonreal shifted factors. No crossing of real exterior poles or degree-period contribution.')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
