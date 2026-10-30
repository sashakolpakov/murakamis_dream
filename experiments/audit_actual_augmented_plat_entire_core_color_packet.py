#!/usr/bin/env python3
"""Actual mixed-circle split and both-parity all-input cosine transforms."""
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_marked_multiport_chebyshev_source_packet import axis_apply


def level(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    d=N-1;M=d//2;rho=(q-pow(q,-1,p))%p
    Et,Ft,Kt=coproduct(rho*rho*E%p,F,K,2,N,p)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    identity=np.eye(N*N,dtype=np.int64)
    circles=[np.zeros_like(O),identity]
    if N>=2:circles.append(-O%p)
    for n in range(2,N):circles.append((-O@circles[-1]-circles[-2])%p)
    cheb=[identity,O*pow(2,-1,p)%p]
    for h in range(1,N-1):cheb.append((O@cheb[-1]-cheb[-2])%p)
    for h in range(N):
        core=pow(-1,h,p)*(cheb[h]@circles[N]%p)%p
        assert np.array_equal(circles[N-h],(core+pow(-1,N,p)*circles[h])%p)
        for crossing in (Rp,Rm):
            assert np.array_equal(crossing@circles[N-h]%p,
                                  (crossing@core+pow(-1,N,p)*crossing@circles[h])%p)
    cosine=np.zeros((N,M+1),dtype=np.int64)
    for h in range(N):
        for j in range(M+1):
            m=N-2*j-1
            cosine[h,j]=(pow(q,h*m,p)+pow(q,-h*m,p))*pow(2,-1,p)%p
            original=pow(-1,h,p)*(pow(q,h*(2*j+1),p)+pow(q,-h*(2*j+1),p))*pow(2,-1,p)%p
            assert int(cosine[h,j])==original
    weights=np.array([1 if N-2*j-1==0 else pow(2,-1,p) for j in range(M+1)],dtype=np.int64)
    assert np.array_equal(cosine.T@cosine%p,np.diag(N*weights%p))
    reproducing=cosine@np.array([pow(int(w),-1,p) for w in weights],dtype=np.int64)%p
    delta=np.zeros(N,dtype=np.int64);delta[0]=N%p
    assert np.array_equal(reproducing,delta)
    rng=np.random.default_rng(7741+N);records=[]
    inverse=cosine.T*np.array([pow(N*int(w)%p,-1,p) for w in weights])[:,None]%p
    for count in (1,2,3):
        a=rng.integers(0,p,size=(M+1,)*count,dtype=np.int64)
        b=rng.integers(0,p,size=(M+1,)*count,dtype=np.int64)
        fa,fb=a.copy(),b.copy();tensor_weight=np.ones_like(a)
        for axis in range(count):
            fa=axis_apply(cosine,fa,axis,p);fb=axis_apply(cosine,fb,axis,p)
            shape=[1]*count;shape[axis]=M+1
            tensor_weight=tensor_weight*weights.reshape(shape)%p
        original=fa.copy()
        for axis in range(count):original=axis_apply(inverse,original,axis,p)
        assert np.array_equal(original,a)
        assert int(np.sum(fa*fb)%p)*pow(N,-count,p)%p==int(np.sum(a*b%p*tensor_weight)%p)
        records.append(dict(auxiliary_regions=count,all_input_reconstruction_and_bilinear_Parseval=True))
    return dict(N=N,full_normal_mixed_split_identities=3*N,centered_character_checks=N*(M+1),
                reproducing_kernel_all_other_grid_values_zero=True,
                tensor_packets=records)


def main():
    result=dict(status='PASS',levels=[level(N) for N in range(2,11)],
                scope='Exact root normal split and entire finite cosine packet; no mixed-source gap or asymptotic noncancellation assertion.')
    Path(__file__).with_name('actual_augmented_plat_entire_core_color_packet_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',levels=len(result['levels']),
                         full_normal_split_identities=sum(r['full_normal_mixed_split_identities'] for r in result['levels']),
                         centered_characters=sum(r['centered_character_checks'] for r in result['levels']),
                         all_input_tensor_packets=sum(len(r['tensor_packets']) for r in result['levels'])),indent=2))


if __name__=='__main__':main()
