#!/usr/bin/env python3
"""Original exceptional matrix, literal tensor reshuffle, and positive packet."""
import json
import math
from pathlib import Path
import mpmath as mp
from audit_actual_q_hahn_physical_generic_jet_bound import Jet,matrix,original
from audit_actual_matching_edge_polynomial_finite_propagation import source_polynomial
from audit_high_color_first_normal_r_degree import root_field
from audit_actual_q_hahn_uniform_complex_amplitude import chosen_packet,original_coefficients,evaluate
from audit_actual_q_hahn_joint_complex_amplitude import Source,selected_packet
from audit_actual_q_hahn_selected_complex_action import J


def factorials(q,n):
    F=[q**0]
    for r in range(1,n+1):F.append(F[-1]*(1-q**(2*r)))
    return F


def clebsch(d,a,q,F,i,j,r):
    m=d-a
    assert i+j==m+r
    value=q**0*0
    for s in range(m+1):
        k=j-m+s
        if not (0<=k<=j and 0<=r-k<=i):continue
        highest=(-1)**s*q**(s*(d-2*a-s-1))*F[a+s]*F[d-s]/F[a]/F[d]
        value+=highest*q**(-d*k+2*s*k)/(F[s]*F[m-s]*F[k]*F[r-k])
    return value*F[i]*F[j]


def cup(weight,q,F,r,scale=1):
    return scale*(-1)**r*q**(r*(weight-r-1))*F[r]*F[weight-r]/F[weight]


def generic_tensor_entry(N,a,q,u,v,t=None):
    d=N-1;h=v-u;r=a-h
    if t is None:t=u+v
    if h>a:return q**0*0
    F=factorials(q,d)
    unit=lambda n:(q**n-q**(-n))/(q-q**-1)
    sf=[q**0]
    for n in range(1,d+1):sf.append(sf[-1]*unit(n))
    canceled=q**0
    for n in range(1,d+a+2):
        if n!=N:canceled*=unit(n)
    scalar=(-1)**a*N*N*q**(a*a-2*d*d)*sf[2*a]*sf[d-a]/canceled
    S=(clebsch(d,a,q,F,d-v,u,r)*cup(2*a,q,F,r)
       *clebsch(d,a,q,F,t-u,d-t+v,2*a-r))
    scale=N*q**(-d*d)
    clock=(-1)**d*q**(-d+2*v)
    return scalar*S/(clock*cup(d,q,F,v,scale)*cup(d,q,F,t-v,scale))


