#!/usr/bin/env python3
"""Finite source norms, interpolation tails and resonance-centered division."""

import json
from pathlib import Path

import mpmath as mp

mp.mp.dps=85
c=2j*mp.pi


def HN(N,z):
    return sum(mp.exp(z*(j-mp.mpf(N-1)/2)/N) for j in range(N))/N


def H(z):
    return 2*mp.sinh(z/2)/z if z else mp.mpf(1)


def beta(N,M):
    Q=mp.exp(c/N)
    upper=(N-1)//2
    value=mp.mpf(1)
    if N%2==0:
        value=(1+1j*M)/(1+1j)
    for j in range(1,upper+1):
        value*= (1-M*M*Q**j)/(1-Q**j)
    return value


def exact_source_norms():
    records=[]
    zs=[mp.mpf(0),mp.mpc('.3','.8'),mp.mpc('-1.5','2'),c,-c,2*c,mp.mpf('.02')+c]
    for N in range(2,19):
        worst=mp.mpf(0)
        for z in zs:
            M=mp.exp(z/(2*N))
            value=HN(N,z)
            geometric=mp.exp(-mp.mpf(N-1)*z/(2*N))*sum(mp.exp(r*z/N) for r in range(N))/N
            worst=max(worst,abs(value-geometric),abs(beta(N,M)*beta(N,1/M)-value))
            if abs(value)>mp.mpf('1e-50'):
                cocycle=N*M**(N-1)/sum(M**(2*r) for r in range(N))
                worst=max(worst,abs(cocycle*value-1))
        assert worst<mp.mpf('1e-70')
        records.append({'level':N,'centered_source_character_Weyl_norm_and_cocycle':True})
    return records


def interpolation_tail():
    records=[]
    for N in range(2,15):
        roots=[mp.exp(c*j/N) for j in range(1,N)]
        colors=[(mp.cos(2*mp.pi*j/N)+mp.sin(4*mp.pi*j/N))/2 for j in range(1,N)]
        assert max(abs(x) for x in colors)<=1
        coeff=[sum(C*(root**(-r)-root) for C,root in zip(colors,roots))/N
               for r in range(N-1)]
        assert max(abs(x) for x in coeff)<=2
        P=lambda Y:sum(a*Y**r for r,a in enumerate(coeff))
        assert max(abs(P(root)-C) for root,C in zip(roots,colors))<mp.mpf('1e-70')
        for z in [0,mp.mpc('.4','.2'),mp.mpc('-2','.3'),c,-c]:
            for order in range(4):
                value=sum(a*(mp.mpf(r)/N)**order*mp.exp(r*z/N) for r,a in enumerate(coeff))
                bound=2*(N-1)*mp.exp(max(0,mp.re(z)))
                assert abs(value)<=bound
        records.append({'level':N,'interpolation_and_all_fixed_test_jets_bound':True})
    return records


def removable_quotient():
    # A universal Laurent-polynomial stress family, not a knot claim:
    # F=S R+1, C_j=1, and the reciprocal pair of Laurent monomials
    # makes F Weyl-even at every odd and even level.
    records=[]
    for N in [3,4,8,16,32]:
        n=N-1;A=mp.mpf(2)**N;den=A+1
        low=n//2;high=n-low
        rho=lambda z:A/(2*den)*(mp.exp((mp.mpf(n)/2-low)*z/N)+mp.exp((mp.mpf(n)/2-high)*z/N))
        g=lambda z:HN(N,z)*rho(z)+1/den
        for k in [-2,-1,1,2]:
            if abs(k)>=N:continue
            zk=c*k
            derivative=(-1)**k/(2j*N*mp.sin(mp.pi*k/N))
            assert abs(mp.diff(lambda z:HN(N,z),zk)-derivative)<mp.mpf('1e-70')
            quotient=mp.diff(g,zk)/derivative
            assert abs(quotient-rho(zk))<mp.mpf('1e-68')
            assert abs(g(zk)-1/den)<mp.mpf('1e-70')
        for z in [0,mp.mpc('.7','.2'),c/2]:
            assert abs(g(z)-g(-z))<mp.mpf('1e-70')
        records.append({'level':N,'exact_fixed_resonance_removable_values':True,
                        'odd_even_full_phase_and_Weyl_marking':True})
    return records


def compact_factor_rate():
    records=[]
    zs=[mp.mpc(r,i) for r in [-2,0,2] for i in [-4,-1,0,1,4]]+[c,-c,2*c]
    for N in [8,16,32,64,128]:
        err=max(abs(HN(N,z)-H(z)) for z in zs)
        assert N*N*err<1000
        records.append({'level':N,'max_factor_error':float(err),'N_squared_error':float(N*N*err)})
    return records


def main():
    result={'actual_finite_source_norm':exact_source_norms(),
            'universal_interpolation_tail':interpolation_tail(),
            'universal_Laurent_resonance_stress_family':removable_quotient(),
            'compact_centered_factor_rate':compact_factor_rate(),
            'scope':'Exact finite source identities and analytic-division checks; no knot-profile convergence assumed.'}
    out=Path(__file__).with_name('scaled_meridian_regular_profile_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,
                      'source_norm_levels':len(result['actual_finite_source_norm']),
                      'largest_factor_grid_level':result['compact_centered_factor_rate'][-1],
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
