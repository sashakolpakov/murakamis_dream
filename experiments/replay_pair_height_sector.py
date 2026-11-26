#!/usr/bin/env python3
"""Independently replay a completed sector-restricted pair-height certificate.

No certificate-generator code or optimizer is imported. Parameter rectangles
and stored arc partitions are checked for exact multiplicity-one coverage.
Every analytic inequality is recomputed at 160 bits or more.
"""

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx


def rational(value):
    value = F(value)
    return arb(value.numerator)/value.denominator


def hull(low, high):
    return low.union(high)


def clipped(value, low, high=None):
    left = max(value.lower(), rational(low))
    right = value.upper() if high is None else min(value.upper(), rational(high))
    assert left <= right
    return hull(left, right)


def increasing(value, low, high, method):
    # Apply the monotone function before rebuilding a ball. Rebuilding first
    # can round a clipped endpoint just outside acosh/asin's real domain.
    left = max(value.lower(), rational(low))
    right = value.upper() if high is None else min(value.upper(), rational(high))
    assert left <= right
    return hull(getattr(left, method)().lower(),
                getattr(right, method)().upper())


def square(value):
    low, high = value.lower(), value.upper()
    if low >= 0:
        return hull((low*low).lower(), (high*high).upper())
    if high <= 0:
        return hull((high*high).lower(), (low*low).upper())
    return hull(arb(0), max((low*low).upper(), (high*high).upper()))


class CoverTree:
    def __init__(self, count):
        self.count = count
        self.low = [0]*(4*count)
        self.high = [0]*(4*count)
        self.lazy = [0]*(4*count)

    def add(self, left, right, change, node=1, start=0, stop=None):
        stop = self.count if stop is None else stop
        if right <= start or stop <= left:
            return
        if left <= start and stop <= right:
            self.low[node] += change
            self.high[node] += change
            self.lazy[node] += change
            return
        mid = (start+stop)//2
        self.add(left, right, change, 2*node, start, mid)
        self.add(left, right, change, 2*node+1, mid, stop)
        self.low[node] = self.lazy[node]+min(self.low[2*node], self.low[2*node+1])
        self.high[node] = self.lazy[node]+max(self.high[2*node], self.high[2*node+1])


def verify_cover(records, low, high):
    endpoints, events, area = {F(0), F(1)}, defaultdict(list), F(0)
    for record in records:
        xl, xh, hl, hh = map(F, record["box"])
        assert 0 <= xl < xh <= 1 and low <= hl < hh <= high
        endpoints.update((xl, xh))
        events[hl].append((xl, xh, 1))
        events[hh].append((xl, xh, -1))
        area += (xh-xl)*(hh-hl)
    xs, hs = sorted(endpoints), sorted(events)
    assert hs[0] == low and hs[-1] == high
    index = {x: j for j, x in enumerate(xs)}
    tree = CoverTree(len(xs)-1)
    for height in hs:
        for left, right, amount in events[height]:
            tree.add(index[left], index[right], amount)
        expected = 0 if height == high else 1
        assert tree.low[1] == tree.high[1] == expected, (
            "Parameter gap or overlap", str(height), tree.low[1], tree.high[1])
    assert area == high-low
    return {"multiplicity": 1, "area": str(area),
            "height_slabs": len(hs)-1, "sector_subintervals": len(xs)-1}


def verify_arc_partition(segments):
    intervals = sorted(tuple(map(F, item)) for item in segments)
    previous = F(0)
    for low, high in intervals:
        assert low == previous and low < high <= 1, "Arc gap or overlap"
        previous = high
    assert previous == 1
    return intervals


def angle_interval(box):
    xl, xh, hl, hh = map(F, box)
    c_low = (rational(hl).sinh()/arb(3).sqrt()).asin()
    c_high = (rational(hh).sinh()/arb(3).sqrt()).asin()
    # a is increasing in the sector coordinate; its dependence on the
    # cut changes sign at coordinate 1/2.
    left_cut = c_low if xl <= F(1,2) else c_high
    right_cut = c_high if xh <= F(1,2) else c_low
    left = arb.pi()*rational(xl)+(1-2*rational(xl))*left_cut
    right = arb.pi()*rational(xh)+(1-2*rational(xh))*right_cut
    return hull(left.lower(), right.upper())


def boundary_coordinates(cap, parameter, kind):
    if kind == "arc":
        t = arb.pi()*parameter/2
        return ((cap/2).cosh()*clipped(t.cos(), 0),
                (cap/2).sinh()*clipped(t.sin(), 0))
    cut = increasing(cap.sinh()/arb(3).sqrt(), 0, 1, "asin")
    if kind in ("left", "right"):
        d = cut*parameter
        h = increasing(arb(3).sqrt()*clipped(d.sin(), 0), 0, None, "asinh")
        if kind == "left":
            return (clipped((d/2).cos(), 0)*(h/2).cosh(),
                    clipped((d/2).sin(), 0)*(h/2).sinh())
        # Independent right-arc formula with beta=pi-d.
        return (clipped((d/2).sin(), 0)*(h/2).cosh(),
                clipped((d/2).cos(), 0)*(h/2).sinh())
    assert kind == "top"
    beta = cut+(arb.pi()-2*cut)*parameter
    return (clipped((beta/2).cos(), 0)*(cap/2).cosh(),
            clipped((beta/2).sin(), 0)*(cap/2).sinh())


