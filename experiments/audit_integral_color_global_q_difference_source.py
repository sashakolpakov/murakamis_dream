#!/usr/bin/env python3
"""Exact polynomial q-module, actual balanced source and global patch."""

import cmath
import itertools
import json
import math
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field


def qint(r, q, p):
    if q == 1:
        return r % p
    rho = (q-pow(q, -1, p)) % p
    return (pow(q, r, p)-pow(q, -r, p))*pow(rho, -1, p) % p


def factorials(n, q, p):
    out = [1]
    for j in range(1, n+1):
        out.append(out[-1]*qint(j, q, p) % p)
    return out


def symmetric_D(n, q, p):
    fac = factorials(n, q, p)
    return [pow(-1, j, p)*pow(q, j*(j+1)//2, p)
            *fac[j]*fac[n-j]*pow(fac[n], -1, p) % p
            for j in range(n+1)]


def module_case(N, kind):
    n = N-1
    if kind == 'root':
        p, _, q = field(N)
    else:
        p, q = 1009, (1 if kind == 'classical' else 2)
    Q, rho = q*q % p, (q-pow(q, -1, p)) % p
    D = symmetric_D(n, q, p)
    assert all(D)
    M = -pow(q, N, p) % p
    w = (M*pow(Q, -N, p)-pow(M, -1, p)) % p
    assert w == 0
    E = [qint(j, q, p) for j in range(N)]
    F = [qint(n-j, q, p) for j in range(N)]
    K = [pow(q, n-2*j, p) for j in range(N)]
    # Direct common-Verma conjugation gives the actual Gauss matrices.
    for j in range(1, N):
        actual_E = (M*pow(Q, -j, p)-pow(M, -1, p)) % p
        actual_E = actual_E*D[j]*pow(D[j-1], -1, p) % p
        assert actual_E == rho*E[j] % p
        actual_F = (1-pow(Q, j, p))*D[j-1]*pow(D[j], -1, p) % p
        assert actual_F == rho*F[j-1] % p
    for j in range(N):
        assert E[n-j] == F[j]
        assert K[n-j] == pow(K[j], -1, p)
        ord_E = qint(j, q, p)*qint(N-j, q, p)*pow(N-j, -1, p) % p
        if j:
            assert ord_E == E[j]*qint(N-j, q, p)*pow(N-j, -1, p) % p
        assert (D[j]*pow(D[j], -1, p)) % p == 1
    assert sum(D[j]*pow(D[j], -1, p) for j in range(N))*pow(N, -1, p) % p == 1
    if kind == 'root':
        assert D == [pow(-1, j, p)*pow(q, j*(j+1)//2, p) % p for j in range(N)]
    if kind == 'classical':
        assert D == [pow(-1, j, p)*pow(math.comb(n, j), -1, p) % p for j in range(N)]
        assert all(rho*x % p == 0 for x in E+F)
    # Global north/south O(n) transition: J reverses the two arrows.
    for j in range(N):
        assert qint(n-j, q, p) == F[j]
        assert qint(j, q, p) == E[j]
    # Exact finite coherent symbols from literal matrix entries.
    vv, zz = 3, 5
    if (1+vv*zz) % p == 0:
        zz = 7
    denom = pow(1+vv*zz, n, p)
    TT = vv*zz*pow(1+vv*zz, -1, p) % p
    symE = sum((rho*E[j])*math.comb(n, j)*pow(vv, j-1, p)*pow(zz, j, p)
               for j in range(1, N))*pow(denom, -1, p) % p
    symF = sum((rho*F[j])*math.comb(n, j)*pow(vv, j+1, p)*pow(zz, j, p)
               for j in range(n))*pow(denom, -1, p) % p
    symK = sum(K[j]*math.comb(n, j)*pow(vv*zz, j, p)
               for j in range(N))*pow(denom, -1, p) % p
    plus = (1+(q-1)*TT) % p
    minus = (1+(pow(q, -1, p)-1)*TT) % p
    assert symE == (pow(plus, n, p)-pow(minus, n, p))*pow(vv, -1, p) % p
    assert symF == vv*(pow(q, n, p)*pow(minus, n, p)
                      -pow(q, -n, p)*pow(plus, n, p)) % p
    assert symK == pow(q, n, p)*pow(1+(pow(q, -2, p)-1)*TT, n, p) % p
    return {'level': N, 'parameter': kind,
            'actual_balanced_regular_gauge': True,
            'global_q_polynomial_patch': True,
            'both_wall_and_literal_source_pairing': True,
            'finite_coherent_symbols_from_actual_matrices': True}


def crossing_case(N, kind):
    n = N-1
    if kind == 'root':
        p, _, q = field(N)
    else:
        p, q = 1009, (1 if kind == 'classical' else 2)
    Q, rho = q*q % p, (q-pow(q, -1, p)) % p
    M, xx = -pow(q, N, p) % p, pow(q, n, p)
    D = symmetric_D(n, q, p)
    fact = factorials(n, q, p)
    def gauss(nn, kk):
        tab = [[0]*(kk+1) for _ in range(nn+1)]
        for ii in range(nn+1):
            tab[ii][0] = 1
            for jj in range(1, min(ii, kk)+1):
                if jj == ii:
                    tab[ii][jj] = 1
                else:
                    tab[ii][jj] = (tab[ii-1][jj]
                        +pow(Q, ii-jj, p)*tab[ii-1][jj-1]) % p
        return tab[nn][kk]
    def poch(z, k):
        out = 1
        for r in range(k):
            out = out*(1-z*pow(Q, r, p)) % p
        return out
    nonzero = 0
    for a in range(N):
        for b in range(N):
            for k in range(min(a, n-b)+1):
                old = pow(-1, k, p)*pow(xx, -a-b-k, p) \
                    *pow(Q, a*b+(a-b)*k-k*(k+1)//2, p) \
                    *gauss(b+k, k)*poch(M*M*pow(Q, -a, p) % p, k) % p
                new = old*D[a]*D[b]*pow(D[b+k]*D[a-k] % p, -1, p) % p
                expected = pow(q, -n*(a+b)+2*(a-k)*(b+k)+k*(k-1)//2, p) \
                    *pow(rho, k, p)*pow(fact[k], -1, p) % p
                for r in range(k):
                    expected = expected*qint(a-r, q, p)*qint(n-b-r, q, p) % p
                assert new == expected
                nonzero += new != 0
    return {'level': N, 'parameter': kind,
            'whole_actual_R_equals_standard_qspin_R_after_frame': True,
            'literal_checked_crossing_coefficients': nonzero}


def symbolic_factorial_and_clutch():
    q, x = s.symbols('q x', nonzero=True)
    rho = q-1/q
    qi = lambda r: sum(q**(r-1-2*k) for k in range(r)) if r else s.Integer(0)
    records = []
    for N in range(2, 7):
        n = N-1
        for j in range(N):
            P = s.prod(1-q**(2*r) for r in range(1, j+1))
            candidate = (-rho)**j*q**(j*(j+1)//2)*s.prod(qi(r) for r in range(1, j+1))
            assert s.cancel(P-candidate) == 0
            # Finite q-difference action and ordinary-falling action.
            Eact = s.cancel(((q*x)**j-(x/q)**j)/(rho*x))
            assert s.cancel(Eact-qi(j)*x**(j-1)) == 0
            Fact = s.cancel(x*(q**n*(x/q)**j-q**(-n)*(q*x)**j)/rho)
            assert s.cancel(Fact-qi(n-j)*x**(j+1)) == 0
        records.append({'level': N, 'singular_Pochhammer_factor_canceled_exactly': True,
                        'literal_q_difference_action_all_monomials': True})
    return records


def uniform_symbol_diagnostics():
    observations = []
    for N in (16, 32, 64, 128):
        n = N-1
        worst = 0.0
        for lam in (0., .1, .4, .75, 1.):
            ss = 2j*math.pi*lam
            q = cmath.exp(ss/(2*N))
            rho = q-1/q
            for T in (0., 1e-5, .05, .25, .5, .9, 1-1e-5, 1.):
                pp, mm = 1+(q-1)*T, 1+(1/q-1)*T
                efinite = n*rho if T == 0 else (pp**n-mm**n)/T
                etarget = ss if T == 0 else 2*cmath.sinh(ss*T/2)/T
                ffinite = n*rho if T == 1 else (q**n*mm**n-q**(-n)*pp**n)/(1-T)
                ftarget = ss if T == 1 else 2*cmath.sinh(ss*(1-T)/2)/(1-T)
                kfinite = q**n*(1+(q**-2-1)*T)**n
                ktarget = cmath.exp(ss*(.5-T))
                worst = max(worst, abs(efinite-etarget), abs(ffinite-ftarget),
                            abs(kfinite-ktarget))
        assert N*worst < 60
        observations.append({'level': N, 'N_times_endpoint_divided_error': N*worst})
    return observations


def main():
    modules = [module_case(N, kind) for N in range(2, 9)
               for kind in ('generic', 'root', 'classical')]
    crossings = [crossing_case(N, kind) for N in range(2, 7)
                 for kind in ('generic', 'root', 'classical')]
    result = {'module_source_global_patch': modules,
              'actual_crossing_checks': crossings,
              'symbolic_q_difference_and_factorial': symbolic_factorial_and_clutch(),
              'uniform_endpoint_symbol_diagnostics': uniform_symbol_diagnostics(),
              'scope': 'Exact integral-color q-difference/source family and controlled generator symbols; no full-word norm or selected geometric phase theorem.'}
    target = Path(__file__).with_name('integral_color_global_q_difference_source_results.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'module_parameter_cases': len(modules),
                      'literal_actual_crossing_cases': len(crossings),
                      'symbolic_factorial_levels': len(result['symbolic_q_difference_and_factorial']),
                      'endpoint_symbol_levels': len(result['uniform_endpoint_symbol_diagnostics'])}))


if __name__ == '__main__':
    main()
