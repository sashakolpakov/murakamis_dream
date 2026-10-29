#!/usr/bin/env python3
"""Literal R-matrix Ward currents, endpoints, and partial reindexing."""

from functools import cache
import json
from pathlib import Path

import sympy as sy

from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def generic_interior_checks():
    Q,A,B,C,x1,x2=sy.symbols('Q A B C x1 x2',nonzero=True)
    records=[]
    for sign in (-1,1):
        if sign>0:
            ratios=[B*C/x2*(1-x1*x1/A)/(1-x1*x1*C/A),
                    A/(x1*C)*(1-Q*B*C)/(1-Q*B),
                    -x2*A/(Q*x1*x1*B*C)*(1-Q*B*C)/(1-Q*C)
                        *(1-Q*x1*x1*C/A)]
        else:
            ratios=[x2/B*(1-Q*A*C)/(1-Q*A),
                    x1/A*(1-x2*x2/B)/(1-x2*x2*C/B),
                    (1-Q*A*C)*(1-Q*x2*x2*C/B)/(x2*(1-Q*C))]
        variables=[A,B,C]
        def ratio(da=0,db=0,dk=0):
            state={A:A,B:B,C:C};value=sy.Integer(1)
            for idx,amount in enumerate((da,db,dk)):
                variable=variables[idx]
                if amount<0:
                    state[variable]=state[variable]/Q
                    value/=ratios[idx].subs(state,simultaneous=True)
                elif amount>0:
                    value*=ratios[idx].subs(state,simultaneous=True)
                    state[variable]=Q*state[variable]
            return sy.cancel(value)
        Fward=(1-Q*A)*ratio(da=1)+A/x1*(1-Q*B)*ratio(db=1,dk=-sign)\
            -(1-B*C**sign)*ratio(dk=-sign)\
            -B*C**sign/x2*(1-Q*A*C**(-sign))
        Eward=x2/B*(1/x1-Q*x1/A)*ratio(da=-1)\
            +(1/x2-Q*x2/B)*ratio(db=-1,dk=sign)\
            -x1*Q*C**sign/A*(1/x2-x2/(B*C**sign))*ratio(dk=sign)\
            -(1/x1-Q*x1*C**sign/A)
        assert sy.cancel(Fward)==0
        assert sy.cancel(Eward)==0
        records.append({'crossing_sign':sign,'independent_rational_F_identity':True,
                        'independent_rational_E_identity':True})
    return records


def case(level,M1,M2,p,q):
    Q=q*q%p
    x1=-M1*pow(q,-1,p)%p;x2=-M2*pow(q,-1,p)%p
    entries=MixedEntries(level,p,q)
    def K(i,n):return (x1 if i==1 else x2)*pow(Q,-n,p)%p
    def f(n):return (1-pow(Q,n+1,p))%p if 0<=n<level-1 else 0
    def e(i,n):
        if not 1<=n<level:return 0
        M=M1 if i==1 else M2
        return (M*pow(Q,-n,p)-pow(M,-1,p))%p
    def ec(i,n):
        M=M1 if i==1 else M2
        return (M*pow(Q,-n,p)-pow(M,-1,p))%p
    @cache
    def r(sign,a,b,k):
        if not (0<=a<level and 0<=b<level):return 0
        maximum=min(a,level-1-b) if sign>0 else min(b,level-1-a)
        if not 0<=k<=maximum:return 0
        return entries.direct(x1,x2,a,b,k,sign)
    def R(sign,a,b,c,d):
        k=sign*(c-b)
        return r(sign,a,b,k) if d==a-sign*k else 0
    counts={'four_term_F':0,'four_term_E':0,'divergence_F':0,
            'divergence_E':0,'cyclic_wall_entries':0,'inserted_partial_identities':0}
    for sign in (-1,1):
        def JF(a,b,k):
            return (pow(K(1,a),-1,p)*f(b)*r(sign,a,b+1,k)
                    -f(b+sign*k)*r(sign,a,b,k))%p
        def DF(a,b,k):
            return (f(a)*r(sign,a+1,b,k)
                    +pow(K(1,a),-1,p)*f(b)*r(sign,a,b+1,k)
                    -(pow(K(2,b+sign*k),-1,p)*f(a-sign*k)
                      +f(b+sign*k))*r(sign,a,b,k))%p
        def JE(a,b,k):
            return (e(2,b)*r(sign,a,b-1,k)
                    -K(1,a-sign*k)*e(2,b+sign*k)*r(sign,a,b,k))%p
        def DE(a,b,k):
            return (K(2,b)*e(1,a)*r(sign,a-1,b,k)
                    +e(2,b)*r(sign,a,b-1,k)
                    -(K(1,a-sign*k)*e(2,b+sign*k)
                      +e(1,a-sign*k))*r(sign,a,b,k))%p
        for a in range(level):
            for b in range(level):
                for k in range(-1,level+1):
                    Fward=(f(a)*r(sign,a+1,b,k)
                        +pow(K(1,a),-1,p)*f(b)*r(sign,a,b+1,k-sign)
                        -f(b+sign*k-1)*r(sign,a,b,k-sign)
                        -pow(K(2,b+sign*k),-1,p)*f(a-sign*k)*r(sign,a,b,k))%p
                    Eward=(K(2,b)*e(1,a)*r(sign,a-1,b,k)
                        +e(2,b)*r(sign,a,b-1,k+sign)
                        -K(1,a-sign*k-1)*e(2,b+sign*k+1)*r(sign,a,b,k+sign)
                        -e(1,a-sign*k)*r(sign,a,b,k))%p
                    assert Fward==0,(level,M1,M2,sign,a,b,k,'F',Fward)
                    assert Eward==0,(level,M1,M2,sign,a,b,k,'E',Eward)
                    assert (DF(a,b,k)+JF(a,b,k-sign)-JF(a,b,k))%p==0
                    assert (DE(a,b,k)+JE(a,b,k+sign)-JE(a,b,k))%p==0
                    for name in ('four_term_F','four_term_E','divergence_F','divergence_E'):
                        counts[name]+=1
                for power in (0,1,2):
                    fsum=esum=0
                    for k in range(-2,level+2):
                        h=pow(Q,power*k,p)
                        fsum+=h*DF(a,b,k)+(pow(Q,power*(k+sign),p)-h)*JF(a,b,k)
                        esum+=h*DE(a,b,k)+(pow(Q,power*(k-sign),p)-h)*JE(a,b,k)
                    assert fsum%p==0 and esum%p==0
                    counts['inserted_partial_identities']+=2
                for c in range(level):
                    for d in range(level):
                        actual=(K(2,b)*ec(1,a)*R(sign,(a-1)%level,b,c,d)
                            +ec(2,b)*R(sign,a,(b-1)%level,c,d)
                            -K(1,d)*ec(2,(c+1)%level)*R(sign,a,b,(c+1)%level,d)
                            -ec(1,(d+1)%level)*R(sign,a,b,c,(d+1)%level))%p
                        kappa1=(M1-pow(M1,-1,p))%p
                        kappa2=(M2-pow(M2,-1,p))%p
                        wall=(kappa1*int(a==0)*K(2,b)*R(sign,level-1,b,c,d)
                            +kappa2*int(b==0)*R(sign,a,level-1,c,d)
                            -kappa2*int(c==level-1)*K(1,d)*R(sign,a,b,0,d)
                            -kappa1*int(d==level-1)*R(sign,a,b,c,0))%p
                        assert actual==wall,(level,sign,a,b,c,d,'wall')
                        counts['cyclic_wall_entries']+=1
    return counts


