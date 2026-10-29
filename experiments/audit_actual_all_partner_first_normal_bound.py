#!/usr/bin/env python3
"""Audit the positive generic presentation and all-partner first-normal route.

The uniform bounds and finite covering argument are proved in the note.
These are exact finite checks of their actual algebraic source formulas.
"""
import itertools
import json
import math
from pathlib import Path

from audit_actual_supported_racah_common_phase_and_normal_metric import (
    divide, factorials_without, forms, germ, mul, quantum_units, root_field,
)

FACES=((0,1,4),(2,3,4),(0,3,5),(1,2,5))
FACESETS={frozenset(f) for f in FACES}
PAIRS=((0,2),(1,3),(4,5))
PERMS=[p for p in itertools.permutations(range(6))
       if {frozenset(p[i] for i in f) for f in FACES}==FACESETS]
assert len(PERMS)==24


def face_supported(bits):
    high={i for i in range(6) if bits>>i&1}
    return any(high<=face for face in FACESETS)


def parameters(N,lab):
    a,b,c,d,e,f=lab;D=N-1
    p=min(a+d,b+c);s=a+b+c+d;h=max(abs(a-b),abs(c-d))
    n=p-f;t=p+f-D;t0=s-2*p;rA=a+b-h;rC=c+d-h
    assert p+h==max(a+c,b+d)
    assert 0<=n<=t<=D and 0<=n<=e-h and h+e+n<=D
    assert 0<=n<=min(rA,rC)<=max(rA,rC)<=D
    assert 0<=t0<=t0+n<=D
    ap,bp,cp,dp=(a,b,c,d) if a+d<=b+c else (b,a,d,c)
    R=(c+d-e,a+b-e,t0,ap-bp+e,dp-cp+e)
    assert all(0<=r<=D for r in R)
    assert 2*N<=s+1<3*N and 0<=s+1-2*N<n
    return p,s,h,n,t,t0,rA,rC,R


def orient(N,base,bits):
    D=N-1
    lab=tuple(D-x if bits>>i&1 else x for i,x in enumerate(base))
    if min(forms(lab)[2])<=2*D:
        return None
    high={i for i in range(6) if bits>>i&1}
    assert any(high<=face for face in FACESETS)
    pair=max(PAIRS,key=lambda ij:sum(lab[i] for i in ij))
    ff=next(i for i in pair if i in high)
    ee=next(i for i in pair if i!=ff)
    perm=next(p for p in PERMS if p[4]==ee and p[5]==ff)
    result=tuple(lab[i] for i in perm)
    a,b,c,d,e,f=result
    assert 2*e<=D<=2*f and e+f>=max(a+c,b+d)
    assert 2*min(a,b)<=D and 2*min(c,d)<=D
    parameters(N,result)
    return result


def exact_presentation(N,lab,order=4):
    p,eta=root_field(N);q=eta*eta % p;D=N-1
    small,s,h,n,t,t0,rA,rC,R=parameters(N,lab)
    e,f=lab[4:]
    one=[1]+[0]*(order-1)
    def power(u):
        return [pow(q,u,p)*pow(u,k,p)*pow(math.factorial(k),-1,p) % p
                for k in range(order)]
    def factor(u):
        return [(int(k==0)-v) % p for k,v in enumerate(power(u))]
    def product(values):
        result=one[:]
        for value in values:
            result=mul(result,value,p)
        return result
    def poch(start,length,omit=None):
        return product(factor(start+2*j) for j in range(length)
                       if start+2*j!=omit)
    G=[0]*order
    term_roots=[]
    for k in range(n+1):
        numerator=product([poch(-2*n,k),poch(-2*(small+f+1),k),
                           poch(2*(h+e+1),k),poch(2*(h-e),k),power(2*k)])
        denominator=product([poch(2,k),poch(2*(t0+1),k),
                             poch(-2*rA,k),poch(-2*rC,k)])
        assert denominator[0]
        term=divide(numerator,denominator,p)
        assert term[0] # every actual generic summand is a root unit
        G=[(a+b) % p for a,b in zip(G,term)]
        term_roots.append(term[0])
    units=quantum_units(q,p,3*N,order)
    normal=factorials_without(units,p,set())
    regular=factorials_without(units,p,{N,2*N})
    rho=[(a-b) % p for a,b in zip(power(1),power(-1))]
    prefnum=product([power(2*N-2*h*n),regular[s+1],poch(-2*rA,n),poch(-2*rC,n)])
    prefden=product([rho]+[normal[r] for r in R]+[poch(2,n),poch(-2*(s+1),n,omit=-4*N)])
    pref=divide(prefnum,prefden,p)
    pref=[(-1)**(D+s)*x % p for x in pref]
    transformed=mul(pref,G,p)
    C,T,original,_=germ(N,lab,q,p,order)
    assert transformed==original,(N,lab,transformed,original)
    # Independent sine/Newton factor conversion of EVERY root summand.
    ii=pow(eta,N,p);sine=[1]
    for u in range(1,N):
        sine.append(sine[-1]*(pow(q,u,p)-pow(q,-u,p))*pow(ii,-1,p) % p)
    cos=lambda j:(pow(q,2*j+1,p)+pow(q,-2*j-1,p)) % p
    for k,root in enumerate(term_roots):
        A=(sine[n]*sine[t]*sine[rA-k]*sine[rC-k]*sine[t0]) % p
        den=(sine[n-k]*sine[t-k]*sine[rA]*sine[rC]*sine[k]*sine[t0+k]) % p
        A=A*pow(den,-1,p) % p
        for j in range(k):A=A*(cos(h+j)-cos(e)) % p
        assert root==A
    return dict(N=N,labels=lab,degree=n,prime=p,
                literal_generic_coefficients_compared=order,
                common_phase_terms_checked=n+1,
                retained_tail_value_nonzero=bool(T[0]))


