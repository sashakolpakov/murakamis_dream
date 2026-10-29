#!/usr/bin/env python3
"""Actual crossing ratios, diagonal obstruction and complete source cancellation."""

import json
from functools import lru_cache
from pathlib import Path

import mpmath as mp

mp.mp.dps=85
c=2j*mp.pi


def poch(x,Q,k):
    return mp.fprod(1-x*Q**r for r in range(k))


def gaussian(m,k,Q):
    return poch(Q,Q,m)/(poch(Q,Q,k)*poch(Q,Q,m-k))


def crossing(sign,N,a,i,j,k,color):
    H0=c/N;H=H0+c*a/(N*N) if color else H0
    b=a/(1+a/N);Q=mp.exp(H)
    x=mp.exp(c/2+H*(b-1)/2);Y=mp.exp(H*b)
    if sign==1:
        return ((-1)**k*x**(-i-j-k)*Q**(i*j+(i-j)*k-k*(k+1)//2)
                *gaussian(j+k,k,Q)*poch(Y*Q**(-i),Q,k))
    return (x**(i+j-k)*Q**(-i*j)*gaussian(i+k,k,Q)*poch(Y*Q**(-j),Q,k))


@lru_cache(maxsize=None)
def F(x):
    if not x:return mp.mpf(0)
    fun=lambda y:c*y/(-mp.expm1(-c*y)) if y else mp.mpf(1)
    return mp.quad(fun,[0,x])


def B(sign,u,v,t):
    if sign==1:
        return c*(u*v+(u-v)*t-t*t/2)+F(v+t)-F(v)-F(t)+F(t-u)-F(-u)
    return -c*u*v+F(u+t)-F(u)-F(t)+F(t-v)-F(-v)


def bulk_ratios():
    records=[]
    aa=[mp.mpf('.3'),mp.mpc('-.2','.15'),mp.mpc('.4','-.1')]
    for N in [16,32,64,128,256]:
        worst=mp.mpf(0);fullworst=mp.mpf(0)
        for sign,target in [(1,('.43','.20','.12')),(-1,('.23','.48','.13'))]:
            i,j,k=[int(mp.floor(N*mp.mpf(x))) for x in target]
            u,v,t=[mp.mpf(x)/N for x in [i,j,k]]
            insertion=B(sign,u,v,t)
            for a in aa:
                ratio=crossing(sign,N,a,i,j,k,True)/crossing(sign,N,a,i,j,k,False)
                predicted=mp.exp(a*insertion)
                worst=max(worst,abs(ratio/predicted-1))
                H0=c/N;H=H0+c*a/(N*N);b=a/(1+a/N)
                color=mp.exp(H*(c/H+b-1)**2/4)
                root=mp.exp(H0*(c/H0+b-1)**2/4)
                fullratio=ratio*(color/root)**sign
                fullpred=mp.exp(a*(insertion-sign*c/4))
                fullworst=max(fullworst,abs(fullratio/fullpred-1))
        assert N*worst<100
        assert N*fullworst<100
        records.append({'level':N,'relative_bulk_error':float(worst),
                        'N_times_error':float(N*worst),
                        'relative_full_Cartan_error':float(fullworst)})
    assert records[-1]['relative_bulk_error']<records[0]['relative_bulk_error']/8
    return records


def source_cancellation():
    records=[]
    for N in [8,16,32,64,128,256]:
        n=N-1;closed_sum=N//3+N//4
        worst=mp.mpf(0)
        for a in [mp.mpf('.3'),mp.mpc('-.2','.15')]:
            H0=c/N;dH=c*a/(N*N);H=H0+dH;b=a/(1+a/N)
            for kappa in [-2,0,4]:
                aux=mp.exp(dH*(n*kappa*(b-1)/2+n*closed_sum))
                # The original exact root factor exp(c*n*kappa/2)=1
                # is retained by its even knot-parity mark.
                route=mp.exp(dH*(N*n*kappa/2+N*closed_sum))
                expected=mp.exp(-c*a*kappa/2)
                worst=max(worst,abs(aux/route/expected-1))
        assert N*worst<200
        records.append({'level':N,'complete_source_residual_error':float(worst),
                        'N_times_error':float(N*worst)})
    return records


def diagonal_obstruction():
    records=[]
    for N in [2,3,5,16]:
        a=mp.mpf('.3');b=a/(1+a/N);dH=c*a/(N*N)
        r00=crossing(1,N,a,0,0,0,True)/crossing(1,N,a,0,0,0,False)
        r11=crossing(1,N,a,1,1,0,True)/crossing(1,N,a,1,1,0,False)
        assert abs(r00-1)<mp.mpf('1e-70')
        assert abs(r11-mp.exp(dH*(2-b)))<mp.mpf('1e-70')
        assert abs(r11-r00)>mp.mpf('1e-5')
        records.append({'level':N,'scalar_adjusted_diagonal_intertwiner_impossible':True})
    return records


def Euler_primitive():
    records=[]
    for x in [mp.mpf('-.7'),mp.mpf('-.25'),mp.mpf('.15'),mp.mpf('.6')]:
        L=(mp.polylog(2,1)-mp.polylog(2,mp.exp(c*x)))/c
        zero=x*mp.log(1-mp.exp(c*x))-L-F(x)
        assert abs(zero)<mp.mpf('1e-70')
        records.append({'x':float(x),'F_equals_Euler_minus_one_of_L':True})
    return records


def main():
    result={'actual_stripped_and_full_crossings':bulk_ratios(),
            'original_source_and_framing_cancellation':source_cancellation(),
            'exact_diagonal_Gamma_obstruction':diagonal_obstruction(),
            'marked_Euler_primitive':Euler_primitive(),
            'scope':'Actual bulk arrays and source factors; no selected global sum or volume claim.'}
    out=Path(__file__).with_name('quantum_normal_bulk_response_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,
                      'largest_bulk_level':result['actual_stripped_and_full_crossings'][-1],
                      'largest_source_level':result['original_source_and_framing_cancellation'][-1],
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
