#!/usr/bin/env python3
"""Fourier--Mellin boundary sources with exact coefficient pointing.

Exact algebra tests use explicitly known recurrences. Literal small-color
knot matrices independently check the Q convention and Kashaev extraction.
No geometric symbol or volume theorem is assumed.
"""

import json
from pathlib import Path

import numpy as np
import sympy as s

from audit_finite_sum_annihilator import field,cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices


Q,Y,X=s.symbols('Q Y X',nonzero=True)


def mellin(operator,n0,colors):
    transformed={};source=0
    for j,a in operator.items():
        for term in s.Add.make_args(s.expand(a)):
            m=int(term.as_powers_dict().get(Y,0))
            coefficient=s.cancel(term/Y**m)
            transformed[m]=transformed.get(m,0)+coefficient*Q**(-m*j)*X**(-j)
            for r in range(n0,n0+j):
                source+=coefficient*Q**(-m*j)*X**(-j)*colors(r)*Q**(m*r)*X**r
    return {m:s.expand(a) for m,a in transformed.items()},s.expand(source)


def exact_source_cases():
    cases=[({0:-Q*Y*Y,1:1},lambda n:Q**(n*n),3),
           ({0:-(1-Q*Y),1:1},lambda n:s.prod(1-Q**r for r in range(1,n+1)),3),
           ({0:Q*Q*Y*Y*(Q*Q*Y*Y-1),1:-Q*(Q*Q*Y**4-1),2:Y*Y-1},
             lambda n:Q**(n*n)+2*Q**n,4)]
    records=[]
    maximum=12
    for operator,colors,n0 in cases:
        operator={j:s.sympify(a) for j,a in operator.items()}
        d=max(operator)
        for n in range(n0,9):
            assert s.expand(sum(a.subs(Y,Q**n)*colors(n+j) for j,a in operator.items()))==0
        transformed,source=mellin(operator,n0,colors)
        series=sum(colors(n)*X**n for n in range(n0,maximum+1))
        lhs=s.expand(sum(a*series.subs(X,Q**m*X) for m,a in transformed.items()))
        difference=s.expand(lhs-source)
        for power in range(n0-d,maximum-d+1):
            assert s.expand(difference.coeff(X,power))==0
        leading=s.expand(source).coeff(X,n0-d)
        expected=s.expand(colors(n0)*operator[d].subs(Y,Q**(n0-d)))
        assert s.expand(leading-expected)==0 and expected!=0
        for N in range(n0,maximum+1):
            assert s.expand(series.coeff(X,N)-colors(N))==0
        records.append({'operator_order':d,'start_color':n0,
                        'transformed_shift_orders':sorted(transformed),
                        'nonzero_source':str(source),
                        'bounded_boundary_window_and_coefficient_period_exact':True})
    return records


def ordinary_data(n,p,q):
    x=pow(q,n-1,p)
    positive,negative,_,_=color_matrices(n,p,q,x)
    pivot=np.diag([x*pow(q,-2*a,p)%p for a in range(n)]).astype(np.int64)
    return positive,negative,pivot,x


def actual_fixed_color_checks():
    diagrams=[(2,[(0,1)]*3),
              (3,[(0,1),(1,-1)]*2),
              (3,[(0,1)]*3+[(1,1),(0,-1),(1,1)])]
    records=[]
    for n in range(2,6):
        p,g,root=field(n)
        for strands,word in diagrams:
            generic=cut_matrix_dense(n,p,ordinary_data(n,p,g),strands,word)
            opposite=cut_matrix_dense(n,p,ordinary_data(n,p,-g%p),strands,word)
            assert np.array_equal(generic,opposite)
            ordinary=cut_matrix_dense(n,p,ordinary_data(n,p,root),strands,word)
            x=pow(root,n-1,p)
            ado=cut_matrix_dense(n,p,color_matrices(n,p,root,x),strands,word)
            assert np.array_equal(ordinary,ado)
            records.append({'color_and_root_level':n,'strands':strands,'crossings':len(word),
                            'generic_Q_parity_exact':True,
                            'actual_color_N_coefficient_equals_ADO_root_cut':True})
    return records


def main():
    result={'formal_source_equations':exact_source_cases(),
            'actual_small_color_checks':actual_fixed_color_checks(),
            'scope':'Actual coefficient-period source construction; no geometric symbol or volume theorem.'}
    path=Path(__file__).with_name('fourier_mellin_actual_source_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exact_source_equations':len(result['formal_source_equations']),
                      'actual_color_and_Q_parity_checks':len(result['actual_small_color_checks']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
