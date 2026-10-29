#!/usr/bin/env python3
"""Exact actual coherent wall rows and zero-extended current identities."""

import json
import math
from pathlib import Path

import sympy as S


def zero(x):
    assert S.expand(x)==0


def rows_and_currents():
    records=[]
    for N in range(2,17):
        n=N-1
        weights=[S.Rational(1,N*2**N)*sum(S.binomial(N,r) for r in range(j+1,N+1))
                 for j in range(N)]
        zero(sum(weights)-S.Rational(1,2))
        F=S.Symbol('F')
        raw_state=[F/N]*N
        matrix_state=[N*x for x in raw_state]
        zero(sum(w*x for w,x in zip(weights,matrix_state))-F/2)
        zero(N*sum(w*x for w,x in zip(weights,raw_state))-F/2)
        zero(sum(matrix_state)/N-sum(raw_state))
        for j in range(N):
            zero(weights[j]+weights[n-j]-S.Rational(1,N))
            t=S.Symbol('t')
            integral=S.binomial(n,j)*S.integrate(t**j*(1-t)**(n-j),(t,0,S.Rational(1,2)))
            zero(integral-weights[j])
        js=list(range(-2,N+3));symbols=S.symbols(' '.join(f'J_{j+2}' for j in js))
        values=dict(zip(js,symbols))
        value=lambda j:values.get(j,0)
        diff=lambda j:value(j+1)-value(j)
        wall=sum(S.binomial(N,j)*value(j) for j in range(N+1))/S.Integer(N*2**N)
        plus=sum(weights[j]*diff(j) for j in range(N))
        minus=sum((S.Rational(1,N)-weights[j])*diff(j) for j in range(N))
        zero(plus-wall+value(0)/N)
        zero(minus+wall-value(N)/N)
        wrange=range(min(js)-1,max(js)+1)
        wp=lambda j:S.Rational(1,N) if j<0 else (weights[j] if j<N else 0)
        wm=lambda j:0 if j<0 else (S.Rational(1,N)-weights[j] if j<N else S.Rational(1,N))
        zero(sum(wp(j)*diff(j) for j in wrange)-wall)
        zero(sum(wm(j)*diff(j) for j in wrange)+wall)
        zero(sum((wp(j)+wm(j))*value(j) for j in js)-sum(values.values())/N)
        records.append({'level':N,'exact_incomplete_beta_wall_rows':True,
                        'Weyl_complement_and_half_normalizations':True,
                        'both_head_endpoints_and_relative_Green_maps':True,
                        'raw_array_matrix_N_normalization_retained':True,
                        'literal_Nth_endpoint_retained':True})
    return records


def wall_primitives():
    v,t,b=S.symbols('v T b',nonzero=True)
    records=[]
    for N in range(2,7):
        n=N-1
        for i in range(N):
            for j in range(N):
                f=S.binomial(n,j)*v**(i-j)*b**j*(1-b)**(n-j)
                anti=S.integrate(S.expand(f),b)
                plus=-(anti.subs(b,t)-anti.subs(b,0))
                minus=anti.subs(b,1)-anti.subs(b,t)
                zero(S.diff(plus,t)+f.subs(b,t))
                zero(S.diff(minus,t)+f.subs(b,t))
                zero(minus-plus-v**(i-j)/N)
                # The off-diagonal Cech difference has this exact primitive.
                if i!=j:zero(S.diff(v**(i-j)/(N*(i-j)),v)-v**(i-j-1)/N)
        records.append({'level':N,'all_actual_matrix_unit_wall_primitives':True,
                        'Cech_class_exactly_normalized_trace':True})
    return records


def entropy_check():
    records=[]
    for N in [32,64,128,256,512]:
        worst=0.0
        for frac in [.125,.25,.5,.8]:
            j=int(N*frac);t=j/N
            actual=(math.lgamma(N+1)-math.lgamma(j+1)-math.lgamma(N-j+1))/N-math.log(2)
            limit=-t*math.log(t)-(1-t)*math.log(1-t)-math.log(2)
            worst=max(worst,abs(actual-limit))
        assert worst*N/math.log(N)<2
        records.append({'level':N,'max_macroscopic_phase_error':worst})
    return records


def main():
    result={'exact_wall_rows_and_zero_extended_currents':rows_and_currents(),
            'actual_coherent_kernel_Cech_primitives':wall_primitives(),
            'entropy_phase_check':entropy_check(),
            'scope':'Actual finite cut/source current map; no internal Gaussian or global volume inference.'}
    out=Path(__file__).with_name('actual_gauss_wall_cut_current_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,
                      'exact_row_levels':len(result['exact_wall_rows_and_zero_extended_currents']),
                      'matrix_unit_levels':len(result['actual_coherent_kernel_Cech_primitives']),
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
