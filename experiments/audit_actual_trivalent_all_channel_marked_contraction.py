#!/usr/bin/env python3
"""Exact ordered ordinary duals and original marked two-vertex contractions.

Finite checks supplement the finite Vandermonde and regular-trace proof.
No full-graph norm or geometric claim is made here.
"""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_trivalent_complete_circle_vertex_kernel import (
    data, vertex_formula, sources, axis_apply, matrix_power,
)
from audit_actual_trivalent_full_cd_normalization_and_magnetic_growth import (
    ordinary, physical_columns, canonical_three_j,
)


def fact_table(q, n, p):
    Q = q*q % p
    f = [1]
    for k in range(1, n+1):
        f.append(f[-1]*(1-pow(Q, k, p)) % p)
    return f


def highest_cup_cap(L, q, p, scale=1):
    Q = q*q % p
    f = fact_table(q, L, p)
    values = [scale*(-1)**r*pow(q, r*(L-r-1), p)*f[r]*f[L-r]*pow(f[L], -1, p) % p
              for r in range(L+1)]
    cup = np.zeros((L+1, L+1), dtype=np.int64)
    cap = cup.copy()
    for r, value in enumerate(values):
        cup[r, L-r] = value
        cap[L-r, r] = pow(value, -1, p)
    assert np.array_equal(cup@cap % p, np.eye(L+1, dtype=np.int64))
    return cup, cap


def cup_cap(j, q, p):
    return highest_cup_cap(2*j,q,p)


def dual_three(value, caps, p):
    result = value.copy()
    for axis, cap in enumerate(caps):
        result = axis_apply(cap, result, axis, p)
    return result.transpose(2, 1, 0)


def generic_theta():
    p, q = 1000003, 2
    Q = q*q % p
    f = fact_table(q, 20, p)
    count = 0
    for a,b,c in itertools.product(range(5), repeat=3):
        J, r, r1, r2 = a+b+c, b+c-a, a+b-c, a+c-b
        if min(r,r1,r2) < 0:
            continue
        modules = [ordinary(j,q,p) for j in (a,b,c)]
        theta = canonical_three_j((a,b,c), modules, q, p)
        reverse = canonical_three_j((c,b,a), list(reversed(modules)), q, p)
        caps = [cup_cap(j,q,p)[1] for j in (c,b,a)]
        dual = dual_three(reverse,caps,p)
        value = int(np.sum(theta*dual) % p)
        expected = (-1)**r1*pow(q,2*c-r1*(r-1),p)*f[2*b]*f[r2]*f[J+1]
        expected *= pow((1-Q)*f[r]*f[2*a]*f[r1]*f[2*c],-1,p)
        assert value == expected % p
        top = theta[:,:,0]
        cut = int(np.sum(top*dual[:,:,0]) % p)*pow(q,2*c,p) % p
        expected_cut = (-1)**r1*pow(q,4*c-r1*(r-1),p)*f[2*b]*f[r2]*f[J+1]
        expected_cut *= pow(f[r]*f[2*a]*f[r1]*f[2*c+1],-1,p)
        assert cut == expected_cut % p
        count += 1
    return {'generic_ordered_theta_pairs': count, 'exact_finite_Vandermonde_normalization': True}


