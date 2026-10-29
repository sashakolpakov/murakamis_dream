#!/usr/bin/env python3
"""Literal finite Sears source transform, exact phases and all-r Ward."""

import json
from pathlib import Path

import mpmath as mp


def poch(a, q, n):
    return mp.fprod(1-a*q**j for j in range(n))


def sears_case(n):
    mp.mp.dps = 90
    Q = mp.mpc('.61','.09')
    a,b,c,d = mp.mpc('.27','.11'),mp.mpc('-.38','.03'),mp.mpc('.49','-.12'),mp.mpc('-.52','.07')
    z = c*d*Q**n/(a*b)
    lhs = mp.fsum(poch(Q**(-n),Q,k)*poch(a,Q,k)*poch(b,Q,k)*z**k
                  /(poch(Q,Q,k)*poch(c,Q,k)*poch(d,Q,k)) for k in range(n+1))
    rhs = poch(c/a,Q,n)/poch(c,Q,n)*mp.fsum(
        poch(Q**(-n),Q,j)*poch(a,Q,j)*poch(d/b,Q,j)*Q**j
        /(poch(Q,Q,j)*poch(d,Q,j)*poch(a*Q**(1-n)/c,Q,j)) for j in range(n+1))
    assert abs(lhs-rhs) < mp.mpf('1e-70')*max(1,abs(lhs),abs(rhs))
    return {'n':n,'independent_generic_finite_identity':True}


def root_case(N, asymptotic=False):
    mp.mp.dps = max(100,N+35)
    q = mp.exp(mp.j*mp.pi/N); Q=q*q; delta=mp.pi/N; M=(N-1)//2
    F=[mp.mpc(1)]
    for j in range(1,N): F.append(F[-1]*(1-Q**j))
    A=[]; U=[]
    for r in range(M+1):
        ar=mp.fsum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r]) for v in range(r,M+1))
        diagonal=Q**(-r*r)*F[2*r]/F[r]**3
        A.append(ar); U.append(ar/diagonal)
    A += [mp.mpc(0),mp.mpc(0)]
    high_count=0; maximum_identity=mp.mpf(0); maximum_ward=mp.mpf(0)
    for r in range(M+1):
        n=M-r; Y=Q**r
        if N%2:
            terms=[poch(Q**(2*r+1),Q*Q,j)*poch(-1,Q,j)*Q**j
                   /(poch(Q**(2*r+2),Q*Q,j)*F[j]) for j in range(n+1)]
            pref=poch(q,Q,n)/poch(Q**(r+1),Q,n)
            h=[abs(z) for z in terms]
            assert max(abs(terms[j]-(mp.j**j)*h[j]) for j in range(n+1)) < mp.mpf('1e-65')*max(1,*h)
            B=mp.fprod(mp.cos(k*delta)*mp.cos((k+1)*delta)/mp.cos((k+mp.mpf('.5'))*delta)**2 for k in range(n))
            gs=[mp.fprod(mp.sin((2*k-1)*delta)/mp.sin(2*k*delta)
                        *mp.sin((n-k+1)*delta)/mp.cos((n-k)*delta) for k in range(1,l+1)) for l in range(n+1)]
            reverse=q**(n*n)*B*mp.fsum((-mp.j)**l*gs[l] for l in range(n+1))
            assert abs(reverse-pref*mp.fsum(terms)) < mp.mpf('1e-65')*max(1,abs(reverse))
        else:
            terms=[poch(-Q**(r+1),Q,j)*poch(-q*Q**r,Q,j)*poch(q,Q,j)*Q**j
                   /(F[j]*poch(Q**(r+1),Q,j)*poch(q**3*Q**r,Q,j)) for j in range(n+1)]
            pref=poch(-q,Q,n)/poch(Q**(r+1),Q,n)
            h=[abs(z) for z in terms]
            assert max(abs(terms[j]-(-mp.exp(mp.j*delta/2))**j*h[j]) for j in range(n+1)) < mp.mpf('1e-65')*max(1,*h)
        transformed=pref*mp.fsum(terms)
        error=abs(transformed-U[r])/max(1,abs(U[r]))
        assert error < mp.mpf('1e-60')
        maximum_identity=max(maximum_identity,error)
        if 4*r>=N:
            high_count+=1
            assert mp.mpf(1)/3<=abs(U[r])<=2*N
            if N%2:
                assert all(h[j+1]>=h[j]*(1-mp.mpf('1e-65')) for j in range(n))
                assert all(gs[l]<=mp.tan(n*delta)**l*(1+mp.mpf('1e-60')) for l in range(n+1))
            else:
                assert all(h[j+1]<=h[j]*(1+mp.mpf('1e-65')) for j in range(n))
        coefficients=(Q*Y**2*(1-Q**2*Y),Y*(2*Q**3*Y**2+Q+1),-Q*(Q*Y+1)*(Q*Y**2-1))
        ward=coefficients[0]*A[r+2]+coefficients[1]*A[r+1]+coefficients[2]*A[r]
        scale=max(1,*(abs(c*a) for c,a in zip(coefficients,(A[r+2],A[r+1],A[r]))))
        assert abs(ward)/scale < mp.mpf('1e-60')
        maximum_ward=max(maximum_ward,abs(ward)/scale)
    samples=[]
    if asymptotic:
        for position in (mp.mpf('.28'),mp.mpf('.333'),mp.mpf('.4')):
            r=int(position*N);n=M-r;a=r*delta;beta=n*delta
            phase=q**(n*n) if N%2 else q**(n*(n+mp.mpf('.5')))
            prediction=(1+mp.j*mp.tan(beta))**(-mp.mpf('.5')) if N%2 else mp.sqrt(mp.sin(a))
            scaled_error=N*abs(U[r]/phase-prediction)
            assert scaled_error < 12
            samples.append({'r':r,'N_times_complex_amplitude_error':float(scaled_error)})
    return {'N':N,'all_original_inner_packets':M+1,'all_r_finite_transform_and_phase':True,
            'all_r_source_Ward_and_endpoints':True,'uniform_nonzero_geometric_range_packets':high_count,
            'maximum_relative_identity_error':float(maximum_identity),
            'maximum_relative_Ward_error':float(maximum_ward),'amplitude_samples':samples}


