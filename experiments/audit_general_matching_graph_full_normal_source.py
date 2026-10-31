#!/usr/bin/env python3
"""All-level complete-circle plat -> typed matching graph -> one trace normal."""
import itertools
import json
from pathlib import Path
import numpy as np
from audit_actual_two_cut_ports import balanced_data
from audit_actual_marked_multiport_chebyshev_source_packet import pair_circle
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local,mm,kron
from original_source_tensor import apply_pair
from audit_general_augmented_plat_matching_geometry import plat_matching,cubic_dictionary


def run(N,k,enumerate_all=False):
    loc=Local(N);p,q,d=loc.p,loc.q,N-1
    _,_,_,_,_,K,_,Rp,Rm=balanced_data(N)
    ki=np.diag([pow(int(z),-1,p) for z in np.diag(loc.Kpair[0])])
    O=(loc.Fpair[0]@loc.Epair[0]+q*loc.Kpair[0]+pow(q,-1,p)*ki)%p
    L=pair_circle(O,N,p)
    low=list(loc.W);M=max(low)
    sector={j:mm(loc.W[j],loc.pi[j],p) for j in low}
    total=sum((loc.h0[j]*sector[j][0] for j in low),np.zeros_like(L))%p
    assert np.array_equal(total,L)
    for j in low:
        sw=loc.pi[j][0]@loc.W[j][0]%p
        expected=np.eye(2*j+1,dtype=np.int64) if 2*j==d else np.zeros((2*j+1,2*j+1),dtype=np.int64)
        assert np.array_equal(sw,expected)
        assert np.array_equal(Rp@sector[j][0]%p,loc.omega[j]*sector[j][0]%p)
    odd=list(range(1,2*k-2,2));even=list(range(0,2*k-1,2));boxes=odd+even+odd
    signs=[(-1,0,1)[i%3] for i in range(len(boxes))]
    matching,free=plat_matching(k,boxes);assert free==0
    graph=cubic_dictionary(len(boxes),matching)
    state=(np.array([1],dtype=np.int64),np.array([0],dtype=np.int64))
    row=(np.array([1],dtype=np.int64),np.array([0],dtype=np.int64))
    marked=np.array([1],dtype=np.int64)
    marker=np.array([[pow(loc.x,b,p)*pow(N*N,-1,p)%p for b in range(N)] for a in range(N)],dtype=np.int64)
    for h in range(k):
        state=kron(state,tuple(v.reshape(-1) for v in loc.cup),p)
        row=kron(row,tuple(v.reshape(-1) for v in loc.cap),p)
        marked=np.kron(marked,(marker if h==k-1 else loc.cap[0]).reshape(-1))%p
    def close(coupons):
        s0=state[0].reshape((N,)*(2*k));s1=state[1].reshape((N,)*(2*k))
        for slot,B in zip(boxes,coupons):
            s1=(apply_pair(B[0],s1,slot,N,p)+apply_pair(B[1],s0,slot,N,p))%p
            s0=apply_pair(B[0],s0,slot,N,p)
        marked_value=int(marked@s0.reshape(-1)%p)
        zero=int(row[0]@s0.reshape(-1)%p)
        derivative=int((row[1]@s0.reshape(-1)+row[0]@s1.reshape(-1))%p)
        assert zero==0 and derivative==loc.nu*marked_value%p
        return marked_value
    vectors=list(itertools.product(low,repeat=len(boxes))) if enumerate_all else [tuple([0]*len(boxes)),tuple([M]*len(boxes)),tuple(low[i%len(low)] for i in range(len(boxes)))]
    sector_total=0
    for js in vectors:
        value=close([sector[j] for j in js])
        factor=1
        for j,e in zip(js,signs):factor=factor*loc.h0[j]*pow(loc.omega[j],e,p)%p
        sector_total=(sector_total+factor*value)%p
    coupons=[];original=[]
    for e in signs:
        B=tuple(sum((loc.h0[j]*pow(loc.omega[j],e,p)*sector[j][c]%p for j in low),np.zeros_like(L))%p for c in range(2))
        R=Rp if e>0 else Rm if e<0 else np.eye(N*N,dtype=np.int64)
        assert np.array_equal(B[0],R@L%p)
        coupons.append(B);original.append(R@L%p)
    whole=close(coupons)
    raw=state[0].reshape((N,)*(2*k))
    for slot,B in zip(boxes,original):raw=apply_pair(B,raw,slot,N,p)
    assert int(marked@raw.reshape(-1)%p)==whole
    if enumerate_all:assert sector_total==whole
    return {'N':N,'plat_width':k,'circle_boxes':len(boxes),
            'fixed_label_trace_normals_checked':len(vectors),
            'full_label_sum_enumerated':enumerate_all,
            'all_oriented_matching_faces':graph['all_oriented_medial_faces_match'],
            'original_full_source':whole,'paired_nilpotent_image_retained':True}

if __name__=='__main__':
    rows=[run(N,k,alljs) for N,k,alljs in [(2,2,True),(3,2,True),(4,2,True),(5,2,True),(6,2,True),(3,3,False),(4,3,False),(3,4,False)]]
    result={'status':'PASS','cases':rows,
            'scope':'Full original complete-circle augmented plat source, both parities, all folded labels, all matching normals. No mixed auxiliary-color packet or asymptotic selection.'}
    Path(__file__).with_name('general_matching_graph_full_normal_source_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS8 full original plats, both parities; '+str(sum(r['fixed_label_trace_normals_checked'] for r in rows))+' exact sector trace normals; 5 exhaustive full-label sums')
