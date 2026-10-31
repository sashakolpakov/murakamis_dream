#!/usr/bin/env python3
"""Literal original-pair serial powers; no general digon adapter test."""
import argparse
import collections
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mpmath as mp
import numpy as np
import sympy as sp
from audit_actual_small_circle_polynomial_face_insertion import Local, physical_colors
from audit_actual_gaussian_resolvent_numerator_and_cap import finite_H, paths


def compose(F,G,d,mod=None):
    out=collections.defaultdict(int if mod else mp.mpf)
    bymiddle=collections.defaultdict(list)
    for (k,i,t,l),a in G.items():
        bymiddle[i].append((k,t,l,a))
    for (k,i,t,l),a in F.items():
        for kk,tt,ll,b in bymiddle[d-t]:
            n=(k+kk,i,tt,l+ll)
            out[n]+=a*b
            if mod:out[n]%=mod
    return {n:a for n,a in out.items() if a}


def complete_homogeneous(vals,r):
    h=[mp.mpf(1)]+[mp.mpf(0)]*r
    for v in vals:
        for j in range(1,r+1):h[j]+=v*h[j-1]
    return h[r]


def real_kernel(N,ell):
    a=[4*mp.cos((j+mp.mpf('.5'))*mp.pi/N)**2 for j in range(N)]
    s=[2*mp.sin(j*mp.pi/N) for j in range(N)]
    H=collections.defaultdict(mp.mpf)
    path_count=0
    for j in range(N):
        for i,edges,vis in paths(N,j):
            weight=mp.mpf(4)
            ones=twos=0
            for v,step in edges:
                if step==1:weight*=s[v]**2;ones+=1
                else:weight*=s[v]*s[v-1];twos+=1
            weight/=mp.fprod(a[v] for v in vis)
            weight*=4**(ell-1)*complete_homogeneous([1/a[v] for v in vis],ell-1)
            for k in range(ones+1):
                H[(k+twos,i,N-1-j,ones-k+twos)]+=weight*math.comb(ones,k)
            path_count+=1
    return dict(H),a,path_count


def run():
    counts=collections.Counter()
    z=sp.symbols('z')
    for N in range(2,31,2):
        chi=2*sp.chebyshevt(N,z/2)+2
        assert chi.subs(z,-2)==4
        assert sp.diff(chi,z).subs(z,-2)==-N*N
        counts['exact_characteristic_endpoint_identities']+=2

    # Original coproduct colors, then ordinary operator multiplication.
    # The separate path/compiler code supplies the homogeneous polynomial.
    for N in (4,6,8):
        loc=Local(N);p=loc.p;d=N-1
        colors=physical_colors(loc)
        Pphys=(colors[N]+2*sum(colors[1:N]))%p
        O=-colors[2]%p
        I=np.eye(N*N,dtype=np.int64)
        assert np.array_equal((2*I+O)@Pphys%p,4*I%p)
        counts['original_full_resolvent_identities']+=1
        H={n:-a%p for n,a in finite_H(loc,-2).items()}
        Hell=H.copy();mat=Pphys.copy()
        for ell in range(1,6):
            if ell>1:
                Hell=compose(H,Hell,d,p)
                mat=Pphys@mat%p
            counts['original_serial_powers']+=1
            for u in range(N):
                for v in range(N):
                    x=-loc.q*pow(loc.Q,u,p)%p
                    y=-pow(loc.q,-1,p)*pow(loc.Q,-v,p)%p
                    for r in range(N):
                        s=(u+v-r)%N;delta=r-u;c=pow(loc.Q,-delta,p)
                        val=sum(a*pow(x,k,p)*pow(c,t,p)*pow(y,l,p)
                                for (k,i,t,l),a in Hell.items())%p
                        pred=val*pow(N,-1,p)*pow(loc.q,-d*delta,p)*pow(c,-d,p)%p
                        assert pred==int(mat[r*N+s,u*N+v]),(N,ell,u,v,r,s)
                        counts['original_physical_grid_entries']+=1
                        counts['wrong_unwrapped_total_zeros']+=r+s!=u+v

    mp.mp.dps=75
    max_error=mp.mpf(0);max_relative_bound=mp.mpf(0)
    for N in (4,6,8,10,12):
        H,a,npaths=real_kernel(N,1)
        err=abs(mp.fsum(1/z for z in a)-mp.mpf(N*N)/4)
        assert err<mp.mpf('1e-65');max_error=max(max_error,err)
        counts['inverse_diagonal_sum_identities']+=1
        for j in range(N):
            assert 1<=4/a[j]<=N*N
            counts['actual_diagonal_bounds']+=1
        composed=H.copy()
        for ell in range(2,6):
            composed=compose(H,composed,N-1)
            direct,_,npth=real_kernel(N,ell)
            counts['actual_path_break_multipliers']+=npth
            assert set(composed)==set(direct)==set(H)
            for n,val in direct.items():
                err=abs(val-composed[n])/max(1,abs(val))
                max_error=max(max_error,err)
                assert err<mp.mpf('1e-64')
                ratio=val/(N**(2*ell-2)*H[n])
                assert ratio<=1+mp.mpf('1e-65')
                assert val>=H[n]*(1-mp.mpf('1e-65'))
                max_relative_bound=max(max_relative_bound,ratio)
                counts['independent_serial_coefficients_and_bounds']+=1
    return dict(status='PASS',precision=mp.mp.dps,counts=dict(counts),
                maximum_relative_error=str(max_error),
                maximum_fraction_of_serial_bound=str(max_relative_bound),
                scope='Same ordered-pair original coproduct powers, physical endpoints, exact homogeneous composition and positive path bound. No arbitrary diagram digon or shared-volume inference.')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_fejer_serial_coupon_bound_results.json'))
    args=parser.parse_args()
    result=run();args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
