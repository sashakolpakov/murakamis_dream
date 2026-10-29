#!/usr/bin/env python3
"""Root-unit seven-factorials, positive metric and retained partner normals.

Finite-field signs do not prove positivity; the note supplies the sine proof.
This audit does not assume an actual physical four-port/source bridge.
"""
import itertools
import json
import math
from pathlib import Path

import mpmath as mp

from audit_high_color_first_normal_r_degree import root_field


def forms(spins):
    a,b,c,d,e,f=spins
    faces=[(a,b,e),(c,d,e),(a,d,f),(b,c,f)]
    F=list(map(sum,faces))
    Q=[a+b+c+d,a+c+e+f,b+d+e+f]
    return faces,F,Q


def mul(a,b,p):
    return [sum(a[j]*b[k-j] for j in range(k+1))%p for k in range(len(a))]


def divide(a,b,p):
    assert b[0]%p
    out=[];iv=pow(b[0],-1,p)
    for k,x in enumerate(a):out.append((x-sum(b[j]*out[k-j] for j in range(1,k+1)))*iv%p)
    return out


def quantum_units(q,p,length,order=4):
    invfact=[pow(math.factorial(k),-1,p) for k in range(order)]
    rho=[(q-pow(q,-1,p)*(-1)**k)*invfact[k]%p for k in range(order)]
    return [divide([(pow(q,u,p)*pow(u,k,p)-pow(q,-u,p)*pow(-u,k,p))*invfact[k]%p for k in range(order)],rho,p)
            for u in range(length+1)]


def factorials_without(units,p,omitted):
    one=[1]+[0]*(len(units[0])-1);out=[one]
    for u in range(1,len(units)):
        out.append(out[-1] if u in omitted else mul(out[-1],units[u],p))
    return out


def germ(N,spins,q,p,order=4):
    D=N-1;faces,F,Q=forms(spins);lo,hi=max(F),min(Q)
    units=quantum_units(q,p,max(3*N,hi+1),order)
    regular=factorials_without(units,p,set())
    noN=factorials_without(units,p,{N})
    noN2N=factorials_without(units,p,{N,2*N})
    zero=[0]*order;C=zero.copy();T=zero.copy();S=zero.copy()
    for z in range(lo,hi+1):
        den=[1]+[0]*(order-1)
        indices=[z-x for x in F]+[x-z for x in Q]
        assert all(0<=u<=D for u in indices)
        for n in indices:den=mul(den,regular[n],p)
        raw=divide(regular[z+1],den,p)
        S=[(x+(-1)**(D+z)*y)%p for x,y in zip(S,raw)]
        val=divide((noN if z<=2*D else noN2N)[z+1],den,p)
        destination=C if z<=2*D else T
        destination[:]=[(x+(-1)**(D+z)*y)%p for x,y in zip(destination,val)]
    G=[(a+b)%p for a,b in zip(C,mul(units[2*N],T,p))]
    assert mul(units[N],G,p)==S
    return C,T,G,units


def value_case(N,spins,q,p,sine):
    D=N-1;faces,F,Q=forms(spins);lo,hi=max(F),min(Q)
    assert lo<=min(hi,2*D) and max(F)<=2*D and hi<3*N-1
    qnum=[(pow(q,u,p)-pow(q,-u,p))*pow(q-pow(q,-1,p),-1,p)%p for u in range(3*N+1)]
    fac=[1];noN=[1]
    for u in range(1,3*N+1):
        fac.append(fac[-1]*qnum[u]%p)
        noN.append(noN[-1] if u==N else noN[-1]*qnum[u]%p)
    root=positive=0
    for z in range(lo,min(hi,2*D)+1):
        indices=[z-x for x in F]+[x-z for x in Q]
        assert all(0<=u<=D for u in indices)
        den=math.prod(fac[u] for u in indices)%p
        root=(root+(-1)**(D+z)*noN[z+1]*pow(den,-1,p))%p
        positive=(positive+N*sine[z-D]*pow(math.prod(sine[u] for u in indices)%p,-1,p))%p
    assert root==positive
    metrics=[];squared_metric=1
    for tri,Fv in zip(faces,F):
        deficits=[Fv-2*ell for ell in tri]
        assert D<=Fv<=2*D and all(0<=u<=D for u in deficits)
        metric=(-1)**(Fv-D)*math.prod(fac[u] for u in deficits)*pow(noN[Fv+1],-1,p)%p
        sine_metric=math.prod(sine[u] for u in deficits)*pow(N*sine[Fv-D],-1,p)%p
        assert metric==sine_metric
        metrics.append(metric);squared_metric=squared_metric*metric%p
    assert (sum(F)-4*D)%2==0
    return root,root*root*squared_metric%p


