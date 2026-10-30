#!/usr/bin/env python3
"""Literal regular complete-circle lift, marks and one retained trace normal.

Boundary domains and individual packet bounds have their own audits.
The finite-product estimate is proved by multiplication and Cauchy;
this audit checks its exact source interface rather than samples a
global period or replaces a full network by independent maxima.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_nc_morse_graph_first_normal_source_reduction import Local
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_actual_matching_edge_antidiagonal_operator_packet import factorials,clebsch,cup
from audit_general_matching_graph_full_normal_source import run


def coefficients():
    duals=jets=high=gamma_defects=mark=units=folds=paired=simple=0
    examples=[]
    for N in range(3,9):
        loc=Local(N);p,q0,d=loc.p,loc.q,N-1
        Jet.p=p;Jet.order=2;q=Jet([q0,q0]);F=factorials(q,d)
        physical_scale=N*q**(-d*d)
        nu=2*N*(-1)**N*pow((q0-pow(q0,-1,p))%p,-1,p)%p
        assert loc.nu==nu
        for a in range(d//2+1):
            L=2*a;m=d-a;s=d-2*a;gamma=Jet(loc.gamma[a])
            assert loc.gamma[a] and loc.h0[a] and loc.omega[a];units+=3
            P=loc.pi[a][0]@loc.W[a][0]%p
            if 2*a==d:
                assert np.array_equal(P,np.eye(L+1,dtype=np.int64));simple+=1
            else:
                assert not np.count_nonzero(P);paired+=1
            for r in range(L+1):
                sigma=m+r
                for i in range(max(0,sigma-d),min(d,sigma)+1):
                    j=sigma-i
                    direct=Jet([int(loc.pi[a][k][r,i*N+j]) for k in range(2)])
                    reversed_white=clebsch(d,a,q,F,d-j,d-i,L-r)
                    original_white=clebsch(d,a,q,F,i,j,r)
                    assert reversed_white==q**(s*(a-r))*original_white
                    expected=(cup(L,q,F,L-r)*reversed_white
                              /(gamma*cup(d,q,F,d-j,physical_scale)
                                *cup(d,q,F,d-i,physical_scale)))
                    assert direct==expected
                    duals+=1;jets+=2;high+=int(sigma>d)
                    moving_gamma=q**(2-a*a)/N**2
                    wrong=expected*gamma/moving_gamma
                    gamma_defects+=int(wrong.c[1]!=expected.c[1])
            if a==d//2:
                if N%2:assert loc.h0[a]==N%p
                else:
                    imaginary=pow(loc.eta,N,p)
                    sine=(q0-pow(q0,-1,p))*pow(2*imaginary,-1,p)%p
                    assert loc.h0[a]==2*N*pow(sine,-1,p)%p
                folds+=1
        for x in range(N):
            actual_mark=pow(q0,d*x,p)*pow(N*N,-1,p)%p
            actual_cap=int(loc.cap[0][d-x,x])
            expected=pow(N,-1,p)*pow(q0,-d*d,p)*pow(q0,2*d*x,p)%p
            assert actual_mark*pow(actual_cap,-1,p)%p==expected;mark+=1
        examples.append(dict(N=N,paired_root_nodes=(N-1)//2+(1 if N%2==0 else 0),
                             simple_fold_present=bool(N%2)))
    return dict(original_categorical_dual_coefficients=duals,retained_value_firstjet_coefficients=jets,
                actual_high_total_coefficients=high,nonzero_wrong_moving_gamma_defects=gamma_defects,
                scalar_root_units=units,maximal_fold_scalar_checks=folds,
                paired_zero_norms_retained=paired,simple_retractions_retained=simple,
                literal_mark_cap_ratios=mark,levels=examples)


def symbolic():
    N,a,x,y,sigma=sp.symbols('N a x y sigma')
    d=N-1;m=d-a
    i=N*x-sp.Rational(1,2);j=N*y-sp.Rational(1,2)
    r=i+j-m
    assert sp.expand(r-a-N*(x+y-1))==0
    assert sp.expand(2*a-r-(a-N*(x+y-1)))==0
    assert sp.expand((d-j)+(d-i)-(m+(2*a-r)))==0
    assert sp.expand(d-2*a-(m-a))==0
    # The marked row/cap quotient keeps the full integer character.
    mark_exponent=d*x;cap_exponent=d*d-d*x
    assert sp.expand(mark_exponent-cap_exponent-(-d*d+2*d*x))==0
    assert sp.expand(2*d*x-2*N*x+2*x)==0
    return dict(exact_affine_offset_and_dual_identities=4,exact_original_mark_characters=2)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    rows=[run(3,2,True),run(4,2,True)]
    result=dict(status='PASS',exact=coefficients(),symbolic=symbolic(),
                original_complete_sources=rows,
                fixed_label_trace_normals=sum(r['fixed_label_trace_normals_checked'] for r in rows),
                scope='Original regular W/pi lift, both folded parities, fixed root scalars and one retained physical trace normal. No global boundary contraction or period claim.')
    path=args.output or Path(__file__).with_name('actual_original_network_resonant_source_envelope_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
