#!/usr/bin/env python3
"""Source-exact q-Pascal packet and its coherent positive metric.

The original path calculation starts at E/F entries, all turns, the
specified original cut coupon and full common Cartan; it is not fitted
to the positive sum or to a known knot scalar.
"""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_finite_sum_annihilator import field
from audit_figure_eight_whole_source import MixedEntries, ACTION_WORD
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_borel_regular_fusion import inv
from audit_actual_two_cut_ports import word_matrix, partial


def original_packet(E, x):
    N, p, Q, d = E.N, E.p, E.Q, E.N-1
    xv = pow(x, -1, p)*pow(Q, -1, p) % p
    g0 = pow(x, 1-N, p)
    cup2 = N*pow(x, -d, p)*pow(g0, -1, p) % p
    answer = {}
    for a in range(N):
        weight = N*pow(x, -(d-a), p)*cup2*g0 % p
        paths = [((a, d-a, d, 0), (), weight)]
        colors = [x, xv, xv, x]
        for position, sign in ACTION_WORD:
            x1, x2 = colors[position:position+2]
            new = []
            for state, route, old in paths:
                aa, bb = state[position:position+2]
                maximum = min(aa, d-bb) if sign > 0 else min(bb, d-aa)
                for k in range(maximum+1):
                    value = E.direct(x1, x2, aa, bb, k, sign)
                    if not value:
                        continue
                    pair = (bb+k, aa-k) if sign > 0 else (bb-k, aa+k)
                    out = state[:position]+pair+state[position+2:]
                    new.append((out, route+(k,), old*value % p))
            paths = new
            colors[position], colors[position+1] = colors[position+1], colors[position]
        for out, route, old in paths:
            if out[0]+out[1] != d or out[2]+out[3] != d:
                continue
            assert route[0] == 0 and route[2:] == (a, 0)
            k = route[1]
            cap1 = pow(x, out[0], p)*pow(N, -1, p) % p
            cap2 = pow(x, out[2], p)*pow(N, -1, p) % p
            # Literal full colored Cartan q^((N-1)alpha_dual).
            value = old*cap1*cap2*pow(xv, d, p) % p
            answer[a, k] = (answer.get((a, k), 0)+value) % p
    return answer


