#!/usr/bin/env python3
"""Actual202/222 positive-total determinant and genuine normal checks."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_q_hahn_complementary_hard_edge import matrices, low_series
from audit_actual_q_hahn_small_channel_generic_normals import jacobi, scalar_K


def gap():
    x,t=sp.symbols('x t',real=True)
    left=(1/(sp.cos(x)*sp.cos(x+t))
          -(sp.sin(x)**2/sp.cos(x)+sp.sin(x+t)**2/sp.cos(x+t))/sp.sin(2*x+t))
    right=(sp.sin(x)*sp.cos(x)/(1+sp.sin(x))
           +sp.sin(x+t)*sp.cos(x+t)/(1+sp.sin(x+t)))/sp.sin(2*x+t)
    assert sp.trigsimp(sp.together(left-right))==0
    assert sp.trigsimp((sp.sin(x)*sp.cos(x)+sp.sin(x+t)*sp.cos(x+t))
                      /sp.sin(2*x+t)-sp.cos(t))==0
    rows=ends=eigen=0;worst=float('inf')
    for N in (3,4,5,8,9,16,33,64,129,257):
        theta=mp.pi/N
        for a in sorted({1,max(1,(N-1)//4),(N-1)//2}):
            weights=[mp.sqrt(mp.sin((2*r+1)*theta)) for r in range(a)]
            edges=[mp.mpf(0)]+[mp.sin(n*theta)**2/(mp.cos(n*theta)
                      *mp.sqrt(mp.sin((2*n-1)*theta)*mp.sin((2*n+1)*theta))) for n in range(1,a)]
            for r in range(a):
                value=1/(mp.cos(r*theta)*mp.cos((r+1)*theta))
                if r:value-=edges[r]*weights[r-1]/weights[r]
                if r+1<a:value-=edges[r+1]*weights[r+1]/weights[r]
                target=(mp.sin(r*theta)*mp.cos(r*theta)/(1+mp.sin(r*theta))
                        +mp.sin((r+1)*theta)*mp.cos((r+1)*theta)/(1+mp.sin((r+1)*theta))
                        )/mp.sin((2*r+1)*theta)
                if r==a-1:
                    finite=mp.sin(a*theta)**2/(mp.cos(a*theta)*mp.sin((2*a-1)*theta))
                    assert abs(value-finite-target)<mp.mpf('1e-100');ends+=1
                else:assert abs(value-target)<mp.mpf('1e-100')
                assert value>=mp.cos(theta)/2-mp.mpf('1e-100');rows+=1
            Hp,Hm=matrices(N,a)
            minimum=float(np.linalg.eigvalsh(Hp+Hm)[0]-np.cos(np.pi/N))
            assert minimum>-1e-8;worst=min(worst,minimum);eigen+=1
    return dict(exact_trigonometric_identities=2,actual_weighted_rows=rows,
                finite_last_row_comparisons=ends,folded_matrix_gaps=eigen,
                minimum_excess_over_cos_theta=worst)


def root_matrix(N,a,X,T):
    theta=mp.pi/N;M=mp.eye(a)/X
    for r in range(a):M[r,r]-=(1+1/T)/(2*mp.cos(r*theta)*mp.cos((r+1)*theta))
    for n in range(1,a):
        bn=mp.sin(n*theta)**2/(mp.cos(n*theta)**2*mp.sin((2*n-1)*theta)*mp.sin((2*n+1)*theta))
        hp=mp.sqrt(bn)*(mp.sin(n*theta)+1j*mp.cos(n*theta));hm=mp.conj(hp)
        M[n-1,n]=-(hm+hp/T)/2
        M[n,n-1]=-(hp+hm/T)/2
    return M


def actual_generic_matrix(N,a,q,sigma,u,original):
    b=q**sigma;w=q*b;X=q**(2*u+1)
    al,be=jacobi(N,q,b,a);M=mp.eye(a);lower_choices=0
    for r in range(a):M[r,r]=1/X+al[r]/w
    for n in range(1,a):
        if abs(original[n-1,n])>=abs(original[n,n-1]):
            M[n-1,n]=original[n-1,n]
            M[n,n-1]=-be[n]/(w*w*M[n-1,n])
        else:
            M[n,n-1]=original[n,n-1]
            M[n-1,n]=-be[n]/(w*w*M[n,n-1]);lower_choices+=1
    return M,lower_choices


def source(N,m,q,sigma,u):
    return low_series(q,N,m,q**(2*u),q**(2*(sigma-u)))


def checks():
    roots=generics=cofactors=circles=normals=aliases=zeroedges=0
    lower_choices=0;worst=mp.mpf(0);maxratio=mp.mpf(0);phases=[]
    for N in (16,17,32,33):
        q0=mp.exp(mp.pi*1j/N);logq=mp.pi*1j/N
        cases=[('202',N*N*mp.mpc('.7','.2'),mp.mpc('1.3','.012')),
               ('222',mp.mpc('-.8','.01'),mp.mpc('1.6','-.013')),
               ('zero-edge',N*N*mp.mpc('.6','-.3'),q0**(-2))]
        for kind,X,T in cases:
            # The marked total is retained, not rebuilt from a free root at each q.
            w0=-mp.sqrt(T);sigma=mp.log(w0)/logq-1
            if mp.re(sigma)<0:sigma+=2*N
            u=(mp.log(X)/logq-1)/2
            a=(N-1)//2;m=N-1-a;s=m-a
            M0=root_matrix(N,a,X,T)
            det0=mp.det(M0);small=source(N,a,q0,sigma,u)
            scalar=(q0*q0**(2*sigma))**a*scalar_K(N,q0,a)
            err=abs(small/(scalar*det0)-1);assert err<mp.mpf('1e-90')
            worst=max(worst,err);roots+=1
            if kind=='zero-edge':
                assert abs(M0[0,1])<mp.mpf('1e-100')
                assert abs(M0[1,0])>mp.mpf('.01')/N;zeroedges+=1
            base=source(N,m,q0,sigma,u)
            P=mp.fprod(q0**(2*sigma)-q0**(2*r) for r in range(a,m))
            assert abs(base/(small*P)-1)<mp.mpf('1e-90')
            for direction in (1,-1,1j,-1j):
                eps=mp.mpf('.01')*direction/N**10;q=q0*mp.exp(eps)
                M,lc=actual_generic_matrix(N,a,q,sigma,u,M0);lower_choices+=lc
                det=mp.det(M)
                direct=source(N,a,q,sigma,u)
                predicted=(q*q**(2*sigma))**a*scalar_K(N,q,a)*det
                err=abs(direct/predicted-1);assert err<mp.mpf('1e-85')
                worst=max(worst,err);generics+=1
                inverse=M**-1
                prev=mp.det(M[:a-1,:a-1]) if a>1 else 1
                assert abs(prev/det-inverse[a-1,a-1])<mp.mpf('1e-90');cofactors+=1
                assert abs(inverse[a-1,a-1])<10
                val=source(N,m,q,sigma,u);ratio=abs(val/base)
                assert ratio<10;circles+=1;maxratio=max(maxratio,ratio)
            for order in (1,2):
                value=mp.diff(lambda eps:source(N,m,q0*mp.exp(eps),sigma,u),0,order)
                assert abs(value/base)/N**(10*order)<10;normals+=1
            # Same root clocks, different actual marked total: first normals differ.
            shifted=source(N,m,q0,sigma+N,u)
            assert abs(shifted/base-1)<mp.mpf('1e-90')
            normal=mp.diff(lambda e:source(N,m,q0*mp.exp(e),sigma,u),0)
            shiftednormal=mp.diff(lambda e:source(N,m,q0*mp.exp(e),sigma+N,u),0)
            assert abs((shiftednormal-normal)/base)>mp.mpf('1e-20');aliases+=1
            phases.append(dict(N=N,domain=kind,marked_total=str(sigma),
                               normalized_alias_normal_difference=str(abs((shiftednormal-normal)/base))))
    return dict(original_root_phase_determinants=roots,original_generic_determinants=generics,
                leading_minor_cofactors=cofactors,genuine_large_partner_circles=circles,
                genuine_first_second_normals=normals,retained_marked_normal_aliases=aliases,
                exact_one_edge_zero_cases=zeroedges,frozen_lower_edge_choices=lower_choices,
                maximum_source_error=str(worst),maximum_relative_circle_ratio=str(maxratio),
                marked_phase_profiles=phases)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    mp.mp.dps=120
    result=dict(status='PASS',precision_digits=mp.mp.dps,gap=gap(),source=checks(),
                scope='Exact uniform positive-sum gap and genuine202/222 numerator normals with marked phases. No full source period or leading normal amplitude.')
    path=args.output or Path(__file__).with_name('actual_q_hahn_positive_total_boundary_normals_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
