#!/usr/bin/env python3
"""Exact actual-crossing Bloch specialization for the figure-eight.

The shape lists are computed from the original Hurwitz representation
and prefix/Gauss coordinates in Q(sqrt(-3)). Numerical regulators only
validate the separately supplied elementary functional-identity proof.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as s

from audit_actual_normal_stationary_period import crossing


def exact_shapes():
    field=s.QQ.algebraic_field(s.sqrt(-3))
    reduce=lambda z:field.to_sympy(field.from_sympy(s.cancel(z)))
    matrix=lambda A:A.applyfunc(reduce)
    z=(1+s.sqrt(-3))/2
    riley=1-z
    A=s.Matrix([[1,1],[0,1]])
    B=s.Matrix([[1,0],[riley,1]])
    C=matrix(A.inv()*B*A*B.inv()*A)
    frame=s.Matrix([[2,-1],[-2,2]])
    Hs=[matrix(-frame.inv()*mu*frame) for mu in (A,B,C)]
    previous=s.eye(2);states=[]
    for H in Hs:
        G=matrix(previous*H*previous.inv())
        k,e=G[0,0],G[0,1]
        f=reduce(G[1,0]/k)
        states.append((k,e,f))
        previous=matrix(s.Matrix([[1,0],[-k*f,k]])*previous)
    initial=list(states)
    expected=[[1,1,-1,1,-1],
              [-1,s.Rational(-1,2),2*z,s.Rational(1,2),-z],
              [z-1,z,1,-1,z],
              [1-z,s.Rational(1,2),2,(1-z)/2,1]]
    lists=[]
    for index,(position,sign) in enumerate([(0,1),(1,-1)]*2):
        k,e,f=states[position];l,g,h=states[position+1]
        aa=reduce(-1/k);bb=reduce(-1/l)
        cc=reduce(1/(1-e*h) if sign>0 else 1-k*g*f/l)
        shapes=([bb,cc,1/aa,bb*cc,cc/aa] if sign>0
                else [aa,cc,1/bb,aa*cc,cc/bb])
        shapes=list(map(reduce,shapes))
        assert all(reduce(a-b)==0 for a,b in zip(shapes,expected[index]))
        lists.append(shapes)
        states[position:position+2]=[
            tuple(map(reduce,state))
            for state in crossing(states[position],states[position+1],sign)]
    assert all(reduce(a-b)==0 for u,v in zip(states,initial) for a,b in zip(u,v))
    residue=reduce(-1/(2*riley-1))
    assert reduce(residue-1/s.sqrt(-3)) == 0
    assert s.simplify(residue*s.conjugate(residue)-s.Rational(1,3)) == 0
    return z,riley,lists,residue


def parabolic_normal_form():
    t=s.symbols('t')
    A=s.Matrix([[1,1],[0,1]]);B=s.Matrix([[1,0],[t,1]])
    C=A.inv()*B*A*B.inv()*A
    initial=[A,B,C];moved=list(initial)
    for position,sign in [(0,1),(1,-1)]*2:
        a,b=moved[position:position+2]
        moved[position:position+2]=([a.inv()*b*a,a] if sign>0
                                   else [b,b*a*b.inv()])
    polynomials=[s.expand(x-y) for a,b in zip(moved,initial)
                 for x,y in zip(a,b) if s.expand(x-y) != 0]
    common=polynomials[0]
    for polynomial in polynomials[1:]:common=s.gcd(common,polynomial)
    common=s.Poly(common,t).monic().as_expr()
    assert common == t*t-t+1
    return str(common)


def regulator_checks(shapes):
    mp.mp.dps=85
    def number(value):
        value=s.sympify(value)
        return mp.mpc(str(s.N(s.re(value),mp.mp.dps)),str(s.N(s.im(value),mp.mp.dps)))
    def D(value):
        value=mp.mpc(value)
        # This is the normalized continuous regulator on real/degenerate terms.
        if not value.imag:return mp.mpf(0)
        return mp.im(mp.polylog(2,value))+mp.log(abs(value))*mp.arg(1-value)
    z=mp.exp(mp.pi*1j/3);eps=(1,1,1,-1,-1)
    local=[mp.fsum(e*D(number(a)) for a,e in zip(row,eps)) for row in shapes]
    actual=mp.fsum(local)
    regular=D(z)
    relations={'D(z/2)=5D(z)/6':D(z/2)-5*regular/6,
               'D(-z)=-2D(z)/3':D(-z)+2*regular/3,
               'D(2z)=D(z/2)':D(2*z)-D(z/2),
               'actual_crossing_regulator=2D(z)':actual-2*regular}
    assert max(abs(v) for v in relations.values()) < mp.mpf('1e-75')
    # Correct first asymptotic coefficient and its marked trace-field value.
    a=2*mp.pi*mp.sqrt(3);b=-8*mp.pi**2;c=-16*mp.pi**3*mp.sqrt(3)
    amplitude1=-mp.pi*mp.sqrt(3);amplitude2=-mp.pi**2
    euler=-mp.pi*mp.sqrt(3)/6
    correction=(euler+amplitude2/(2*a)+amplitude1*b/(2*a*a)
                +c/(8*a*a)+5*b*b/(24*a**3))
    assert abs(correction-11*mp.pi/(36*mp.sqrt(3))) < mp.mpf('1e-75')
    return {'actual_local_regulators':[str(v) for v in local],
            'actual_total_regulator':str(actual),
            'twice_regular_Bloch_value':str(2*regular),
            'largest_functional_identity_error':str(max(abs(v) for v in relations.values())),
            'first_positive_source_correction':str(correction)}


def main():
    z,riley,shapes,residue=exact_shapes()
    result={'coefficient_field':'Q(sqrt(-3))',
            'positive_regular_shape':str(z),
            'actual_geometric_Riley_embedding':str(riley),
            'actual_frame':[2,-2],
            'noncentral_parabolic_fixed_point_polynomial':parabolic_normal_form(),
            'actual_crossing_shape_lists':[[str(z) for z in row] for row in shapes],
            'shape_signs':[1,1,1,-1,-1],
            'marked_principal_residue':str(residue),
            'regulator_diagnostics':regulator_checks(shapes),
            'scope':'Exact actual Bloch specialization; degenerate normalized terms are zero. This frame is not used for Gaussian density.'}
    output=Path(__file__).with_name('figure_eight_bloch_specialization_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exact_actual_shapes':20,'regulator_identification':'2 D((1+sqrt(-3))/2)',
                      'marked_residue':str(residue),'output':str(output)},indent=2))


if __name__ == '__main__':main()