def generic_physical_lifts():
    p,q = 1000003,2
    Q = q*q % p
    count = 0
    for N in range(2,7):
        d = N-1
        f = fact_table(q,2*N,p)
        E = np.diag([pow(q,-d-1,p)*(1-pow(Q,d+1-r,p)) % p for r in range(1,N)],1)
        F = np.diag([(1-pow(Q,r,p)) % p for r in range(1,N)],-1)
        K = np.diag([pow(q,d-2*r,p) for r in range(N)])
        Et,Ft,Kt = coproduct(E,F,K,2,N,p)
        for j in range(d//2+1):
            t = d-j
            W = np.zeros((N*N,2*j+1),dtype=np.int64)
            poch = 1
            for a in range(t+1):
                W[a*N+t-a,0] = (-1)**a*pow(q,-d*a,p)*pow(Q,a*(t-1)-a*(a-1)//2,p)*poch*f[d-a]*pow(f[d],-1,p) % p
                poch = poch*(1-pow(Q,j+1+a,p)) % p
            for r in range(1,2*j+1):
                W[:,r] = Ft@W[:,r-1] % p*pow(1-pow(Q,r,p),-1,p) % p
            for physical,ordinary_matrix in zip((Et,Ft,Kt),ordinary(j,q,p)):
                assert np.array_equal(physical@W % p,W@ordinary_matrix % p)
            count += 1
    return {'regular_generic_physical_Clebsch_lifts':count,'all_E_F_K_covariances':True}


def level(N):
    p, eta, q, *_ = balanced_data(N)
    d, M, Q = N-1, (N-1)//2, q*q % p
    x = pow(q,d,p)
    Ws, fac, _ = physical_columns(N,q,p)
    bars, _, _ = physical_columns(N,pow(q,-1,p),p)
    imag = pow(eta,N,p)
    sine = [pow(imag,k,p)*pow(q,-k*(k+1)//2,p)*fac[k] % p for k in range(N)]
    P = np.eye(N*N,dtype=np.int64).reshape((N,)*4).transpose(1,0,2,3).reshape(N*N,N*N)
    cap = np.array([[pow(x,a,p)*pow(N,-1,p) % p if a+b==d else 0
                     for b in range(N)] for a in range(N)],dtype=np.int64)
    labels, columns, bar_columns, offsets, metrics, h0s = [], [], [], {}, {}, {}
    dual_checks = 0
    for j in range(M+1):
        offsets[j] = len(labels)
        G = [sine[2*j]*pow(sine[r]*sine[2*j-r],-1,p) % p for r in range(2*j+1)]
        metrics[j] = G
        h0s[j] = N if 2*j==d else 2*N*sine[2*j]*pow(sine[j]**2,-1,p) % p
        pi = np.array([pow(int(g),-1,p) for g in G])[:,None]*bars[j].T % p@P % p
        ordinary_cup, _ = cup_cap(j,q,p)
        dual = ordinary_cup.T@Ws[j].T % p@np.kron(cap.T,cap.T) % p@P % p
        gamma = pow(q,2-j*j,p)*pow(N,-2,p) % p
        assert np.array_equal(dual,gamma*pi % p)
        for r in range(2*j+1):
            labels.append((d-j+r,j))
            columns.append(Ws[j][:,r])
            bar_columns.append(bars[j][:,r])
        dual_checks += 1
    U,V,Vm = vertex_formula(N,x,p,labels,np.column_stack(bar_columns))
    _,Vbar,Vmbar = vertex_formula(N,pow(x,-1,p),p,labels,np.column_stack(columns))
    triples, forbidden, direct_values = 0,0,[]
    for a,b,c in itertools.product(range(M+1),repeat=3):
        js = (a,b,c)
        ids = [list(range(offsets[j],offsets[j]+2*j+1)) for j in js]
        block = U[np.ix_(*ids)]
        marked = Vmbar[np.ix_(*ids)]
        balanced = block.copy()
        for k,j in enumerate(js):
            shape = [1,1,1]
            shape[k] = 2*j+1
            balanced = balanced*np.array([pow(int(g),-1,p) for g in metrics[j]]).reshape(shape) % p
        observed = pow(N,-7,p)*int(np.sum(balanced*marked) % p) % p
        observed = observed*int(np.prod([h0s[j] for j in js],dtype=object)) % p
        J = a+b+c
        if J<d:
            assert not np.any(block) and observed==0
            forbidden += 1
            continue
        r,r1,r2,delta = b+c-a,a+b-c,a+c-b,J-d
        A = int(block[2*a,r,0])*pow(N,-3,p) % p
        phase = (-1)**(N+J)*pow(q,2*a*a-a*b-a*c+b*c-J-3,p) % p
        Aabs = A*pow(phase,-1,p) % p
        weight = N*sine[delta]*sine[r]*sine[r1]*sine[r2]
        weight *= int(np.prod([h0s[j] for j in js],dtype=object))
        weight *= pow(sine[2*a]*sine[2*b]*sine[2*c],-1,p)
        assert observed == weight*Aabs*Aabs % p
        theta = canonical_three_j(js,[ordinary(j,q,p) for j in js],q,p)
        source_scalar = N**3*A*pow(int(metrics[b][r]),-1,p) % p
        assert np.array_equal(balanced,source_scalar*theta % p)
        marked_functional = int(np.sum(theta*marked) % p)
        expected_functional = N**5*sine[delta]*sine[r2]*pow(sine[2*a]*sine[2*c],-1,p)
        expected_functional *= Aabs*pow(phase,-1,p)
        assert marked_functional == expected_functional % p
        # The ordinary white uses the reversed-label black, not a same-label
        # Hermitian adjoint. Check the full ordered pivotal identity.
        reverse_ids = [list(range(offsets[j],offsets[j]+2*j+1)) for j in (c,b,a)]
        reverse = U[np.ix_(*reverse_ids)].copy()
        for k,j in enumerate((c,b,a)):
            shape = [1,1,1]
            shape[k] = 2*j+1
            reverse = reverse*np.array([pow(int(g),-1,p) for g in metrics[j]]).reshape(shape) % p
        ordinary_white = pow(N,-6,p)*Vbar[np.ix_(*ids)] % p
        rightdual = dual_three(reverse,[cup_cap(j,q,p)[1] for j in (c,b,a)],p)
        gammas = pow(q,6-a*a-b*b-c*c,p)*pow(N,-6,p) % p
        assert np.array_equal(ordinary_white,gammas*rightdual % p)
        assert int(np.sum(ordinary_white*balanced) % p)==0
        if N<=7 and ((a,b,c)==(M,M,M) or (a,b,c)==(max(0,d-2*M),M,M)):
            # Independent ungrouped source with the genuine full-normal
            # L_N(Omega) value-Lagrange summand, not an assumed quotient.
            raw = data(N)
            _,_,_,Rp,Rm,L,Pphysical,*_ = raw
            E = np.diag([(pow(Q,-r,p)-1) % p for r in range(1,N)],1)
            F = np.diag([(1-pow(Q,r,p)) % p for r in range(1,N)],-1)
            K = np.diag([pow(x,1,p)*pow(Q,-r,p) % p for r in range(N)])
            Et,Ft,Kt = coproduct(E,F,K,2,N,p)
            Ki = np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
            O = (Ft@Et+q*Kt+pow(q,-1,p)*Ki) % p
            eye = np.eye(N*N,dtype=np.int64)
            circle = {}
            for j in set(js):
                value = L.copy()
                cj = (pow(q,2*j+1,p)+pow(q,-2*j-1,p)) % p
                for other in range(M+1):
                    if other==j: continue
                    ck = (pow(q,2*other+1,p)+pow(q,-2*other-1,p)) % p
                    value = value@(O-ck*eye) % p*pow(cj-ck,-1,p) % p
                actual_factor = h0s[j]*(Ws[j]*np.array([pow(int(g),-1,p) for g in metrics[j]])[None,:]) % p@bars[j].T % p@Pphysical % p
                assert np.array_equal(value,actual_factor)
                circle[j] = value
            source,ordinary_cap,marker = sources(N,x,p)
            for exponents in ((0,0,0),(1,-2,3)):
                value = source.copy()
                phase_twists = 1
                for axis,(j,e) in enumerate(zip(js,exponents)):
                    box = matrix_power(Rp,e,Rm,p)@circle[j] % p
                    omega = pow(eta,d*d,p)*(-1)**j*pow(q,j*(j+1),p) % p
                    phase_twists = phase_twists*pow(omega,e,p) % p
                    value = axis_apply(box,value,axis,p)
                scalar = int(np.sum(marker*value) % p)
                assert int(np.sum(ordinary_cap*value) % p)==0
                assert scalar == observed*phase_twists % p
                direct_values.append({'labels':list(js),'signed_original_exponents':list(exponents),'actual_marked_scalar':scalar})
        triples += 1
    return {'N':N,'all_channel_dual_maps':dual_checks,'supported_marked_triples':triples,
            'zero_source_triples':forbidden,'literal_marked_and_reversed_ordinary_sources':True,
            'ungrouped_full_normal_physical_sources':direct_values}


if __name__=='__main__':
    rows = [level(N) for N in range(2,12)]
    result = {'status':'PASS','generic_theta':generic_theta(),'generic_physical_lifts':generic_physical_lifts(),'exact_levels':rows,
              'scope':'All folded-channel original marked two-vertex contraction with full circle normals. No arbitrary graph contraction or volume claim.'}
    Path(__file__).with_name('actual_trivalent_all_channel_marked_contraction_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 10 all-channel physical levels; exact generic ordered theta/Vandermonde; all original marked contractions')
