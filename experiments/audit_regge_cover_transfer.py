#!/usr/bin/env python3
"""Regge period lifts and classical/quantum cover transfer.

All finite group, polynomial and split-field checks are exact.
Complex dilogarithm values check branch choices in the proved lifts.
No selected invariant of a manifold cover is identified with a
restriction-of-scalars module by these calculations.
"""

import json
import math
from collections import deque
from itertools import permutations, product
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import determinant, power
from audit_finite_sum_annihilator import field
from audit_pointed_tetrahedron_gluing import adapter, shape_field, shape_module
from audit_regular_holonomy_braiding import mm


def perm_multiply(a, b):
    return tuple(a[b[j]] for j in range(len(a)))


def perm_inverse(a):
    return tuple(a.index(j) for j in range(len(a)))


def generated_permutations(generators, size):
    identity = tuple(range(size))
    group, queue = {identity}, deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            candidate = perm_multiply(g, h)
            if candidate not in group:
                group.add(candidate)
                queue.append(candidate)
    return group


def derived_permutations(group):
    inverse = {g: perm_inverse(g) for g in group}
    commutators = {perm_multiply(perm_multiply(perm_multiply(g, h), inverse[g]), inverse[h])
                   for g in group for h in group}
    return generated_permutations(commutators, len(next(iter(group))))


