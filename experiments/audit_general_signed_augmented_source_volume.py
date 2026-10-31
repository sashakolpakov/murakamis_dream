#!/usr/bin/env python3
"""Actual finite continuants, original signed sources, and fold diagnostics.

The uniform recurrence/relative-sum theorem is proved in the note. Finite
asymptotic errors below are diagnostics, never substitutes for that proof.
"""
import argparse
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_positive_face_channel_rate import (
    continuants, forced, matrix, sine_factorials,
)
from audit_actual_complete_circle_positive_face_polynomial import determinant_coefficients
from audit_actual_original_marked_face_coefficient import (
    add, local_polynomials, morse_faces, mul, substitute,
)
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local
from original_source_tensor import apply_pair


PATTERNS = [
    ('222', '1.3', '.7', '1.9', '2.1'),
    ('202', '1.1', '0', '0', '1.7'),
    ('202_equal', '1.4', '0', '0', '1.4'),
    ('220_200', '1.7', '.8', '0', '0'),
    ('022_002', '0', '0', '1.2', '1.7'),
    ('220_220', '1.7', '.8', '1.2', '0'),
    ('022_022', '0', '.8', '1.2', '1.7'),
]


def symbolic():
    k, h, al, ta = sp.symbols('k h al ta', positive=True)
    lam = 2*sp.sqrt(al+ta)
    # Independent finite-k residual expansion, with h=pi/N.
    tr = k/(k+1) * (1+(k*k-(k+1)**2)*h*h/3)
    app = sp.exp(lam*k*h)
    rhs = ((1+tr)*(1+2*al*sp.sin(k*h)*sp.sin((k+1)*h))
           -tr*(1-4*ta*sp.sin((k+1)*h)**2)*sp.exp(-lam*(k+1)*h))
    coeff = sp.simplify(sp.expand(sp.series(app-rhs, h, 0, 3).removeO()).coeff(h, 2))
    assert sp.simplify(coeff+2*ta*k) == 0
    N, t, s0 = sp.symbols('N t s0', integer=True)
    assert sp.expand(t*(s0+1)/2+t*(t-1)/2-t*(t+s0)/2) == 0
    M = (N-1-s0)/2
    exponent = sp.expand(N*t+(M-t)*(M-t+1)-M*(M+1))
    assert sp.expand(exponent-t*(t+s0)) == 0
    assert sp.expand(t*(t+1)-(t+sp.Rational(1,2))**2+sp.Rational(1,4)) == 0
    return {'residual_half_offset_and_twist_identities': 4,
            'residual_convention': 'app minus recurrence RHS has h^2 coefficient -2*tau*k; its absolute O(k/N^2) term is retained.'}


