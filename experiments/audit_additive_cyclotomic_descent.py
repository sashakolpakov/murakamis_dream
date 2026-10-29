#!/usr/bin/env python3
"""Exact pole-orbit and ramified additive curvature diagnostics."""

import json
from pathlib import Path

import sympy as s


Q,Y,U,M,z=s.symbols('Q Y U M z')


def universal_pole_coefficients():
    psi=M/(1-U);records=[]
    for r in range(1,7):
        assert s.simplify(s.limit((1-U)**r*psi,U,1)-M**r)==0
        records.append({'pole_order':r,'leading_orbit_coefficient':f'm^{r}',
                        'whole_universal_orbit_function':str(s.factor(psi))})
        psi=s.cancel(psi+M*U*s.diff(psi,U)/r)
    return records


def ramified_weighted_flow():
    root=s.sqrt(Q-1)
    f=(1-Y)**2-(Q-1)*Y**2
    first=(1+root)/(2*root)
    second=-(1-root)/(2*root)
    poles=first/(1-(1+root)*Y)+second/(1-(1-root)*Y)
    assert s.simplify(poles-1/f)==0
    c=s.cancel((1/f).subs(Y,Q*Y)-1/f)
    expected=first/(1-Q*(1+root)*Y)-first/(1-(1+root)*Y)
    expected+=second/(1-Q*(1-root)*Y)-second/(1-(1-root)*Y)
    assert s.simplify(c-expected)==0
    for r in (1,2,3):
        value=1/(1-Y)**r
        coefficient=s.cancel(value.subs(Y,Q*Y)-value)
        assert s.cancel(coefficient-((1-Q*Y)**-r-(1-Y)**-r))==0
    return {'ramified_partial_fraction_weights_have_Puiseux_poles':True,
            'weighted_orbit_charges_cancel_exactly':True,
            'rational_additive_primitive_recovered':str(1/f)}


def field(N):
    k=(10000+N-1)//N
    while not s.isprime(N*k+1):k+=1
    p=int(N*k+1);g=int(s.primitive_root(p))
    return p,g,pow(g,(p-1)//N,p)


def additive_scaled_sums():
    records=[]
    for N in range(5,20):
        p,g,omega=field(N)
        for k in range(1,5):
            q=pow(omega,k,p);order=N//int(s.gcd(N,k))
            for kind in ('high_poles_and_Laurent','ramified_weights','ramified_double_poles'):
                def b(y):
                    if kind=='high_poles_and_Laurent':
                        if (1-y)%p==0 or (1+y)%p==0:return None
                        return (pow((1-y)%p,-3,p)+2*pow((1+y)%p,-2,p)
                                +pow(q,-1,p)*y*y+q*pow(y,-1,p))%p
                    denominator=(pow(1-y,2,p)-(q-1)*y*y)%p
                    if not denominator:return None
                    return pow(denominator,-1 if kind=='ramified_weights' else -2,p)
                chosen=None
                for power in range(1,500):
                    y=pow(g,power,p)
                    values=[b(y*pow(q,j,p)%p) for j in range(N+1)]
                    if all(v is not None for v in values):
                        chosen=y;break
                assert chosen is not None
                total=sum(values[j+1]-values[j] for j in range(N))%p
                short=sum(values[j+1]-values[j] for j in range(order))%p
                assert total==0 and short==0
                records.append({'level':N,'scaled_k':k,'actual_orbit_order':order,
                                'kind':kind,'whole_additive_curvature':0})
    return records


def nonzero_Laurent_primitive():
    records=[]
    for exponent in (-3,-1,1,2,4):
        c=(Q+Q**-1)*Y**exponent
        primitive=c/(Q**exponent-1)
        assert s.cancel(primitive.subs(Y,Q*Y)-primitive-c)==0
        records.append({'Laurent_exponent':exponent,'primitive_exact':True})
    return records


def main():
    result={'universal_pole_coefficients':universal_pole_coefficients(),
            'ramified_weighted_flow':ramified_weighted_flow(),
            'additive_scaled_root_sums':additive_scaled_sums(),
            'nonconstant_Laurent_terms':nonzero_Laurent_primitive(),
            'scope':'Untwisted additive full-root descent; no unknown knot source comparison or volume theorem.'}
    path=Path(__file__).with_name('additive_cyclotomic_descent_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'universal_pole_orders':len(result['universal_pole_coefficients']),
                      'scaled_root_additive_checks':len(result['additive_scaled_root_sums']),
                      'ramified_weighted_partial_fractions_exact':True,
                      'Laurent_primitives':len(result['nonconstant_Laurent_terms']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
