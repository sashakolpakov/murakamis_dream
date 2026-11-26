#!/usr/bin/env python3
"""Outward support certificate for the positive-path maximum-height bound.

Numerical optimization chooses rational support slopes only. Every accepted
parameter box and every boundary segment is checked with Arb interval arithmetic.
No result file is written unless the whole parameter rectangle is covered.
"""
import argparse
import hashlib
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar
from flint import arb, ctx


ctx.prec = 100
PI = arb.pi()


def rat(x):
    if isinstance(x, F):
        return arb(x.numerator) / x.denominator
    return arb(x)


def interval(lo, hi):
    lo, hi = rat(lo), rat(hi)
    return (lo + hi) / 2 + arb(0, ((hi - lo) / 2).upper())


def clipped(x, low, high=None):
    """Intersect an enclosure with an independently known closed range."""
    lo, hi = x.lower(), x.upper()
    low = rat(low)
    if lo < low:
        lo = low
    if high is not None:
        high = rat(high)
        if hi > high:
            hi = high
    assert lo <= hi
    return interval(lo, hi)


def monotone_clipped(x, low, high, method):
    lo, hi = x.lower(), x.upper()
    low = rat(low)
    if lo < low:
        lo = low
    if high is not None and hi > rat(high):
        hi = rat(high)
    assert lo <= hi
    return interval(getattr(lo, method)().lower(),
                    getattr(hi, method)().upper())


def support_value(a, height, parameter, kind, slope):
    denominator = a.cos() + height.cosh()
    ur = clipped(a.sin(), 0) / denominator
    vi = height.sinh() / denominator
    C, S = (height / 2).cosh(), (height / 2).sinh()
    if kind == "arc":
        angle = PI * parameter / 2
        cx = C * clipped(angle.cos(), 0)
        cy = S * clipped(angle.sin(), 0)
    elif kind == "real":
        cx, cy = C * parameter, arb(0)
    elif kind == "imaginary":
        cx, cy = arb(0), S * parameter
    else:
        raise ValueError(kind)
    zx, zy = ur * cx + vi * cy, ur * cy - vi * cx
    dplus = (zx ** 2 + (zy + 1) ** 2).nonnegative_part().sqrt()
    dminus = (zx ** 2 + (zy - 1) ** 2).nonnegative_part().sqrt()
    k = monotone_clipped((dplus + dminus) / 2, 1, None, "acosh")
    g = monotone_clipped((dplus - dminus) / 2, -1, 1, "asin")
    return k - rat(slope) * g


def choose_slope(box):
    al, ah, hl, hh = box
    a = math.pi * float((al + ah) / 2)
    H = float((hl + hh) / 2)
    t = np.linspace(0.0, 1.0, 161)
    C, S = np.cosh(H / 2), np.sinh(H / 2)
    c = np.concatenate((C * np.cos(np.pi * t / 2)
                        + 1j * S * np.sin(np.pi * t / 2),
                        C * t, 1j * S * t))
    r = np.arcsinh(np.tan((a - 1j * H) / 2) * c)
    target_k, target_g = 3 * H / 4, 3 * a / 4 - np.pi / 2
    # The extra slope condition makes the n=3 certificate imply every n>=3.
    upper = min(8.0, 0.9 * float(hl) / (math.pi * float(ah)))
    def objective(lam):
        return np.max(r.real - target_k - lam * (r.imag - target_g))
    chosen = minimize_scalar(objective, bounds=(-8.0, upper),
                             method="bounded", options={"xatol": 1e-7}).x
    slope = F(round(chosen * 1024), 1024)
    # Rational rounding can be toward the upper endpoint, so check directly.
    if not rat(hl) - rat(slope) * PI * rat(ah) > 0:
        slope -= F(1, 1024)
    return slope


def certify_box(box, maximum_segments):
    al, ah, hl, hh = box
    a, height = PI * interval(al, ah), interval(hl, hh)
    slope = choose_slope(box)
    assert height - rat(slope) * a > 0
    target = 3 * height / 4 - rat(slope) * (3 * a / 4 - PI / 2)
    target_lower = target.lower()
    counts = {}
    minimum_slack = None
    for kind in ("arc", "real", "imaginary"):
        stack = [(F(0), F(1))]
        accepted = 0
        visits = 0
        while stack:
            low, high = stack.pop()
            visits += 1
            bound = support_value(a, height, interval(low, high), kind, slope)
            if bound.is_finite() and bound.upper() < target_lower:
                slack = (target_lower - bound.upper()).lower()
                minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
                accepted += 1
                continue
            middle = (low + high) / 2
            point = support_value(a, height, rat(middle), kind, slope)
            if not point.is_finite() or not point.upper() < target_lower:
                return None
            if visits >= maximum_segments or high - low < F(1, 2 ** 16):
                return None
            stack.append((low, middle))
            stack.append((middle, high))
        counts[kind] = accepted
    return {"box": [str(x) for x in box], "slope": str(slope),
            "boundary_segments": counts, "minimum_support_slack": str(minimum_slack)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1]
                        / "repro/results/research-positive-path-maximum-height.json")
    parser.add_argument("--maximum-segments", type=int, default=384)
    parser.add_argument("--maximum-boxes", type=int, default=100000)
    args = parser.parse_args()
    # Coarse reduction: the written proof shows monotonicity for H>=2.
    coarse = (arb(5) / 2).cosh() - (arb(1) / 2).cosh() - arb(2).cosh() - 1
    assert coarse > 0
    stack = [(F(i, 8), F(i + 1, 8),
              F(23, 20) + F(17 * j, 80), F(23, 20) + F(17 * (j + 1), 80))
             for i in range(8) for j in range(4)]
    accepted = []
    visited = 0
    started = time.monotonic()
    last_report = started
    while stack:
        box = stack.pop()
        visited += 1
        assert visited <= args.maximum_boxes, "Parameter-box budget exceeded; no certificate saved."
        result = certify_box(box, args.maximum_segments)
        if result is not None:
            accepted.append(result)
        else:
            al, ah, hl, hh = box
            if math.pi * float(ah - al) >= float(hh - hl):
                middle = (al + ah) / 2
                stack.extend(((al, middle, hl, hh), (middle, ah, hl, hh)))
            else:
                middle = (hl + hh) / 2
                stack.extend(((al, ah, hl, middle), (al, ah, middle, hh)))
        now = time.monotonic()
        if now - last_report >= 20:
            print(json.dumps({"accepted": len(accepted), "visited": visited,
                              "pending": len(stack), "seconds": round(now - started, 1),
                              "current_box": [str(x) for x in box]}), flush=True)
            last_report = now
    # A disjoint subdivision of the 32 initial boxes covers the full rectangle.
    area = sum((F(r["box"][1]) - F(r["box"][0]))
               * (F(r["box"][3]) - F(r["box"][2])) for r in accepted)
    assert area == F(17, 20)
    result = {
        "status": "passed", "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "precision_bits": ctx.prec, "domain": {"angle_over_pi": ["0", "1"], "height": ["23/20", "2"]},
        "base_power": 3, "all_larger_powers": "H-lambda*a > 0 checked on every parameter box",
        "coarse_height_two_margin": str(coarse), "visited_boxes": visited,
        "accepted_boxes": len(accepted),
        "boundary_segments": sum(sum(r["boundary_segments"].values()) for r in accepted),
        "elapsed_seconds": time.monotonic() - started, "certificate": accepted,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "certificate"}, indent=2))


if __name__ == "__main__":
    main()
