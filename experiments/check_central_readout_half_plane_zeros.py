#!/usr/bin/env python3
"""Original-matrix normalization and exact cubic Rouché certificate."""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

import mpmath as mp

from check_twist_period_insertion import original_matrices


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def scale(a, x):
    return a*x[0], a*x[1]


def l1(x):
    return abs(x[0])+abs(x[1])


def rational_certificate():
    z = F(-4293, 1000), F(-4916, 1000)
    s, eps, radius = F(141421356237, 10**11), F(1, 10**11), F(1, 500)
    assert s*s < 2 < (s+eps)**2
    a, b, c = (F(2), F(-1)), (F(30), F(-8)), (F(-76), F(98))
    z2 = mul(z, z)
    value = add(add(mul(z2, z), scale(s, mul(a, z2))),
                add(mul(b, z), scale(s, c)))
    upper = l1(value)+eps*l1(add(mul(a, z2), c))
    derivative = add(add(scale(3, z2), scale(2*s, mul(a, z))), b)
    lower = max(abs(derivative[0]), abs(derivative[1]))-2*eps*l1(mul(a, z))
    quadratic = l1(add(scale(3, z), scale(s, a)))+eps*l1(a)
    margin = radius*lower-upper-radius**2*quadratic-radius**3
    expected = (
        F(7540696563473, 156250000000000),
        F(643497938473027, 6250000000000),
        F(1310639321883, 50000000000),
        F(393885057898477, 2500000000000000),
    )
    assert (upper, lower, quadratic, margin) == expected
    assert margin > 0
    return dict(zip(("value_upper", "derivative_lower", "quadratic_upper",
                     "rouche_margin"), map(str, expected)))


def relative(a, b):
    return abs(a-b)/max(1, abs(a), abs(b))


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    maximum = mp.mpf(0)
    records = []
    comparisons = 0
    for level in (3, 4, 5, 8, 9, 12):
        crossing, _, _ = original_matrices(level)
        top = level-1
        theta = mp.pi/level
        q = mp.exp(1j*theta)
        kappa = q**(mp.mpf(top**2)/2)
        c0, s1 = 2*mp.cos(theta), 2*mp.sin(theta)
        basis = [[mp.mpc(1)]]
        for j in range(top):
            node = 2*mp.cos((2*j+1)*theta)
            factor = 4*mp.sin((j+1)*theta)**2
            nxt = [mp.mpc(0)]*(len(basis[-1])+1)
            for k, value in enumerate(basis[-1]):
                nxt[k] += node*value/factor
                nxt[k+1] -= value/factor
            basis.append(nxt)
        for power in (-5, -3, -1, 0, 1, 3, 5):
            original = crossing**power
            # Literal trace of R^n K: use its bottom row, not the cap column.
            coeff = [mp.mpc(0)]*level
            for j in range(level):
                for k, value in enumerate(basis[j]):
                    coeff[k] += original[top, j]*value
            expected_first = -(1-(-q*q)**power)/c0
            expected_sum = -c0+s1*s1*expected_first
            errors = [
                relative(coeff[-1], kappa**power*(-1)**top/level**2),
                relative(-coeff[-2]/coeff[-1], expected_sum),
                relative(original[1, 0]/kappa**power, expected_first),
            ]
            comparisons += len(errors)
            if level == 4 and power == 3:
                expected_poly = [
                    mp.sqrt(2)*(-76+98j), 30-8j, mp.sqrt(2)*(2-1j), 1,
                ]
                errors += [relative(-16*coeff[k]/kappa**3, expected_poly[k])
                           for k in range(4)]
                comparisons += 4
            error = max(errors)
            maximum = max(maximum, error)
            if error >= tolerance:
                raise ArithmeticError((level, power, error))
            records.append({"N": level, "power": power,
                            "maximum_relative_error": mp.nstr(error, 24)})
    root = Path(__file__).resolve().parent.parent
    dependencies = {}
    for module in tuple(sys.modules.values()):
        source = getattr(module, "__file__", None)
        if source:
            path = Path(source).resolve()
            if path.parent == root/"experiments" and path.suffix == ".py":
                dependencies[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "status": "passed",
        "scope": "Original central-polynomial identities and exact rational Rouche certificate; no asymptotic fit or root scan.",
        "decimal_precision": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "project_dependency_sha256": dict(sorted(dependencies.items())),
        "source_cases": len(records),
        "complex_comparisons": comparisons,
        "maximum_relative_error": mp.nstr(maximum, 30),
        "rational_certificate": rational_certificate(),
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.precision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in
                      ("status", "source_cases", "complex_comparisons",
                       "maximum_relative_error", "script_sha256")}, indent=2))


if __name__ == "__main__":
    main()
