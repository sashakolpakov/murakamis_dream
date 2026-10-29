#!/usr/bin/env python3
"""Exact actual Euler cap, wrapped source, and Cauchy boundary identities.

Finite-field matrix checks use the original pivotal cap after the actual
triangular fusion. They do not identify central F with Fourier momentum.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import (
    alg_product, fusion, inv, physical_cap, right_regular,
)
from audit_actual_two_cut_ports import balanced_data


def case(N: int):
    p, _, q, _, _, K, _, plus, minus = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, p)) % p)
    gamma = N*pow(x, 2-2*N, p)*Q % p
    one = np.zeros(N*N, dtype=np.int64)
    one[:N] = 1
    e = np.zeros(N*N, dtype=np.int64)
    e[N-1] = 1
    u, v, wrap = (np.zeros(N*N, dtype=np.int64) for _ in range(3))
    for j in range(N):
        u[j*N:(j+1)*N] = pow(x, j, p)*pow(fac[j], -1, p) % p
        v[j*N:(j+1)*N] = (pow(-1, j, p)*pow(Q, j*(j+3)//2, p)
                          *pow(x, j, p)*pow(fac[j], -1, p)) % p
    for a in range(1, N):
        for b in range(a):
            wrap[(N-1-a)*N+b] = (pow(x, 1-N-a, p)*pow(Q, -b, p)
                                              *fac[b]*pow(fac[N+b-a], -1, p)) % p

    def mul(a, b, phi):
        return alg_product(a, b, N, phi, p)

    def sigma(a):
        return np.concatenate([a[j*N:(j+1)*N]*pow(Q, j, p) % p
                               for j in range(N)])

    f = np.zeros(N*N, dtype=np.int64)
    f[N:2*N] = 1
    qfac = pow(x, N, p)*pow(N, -1, p) % p
    counts = {"nilpotent_basis_Cauchy_and_dressed_Ward": 0,
              "nilpotent_rational_kernel_basis": 0,
              "whole_actual_cap_basis": 0, "whole_Euler_and_wrap": 0,
              "whole_affine_co_source_Ward": 0, "nilpotent_x_connection": 0}
    for phi1, phi2 in ((0, 0), (0, 3), (2, 3), (2, -2*pow(x, N, p) % p)):
        C, Ci, phi, _, _, Ks, _ = fusion(N, p, Q, [x, x], [phi1, phi2 % p])
        t = (one-x*f) % p
        assert np.array_equal((sigma(u)-mul(t, u, phi)) % p, qfac*phi*one % p)
        t2 = (one-pow(Q, 2, p)*x*f) % p
        assert np.array_equal((mul(t2, sigma(v), phi)-v) % p, -qfac*phi*one % p)
        euv = mul(mul(e, v, phi), mul(u, e, phi), phi)
        d = (1+(N-3)*pow(2*N, -1, p)*pow(x, N, p)*phi) % p
        assert np.array_equal(euv, d*e % p)
        predicted = (gamma*mul(mul(u, e, phi), v, phi)
                     -pow(x, N, p)*phi1*wrap) % p
        actual = np.zeros(N*N, dtype=np.int64)
        for a, k in itertools.product(range(N), repeat=2):
            b = (k+a) % N
            value = (pow(x, 1-N-a, p)*pow(Q, -b, p)*fac[b]
                     *pow(fac[k], -1, p)*((phi2 % p) if k+a >= N else 1)) % p
            z = np.zeros(N*N, dtype=np.int64)
            z[a*N+k] = 1
            literal = physical_cap(C@right_regular(z, N, phi, p)@Ci % p, Ks, N, p)
            assert literal == value
            actual[(N-1-a)*N+b] = value
            got = mul(predicted, z, phi)[(N-1)*N:].sum() % p
            assert got == value, (N, phi1, phi2, phi, a, k, int(got), value)
            counts["whole_actual_cap_basis"] += 1
        assert np.array_equal(actual, predicted)
        norm = (1-pow(x, N, p)*phi) % p
        if norm:
            t2_inv, power = one.copy(), one.copy()
            for j in range(1, N):
                power = mul(power, pow(Q, 2, p)*x*f % p, phi)
                t2_inv = (t2_inv+power) % p
            t2_inv = t2_inv*pow(norm, -1, p) % p
            aff = qfac*phi % p
            for a, k in itertools.product(range(N), repeat=2):
                z = np.zeros(N*N, dtype=np.int64)
                z[a*N+k] = 1
                V = mul(t2_inv, sigma(z), phi)
                Tz = mul(V, t, phi)
                delta_z = (Tz-pow(Q, -1, p)*z) % p
                lhs = int(mul(actual, delta_z, phi)[(N-1)*N:].sum()) % p
                correction = (mul(mul(V, t, phi), u, phi)+aff*V-mul(v, V, phi)) % p
                rhs = (gamma*aff*int(correction[(N-1)*N])
                       -pow(x, N, p)*phi1*int(mul(wrap, delta_z, phi)[(N-1)*N:].sum())) % p
                assert lhs == rhs
                counts["whole_affine_co_source_Ward"] += 1
        if phi1 == 0:
            assert np.array_equal(mul(actual, actual, phi), gamma*d*actual % p)
        counts["whole_Euler_and_wrap"] += 1
        if phi1 == 0 and phi2 == 0:
            v0 = np.concatenate([v[j*N:(j+1)*N]*pow(Q, -2*j, p) % p
                                  for j in range(N)])
            assert np.array_equal(mul(u, v0, 0), one)
            kernel = mul(v, u, 0)
            tq = (one-Q*x*f) % p
            assert np.array_equal(mul(mul(t, tq, 0), kernel, 0), one)
            # Original nilpotent cap equals the dressed highest coefficient.
            t_inv = one.copy()
            power = one.copy()
            for j in range(1, N):
                power = mul(power, pow(Q, 2, p)*x*f % p, 0)
                t_inv = (t_inv+power) % p
            for a, k in itertools.product(range(N), repeat=2):
                z = np.zeros(N*N, dtype=np.int64)
                z[a*N+k] = 1
                dressed = mul(mul(v, z, 0), u, 0)
                conjugated = mul(mul(v0, z, 0), u, 0)
                assert np.array_equal(dressed, mul(kernel, conjugated, 0))
                counts["nilpotent_rational_kernel_basis"] += 1
                value = gamma*int(dressed[(N-1)*N]) % p
                literal = mul(actual, z, 0)[(N-1)*N:].sum() % p
                assert value == literal
                Tz = mul(mul(t_inv, sigma(z), 0), t, 0)
                assert (mul(actual, Tz, 0)[(N-1)*N:].sum()
                        -pow(Q, -1, p)*literal) % p == 0
                counts["nilpotent_basis_Cauchy_and_dressed_Ward"] += 1
                A, A2 = np.zeros(N*N, dtype=np.int64), np.zeros(N*N, dtype=np.int64)
                for r in range(1, N):
                    A[r*N:(r+1)*N] = pow(x, r-1, p)*pow(1-pow(Q, r, p), -1, p) % p
                    A2[r*N:(r+1)*N] = A[r*N:(r+1)*N]*pow(Q, 2*r, p) % p
                conn = (mul(z, A, 0)-mul(A2, z, 0)) % p
                conn_value = int(mul(actual, conn, 0)[(N-1)*N:].sum()) % p
                assert ((1-N-a)*literal*pow(x, -1, p)
                        -(2-2*N)*literal*pow(x, -1, p)-conn_value) % p == 0
                counts["nilpotent_x_connection"] += 1

    # Literal signed local crossings, transported by actual fusion, retain
    # the original highest-input/all-ones-output/pivotal source.
    C, Ci, phi, _, _, Ks, _ = fusion(N, p, Q, [x, x], [0, 0])
    for W in (plus, minus, plus@minus % p, plus@plus@plus % p):
        relative = Ci@W@C % p
        a = relative@one % p
        dressed = mul(mul(v, a, 0), u, 0)
        assert gamma*int(dressed[(N-1)*N]) % p == physical_cap(W, Ks, N, p)
    counts["actual_signed_word_periods"] = 4
    return {"N": N, "field": p, **counts}


def main():
    rows = [case(N) for N in range(2, 8)]
    result = {"status": "pass", "levels": rows,
              "scope": "Actual root-source Euler/Cauchy transform, central-F affine defects and both-leg wrap correction. No Fourier-momentum or q-normal identification."}
    output = Path(__file__).with_name("actual_euler_cap_boundary_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
