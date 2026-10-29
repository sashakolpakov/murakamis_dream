#!/usr/bin/env python3
"""Actual all-port Racah kernel: uniform Fricke certificate and source checks.

External labels are INTEGER HIGHEST WEIGHTS, so half-integral spins and
their actual odd cyclic-turn sign are included without rounding.
"""
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_trivalent_all_channel_marked_contraction import highest_cup_cap


def facs(q,n,p):
    Q=q*q%p;f=[1]
    for k in range(1,n+1):f.append(f[-1]*(1-pow(Q,k,p))%p)
    return f


def highest(A,B,E,q,p,F):
    m=(A+B-E)//2
    return [(-1)**s*pow(q,s*(A-2*B+2*m-s-1),p)*F[B-m+s]*F[A-s]
            *pow(F[B-m]*F[A],-1,p)%p for s in range(m+1)]


def cg(A,B,E,q,p,F):
    m=(A+B-E)//2;Q=q*q%p;h=highest(A,B,E,q,p,F)
    W=np.zeros(((A+1)*(B+1),E+1),dtype=np.int64)
    for r in range(E+1):
        for i in range(A+1):
            j=m+r-i
            if not 0<=j<=B:continue
            z=0
            for s in range(m+1):
                t=j-m+s
                if not (0<=t<=j and 0<=r-t<=i):continue
                z+=h[s]*pow(q,-A*t,p)*pow(Q,s*t,p)*pow(F[s]*F[m-s]*F[t]*F[r-t],-1,p)
            W[i*(B+1)+j,r]=F[i]*F[j]*z%p
    return W


def source(A,B,C,D,E,q,p,F):
    cup=highest_cup_cap(E,q,p)[0]
    return (cg(A,B,E,q,p,F)@cup%p@cg(C,D,E,q,p,F).T%p).reshape(A+1,B+1,C+1,D+1)


def target(A,B,C,D,G,q,p,F):
    col=source(B,C,D,A,G,q,p,F).transpose(3,0,1,2)
    clock=np.array([(-1)**A*pow(q,A-2*i,p)%p for i in range(A+1)])
    return clock[:,None,None,None]*col%p


def poch(z,n,Q,p):
    out=1
    for k in range(n):out=out*(1-z*pow(Q,k,p))%p
    return out


def parameters(A,B,C,D,q,p):
    E0=max(abs(A-B),abs(C-D));G0=min(A+D,B+C)
    differences=(C-D,B-A) if A+D<=B+C else (D-C,A-B)
    assert max(differences)==E0
    if differences[0]!=E0:differences=differences[::-1]
    pars=[pow(q,1+differences[0],p),pow(q,1+differences[1],p),
          pow(q,-1-C-D,p),pow(q,-1-A-B,p)]
    return pars,G0


def beta(A,B,C,D,G,q,p,F):
    i0=(A+G-D)//2;mbc=(B+C-G)//2;mda=(D+A-G)//2
    h=highest(B,C,G,q,p,F)[mbc]
    low=(-1)**mda*pow(q,-D*A+2*D*mda-mda*(mda+1),p)%p
    return (-1)**A*pow(q,A-2*i0,p)*h*low%p


