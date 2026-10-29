#!/usr/bin/env python3
"""Exact root factorial interpolation and its complex asymptotic marks.

Numerics use the finite Barnes product independently of lattice products
and of the complex asymptotic formula. Uniform proofs are in the note.
"""

import json
from pathlib import Path

import mpmath as mp


def log_sine_factorial(N, z):
    z = mp.mpc(z)
    return (z*mp.log(2*mp.pi/N)+mp.loggamma(z+1)
            +sum(mp.log(mp.barnesg(1+(r-z)/N))
                 -mp.log(mp.barnesg(1+(r+z+1)/N)) for r in range(N)))


def sine_factorial(N, z):
    return mp.exp(log_sine_factorial(N, z))


def factorial(N, z):
    return mp.exp(1j*mp.pi*z*(z+1)/(2*N)-1j*mp.pi*z/2)*sine_factorial(N, z)


def lattice_and_whole_checks():
    lattice = reflection = shift = 0
    max_error = mp.mpf(0)
    for N in range(2, 13):
        Q = mp.exp(2j*mp.pi/N)
        value = mp.mpc(1)
        for n in range(N):
            if n:
                value *= 1-Q**n
            error = abs(factorial(N, n)/value-1)
            max_error = max(max_error, error)
            assert error < mp.mpf('1e-40')
            lattice += 1
        for z in (mp.mpc('.17','.23'), mp.mpc(N/3, '-.31')):
            F = factorial(N, z)
            error = abs(factorial(N,z+1)/F/(1-mp.exp(2j*mp.pi*(z+1)/N))-1)
            max_error = max(max_error, error)
            assert error < mp.mpf('1e-40')
            shift += 1
            error = abs(sine_factorial(N,z)*sine_factorial(N,N-1-z)/N-1)
            max_error = max(max_error,error)
            assert error < mp.mpf('1e-40')
            reflection += 1
    return dict(lattice_values=lattice, whole_shifts=shift,
                whole_reflections=reflection, max_relative_error=float(max_error))


def J(x):
    X = mp.exp(2j*mp.pi*x)
    return ((mp.polylog(2,1)-mp.polylog(2,X))/(2j*mp.pi)
            -1j*mp.pi*(x*x-x)/2)


def complex_asymptotics():
    points = [mp.mpc('.21','.13'), mp.mpc('.63','-.18'),
              mp.mpc('.8692','.0922'), mp.mpc('.6119','-.0224')]
    rows = []
    for index,x in enumerate(points):
        previous = None
        for N in (12,24,48,96):
            actual = sine_factorial(N,N*x)
            predicted_log = N*J(x)+mp.log(2*N*mp.sin(mp.pi*x))/2+mp.pi*mp.cot(mp.pi*x)/(12*N)
            error = abs(actual/mp.exp(predicted_log)-1)
            if previous is not None:
                # Diagnostic of the proved O(N^-3) remainder, not its proof.
                assert error < previous/5, (index,N,error,previous)
            assert N**3*error < 10
            previous = error
            rows.append(dict(point=index,N=N,x=[float(mp.re(x)),float(mp.im(x))],
                             relative_error=float(error),scaled_N3_error=float(N**3*error)))
    return rows


def finite_product_identity():
    rows=[]
    for N,z in ((3,mp.mpc('.4','.2')),(5,mp.mpc('1.2','-.3'))):
        for count in (8,24):
            raw=(2*mp.pi/N)**z*mp.gamma(z+1)
            for k in range(1,count+1):
                raw*=mp.gamma(N*k+z+1)/(mp.gamma(N*k-z)*(N*k)**(2*z+1))
            correction=mp.gamma(count+1)**(-(2*z+1))
            for r in range(N):
                a=(r+z+1)/N
                b=(r-z)/N
                correction*=mp.barnesg(count+1+a)/mp.barnesg(count+1+b)
            error=abs(raw/(sine_factorial(N,z)*correction)-1)
            assert error < mp.mpf('1e-38')
            rows.append(dict(N=N,truncation=count,relative_error=float(error)))
    return rows


def main():
    with mp.workdps(55):
        exact=lattice_and_whole_checks()
        products=finite_product_identity()
        asymptotic=complex_asymptotics()
    result=dict(status='PASS',exact=exact,finite_Gamma_Barnes_products=products,
                complex_asymptotics=asymptotic,
                scope='Actual factorial lattice values and uniform complex interpolant; no chosen-knot thimble or volume theorem.')
    Path(__file__).with_name('exact_factorial_interpolation_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',exact=exact,finite_product_cases=len(products),
                         complex_cases=len(asymptotic),
                         max_scaled_complex_error=max(r['scaled_N3_error'] for r in asymptotic)),indent=2))


if __name__=='__main__':
    main()
