#!/usr/bin/env python3
"""Outward support bounds for simultaneous activation of an adjacent pair.

The scaled mode excludes H >= 59*charge/50 for H >= 1/1000.
The affine mode excludes H >= 37/200 + 37*charge/40 for charge >= 4/5.
Both assume the separately proved global height cap. Affine mode also
uses the proved tangent-sector bound sinh(h)/sin(b) < sqrt(3).
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

from certify_positive_path_maximum_height import interval, rat, clipped, monotone_clipped


def charge_bound(height, mode):
    if mode == "scaled":
        return height * 50 / 59
    raw = (height - rat(F(37, 200))) * 40 / 37
    return interval(min(raw.lower(), arb(1)), min(raw.upper(), arb(1)))


def return_support(a, height, cap, parameter, kind, slope):
    den = a.cos() + height.cosh()
    ur = clipped(a.sin(), 0) / den
    vi = height.sinh() / den
    if kind in ("arc", "real", "imaginary"):
        C, S = (cap / 2).cosh(), (cap / 2).sinh()
        if kind == "arc":
            b = arb.pi() * parameter / 2
            cx, cy = C * clipped(b.cos(), 0), S * clipped(b.sin(), 0)
        elif kind == "real":
            cx, cy = C * parameter, arb(0)
        else:
            cx, cy = arb(0), S * parameter
    elif kind == "bottom":
        cx, cy = parameter, arb(0)
    else:
        root3 = arb(3).sqrt()
        cut = monotone_clipped(cap.sinh() / root3, 0, 1, "asin")
        if kind == "left":
            b = cut * parameter
            h = monotone_clipped(root3 * clipped(b.sin(), 0), 0, None, "asinh")
        elif kind == "right":
            b = arb.pi() - cut * parameter
            h = monotone_clipped(root3 * clipped(b.sin(), 0), 0, None, "asinh")
        elif kind == "top":
            b = cut + (arb.pi() - 2 * cut) * parameter
            h = cap
        else:
            raise ValueError(kind)
        cx = clipped((b / 2).cos(), 0) * (h / 2).cosh()
        cy = clipped((b / 2).sin(), 0) * (h / 2).sinh()
    zx, zy = ur * cx + vi * cy, ur * cy - vi * cx
    if not zx.is_finite() or not zy.is_finite():
        return arb("nan")
    plus = (zx**2 + (zy + 1)**2).nonnegative_part().sqrt()
    minus = (zx**2 + (zy - 1)**2).nonnegative_part().sqrt()
    k = monotone_clipped((plus + minus) / 2, 1, None, "acosh")
    g = monotone_clipped((plus - minus) / 2, -1, 1, "asin")
    return k - rat(slope) * g


def sampled_returns(a, height, cap, mode):
    u = np.linspace(0, 1, 193)
    if mode == "scaled":
        C, S = np.cosh(cap / 2), np.sinh(cap / 2)
        c = np.r_[C * np.cos(np.pi * u / 2) + 1j * S * np.sin(np.pi * u / 2),
                  C * u, 1j * S * u]
    else:
        cut = np.arcsin(np.sinh(cap) / np.sqrt(3))
        b = np.r_[cut*u, cut + (np.pi-2*cut)*u, np.pi-cut*u]
        h = np.minimum(cap, np.arcsinh(np.sqrt(3)*np.maximum(np.sin(b), 0)))
        c = np.r_[np.cos((b-1j*h)/2), u]
    return np.arcsinh(np.tan((a-1j*height)/2)*c)


def certify_box(box, mode, max_segments):
    al, ah, hl, hh = box
    a, height = arb.pi() * interval(al, ah), interval(hl, hh)
    amid, hmid = math.pi*float((al+ah)/2), float((hl+hh)/2)
    samples = [sampled_returns(amid, hmid, cap, mode) for cap in (1.15, hmid)]
    ch = min(1, hmid*50/59 if mode == "scaled" else (hmid-.185)*40/37)

    def objective(slope):
        return (sum(np.max(r.real-slope*r.imag) for r in samples)
                - 1.5*hmid + slope*(1.5*amid-np.pi*ch))

    opt = minimize_scalar(objective, bounds=(-64, 0), method="bounded")
    slope = min(F(round(opt.x*4096), 4096), F(0))
    target = 3*height/2-rat(slope)*(3*a/2-arb.pi()*charge_bound(height, mode))
    target_lower = target.lower()
    maxima = [float(np.max(r.real-float(slope)*r.imag)) for r in samples]
    gap = float(target_lower)-sum(maxima)
    if gap <= 0:
        return None
    budgets = [F.from_float(value + .45*gap) for value in maxima]
    if not sum((rat(v) for v in budgets), arb(0)) < target_lower:
        return None
    kinds = ("arc", "real", "imaginary") if mode == "scaled" else (
        "left", "top", "right", "bottom")
    all_counts = []
    minimum_slack = None
    for cap, budget in zip((rat(F(23, 20)), height), budgets):
        counts = {}
        for kind in kinds:
            stack = [(F(0), F(1))]
            accepted = visits = 0
            while stack:
                low, high = stack.pop()
                visits += 1
                bound = return_support(a, height, cap, interval(low, high), kind, slope)
                if bound.is_finite() and bound.upper() < rat(budget):
                    slack = (rat(budget)-bound.upper()).lower()
                    minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
                    accepted += 1
                    continue
                middle = (low+high)/2
                point = return_support(a, height, cap, rat(middle), kind, slope)
                if (not point.is_finite() or not point.upper() < rat(budget)
                        or visits >= max_segments or high-low < F(1, 2**18)):
                    return None
                stack.extend(((low, middle), (middle, high)))
            counts[kind] = accepted
        all_counts.append(counts)
    return {
        "box": [str(v) for v in box], "slope": str(slope),
        "support_budgets": [str(v) for v in budgets],
        "boundary_segments": all_counts,
        "minimum_boundary_slack": str(minimum_slack),
        "target_slack": str((target_lower-sum((rat(v) for v in budgets), arb(0))).lower()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("scaled", "affine"), required=True)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--maximum-boxes", type=int, default=300000)
    parser.add_argument("--maximum-segments", type=int, default=512)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    assert ctx.prec >= 100
    lower = F(1, 1000) if args.mode == "scaled" else F(37, 40)
    upper = F(23, 20)
    heights = ([lower, F(1, 100), F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(1), upper]
               if args.mode == "scaled" else [lower, F(1), F(111, 100), upper])
    stack = [(F(i, 8), F(i+1, 8), low, high)
             for i in range(8) for low, high in zip(heights, heights[1:])]
    accepted = []
    visits = 0
    start = last = time.monotonic()
    while stack:
        box = stack.pop()
        visits += 1
        assert visits <= args.maximum_boxes, "Coverage unfinished; no certificate saved."
        result = certify_box(box, args.mode, args.maximum_segments)
        if result is not None:
            accepted.append(result)
        else:
            al, ah, hl, hh = box
            if math.pi*float(ah-al) >= float(hh-hl):
                mid = (al+ah)/2
                stack.extend(((al, mid, hl, hh), (mid, ah, hl, hh)))
            else:
                mid = (hl+hh)/2
                stack.extend(((al, ah, hl, mid), (al, ah, mid, hh)))
        now = time.monotonic()
        if now-last >= 20:
            print(json.dumps({"mode": args.mode, "accepted": len(accepted),
                              "visited": visits, "pending": len(stack),
                              "seconds": round(now-start, 1),
                              "current_box": [str(v) for v in box]}), flush=True)
            last = now
    area = sum((F(r["box"][1])-F(r["box"][0]))*(F(r["box"][3])-F(r["box"][2]))
               for r in accepted)
    assert area == upper-lower
    here = Path(__file__).resolve()
    dep = here.with_name("certify_positive_path_maximum_height.py")
    record = {
        "status": "passed", "mode": args.mode, "precision_bits": ctx.prec,
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "dependency_sha256": {dep.name: hashlib.sha256(dep.read_bytes()).hexdigest()},
        "domain": {"angle_over_pi": ["0", "1"], "height": [str(lower), str(upper)]},
        "accepted_boxes": len(accepted), "visited_boxes": visits,
        "boundary_segments": sum(sum(sum(c.values()) for c in r["boundary_segments"])
                                 for r in accepted),
        "elapsed_seconds": time.monotonic()-start, "certificate": accepted,
    }
    output = args.output or here.parents[1] / (
        "repro/results/research-positive-pair-activation-height-"+args.mode+".json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({k:v for k,v in record.items() if k != "certificate"}, indent=2))


if __name__ == "__main__":
    main()
