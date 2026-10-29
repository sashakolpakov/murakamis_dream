#!/usr/bin/env python3
"""Actual pure-braid powers and their spectral source algebra.

Split-field checks verify exact identities, not infinite group density.
The characteristic-zero SL2 quotient follows from the independent
trace-sign and invariant-plane proof in the companion note.
"""

import json
from itertools import product
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import power
from audit_kashaev_ado_pointing import color_matrices
from audit_regular_holonomy_braiding import mm
from audit_sewn_source_corner import full_cut_factor, root_data


def symbolic_algebra():
    c, s, t = sp.symbols('c s t')
    zero = sp.zeros(4, 1)
    e = [sp.eye(4)[:, j] for j in range(4)]
    table = {(0, j): e[j] for j in range(4)}
    table.update({(j, 0): e[j] for j in range(4)})
    table.update({(1, 1): zero, (2, 2): zero, (1, 2): e[3],
                  (2, 1): c * e[0] - e[3], (1, 3): zero,
                  (3, 1): c * e[1], (2, 3): c * e[2],
                  (3, 2): zero, (3, 3): c * e[3]})

    def mul(a, b):
        return sp.simplify(sum((a[i] * b[j] * table[i, j] for i, j in product(range(4), repeat=2)), start=sp.zeros(4, 1)))

    for i, j, k in product(range(4), repeat=3):
        assert mul(mul(e[i], e[j]), e[k]) == mul(e[i], mul(e[j], e[k]))
    commutator = mul(mul(mul(e[0] + s * e[1], e[0] + t * e[2]), e[0] - s * e[1]), e[0] - t * e[2])
    assert (commutator - sp.Matrix([1 - s * t * c, -s**2 * t * c,
                                     s * t**2 * c, 2 * s * t + s**2 * t**2 * c])).applyfunc(sp.expand) == zero
    assert commutator.subs(c, 0) == e[0] + 2 * s * t * e[3]
    for i, j, k in product(range(1, 4), repeat=3):
        assert mul(mul(e[i], e[j]), e[k]).subs(c, 0) == zero

    X = sp.Matrix([[0, 1], [0, 0]])
    Y = sp.Matrix([[0, 0], [c, 0]])
    matrix = sp.eye(2) + s * X
    other = sp.eye(2) + t * Y
    C = sp.expand(matrix * other * (sp.eye(2) - s * X) * (sp.eye(2) - t * Y))
    assert sp.expand(sp.trace(C) - (2 + s**2 * t**2 * c**2)) == 0
    assert sp.expand(C.det()) == 1
    delta, A = sp.symbols('delta A', nonzero=True)
    T1, T2 = sp.Matrix([[delta, A], [0, 0]]), sp.Matrix([[0, 0], [A, delta]])
    z = A**2 - delta**2
    assert T1 * T2 + T2 * T1 - delta * (T1 + T2) == z * sp.eye(2)
    E11 = sp.simplify((T1 * T2 - delta * T1) / z)
    E22 = sp.simplify((T2 * T1 - delta * T2) / z)
    E12, E21 = sp.simplify((T1 - delta * E11) / A), sp.simplify((T2 - delta * E22) / A)
    assert E11 == sp.diag(1, 0) and E22 == sp.diag(0, 1)
    assert E12 == sp.Matrix([[0, 1], [0, 0]]) and E21 == sp.Matrix([[0, 0], [1, 0]])
    # The exact weighted odd-root sum used in the uniform pivotal proof.
    q = sp.symbols('q', nonzero=True)
    for N in range(2, 31):
        weighted = sum((N - h) * (q**h - q**(-h)) for h in range(1, N, 2))
        numerator = sp.expand(q**N * ((q - 1 / q) * weighted + 2 * N))
        assert sp.rem(numerator, sp.cyclotomic_poly(2 * N, q), q) == 0
    return {"flat_rank_four_algebra_associative": True,
            "zero_fiber_radical_cube_zero_and_class_two_commutator": True,
            "generic_commutator_trace_and_determinant_exact": True,
            "quadratic_spectral_cover_matrix_units_exact": True,
            "weighted_odd_root_sum_certificates_through_level": 30}


