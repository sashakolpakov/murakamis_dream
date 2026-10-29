#!/usr/bin/env python3
"""Uniform reciprocal-source factorial certificates and partner values.

The proof uses exact polynomial/factorial exponent cancellation, genuine
cyclic turns, saturated analytic source lattices and projector residues.
Value tests do not assert equality of generic normals.
"""
import itertools
import json
from pathlib import Path

import sympy as sp
import numpy as np

from audit_actual_general_four_port_single_racah_kernel import facs,single_kernel
from audit_actual_supported_racah_common_phase_and_normal_metric import (
    forms,value_case,germ,mul,divide,factorials_without,root_field,
)


class FM:
    def __init__(self,phase=0,sign=0,rho=0,factors=None):
        self.phase=sp.expand(phase);self.sign=sp.expand(sign);self.rho=sp.expand(rho)
        self.factors={sp.expand(k):v for k,v in (factors or {}).items() if v and sp.expand(k)!=0}
    def mul(self,other,power=1):
        data=self.factors.copy()
        for k,v in other.factors.items():
            data[k]=data.get(k,0)+power*v
            if not data[k]:del data[k]
        return FM(self.phase+power*other.phase,self.sign+power*other.sign,self.rho+power*other.rho,data)


def F(n,power=1):return FM(factors={sp.expand(n):power})
def tr(n):return n*(n-1)/2
def sf(n):return FM(phase=-tr(n),rho=-n).mul(F(n))


def source_prefactor(A,B,C,D,E,G,first):
    s=(A+B+C+D)/2;H=(A+B+C-D)/2
    Gmax=A+D if first else B+C;L=A if first else H
    n=(Gmax-G)/2;t0=s-Gmax;U=(C+E-D)/2;V=(D-C+E)/2;m=(A+B-E)/2
    chi=FM(U*(E-U-1)-C*V,U).mul(F(U)).mul(F(D)).mul(F((C+D-E)/2),-1).mul(F(E),-1)
    if first:
        k=E-U
        endpoint=FM(-A*B+2*A*m-m*m-m+k*(E-B),m).mul(F(m+k)).mul(F(m),-1).mul(F(k),-1)
    else:
        endpoint=FM(m*(A-2*B+m-1),m).mul(F(H)).mul(F(B)).mul(F(A-m))
        for r in (m,U,B-m,A):endpoint=endpoint.mul(F(r),-1)
    i0=(A+G-D)/2;mbc=(B+C-G)/2;mda=(D+A-G)/2
    beta=FM(A-2*i0+mbc*(B-2*C+mbc-1)-A*D+2*D*mda-mda*(mda+1),A+mbc+mda)
    beta=beta.mul(F(C)).mul(F(B-mbc)).mul(F(C-mbc),-1).mul(F(B),-1)
    J=FM(-n*(B+1)).mul(F(L)).mul(F(B-H+L)).mul(F(L-n),-1).mul(F(B-H+L-n),-1)
    a,b,c,d=(A,B,C,D) if first else (B,A,D,C)
    R=((C+D-E)/2,(A+B-E)/2,t0,(a-b+E)/2,(d-c+E)/2)
    S0=FM(-tr(s+1)+sum(tr(r) for r in R),s,-1).mul(F(s+1))
    for r in R:S0=S0.mul(F(r),-1)
    M=(Gmax+G)/2+1
    normal=FM(n+2*n*(t0+n)).mul(F(M)).mul(F(s+1-n)).mul(F(t0))
    for r in (G+1,s+1,n,t0+n):normal=normal.mul(F(r),-1)
    result=chi.mul(endpoint)
    for obj in (beta,J,S0,normal):result=result.mul(obj,-1)
    return result


def face(A,B,E):
    obj=FM()
    for r in ((A+B-E)/2,(A+E-B)/2,(B+E-A)/2):obj=obj.mul(sf(r))
    return obj.mul(sf((A+B+E)/2+1),-1)


def qdim(E):return FM(-E,rho=-1).mul(F(E+1)).mul(F(E),-1)


def uniform_prefactor_certificate():
    A,B,C,D,E,G=sp.symbols('A B C D E G')
    expected=qdim(E).mul(qdim(G))
    for triple in ((A,B,E),(C,D,E),(B,C,G),(D,A,G)):expected=expected.mul(face(*triple))
    rows=[]
    for first,second in itertools.product((True,False),repeat=2):
        actual=source_prefactor(A,B,C,D,E,G,first).mul(source_prefactor(B,C,D,A,G,E,second))
        ratio=actual.mul(expected,-1)
        assert not ratio.factors, (first,second,ratio.factors)
        assert sp.expand(ratio.phase)==0 and sp.expand(ratio.rho)==0
        # Channel parities E=A+B mod2, G=B+C mod2 make this even.
        sign=sp.expand(ratio.sign)
        assert sp.expand(sign-(E+G-3*A-2*B-C-2*D))==0
        rows.append({'Gmax_first_pair':first,'cyclic_Gmax_first_pair':second,
                     'all_factorial_exponents_cancel':True,'zeta_exponent_difference':0,
                     'one_minus_Q_exponent_difference':0,'remaining_sign_exponent':str(sign),
                     'remaining_sign_is_even_by_channel_parities':True})
    return rows


