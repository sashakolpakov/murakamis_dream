#!/usr/bin/env python3
"""Exact algebra for the homogeneous-three action calibration.

Shape identities are checked by polynomial remainders over Q(i,sqrt(3)).
Functional identities are checked only at the level of their logarithmic
differential symbols. No numerical dilogarithm value, phase comparison, or
positive-shape branch choice is inferred from this computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ii, sqrt3 = sp.I, sp.sqrt(3)
    field = sp.QQ.algebraic_field(ii, sqrt3)
    v = sp.Symbol("v")
    v_square = -sp.Rational(1, 3) - 2 * ii * sqrt3 / 3
    modulus = sp.Poly(v**2 - v_square, v, domain=field)
    q = 2 * sqrt3 / 3 - ii
    zeta = (1 + ii * sqrt3) / 2
    shape_a = (q + v) / (v - ii)
    shape_b = -(q - v) / (v + ii)
    shape_c = (q - v) / (v - ii)
    shape_d = -(q + v) / (v + ii)
    checks = []

    def remainder_identity(name, expression):
        numerator, denominator = sp.fraction(sp.together(expression))
        num = sp.Poly(numerator, v, domain=field)
        den = sp.Poly(denominator, v, domain=field)
        remainder = num.rem(modulus)
        assert remainder.is_zero, (name, remainder)
        gcd = sp.gcd(den, modulus)
        assert gcd.degree() == 0, (name, "denominator vanishes on a root", gcd)
        checks.append({
            "name": name,
            "numerator_remainder": str(remainder.as_expr()),
            "denominator_gcd_degree": int(gcd.degree()),
        })

    remainder_identity("q_squared_minus_2v_squared", q**2 - 2 * v**2 - 1)
    remainder_identity(
        "original_cos_t",
        (1 - v**2) / (1 + v**2) - (-sp.Rational(1, 4) + 3 * ii * sqrt3 / 4),
    )
    remainder_identity("6_B_minus_reciprocal", shape_b + 1 / shape_a)
    remainder_identity("6_D0_minus_reciprocal", shape_d + 1 / shape_c)
    remainder_identity("6_C_Mobius", shape_c - (shape_a - 1) / (shape_a + 1))
    remainder_identity("6_A_minus_reciprocal", shape_a - 1 / shape_a - zeta)
    remainder_identity("7_elimination", shape_a - 1 / shape_a - 2 * (q + ii) / (q - ii))
    remainder_identity("7_middle_fraction", 2 * (q + ii) / (q - ii) - 2 / (1 - ii * sqrt3))
    remainder_identity("7_zeta_fraction", 2 / (1 - ii * sqrt3) - zeta)
    remainder_identity("A_minimal_relation", shape_a**2 - zeta * shape_a - 1)
    remainder_identity("zeta_complement", zeta * (1 - zeta) - 1)
    remainder_identity("zeta_cube", zeta**3 + 1)
    xx, yy = shape_a, zeta / shape_a
    middle = (xx - xx * yy) / (1 - xx * yy)
    last = (yy - xx * yy) / (1 - xx * yy)
    remainder_identity("12_product", xx * yy - zeta)
    remainder_identity("12_middle_argument", middle - yy)
    remainder_identity("12_last_argument", last - 1 / (1 + shape_a))
    remainder_identity("12_last_times_1plusA", last * (1 + shape_a) - 1)
    remainder_identity("12_last_product_reduction", last * (1 + shape_a) - zeta**2 * (1 / shape_a - shape_a))
    remainder_identity("12_last_product_zeta_cube", zeta**2 * (1 / shape_a - shape_a) + zeta**3)

    # An independent calculation uses A as the formal generator.
    aa = sp.Symbol("A")
    a_modulus = sp.Poly(aa**2 - zeta * aa - 1, aa, domain=field)
    a_checks = []
    for name, expression in [
        ("middle_from_A_relation", (aa - zeta) / (1 - zeta) - zeta / aa),
        ("last_from_A_relation", (zeta / aa - zeta) / (1 - zeta) - 1 / (1 + aa)),
    ]:
        num, den = sp.fraction(sp.together(expression))
        rem = sp.Poly(num, aa, domain=field).rem(a_modulus)
        gcd = sp.gcd(sp.Poly(den, aa, domain=field), a_modulus)
        assert rem.is_zero and gcd.degree() == 0
        a_checks.append({"name": name, "numerator_remainder": str(rem.as_expr()),
                         "denominator_gcd_degree": int(gcd.degree())})

    # Verify every rational divisor decomposition before canceling the
    # formal coefficients of log|atom_i| d arg(atom_j).
    x, y, z = sp.symbols("x y z")
    atoms = [x, y, 1 - x, 1 - y, 1 - x * y]
    arguments = [
        (x, [1, 0, 0, 0, 0], [0, 0, 1, 0, 0], 1),
        (y, [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], 1),
        (x * y, [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], -1),
        ((x - x * y) / (1 - x * y), [1, 0, 0, 1, -1], [0, 0, 1, 0, -1], -1),
        ((y - x * y) / (1 - x * y), [0, 1, 1, 0, -1], [0, 0, 0, 1, -1], -1),
    ]

    def monomial(factors, exponents):
        return sp.prod(a**e for a, e in zip(factors, exponents))

    def wedge(a, b):
        a, b = sp.Matrix(a), sp.Matrix(b)
        return a * b.T - b * a.T

    five_term = sp.zeros(5)
    for argument, first, second, sign in arguments:
        assert sp.cancel(argument - monomial(atoms, first)) == 0
        assert sp.cancel(1 - argument - monomial(atoms, second)) == 0
        five_term += sign * wedge(first, second)
    assert five_term == sp.zeros(5)

    inverse_symbol = wedge([-1, 0], [-1, 1]) + wedge([1, 0], [0, 1])
    one_minus_inverse_symbol = wedge([0, -1], [1, -1]) - wedge([1, 0], [0, 1])
    assert inverse_symbol == one_minus_inverse_symbol == sp.zeros(2)
    assert sp.cancel((1 - 1 / z) / ((1 - z) / z)) == -1
    assert sp.cancel((1 - 1 / (1 - z)) / (z / (1 - z))) == -1

    # H0 uses atoms z,1-z,1+z,2. The last atom has log|2| but
    # identically zero argument differential: retain it explicitly.
    h_atoms = [z, 1 - z, 1 + z, sp.Integer(2)]
    w = (z - 1) / (z + 1)
    h_vectors = [
        (w, [0, 1, -1, 0], [0, 0, -1, 1]),
        (-w, [0, 1, -1, 0], [1, 0, -1, 1]),
        (z, [1, 0, 0, 0], [0, 1, 0, 0]),
        (-z, [1, 0, 0, 0], [0, 0, 1, 0]),
    ]

    def differential_symbol(first, second):
        first, second = sp.Matrix(first), sp.Matrix(second)
        first_arg, second_arg = first.copy(), second.copy()
        first_arg[-1] = second_arg[-1] = 0
        return first * second_arg.T - second * first_arg.T

    h_difference = sp.zeros(4)
    for (argument, first, second), sign in zip(h_vectors, [1, -1, -1, 1]):
        assert sp.cancel(argument / monomial(h_atoms, first)) in (1, -1)
        assert sp.cancel((1 - argument) / monomial(h_atoms, second)) in (1, -1)
        h_difference += sign * differential_symbol(first, second)
    assert h_difference == sp.zeros(4)
    assert sp.cancel(((w - 1) / (w + 1)) + 1 / z) == 0
    assert sp.simplify(w.subs(z, ii) - ii) == 0
    a, height, pi_symbol = sp.symbols("a H p", real=True)
    t = a - ii * height
    action_correction = 2 * pi_symbol * sp.re(
        3 * ii * t**2 / (4 * pi_symbol) - ii * t)
    assert sp.simplify(action_correction - 4 * height * (3 * a / 4 - pi_symbol / 2)) == 0
    # The unexponentiated stationary equation is checked symbolically;
    # its actual branch choice remains a cited analytic input.
    rr = 3 * height / 4 + ii * (3 * a / 4 - pi_symbol / 2)
    assert sp.expand(3 * t + 4 * ii * rr - 2 * pi_symbol) == 0

    root = Path(__file__).resolve().parents[1]
    dependencies = [
        Path(__file__).resolve(),
        root / "notes/research_homogeneous_three_action_calibration.md",
        root / "notes/research_bare_kernel_power_three_obstruction.md",
        root / "notes/research_positive_edge_volume_identity.md",
    ]
    result = {
        "status": "all exact algebra checks passed",
        "scope": (
            "Exact rational-function identities modulo quadratic relations over Q(i,sqrt(3)); "
            "formal logarithmic differential cancellation and action-correction algebra. "
            "No numerical dilogarithms, numerical phase comparison, positivity/root-branch "
            "selection, functional integration constants, or quantum asymptotic checked."
        ),
        "coefficient_field": str(field),
        "v_modulus": str(modulus.as_expr()),
        "A_modulus": str(a_modulus.as_expr()),
        "shape_remainder_checks": checks,
        "independent_A_remainder_checks": a_checks,
        "differential_checks": {
            "five_term": {"matrix_size": 5, "zero_coefficients": 25, "argument_factorizations": 10},
            "two_inversion_identities": {"zero_coefficients": 8},
            "H0_Mobius": {"matrix_size": 4, "zero_coefficients": 16,
                          "argument_factorizations": 8, "log2_retained": True},
        },
        "additional_exact_identities": [
            "Mobius transformation squared is -1/z",
            "Mobius transformation fixes i",
            "action correction equals 4H Im(r)",
            "full homogeneous period equation",
        ],
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
