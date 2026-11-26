#!/usr/bin/env python3
"""Exact Gaussian-integer bulk check for the original (-4,-5) source."""

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    y = sp.symbols("Y", nonzero=True)
    z = -2/y
    ell = -2*y
    third = 2+4*sp.I+2*sp.I*(y+1/y)
    values = [ell, third]
    for _ in range(1, 5):
        values.append(sp.expand(8-z*values[-1]-values[-2]))
    transformed = [z, values[4]]
    for _ in range(1, 4):
        transformed.append(sp.expand(
            8-values[5]*transformed[-1]-transformed[-2]))
    polynomial = sp.expand(transformed[4]-2)
    coefficients = [polynomial.coeff(y, offset) for offset in (-19, -18, -17)]
    assert coefficients == [
        -524288, -4194304+2097152*sp.I, -10092544+16777216*sp.I]
    ratio = sp.simplify(coefficients[1]**2/(coefficients[0]*coefficients[2]))
    expected = (sp.Integer(47552)+4864*sp.I)/22313
    assert sp.simplify(ratio-expected) == 0
    assert sp.im(sp.expand_complex(ratio)) == sp.Rational(4864, 22313)
    record = {
        "status": "pass",
        "scope": "Exact bulk coefficients and nonreal diagonal-gauge invariant "
                 "for the original M^-5 J M^-4 source; no determinant lower bound.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "coefficients_at_offsets_minus_19_minus_18_minus_17": [
            str(v) for v in coefficients],
        "exact_cross_ratio": str(sp.expand_complex(ratio)),
        "exact_positive_imaginary_part": "4864/22313",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps(record))


if __name__ == "__main__":
    main()
