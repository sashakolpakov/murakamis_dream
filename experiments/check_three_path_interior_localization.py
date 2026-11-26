#!/usr/bin/env python3
"""Exact local coordinate algebra for the geometric boundary-decay proof.

This does not check compactness, existence of geometric solutions, or a
quantum asymptotic. Those parts are written arguments.
"""

from hashlib import sha256
import json
from pathlib import Path

import sympy as s


def main():
    a, b, c, d = s.symbols("a b c d", real=True)
    variables = s.Matrix([a, b, c, d])
    g_right = 3*a/4+b
    g_left_next = 3*c/4-d
    squares = s.Matrix([
        a/4-g_left_next/2,
        g_right/2+c/4,
        a/4+g_left_next/2,
        g_right/2-c/4,
    ])
    K = s.Matrix([
        [s.Rational(1,4), 0, -s.Rational(3,8), s.Rational(1,2)],
        [s.Rational(3,8), s.Rational(1,2), s.Rational(1,4), 0],
        [s.Rational(1,4), 0, s.Rational(3,8), -s.Rational(1,2)],
        [s.Rational(3,8), s.Rational(1,2), -s.Rational(1,4), 0],
    ])
    assert squares.jacobian(variables) == K
    gram = K.T*K
    t = s.Symbol("t")
    polynomial = (t**2-s.Rational(29,32)*t+s.Rational(1,16))**2
    assert s.expand(gram.charpoly(t).as_expr()-polynomial) == 0
    margins = {}
    for label, matrix in (
        ("lower", gram-s.eye(4)/16),
        ("upper", s.Rational(7,8)*s.eye(4)-gram),
    ):
        for k in range(1,5):
            minor = s.det(matrix[:k,:k])
            assert minor > 0
            margins[f"{label} leading minor {k}"] = str(minor)
    height = s.Symbol("H", real=True)
    # A constrained state change has delta g_-+delta g_+=3 delta a/2.
    assert s.expand(3*height*a/2-height*((3*a/4-b)+(3*a/4+b))) == 0

    # Each selected vertex receives exactly two edge Gram contributions,
    # including both attaching edges. These exact finite assemblies test
    # the factors used in the general bound, whose proof is incidence counting.
    assembly_checks = []
    for size in range(1,9):
        assembled = s.zeros(2*size)
        for edge in range(size+1):
            injection = s.zeros(4,2*size)
            for slot,vertex in ((0,edge-1),(2,edge)):
                if 0 <= vertex < size:
                    injection[slot,2*vertex] = 1
                    injection[slot+1,2*vertex+1] = 1
            assembled += injection.T*gram*injection
        # With E''=I, the bounds are 1/2 I < 4*assembly < 7 I.
        for label, matrix in (
            ("lower", 4*assembled-s.eye(2*size)/2),
            ("upper", 7*s.eye(2*size)-4*assembled),
        ):
            # The assembled Gram happens to be block diagonal. Check each
            # exact 2x2 block and absence of off-block entries.
            for i in range(size):
                block = matrix[2*i:2*i+2,2*i:2*i+2]
                assert block[0,0]>0 and block.det()>0
                for j in range(size):
                    if j != i:
                        assert matrix[2*i:2*i+2,2*j:2*j+2] == s.zeros(2)
            assembly_checks.append(f"{size} selected vertices: {label} bound")

    root = Path(__file__).resolve().parents[1]
    paths = [
        "experiments/check_three_path_interior_localization.py",
        "notes/research_three_path_interior_localization.md",
        "notes/research_positive_filling_convex_variation.md",
        "notes/research_positive_edge_volume_identity.md",
        "notes/research_bare_kernel_power_three_obstruction.md",
    ]
    result = {
        "status": "passed",
        "scope": "Exact constrained edge coordinates, Gram bounds, tangent cancellation and finite incidence normalization. Compactness, uniform geometric interiority and inverse-decay arguments remain written; no quantum coefficient conclusion.",
        "coordinate_and_tangent_identities": 3,
        "strict_principal_minor_comparisons": margins,
        "finite_incidence_checks": assembly_checks,
        "gram": str(gram),
        "gram_characteristic_polynomial": str(polynomial),
        "sha256": {name: sha256((root/name).read_bytes()).hexdigest()
                   for name in paths},
    }
    output = root/"repro/results/research-three-path-interior-localization.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"Passed 3 identities, {len(margins)} exact minor comparisons and {len(assembly_checks)} incidence checks.")
    print(output)


if __name__ == "__main__":
    main()