def source_prefactor_orders(N,spins):
    a,b,c,d,e,f=spins;D=N-1
    small,large=min(a+d,b+c),max(a+d,b+c)
    n=small-f;t0=large-small;s=small+large
    assert D<=s<=2*D and n>=0
    assert t0+n<=D and s-D>=n
    numerator_zeros=sum((-(small+f+1)+k)%N==0 for k in range(n))
    assert numerator_zeros==int(2*f<D)
    return -numerator_zeros


def level(N):
    p,eta=root_field(N);q=eta*eta%p;D=N-1;M=D//2
    sine=[1]
    for r in range(1,N):
        sine.append(sine[-1]*(pow(q,r,p)-pow(q,-r,p))*pow(pow(eta,N,p),-1,p)%p)
    folded=[]
    for spins in itertools.product(range(M+1),repeat=6):
        if min(forms(spins)[1])>=D:
            value_case(N,spins,q,p,sine)
            assert source_prefactor_orders(N,spins)==(-1 if 2*spins[-1]<D else 0)
            folded.append(spins)
    assert folded
    selected=sorted(set([folded[0],folded[len(folded)//2],folded[-1]]))
    partner_values=partner_jets=0;nonzero_tail=0
    for base in selected:
        partners=sorted(set(tuple(D-v if bit else v for bit,v in zip(bits,base)) for bits in itertools.product((0,1),repeat=6)))
        for spins in partners:
            root,_=value_case(N,spins,q,p,sine);partner_values+=1
            if N<=7:
                C,T,G,units=germ(N,spins,q,p)
                assert G[0]==root and G[1]==(C[1]+units[2*N][1]*T[0])%p
                nonzero_tail+=bool(T[0]);partner_jets+=1
    # Genuine generic parameter, where division by [N] is a unit: all
    # Taylor coefficients of the factorization are checked, not just root values.
    for spins in selected:
        germ(N,spins,2,1000003)
    return {'N':N,'prime':p,'all_folded_supported_tuples':len(folded),
            'partner_value_and_face_metric_checks':partner_values,
            'four_coefficient_partner_germs':partner_jets,
            'partner_cases_with_nonzero_retained_tail_at_root':nonzero_tail,
            'true_denominator_indices_and_root_multiplicities':True,
            'actual_source_prefactor_paired_simple_orders':True}


def missing_current_example():
    N=4;p,eta=root_field(N);q=eta*eta%p
    C,T,G,units=germ(N,(2,2,2,2,2,1),q,p)
    sqrt2=(q+pow(q,-1,p))%p;imag=pow(eta,N,p)
    assert C[0]==sqrt2 and T[0]==(-1)%p
    current=(G[1]-C[1])%p
    assert current==8*sqrt2*imag%p and current!=0
    return {'N':N,'partner_labels':[2,2,2,2,2,1],'C0':'sqrt(2)','T0':-1,
            'missing_first_log_q_normal':'8 sqrt(2) i','exact_field_check':True}


def calibration(N,kind):
    with mp.workdps(80):
        D=N-1;j=(D+2)//3 if kind=='ideal' else D//2
        spins=(j,)*6;faces,F,Q=forms(spins);s=[mp.mpf(1)]
        for r in range(1,N):s.append(s[-1]*2*mp.sin(mp.pi*r/N))
        R=N*mp.fsum(s[z-D]/mp.fprod([s[z-x] for x in F]+[s[x-z] for x in Q]) for z in range(max(F),min(Q)+1))
        met=mp.fprod(mp.fprod(s[Fv-2*ell] for ell in tri)/(N*s[Fv-D]) for tri,Fv in zip(faces,F))
        W=R*mp.sqrt(met)
        lam=lambda t:mp.im(mp.polylog(2,mp.exp(2j*t)))/2
        target=3*lam(mp.pi/3) if kind=='ideal' else 8*lam(mp.pi/4)
        rate=mp.pi*mp.log(W)/N
        assert abs(rate-target)<12*mp.log(N)/N
        return {'N':N,'scaled_labels':str(mp.mpf(j)/N),'calibration':kind,
                'pi_log_W_over_N':mp.nstr(rate,25),'limiting_action_calibration':mp.nstr(target,25),
                'scope':'Positive factorial action only; no source or geometric identification assumed.'}


if __name__=='__main__':
    rows=[level(N) for N in range(3,11)]
    example=missing_current_example()
    profiles=[calibration(N,kind) for kind in ('ideal','rectified') for N in (24,48,96)]
    result={'status':'PASS','levels':rows,'retained_high_partner_normal':example,
            'metric_action_calibrations':profiles,
            'scope':'Independent seven-factorial/root-metric theorem; source-order corollary uses the separately proved actual four-port kernel. Low-fold complete germ and partner value cores are distinguished from retained high tails.'}
    Path(__file__).with_name('actual_supported_racah_common_phase_and_normal_metric_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS8 exhaustive folded levels /',sum(r['all_folded_supported_tuples'] for r in rows),
          'tuples /',sum(r['partner_value_and_face_metric_checks'] for r in rows),
          'partner metrics / exact missing normal /6 action calibrations')
