#!/usr/bin/env python3
"""Exact root checks for actual high-color blocks and retained braiding signs.

The characteristic-zero proof uses integral Weyl Gaussian coefficients;
these finite-field calculations independently test both crossing signs,
block carries and the literal original root state at larger colors.
"""

import json
from pathlib import Path

from audit_finite_sum_annihilator import field
from audit_cyclotomic_mellin_residue import integer, integral_ordinary_cut


def sign(k):
    return -1 if k % 2 else 1


def beta(N, block, index):
    return sign(N * block * (block - 1) // 2 + block * index)


def crossing(N, color, a, b, transfer, crossing_sign, p, q):
    """Literal integral-Weyl checked crossing, common half-Cartan stripped."""
    k = transfer
    n = color
    if crossing_sign > 0:
        if k > min(a, n - 1 - b):
            return None, 0
        low, high = a, b
        target = b + k, a - k
    else:
        if k > min(b, n - 1 - a):
            return None, 0
        low, high = b, a
        target = b - k, a + k
    ep = fp = factorial = 1
    for j in range(1, k + 1):
        ep = ep * integer(n - low + j - 1, p, q) % p
        fp = fp * integer(high + j, p, q) % p
        factorial = factorial * integer(j, p, q) % p
    rho = (q - pow(q, -1, p)) % p
    factor = ep * fp * pow(rho, k, p) * pow(factorial, -1, p)
    if crossing_sign > 0:
        exponent = k * (k - 1) // 2 - (n - 1) * (a + b) + 2 * (a - k) * (b + k)
    else:
        factor *= sign(k)
        exponent = -k * (k - 1) // 2 + (n - 1) * (a + b) - 2 * a * b
    return target, factor * pow(q, exponent, p) % p


def all_crossings():
    records = []
    total = 0
    nontrivial_phases = 0
    for N in range(2, 8):
        p, _, q = field(N)
        for r in range(1, N + 1):
            n = N * (r + 1)
            epsilon = sign(n - 1)
            count = 0
            for a in range(r + 1):
                for b in range(r + 1):
                    for s in range(N):
                        for t in range(N):
                            for cs in (1, -1):
                                for k in range(N):
                                    target, raw = crossing(N, n, a*N+s, b*N+t, k, cs, p, q)
                                    # Small W has the same highest H, ordinary E=(-1)^r E_St.
                                    small_target, small = crossing(N, N, s, t, k, cs, p, q)
                                    if small_target is None:
                                        assert raw == 0
                                        continue
                                    # Retain W's highest-weight Cartan, rather than replacing by St.
                                    small = small * sign(r*k) * pow(q, cs*(-N*r*(s+t)), p) % p
                                    expected = small * pow(epsilon, a+b, p) % p
                                    out0, out1 = target
                                    gauge = (beta(N,a,s)*beta(N,b,t)
                                             *beta(N,out0//N,out0%N)*beta(N,out1//N,out1%N))
                                    actual = raw*gauge % p
                                    assert actual == expected, (N,r,a,b,s,t,cs,k,actual,expected)
                                    assert (out0//N,out1//N) == (b,a)
                                    if expected and pow(epsilon,a+b,p) != 1:
                                        nontrivial_phases += 1
                                    count += 1
            records.append({'level':N,'frobenius_degree':r,'actual_color':n,
                            'both_signed_crossing_entries':count})
            total += count
    assert nontrivial_phases
    return {'records':records,'checked_entries':total,
            'nontrivial_half_braiding_signs_retained':nontrivial_phases}


def actual_large_color_periods():
    records=[]
    diagrams=[(2,[(0,1)]*3),(3,[(0,1),(1,-1)]*2)]
    for N in range(2,5):
        p,_,q=field(N)
        for strands,word in diagrams:
            baseline=integral_ordinary_cut(N,N,p,q,strands,word)
            for r in (1,N):
                n=N*(r+1)
                got=integral_ordinary_cut(N,n,p,q,strands,word)
                assert got == baseline,(N,n,strands,got,baseline)
                records.append({'level':N,'actual_color':n,'strands':strands,
                                'crossings':len(word),'original_reduced_period_retained':True})
    return records


def main():
    result={'actual_high_color_crossing_factorization':all_crossings(),
            'original_knot_period_at_actual_high_colors':actual_large_color_periods(),
            'scope':'Actual root high-color realization; no off-root equivalence or framing-current map inferred.'}
    path=Path(__file__).with_name('frobenius_high_color_braiding_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,
                      'crossing_entries':result['actual_high_color_crossing_factorization']['checked_entries'],
                      'actual_large_color_periods':len(result['original_knot_period_at_actual_high_colors']),
                      'output':str(path)},indent=2))


if __name__=='__main__':
    main()
