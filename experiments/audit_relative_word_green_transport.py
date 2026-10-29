#!/usr/bin/env python3
"""Exact checks of actual number, clock and projector relative lifts."""

import json
import math
from pathlib import Path

import sympy as s


def expjet(h,a):
    return s.Matrix(h+1,h+1,lambda n,r:
                    s.binomial(n,r)*a**(n-r) if n>=r else 0)


def choose_operator(a,degree):
    out=s.eye(a.rows)
    for r in range(degree):out=out*(a-r*s.eye(a.rows))
    return out/math.factorial(degree)


def zero(a):
    return a.applyfunc(s.expand)==s.zeros(a.rows,a.cols)


def main():
    n,j,sigma,a=s.symbols('N j sigma a')
    records=[]
    for h in range(6):
        exponential=expjet(h,sigma)
        inverse=expjet(h,-sigma)
        multiplication=s.zeros(h+1)
        for r in range(1,h+1):multiplication[r,r-1]=r
        number=s.diag(*(j+n*r for r in range(h+1)))
        lifted=number-n*sigma*multiplication
        assert zero(exponential*number*inverse-lifted)
        checks=0
        for degree in range(h+1):
            assert zero(exponential*choose_operator(number,degree)*inverse
                        -choose_operator(lifted,degree))
            checks+=1
        projector=s.zeros(h+1);projector[0,0]=1
        p_lift=exponential*projector
        assert zero(exponential*projector*inverse-p_lift)
        assert zero(p_lift*p_lift-p_lift)
        assert zero(s.diff(p_lift,sigma)-multiplication*p_lift+p_lift*multiplication)
        clock=s.diag(*(a**r for r in range(h+1)))
        assert zero(exponential*clock*inverse-expjet(h,sigma*(1-a))*clock)
        # A complete word containing a head projector and both actual
        # insertion types, rather than only one degree-zero coupon.
        word=clock*projector*number
        lifted_word=(exponential*clock*inverse)*p_lift*lifted
        assert zero(lifted_word-exponential*word*inverse)
        records.append({'normal_jet_order':h,'Green_binomial_moment_lifts':checks,
                        'whole_clock_and_internal_projector':True,
                        'ordered_word_composition':True})
    result={'relative_operator_checks':records,
            'scope':'Exact whole-source operator lift; no geometric generator or scalar volume claim.'}
    out=Path(__file__).with_name('relative_word_green_transport_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'jet_orders':len(records),
                      'moment_lifts':sum(r['Green_binomial_moment_lifts'] for r in records),
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
