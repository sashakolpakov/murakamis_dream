#!/usr/bin/env python3
"""Symbolic nonvanishing certificates for the actual complete phase chart."""
import json
from pathlib import Path
import sympy as s


def main():
    a,b,c,d,r,T,U,Z=s.symbols('a b c d r T U Z')
    prefix=s.Matrix([[a,b],[c,d]])
    A=-s.Matrix([[1,1],[0,1]])
    B=-s.Matrix([[1,0],[-4,1]])
    P=B*A; g=s.Matrix([[1,r],[0,1]])
    diagonal=[(g*Q*prefix*g.inv())[0,0] for Q in (s.eye(2),A,P)]
    bad=diagonal[0]*diagonal[1]+diagonal[1]*diagonal[2]+diagonal[0]*diagonal[2]
    assert s.factor(bad)==-(-a+c*r-c)**2
    assert s.trace(s.eye(2)+P+4*A)==-8
    aa,bb,cc=s.symbols('a0 a1 a2',nonzero=True)
    mapped={T:aa/cc,U:-aa/bb}
    assert s.factor((T+1-U).subs(mapped))==(aa*bb+aa*cc+bb*cc)/(bb*cc)
    assert s.factor((U*(T+1)-4*T).subs(mapped))==-aa*(aa+4*bb+cc)/(bb*cc)
    quadratic=s.expand(T*(-1-Z)**2*(U-Z)+(Z-1)**2*(T*Z+U))
    assert s.factor(s.discriminant(quadratic,Z))==16*T*U*(T-U+1)
    excluded={str(z):str(s.factor(quadratic.subs(Z,z))) for z in (0,1,-1,U,-U/T)}
    assert all(value!='0' for value in excluded.values())
    hi={T:1/T,U:U/T}
    assert s.cancel((T+1-U).subs(hi,simultaneous=True)-(T+1-U)/T)==0
    assert s.cancel((U*(T+1)-4*T).subs(hi,simultaneous=True)-(U*(T+1)-4*T)/T**2)==0
    result={
        'status':'PASS',
        'canonical_prefix_discriminant':'-(−a+c*r−c)^2; not identically zero for an invertible prefix',
        'leading_coefficient_matrix_trace':-8,
        'endpoint_discriminant':'16*T*U*(T+1-U)',
        'excluded_root_substitutions':excluded,
        'high_chamber_divisor_transform':'same zero loci after multiplication by units',
        'scope':'Regular geometric chart and unconstrained principal candidate; no physical support/cycle or asymptotic claim.'
    }
    Path(__file__).with_name('actual_augmented_plat_regular_geometric_phase_chart_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact generic-prefix chart, endpoint root exclusions and both-chamber divisors')


if __name__=='__main__':main()
