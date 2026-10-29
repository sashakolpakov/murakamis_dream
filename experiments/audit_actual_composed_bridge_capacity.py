#!/usr/bin/env python3
"""Actual all-width source block and its sharp coherent capacity."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.special import logsumexp

from audit_actual_two_cut_ports import balanced_data
from audit_actual_complete_source_multiplicity_module import apply_pair
from audit_actual_half_clock_source_dilation import original_factorial_R
from audit_actual_coherent_terminal_bridge_metric import data, row_potential


def original_all_width(N, pairs):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, width, Q = N-1, 2*pairs, q*q % prime
    x = int(K[0, 0])
    cup, cap, marked = [np.zeros(N*N, dtype=np.int64) for _ in range(3)]
    for a in range(N):
        for b in range(N):
            marked[a*N+b] = pow(x, b, prime)*pow(N, -2, prime) % prime
            if a+b == d:
                cup[a*N+b] = N*pow(x, -b, prime) % prime
                cap[a*N+b] = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
    bottom, top = cup.copy(), marked.copy()
    for _ in range(pairs-1):
        bottom = np.kron(bottom, cup) % prime
        top = np.kron(cap, top) % prime
    prefix = [width-1, -1, width-2, 2]
    state = bottom[:, None]
    for a in prefix:
        state = apply_pair(Rp if a > 0 else Rm, state, abs(a)-1, width, N, prime)
    # This is the original EVEN invariant-tensor inverse; the marked partner
    # was crossed in the prefix, so an odd-head extraction would be invalid.
    reduced = (state[:, 0].reshape(N**(width-2), N, N)[:, 0, d]
               *pow(x, d, prime)*pow(N, -1, prime)) % prime
    for _ in range(pairs-3):
        reduced = cap@reduced.reshape(N*N, -1) % prime
    states = [v for v in itertools.product(range(N), repeat=4) if sum(v) == 2*d]
    ids = [((a*N+b)*N+c)*N+e for a,b,c,e in states]
    incoming = reduced[ids]
    L = np.zeros((N, len(states)), dtype=np.int64)
    for j, (a,b,c,e) in enumerate(states):
        u = d-e
        L[u,j] = cap[a*N+d-a]*Rp[(d-a)*N+u, b*N+c] % prime
    pair_ids = [j*N+d-j for j in range(N)]
    R = Rp[np.ix_(pair_ids, pair_ids)]
    P = [1]
    for t in range(1, N):
        P.append(((1-pow(Q, t, prime))**2*P[-1]+pow(Q, t, prime)) % prime)
    H = pow(N, -1, prime)*np.diag([pow(x, j, prime) for j in range(N)])@R % prime@np.diag(P[::-1]) % prime
    predicted = int(np.sum(H@L % prime@incoming % prime)) % prime
    suffix = [width-4, -(width-3), width-2, width-2]
    for a in suffix:
        state = apply_pair(Rp if a > 0 else Rm, state, abs(a)-1, width, N, prime)
    assert int(top@state[:, 0]) % prime == predicted
    return {'N': N, 'plat_heads': width, 'original_full_marked_source': True,
            'prefix_crosses_last_marked_partner': True, 'coherent_terminal_block': suffix}


def finite_composition(N):
    q,Q,x,F,s,T,L,charges,cup = data(N)
    d = N-1
    Rfull = original_factorial_R(N)
    ids = [j*N+d-j for j in range(N)]
    R = Rfull[np.ix_(ids, ids)]
    H = np.linalg.solve(R.T, T.T).T
    P = [1.+0j]
    for t in range(1, N):
        P.append((1-Q**t)**2*P[-1]+Q**t)
    expected = np.diag(x**np.arange(N))@R@np.diag(P[::-1])/N
    assert np.allclose(H, expected, rtol=3e-7, atol=3e-7)
    potential, _ = row_potential(N, s, 0)
    block = H@L
    gram = (H*potential[None, :])@H.conj().T
    assert np.allclose(block@block.conj().T, gram, rtol=3e-7, atol=3e-7)
    weighted = H*np.sqrt(potential)[None, :]
    op = np.linalg.svd(weighted, compute_uv=False)[0]
    assert np.isclose(op, np.linalg.svd(block, compute_uv=False)[0], rtol=3e-7)
    maximum = np.max(np.abs(weighted))
    assert maximum <= op*(1+3e-7) and op <= N*maximum*(1+3e-7)
    # Check the physical crossing capacities in the SAME source gauge,
    # including the literal negative matrix, rather than assuming the sign.
    gauge = np.kron(s/np.sqrt(N), s/np.sqrt(N))
    for sign, matrix in [(1, Rfull), (-1, np.linalg.inv(Rfull))]:
        actual = gauge[:, None]*matrix/gauge[None, :]
        magnitude = np.zeros((N*N, N*N))
        for a in range(N):
            for b in range(N):
                if sign == 1:
                    for k in range(min(a, d-b)+1):
                        magnitude[(b+k)*N+a-k, a*N+b] = s[b+k]**2/(s[b]**2*s[k])
                else:
                    for k in range(min(b, d-a)+1):
                        magnitude[(b-k)*N+a+k, a*N+b] = s[a+k]**2/(s[a]**2*s[k])
        assert np.allclose(np.abs(actual), magnitude, rtol=3e-7, atol=3e-7)
    return {'N': N, 'complete_original_composed_Gram': True,
            'both_physical_signed_capacity_formulas': True,
            'exact_matrix_norm_sandwich': True}


def lambda_value(theta):
    return mp.im(mp.polylog(2, mp.exp(2j*theta)))/2


def angle_optimizer():
    with mp.workdps(75):
        pi = mp.pi
        def equations(a,b):
            g = pi-a-b
            return (mp.sin(g)-2*mp.sin(a)**2,
                    mp.sin(g)*mp.cos(b/2)**2-mp.sin(b)**3)
        a,b = mp.findroot(equations, (.24*pi, .35*pi))
        assert 0 < a < pi/2 and pi/6 < b < pi/2
        g = pi-a-b
        value = 4*lambda_value(a)+6*lambda_value(b)+2*lambda_value(g)+8*lambda_value((pi-b)/2)
        v8, v3 = 8*lambda_value(pi/4), 3*lambda_value(pi/3)
        assert v8+3*v3 < value < 2*v8
        aa,bb,gg = mp.cot(a),mp.cot(b),mp.cot(g)
        hessian = mp.matrix([[4*aa+2*gg, 2*gg], [2*gg, 6*bb+2*gg+2*mp.tan(b/2)]])
        assert hessian[0,0] > 0 and mp.det(hessian) > 0
        assert max(abs(v) for v in equations(a,b)) < mp.mpf('1e-65')
        return {'alpha_over_pi': mp.nstr(a/pi, 45), 'beta_over_pi': mp.nstr(b/pi,45),
                'capacity': mp.nstr(value,45), 'separate_capacity': mp.nstr(2*v8,30),
                'smaller_Green_remainder_capacity': mp.nstr(v8+3*v3,30)}


def growing_capacity(N, target):
    with mp.workdps(N+75):
        q=mp.exp(mp.j*mp.pi/N);Q=q*q;d=N-1;x=q**d;kappa=q**(mp.mpf(d*d)/2)
        F=[mp.mpc(1)];P=[mp.mpc(1)]
        for j in range(1,N):
            F.append(F[-1]*(1-Q**j))
            P.append((1-Q**j)**2*P[-1]+Q**j)
        logs=np.array([float(mp.log(abs(v))) for v in F])
        k_cost=np.array([-2*logs[k]+logsumexp([-4*logs[a]-4*logs[d-k-a]
                                             for a in range(d-k+1)]) for k in range(N)])
        logE=np.array([2*np.log(N)+logsumexp(k_cost[:d-u+1]) for u in range(N)])
        entries=[]
        for i in range(N):
            for u in range(d-i,N):
                h=i+u-d
                R=kappa*x**(-d+h)*Q**((d-u)*(d-i))*F[i]*F[u]/(F[h]*F[d-u]*F[d-i])
                value=x**i/N*R*P[d-u]
                if value:
                    logmod=float(mp.log(abs(value)))+logE[u]/2
                    entries.append((i,u,logmod,complex(value/abs(value))))
        scale=max(e[2] for e in entries)
        A=np.zeros((N,N),complex)
        for i,u,logmod,phase in entries:
            A[i,u]=np.exp(logmod-scale)*phase
        singular=np.linalg.svd(A,compute_uv=False)[0]
        lognorm2=2*(scale+np.log(singular))
        lower, upper=2*scale, 2*scale+2*np.log(N)
        assert lower-1e-8<=lognorm2<=upper+1e-8
        rate=np.pi*lognorm2/N
        # The analytic uniform O(log N) estimate is proved in the note.
        # These independent full complex products check its observed scale.
        assert abs(rate-target)<=20*np.log(N)/N
        return {'N':N, 'coherent_operator_pi_lograte':float(rate),
                'max_entry_lower_rate':float(np.pi*lower/N),
                'polynomial_HS_upper_rate':float(np.pi*upper/N),
                'target_unique_angle_capacity':target}


if __name__=='__main__':
    exact=[original_all_width(N,k) for N,k in [(2,3),(3,3),(2,4),(2,5)]]
    finite=[finite_composition(N) for N in range(2,9)]
    optimizer=angle_optimizer()
    target=float(optimizer['capacity'])
    rates=[growing_capacity(N,target) for N in (16,32,64,96,128)]
    output={'status':'PASS','original_all_width_sources':exact,'actual_finite_composition':finite,
            'analytic_optimizer_diagnostic':optimizer,'growing_coherent_capacity':rates,
            'scope':'Sharp all-input block capacity and broad whole-source bound; no sharp knot-volume claim.'}
    Path(__file__).with_name('actual_composed_bridge_capacity_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print('PASS 4 full marked plat sources through ten heads; 7 exact composed norms; unique angle optimizer; 5 growing coherent capacities')
