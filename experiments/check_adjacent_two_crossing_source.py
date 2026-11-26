#!/usr/bin/env python3
"""Check the exact adjacent-(2,2) source and its proposed leading term.

The coefficient checks use exact cyclotomic arithmetic and the original
crossing matrix. The large-level comparisons are numerical diagnostics,
not a proof that the selected saddle contributes or dominates the sum.
"""

import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.polys.domains import QQ


def exact_coefficients(level):
    symbol = sp.Symbol("x")
    field = QQ.alg_field_from_poly(
        sp.Poly(sp.cyclotomic_poly(4 * level, symbol), symbol), alias="x"
    )
    root = field([1, 0])
    q, Q, imaginary = root**2, root**4, root**level
    top = level - 1
    kappa = root**(top * top)
    sine, factorial = [field.one], [field.one]
    for index in range(1, level):
        sine.append(sine[-1] * (q**index - q**(-index)) / imaginary)
        factorial.append(factorial[-1] * (1 - Q**index))
    crossing = [
        [kappa * (-1)**i * q**(i * (j + 1)) * sine[i]
         / (sine[j] * sine[i-j]) if i >= j else field.zero
         for j in range(level)] for i in range(level)
    ]
    squared = [
        [sum((crossing[i][a] * crossing[a][j] for a in range(level)), field.zero)
         for j in range(level)] for i in range(level)
    ]
    for j in range(level):
        original = sum(
            (squared[top-i][0] * squared[top-i][j] for i in range(level)),
            field.zero,
        )
        formula = level**2 * sum(
            (q**(i*i + (i-j)**2) * factorial[i+j]
             / (factorial[i]**3 * factorial[j]**2)
             for i in range(level-j)), field.zero,
        )
        assert original == formula, (level, j)
    return {"level": level, "exact_boundary_coefficients": level}


def stationary_prediction():
    X = (5 + 1j * mp.sqrt(7)) / 16
    Y = 1j / mp.sqrt(7)
    x, y = mp.log(X)/(2j * mp.pi), mp.log(Y)/(2j * mp.pi)

    def J(z):
        return (
            .5j * mp.pi * z * (1-z)
            + (mp.pi**2/6-mp.polylog(2, mp.exp(2j*mp.pi*z)))/(2j*mp.pi)
        )

    action = (
        J(x+y)-3*J(x)-6*J(y)+J(2*y)
        + 1j*mp.pi*(x*x-x*y+y*y/2+x+y/2)
    )
    cot = lambda z: 1/mp.tan(mp.pi*z)
    hxx = mp.pi*(cot(x+y)-3*cot(x)+2j)
    hxy = mp.pi*(cot(x+y)-1j)
    hyy = mp.pi*(cot(x+y)-6*cot(y)+4*cot(2*y)+1j)
    summand = (
        mp.exp(-1j*mp.pi*(x+y/2)) * mp.sqrt(mp.sin(mp.pi*(x+y)))
        / (8*mp.sin(mp.pi*x)**mp.mpf('1.5')*mp.sin(mp.pi*y)**2)
    )
    amplitude = 2*mp.pi*summand/mp.sqrt(hxx*hyy-hxy*hxy)
    return x, y, action, amplitude


def full_source(level):
    q = mp.exp(1j*mp.pi/level)
    Q = q*q
    factorial = [mp.mpc(1)]
    complete = [mp.mpf(1)]
    for index in range(1, level):
        factorial.append(factorial[-1]*(1-Q**index))
        if level % 2 and 2*index >= level:
            # At odd levels, -2 is an exact simple root.
            complete.append(mp.mpf(0))
        else:
            complete.append(
                complete[-1]*(2*mp.cos((2*index-1)*mp.pi/level)+2)
                / (2*mp.sin(mp.pi*index/level))**2
            )
    columns = []
    for j in range(level):
        coefficient = mp.fsum(
            q**(i*i+(i-j)**2) * factorial[i+j]
            / (factorial[i]**3*factorial[j]**2)
            for i in range(level-j)
        )
        columns.append(coefficient*complete[j])
    return level**2*mp.fsum(columns)


def encode(z):
    return {"real": mp.nstr(mp.re(z), 30), "imag": mp.nstr(mp.im(z), 30)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact-max-level", type=int, default=10)
    parser.add_argument("--levels", default="12,13,24,25,48,49,96,97")
    parser.add_argument("--precision", type=int, default=200)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.exact_max_level < 2 or args.precision < 30:
        parser.error("require exact-max-level >= 2 and precision >= 30")
    exact = [exact_coefficients(n) for n in range(2, args.exact_max_level+1)]
    mp.mp.dps = args.precision
    x, y, action, amplitude = stationary_prediction()
    comparisons = []
    for level in map(int, args.levels.split(',')):
        if level < 2:
            parser.error("levels must be at least two")
        ratio = full_source(level)/(amplitude*mp.exp(level*action))
        comparisons.append({
            "level": level,
            "finite_over_predicted_leading": encode(ratio),
            "level_times_relative_error": encode(level*(ratio-1)),
        })
        print(f"Computed level {level}", flush=True)
    result = {
        "scope": "Exact finite coefficient identity and numerical saddle diagnostics; no global asymptotic theorem is asserted",
        "exact_checks": exact,
        "decimal_precision": args.precision,
        "selected_point": {"x": encode(x), "y": encode(y)},
        "predicted_action": encode(action),
        "predicted_amplitude": encode(amplitude),
        "comparisons": comparisons,
    }
    encoded = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(f"Wrote {args.output}", flush=True)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
