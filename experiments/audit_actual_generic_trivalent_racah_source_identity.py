#!/usr/bin/env python3
"""Uniform symbolic Jacobi certificates and original generic source checks.

The proof uses actual mixed-highest source columns and own finite AW/Sears
identities. It does not infer a source identity from sampled recoupling data.
"""
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_generic_six_head_tetrahedral_source import Generic
from audit_generic_trivalent_bilinear_racah_port import candidate_racah


def symbolic_certificates():
    q, t, H, B, Y = sp.symbols('q t H B Y', nonzero=True)
    Q = q*q
    lam = lambda z: q*z+1/(q*z)
    kap = t*B
    bp = -(Y/H)/kap*(1-Q*Y*H)*(1-H*B*B/Y)*(1-t*t/(Q*Y))/((1-Q*Y*Y)*(1+Q*Y))
    bm = -Y/kap*(1-Y/H)*(1-t*t*Y)*(1-Q*H*B*B*Y)/((1+Y)*(1-Q*Y*Y))
    diag = (t+1/t)*(lam(H*B)+lam(B))/(q+1/q+lam(Y))
    first_A = (q/(t*t)*(1-H)*(1-t*t/H)
               +q*H/(t*t)*(1-t*t/Q)*(1-Q)+q/H+H/q)
    first_B = Q*H*B/t+t/(Q*H*B)
    rowsum = first_B-t*B/q*(lam(Y)-first_A)
    assert sp.cancel(bp+bm+diag-rowsum) == 0
    alpha = (t+1/t)**2+lam(H*B)*lam(B)
    gamma = (t+1/t)*(lam(H*B)+lam(B))
    rho, delta = q-1/q, q+1/q
    plus = bp*bm.subs(Y, Q*Y)
    minus = bp.subs(Y, Y/Q)*bm
    left = ((2*lam(Y)-(Q+1/Q)*lam(Q*Y))*plus
            +(2*lam(Y)-(Q+1/Q)*lam(Y/Q))*minus)
    right = rho*rho*(delta*alpha-gamma*diag-delta*delta*lam(Y)+lam(Y)*diag*diag)
    assert sp.cancel(left-right) == 0
    # c=0 is identically exceptional in the first Fricke diagonal:
    # prove its value by the ACTUAL cup/cap projection instead.
    x0 = Q*B/t
    cup_projection = (x0*(1+t*t)
                      +(1/x0-x0*t*t)*(1+1/(t*t))/(1+1/Q))
    assert sp.cancel(cup_projection-(t+1/t)*lam(B)/delta) == 0
    uf = ((1-Q*H*Y)*(1-Q*Y)*(1-Y/(H*B*B))*(1-Q*Y/(t*t))
          /((1-Q*Y*Y)*(1-Q*Q*Y*Y)))
    ub = ((1-H/Y)*(1-1/Y)*(1-1/(Q*H*B*B*Y))*(1-1/(t*t*Y))
          /((1-1/(Q*Y*Y))*(1-1/(Y*Y))))
    lmb = (1/B-1)*(1-1/(t*t*B))
    assert sp.cancel(diag-(t+1/t-kap*(lmb+uf+ub))) == 0
    sigma_ratio = (-Y/H*(1-Q*H*Y)*(1-Q**3*Y*Y)
        *(1-H*B*B/Y)*(1-t*t/(Q*Y))
        /((1-Q*Y*Y)*(1-Q*t*t*Y)*(1-Q*Q*H*B*B*Y)*(1-Q*Y/H)))
    assert sp.cancel(bp-kap*ub.subs(Y, Q*Y)*sigma_ratio) == 0
    assert sp.cancel(bm-kap*uf.subs(Y, Y/Q)/sigma_ratio.subs(Y, Y/Q)) == 0
    a, b, c, d = sp.symbols('a b c d')
    J, r, r1, r2 = a+b+c, b+c-a, a+b-c, a+c-b
    triangular = lambda n: n*(n-1)/2
    phase = lambda a,b,c:a*a-b*b+c*c-a*b-a*c+b*c-c*d
    actual_trace_phase = d*(3*a+2*b+3*c+3)-4*a*a-4*c*c+2*a*c-2*J
    closed_phase = (actual_trace_phase+phase(a,b,c)+phase(c,b,a)
                    +sum(triangular(n) for n in (r,r1,r2,J+1))
                    +sum(triangular(d-j)-triangular(d+1+j)+2*j for j in (a,b,c)))
    assert sp.expand(closed_phase) == 0
    return {'independent_formal_parameters': ['zeta', 'zeta^N', 'Q^(a-b)', 'Q^b', 'Q^c'],
            'exact_rational_row_sum_identity': True,
            'exact_rational_Fricke_product_recurrence': True,
            'exceptional_c0_actual_cup_projection': True,
            'closed_trace_symmetric_factorial_phase_cancellation': True,
            'exact_AW_diagonal_and_transpose_gauge_identities': True,
            'all_cleared_numerators_identically_zero': True}


