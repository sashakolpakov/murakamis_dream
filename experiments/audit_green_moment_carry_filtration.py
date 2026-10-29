#!/usr/bin/env python3
"""Exact universal checks of actual index moments and relative normal jets."""

import json
import math
from pathlib import Path

import sympy as s


def falling_binomial(x,h):
    return s.expand(s.prod(x-r for r in range(h))/math.factorial(h))


def newton_moments():
    n,j,t,anchor,k=s.symbols('N j t anchor k')
    records=[]
    for h in range(7):
        p=falling_binomial(k,h)
        actual=s.Integer(1)
        for r in range(h):
            actual=s.expand((j-r)*actual+n*t*s.diff(actual,t)+n*anchor*t*actual)
        actual=s.expand(actual/math.factorial(h))
        delta=p
        expected=s.Integer(0)
        for m in range(h+1):
            expected+=delta.subs(k,j)*(anchor*t)**m/math.factorial(m)
            delta=s.expand(delta.subs(k,k+n)-delta)
        assert s.expand(actual-expected)==0
        falling=s.Integer(1)
        for r in range(h):
            falling=s.expand(-r*n*falling+n*t*s.diff(falling,t)+n*anchor*t*falling)
        assert s.expand(falling-(n*anchor*t)**h)==0
        records.append({'actual_green_binomial_degree':h,
                        'Newton_number_kernel_identity':True,
                        'step_N_falling_factorial':True})
    return records


def exponential_jet(h,a):
    return s.Matrix(h+1,h+1,lambda n,r:
                    s.binomial(n,r)*a**(n-r) if n>=r else 0)


def normal_jet_complex():
    sigma=s.symbols('sigma')
    records=[]
    for h in range(6):
        th=s.zeros(h+1)
        for n in range(1,h+1):th[n,n-1]=n
        ep=exponential_jet(h,sigma)
        em=exponential_jet(h,-sigma)
        assert ep*em==s.eye(h+1)
        assert s.simplify(s.diff(ep,sigma)-th*ep)==s.zeros(h+1)
        checks=0
        for r in range(h+1):
            for degree in range(3):
                f=s.zeros(h+1,1);f[r]=sigma**degree
                bulk=s.diff(f,sigma)-th*f
                result=(em*bulk).applyfunc(lambda v:s.integrate(v,(sigma,0,1)))
                result-=exponential_jet(h,-1)*f.subs(sigma,1)
                result+=f.subs(sigma,0)
                assert result==s.zeros(h+1,1)
                checks+=1
        records.append({'jet_order':h,'relative_endpoint_checks':checks,
                        'endpoint_U_binomial_adapter':True})
    return records


def coefficient_normal_rows():
    n,j,k,u,c=s.symbols('N j k u c',nonzero=True)
    records=[]
    for h in range(6):
        p=falling_binomial(k,h)
        jets=s.symbols(f'f0:{h+1}')
        f=sum(jets[r]*u**r/math.factorial(r) for r in range(h+1))
        delta=p
        converted=s.Integer(0)
        rhs=s.Integer(0)
        for r in range(h+1):
            value=delta.subs(k,j)
            converted+=value*(u/c)**r/(math.factorial(r)*n**r)
            rhs+=c**(h-r)*value*jets[h-r]/(math.factorial(r)*math.factorial(h-r)*n**r)
            delta=s.expand(delta.subs(k,k+n)-delta)
        lhs=c**h/math.factorial(h)*s.diff(s.expand(converted*f),u,h).subs(u,0)
        assert s.expand(lhs-rhs)==0
        records.append({'actual_moment_degree':h,'all_coefficient_normal_jets_retained':True})
    return records


def irregular_clock_and_source():
    z,n=s.symbols('z N',nonzero=True)
    records=[]
    for h in range(6):
        anchor=1/(n*(z-1))
        g=exponential_jet(h,anchor)
        gi=exponential_jet(h,-anchor)
        gamma=s.zeros(h+1);gamma[0,0]=1
        assert gamma*g==gamma
        transformed=gi*gamma*g
        expected=s.zeros(h+1)
        for r in range(h+1):expected[r,0]=(-anchor)**r
        assert s.simplify(transformed-expected)==s.zeros(h+1)
        count=0
        for m in (-2,-1,0,1,2,3):
            dilation=s.diag(*(z**(m*r) for r in range(h+1)))
            actual=gi*dilation*g
            ratio=(z**m-1)/(n*(z-1))
            predicted=exponential_jet(h,ratio)*dilation
            assert s.simplify(actual-predicted)==s.zeros(h+1)
            root=predicted.applyfunc(lambda v:s.limit(v,z,1))
            assert root==exponential_jet(h,s.Rational(m,1)/n)
            count+=1
        records.append({'jet_order':h,'whole_clock_powers':count,
                        'finite_vacuum_projector_pole_retained':True})
    return records


def main():
    result={'actual_index_moments':newton_moments(),
            'relative_jet_complex':normal_jet_complex(),
            'coefficient_normal_rows':coefficient_normal_rows(),
            'irregular_clock_and_source':irregular_clock_and_source(),
            'scope':'Exact polynomial/current and relative-source sector maps; no knot-period or geometric gluing comparison.'}
    out=Path(__file__).with_name('green_moment_carry_filtration_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'moment_degrees':len(result['actual_index_moments']),
                      'relative_jet_orders':len(result['relative_jet_complex']),
                      'relative_endpoint_checks':sum(r['relative_endpoint_checks'] for r in result['relative_jet_complex']),
                      'whole_clock_checks':sum(r['whole_clock_powers'] for r in result['irregular_clock_and_source']),
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
