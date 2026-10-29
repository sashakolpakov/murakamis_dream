#!/usr/bin/env python3
"""Actual integral-color periodicity and the Fourier--Mellin residue.

Integral Weyl matrices use the original finite R series at a root.
The checks include colors above N and multiples of N; they do not
assume Habiro expansion or a volume theorem.
"""

from functools import lru_cache
from itertools import product
import json
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field
from audit_regularized_kashaev_period import actual_laurent_period, evaluate


def integer(r,p,q):
    return (pow(q,r,p)-pow(q,-r,p))*pow((q-pow(q,-1,p))%p,-1,p)%p


def integral_ordinary_cut(level,n,p,q,strands,word):
    Q=q*q%p;x=pow(q,n-1,p);rho=(q-pow(q,-1,p))%p
    factorial=[1]
    for k in range(1,level):
        factorial.append(factorial[-1]*integer(k,p,q)%p)

    @lru_cache(None)
    def transitions(a,b,sign):
        answer=[];ep=fp=1
        maximum=min(a,n-1-b) if sign>0 else min(b,n-1-a)
        for k in range(min(maximum,level-1)+1):
            if k:
                es=a if sign>0 else b;fs=b if sign>0 else a
                ep=ep*integer(n-es+k-1,p,q)%p
                fp=fp*integer(fs+k,p,q)%p
            if sign>0:
                value=pow(q,k*(k-1)//2,p)*pow(rho,k,p)*pow(factorial[k],-1,p)*ep*fp
                value=value*pow(x,-a-b,p)*pow(Q,(a-k)*(b+k),p)%p
                pair=(b+k,a-k)
            else:
                value=pow(-1,k,p)*pow(q,-k*(k-1)//2,p)*pow(rho,k,p)*pow(factorial[k],-1,p)*ep*fp
                value=value*pow(x,a+b,p)*pow(Q,-a*b,p)%p
                pair=(b-k,a+k)
            if value:answer.append((pair,value))
        return answer

    total=0
    for closed in product(range(n),repeat=strands-1):
        initial=(0,)+closed;weight=1
        for a in closed:weight=weight*x*pow(Q,-a,p)%p
        paths={initial:weight}
        for i,sign in reversed(word):
            following={}
            for state,old in paths.items():
                for pair,c in transitions(state[i],state[i+1],sign):
                    target=state[:i]+pair+state[i+2:]
                    following[target]=(following.get(target,0)+old*c)%p
            paths=following
        total=(total+paths.get(initial,0))%p
    return total*pow(x,-sum(sign for i,sign in word),p)%p


def module_subquotients():
    records=[]
    for N in range(2,11):
        p,g,q=field(N)
        for n in range(1,3*N+2):
            k,r=divmod(n,N)
            target=r if r else N
            h=k*N if r else (k-1)*N
            for j in range(target):
                assert pow(q,n-1-2*j,p) == pow(q,h+target-1-2*j,p)
                if j:
                    assert integer(n-j,p,q) == pow(-1,h//N,p)*integer(target-j,p,q)%p
                if j+1<target:
                    assert integer(j+1,p,q) != 0
            if r:
                assert integer(n-r,p,q) == 0
            else:
                assert integer(N,p,q) == 0
            records.append({'level':N,'color':n,'target_dimension':target,
                            'one_dimensional_weight_shift':h,
                            'quotient_if_true_submodule_if_false':bool(r)})
    return records


def actual_periodicity():
    diagrams=[(2,[(0,1)]*3),
              (3,[(0,1),(1,-1)]*2),
              (3,[(0,1)]*3+[(1,1),(0,-1),(1,1)])]
    records=[];root_values=[]
    for N in range(2,7):
        p,g,q=field(N);Q=q*q%p
        for strands,word in diagrams:
            F=actual_laurent_period(N,p,q,strands,word)
            values={}
            for n in range(1,2*N+3):
                got=integral_ordinary_cut(N,n,p,q,strands,word)
                expected=evaluate(F,pow(Q,n,p),p)
                assert got == expected,(N,n,strands,word,got,expected)
                values[n]=got
                if n>N:assert got == values[n-N]
                records.append({'level':N,'color':n,'strands':strands,'crossings':len(word),
                                'whole_color_period_matches_original_ADO':True,
                                'multiple_of_level':n%N == 0})
            root_values.append((N,p,Q,values))
    return records,root_values


def residues(root_values):
    records=[]
    for N,p,Q,values in root_values:
        K=values[N]
        # Res at X=gamma of P/(1-X^N) dX/X is -P(gamma)/N.
        residue_sum=0
        for j in range(N):
            gamma=pow(Q,j,p)
            numerator=sum(values[r]*pow(gamma,r,p) for r in range(1,N+1))%p
            residue_sum=(residue_sum-numerator*pow(N,-1,p))%p
        assert -residue_sum%p == K
        records.append({'level':N,'sum_of_cyclotomic_residues':residue_sum,
                        'original_complete_value':K,'normalized_infinity_residue_exact':True})
    X=s.symbols('X')
    c1,c2,K=s.symbols('c1 c2 K')
    rational=(c1*X+c2*X*X+K*X**3)/(1-X**3)
    u=s.symbols('u')
    for n0 in (1,2,3,4,6):
        vals={1:c1,2:c2,0:K}
        low=sum(vals[n%3]*X**n for n in range(1,n0))
        tail=rational-low
        # Infinity residue after X=1/u.
        assert s.residue(-tail.subs(X,1/u)/u,u,0) == K
    return {'finite_field_actual_residues':records,
            'symbolic_infinity_residue_for_different_fixed_tails':5}


def main():
    modules=module_subquotients()
    periods,roots=actual_periodicity()
    result={'integral_root_subquotients':modules,
            'actual_periodicity':periods,
            'whole_root_residues':residues(roots),
            'scope':'Actual root rational Fourier--Mellin period and Kashaev residue; no regulator norm estimate.'}
    path=Path(__file__).with_name('cyclotomic_mellin_residue_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'integral_subquotient_checks':len(modules),
                      'actual_color_periods':len(periods),
                      'actual_root_residues':len(roots),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
