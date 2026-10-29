#!/usr/bin/env python3
"""Actual weighted R/Green-source rates, exact HS factorization and variational maximum."""

import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import logsumexp, spence


CATALAN = .915965594177219015054603514932384110774
M0 = 2*CATALAN/np.pi


def J(s):
    s = np.asarray(s, dtype=float)
    value = -np.imag(spence(1-np.exp(2j*np.pi*s)))/(2*np.pi)
    return np.where((s == 0) | (s == 1), 0., value)


def weights(rho, sign=1):
    a, b, c, d = rho
    if sign < 0:
        a, b, c, d = b, a, d, c
    return c-a, c-b, d-a


def profile(alpha, p, qw, r):
    if alpha <= 0:
        return max(0., qw)+max(0., r)
    if alpha >= 1:
        return p
    sa, ca = np.sin(np.pi*alpha), np.cos(np.pi*alpha)
    beta = np.arctan2(sa, np.exp(-qw)-ca)/np.pi
    gamma = np.arctan2(sa, np.exp(-r)-ca)/np.pi
    return float(J(alpha+beta)+J(alpha+gamma)-J(alpha)-J(beta)-J(gamma)
                 +p*alpha+qw*beta+r*gamma)


def variational(rho, sign=1):
    w = weights(rho, sign)
    candidates = [(profile(0., *w), 0.), (profile(1., *w), 1.)]
    # Diagnostic optimization only: the all-weight one-dimensional formula
    # and the unweighted unique maximum are proved analytically in the note.
    grid = np.linspace(0, 1, 33)
    for lo, hi in zip(grid[:-1], grid[1:]):
        result = minimize_scalar(lambda x: -profile(x, *w), bounds=(lo, hi),
                                 method='bounded', options={'xatol': 2e-13})
        candidates.append((-float(result.fun), float(result.x)))
    return max(candidates)


def factorial_logs(N):
    return np.r_[0., np.cumsum(np.log(2*np.sin(np.pi*np.arange(1, N)/N)))]


def crossing_log_hs(N, rho, sign=1):
    p, qw, r = weights(rho, sign)
    F = factorial_logs(N)
    rows = []
    for k in range(N):
        t = np.arange(N-k)
        terms = F[k+t]-F[t]
        rows.append(2*(-F[k]+p*k)
                    +logsumexp(2*(terms+qw*t))
                    +logsumexp(2*(terms+r*t)))
    return float(logsumexp(rows)/2)


def endpoint_log_hs(N, rho):
    a, b, c, d = rho
    p, qw, r = c-a, c-b, d-a
    ground_out, ground_in = [], []
    for t in range(1, N):
        aa = np.arange(1, t+1)
        bb = t-aa
        ground_out.extend(2*(p*aa+qw*bb))
        e = np.arange(1, t+1)
        ground_in.extend(2*(p*(t-e)+r*e))
    e = np.arange(1, N)
    top = logsumexp(2*(c*(N-e)+d*e))+logsumexp(-2*(a*e+b*(N-e)))
    return float(logsumexp([logsumexp(ground_out), logsumexp(ground_in), top])/2)


def literal_matrices(N, rho):
    Q = np.exp(2j*np.pi/N)
    x = -np.exp(-1j*np.pi/N)
    F = [1.+0j]
    for j in range(1, N):
        F.append(F[-1]*(1-Q**j))
    Rp = np.zeros((N*N, N*N), dtype=complex)
    L = np.zeros_like(Rp)
    for a in range(N):
        for b in range(N):
            for j in range(a+1):
                c = a+b-j
                if c >= N:
                    continue
                Rp[c*N+j, a*N+b] = (x**(-b-j)*Q**(j*b)*F[c]*F[a]
                                     /(F[a-j]*F[b]*F[j]))
            if a >= 1 and a+b < N:
                L[(a+b)*N, a*N+b] += x**(-b-2)
            if b == 0:
                for e in range(1, a+1):
                    L[(a-e)*N+e, a*N] += Q*x**(-e)
            if a >= 1 and b == N-a:
                for e in range(1, N):
                    L[(N-e)*N+e, a*N+b] -= Q*x**(-e)*x**(a-N)
    states = [(a, b) for a in range(N) for b in range(N)]
    ra, rb, rc, rd = rho
    out = np.array([np.exp(rc*a+rd*b) for a, b in states])
    inv = np.array([np.exp(-ra*a-rb*b) for a, b in states])
    Rp = out[:, None]*Rp*inv[None, :]
    L = out[:, None]*L*inv[None, :]
    return Rp, L


