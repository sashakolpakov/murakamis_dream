#!/usr/bin/env python3
"""Exact finite-field audits for the charged star's retained defect polynomial."""

import itertools
import json
from pathlib import Path

from audit_actual_hardy_cauchy_network import HardyNetwork


def trim(P, p):
    return {m: c % p for m, c in P.items() if c % p}


def mul(P, R, p):
    out = {}
    for m, c in P.items():
        for n, t in R.items():
            k = tuple(a+b for a, b in zip(m, n))
            out[k] = (out.get(k, 0)+c*t) % p
    return trim(out, p)


def order(m):
    return m[1], m[2], m[0]


def divide(P, D, p):
    work, result = dict(P), {}
    leading = max(D, key=order)
    inverse = pow(D[leading], -1, p)
    while work:
        term = max(work, key=order)
        shift = tuple(a-b for a, b in zip(term, leading))
        assert min(shift) >= 0, (term, leading)
        coefficient = work[term]*inverse % p
        result[shift] = (result.get(shift, 0)+coefficient) % p
        for m, c in D.items():
            n = tuple(a+b for a, b in zip(m, shift))
            work[n] = (work.get(n, 0)-coefficient*c) % p
            if not work[n]:
                del work[n]
    return trim(result, p)


def qbinom(H, a, b):
    if b < 0 or b > a:
        return 0
    return H.fac[a]*pow(H.fac[b]*H.fac[a-b] % H.p, -1, H.p) % H.p


def star(H, lengths):
    d, p, Q = H.N-1, H.p, H.Q
    out = {}
    for r0 in range(lengths[0]+1):
        for r1 in range(lengths[1]+1):
            r2 = d-r0-r1
            if not 0 <= r2 <= lengths[2]:
                continue
            rs = (r0, r1, r2)
            monomial = tuple(L-r for L, r in zip(lengths, rs))
            coefficient = pow(-1, d, p)
            for L, r in zip(lengths, rs):
                coefficient = coefficient*pow(Q, r*(r-1)//2, p)*qbinom(H, L, r) % p
            out[monomial] = coefficient
    return trim(out, p)


def delta(H, lengths):
    d, p, Q = H.N-1, H.p, H.Q
    e = 2*d-sum(lengths)
    ks = [d-L for L in lengths]
    aa = [k-e for k in ks]
    result = {(0, 0, 0): 1}
    for i, j, third in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        for r in range(aa[third]):
            left, right = [0]*3, [0]*3
            left[i], right[j] = 1, 1
            result = mul(result, {tuple(left): 1, tuple(right): -pow(Q, ks[j]+1+r, p)}, p)
    return result


def marked(H, lengths):
    d, p, Q = H.N-1, H.p, H.Q
    e = 2*d-sum(lengths)
    ks = [d-L for L in lengths]
    a3 = ks[2]-e
    T = lambda n: n*(n-1)//2
    exponent = T(lengths[0])+T(ks[0])-(ks[1]+1)*a3-T(a3)
    return pow(-1, d-a3, p)*pow(Q, exponent, p)*qbinom(H, lengths[2], ks[0]) % p


def formal_rectangle_check(H, lengths, F, D, R):
    """Independently recover the quotient from the norm proof's a,b chart."""
    d, p = H.N-1, H.p
    e = 2*d-sum(lengths)
    k = [d-L for L in lengths]
    a2 = k[1]-e
    lead = max(D, key=order)
    invlead = pow(D[lead], -1, p)
    FF, DD = {}, {}
    for destination, source in ((FF, F), (DD, D)):
        for m, c in source.items():
            index = (m[0], m[0]+m[2]-a2)
            assert min(index) >= 0
            destination[index] = c*invlead % p
    assert DD.get((0, 0)) == 1
    inverse = {(0, 0): 1}
    for total in range(1, 2*e+1):
        for i in range(e+1):
            j = total-i
            if not 0 <= j <= e:
                continue
            value = sum(c*inverse.get((i-a, j-b), 0)
                        for (a, b), c in DD.items() if a+b and a <= i and b <= j)
            inverse[i, j] = -value % p
    expected = {(m[0], m[0]+m[2]): c for m, c in R.items()}
    for i in range(e+1):
        for j in range(e+1):
            value = sum(FF.get((a, b), 0)*inverse.get((i-a, j-b), 0)
                        for a in range(i+1) for b in range(j+1)) % p
            assert value == expected.get((i, j), 0)
            # Direct formula for the coefficients whose magnitudes are bounded.
            rs = (lengths[0]-i, j, k[0]-j+i)
            direct = 0
            if all(0 <= r <= L for r, L in zip(rs, lengths)):
                direct = pow(-1, d, p)*invlead % p
                for L, r in zip(lengths, rs):
                    direct = direct*pow(H.Q, r*(r-1)//2, p)*qbinom(H, L, r) % p
            assert direct == FF.get((i, j), 0)


def main():
    rows = []
    for N in range(2, 13):
        H = HardyNetwork(N, 1)
        d, cases, balanced, defective = N-1, 0, 0, 0
        defects, max_terms = set(), 0
        for lengths in itertools.product(range(N), repeat=3):
            if sum(lengths) > 2*d or any(lengths[i]+lengths[j] < d for i, j in ((0, 1), (1, 2), (2, 0))):
                continue
            e = 2*d-sum(lengths)
            F, D = star(H, lengths), delta(H, lengths)
            R = divide(F, D, H.p)
            assert mul(D, R, H.p) == F
            assert all(sum(m) == e for m in R)
            assert R.get((0, e, 0)) == marked(H, lengths) != 0
            formal_rectangle_check(H, lengths, F, D, R)
            # The nonzero marked coefficient is also the lex leading term.
            assert max(R, key=order) == (0, e, 0)
            if e == 0:
                k1, k2, k3 = [d-L for L in lengths]
                C = pow(-1, k1+k3, H.p)*pow(H.Q, k1*(k1-1)//2+k3*(k3-1)//2-k2, H.p)*qbinom(H, d-k2, k3) % H.p
                assert R == {(0, 0, 0): C}
                balanced += 1
            else:
                defective += 1
            # Arbitrary invertible coefficients on the three Z incidences.
            scales = (2, 3, 5)
            scalar = 1
            for t, L in zip(scales, lengths):
                scalar = scalar*pow(t, L, H.p) % H.p
            def rescale(P, overall):
                result = {}
                for m, c in P.items():
                    value = overall*c
                    for t, exponent in zip(scales, m):
                        value = value*pow(t, -exponent, H.p) % H.p
                    result[m] = value % H.p
                return trim(result, H.p)
            assert mul(rescale(D, 1), rescale(R, scalar), H.p) == rescale(F, scalar)
            cases += 1
            defects.add(e)
            max_terms = max(max_terms, len(R))
        rows.append({'N': N, 'all_admissible_ordered_length_triples': cases,
                     'balanced_cases': balanced, 'nonzero_defect_cases': defective,
                     'defects_checked': sorted(defects), 'largest_residual_support': max_terms,
                     'independent_formal_rectangle_and_shifted_index_checks': True})
    output = {'status': 'PASS', 'rows': rows,
              'scope': 'All displayed exact polynomial identities and the norm proof coefficient chart; growing-defect norm bound proved analytically, no global source noncancellation inferred.'}
    Path(__file__).with_name('charged_star_triangle_defect_jets_results.json').write_text(json.dumps(output, indent=2)+'\n')
    print('PASS all admissible ordered stars N=2..12, exact triangle division, marked scalar and arbitrary incidence rescaling')


if __name__ == '__main__':
    main()
