#!/usr/bin/env python3
"""Check normalized original rational-word cofactors, including full jets.

Uses literal original crossing matrices. Adjugates are computed by their
minors, independently of the rank-one formula under test. No asymptotic
or generic-rank assumption enters the checks.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_internal_two_crossing_chain import basis_jet, relative
from check_current_free_aw_crossing_transport import newton_multiplication


def submatrix(matrix, rows, columns):
    return mp.matrix([[matrix[i, j] for j in columns] for i in rows])


def finite_determinant(matrix):
    """Partial-pivot elimination, including exactly singular minors."""
    a = matrix.copy()
    answer = mp.mpc(1)
    for k in range(a.rows):
        pivot = max(range(k, a.rows), key=lambda r: abs(a[r, k]))
        if a[pivot, k] == 0:
            return mp.mpc(0)
        if pivot != k:
            for column in range(a.cols):
                a[k, column], a[pivot, column] = a[pivot, column], a[k, column]
            answer = -answer
        diagonal = a[k, k]
        answer *= diagonal
        for row in range(k+1, a.rows):
            multiplier = a[row, k]/diagonal
            for column in range(k+1, a.cols):
                a[row, column] -= multiplier*a[k, column]
            a[row, k] = 0
    return answer


def adjugate(matrix):
    size = matrix.rows
    answer = mp.matrix(size)
    for i in range(size):
        for j in range(size):
            minor = submatrix(matrix,
                              [r for r in range(size) if r != j],
                              [c for c in range(size) if c != i])
            answer[i, j] = (-1)**(i+j)*finite_determinant(minor)
    return answer


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    words = [
        [],
        [2, "T"],
        [-3, "T"],
        [2, "T", -2, "T"],
        [-2, "T", -3, "T", -2, "T"],
        [1, "T", -3, "T", 2],
        ["T", -2, "T", 3, "T", -1, "T"],
    ]
    rows = []
    for level in range(2, 10):
        crossing, _, _ = original_matrices(level)
        turn = mp.matrix([[int(i+j == level-1)
                           for j in range(level)] for i in range(level)])
        z = newton_multiplication(level)
        ell = z.T
        c0 = z[0, 0]
        q = mp.exp(mp.pi*1j/level)
        base = ell-c0*mp.eye(level)
        ell1 = crossing**-1*ell*crossing
        explicit = mp.matrix(level)
        for j in range(level):
            explicit[j, j] = 4*q*q**(2*j)-q*(1+q*q)*q**(4*j)
            if j+1 < level:
                explicit[j, j+1] = explicit[j+1, j] = -(1-q**(2*j+2))**2
        algebra_error = relative(explicit, ell1)
        algebra_error = max(algebra_error, relative(
            (q*q-q**-2)*ell1,
            q**-1*z*ell-q*ell*z+8*(q-q**-1)*mp.eye(level)))
        for word in words:
            w = mp.eye(level)
            for letter in word:
                w = (turn if letter == "T" else crossing**letter)*w
            f = w[:, 0]
            cap = w*base*w**-1
            adj = adjugate(cap)
            maximum = max(algebra_error,
                          relative(w.H*turn*w, turn),
                          relative(adj*turn, level**2*f*f.H))
            closed_minor = submatrix(cap, range(1, level), range(level-1))
            maximum = max(maximum, relative(
                (-1)**(level-1)*finite_determinant(closed_minor),
                level**2*abs(f[level-1])**2))
            jet_cases = 0
            probes = [
                (mp.mpf(-2), c0),
                (mp.mpc(".37", ".12"), mp.mpc("-1.1", ".23")),
            ]
            for left, right in probes:
                jets_left = basis_jet(level, left)
                jets_right = basis_jet(level, right)
                for vl in jets_left:
                    for vr in jets_right:
                        lhs = (vl.T*adj*turn*vr)[0]
                        rhs = level**2*(vl.T*f)[0]*(vr.T*f.conjugate())[0]
                        maximum = max(maximum, relative(lhs, rhs))
                        jet_cases += 1
                vl = jets_left[0]
                boundary_det = finite_determinant(cap+turn*vl.conjugate()*vl.T)
                maximum = max(maximum, relative(
                    boundary_det, level**2*abs((vl.T*f)[0])**2))
            assert maximum < tolerance, (level, word, maximum)
            rows.append({
                "N": level, "word_in_applied_order": word,
                "polarized_value_and_normal_cases": jet_cases,
                "maximum_relative_error": mp.nstr(maximum, 18),
            })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = run(args.precision)
    output = {
        "status": "pass",
        "scope": "Exact normalized cofactor, closed scalar, full polarized "
                 "boundary jets, and tridiagonal trace generator; no "
                 "determinant asymptotic claimed.",
        "precision_decimal_digits": args.precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ("check_twist_period_insertion.py",
                         "check_internal_two_crossing_chain.py",
                         "check_current_free_aw_crossing_transport.py")
        },
        "checks": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "level_word_cases": len(rows),
        "polarized_jet_cases": sum(r["polarized_value_and_normal_cases"] for r in rows),
        "maximum_relative_error": mp.nstr(max(
            mp.mpf(r["maximum_relative_error"]) for r in rows), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
