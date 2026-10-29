#!/usr/bin/env python3
"""Exact original prefix and high-precision shrinking-arc jet diagnostic.

Growth data are numerical diagnostics, NOT an all-N exponent theorem.
All arc energies are complete finite-polynomial integrals, not Taylor truncations.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_terminal_bridge_operator_reduction import terminal_matrix


def exact_source_case(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    d,Q,x=N-1,q*q % p,int(K[0,0])
    kappa=int(Rp[0,0])
    fac=[1]
    for j in range(1,N):fac.append(fac[-1]*(1-pow(Q,j,p)) % p)
    ids=[j*N+d-j for j in range(N)]
    R=Rp[np.ix_(ids,ids)]
    cup=np.zeros(N**3,dtype=np.int64)
    for j in range(N):cup[(j*N+d-j)*N]=N*pow(x,j-d,p) % p
    physical=np.kron(np.eye(N,dtype=np.int64),Rm)@cup % p
    highest=[physical[(j*N+d-j)*N]for j in range(N)]
    expected=np.zeros(N,dtype=np.int64);expected[d]=N*pow(kappa,-1,p) % p
    assert np.array_equal(np.array(highest),expected)
    v=R@expected % p
    explicit=np.array([N*N*pow(x,j-d,p)*pow(fac[d-j],-1,p) % p for j in range(N)])
    assert np.array_equal(v,explicit)
    _,_,T=terminal_matrix(N,1,p,q,E,F,K,Rp)
    coefficients=T@v % p
    row=np.array([pow(x*Q,j-d,p)*pow(N,-1,p) % p for j in range(N)])
    assert np.array_equal(np.sum(T,axis=0) % p,row)
    raw=sum(map(int,coefficients)) % p
    bar_endpoint=sum(pow(-1,j,p)*pow(Q,-j*(j+1)//2,p)*fac[j]for j in range(N)) % p
    assert raw==bar_endpoint
    # Independent FULL crossed-diagonal Green packet, all kappa factors retained.
    green=[1]
    for t in range(1,N):green.append(((1-pow(Q,t,p))**2*green[-1]+pow(Q,t,p)) % p)
    closed=(np.diag([pow(x,n,p)for n in range(N)])@R
            @np.diag(green[::-1])@R)*pow(N,-1,p) % p
    assert np.array_equal(T,closed)
    assert sum(n*int(coefficients[n])for n in range(N)) % p == sum(
        n*int((closed@v % p)[n])for n in range(N)) % p
    # Exact ALL-INPUT normal-current split; no period or fitted jet is used.
    J=np.diag(np.arange(N,dtype=np.int64))
    xr=np.array([pow(x,j,p)for j in range(N)],dtype=np.int64)
    assert np.array_equal(R,R.T)
    assert np.array_equal(xr@R % p,kappa*xr % p)
    normal=xr@(J@R-R@J) % p
    normal=normal@np.diag(green[::-1]) % p
    normal=normal@R % p
    normal=normal*pow(N,-1,p) % p
    regular=kappa*(xr@J) % p
    regular=regular@np.diag(green[::-1]) % p
    regular=regular@R % p
    regular=regular*pow(N,-1,p) % p
    literal=np.arange(N,dtype=np.int64)@T % p
    assert np.array_equal(literal,(regular+normal) % p)
    assert np.any(normal)
    return {'N':N,'literal_prefix_R12_R23_inverse_on_original_cup':True,
            'exact_full_terminal_coefficients_and_raw_closed_source':True,
            'all_input_recorded_normal_current_with_original_neighbors':True,
            'all_original_kappa_and_cap_cup_normalizations':True}


def matvec(A,v):
    return [mp.fsum(a*b for a,b in zip(row,v))for row in A]


def derivative_constant(d):
    r=(d-1)//2
    b=mp.binomial(2*r,r)/mp.mpf(4)**r
    return ((2*r+1)*(2*r+3)*b)**2/3


def cayley_coefficients(coeff):
    N,d=len(coeff),len(coeff)-1
    old=[1]*N
    current=[2*n-d for n in range(N)]
    result=[mp.fsum(coeff)]
    if d:result.append(mp.j*mp.fsum(current[n]*coeff[n]for n in range(N)))
    for r in range(1,d):
        numerators=[(2*n-d)*current[n]-(d-r+1)*old[n]for n in range(N)]
        assert all(z % (r+1)==0 for z in numerators)
        following=[z//(r+1)for z in numerators]
        result.append(mp.j**(r+1)*mp.fsum(following[n]*coeff[n]for n in range(N)))
        old,current=current,following
    return result


def complete_arc_energy(cayley,a):
    scaled=[a**r*cayley[r]for r in range(len(cayley))]
    diagonal=mp.fsum(abs(z)**2/(2*r+1)for r,z in enumerate(scaled))
    mixed=mp.fsum(2*mp.re(scaled[r]*mp.conj(scaled[s]))/(r+s+1)
                 for r in range(len(scaled))for s in range(r+1,len(scaled))if(r+s)%2==0)
    energy=diagonal+mixed
    assert energy>0
    return energy


def high_precision_case(N,digits=None):
    mp.mp.dps=digits or N+100
    q=mp.exp(mp.j*mp.pi/N);Q=q*q;x=-1/q;d=N-1
    kappa=q**(mp.mpf(d*d)/2)
    fac=[mp.mpc(1)]
    for j in range(1,N):fac.append(fac[-1]*(1-Q**j))
    R=[[mp.mpc(0)for _ in range(N)]for _ in range(N)]
    for a in range(N):
        b=d-a
        for k in range(a+1):
            R[b+k][a]=(kappa*x**(-d+k)*Q**(b*(a-k))*fac[b+k]*fac[a]
                       /(fac[k]*fac[b]*fac[a-k]))
    green=[mp.mpc(1)]
    for t in range(1,N):green.append((1-Q**t)**2*green[-1]+Q**t)
    v=[N*N*x**(j-d)/fac[d-j]for j in range(N)]
    transformed=matvec(R,v)
    transformed=[green[d-j]*transformed[j]for j in range(N)]
    transformed=matvec(R,transformed)
    coeff=[x**j*transformed[j]/N for j in range(N)]
    jets=[mp.fsum(mp.ff(j,r)*coeff[j]for j in range(N))for r in range(4)]
    D=2*jets[1]-d*jets[0]
    endpoint=mp.fsum(fac)
    error=abs(jets[0]/mp.conj(endpoint)-1)
    assert error<mp.mpf('1e-45')
    assert abs(jets[0])<=3*N*N*(1+mp.mpf('1e-40'))
    cayley=cayley_coefficients(coeff)
    assert abs(cayley[1]/(mp.j*D)-1)<mp.mpf('1e-45')
    arcs=[];energies={}
    for power in (1,2):
        a=mp.mpf(N)**(-power)
        energy=complete_arc_energy(cayley,a)
        lower=a*a*abs(D)**2/derivative_constant(d)
        assert energy>=lower*(1-mp.mpf('1e-35'))
        jet_reference=a*a*abs(D)**2/3
        arcs.append({'power_A':power,'log_complete_weighted_arc_energy_over_N':float(mp.log(energy)/N),
                     'unweighted_log_energy_lower_over_N':float((mp.log(energy)-d*mp.log1p(a*a))/N),
                     'exact_first_jet_Legendre_lower_log_over_N':float(mp.log(lower)/N),
                     'complete_energy_over_linear_jet_energy':float(energy/jet_reference)})
        energies[power]=energy
    row={'N':N,'decimal_digits':mp.mp.dps,
         'log_raw_closed_period_over_N':float(mp.log(abs(jets[0]))/N),
         'log_first_phase_derivative_over_N':float(mp.log(abs(jets[1]))/N),
         'log_centered_first_jet_over_N':float(mp.log(abs(D))/N),
         'raw_closed_source_relative_error':mp.nstr(error,8),
         'arc_data':arcs,'analytic_positive_jet_exponent_proved':False}
    return row,D,energies


if __name__=='__main__':
    exact=[exact_source_case(N)for N in range(2,11)]
    rows=[];values={}
    for N in (8,16,24,32,48,64,96,128,192,256):
        row,jet,energies=high_precision_case(N)
        rows.append(row);values[N]=(jet,energies)
    refined,jet,energies=high_precision_case(128,360)
    jet_error=abs(jet/values[128][0]-1)
    arc_error=max(abs(energies[A]/values[128][1][A]-1)for A in (1,2))
    assert jet_error<mp.mpf('1e-100') and arc_error<mp.mpf('1e-100')
    output={'status':'PASS','exact_original_prefix_and_closed_source':exact,
            'full_finite_jet_and_complete_Cayley_arc_diagnostics':rows,
            'N128_first_jet_precision_refinement_error':mp.nstr(jet_error,8),
            'N128_full_arc_energy_precision_refinement_error':mp.nstr(arc_error,8),
            'scope':'Source and finite arc identities proved; all-N exponential first-jet growth remains UNPROVED.'}
    Path(__file__).with_name('actual_terminal_shrinking_arc_jet_diagnostic_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print('PASS 9 exact original sources; 10 full high-precision jet/arc profiles through N256; precision refinement; exponent diagnostic only')
