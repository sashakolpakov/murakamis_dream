#!/usr/bin/env python3
"""Exact interval exclusion of magnitude-three corners next to four or five.

The domain is the entire compact angle rectangle implied by Lemma 12
and the original angle bounds. Every leaf of the rational bisection
violates a necessary KKT inequality. No approximate optimizer is used.
"""

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import verify_conway_two_leaf_block_alias_certificate as arith
import check_negative_three_corner_necessary_conditions as elementary

I, PI, SCALE = arith.I, arith.PI, arith.S
sqrt_interval = elementary.sqrt_interval
sine, cosine = elementary.sine, elementary.cosine


def asinh_interval(value):
    # Evaluating monotone endpoint values avoids a needlessly wide
    # logarithm interval before the first bisection.
    lo = elementary.asinh_interval(I(value.lo, value.lo, raw=True))
    hi = elementary.asinh_interval(I(value.hi, value.hi, raw=True))
    return I(lo.lo, hi.hi, raw=True)


def tangent(interval):
    assert 0 < interval[0] < interval[1] < F(1, 2)
    return sine(interval) / cosine(interval)


def tangent_upper(point):
    assert 0 < point < F(1, 2)
    return (arith.sinpi(point) / arith.sinpi(F(1, 2)-point)).hi


def exclude(n, x, y, C):
    # x and y are the angles divided by pi.
    if y[0] >= 4*x[1]/3:
        return "lemma_12", y[0]-4*x[1]/3
    lam_hi = x[1]+n*y[1]-(n-3)
    if lam_hi <= 0:
        return "positive_lambda", -lam_hi
    sx, cx, sy, cy = sine(x), cosine(x), sine(y), cosine(y)
    X = asinh_interval(cx*sy/sx)/2
    H = asinh_interval(cy*sx/sy)/2
    real_gap = C-n*X+H
    if real_gap.lo > 0:
        return "positive_endpoint_real", F(real_gap.lo, SCALE)
    R = sqrt_interval(1-cx*cx*cy*cy)/(cx*(1+cy))
    arg = ((3*x[0]-y[1])/2, (3*x[1]-y[0])/2)
    outgoing_gap = R-tangent(arg)
    if outgoing_gap.lo >= 0:
        return "negative_endpoint_outgoing", F(outgoing_gap.lo, SCALE)
    if lam_hi < 1:
        # If lambda<=0, the angle inequality has already failed.
        # On the remaining portion, tan(lambda/2) is positive and
        # increasing, so its upper endpoint gives a valid upper bound.
        rhs_hi = sy.hi*tangent_upper(lam_hi/2)
        outgoing_gap_lo = F(2*H.lo, n*SCALE)-F(rhs_hi, SCALE*SCALE)
        if outgoing_gap_lo >= 0:
            return "positive_endpoint_outgoing", outgoing_gap_lo
    return None


def verify_case(n):
    x = (F(3*(n-3), 4*n+3), F(1, 3))
    y = (F(n-3, n)-F(1, 3*n), F(4, 9))
    C = (n*asinh_interval(I(F(1, n)))+asinh_interval(I(n)))/2
    stack = [(x, y, 0)]
    leaves, reasons = [], Counter()
    nodes = max_depth = 0
    while stack:
        x, y, depth = stack.pop()
        nodes += 1
        assert nodes < 200000, "Node budget exceeded; no exclusion established."
        result = exclude(n, x, y, C)
        if result is not None:
            reason, margin = result
            reasons[reason] += 1
            leaves.append({
                "x_over_pi": list(map(str, x)),
                "y_over_pi": list(map(str, y)),
                "reason": reason,
                "rational_margin": str(margin),
            })
            max_depth = max(max_depth, depth)
            continue
        assert depth < 30, ("Unresolved box", n, x, y)
        if x[1]-x[0] >= y[1]-y[0]:
            mid = sum(x)/2
            stack.extend([((x[0], mid), y, depth+1),
                          ((mid, x[1]), y, depth+1)])
        else:
            mid = sum(y)/2
            stack.extend([(x, (y[0], mid), depth+1),
                          (x, (mid, y[1]), depth+1)])
    assert nodes == 2*len(leaves)-1
    return {"n": n, "nodes": nodes, "leaves": len(leaves),
            "maximum_depth": max_depth, "reasons": dict(reasons),
            "certificate": leaves}


def verify():
    cases = [verify_case(n) for n in (4, 5)]
    paths = [Path(__file__), Path(arith.__file__), Path(elementary.__file__)]
    return {
        "claim": "No magnitude-three corner can have positive endpoint four or five.",
        "method": "Complete rational bisection; every terminal box violates a necessary inequality.",
        "cases": cases,
        "sha256": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                   for path in paths},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    concise = dict(result)
    concise["cases"] = [{k: v for k, v in case.items() if k != "certificate"}
                        for case in result["cases"]]
    print(json.dumps(concise, indent=2))
