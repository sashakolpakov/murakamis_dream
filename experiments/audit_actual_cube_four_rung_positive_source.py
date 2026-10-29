#!/usr/bin/env python3
"""Original marked cube, eight Steinberg cycles and four arbitrary rungs.

Exact prime-field comparisons retain both local normal components and the
unrestricted physical marked row. Positivity is proved over C in the note;
no sign or nonvanishing inference is made from a finite field.
"""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_odd_central_cube_reflection_packet import turn
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local, graph_case
from audit_actual_trivalent_complete_circle_vertex_kernel import ordered_cube_graph
from audit_actual_trivalent_full_cd_normalization_and_magnetic_growth import physical_columns
from audit_actual_two_cut_ports import balanced_data


def level(N, exhaustive):
    local=Local(N);p,q,d=local.p,local.q,N-1;m=d//2
    W,fac,(Et,Ft,Kt)=physical_columns(N,q,p)
    Ki=np.diag([pow(int(k),-1,p) for k in np.diag(Kt)])
    Omega=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    _,eta,*_=balanced_data(N)
    imaginary=pow(eta,N,p)
    sine=[pow(imaginary,k,p)*pow(q,-k*(k+1)//2,p)*fac[k]%p for k in range(N)]
    nodes=[(pow(q,2*k+1,p)+pow(q,-2*k-1,p))%p for k in range(N)]
    I=np.eye(N*N,dtype=np.int64)
    basis=[I]
    for k in range(d):
        step=(sine[k+1]*pow(sine[k],-1,p)%p)**2%p
        basis.append((nodes[k]*I-Omega)@basis[-1]%p*pow(step,-1,p)%p)
    pv=[int(local.cup[0][u,d-u]) for u in range(N)]
    H={};Pnode={};source_checks=0
    root_scale=N*pow(q,-d*d,p)%p
    for j in range(m+1):
        mult=1 if j==m else 2
        circle=local.h0[j]*local.W[j][0]%p@local.pi[j][0]%p
        H[j]=turn(circle,N,p,pv)*pow(N*mult,-1,p)%p
        coeff=[sine[j+r]*pow(sine[j-r]*sine[r]**2,-1,p)%p for r in range(j+1)]
        reconstructed=sum((coeff[r]*basis[r] for r in range(j+1)),np.zeros_like(I))%p
        assert np.array_equal(H[j],reconstructed)
        Pnode[j]=sum(coeff[r]*sine[m]**2*pow(sine[r]**2*sine[m-r]**2,-1,p) for r in range(j+1))%p
        # Actual U is pivotal cyclic before choosing any canonical theta.
        for js in ((m,m,j),(m,j,m),(j,m,m)):
            rotated=js[1:]+js[:1]
            U=local.vertex(js)['U'];V=local.vertex(rotated)['U']
            K=local.ordinary[js[0]][2]
            v0=V[0].transpose(2,0,1);v1=V[1].transpose(2,0,1)
            k0=np.diag(K[0])[:,None,None];k1=np.diag(K[1])[:,None,None]
            assert np.array_equal(U[0],k0*v0%p)
            assert np.array_equal(U[1],(k0*v1+k1*v0)%p)
            source_checks+=1
        s=local.vertex((m,m,j))['s'][0]
        anchor=(-1)**(d-j)*pow(q,-j*(j+1)-d,p)%p
        actual=local.gamma[j]**2*s*s*pow(anchor*anchor,-1,p)%p
        target=N*N*pow(q,2*m*m-2,p)*Pnode[j]**2%p
        assert actual==target
        # Keep the paired nilpotent as a regular W D_can(W), not a projector.
        canonical_dual=(root_scale*root_scale*local.gamma[j])*local.pi[j][0]%p
        rung=local.W[j][0]@canonical_dual%p
        expected=root_scale**2*local.gamma[j]*pow(local.h0[j],-1,p)*circle%p
        assert np.array_equal(rung,expected)
        if j<m:
            assert not np.any(rung@rung%p)
    K=local.ordinary[m][2][0]
    pivot=np.kron(np.eye(N,dtype=np.int64),K)
    pairs={(a,b):H[a]@H[b]%p for a,b in itertools.product(range(m+1),repeat=2)}
    if exhaustive:
        labels_to_check=list(itertools.product(range(m+1),repeat=4))
    else:
        labels_to_check=sorted(set([(m,)*4,(0,m,m,m),(0,0,m,m),(0,0,0,m),
            (max(0,m-1),)*4,(0,1,m-1,m),(0,0,0,0),(1,1,1,1)]))
    rows=[];unsupported=0
    for js in labels_to_check:
        labels=[m]*12
        for edge,j in zip((1,10,4,7),js):labels[edge]=j
        product=pairs[js[:2]]@pairs[js[2:]]%p
        period=int(np.trace(pivot@product%p)%p)*pow(N,-1,p)%p
        prefactor=pow(N,12,p)
        for j in js:prefactor=prefactor*(1 if j==m else 2)*Pnode[j]**2%p
        expected=prefactor*period%p
        result=graph_case(local,'four_rung_cube',ordered_cube_graph(),labels,[0]*12)
        assert result['original_marked_scalar']==expected
        if sum(js)<d:
            assert period==expected==0
            unsupported+=1
        rows.append({'rung_labels':js,'original_marked_source':expected})
    # A separate literal signed source retains both cycle and rung phases.
    js=(0,m,m,m)
    labels=[m]*12
    for edge,j in zip((1,10,4,7),js):labels[edge]=j
    powers=[1,-2,3,0,-1,0,0,2,0,0,-3,0]
    actual=graph_case(local,'signed_four_rung_cube',ordered_cube_graph(),labels,powers)['original_marked_scalar']
    product=pairs[js[:2]]@pairs[js[2:]]%p
    prefactor=pow(N,12,p)
    for j in js:prefactor=prefactor*(1 if j==m else 2)*Pnode[j]**2%p
    expected=prefactor*int(np.trace(pivot@product%p)%p)*pow(N,-1,p)%p
    for j,e in zip(labels,powers):expected=expected*pow(local.omega[j],e,p)%p
    assert actual==expected
    return {'N':N,'prime':p,'exhaustive_four_rung_cube':exhaustive,
        'full_normal_pivotal_source_cycles':source_checks,
        'all_paired_regular_rung_and_halfdegree_packets':m+1,
        'untwisted_actual_marked_sources':rows,'unsupported_whole_source_count':unsupported,
        'literal_signed_phase_source':actual}


if __name__=='__main__':
    rows=[level(N,N<=7) for N in (3,5,7,9,11)]
    out={'status':'PASS','levels':rows,
        'scope':'Actual four-rung packet with eight fixed odd Steinberg cycle edges; no whole-cube/all-parity claim.'}
    Path(__file__).with_name('actual_cube_four_rung_positive_source_results.json').write_text(json.dumps(out,indent=2)+'\n')
    count=sum(len(r['untwisted_actual_marked_sources']) for r in rows)
    print(f'PASS5 odd levels/{count} original untwisted cube sources/5 signed phases; all rung-source normals and paired nilpotents retained')
