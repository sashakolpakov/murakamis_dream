#!/usr/bin/env python3
"""Own generic Euler identities and tests of the separate Racah target.

The double-sum/Euler-moment and bilinear identities have finite proofs in
the note. Candidate single-sum comparisons are tests, not that missing proof.
"""
import itertools
import json
from pathlib import Path

from audit_actual_generic_six_head_tetrahedral_source import Generic


def poly_mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] = (out[i+j]+x*y) % p
    return out


def euler(start, length, Q, p):
    out = [1]
    for i in range(length): out = poly_mul(out, [1, -start*pow(Q, i, p) % p], p)
    return out


def gaussian(n, k, Q, p):
    if not 0 <= k <= n: return 0
    out = 1
    for i in range(1, k+1): out = out*(1-pow(Q, n-k+i, p))*pow(1-pow(Q, i, p), -1, p) % p
    return out


def bilinear_cases():
    p, Q = 1000003, 4
    count = 0
    for m, n, V in itertools.product(range(8), range(8), (1, 7, pow(Q, 11, p))):
        actual = poly_mul(euler(1, m, Q, p), euler(V, n, Q, p), p)
        expected = [0]*(m+n+1)
        for k in range(n+1):
            coefficient = pow(Q, k*(k-1)//2, p)*gaussian(n, k, Q, p) % p
            for s in range(k): coefficient = coefficient*(pow(Q, m-s, p)-V) % p
            for i, v in enumerate(euler(1, m+n-k, Q, p)):
                expected[k+i] = (expected[k+i]+coefficient*v) % p
        assert actual == expected
        count += 1
    return count


def moment(g, a, n):
    d, Q, p, f = g.d, g.Q, g.p, g.fac
    return sum(pow(Q, (a+1+n)*k, p)*f[d-k]*f[a+k]
               * pow(f[d-a-k]*f[k], -1, p) for k in range(d-a+1)) % p


def moment_coefficient(g, a, n):
    """F_a²[z^(d-a)](zQ^(a+1))_n/(z)_(2a+2+n)."""
    Q, p, degree = g.Q, g.p, g.d-a
    numerator = euler(pow(Q, a+1, p), n, Q, p)
    coefficients = [1]+[0]*degree
    for s in range(2*a+2+n):
        v = pow(Q, s, p)
        for k in range(1, degree+1): coefficients[k] = (coefficients[k]+v*coefficients[k-1]) % p
    value = sum(numerator[j]*coefficients[degree-j] for j in range(min(degree, n)+1)) % p
    return g.fac[a]**2*value % p


def source_euler(g, js):
    a, b, c = js
    d, q, Q, p, f = g.d, g.q, g.Q, g.p, g.fac
    r, r1 = b+c-a, a+b-c
    coefficients = poly_mul(euler(1, b, Q, p), euler(pow(Q, g.N, p), b, Q, p), p)
    total = 0
    for e in range(r+1):
        total += coefficients[e]*pow(Q, -c*e, p)*f[2*b-e]*pow(f[r-e], -1, p)*moment(g, a, r-e)
    exponent = (2*a*a-b*b+3*c*c-2*a*c+2*b*c
                -d*(a+b+2*c+1)+b+c)
    return ((-1)**(d+b-c)*pow(q, exponent, p)*total
            * pow(f[a]*f[b]*f[c]*f[r1], -1, p)) % p


def qfact(g, n):
    return pow(g.q, -n*(n-1)//2, g.p)*g.fac[n]*pow(1-g.Q, -n, g.p) % g.p


def pochhammer(start, length, Q, p):
    value = 1
    for i in range(length): value = value*(1-start*pow(Q, i, p)) % p
    return value


def residual_source_polynomial(g, js):
    a, b, c = js
    r, J = b+c-a, sum(js)
    p, Q, f = g.p, g.Q, g.fac
    result = [0]*(r+1)
    A = pow(Q, a+1, p)
    for e in range(r+1):
        ce = [0]*(e+1)
        for u in range(e+1):
            v = e-u
            if max(u, v) > b: continue
            ce[u] = ((-1)**e*pow(Q, u*(u-1)//2+v*(v-1)//2, p)
                     *gaussian(b, u, Q, p)*gaussian(b, v, Q, p)) % p
        n = r-e
        hn = [gaussian(n, t, Q, p)*pochhammer(A, t, Q, p)
              *pochhammer(A, n-t, Q, p) % p for t in range(n+1)]
        weight = pow(Q, -c*e, p)*f[2*b-e]*pow(f[n]*f[J+1-e], -1, p) % p
        for k, value in enumerate(poly_mul(ce, hn, p)):
            result[k] = (result[k]+weight*value) % p
    return result


def residual_target_polynomial(g, js):
    a, b, c = js
    r, r1, J = b+c-a, a+b-c, sum(js)
    p, Q, f = g.p, g.Q, g.fac
    result = [0]*(r+1)
    outside = pow(Q, b*r, p)*f[b]**2*f[c]**2*f[r1]*pow(f[J+1], -1, p) % p
    for k in range(r+1):
        denominator = f[k]*f[a-b+k]*f[a-c+k]*f[b-k]*f[c-k]*f[r-k]
        weight = (outside*(-1)**k*pow(Q, 3*k*(k-1)//2+(a-2*b-2*c+1)*k, p)
                  *pow(denominator, -1, p)) % p
        term = poly_mul(euler(pow(Q, -a-r+k, p), r-k, Q, p),
                        euler(pow(Q, a+1, p), k, Q, p), p)
        for j, value in enumerate(term): result[j] = (result[j]+weight*value) % p
    return result


def candidate_racah(g, js):
    a, b, c = js
    d, p, J = g.d, g.p, sum(js)
    total = 0
    for z in range(max(J, d+a, d+b, d+c), min(d+a+b, d+a+c, d+b+c)+1):
        denominator = qfact(g, z-J)
        for j in js: denominator = denominator*qfact(g, z-d-j) % p
        for j, k in ((a, b), (a, c), (b, c)):
            denominator = denominator*qfact(g, d+j+k-z) % p
        total += (-1)**z*qfact(g, z+1)*pow(denominator, -1, p)
    exponent = a*a-b*b+c*c-a*b-a*c+b*c-c*d
    return ((-1)**J*pow(g.q, exponent, p)*total
            *qfact(g, a)*qfact(g, b)*qfact(g, c)*pow(qfact(g, J+1), -1, p)) % p


def level(N):
    g = Generic(N)
    count = 0
    moment_count = 0
    polynomial_count = 0
    for a in range(N):
        for n in range(2*g.d+1):
            assert moment(g, a, n) == moment_coefficient(g, a, n)
            moment_count += 1
    for js in itertools.product(range(N), repeat=3):
        a, b, c = js
        if min(b+c-a, a+b-c, a+c-b) < 0: continue
        actual = g.regular_corner_sum(js)
        assert source_euler(g, js) == actual, (N, js, 'proved Euler moment')
        assert candidate_racah(g, js) == actual, (N, js, 'candidate single-sum test')
        if a == max(js):
            src = residual_source_polynomial(g, js)
            tgt = residual_target_polynomial(g, js)
            assert src == list(reversed(src)), (N, js, 'proved reciprocity')
            X = pow(g.Q, N, g.p)
            value = sum(v*pow(X, k, g.p) for k, v in enumerate(src)) % g.p
            exponent = (2*a*a-b*b+3*c*c-2*a*c+2*b*c
                        -g.d*(a+b+2*c+1)+b+c)
            outside = ((-1)**(g.d+b-c)*pow(g.q, exponent, g.p)*g.fac[a]
                       *pow(g.fac[b]*g.fac[c]*g.fac[a+b-c], -1, g.p)) % g.p
            reconstructed = outside*pochhammer(X*pow(g.Q, -a, g.p)%g.p, 2*a+1, g.Q, g.p)*value % g.p
            assert reconstructed == actual, (N, js, 'proved source polynomial normalization')
            x0 = pow(g.Q, b, g.p)
            first = sum(v*pow(x0, k, g.p) for k, v in enumerate(src)) % g.p
            r = b+c-a
            first_target = (g.fac[2*b]*pow(g.fac[sum(js)+1], -1, g.p)
                            *pow(g.Q, b*r, g.p)*gaussian(c, r, g.Q, g.p)
                            *pochhammer(pow(g.Q, -b-c, g.p), r, g.Q, g.p)) % g.p
            assert first == first_target, (N, js, 'proved first interpolation')
            assert src == tgt, (N, js, 'UNPROVED target polynomial comparison')
            polynomial_count += 1
        count += 1
    return {'N': N, 'proved_generic_source_Euler_moment_checks': count,
            'proved_finite_generating_function_moments': moment_count,
            'proved_source_polynomial_reciprocity_normalization_and_first_interpolation': polynomial_count,
            'candidate_full_polynomial_equality_checks_NOT_a_proof': polynomial_count,
            'candidate_single_Racah_sum_checks_NOT_a_proof': count}


if __name__ == '__main__':
    rows = [level(N) for N in range(2, 10)]
    out = {'status': 'PASS', 'generic_bilinear_Euler_identity_checks': bilinear_cases(),
           'all_partner_source_families': rows,
           'scope': 'Finite proof and exact tests for generic bilinear Euler linearization and source Euler-moment reduction. The actual-source-to-single-Racah identity remains a separate unproved target; exact comparisons are not its proof.'}
    Path(__file__).with_name('generic_trivalent_bilinear_racah_port_results.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', len(rows), 'generic all-partner Euler-moment families;',
          out['generic_bilinear_Euler_identity_checks'], 'bilinear identities; candidate Racah comparisons explicitly not proof')
