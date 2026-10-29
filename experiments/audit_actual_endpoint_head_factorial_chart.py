#!/usr/bin/env python3
"""Finite checks of the endpoint chart, with the actual signed source retained."""

import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix, partial


def condition_bounds():
    rows = []
    for N in (2, 3, 4, 5, 8, 12, 24, 48, 96, 192, 384):
        logs = [mp.mpf(0)]
        for a in range(1, N):
            logs.append(logs[-1]+mp.log(2*mp.sin(mp.pi*a/N)))
        radii = sorted({0, (N-1)//2, min((N-1)//2, int(N**.6))})
        for R in radii:
            band = sorted(set(range(R+1)) | set(range(N-1-R, N)))
            logH = mp.mpf(R)*mp.log(mp.e*N/R) if R else mp.mpf(0)
            hi = max(logs[a] for a in band)
            lo = min(logs[a] for a in band)
            tol = mp.mpf('1e-60')
            assert hi <= mp.log(N)+logH+tol
            assert -lo <= logH+tol
            assert hi-lo <= mp.log(N)+2*logH+tol
            rows.append(dict(N=N, R=R, actual_log_condition=float(hi-lo),
                             proved_log_bound=float(mp.log(N)+2*logH)))
    return rows


def generator_checks():
    rows = []
    for N in range(2, 13):
        H = HardyNetwork(N, 1)
        p, Q, d = H.p, H.Q, N-1
        F = [int(v) for v in H.fac]
        assert F[-1] == N % p
        shift = np.zeros((N, N), dtype=np.int64)
        for a in range(d):
            shift[a+1, a] = 1
        cycle = shift.copy()
        cycle[0, d] = 1
        diag = np.array(F, dtype=np.int64)
        inv = np.array([pow(a, -1, p) for a in F], dtype=np.int64)
        actual = np.zeros_like(shift)
        for a in range(d):
            actual[a+1, a] = (1-pow(Q, a+1, p)) % p
        assert np.array_equal(diag[:, None]*shift*inv[None, :] % p, actual)
        cyclic = diag[:, None]*cycle*inv[None, :] % p
        cyclic[0, d] = (cyclic[0, d]-pow(N, -1, p)) % p
        assert np.array_equal(cyclic, actual)
        for R in sorted({0, min(2, d//2), d//2}):
            band = set(range(R+1)) | set(range(d-R, N))
            g = np.array([F[a] if a in band else 1 for a in range(N)], dtype=np.int64)
            gi = np.array([pow(int(v), -1, p) for v in g], dtype=np.int64)
            chart = gi[:, None]*actual*g[None, :] % p
            for a in range(d):
                expected = (1-pow(Q, a+1, p))*int(g[a])*int(gi[a+1]) % p
                assert chart[a+1, a] == expected
                if a in band and a+1 in band:
                    assert chart[a+1, a] == 1
        rows.append(dict(N=N, exact_unilateral_chart=True,
                         cyclic_rank_one_correction_retained=True,
                         endpoint_band_interfaces_retained=True))
    return rows


def whole_word_checks():
    rows = []
    for N in range(2, 7):
        H = HardyNetwork(N, 1)
        p, d, b = H.p, N-1, 3
        for word in ([1, -2, 1, -2], [-1, 2, -1, 2]):
            size = N**b
            original = np.eye(size, dtype=np.int64)
            transformed = original.copy()
            prev = np.ones(size, dtype=np.int64)
            for step, letter in enumerate(reversed(word)):
                gate = word_matrix([letter], H.plus, H.minus, b, N, p)
                nxt = np.ones(size, dtype=np.int64)
                if step < len(word)-1:
                    R = min(d//2, step % 2)
                    selected = step % b
                    band = set(range(R+1)) | set(range(d-R, N))
                    for i, state in enumerate(itertools.product(range(N), repeat=b)):
                        a = state[selected]
                        nxt[i] = int(H.fac[a]) if a in band else 1
                inverse = np.array([pow(int(v), -1, p) for v in nxt], dtype=np.int64)
                gauged = inverse[:, None]*gate*prev[None, :] % p
                original = gate@original % p
                transformed = gauged@transformed % p
                prev = nxt
            assert np.array_equal(original, transformed)
            # The same ORIGINAL pivotal and marked scalar, not a replacement norm.
            oldcut = partial(original, H.pivot, b, N, p)
            newcut = partial(transformed, H.pivot, b, N, p)
            assert np.array_equal(oldcut, newcut)
            external = H.dimension*pow(H.twist, -sum(1 if j > 0 else -1 for j in word), p) % p
            old = int(np.trace(oldcut))*pow(N, -1, p)*external % p
            new = int(np.trace(newcut))*pow(N, -1, p)*external % p
            assert old == new
            rows.append(dict(N=N, word=list(word), original_period_mod_p=old,
                             all_internal_basis_changes_cancel_exactly=True,
                             original_pivot_and_external_factors_retained=True))
    return rows


def chart_and_source_checks():
    B, f = sp.symbols('B f', nonzero=True)
    K, e = -1/B, (1-B)**2/(B*f)
    G = sp.Matrix([[K, e], [f*K, f*e+1/K]])
    assert sp.simplify(G.det()-1) == 0
    assert sp.simplify(sp.trace(G)+2) == 0
    assert G.subs(B, 1) == sp.Matrix([[-1, 0], [-f, -1]])
    tests = []
    for N, R in ((3, 0), (8, 2), (16, 3), (32, 5)):
        Q = np.exp(2j*np.pi/N)
        U = np.array([[Q**(-a*j)/math.sqrt(N) for a in range(N)] for j in range(N)])
        P = np.diag([1 if a <= R else 0 for a in range(N)])
        kernel = U@P@U.conj().T
        expected = np.array([[sum(Q**(a*(j-i)) for a in range(R+1))/N
                              for j in range(N)] for i in range(N)])
        assert np.max(abs(kernel-expected)) < 2e-14
        for t in (mp.mpf('.5'), mp.mpc('.7', '.2'), mp.mpf('1.3')):
            direct = sum(t**a for a in range(R+1))
            geometric = (1-t**(R+1))/(1-t)
            assert abs(direct-geometric) < mp.mpf('1e-60')
            assert abs(direct) <= (R+1)*max(1, abs(t))**R+mp.mpf('1e-60')
        # Residues of the apparent two matching poles sum to exactly zero.
        t = sp.symbols('t')
        assert sp.residue(1/(1-t), t, 1)+sp.residue(-t**(R+1)/(1-t), t, 1) == 0
        tests.append(dict(N=N, R=R, full_Fourier_projector_retained=True,
                          canceled_matching_residues=True,
                          off_diagonal_half_ratio_value=float(sum(mp.mpf('.5')**a for a in range(R+1))/N)))
    return dict(actual_noncentral_meridian_chart=True, source_checks=tests)


def main():
    mp.mp.dps = 75
    data = dict(status='PASS', condition_bounds=condition_bounds(),
                exact_generator_charts=generator_checks(),
                original_signed_word_changes=whole_word_checks(),
                classical_chart_and_normal_source=chart_and_source_checks(),
                scope='Endpoint chart cost only. Neither normal matching nor a geometric whole-source bound is inferred.')
    Path(__file__).with_name('actual_endpoint_head_factorial_chart_results.json').write_text(json.dumps(data, indent=2)+'\n')
    print('PASS endpoint condition bounds, 11 exact generator families, 10 original signed words, and retained Fourier normal sources')


if __name__ == '__main__':
    main()
