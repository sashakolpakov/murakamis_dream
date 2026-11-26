#!/usr/bin/env python3
"""Check the full two-boundary same-sign two-crossing chain identity.

These finite original-matrix comparisons test ordering, scalar phases,
both tensor first normals and their mixed normal. They are not tests
of the large-level asymptotic or of a marked tangle isotopy.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices


def basis_jet(level, z):
    values = [mp.mpc(1)]
    derivatives = [mp.mpc(0)]
    for index in range(level - 1):
        center = 2 * mp.cos((2 * index + 1) * mp.pi / level)
        scale = 4 * mp.sin((index + 1) * mp.pi / level) ** 2
        values.append((center - z) * values[-1] / scale)
        derivatives.append(
            ((center - z) * derivatives[-1] - values[-2]) / scale
        )
    return mp.matrix(values), mp.matrix(derivatives)


def relative(left, right):
    if isinstance(left, mp.matrix):
        return mp.norm(left - right) / max(1, mp.norm(left), mp.norm(right))
    return abs(left - right) / max(1, abs(left), abs(right))


def scalar(left, coefficient, right):
    return (left.T * coefficient * right)[0]


def encode(value):
    return {"real": mp.nstr(mp.re(value), 35),
            "imag": mp.nstr(mp.im(value), 35)}


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision // 2)
    rows = []
    unreduced_example = None
    lengths = (1, 2, 3, 4, 7, 8, 31, 32)
    for level in range(2, 11):
        crossing, _, _ = original_matrices(level)
        turn = mp.matrix([[int(i + j == level - 1)
                           for j in range(level)]
                          for i in range(level)])
        kappa = mp.exp(mp.pi * 1j * (level - 1) ** 2 / (2 * level))
        points = [
            (2 * mp.cos(mp.pi / level),
             2 * mp.cos(3 * mp.pi / level)),
            (mp.mpf(-2), mp.mpc("0.3", "0.2")),
            (mp.mpc("0.37", "0.12"), mp.mpc("-1.2", "0.17")),
        ]
        jets = [(basis_jet(level, z), basis_jet(level, w))
                for z, w in points]
        for sign in (-1, 1):
            boundary_crossing = crossing ** (-sign)
            for length in lengths:
                chain = (turn * crossing ** (2 * sign)) ** length
                middle = turn * crossing ** (-sign * (length + 1))
                unit = kappa ** (sign * (length + 1))
                reduced = unit * boundary_crossing * middle * boundary_crossing.T
                coefficient_error = relative(chain, reduced)
                normal_errors = []
                for left_pair, right_pair in jets:
                    for left in left_pair:
                        for right in right_pair:
                            normal_errors.append(relative(
                                scalar(left, chain, right),
                                scalar(left, reduced, right),
                            ))
                carrier = mp.exp(-sign * mp.pi * 1j
                                 * (level - 1) ** 2 / (4 * level))
                carrier_error = relative(unit * carrier ** 2,
                                         kappa ** (sign * length))
                maximum = max(coefficient_error, carrier_error, *normal_errors)
                if maximum > tolerance:
                    raise ArithmeticError((level, sign, length, maximum))
                rows.append({
                    "N": level, "sign": sign, "length": length,
                    "full_coefficient_relative_error":
                        mp.nstr(coefficient_error, 35),
                    "maximum_boundary_jet_relative_error":
                        mp.nstr(max(normal_errors), 35),
                    "carrier_relative_error": mp.nstr(carrier_error, 35),
                    "boundary_jet_cases": len(normal_errors),
                })
                if (level, sign, length) == (5, 1, 3):
                    (vz, _), (vw, _) = jets[-1]
                    crossing_coefficients = boundary_crossing[:, 0]
                    raw = (unit * (vz.T * crossing_coefficients)[0]
                           * (vw.T * crossing_coefficients)[0]
                           * scalar(vz, middle, vw))
                    canonical = scalar(vz, chain, vw)
                    difference = relative(raw, canonical)
                    if difference <= mp.mpf("1e-8"):
                        raise ArithmeticError("Expected a nontrivial quotient correction")
                    unreduced_example = {
                        "N": level, "sign": sign, "length": length,
                        "z": encode(points[-1][0]), "w": encode(points[-1][1]),
                        "canonical_value": encode(canonical),
                        "unreduced_ordinary_product": encode(raw),
                        "relative_difference": mp.nstr(difference, 35),
                    }
        print(f"Full two-boundary chain and mixed normals checked at N={level}.",
              flush=True)
    return {
        "scope": "Finite original-matrix normalization and tensor-Hermite diagnostics; no asymptotic or marking claim is inferred.",
        "decimal_precision": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "matrix_cases": len(rows),
        "boundary_jet_cases": sum(row["boundary_jet_cases"] for row in rows),
        "checks": rows,
        "unreduced_product_example": unreduced_example,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.precision)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
        print(f"Saved {args.output}.")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
