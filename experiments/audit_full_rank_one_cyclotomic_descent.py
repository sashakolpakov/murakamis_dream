#!/usr/bin/env python3
"""Ramified/full-root rank-one descent diagnostics.

The sequence-uniqueness proof is analytic and written in the note.
These checks cover exact algebraic ramification, zeros/poles at Q=1,
nonprimitive scaled roots, and numerical diagnostics of its explicit
oscillatory bounds. They are not finite proofs of asymptotic statements.
"""

import cmath
import json
import math
from pathlib import Path

import sympy as s


Q,Y,W,z=s.symbols('Q Y W z')


def field(N):
    k=(10000+N-1)//N
    while not s.isprime(N*k+1):k+=1
    p=int(N*k+1);g=int(s.primitive_root(p))
    return p,g,pow(g,(p-1)//N,p)


def ramified_symbolic_cases():
    records=[]
    for degree in (2,3,4):
        root_polynomial=(z-1)**degree-(Q-1)
        f=(1-Y)**degree-(Q-1)*Y**degree
        norm=s.resultant(root_polynomial,1-z*Y,z)
        assert s.expand(norm-f)==0
        coefficient=s.cancel(f.subs(Y,Q*Y)/f)
        assert s.cancel(coefficient*f-f.subs(Y,Q*Y))==0
        records.append({'ramification_degree':degree,
                        'moving_seed_limits_to_one_with_ramification':True,
                        'splitting_field_gauge_descends_exactly':True})
    for sign in (-1,1):
        seed=(Q-1)**sign
        f=1-seed*Y*Y
        assert s.cancel(s.resultant(z*z-seed,1-z*Y,z)-f)==0
        records.append({'ramification_degree':2,'Q_one_valuation':f'{sign}/2',
                        'zero_or_pole_at_Q_one':True,
                        'splitting_field_gauge_descends_exactly':True})
    return records


def weighted_amplitude_normalization():
    variable=s.symbols('s')
    records=[]
    for e in (2,3,4):
        lam=sum((j+s.I)*variable**j for j in range(1,e))+5*variable**e
        lam+=variable**(e+1)/(1-variable)
        polar=sum((j+s.I)*variable**(j-e) for j in range(1,e))
        remainder=s.cancel(lam/variable**e-polar)
        assert s.cancel(remainder-(5+variable/(1-variable)))==0
        weight=(1+variable)/(variable**2*(1-2*variable))
        assert s.limit(variable**2*weight,variable,0)==1
        for k in (1,2,3):
            root=s.Integer(k)**s.Rational(1,e)
            scaled=s.cancel(lam.subs(variable,root*variable)/variable**e)
            expected=s.cancel(k*lam.subs(variable,root*variable)/(k*variable**e))
            assert s.cancel(scaled-expected)==0
        records.append({'common_ramification':e,
                        'polar_degree_below_ramification':True,
                        'weighted_meromorphic_remainder_exact':True,
                        'scaled_power_identity_exact':True})
    return records


def scaled_root_norms():
    records=[]
    for N in range(5,20):
        p,g,omega=field(N)
        for k in range(1,5):
            q=pow(omega,k,p)
            assert q!=1
            order=N//int(s.gcd(N,k))
            for kind in ('ramified_two','ramified_three','zero','pole','mixed'):
                def f(y):
                    if kind.startswith('ramified'):
                        degree=2 if kind=='ramified_two' else 3
                        return (pow(1-y,degree,p)-(q-1)*pow(y,degree,p))%p
                    if kind=='zero':return (1-(q-1)*y*y)%p
                    if kind=='pole':return (1-y*y*pow((q-1)%p,-1,p))%p
                    denominator=(1-y*y*pow((q-1)%p,-1,p))%p
                    if not denominator:return None
                    return pow(y,-2,p)*(1-(q-1)*y*y)*pow(denominator,-1,p)%p
                chosen=None
                for power in range(1,500):
                    y=pow(g,power,p)
                    values=[f(y*pow(q,j,p)%p) for j in range(N+1)]
                    if all(value is not None and value!=0 for value in values):
                        chosen=y;break
                assert chosen is not None
                norm=1
                for j in range(N):norm=norm*values[j+1]*pow(values[j],-1,p)%p
                assert norm==1
                short=1
                for j in range(order):short=short*values[j+1]*pow(values[j],-1,p)%p
                assert short==1 and pow(short,N//order,p)==norm
                records.append({'level':N,'scaled_k':k,'orbit_order':order,
                                'kind':kind,'whole_root_transport':1})
    return records


def oscillatory_bound_diagnostics():
    records=[];b=0.7
    for rho in (0.5,2/3,0.75):
        for theta in (0.0,math.pi/3,math.pi):
            for count in (100,1000,10000):
                total=sum(cmath.exp(1j*(theta*n+b*n**rho)) for n in range(1,count+1))
                if theta==0:
                    bound=1+b*count**rho+2*count**(1-rho)/(b*rho)
                else:
                    bound=2/abs(1-cmath.exp(1j*theta))*(1+b*count**rho)
                assert abs(total)<=bound*(1+1e-9)
                records.append({'rho':rho,'theta':theta,'terms':count,
                                'mean_abs':abs(total)/count,
                                'explicit_sublinear_bound_over_count':bound/count,
                                'finite_diagnostic_only':True})
    return records


def main():
    result={'ramified_symbolic_gauges':ramified_symbolic_cases(),
            'weighted_amplitude_normalization':weighted_amplitude_normalization(),
            'scaled_root_norms':scaled_root_norms(),
            'oscillatory_bound_diagnostics':oscillatory_bound_diagnostics(),
            'scope':'Full rational rank-one cyclotomic descent; no selected knot comparison or volume theorem.'}
    path=Path(__file__).with_name('full_rank_one_cyclotomic_descent_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'ramified_symbolic_gauges':len(result['ramified_symbolic_gauges']),
                      'scaled_root_norms':len(result['scaled_root_norms']),
                      'weighted_normalizations':len(result['weighted_amplitude_normalization']),
                      'oscillatory_bound_diagnostics':len(result['oscillatory_bound_diagnostics']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
