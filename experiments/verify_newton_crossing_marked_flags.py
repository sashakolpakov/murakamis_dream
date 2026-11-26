#!/usr/bin/env python3
"""Exact matrix and oriented-face checks for the Newton crossing flags.

This verifies rational identities, not an assembled triangulation or
an asymptotic theorem. See research_newton_crossing_marked_flags.md.
"""

import argparse
from collections import Counter
import itertools
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    checks = []

    def check(name, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        residuals = [sp.factor(sp.cancel(value)) for value in entries]
        if any(value != 0 for value in residuals):
            raise AssertionError((name, residuals))
        checks.append(name)

    E, R, Y, V = sp.symbols("E R Y V")
    W = [
        sp.Matrix([[1, 0], [0, E]]),
        sp.Matrix([[1, E - 1], [0, E]]),
        sp.Matrix([[E - R, R * (1 - E)], [E - 1, 1 - E * R]]),
        sp.Matrix([[R, 0], [1 - E, E * R]]),
    ]
    P = []
    for j in range(4):
        quotient = W[j - 1].inv() * W[j]
        P.append(sp.simplify(2 * quotient / sp.trace(quotient)))
    check("original cyclic meridian product", P[0] * P[1] * P[2] * P[3] - sp.eye(2))

    z = (V + 1) * (Y - 1) ** 2 / (V * Y)
    p = V / ((V + 1) * (Y - 1))
    d = 1 / (Y - 1)
    h = (V + 1) ** 2 * (Y - 1) ** 2 / V
    a = sp.Matrix([[1, 1], [0, 1]])
    b = sp.Matrix([[1, 0], [z, 1]])
    c = sp.Matrix([[1 - h * p, h * p * p], [-h, 1 + h * p]])
    dm = sp.simplify((c * b * a).inv())
    quadruple = [a, b, c, dm]
    flags = [sp.Matrix([1, 0]), sp.Matrix([0, 1]),
             sp.Matrix([p, 1]), sp.Matrix([d, 1])]
    for j, (matrix, flag) in enumerate(zip(quadruple, flags)):
        check(f"determinant {j}", matrix.det() - 1)
        check(f"trace {j}", sp.trace(matrix) - 2)
        check(f"fixed flag {j}", sp.Matrix.hstack(matrix * flag, flag).det())
    check("reverse product", dm * c * b * a - sp.eye(2))

    A = Y + 1 / Y + (Y + 1 / Y - 2) / V
    B = Y + 1 / Y + (Y + 1 / Y - 2) * V
    C = 2 - (Y - 1) ** 2 * (V + 1) ** 2 / V
    check("trace A", sp.trace(a * b) - A)
    check("trace B", sp.trace(b * c) - B)
    check("trace C", sp.trace(a * c) - C)
    check("Fricke relation", A * A + B * B + C * C + A * B * C
          - 8 * (A + B + C) + 28)

    actual = [P[1].inv(), P[2].inv(), P[3].inv(), P[0].inv()]
    Nin = sp.Matrix([[1, -1], [0, 1 - E]])
    substitution = {Y: E, V: (1 - R) / R}
    for j, (matrix, target) in enumerate(zip(actual, quadruple)):
        check(f"original white normalization {j}",
              Nin * matrix * Nin.inv() - target.subs(substitution))

    X = Y + (Y - 1) / V
    U = -Y * (1 + V)
    Nout = sp.Matrix([[0, 1], [z, z]])
    moved = [a.inv() * b * a, a, c, dm]
    for j, (matrix, target) in enumerate(zip(moved, quadruple)):
        check(f"full output conjugacy {j}",
              Nout * matrix * Nout.inv()
              - target.subs({Y: X, V: U}, simultaneous=True))
    check("active crossing trace", sp.trace(moved[0] * moved[2]) - (8 - A * C - B))

    def point(value):
        return sp.Matrix([value, 1])

    infinity = sp.Matrix([1, 0])

    def det(v, w):
        return sp.Matrix.hstack(v, w).det()

    def shape(v0, v1, v2, v3):
        return det(v3, v0) * det(v2, v1) / (det(v3, v1) * det(v2, v0))

    check("input tetrahedron shape",
          shape(point(p), infinity, point(d), point(0)) + V)
    check("output tetrahedron shape",
          shape(point(p), point(-1), point(d), infinity) + U)

    # The two-flip output table, using only actual side maps.
    # Its geometric use requires the all-white interface in the note.
    def mobius(matrix, value):
        return (matrix[0, 0] * value + matrix[0, 1]) / (
            matrix[1, 0] * value + matrix[1, 1]
        )

    Sin = [
        sp.simplify((Nin * matrix * Nin.inv()).subs(
            {E: Y, R: 1 / (1 + V)}, simultaneous=True))
        for matrix in W
    ]
    check("other-copy unfolded zero", mobius(Sin[0].inv(), 0) + 1)
    check("other-copy unchanged d", mobius(Sin[0].inv(), d) - d)
    frame_M = sp.Matrix([[(p + 1) / p, -1], [0, 1]])
    frame_L = sp.Matrix([[1, -d], [1, 1]])
    check("second-output fourth flag",
          mobius(frame_M * Sin[2].inv(), d) - d)
    check("output quadrilateral shape", mobius(frame_L, p) - 1 / (1 + U))
    Sout = [
        frame_M * Sin[2].inv() * Sin[0],
        frame_M * Sin[1].inv() * Sin[0],
        frame_M,
        frame_M * Sin[2].inv() * Sin[3],
    ]
    scalars = [
        (V + 1) / V, sp.Integer(1),
        (V * Y + Y - 1) / (Y * (V + 1)),
        -(V * Y + Y - 1) / V,
    ]
    for j, (matrix, scalar, target) in enumerate(zip(Sout, scalars, W)):
        target = target.subs({E: X, R: 1 / (1 + U)}, simultaneous=True)
        check(f"two-flip full white map {j}",
              frame_L * matrix * frame_L.inv() - scalar * target)

    # Vertex labels: p=0, infinity=1, d=2, zero=3, minus_one=4.
    def oriented_face(face):
        inversions = sum(face[i] > face[j]
                         for i, j in itertools.combinations(range(3), 2))
        return tuple(sorted(face)), (-1) ** inversions

    boundary = Counter()
    for tetrahedron in [(0, 1, 2, 3), (0, 4, 2, 1)]:
        for omitted in range(4):
            face = tetrahedron[:omitted] + tetrahedron[omitted + 1:]
            key, sign = oriented_face(face)
            boundary[key] += (-1) ** omitted * sign
    if boundary[(0, 1, 2)] != 0:
        raise AssertionError("The common face does not cancel")
    nonzero = {str(key): value for key, value in boundary.items() if value}
    if len(nonzero) != 6 or any(abs(value) != 1 for value in nonzero.values()):
        raise AssertionError(("Unexpected boundary", nonzero))
    checks.append("common oriented face cancels with six exterior triangles")

    result = {
        "status": "passed",
        "kind": "exact rational identities and oriented-chain boundary",
        "checks": checks,
        "check_count": len(checks),
        "exterior_faces": nonzero,
        "scope": (
            "Exact algebra for the marked crossing and its two-flip "
            "white-transition table. The literal attachment requires "
            "actual all-white sides; no masked-interface extension, "
            "positive assembled saddle, or source asymptotic is tested."
        ),
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
