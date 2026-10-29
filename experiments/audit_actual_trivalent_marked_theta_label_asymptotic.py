#!/usr/bin/env python3
"""Exact twist/fold algebra and coherent whole-label asymptotic checks.

The original marked source identity is proved/audited separately in
audit_actual_trivalent_all_channel_marked_contraction.py.
"""
import functools
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


def exact_phase_and_fold():
    count = 0
    for N in range(2,129):
        d = N-1
        m = Fraction(d,2)
        unfolded = Counter()
        for j in range(d//2+1):
            h = m-j
            ew = Fraction(d*d,2)+N*j+j*(j+1)
            eo = Fraction(d*d,2)+N*m+m*(m+1)+N*d
            difference = ew-eo-h*h
            assert difference == -2*N*(d-j)
            assert difference/(2*N) == j-d
            if h==0:
                unfolded[h] += 1
            else:
                unfolded[h] += 1
                unfolded[-h] += 1
            count += 1
        expected = Counter({-m+k:1 for k in range(d+1)})
        assert unfolded == expected
    return {'exact_rational_root_phase_checks':count,'integer_and_half_integer_fold_families':127}


def symbolic_action():
    x,y,z,t = sp.symbols('x y z t', real=True)
    rows = [(x-y-z)/2,(-x+y-z)/2,(-x-y+z)/2,(x+y+z)/2]
    assert sp.expand(sum(v*v for v in rows)-x*x-y*y-z*z)==0
    row_vectors = [(1,-1,-1),(-1,1,-1),(-1,-1,1),(1,1,1)]
    canonical = lambda v:min(tuple(v),tuple(-w for w in v))
    original = Counter(canonical(v) for v in row_vectors)
    for axis in range(3):
        assert original == Counter(canonical(tuple(-w if i==axis else w for i,w in enumerate(v))) for v in row_vectors)
    sn,cs = sp.sin(sp.pi*t),sp.cos(sp.pi*t)
    assert sp.trigsimp(sp.cancel(cs/sn+sn/cs-1/(sn*cs)))==0
    return {'separate_evenness_and_joint_Hessian':True,'strict_one_angle_concavity_identity':True}


def level(N):
    d,M,m = N-1,(N-1)//2,mp.mpf(N-1)/2
    sine = [mp.mpf(1)]
    for r in range(1,N):sine.append(sine[-1]*2*mp.sin(mp.pi*r/N))
    @functools.lru_cache(None)
    def core(labels):
        J = sum(labels)
        R = sum(sine[t]*sine[J-t]/mp.fprod(sine[t-j]*sine[J-j-t] for j in labels)
                for t in range(max(labels),J-max(labels)+1))
        return N*N*mp.fprod(sine[J-2*j] for j in labels)/sine[J-d]*R*R
    exponents = [(0,0,0),(1,-2,3),(5,7,9),(-5,-7,-9)]
    sums = [mp.mpc(0) for _ in exponents]
    count = 0
    for labels in itertools.product(range(M+1),repeat=3):
        if sum(labels)<d:continue
        weight = core(tuple(sorted(labels)))*mp.fprod(1 if 2*j==d else 2 for j in labels)
        assert weight>0
        h2 = [(m-j)**2 for j in labels]
        for index,es in enumerate(exponents):
            # Exact preceding phase proof retains/factors the literal Omega_N^sum e.
            sums[index] += weight*mp.exp(1j*mp.pi/N*sum(e*h for e,h in zip(es,h2)))
        count += 1
    j0 = 4*mp.catalan/mp.pi
    result = []
    for es,actual in zip(exponents,sums):
        gaussian = mp.fprod(mp.sqrt(2-1j*e) for e in es)
        predicted = N**mp.mpf('1.5')*mp.exp(2*N*j0)/(16*gaussian)
        ratio = actual/predicted
        error = N*abs(ratio-1)
        assert error<12
        # Large all-positive twists exercise the nonprincipal determinant branch.
        if es==(5,7,9):
            assert abs(gaussian+mp.sqrt(mp.fprod(2-1j*e for e in es)))<mp.mpf('1e-40')
        result.append({'signed_edge_twists':es,'whole_source_normalized_ratio':[float(mp.re(ratio)),float(mp.im(ratio))],
                       'scaled_N_error':float(error),'product_individual_right_halfplane_roots':True})
    return {'N':N,'all_supported_physical_labels':count,'coherent_signed_whole_label_profiles':result}


def main():
    exact = exact_phase_and_fold()
    action = symbolic_action()
    with mp.workdps(55):
        rows = [level(N) for N in (32,33,64,65,128,129)]
    out = {'status':'PASS','exact_phase_and_folding':exact,'symbolic_action':action,
           'all_parity_complete_label_sums':rows,
           'scope':'Actual specified two-vertex marked source via the separately proved full-normal contraction. No arbitrary-graph energy or complement-volume identification.'}
    Path(__file__).with_name('actual_trivalent_marked_theta_label_asymptotic_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {exact["exact_rational_root_phase_checks"]} exact full-Cartan phase checks,127 parity folds, symbolic action,6 all-parity complete-label families/24 signed profiles')


if __name__=='__main__':
    main()