def complete_wall_cancellation(level,p,q,M):
    Q=q*q%p;x=-M*pow(q,-1,p)%p
    entries=MixedEntries(level,p,q);size=level**2
    def multiply(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(size))%p
                 for j in range(size)] for i in range(size)]
    R=[[0]*size for _ in range(size)]
    for a in range(level):
        for b in range(level):
            for k in range(min(a,level-1-b)+1):
                R[(b+k)*level+a-k][a*level+b]=entries.direct(x,x,a,b,k,1)
    W=[[0]*size for _ in range(size)]
    for a in range(level):
        for b in range(level):
            if a==0:W[(level-1)*level+b][a*level+b]=(x*pow(Q,-b,p))%p
            if b==0:W[a*level+level-1][a*level+b]+=1
    inverseK=[pow(x*x*pow(Q,-a-b,p)%p,-1,p)
              for a in range(level) for b in range(level)]
    pivot=[pow(x*pow(Q,-b,p)%p,1-level,p) for b in range(level)]
    records=[]
    for crossings,word in ((1,R),(3,multiply(multiply(R,R),R))):
        left=multiply(W,word);right=multiply(word,W)
        source=[[(left[i][j]-right[i][j])*inverseK[j]%p
                 for j in range(size)] for i in range(size)]
        for a in range(level):
            for b in range(level):
                assert sum(pivot[c]*source[a*level+c][b*level+c]
                           for c in range(level))%p==0
        records.append({'level':level,'complete_color':M==1,
                        'two_strand_crossings':crossings,
                        'ordinary_full_divided_wall_pushforward_zero':True})
    return records


def main():
    records=[]
    total={}
    for level in range(2,9):
        p,g,q=field(level);Q=q*q%p
        for M in (1,pow(g,3,p)):
            for M1,M2 in ((M,M),(M,pow(M,-1,p)),(M,pow(g,5,p))):
                counts=case(level,M1,M2,p,q)
                records.append({'level':level,'first_color_complete':M1==1,
                                'second_color_complete':M2==1,'counts':counts})
                for name,value in counts.items():total[name]=total.get(name,0)+value
        x=-pow(q,-1,p)%p
        entries=MixedEntries(level,p,q)
        divided=(x*pow(Q,-(level-1),p)*entries.direct(x,x,level-1,level-1,0,1)
                 -entries.direct(x,x,0,level-1,0,1))%p
        predicted=pow(x,-(level-1),p)*(pow(x,2-level,p)*pow(Q,2,p)-1)%p
        assert divided==predicted
        if level>=3:assert divided!=0
    cancellations=[]
    for level in range(2,6):
        p,g,q=field(level)
        for M in (1,pow(g,3,p)):
            cancellations.extend(complete_wall_cancellation(level,p,q,M))
    result={'actual_mixed_crossing_cases':records,'counts':total,
            'generic_interior_identities':generic_interior_checks(),
            'ordinary_full_divided_wall_cancellation':cancellations,
            'explicit_divided_complete_source_nonzero_from_level_three':True,
            'scope':'Local actual currents and linear partial pushforward; no global Bockstein survival.'}
    path=Path(__file__).with_name('local_r_ward_transfer_currents_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'actual_mixed_crossing_cases':len(records),'counts':total,
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