def actual_root_case(N):
    p, q, x, B, Bi, pivot, theta, cup, cap, rho, dimension = root_data(N)
    eye = np.eye(N * N, dtype=np.int64)
    J = (power(B, 2 * N, p) - eye) % p
    assert pow(theta, 2 * N, p) == 1
    assert not np.any(mm(p, J, J))
    qi = pow(q, -1, p)
    Bconj = color_matrices(N, p, qi, pow(qi, N - 1, p))[0]
    Jconj = (power(Bconj, 2 * N, p) - eye) % p
    swap = np.zeros_like(eye)
    for a, b in product(range(N), repeat=2):
        swap[b * N + a, a * N + b] = 1
    cartan = [pow(x, -a - b, p) * pow(q, 2 * a * b, p) % p
              for a, b in product(range(N), repeat=2)]
    D = np.diag(cartan).astype(np.int64)
    Di = np.diag([pow(v, -1, p) for v in cartan]).astype(np.int64)
    assert np.array_equal(Bconj, mm(p, Di, swap, Bi, swap, D))
    assert np.array_equal(Jconj, -mm(p, Di, swap, J, swap, D) % p)
    first = np.trace(J.reshape((N,) * 4), axis1=0, axis2=2) % p
    second = np.trace(J.reshape((N,) * 4), axis1=1, axis2=3) % p
    first_conj = np.trace(Jconj.reshape((N,) * 4), axis1=0, axis2=2) % p
    assert np.array_equal(second, -first_conj % p)
    assert np.array_equal(first, np.diag(np.diag(first)))
    assert np.array_equal(second, np.diag(np.diag(second)))
    diag = np.diag(J).reshape(N, N)
    K = np.array([x * pow(q, -2 * a, p) % p for a in range(N)], dtype=np.int64)
    phi = -2 * N * N * pow(rho, -1, p) % p
    weighted = np.sum(diag * K[None, :], axis=1) % p
    assert np.array_equal(weighted, phi * np.ones(N, dtype=np.int64) % p)
    assert int(np.trace(mm(p, first, np.diag(K)))) % p == N * phi % p
    L = pow(-1, N - 1, p) * phi % p
    g = np.diag(pivot)
    actual_reduced_cut = int(np.sum(diag[0, :, None] * diag * g[:, None] * g[None, :])) % p
    assert actual_reduced_cut == L * L % p
    full_cut = dimension * actual_reduced_cut % p
    assert full_cut

    # This is a separate actual localized cup/cap source test. The
    # two-copy corner is not assumed invariant under the full braid.
    little_eye = np.eye(N, dtype=np.int64)
    U = np.column_stack((np.kron(cup, little_eye), np.kron(little_eye, cup)))
    R = np.vstack((np.kron(little_eye, cap), np.kron(cap, little_eye)))
    assert np.array_equal(mm(p, R, U), np.eye(2 * N, dtype=np.int64))
    upper = np.array([[1, 1], [0, 1]], dtype=np.int64)
    lower = np.array([[1, 0], [1, 1]], dtype=np.int64)
    upper_inverse = np.array([[1, -1], [0, 1]], dtype=np.int64)
    lower_inverse = np.array([[1, 0], [-1, 1]], dtype=np.int64)
    C = mm(p, upper, lower, upper_inverse, lower_inverse)
    chebyshev = [2, 3]
    for _ in range(2, 6):
        chebyshev.append(3 * chebyshev[-1] - chebyshev[-2])
    moments = []
    for winding in [1, 2, 3, 5]:
        block = (power(C, winding, p) - np.eye(2, dtype=np.int64)) % p
        left = mm(p, U, np.kron(block, little_eye))
        value = full_cut_factor(left, R, N, 3, pivot, dimension, p)
        expected = dimension * (chebyshev[winding] - 2) % p
        assert value == expected
        moments.append({"commutator_winding": winding, "full_original_modified_cut": int(value)})
    return {"level": N, "prime": p, "actual_pure_powers_square_zero": True,
            "Cartan_conjugation_and_partial_trace_star_identities": True,
            "exact_pivotal_moment": int(phi), "full_XY_modified_cut": int(full_cut),
            "ordinary_pair_trace_reduction": int(np.trace(mm(p, first, second))) % p,
            "localized_actual_source_commutator_moments": moments}


