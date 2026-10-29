#!/usr/bin/env python3
"""Exact checks of the actual crossing's relative tetrahedral presentation.

This audits an algebraic rewrite of the already fixed ADO/Kashaev state,
not a new invariant.  Symbolic geometry, finite fields, and complex
products check different parts of the derivation.  The final numerical
checks illustrate a proved local upper bound, not the volume conjecture.
"""

import json
from collections import Counter
from itertools import combinations
from math import prod
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.special import spence

from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices


def pochhammer_mod(u, base, length, prime):
    result = 1
    for j in range(length):
        result = result*(1-u*pow(base, j, prime)) % prime
    return result


def root_factorials(base, level, prime):
    values = [1]
    for j in range(1, level):
        values.append(values[-1]*(1-pow(base, j, prime)) % prime)
    return values


def rewritten_crossing(a, b, k, sign, q, x, factorials, prime):
    """The exact generic-q five-Pochhammer formulas, including phases."""
    base = q*q % prime
    start = a if sign > 0 else b
    gaussian_binomial = (factorials[start]*pow(factorials[k], -1, prime)
                         *pow(factorials[start-k], -1, prime)) % prime
    atom = pochhammer_mod(x*x*pow(base, 1-start, prime) % prime,
                          base, k, prime)
    if sign > 0:
        phase = (pow(-1, k, prime)*pow(x, -a-b-k, prime)
                 *pow(base, a*b+(a-b)*k-k*(k+1)//2, prime)) % prime
    else:
        phase = pow(x, a+b-k, prime)*pow(base, -a*b, prime) % prime
    return phase*gaussian_binomial*atom % prime


def crossing_check(level):
    prime, generic, root = field(level)
    records = []
    for at_root, q in ((False, generic), (True, root)):
        base = q*q % prime
        factorials = root_factorials(base, level, prime)
        colors = [("generic", pow(generic, level+7, prime))]
        if at_root:
            colors.append(("Kashaev", pow(q, level-1, prime)))
        for label, x in colors:
            positive, negative, _, _ = color_matrices(level, prime, q, x)
            checked = contiguities = kashaev_squares = peripheral_contiguities = 0
            for sign, old in ((1, positive), (-1, negative)):
                new = np.zeros_like(old)
                for a in range(level):
                    for b in range(level):
                        maximum = (min(a, level-1-b) if sign > 0
                                   else min(b, level-1-a))
                        for k in range(maximum+1):
                            value = rewritten_crossing(a, b, k, sign, q, x,
                                                       factorials, prime)
                            c, d = ((b+k, a-k) if sign > 0 else (b-k, a+k))
                            new[c*level+d, a*level+b] = value
                            checked += 1
                            if sign > 0:
                                A, B, C = (pow(base, a, prime), pow(base, b, prime),
                                           pow(base, k, prime))
                                X = x*x % prime
                                if a+1 < level:
                                    numerator = (B*C*pow(x, -1, prime)*(1-base*A)
                                                 *(1-X*pow(A, -1, prime))) % prime
                                    denominator = ((1-base*A*pow(C, -1, prime))
                                                   *(1-X*C*pow(A, -1, prime))) % prime
                                    adjacent = rewritten_crossing(a+1, b, k, sign,
                                                                  q, x, factorials, prime)
                                    assert denominator*adjacent % prime == numerator*value % prime
                                    peripheral_contiguities += 1
                                if b+1+k < level:
                                    adjacent = rewritten_crossing(a, b+1, k, sign,
                                                                  q, x, factorials, prime)
                                    assert adjacent == A*pow(C*x % prime, -1, prime)*value % prime
                                    peripheral_contiguities += 1
                                shifted = rewritten_crossing(a, b, k, sign, q,
                                                             q*x % prime, factorials, prime)
                                numerator = (pow(q, -a-b-k, prime)
                                             *(1-base*X*C*pow(A, -1, prime))) % prime
                                denominator = (1-base*X*pow(A, -1, prime)) % prime
                                assert denominator*shifted % prime == numerator*value % prime
                                peripheral_contiguities += 1
                            if k < maximum:
                                A, B, C = (pow(base, a, prime),
                                           pow(base, b, prime), pow(base, k, prime))
                                X = x*x % prime
                                if sign > 0:
                                    ratio = (-A*pow(base*B*C*x % prime, -1, prime)
                                             *(1-A*pow(C, -1, prime))
                                             *(1-base*X*C*pow(A, -1, prime))
                                             *pow(1-base*C, -1, prime)) % prime
                                else:
                                    ratio = (pow(x, -1, prime)*(1-B*pow(C, -1, prime))
                                             *(1-base*X*C*pow(B, -1, prime))
                                             *pow(1-base*C, -1, prime)) % prime
                                following = rewritten_crossing(a, b, k+1, sign,
                                                               q, x, factorials, prime)
                                assert following == ratio*value % prime
                                contiguities += 1
                            if label == "Kashaev":
                                start = a if sign > 0 else b
                                square = (factorials[start]**2
                                          *pow(factorials[start-k], -2, prime)
                                          *pow(factorials[k], -1, prime)) % prime
                                if sign > 0:
                                    phase = (pow(x, -a-b-k, prime)
                                             *pow(base, b*(a-k)-k, prime)) % prime
                                else:
                                    phase = (pow(-1, k, prime)*pow(x, a+b-k, prime)
                                             *pow(base, -a*b-b*k+k*(k-1)//2, prime)) % prime
                                assert value == phase*square % prime
                                kashaev_squares += 1
                assert np.array_equal(new, old)
            records.append({"root_specialized": at_root, "color": label,
                            "actual_positive_and_inverse_matrices_equal": True,
                            "entries_checked": checked,
                            "exact_contiguity_relations_checked": contiguities,
                            "positive_index_and_meridian_contiguities_checked": peripheral_contiguities,
                            "Kashaev_square_factorial_identities": kashaev_squares})
    return {"level": level, "finite_field_prime": prime, "records": records}


def face_sign(face):
    return (-1)**sum(face[i] > face[j] for i in range(len(face))
                     for j in range(i+1, len(face)))


def octahedron_check():
    A, C, X = sp.symbols("A C X")
    Z = C*(A-X)/(A-C*X)
    coordinates = {"I": sp.oo, "O": sp.Integer(0), "U": sp.Integer(1),
                   "C": C, "A": A, "Z": Z}
    tetrahedra = [("I", "O", "U", "C"), ("I", "O", "C", "A"),
                  ("I", "O", "A", "U"), ("U", "C", "O", "Z"),
                  ("U", "C", "Z", "I")]

    def cross_ratio(tetrahedron):
        v0, v1, v2, v3 = [coordinates[v] for v in tetrahedron]
        if v0 is sp.oo:
            return sp.cancel((v3-v1)/(v2-v1))
        if v3 is sp.oo:
            return sp.cancel((v2-v0)/(v2-v1))
        return sp.cancel((v3-v1)*(v2-v0)/((v3-v0)*(v2-v1)))

    expected = [C, A/C, 1/A, X/A, A/(C*X)]
    shapes = [cross_ratio(tet) for tet in tetrahedra]
    assert all(sp.cancel(left-right) == 0 for left, right in zip(shapes, expected))
    boundary = Counter()
    face_incidence = Counter()
    for tet in tetrahedra:
        for i in range(4):
            face = tet[:i]+tet[i+1:]
            boundary[tuple(sorted(face))] += (-1)**i*face_sign(face)
            face_incidence[tuple(sorted(face))] += 1
    exterior = [face for face in boundary if boundary[face]]
    interior = [face for face in boundary if not boundary[face]]
    assert len(exterior) == 8 and len(interior) == 6
    assert all(abs(boundary[face]) == 1 and face_incidence[face] == 1 for face in exterior)
    assert all(face_incidence[face] == 2 for face in interior)
    exterior_edges = {tuple(sorted(edge)) for face in exterior
                      for edge in combinations(face, 2)}
    vertices = set(coordinates)
    opposite = {tuple(sorted(pair)) for pair in combinations(vertices, 2)}-exterior_edges
    assert opposite == {("I", "O"), ("C", "U"), ("A", "Z")}
    assert sp.cancel(shapes[0]*shapes[1]*shapes[2]-1) == 0
    assert sp.cancel(shapes[0]*shapes[3]*shapes[4]-1) == 0

    # The prescribed shelling attaches a tetrahedron along one or two
    # adjacent faces at each step; these are disks, so the union is a ball.
    old_faces = set()
    attaching_face_counts = []
    for tet in tetrahedra:
        faces = {tuple(sorted(tet[:i]+tet[i+1:])) for i in range(4)}
        shared = faces & old_faces
        attaching_face_counts.append(len(shared))
        if len(shared) == 2:
            a, b = list(shared)
            assert len(set(a) & set(b)) == 2
        old_faces |= faces
    assert attaching_face_counts == [0, 1, 2, 1, 2]
    return {"sixth_vertex": str(Z), "ordered_tetrahedron_shapes": [str(z) for z in shapes],
            "internal_faces_cancelled": len(interior), "exterior_triangles": len(exterior),
            "opposite_vertex_pairs": [list(pair) for pair in sorted(opposite)],
            "internal_edge_products_equal_one": True,
            "ball_shelling_attaching_face_counts": attaching_face_counts}


def infinite_product_check():
    """Independent convergent-product check; never specialize atoms at a root."""
    mp.mp.dps = 80
    records = []
    for base in (mp.mpc("0.31", "0.09"), mp.mpc("0.47", "-0.07")):
        x = mp.mpc("0.73", "0.16")

        def atom(u):
            return mp.fprod(1-u*base**j for j in range(400))

        def finite(u, length):
            return mp.fprod(1-u*base**j for j in range(length))

        worst = mp.mpf(0)
        for a, k in ((1, 0), (2, 1), (4, 2), (6, 3), (7, 7)):
            A, C, X = base**a, base**k, x*x
            finite_value = (finite(base, a)/(finite(base, k)*finite(base, a-k))
                            *finite(base*X/A, k))
            five_atoms = (atom(base*A/C)*atom(base*C)*atom(base*X/A)
                          /(atom(base*A)*atom(base*X*C/A)*atom(base)))
            error = abs(five_atoms-finite_value)/max(1, abs(finite_value))
            assert error < mp.mpf("1e-65")
            worst = max(worst, error)
        records.append({"base": str(base), "cases": 5,
                        "maximum_relative_error": float(worst)})
    return records


def relative_source_check(level):
    prime, generator, q = field(level)
    omega = pow(q, -2, prime)
    etale_points = [pow(omega, a, prime) for a in range(level)]
    boundary = [sum(pow(omega*t % prime, r, prime) for r in range(level))
                *pow(level, -1, prime) % prime for t in etale_points]
    assert boundary == [0]*(level-1)+[1]
    assert all(e*e % prime == e for e in boundary)
    assert all((1-omega*t)*e % prime == 0 for t, e in zip(etale_points, boundary))
    good = bad = 0
    for Y in (1, pow(generator, 2*(level+5), prime), omega):
        values = [1]
        for a in range(1, level):
            values.append(values[-1]*(1-pow(omega, a, prime)*Y) % prime)
        S = sum(pow(Y, a, prime) for a in range(level)) % prime
        assert values[-1] == S
        assert (1-Y)*S % prime == (1-pow(Y, level, prime)) % prime
        following = values[1:]+values[:1]
        raw = [(1-omega*Y*t) % prime for t in etale_points]
        assert prod(raw) % prime == (1-pow(Y, level, prime)) % prime
        source = [(f-a*v) % prime for f, a, v in zip(following, raw, values)]
        assert source == [pow(Y, level, prime)*e % prime for e in boundary]
        cyclic_system = sp.zeros(level)
        for a in range(level):
            cyclic_system[a, (a+1) % level] = 1
            cyclic_system[a, a] -= raw[a]
        determinant = int(cyclic_system.det()) % prime
        assert determinant == pow(-1, level-1, prime)*pow(Y, level, prime) % prime
        assert determinant != 0
        if not S:
            bad += 1
            assert 0 in values
            continue
        good += 1
        h = pow(S, -1, prime)
        completed = [(a+pow(Y, level, prime)*h*e) % prime
                     for a, e in zip(raw, boundary)]
        assert completed[-1] == h
        assert all(f == a*v % prime for f, a, v in zip(following, completed, values))
        assert prod(completed) % prime == 1
        inverse_values = [pow(v, -1, prime) for v in values]
        inverse_following = inverse_values[1:]+inverse_values[:1]
        inverse_source = [(a*f-v) % prime
                          for a, f, v in zip(raw, inverse_following, inverse_values)]
        assert inverse_source == [-pow(Y, level, prime)*h*e % prime for e in boundary]
        if Y == 1:
            assert h == pow(level, -1, prime)

    # Independently defined modified dimension, at a generic meridian.
    M = pow(generator, level+7, prime)
    x = -pow(q, -1, prime)*M % prime
    i = pow(generator, (prime-1)//4, prime)
    eta = pow(i, level+3, prime)
    assert eta == pow(-1, level+1, prime)*pow(q, level*(1-level)//2, prime) % prime
    h = pow(sum(pow(M, 2*a, prime) for a in range(level)) % prime, -1, prime)
    from_completion = eta*pow(M, level-1, prime)*h % prime
    old_dimension = (-pow(q, level*(1-level)//2, prime)
                     *(q*x-pow(q*x, -1, prime))
                     *pow(pow(x, level, prime)-pow(x, -level, prime), -1, prime)) % prime
    assert from_completion == old_dimension
    return {"level": level, "finite_field_prime": prime,
            "boundary_idempotent_checked": True,
            "cyclic_resolvent_determinant_and_uniqueness_checked": True,
            "polynomial_source_cases": good+bad,
            "unit_completion_and_norm_one_cases": good,
            "retained_polar_divisor_cases": bad,
            "reciprocal_source_checked": True,
            "modified_dimension_is_boundary_transition_exact": True,
            "Kashaev_boundary_transition": "1/N"}


def distribution_check():
    Y = sp.symbols("Y")
    pairs = [(2, 2), (2, 3), (3, 3), (3, 4), (3, 5)]
    for a, b in pairs:
        whole = sum(Y**j for j in range(a*b))
        factored = sum(Y**j for j in range(a))*sum(Y**(a*j) for j in range(b))
        assert sp.expand(whole-factored) == 0
    return {"level_pairs": pairs, "full_polynomial_factorization_exact": True}


def bloch_circle(s):
    return np.imag(spence(1-np.exp(2j*np.pi*np.asarray(s))))


def magnitude_checks():
    records = []
    voct = float(4*mp.catalan)
    for level in (16, 31, 32, 63, 64, 127, 128, 255, 256, 512, 1024):
        j = np.arange(1, level)
        logs = np.concatenate(([0.0], np.cumsum(np.log(2*np.sin(np.pi*j/level)))))
        integral = -level*bloch_circle(np.arange(level)/level)/(2*np.pi)
        maximum_error = float(np.max(np.abs(logs-integral)))
        assert maximum_error <= 2*np.log(level)+4
        # Every pair 0<=k<=a<N; b only further restricts the allowed pairs.
        largest = -np.inf
        for a in range(level):
            k = np.arange(a+1)
            largest = max(largest, float(np.max(2*logs[a]-2*logs[a-k]-logs[k])))
        exponent = largest*2*np.pi/level
        assert exponent <= voct+5*(2*np.log(level)+4)*2*np.pi/level
        records.append({"level": level, "uniform_factorial_error": maximum_error,
                        "error_divided_by_log_N": maximum_error/np.log(level),
                        "maximum_actual_entry_exponent": exponent,
                        "octahedral_bound": voct})
    grid = np.arange(401)/400
    s, t = np.meshgrid(grid, grid, indexing="ij")
    phi = 2*bloch_circle(s-t)+bloch_circle(t)-2*bloch_circle(s)
    phi[t > s] = -np.inf
    where = np.unravel_index(np.argmax(phi), phi.shape)
    assert tuple(grid[j] for j in where) == (0.75, 0.5)
    assert abs(phi[where]-voct) < 1e-12
    return {"uniform_estimate_records": records,
            "triangular_grid_points": int(np.count_nonzero(t <= s)),
            "maximizing_pair": [0.75, 0.5], "maximum": voct,
            "scope": "Local magnitude/upper bound only; no lower bound for a knot contraction."}


def main():
    levels = (2, 3, 4, 5, 6, 8, 9, 10, 12, 15)
    result = {"scope": "Actual local crossing, canonical relative source, and classical octahedron. No global regulator-period theorem.",
              "crossings": [crossing_check(level) for level in levels],
              "octahedron": octahedron_check(),
              "convergent_five_atom_product": infinite_product_check(),
              "relative_factorial_sources": [relative_source_check(level) for level in levels],
              "normalization_distribution": distribution_check(),
              "local_norm_checks": magnitude_checks()}
    Path(__file__).with_name("relative_octahedral_period_results.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps({"crossing_levels": list(levels),
                      "crossing_entries_checked": sum(r["entries_checked"] for n in result["crossings"]
                                                      for r in n["records"]),
                      "relative_sources_checked": sum(n["polynomial_source_cases"]
                                                      for n in result["relative_factorial_sources"]),
                      "octahedron": result["octahedron"],
                      "local_volume_maximum": result["local_norm_checks"]["maximum"],
                      "all_checks_passed": True}), flush=True)


if __name__ == "__main__":
    main()
