#!/usr/bin/env python3
"""Actual divided clock symbols, marked finite flux and pole continuation."""

import json
from pathlib import Path

import mpmath as mp

from audit_finite_sum_annihilator import field
from audit_high_integral_color_frobenius_source import gaussian_Q_dual_factory
from audit_high_color_two_clock_source import string_dual


def actual_source_clocks():
    records=[]
    for N in range(3,11):
        prime,_,q=field(N)
        Q=q*q%prime
        choose=gaussian_Q_dual_factory(Q,prime)
        for s in sorted({0,N//2,N-1}):
            psi,_,row,_=string_dual(N,N,s,q,prime,choose)
            for t,u in [(2,3),(3,5),(5,7)]:
                unit=sum(int(row[k])*int(psi[k])*pow(t*u,k,prime)
                         for k in range(N+1))%prime
                assert unit
                moment=sum(int(row[k])*int(psi[k])*pow(t*u,k,prime)
                           *pow(Q,-k,prime) for k in range(N+1))%prime
                moment=moment*pow(unit,-1,prime)%prime
                T=t*u*pow(1+t*u,-1,prime)%prime
                expected=pow((1+(pow(Q,-1,prime)-1)*T)%prime,N,prime)
                south=pow((1+(Q-1)*(1-T))%prime,N,prime)
                assert moment==expected==south
                records.append({'N':N,'head_index':s,'source_flags':[t,u],
                                'actual_gaussian_divided_clock_and_clutch':True})
    return records


def flux_and_continuation():
    mp.mp.dps=90
    c=2*mp.pi*1j
    records=[]
    for N in [3,4,5,8,16,32,64,128,256]:
        Q=mp.exp(c/N)
        alpha=Q**-1-1
        F=lambda T:(1+alpha*T)**N
        tt=lambda T:-N/c*mp.log(1+alpha*T)
        derivative=lambda T:-N*alpha/(c*(1+alpha*T))
        period=c*N*mp.quad(lambda T:alpha/(1+alpha*T),[0,1])
        assert abs(period-4*mp.pi**2)<mp.mpf('1e-70')
        assert abs(tt(0))<mp.mpf('1e-70')
        assert abs(tt(1)-1)<mp.mpf('1e-70')
        pole_betas=[(1-derivative(0))/(-N*alpha),
                    (1-derivative(1))/(-N*alpha*(1+alpha)**(N-1))]
        scaled_beta=max(N*abs(x) for x in pole_betas)
        minimum=mp.cos(mp.pi/N)**N
        for j in range(1,100):
            T=mp.mpf(j)/100
            assert abs(F(T))>=minimum-mp.mpf('1e-70')
            assert abs(F(T))<=1+mp.mpf('1e-70')
            scaled_beta=max(scaled_beta,N*abs((T-tt(T))/(1-F(T))))
        assert scaled_beta<10
        records.append({'N':N,'marked_flux_real':float(period.real),
                        'maximum_scaled_centralizer_shift_on_grid':float(scaled_beta),
                        'clock_modulus_lower_bound':float(minimum),
                        'midpoint_reparametrization_error':float(abs(tt(mp.mpf('0.5'))-mp.mpf('0.5')))})
    return records


def main():
    result={'actual_integral_divided_clock':actual_source_clocks(),
            'marked_flux_and_both_poles':flux_and_continuation(),
            'scope':'Single inserted Fr clock graph; no identification with the old head clock after Fourier gauge.'}
    path=Path(__file__).with_name('finite_frobenius_clock_graph_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,
                      'actual_clock_cases':len(result['actual_integral_divided_clock']),
                      'flux_levels':len(result['marked_flux_and_both_poles']),
                      'output':str(path)},indent=2))


if __name__=='__main__':
    main()
