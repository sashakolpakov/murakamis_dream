#!/usr/bin/env python3
"""Actual length normalization, full star phases and compulsory Gram weights."""

import itertools
import json
from pathlib import Path

import mpmath as mp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_general_flow_fusion import (
    star_coefficients, triangle_data, multiply, outer_block)


def exact_polynomial_checks():
    rows = []
    for N in range(2, 10):
        H = HardyNetwork(N, 1)
        count = 0
        for k1 in range(N):
            for k2 in range(N-k1):
                ks = (k1, k2, N-1-k1-k2)
                for roots in ((1, 1, 1), (2, 3, 5)):
                    old = star_coefficients(H, [N-1-k for k in ks], roots)
                    scalar, edges = triangle_data(H, ks, roots)
                    new = {(0, 0, 0): scalar}
                    for edge in edges:
                        new = multiply(new, outer_block(H, *edge), H.p)
                    assert old == new
                    count += 1
        rows.append({'N': N, 'full_coefficient_polynomial_stars': count})
    return rows


def metric_and_phase_checks():
    mp.mp.dps = 75
    rows = []
    for N in range(2, 16):
        q, d = mp.e**(mp.j*mp.pi/N), N-1
        Q = q*q
        s, F = [mp.mpf(1)], [mp.mpc(1)]
        for j in range(1, N):
            s.append(s[-1]*2*mp.sin(mp.pi*j/N))
            F.append(F[-1]*(1-Q**j))
        D = [mp.sqrt(a)/mp.root(N, 4) for a in s]
        close = lambda x, y: abs(x-y) < mp.mpf('1e-60')*max(1, abs(y))
        assert all(close(D[a]*D[d-a], 1) for a in range(N))
        stars = 0
        for k1 in range(N):
            for k2 in range(N-k1):
                k3 = d-k1-k2
                ks = (k1, k2, k3)
                roots = [mp.e**(mp.j*t) for t in (.17, -.31, .43)]
                scalar = ((-1)**(k1+k3)*Q**(k1*(k1-1)//2+k3*(k3-1)//2-k2)
                          *F[d-k2]/(F[k3]*F[k1])
                          *roots[0]**k2*roots[1]**k3*roots[2]**k1)
                phase = ((-1)**(k1+k3)*Q**(k1*(k1-1)//2+k3*(k3-1)//2-k2)
                         *q**(k1*k3)*roots[0]**k2*roots[1]**k3*roots[2]**k1)
                normalized = scalar*mp.fprod(D[k]/D[d-k] for k in ks)
                assert close(normalized, phase/mp.sqrt(N))
                assert close(abs(normalized)**2, mp.mpf(1)/N)
                w = 1/mp.fprod(s[k] for k in ks)
                # The trivalent dual source metric m=s/sqrt(N).
                dual = mp.fprod(mp.sqrt(N)/s[k] for k in ks)
                assert close(dual, N**mp.mpf('1.5')*w)
                stars += 1
        parallel, coefficients = 0, 0
        for L in range(N):
            for M in range(N-L):
                w = 1/(s[L]*s[M]*s[d-L-M])
                scalar = D[L+M]/(D[L]*D[M])
                assert close(scalar, N**mp.mpf('.75')*mp.sqrt(w))
                parallel += 1
            for r in range(L+1):
                beta = s[L]/(s[r]*s[L-r])
                # Squared coefficient of b_L in the actual product metric.
                gram = beta**2/D[L]**2*(s[r]/mp.sqrt(N))*(s[L-r]/mp.sqrt(N))
                w = 1/(s[r]*s[L-r]*s[d-L])
                assert close(gram, mp.sqrt(N)*w)
                coefficients += 1
        rows.append({'N': N, 'complete_star_phases_and_Gram': stars,
                     'parallel_angle_weights': parallel,
                     'block_and_dual_metric_coefficients': coefficients})
    return rows


if __name__ == '__main__':
    result = {'status': 'PASS', 'exact_polynomial': exact_polynomial_checks(),
              'metric_and_phases': metric_and_phase_checks()}
    Path(__file__).with_name('actual_length_normalized_star_gram_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS: 8 exact polynomial levels, 14 full phase/Gram/parallel-fusion levels')
