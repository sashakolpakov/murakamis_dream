"""Actual R composition and the canonical Hermite triangle-bound obstruction.

Finite original matrices are tested independently of the root Casimir
interpolation. The real-coefficient block checks the new inequality;
neither block asserts a phase-preserving global asymptotic.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_homogeneous_casimir_face_source import homogeneous
from audit_actual_small_circle_polynomial_face_insertion import Local
from audit_actual_braided_two_cut_source_adapter import original_crossings


def compose(F, G, d, p):
    out = {}
    for (a, i, t, b), v in F.items():
        for (aa, ii, tt, bb), w in G.items():
            if t + ii == d:
                e = (a + aa, i, tt, b + bb)
                out[e] = (out.get(e, 0) + v * w) % p
    return {e: v for e, v in out.items() if v}


def original_powers():
    counts = dict(powers=0, original_physical_entries=0,
                  wrong_unwrapped_zeros=0, composition_coefficients=0)
    for N in range(3, 7):
        loc = Local(N)
        p, q, Q, d = loc.p, loc.q, loc.Q, loc.d
        _, _, _, Rs = original_crossings(N)
        for eps in (-1, 1):
            H = homogeneous(loc, 1, 0)
            base = {e: v * pow(loc.eta, eps * d * d, p) % p
                    for e, v in homogeneous(loc, 1, eps).items()}
            op = np.eye(N * N, dtype=np.int64)
            step = Rs[0 if eps > 0 else 1][0]
            for n in range(1, 6):
                H = compose(base, H, d, p)
                op = step @ op % p
                if n not in (2, 3, 5):
                    continue
                for u in range(N):
                    for v in range(N):
                        x = -q * pow(Q, u, p) % p
                        y = -pow(q, -1, p) * pow(Q, -v, p) % p
                        for r in range(N):
                            s = (u + v - r) % N
                            delta = r - u
                            c = pow(Q, -delta, p)
                            value = sum(co * pow(x, a, p) * pow(c, t, p)
                                        * pow(y, b, p)
                                        for (a, i, t, b), co in H.items()) % p
                            pred = (value * pow(N, -1, p)
                                    * pow(q, -d * delta, p)
                                    * pow(c, -d, p)) % p
                            assert pred == int(op[r * N + s, u * N + v])
                            counts['original_physical_entries'] += 1
                            if r + s != u + v:
                                assert pred == 0
                                counts['wrong_unwrapped_zeros'] += 1
                counts['powers'] += 1
                counts['composition_coefficients'] += len(H)
    return counts


def real_omega_powers(N):
    """Literal Omega=-T action, with all physical lowering endpoints."""
    d = N - 1
    sine = [2 * mp.sin(mp.pi * j / N) for j in range(N)]
    clock = [2 * mp.cos(mp.pi * (2 * j + 1) / N) for j in range(N)]
    powers = [{(0, j, d - j, 0): mp.mpf(1) for j in range(N)}]
    for k in range(1, N):
        out = {}
        def add(e, value):
            out[e] = out.get(e, mp.mpf(0)) + value
        for (a, i, t, b), value in powers[-1].items():
            add((a, i, t, b), clock[i] * value)
            if i >= 1:
                add((a + 1, i - 1, t, b), -sine[i]**2 * value)
                add((a, i - 1, t, b + 1), -sine[i]**2 * value)
            if i >= 2:
                add((a + 1, i - 2, t, b + 1),
                    -sine[i] * sine[i - 1] * value)
        powers.append(out)
    return powers


def kernel(coefficients, powers):
    out = {}
    for co, power in zip(coefficients, powers):
        for e, value in power.items():
            out[e] = out.get(e, mp.mpf(0)) + co * value
    return out


def hermite_envelopes():
    z = sp.symbols('z')
    counts = dict(levels=0, canonical_node_data=0, envelope_coefficients=0,
                  power_envelope_coefficients=0, paired_ratio_checks=0,
                  gaussian_values=0, gaussian_derivatives=0, odd_simple_values=0)
    max_error = mp.mpf(0)
    max_ratio_over_N2 = mp.mpf(0)
    tol = mp.mpf('1e-65')
    for N in range(3, 13):
        d = N - 1
        nodes = [(a, 2 * mp.cos(mp.pi * (2 * a + 1) / N))
                 for a in range(N // 2)]
        data = [(c, j) for a, c in nodes for j in (0, 1)]
        if N % 2:
            data.append((mp.mpf(-2), 0))
        V = mp.matrix([[c**k if derivative == 0 else
                        (k * c**(k - 1) if k else mp.mpf(0))
                        for k in range(N)] for c, derivative in data])
        inverse = V**-1
        ident = V * inverse
        max_error = max(max_error, max(abs(ident[i, j] - int(i == j))
                                      for i in range(N) for j in range(N)))
        counts['canonical_node_data'] += N * N
        powers = real_omega_powers(N)
        basis = [kernel([inverse[k, j] for k in range(N)], powers)
                 for j in range(N)]
        lp = sp.Poly((-1)**d * sp.chebyshevu(d, z / 2), z)
        L = kernel([mp.mpf(int(lp.nth(k))) for k in range(N)], powers)
        keys = set().union(*(H.keys() for H in basis))
        gamma = []
        for a, c in nodes:
            h = 2 * a + 1
            phi = mp.pi * h / N
            g = -(N - h) / (4j * mp.sin(phi))
            gamma.append(g)
            derivative = mp.polyval([int(v) for v in sp.Poly(sp.diff(lp.as_expr(), z), z).all_coeffs()], c)
            expected = N / (2 * mp.sin(phi)**2)
            max_error = max(max_error, abs(abs(derivative) / expected - 1))
            ratio = expected / abs(g)
            assert ratio <= N**2 + tol
            max_ratio_over_N2 = max(max_ratio_over_N2, ratio / N**2)
            counts['paired_ratio_checks'] += 1
        for n in (-5, -2, -1, 1, 2, 5):
            E = {e: mp.mpf(0) for e in keys}
            values = []
            for j, (a, c) in enumerate(nodes):
                phi = mp.pi * (2 * a + 1) / N
                q = mp.exp(mp.pi * 1j / N)
                nu = (-1)**a * q**(a * (a + 1))
                full = q**(n * d * d / 2) * nu**n
                hbar = 2 * mp.pi * 1j / N
                kval = -(phi - mp.pi)**2
                gaussian = mp.exp(mp.pi * 1j * n * d * d / (4 * N)
                                  + n * kval / (2 * hbar))
                max_error = max(max_error, abs(full - gaussian))
                kd = (phi - mp.pi) / mp.sin(phi)
                max_error = max(max_error, abs(n * kd / (2 * hbar) - n * gamma[j]))
                counts['gaussian_values'] += 1
                counts['gaussian_derivatives'] += 1
                values.extend((nu**n, n * gamma[j] * nu**n))
                for e in keys:
                    E[e] += abs(basis[2*j].get(e, 0))
                    E[e] += abs(n * gamma[j]) * abs(basis[2*j+1].get(e, 0))
            if N % 2:
                a = d // 2
                nu = (-1)**a * mp.exp(mp.pi * 1j * a * (a + 1) / N)
                values.append(nu**n)
                full = mp.exp(mp.pi * 1j * n * d * d / (2 * N)) * nu**n
                gaussian = mp.exp(mp.pi * 1j * n * d * d / (4 * N))
                simple_L = sum(mp.mpf(int(lp.nth(k))) * (-2)**k for k in range(N))
                max_error = max(max_error, abs(full - gaussian), abs(simple_L - N))
                counts['odd_simple_values'] += 1
                for e in keys:
                    E[e] += abs(basis[-1].get(e, 0))
            F = {e: sum(values[j] * basis[j].get(e, 0) for j in range(N))
                 for e in keys}
            for e in keys:
                scale = max(mp.mpf(1), N**2 * E[e], abs(L.get(e, 0)))
                assert L.get(e, 0) >= -tol * scale
                assert L.get(e, 0) <= N**2 * E[e] + tol * scale
                assert abs(F[e]) <= E[e] + tol * scale
                counts['envelope_coefficients'] += 1
                counts['power_envelope_coefficients'] += 1
        counts['levels'] += 1
    assert max_error < tol
    return dict(counts=counts, maximum_exact_comparison_error=str(max_error),
                maximum_ratio_divided_by_N_squared=str(max_ratio_over_N2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'actual_direct_long_power_source_results.json'))
    args = parser.parse_args()
    mp.mp.dps = 90
    result = dict(status='PASS', precision=mp.mp.dps,
                  original_source=original_powers(), hermite=hermite_envelopes(),
                  scope='Exact original root composition and canonical Hermite-envelope comparison. '
                        'No generic-q, selected-cycle, or phase-preserving global rate assertion.')
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
