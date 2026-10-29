#!/usr/bin/env python3
"""FULL actual reassociation, physical quarter metric and b-angle kernel.

Fusion is built independently from original coproduct powers. Original R
comes from its separate E/F construction, with common Cartan retained.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork


def actual_divided_fusion(H, x):
    N,p,Q,d = H.N,H.p,H.Q,H.N-1
    F = np.zeros((N,N),dtype=np.int64)
    S = np.zeros_like(F)
    for a in range(d):
        F[a+1,a] = (1-pow(Q,a+1,p)) % p
        S[a,a+1] = 1
    Kinv = np.diag([pow(x,-1,p)*pow(Q,a,p) % p for a in range(N)])
    total = (np.kron(F,np.eye(N,dtype=np.int64))+np.kron(Kinv,F)) % p
    powers = [np.eye(N*N,dtype=np.int64)]
    for _ in range(d):
        powers.append(powers[-1]@total % p)
    C = np.zeros((N*N,N*N),dtype=np.int64)
    for a in range(N):
        for b in range(N):
            C[:,a*N+b] = powers[a][:,b]*pow(H.fac[a],-1,p) % p

    T = pow(x,-1,p)*np.kron(S,F) % p
    Euler,Inverse = np.eye(N*N,dtype=np.int64),np.eye(N*N,dtype=np.int64)
    power = np.eye(N*N,dtype=np.int64)
    for r in range(1,N):
        power = power@T % p
        term = power*pow(H.fac[r],-1,p) % p
        Euler = (Euler+term) % p
        Inverse = (Inverse+pow(-1,r,p)*pow(Q,r*(r-1)//2,p)*term) % p
    assert np.array_equal(Euler,C)
    assert np.array_equal(C@Inverse % p,np.eye(N*N,dtype=np.int64))
    assert np.array_equal(Inverse@C % p,np.eye(N*N,dtype=np.int64))
    assert np.array_equal(S@F % p,((1-Q)*np.eye(N,dtype=np.int64)+Q*F@S) % p)
    return C,Inverse


def all_entry_checks():
    rows = []
    for N in range(2,8):
        H = HardyNetwork(N,1)
        p,Q,d = H.p,H.Q,N-1
        x,y = H.x,2*H.x % p
        Cx,_ = actual_divided_fusion(H,x)
        _,Cyi = actual_divided_fusion(H,y)
        actual = np.kron(np.eye(N,dtype=np.int64),Cyi)@np.kron(Cx,np.eye(N,dtype=np.int64)) % p
        expected = np.zeros_like(actual)
        entries = 0
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    for r in range(min(a,d-b)+1):
                        m = b+r
                        for s in range(min(m,d-c)+1):
                            u,v,w = a-r,m-s,c+s
                            bin1 = H.fac[m]*pow(H.fac[r]*H.fac[b] % p,-1,p) % p
                            bin2 = H.fac[w]*pow(H.fac[s]*H.fac[c] % p,-1,p) % p
                            value = (pow(-1,s,p)*pow(Q,s*(s-1)//2,p)
                                     *pow(x,-r,p)*pow(y,-s,p)*bin1*bin2) % p
                            row,col = (u*N+v)*N+w,(a*N+b)*N+c
                            assert expected[row,col] == 0  # Unique path.
                            expected[row,col] = value
                            cells = [(r,u,d-a),(r,b,d-m),(s,v,d-m),(s,c,d-w)]
                            assert all(min(t)>=0 and sum(t)==d for t in cells)
                            assert cells[0][0]==cells[1][0] and cells[2][0]==cells[3][0]
                            assert cells[1][2]==cells[2][2]
                            recovered = (cells[0][0]+cells[0][1],cells[1][1],cells[3][1],
                                         cells[0][1],cells[2][1],cells[3][0]+cells[3][1])
                            assert recovered == (a,b,c,u,v,w)
                            entries += 1
        assert np.array_equal(actual,expected)
        rows.append({'N':N,'complete_nonzero_entries_with_phase':entries,
                     'all_zero_entries_also_compared':N**6-entries,
                     'strict_intermediate_wall_and_cell_bijection':True})
    return rows


def physical_crossing_checks():
    rows = []
    for N in range(2,10):
        for M in (1,2):
            H = HardyNetwork(N,M)
            p,Q,x,d = H.p,H.Q,H.x,N-1
            C,Ci = actual_divided_fusion(H,x)
            flip = np.zeros((N*N,N*N),dtype=np.int64)
            for a in range(N):
                for b in range(N):
                    flip[b*N+a,a*N+b] = 1
            C21,C21i = flip@C@flip % p,flip@Ci@flip % p
            D = np.diag([pow(-1,b,p)*pow(Q,b*(b-1)//2,p)*pow(x,-2*b,p) % p
                         for a in range(N) for b in range(N)])
            Di = np.diag([pow(int(t),-1,p) for t in np.diag(D)])
            positive = H.kappa*C@D % p@C21 % p@Ci % p
            negative = pow(H.kappa,-1,p)*C@C21i % p@Di % p@Ci % p
            assert np.array_equal(positive,H.plus)
            assert np.array_equal(negative,H.minus)
            rows.append({'N':N,'M':M,'original_positive_negative_full_matrices':True,
                         'literal_Cartan_entry':H.kappa,'normalization':H.normalization})
    return rows


def metric_phase_and_b_checks():
    mp.mp.dps = 80
    rows = []
    for N in range(2,11):
        q,d = mp.e**(mp.j*mp.pi/N),N-1
        Q = q*q
        x,y = -q**-1,mp.e**(mp.j*mp.mpf('.27'))
        s,F = [mp.mpf(1)],[mp.mpc(1)]
        for j in range(1,N):
            s.append(s[-1]*2*mp.sin(mp.pi*j/N))
            F.append(F[-1]*(1-Q**j))
        beta = lambda L,r:s[L]/(s[r]*s[L-r])
        wfun = lambda t:1/mp.fprod(s[j] for j in t)
        tau = {}
        for L in range(N):
            D = mp.sqrt(s[L])/mp.root(N,4)
            for r in range(L+1):
                coefficient = (-1)**r*Q**(r*(r-1)//2)*F[L]/(F[r]*F[L-r])
                tau[L,r] = mp.sqrt(s[r]*s[L-r]/N)*coefficient/D
                assert abs(abs(tau[L,r])**2/(mp.sqrt(N)*wfun((r,L-r,d-L)))-1) < mp.mpf('1e-65')
        assert abs(tau[0,0]-N**mp.mpf('-.25')) < mp.mpf('1e-70')
        # Every complementary original cup entry is fixed by the SAME
        # physical gauge; cap inverses and pivots then follow directly.
        g = [mp.root(N,4)/mp.sqrt(t) for t in s]
        assert all(abs(g[a]*g[d-a]-1)<mp.mpf('1e-65') for a in range(N))

        count,full = 0,N<=6
        inputs = range(N) if full else sorted({0,1,d//3,2*d//3,d})
        for a in inputs:
            for b in inputs:
                for c in inputs:
                    for r in range(min(a,d-b)+1):
                        m = b+r
                        for t in range(min(m,d-c)+1):
                            u,v,z = a-r,m-t,c+t
                            raw = ((-1)**t*Q**(t*(t-1)//2)*x**(-r)*y**(-t)
                                   *F[m]/(F[r]*F[b])*F[z]/(F[t]*F[c]))
                            weighted = raw*g[u]*g[v]*g[z]/(g[a]*g[b]*g[c])
                            cells = [(r,u,d-a),(r,b,d-m),(t,v,d-m),(t,c,d-z)]
                            weight = mp.fprod(wfun(cell) for cell in cells)
                            omega = (-1)**t*x**(-r)*y**(-t)*q**(r*b+t*c+t*(t-1))
                            target = N*N*omega*mp.sqrt(weight)
                            assert abs(weighted/target-1)<mp.mpf('1e-60')
                            eta = (-1)**t*x**(-r)*y**(-t)*q**(r*(2-a-r)+t*(1-b-r))
                            btarget = N*eta*tau[a,r]*tau[m,r]*tau[m,t]*tau[z,t]
                            assert abs(weighted/btarget-1)<mp.mpf('1e-60')
                            count += 1
        rows.append({'N':N,'full_input_set':full,'quarter_metric_complete_kernel_checks':count,
                     'actual_unit_phase_and_b_half_density':True,
                     'original_source_complements_and_zero_length_slots':True})
    return rows


if __name__=='__main__':
    result = {'status':'PASS','actual_all_entries':all_entry_checks(),
              'full_original_crossings':physical_crossing_checks(),
              'physical_metric_and_normalized_b':metric_phase_and_b_checks()}
    Path(__file__).with_name('actual_reassociation_angle_kernel_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS: 6 full reassociation levels, 16 original signed crossing families, 9 quarter-metric/b/source levels')
