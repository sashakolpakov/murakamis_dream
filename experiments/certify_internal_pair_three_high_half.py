#!/usr/bin/env python3
"""Outward phase bounds for the high half of the original mixed wire.

The outer Newton index remains real. An exact endpoint-maximum argument
reduces the fixed-wire real interval [1/2,1] to its two ends. This script
certifies those six resulting trace surfaces and the original real tails.
Finite-source contour identities and factorial bounds are written separately.
"""

import argparse
import hashlib
import json
import platform
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import acb, arb, ctx

import certify_internal_pair_three_mixed_packet as mixed

e = mixed.e
HEIGHT = Q(7, 20)
TARGET = Q(5, 4)
ANGLE = Q(39, 20)
STOP = Q(311, 1000)
ALPHA, BETA = Q(1, 32), Q(15, 32)


def fixed_b(x, t):
    return (-e.Js(e.half-x+t/(2*e.pi), -1)
            -e.Js(e.half-x-t/(2*e.pi), -1)-2*e.Ju(x))


def phase(y, t, x):
    return mixed.BASE_PHASE(y, t, 1)+fixed_b(x, t)


def gradient(y, t, x):
    gy, gt = mixed.BASE_GRADIENT(y, t, 1)
    gt += (-e.jp(e.half-x+t/(2*e.pi), -1)
           +e.jp(e.half-x-t/(2*e.pi), -1))/(2*e.pi)
    return gy, gt


def hessian(y, t, x):
    yy, yt, tt = mixed.BASE_HESSIAN(y, t)
    tt -= ((e.pi*x+t/2).tan()+(e.pi*x-t/2).tan())/(4*e.pi)
    return yy, yt, tt


def mapping(p, q, kind):
    if kind == "bottom":
        return acb(p), acb(2*e.pi*q, -e.rat(HEIGHT)), 2*e.pi
    sign = 1 if kind == "right" else -1
    return acb(p), acb(sign*e.rat(ANGLE), -q), -e.I


def bound(box, kind, x):
    a, b, c, d = box
    ybox, tbox, tq = mapping(e.ball(a, b), e.ball(c, d), kind)
    direct = phase(ybox, tbox, x).real
    if direct < e.rat(TARGET):
        return direct, "direct"
    y, t, _ = mapping(e.rat((a+b)/2), e.rat((c+d)/2), kind)
    py, pq = e.rat((b-a)/2), e.rat((d-c)/2)
    gy, gt = gradient(y, t, x)
    yy, yt, tt = hessian(ybox, tbox, x)
    upper = (phase(y, t, x).real+abs(gy.real)*py
             +abs((gt*tq).real)*pq
             +(abs(yy.real)*py*py
               +2*abs((yt*tq).real)*py*pq
               +abs((tt*tq*tq).real)*pq*pq)/2)
    if upper.is_finite() and (not direct.is_finite() or upper < direct):
        return upper, "Taylor"
    return direct, "direct"


def certify(kind, fixed_real, height, maximum_boxes):
    x = acb(e.rat(fixed_real), height)
    initial = ((ALPHA, BETA, -STOP, STOP) if kind == "bottom"
               else (ALPHA, BETA, Q(0), HEIGHT))
    todo = [initial]
    counts, cover = Counter(), []
    largest = None
    while todo:
        box = todo.pop()
        counts["visited"] += 1
        upper, method = bound(box, kind, x)
        if upper < e.rat(TARGET):
            counts[method] += 1
            value = upper.upper()
            largest = value if largest is None else max(largest, value)
            cover.append({"box": [str(v) for v in box],
                          "method": method, "upper_bound": str(value)})
            continue
        if counts["visited"] > maximum_boxes:
            raise RuntimeError(f"Unproved {kind}, fixed real {fixed_real}: "
                               f"subdivision budget exhausted at {box}")
        a, b, c, d = box
        # Trace coordinate is normalized by 2 pi on the bottom.
        scale = Q(1) if kind == "bottom" else Q(1, 3)
        if b-a >= scale*(d-c):
            middle = (a+b)/2
            todo.extend([(a, middle, c, d), (middle, b, c, d)])
        else:
            middle = (c+d)/2
            todo.extend([(a, b, c, middle), (a, b, middle, d)])
    return {"surface": kind, "fixed_wire_real": str(fixed_real),
            "initial_box": [str(v) for v in initial],
            "strict_upper_target": str(TARGET),
            "counts": dict(counts), "largest_upper_bound": str(largest),
            "cover": cover}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument("--maximum-boxes", type=int, default=50000)
    parser.add_argument("--output", type=Path,
                        default=Path("repro/results/research-internal-pair-three-high-half.json"))
    args = parser.parse_args()
    if args.precision < 140:
        parser.error("At least 140 bits are required.")
    root = mixed.setup(args.precision)
    Y = e.polarized.imag
    assert 0 < e.rat(HEIGHT) < 2*e.pi*Y
    assert e.rat(STOP)*2*e.pi > e.rat(ANGLE)
    assert e.rat(STOP)*2*e.pi < arb(49)/25
    assert e.M > e.rat(TARGET)+arb(1)/100

    # Exact elementary hypotheses of the endpoint-maximum argument.
    cap = Q(49, 25)
    p6 = 1-cap**2/2+cap**4/24-cap**6/720
    assert p6 > -Q(2, 5)
    assert 1/(1-HEIGHT**2/2) < Q(8, 7)
    assert 2*(1-Q(2, 5)*Q(8, 7)) > 1
    assert (Q(8, 7)**2-1) < 1

    g_alpha = (e.Js(2*e.rat(ALPHA), 1)-4*e.Js(e.rat(ALPHA), 1)).real
    wire_tail = e.pi*Y+2*g_alpha
    T = e.rat(ANGLE)
    yT = (T/2).cos().atan()/e.pi
    edge_T = (mixed.BASE_PHASE(yT, T, 1)
              -3*e.I*T*T/(4*e.pi)+e.I*T).real
    angular_tail = e.pi*Y+edge_T
    assert wire_tail < e.rat(TARGET)
    assert angular_tail < e.rat(TARGET)

    results = []
    document = {
        "status": "incomplete",
        "scope": "Six limiting phase surfaces plus the original real tails; finite-source proof separate.",
        "precision_bits": ctx.prec,
        "python_version": platform.python_version(),
        "python_flint_version": flint.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "root_script_sha256": hashlib.sha256(Path(mixed.__file__).read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest(),
        "root": root, "fixed_wire_height": str(Y),
        "trace_height": str(HEIGHT), "angle_cutoff": str(ANGLE),
        "strict_upper_target": str(TARGET),
        "wire_tail_upper": str(wire_tail.upper()),
        "angular_tail_upper": str(angular_tail.upper()),
        "expected_surface_count": 6, "surfaces": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2)+"\n")
    for fixed_real in (Q(1, 2), Q(1)):
        for kind in ("bottom", "right", "left"):
            result = certify(kind, fixed_real, Y, args.maximum_boxes)
            results.append(result)
            args.output.write_text(json.dumps(document, indent=2)+"\n")
            print(f"{fixed_real} {kind}: {result['counts']['visited']} boxes", flush=True)
    document["status"] = "certified"
    args.output.write_text(json.dumps(document, indent=2)+"\n")
    print("certified: six high-half trace surfaces and both original tails", flush=True)


if __name__ == "__main__":
    main()