def generic_cyclic_sources():
    q,p=2,1000003;factorials=facs(q,30,p);families=0;entries=0
    for A,B,C,D in itertools.product(range(4),repeat=4):
        if (A+B+C+D)%2:continue
        es=list(range(max(abs(A-B),abs(C-D)),min(A+B,C+D)+1,2))
        gs=list(range(max(abs(B-C),abs(D-A)),min(B+C,D+A)+1,2))
        if not es:continue
        L=np.array([[single_kernel(A,B,C,D,E,G,q,p,factorials) for E in es] for G in gs],dtype=np.int64)
        R=np.array([[single_kernel(B,C,D,A,G,E,q,p,factorials) for G in gs] for E in es],dtype=np.int64)
        assert np.array_equal(R@L%p,np.eye(len(es),dtype=np.int64))
        families+=1;entries+=len(es)*len(gs)
    return {'actual_generic_external_families':families,'all_inverse_entries':entries,
            'true_cyclic_reciprocal_source_matrices_are_inverse':True}


def root_level(N):
    D=N-1;M=D//2;p,eta=root_field(N);q=eta*eta%p
    sine=[1]
    for r in range(1,N):sine.append(sine[-1]*(pow(q,r,p)-pow(q,-r,p))*pow(pow(eta,N,p),-1,p)%p)
    folded=partners=0;orders={0:0,1:0,2:0}
    for base in itertools.product(range(M+1),repeat=6):
        if min(forms(base)[1])<D:continue
        reference=value_case(N,base,q,p,sine)[1];folded+=1
        choices=sorted(set(tuple(D-v if bit else v for bit,v in zip(bits,base))
                           for bits in itertools.product((0,1),repeat=6)))
        for spins in choices:
            assert value_case(N,spins,q,p,sine)[1]==reference
            a,b,c,d,e,f=spins
            for x,I in ((e,range(max(abs(a-b),abs(c-d)),min(a+b,c+d)+1)),
                        (f,range(max(abs(b-c),abs(d-a)),min(b+c,d+a)+1))):
                collision=[k for k in I if (k-x)%N==0 or (k+x+1)%N==0]
                assert collision==sorted(set((x,D-x))), (N,spins,x,collision)
            order=int(2*e!=D)+int(2*f!=D)
            orders[order]+=1;partners+=1
    return {'N':N,'prime':p,'all_supported_folded_sextuples':folded,
            'distinct_partner_value_checks':partners,'actual_full_channel_collision_classes':True,
            'projector_trace_pole_budgets':orders}


def normalized_metric_jet(N,spins,q,p):
    C,T,G,units=germ(N,spins,q,p,3)
    noN=factorials_without(units,p,{N});ordinary=factorials_without(units,p,set())
    out=mul(G,G,p)
    faces,F,_=forms(spins)
    for tri,total in zip(faces,F):
        numerator=[1,0,0]
        for j in tri:numerator=mul(numerator,ordinary[total-2*j],p)
        delta=divide(numerator,noN[total+1],p)
        delta=[(-1)**(total-(N-1))*v%p for v in delta]
        out=mul(out,delta,p)
    return out,C,T,G,units


def retained_normal_counterexample():
    N=4;p,eta=root_field(N);q=eta*eta%p
    base=(1,)*6;flipped=(2,1,1,1,1,1)
    low,*_=normalized_metric_jet(N,base,q,p)
    high,*_=normalized_metric_jet(N,flipped,q,p)
    assert q==762 and p==1009
    assert low[:2]==[2,994] and high[:2]==[2,426]
    assert (high[1]-low[1])%p==441
    _,C,T,G,units=normalized_metric_jet(N,(2,2,2,2,2,1),q,p)
    current=(G[1]-C[1])%p
    sqrt2=(q+pow(q,-1,p))%p;imag=pow(eta,N,p)
    assert T[0] and current==8*sqrt2*imag%p and current
    # Exact complete two-channel Ward sum retains every partner jet.
    ward=[0,0,0]
    for e,f in itertools.product((1,2),repeat=2):
        spins=(1,1,1,1,e,f)
        metric,_,_,_,units=normalized_metric_jet(N,spins,q,p)
        weight=mul(units[2*e+1],units[2*f+1],p)
        term=mul(weight,metric,p)
        ward=[(a+b)%p for a,b in zip(ward,term)]
    assert ward[0]==ward[1]==0
    return {'N':N,'prime':p,'q_image':q,'folded':base,'single_partner':flipped,
            'normalized_metric_value_both':2,'first_log_zeta_coefficients':[994,426],
            'nonzero_first_normal_difference_mod_prime':441,
            'five_high_partner_tail_current':'8 sqrt(2) i',
            'complete_weighted_double_partner_first_normal_Ward_sum':ward,
            'generic_jet_symmetry_is_not_claimed_and_is_false':True}


if __name__=='__main__':
    rows=uniform_prefactor_certificate()
    cyclic=generic_cyclic_sources()
    roots=[root_level(N) for N in range(3,11)]
    normal=retained_normal_counterexample()
    result={'status':'PASS','uniform_generic_reciprocal_source_certificates':rows,
            'literal_generic_cyclic_sources':cyclic,'root_partner_value_families':roots,
            'retained_first_normal_counterexample':normal,
            'scope':'Uniform actual reciprocal-source normalization and all64 root VALUE reflection via saturated analytic channel projectors. Generic jets are not invariant; explicit first-normal counterexample and [2N] current retained.'}
    Path(__file__).with_name('actual_racah_partner_reflection_identity_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS4 uniform factorial/phase certificates;',cyclic['actual_generic_external_families'],'actual cyclic families;',
          sum(v['distinct_partner_value_checks'] for v in roots),'all-partner values; exact nonzero normal counterexample')
