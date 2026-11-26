#!/usr/bin/env python3
"""Check the original elementary cap against its exact path Laplacian.

The original crossing matrix, not its explicit conjugated tridiagonal
formula, constructs the operator being tested. These finite precision
checks diagnose normalization and parity; the note proves all levels.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_current_free_aw_crossing_transport import newton_multiplication
from check_rational_word_normalized_cofactor import finite_determinant, submatrix


def relative(left, right):
    return mp.norm(left-right)/max(mp.mpf(1), mp.norm(left), mp.norm(right))


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    rows = []
    for level in list(range(2, 19)) + [24, 25]:
        q = mp.exp(mp.pi*1j/level)
        qq = q*q
        identity = mp.eye(level)
        crossing, _, _ = original_matrices(level)
        z = newton_multiplication(level)
        ell = z.T
        cap = crossing**-1*ell*crossing-z[0, 0]*identity
        x = mp.diag([qq**j for j in range(level)])
        shift = mp.matrix(level)
        for j in range(level):
            shift[(j+1) % level, j] = 1
        a = identity+q*shift
        p = mp.diag([4*mp.sin(mp.pi*(j+1)/level)**2
                     for j in range(level-1)] + [0])
        h = a*p*a.H
        unitary = mp.diag([(-q)**j for j in range(level)])
        delta = mp.matrix(level)
        for j in range(level-1):
            weight = p[j, j]
            delta[j, j] += weight
            delta[j+1, j+1] += weight
            delta[j, j+1] -= weight
            delta[j+1, j] -= weight
        maximum = max(
            relative(z, q*x+q**-1*x**-1+(x+x**-1-2*identity)*shift),
            relative(ell, q*x+q**-1*x**-1
                     +(qq*x+qq**-1*x**-1-2*identity)*shift.T),
            relative(cap, -q**-1*a*(identity-qq*x)**2
                     *(identity+q*shift.T)),
            relative(cap, q*h*x),
            relative(unitary.H*h*unitary, delta),
            relative(finite_determinant(a), 1+(-1)**level),
        )
        flat = mp.matrix([(-q)**j/mp.sqrt(level) for j in range(level)])
        maximum = max(maximum, relative(h*flat, mp.zeros(level, 1)),
                      relative((flat.H*x**-1*flat)[0], 0))
        cofactors = []
        for removed in range(level):
            keep = [j for j in range(level) if j != removed]
            cofactor = finite_determinant(submatrix(h, keep, keep))
            cofactors.append(cofactor)
            maximum = max(maximum, relative(cofactor, level**2))
        pinned = submatrix(delta, range(1, level), range(1, level))
        green = mp.matrix(level-1)
        for i in range(1, level):
            for j in range(1, level):
                green[i-1, j-1] = mp.fsum(
                    1/p[k, k] for k in range(min(i, j)))
        resistance = mp.fsum(1/p[j, j] for j in range(level-1))
        maximum = max(maximum,
                      relative(pinned*green, mp.eye(level-1)),
                      relative(green, pinned**-1),
                      relative(resistance, mp.mpf(level**2-1)/12))
        eigenvalues = mp.eigsy(delta, eigvals_only=True)
        positive_product = mp.fprod(eigenvalues[j] for j in range(1, level))
        singular_values = mp.svd(cap, compute_uv=False)
        for j in range(level-1):
            maximum = max(maximum, relative(
                singular_values[j], eigenvalues[level-1-j]))
        maximum = max(maximum, relative(positive_product, level**3))
        gap_bound = max(mp.mpf(48)/(level*(level**2-1)),
                        mp.mpf(8)/(3*level**2))
        assert eigenvalues[1] >= gap_bound*(1-tolerance)
        assert eigenvalues[level-1] <= 16*(1+tolerance)
        assert maximum < tolerance, (level, maximum)
        rows.append({
            "N": level,
            "principal_cofactors_checked": len(cofactors),
            "maximum_relative_error": mp.nstr(maximum, 18),
            "smallest_positive_singular_value": mp.nstr(eigenvalues[1], 18),
            "proved_gap_lower_bound": mp.nstr(gap_bound, 18),
            "endpoint_resistance": mp.nstr(resistance, 18),
        })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = run(args.precision)
    dependencies = [
        "check_twist_period_insertion.py",
        "check_current_free_aw_crossing_transport.py",
        "check_rational_word_normalized_cofactor.py",
    ]
    result = {
        "status": "pass",
        "scope": "Original full-matrix elementary cap, exact quantum factor, "
                 "path Laplacian, all principal cofactors, Green matrix, "
                 "parity and singular-value normalization. No general "
                 "rational-word asymptotic is tested.",
        "precision_decimal_digits": args.precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in dependencies
        },
        "checks": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "levels": len(rows),
        "principal_cofactors": sum(r["principal_cofactors_checked"] for r in rows),
        "maximum_relative_error": mp.nstr(max(
            mp.mpf(r["maximum_relative_error"]) for r in rows), 12),
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
