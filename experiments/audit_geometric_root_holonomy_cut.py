#!/usr/bin/env python3
"""Literal one-cut evaluation on irreducible figure-eight root holonomy.

Exact finite-field diagnostics use the full quantum automorphism, not the
semiclassical phase equations as a substitute.  Nonzero reduction certifies
nonzero characteristic-zero evaluation on a compatible algebraic lift.
"""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path
from random import Random

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod, matrix_power, tensor_module
from audit_cyclic_steinberg_lattice import determinant
from audit_marked_braid_holonomy import (
    mm as group_mul, mi as group_inverse, conjugate, from_holonomies,
    braid_groups, braid_states, crossing_mod,
)
from audit_regular_holonomy_braiding import (
    regular_module, embed, holonomy, inverse_holonomy, mm, central,
)
from audit_closed_braid_period_line import partial_cut


ACTION = [(0, 1), (1, -1), (0, 1), (1, -1)]
OPERATOR = list(reversed(ACTION))


def primitive_data(level, lower=100):
    modulus = sp.ilcm(2 * level, 3)
    for prime in sp.primerange(lower, 100000):
        if (prime - 1) % modulus == 0:
            generator = int(sp.primitive_root(prime))
            q = pow(generator, (prime - 1) // (2 * level), prime)
            riley = [a for a in range(1, prime) if (a * a - a + 1) % prime == 0]
            if riley:
                yield int(prime), q, riley


def riley_tuple(parameter, prime):
    a = (1, 1, 0, 1)
    b = (1, 0, parameter, 1)
    c = group_mul(group_mul(group_mul(group_mul(
        group_inverse(a, prime), b, prime), a, prime),
        group_inverse(b, prime), prime), a, prime)
    result = [a, b, c]
    assert braid_groups(result, ACTION, prime) == result
    # Noncommuting parabolics with distinct fixed lines: irreducible over Fbar.
    assert parameter != 0
    return result


def center_admissible(states, prime):
    current = list(states)
    for j, sign in OPERATOR:
        # Algebra pullback checked center map is inverse to the positive
        # classical step, so signs are reversed here.
        current[j:j + 2] = crossing_mod(current[j], current[j + 1], prime, -sign)
        if any(k == 0 for k, _, _ in current):
            return False
    return current == states


def global_images(original, prime, q):
    values = list(original)
    for j, sign in OPERATOR:
        left, right = values[j:j + 2]
        if sign > 0:
            values[j:j + 2] = holonomy(right, left, prime, q)
        else:
            a, b = inverse_holonomy(left, right, prime, q)
            values[j:j + 2] = (b, a)
    return values


def matrix_unit_frame(initial, images, roots, level, prime):
    size = level ** len(initial)
    eye = np.eye(size, dtype=np.int64)
    projector = eye.copy()
    for image, root in zip(images, roots):
        normalized = image[2] * pow(root, -1, prime) % prime
        power = eye.copy()
        total = np.zeros_like(eye)
        for _ in range(level):
            total = (total + power) % prime
            power = mm(prime, power, normalized)
        projector = mm(prime, projector, total * pow(level, -1, prime) % prime)
    anchor = next(j for j in range(size) if np.any(projector[:, j]))
    vector = projector[:, anchor:anchor + 1]
    powers = [[matrix_power(image[1], j, prime) for j in range(level)]
              for image in images]
    columns = []
    for indices in product(range(level), repeat=len(initial)):
        column = vector
        for matrices, j in zip(powers, indices):
            column = mm(prime, matrices[j], column)
        columns.append(column[:, 0])
    frame = np.column_stack(columns)
    assert determinant(frame, prime)
    for before, after in zip(initial, images):
        for a, b in zip(before, after):
            assert np.array_equal(mm(prime, b, frame), mm(prime, frame, a))
    return frame, anchor


def one_case(level, embedding=0, seed=0):
    delta = (-1) ** (level - 1)
    rng = Random(29317 + 193 * level + seed)
    attempts = 0
    for prime, q, riley_roots in primitive_data(level):
        parameter = riley_roots[embedding % 2]
        mu = riley_tuple(parameter, prime)
        roots = {pow(a, level, prime): a for a in range(1, prime)}
        rho = (q - pow(q, -1, prime)) % prime
        for _ in range(3000):
            attempts += 1
            r, s = rng.randrange(prime), rng.randrange(1, prime)
            basis = (r, (1 - r) % prime, s, -s % prime)
            groups = [tuple(delta * a % prime for a in conjugate(
                group_inverse(basis, prime), value, prime)) for value in mu]
            try:
                states = from_holonomies(groups, prime)
                if any(not k or not e or not f or k not in roots
                       or k == delta % prime for k, e, f in states):
                    continue
                if not center_admissible(states, prime):
                    continue
                xs = [roots[k] for k, _, _ in states]
                modules = [regular_module(
                    level, prime, q, x, -2 % prime,
                    e * pow(rho, -level, prime) % prime,
                    -f * pow(rho, -level, prime) % prime)
                    for x, (_, e, f) in zip(xs, states)]
                original = [embed(modules, j) for j in range(3)]
                images = global_images(original, prime, q)
                for before, after in zip(original, images):
                    assert central(before, level, prime, q) == central(
                        after, level, prime, q)
                frame, anchor = matrix_unit_frame(
                    original, images, xs, level, prime)
            except (ValueError, StopIteration, ZeroDivisionError):
                continue
            # Intertwining the full algebra automorphism must preserve its
            # literal diagonal coproduct, hence the actual cut is scalar.
            total = tensor_module(tensor_module(modules[0], modules[1], prime),
                                  modules[2], prime)
            for generator in total:
                assert np.array_equal(mm(prime, frame, generator),
                                      mm(prime, generator, frame))
            cut = partial_cut(modules, frame, level, prime)
            return {
                "N": level, "prime": prime, "q": q,
                "Riley_parameter": parameter, "Riley_embedding": embedding,
                "frame_rs": [r, s], "root_Gauss_states": states,
                "K_eigenvalue_roots": xs, "projector_anchor": anchor,
                "attempts": attempts, "frame_determinant": determinant(frame, prime),
                "cut_scalar": int(cut[0, 0]),
                "cut_zero": not np.any(cut),
                "full_quantum_intertwining": True,
                "full_diagonal_coproduct_intertwining": True,
                "irreducible_root_central_Riley_representation": True,
            }
    raise RuntimeError(("no admissible case", level, embedding))


def symbolic_riley_component():
    z, u, meridian = sp.symbols("z u M", nonzero=True)
    a = sp.Matrix([[z, 1], [0, 1 / z]])
    b = sp.Matrix([[z, 0], [u, 1 / z]])
    c = a.inv() * b * a * b.inv() * a
    polynomial = u ** 2 + (z ** 2 + z ** -2 - 3) * (u - 1)
    expected = sp.Matrix([[0, polynomial / z],
                          [-u * z * polynomial, -u * polynomial]])
    assert (c * a - b * c - expected).applyfunc(sp.factor) == sp.zeros(2)
    assert sp.factor(polynomial.subs(z, 1) - (u * u - u + 1)) == 0
    golden = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(polynomial.subs({z: golden, u: 0})) == 0
    records = []
    for level in range(2, 13):
        left = sp.Poly(meridian ** (4 * level) - 3 * meridian ** (2 * level) + 1,
                       meridian)
        right = sp.Poly(meridian ** (4 * level) + meridian ** (2 * level) + 1,
                        meridian)
        assert sp.gcd(left, left.diff()).degree() == 0
        assert sp.gcd(right, right.diff()).degree() == 0
        assert sp.gcd(left, right).degree() == 0
        records.append({"N": level, "discriminant_simple_zero_count": 8 * level})
    return {
        "fixed_braid_polynomial_checked_directly": True,
        "complete_Riley_and_reducible_golden_attachment": True,
        "squarefree_discriminant_checks": records,
        "uniform_proof": (
            "For every N, each quadratic in M^(2N) has distinct nonzero "
            "roots, and their difference is4M^(2N); hence8N simple zeros. "
            "The positive-real upper-triangular anchor has positive exact "
            "figure-eight whole-source factors at every level."
        ),
    }


def main():
    records = []
    for level in (2, 3, 4):
        for embedding in (0, 1):
            record = one_case(level, embedding)
            records.append(record)
            print(json.dumps(record), flush=True)
    result = {
        "scope": (
            "Exact full root-holonomy fixed-scheme cut evaluation, not a "
            "semiclassical geometric-source identity or volume estimate."
        ),
        "symbolic_Riley_component": symbolic_riley_component(),
        "records": records,
    }
    Path(__file__).with_name("geometric_root_holonomy_cut_results.json").write_text(
        json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
