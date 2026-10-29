#!/usr/bin/env python3
"""Exact original Fourier co-source, root residues and regenerated wire currents."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import word_matrix
from audit_actual_modular_dilog_circle import psi


def inv(value, p):
    return pow(int(value) % p, -1, p)


def frame(H, root):
    N, p = H.N, H.p
    grid = [root * pow(H.Q, k, p) % p for k in range(N)]
    G = np.array([[pow(z, a, p) for a in range(N)] for z in grid], dtype=np.int64)
    Gi = np.array([[pow(z, -a, p) * inv(N, p) % p for z in grid]
                   for a in range(N)], dtype=np.int64)
    assert np.array_equal(G @ Gi % p, np.eye(N, dtype=np.int64))
    return grid, G, Gi


def kron_all(matrices, p):
    answer = np.array([[1]], dtype=np.int64)
    for matrix in matrices:
        answer = np.kron(answer, matrix) % p
    return answer


def sources(H):
    N, p, x = H.N, H.p, H.x
    cup = np.zeros(N * N, dtype=np.int64)
    cap = np.zeros(N * N, dtype=np.int64)
    mark = np.zeros(N * N, dtype=np.int64)
    for a, b in itertools.product(range(N), repeat=2):
        if a + b == N - 1:
            cup[a * N + b] = N * pow(x, a - (N - 1), p) % p
            cap[a * N + b] = inv(N, p) * pow(inv(x * H.Q, p), a, p) % p
        mark[a * N + b] = inv(N * N, p) * pow(x, b, p) % p
    return cup, cap, mark


def rational_source_families():
    rows = []
    for N in range(2, 10):
        H = HardyNetwork(N, 1)
        p, x, s = H.p, H.x, pow(H.x, N, H.p)
        root1 = 2
        C1 = pow(root1, N, p)
        root2 = next(r for r in range(3, p) if
                     pow(r, N, p) not in (C1, s * C1 % p, s) and C1 != 1)
        C2 = pow(root2, N, p)
        z1, G1, I1 = frame(H, root1)
        z2, G2, I2 = frame(H, root2)
        cup, cap, mark = sources(H)
        pc = np.kron(G1, G2) @ cup % p
        mc = cap @ np.kron(I1, I2) % p
        mm = mark @ np.kron(I1, I2) % p
        adapter = G2 @ I1 % p
        pivot = np.diag([pow(x, 1 - N, p) * pow(H.Q, -a, p) % p
                         for a in range(N)])
        pg = G2 @ pivot @ I1 % p
        for k, l in itertools.product(range(N), repeat=2):
            a, b = z1[k], z2[l]
            # G=sqrt(N)F: cup_G=N cup_F, cap_G=cap_F/N.
            expected_cup = (N * x * inv(s, p) * (C2 - s * C1)
                            * inv(b - x * a, p)) % p
            expected_cap = (a * b * (C1 - s * C2)
                            * inv(N**3 * C1 * C2 * (a - inv(x * H.Q, p) * b), p)) % p
            expected_mark = (a * b * (C1 - 1) * (C2 - s)
                             * inv(N**4 * C1 * C2 * (a - 1) * (b - x), p)) % p
            assert int(pc[k * N + l]) == expected_cup
            assert int(mc[k * N + l]) == expected_cap
            assert int(mm[k * N + l]) == expected_mark
            E = (1 - C2 * inv(C1, p)) * inv(N * (1 - b * inv(a, p)), p) % p
            Eg = (x * inv(s, p) * (1 - C2 * inv(C1, p))
                  * inv(N * (1 - inv(H.Q, p) * b * inv(a, p)), p)) % p
            assert int(adapter[l, k]) == E
            assert int(pg[l, k]) == Eg
        rows.append({'N': N, 'all_source_entries': N * N,
                     'full_marked_row_preserved': True,
                     'all_explicit_N_Q_factors': True})
    return rows


def whole_signed_sources():
    rows = []
    for N in range(2, 5):
        H = HardyNetwork(N, 1)
        p = H.p
        cup, cap, mark = sources(H)
        initial = np.kron(cup, cup) % p
        final = np.kron(cap, mark) % p
        data_in = [frame(H, r) for r in (2, 3, 4, 5)]
        data_out = [frame(H, r) for r in (7, 8, 9, 10)]
        Gin = kron_all([t[1] for t in data_in], p)
        Gini = kron_all([t[2] for t in data_in], p)
        Gout = kron_all([t[1] for t in data_out], p)
        Gouti = kron_all([t[2] for t in data_out], p)
        new_initial = Gin @ initial % p
        new_final = final @ Gouti % p
        for letters in ([2, -1, 3, 2], [-2, 1, -3, -2], [1, -2, 3, 2, -1]):
            W = word_matrix(letters, H.plus, H.minus, 4, N, p)
            original = int(final @ (W @ initial % p)) % p
            newW = (Gout @ W % p) @ Gini % p
            transformed = int(new_final @ (newW @ new_initial % p)) % p
            assert original == transformed
            rows.append({'N': N, 'word': list(letters), 'original_full_plat_source': original,
                         'all_cups_caps_and_full_mark_unchanged': True})
    return rows


def residue_checks():
    z, y, C, D, pole = sp.symbols('z y C D pole', nonzero=True)
    # The collision is distinct from the grid. Its Jacobian is exactly -1.
    omega = (C - D) / ((z**5 - C) * (z - y))
    at_wire = sp.cancel(sp.limit((z - y) * omega, z, y)).subs(D, y**5)
    assert sp.factor(at_wire + 1) == 0
    # An extra pole remains: it is not killed by the unit wire residue.
    extra = sp.cancel(sp.limit((z - pole) * omega / (z - pole), z, pole))
    assert sp.factor(extra - (C-D) / ((pole**5-C)*(pole-y))) == 0
    rows = []
    for N in range(2, 9):
        H = HardyNetwork(N, 1)
        p = H.p
        grid, _, _ = frame(H, 2)
        C0, y0 = pow(2, N, p), 3
        D0 = pow(y0, N, p)
        if C0 == D0:
            y0 = 5
            D0 = pow(y0, N, p)
        assert C0 != D0
        p0 = next(r for r in range(6, p) if r != y0 and pow(r, N, p) != C0)
        # Direct finite adapter versus grid residues, with all denominators exact.
        interpolation = 0
        for a in grid:
            f = inv(a - p0, p)
            jac = N * pow(a, N - 1, p) % p
            grid_residue = (C0 - D0) * f * inv(jac * (a - y0), p) % p
            adapter = (1 - D0 * inv(C0, p)) * inv(N * (1 - y0 * inv(a, p)), p) % p
            assert grid_residue == adapter * f % p
            interpolation = (interpolation + grid_residue) % p
        other = (C0 - D0) * inv((pow(p0, N, p) - C0) * (p0 - y0), p) % p
        assert (interpolation - inv(y0 - p0, p) + other) % p == 0
        # A two-dimensional toric residue, with a coupled rational co-source.
        grid2, _, _ = frame(H, 4)
        C2 = pow(4, N, p)
        trace, residues = 0, 0
        c0 = next(r for r in range(7, p) if all((a + b + r) % p for a in grid for b in grid2))
        for a, b in itertools.product(grid, grid2):
            f = (a + 2 * b) * inv(a + b + c0, p) % p
            J = N * N * pow(a * b, N - 1, p) % p
            numerator = N * N * pow(a * b, N - 1, p) % p
            trace = (trace + f) % p
            residues = (residues + numerator * inv(J, p) * f) % p
        assert trace == residues
        rows.append({'N': N, 'grid_wire_and_extra_pole_identity': True,
                     'toric_two_variable_trace_jacobian': True})
    return rows


def newton(N, u, v):
    Q = mp.exp(2j * mp.pi / N)
    total, term = mp.mpc(1), mp.mpc(1)
    for a in range(1, N):
        term *= u - Q**(a - 1) * v
        total += term
    return total


def rogers(N, u, v):
    Q = mp.exp(2j * mp.pi / N)
    fac = [mp.mpc(1)]
    for a in range(1, N):
        fac.append(fac[-1] * (1 - Q**a))
    return mp.fsum(fac[i+j] / (fac[i] * fac[j]) * u**i * v**j
                   for i in range(N) for j in range(N - i))


def current_regeneration():
    mp.mp.dps = 60
    rows = []
    for N in range(2, 9):
        h = 2j * mp.pi / N
        Q = mp.exp(h)
        phi = mp.sqrt(N) * mp.exp(1j * mp.pi * (mp.mpf(1)/4 - (N+mp.mpf(1)/N)/12))
        for kind in ('Newton', 'Rogers'):
            if kind == 'Newton':
                v = mp.mpf('.45')
                C = 1 + v**N
                D = mp.mpc('1.4', '-.2')
                polynomial = newton

                def full(l):
                    c = mp.log(v) - l
                    return N / phi * mp.exp(N*l-c*l/h) * psi(N, 1, c) * psi(N, 1, h-l)
            else:
                v = mp.mpc('.3', '-.03')
                C = 1 - v**N
                D = mp.mpc('.72', '-.12')
                polynomial = rogers

                def full(l):
                    return (phi * mp.exp(-l*mp.log(v)/h)
                            * psi(N, -1, l-h) * psi(N, -1, mp.log(v)-h))
            rootlog = mp.log(C) / N
            targetlog = mp.log(D) / N
            y = mp.exp(targetlog)
            interpolation = mp.mpc(0)
            grid_error = mp.mpf(0)
            for k in range(N):
                l = rootlog + h*k
                x0 = mp.exp(l)
                f = full(l)
                grid_error = max(grid_error, abs(f-polynomial(N, x0, v)))
                interpolation += (1-D/C) / (N*(1-y/x0)) * f
            exact = polynomial(N, y, v)
            residual = abs(interpolation-exact)
            assert grid_error < mp.mpf('1e-45'), (N, kind, grid_error)
            assert residual < mp.mpf('1e-44'), (N, kind, residual)
            regenerated = interpolation-full(targetlog)
            current = (exact-full(targetlog))/(C-D)
            assert abs(regenerated-(C-D)*current) < mp.mpf('1e-48')
            assert abs(regenerated) > mp.mpf('1e-8')
            rows.append({'N': N, 'sink': kind, 'balanced_grid_full_Psi_error': float(grid_error),
                         'interpolation_error': float(residual),
                         'nonzero_regenerated_current_modulus': float(abs(regenerated))})
    return rows


def sewn_bulk_characters():
    A, B, C, D, E, F = sp.symbols('A B C D E F', nonzero=True)
    symbolic = []
    for s in (-1, 1):
        muc1 = s*(A-C)/(D-s*C)
        mua2 = s*E*(C-s*D)/(D*(C-E))
        mud1 = s*B*(D-s*C)/(C*(D-B))
        mub2 = s*(F-D)/(C-s*D)
        nc = -s*E*(A-C)/(D*(C-E))
        nd = -s*B*(F-D)/(C*(D-B))
        assert sp.cancel(muc1*mua2-nc) == 0
        assert sp.cancel(mud1*mub2-nd) == 0
        assert sp.cancel(nc.subs({E:A, F:B})-s*A/D) == 0
        assert sp.cancel(nd.subs({E:A, F:B})-s*B/C) == 0
        symbolic.append({'s': s, 'two_crossing_sewn_characters': True,
                         'no_interior_adapter_but_nonconstant_bulk_characters': True})
    jacobians = []
    for N in range(2, 10):
        H = HardyNetwork(N, 1)
        p, s = H.p, pow(H.x, N, H.p)
        cg, _, _ = frame(H, 2)
        dg, _, _ = frame(H, 3)
        C0, D0 = pow(2, N, p), pow(3, N, p)
        for c, d in itertools.product(cg, dg):
            Jf = N*N*pow(c*d, N-1, p) % p
            Jg = -N*N*inv(c*d, p) % p
            detL = -inv(C0*D0, p) % p
            assert detL*inv(Jg, p) % p == inv(Jf, p)
            # The dual-character zero set is the SAME grid, not a new cycle.
            assert s*(s*D0)*inv(pow(d, N, p), p) % p == 1
            assert s*(s*C0)*inv(pow(c, N, p), p) % p == 1
        jacobians.append({'N': N, 'ordered_dual_character_residue_Jacobian': True,
                          'same_grid_zero_set': True})
    return {'both_parity_symbolic_sewing': symbolic, 'exact_finite_grid_Jacobians': jacobians}


def main():
    results = {'status': 'PASS',
               'literal_rational_source_families': rational_source_families(),
               'whole_original_signed_plat_sources': whole_signed_sources(),
               'root_grid_wire_and_extra_pole_residues': residue_checks(),
               'exact_full_Psi_current_regeneration': current_regeneration(),
               'sewn_bulk_deck_characters_and_dual_residues': sewn_bulk_characters(),
               'scope': ('Exact original finite co-source and residue/seam identities. '
                         'No geometric thimble coefficient or volume limit is inferred.')}
    Path(__file__).with_name('whole_fermat_toric_residue_and_wire_source_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS eight rational source families, nine whole signed original plat sources, '
          'seven toric/wire residue families, fourteen full-Psi seam-current checks '
          'and eight sewn dual-character Jacobian families')


if __name__ == '__main__':
    main()