def complex_trace_case(N):
    mp.mp.dps = 90
    q = mp.exp(mp.pi * 1j / N)
    rho, x = q - 1 / q, q**(N - 1)
    integers = [mp.mpf(0)] + [mp.sin(mp.pi * j / N) / mp.sin(mp.pi / N) for j in range(1, N)]
    factorials = [mp.mpf(1)]
    for j in range(1, N):
        factorials.append(factorials[-1] * integers[j])
    diagonal = mp.matrix(N, N)
    for degree in range(2 * N - 1):
        basis = [(a, degree - a) for a in range(N) if 0 <= degree - a < N]
        indices = {ab: j for j, ab in enumerate(basis)}
        B = mp.matrix(len(basis), len(basis))
        for column, (a, b) in enumerate(basis):
            e = mp.mpf(1)
            for k in range(min(a, N - 1 - b) + 1):
                if k:
                    e *= integers[a - k + 1]**2
                coefficient = q**(k * (k - 1) // 2) * rho**k / factorials[k]
                coefficient *= e * x**(-degree) * q**(2 * (a - k) * (b + k))
                B[indices[b + k, a - k], column] = coefficient
        J = B**(2 * N) - mp.eye(len(basis))
        for j, (a, b) in enumerate(basis):
            diagonal[a, b] = J[j, j]
    left = [sum(diagonal[a, b] for a in range(N)) for b in range(N)]
    right = [sum(diagonal[a, b] for b in range(N)) for a in range(N)]
    scale = max(mp.mpf(1), *(abs(a) for a in left))
    assert max(abs(b + mp.conj(a)) for a, b in zip(left, right)) / scale < mp.mpf('1e-65')
    negative_trace = sum(abs(a)**2 for a in left)
    literal_trace = sum(a * b for a, b in zip(left, right))
    assert abs(literal_trace + negative_trace) / negative_trace < mp.mpf('1e-65')
    phi = -2 * N * N / rho
    lower_bound = N * abs(phi)**2
    assert negative_trace >= lower_bound * (1 - mp.mpf('1e-65'))
    return {"level": N, "negative_ordinary_trace": float(-negative_trace),
            "proved_absolute_lower_bound": float(lower_bound),
            "nonzero_trace_is_a_characteristic_zero_diagnostic": True}


def main():
    algebra = symbolic_algebra()
    roots = [actual_root_case(N) for N in range(2, 17)]
    complex_cases = [complex_trace_case(N) for N in range(2, 11)]
    result = {"scope": "Uniform original-braid nonnilpotence proof and spectral-source reduction; no selected quantum-A regulator norm theorem.",
              "symbolic_spectral_algebra": algebra, "actual_crossings_and_full_cuts": roots,
              "canonical_complex_embedding_diagnostics": complex_cases}
    path = Path(__file__).with_name('actual_semisimple_transport_results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({"result": str(path), "actual_root_levels": len(roots),
                      "full_original_source_commutator_closings": sum(len(r['localized_actual_source_commutator_moments']) for r in roots),
                      "canonical_complex_trace_cases": len(complex_cases),
                      "spectral_algebra_and_quadratic_cover_certificates": True}, indent=2))


if __name__ == '__main__':
    main()
