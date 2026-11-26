#!/usr/bin/env python3
"""Check the prepared ordinary boundary sum against original crossing matrices.

The factorial triple sum and its next-crossing reduction are formed separately
from the literal original matrix products. Negative powers use triangular
solves. These finite identities do not certify a global saddle asymptotic.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_even_reflected_casimir_insertions import (
    apply_power, original_crossing,
)


ROOT = Path(__file__).resolve().parents[1]


def newton_jets(level, value, factorials):
    values = [mp.mpc(1)]
    derivatives = [mp.mpc(0)]
    for j in range(level-1):
        node = 2*mp.cos((2*j+1)*mp.pi/level)
        ratio = (factorials[j+1]/factorials[j])**2
        values.append((node-value)*values[-1]/ratio)
        derivatives.append(
            ((node-value)*derivatives[-1]-values[-2])/ratio
        )
    return values, derivatives


def run(precision):
    mp.mp.dps = precision
    counts = {}
    worst = mp.mpf(0)
    tolerance = mp.power(10, -precision//2)

    def check(name, actual, expected):
        nonlocal worst
        residual = abs(actual-expected)/max(1, abs(actual), abs(expected))
        worst = max(worst, residual)
        counts[name] = counts.get(name, 0)+1
        if residual > tolerance:
            raise ArithmeticError(f"{name}: {mp.nstr(residual, 20)}")

    for level in range(2, 13):
        matrix = original_crossing(level)
        factorials = [mp.mpf(1)]
        for j in range(1, level):
            factorials.append(
                factorials[-1]*2*mp.sin(mp.pi*j/level)
            )
        for sign in (1, -1):
            q = mp.exp(sign*mp.pi*1j/level)
            kappa = mp.exp(sign*mp.pi*1j*(level-1)**2/(2*level))
            h = [
                q**(j*(j+2))*factorials[j]**2
                for j in range(level)
            ]
            # Set the free scalar A_N to one. Linearity reinstates its
            # exact original value; every crossing and its unit remain.
            actual_next = [
                kappa**3*value
                for value in apply_power(matrix, h[::-1], sign)
            ]
            actual_boundary = [
                kappa**3*value
                for value in apply_power(matrix, h[::-1], 3*sign)[::-1]
            ]

            reduced_next = []
            for j in range(level):
                value = mp.fsum(
                    q**(k*(j+k))
                    /(factorials[k]**3*factorials[j-k])
                    for k in range(j+1)
                )
                reduced_next.append(
                    level**2*kappa**2*(-q)**j*factorials[j]*value
                )
                check("prepared_next_column", actual_next[j], reduced_next[j])

            triple_boundary = []
            for i in range(level):
                value = mp.fsum(
                    (sign*1j)**(i+j)*(-1)**j
                    *q**(mp.mpf((i-j)**2-i+j)/2+k*(j+k))
                    *factorials[i+j]
                    /(factorials[i]**2*factorials[j]
                      *factorials[k]**3*factorials[j-k])
                    for j in range(level-i)
                    for k in range(j+1)
                )
                triple_boundary.append(level**3*kappa**2*value)
                check(
                    "prepared_boundary_coefficient",
                    actual_boundary[i], triple_boundary[i],
                )

            # Actual complete values, physical endpoint normals, another
            # original spectral color, and a free complex boundary.
            points = [
                mp.mpc(-2),
                mp.mpc(2*mp.cos(mp.pi/level)),
                mp.mpc(2*mp.cos((2*((level-1)//3)+1)*mp.pi/level)),
                mp.mpc("-1.1", ".27"),
            ]
            for value in points:
                jets = newton_jets(level, value, factorials)
                for order, basis in enumerate(jets):
                    check(
                        "ordinary_boundary_value" if order == 0
                        else "ordinary_boundary_normal",
                        mp.fsum(a*b for a, b in zip(actual_boundary, basis)),
                        mp.fsum(a*b for a, b in zip(triple_boundary, basis)),
                    )
        print(f"Checked prepared boundary, both signs, N={level}.", flush=True)

    path = Path(__file__).resolve()
    dependency = path.with_name("check_even_reflected_casimir_insertions.py")
    return {
        "status": "passed",
        "precision_decimal_digits": precision,
        "mpmath_version": mp.__version__,
        "levels": list(range(2, 13)),
        "crossing_signs": [1, -1],
        "exact_check_counts": counts,
        "maximum_relative_residual": mp.nstr(worst, 30),
        "script_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "dependency_sha256": {
            str(dependency.relative_to(ROOT)):
                hashlib.sha256(dependency.read_bytes()).hexdigest(),
        },
        "scope": "Exact original columns and ordinary boundary values/normals; "
                 "no asymptotic assertion.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT/"repro/results/research-three-crossing-prepared-boundary-sum.json",
    )
    args = parser.parse_args()
    result = run(args.precision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Saved {args.output}")
