#!/usr/bin/env python3
"""Exact original-R audits of shared quantum flags and the charged cap wall.

Uses prime fields and the independent original E/Cartan coefficient evaluator.
The common Cartan scalar, framing and peripheral line are external on BOTH
sides. No numerical value is substituted for those retained scalar lines.
"""

import json
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import inv
from audit_actual_rogers_bridge_transport import crossing
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def mm(a, b, p):
    return a @ b % p


def mpow(a, n, p):
    out = np.eye(a.shape[0], dtype=np.int64)
    for _ in range(n):
        out = mm(out, a, p)
    return out


def equal(a, b, p):
    assert np.array_equal(a % p, b % p)


def head(E, x):
    N, p, Q = E.N, E.p, E.Q
    z = np.diag([pow(Q, a, p) for a in range(N)]).astype(np.int64)
    k = x * inv(z, p) % p
    e = np.zeros((N, N), dtype=np.int64)
    f = np.zeros_like(e)
    for a in range(1, N):
        e[a-1, a] = (E.q * E.rho**2 * E.E(x, a) * E.F[a-1]
                     * pow(E.F[a], -1, p)) % p
        f[a, a-1] = (1-pow(Q, a, p)) % p
    return z, k, e, f


def gauss(E, x, position):
    N, p = E.N, E.p
    _, k, e, f = head(E, x)
    i = np.eye(N, dtype=np.int64)
    embed = (lambda a: np.kron(a, i)) if position == 0 else (lambda a: np.kron(i, a))
    k, e, f = embed(k), embed(e), embed(f)
    ki = inv(k, p)
    i2 = np.eye(N*N, dtype=np.int64)
    zero = np.zeros_like(i2)
    G = np.block([[k, e], [mm(f, k, p), (mm(f, e, p)+ki) % p]])
    lm = np.block([[i2, zero], [-mm(k, f, p) % p, k]])
    lmi = np.block([[i2, zero], [f, ki]])
    return G, lm, lmi


def shift(N, mu):
    s = np.zeros((N, N), dtype=np.int64)
    for a in range(N-1):
        s[a+1, a] = 1
    s[0, N-1] = mu
    return s