def finite_recurrence():
    counts = dict(original_scaled_pivots=0, direct_original_matrices=0,
                  exact_single_summand_pivots=0, original_forced_pairs=0,
                  original_circle_ratios=0, literal_half_twist_ratios=0,
                  actual_fold_multiplicities=0, complex_radius_pivots=0)
    worst = mp.mpf(0)

    def check(x, y):
        nonlocal worst
        err = abs(x-y)/max(1, abs(y))
        worst = max(worst, err)
        assert err < mp.mpf('1e-65'), (x, y, err)

    for N in range(3, 21):
        d=N-1; M=d//2; s0=d-2*M; th=mp.pi/N
        q=mp.exp(1j*th); S=sine_factorials(N)
        beta=[S[2*a]/S[a]**2 for a in range(M+1)]
        omega=[mp.exp(1j*th*d*d/2)*(-1)**a*q**(a*(a+1)) for a in range(M+1)]
        for a in range(M+1):
            t=M-a
            check(omega[a]/omega[M], mp.exp(1j*th*t*(t+s0)))
            counts['literal_half_twist_ratios']+=1
            ka=1 if 2*a==d else 2
            assert ka == (1 if N%2 and t==0 else 2)
            counts['actual_fold_multiplicities']+=1
        for name,*params in PATTERNS:
            x,b,c,y=map(mp.mpf,params); A=x+y
            allD=[]
            for middle in (b,c):
                D=continuants(N,M,x,middle,y); allD.append(D)
                e=[None]+[beta[a]*D[a]/(beta[a-1]*D[a-1]) for a in range(1,M+1)]
                for a in range(1,M+1):
                    expected=A+2*middle*mp.cos(th)
                    if a>1:
                        tau=mp.tan((a-1)*th)/mp.tan(a*th)
                        expected=((1+tau)*(A+2*middle*mp.cos(a*th)*mp.cos((a-1)*th))
                                  -tau*(A*A-4*x*y*mp.cos((a-1)*th)**2)/e[a-1])
                    check(e[a],expected)
                    assert e[a]>=A-mp.mpf('1e-65') and e[a]<=2*A+4*middle+mp.mpf('1e-65')
                    counts['original_scaled_pivots']+=1
                    if N<=10:
                        check(D[a],mp.det(matrix(N,a,x,middle,y)))
                        counts['direct_original_matrices']+=1
                    if middle==0 and x*y==0:
                        check(e[a],A); counts['exact_single_summand_pivots']+=1
                # A small genuine complex log-radius perturbation: use the
                # independent original continuant, never conjugating its input.
                xx=x*mp.exp(mp.mpc('.009','.007'))
                bb=middle*mp.exp(mp.mpc('-.006','.005'))
                yy=y*mp.exp(mp.mpc('.004','-.008'))
                Dz=continuants(N,M,xx,bb,yy)
                for a in sorted({1,M}):
                    ratio=(Dz[a]/Dz[a-1])/(D[a]/D[a-1])
                    assert abs(mp.log(ratio))<mp.mpf('.1')
                    counts['complex_radius_pivots']+=1
            Db,Dc=allD
            values=[beta[a]**2*Db[a]*Dc[a]*forced(N,a,x,y) for a in range(M+1)]
            assert all(abs(mp.im(z))<mp.mpf('1e-62')*max(1,abs(z)) and mp.re(z)>0 for z in values)
            for t in range(M+1):
                a=M-t
                prod=mp.fprod(A*A-4*x*y*mp.sin((mp.mpf(N)/2-j)*th)**2 for j in range(a+1,M+1))
                check(forced(N,a,x,y)/forced(N,M,x,y),prod)
                counts['original_forced_pairs']+=1
                expected=(beta[a]*Db[a]/(beta[M]*Db[M])
                          *beta[a]*Dc[a]/(beta[M]*Dc[M])*prod)
                check(values[a]/values[M],expected)
                counts['original_circle_ratios']+=1
    counts['maximum_exact_relative_error']=str(worst)
    return counts


def local_diagnostics():
    rows=[]; worst_res=worst_pivot=worst_circle=mp.mpf(0)
    count=0
    for N in (32,33,64,65,128,129,256,257):
        M=(N-1)//2; s0=N-1-2*M; th=mp.pi/N
        S=sine_factorials(N); beta=[S[2*a]/S[a]**2 for a in range(M+1)]
        for name,*params in PATTERNS:
            x,b,c,y=map(mp.mpf,params); A=x+y
            Ds=[]
            for middle in (b,c):
                D=continuants(N,M,x,middle,y); Ds.append(D)
                lam=2*mp.pi*mp.sqrt(middle*A+x*y)/A
                for a in range(max(2,M-int(mp.sqrt(N))),M+1):
                    k=mp.mpf(N)/2-a
                    actual=beta[a]*D[a]/(beta[a-1]*D[a-1])/A
                    app=mp.exp(lam*k/N)
                    tr=mp.tan(k*th)/mp.tan((k+1)*th)
                    rhs=((1+tr)*(1+2*middle/A*mp.sin(k*th)*mp.sin((k+1)*th))
                         -tr*(1-4*x*y/A**2*mp.sin((k+1)*th)**2)/mp.exp(lam*(k+1)/N))
                    residual=abs(app-rhs)/(k/N**2+k**3/N**3)
                    error=abs(mp.log(actual)-lam*k/N)/(1/mp.mpf(N)+k*k/N**2)
                    worst_res=max(worst_res,residual);worst_pivot=max(worst_pivot,error);count+=1
            Db,Dc=Ds
            C=mp.pi*(mp.sqrt(b*A+x*y)+mp.sqrt(c*A+x*y))/A
            for t in sorted({1,max(1,int(mp.sqrt(N)/2)),min(M,int(mp.sqrt(N)))}):
                a=M-t
                ratio=beta[a]**2*Db[a]*Dc[a]*forced(N,a,x,y)/(beta[M]**2*Db[M]*Dc[M]*forced(N,M,x,y))
                err=mp.re(mp.log(ratio))+C*t*(t+s0)/N
                scaled=abs(err)/(mp.mpf(t)/N+mp.mpf(t)**3/N**2)
                worst_circle=max(worst_circle,scaled)
                rows.append({'N':N,'pattern':name,'t':t,'log_relative_error':str(err),'scaled_log_error':str(scaled)})
    assert worst_res<100 and worst_pivot<100 and worst_circle<100
    return {'scope':'Finite asymptotic diagnostics; the uniform estimates are proved analytically.',
            'actual_pivot_residual_samples':count,'actual_circle_packet_samples':len(rows),
            'max_scaled_residual':str(worst_res),'max_scaled_pivot_log_error':str(worst_pivot),
            'max_scaled_circle_log_error':str(worst_circle),'profiles':rows}


