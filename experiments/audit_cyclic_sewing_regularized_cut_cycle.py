#!/usr/bin/env python3
"""Check actual cyclic-sewing cut residues and finite-part signs.

The uniform proof is in notes/cyclic_sewing_regularized_cut_cycle.md.
The singular endpoint integrals are evaluated by the independent
integration-by-parts formula, not by subtracting divergent quadratures.
"""

import json
from pathlib import Path

import mpmath as mp


def A_value(N, epsilon, t):
    Q = mp.exp(epsilon * 2j * mp.pi / N)
    weights = [(mp.mpf(k)/N, Q**k) for k in range(1, N)]
    value = mp.exp(-sum(w*mp.log(1-t*z) for w, z in weights))
    derivative = value * sum(w*z/(1-t*z) for w, z in weights)
    return value, derivative


def radial_cut(N, epsilon, j, beta, order, same_branch):
    Q = mp.exp(epsilon * 2j * mp.pi / N)
    alpha, u = Q**(-j), mp.mpf(j)/N
    terms = [(mp.mpf(k)/N, Q**(k-j)) for k in range(1, N) if k != j]

    def regular(x):
        g = mp.exp(-sum(w*mp.log(1-(1+x)*z) for w, z in terms))
        if not same_branch:
            return g / ((1+x)*(alpha*(1+x)-beta)**order)
        # x^order alpha*g/[alpha(1+x)(alpha*x)^order]
        H = alpha**(-order)*g/(1+x)
        if order == 0:
            return H
        log1 = sum(w*z/(1-(1+x)*z) for w, z in terms)-1/(1+x)
        if order == 1:
            return H*log1/u
        log2 = sum(w*z*z/(1-(1+x)*z)**2 for w, z in terms)+1/(1+x)**2
        return H*(log1*log1+log2)/(u*(u+1))

    def pulled(y):
        if not y:
            return N*regular(mp.mpf(0)) if j == N-1 else mp.mpc(0)
        x = y**N
        return N*y**(N-j-1)*regular(x)

    return mp.sin(mp.pi*u)/mp.pi*mp.quad(pulled, [0, mp.mpf('0.5'), 1, 2, mp.inf])


def branch_checks():
    rows = []
    for N in (2, 3, 4, 5):
        for epsilon in (-1, 1):
            Q = mp.exp(epsilon * 2j * mp.pi / N)
            j0 = N-1
            beta = Q**(-j0)
            for order in (1, 2):
                cut = sum(radial_cut(N, epsilon, j, beta, order, j == j0)
                          for j in range(1, N))
                expected = (-beta)**(-order)  # residue at zero of A/[t(t-beta)^order]
                error = abs(cut-expected)
                assert error < mp.mpf('1e-30'), (N, epsilon, order, cut, expected)
                rows.append(dict(N=N, epsilon=epsilon, pole_order=order, error=float(error)))
    return rows


def unramified_checks():
    rows = []
    for N in (2, 3, 4, 5):
        for epsilon in (-1, 1):
            # Exactly the complete cyclic divisor: odd N admits beta=1;
            # even N admits the half-root beta=exp(pi*i/N).
            beta = mp.mpc(1) if N % 2 else mp.exp(mp.pi*1j/N)
            A, Ap = A_value(N, epsilon, beta)
            for order in (1, 2):
                cut = sum(radial_cut(N, epsilon, j, beta, order, False)
                          for j in range(1, N))
                residue = A/beta if order == 1 else Ap/beta-A/(beta*beta)
                expected = (-beta)**(-order)
                error = abs(cut-residue-expected)
                assert error < mp.mpf('1e-30'), (N, epsilon, order, cut, residue, expected)
                rows.append(dict(N=N, epsilon=epsilon, pole_order=order, error=float(error)))
    return rows


def actual_source_witness():
    Aplus, Aprime_plus = A_value(2, 1, 1j)
    Aminus, Aprime_minus = A_value(2, 1, -1j)
    residues = 1j*(Aprime_plus+Aprime_minus)-2*Aplus+2*Aminus

    def B(t):
        return -2j*(t*t-1)/(t*t*(t*t+1)**2)

    # On the sole cut t=-(1+x), the jump is x^-1/2.
    cut = mp.quad(lambda y: -2*B(-(1+y*y))/mp.pi, [0, 1, 2, mp.inf])
    expected = -1j
    error = abs(cut-residues-expected)
    assert error < mp.mpf('1e-35')
    assert abs(residues) > mp.mpf('0.1')
    return dict(cut=[float(mp.re(cut)), float(mp.im(cut))],
                retained_residues=[float(mp.re(residues)), float(mp.im(residues))],
                original_period=[0.0, -1.0], error=float(error))


def main():
    with mp.workdps(55):
        branch = branch_checks()
        ordinary = unramified_checks()
        actual = actual_source_witness()
    result = dict(status='PASS', ramified=branch, unramified=ordinary,
                  actual_crossing_source=actual,
                  scope='Canonical cut finite parts and retained original-source residues; no volume lower bound.')
    Path(__file__).with_name('cyclic_sewing_regularized_cut_cycle_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', ramified_cases=len(branch), unramified_cases=len(ordinary),
                         max_error=max(r['error'] for r in branch+ordinary),
                         actual_source=actual), indent=2))


if __name__ == '__main__':
    main()
