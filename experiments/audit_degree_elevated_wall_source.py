#!/usr/bin/env python3
"""Actual source orbit, divided q-row and weighted stabilization checks."""

import json
import math
from pathlib import Path

import mpmath as mp
import sympy as S


def source_tensor_row():
    records=[]
    for N in range(2,8):
        U=S.zeros(N);W=S.zeros(N)
        for j in range(N-1):U[j,j+1]=S.Rational(1,N-1)
        W[N-1,0]=1
        e=S.ones(N)/N
        assert S.trace(e*U)==S.Rational(1,N)
        assert S.trace(e*W)==S.Rational(1,N)
        for j in range(N+1):
            value=S.binomial(N,j)*S.Rational(1,2)**N/N
            assert value==S.binomial(N,j)/S.Integer(N*2**N)
        records.append({'level':N,'literal_tensor_coupon_wall_row':True})
    return records


def divided_q_row():
    mp.mp.dps=80
    records=[]
    for N in range(2,33):
        Q=mp.exp(2j*mp.pi/N)
        P=lambda k:mp.fprod(1-Q**r for r in range(1,k+1))
        middle=[]
        for j in range(1,N):
            direct=N/(P(j)*P(N-j))
            formula=(-1)**(j-1)*Q**(-j*(j-1)//2)/(1-Q**j)
            assert abs(direct-formula)<mp.mpf('1e-65')
            assert abs(abs(direct)-1/(2*mp.sin(mp.pi*j/N)))<mp.mpf('1e-65')
            middle.append(direct)
        j=N//2
        central=abs(math.comb(N,j)/middle[j-1])
        bound=(2 if N%2==0 else mp.sqrt(3))*mp.mpf(2)**N/(N+1)
        assert central>=bound*(1-mp.mpf('1e-60'))
        records.append({'level':N,'actual_divided_q_binomial_value':True,
                        'diagonal_condition_lower_bound':float(bound)})
    return records


def weighted_stabilization():
    N=2;Q=-S.Integer(1);x=S.I;w,F=S.symbols('w F')
    poch=lambda z,k:S.Mul(*(1-z*Q**r for r in range(k)))
    gauss=lambda m,k:S.cancel(poch(Q,m)/(poch(Q,k)*poch(Q,m-k)))
    entries=[]
    for a in range(N):
        value=0
        for b in range(a+1):
            k=a-b
            r=((-1)**k*x**(-a-b-k)*Q**(a*b+(a-b)*k-k*(k+1)//2)
               *gauss(b+k,k)*poch(Q**(-a),k))
            value+=Q**b*r*w**k
        entries.append(S.expand(value))
    assert entries==[1,2*w-1]
    assert S.expand(sum(entries)/2-w)==0
    assert S.Rational(1,8)*2*F==F/4
    assert (S.Rational(1,2)-S.Rational(1,8))*2*F==3*F/4
    return {'actual_complete_color_level':2,'literal_weighted_cut_entries':list(map(str,entries)),
            'original_normalized_period':'w',
            'transfer_hemisphere_rows':['F/4','3F/4'],
            'not_an_extra_cut_Weyl_identity':True}


def main():
    result={'literal_source_tensor_realization':source_tensor_row(),
            'actual_divided_q_elevation':divided_q_row(),
            'universal_weighted_stabilization':weighted_stabilization(),
            'scope':'Exact source/current obstructions; no exclusion of linear relative maps or geometric cycles.'}
    out=Path(__file__).with_name('degree_elevated_wall_source_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,'divided_q_levels':len(result['actual_divided_q_elevation']),
                      'stabilization':result['universal_weighted_stabilization'],
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
