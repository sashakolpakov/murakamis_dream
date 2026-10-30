#!/usr/bin/env python3
"""Actual primitive word identities; freeness argument is analytical."""
import json
from pathlib import Path
import sympy as s


def main():
    b,c=s.symbols('b c',nonzero=True);I=s.eye(2)
    A=-s.Matrix([[1,1],[0,1]]);B=-s.Matrix([[1,0],[-4,1]])
    P=B*A;H=P+I;S=I+H/2;C=I+b*H
    assert H*H==s.zeros(2)
    assert P.inv()-I==-2*S
    assert S*B*S.inv()==A
    assert S.inv()*B*S==B*A*B.inv()
    output=C*B*C.inv()
    for eps,core in [(0,B),(1,A),(-1,B*A*B.inv())]:
        mu=C.inv()*S**eps
        assert s.simplify(mu-(I+(s.Rational(eps,2)-b)*H))==s.zeros(2)
        assert s.simplify(output-mu.inv()*core*mu)==s.zeros(2)
        tau=2*s.I*c/(1-eps*s.I*c)
        assert s.simplify(s.Rational(eps,2)+1/tau+s.I/(2*c))==0
    W=s.simplify(B.inv()*output)
    assert s.expand(s.trace(W))==2+16*b*b
    assert s.simplify(s.trace(W).subs(b,-s.I/(2*c))-(2-4/c**2))==0
    Z=s.simplify(W.subs(b,-s.I/2)+I)
    assert Z==s.Matrix([[2*s.I,-1],[-4,-2*s.I]]) and Z*Z==s.zeros(2)
    result=dict(status='PASS',nilpotent_and_half_turn_identities=4,
                all_parity_actual_word_and_primitive_identities=9,
                target_trace_identities=2,nontrivial_parabolic_endpoint=1,
                scope='Exact marked words and trace; complete deck-action exclusion is an analytical argument. No strict c<1 or source asymptotic.')
    Path(__file__).with_name('actual_matching_circle_rectangle_bound_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