def support_upper(angle, height, cap, parameter, kind, slope):
    denominator = angle.cos()+height.cosh()
    assert denominator > 0
    u, v = clipped(angle.sin(), 0)/denominator, height.sinh()/denominator
    cx, cy = boundary_coordinates(cap, parameter, kind)
    x, y = clipped(u*cx+v*cy, 0), u*cy-v*cx
    candidates = []
    if x > 0:
        # The positive-real-part square root and logarithm give the
        # right-half-plane asinh branch, without calling acb.asinh.
        z = acb(x, y)
        value = (z+(1+z*z).sqrt()).log()
        estimate = value.real-slope*value.imag
        if estimate.is_finite():
            candidates.append(estimate.upper())
    norm_squared = square(x)+square(y)
    if norm_squared.upper() < 1:
        b = 1-norm_squared
        root_t = arb(2).sqrt()*x/((square(b)+4*square(x)).sqrt()+b).sqrt()
        k = root_t.asinh()
        g = increasing(y/(1+square(root_t)).sqrt(), -1, 1, "asin")
        estimate = k-slope*g
        if estimate.is_finite():
            candidates.append(estimate.upper())
    # Continuous boundary formula, including c=0 and either imaginary cut.
    d_plus = (square(x)+square(y+1)).nonnegative_part().sqrt()
    d_minus = (square(x)+square(y-1)).nonnegative_part().sqrt()
    k = increasing((d_plus+d_minus)/2, 1, None, "acosh")
    g = increasing((d_plus-d_minus)/2, -1, 1, "asin")
    estimate = k-slope*g
    if estimate.is_finite():
        candidates.append(estimate.upper())
    assert candidates, "No finite support enclosure"
    return min(candidates)


def replay_row(record, mode):
    xl, xh, hl, hh = map(F, record["box"])
    angle = angle_interval(record["box"])
    height = hull(rational(hl), rational(hh))
    slope_fraction = F(record["slope"])
    assert slope_fraction <= 0
    slope = rational(slope_fraction)
    budgets = [rational(F(b)) for b in record["support_budgets"]]
    assert len(budgets) == len(record["arcs"]) == 2
    # Evaluate the affine expression independently at interval corners,
    # including the cap breakpoint if necessary.
    heights = [hl, hh]
    if hl < F(111,100) < hh:
        heights.append(F(111,100))
    targets = []
    for h in heights:
        charge = 50*h/59 if mode == "scaled" else min(F(1), (h-F(37,200))*40/37)
        for a in (angle.lower(), angle.upper()):
            targets.append(3*rational(h)/2-slope*(3*a/2-arb.pi()*rational(charge)))
    target_lower = min(t.lower() for t in targets)
    margin = (target_lower-sum(budgets, arb(0))).lower()
    assert margin > 0, "Support budgets do not imply separation"
    expected = {"arc"} if mode == "scaled" else {"left", "top", "right"}
    count, refinements = 0, 0
    for cap, budget, arcs in zip((rational(F(23,20)), height), budgets, record["arcs"]):
        assert set(arcs) == expected
        for kind in sorted(expected):
            for low, high in verify_arc_partition(arcs[kind]):
                pending = [(low, high, 0)]
                while pending:
                    left, right, depth = pending.pop()
                    upper = support_upper(angle, height, cap,
                                          hull(rational(left), rational(right)),
                                          kind, slope)
                    if upper < budget.lower():
                        margin = min(margin, (budget.lower()-upper).lower())
                        count += 1
                        continue
                    assert depth < 24, ("Saved support bound failed", record["box"], kind)
                    middle = (left+right)/2
                    point_upper = support_upper(angle, height, cap, rational(middle), kind, slope)
                    assert point_upper < budget.lower(), (
                        "Saved support fails at a midpoint", record["box"], kind, str(middle))
                    refinements += 1
                    pending.extend(((left, middle, depth+1), (middle, right, depth+1)))
    return count, refinements, margin


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    here = Path(__file__).resolve()
    script_bytes = here.read_bytes()
    input_bytes = args.certificate.read_bytes()
    data = json.loads(input_bytes)
    assert data["status"] == "passed" and data["pending"] == []
    mode = data["mode"]
    assert mode in ("scaled", "affine")
    low = F(3,100) if mode == "scaled" else F(37,40)
    high = F(23,20)
    assert data["domain"] == {
        "sector_coordinate": ["0","1"], "height": [str(low),str(high)]}
    rows = data["certificate"]
    assert len(rows) == data["accepted_boxes"]
    root = here.parents[1]
    for filename, expected in data["sha256"].items():
        assert hashlib.sha256((root/filename).read_bytes()).hexdigest() == expected
    cover = verify_cover(rows, low, high)
    start = last = time.monotonic()
    leaves = refinements = 0
    minimum_margin = None
    for index, row in enumerate(rows, 1):
        count, refined, margin = replay_row(row, mode)
        leaves += count
        refinements += refined
        minimum_margin = margin if minimum_margin is None else min(minimum_margin, margin)
        now = time.monotonic()
        if now-last >= 30:
            print(json.dumps({"replayed_boxes": index, "total_boxes": len(rows),
                              "seconds": round(now-start, 1)}), flush=True)
            last = now
    result = {
        "status": "passed", "mode": mode, "precision_bits": ctx.prec,
        "certificate_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "script_sha256": hashlib.sha256(script_bytes).hexdigest(),
        "parameter_cover": cover, "replayed_boxes": len(rows),
        "verified_arc_leaves": leaves, "additional_arc_refinements": refinements,
        "minimum_margin": str(minimum_margin),
        "elapsed_seconds": time.monotonic()-start,
        "method": "Independent angle/branch formulas and exact rectangle/arc coverage",
    }
    output = args.output or args.certificate.with_name(
        args.certificate.stem+"-replay.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
