#!/usr/bin/env python3
"""Exact full Fermat frames, original four-leg crossings, and norm rates."""

from itertools import product
import json
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing
from audit_cap_wall_fermat_quad_residue import data,frames,affine_points
from audit_figure_eight_whole_source import MixedEntries


def full_frames(N,p,Q,u,v,w):
    P,L=frames(N,p,Q,u,v,w)
    H=np.array([[P[(n-k)%N] for k in range(N)] for n in range(N)],dtype=np.int64)
    kap=pow(v,N,p)*pow(N*pow(u,N-1,p)*(w-u)%p,-1,p)%p
    h=[kap]
    for n in range(1,N):
        h.append(h[-1]*v*pow(Q,-1,p)*pow((w-u*pow(Q,-n,p))%p,-1,p)%p)
    Hi=np.array([[h[(n-k)%N] for k in range(N)] for n in range(N)],dtype=np.int64)
    M=np.column_stack([frames(N,p,Q,u*pow(Q,j,p)%p,v,w)[0] for j in range(N)])
    Mi=[]
    for j in range(N):
        uj=u*pow(Q,j,p)%p;_,Lj=frames(N,p,Q,uj,v,w)
        scale=pow(v,N,p)*pow(N*pow(uj,N-1,p)*(w-uj)%p,-1,p)%p
        Mi.append([scale*pow(Q,n,p)*int(Lj[n])%p for n in range(N)])
    Mi=np.array(Mi,dtype=np.int64)
    assert np.array_equal(H@Hi%p,np.eye(N,dtype=np.int64))
    assert np.array_equal(Mi@M%p,np.eye(N,dtype=np.int64))
    return H,Hi,M,Mi


def exact_case(N):
    p,g,q,Q,gamma,Z,S,W,Wi,F=data(N)
    points=affine_points(N,p)
    assert len(points)>=4
    checked=0
    for u,v,w in points[:8]:
        H,Hi,M,Mi=full_frames(N,p,Q,u,v,w)
        assert np.array_equal(Hi@S@H%p,S)
        expected=pow(u,-1,p)*(w*np.eye(N,dtype=np.int64)-v*S)@Z%p
        assert np.array_equal(Hi@Z@H%p,expected)
        # All cap-normalized columns, with their actual factorial normalization.
        cols=[];ratios=[1]
        for k in range(N):
            col=frames(N,p,Q,u*pow(Q,-k,p)%p,v,w)[0]
            if k:
                col=col*pow(v,N-k,p)*pow(F[N-k],-1,p)%p
                poch=1
                for j in range(1,N-k+1):poch=poch*(1-u*pow(Q,j,p))%p
                ratios.append(poch*pow(F[N-k],-1,p)%p)
            cols.append(col)
        K=np.column_stack(cols)
        assert np.array_equal(K,H@np.diag(ratios)%p)
        checked+=1
    E=MixedEntries(N,p,q)
    fs=[full_frames(N,p,Q,*points[j]) for j in range(4)]
    kernel_checks=0
    for sign in (-1,1):
        R=crossing(E,g,pow(g,2,p),sign)
        Rf=np.kron(fs[2][3],fs[3][3])@R@np.kron(fs[0][2],fs[1][2])%p
        for j1,j2,j3,j4 in ((0,0,0,0),(N-1,0,0,N-1),
                            (0,N-1,N-1,0),(N//2,N//2,N//2,N//2)):
            direct=0
            for a,b in product(range(N),repeat=2):
                maximum=min(a,N-1-b) if sign>0 else min(b,N-1-a)
                for h in range(maximum+1):
                    c,e=(b+h,a-h) if sign>0 else (b-h,a+h)
                    direct += int(fs[2][3][j3,c])*int(fs[3][3][j4,e])\
                        *E.direct(g,pow(g,2,p),a,b,h,sign)\
                        *int(fs[0][2][a,j1])*int(fs[1][2][b,j2])
            assert int(Rf[j3*N+j4,j1*N+j2])==direct%p
            kernel_checks+=1
    # The selected coefficient proving full support is nonzero for every entry.
    support_coefficients=0
    for a,b,c,e in product(range(N),repeat=4):
        r=(-a)%N;s=(-b)%N
        coefficient=pow(-1,c+e,p)*pow(Q,c*(c-1)//2+e*(e-1)//2,p)\
            *pow(F[r]*F[s]*F[c]*F[e]%p,-1,p)%p
        assert coefficient
        support_coefficients+=1
    return {'N':N,'Fermat_frames':checked,'strict_actual_four_line_checks':kernel_checks,
            'nonzero_full_support_witness_coefficients':support_coefficients,
            'exact_dual_inverse_and_cap_frame':True}


def norms():
    mp.mp.dps=80
    central_u=mp.mpc('.4','.3');central_v=1-central_u
    a=mp.log(central_u);b=mp.log(central_v)
    gamma=-mp.quad(lambda t:mp.log(2*mp.sin(mp.pi*t)),[0,mp.mpf(1)/6])
    output=[]
    for N in (16,32,64,128,256):
        Q=mp.exp(2j*mp.pi/N);u=mp.exp(a/N);v=mp.exp(b/N)
        kap=v**N/(N*u**(N-1)*(1-u))
        p=[mp.mpc(1)];h=[kap];F=[mp.mpc(1)]
        for n in range(1,N):
            p.append(p[-1]*v/(1-u*Q**n))
            h.append(h[-1]*v/Q/(1-u*Q**(-n)))
            F.append(F[-1]*(1-Q**n))
        pf=np.array([complex(z) for z in p]);hf=np.array([complex(z) for z in h])
        Hnorm=float(max(abs(np.fft.fft(pf))))
        Hinorm=float(max(abs(np.fft.fft(hf))))
        r=[mp.mpc(1)]
        for k in range(1,N):
            poch=mp.fprod(1-u*Q**j for j in range(1,N-k+1))
            r.append(poch/F[N-k])
        maximum=max(abs(z) for z in r);minimum=min(abs(z) for z in r)
        output.append({'N':N,'gamma_integral':float(gamma),
            'log_H_norm_over_N':float(mp.log(Hnorm)/N),
            'log_inverse_norm_over_N':float(mp.log(Hinorm)/N),
            'log_condition_over_N':float(mp.log(Hnorm*Hinorm)/N),
            'selected_column_log_norm_over_N':float(mp.log(mp.sqrt(mp.fsum(abs(z)**2 for z in p)))/N),
            'selected_inverse_row_log_norm_over_N':float(mp.log(mp.sqrt(mp.fsum(abs(z)**2 for z in h)))/N),
            'raw_coherent_maximum_entry_log_rate':float(mp.log(max(abs(z) for z in p)/min(abs(z) for z in p))/N),
            'cap_diagonal_minimum':float(minimum),'cap_diagonal_maximum':float(maximum)})
    return output


if __name__=='__main__':
    result={'scope':'exact actual four-leg frame identity; no positive geometric gluing claim',
            'exact':[exact_case(N) for N in range(2,9)],'norm_diagnostics':norms()}
    path=Path(__file__).with_name('actual_four_line_fermat_crossing_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',sum(c['Fermat_frames'] for c in result['exact']),'full frames;',
          sum(c['strict_actual_four_line_checks'] for c in result['exact']),
          'original mixed crossing entries;',
          sum(c['nonzero_full_support_witness_coefficients'] for c in result['exact']),
          'all-N-pattern support coefficients;',len(result['norm_diagnostics']),'norm scales')