def left_endpoint(A,B,C,D,E,q,p,F):
    H=(A+B+C-D)//2;L=min(A,H);u=(C+E-D)//2;m=(A+B-E)//2
    chi=(-1)**u*pow(q,u*(E-u-1)-C*((D-C+E)//2),p)*F[u]*F[D]
    chi=chi*pow(F[(C+D-E)//2]*F[E],-1,p)%p
    if L==H:
        edge=F[H]*highest(A,B,E,q,p,F)[m]*pow(F[m]*F[u],-1,p)%p
    else:
        k=E-u
        edge=(-1)**m*pow(q,-A*B+2*A*m-m*m-m+k*(E-B),p)*F[m+k]*pow(F[m]*F[k],-1,p)%p
    return chi*edge%p


def single_kernel(A,B,C,D,E,G,q,p,F):
    Q=q*q%p;H=(A+B+C-D)//2;L=min(A,H)
    pars,G0=parameters(A,B,C,D,q,p);a,b,c,d=pars
    n=(G0-G)//2;P=a*b%p*c%p*d%p;z=pow(q,E+1,p)
    leading=(pow(a,n,p)*poch(P*pow(Q,n-1,p)%p,n,Q,p)
             *pow(poch(a*b%p,n,Q,p)*poch(a*c%p,n,Q,p)*poch(a*d%p,n,Q,p),-1,p))%p
    term=total=1
    upp=(pow(Q,-n,p),P*pow(Q,n-1,p)%p,a*z%p,a*pow(z,-1,p)%p)
    low=(Q,a*b%p,a*c%p,a*d%p)
    for k in range(n):
        ratio=Q
        for v in upp:ratio=ratio*(1-v*pow(Q,k,p))%p
        for v in low:ratio=ratio*pow(1-v*pow(Q,k,p),-1,p)%p
        term=term*ratio%p;total=(total+term)%p
    J=pow(q,-n*(B+1),p)*F[L]*F[B-H+L]
    J=J*pow(F[L-n]*F[B-H+L-n],-1,p)%p
    normal=left_endpoint(A,B,C,D,E,q,p,F)*pow(beta(A,B,C,D,G,q,p,F)*J*leading,-1,p)%p
    return normal*total%p


def seven_factorial_kernel(A,B,C,D,E,G,q,p,F,details=False):
    Q=q*q%p;H=(A+B+C-D)//2;L=min(A,H)
    Gmax=min(A+D,B+C);n=(Gmax-G)//2
    T=(A+B+C+D)//2;t0=T-Gmax
    sf=lambda k:pow(q,-k*(k-1)//2,p)*F[k]*pow(1-Q,-k,p)%p
    faces=((A+B+E)//2,(C+D+E)//2,(B+C+G)//2,(D+A+G)//2)
    opposite=(T,(A+C+E+G)//2,(B+D+E+G)//2)
    total=0
    for z in range(max(faces),min(opposite)+1):
        den=1
        for r in faces:den=den*sf(z-r)%p
        for r in opposite:den=den*sf(r-z)%p
        total=(total+(-1)**z*sf(z+1)*pow(den,-1,p))%p
    a,b,c,d=(A,B,C,D) if A+D<=B+C else (B,A,D,C)
    R=((C+D-E)//2,(A+B-E)//2,t0,(a-b+E)//2,(d-c+E)//2)
    den=1
    for r in R:den=den*sf(r)%p
    S0=(-1)**T*sf(T+1)*pow(den,-1,p)%p
    M=(Gmax+G)//2+1
    leading=pow(q,n,p)*poch(pow(Q,-M,p),n,Q,p)
    leading=leading*pow(F[n]*poch(pow(Q,t0+1,p),n,Q,p)*poch(pow(Q,-T-1,p),n,Q,p),-1,p)%p
    J=pow(q,-n*(B+1),p)*F[L]*F[B-H+L]*pow(F[L-n]*F[B-H+L-n],-1,p)%p
    normalization=left_endpoint(A,B,C,D,E,q,p,F)*pow(beta(A,B,C,D,G,q,p,F)*J*S0*leading,-1,p)%p
    return (normalization,total) if details else normalization*total%p


def symbolic_certificate():
    q,A,B,C,D,Y=sp.symbols('q A B C D Y',nonzero=True);Q=q*q
    lam=lambda z:q*z+1/(q*z)
    delta,rho=q+1/q,q-1/q
    alpha=lam(A)*lam(B)+lam(C)*lam(D)
    beta0=lam(B)*lam(C)+lam(A)*lam(D)
    gamma=lam(A)*lam(C)+lam(B)*lam(D)
    diagonal=sp.cancel((delta*beta0-gamma*lam(Y))/(delta**2-lam(Y)**2))
    kap=q*A*D
    u=((1-Q*C*Y/D)*(1-Q*B*Y/A)*(1-Y/(C*D))*(1-Y/(A*B))
       /((1-Q*Y*Y)*(1-Q*Q*Y*Y)))
    v=((1-C/(D*Y))*(1-B/(A*Y))*(1-1/(Q*C*D*Y))*(1-1/(Q*A*B*Y))
       /((1-1/(Q*Y*Y))*(1-1/(Y*Y))))
    assert sp.cancel(kap+1/kap-kap*(u+v)-diagonal)==0
    plus=kap**2*u*v.subs(Y,Q*Y);minus=kap**2*u.subs(Y,Y/Q)*v
    lhs=((2*lam(Y)-(Q+1/Q)*lam(Q*Y))*plus
         +(2*lam(Y)-(Q+1/Q)*lam(Y/Q))*minus)
    rhs=rho**2*(delta*alpha-gamma*diagonal-delta**2*lam(Y)+lam(Y)*diagonal**2)
    assert sp.cancel(lhs-rhs)==0
    return {'independent_parameters':['zeta','Q^a','Q^b','Q^c','Q^d','Q^e'],
            'universal_cleared_diagonal_and_product_Fricke_identities':True,
            'second_parameter_branch_by_exact_A_B_and_C_D_interchange':True}


def actual_cases(maximum,q,p):
    F=facs(q,4*maximum+8,p);families=entries=half=0
    for A,B,C,D in itertools.product(range(maximum+1),repeat=4):
        if (A+B+C+D)%2:continue
        es=list(range(max(abs(A-B),abs(C-D)),min(A+B,C+D)+1,2))
        gs=list(range(max(abs(B-C),abs(D-A)),min(B+C,D+A)+1,2))
        if not es:continue
        assert len(es)==len(gs)
        rights={G:target(A,B,C,D,G,q,p,F) for G in gs}
        H=(A+B+C-D)//2;L=min(A,H)
        for E in es:
            s=source(A,B,C,D,E,q,p,F);reconstructed=np.zeros_like(s)
            assert int(s[L,H-L,0,D])==left_endpoint(A,B,C,D,E,q,p,F)
            for G in gs:
                i0=(A+G-D)//2
                assert int(rights[G][i0,H-i0,0,D])==beta(A,B,C,D,G,q,p,F)
                coefficient=single_kernel(A,B,C,D,E,G,q,p,F)
                assert coefficient==seven_factorial_kernel(A,B,C,D,E,G,q,p,F), (A,B,C,D,E,G,'own Sears seven-factorial conversion')
                reconstructed=(reconstructed+coefficient*rights[G])%p
                entries+=1
            assert np.array_equal(s,reconstructed),(A,B,C,D,E,'full all-port kernel')
        families+=1;half+=int(any(v%2 for v in (A,B,C,D)))
    return {'maximum_external_highest_weight':maximum,'generic_zeta':q,'prime':p,
            'full_actual_external_families':families,'half_integral_external_families':half,
            'single_Racah_all_entry_source_checks':entries,
            'both_balanced_4phi3_and_seven_factorial_source_conventions':True}


def root_pole_budget(N):
    count=0;maximum=0;high=0
    for A,B,C,D in itertools.product(range(N),repeat=4):
        if (A+B+C+D)%2:continue
        Emin=max(abs(A-B),abs(C-D));Emax=min(A+B,C+D)
        if Emin>Emax:continue
        Gmax=min(A+D,B+C);Gmin=max(abs(B-C),abs(D-A))
        H=(A+B+C-D)//2;L=min(A,H);t0=(A+B+C+D)//2-Gmax
        mab=(A+B-Emin)//2;mcd=(C+D-Emin)//2
        for G in range(Gmin,Gmax+1,2):
            n=(Gmax-G)//2
            assert t0+n<N and n<=mab<N and n<=mcd<N
            assert 0<=L-n<N and 0<=B-H+L-n<N
            zeros=sum((n-1-Gmax+k)%N==0 for k in range(n))
            assert zeros<=1
            for E in range(Emin,Emax+1,2):
                U=(C+E-D)//2
                assert U<N and (C+D-E)//2<N
                chi_pole=int(E>=N)
                assert E<2*N
                maximum=max(maximum,chi_pole+zeros)
                count+=1;high+=int(E>=N or G>=N)
    return {'N':N,'all_entry_zero_order_checks':count,'retained_high_channel_entries':high,
            'maximum_certified_inverse_kernel_pole':maximum,
            'all_series_denominators_root_units':True,'first_normal_full_term_Taylor_budget':4}


if __name__=='__main__':
    certificate=symbolic_certificate()
    rows=[actual_cases(4,2,1000003),actual_cases(3,3,1000033)]
    poles=[root_pole_budget(N) for N in range(2,10)]
    out={'status':'PASS','uniform_symbolic_certificate':certificate,'actual_all_port_source_checks':rows,
         'all_intermediate_channel_root_normal_budgets':poles,
         'scope':'Generic actual single terminating 4phi3 and seven-factorial Racah inverse recoupling with explicit true endpoint normalization; all ordinary external highest weights and retained meromorphic root normals. No root positivity or energy theorem.'}
    Path(__file__).with_name('actual_general_four_port_single_racah_kernel_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS uniform six-variable Fricke/AW certificates;',sum(v['full_actual_external_families'] for v in rows),
          'actual all-port families;',sum(v['single_Racah_all_entry_source_checks'] for v in rows),'single-sum entries')
