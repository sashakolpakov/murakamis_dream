#!/usr/bin/env python3
"""Uniform actual closed trace route in the full physical Pascal alphabet."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_reassociation_angle_kernel import actual_divided_fusion
from audit_actual_two_cut_ports import word_matrix, partial


def field_case(r):
    N, d = 3*r+1, 3*r
    H = HardyNetwork(N, 1)
    p, Q, x = H.p, H.Q, H.x
    C, Ci = actual_divided_fusion(H, x)
    flip = np.zeros((N*N, N*N), dtype=np.int64)
    for a in range(N):
        for b in range(N):
            flip[b*N+a, a*N+b] = 1
    C21, C21i = flip@C@flip % p, flip@Ci@flip % p
    D = np.diag([pow(-1,b,p)*pow(Q,b*(b-1)//2,p)*pow(x,-2*b,p) % p
                 for a in range(N) for b in range(N)])
    Di = np.diag([pow(int(t),-1,p) for t in np.diag(D)])
    assert np.array_equal(H.kappa*C@D % p@C21 % p@Ci % p, H.plus)
    assert np.array_equal(pow(H.kappa,-1,p)*C@C21i % p@Di % p@Ci % p, H.minus)
    route_count = 0
    for pair in [(2*r,r),(r,2*r)]:
        for sign in [1,-1]:
            middle = C21 if sign>0 else C21i
            states = ([pair,(r,2*r),(2*r,r),pair] if pair[0]==2*r
                      else [pair,pair,(2*r,r),pair])
            value = 1
            for gate, before, after in zip([Ci,middle,C],states,states[1:]):
                factor = int(gate[after[0]*N+after[1],before[0]*N+before[1]])
                assert factor
                value = value*factor % p
            diagonal_state = states[2] if sign>0 else states[1]
            diagonal = D if sign>0 else Di
            value = value*int(diagonal[diagonal_state[0]*N+diagonal_state[1],
                                     diagonal_state[0]*N+diagonal_state[1]]) % p
            value = value*(H.kappa if sign>0 else pow(H.kappa,-1,p)) % p
            assert value
            # Some nonzero expanded routes cancel already inside one R.
            if (sign>0 and pair[0]==r) or (sign<0 and pair[0]==2*r):
                matrix = H.plus if sign>0 else H.minus
                assert int(matrix[pair[0]*N+pair[1],pair[0]*N+pair[1]]) == 0
            route_count += 1

    source_checked = False
    if N<=7:
        word = [1,-2,1,-2]
        full = word_matrix(word,H.plus,H.minus,3,N,p)
        cut = partial(full,H.pivot,3,N,p)
        assert np.array_equal(cut,np.diag(np.diag(cut)))
        literal_marked = int(np.sum(cut))*pow(N,-1,p) % p
        averaged_trace = int(np.trace(cut))*pow(N,-1,p) % p
        assert literal_marked == averaged_trace
        state = (2*r,r,2*r)
        pivotal_weight = pow(N,-1,p)
        for a in state[1:]:
            pivotal_weight = pivotal_weight*int(H.pivot[a]) % p
        assert pivotal_weight
        source_checked = True
    return {'r':r,'N':N,'full_original_signed_crossings':True,
            'nonzero_signed_net_identity_routes':route_count,
            'literal_marked_vs_averaged_trace':source_checked}


def metric_case(r):
    N,d = 3*r+1,3*r
    q = mp.exp(mp.j*mp.pi/N)
    Q,x = q*q,-1/q
    F,s = [mp.mpc(1)],[mp.mpf(1)]
    for a in range(1,N):
        F.append(F[-1]*(1-Q**a))
        s.append(abs(F[-1]))
    g = [mp.root(N,4)/mp.sqrt(t) for t in s]
    w = 1/s[r]**3
    beta = lambda L,t:F[L]/(F[t]*F[L-t])
    route_energy = []
    for high_first in [True,False]:
        pair = (2*r,r) if high_first else (r,2*r)
        transfers = [r,r,0] if high_first else [0,r,r]
        for sign in [1,-1]:
            state = pair
            energy = mp.mpf(1)
            regular = 0
            for stage,t in enumerate(transfers):
                inverse = stage==0 or (stage==1 and sign<0)
                a,b = state if stage!=1 else state[::-1]
                assert 0<=t<=min(a,d-b)
                raw = x**(-t)*beta(b+t,t)
                if inverse:
                    raw *= (-1)**t*Q**(t*(t-1)//2)
                out = (a-t,b+t)
                weighted = raw*g[out[0]]*g[out[1]]/(g[a]*g[b])
                cells = [(t,a-t,d-a),(t,b,d-b-t)]
                assert all(sum(z)==d and min(z)>=0 for z in cells)
                if t:
                    assert cells == [(r,r,r),(r,r,r)]
                    regular += 2
                predicted = N*N/mp.fprod(s[k] for z in cells for k in z)
                assert abs(abs(weighted)**2/predicted-1)<mp.mpf('1e-75')
                energy *= abs(weighted)**2
                state = out if stage!=1 else out[::-1]
            assert state==pair and regular==4
            assert abs(energy/(N**4*w**4)-1)<mp.mpf('1e-75')
            route_energy.append(energy)
    return {'r':r,'N':N,'all_four_signed_oriented_routes':True,
            'squared_one_crossing_route':mp.nstr(route_energy[0],24),
            'rate_per_crossing':mp.nstr(mp.log(route_energy[0])/N,18)}


def main():
    mp.mp.dps = 100
    result = {'status':'PASS','independent_original_operators':[field_case(r) for r in [1,2,3]],
              'actual_quarter_metric_routes':[metric_case(r) for r in range(1,13)],
              'scope':'Phase-free expanded C-path source only; no surviving coherent-sector or geometric-bound claim.'}
    Path(__file__).with_name('actual_closed_pascal_route_energy_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS 3 original full signed levels/12 closed route orders; '
          '2 original whole-source trace comparisons; 48 exact quarter-metric routes')


if __name__=='__main__':
    main()
