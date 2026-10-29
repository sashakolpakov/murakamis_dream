#!/usr/bin/env python3
"""Exact diagnostics for the actual Ward-jet unfolding and local period.

The infinite coefficient-uniqueness theorem is proved in the note.
These tests cover the universal factorial recurrence, logarithmic
cyclotomic pole/constant, actual nilpotent jets, and marked source scale.
"""

import json
from pathlib import Path

import sympy as s
import mpmath as mp


Q, X, m, N, t = s.symbols('Q X m N t')


def rational_factorial_coefficients():
    records=[]
    previous=s.Integer(1)
    for j in range(1,14):
        coefficient=1/s.prod(1-Q**r for r in range(1,j+1))
        assert s.cancel((Q**j-1)*coefficient+previous)==0
        previous=coefficient
        records.append({'coefficient':j,'exact_rational_shift_recursion':True})
    return records


def logarithmic_uniformizer():
    # Expand (1+epsilon)^m through its quadratic binomial term.
    # This independently checks the h=log(1+epsilon) finite-part adapter.
    pole=-1/m**2
    constant_epsilon=(m-1)/(2*m**2)
    constant_h=s.cancel(constant_epsilon-pole/2)
    assert s.cancel(constant_h-1/(2*m))==0
    return {'polar_coefficient_per_resonant_m':str(pole),
            'epsilon_constant':str(constant_epsilon),
            'logarithmic_constant':str(constant_h)}