def source_sums():
    """Whole signed sums: literal W/pi/cups/mark vs independent coefficient."""
    rows=[]
    for N,k,boxes in [(3,2,[1,0,2,1]),(4,2,[1,0,2,1]),
                       (5,2,[1,0,2,1]),(6,2,[1,0,2,1]),
                       (3,3,[1,3,0,2,4,1,3])]:
        loc=Local(N);p=loc.p;d=N-1;M=d//2;chart=morse_faces(k,boxes)
        variables=[f for f in range(chart['faces']) if f not in (0,chart['v'])]
        polys={a:local_polynomials(loc,a) for a in range(M+1)}
        imag=pow(loc.eta,N,p)
        sine=[pow(imag,j,p)*pow(loc.q,-j*(j+1)//2,p)*loc.fac[j]%p for j in range(N)]
        beta=[sine[2*a]*pow(sine[a]**2,-1,p)%p for a in range(M+1)]
        for signs in [tuple(1 for _ in boxes),tuple((-1,0,1)[j%3] for j in range(len(boxes)))]:
            state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
            marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
            for j in range(k):
                state=np.kron(state,loc.cup[0].reshape(-1))%p
                mark=np.kron(mark,(marker if j==chart['marked'] else loc.cap[0]).reshape(-1))%p
            state=state.reshape((N,)*(2*k))
            product={(0,)*len(variables):1}
            for slot,faces,eps in zip(boxes,chart['circles'],signs):
                coupon=np.zeros((N*N,N*N),dtype=np.int64)
                polynomial={}
                x,b,c,y=faces
                for a in range(M+1):
                    unit=pow(loc.omega[a],eps,p)
                    coupon=(coupon+loc.h0[a]*unit%p*(loc.W[a][0]@loc.pi[a][0]%p))%p
                    D,P=polys[a];local={(0,)*len(variables):1}
                    for poly,ids in [(D,(x,b,y)),(D,(x,c,y)),(P,(x,y))]:
                        local=mul(local,substitute(poly,ids,variables,p),p,d)
                    ka=1 if 2*a==d else 2
                    polynomial=add(polynomial,local,p,ka*beta[a]**2*unit%p)
                product=mul(product,polynomial,p,d)
                state=apply_pair(coupon,state,slot,N,p)
            original=int(mark@state.reshape(-1)%p)
            coefficient=product.get((d,)*len(variables),0)
            expected=pow(N,len(boxes),p)*coefficient%p
            assert original==expected,(N,k,signs,original,expected)
            rows.append({'N':N,'bridge_width':k,'boxes':len(boxes),'signs':signs,
                         'field':p,'literal_source':original,'exact_coefficient_source':expected})
    return {'whole_original_signed_source_sums':len(rows),'cases':rows,
            'scope':'All channels summed inside the original W/pi coupons, with actual cups and unrestricted marked cap; independently summed positive face factors retain every omega phase and N^R measure.'}


def normalized_one_zero_polynomials(N):
    """Z_a(z)=beta_a D_a(0,1,z), computed by the original continuant."""
    M=(N-1)//2;th=mp.pi/N;S=sine_factorials(N)
    D=[[mp.mpf(1)]]
    for n in range(M):
        diag=1/(2*mp.cos(n*th)*mp.cos((n+1)*th))
        now=[mp.mpf(0)]*(n+2)
        for j,c in enumerate(D[-1]):now[j]+=c;now[j+1]+=diag*c
        if n:
            bn=mp.sin(n*th)**2/(mp.cos(n*th)**2*mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))/4
            for j,c in enumerate(D[-2]):now[j+2]-=bn*c
        assert all(c>0 for c in now)
        D.append(now)
    return [[S[2*a]/S[a]**2*c for c in row] for a,row in enumerate(D)]


def tetrahedral_signed_diagnostics():
    """Actual K4 face coefficient, all labels and actual signed phases.

    Matching01,23 and marked MAIN02: L0=L2=0,L1=z,L3=1.
    beta_a D_a(0,0,1)=1 removes the exact one-variable factors.
    F(a,b)=sum_r Z_a[a-r] Z_b[b-r] is the literal coefficient.
    """
    profiles=[];checks=0;max_poly=mp.mpf(0)
    for N in (9,10,17,18,33,34,65,66,129,130):
        M=(N-1)//2;s0=N-1-2*M
        rows=normalized_one_zero_polynomials(N)
        if N<=18:
            S=sine_factorials(N)
            for a in range(M+1):
                dc=determinant_coefficients(N,a)
                beta=S[2*a]/S[a]**2
                for j,c in enumerate(rows[a]):
                    expected=beta*dc[(0,a-j,j)]
                    err=abs(c-expected)/max(1,abs(expected));max_poly=max(max_poly,err)
                    assert err<mp.mpf('1e-65');checks+=1
        central=mp.fsum(c*c for c in rows[M])
        for eps1,eps2 in ((0,0),(1,1),(1,-1),(-1,0)):
            vectors=[]
            for eps in (eps1,eps2):
                v=[mp.mpc(0)]*(M+1)
                for a,row in enumerate(rows):
                    t=M-a;ka=1 if N%2 and t==0 else 2
                    phase=mp.exp(1j*mp.pi*eps*t*(t+s0)/N)
                    for r in range(a+1):v[r]+=ka*phase*row[a-r]
                vectors.append(v)
            actual=mp.fsum(x*y for x,y in zip(*vectors))/central
            predicted=N/mp.sqrt(1-1j*eps1)/mp.sqrt(1-1j*eps2)
            rel=actual/predicted-1
            assert abs(rel)<1
            profiles.append({'N':N,'signs':[eps1,eps2],
                             'normalized_exact_sum':str(actual),'Gaussian_prediction':str(predicted),
                             'relative_error':str(rel)})
    return {'independent_actual_polynomial_coefficients':checks,
            'maximum_exact_polynomial_error':str(max_poly),
            'all_channel_signed_tetrahedral_profiles':len(profiles),'profiles':profiles,
            'scope':'All original internal labels and exact half-twist ratios are summed. Finite Gaussian errors are diagnostics, not a proof of the graph-wide estimate.'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',default='experiments/general_signed_augmented_source_volume_results.json')
    args=ap.parse_args();mp.mp.dps=90
    result={'status':'PASS','precision_digits':90,'symbolic':symbolic(),
            'finite':finite_recurrence(),'local_diagnostics':local_diagnostics(),
            'original_source':source_sums(),'tetrahedral':tetrahedral_signed_diagnostics(),
            'scope':'Original finite recurrence, scalar/parity/phase identities, actual whole signed W/pi source sums and independent positive coefficients. Uniform relative estimates, signed noncancellation and general volume equality are analytical theorems; finite asymptotic profiles only diagnose their constants.'}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('local_diagnostics','original_source','tetrahedral')},indent=2))
    print(json.dumps({'local_profiles':result['local_diagnostics']['actual_circle_packet_samples'],
                      'whole_sources':result['original_source']['whole_original_signed_source_sums'],
                      'signed_profiles':result['tetrahedral']['all_channel_signed_tetrahedral_profiles']},indent=2))


if __name__=='__main__':main()