def channel_values(g, a, b, c):
    q, Q, p, d = g.q, g.Q, g.p, g.d
    la = lambda j: (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
    h, kap = a-b, pow(q, g.N+2*b, p)
    bp = (-pow(kap, -1, p)*pow(Q, c-h, p)*(1-pow(Q, c+h+1, p))
          *(1-pow(Q, a+b-c, p))*(1-pow(Q, d-c, p))
          *pow((1-pow(Q, 2*c+1, p))*(1+pow(Q, c+1, p)), -1, p)) % p
    bm = (-pow(kap, -1, p)*pow(Q, c, p)*(1-pow(Q, c-h, p))
          *(1-pow(Q, g.N+c, p))*(1-pow(Q, a+b+c+1, p))
          *pow((1+pow(Q, c, p))*(1-pow(Q, 2*c+1, p)), -1, p)) % p
    b0 = ((pow(q, g.N, p)+pow(q, -g.N, p))*(la(a)+la(b))
          *pow(q+pow(q, -1, p)+la(c), -1, p)) % p
    return bp, b0, bm


def K_gauge(g, a, b, c):
    d, q, p, f = g.d, g.q, g.p, g.fac
    J, r, r1 = a+b+c, b+c-a, a+b-c
    P = 2*a*a-b*b+3*c*c-2*a*c+2*b*c-d*(a+b+2*c+1)+b+c
    numerator = f[a]*f[g.N+a]*f[2*b]*f[d-a+b]
    denominator = f[J+1]*f[a-b]*f[r]*f[b]*f[d-a]*f[r1]*f[d-c]
    return (-1)**(d+b+c)*pow(q, P, p)*numerator*pow(denominator, -1, p) % p


def Hom_prefactor(g, a, b, c):
    d, q, p, f = g.d, g.q, g.p, g.fac
    r1, r2 = a+b-c, a+c-b
    E = -2*a*a-5*c*c+2*a*c+2*b*c+a*d+3*d*c-c+d
    return ((-1)**(d+c)*pow(q, E, p)*f[r1]*f[r2]*f[d-a]*f[d-c]*f[2*c+1]
            *pow(f[a]*f[d]*f[d+c+1], -1, p)) % p


def level(N, q=2, p=1000003):
    g = Generic(N, q=q, p=p)
    d, Q, f = g.d, g.Q, g.fac
    vector_checks = source_checks = cyclic_checks = 0
    for a in range(N):
        for b in range(a+1):
            h, D0 = a-b, d+a-b
            indices = list(range(h, d+1))
            position = {A: i for i, A in enumerate(indices)}
            Bmix = np.zeros((len(indices),)*2, dtype=np.int64)
            for A in indices:
                i = position[A]
                Bmix[i, i] = (pow(q, -d+2*b+1, p)*pow(Q, A, p)
                              +pow(q, d-2*b-1, p)*pow(Q, -A, p)) % p
                if A > h:
                    Bmix[i-1, i] = (-pow(q, 2*a-1, p)*pow(Q, A-D0, p)
                        *(1-pow(Q, d+1-A, p))*(1-pow(Q, D0-A+1, p))) % p
            cs = list(range(h, min(a+b, d)+1))
            basis, sigma, source = {}, {}, {}
            for c in cs:
                r2 = a+c-b
                v = np.array([g.W[c][A*N+D0-A, r2] for A in indices], dtype=np.int64)
                phi = (pow(q, -d*c+2*(d-c)*h, p)*f[d-h]
                       *pow(f[d-c]*f[c-h], -1, p)) % p
                assert int(v[0]) == phi
                basis[c] = v*pow(phi, -1, p) % p
                nu = ((-1)**r2*pow(q, r2*(2*c-4*a+r2-1), p)
                      *f[2*a]*f[b+c-a]*pow(f[a+b-c]*f[2*c], -1, p)) % p
                sigma[c] = Hom_prefactor(g, a, b, c)*nu*phi*K_gauge(g, a, b, c) % p
                source[c] = g.regular_corner_sum((a, b, c))*pow(K_gauge(g, a, b, c), -1, p) % p
            assert source[h] == 1
            for c in cs:
                bp, b0, bm = channel_values(g, a, b, c)
                predicted = b0*basis[c] % p
                if c < cs[-1]: predicted = (predicted+bp*basis[c+1]) % p
                else: assert bp == 0
                if c > h: predicted = (predicted+bm*basis[c-1]) % p
                else: assert bm == 0
                assert np.array_equal(Bmix@basis[c] % p, predicted), (N, a, b, c, 'Jacobi')
                vector_checks += 1
            delta_a = ((-1)**a*pow(q, a*(d-3*a-1), p)*f[2*a]*f[d-a]
                       *pow(f[a]*f[d], -1, p)) % p
            right = np.zeros(len(indices), dtype=np.int64)
            for A in indices:
                u = d-b-A
                if 0 <= A <= d-b and u >= 0:
                    right[position[A]] = delta_a*g.high(b, A)*f[D0-A]*pow(f[a]*f[u], -1, p) % p
            actual = np.zeros_like(right)
            for c in cs: actual = (actual+sigma[c]*source[c]*basis[c]) % p
            assert np.array_equal(actual, right), (N, a, b, 'literal Hom column')
            eigen = (pow(q, N, p)+pow(q, -N, p)) % p
            assert np.array_equal(Bmix@right % p, eigen*right % p)
            for c in cs:
                assert g.regular_corner_sum((a,b,c)) == candidate_racah(g,(a,b,c))
                source_checks += 1
    for a in range(N):
        for b in range(N):
            for c in range(abs(a-b), min(a+b, d)+1):
                D = lambda a,b,c:a*a-b*b+c*c-a*b-a*c+b*c-c*d
                left, right = g.regular_corner_sum((b,c,a)), g.regular_corner_sum((a,b,c))
                assert left == pow(q, D(b,c,a)-D(a,b,c), p)*right % p
                cyclic_checks += 1
    return {'N':N, 'generic_zeta':q, 'prime':p,
            'all_actual_mixed_Jacobi_vector_identities':vector_checks,
            'source_normalization_and_single_Racah_checks':source_checks,
            'literal_cyclic_source_covariance_checks':cyclic_checks,
            'full_input_Hom_column_and_endpoint_normalization':True}


if __name__ == '__main__':
    symbolic = symbolic_certificates()
    rows = [level(N) for N in range(2,9)]
    rows += [level(N, q=3, p=1000033) for N in range(2,6)]
    result = {'status':'PASS', 'uniform_symbolic_certificates':symbolic,
              'actual_generic_source_families':rows,
              'scope':'Own universal Fricke/boundary recurrence certificate plus actual generic source column normalization, finite AW/Sears uniqueness and root-normal-safe Racah identity. No conditioning or asymptotic bound follows from this finite proof alone.'}
    Path(__file__).with_name('actual_generic_trivalent_racah_source_identity_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS uniform symbolic Jacobi/AW certificates;',len(rows),'all-input generic families;',
          sum(v['all_actual_mixed_Jacobi_vector_identities'] for v in rows),'vector recurrences')
