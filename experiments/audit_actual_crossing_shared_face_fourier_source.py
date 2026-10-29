#!/usr/bin/env python3
"""Whole positive crossing shared-face source, coupled Ward and Fourier norms."""

import json
from pathlib import Path
import mpmath as mp
import sympy as sp
import numpy as np

from audit_finite_sum_annihilator import field
from audit_figure_eight_whole_source import MixedEntries
from audit_actual_modular_dilog_circle import psi
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix,partial


def add(a,b,p):
    out=a.copy()
    for k,v in b.items():out[k]=(out.get(k,0)+v)%p
    return {k:v for k,v in out.items() if v}
def scale(a,c,p):return {k:v*c%p for k,v in a.items() if v*c%p}
def mul(a,b,p):
    out={}
    for i,v in a.items():
        for j,w in b.items():out[i+j]=(out.get(i+j,0)+v*w)%p
    return {k:v for k,v in out.items() if v}
def qshift(a,Q,p):return {k:v*pow(Q,-k,p)%p for k,v in a.items()}


def finite_ward():
    rows=[]
    for N in range(2,12):
        p,_,q=field(N);E=MixedEntries(N,p,q);Q=E.Q
        x=-pow(q,-1,p)%p
        z0,z1,z6,z7=2,3,5,7
        a0=pow(z1,-1,p);b0=pow(x*z0,-1,p)
        f=z7*pow(x*z6,-1,p)%p;r=z6*pow(z0,-1,p)%p
        s0=z6*pow(x,-1,p)%p
        pp=[(-1)**j*pow(Q,j*(j-1)//2,p)*pow(E.F[j],-1,p)%p for j in range(N)]
        B0={0:1};term=1
        for a in range(1,N):
            term=term*(a0-pow(Q,a-1,p)*b0)%p;B0[a]=term
        R={};Bf={}
        for i in range(N):
            for j in range(N-i):
                binom=E.F[i+j]*pow(E.F[i]*E.F[j],-1,p)%p
                R[-j]=(R.get(-j,0)+binom*pow(r,i,p)*pow(s0,j,p))%p
                coeff=E.F[i+j]*pow(E.F[i],-1,p)*pp[j]%p
                Bf[-j]=(Bf.get(-j,0)+coeff*pow(f,i+j,p)*pow(s0,j,p))%p
        DB={0:(1-pow(f,N,p))%p,-N:pow(f*s0,N,p)}
        DR={0:(1-pow(r,N,p))%p,-N:-pow(s0,N,p)%p}
        D0={0:1,N:(pow(b0,N,p)-pow(a0,N,p))%p}
        F=mul(Bf,R,p)
        Hpair=add(mul(DB,R,p),scale(mul(DR,qshift(Bf,Q,p),p),f,p),p)
        assert add(F,scale(qshift(F,Q,p),-f*r,p),p)==Hpair
        linear={1:(b0-Q*f*r*a0)%p,0:Q*f*r%p}
        lhs=mul(linear,mul(B0,F,p),p).get(0,0)
        rhs=add(mul({1:b0},mul(B0,Hpair,p),p),scale(mul(D0,F,p),Q*f*r,p),p).get(0,0)
        assert lhs==rhs
        # The two norm equations cannot be erased independently.
        bezout=add(DB,scale(DR,pow(f,N,p),p),p)
        assert bezout=={0:(1-pow(f*r,N,p))%p} or not bezout and pow(f*r,N,p)==1
        rows.append({'N':N,'paired_full_polynomial_Ward':True,
                     'whole_crossing_linear_Green_source':True,'retained_boundary_norm':True})
    return rows


def logarithmic_algebra():
    A,B,C,D,X,tau=sp.symbols('A B C D X tau')
    beta=B-A-X;f=D-C-X;rho=C-A;sigma=C-tau-X
    original=-beta*(tau-B)-sigma*f-rho*sigma
    separated=(D-B)*tau+beta*B-(C-X)*(f+rho)
    assert sp.expand(original-separated)==0
    return {'full_boundary_Gaussian':True,'affine_two_pi_log_t_source_retained':True}


def physical_green():
    rows=[];word_rows=[]
    for N in range(2,9):
        for color in (1,3):
            H=HardyNetwork(N,color);p,Q,x,d=H.p,H.Q,H.x,N-1
            F=H.fac;iv=H.inv
            pp=[H.v[j]*pow(x,j,p)%p for j in range(N)]
            L=np.zeros((N*N,N*N),dtype=np.int64)
            HG=np.zeros_like(L);HT=np.zeros_like(L);G=np.zeros_like(L)
            triples=[(i,j) for i in range(N) for j in range(N-i)]
            for i,j in triples:
                b0=F[i+j]*iv[i]*pp[j]*pow(x,-j,p)%p
                for r,k in triples:
                    rc=F[r+k]*iv[r]*iv[k]*pow(x,-k,p)%p
                    for h,l in triples:
                        bf=F[h+l]*iv[h]*pp[l]*pow(x,-h-2*l,p)%p
                        coefficient=b0*rc*bf%p
                        power=i+j-k-l
                        # Each physical term keeps BOTH original finite
                        # boundary heads; no monomial is commuted past a cut.
                        candidates=[]
                        if power==-1:
                            candidates += [(j+r+1,i,r+k-h,h+l,pow(x,-1,p)),
                                           (j+r+1,i+1,r+k-h,h+l+1,-Q*pow(x,-1,p))]
                        if power==0:
                            candidates.append((j+r+1,i,r+k-h,h+l+1,Q*pow(x,-1,p)))
                        for a,b,c,e,mult in candidates:
                            if min(a,b,c,e)>=0 and max(a,b,c,e)<N:
                                L[c*N+e,a*N+b]=(L[c*N+e,a*N+b]+mult*coefficient)%p
            for a in range(1,N):
                for b in range(N-a):
                    value=0
                    for j in range(a):
                        r=a-j-1;k=b+j+1
                        b0=F[b+j]*iv[b]*pp[j]*pow(x,-j,p)%p
                        rc=F[a+b]*iv[r]*iv[k]*pow(x,-k,p)%p
                        value=(value+pow(x,-1,p)*b0*rc)%p
                    HG[(a+b)*N,a*N+b]=value
                for e in range(1,a+1):
                    G[(a-e)*N+e,a*N]=Q*pow(x,-e,p)%p
                b=N-a
                for e in range(1,N):
                    HT[(N-e)*N+e,a*N+b]=(-pow(x,-N-a-e,p)*F[d]*iv[N-a]*pp[a-1])%p
            assert np.array_equal(L%p,(HG+HT+G)%p),(N,color)
            cup=np.zeros(N*N,dtype=np.int64);marker=np.zeros(N*N,dtype=np.int64)
            for a in range(N):
                cup[a*N+d-a]=N*pow(x,a-d,p)%p
                for b in range(N):marker[a*N+b]=pow(x,b,p)*pow(N,-2,p)%p
            if color==1:
                assert int(marker@HG@cup)%p==-pow(N,-1,p)%p
                assert int(marker@HT@cup)%p==0
                assert int(marker@G@cup)%p==Q*d*pow(N,-1,p)%p
                assert int(marker@L@cup)%p==(Q*d-1)*pow(N,-1,p)%p
                w=np.zeros(N*N,dtype=np.int64)
                W=np.zeros((N,N),dtype=np.int64)
                for e in range(1,N):
                    w[(N-e)*N+e]=pow(x,-e,p)
                    W[N-e,e]=pow(x,-e,p)
                Etop=-np.outer(w,w)%p
                B=H.plus*pow(H.kappa,-1,p)%p
                Bi=H.minus*H.kappa%p
                assert int(w@w)%p==p-1
                assert np.array_equal(HT%p,Q*Etop%p)
                assert np.array_equal(Etop@Etop%p,Etop)
                assert np.array_equal(B@w%p,w)
                assert np.array_equal(w@B%p,w)
                assert np.array_equal(Bi@w%p,w)
                assert np.array_equal(w@Bi%p,w)
                assert np.array_equal(B@Etop%p,Etop)
                assert np.array_equal(Etop@B%p,Etop)
                simple_HG=np.zeros_like(HG)
                for a in range(1,N):
                    for b in range(N-a):
                        simple_HG[(a+b)*N,a*N+b]=pow(x,-b-2,p)
                assert np.array_equal(HG%p,simple_HG)
                Pnonzero=np.diag([0]+[1]*d)
                assert np.array_equal(W@W%p,pow(x,-N,p)*Pnonzero%p)
                if N<=5:
                    E12=np.kron(Etop,np.eye(N,dtype=np.int64))
                    E23=np.kron(np.eye(N,dtype=np.int64),Etop)
                    assert np.array_equal(E12@E23%p@E12%p,np.kron(Etop,Pnonzero)%p)
                    assert np.array_equal(E23@E12%p@E23%p,np.kron(Pnonzero,Etop)%p)
                flower=np.zeros((N,N),dtype=np.int64)
                for j in range(d):flower[j+1,j]=(1-pow(Q,j+1,p))%p
                kinv=np.diag([pow(x,-1,p)*pow(Q,j,p)%p for j in range(N)])
                normal_F=-np.kron(kinv,flower)%p
                Z1=np.kron(np.diag([pow(Q,j,p) for j in range(N)]),np.eye(N,dtype=np.int64))
                assert np.array_equal(normal_F@cup%p,N*(np.eye(N*N,dtype=np.int64)-Z1)@w%p)
            rows.append({'N':N,'color':color,'complete_physical_Green_endpoint_filtration':True,
                         'ground_output_rank_bound':N-1,'top_total_degree':N,'top_rank':1,
                         'complete_top_carry_idempotent_and_Ward_normal':color==1,
                         'complete_top_carry_fixed_by_original_both_crossings':color==1,
                         'complete_ground_output_unit_phase':color==1,
                         'ground_input_rank':N-1,'complete_original_cap_checked':color==1})
            if color==1 and N<=4:
                eye=np.eye(N,dtype=np.int64)
                word=word_matrix([1,-2,1,-2],H.plus,H.minus,3,N,p)
                values=[]
                for coupon in (L,HG,HT,G):
                    full=word@np.kron(coupon,eye)%p
                    cut=partial(full,H.pivot,3,N,p)
                    values.append(int(cut.sum())*pow(N,-1,p)%p)
                assert values[0]==sum(values[1:])%p
                word_rows.append({'N':N,'original_figure_eight_marked_values':values,
                                  'original_full_pivots_and_average':True})
    return rows,word_rows


def sharp_endpoint_norms():
    """Independent complex-matrix checks in the ORIGINAL Euclidean metric."""
    rows=[]
    for N in range(2,17):
        Q=np.exp(2j*np.pi/N);x=-np.exp(-1j*np.pi/N);d=N-1
        fac=[1+0j]
        for j in range(1,N):fac.append(fac[-1]*(1-Q**j))
        pp=[(-1)**j*Q**(j*(j-1)//2)/fac[j] for j in range(N)]
        largest=0.0;coefficient_error=0.0
        for t in range(1,N):
            gout=np.zeros((t+1,t+1),dtype=complex)
            gin=np.zeros_like(gout)
            for b in range(t):
                a=t-b
                value=x**(-b-2)*fac[a+b]/fac[b]*sum(
                    pp[j]*x**(-2*j)/(fac[a-j-1]*(1-Q**(b+j+1)))
                    for j in range(a))
                coefficient_error=max(coefficient_error,abs(value-x**(-b-2)))
                gout[0,b]=value
            for e in range(1,t+1):gin[e,0]=Q*x**(-e)
            assert abs(np.linalg.norm(gout,2)-np.sqrt(t))<1e-8
            assert abs(np.linalg.norm(gin,2)-np.sqrt(t))<1e-8
            norm=float(np.linalg.norm(gout+gin,2))
            assert abs(norm-np.sqrt(t+np.sqrt(t)))<1e-8,(N,t,norm)
            largest=max(largest,norm)
        w=np.array([x**(-e) for e in range(1,N)])
        top=-Q*np.outer(w,w)
        topnorm=float(np.linalg.norm(top,2))
        assert abs(topnorm-d)<1e-10
        largest=max(largest,topnorm)
        expected=max(d,np.sqrt(d+np.sqrt(d)))
        assert abs(largest-expected)<1e-8
        rows.append({'N':N,'complete_Green_operator_norm':largest,
                     'exact_formula':float(expected),
                     'maximum_partial_fraction_coefficient_error':coefficient_error,
                     'original_flat_metric':True})
    return rows


def complete_root_orbit_source():
    """Original finite boundary blocks, not sectorwise Fourier support."""
    rows=[];words=[]
    for N in range(2,7):
        for color in (1,3):
            H=HardyNetwork(N,color);p,Q,x=H.p,H.Q,H.x
            F,iv=H.fac,H.inv
            pp=[(-1)**j*pow(Q,j*(j-1)//2,p)*iv[j]%p for j in range(N)]
            triples=[(i,j) for i in range(N) for j in range(N-i)]
            averaged={}
            for sign in (1,-1):
                ct=np.zeros((N*N,N*N),dtype=np.int64)
                carry=np.zeros_like(ct)
                for i,j in triples:
                    b0=F[i+j]*iv[i]*pp[j]*pow(x,-j,p)%p
                    for r,k in triples:
                        for h,l in triples:
                            a,b=j+r,i
                            if sign>0:
                                c,e=r+k-h,h+l
                                power=i+j-k-l
                                rc=F[r+k]*iv[r]*iv[k]*pow(x,-k,p)%p
                                bf=F[h+l]*iv[h]*pp[l]*pow(x,-h-2*l,p)%p
                                coefficient=b0*rc*bf%p
                            else:
                                c,e=r+k-l,h+l
                                power=i+j-k-h
                                mid=F[r+k]*iv[r]*pp[k]*pow(x,-k,p)%p
                                final=F[h+l]*iv[h]*iv[l]*pow(x,-l,p)%p
                                n=k+h
                                # ONE original negative Gaussian, including
                                # its powers >=N in the root-average alias.
                                gaussian=(-1)**n*pow(x,2*n,p)*pow(Q,-n*(n-1)//2,p)%p
                                coefficient=b0*mid*final*gaussian%p
                            assert c+e-a-b==-power
                            if min(a,b,c,e)<0 or max(a,b,c,e)>=N:continue
                            if power==0:
                                ct[c*N+e,a*N+b]=(ct[c*N+e,a*N+b]+coefficient)%p
                            elif power%N==0:
                                assert power==-N
                                assert c+e==a+b+N
                                carry[c*N+e,a*N+b]=(carry[c*N+e,a*N+b]+coefficient)%p
                scalar=H.kappa if sign>0 else pow(H.kappa,-1,p)
                literal=H.plus if sign>0 else H.minus
                assert np.array_equal(scalar*ct%p,literal%p),(N,color,sign)
                averaged[sign]=scalar*(ct+pow(2,-N,p)*carry)%p
                rows.append({'N':N,'color':color,'sign':sign,
                             'original_finite_crossing_constant_term':True,
                             'sole_root_orbit_alias_raises_integer_degree_by_N':True,
                             'alias_nonzero_entries':int(np.count_nonzero(carry))})
            if N<=4:
                word=[1,-2,1,-2]
                original=word_matrix(word,H.plus,H.minus,3,N,p)
                sampled=word_matrix(word,averaged[1],averaged[-1],3,N,p)
                origcut=partial(original,H.pivot,3,N,p)
                samplecut=partial(sampled,H.pivot,3,N,p)
                assert np.array_equal(origcut%p,samplecut%p)
                words.append({'N':N,'color':color,'signed_word':word,
                              'entire_original_pivotal_cut_matrix_preserved':True})
    return rows,words


def resonant_fourier_source():
    """Normalize against the independently proved full Fourier scalar."""
    mp.mp.dps=60;rows=[]
    for N in (3,5,8,11):
        h=2j*mp.pi/N
        z=mp.mpc('-.6','1.4');lam=mp.mpc('.3','-.7')
        ph=mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf('1/4')-(N+mp.mpf(1)/N)/12))
        cb=1j*(mp.sqrt(N)+1/mp.sqrt(N))/2
        zeta=mp.exp(-mp.pi*1j*(1+2*cb*cb)/6)
        zeta0=mp.exp(mp.pi*1j*(1-4*cb*cb)/12)
        u=mp.exp(lam);v=mp.exp(lam+z-h)
        total=term=mp.mpc(1)
        for j in range(1,N):
            term*=u-mp.exp(-(j-1)*h)*v;total+=term
        sampled=sum(psi(N,1,z-h*j)*mp.exp(lam*j) for j in range(N))
        sample_error=abs(sampled/(psi(N,1,z)*total)-1)
        assert sample_error<mp.mpf('1e-45')
        homogeneous=(N/mp.conj(ph)*mp.exp(N*lam)*(1-mp.exp(N*z))
                     *psi(N,-1,-h-lam)*mp.exp((z-h)*lam/h))
        # Evaluate the reference's exterior full-Psi from an independent
        # inversion identity; all direct finite products here have Re<0.
        target=(zeta*mp.exp(mp.pi*1j*(mp.sqrt(N)*lam/(2*mp.pi)+cb)**2)
                /psi(N,1,-lam))
        FT=(zeta0/(1j*mp.sqrt(N))*mp.exp(1j*mp.sqrt(N)*lam*cb
              -1j*N*lam*lam/(4*mp.pi))*target)
        H=(1j*mp.sqrt(N)*ph*zeta0*(mp.exp(N*lam)-1)*(1-mp.exp(N*z))
             *mp.exp((N+z/h)*lam))
        normalization_error=abs(homogeneous/(H*FT)-1)
        assert normalization_error<mp.mpf('1e-45')
        A=mp.exp(N*lam)*(1-mp.exp(N*z))
        assert abs(u**N-v**N-A)<mp.mpf('1e-45')
        # The full-turn factor is the same source closure defect; no
        # balanced divisor is imposed in this generic test.
        monodromy=(psi(N,1,z-h*N)*mp.exp(lam*N)/psi(N,1,z))
        assert abs(monodromy-A)<mp.mpf('1e-45')
        rows.append({'N':N,'finite_orbit_Newton_identity_error':float(sample_error),
                     'reference_Fourier_full_scalar_error':float(normalization_error),
                     'actual_deck_norm_equals_Newton_norm':True,
                     'balanced_divisor_not_forced':True})
    return rows


def analytic_fusion():
    mp.mp.dps=55;rows=[]
    for N in (4,7,11):
        h=2j*mp.pi/N;Q=mp.exp(h);x=-mp.exp(-h/2);X=mp.log(x)
        A,B,C,D,tau=map(mp.log,[3,mp.mpf('.4'),mp.mpf('.7'),mp.mpf('1.4'),mp.mpf('1.1')])
        beta=B-A-X;f=D-C-X;rho=C-A;sigma=C-tau-X
        lu=tau-B
        phi=mp.sqrt(N)*mp.exp(mp.pi*1j*(mp.mpf('1/4')-(N+mp.mpf(1)/N)/12))
        S0=N/phi*mp.exp(N*lu)*psi(N,1,h-lu)*psi(N,1,beta)*mp.exp(-beta*lu/h)
        Sf=N/phi*mp.exp(N*f)*psi(N,1,h-f)*psi(N,1,sigma)*mp.exp(-sigma*f/h)
        TR=phi*psi(N,-1,rho-h)*psi(N,-1,sigma-h)*mp.exp(-rho*sigma/h)
        fused=(N*N/phi*mp.exp(N*(lu+f))*(1-mp.exp(N*rho))*(1-mp.exp(N*sigma))
               *psi(N,1,h-lu)*psi(N,1,beta)*psi(N,1,h-f)/psi(N,1,rho)
               *mp.exp(-(beta*lu+sigma*(f+rho))/h))
        error=abs(S0*Sf*TR/fused-1)
        assert error<mp.mpf('1e-43')
        # Exact full-Phi reference Fourier transform; NOT an identification
        # of its real contour with the original lifted Cauchy source.
        cb=1j*(mp.sqrt(N)+1/mp.sqrt(N))/2
        zeta0=mp.exp(mp.pi*1j*(1-4*cb*cb)/12)
        def FT(lam):
            return (zeta0/(1j*mp.sqrt(N))*mp.exp(1j*mp.sqrt(N)*lam*cb-1j*N*lam*lam/(4*mp.pi))
                    *psi(N,1,lam+2j*mp.pi+h))
        lam=mp.mpc('-.3','-1.1')
        fourier_error=abs(FT(lam-2j*mp.pi)/FT(lam)-(1-mp.exp(-N*lam)))
        assert fourier_error<mp.mpf('1e-43')
        rows.append({'N':N,'full_shared_face_fusion_relative_error':float(error),
                     'reference_Fourier_dual_shift_error':float(fourier_error),
                     'original_cycle_not_replaced_by_reference':True})
    return rows


def main():
    physical,words=physical_green()
    orbit,orbitwords=complete_root_orbit_source()
    result={'logarithmic_algebra':logarithmic_algebra(),'finite_current_Green':finite_ward(),
            'physical_endpoint_filtration':physical,'whole_original_word_endpoint_sources':words,
            'sharp_complete_endpoint_norms':sharp_endpoint_norms(),
            'complete_signed_root_orbit_source':orbit,
            'root_orbit_whole_original_words':orbitwords,
            'resonant_reference_Fourier_source':resonant_fourier_source(),
            'exact_full_function_fusion':analytic_fusion(),
            'scope':'exact combined source, retained norms and full crossing Green constraint; '
                    'no automatic current cancellation or Fourier-cycle identification'}
    Path(__file__).with_name('audit_actual_crossing_shared_face_fourier_source_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS ten coupled Ward/Green identities, fourteen physical endpoint filtrations, '
          'same-crossing carry invariance, fifteen sharp flat-metric norm cases, '
          'twenty signed root-orbit layers/six original words/four resonant Fourier sources, '
          'original cap/wholeword sources and three full-Psi fusions/Fourier norm shifts')


if __name__=='__main__':main()
