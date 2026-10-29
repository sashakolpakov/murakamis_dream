#!/usr/bin/env python3
"""Exact pointed 5_2 four-plat reduction and proved cyclotomic transform.

The triple source sum is proved by literal transfer elimination. The
whole-meridian cyclotomic formula has a separate finite q-binomial
proof; this audit checks its agreement with the literal original state.
"""

import json
from pathlib import Path

import sympy as s

from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field,cut_entry_by_paths


ACTION=((1,1),(0,-1),(0,-1),(1,1),(1,1))
THREE_BRAID=[(0,1)]*3+[(1,1),(0,-1),(1,1)]


def literal_plat(entries,x):
    N=entries.N;p=entries.p;Q=entries.Q;d=N-1
    xv=pow(x,-1,p)*pow(Q,-1,p)%p
    g0=pow(x,-d,p)
    total=0;routes=0
    for a in range(N):
        # coev_L(x), coev_R(x), and the fourth-leg left-trace coupon g E00.
        initial=(a,d-a,d,0)
        top=N*N*pow(x,a-2*d,p)%p
        paths=[(initial,(),top)];colors=[x,xv,xv,x]
        for position,sign in ACTION:
            x1,x2=colors[position:position+2];following=[]
            for state,route,previous in paths:
                aa,bb=state[position:position+2]
                bound=min(aa,d-bb) if sign>0 else min(bb,d-aa)
                for k in range(bound+1):
                    coefficient=entries.direct(x1,x2,aa,bb,k,sign)
                    if not coefficient:continue
                    out=(bb+k,aa-k) if sign>0 else (bb-k,aa+k)
                    following.append((state[:position]+out+state[position+2:],
                                      route+(k,),previous*coefficient%p))
            paths=following
            colors[position],colors[position+1]=colors[position+1],colors[position]
        assert colors == [x,xv,xv,x]
        for state,route,previous in paths:
            if state[0]+state[1] != d or state[2]+state[3] != d:continue
            assert route[0] == 0 and route[3] == a and route[4] == 0
            k,l=route[1:3];assert a+k<N and 0<=l<=k
            # First pair is primal-dual (right cap); second is dual-primal (left cap).
            gb=pow(x,-d,p)*pow(Q,-state[0],p)%p
            cap1=pow(x,state[1],p)*gb*pow(N,-1,p)%p
            cap2=pow(x,state[2],p)*pow(N,-1,p)%p
            # Full mixed Cartan factors and the literal zero-framing twist.
            actual=previous*cap1*cap2*pow(xv,3*d,p)%p
            j=k-l;m=a+j;n=m+l;Y=Q*x*x%p
            predicted=pow(Y,2*(d-m),p)*pow(Q,j*(m+1)+m+l+2,p)\
                *entries.gaussian(m+l,l)*entries.gaussian(m,j)\
                *entries.pochhammer(Q*pow(Y,-1,p)%p,m+l)\
                *entries.pochhammer(pow(Q,j+1,p)*pow(Y,-1,p)%p,l)%p
            assert actual == predicted,(N,a,k,l,actual,predicted)
            total=(total+actual)%p;routes+=1
    return total,routes


