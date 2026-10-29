#!/usr/bin/env python3
"""Original retained-belt source, exact Chebyshev sampling, finite diagnostics.

The limiting theorem is the written ellipse/sampling argument. Numeric
rate rows are only calibrations, never its noncancellation premise.
"""
import json
from collections import Counter
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pair_casimir_commutant_and_rotated_trace import phi, rotated


def physical_level(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x = N-1, q*q % p, int(K[0, 0])
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    I = np.eye(N*N, dtype=np.int64)
    U0, U1 = I.copy(), O.copy()
    if d == 1:
        L = -U1 % p
    else:
        for _ in range(2, d+1):
            U0, U1 = U1, (O@U1-U0) % p
        L = (-1)**d*U1 % p

    def turn(A):
        return pow(x, d, p)*rotated(A, N, x, p) % p

    z, zsharp = turn(Rm@L % p), turn(Rp@L % p)
    ids = [a*N+d-a for a in range(N)]
    middle = z[np.ix_(ids, ids)]
    middle_sharp = zsharp[np.ix_(ids, ids)]
    nodes = [(pow(q, 2*a+1, p)+pow(q, -2*a-1, p)) % p
             for a in range(N)]
    mult = Counter(nodes)
    M = d//2
    assert len(mult) == (N+1)//2 and sum(mult.values()) == N
    # Full actual Newton coefficients, using the original endpoint source.
    packet, sine2 = [I], [1]
    for r in range(1, N):
        f = 1-pow(Q, r, p)
        sine2.append(sine2[-1]*(-pow(Q, -r, p))*f*f % p)
        packet.append((nodes[r-1]*I-O)@packet[-1]
                      *int(sine2[r-1])*pow(int(sine2[r]), -1, p) % p)
    alpha = [int((middle@A[np.ix_(ids, ids)] % p)[0, d])
             for A in reversed(packet)]
    ash = [int((middle_sharp@A[np.ix_(ids, ids)] % p)[0, d])
           for A in reversed(packet)]
    assert not any(alpha[M+1:]) and not any(ash[M+1:])

    def evaluate(a, c):
        b, value = 1, 0
        for r in range(M+1):
            value = (value+a[r]*b) % p
            if r < M:
                b = (b*(nodes[r]-c)*int(sine2[r])
                     *pow(int(sine2[r+1]), -1, p)) % p
        return value

    # Independent endpoint-source vs nodal retained-belt contractions.
    product, source_rows = I.copy(), []
    zz = zsharp@z % p
    for k in range(1, 4):
        product = product@zz % p
        actual = phi(L@product % p, N, pivot, p)
        expected = sum(N*m*pow(evaluate(alpha, c)*evaluate(ash, c) % p, k, p)
                       for c, m in mult.items()) % p
        assert actual == expected
        source_rows.append({'reflected_power': k, 'literal_original_source': int(actual)})
    # The cut base f has exactly the same FULL reflected product, not only values.
    f, fs = zsharp@Rm % p, z@Rp % p
    assert np.array_equal(fs@f % p, zz)
    for power in (-2, -1, 0, 1, 2):
        Rpow = I.copy()
        for _ in range(abs(power)):
            Rpow = Rpow@(Rp if power >= 0 else Rm) % p
        Rback = I.copy()
        for _ in range(abs(power)):
            Rback = Rback@(Rm if power >= 0 else Rp) % p
        assert np.array_equal(Rback@zz@Rpow % p, zz)

    # Exact weighted discrete-Chebyshev orthogonality in the same root field.
    inv2, invN = pow(2, -1, p), pow(N, -1, p)
    values = {}
    for c in mult:
        row = [1]
        if M:
            row.append(c*inv2 % p)
        for _ in range(1, M):
            row.append((c*row[-1]-row[-2]) % p)
        values[c] = row
    for k in range(M+1):
        for l in range(M+1):
            actual = invN*sum(m*values[c][k]*values[c][l] for c, m in mult.items()) % p
            expected = 0 if k != l else (1 if k == 0 else inv2)
            assert actual == expected
    # The first excluded degree is a genuine nonzero full-normal radical.
    G = I.copy()
    for c in mult:
        G = G@(O-c*I) % p
    assert np.any(G) and not np.any(G@G % p)
    assert phi(L@G@G % p, N, pivot, p) == 0
    return {'N': N, 'physical_full_Casimir_and_literal_reflection': True,
            'original_marked_complete_belt_sources': source_rows,
            'full_normal_cut_product_and_twist_interfaces': True,
            'exact_multiplicity_weighted_Chebyshev_sampling': True,
            'first_excluded_degree_retains_nonzero_root_normal': True}


def complex_sampling(N):
    M = (N-1)//2
    theta = (2*np.arange(N)+1)*np.pi/N
    C = np.cos(np.arange(M+1)[:, None]*theta)
    orth = C@C.T/N
    expected = np.diag([1]+[.5]*M)
    assert np.max(abs(orth-expected)) < 2e-13
    rng = np.random.default_rng(31000+N)
    a = rng.normal(size=M+1)+1j*rng.normal(size=M+1)
    nodes = a@C
    recon = C@nodes/N
    recon[1:] *= 2
    assert np.max(abs(recon-a)) < 1e-11
    maxnode = np.max(abs(nodes))
    for eta in (.02, .1, .3):
        value = sum(a[k]*(-1)**k*np.cosh(k*eta) for k in range(M+1))
        bound = N*np.exp(M*eta)*maxnode
        assert abs(value) <= bound*(1+1e-12)
    return {'N': N, 'complex_sampling_reconstruction_and_ellipse_bound': True}


def diagnostic(N):
    mp.mp.dps = max(100, 2*N)
    d, M = N-1, (N-1)//2
    q = mp.exp(mp.pi*1j/N)
    Q, kappa = q*q, q**(d*d/2)
    sine = [mp.mpf(1)]
    for r in range(1, N):
        sine.append(sine[-1]*2*mp.sin(mp.pi*r/N))
    weights = [2]*(M+1)
    if N % 2:
        weights[-1] = 1
    vals = []
    for j in range(M+1):
        c = 2*mp.cos((2*j+1)*mp.pi/N)
        prev, current, total = mp.mpf(0), mp.mpf(1), mp.mpf(N*N)/kappa
        for r in range(M):
            diagonal = 4*q*Q**r-q*(1+Q)*Q**(2*r)
            forward, backward = -(1-Q**(r+1))**2, -(1-Q**r)**2
            nxt = ((c-diagonal)*current-backward*prev)/forward
            prev, current = current, nxt
            v = r+1
            total += N*N*sine[2*v]*current/(sine[v]**4*kappa)
        vals.append(total)
    maxvalue = max(map(abs, vals))
    energy = N*sum(w*abs(v)**2 for w, v in zip(weights, vals))
    assert N*maxvalue**2 <= energy*(1+mp.mpf('1e-60'))
    assert energy <= N*N*maxvalue**2*(1+mp.mpf('1e-60'))
    return {'N': N, 'log_max_physical_node_over_N': mp.nstr(mp.log(maxvalue)/N, 20),
            'log_retained_belt_energy_over_N': mp.nstr(mp.log(energy)/N, 20),
            'proved_max_rate': mp.nstr(4*mp.catalan/mp.pi, 20),
            'scope': 'finite diagnostic only; proof uses fixed-ellipse lower and exact sampling'}


if __name__ == '__main__':
    out = {'status': 'PASS', 'original_source_levels': [physical_level(N) for N in range(2, 9)],
           'complex_sampling_levels': [complex_sampling(N) for N in range(2, 42)],
           'finite_rate_diagnostics': [diagnostic(N) for N in (16, 17, 32, 33, 64, 65)],
           'scope': 'Complete physical nodal-energy and literal retained-belt source theorem; '
                    'geometric belt-gluing identification is separate.'}
    Path(__file__).with_name('actual_complete_circle_nodal_energy_and_belt_sewing_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS 7 literal complete-belt source levels/21 reflected powers; '
          '40 exact-sampling complex levels; 6 finite nodal-rate diagnostics')
