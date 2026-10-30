#!/usr/bin/env python3
"""Exact general seed identities and finite support/parity certificates."""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def exact_recurrences():
    X=sp.symbols('X', positive=True)
    B,Y=X,sp.Integer(1)
    rows=[]
    for s in range(2,15):
        denominator=B+X
        B,Y=sp.cancel((B*X+X*X-1)/denominator),sp.cancel(Y/denominator)
        assert sp.cancel(B-sp.chebyshevt(s,X)/sp.chebyshevu(s-1,X))==0
        assert sp.cancel(Y-1/sp.chebyshevu(s-1,X))==0
        assert sp.cancel(X*X+Y*Y-B*B-1)==0
        assert B.subs(X,1)==sp.Rational(1,s)
        assert Y.subs(X,1)==sp.Rational(1,s)
        rows.append(dict(s=s,B=str(B),Y=str(Y)))
    # The step itself is an identity for arbitrary angle; induction fixes
    # the allowed branch, not the finite number of rows above.
    a,b=sp.symbols('a b', real=True)
    h=sp.sin(a)
    lhs=sp.expand_trig((h*sp.cos(b)/sp.sin(b))*sp.cos(a)+sp.cos(a)**2-1)
    rhs=sp.expand_trig(h*sp.cos(a+b)/sp.sin(a+b)
                      *(h*sp.cos(b)/sp.sin(b)+sp.cos(a)))
    assert sp.trigsimp(sp.together(lhs-rhs))==0
    return rows


def support_checks():
    rows=[]
    for N in range(3,31):
        D=N-1;M=D//2
        for s in range(3,13):
            for output in range(N):
                remaining=output; labels=[]
                for _ in range(s):
                    value=min(remaining,M);labels.append(value);remaining-=value
                assert remaining==0
                partial=0
                for value in labels:
                    assert partial+value<=D
                    # Choosing the top output realizes a positive factor.
                    partial+=value
                assert partial==output
            rows.append(dict(N=N,s=s,all_outputs=True))
    return rows


def analytic_branch_diagnostics():
    rows=[]
    for s in range(3,21):
        for fraction in (mp.mpf('.1'),mp.mpf('.5'),mp.mpf('.9')):
            alpha=fraction*mp.pi/(s+1);X=mp.cos(alpha);h=mp.sin(alpha)
            B=h*mp.cot(s*alpha);Y=h/mp.sin(s*alpha)
            assert -Y<B<X and 0<X<1 and 0<Y<1
            leaf=mp.atan(1/X)/mp.pi
            upper=mp.atan(1/mp.cos(mp.pi/(s+1)))/mp.pi
            assert mp.mpf('.25')<leaf<upper
            assert upper<=mp.atan(mp.sqrt(2))/mp.pi+mp.mpf('1e-50')
            assert abs(X*X+Y*Y-B*B-1)<mp.mpf('1e-45')
            rows.append(dict(s=s,alpha_fraction=float(fraction),
                             leaf=float(leaf),proper_upper=float(upper)))
        if s>=4:
            X=mp.cos(mp.pi/s);h=mp.sin(mp.pi/s)
            assert abs(h*mp.cot((s-1)*mp.pi/s)+X)<mp.mpf('1e-44')
            assert mp.mpf('.25')<mp.atan(1/X)/mp.pi
            assert mp.atan(1/X)/mp.pi<=mp.atan(mp.sqrt(2))/mp.pi+mp.mpf('1e-50')
    return rows


def parity_certificates():
    # Each table value is (output pairing, added internal components).
    table={('I','I'):('I',0),('I','U'):('U',0),('I','X'):('X',0),
           ('U','I'):('U',0),('U','U'):('U',1),('U','X'):('U',0),
           ('X','I'):('X',0),('X','U'):('U',0),('X','X'):('I',0)}
    seed_rows=[]
    for s in range(3,31):
        outcomes=set()
        for word in (['X']*s,['U']+['X']*(s-1)):
            output=word[0];loops=0
            for value in word[1:]:
                output,extra=table[output,value];loops+=extra
            assert loops==0;outcomes.add(output)
        assert outcomes==({'U','X'} if s%2 else {'I','U'})
        seed_rows.append(dict(s=s,loop_free_types=sorted(outcomes)))
    sets=[{'I','U'},{'I','X'},{'U','X'},{'I','U','X'}]
    for left in sets:
        for right in sets:
            result={table[x,y][0] for x in left for y in right if not table[x,y][1]}
            assert len(result)>=2
    return dict(seed_types=seed_rows,closed_set_products=16)


def main():
    with mp.workdps(55):
        result=dict(status='PASS',exact_seed_recurrences=exact_recurrences(),
                    all_output_finite_support=support_checks(),
                    proper_seed_interval_diagnostics=analytic_branch_diagnostics(),
                    knot_parity=parity_certificates(),
                    scope='Exact recurrences and combinatorial source/parity checks; all-width strictness, geometry and source interfaces are proved in the note.')
    Path(__file__).with_name('actual_conway_arbitrary_width_seeds_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',recurrence_widths=len(result['exact_seed_recurrences']),
                         finite_support_families=len(result['all_output_finite_support']),
                         interval_samples=len(result['proper_seed_interval_diagnostics']),
                         parity_widths=len(result['knot_parity']['seed_types'])),indent=2))


if __name__=='__main__':
    main()
