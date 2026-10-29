#!/usr/bin/env python3
"""Independent exact Newton-chart germ and Chebyshev normalization checks."""

import json
from pathlib import Path

import sympy as s


def main():
    y,w,tau,c3=s.symbols('y w tau c3')
    a,b=s.symbols('a b',real=True)
    Y,L=s.symbols('Y L',nonzero=True)
    u=(Y*L+1)/(Y+L)
    e=Y*(Y+L)*(Y*L+1)/(L*(Y**2-1)**2)
    x=Y+1/Y
    assert s.cancel(1-e*(2-u-1/u)-e*(x-2))==0
    assert s.cancel(u-u.subs({Y:1/Y,L:1/L},simultaneous=True))==0
    assert s.cancel(e-e.subs({Y:1/Y,L:1/L},simultaneous=True))==0
    # Divide numerator and denominator by their known vanishing orders
    # before formal division, retaining the cubic branch coefficient.
    numerator_u=(1+tau)/2+y*y*(c3/2+(1+tau)**3/48)
    denominator_u=(1-tau)/2+y*y*(-c3/2+(1-tau)**3/48)
    useries=s.series(-numerator_u/denominator_u,y,0,3).removeO()
    u0=(tau+1)/(tau-1)
    u2=(tau**3-tau-12*c3)/(6*(tau-1)**2)
    assert s.factor(useries-u0-u2*y*y)==0
    numerator_e=(1-tau*tau)/2+y*y*((1-tau**4)/24-tau*c3)
    denominator_e=2+s.Rational(2,3)*y*y
    eseries=s.series(numerator_e/denominator_e,y,0,3).removeO()
    e0=(1-tau*tau)/4
    assert s.cancel(eseries.subs(y,0)-e0)==0
    assert s.cancel(e0+u0/(u0-1)**2)==0
    assert s.simplify(s.im(u0.subs(tau,a+s.I*b))+2*b/((a-1)**2+b*b))==0
    # Even a constant u projection is transverse over r.
    ew=e0/(1+e0*w)
    rw=s.cancel(1-ew*(2-u0-1/u0))
    assert s.cancel(rw-ew*w)==0
    assert s.cancel(s.diff(rw,w).subs(w,0)-e0)==0
    records=[]
    X=s.symbols('X')
    C0,C1=s.Integer(2),X
    for level in range(1,16):
        if level>1:C0,C1=C1,s.expand(X*C1-C0)
        H=s.cancel((C1-2)/(X-2))
        assert s.Poly(H,X)
        assert H.subs(X,2)==level**2
        assert s.diff(C1,X,2).subs(X,2)/2==s.Rational(level**2*(level**2-1),12)
        # Polynomial projector modulo the complete source relation.
        projector=H/level**2
        remainder=s.rem(s.together(projector**2-projector),C1-2,X)
        assert s.expand(remainder)==0
        records.append({'level':level,'trace_adapter':level**2,
                        'quadratic_adapter':str(s.Rational(level**2*(level**2-1),12)),
                        'full_source_projector_mod_relation':True})
    result={'rational_chart_identity':True,'Weyl_invariance':True,
            'tau_and_cubic_branch_germ':True,'constant_u_transverse_example':True,
            'Chebyshev_and_projector_checks':records,
            'scope':'Geometric target and marked normal scales only; no actual selected-period claim.'}
    path=Path(__file__).with_name('newton_resolution_independent_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'germ_and_transversality_exact':True,
                      'Chebyshev_projector_levels':len(records),'output':str(path)},indent=2))


if __name__=='__main__':main()
