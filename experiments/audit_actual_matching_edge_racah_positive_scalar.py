#!/usr/bin/env python3
"""Actual all-physical four-port scalar, root jets, phases and pole budget."""
import json
import math
from pathlib import Path
import numpy as np
from audit_actual_supported_racah_common_phase_and_normal_metric import quantum_units, factorials_without, mul, divide
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_general_four_port_single_racah_kernel import facs,source,target,single_kernel,seven_factorial_kernel


def range_data(N,a,g):
    d=N-1
    F=[d+a,d+a,d+g,d+g];Q=[2*d,d+a+g,d+a+g]
    lo,hi=max(F),min(Q)
    assert d<=lo<=hi<=2*d
    for k in (a,g):assert 0<=k<=d and 0<=d-k<=d
    for z in range(lo,hi+1):
        assert all(0<=u<=d for u in [z-x for x in F]+[x-z for x in Q])
        assert (z+1)//N==1
    assert (4*d+2*a+2*g)%2==0
    n=d-g
    nv=sum((-d-g-1+k)%N==0 for k in range(n))
    dv=sum((k+1)%N==0 for k in range(n))*2+sum((-2*d-1+k)%N==0 for k in range(n))
    assert dv==0 and nv==int(2*g<d)
    assert (2*d+1)//N==1
    coefficient_order=-nv
    cup_pole=int(2*g>=N)
    assert not(nv and cup_pole) and nv+cup_pole<=1
    return F,Q,lo,hi


def root_level(N):
    p,eta=root_field(N);q=eta*eta%p;d=N-1;ii=pow(eta,N,p)
    units=quantum_units(q,p,2*N,order=4)
    regular=factorials_without(units,p,set());noN=factorials_without(units,p,{N})
    sf=[1]
    for r in range(1,N):sf.append(sf[-1]*(pow(q,r,p)-pow(q,-r,p))*pow(ii,-1,p)%p)
    assert sf[d]==N%p
    for r in range(N):assert sf[r]*sf[d-r]%p==N%p
    results={};count=terms=faces=0
    for a in range(d//2+1):
        for g in range(d+1):
            F,Q,lo,hi=range_data(N,a,g)
            G=[0]*4;raw=[0]*4
            for z in range(lo,hi+1):
                den=[1,0,0,0]
                for k in [z-v for v in F]+[v-z for v in Q]:den=mul(den,regular[k],p)
                term=divide(noN[z+1],den,p);full=divide(regular[z+1],den,p)
                sign=(-1)**(d+z)
                G=[(x+sign*y)%p for x,y in zip(G,term)]
                raw=[(x+sign*y)%p for x,y in zip(raw,full)]
            assert mul(units[N],G,p)==raw
            positive=0
            for r in range(max(0,a-g),min(a,d-g)+1):
                denominator=sf[g+r-a]*sf[r]*sf[a-r]%p
                tr=sf[g+r]*pow(denominator,-1,p)%p
                positive=(positive+tr*tr)%p;terms+=1
                rp=a-r;gp=d-g
                partner=sf[gp+rp]*pow(sf[gp+rp-a]*sf[rp]*sf[a-rp]%p,-1,p)%p
                assert tr==partner
            assert G[0]==positive
            face_jets=[]
            for k in (a,g):
                num=mul(mul(regular[k],regular[k],p),regular[d-k],p)
                D=[(-1)**k*x%p for x in divide(num,noN[d+k+1],p)]
                assert D[0]==1;face_jets.append(D);faces+=1
            H=mul(mul(G,face_jets[0],p),face_jets[1],p)
            assert H[0]==positive
            results[a,g]=G;count+=1
    differing=sum(results[a,g][1]!=results[a,d-g][1] for a,g in results)
    return dict(N=N,exact_root_germs=count,exact_termwise_partner_pairs=terms,
                exact_face_unit_jets=faces,root_equal_but_generic_derivative_different=differing)


def generic_source():
    p=1000003;q=2;families=entries=0
    for N in range(3,7):
        d=N-1;F=facs(q,8*N,p)
        targets=[target(d,d,d,d,2*g,q,p,F) for g in range(d+1)]
        for a in range(d//2+1):
            original=source(d,d,d,d,2*a,q,p,F)
            recovered=np.zeros_like(original)
            for g in range(d+1):
                L=single_kernel(d,d,d,d,2*a,2*g,q,p,F)
                fact=seven_factorial_kernel(d,d,d,d,2*a,2*g,q,p,F)
                assert L==fact
                recovered=(recovered+L*targets[g])%p;entries+=1
            assert np.array_equal(original,recovered)
            families+=1
    return dict(actual_generic_tensor_families=families,
                actual_all_channel_source_coefficients=entries)


def main():
    labels=0
    for N in range(3,51):
        for a in range((N-1)//2+1):
            for g in range(N):range_data(N,a,g);labels+=1
    rows=[root_level(N) for N in range(3,15)]
    assert sum(r['root_equal_but_generic_derivative_different'] for r in rows)>0
    result=dict(status='PASS',all_label_support_phase_pole_cases=labels,
                original_generic_source=generic_source(),root_levels=rows,
                scope='Exact all-physical matching-edge scalar, positive-square convention at both parities, retained generic jets, and simple-pole budget. No completed block norm or full-source asymptotic follows.')
    Path(__file__).with_name('actual_matching_edge_racah_positive_scalar_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',all_label_support_phase_pole_cases=labels,
                         **result['original_generic_source'],
                         **{k:sum(r[k] for r in rows) for k in rows[0] if k!='N'},scope=result['scope']),indent=2))

if __name__=='__main__':main()