def cyclotomic_formula(entries,Y):
    N=entries.N;p=entries.p;Q=entries.Q
    term=1;total=1
    for n in range(1,N):
        term=term*(Y+pow(Y,-1,p)-pow(Q,n,p)-pow(Q,-n,p))%p
        coefficient=sum(entries.gaussian(n,j)*pow(Q,-j*(n+1),p)
                        for j in range(n+1))%p
        coefficient=coefficient*pow(-1,n,p)*pow(Q,-n*(n+3)//2,p)%p
        total=(total+coefficient*term)%p
    return total


def complete_double_sum(entries):
    N=entries.N;p=entries.p;Q=entries.Q
    return sum(pow(Q,-n*(n+2)-j*(n+1),p)
               *entries.pochhammer(Q,n)**2*entries.gaussian(n,j)
               for n in range(N) for j in range(n+1))%p


def exact_normal_basis():
    Q,Y=s.symbols('Q Y',nonzero=True);checked=[]
    for n in range(7):
        T=s.prod(Y+1/Y-Q**r-Q**-r for r in range(1,n+1))
        contiguous=-Y**(n+1)*s.prod(1-Q**(-n+r)/Y for r in range(2*n+1))
        assert s.cancel((1-Y)*T-contiguous) == 0
        checked.append(n)
    return checked


def topology_and_framing():
    T=s.Matrix([[1,1],[0,1]]);U=s.Matrix([[1,0],[1,1]])
    assert T*T*U*U*T*s.Matrix([0,1]) == s.Matrix([7,3])
    A,N=s.symbols('A N');d=N-1;B=2*d-A
    colors=[A,B,B,A];orientations=[1,-1,-1,1];cartan=0;writhe=0
    for position,sign in ACTION:
        cartan+=sign*colors[position]*colors[position+1]/2
        writhe+=sign*orientations[position]*orientations[position+1]
        colors[position],colors[position+1]=colors[position+1],colors[position]
        orientations[position],orientations[position+1]=orientations[position+1],orientations[position]
    assert writhe == 5
    zero_framed=cartan-writhe*(A*A-2*d*A)/2
    assert s.expand(zero_framed-3*d*B) == 0
    return {'rational_tangle_slope':[7,3],'oriented_writhe':5,
            'Cartan_plus_zero_framing_exponent':'3(N-1)*alpha_dual',
            'source':'fourth-leg D0=g E00 in left pivotal trace'}


def main():
    cases=[];top_rows=[]
    for N in range(2,11):
        p,g,q=field(N);Q=q*q%p
        for M in (1,pow(g,2,p),pow(g,3,p)):
            E=MixedEntries(N,p,q);x=-M*pow(q,-1,p)%p;Y=M*M%p
            actual,routes=literal_plat(E,x)
            cyclotomic=cyclotomic_formula(E,Y)
            assert actual == cyclotomic
            if M==1:
                assert actual == complete_double_sum(E)
            old=None
            if N<=7:
                old=cut_entry_by_paths(N,p,q,x,3,THREE_BRAID)
                assert old == actual
            cases.append({'level':N,'meridian':M,'literal_source_value':actual,
                          'surviving_routes':routes,'original_three_braid_compared':old is not None,
                          'proved_cyclotomic_value_agrees':True,
                          'original_complete_double_sum_checked':M==1})
        d=N-1
        top=Q*sum(E.gaussian(d,j) for j in range(N))%p
        top_formula=pow(-1,d,p)*pow(Q,-d*(d+3)//2,p)\
            *sum(E.gaussian(d,j)*pow(Q,-j*(d+1),p) for j in range(N))%p
        assert top == top_formula
        top_rows.append({'level':N,'top_Newton_coefficient':top,'proved_top_row_matches_cyclotomic_formula':True})
    result={'normalization':topology_and_framing(),
            'literal_source_checks':cases,'proved_top_Newton_rows':top_rows,
            'generic_normal_basis_checks':exact_normal_basis(),
            'theorem':'Exact actual whole-source triple sum and proved whole-meridian cyclotomic coefficient transform.',
            'cyclotomic_transform_status':'PROVED by finite qChu/Newton/root-Rogers identities.',
            'proof':'notes/five_two_cyclotomic_transform_proof.md',
            'scope':'5_2 source diagnostic toward arbitrary-bridge comparison; no broad volume theorem.'}
    out=Path(__file__).with_name('five_two_whole_source_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'literal_plat_cases':len(cases),
                      'original_three_braid_comparisons':sum(c['original_three_braid_compared'] for c in cases),
                      'proved_top_Newton_rows_checked':len(top_rows),
                      'cyclotomic_transform_status':'PROVED',
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
