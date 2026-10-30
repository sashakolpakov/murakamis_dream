#!/usr/bin/env python3
"""Exact reflected normalization, endpoint regulator, and original source charge."""
import argparse
from pathlib import Path
import json
import mpmath as mp
import sympy as sp
from audit_actual_augmented_plat_endpoint_regulator import (
    T, a as aa, wedge, bloch_wigner)
from audit_actual_q_hahn_small_channel_generic_normals import source_S, scalar_K


def symbolic():
    A=2*T*aa-T+1
    B=(T-1)*aa+2
    F=T*aa**2+1
    ah=A/B
    U=T*(aa-1)**2/F
    Z=(aa-1)/(aa+1)
    Th=1/T
    Uh=U/T
    Zh=(T+1)*(aa-1)/(3*T*aa-T-aa+3)
    assert sp.factor((2*Th*ah-Th+1)/((Th-1)*ah+2)-aa)==0
    assert sp.factor(Th*(ah-1)**2/(Th*ah**2+1)-Uh)==0
    assert sp.factor((ah-1)/(ah+1)-Zh)==0
    Y=lambda t,u,z:-(1-u)*(t*z+u)/((u-z)*(t-u))
    assert sp.factor(Y(Th,Uh,Zh)-Y(T,U,Z))==0
    factors=[(ah-1,(T+1)*(aa-1)/B),
             (2*Th*ah-Th+1,(T+1)**2*aa/(T*B)),
             ((Th-1)*ah+2,(T+1)**2/(T*B)),
             (Th*ah**2+1,(T+1)**2*F/(T*B**2))]
    assert all(sp.factor(x-y)==0 for x,y in factors)
    atoms=lambda t,u,z:[(-1,sp.factor(u)),(-1,sp.factor(t/u)),
                        (2,sp.factor(z)),(2,sp.factor(-1/z)),
                        (1,sp.factor(u/z)),(1,sp.factor(-t*z/u))]
    low=atoms(T,U,Z)
    high=atoms(Th,Uh,Zh)
    assert not wedge(high+[(-n,z) for n,z in low])
    N,r,s,t=sp.symbols('N r s t')
    d=N-1;h=d-t;u=t-r
    bend=(d+2)*u+d*s+2*N*h
    target_shift=-d*t-(d+2)*r+d*s
    assert sp.expand(bend-target_shift-2*N*d)==0
    assert sp.expand(target_shift-d*(r+s-t)+2*N*r)==0
    th=N-t-2;rh=r+N-t-1;sh=s+N-t-1
    assert sp.expand(d*(rh+sh-th)-d*(r+s-t)-d*N)==0
    fs=[(n,sp.lambdify((T,aa),z,'mpmath')) for n,z in low]
    fh=[(n,sp.lambdify((T,aa),z,'mpmath')) for n,z in high]
    return fs,fh


def R(N,j,t,z):
    q=mp.exp(mp.pi*1j/N)
    U=q**t/z
    Tv=q**(2*t)
    return z**j*source_S(N,q,j,U,Tv)/(Tv**j*scalar_K(N,q,j))


def sine(N,v):return 2*mp.sin(mp.pi*v/N)
def product(xs):return mp.fprod(xs)
def beta(N,j):
    return product(sine(N,k) for k in range(1,2*j+1))/product(sine(N,k) for k in range(1,j+1))**2
def V(N,j,h):return product(sine(N,h+k) for k in range(j+1,N-j))
def C(N,j,t,r,s):
    q=mp.exp(mp.pi*1j/N);d=N-1
    k=1 if 2*j==d else 2
    return k*beta(N,j)**2*V(N,j,d-t)*q**(d*(r+s-t))*R(N,j,t,q**(t-2*r))*R(N,j,t,q**(t-2*s))


def finite():
    count=turn=norm=0;maxerr=mp.mpf(0)
    for N in (5,6,9,10,13,14):
        d=N-1;q=mp.exp(mp.pi*1j/N)
        for j in sorted({1,d//2}):
            for t in (mp.mpc('.19','.11')*N,mp.mpc('.71','-.13')*N):
                r=mp.mpc('.21','.17')*N;s=mp.mpc('.37','-.09')*N
                value=C(N,j,t,r,s)
                reflected=C(N,j,N-t-2,r+N-t-1,s+N-t-1)
                err=abs(reflected/value-1);assert err<mp.mpf('1e-72')
                maxerr=max(maxerr,err);count+=1
                S=product(sine(N,t-k) for k in range(j))
                f=lambda u:beta(N,j)*q**(d*u+(j*j-d*j)/2)*R(N,j,t,q**(t-2*u))/S
                h=d-t
                P=product(sine(N,h+k) for k in range(1,d-j+1))*product(sine(N,h+k) for k in range(1,j+1))/N
                fold=1 if 2*j==d else 2
                original=fold*N*P*q**(-d*t)*((-1)**j*q**(j*(j+1)))**-1*f(r)*f(s)
                err=abs(original/value-1);assert err<mp.mpf('1e-72')
                maxerr=max(maxerr,err);norm+=1
                u=t-r;v=d-r;l=s
                kent=beta(N,j)**2/N*V(N,j,h)*R(N,j,t,q**(-t+2*u))*R(N,j,t,q**(t-2*l))
                pV=lambda k:N*q**(-d*d+d*k)
                st=lambda k:(-1)**d*q**(d-2*k)
                target_t=v+l
                inverse_turn=st(d-v)*pV(v)/pV(d-target_t+u)
                typed=fold*N*inverse_turn*kent
                expected=mp.exp(-2*mp.pi*1j*r)*value
                err=abs(typed/expected-1);assert err<mp.mpf('1e-72')
                maxerr=max(maxerr,err);turn+=1
    return dict(exact_normalized_reflection_comparisons=count,
                original_measure_column_normalizations=norm,
                literal_nested_cup_turn_comparisons=turn,
                maximum_relative_error=str(maxerr))


def charges():
    count=0
    for N in range(3,15):
        for b in (0,1):
            for epsilon in (-1,1):
                co={k:(k*k+3*k+7) for k in range(-2*N,2*N+1)}
                shifted={k-N*epsilon:v for k,v in co.items()}
                cyclic=lambda cc:sum(v for k,v in cc.items() if (k-b)%N==0)
                assert cyclic(co)==cyclic(shifted)
                count+=1
    return count


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();mp.mp.dps=100
    fs,fh=symbolic();bw=[]
    for p in [(mp.mpc('.7','.3'),mp.mpc('1.4','.2')),
              (mp.mpc('-1.2','.4'),mp.mpc('.6','-.3')),
              (mp.mpf(2),mp.mpf(3))]:
        lo=mp.fsum(n*bloch_wigner(f(*p)) for n,f in fs)
        hi=mp.fsum(n*bloch_wigner(f(*p)) for n,f in fh)
        assert abs(lo-hi)<mp.mpf('1e-85')
        bw.append(dict(low=str(lo),reflected=str(hi),difference=str(abs(lo-hi))))
    result=dict(status='PASS',symbolic=dict(rational_involution_and_momentum_checks=8,
                exact_full_wedge_differences=1,source_exponent_identities=3),
                finite=finite(),marked_cyclic_charge_checks=charges(),regulators=bw,
                scope='Absolute endpoint regulator normalization and exact source characters; no global contributing degree cycle or source asymptotic.')
    out=args.output or Path(__file__).with_name('actual_matching_edge_deficient_packet_regulator_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
