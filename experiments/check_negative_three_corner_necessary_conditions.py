#!/usr/bin/env python3
"""An exact open-box witness for three necessary corner inequalities.

This does not construct a corner, a KKT solution, or a geometric filling.
All decisions use rational interval arithmetic, including Machin bounds
for pi and convergent rational bounds for sine and logarithm.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path

import verify_conway_two_leaf_block_alias_certificate as arith

I, PI, SCALE = arith.I, arith.PI, arith.S


def sqrt_interval(value):
    assert value.lo >= 0
    lower = isqrt(value.lo * SCALE)
    upper = isqrt(value.hi * SCALE)
    if upper * upper < value.hi * SCALE:
        upper += 1
    return I(lower, upper, raw=True)


def asinh_interval(value):
    assert value.lo > 0
    return arith.logi(value + sqrt_interval(1 + value * value))


def sine(interval):
    lo, hi = interval
    assert 0 < lo < hi < 1
    ends = [arith.sinpi(lo), arith.sinpi(hi)]
    upper = max(x.hi for x in ends)
    if lo <= F(1, 2) <= hi:
        upper = SCALE
    return I(min(x.lo for x in ends), upper, raw=True)


def cosine(interval):
    lo, hi = interval
    assert 0 < lo < hi < 1
    def point(x):
        if x < F(1, 2):
            return arith.sinpi(F(1, 2) - x)
        return -arith.sinpi(x - F(1, 2))
    return I(point(hi).lo, point(lo).hi, raw=True)


def verify():
    radius = F(1, 100000)
    theta = (F(5, 6) - radius, F(5, 6) + radius)
    phi = (F(79, 100) - radius, F(79, 100) + radius)
    st, ct, sp, cp = sine(theta), cosine(theta), sine(phi), cosine(phi)
    X = asinh_interval(-ct * sp / st) / 2
    H = asinh_interval(-cp * st / sp) / 2
    R = sqrt_interval(1 - ct * ct * cp * cp) / (-ct * (1 - cp))
    g = ((3 * theta[0] - 1 - phi[1]) / 2,
         (3 * theta[1] - 1 - phi[0]) / 2)
    assert 0 < g[0] < g[1] < F(1, 2)
    C4 = (4 * asinh_interval(I(F(1, 4))) + asinh_interval(I(4))) / 2
    margins = {
        "cos_g_minus_R_sin_g": cosine(g) - R * sine(g),
        "four_pi_minus_theta_minus_four_phi":
            (4 - I(*theta) - 4 * I(*phi)) * PI,
        "four_X_minus_C4_minus_H": 4 * X - C4 - H,
    }
    thresholds = {
        "cos_g_minus_R_sin_g": F(1, 100),
        "four_pi_minus_theta_minus_four_phi": F(1, 50),
        "four_X_minus_C4_minus_H": F(1, 400),
    }
    for name, value in margins.items():
        assert F(value.lo, SCALE) > thresholds[name], (name, value.bounds())
    paths = [Path(__file__), Path(arith.__file__)]
    return {
        "claim": "Only the three stated necessary inequalities are feasible.",
        "not_claimed": "No corner covector, KKT solution, or minimizer is constructed.",
        "n": 4,
        "theta_over_pi": list(map(str, theta)),
        "phi_over_pi": list(map(str, phi)),
        "exact_rational_bounds": {name: value.bounds()
                                  for name, value in margins.items()},
        "strict_lower_bounds": {name: str(value)
                               for name, value in thresholds.items()},
        "sha256": {str(path.name): hashlib.sha256(path.read_bytes()).hexdigest()
                   for path in paths},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output)
