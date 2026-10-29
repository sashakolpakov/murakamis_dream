#!/usr/bin/env python3
"""Actual cup-source Hermite channel, full signed R and Plancherel frame.

Finite-field matrices come from the original E/F/R implementation.
Generic-q cup confluence is checked independently in complex arithmetic.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data


def exact_actual_matrices():
    rows = []
    for N in range(2,17):
        p,eta,q,E,F,K,pivot,Rp,Rm = balanced_data(N)
        Q,d,rho = q*q % p,N-1,(q-pow(q,-1,p)) % p
        x = int(K[0,0])
        Ecal = rho*rho*E % p
        assert all(int(Ecal[j-1,j])==(pow(Q,-j,p)-1) % p for j in range(1,N))
        I = np.eye(N,dtype=np.int64)
        Ki = np.diag([pow(int(z),-1,p) for z in np.diag(K)])
        Ft = (np.kron(F,I)+np.kron(Ki,F)) % p
        Et = (np.kron(Ecal,K)+np.kron(I,Ecal)) % p
        Kt = np.kron(K,K) % p
        Kti = np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
        Omega = (Ft@Et+q*Kt+pow(q,-1,p)*Kti) % p
        ids = [u*N+d-u for u in range(N)]
        O = Omega[np.ix_(ids,ids)]
        cstar = (q+pow(q,-1,p)) % p

        harmonic = [0]
        for j in range(1,N):
            harmonic.append((harmonic[-1]+pow(1-pow(Q,j,p),-1,p)) % p)
        assert harmonic[-1] == d*pow(2,-1,p) % p
        g = np.array([pow(x,u-d,p) for u in range(N)],dtype=np.int64)
        v = np.array([-int(g[u])*harmonic[u]*pow(rho,-1,p) % p for u in range(N)],dtype=np.int64)
        cup = N*g % p
        ordinary = np.array([pow(x,-u,p)*pow(Q,-u,p)*pow(N,-1,p) % p for u in range(N)])
        marked = np.array([pow(x,d-u,p)*pow(N,-2,p) % p for u in range(N)])
        gamma = q*pow(x,-d,p)*pow(N*rho*rho % p,-1,p) % p
        assert gamma == pow(-1,N,p)*pow(N*rho*rho % p,-1,p) % p
        assert int(ordinary@g) % p == 0 and int(marked@g) % p == pow(N,-1,p)
        assert int(ordinary@v) % p == gamma
        mu = int(marked@v) % p
        assert mu == -sum(harmonic)*pow(N*N*rho % p,-1,p) % p
        t = (v-mu*cup)*pow(gamma,-1,p) % p
        V = np.column_stack([cup,t])
        U = np.vstack([marked,ordinary])
        assert np.array_equal(U@V % p,np.eye(2,dtype=np.int64))
        theta = pow(-1,N,p)*rho*rho % p
        J = np.array([[cstar,theta],[0,cstar]],dtype=np.int64)
        assert np.array_equal(O@V % p,V@J % p)
        tau = pow(-1,N+1,p)*d*rho*pow(2,-1,p) % p
        kappa = int(Rp[0,0])
        for sign,R in ((1,Rp),(-1,Rm)):
            B = R[np.ix_(ids,ids)]
            expected = pow(kappa,sign,p)*V@np.array([[1,sign*tau % p],[0,1]],dtype=np.int64) % p
            assert np.array_equal(B@V % p,expected)
        for k in range(1,N):
            actual = sum(harmonic[u]*pow(Q,-k*u,p) for u in range(N)) % p
            target = -k*pow(1-pow(Q,-k,p),-1,p) % p
            assert actual == target
        rows.append({'N':N,'original_EF_Casimir_and_both_R':True,
                     'original_cup_ordinary_marked_dual_rows':True,
                     'halfroot_parity_and_exact_full_DFT':True})
    return rows


def omega_block(N,z):
    d,Q,x = N-1,z*z,z**(N-1)
    M = -z**N
    e = lambda j:M*Q**(-j)-1/M
    O = mp.zeros(N)
    for u in range(N):
        b = d-u
        if u:
            E1 = e(u)*x*Q**(-b)
            O[u,u] += E1*(1-Q**u)
            if b<d:
                O[u-1,u] += E1/x*Q**(u-1)*(1-Q**(b+1))
        if b:
            E2 = e(b)
            if u<d:
                O[u+1,u] += E2*(1-Q**(u+1))
            O[u,u] += E2/x*Q**u*(1-Q**b)
        O[u,u] += z+1/z  # K_tot=1 exactly on degree d.
    return O


def qcup_vectors(N,z):
    d,x = N-1,z**(N-1)
    fac = [mp.mpc(1)]
    for j in range(1,N):
        fac.append(fac[-1]*(1-z**(2*j)))
    g = mp.matrix([x**(u-d) for u in range(N)])
    h = mp.matrix([g[u]*(-1)**u*z**(-u*(u+1))*fac[u]*fac[d-u]/fac[d]
                   for u in range(N)])
    return g,h


def generic_q_confluence_checks():
    mp.mp.dps = 85
    rows = []
    for N in (2,3,4,6,9,12):
        q = mp.e**(mp.j*mp.pi/N)
        Q,rho,d = q*q,q-1/q,N-1
        harmonic = [mp.mpc(0)]
        for u in range(1,N):
            harmonic.append(harmonic[-1]+1/(1-Q**u))
        groot,_ = qcup_vectors(N,q)
        v = mp.matrix([-groot[u]*harmonic[u]/rho for u in range(N)])
        z = q*mp.exp(mp.mpf('0.00013')+mp.j*mp.mpf('0.00007'))
        g,h = qcup_vectors(N,z)
        O = omega_block(N,z)
        ctop = z**(2*N-1)+z**(-2*N+1)
        ctri = z+1/z
        assert mp.norm(O*g-ctop*g)<mp.mpf('1e-65')*max(1,mp.norm(g))
        assert mp.norm(O*h-ctri*h)<mp.mpf('1e-65')*max(1,mp.norm(h))
        # An independent analytic derivative of the ACTUAL cup ratio.
        for u in range(N):
            def ratio(t):
                gg,hh = qcup_vectors(N,t)
                return hh[u]/gg[u]
            derivative = q*mp.diff(ratio,q)
            assert abs(derivative+2*N*harmonic[u])<mp.mpf('1e-60')
        z = q*mp.exp(mp.mpf('1e-18'))
        gg,hh = qcup_vectors(N,z)
        gap = z+1/z-z**(2*N-1)-z**(-2*N+1)
        quotient = (hh-gg)/gap
        assert mp.norm(quotient-v)<mp.mpf('1e-11')*max(1,mp.norm(v))
        rows.append({'N':N,'actual_generic_q_invariant_cup_and_top_descendant':True,
                     'harmonic_divided_difference_and_root_limit':True})
    return rows


def physical_plancherel_checks():
    mp.mp.dps = 85
    rows = []
    for N in (2,3,4,5,6,7,8,9,12,16,24,32,64,128):
        q,d = mp.e**(mp.j*mp.pi/N),N-1
        Q,rho,x = q*q,q-1/q,q**d
        H = [mp.mpc(0)]
        for j in range(1,N):
            H.append(H[-1]+1/(1-Q**j))
        bar = mp.fsum(H)/N
        g = [x**(u-d) for u in range(N)]
        cup = [N*a for a in g]
        t = [(-1)**(N+1)*N*rho*g[u]*(H[u]-bar) for u in range(N)]
        norm2 = mp.fsum(abs(a)**2 for a in t)
        target = N*abs(rho)**2*mp.fsum(k*k/abs(1-Q**k)**2 for k in range(1,N))
        assert abs(norm2/target-1)<mp.mpf('1e-65')
        assert abs(mp.fsum(mp.conj(cup[u])*t[u] for u in range(N)))<mp.mpf('1e-60')
        rootsum = mp.fsum(1/abs(1-Q**k)**2 for k in range(1,N))
        assert abs(rootsum-mp.mpf(N*N-1)/12)<mp.mpf('1e-65')
        assert norm2>=N**3/4*(1-mp.mpf('1e-65'))
        assert norm2<=mp.pi**2*N**3/6*(1+mp.mpf('1e-65'))
        condition = max(N**mp.mpf('1.5'),mp.sqrt(norm2))/min(N**mp.mpf('1.5'),mp.sqrt(norm2))
        assert condition<=2*(1+mp.mpf('1e-65'))
        ordinary = [x**(-u)*Q**(-u)/N for u in range(N)]
        marked = [x**(d-u)/N**2 for u in range(N)]
        assert abs(mp.fsum(ordinary[u]*t[u] for u in range(N))-1)<mp.mpf('1e-60')
        assert abs(mp.fsum(marked[u]*t[u] for u in range(N)))<mp.mpf('1e-60')
        rows.append({'N':N,'exact_Plancherel_norm':float(norm2/N**3),
                     'physical_frame_condition':float(condition),
                     'uniform_upper_condition':2,
                     'original_source_duals':True})
    return rows


if __name__=='__main__':
    result = {'status':'PASS','literal_original_matrices':exact_actual_matrices(),
              'source_preserving_q_confluence':generic_q_confluence_checks(),
              'uniform_physical_Gram':physical_plancherel_checks()}
    Path(__file__).with_name('actual_tame_c0_hermite_source_frame_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS: 15 original Casimir/R/source levels, 6 generic-q confluences, 14 uniform Plancherel frames')
