#!/usr/bin/env python3
"""Original overclock sectors, complete q-Pascal fusion and pivotal sum.

The matrices are constructed from the original four-index crossing,
independently of the proposed sector formula. The charged comparison
also retains every original external scalar line.
"""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_kashaev_crossing import original
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import setup,graph_blocks,charged_data
from audit_actual_general_flow_fusion import normalized_graph
from audit_actual_forced_source_fusion import reduce_source,coefficient


def root_data(N):
    p = next(4*N*j+1 for j in range(1,1000) if sp.isprime(4*N*j+1))
    eta = pow(int(sp.primitive_root(p)),(p-1)//(4*N),p)
    return p,pow(eta,2,p),pow(eta,4,p)


def field_source_case(N):
    p,q,Q = root_data(N)
    raw,_,F = original(N,p,Q)
    flip = np.zeros_like(raw)
    for a,b in itertools.product(range(N),repeat=2):
        flip[b*N+a,a*N+b] = 1
    B = flip@raw.T % p
    T = B[:N,:N]
    Qinv = pow(Q,-1,p)
    count = 0
    total = 0
    for H,J in itertools.product(range(N),repeat=2):
        ih,ij = (0 if H==N-1 else H+1),(0 if J==N-1 else J+1)
        actual = Qinv*int(T[ih,1])*int(T[ij,ih])*int(T[0,ij]) % p
        expected = (0 if H>J else
                    pow(-1,H,p)*pow(Q,1+H*(H+1)//2,p)*F[J]
                    *pow(F[H]*F[J-H] % p,-1,p) % p)
        assert actual == expected,(N,H,J,actual,expected)
        total = (total+actual) % p
        count += 1
    for J in range(N):
        fused = sum(pow(-1,H,p)*pow(Q,1+H*(H+1)//2,p)*F[J]
                    *pow(F[H]*F[J-H] % p,-1,p) for H in range(J+1)) % p
        assert fused == Q*F[J] % p
    full = ((B@B) % p)@B % p
    closed = sum(int(full[A,(A+1)%N]) for A in range(N))*Qinv % p
    assert closed == total == Q*sum(F) % p
    # Independent actual spectral-jet closing formula, every root level.
    phi = 0
    for k in range(N//2):
        a = 2*k+1
        c = (pow(q,a,p)+pow(q,-a,p)) % p
        aa = (pow(q,a,p)-pow(q,-a,p)) % p
        nu = pow(-1,k,p)*pow(q,k*(k+1),p) % p
        derivative = -3*pow(nu,3,p)*(N-a)*pow(2*aa % p,-1,p) % p
        phi = (phi-c*pow(nu,3,p)-(c*c-4)*derivative) % p
    if N%2:
        k=(N-1)//2
        nu=pow(-1,k,p)*pow(q,k*(k+1),p) % p
        phi=(phi+pow(nu,3,p)) % p
    spectral = pow(-q,3,p)*phi % p
    assert spectral == total,(N,spectral,total)
    return dict(N=N,all_actual_overclock_sectors=count,
                first_coherent_clock_sums=N,
                original_full_matrix_cut_and_spectral_jet_both_match=True,
                normalized_period_mod_p=int(total))


def charged_source_case(N):
    H = HardyNetwork(N,1)
    p,d = H.p,N-1
    S = setup(H,2,[1,1,1])
    common = None
    sectors = 0
    for a,b in itertools.product(range(N),repeat=2):
        hs=(0,a,b)
        G=graph_blocks(H,S,hs)
        normal,E,V=normalized_graph(H,G)
        scalar,edges,charges,_=reduce_source(H,E,{v:d for v in V})
        _,weight,_,_=charged_data(H,S,hs)
        reduced = weight*normal*scalar*(coefficient(H,edges,charges) if scalar else 0) % p
        target = (0 if a>b else pow(-1,a,p)*pow(H.Q,1+a*(a+1)//2,p)
                  *H.fac[b]*pow(H.fac[a]*H.fac[b-a] % p,-1,p) % p)
        if common is None:
            common=reduced*pow(target,-1,p) % p
            # N times a retained root phase; the original exterior 1/N remains.
            assert pow(common*pow(N,-1,p) % p,8*N,p)==1
        assert reduced == common*target % p,(N,a,b,reduced,target,common)
        sectors += 1
    external=H.dimension*pow(H.twist,-3,p) % p
    assert external
    return dict(N=N,fully_reduced_original_charged_sectors=sectors,
                exact_common_original_source_factor_mod_p=int(common),
                original_kappa_pivots_and_external_line_retained=True)


def complex_rates():
    rows=[]
    v3=mp.im(mp.polylog(2,mp.exp(1j*mp.pi/3)))
    for N in (36,72,144):
        q=mp.exp(1j*mp.pi/N);Q=q*q
        F=[mp.mpc(1)]
        for j in range(1,N):
            F.append(F[-1]*(1-Q**j))
        H,J=N//3,2*N//3
        rate=mp.log(abs(F[J]/(F[H]*F[J-H])))/N
        residual=mp.log(abs(F[5*N//6]))/N
        assert abs(rate-v3/mp.pi)*N/mp.log(N)<10
        assert abs(residual-v3/(2*mp.pi))*N/mp.log(N)<10
        value=Q*sum(F)
        assert abs(value)<=3*N*N
        rows.append(dict(N=N,macroscopic_fixed_clock_rate=float(rate),
                         fixed_clock_limit=float(v3/mp.pi),
                         first_fused_current_rate=float(residual),
                         first_fused_limit=float(v3/(2*mp.pi)),
                         full_original_period_modulus=float(abs(value)),
                         exact_proved_polynomial_bound=3*N*N))
    return rows


def main():
    fields=[field_source_case(N) for N in range(2,13)]
    charged=[charged_source_case(N) for N in range(2,8)]
    with mp.workdps(90):
        rates=complex_rates()
    result=dict(status='PASS',original_cyclic_source=fields,
                complete_charged_source_after_all_full_fusions=charged,
                exponential_current_diagnostics=rates,
                scope='Exact proved three-crossing original source and its macroscopic clock current. No arbitrary-run, broad hyperbolic class or new volume theorem.')
    target=Path(__file__).with_name('actual_overclock_sector_obstruction_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',original_levels=len(fields),
                         actual_clock_sectors=sum(r['all_actual_overclock_sectors'] for r in fields),
                         fully_reduced_charged_sectors=sum(r['fully_reduced_original_charged_sectors'] for r in charged),
                         rate_checks=len(rates)),indent=2))


if __name__=='__main__':
    main()
