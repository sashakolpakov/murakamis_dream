#!/usr/bin/env python3
"""Original paired white/cup source and genuine scaled generic recurrence.

Uniform estimates are proved in the note; sampled rates are diagnostics.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp

from audit_actual_q_hahn_complementary_hard_edge import det_pair, low_series
from audit_actual_q_hahn_small_channel_generic_normals import scalar_K, jacobi, gauss
from audit_actual_matching_edge_generic_deficient_operator_lift import white, scalar, continued
from audit_actual_matching_edge_antidiagonal_operator_packet import factorials
from audit_actual_matching_edge_deficient_packet_regulator import beta, V, C
from audit_actual_q_hahn_generic_resonant_hard_edge import reindexed, top


def source_H(q,N,m,U,Vv):
    return low_series(q,N,m,U,Vv)


def exact_circle(N,a,sigma,R,S):
    q=mp.exp(mp.pi*1j/N);Q=q*q;d=N-1;m=d-a
    T=q**(2*sigma);Uo=q**(2*R);Ui=q**(2*S)
    P=mp.fprod(T-Q**j for j in range(a,m))
    fold=1 if 2*a==d else 2
    return (fold*V(N,a,d-sigma)*q**(d*(R+S-sigma)-2*a*a)
            *source_H(q,N,m,Uo,T/Uo)*source_H(q,N,m,Ui,T/Ui)/(T**a*P**2))


def literal_root_lift(N,a,sigma,R,S):
    q=mp.exp(mp.pi*1j/N);d=N-1;s=d-2*a
    u=sigma-R;v=d-R;ell=S;h=d-sigma;r=a-h
    F=factorials(q,d)
    coeff=N*N*q**(a*a-2*d*d)*beta(N,a)
    pc=N*q**(2*a*r-s*h)/(F[2*a]*V(N,a,h))
    pv=lambda x:N*q**(-d*d+d*x)
    clock=(-1)**d*q**(-d+2*v)
    K=(coeff*q**(s*h)*white(N,a,q,sigma,R,F)*white(N,a,q,sigma,S,F)
       *pc/(clock*pv(v)*pv(ell)))
    fold=1 if 2*a==d else 2
    restored=fold*N*q**(d*(ell-u))*mp.exp(2*mp.pi*1j*v)*K
    return K,restored


def normalization():
    identities=literal=character=barnes=0;worst=mp.mpf(0)
    for N in (5,6,9,10,13,14):
        q=mp.exp(mp.pi*1j/N)
        for a in sorted({1,(N-1)//2}):
            for offset in (mp.mpc('.13','.17'),mp.mpc('.31','-.23')):
                sigma=N*offset;R=N*mp.mpc('.42','.14');S=N*mp.mpc('.16','-.11')
                actual=C(N,a,sigma,R,S)
                alt=exact_circle(N,a,sigma,R,S)
                err=abs(alt/actual-1);assert err<mp.mpf('1e-100')
                worst=max(worst,err);identities+=1
                K,restored=literal_root_lift(N,a,sigma,R,S)
                err=abs(restored/actual-1);assert err<mp.mpf('1e-100')
                worst=max(worst,err);literal+=1
                v=N-1-R
                assert abs(mp.exp(-2*mp.pi*1j*R)/mp.exp(2*mp.pi*1j*v)-1)<mp.mpf('1e-100')
                character+=1
    # Independent moving-Gamma/root-cup implementation from the original lift.
    for N,a in ((7,3),(8,3)):
        sigma=N*mp.mpc('.71','.23');R=N*mp.mpc('.43','.07');S=N*mp.mpc('.21','-.09')
        u=sigma-R;v=N-1-R;t=v+S
        direct=continued(N,a,0,t,u,v,'root')
        val,_=literal_root_lift(N,a,sigma,R,S)
        err=abs(direct/val-1);assert err<mp.mpf('1e-90')
        worst=max(worst,err);barnes+=1
    return dict(exact_full_circle_normalizations=identities,
                original_white_channel_cup_physical_cap_restorations=literal,
                retained_turn_characters=character,independent_root_Barnes_checks=barnes,
                maximum_source_error=str(worst))


def actual_frame(N,c=mp.mpf('.7'),alpha=mp.mpf('.21'),j=1):
    q=mp.exp(mp.pi*1j/N);Q=q*q
    sf=mp.exp(-2*mp.pi*1j*alpha)-1
    rr=1/(1-Q**(-j))
    F=mp.matrix([[rr,1-rr],[sf,-sf]])
    E=mp.matrix([[1,0],[0,0]]);Pi=F*E*F**-1
    A=mp.matrix([[-1,0],[4,-1]]);B=mp.matrix([[-1,-1],[0,-1]])
    P=B*A;collar=mp.eye(2)-1j/(2*c)*(P+mp.eye(2))
    Ao=collar**-1*A*collar;W=A**-1
    tr=lambda M:mp.fsum((M*Pi)[k,k] for k in range(2))
    Uiraw=-tr(W)/tr(A*W);Viraw=-tr(A*W)/tr(P*W)
    Uoraw=-tr(W)/tr(Ao*W)
    logq=mp.pi*1j/N
    Sin=mp.log(Uiraw)/(2*logq)-mp.mpf('.5')
    Din=mp.log(Viraw)/(2*logq)-mp.mpf('.5')
    lo=mp.log(Uoraw)
    if mp.im(lo)<0:lo+=2*mp.pi*1j
    Rout=lo/(2*logq)-mp.mpf('.5')
    return Sin+Din,Rout,Sin,sf


def packet(N,a,sigma,R,S):
    q=mp.exp(mp.pi*1j/N);Q=q*q;d=N-1;m=d-a;s=m-a
    T=q**(2*sigma);Ui=q**(2*S);Vi=T/Ui;Uo=q**(2*R);Vo=T/Uo
    P=mp.fprod(T-Q**j for j in range(a,m));fold=1 if s==0 else 2
    Ki=mp.sin(mp.pi*m/N)**2*(Vi-1)/(mp.pi**2*(Ui/N**2)*Vi)
    Zi=top(q,N,m,Ui,Vi)
    out=Vo**m*Uo**s*gauss(Q,2*a,a)*det_pair(N,a,Uo)
    pref=(fold*V(N,a,d-sigma)*q**(d*(R+S-sigma)-2*a*a)
          *Zi*out/(T**a*P**2))
    incoming=Zi*reindexed(q,N,m,Ui,Vi)
    outgoing=source_H(q,N,m,Uo,Vo)
    actual=(fold*V(N,a,d-sigma)*q**(d*(R+S-sigma)-2*a*a)
            *incoming*outgoing/(T**a*P**2))
    return actual,pref,mp.besselj(0,2*mp.sqrt(Ki))


def paired_rates():
    rows=[];maxerr=mp.mpf(0)
    for N in (32,65,128,257):
        sigma,R,S,sf=actual_frame(N)
        for a in sorted({(N-1)//2,(N-1)//2-1}):
            actual,pref,model=packet(N,a,sigma,R,S)
            err=N*abs(actual/pref-model)
            assert err<100
            maxerr=max(maxerr,err)
            assert abs(model)>.1
            rows.append(dict(N=N,separation=N-1-2*a,N_absolute_error=str(err),
                             bessel_modulus=str(abs(model)),
                             relative_packet_error=str(abs(actual/(pref*model)-1))))
    return dict(actual_paired_frame_full_circle_packets=len(rows),
                maximum_N_absolute_error=str(maxerr),profiles=rows)


def scaled_matrix(N,a,q,sigma,R,root_upper):
    U=q**(2*R);Vv=q**(2*(sigma-R));b=q**sigma;z=b/U
    al,be=jacobi(N,q,b,a)
    M=mp.eye(a)
    for n in range(a):M[n,n]=1+al[n]/z
    for n in range(1,a):
        M[n-1,n]=root_upper[n-1]
        M[n,n-1]=-be[n]/(z*z*root_upper[n-1])
    return M,Vv,z


def genuine220():
    identities=cofactors=circles=normals=0;worst=mp.mpf(0);maxratio=mp.mpf(0)
    for N in (20,21,40,41):
        sigma,R,S,sf=actual_frame(N);q0=mp.exp(mp.pi*1j/N);th=mp.pi/N
        U0=q0**(2*R);V0=q0**(2*(sigma-R))
        for a in sorted({(N-1)//2,(N-1)//2-1}):
            m=N-1-a;root=source_H(q0,N,m,U0,V0)
            upper=[]
            for n in range(1,a):
                bn=mp.sin(n*th)**2/(mp.cos(n*th)**2*mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th))
                upper.append(-mp.sqrt(bn)*(q0*U0/2*(mp.sin(n*th)-1j*mp.cos(n*th))
                                      +1/(2*q0*V0)*(mp.sin(n*th)+1j*mp.cos(n*th))))
            for direction in (1,-1,1j,-1j):
                eps=mp.mpf('.01')*direction/N**10;q=q0*mp.exp(eps)
                U=q**(2*R);Vv=q**(2*(sigma-R))
                M,Vv,z=scaled_matrix(N,a,q,sigma,R,upper)
                det=mp.det(M)
                small=source_H(q,N,a,U,Vv)/(Vv**a*scalar_K(N,q,a))
                err=abs(det/small-1);assert err<mp.mpf('1e-90');worst=max(worst,err)
                identities+=1
                inv=M**-1
                prev=mp.det(M[:a-1,:a-1]) if a>1 else 1
                assert abs(prev/det-inv[a-1,a-1])<mp.mpf('1e-90')
                assert abs(inv[a-1,a-1])<5;cofactors+=1
                actual=source_H(q,N,m,U,Vv)
                ratio=abs(actual/root)
                assert ratio<10;maxratio=max(maxratio,ratio);circles+=1
            for order in (1,2):
                fun=lambda e:source_H(q0*mp.exp(e),N,m,
                                    mp.exp(2*R*(mp.pi*1j/N+e)),
                                    mp.exp(2*(sigma-R)*(mp.pi*1j/N+e)))
                value=mp.diff(fun,0,order)
                assert abs(value/root)/N**(10*order)<10;normals+=1
    return dict(actual_scaled_generic_determinants=identities,independent_cofactor_checks=cofactors,
                genuine_large_220_circle_checks=circles,genuine_large_220_normals=normals,
                maximum_determinant_identity_error=str(worst),maximum_relative_circle_ratio=str(maxratio))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    mp.mp.dps=140
    result=dict(status='PASS',precision_digits=mp.mp.dps,source=normalization(),
                packet=paired_rates(),generic=genuine220(),
                scope='Actual full root circle restoration and original generic220 numerator control. Full generic operator estimate is a proved factor-by-factor consequence; no leading normal amplitude or global relative cycle coefficient.')
    path=args.output or Path(__file__).with_name('actual_q_hahn_paired_resonant_circle_packet_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
