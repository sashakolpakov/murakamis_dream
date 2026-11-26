#!/usr/bin/env python3
"""Replay a saved pair-activation support certificate without optimization.

The parameter rectangles must form an exact cover with multiplicity one.
Every stored rational slope and support budget is checked afresh at 160 bits.
The two return domains and the branch-safe return formula are implemented here;
no code is imported from the certificate generator.
"""

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import arb, ctx


def ball(value):
    if isinstance(value, F):
        return arb(value.numerator) / value.denominator
    return arb(value)


def span(low, high):
    return ball(low).union(ball(high))


def restricted_endpoints(value, low, high=None):
    left = max(value.lower(), ball(low))
    right = value.upper() if high is None else min(value.upper(), ball(high))
    assert left <= right, "An independently known range became empty."
    return left, right


def positive(value):
    return span(*restricted_endpoints(value, 0))


def increasing(value, low, high, operation):
    left, right = restricted_endpoints(value, low, high)
    return span(getattr(left, operation)().lower(),
                getattr(right, operation)().upper())


class CoverTree:
    """Exact multiplicity of intervals between consecutive rational abscissae."""

    def __init__(self, count):
        self.count = count
        self.low = [0] * (4 * count)
        self.high = [0] * (4 * count)
        self.lazy = [0] * (4 * count)

    def add(self, left, right, amount, node=1, start=0, stop=None):
        if stop is None:
            stop = self.count
        if right <= start or stop <= left:
            return
        if left <= start and stop <= right:
            self.low[node] += amount
            self.high[node] += amount
            self.lazy[node] += amount
            return
        middle = (start + stop) // 2
        self.add(left, right, amount, 2 * node, start, middle)
        self.add(left, right, amount, 2 * node + 1, middle, stop)
        self.low[node] = self.lazy[node] + min(self.low[2 * node], self.low[2 * node + 1])
        self.high[node] = self.lazy[node] + max(self.high[2 * node], self.high[2 * node + 1])


def verify_cover(records, height_low, height_high):
    events = defaultdict(list)
    coordinates = {F(0), F(1)}
    area = F(0)
    for row in records:
        al, ah, hl, hh = map(F, row["box"])
        assert 0 <= al < ah <= 1
        assert height_low <= hl < hh <= height_high
        coordinates.update((al, ah))
        events[hl].append((al, ah, 1))
        events[hh].append((al, ah, -1))
        area += (ah - al) * (hh - hl)
    coordinates = sorted(coordinates)
    indices = {x: j for j, x in enumerate(coordinates)}
    heights = sorted(events)
    assert heights[0] == height_low and heights[-1] == height_high
    tree = CoverTree(len(coordinates) - 1)
    for height in heights:
        for al, ah, amount in events[height]:
            tree.add(indices[al], indices[ah], amount)
        expected = 0 if height == height_high else 1
        assert tree.low[1] == tree.high[1] == expected, (
            "Gap or overlap in the exact parameter cover", str(height),
            tree.low[1], tree.high[1])
    assert area == height_high - height_low
    return {"area": str(area), "height_slices": len(heights) - 1,
            "angle_subintervals": len(coordinates) - 1,
            "cover_multiplicity": 1}


def boundary_function(angle, height, cap, slope, mode, kind):
    denominator = angle.cos() + height.cosh()
    real_a = positive(angle.sin()) / denominator
    minus_imag_a = height.sinh() / denominator
    if mode == "scaled":
        c_axis, s_axis = (cap / 2).cosh(), (cap / 2).sinh()
    else:
        cut = increasing(cap.sinh() / arb(3).sqrt(), 0, 1, "asin")

    def support(parameter):
        if mode == "scaled":
            if kind == "real":
                cx, cy = c_axis * parameter, arb(0)
            elif kind == "imaginary":
                cx, cy = arb(0), s_axis * parameter
            else:
                theta = arb.pi() * parameter / 2
                cx = c_axis * positive(theta.cos())
                cy = s_axis * positive(theta.sin())
        elif kind == "bottom":
            cx, cy = parameter, arb(0)
        elif kind in ("left", "right"):
            # On the right branch use b=pi-d explicitly. This avoids subtracting
            # near-endpoint angles before evaluating their sine and cosine.
            d = cut * parameter
            h = increasing(arb(3).sqrt() * positive(d.sin()), 0, None, "asinh")
            if kind == "left":
                cx = positive((d / 2).cos()) * (h / 2).cosh()
                cy = positive((d / 2).sin()) * (h / 2).sinh()
            else:
                cx = positive((d / 2).sin()) * (h / 2).cosh()
                cy = positive((d / 2).cos()) * (h / 2).sinh()
        else:
            b = cut + (arb.pi() - 2 * cut) * parameter
            cx = positive((b / 2).cos()) * (cap / 2).cosh()
            cy = positive((b / 2).sin()) * (cap / 2).sinh()
        zx = real_a * cx + minus_imag_a * cy
        zy = real_a * cy - minus_imag_a * cx
        if not zx.is_finite() or not zy.is_finite():
            return arb("nan")
        d_plus = (zx ** 2 + (zy + 1) ** 2).nonnegative_part().sqrt()
        d_minus = (zx ** 2 + (zy - 1) ** 2).nonnegative_part().sqrt()
        k = increasing((d_plus + d_minus) / 2, 1, None, "acosh")
        g = increasing((d_plus - d_minus) / 2, -1, 1, "asin")
        return k - slope * g

    return support