def amplitude_case(N):
    mp.mp.dps=max(100,N//2+50)
    q=mp.exp(mp.j*mp.pi/N);Q=q*q;M=(N-1)//2;F=[mp.mpc(1)]
    for j in range(1,N):F.append(F[-1]*(1-Q**j))
    samples=[]
    for position in (mp.mpf('.28'),mp.mpf('.333'),mp.mpf('.4')):
        r=int(position*N);n=M-r;u=mp.pi*r/N;beta=mp.pi*n/N
        A=mp.fsum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r]) for v in range(r,M+1))
        U=A/(Q**(-r*r)*F[2*r]/F[r]**3)
        phase=q**(n*n) if N%2 else q**(n*(n+mp.mpf('.5')))
        prediction=(1+mp.j*mp.tan(beta))**(-mp.mpf('.5')) if N%2 else mp.sqrt(mp.sin(u))
        scaled_error=N*abs(U/phase-prediction)
        assert scaled_error<12
        samples.append({'r':r,'N_times_complex_amplitude_error':float(scaled_error)})
    return {'N':N,'samples':samples,'literal_inner_sum_used':True}


def central_packet_case(N):
    mp.mp.dps=120
    q=mp.exp(mp.j*mp.pi/N);Q=q*q;d=N-1;M=d//2
    F=[mp.mpc(1)]
    for j in range(1,N):F.append(F[-1]*(1-Q**j))
    kappa=q**(mp.mpf(d*d)/2)
    T=mp.mpf(14);eta=mp.acosh(T/2);u=mp.atan(mp.sqrt(T+2)/2)
    lob=lambda a:mp.im(mp.polylog(2,mp.exp(2*mp.j*a)))/2
    J=(-lob(2*u)+6*lob(u))/mp.pi+mp.quad(
        lambda v:mp.log(T+2*mp.cos(v)),[0,2*u])/(2*mp.pi)
    jp=mp.atan(mp.sinh(eta/2))/mp.pi
    jpp=1/(2*mp.pi*mp.cosh(eta/2))
    amp=mp.exp(-mp.j*mp.pi*d/4+mp.j*u/2)/(2*((T+2)*(T+6))**mp.mpf('.25'))
    A={r:mp.fsum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r]) for v in range(r,M+1))
       for r in range((N+3)//4,M+1)}
    rows=[]
    for tau in (-1,0,1):
        w=-mp.exp(eta+mp.j*tau/mp.sqrt(N));z=w+1/w
        P=mp.mpc(1);packet=mp.mpc(0)
        for r in range(M+1):
            if r in A:
                packet+=(-1)**r*Q**(mp.mpf(r*(r+1))/2)*P*A[r]/F[r]**3
            P*=1-q*Q**r*z+Q**(2*r+1)
        packet*=N*N/kappa
        predicted=amp*mp.exp(N*J+mp.j*mp.sqrt(N)*jp*tau-jpp*tau*tau/2)
        ratio=packet/predicted
        assert mp.sqrt(N)*abs(ratio-1)<8
        if tau==0:assert N*abs(ratio-1)<8
        rows.append({'tau':tau,'literal_high_packet_over_predicted':
                     [float(mp.re(ratio)),float(mp.im(ratio))]})
    return {'N':N,'full_kappa_and_both_parity_phase':True,'central_window':rows}


if __name__=='__main__':
    generic=[sears_case(n) for n in range(1,9)]
    root=[root_case(N) for N in range(2,41)]
    amplitude=[amplitude_case(N) for N in (63,64,127,128,255,256)]
    central=[central_packet_case(N) for N in (63,64,127,128)]
    result={'status':'PASS','generic_finite_identity':generic,'complete_original_root_packets':root,
            'complex_amplitude_profiles':amplitude,'literal_central_gaussian_packets':central,
            'scope':'Exact all-r transform/Ward; nonzero tame packet only r>=ceil(N/4). Full low-r upper and outer source asymptotic unproved.'}
    Path(__file__).with_name('actual_pretzel_coherent_inner_gauss_elimination_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(generic)} generic finite transforms; {len(root)} all-r original root families; {len(amplitude)} coherent complex-amplitude profiles; {len(central)} literal central Gaussian packets')
