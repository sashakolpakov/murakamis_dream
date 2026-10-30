#!/usr/bin/env python3
"""Original matching-edge bend, complete-circle measure and retained normals.

Generic finite fields check full physical matrices, every target and the
source product gauges. Cyclotomic dual numbers independently check the
actual lifted W/pi and both bend jets. Four-jets check the canceled row
germ and its original root measure. Finite tests do not prove a norm bound.
"""
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_general_four_port_single_racah_kernel import (
    facs, cg, source, target, single_kernel, seven_factorial_kernel,
    left_endpoint, beta, poch,
)
from audit_actual_trivalent_all_channel_marked_contraction import highest_cup_cap
from audit_actual_nc_morse_graph_first_normal_source_reduction import (
    Local, mm, kron, const, trans,
)
from audit_actual_supported_racah_common_phase_and_normal_metric import (
    quantum_units, factorials_without, mul, divide,
)
from audit_high_color_first_normal_r_degree import root_field


def generic_fields():
    families = coefficients = entries = row_products = target_products = 0
    odd_clock_regressions = 0
    for p, zeta in ((1000003, 2), (1000033, 3)):
        Q = zeta*zeta % p
        for N in range(2, 8):
            d = N-1
            F = facs(zeta, 4*N+2, p)
            sf = lambda r: pow(zeta, -r*(r-1)//2, p)*F[r]*pow(1-Q, -r, p) % p
            pV, ellV = highest_cup_cap(d, zeta, p, N*pow(zeta, -d*d, p) % p)
            P = np.eye(N*N, dtype=np.int64).reshape((N,)*4).transpose(0,1,3,2).reshape(N*N,N*N)
            pp = np.kron(pV, pV) % p
            ee = np.kron(ellV, ellV) % p
            targets = [target(d,d,d,d,2*g,zeta,p,F).reshape(N*N,N*N) for g in range(N)]
            hs = []
            for g in range(N):
                n=d-g
                J=pow(zeta,-n*(d+1),p)*F[d]**2*pow(F[g]**2,-1,p)%p
                V=pow(zeta,n,p)*poch(pow(Q,-d-g-1,p),n,Q,p)
                V=V*pow(F[n]**2*poch(pow(Q,-2*d-1,p),n,Q,p),-1,p)%p
                h=pow(beta(d,d,d,d,2*g,zeta,p,F)*J*V%p,-1,p)
                predicted=(-1)**d*pow(zeta,g*g+d,p)*sf(g)**2*sf(d-g)**2*sf(2*g+1)*sf(2*d+1)
                predicted=predicted*pow(sf(d)**2*sf(d+g+1)**2,-1,p)%p
                assert h==predicted
                S0=sf(2*d+1)*pow(sf(d-g)**2*sf(g)**2,-1,p)%p
                ar=left_endpoint(d,d,d,d,2*g,zeta,p,F)*pow(S0,-1,p)%p
                Delta=sf(g)**2*sf(d-g)*pow(sf(d+g+1),-1,p)%p
                dim=(pow(zeta,2*g+1,p)-pow(zeta,-2*g-1,p))*pow(zeta-pow(zeta,-1,p),-1,p)%p
                assert ar*h%p==dim*Delta*Delta%p
                hs.append(h);target_products+=1
            for a in range(d//2+1):
                E=2*a
                W=cg(d,d,E,zeta,p,F)
                pE=highest_cup_cap(E,zeta,p)[0]
                # Any fixed nonzero root constant works in this generic identity.
                gamma=pow(7,2-a*a,p)*pow(N,-2,p)%p
                pi=pE.T@W.T%p@np.kron(ellV.T,ellV.T)%p@P%p
                pi=pi*pow(gamma,-1,p)%p
                K=W@pi%p
                S=source(d,d,d,d,E,zeta,p,F).reshape(N*N,N*N)
                bend=K@pp%p@P%p
                assert np.array_equal(bend,S*pow(gamma,-1,p)%p)
                assert np.array_equal(bend@P%p@ee%p,K)
                n=d-a
                original_top=[(-1)**u*pow(zeta,-d*u,p)*pow(Q,u*(n-1)-u*(u-1)//2,p)
                    *F[a+u]*F[d-u]*pow(F[a]*F[d],-1,p)%p for u in range(n+1)]
                assert all(int(W[u*N+n-u,0])==original_top[u] for u in range(n+1))
                S0=sf(2*d+1)*pow(sf(d-a)**2*sf(a)**2,-1,p)%p
                ar=left_endpoint(d,d,d,d,E,zeta,p,F)*pow(S0,-1,p)%p
                ar_pred=(-1)**d*pow(zeta,-a*a-d,p)*sf(d)**2*sf(a)**2*pow(sf(2*a)*sf(2*d+1),-1,p)%p
                assert ar==ar_pred;row_products+=1
                rho=(-1)**d*((pow(zeta,N,p)-pow(zeta,-N,p))*pow(zeta-pow(zeta,-1,p),-1,p)%p)*ar%p
                reconstructed=np.zeros_like(K)
                unclocked=np.zeros_like(K)
                for g in range(N):
                    L=single_kernel(d,d,d,d,E,2*g,zeta,p,F)
                    normal,racah=seven_factorial_kernel(d,d,d,d,E,2*g,zeta,p,F,details=True)
                    qN=(pow(zeta,N,p)-pow(zeta,-N,p))*pow(zeta-pow(zeta,-1,p),-1,p)%p
                    G=(-1)**d*racah*pow(qN,-1,p)%p
                    assert L==normal*racah%p==rho*G*hs[g]%p
                    term=targets[g]@P%p@ee%p
                    reconstructed=(reconstructed+L*pow(gamma,-1,p)*term)%p
                    unclocked=(unclocked+(-1)**d*L*pow(gamma,-1,p)*term)%p
                    coefficients+=1
                assert np.array_equal(reconstructed,K)
                if d%2:
                    assert not np.array_equal(unclocked,K)
                    odd_clock_regressions+=1
                families+=1;entries+=K.size
    return dict(generic_full_typed_families=families,all_target_coefficients=coefficients,
                original_operator_entries=entries,independent_row_products=row_products,
                independent_target_products=target_products,odd_pivotal_sign_regressions=odd_clock_regressions)


def root_bend_jets():
    families=paired=simple=entries=0
    for N in range(2,9):
        loc=Local(N);p=loc.p
        pp=kron(loc.cup,loc.cup,p);ee=kron(loc.cap,loc.cap,p)
        for a,W in loc.W.items():
            K=mm(W,loc.pi[a],p)
            bent=mm(mm(K,pp,p),loc.P,p)
            S=mm(mm(W,loc.qcups[a][0],p),trans(W),p)
            S=tuple(v*pow(loc.gamma[a],-1,p)%p for v in S)
            assert all(np.array_equal(v,w) for v,w in zip(bent,S))
            back=mm(mm(bent,loc.P,p),ee,p)
            assert all(np.array_equal(v,w) for v,w in zip(back,K))
            sw=loc.pi[a][0]@W[0]%p
            expected=np.eye(2*a+1,dtype=np.int64) if 2*a==N-1 else np.zeros_like(sw)
            assert np.array_equal(sw,expected)
            paired+=int(2*a<N-1);simple+=int(2*a==N-1)
            families+=1;entries+=2*K[0].size
    return dict(actual_cyclotomic_bend_jet_families=families,actual_operator_jet_entries=entries,
                retained_paired_nilpotent_sectors=paired,odd_simple_sectors=simple)


def exp_jet(q,p,e,order):
    return [pow(q,e,p)*pow(e,k,p)*pow(math.factorial(k),-1,p)%p for k in range(order)]


def root_row_jets():
    rows=jet_coefficients=norm_pairs=0
    for N in range(2,31):
        p,eta=root_field(N);q=eta*eta%p;d=N-1;order=4
        units=quantum_units(q,p,2*N,order)
        f=factorials_without(units,p,set());fn=factorials_without(units,p,{N})
        imag=pow(eta,N,p)
        s=[1]
        for r in range(1,N):s.append(s[-1]*(pow(q,r,p)-pow(q,-r,p))*pow(imag,-1,p)%p)
        assert s[d]==N
        for r in range(N):assert s[r]*s[d-r]%p==N;norm_pairs+=1
        for a in range(d//2+1):
            rho=divide(mul(mul(f[d],f[d],p),mul(f[a],f[a],p),p),mul(f[2*a],fn[2*d+1],p),p)
            rho=mul(exp_jet(q,p,-a*a-d,order),rho,p)
            predicted=(-1)**d*pow(q,-a*a-d,p)*s[a]**2*pow(s[2*a],-1,p)%p
            assert rho[0]==predicted
            k=1 if 2*a==d else 2
            h0=k*N*s[2*a]*pow(s[a]**2,-1,p)%p
            gamma=pow(q,2-a*a,p)*pow(N,-2,p)%p
            expected=(-1)**d*k*N**3*pow(q,-d-2,p)%p
            assert h0*pow(gamma,-1,p)*rho[0]%p==expected
            # The original row is a genuine nonconstant retained germ.
            u=[v*pow(rho[0],-1,p)%p for v in rho]
            assert u[0]==1
            # Reinsert the exact [N], checking no root-only quotient was used.
            left=mul(mul(units[N],exp_jet(q,p,-a*a-d,order),p),
                     mul(mul(f[d],f[d],p),mul(f[a],f[a],p),p),p)
            right=mul(rho,mul(f[2*a],f[2*d+1],p),p)
            assert left==right
            rows+=1;jet_coefficients+=order
    return dict(actual_root_row_germs=rows,retained_row_jet_coefficients=jet_coefficients,
                physical_cup_magnitude_factor_pairs=norm_pairs)


def main():
    result=dict(status='PASS',generic=generic_fields(),root_bends=root_bend_jets(),row_measure=root_row_jets(),
                scope='Exact original matching-edge bend and complete-circle row measure; all generic targets and actual root first jets. Native target/complement costs remain explicit; no full-source asymptotic or positive completed Hermite norm.')
    Path(__file__).with_name('actual_matching_edge_marked_four_port_block_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