def main():
    metric_cases = [(0., 0., 0., 0.), (.05, -.07, .09, -.02),
                    (-.1, .1, .1, -.1), (.1, -.1, -.1, .1),
                    (.08, .08, .08, .08)]
    literal = []
    for N in range(2, 10):
        for rho in metric_cases[:3]:
            R, L = literal_matrices(N, rho)
            er = abs(np.log(np.linalg.norm(R))-crossing_log_hs(N, rho))
            el = abs(np.log(np.linalg.norm(L))-endpoint_log_hs(N, rho))
            assert max(er, el) < 2e-12
            literal.append({'N': N, 'rho': rho, 'R_exact_HS_factorization_error': er,
                            'complete_endpoint_HS_error': el})
    mx, alpha = variational(metric_cases[0])
    assert abs(mx-M0) < 1e-12 and abs(alpha-.5) < 1e-7
    factorial = []
    for N in [4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        err = np.max(np.abs(factorial_logs(N)-N*J(np.arange(N)/N)))
        assert err < 4*np.log(N)
        factorial.append({'N': N, 'max_uniform_factorial_error': float(err),
                          'error_over_logN': float(err/np.log(N))})
    rates = []
    for rho in metric_cases:
        delta = max(0., max(rho[2:])-min(rho[:2]))
        lp = (3*rho[2]+rho[3]-3*rho[0]-rho[1])/4
        lm = (rho[2]+3*rho[3]-rho[0]-3*rho[1])/4
        assert M0+min(lp, lm)-delta > .18
        for sign in [1, -1]:
            M, astar = variational(rho, sign)
            lower = M0+(lp if sign > 0 else lm)
            assert M >= lower-1e-12
            rows = []
            for N in [32, 64, 128, 256, 512]:
                lr = crossing_log_hs(N, rho, sign)
                # The negative source is obtained by swapping both boundaries;
                # delta is invariant, but its finite-N HS norm need not be.
                source_rho = rho if sign > 0 else (rho[1], rho[0], rho[3], rho[2])
                ll = endpoint_log_hs(N, source_rho)
                assert abs(lr-N*M) < 12*np.log(N)
                assert abs(ll-N*delta) < 8*np.log(N)
                rows.append({'N': N, 'crossing_rate': lr/N,
                             'complete_endpoint_rate': ll/N,
                             'observed_log_norm_gap_over_N': (lr-ll)/N})
            rates.append({'rho': rho, 'sign': sign, 'variational_rate': M,
                          'alpha_optimizer_diagnostic': astar, 'endpoint_rate': delta,
                          'rigorous_anchor_gap': lower-delta, 'finite_N': rows})
    result = {'status': 'PASS', 'flat_unique_maximum': {'alpha': .5, 'beta': .25,
              'gamma': .25, 'value': M0, 'exact_value': '2*Catalan/pi'},
              'literal_weighted_R_and_source_checks': literal,
              'uniform_factorial_endpoint_estimates': factorial,
              'signed_weighted_rate_diagnostics': rates,
              'scope': ('Original weighted operator/HS norm and complete Green-source gap; '
                        'no scalar source noncancellation or knot volume limit asserted.')}
    Path(__file__).with_name('weighted_crossing_source_gap_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS24 literal weighted R/source HS identities, nine uniform factorial endpoint '
          'estimates, unique flat maximum and ten signed metric rate/gap families')


if __name__ == '__main__':
    main()
