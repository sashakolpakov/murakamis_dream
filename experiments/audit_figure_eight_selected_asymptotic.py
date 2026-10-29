#!/usr/bin/env python3
"""Selected positive figure-eight period, its density and first correction.

The all-level source identity is proved independently in its companion
note. Numerical asymptotic diagnostics are distinguished from exact
symbolic coefficient checks; they are not an all-knot volume theorem.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as s


def exact_local_coefficients():
    x=s.symbols('x',real=True)
    f=2*s.log(2*s.sin(s.pi*x))
    amplitude=2*s.sin(s.pi*x)
    point=s.Rational(5,6)
    A=-s.diff(f,x).subs(x,point)
    B=s.diff(f,x,2).subs(x,point)
    C=s.diff(f,x,3).subs(x,point)
    a0=amplitude.subs(x,point)
    a1=s.diff(amplitude,x).subs(x,point)
    a2=s.diff(amplitude,x,2).subs(x,point)
    boundary=s.pi*s.cot(s.pi*point)/6
    correction=s.simplify(boundary+a2/(2*A*a0)+a1*B/(2*A*A*a0)
                          +C/(8*A*A)+5*B*B/(24*A**3))
    assert A==2*s.pi*s.sqrt(3)
    assert B==-8*s.pi*s.pi
    assert C==-16*s.pi**3*s.sqrt(3)
    assert correction==11*s.pi/(36*s.sqrt(3))
    t=(1+s.sqrt(3)*s.I)/2
    residue=-1/(2*t-1)
    assert s.simplify(residue*s.conjugate(residue)-s.Rational(1,3))==0
    return {'maximum_point':'5/6','negative_Hessian':str(A),
            'selected_leading_coefficient':'3^(-1/4)',
            'first_relative_correction':str(correction),
            'algebraic_squared_density_modulus_squared':'1/3',
            'leading_density_matches_exact_selected_coefficient':True}


def positive_period_diagnostics():
    mp.mp.dps=90
    geometric=mp.exp(mp.pi*mp.j/3)
    volume=2*mp.im(mp.polylog(2,geometric))
    lobachevsky=mp.im(mp.polylog(2,mp.exp(mp.pi*mp.j/3)))/2
    phi=2*lobachevsky/mp.pi
    assert abs(2*mp.pi*phi-volume)<mp.mpf('1e-80')
    correction=11*mp.pi/(36*mp.sqrt(3))
    rows=[]
    for N in (20,40,80,160,320,640,1280):
        logs=[mp.mpf('0')]
        for k in range(1,N):
            logs.append(logs[-1]+mp.log(4*mp.sin(mp.pi*k/N)**2))
        maximum=max(logs)
        log_period=maximum+mp.log(mp.fsum(mp.exp(v-maximum) for v in logs))
        ratio=mp.exp(log_period-N*phi-mp.mpf('1.5')*mp.log(N)+mp.log(3)/4)
        remainder=N*N*(ratio-1-correction/N)
        assert abs(remainder)<2
        rows.append({'level':N,'volume_rate':mp.nstr(2*mp.pi*log_period/N,25),
                     'ratio_to_normalized_geometric_character':mp.nstr(ratio,25),
                     'N_times_first_relative_error':mp.nstr(N*(ratio-1),25),
                     'N_squared_remainder_after_first_correction':mp.nstr(remainder,25)})
    return {'marked_complete_volume':mp.nstr(volume,60),
            'first_correction_target':mp.nstr(correction,35),
            'diagnostics':rows}


def main():
    result={'exact_local_coefficients':exact_local_coefficients(),
            'selected_period_numerics':positive_period_diagnostics(),
            'scope':'Actual figure-eight source with independently proved all-level identity; asymptotic numerics only validate the direct proof.'}
    path=Path(__file__).with_name('figure_eight_selected_asymptotic_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'symbolic_leading_density_and_first_correction':True,
                      'positive_period_diagnostics':len(result['selected_period_numerics']['diagnostics']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
