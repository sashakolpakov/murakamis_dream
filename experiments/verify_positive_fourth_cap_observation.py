#!/usr/bin/env python3
"""Exact scalar certificate for a stationary observation of the fourth cap.

Root isolation uses rational bisection. Rate enclosures use the existing
rational logarithm/dilogarithm series with explicit remainder bounds.
Symbolic identities check the stationary elimination and concavity formulas.
No sampled value is used in an asserted comparison.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp

import verify_three_crossing_real_tail_rates as rates


ROOT = Path(__file__).resolve().parents[1]
base = rates.base
R, C, PI, IM = rates.R, rates.C, rates.PI, rates.IM


def quartic_root():
    def polynomial(z):
        return z**4 - 2*z*z - z - 1
    low, high = F(-2), F(-1)
    assert polynomial(low) > 0 > polynomial(high)
    # On [-2,-1], g'(z)=4z(z^2-1)-1 <= -1.
    for _ in range(150):
        middle = (low + high) / 2
        if polynomial(middle) > 0:
            low = middle
        else:
            high = middle
    assert polynomial(low) > 0 > polynomial(high)
    return R(low, high)


def symbolic_checks():
    X, Z, t, h, w = sp.symbols("X Z t h w")
    spectral = (3 - 2*X + t) / 2
    assert sp.cancel(
        (spectral - X*(1+t)**3/8).subs(X, 4/(t*t+3))
    ) == 0

    stationary_lambda = Z*(X-1)**3/(X*(Z-X))
    f = (X-1)*(X*X+1)*Z*Z + X*X*(1-2*X)*Z + X**3
    characteristic = (stationary_lambda**2
                      - (3-2*X)*stationary_lambda + (X-1)**3/X)
    assert sp.cancel(characteristic
                     - (X-1)**3*f/(X*X*(X-Z)**2)) == 0
    reciprocal = sp.cancel(
        X**3*Z**2*f.subs({X: 1/X, Z: 1/Z}, simultaneous=True))
    resultant = sp.factor(sp.resultant(f, reciprocal, Z))
    z = X + 1/X
    expected = (X-1)**4*X**4*(z**4 - 2*z*z - z - 1)
    assert sp.cancel(resultant - expected) == 0

    # h decreases from one to zero as x increases from zero to one half.
    A_log = sp.log((1+h)*(1+3*h*h))/2 - sp.log(1-h)
    B_log = sp.log(1+h) - sp.log((1+3*h*h)*(1-h))/2
    A_derivative = 1/(2*(1+h)) + 3*h/(1+3*h*h) + 1/(1-h)
    B_numerator = 3 - 7*h + 9*h*h + 3*h**3
    B_derivative = B_numerator/(2*(1-h*h)*(1+3*h*h))
    assert sp.cancel(sp.diff(A_log, h) - A_derivative) == 0
    assert sp.cancel(sp.diff(B_log, h) - B_derivative) == 0
    assert sp.expand(B_numerator
                     - (3*h**3 + 9*(h-sp.Rational(7,18))**2
                        + sp.Rational(59,36))) == 0
    # There is no second negative quartic root in [-1,0].
    assert sp.expand((w**4-2*w*w+w-1) - (-w*w+w-1)
                     - w*w*(w*w-1)) == 0
    return {
        "lambda_factorization": "verified",
        "stationary_characteristic_substitution": "verified",
        "unit_circle_resultant": str(resultant),
        "A_log_derivative": str(A_derivative),
        "B_log_derivative": str(B_derivative),
        "B_positive_numerator":
            "3*h^3 + 9*(h-7/18)^2 + 59/36",
        "negative_quartic_uniqueness_reduction": "verified",
    }


def run():
    algebra = symbolic_checks()
    root = quartic_root()
    X = C(root/2, -rates.sqrt_real(1-(root/2).square()))
    branch_root = rates.sqrt_upper(4*X.inverse()-3)
    lam = (3-2*X+branch_root)/2
    assert branch_root.re.lo > 0 and branch_root.im.lo > 0
    assert lam.re.lo > 0 and lam.im.lo > 0
    conjugate_lam = C(lam.re, -lam.im)
    Z = lam / conjugate_lam

    logX = base.logarithm(IM*X) - IM*C(PI/2)
    x = -logX.im/(2*PI)
    k = base.logarithm(lam).im/PI
    assert F(367,1000) < x.lo and x.hi < F(368,1000)
    assert F(214,1000) < k.lo and k.hi < F(215,1000)
    assert (x+k).hi < 1

    A, action_data = rates.stationary_real_rate(X)
    Jxk = rates.sine_integral_from_clock(Z/X)
    Jx = rates.sine_integral_from_clock(X.inverse())
    Jk = rates.sine_integral_from_clock(Z)
    observation = A + Jxk - Jx - Jk
    assert observation.lo > F(3,4)

    peak_root = rates.cubic_real_root()
    peak_X = C(peak_root/2,
               -rates.sqrt_real(1-(peak_root/2).square()))
    peak_A, peak_data = rates.stationary_real_rate(peak_X)
    third_rate = 2*peak_A
    assert third_rate.hi < F(91,100)
    # c>8/25 is the proved exact lower bound in the cap-seed note.
    old_rate_upper = 2*F(91,100)-F(8,25)
    assert old_rate_upper == F(3,2)
    assert 2*observation.lo > old_rate_upper

    script = Path(__file__).resolve()
    dependencies = [Path(rates.__file__).resolve(),
                    Path(base.__file__).resolve()]
    return {
        "status": "passed",
        "method": "Rational root isolation and outward analytic series",
        "rounding_denominator": str(base.DEN),
        "symbolic_identities": algebra,
        "quartic_negative_root": root.record(),
        "selected_clock_X": X.record(),
        "selected_square_root": branch_root.record(),
        "selected_lambda": lam.record(),
        "observation_clock_Z": Z.record(),
        "x": {"interval": x.record(), "bounds": ["367/1000","368/1000"]},
        "k": {"interval": k.record(), "bounds": ["214/1000","215/1000"]},
        "observation": {
            "rate": observation.record(),
            "strict_lower_bound": "3/4",
            "A": A.record(),
            "J_x_plus_k": Jxk.record(),
            "J_x": Jx.record(),
            "J_k": Jk.record(),
            "action_data": action_data,
        },
        "third_moment_rate": {
            "interval": third_rate.record(), "strict_upper_bound": "91/100",
            "cubic_root": peak_root.record(), "action_data": peak_data,
        },
        "old_fourth_lower_rate_strict_upper": str(old_rate_upper),
        "twice_observation_rate_strict_lower": "3/2",
        "scope": ("Scalar and algebraic inputs only; the original finite-sum "
                  "stationary-phase argument is proved separately."),
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "dependencies": {
            str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in dependencies},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-positive-fourth-cap-observation.json")
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("All fourth-cap scalar observation certificates passed.")
    print(f"Saved {args.output}")
