#!/usr/bin/env python3
"""Source-exact whole Newton/Hadamard construction and selected-level checks.

No level is inferred to be geometric from the connectivity diagnostics.
The polynomial-mass theorem is proved in the accompanying note.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_regularized_kashaev_period import actual_laurent_period, evaluate


def trim(a, p):
    a = [int(x) % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p, scalar=1):
    out = list(a)+[0]*max(0, len(b)-len(a))
    for j, c in enumerate(b):
        out[j] = (out[j]+scalar*c) % p
    return trim(out, p)


def multiply(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for j, c in enumerate(a):
        for k, d in enumerate(b):
            out[j+k] = (out[j+k]+c*d) % p
    return trim(out, p)


def whole_newton(F, N, Q, p):
    degree = max(map(abs, F), default=0)
    assert all(F.get(k, 0) == F.get(-k, 0) for k in range(degree+1))
    H = [F.get(0, 0)]
    C0, C1 = [2], [0, 1]
    if degree:
        H = add(H, C1, p, F.get(1, 0))
    for k in range(2, degree+1):
        C0, C1 = C1, add([0]+C1, C0, p, -1)
        H = add(H, C1, p, F.get(k, 0))
    basis = [[1]]
    for n in range(1, degree+1):
        a = (pow(Q, n, p)+pow(Q, -n, p)) % p
        basis.append(multiply(basis[-1], [-a, 1], p))
    remainder = list(H)+[0]*max(0, degree+1-len(H))
    coeff = [0]*(degree+1)
    for n in range(degree, -1, -1):
        coeff[n] = remainder[n] % p
        for j, b in enumerate(basis[n]):
            remainder[j] = (remainder[j]-coeff[n]*b) % p
    assert not any(remainder)
    assert coeff[0] == 1
    return coeff, degree


def original_sources():
    rows = []
    cases = ((1, []), (2, [(0, 1)]), (2, [(0, 1)]*3),
             (3, [(0, 1), (1, -1)]*2),
             (3, [(0, 1)]*3+[(1, 1), (0, -1), (1, 1)]))
    for N in range(2, 7):
        p, _, q = field(N)
        Q = q*q % p
        for strands, word in cases:
            F = actual_laurent_period(N, p, q, strands, word)
            coeff, whole_degree = whole_newton(F, N, Q, p)
            A = trim((coeff+[0]*N)[:N], p)
            w = [1]
            for n in range(1, N):
                w.append(w[-1]*(2-pow(Q, n, p)-pow(Q, -n, p)) % p)
            assert w[-1] == N*N % p
            W = list(reversed(w))
            P = multiply(A, W, p)
            assert P[0] == N*N % p
            assert len(P)-1 == N-1+len(A)-1
            actual_K = evaluate(F, 1, p)
            assert P[N-1] == actual_K
            for j in range(N):
                Y = pow(Q, j, p)
                h = (Y+pow(Y, -1, p)) % p
                val, t = 0, 1
                for n, a in enumerate(A):
                    val = (val+a*t) % p
                    t = t*(h-pow(Q, n+1, p)-pow(Q, -n-1, p)) % p
                assert val == evaluate(F, Y, p)
            if len(A) == 1:
                assert actual_K == 1
            rows.append({'N': N, 'braid_width': strands, 'word': word,
                         'whole_meridian_degree': whole_degree,
                         'truncated_Newton_degree': len(A)-1,
                         'one_pole_case': len(A) == 1,
                         'all_original_root_color_values_preserved': True,
                         'Hadamard_coefficient_original_K': actual_K,
                         'known_constant_polynomial_coefficient': N*N % p})
    return rows


def selected_positive_prototypes():
    rows = []
    for N in (4, 8, 12, 20, 32, 64):
        w = [mp.mpf(1)]
        for k in range(1, N):
            w.append(w[-1]*4*mp.sin(mp.pi*k/N)**2)
        # Figure-eight A_N=1+...+z^d, exact ORIGINAL source identity.
        def master(rho):
            return mp.fsum(mp.exp(n*rho) for n in range(N))*mp.fsum(
                w[n]*mp.exp(-n*rho) for n in range(N))
        def derivative(rho):
            A = mp.fsum(mp.exp(n*rho) for n in range(N))
            Ap = mp.fsum(n*mp.exp(n*rho) for n in range(N))
            B = mp.fsum(w[n]*mp.exp(-n*rho) for n in range(N))
            Bp = mp.fsum(-n*w[n]*mp.exp(-n*rho) for n in range(N))
            return Ap/A+Bp/B
        low, high = mp.mpf(-5), mp.mpf(5)
        assert derivative(low) < 0 < derivative(high)
        for _ in range(200):
            middle = (low+high)/2
            if derivative(middle) < 0:
                low = middle
            else:
                high = middle
        rho = (low+high)/2
        Rsep = master(rho)
        K = mp.fsum(w)
        assert Rsep <= N*K*(1+mp.mpf('1e-50'))
        rows.append({'N': N, 'positive_selected_critical_log_radius': float(rho),
                     'selected_level_log_rate': float(mp.log(Rsep)/N),
                     'original_K_log_rate': float(mp.log(K)/N),
                     'Rsep_over_N_K': float(Rsep/(N*K)),
                     'scope': 'Positive-coefficient prototype only; no general positivity claimed.'})
    # Exact example in which the largest critical modulus is inaccessible
    # to this source-selected threshold.
    z = sp.Symbol('z')
    f = 1/z+sp.Rational(91, 100)*z+sp.Rational(9, 200)*z*z
    assert sp.factor(100*z*z*sp.diff(f, z)) == (z-1)*(z+10)*(9*z+10)
    selected = f.subs(z, 1)
    largest = abs(f.subs(z, -10))
    assert selected == sp.Rational(391, 200) and largest == sp.Rational(47, 10)
    assert selected < largest
    return {'figure_eight_positive_whole_sources': rows,
            'exact_pole_selected_vs_largest_critical': {'Rsep': str(selected),
                                                       'largest_critical_modulus': str(largest)}}


def main():
    mp.mp.dps = 90
    data = {'status': 'PASS', 'whole_original_source_constructions': original_sources(),
            'selected_level_prototype_checks': selected_positive_prototypes(),
            'scope': ('Source exactness and selected planar level theorem only; '
                      'no geometric action bound for general knots or five-crossing connectivity certification.')}
    Path(__file__).with_name('whole_source_hadamard_lemniscate_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print('PASS25 original whole-source Newton/Hadamard constructions, all-color '
          'truncation, one-pole cases and selected-level prototype distinctions')


if __name__ == '__main__':
    main()