def exact():
    tensor=positive=zeros=nonzerojets=0
    for N in range(3,13):
        p,eta=root_field(N);q0=eta*eta%p;Jet.p=p;Jet.order=4
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        qi=Jet(pow(q0,-1,p));qr=Jet(q0)
        Fr=factorials(qr,N-1);Fi=factorials(qi,N-1)
        imag=pow(eta,N,p);s=[1]
        for n in range(1,N):
            s.append(s[-1]*(pow(q0,n,p)-pow(q0,-n,p))*pow(imag,-1,p)%p)
        for t in range(N):
            diag,up,low=matrix(N,q,t)
            for u in range(t//2+1):
                v=t-u;h=v-u
                e=[Jet(int(k==v)) for k in range(t+1)]
                for a in range((N-1)//2+1):
                    out,_,_=source_polynomial(N,q,a,diag,up,low,e,Jet(3))
                    if h>a:
                        assert out[u]==0
                        zeros+=1
                        continue
                    if N<=9:
                        expected=generic_tensor_entry(N,a,q,u,v)
                        assert out[u]==expected,(N,a,t,u)
                        tensor+=1
                        if expected.c[1] or expected.c[2]:nonzerojets+=1
                    f=original(N,qr,N-1-h,a,u,Fr).c[0]
                    fc=original(N,qi,N-1-h,a,u,Fi).c[0]
                    expected=s[a+h]*pow(s[h]**2*s[a-h],-1,p)*f*fc%p
                    assert out[u].c[0]==expected,(N,a,t,u,'square')
                    positive+=1
    return dict(original_four_jet_tensor_reshuffles=tensor,
                original_positive_square_identities=positive,
                all_four_jet_outside_band_zeros=zeros,
                nonzero_retained_normal_entries=nonzerojets)


def numeric_matrix_entry(N,a,u,v,t=None):
    q=mp.exp(mp.pi*1j/N);d=N-1
    if t is None:t=u+v
    D,U,L=matrix(N,q,t)
    term=[mp.mpc(int(r==v)) for r in range(t+1)];value=term[u]
    unit=lambda n:mp.sin(mp.pi*n/N)/mp.sin(mp.pi/N)
    for k in range(a):
        node=q**(2*k+1)+q**(-2*k-1)
        coef=-unit(a-k)*unit(a+k+1)/(unit(k+1)**2*unit(d-k)*unit(d+k+2)*(q-q**-1)**2)
        term=[coef*((D[r]-node)*term[r]+(L[r-1]*term[r-1] if r else 0)
                    +(U[r]*term[r+1] if r<t else 0)) for r in range(t+1)]
        value+=term[u]
    return value


def all_entries():
    identities=germs=products=0
    for N in range(3,12):
        p,eta=root_field(N);q0=eta*eta%p;Jet.p=p;Jet.order=4
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        qr=Jet(q0);qi=qr**-1;F=factorials(qr,N-1);Fi=factorials(qi,N-1)
        s=[1];imag=pow(eta,N,p);d=N-1
        sine=lambda n:(pow(q0,n,p)-pow(q0,-n,p))*pow(imag,-1,p)%p
        for n in range(1,N):s.append(s[-1]*sine(n)%p)
        for a in range(d//2+1):
            for h in range(N):
                product=pow(N,-1,p)
                for r in range(1,d-a+1):product=product*sine(h+r)%p
                for r in range(1,a+1):product=product*sine(h+r)%p
                expected=s[a+h]*pow(s[h]**2*s[a-h],-1,p)%p if h<=a else 0
                assert product==expected;products+=1
        for t in range(N):
            D,U,L=matrix(N,q,t)
            for v in range(t+1):
                e=[Jet(int(k==v)) for k in range(t+1)]
                for a in range(d//2+1):
                    out,_,_=source_polynomial(N,q,a,D,U,L,e,Jet(3))
                    for u in range(v+1):
                        h=v-u
                        if h>a:assert out[u]==0;continue
                        f=original(N,qi,d-h,a,u,Fi).c[0]
                        g=original(N,qr,d-h,a,t-v,F).c[0]
                        expected=pow(q0,-d*(t-u-v),p)*s[a+h]*pow(s[h]**2*s[a-h],-1,p)*f*g%p
                        assert out[u].c[0]==expected,(N,t,a,u,v)
                        identities+=1
                        if N<=7:
                            assert out[u]==generic_tensor_entry(N,a,q,u,v,t)
                            germs+=1
    return dict(all_original_kernel_entries=identities,
                all_entry_generic_tensor_four_jets=germs,
                finite_entire_scalar_products=products)


def complex_kernel():
    mp.mp.dps=160;rows=[];worst=mp.mpf(0);directerr=mp.mpf(0)
    for N in (24,25,48,49,96,97):
        a=(N-1)//2;alpha=mp.mpf(a)/N;src=Source(N,a)
        for complex_case in (False,True):
            if complex_case:
                delta=mp.mpc('.2','.018');nu=mp.mpc('.16','-.012');lam=mp.mpc('.27','.009')
            else:
                delta=mp.mpf(N//5)/N;nu=mp.mpf(N//6)/N;lam=mp.mpf(N//4)/N
            tp=1-delta-mp.mpf(1)/N
            scalar=mp.fprod(2*mp.sin(mp.pi*(delta+mp.mpf(r)/N)) for r in range(1,N-a))
            scalar*=mp.fprod(2*mp.sin(mp.pi*(delta+mp.mpf(r)/N)) for r in range(1,a+1));scalar/=N
            f1=mp.conj(src.determinant(mp.conj(tp),mp.conj(nu)))
            f2=src.determinant(tp,lam)
            direct1=mp.conj(src.direct(mp.conj(tp),mp.conj(nu)));direct2=src.direct(tp,lam)
            err=max(abs(direct1/f1-1),abs(direct2/f2-1));assert err<mp.mpf('1e-110')
            directerr=max(directerr,err)
            value=mp.exp(-mp.pi*1j*(N-1)*(lam-nu))*scalar*f1*f2
            if not complex_case:
                u=int(mp.nint(N*nu));h=int(mp.nint(N*delta));v=u+h;t=v+int(mp.nint(N*lam))
                assert abs(numeric_matrix_entry(N,a,u,v,t)/value-1)<mp.mpf('1e-105')
            phi1,B1,_=selected_packet(mp.conj(tp),alpha,mp.conj(nu))
            phi2,B2,_=selected_packet(tp,alpha,lam)
            H=(J(alpha+delta)-2*J(delta)-J(alpha-delta)+mp.conj(phi1)+phi2
               -mp.pi*1j*(lam-nu))
            C=(mp.exp(mp.pi*1j*(lam-nu))*mp.conj(B1)*B2/(2*mp.sin(mp.pi*delta))
               *mp.sqrt(mp.sin(mp.pi*(alpha+delta))/mp.sin(mp.pi*(alpha-delta))))
            pred=C*mp.exp(N*H)/(N*N)
            scaled=N*abs(value/pred-1);assert scaled<20
            worst=max(worst,scaled)
            rows.append(dict(N=N,complex_case=complex_case,N_times_relative_error=str(scaled)))
    return dict(precision_digits=mp.mp.dps,real_and_complex_kernel_amplitudes=len(rows),
                literal_ordinary_source_comparisons=2*len(rows),
                max_literal_source_relative_error=str(directerr),
                max_N_times_kernel_relative_error=str(worst),cases=rows)


def calibration():
    mp.mp.dps=140;rows=[];worst=mp.mpf(0);sourceerr=mp.mpf(0)
    for N in [24,25,48,49,96,97]:
        for alpha,delta,nu in [('0.5','0.2','0.2'),('0.4','0.1','0.12')]:
            a=min((N-1)//2,int(mp.mpf(alpha)*N));h=int(mp.mpf(delta)*N)
            u=int(mp.mpf(nu)*N);v=u+h;tprime=N-1-h
            x,dd,tt,uu=[mp.mpf(n)/N for n in (a,h,tprime,u)]
            sf=[mp.mpf(1)]
            for n in range(1,N):sf.append(sf[-1]*2*mp.sin(mp.pi*n/N))
            scalar=sf[a+h]/(sf[h]**2*sf[a-h])
            q=mp.exp(mp.pi*1j/N)
            co=original_coefficients(N,tprime,a,u)
            val,_=evaluate(N,co,q**(tprime+a-(N-1)))
            val*=(-1)**u*q**(-(a+1)*u)
            positive=scalar*abs(val)**2
            direct=numeric_matrix_entry(N,a,u,v)
            err=abs(direct/positive-1);assert err<mp.mpf('1e-85')
            sourceerr=max(sourceerr,err)
            w=mp.exp(mp.pi*1j*(tt+x-1))
            psi,amp,saddle,_=chosen_packet(tt,x,uu,w)
            B=amp*mp.exp(mp.pi*1j*(saddle-uu))
            Phi=psi+mp.pi*1j*uu*(1-x)
            predicted=scalar/N*abs(B)**2*mp.exp(2*N*mp.re(Phi))
            scaled=N*abs(positive/predicted-1)
            assert scaled<10
            worst=max(worst,scaled)
            rows.append(dict(N=N,a=a,u=u,v=v,target_total=tprime,
                             original_total=u+v,N_times_relative_error=str(scaled)))
    return dict(precision_digits=mp.mp.dps,actual_operator_amplitudes=len(rows),
                max_literal_matrix_square_relative_error=str(sourceerr),
                max_N_times_operator_relative_error=str(worst),cases=rows)


def main():
    result=dict(status='PASS',exact=exact(),all_entries=all_entries(),calibration=calibration(),complex_kernel=complex_kernel(),
                scope='Actual full physical kernel, genuine physical generic tensor jets and literal root-kernel complex packet; no complex generic-normal, geometric sheet or coherent-source assertion.')
    Path(__file__).with_name('actual_matching_edge_antidiagonal_operator_packet_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'calibration':{k:v for k,v in result['calibration'].items() if k!='cases'},
                     'complex_kernel':{k:v for k,v in result['complex_kernel'].items() if k!='cases'}},indent=2))


if __name__=='__main__':main()
