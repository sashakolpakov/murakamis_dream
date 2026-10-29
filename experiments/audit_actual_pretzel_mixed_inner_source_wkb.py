#!/usr/bin/env python3
"""Literal mixed core, endpoint wall, analytic ratio and selected WKB."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_exact_factorial_interpolation import factorial


def poch(a,Q,n):return mp.fprod(1-a*Q**j for j in range(n))


def finite_case(N):
    p,eta,q,*_=balanced_data(N);Q=q*q%p;M=(N-1)//2
    F=[1]
    for j in range(1,N):F.append(F[-1]*(1-pow(Q,j,p))%p)
    count=0;sears_count=0;source_phase_count=0
    def fp(a,base,n):
        value=1
        for j in range(n):value=value*(1-a*pow(base,j,p))%p
        return value
    for h in range(M+1):
        for v in range(h,M+1):
            x=pow(q,N-1,p);a=N-1-v
            sine_square=pow(-1,a,p)*pow(q,-a*(a+1),p)*F[a]*F[a]%p
            actual=sine_square*pow(q,h*h-v*v,p)*F[2*v]*pow(F[v-h]*F[v+h]%p,-1,p)%p
            expected=N*N*pow(q,h*h,p)*F[2*v]*pow(F[v]*F[v]*F[v-h]*F[v+h]%p,-1,p)%p
            assert actual*pow(x,v,p)%p==expected
            source_phase_count+=1
        A=[]
        for r in range(M+1):
            A.append(sum(pow(Q,-v*r,p)*F[2*v]*pow(F[v]*F[v-h]*F[v+h]*F[v-r]%p,-1,p)
                         for v in range(max(h,r),M+1))%p)
        A +=[0,0]
        H=pow(Q,h,p);T=(H+pow(H,-1,p))%p
        for r in range(M+1):
            Y=pow(Q,r,p)
            ward=(Q*Y*Y*(1-Q*Q*Y)*A[r+2]+Y*(T*pow(Q,3,p)*Y*Y+Q+1)*A[r+1]
                  -Q*(Q*Y+1)*(Q*Y*Y-1)*A[r])%p
            assert ward==0
            if r>=h:
                D=pow(Q,-r*r,p)*F[2*r]*pow(F[r]*F[r-h]*F[r+h]%p,-1,p)%p
                U=A[r]*pow(D,-1,p)%p
                if N%2:
                    n=M-r
                    pref=fp(q*pow(Q,h,p)%p,Q,n)*pow(fp(pow(Q,r+h+1,p),Q,n),-1,p)%p
                    transformed=pref*sum(fp(pow(Q,2*r+1,p),Q*Q%p,j)*fp(-pow(Q,-h,p),Q,j)*pow(Q,j,p)
                        *pow(fp(pow(Q,2*r+2-2*h,p),Q*Q%p,j)*F[j]%p,-1,p) for j in range(n+1))%p
                    assert U==transformed
                    sears_count+=1
                if r<M:
                    den=(1-Q*Y*pow(H,-1,p))*(1-Q*Y*H)%p
                    pp=-pow(Q,-2,p)*pow(Y,-1,p)*(T*pow(Q,3,p)*Y*Y+Q+1)*pow(den,-1,p)%p
                    denn=(1-Q*Q*Y*pow(H,-1,p))*(1-Q*Q*Y*H)%p
                    qq=-pow(Q,-4,p)*pow(Y,-2,p)*(1-Q*Q*Y)*(1-pow(Q,3,p)*Y*Y)*(1+Q*Q*Y)*pow(den*denn%p,-1,p)%p
                    D1=pow(Q,-(r+1)**2,p)*F[2*r+2]*pow(F[r+1]*F[r+1-h]*F[r+1+h]%p,-1,p)%p
                    U1=A[r+1]*pow(D1,-1,p)%p
                    if r+1<M:
                        D2=pow(Q,-(r+2)**2,p)*F[2*r+4]*pow(F[r+2]*F[r+2-h]*F[r+2+h]%p,-1,p)%p
                        U2=A[r+2]*pow(D2,-1,p)%p
                    else:U2=0;assert qq==0
                    assert (U-pp*U1-qq*U2)%p==0
                if r==M:assert U==1
            count+=1
    return {'N':N,'all_integer_color_index_Wards':count,'normalized_terminal_wall':True,
            'literal_low_core_marked_phases':source_phase_count,
            'odd_finite_mixed_balanced_transform_packets':sears_count}


def pq(tau,chi,eps):
    Q=mp.exp(2*mp.pi*mp.j*eps);Y=mp.exp(2*mp.pi*mp.j*tau);H=mp.exp(2*mp.j*chi)
    T=H+1/H;den=lambda z:(1-z/H)*(1-z*H)
    p=-Q**-2/Y*(T*Q**3*Y**2+Q+1)/den(Q*Y)
    q=-Q**-4/Y**2*(1-Q**2*Y)*(1-Q**3*Y**2)*(1+Q**2*Y)/(den(Q*Y)*den(Q**2*Y))
    return p,q


def mu(tau,chi):
    Y=mp.exp(2*mp.pi*mp.j*tau);p,q=pq(tau,chi,0);c=mp.cot(mp.pi*tau)**2
    baseline=Y**-2*(1+c)**2
    return (p-Y**-1*(1+c)*mp.sqrt((p*p+4*q)/baseline))/2


def nu_over_mu(tau,chi):
    m=mu(tau,chi);p0,q0=pq(tau,chi,0)
    p1=mp.diff(lambda e:pq(tau,chi,e)[0],0)
    q1=mp.diff(lambda e:pq(tau,chi,e)[1],0)
    dm=mp.diff(lambda t:mu(t,chi),tau)
    return (p1+q1/m-q0*dm/m**2)/(1+q0/m**2)/m


def literal_U(N,r,chi):
    q=mp.exp(mp.j*mp.pi/N);Q=q*q;H=mp.exp(2*mp.j*chi);n=(N-1)//2-r
    # Exact finite factorial completion: complex h only enters the two
    # below-N factorial shift ratios, not a fitted recurrence solution.
    return mp.fsum(poch(q*Q**r,Q,k)*poch(-q*Q**r,Q,k)*poch(-Q**(r+1),Q,k)*Q**(-r*k)
                   /(poch(Q,Q,k)*poch(Q**(r+1)/H,Q,k)*poch(Q**(r+1)*H,Q,k)) for k in range(n+1))


def ratio(N,tau,chi,terminal_offset=0):
    L=int(mp.ceil(mp.mpf('.21')*N));eps=mp.mpf(1)/N
    z=mu(tau+L*eps,chi)+terminal_offset
    for j in reversed(range(L)):
        p,q=pq(tau+j*eps,chi,eps);z=p+q/z
    return z


def complex_factorial_source_case(N):
    mp.mp.dps=65;M=(N-1)//2;r=int(mp.ceil(mp.mpf('.3')*N))
    chi=mp.mpc('.025','.012');h=N*chi/mp.pi;Q=mp.exp(2*mp.pi*mp.j/N)
    F=[mp.mpc(1)]
    for j in range(1,N):F.append(F[-1]*(1-Q**j))
    fm,fplus=factorial(N,r-h),factorial(N,r+h)
    D=Q**(-r*r)*F[2*r]/(F[r]*fm*fplus)
    total=mp.mpc(0);a,b=fm,fplus
    for v in range(r,M+1):
        total+=Q**(-v*r)*F[2*v]/(F[v]*a*b*F[v-r])
        a*=1-Q**(v+1-h);b*=1-Q**(v+1+h)
    assert abs(total/D-literal_U(N,r,chi))<mp.mpf('1e-45')*max(1,abs(total/D))
    return {'N':N,'canonical_complex_factorial_source':True}


def wkb_case(N):
    mp.mp.dps=85;rows=[]
    for position,chi in ((mp.mpf('.32'),mp.mpc(0)),(mp.mpf('.4'),mp.mpc('.04')),
                         (mp.mpf('.35'),mp.mpc('.025','.012'))):
        r=int(position*N);tau=mp.mpf(r)/N;U=literal_U(N,r,chi)
        physical=U/literal_U(N,r+1,chi)
        interpolated=ratio(N,tau,chi)
        assert abs(interpolated-physical)<mp.mpf('1e-55')*max(1,abs(physical))
        assert abs(ratio(N,tau,chi,mp.mpf('.1'))-interpolated)<mp.mpf('1e-55')
        trial=mu(tau,chi)*(1+nu_over_mu(tau,chi)/N)
        assert N*N*abs(physical-trial)<400
        S=mp.quad(lambda t:mp.log(mu(t,chi)),[tau,mp.mpf('.5')])
        C=mp.sqrt(mu(tau,chi))*mp.exp(mp.quad(lambda t:nu_over_mu(t,chi),[tau,mp.mpf('.5')]))
        prediction=C*mp.exp(N*S);error=U/prediction-1
        assert N*abs(error)<30
        if not chi:
            S0=mp.j*mp.pi*(mp.mpf('.5')-tau)**2
            C0=mp.sqrt(mp.sin(mp.pi*tau))*mp.exp(-3*mp.pi*mp.j*(mp.mpf('.5')-tau)/2)
            assert abs(S-S0)<mp.mpf('1e-55') and abs(C-C0)<mp.mpf('1e-55')
        rows.append({'r':r,'chi':[float(mp.re(chi)),float(mp.im(chi))],
                     'N_times_relative_source_amplitude_error':float(N*abs(error)),
                     'literal_selected_ratio_exact':True})
    return {'N':N,'rows':rows}


def newton_factor_case(N,integer):
    mp.mp.dps=60
    q=mp.exp(mp.j*mp.pi/N);eta=mp.mpc('.9','.012')
    tau=mp.mpc('.28','.004')
    r=int(mp.ceil(mp.mpf('.28')*N)) if integer else N*tau
    ap=(N+1)/2-mp.j*N*eta/(2*mp.pi)
    am=(N+1)/2+mp.j*N*eta/(2*mp.pi)
    actual=q**(-r*r)*factorial(N,ap+r-1)*factorial(N,am+r-1)/(factorial(N,ap-1)*factorial(N,am-1))
    if integer:
        expected=mp.fprod(2*mp.cos((2*a+1)*mp.pi/N)+2*mp.cosh(eta) for a in range(r))
        error=abs(actual/expected-1)
        assert error<mp.mpf('1e-40')
    else:
        phase=mp.quad(lambda v:mp.log(2*mp.cosh(eta)+2*mp.cos(v)),[0,2*mp.pi*tau])/(2*mp.pi)
        expected=mp.exp(N*phase);error=abs(actual/expected-1)
        assert N*error<20
    return {'N':N,'physical_integer_r':integer,'relative_marked_Newton_error':float(error)}


if __name__=='__main__':
    fields=[finite_case(N) for N in range(2,19)]
    source=[complex_factorial_source_case(N) for N in (8,9,12,13)]
    wkb=[wkb_case(N) for N in (32,33,64,65,128,129)]
    newton=[newton_factor_case(N,integer) for N,integer in ((8,True),(9,True),(12,False),(24,False))]
    result={'status':'PASS','all_index_original_finite_packets':fields,
            'whole_complex_factorial_source':source,'selected_holomorphic_source_WKB':wkb,
            'canonical_analytic_Newton_factor':newton,
            'scope':'Low core only; exact endpoint-source interpolation and proved analytic EM remainder. Upper R P band and outer mixed-color cycle retained separately.'}
    Path(__file__).with_name('actual_pretzel_mixed_inner_source_wkb_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(fields)} all-color/all-index finite families; {len(source)} canonical complex factorial sources; {len(wkb)} both-parity selected analytic-WKB families; {len(newton)} marked complex Newton factors')
