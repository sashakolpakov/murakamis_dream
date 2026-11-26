#!/usr/bin/env python3
"""Original-matrix checks of the periodic full-Hermite crossing trace.

The finite checks compare values, first normals, whole boundary products,
and the finite Fourier charge formula. The larger checks illustrate the
proved band-edge cancellation; they are not inputs to the proof.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices, encode


def crossing_fourier(level, power):
    D = level - 1
    unit = mp.exp(1j*mp.pi*power*D*D/(4*level))
    ts = [mp.pi*(D-2*j)/level for j in range(level)]
    values = [unit*mp.exp(1j*power*level*t*t/(4*mp.pi)) for t in ts]
    derivs = [1j*power*level*t*v/(2*mp.pi) for t,v in zip(ts,values)]
    coeff = {}
    for m in range(level):
        V = mp.fsum(v*mp.exp(-1j*m*t) for t,v in zip(ts,values))/level
        W = mp.fsum(v*mp.exp(-1j*m*t) for t,v in zip(ts,derivs))/(1j*level)
        c = V if m == 0 else ((level-m)*V+W)/level
        coeff[m] = c
        coeff[-m] = c
    return coeff,ts,values,derivs


def evaluate(coeff,t,derivative=0):
    return mp.fsum(v*(1j*k)**derivative*mp.exp(1j*k*t) for k,v in coeff.items())


def multiply(a,b):
    out = {}
    for k,v in a.items():
        for l,w in b.items():
            out[k+l] = out.get(k+l,mp.mpc(0))+v*w
    return out


def newton_basis(level):
    out = [{0:mp.mpf(1)}]
    for k in range(level-1):
        c = 2*mp.cos((2*k+1)*mp.pi/level)
        scale = 4*mp.sin((k+1)*mp.pi/level)**2
        out.append({a:v/scale for a,v in multiply(out[-1],{-1:1,0:c,1:1}).items()})
    return out


def edge_fourier(basis,u):
    out = {}
    for e in basis:
        value = evaluate(e,u)
        for k,v in e.items():
            out[k] = out.get(k,mp.mpc(0))+value*v
    return out


def kernel_matrix(level,basis,u):
    D = level-1
    z = mp.matrix(level)
    for j in range(level):
        z[j,j] = 2*mp.cos((2*j+1)*mp.pi/level)
        if j<D:
            z[j+1,j] = -4*mp.sin((j+1)*mp.pi/level)**2
    I=mp.eye(level)
    e=I.copy()
    K=evaluate(basis[0],u)*e
    for k in range(D):
        e=(2*mp.cos((2*k+1)*mp.pi/level)*I-z)*e/(4*mp.sin((k+1)*mp.pi/level)**2)
        K+=evaluate(basis[k+1],u)*e
    return K


def fourier_trace(level,coeff):
    eta=(-1)**(level-1)
    L=max(abs(k) for k in coeff)
    return level**2*mp.fsum(
        ell*eta**(ell+1)*(coeff.get(ell*level-1,0)-coeff.get(ell*level+1,0))
        for ell in range(1,(L+1)//level+1)
    )


def run(precision):
    mp.mp.dps=precision
    rows=[]
    for N in (3,4,5,8):
        crossing,_,_=original_matrices(N)
        basis=newton_basis(N)
        boundaries=[mp.mpf('0.13')+mp.mpf('0.04')*1j,
                    -mp.mpf('0.21')+mp.mpf('0.02')*1j]
        kernels=[kernel_matrix(N,basis,u) for u in boundaries]
        angle_kernel=multiply(edge_fourier(basis,boundaries[0]),edge_fourier(basis,boundaries[1]))
        for power in (-3,0,1,2):
            b,ts,values,derivs=crossing_fourier(N,power)
            value_error=max(abs(evaluate(b,t)-v) for t,v in zip(ts,values))
            normal_error=max(abs(evaluate(b,t,1)-v) for t,v in zip(ts,derivs))
            matrix=(crossing**power*kernels[0]*kernels[1])[N-1,0]
            fourier=fourier_trace(N,multiply(b,angle_kernel))
            error=abs(matrix-fourier)/max(1,abs(matrix),abs(fourier))
            if max(value_error,normal_error,error)>mp.mpf('1e-45'):
                raise ArithmeticError('Original matrix/Hermite/Fourier comparison failed')
            if power==1:
                expected=mp.exp(1j*mp.pi*(N-1)**2/(2*N))*(-1)**(N-1)*mp.exp(1j*mp.pi*(N-1)/N)/N**2
                if abs(b[N-1]-expected)>mp.mpf('1e-45'):
                    raise ArithmeticError('One-crossing highest coefficient failed')
            if power==2 and abs(b[N-1]-mp.mpf(1)/N)>mp.mpf('1e-45'):
                raise ArithmeticError('Two-crossing highest coefficient failed')
            rows.append({'N':N,'power':power,'value_error':mp.nstr(value_error,25),
                         'first_normal_error':mp.nstr(normal_error,25),
                         'whole_boundary_trace_relative_error':mp.nstr(error,25)})
        print(f'Checked original matrix and full Hermite Fourier trace at N={N}.',flush=True)
    asymptotics=[]
    for N in (24,25,48,49,96,97):
        basis=newton_basis(N)
        c=edge_fourier(basis,mp.mpf(0))
        summand=N*(c[0]-c.get(2,0))
        leading=mp.pi/N**2*mp.exp(N*4*mp.catalan/mp.pi)
        q=mp.exp(1j*mp.pi/N)
        S=mp.mpf(1)
        terms=[]
        for k,e in enumerate(basis):
            if k: S*=2*mp.sin(mp.pi*k/N)
            terms.append(N*1j**k*q**(mp.mpf(k*(k-1))/2)*evaluate(e,0)/S)
        actual=mp.fsum(terms)
        expected=mp.exp(-1j*mp.pi/4)/2*mp.exp(N*(2*mp.catalan/mp.pi+1j*mp.pi/8))
        asymptotics.append({'N':N,'single_summand_over_leading':encode(summand/leading),
                            'actual_source_over_leading':encode(actual/expected),
                            'log_single_summand_over_N':mp.nstr(mp.log(abs(summand))/N,25),
                            'log_actual_source_over_N':mp.nstr(mp.log(abs(actual))/N,25)})
        print(f'Checked the isolated Fourier summand and original source at N={N}.',flush=True)
    return {'scope':'Finite full-Hermite and original-matrix checks; asymptotic ratios are normalization diagnostics, not proof.',
            'decimal_precision':precision,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'matrix_checks':rows,'asymptotic_checks':asymptotics}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--precision',type=int,default=100)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    data=run(args.precision)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2)+'\n')
        print(f'Saved {args.output}.')
    else: print(json.dumps(data,indent=2))

if __name__=='__main__':main()
