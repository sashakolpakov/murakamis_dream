#!/usr/bin/env python3
"""Actual ordinary-cap trees: complete phases, one-simplex energy and overlaps."""

import itertools
import json
from functools import lru_cache
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_reassociation_angle_kernel import actual_divided_fusion


@lru_cache(None)
def trees(length, start=0):
    if length==1:
        return (start,)
    return tuple((left,right) for cut in range(1,length)
                 for left in trees(cut,start)
                 for right in trees(length-cut,start+cut))


def node_indices(tree, values):
    if isinstance(tree,int):
        return values[tree], []
    a,left = node_indices(tree[0],values)
    c,right = node_indices(tree[1],values)
    return a+c, left+right+[(a,c)]


def actual_node_field(N):
    H = HardyNetwork(N,1)
    p,Q,x,d = H.p,H.Q,H.x,N-1
    C,Ci = actual_divided_fusion(H,x)
    A = np.kron(np.eye(N,dtype=np.int64),Ci)@np.kron(C,np.eye(N,dtype=np.int64)) % p
    K = np.zeros((N,N**3),dtype=np.int64)
    for u in range(N):
        ell = pow(x*Q % p,-u,p)*pow(N,-1,p) % p
        for n in range(N):
            K[n,:] = (K[n,:]+ell*A[(u*N+d-u)*N+n,:]) % p
    count = 0
    for a,b,c in itertools.product(range(N),repeat=3):
        column = (a*N+b)*N+c
        for n in range(N):
            predicted = 0
            if b==d and n==a+c and n<=d:
                phase = pow(-1,a,p)*pow(Q,a*(a-1)//2,p) % p
                predicted = (pow(N,-1,p)*phase*H.fac[n]
                             *pow(H.fac[a]*H.fac[c] % p,-1,p)) % p
            assert int(K[n,column]) == predicted
            count += 1
    tree_entries = 0
    for length in range(1,5):
        for tree in trees(length):
            for values in itertools.product(range(N),repeat=length):
                n,nodes = node_indices(tree,values)
                if n>d:
                    continue
                direct,predicted = 1,pow(N,-(length-1),p)*H.fac[n] % p
                for a,c in nodes:
                    direct = direct*int(K[a+c,(a*N+d)*N+c]) % p
                    predicted = predicted*pow(-1,a,p)*pow(Q,a*(a-1)//2,p) % p
                for a in values:
                    predicted = predicted*pow(H.fac[a],-1,p) % p
                assert direct == predicted
                tree_entries += 1
    return {'N':N,'literal_cap_reassociation_entries':count,
            'complete_tree_phase_entries':tree_entries}


def metric_tree_case(N,length):
    q = mp.exp(mp.j*mp.pi/N)
    d = N-1
    s = [mp.mpf(1)]
    for a in range(1,N):
        s.append(s[-1]*2*mp.sin(mp.pi*a/N))
    allowed = [x for x in itertools.product(range(N),repeat=length) if sum(x)<=d]
    all_trees = trees(length)
    rows_by_tree = []
    E = [mp.mpf(0)]*N
    for values in allowed:
        n = sum(values)
        E[n] += N**mp.mpf(-(length-1))*s[n]/mp.fprod(s[a] for a in values)
    for tree in all_trees:
        rows = [dict() for _ in range(N)]
        for values in allowed:
            n,nodes = node_indices(tree,values)
            direct = mp.mpc(1)
            theta = 0
            for a,c in nodes:
                direct *= q**(a*(a+c-N-1))/mp.sqrt(s[a]*s[c]*s[d-a-c])
                theta += a*(a+c-N-1)
            target = (N**mp.mpf(-(length-1)/2)
                      *mp.sqrt(s[n]/mp.fprod(s[a] for a in values))*q**theta)
            assert abs(direct/target-1)<mp.mpf('1e-70')
            angle = (d-n,)+values
            assert sum(angle)==d and min(angle)>=0
            target_energy = N**mp.mpf(2-length)/mp.fprod(s[a] for a in angle)
            assert abs(abs(direct)**2/target_energy-1)<mp.mpf('1e-70')
            rows[n][values] = direct
        for n,row in enumerate(rows):
            energy = mp.fsum(abs(z)**2 for z in row.values())
            assert abs(energy/E[n]-1)<mp.mpf('1e-70')
        rows_by_tree.append(rows)
    hs = mp.fsum(E)
    Z = mp.fsum(1/(s[d-sum(values)]*mp.fprod(s[a] for a in values))
                for values in allowed)
    assert abs(hs/(N**mp.mpf(2-length)*Z)-1)<mp.mpf('1e-70')
    # Full mixed sums, not a diagonal-leaf replacement.
    minimum_overlap = mp.mpf(1)
    first,last = rows_by_tree[0],rows_by_tree[-1]
    for n in range(N):
        mixed = mp.fsum(first[n][a]*mp.conj(last[n][a]) for a in first[n])/E[n]
        assert abs(mixed)<=1+mp.mpf('1e-70')
        minimum_overlap = min(minimum_overlap,abs(mixed))
    # Specified arbitrary root co-source norm, retained exactly.
    z = [mp.exp(mp.j*(n*n+1)/7)*(n+1) for n in range(N)]
    actual = mp.fsum(abs(z[n]*value)**2 for n,row in enumerate(first) for value in row.values())
    predicted = mp.fsum(abs(z[n])**2*E[n] for n in range(N))
    assert abs(actual/predicted-1)<mp.mpf('1e-70')
    return {'N':N,'leaves':length,'tree_shapes':len(all_trees),
            'supported_angle_compositions':len(allowed),
            'HS_energy':mp.nstr(hs,18),
            'smallest_extreme_tree_normalized_overlap':mp.nstr(minimum_overlap,12),
            'full_mixed_phase_overlap_and_root_source':True}


def main():
    mp.mp.dps = 95
    result = {'status':'PASS','actual_literal_nodes_and_trees':[actual_node_field(N) for N in range(2,7)],
              'complete_coherent_tree_metrics':[metric_tree_case(N,l) for N in [2,4,7,10] for l in range(1,6)],
              'scope':'All ordinary-cap binary trees and their compressed boundary overlaps; no complete-channel interior or whole-knot bound.'}
    Path(__file__).with_name('actual_cap_tree_angle_energy_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS 5 literal original cap/reassociation levels and complete tree phases; '
          '20 all-shape metric/simplex/overlap/source families')


if __name__=='__main__':
    main()
