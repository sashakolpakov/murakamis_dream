#!/usr/bin/env python3
"""Actual large-H/cup scalar, positive face coefficients and local support."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_q_hahn_negative_clock_boundary import literal_h, matrix
from audit_actual_correlated_boundary_band_ratio import root_cup
from audit_high_color_first_normal_r_degree import root_field


def source_checks():
    checks=carries=0;worst=mp.mpf(0)
    for N in range(3,14):
        d=N-1;theta=mp.pi/N;q=mp.exp(1j*theta);Q=q*q
        F=lambda j:mp.fprod(1-Q**k for k in range(1,j+1))
        S=lambda j:mp.fprod(2*mp.sin(k*theta) for k in range(1,j+1))
        for a in range(d//2+1):
            m=d-a;s=d-2*a;mult=1 if s==0 else 2;beta=S(2*a)/S(a)**2
            for xx,bb,cc,yy in [(mp.mpc('1.3','.1'),mp.mpc('.9','-.1'),mp.mpc('1.7','.2'),mp.mpc('2.1','.1')),
                                (mp.mpf('.7'),mp.mpf('2.3'),mp.mpf('.8'),mp.mpf('1.1'))]:
                def heads(mid):
                    return d/2+N*(mp.log(xx)-mp.log(mid))/(2j*mp.pi),d/2+N*(mp.log(mid)-mp.log(yy))/(2j*mp.pi)
                i,j=heads(bb);ii,jj=heads(cc);sigma=i+j;r=sigma-m
                def W(x,y,row):
                    return ((-1)**m*mp.exp(1j*theta*(-d*row+d*x-m*(m-1)))
                            *literal_h(N,m,mp.exp(2j*theta*x),mp.exp(2j*theta*y))/F(m))
                pV=lambda z:N*mp.exp(1j*theta*(-d*d+d*z))
                gamma=mp.exp(1j*theta*(2-a*a))/N**2
                source=(mult*N*beta*W(i,j,r)/gamma*root_cup(N,2*a,2*a-r)
                        *W(d-jj,d-ii,2*a-r)/(pV(d-jj)*pV(d-ii)))
                DD=lambda mid:mp.mpc(1) if a==0 else mid**a*mp.det(matrix(N,a,xx/(2*mid),yy/(2*mid)))
                PP=mp.fprod(xx-Q**v*yy for v in range(a+1,d-a+1))
                candidate=mult*beta**2*DD(bb)*DD(cc)*PP/mp.exp(mp.mpf(d)/2*(mp.log(bb)+mp.log(cc)))
                err=abs(source-candidate)/max(1,abs(candidate));worst=max(worst,err)
                assert err<mp.mpf('1e-65');checks+=1
                # Same degree, actual N-lift of the outgoing first physical head.
                if a==d//2:
                    shifted=(mult*N*beta*W(i,j,r)/gamma*root_cup(N,2*a,2*a-r)
                             *W(d-(jj-N),d-(ii+N),2*a-r)
                             /(pV(d-(jj-N))*pV(d-(ii+N))))
                    assert abs(shifted/source-(-1)**d)<mp.mpf('1e-65');carries+=1
    N,a,j=sp.symbols('N a j',integer=True)
    d=N-1;m=d-a;s=d-2*a
    assert sp.expand(j*(2*a+2)+j*(j-1)+j*(s-j)-j*N)==0
    assert sp.expand(d/2-s/2-a)==0
    assert sp.expand(2*d*(d/2)-d*d)==0
    return dict(literal_large_white_dual_cup_circle_identities=checks,
                retained_N_lift_characters=carries,symbolic_phase_and_mark_identities=3,
                maximum_source_relative_error=str(worst))


def add(p,q):
    out=dict(p)
    for k,v in q.items():out[k]=out.get(k,0)+v
    return out


def mul(p,q):
    out={}
    for i,x in p.items():
        for j,y in q.items():
            key=tuple(a+b for a,b in zip(i,j))
            out[key]=out.get(key,0)+x*y
    return out


def determinant_coefficients(N,a):
    th=mp.pi/N
    before={(0,0,0):mp.mpf(1)}
    if a==0:return before
    now={(1,0,0):1/(2*mp.cos(th)),(0,1,0):mp.mpf(1),(0,0,1):1/(2*mp.cos(th))}
    for n in range(1,a):
        diag=1/(2*mp.cos(n*th)*mp.cos((n+1)*th))
        linear={(1,0,0):diag,(0,1,0):mp.mpf(1),(0,0,1):diag}
        bn=mp.sin(n*th)**2/(mp.cos(n*th)**2*mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))
        negative_product={(2,0,0):-bn/4,(1,0,1):bn*mp.cos(2*n*th)/2,(0,0,2):-bn/4}
        before,now=now,add(mul(linear,now),mul(negative_product,before))
    return now


def positivity_checks():
    determinant_count=det_coeffs=forced_coeffs=0;worst=mp.mpf(0)
    for N in range(3,18):
        d=N-1;Q=mp.exp(2j*mp.pi/N)
        sins=[mp.mpf(1)]
        for k in range(1,N):sins.append(sins[-1]*2*mp.sin(mp.pi*k/N))
        for a in range(d//2+1):
            coeff=determinant_coefficients(N,a)
            assert len(coeff)==(a+1)*(a+2)//2
            assert all(v>0 and sum(k)==a for k,v in coeff.items())
            x,z,y=mp.mpc('1.2','.1'),mp.mpc('.8','-.2'),mp.mpc('1.7','.3')
            value=mp.fsum(v*x**i*z**j*y**k for (i,j,k),v in coeff.items())
            direct=mp.mpc(1) if a==0 else z**a*mp.det(matrix(N,a,x/(2*z),y/(2*z)))
            err=abs(value-direct)/max(1,abs(direct));worst=max(worst,err)
            assert err<mp.mpf('1e-65')
            determinant_count+=1;det_coeffs+=len(coeff)
            s=d-2*a
            poly=[mp.mpc(1)]
            for k in range(a+1,d-a+1):
                nxt=[mp.mpc(0)]*(len(poly)+1)
                for r,v in enumerate(poly):nxt[r]+=v;nxt[r+1]-=Q**k*v
                poly=nxt
            for j,value in enumerate(poly):
                expected=sins[s]/(sins[j]*sins[s-j])
                err=abs(value-expected)/max(1,expected);worst=max(worst,err)
                assert err<mp.mpf('1e-65');forced_coeffs+=1
    return dict(original_D_polynomials=determinant_count,
                strictly_positive_D_coefficients=det_coeffs,
                exact_all_label_positive_forced_coefficients=forced_coeffs,
                maximum_coefficient_identity_error=str(worst))


def support_checks():
    invalid=forced=small=valid=cross=physical_cups=0
    for N in range(3,18):
        p,eta=root_field(N);q=eta*eta%p;Q=q*q%p;d=N-1
        powers=[pow(Q,k,p) for k in range(N)]
        for i in range(N):
            for j in range(N):
                if (i+j-d)%N==0:
                    assert i+j==d;physical_cups+=1
        fs=[1]
        for k in range(1,N):fs.append(fs[-1]*(1-powers[k])%p)
        for a in range(d//2+1):
            m=d-a
            cs=[((-1)**k*pow(Q,k*(k+1)//2,p)
                 *(fs[a]*pow(fs[k]*fs[a-k]%p,-1,p)%p)**2)%p for k in range(a+1)]
            newton=[]
            for i in range(N):
                row=[1]
                for k in range(a):row.append(row[-1]*(powers[i]-powers[k])%p)
                newton.append(row)
            nonzero_by_total={}
            for i in range(N):
                for j in range(N):
                    sig=i+j;T=powers[sig%N]
                    H=sum(cs[k]*pow(powers[j],k,p)*newton[i][k]*newton[j][a-k] for k in range(a+1))%p
                    Ps=1
                    for k in range(a,m):Ps=Ps*(T-powers[k])%p
                    nonzero_by_total.setdefault(sig,[]).append(H)
                    if sig<m or sig>d+a:
                        assert H*Ps%p==0
                        invalid+=1;forced+=int(Ps==0);small+=int(H==0)
                    else:
                        assert 0<=sig-m<=2*a
                        valid+=1
            for sig in range(N-1):
                other=sig+N
                if other>2*d:continue
                T=powers[sig]
                Ps=1
                for k in range(a,m):Ps=Ps*(T-powers[k])%p
                for H in nonzero_by_total[sig]:
                    for HH in nonzero_by_total[other]:
                        assert H*HH*Ps%p==0;cross+=1
    return dict(forbidden_physical_pair_zeros=invalid,retained_forced_zero_cases=forced,
                small_or_complementary_Newton_zero_cases=small,
                actual_unwrapped_supported_pairs=valid,unequal_congruent_total_circle_zeros=cross,
                exact_physical_cup_modular_support=physical_cups)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();mp.mp.dps=85
    result=dict(status='PASS',precision_digits=mp.mp.dps,source=source_checks(),
                positivity=positivity_checks(),support=support_checks(),
                scope='Exact original local circle scalar/carries, all-label positive face polynomials and retained modular-support zeros. No global grid measure, cycle selection or stationary coefficient claim.')
    target=args.output or Path(__file__).with_name('actual_complete_circle_positive_face_polynomial_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