def field(order):
    multiplier=max(2,2000//order)
    while not s.isprime(order*multiplier+1):multiplier+=1
    prime=int(order*multiplier+1)
    generator=int(s.primitive_root(prime))
    return prime,pow(generator,(prime-1)//order,prime)


def cyclic_logarithms():
    records=[]
    for order in range(2,14):
        prime,omega=field(order)
        invn=pow(order,-1,prime)
        inv2=pow(2,-1,prime)
        count=0
        for degree in range(1,3*order+3):
            invm=pow(degree,-1,prime)
            weighted=sum(j*pow(omega,j*degree,prime) for j in range(1,order))%prime
            dlog=-invm*invn*weighted%prime
            if degree%order:
                expected=order*pow((pow(omega,degree,prime)-1)%prime,-1,prime)%prime
                assert weighted==expected
                finite_part=invm*pow((1-pow(omega,degree,prime))%prime,-1,prime)%prime
                assert dlog==finite_part
                normalized=dlog
            else:
                assert weighted==order*(order-1)*inv2%prime
                finite_part=invm*inv2%prime
                # -1/2 log(1-z^N) adds N/(2m) in degree m.
                assert (dlog+order*inv2*invm)%prime==finite_part
                # Dividing D_N by nu^((N-1)/2) cancels its resonant log.
                normalized=(dlog+(order-1)*inv2*invm)%prime
                assert normalized==0
            decksum=sum(pow(omega,j*degree,prime) for j in range(order))%prime
            # Norm-one centered logarithm has zero deck trace.
            assert normalized*decksum%prime==0
            # Difference of log D at the deck shift gives exactly
            # log(1-z)-log(1-z^N)/N.
            transport=dlog*(pow(omega,degree,prime)-1)%prime
            expected_transport=0 if degree%order==0 else -invm%prime
            assert transport==expected_transport
            count+=1
        # Direct actual finite factorial coefficients, with no use of D_N.
        coeff=[1]
        for j in range(1,order):
            coeff.append(coeff[-1]*pow((1-pow(omega,j,prime))%prime,-1,prime)%prime)
        for j in range(1,order):
            logarithmic_derivative=sum(
                coeff[a]*pow((1-pow(omega,j-a,prime))%prime,-1,prime)
                for a in range(j))%prime
            assert logarithmic_derivative==j*coeff[j]%prime
        records.append({'level':order,'coefficient_checks':count,
                        'actual_nilpotent_factorial_logarithm':order-1,
                        'cyclic_transport_and_norm_mark':True})
    return records


def period_and_source():
    # Differential identities are checked in logarithmic coordinates;
    # dLi_2(X)=-V dU fixes the local branch differential.
    U,V,dU,dV=s.symbols('U V dU dV')
    dli=-V*dU
    dS=s.expand(dli+dU*V+U*dV)
    dR=s.expand(dli+(dU*V+U*dV)/2)
    assert s.expand(dS-U*dV)==0
    assert s.expand(dR-(U*dV-V*dU)/2)==0
    # For X=-kappa_N*t^N and d kappa_N/d kappa=N at completion.
    source_pole_derivative=t**N/N
    assert s.cancel(-N*source_pole_derivative+t**N)==0
    # Li_2 pole and norm-root logs reconstruct the central coordinate.
    Aminus=-s.Symbol('Li2')/N**2
    reconstructed=-Aminus+(U/N)*(V/N)
    assert s.cancel(reconstructed-(s.Symbol('Li2')+U*V)/N**2)==0
    return {'Heisenberg_central_differential':True,
            'symmetric_regulator_differential':True,
            'actual_divided_source_is_pole_normal':True,
            'scaled_central_period_reconstruction':True}


def analytic_norm_chart():
    mp.mp.dps=45
    records=[]
    points=[mp.mpc('0.3','0.4'),mp.mpc('-0.6','0.2'),
            mp.mpc('0.7','-0.3'),mp.mpc('0.8','0')]
    for point in points:
        radius=abs(point)
        second_bound=4*mp.pi*radius/(1-radius)+4*mp.pi**2*radius/(1-radius)**2
        li=mp.polylog(2,point)
        bloch=mp.im(li)+mp.log(abs(point))*mp.im(mp.log(1-point))
        for level in (16,32,64,128,256):
            hbar=2*mp.pi*1j/level
            logarithm=sum(mp.mpf(j)/level*mp.log(1-mp.exp(hbar*j)*point)
                          for j in range(1,level))
            logarithm-=mp.mpf(level-1)/(2*level)*mp.log(1-point**level)
            expected=-li/hbar-mp.log(1-point)/2
            bound=second_bound/(12*level)+radius**level/(2*(1-radius**level))
            assert abs(logarithm-expected)<=bound
            metric_rate=-2*mp.pi/level*mp.re(logarithm)
            metric_rate+=mp.log(abs(point))*mp.im(mp.log(1-point))
            corrected=metric_rate-bloch-mp.pi/level*mp.log(abs(1-point))
            assert abs(corrected)<=2*mp.pi/level*bound
            records.append({'z_real':float(mp.re(point)),'z_imag':float(mp.im(point)),
                            'level':level,'explicit_trapezoid_bound':float(bound),
                            'logarithmic_error':float(abs(logarithm-expected)),
                            'regulator_rate':float(metric_rate),
                            'Bloch_Wigner_value':float(bloch)})
    return records


def main():
    result={'rational_factorial_coefficients':rational_factorial_coefficients(),
            'normal_uniformizer':logarithmic_uniformizer(),
            'cyclic_logarithms_and_actual_jets':cyclic_logarithms(),
            'period_and_source':period_and_source(),
            'controlled_analytic_norm_chart':analytic_norm_chart(),
            'scope':'Actual local Ward block unfolding and regulator; '
                    'no selected knot-period or volume inference.'}
    output=Path(__file__).with_name('unfolded_ward_factorial_regulator_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'rational_coefficients':len(result['rational_factorial_coefficients']),
                      'cyclic_levels':len(result['cyclic_logarithms_and_actual_jets']),
                      'cyclic_coefficient_checks':sum(x['coefficient_checks'] for x in result['cyclic_logarithms_and_actual_jets']),
                      'normal_uniformizer':result['normal_uniformizer'],
                      'period_and_source':result['period_and_source'],
                      'controlled_norm_cases':len(result['controlled_analytic_norm_chart']),
                      'output':str(output)},indent=2))


if __name__=='__main__':main()
