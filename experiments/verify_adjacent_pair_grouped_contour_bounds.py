#!/usr/bin/env python3
"""Certified ball enclosures for all remaining adjacent-pair contour faces.

Uses python-flint's Arb/Acb arithmetic. Every accepted box is bounded as
a whole; no sampled values or floating-point optimizer enter a decision.
The adaptive subdivision covers each input rectangle by exact rational
binary partitions. The output records exact coverage areas and a hash of
all accepted boxes; rerunning this script rechecks every box.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import flint
from flint import arb, acb, ctx


CUT = F(1, 100000)
EX_THRESHOLD = F(169, 200)
OTHER_THRESHOLD = F(3, 4)


def q(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def interval(left, right):
    return q(left).union(q(right))


def positive_part(value):
    return (value + abs(value)) / 2


def setup(precision):
    global PI, HX, HY, HA, DELTA
    ctx.prec = precision
    PI = arb.pi()
    HX = 3 * arb(2).log() / (4 * PI)
    HY = arb(7).log() / (4 * PI)
    HA = arb(2).log() / (4 * PI)
    DELTA = q(CUT)


def real_j(a, height):
    """Re J(a+i height), on the continued canonical branch.

    All calls either have 0<=a<=1 or have strictly positive height.
    For the former, Schwarz reflection permits replacement of height
    by its absolute value. The upper-half-plane dilogarithm formula
    also applies when a exceeds 1.
    """
    height = abs(height)
    z = acb(-2 * PI * height, 2 * PI * a).exp()
    return -z.polylog(2).imag / (2 * PI) - PI * height * (1 - 2 * a) / 2


def grouped_value(s, t, b, sign):
    real_phase = (
        real_j(b, s + t) + 3 * PI * abs(s) / 2
        - 6 * real_j(b, t) + real_j(2 * b, 2 * t)
        - PI * (s * (1 - b) + t * (b + q(F(1, 2))))
    )
    # The sign is fixed by the exact parameter domain. Testing the sign
    # of an outward-rounded ball containing zero would be incorrect.
    if sign < 0:
        exponent = 4 * PI * s + 2 * PI * positive_part(t)
    else:
        exponent = 2 * PI * positive_part(t - 2 * s)
    return real_phase + exponent


def upper_x_endpoint(a, t, b):
    return (
        real_j(a + b, HX + t) - 3 * real_j(a, HX)
        + (2 if b == 0 else 1) * PI * abs(t)
        - PI * ((2 * a - b + 1) * HX + (-a + b + q(F(1, 2))) * t)
        - 2 * PI * positive_part(-t)
    )


def upper_x_lower_y(a, b):
    t = -HY
    return (
        real_j(a + b, HX + t) - 3 * real_j(a, HX)
        - 6 * real_j(b, t) + real_j(2 * b, 2 * t)
        - PI * ((2 * a - b + 1) * HX + (-a + b + q(F(1, 2))) * t)
        - 2 * PI * HY
    )


def evaluate(name, box):
    a = interval(*box[0])
    u = interval(*box[1])
    if name.startswith("grouped"):
        sign = -1 if name.endswith("negative") else 1
        s = -u if sign < 0 else HX * u
        t = DELTA + ((HA if sign < 0 else HY) - DELTA) * u
        lower = "lower" in name
        if lower:
            t = -HY
        return grouped_value(s, t, a, sign) - (2 * PI * HY if lower else 0)
    if name == "upper_x_lower_y":
        return upper_x_lower_y(a, u / 2)
    return upper_x_endpoint(
        a, HY * (2 * u - 1),
        0 if name == "upper_x_bottom_endpoint" else q(F(1, 2)),
    )


def verify_rectangle(name, max_boxes):
    grouped = name.startswith("grouped")
    threshold = EX_THRESHOLD if grouped else OTHER_THRESHOLD
    first = (CUT, F(1, 2) - CUT) if grouped else (F(0), F(1))
    initial = (first, (F(0), F(1)))
    queue = [(initial, 0)]
    accepted = examined = maximum_depth = 0
    area = F(0)
    digest = hashlib.sha256()
    largest_upper = None
    while queue:
        box, depth = queue.pop()
        examined += 1
        if examined > max_boxes:
            raise RuntimeError(f"{name}: maximum box count exceeded")
        value = evaluate(name, box)
        # For a non-finite enclosure this comparison is false and the
        # box is subdivided. A non-finite special-function value is
        # never accepted.
        if value.is_finite() and value < q(threshold):
            accepted += 1
            maximum_depth = max(maximum_depth, depth)
            area += (box[0][1] - box[0][0]) * (box[1][1] - box[1][0])
            digest.update((repr(box) + "\n").encode())
            upper = value.upper()
            if largest_upper is None or upper > largest_upper:
                largest_upper = upper
            continue
        if depth >= 36:
            raise RuntimeError(f"{name}: unresolved box {box}, enclosure {value}")
        # Both original coordinate lengths are normalized to one here.
        width0 = (box[0][1] - box[0][0]) * (2 if grouped else 1)
        width1 = box[1][1] - box[1][0]
        axis = 0 if width0 >= width1 else 1
        left, right = box[axis]
        middle = (left + right) / 2
        first_child, second_child = list(box), list(box)
        first_child[axis] = (left, middle)
        second_child[axis] = (middle, right)
        queue.extend(((tuple(first_child), depth + 1), (tuple(second_child), depth + 1)))
    required_area = first[1] - first[0]
    if area != required_area:
        raise RuntimeError(f"{name}: rational coverage area failed")
    return {
        "name": name,
        "domain": [[str(x) for x in pair] for pair in initial],
        "strict_upper_bound": str(threshold),
        "examined_boxes": examined,
        "accepted_boxes": accepted,
        "maximum_depth": maximum_depth,
        "exact_covered_area": str(area),
        "largest_accepted_ball_upper": str(largest_upper),
        "accepted_partition_sha256": digest.hexdigest(),
    }


def run(precision, max_boxes):
    setup(precision)
    names = [
        "grouped_upper_negative", "grouped_upper_positive",
        "grouped_lower_negative", "grouped_lower_positive",
        "upper_x_bottom_endpoint", "upper_x_top_endpoint",
        "upper_x_lower_y",
    ]
    certificates = []
    for name in names:
        result = verify_rectangle(name, max_boxes)
        certificates.append(result)
        print(f"{name}: {result['accepted_boxes']} boxes, bound {result['strict_upper_bound']}", flush=True)
    return {
        "scope": "Grouped-side and upper-x contour phase bounds; exact lattice assembly and factorial estimates are separate inputs.",
        "arithmetic": "Arb/Acb complex-ball enclosures with exact rational binary domain partitions",
        "python_flint_version": flint.__version__,
        "precision_bits": precision,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "endpoint_strip_width": str(CUT),
        "profile_minimum_height": str(CUT),
        "endpoint_strip_rate_cost_upper": "193/100000",
        "certificates": certificates,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--max-boxes", type=int, default=200000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.precision, args.max_boxes)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        print(f"Saved {args.output}.")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