def replay_row(row, mode):
    al, ah, hl, hh = map(F, row["box"])
    angle, height = arb.pi() * span(al, ah), span(hl, hh)
    rational_slope = F(row["slope"])
    assert rational_slope <= 0
    slope = ball(rational_slope)
    budgets = [ball(F(value)) for value in row["support_budgets"]]
    assert len(budgets) == 2
    if mode == "scaled":
        charge = 50 * height / 59
        kinds = ("arc", "real", "imaginary")
    else:
        raw_charge = (height - ball(F(37, 200))) * 40 / 37
        charge = span(min(raw_charge.lower(), arb(1)), min(raw_charge.upper(), arb(1)))
        kinds = ("left", "top", "right", "bottom")
    target = 3 * height / 2 - slope * (3 * angle / 2 - arb.pi() * charge)
    target_margin = (target - sum(budgets, arb(0))).lower()
    assert target_margin > 0, "The stored support budgets do not imply separation."
    margin = target_margin
    visits = leaves = 0
    for cap, budget in zip((ball(F(23, 20)), height), budgets):
        for kind in kinds:
            support = boundary_function(angle, height, cap, slope, mode, kind)
            pending = [(F(0), F(1), 0)]
            while pending:
                low, high, depth = pending.pop()
                visits += 1
                value = support(span(low, high))
                if value.is_finite() and value.upper() < budget.lower():
                    margin = min(margin, (budget.lower() - value.upper()).lower())
                    leaves += 1
                    continue
                assert depth < 25, ("A saved support bound failed fresh replay", row["box"], kind)
                middle = (low + high) / 2
                midpoint_value = support(ball(middle))
                assert midpoint_value.is_finite() and midpoint_value.upper() < budget.lower(), (
                    "The saved budget could not be reproduced even at a boundary midpoint",
                    row["box"], kind, str(middle))
                pending.extend(((low, middle, depth + 1), (middle, high, depth + 1)))
    return visits, leaves, margin


def scalar_consequence():
    integral = 2 * (F(59, 50) * F(4, 5) ** 2 / 2 + F(37, 200) / 5
                    + F(37, 40) * (1 - F(4, 5) ** 2) / 2)
    assert integral == F(5811, 5000)
    catalan_lower = sum((F((-1) ** j, (2 * j + 1) ** 2) for j in range(8)), F())
    margin = 4 * catalan_lower / F(22, 7) - integral
    assert margin == F(712208857, 637702065000) and margin > F(1, 1000)
    return {"twice_integrated_height_envelope": str(integral),
            "catalan_lower_bound": str(catalan_lower),
            "volume_rate_margin_lower_bound": str(margin)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    assert ctx.prec >= 160
    here = Path(__file__).resolve()
    script_hash = hashlib.sha256(here.read_bytes()).hexdigest()
    input_bytes = args.certificate.read_bytes()
    data = json.loads(input_bytes)
    assert data["status"] == "passed"
    mode = data["mode"]
    assert mode in ("scaled", "affine")
    height_low = F(1, 1000) if mode == "scaled" else F(37, 40)
    height_high = F(23, 20)
    assert data["domain"] == {"angle_over_pi": ["0", "1"],
                              "height": [str(height_low), str(height_high)]}
    records = data["certificate"]
    assert len(records) == data["accepted_boxes"]
    cover = verify_cover(records, height_low, height_high)
    total_visits = total_leaves = 0
    margin = None
    started = last_report = time.monotonic()
    for index, row in enumerate(records, 1):
        visits, leaves, row_margin = replay_row(row, mode)
        total_visits += visits
        total_leaves += leaves
        margin = row_margin if margin is None else min(margin, row_margin)
        now = time.monotonic()
        if now - last_report >= 20:
            print(json.dumps({"mode": mode, "replayed": index, "total": len(records),
                              "seconds": round(now - started, 1)}), flush=True)
            last_report = now
    result = {"status": "passed", "mode": mode, "precision_bits": ctx.prec,
              "script_sha256": script_hash,
              "input_certificate_sha256": hashlib.sha256(input_bytes).hexdigest(),
              "generator_script_sha256_in_input": data["script_sha256"],
              "parameter_boxes": len(records), "exact_cover": cover,
              "boundary_segments": total_leaves, "boundary_visits": total_visits,
              "minimum_strict_margin": str(margin),
              "scalar_consequence": scalar_consequence(),
              "elapsed_seconds": time.monotonic() - started}
    output = args.output or here.parents[1] / (
        "repro/results/research-positive-pair-activation-height-" + mode + "-replay.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
