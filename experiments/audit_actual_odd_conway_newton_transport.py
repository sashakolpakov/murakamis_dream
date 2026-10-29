#!/usr/bin/env python3
"""Full physical half-twist transport and complete odd-source calibration.

Finite fields certify operator identities, not inequalities. Positive
real bounds and the analytic rate theorem are proved in the note.
"""
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_odd_central_cube_reflection_packet import turn
from audit_actual_pure_conway_auxiliary_color_leaf import root_data


def physical_case(N):
    p, eta, q, E, F, K, pivot, rp, rm = balanced_data(N)
    p2, eta2, q2, sine, nodes, _ = root_data(N)
    assert (p, eta, q) == (p2, eta2, q2)
    D = N-1
    kappa = pow(eta, D*D, p)
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(a), -1, p) for a in np.diag(Kt)])
    omega = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    identity = np.eye(N*N, dtype=np.int64)
    hats = [identity]
    for r in range(1, N):
        step = sine[r]*pow(sine[r-1], -1, p) % p
        hats.append((nodes[r-1]*identity-omega)@hats[-1] % p *pow(step*step % p, -1, p) % p)
    pv = [N*pow(q, -D*(D-u), p) % p for u in range(N)]
    transport = {}
    for sign, crossing in [(-1, rm), (1, rp)]:
        columns = []
        for v in range(N):
            coefficients = [0]*N
            for r in range(v+1):
                gaussian = sine[v]*pow(sine[r]*sine[v-r] % p, -1, p) % p
                coefficients[r] = pow(kappa, sign, p)*(-1)**v*pow(q, sign*v*(r+1), p)*gaussian % p
            expected = sum((a*hat for a, hat in zip(coefficients, hats)), np.zeros_like(identity)) % p
            actual = turn(crossing@hats[D-v] % p, N, p, pv)
            assert np.array_equal(actual, expected)
            columns.append(coefficients)
        transport[sign] = columns
    # Complete sources and original marked closure for all 27 patterns.
    hc = [N*N*sine[2*r]*pow(sine[r]**4 % p, -1, p) % p if r <= D//2 else 0 for r in range(N)]
    leaves = {0: hc}
    for sign in (-1, 1):
        leaves[sign] = [sum(hc[v]*transport[sign][v][r] for v in range(N)) % p for r in range(N)]
        assert not any(leaves[sign][D//2+1:])
    matrices = {sign: sum((a*hat for a, hat in zip(c, hats)), np.zeros_like(identity)) % p
                for sign, c in leaves.items()}
    table = []
    for i in range(N):
        for j in range(N-i):
            for r in range(max(i, j), i+j+1):
                mu = sine[i+j]*sine[r]*pow(sine[i]*sine[j]*sine[r-i]*sine[r-j]*sine[i+j-r] % p, -1, p) % p
                table.append((i, j, r, mu))
    def multiply(a, b):
        out = [0]*N
        for i, j, r, mu in table:
            out[r] = (out[r]+a[i]*b[j]*mu) % p
        return out
    for signs in itertools.product((-1, 0, 1), repeat=3):
        coefficients = multiply(multiply(leaves[signs[0]], leaves[signs[1]]), leaves[signs[2]])
        matrix = matrices[signs[0]]@matrices[signs[1]] % p@matrices[signs[2]] % p
        actual_phi = sum(int(pivot[b])*int(matrix[a*N+b, a*N+b])
                         for a in range(N) for b in range(N))*pow(N, -1, p) % p
        assert actual_phi == coefficients[D]
    return {'N': N, 'full_physical_transport_columns': 2*N,
            'original_marked_mixed_sign_three_leaf_sources': 27}


def complete_coefficients(N):
    q = mp.exp(mp.j*mp.pi/N)
    Q, D, M = q*q, N-1, (N-1)//2
    kappa = mp.exp(mp.j*mp.pi*D*D/(2*N))
    F, s = [mp.mpc(1)], [mp.mpf(1)]
    for r in range(1, N):
        F.append(F[-1]*(1-Q**r))
        s.append(s[-1]*2*mp.sin(mp.pi*r/N))
    pure = [N*N*s[2*r]/s[r]**4 for r in range(M+1)]
    minus = []
    for r in range(M+1):
        inner = mp.fsum(Q**(-v*r)*F[2*v]/(F[v]**3*F[v-r]) for v in range(r, M+1))
        value = N*N/kappa*(-1)**r*q**(2*r*r+r)*inner*s[r]**2/F[r]**3
        # Independent exact transport of the pure complete coefficients.
        transported = mp.fsum(pure[v]/kappa*(-1)**v*q**(-v*(r+1))
                              *s[v]/(s[r]*s[v-r]) for v in range(r, M+1))
        assert abs(value-transported) < mp.mpf('1e-55')*max(1, abs(value))
        minus.append(value)
    return s, {0: pure, -1: minus, 1: [mp.conj(v) for v in minus]}


def complete_calibration(N):
    mp.mp.dps = max(110, N+50)
    s, leaves = complete_coefficients(N)
    D, M = N-1, (N-1)//2
    patterns = [(-1, -1, -1), (-1, 1, -1), (-1, 0, 0), (-1, 0, 1), (1, 1, 1)]
    values = [mp.mpc(0) for _ in patterns]
    for i in range(M+1):
        for j in range(M+1):
            for k in range(max(0, D-i-j), M+1):
                t = D-k
                mu = s[i+j]*s[t]/(s[i]*s[j]*s[t-i]*s[t-j]*s[i+j-t])
                for n, pattern in enumerate(patterns):
                    values[n] += leaves[pattern[0]][i]*leaves[pattern[1]][j]*leaves[pattern[2]][k]*mu
    a = mp.atan(2)/mp.pi
    F0 = 8*mp.catalan/mp.pi
    pure_leading = mp.sqrt(2)/64*N**mp.mpf('1.5')*mp.exp(N*F0)
    rows = []
    for pattern, actual in zip(patterns, values):
        phase = mp.exp(mp.j*mp.pi*D*sum(pattern)/4)
        amplitude = mp.fprod(mp.sqrt(mp.sin(mp.pi*a))*mp.exp(-mp.j*sign*mp.pi*a/2)
                            for sign in pattern if sign)
        ratio = actual/(phase*amplitude*pure_leading)
        rows.append({'pattern': pattern, 'ratio_real': mp.nstr(mp.re(ratio), 19),
                     'ratio_imag': mp.nstr(mp.im(ratio), 19),
                     'N_times_relative_error': mp.nstr(N*abs(ratio-1), 19)})
    return {'N': N, 'source_ratio_diagnostics': rows,
            'scope': 'Original finite sums; diagnostic only, not an asymptotic proof.'}


def alias_checks():
    mp.mp.dps = 70
    count = 0
    for N in range(2, 61):
        sine = [mp.mpf(1)]
        for r in range(1, N):
            sine.append(sine[-1]*2*mp.sin(mp.pi*r/N))
        for t in range(1, N//2+1):
            v = N-t
            for r in range(v+1):
                original = sine[v]/(sine[r]*sine[v-r])
                reflected = sine[t+r-1]/(sine[t-1]*sine[r])
                assert abs(original-reflected) < mp.mpf('1e-55')*max(1, original)
                assert original <= math.comb(t+r-1, t-1)*(1+mp.mpf('1e-55'))
                assert original <= math.comb(N-1, t-1)*(1+mp.mpf('1e-55'))
                if t == 1:
                    assert abs(original-1) < mp.mpf('1e-55')
                count += 1
    return {'exact_reflection_and_binomial_bounds_checked': count,
            'levels': 59, 'principal_root_precision_digits': 70}


if __name__ == '__main__':
    physical = [physical_case(N) for N in range(2, 11)]
    aliases = alias_checks()
    diagnostics = [complete_calibration(N) for N in (12, 13, 24, 25, 48, 49)]
    result = {'status': 'PASS', 'full_physical_cases': physical,
              'alias_checks': aliases, 'complete_half_twist_source_diagnostics': diagnostics,
              'scope': 'Full Newton source identities and complete-coupon diagnostics. No whole mixed-color alias gap or odd-coupon filling theorem.'}
    Path(__file__).with_name('actual_odd_conway_newton_transport_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {sum(v["full_physical_transport_columns"] for v in physical)} full transport columns, '
          f'{sum(v["original_marked_mixed_sign_three_leaf_sources"] for v in physical)} marked mixed-sign sources, '
          f'{aliases["exact_reflection_and_binomial_bounds_checked"]} alias bounds; '
          f'{len(diagnostics)*5} complete finite-source diagnostics')