def regge_group():
    edges = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]
    generators = []
    for j in range(3):
        p = list(range(4))
        p[j], p[j + 1] = p[j + 1], p[j]
        matrix = sp.zeros(6)
        for k, edge in enumerate(edges):
            target = tuple(sorted((p[edge[0]], p[edge[1]])))
            matrix[edges.index(target), k] = 1
        generators.append(sp.ImmutableMatrix(matrix))
    regge = sp.eye(6)
    for i in range(2, 6):
        for j in range(2, 6):
            regge[i, j] = sp.Rational(1, 2) - int(i == j)
    generators.append(sp.ImmutableMatrix(regge))
    identity = sp.ImmutableMatrix(sp.eye(6))
    group, queue = {identity}, deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            gh = g * h
            if gh not in group:
                group.add(gh)
                queue.append(gh)
    assert len(group) == 144
    basis = sp.zeros(6)
    for i in range(3):
        basis[i, 2 * i] = basis[i, 2 * i + 1] = sp.Rational(1, 2)
        basis[i + 3, 2 * i] = sp.Rational(1, 2)
        basis[i + 3, 2 * i + 1] = -sp.Rational(1, 2)
    inverse_basis = basis.inv()
    diagonals = [sp.Matrix(v) for v in [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]]
    pairs, ideal_actions = set(), set()
    for g in group:
        transformed = basis * g * inverse_basis
        assert transformed[:3, 3:] == sp.zeros(3)
        assert transformed[3:, :3] == sp.zeros(3)
        p, d = transformed[:3, :3], transformed[3:, 3:]
        p_action = tuple(list(p[:, j]).index(1) for j in range(3))
        d_action = tuple(diagonals.index(d * v) for v in diagonals)
        pairs.add((p_action, d_action))
        ideal_actions.add(p_action)
    assert pairs == set(product(permutations(range(3)), permutations(range(4))))
    action = {p + tuple(3 + j for j in d) for p, d in pairs}
    orders = []
    while len(action) != 1:
        orders.append(len(action))
        action = derived_permutations(action)
    orders.append(1)
    assert orders == [144, 36, 4, 1]
    return {"order": len(group), "direct_product_exactly_S3_times_S4": True,
            "derived_group_orders": orders, "ideal_image_order": len(ideal_actions),
            "ideal_kernel_order": len(group) // len(ideal_actions)}


def period_lifts():
    u, v, r = sp.symbols('u v r')
    third, sixth = sp.Rational(1, 3), sp.Rational(1, 6)

    def rho(x):
        a, b, c, epsilon = x
        return -b, a - b - epsilon, c - epsilon * b / 2 - sixth, epsilon

    def sigma(x):
        a, b, c, epsilon = x
        return b, a, -c - sixth, -epsilon

    def center(x):
        a, b, c, epsilon = x
        return a - epsilon * third, b + epsilon * third, c - epsilon * (a + b) / 6 + sp.Rational(1, 12), epsilon

    def equal(a, b):
        assert all(sp.expand(x - y) == 0 for x, y in zip(a, b))

    for epsilon in [sp.Integer(1), sp.Integer(-1)]:
        x = u, v, r, epsilon
        equal(rho(rho(rho(x))), x)
        equal(sigma(sigma(x)), x)
        equal(sigma(rho(sigma(x))), rho(rho(x)))
        a, b, c, e = center(x)
        equal(center(rho(x)), (-b, a - b, c, e))
        equal(center(sigma(x)), (b, a, -c, -e))
        # Pull back (u dv-v du)/2 under the centering and compare dr.
        a, b, c, _ = center(x)
        for variable, expected in [(u, -v / 2), (v, u / 2)]:
            pullback = (a * sp.diff(b, variable) - b * sp.diff(a, variable)) / 2
            assert sp.expand(pullback - expected - sp.diff(c - r, variable)) == 0

    a, b, c, aa, bb, cc = sp.symbols('a b c aa bb cc')

    def H(g, x):
        A, B, C = g
        x1, x2, x3 = x
        return x1 + 2 * A, x2 + 2 * B, x3 + A * x2 - B * x1 + C / 3

    equal(H((a, b, c), H((aa, bb, cc), (u, v, r))),
          H((a + aa, b + bb, c + cc + 6 * (a * bb - b * aa)), (u, v, r)))
    commutator = H((a, b, c), H((aa, bb, cc), H((-a, -b, -c), H((-aa, -bb, -cc), (u, v, r)))))
    equal(commutator, (u, v, r + 4 * (a * bb - b * aa)))
    return {"both_orientation_S3_relations_exact": True,
            "centered_determinant_twist_exact": True,
            "centered_connection_exact": True,
            "Heisenberg_group_law_and_central_commutator_exact": True}


def analytic_branches():
    mp.mp.dps = 70
    tau = mp.pi * 1j

    def data(z):
        u, v = mp.log(z), mp.log(1 - z)
        return u, v, mp.polylog(2, z) + u * v / 2

    def bloch(z):
        return mp.im(mp.polylog(2, z)) + mp.log(abs(z)) * mp.arg(1 - z)

    records = []
    for z in [mp.mpc('.2', '.3'), mp.mpc('1.3', '.4'), mp.mpc('-.7', '.2')]:
        for z in [z, mp.conj(z)]:
            epsilon = 1 if z.imag > 0 else -1
            u, v, r = data(z)
            actual_rho = data(1 / (1 - z))
            actual_sigma = data(1 - z)
            expected_rho = -v, u - v - epsilon * tau, r - epsilon * tau * v / 2 - tau**2 / 6
            expected_sigma = v, u, -r - tau**2 / 6
            error = max(abs(a - b) for a, b in zip(actual_rho + actual_sigma, expected_rho + expected_sigma))
            assert error < mp.mpf('1e-65')
            orbit = [z, 1 / (1 - z), (z - 1) / z,
                     1 - z, 1 / z, z / (z - 1)]
            assert abs(sum(bloch(w) for w in orbit)) < mp.mpf('1e-65')
            for w in orbit:
                ew = 1 if w.imag > 0 else -1
                assert abs(ew * bloch(w) - epsilon * bloch(z)) < mp.mpf('1e-65')
            records.append({"shape": [float(z.real), float(z.imag)],
                            "lift_error": float(error), "oriented_volume_descent": True,
                            "untwisted_six_sheet_sum_zero": True})
    return records


def gaussian_ordering():
    mp.mp.dps = 90
    exact, metrics = [], []
    for N in range(2, 17):
        prime, half_root, (s, t) = shape_field(N)
        for sign in [1, -1]:
            r = half_root if sign == 1 else pow(half_root, -1, prime)
            R = r * r % prime
            invN = pow(N, -1, prime)
            F = np.array([[pow(R, i * a, prime) * invN % prime for a in range(N)] for i in range(N)], dtype=np.int64)
            phase = np.diag([pow(-1, a, prime) * pow(r, a * a, prime) % prime for a in range(N)]).astype(np.int64)
            Krho = mm(prime, F, phase)
            Finv = np.array([[pow(R, -i * a, prime) * invN % prime for a in range(N)] for i in range(N)], dtype=np.int64)
            assert np.array_equal(mm(prime, F, Finv), invN * np.eye(N, dtype=np.int64) % prime)
            gauss = sum(pow(-1, a, prime) * pow(r, a * a, prime) for a in range(N)) % prime
            assert np.array_equal(power(Krho, 3, prime), gauss * pow(N, -2, prime) * np.eye(N, dtype=np.int64) % prime)
            assert gauss
            for name, K in [('rho', Krho), ('sigma', F)]:
                old, target = adapter(N, prime, (s, t, r), name)
                _, _, ptarget = shape_module(N, prime, *target)
                anchor = int((K @ ptarget % prime)[0])
                assert anchor
                assert np.array_equal(K * pow(anchor, -1, prime) % prime, old)
            exact.append({"level": N, "orientation_parameter": sign,
                          "closed_Gaussians_equal_independent_pointed_adapters": True,
                          "unpointed_cycle_phases_retained_exactly": True})

        r = mp.exp(mp.pi * 1j / N)
        R = r * r
        s = mp.mpc('.5', '.15')
        t = mp.exp(mp.log(1 - s**N) / N)

        def kernel(ss, tt, rr):
            values = [mp.mpf(1)]
            for a in range(1, N):
                values.append(values[-1] * tt / (1 - ss * rr**(2 * a)))
            return mp.matrix(values)

        psource = kernel(s, t, r)
        norm_p = mp.sqrt(sum(abs(x)**2 for x in psource))
        for name in ['rho', 'sigma']:
            if name == 'rho':
                target = (1 / t, r * s / t, r)
                K = mp.matrix([[(-1)**a * r**(a * a) * R**(i * a) / N for a in range(N)] for i in range(N)])
            else:
                target = (t, s, 1 / r)
                K = mp.matrix([[R**(i * a) / N for a in range(N)] for i in range(N)])
            pt = kernel(*target)
            image = K * pt
            h = image[0]
            assert max(abs(image[i] / h - psource[i]) for i in range(N)) < mp.mpf('1e-65')
            norm_pt = mp.sqrt(sum(abs(x)**2 for x in pt))
            predicted = norm_pt / (mp.sqrt(N) * norm_p)
            error = abs(abs(h) / predicted - 1)
            assert error < mp.mpf('1e-65')
            metrics.append({"level": N, "generator": name, "pointed_metric_relative_error": float(error)})
    return {"exact_pointed_Gaussian_cases": exact, "complex_pointed_metric_diagnostics": metrics}


def classical_cover():
    a, b, c, d, U, V = sp.symbols('a b c d U V')
    Up, Vp = a * U + b * V, c * U + d * V
    for variable in [U, V]:
        left = sp.expand(Up * sp.diff(Vp, variable) - Vp * sp.diff(Up, variable))
        right = (a * d - b * c) * (U * sp.diff(V, variable) - V * sp.diff(U, variable))
        assert sp.expand(left - right) == 0
    m, u, L, q = sp.symbols('m u L q')
    results = []
    for k in range(2, 7):
        image = sp.resultant(m**k - u, L - 1 - m, m)
        assert sp.expand(image - ((L - 1)**k - u)) == 0
        assert sp.rem(image.subs(u, m**k), L - 1 - m, L) == 0
        Z = sp.zeros(k)
        for j in range(k - 1):
            Z[j + 1, j] = 1
        Z[0, k - 1] = u
        D = sp.diag(*(q**j for j in range(k)))
        B_res = (sp.eye(k) + Z) * D
        classical = sp.expand((L * sp.eye(k) - B_res.subs(q, 1)).det())
        assert sp.expand(classical - image) == 0
        results.append({"degree": k, "toy_image_polynomial": str(image),
                        "quantum_restriction_classical_symbol_matches_norm": True})
    return {"all_integer_peripheral_regulator_formulas_exact": True,
            "cyclic_elimination_and_restriction_examples": results}


def root_transfer(N, k):
    prime, _, half_root = field(N)
    Q = half_root * half_root % prime
    ident = np.eye(k, dtype=np.int64)
    D = np.diag([pow(Q, j, prime) for j in range(k)]).astype(np.int64)

    def Z(u):
        matrix = np.zeros((k, k), dtype=np.int64)
        for j in range(k - 1):
            matrix[j + 1, j] = 1
        matrix[0, k - 1] = u
        return matrix

    g = math.gcd(N, k)
    length = N // g
    for u in [2, 3]:
        whole, short = ident.copy(), ident.copy()
        for j in range(N):
            coefficient = mm(prime, ident + Z(u * pow(Q, k * j, prime) % prime), D)
            whole = mm(prime, whole, coefficient)
            if j < length:
                short = mm(prime, short, coefficient)
        c = pow(-1, N, prime)
        expected = (ident - c * power(Z(u), N, prime)) % prime
        assert np.array_equal(whole, expected)
        assert np.array_equal(power(short, g, prime), expected)
        # Norm across all deck branches; repeated sectors appear if gcd>1.
        for value in range(k + 1):
            norm = (pow(value - 1, k // g, prime)
                    - pow(-c, k // g, prime) * pow(u, N // g, prime)) % prime
            norm = pow(norm, g, prime)
            assert determinant(value * ident - whole, prime) == norm
    return {"root_order": N, "cover_degree": k, "gcd": g,
            "cover_orbit_length": length,
            "whole_monodromy_is_restricted_base_monodromy": True,
            "short_orbit_power_and_repeated_norm_sectors_exact": True}


def quantum_peripheral_maps():
    records = []
    matrices = [(3, 0, 0, 1), (2, 1, 1, 2), (1, 2, 0, 3), (2, 1, -1, 1)]
    for N in [5, 6, 8]:
        prime, _, half_root = field(N)
        Q = half_root * half_root % prime
        m = np.zeros((N, N), dtype=np.int64)
        for j in range(N):
            m[(j + 1) % N, j] = 1
        l = np.diag([pow(Q, j, prime) for j in range(N)]).astype(np.int64)

        def W(a, b):
            return pow(half_root, a * b, prime) * mm(prime, power(m, a % N, prime), power(l, b % N, prime)) % prime

        for a, b, c, d in matrices:
            degree = a * d - b * c
            mp_, lp_ = W(a, b), W(c, d)
            assert np.array_equal(mm(prime, lp_, mp_), pow(Q, degree, prime) * mm(prime, mp_, lp_) % prime)
            records.append({"root_order": N, "peripheral_matrix": [[a, b], [c, d]],
                            "degree": degree, "cover_parameter_order": N // math.gcd(N, degree),
                            "retained_half_phase_commutation_exact": True})
    return records


def main():
    group = regge_group()
    lifts = period_lifts()
    analytic = analytic_branches()
    gaussian = gaussian_ordering()
    classical = classical_cover()
    roots = [root_transfer(N, k) for N in range(2, 11) for k in range(2, 7)]
    peripheral = quantum_peripheral_maps()
    result = {"scope": "Classical ideal period group and exact module transfers; no selected cover-state or Kashaev volume comparison.",
              "regge_group": group, "period_group": lifts, "branch_diagnostics": analytic,
              "quantum_ordering_Gaussians": gaussian,
              "classical_cover_and_norm": classical, "root_restriction_checks": roots,
              "quantum_peripheral_maps": peripheral}
    path = Path(__file__).with_name('regge_cover_transfer_results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({"result": str(path), "regge_group_order": group['order'],
                      "ideal_action_order": group['ideal_image_order'],
                      "exact_root_transfer_cases": len(roots),
                      "noncoprime_root_cases": sum(r['gcd'] > 1 for r in roots),
                      "quantum_peripheral_cases": len(peripheral),
                      "exact_pointed_Gaussian_cases": len(gaussian['exact_pointed_Gaussian_cases']),
                      "dilogarithm_branch_cases": len(analytic)}, indent=2))


if __name__ == '__main__':
    main()