def star_route(N,base,bits):
    D=N-1;high={i for i in range(6) if bits>>i&1}
    assert len(high)==3 and not face_supported(bits)
    assert all(sum(i in high for i in pair)==1 for pair in PAIRS)
    lab=tuple(D-x if i in high else x for i,x in enumerate(base))
    _,F,Q=forms(lab)
    if min(Q)<=2*D:return 'tail_free'
    if F.count(max(F))>1:return 'repeated_maximum'
    face=FACESETS.intersection([frozenset(FACES[F.index(max(F))])]).pop()
    assert len(face&high)==2
    dual=high.symmetric_difference(set(range(6))-set(face))
    states=[sum(i in dual for i in pair) for pair in PAIRS]
    assert sorted(states)==[0,2,2]
    choices=[]
    for pair,state in zip(PAIRS,states):
        choices.append([set()] if state==0 else [set(),{pair[0]},{pair[1]}])
    targets=[set.union(*x) for x in itertools.product(*choices)]
    assert len(targets)==9 and all(len(x)<=2 for x in targets)
    assert all(any(x<=f for f in FACESETS) for x in targets)
    return 'fourier_then_two_Ward_squares'


def main():
    source_rows=[];branch_checks=0;live_faces=0;level_rows=[]
    star_counts={key:0 for key in ('tail_free','repeated_maximum','fourier_then_two_Ward_squares')}
    for N in range(3,13):
        D=N-1;M=D//2
        bases=[lab for lab in itertools.product(range(M+1),repeat=6)
               if min(forms(lab)[1])>=D]
        oriented=set();this_live=0
        for base in bases:
            for bits in range(64):
                if face_supported(bits):
                    branch_checks+=1
                    lab=orient(N,base,bits)
                    if lab is not None:
                        oriented.add(lab);this_live+=1
                elif bits.bit_count()==3 and all(sum(bits>>i&1 for i in pair)==1 for pair in PAIRS):
                    star_counts[star_route(N,base,bits)]+=1
        for lab in sorted(oriented):
            source_rows.append(exact_presentation(N,lab))
        live_faces+=this_live
        level_rows.append(dict(N=N,folded_bases=len(bases),
                               live_face_bit_branches=this_live,
                               distinct_oriented_generic_presentations=len(oriented)))
    result=dict(
        status='PASS',
        theorem_scope='All64 actual first-normal scalar bound; all fixed generic jets on face-supported and tail-free branches only.',
        supported_face_bit_classifications=branch_checks,
        live_face_bit_branches=live_faces,
        exact_full_generic_presentations=len(source_rows),
        exact_generic_coefficients_per_presentation=4,
        nonzero_retained_tail_presentations=sum(r['retained_tail_value_nonzero'] for r in source_rows),
        source_presentations=source_rows,levels=level_rows,
        all_high_star_routes=star_counts,
        source_identity='Original seven-factorial C+[2N]T equals explicitly zero-cancelled actual prefactor times entire positive 4phi3, through four literal Taylor coefficients.',
        limitations=['General higher-order partner jets are not inferred from the first-order Ward equation.',
                     'No completed physical recoupling norm or global volume equality is claimed.'])
    path=Path(__file__).with_name('actual_all_partner_first_normal_bound_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',branch_checks,'face classifications;',live_faces,'live faces;',
          len(source_rows),'four-jet actual generic presentations;',sum(star_counts.values()),'star reductions')

if __name__=='__main__':
    main()
