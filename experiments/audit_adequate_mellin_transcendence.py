#!/usr/bin/env python3
"""Exact truncation/valuation proof diagnostics for algebraic series.

Cases include a singular initial derivative and moving Q-extreme
coefficients. This tests the normalization argument, not an assumed
volume lower bound.
"""

import json
from pathlib import Path

import sympy as s


Q,X,Z,W,V=s.symbols('Q X Z W V')


def valuation(r,infinity=False):
    if r==0:return s.oo
    numerator,denominator=s.cancel(r).as_numer_denom()
    a=s.Poly(numerator,Q);b=s.Poly(denominator,Q)
    if infinity:return int(b.degree()-a.degree())
    return min(m[0] for m in a.monoms())-min(m[0] for m in b.monoms())


def coefficients(expr,maximum):
    return [s.cancel(s.expand(expr).coeff(X,n)) for n in range(maximum+1)]


def check_case(label,polynomial,series,m,maximum=14):
    series=s.series(series,X,0,maximum+1).removeO().expand()
    coeff=coefficients(series,maximum)
    k=m+1
    prefix=sum(coeff[n]*X**n for n in range(k))
    derivative=s.expand(s.diff(polynomial,Z).subs(Z,series))
    assert min(n for n in range(maximum+1) if derivative.coeff(X,n)!=0)==m
    F=s.cancel(polynomial.subs(Z,prefix+X**k*W)/X**(m+k)).expand()
    # Polynomiality is the nontrivial singular-derivative repair.
    s.Poly(F,X,W)
    at_zero=s.expand(F.subs(X,0))
    a=at_zero.coeff(W,1);b=at_zero.subs(W,0)
    assert a!=0 and s.expand(at_zero-a*W-b)==0
    w0=s.cancel(-b/a)
    assert s.cancel(w0-coeff[k])==0
    G=s.cancel(F.subs(W,w0+V)/a).expand()
    assert s.expand(G.subs(X,0)-V)==0
    H=s.cancel((G-V)/X).expand()
    hp=s.Poly(H,X,V)
    records=[]
    for infinity in (False,True):
        required=[s.ceiling(s.Rational(-valuation(c,infinity),i+1))
                  for (i,j),c in hp.terms() if c!=0]
        B=int(max([0]+required))
        pi=Q**-1 if infinity else Q
        scaled=s.expand(pi**B*H.subs(X,pi**B*X))
        assert all(valuation(c,infinity)>=0 for _,c in s.Poly(scaled,X,V).terms())
        A=max([0]+[-valuation(coeff[n],infinity)-B*n
                       for n in range(k+1) if coeff[n]!=0])
        assert all(valuation(c,infinity)>=-A-B*n for n,c in enumerate(coeff))
        # Independent coefficient recursion, truncated before products
        # grow; no expression-level fixed-point expansion is needed.
        depth=7;solved=[s.Integer(0)]*(depth+1)
        terms=s.Poly(scaled,X,V).terms()
        def power_coefficient(power,degree):
            current=[s.Integer(1)]+[s.Integer(0)]*degree
            for _ in range(power):
                current=[s.expand(sum(current[j]*solved[i-j] for j in range(i+1)))
                         for i in range(degree+1)]
            return current[degree]
        for n in range(1,depth+1):
            solved[n]=s.cancel(-sum(h*power_coefficient(j,n-i-1)
                                    for (i,j),h in terms if n-i-1>=0))
        assert all(s.cancel(solved[r]-coeff[k+r]*pi**(B*r))==0
                   for r in range(1,depth+1))
        assert all(valuation(c,infinity)>=0 for c in solved)
        records.append({'valuation':'infinity' if infinity else 'zero',
                        'rescaling_B':B,'finite_prefix_A':int(A),
                        'integral_recursion_and_linear_bound_exact':True})
    return {'case':label,'derivative_order_m':m,'truncation_k':k,
            'unit_linear_derivative_after_truncation':True,'valuation_checks':records}


def main():
    a=Q**-2+Q**3
    catalan=(1-s.sqrt(1-4*a*X))/(2*a*X)
    cases=[('Catalan_with_two_Q_extremes',Z-1-a*X*Z**2,catalan,0),
           ('rational_with_two_Q_scales',(1-Q**-2*X-Q**3*X**2)*Z-1,
             1/(1-Q**-2*X-Q**3*X**2),0),
           ('singular_derivative_order_one',Z**2-Q**-4*X**2*(1+a*X),
             Q**-2*X*s.sqrt(1+a*X),1),
           ('singular_derivative_order_three',(Z-1-Q*X)**2-Q**-4*X**6*(1+a*X),
             1+Q*X+Q**-2*X**3*s.sqrt(1+a*X),3)]
    results=[check_case(*case) for case in cases]
    # The explicit adequate formula remains quadratic after Q=q^2.
    n,c,v=s.symbols('n c v')
    span=c*(n-1)**2/s.Integer(2)+(v-2)*(n-1)/2
    assert s.expand(span).coeff(n,2)==c/2
    output={'algebraic_series_valuation_cases':results,
            'adequate_Q_span_quadratic_coefficient':'crossings/2',
            'scope':'Pointed generic transcendence from degree span; no generic affine nonsplitting or volume lower bound.'}
    path=Path(__file__).with_name('adequate_mellin_transcendence_results.json')
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'algebraic_series_cases':len(results),
                      'zero_and_infinity_integral_recursion_checks':2*len(results),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