def euler(E, a):
    out = np.zeros_like(a)
    power = np.eye(a.shape[0], dtype=np.int64)
    for h in range(E.N):
        coeff = pow(-1, h, E.p)*pow(E.Q, h*(h-1)//2, E.p)*pow(E.F[h], -1, E.p)
        out = (out+coeff*power) % E.p
        power = mm(power, a, E.p)
    return out


def cyclic_inverse_representative(E, v, t, nu):
    """D_N(tv), up to scalar, by its EXACT cyclic functional equation.

    The actual literature atom is the inverse, with its retained determinant
    root scalar. The identity has one identical atom on either side, so its
    verification is homogeneous in that scalar.
    """
    p, Q = E.p, E.Q
    coeff = [1]
    for j in range(1, E.N):
        coeff.append(-t*coeff[-1]*pow((nu*pow(Q, j, p)-1) % p, -1, p) % p)
    assert (nu-1)*coeff[0] % p == -t*coeff[-1] % p
    out = np.zeros_like(v)
    power = np.eye(v.shape[0], dtype=np.int64)
    for c in coeff:
        out = (out+c*power) % p
        power = mm(power, v, p)
    return out, coeff


def main():
    generic, flags, wrong_wrap, mixed_pentagons = [], [], [], []
    for N in range(2, 9):
        p, g, q = field(N)
        E = MixedEntries(N, p, q)
        Q, d = E.Q, N-1
        x0 = -pow(q, -1, p) % p
        for x, y in ((g, pow(g, 2, p)), (x0, g), (x0, x0)):
            B = crossing(E, x, y, 1)
            BB = np.kron(np.eye(2, dtype=np.int64), B)
            G1, _, _ = gauss(E, x, 0)
            G2, _, _ = gauss(E, y, 1)
            _, lm1, lmi1 = gauss(E, x, 0)
            H2 = mm(mm(lmi1, G2, p), lm1, p)
            Go1, lmo1, lmoi1 = gauss(E, y, 0)
            Go2, _, _ = gauss(E, x, 1)
            Ho2 = mm(mm(lmoi1, Go2, p), lmo1, p)
            ci = (pow(x, -1, p)+Q*x) % p
            idbig = np.eye(2*N*N, dtype=np.int64)
            equal(mm(G1, G1, p)-ci*G1+Q*idbig, np.zeros_like(idbig), p)
            equal(mm(BB, G1, p), mm(Ho2, BB, p), p)
            Ho2i = (ci*idbig-Ho2)*pow(Q, -1, p) % p
            equal(mm(BB, H2, p), mm(mm(mm(Ho2, Go1, p), Ho2i, p), BB, p), p)
            generic.append({'N': N, 'x': x, 'y': y, 'quantum_Hurwitz': True})

        x = x0
        z, k, e, f = head(E, x)
        lam, kn = pow(x, -1, p), pow(x, N, p)
        i = np.eye(N, dtype=np.int64)
        i2 = np.eye(N*N, dtype=np.int64)
        B = crossing(E, x, x, 1)
        Bi = inv(B, p)
        K1, K2 = np.kron(k, i), np.kron(i, k)
        e2, f1 = np.kron(i, e), np.kron(f, i)
        cup = np.zeros(N*N, dtype=np.int64)
        marker = np.zeros_like(cup)
        for a in range(N):
            cup[a*N+d-a] = N*pow(x, a-d, p) % p
            for b in range(N):
                marker[a*N+b] = pow(x, b, p)*pow(N, -2, p) % p
        equal(B@cup, cup, p)
        assert int(marker@cup) % p == 1
        degree = np.diag([a+b for a in range(N) for b in range(N)])
        equal((degree+i2)@cup, N*cup, p)

        for mu in (1, g, pow(g, 2, p)):
            S1 = np.kron(shift(N, mu), i)
            S2 = np.kron(i, shift(N, kn*mu % p))
            t1 = S1
            t2 = (f1+mm(inv(K1, p), S2, p)) % p
            delta = (t2-t1) % p
            gamma = mm(mm((K2-lam*i2) % p, inv(S2, p), p), K1, p)
            v = (np.kron(i, inv(z, p))+mm(S1, e2, p)) % p
            vi = mpow(v, N-1, p)
            equal(mm(B, S1, p), mm(t2, B, p), p)
            equal(mm(mm(v, B, p), S2, p), lam*mm(S1, B, p), p)
            equal(mm(mm(B, S2, p), Bi, p), lam*mm(S1, vi, p), p)
            equal(mpow(v, N, p), i2, p)
            equal(mpow(delta, N, p), np.zeros_like(i2), p)
            equal(mpow(gamma, N, p), np.zeros_like(i2), p)
            equal(mm(delta, gamma, p)-Q*mm(gamma, delta, p), lam*(Q-1)*i2, p)
            equal(v, i2+pow(lam, -1, p)*mm(delta, gamma, p), p)
            equal(mm(delta, v, p), Q*mm(v, delta, p), p)
            t3 = mm(mm(B, t2, p), Bi, p)
            equal(t3, t2-Q*mm(delta, vi, p), p)
            equal(t3-t1, mm(i2-v, t3-t2, p), p)
            equal(v@cup, Q*cup, p)
            equal(delta@cup, np.zeros_like(cup), p)
            endpoint = np.zeros((N, N), dtype=np.int64)
            endpoint[0, d] = 1
            b1, b2 = np.kron(endpoint, i), np.kron(i, endpoint)
            z1 = np.kron(z, i)
            wall1 = mu*mm(z1, b1, p) % p
            wall2 = lam*kn*mu*mm(z1, b2, p) % p
            equal(mm(degree, delta, p)-mm(delta, degree, p),
                  delta-N*(wall2-wall1), p)
            assert int(marker@wall1@cup) % p == mu*pow(N, -1, p) % p
            assert int(marker@wall2@cup) % p == mu*pow(N, -1, p) % p
            # Actual-source spectral projectors: exactly the j=1 wall survives.
            for j in range(N):
                proj = sum((pow(Q, -j*r, p)*mpow(v, r, p) for r in range(N)),
                           np.zeros_like(i2))*pow(N, -1, p) % p
                assert int(marker@proj@cup) % p == int(j == 1)
            nth_powers = {pow(a, N, p): a for a in range(1, p)}
            t, nu = next((a, nth_powers[(1-pow(a, N, p)) % p])
                         for a in range(1, p)
                         if (1-pow(a, N, p)) % p in nth_powers)
            rawD, coefficients = cyclic_inverse_representative(E, v, t, nu)
            atom = inv(rawD, p)
            atom_source = pow(sum(c*pow(Q, j, p) for j, c in enumerate(coefficients)) % p, -1, p)
            equal(atom@cup, atom_source*cup, p)
            for alpha in (1, g):
                aterm = alpha*pow(nu, -1, p)*delta % p
                bterm = -alpha*pow(nu, -1, p)*pow(Q, -1, p)*t*mm(delta, v, p) % p
                lhs = mm(atom, euler(E, alpha*delta % p), p)
                rhs = mm(mm(euler(E, aterm), euler(E, bterm), p), atom, p)
                equal(lhs, rhs, p)
                assert int(marker@lhs@cup)*pow(atom_source, -1, p) % p == 1
                mixed_pentagons.append({'N': N, 'mu': mu, 'alpha': alpha,
                                        't': t, 'nu': nu, 'source_unit': 1})
            flags.append({'N': N, 'mu': mu, 'typed_second_wrap': kn*mu % p,
                          'cleared_quantum_Ptolemy': True,
                          'original_cap_wall': 1, 'affine_charge': N})
        if N % 2 == 0:
            S1 = np.kron(shift(N, 1), i)
            badS2 = np.kron(i, shift(N, 1))
            badt2 = (f1+mm(inv(K1, p), badS2, p)) % p
            assert np.any((mm(B, S1, p)-mm(badt2, B, p)) % p)
            wrong_wrap.append(N)
    data = {'quantum_Hurwitz_cases': generic, 'charged_shared_flag_cases': flags,
            'even_N_frozen_wrap_obstructions': wrong_wrap,
            'actual_flag_mixed_two_to_three_identities': mixed_pentagons,
            'scope': 'original root-family matrices; no geometric cycle or volume claim'}
    path = Path(__file__).with_name('audit_actual_shared_quantum_flags_results.json')
    path.write_text(json.dumps(data, indent=2)+'\n')
    print(f'PASS {len(generic)} quantum Hurwitz families; {len(flags)} charged flag families; '
          f'{len(wrong_wrap)} even-level wrap obstructions; '
          f'{len(mixed_pentagons)} mixed two-to-three identities')


if __name__ == '__main__':
    main()
