#!/usr/bin/env python3
"""Check the exact even radical reflection and rational rate separation.

The asymptotic theorem is proved in the companion note. Finite kernel
rates below are diagnostics, not substitutes for the uniform proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEPENDENCIES = (
    "experiments/check_even_complete_radical_asymptotic.py",
    "notes/research_even_complete_radical_asymptotic.md",
    "notes/research_last_physical_row_riccati.md",
    "notes/research_even_complete_low_kernel.md",
    "notes/research_bare_kernel_power_three_obstruction.md",
)


def rational_checks():
    records = []

    def check(name, left, right, relation="<"):
        passed = left < right if relation == "<" else left == right
        if not passed:
            raise AssertionError((name, left, relation, right))
        records.append({
            "name": name, "left": str(left), "relation": relation,
            "right": str(right), "status": "passed",
        })

    catalan_upper = sum((F((-1)**j, (2*j+1)**2)
                         for j in range(15)), F(0))
    check("Catalan alternating upper bound", catalan_upper, F(11, 12))
    check("sqrt(3) upper bound squared", F(3), F(26, 15)**2)
    machin_lower = 16*(F(1, 5)-F(1, 375))-F(4, 239)
    check("Machin lower bound for pi", F(157, 50), machin_lower)
    check("phase numerator", 4*F(11, 12)+F(26, 15)-2, F(17, 5), "=")
    check("phase rate upper bound", F(17, 5)/F(157, 50), F(170, 157), "=")
    check("sqrt(13) lower bound squared", F(18, 5)**2, F(13))
    check("cosh(H) algebraic lower bound", (11+3*F(18, 5))/8, F(109, 40), "=")
    check("cosh(H) versus 33/20", F(33, 20)**2, F(109, 40))
    x = F(13, 12)
    ratio = x*x/F(9*10)
    check("positive Taylor tail ratio", ratio, F(1))
    cosh_upper = sum((x**(2*j)/math.factorial(2*j)
                      for j in range(4)), F(0))
    cosh_upper += x**8/math.factorial(8)/(1-ratio)
    check("cosh(13/12) Taylor upper bound", cosh_upper, F(33, 20))
    check("strict rational rate gap", F(13, 12)-F(170, 157), F(1, 1884), "=")
    return records


def direct_kernels(level, w):
    """Original Newton products; no Riccati recurrence is used."""
    colors = [
        mp.mpf(-2) if 2*j+1 == level
        else 2*mp.cospi(mp.mpf(2*j+1)/level)
        for j in range(level)
    ]
    squares = [(2*mp.sinpi(mp.mpf(j)/level))**2
               for j in range(level)]
    complete, ordinary = [mp.mpc(1)], [mp.mpc(1)]
    for j in range(1, level):
        complete.append(complete[-1]*(colors[j-1]+2)/squares[j])
        ordinary.append(ordinary[-1]*(colors[j-1]-w)/squares[j])
    cutoff = level-level//2
    products = [a*b for a, b in zip(complete, ordinary)]
    low = mp.fsum(products[:cutoff])
    high = mp.fsum(products[cutoff:])
    return low, high, mp.fsum(products), colors, squares


def chebyshev_polynomial(level, w):
    """P_N=2T_N(w/2)+2 by its defining polynomial recurrence."""
    previous, current = mp.mpc(1), w/2
    if level == 0:
        return mp.mpc(4)
    for _ in range(1, level):
        previous, current = current, w*current-previous
    return 2*current+2


def reflected_radical(level, w, colors, squares):
    term = 1/((colors[0]+2)*(colors[0]-w))
    terms = [term]
    for r in range(1, level//2):
        term *= squares[r]**2/((colors[r]+2)*(colors[r]-w))
        terms.append(term)
    polynomial = chebyshev_polynomial(level, w)
    return 4*polynomial*mp.fsum(terms)/level**4, polynomial, 4*terms[0]


def relative_error(a, b):
    return abs(a-b)/max(mp.mpf(1), abs(a), abs(b))


def complex_record(z, digits=32):
    return [mp.nstr(z.real, digits), mp.nstr(z.imag, digits)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=1000,
                        help="decimal digits for direct finite Newton products")
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-even-complete-radical-asymptotic.json")
    args = parser.parse_args()
    if args.precision < 800:
        parser.error("use at least 800 digits for the largest diagnostic levels")
    mp.mp.dps = args.precision
    rational = rational_checks()
    w_star = mp.mpc(mp.mpf(1)/2, -3*mp.sqrt(3)/2)
    t_star = mp.acos(-w_star/2)
    height = -t_star.imag
    equation = 3*t_star+4j*mp.asinh(mp.sin(t_star/2))-2*mp.pi
    homogeneous_error = abs(equation)
    height_identity_error = abs(mp.cosh(height)**2-(11+3*mp.sqrt(13))/8)
    if max(homogeneous_error, height_identity_error) > mp.power(10, -args.precision//2):
        raise AssertionError("algebraic point or original logarithmic branch failed")
    colors_to_test = [w_star, mp.mpc("-0.7", "1.3"), mp.mpc("1.4", "-2.2")]
    maximum_error = mp.mpf(0)
    reflection_count = 0
    for level in (2, 4, 6, 8, 16, 32):
        for w in colors_to_test:
            _, high, _, colors, squares = direct_kernels(level, w)
            reflected, _, _ = reflected_radical(level, w, colors, squares)
            maximum_error = max(maximum_error, relative_error(high, reflected))
            reflection_count += 1
    if maximum_error > mp.power(10, -args.precision//2):
        raise AssertionError("original finite reflection identity failed")
    with mp.workdps(100):
        c = mp.sqrt(2-w_star)/2
        phase = 2/mp.pi*mp.quad(
            lambda y: mp.asinh(c*mp.cot(y)),
            [0, mp.pi/4, mp.pi/2],
        )
    diagnostics = []
    for level in (512, 513, 1024, 1025, 2048, 2049):
        low, high, full, colors, squares = direct_kernels(level, w_star)
        entry = {
            "level": level,
            "low_rate": mp.nstr(mp.log(abs(low))/level, 32),
            "full_rate": mp.nstr(mp.log(abs(full))/level, 32),
        }
        if level % 2:
            if high != 0:
                raise AssertionError("odd complete-end radical did not vanish exactly")
            entry["high_is_exact_zero"] = True
        else:
            reflected, polynomial, leading = reflected_radical(
                level, w_star, colors, squares)
            error = relative_error(high, reflected)
            if error > mp.power(10, -100):
                raise AssertionError("large-level reflection comparison lost precision")
            normalized = level**4*high/polynomial
            entry.update({
                "high_rate": mp.nstr(mp.log(abs(high))/level, 32),
                "relative_reflection_error": mp.nstr(error, 18),
                "N4_high_over_P": complex_record(normalized),
                "N4_remainder_after_finite_leading_term":
                    complex_record(level**4*(normalized-leading)),
            })
        diagnostics.append(entry)
    record = {
        "status": "passed",
        "scope": "exact rational comparisons and finite identity diagnostics; asymptotic proof is written",
        "precision_digits": args.precision,
        "rational_comparisons": rational,
        "finite_reflection_identity_count": reflection_count,
        "maximum_relative_reflection_error": mp.nstr(maximum_error, 24),
        "homogeneous_equation_error": mp.nstr(homogeneous_error, 18),
        "height_algebraic_identity_error": mp.nstr(height_identity_error, 18),
        "algebraic_color": complex_record(w_star),
        "selected_angle": complex_record(t_star),
        "phase_numerical_diagnostic": complex_record(phase),
        "exact_rate_gap_lower_bound": "1/1884",
        "kernel_rate_diagnostics": diagnostics,
        "project_dependency_sha256": {
            name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            for name in DEPENDENCIES
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": record["status"],
        "rational_comparisons": len(rational),
        "finite_reflection_identity_count": reflection_count,
        "maximum_relative_reflection_error": record["maximum_relative_reflection_error"],
        "diagnostic_levels": [d["level"] for d in diagnostics],
    }, indent=2))


if __name__ == "__main__":
    main()