def finite_field_checks():
    rows = []
    for N in range(2, 10):
        p, generator, q = field(N)
        E = MixedEntries(N, p, q)
        Q = E.Q
        P = [[E.gaussian(n, k) if k <= n else 0 for k in range(N)]
             for n in range(N)]
        B = [[((-1)**(n-k)*pow(Q, (n-k)*(n-k-1)//2, p)*E.gaussian(n, k)) % p
              if k <= n else 0 for k in range(N)] for n in range(N)]
        for n in range(N):
            for k in range(N):
                assert sum(P[n][j]*B[j][k] for j in range(N)) % p == (n == k)
                assert sum(B[n][j]*P[j][k] for j in range(N)) % p == (n == k)

        count, fibers = 0, 0
        for M in (1, pow(generator, 3, p)):
            x = -M*pow(q, -1, p) % p
            Y = Q*x*x % p
            packet = original_packet(E, x)
            for u in (1, 2, 5):
                exterior = [pow(generator, n*n+3*n+1, p) for n in range(N)]
                direct_total = sum(value*pow(u, k, p)*exterior[a+k]
                                   for (a, k), value in packet.items()) % p
                collapsed_total = 0
                for n in range(N):
                    C = (-1)**n*pow(Q, -n*(n+1)//2, p)*E.pochhammer(Q*pow(Y, -1, p) % p, n) % p
                    v = [(-1)**k*pow(Q, k*(k-1)//2, p)*pow(u*Y*Q, k, p) % p
                         for k in range(N)]
                    output = sum(P[n][k]*v[k] for k in range(n+1)) % p
                    assert output == E.pochhammer(u*Y*Q % p, n)
                    for k in range(n+1):
                        # Original zero coefficients remain zero whole factors;
                        # no division by C_n or interpolation is performed.
                        actual = packet.get((n-k, k), 0)*pow(u, k, p) % p
                        predicted = C*P[n][k]*v[k] % p
                        assert actual == predicted, (N, M, n, k, u, actual, predicted)
                        count += 1
                    collapsed_total += exterior[n]*C*output
                    fibers += 1
                assert direct_total == collapsed_total % p
        # All-exterior coordinate transport is a true matrix operation.
        A = [[pow(generator, 2*i+j*j+1, p) for j in range(N)] for i in range(3)]
        AB = [[sum(A[i][j]*B[j][k] for j in range(N)) % p for k in range(N)]
              for i in range(3)]
        assert all(sum(AB[i][j]*P[j][k] for j in range(N)) % p == A[i][k]
                   for i in range(3) for k in range(N))
        rows.append({'N': N, 'original_full_route_fugacity_checks': count,
                     'retained_boundary_fiber_checks': fibers,
                     'both_exact_Pascal_inverses_and_arbitrary_exterior': True})
    return rows


def gram_checks():
    mp.mp.dps = 85
    rows = []
    for N in range(2, 15):
        q, d = mp.e**(mp.j*mp.pi/N), N-1
        Q = q*q
        F = [mp.mpc(1)]
        for j in range(1, N):
            F.append(F[-1]*(1-Q**j))
        P = mp.matrix(N)
        B = mp.matrix(N)
        for n in range(N):
            for k in range(n+1):
                P[n, k] = F[n]/(F[k]*F[n-k])
                B[n, k] = (-1)**(n-k)*Q**((n-k)*(n-k-1)//2)*P[n, k]
        close = lambda a, b: mp.norm(a-b) <= mp.mpf('1e-65')*max(1, mp.norm(b))
        assert close(P*B, mp.eye(N))
        v = mp.matrix([(-1)**k*Q**(k*(k+1)//2) for k in range(N)])
        f = mp.matrix(F)
        H = mp.diag([abs(z)**2 for z in F])
        G = P.H*H*P
        Gi = B*mp.diag([1/abs(z)**2 for z in F])*B.H
        a = P.H*f
        assert close(P*v, f)
        # Literal original physical current Euler realization, including
        # the compulsory Gaussian relating the transposed lowering current.
        Fop, Eop = mp.matrix(N), mp.matrix(N)
        for j in range(N-1):
            Fop[j+1,j] = 1-Q**(j+1)
            Eop[j,j+1] = Q**(-j-1)-1
        def euler(A):
            total, power = mp.eye(N), mp.eye(N)
            for r in range(1,N):
                power = power*A
                total += power/F[r]
            return total
        assert close(euler(Fop), P)
        Uphysical = mp.diag([Q**(-j*(j+1)//2) for j in range(N)])
        assert close(Uphysical*euler(Eop)*Uphysical.H, P.T)
        assert close(G, G.H)
        # Remove only independently bounded roundoff anti-Hermitian part
        # before the library's exact-diagonal Hermiticity test.
        mp.cholesky((G+G.H)/2)  # Full rank, not a rank-one co-source metric.
        assert abs((a.H*Gi*a)[0]-N) < mp.mpf('1e-60')
        energy = mp.fsum(abs(z)**4 for z in F)
        assert abs((v.H*G*v)[0]/energy-1) < mp.mpf('1e-65')
        K = (a.H*v)[0]
        assert abs(K-mp.fsum(abs(z)**2 for z in F)) < mp.mpf('1e-65')*max(1, abs(K))
        assert abs(K)**2 <= N*energy*(1+mp.mpf('1e-65'))

        D = mp.diag([mp.sqrt(abs(z))/mp.root(N, 4) for z in F])
        Di = mp.diag([1/D[j,j] for j in range(N)])
        Pb, Hb, cb = Di*P, D*D*H, D*mp.matrix([mp.conj(z) for z in F])
        assert close(Pb.H*Hb*Pb, G)
        assert close(cb.T*Pb*v, f.H*f)
        assert abs(Pb[0,0]-mp.root(N,4)) < mp.mpf('1e-70')

        for ell in (-3, 2):
            U = mp.diag([Q**(ell*k*(k+1)//2) for k in range(N)])
            Gs, ass = U.H*G*U, U.H*a
            Gis = U.H*Gi*U
            assert abs((ass.H*Gis*ass)[0]-N) < mp.mpf('1e-60')
            assert close(Gs, Gs.H)
        rows.append({'N': N, 'full_rank_non_diagonal_Gram': True,
                     'source_dual_norm_squared': N,
                     'literal_b_zero_row_and_all_normalizers': True,
                     'unitary_chirp_pullbacks': 2})
    return rows


def actual_fusion_blocks():
    rows = []
    for N in range(2,10):
        p,g,q = field(N)
        E = MixedEntries(N,p,q)
        Q,d = E.Q,N-1
        Fop = np.zeros((N,N),dtype=np.int64)
        for j in range(d):
            Fop[j+1,j] = (1-pow(Q,j+1,p)) % p
        checked = 0
        for M in (1,pow(g,3,p)):
            x = -M*pow(q,-1,p) % p
            Ki = np.diag([pow(x,-1,p)*pow(Q,j,p) % p for j in range(N)])
            current = (np.kron(Fop,np.eye(N,dtype=np.int64))
                       +np.kron(Ki,Fop)) % p
            powers = [np.eye(N*N,dtype=np.int64)]
            for _ in range(d):
                powers.append(powers[-1]@current % p)
            for T in range(2*d+1):
                interval = range(max(0,T-d),min(T,d)+1)
                for a in interval:
                    col = powers[a][:,T-a]  # seed |0,T-a>
                    for u in interval:
                        expected = 0
                        if u<=a:
                            dout = pow(x,u,p)*E.F[u]*E.F[T-u] % p
                            din = pow(x,-a,p)*pow(E.F[T-a],-1,p) % p
                            expected = dout*E.gaussian(a,u)*din % p
                        assert int(col[u*N+T-u]) == expected
                        checked += 1
            Cd = np.zeros((N,N),dtype=np.int64)
            for a in range(N):
                for u in range(N):
                    Cd[u,a] = powers[a][u*N+d-u,d-a]
            cup = [N*pow(x,u-d,p) % p for u in range(N)]
            cap = [pow(x,-u,p)*pow(Q,-u,p)*pow(N,-1,p) % p for u in range(N)]
            marker = [pow(x,d-u,p)*pow(N,-2,p) % p for u in range(N)]
            assert list(Cd[:,d]) == cup
            for a in range(N):
                ordinary = sum(cap[u]*int(Cd[u,a]) for u in range(N)) % p
                assert ordinary == (pow(N,-1,p) if a==0 else 0)
                marked = sum(marker[u]*int(Cd[u,a]) for u in range(N)) % p
                sine_squared = (-1)**a*pow(Q,-a*(a+1)//2,p)*E.F[a]**2 % p
                expected = pow(x,d-a,p)*sine_squared*pow(N,-2,p) % p
                assert marked == expected
        rows.append({'N':N,'literal_total_current_Pascal_block_entries':checked,
                     'all_total_integer_degrees_including_high_blocks':True})
    return rows


def actual_signed_crossing_alphabet():
    rows = []
    for N in range(2,9):
        for M in (1,2):
            H = HardyNetwork(N,M)
            p,Q,x,d = H.p,H.Q,H.x,N-1
            positive,negative = np.zeros_like(H.plus),np.zeros_like(H.minus)
            for T in range(2*d+1):
                indices = list(range(max(0,T-d),min(T,d)+1))
                n = len(indices)
                C,U,Ui = (np.zeros((n,n),dtype=np.int64) for _ in range(3))
                for i,u in enumerate(indices):
                    for j,a in enumerate(indices):
                        if u<=a:
                            C[i,j] = (pow(x,u-a,p)*H.fac[a]*H.fac[T-u]
                                      *pow(H.fac[a-u]*H.fac[T-a] % p,-1,p)) % p
                        if u>=a:
                            r = u-a
                            U[i,j] = pow(x,-r,p)*pow(H.fac[r],-1,p) % p
                            Ui[i,j] = (pow(-1,r,p)*pow(Q,r*(r-1)//2,p)
                                       *int(U[i,j])) % p
                D = np.diag([pow(-1,T-a,p)*pow(Q,(T-a)*(T-a-1)//2,p)
                             *pow(x,-2*(T-a),p) % p for a in indices])
                Di = np.diag([pow(int(z),-1,p) for z in np.diag(D)])
                Ci = inv(C,p)
                assert np.array_equal(U@Ui % p,np.eye(n,dtype=np.int64))
                Rp = H.kappa*C@D % p@U % p@Ci % p
                Rm = pow(H.kappa,-1,p)*C@Ui % p@Di % p@Ci % p
                physical = [a*N+T-a for a in indices]
                assert np.array_equal(Rp,H.plus[np.ix_(physical,physical)])
                assert np.array_equal(Rm,H.minus[np.ix_(physical,physical)])
                positive[np.ix_(physical,physical)] = Rp
                negative[np.ix_(physical,physical)] = Rm
            assert np.array_equal(positive,H.plus)
            assert np.array_equal(negative,H.minus)
            words = []
            if N<=4:
                for width,word in ((2,[1,1,1]),(3,[1,-2,1,-2]),(4,[1,-2,3,1,-2])):
                    old = word_matrix(word,H.plus,H.minus,width,N,p)
                    new = word_matrix(word,positive,negative,width,N,p)
                    assert np.array_equal(old,new)
                    writhe = sum(1 if letter>0 else -1 for letter in word)
                    external = H.dimension*pow(H.twist,-writhe,p) % p
                    oldcap = external*partial(old,H.pivot,width,N,p) % p
                    newcap = external*partial(new,H.pivot,width,N,p) % p
                    assert np.array_equal(oldcap,newcap)
                    words.append({'width':width,'word':word,'full_original_cut_matrix':True})
            rows.append({'N':N,'M':M,'both_original_signs_all_total_blocks':2*(2*d+1),
                         'common_Cartan_and_literal_negative_inverse':True,
                         'full_pivotal_source_words':words})
    return rows


def overlap_checks():
    rows = []
    for N in range(2,8):
        H = HardyNetwork(N,1)
        p,Q,x,d = H.p,H.Q,H.x,N-1
        C = np.zeros((N*N,N*N),dtype=np.int64)
        for a in range(N):
            for k in range(N):
                for u in range(a+1):
                    v = k+a-u
                    if v<N:
                        # Divided-power fusion C'=C/F_a, with original x.
                        C[u*N+v,a*N+k] = (pow(x,u-a,p)*H.fac[v]
                            *pow(H.fac[a-u]*H.fac[k] % p,-1,p)) % p
        Cd = C[np.ix_([u*N+d-u for u in range(N)],
                      [a*N+d-a for a in range(N)])]
        Cdi = inv(Cd,p)
        for a in range(N):
            for u in range(a,N):
                V_a = pow(x,a,p)*pow(-1,a,p)*pow(Q,a*(a+1)//2,p) % p
                V_u = pow(x,u,p)*pow(-1,u,p)*pow(Q,u*(u+1)//2,p) % p
                beta = H.fac[u]*pow(H.fac[a]*H.fac[u-a] % p,-1,p) % p
                expected = (V_a*pow(V_u,-1,p)*pow(-1,u-a,p)
                            *pow(Q,(u-a)*(u-a-1)//2,p)*beta) % p
                assert int(Cdi[a,u]) == expected
        if N<=4:
            Ci = inv(C,p)
            A = np.kron(np.eye(N,dtype=np.int64),Ci)@np.kron(C,np.eye(N,dtype=np.int64)) % p
            for u in range(N):
                col = u*N+d-u  # |0,u,d-u>
                for a in range(N):
                    row = a*N+d-a
                    assert int(A[row,col]) == int(Cdi[a,u])
        rows.append({'N':N,'all_pair_d_overlap_entries':N*(N+1)//2,
                     'full_three_head_matrix_checked':N<=4})
    return rows


def energy_rate_checks():
    mp.mp.dps = 70
    V = 2*mp.im(mp.polylog(2, mp.e**(mp.j*mp.pi/3)))
    rows = []
    for N in (16, 32, 64, 128, 256, 512, 1024):
        logs = [mp.mpf(0)]
        for j in range(1, N):
            logs.append(logs[-1]+mp.log(2*mp.sin(mp.pi*j/N)))
        maximum = max(4*x for x in logs)
        log_energy = maximum+mp.log(mp.fsum(mp.exp(4*x-maximum) for x in logs))
        scaled = mp.pi*(mp.log(N)+log_energy)/N
        rows.append({'N': N, 'pi_log_Cauchy_budget_over_N': float(scaled),
                     'target_volume': float(V)})
    assert abs(rows[-1]['pi_log_Cauchy_budget_over_N']-float(V)) < .12
    return rows


if __name__ == '__main__':
    result = {'status': 'PASS', 'original_packets': finite_field_checks(),
              'physical_fusion_embedding':actual_fusion_blocks(),
              'original_signed_crossing_alphabet':actual_signed_crossing_alphabet(),
              'actual_reassociation':overlap_checks(),
              'coherent_metric': gram_checks(), 'sharp_energy': energy_rate_checks()}
    Path(__file__).with_name('actual_pascal_coherent_gram_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS: 8 packet/fusion levels, 14 signed crossing families, 18 pivotal words, 13 Gram/source levels, 7 rates')
