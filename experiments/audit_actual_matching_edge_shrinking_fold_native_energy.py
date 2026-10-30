#!/usr/bin/env python3
"""Actual all-degree source phase and shrinking real folded energy.

The theorem, rather than these finite samples, proves the unrestricted
sublinear window. Incomplete-band comparisons use the original source.
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_q_hahn_physical_generic_jet_bound import original
from audit_actual_matching_edge_magnetic_energy_profile import (
    sine_factorials, positive_polynomials, norm_from_positive,
)


def exact_phase():
    a,j,u,v,d=sp.symbols('a j u v d', integer=True)
    descendant=2*a*v+a*(a-1)+2*a*(a-j)
    gaussians=a*(j-a)+a*(u-a)+(j-a)*(v-j+a)-j*(u+v-j)
    total=d*u-2*d*a+(d+1)*a+descendant+gaussians
    assert sp.expand(total-((d-j)*u+a*(u+v+j-d))) == 0
    return 1


def original_all_degree_checks():
    counts=dict(original_physical_phase_identities=0,
                incomplete_band_original_identities=0,
                exact_root_highest_factor_complements=0)
    for N in range(3,16):
        q=mp.exp(mp.pi*1j/N);Q=q*q;d=N-1
        F=[mp.mpc(1)]
        for k in range(1,N):F.append(F[-1]*(1-Q**k))
        sf=sine_factorials(N)
        beta=lambda n,k:sf[n]/sf[k]/sf[n-k]
        for j in range((N-1)//2+1):
            for a in range(j+1):
                ratio=F[N-j+a-1]*F[N-a-1]/F[N-j-1]/F[N-1]
                converted=Q**(a*(a-j))*F[j]/F[a]/F[j-a]
                assert abs(ratio-converted)<mp.mpf('1e-75')*max(1,abs(ratio))
                counts['exact_root_highest_factor_complements']+=1
            for t in range(j,N):
                for u in range(t+1):
                    lo,hi=max(0,u-t+j),min(j,u)
                    positive=[beta(j,a)*beta(u,a)*beta(t-u,j-a)/beta(t,j)
                              for a in range(lo,hi+1)]
                    proposed=q**((d-j)*u)*mp.fsum(E*q**(a*(t+j-d)) for a,E in zip(range(lo,hi+1),positive))
                    actual=original(N,q,t,j,u,F)
                    assert abs(actual-proposed)<mp.mpf('1e-72')*max(1,abs(actual))
                    assert abs(actual)<=mp.fsum(positive)*(1+mp.mpf('1e-72'))
                    counts['original_physical_phase_identities']+=1
                    if t<d-j:
                        counts['incomplete_band_original_identities']+=1
    return counts


def endpoint_and_energy():
    rows=[];counts=dict(general_complete_center_scalars=0,
                       endpoint_physical_root_polynomials=0,
                       actual_center_half_step_bounds=0)
    v3=mp.im(mp.polylog(2,mp.exp(mp.pi*1j/3)))
    for N in (31,32,63,64,127,128):
        d=N-1;m=d//2
        # A growing distance from the maximal channel. These samples
        # do not impose a growth restriction on the proved theorem.
        offset=max(1,int(mp.log(N)))
        j=m-offset;l=d-j
        q=mp.exp(mp.pi*1j/N);Q=q*q;sf=sine_factorials(N)
        a_j=2*mp.sin(mp.pi*(2*j+1)/N)
        beta=lambda n,k:sf[n]/sf[k]/sf[n-k]
        complete=[];scalar_rates=[];Rend=None
        for t,p in positive_polynomials(N,j):
            norm=norm_from_positive(N,t,j,p,sf)
            fcenter=mp.fsum(p)/sf[j]
            R=fcenter*(sf[t]/sf[t-j])/beta(2*j,j)
            A=a_j*a_j/N*sf[2*j]**2/sf[j]**4*sf[t-j]/sf[t-l]
            sigma=N*sf[t-j]*sf[t+j-d]/(sf[t]**2*a_j*a_j)
            assert abs(fcenter*fcenter/sigma/(A*R*R)-1)<mp.mpf('1e-75')
            counts['general_complete_center_scalars']+=1
            complete.append(norm);scalar_rates.append(abs(mp.log(A)/N))
            if t==d:
                Rend=R;pend=p
        u=d//2;v=d-u
        P=mp.fsum(beta(j,a)*beta(u,a)*beta(v,j-a)*q**(j*a) for a in range(j+1))
        physical=q**((d-j)*u)*P
        F=[mp.mpc(1)]
        for k in range(1,N):F.append(F[-1]*(1-Q**k))
        actual=original(N,q,d,j,u,F)
        assert abs(actual-physical)<mp.mpf('1e-70')*max(1,abs(actual))
        counts['endpoint_physical_root_polynomials']+=1
        fcenter=mp.fsum(pend)/sf[j]
        assert mp.cos(mp.pi/(2*N))**j<=abs(actual)/fcenter*(1+mp.mpf('1e-70'))
        assert abs(actual)/fcenter<=1+mp.mpf('1e-70')
        counts['actual_center_half_step_bounds']+=1
        assert abs(fcenter/(Rend*sf[2*j]/sf[j]**3)-1)<mp.mpf('1e-75')
        rows.append(dict(N=N,j=j,fold_distance=d-2*j,
                         endpoint_determinant_rate=float(2*mp.log(Rend)/N),
                         max_complete_energy_rate=float(mp.log(max(complete))/N),
                         max_absolute_center_scalar_rate=float(max(scalar_rates)),
                         limiting_rate=float(5*v3/mp.pi)))
    return dict(counts=counts, rows=rows)


def main():
    mp.mp.dps=100
    result=dict(status='PASS',formal_phase_identities=exact_phase(),
                physical_source=original_all_degree_checks(),
                shrinking_examples=endpoint_and_energy(),
                scope='Actual all-j physical source including incomplete band; real native shrinking-fold theorem. No enlarged complex-normal corridor or whole-network estimate.')
    Path(__file__).with_name('actual_matching_edge_shrinking_fold_native_energy_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
