#!/usr/bin/env python3
"""Outward 3-real-variable covers for the central mixed-wire period.

The angular connector is split where the polarized factorial changes
dominant continuation. Every logical trace-first surface is retained.
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
import certify_internal_pair_three_mixed_packet as m

e = m.e
LEFT, RIGHT = Q(7, 100), Q(3, 10)
LOCAL = (Q(183, 1000), Q(191, 1000),
         Q(225, 1000), Q(233, 1000), Q(235, 1000), Q(243, 1000))


def setup(precision):
    root = m.setup(precision)
    Y, hy, ht, T = e.polarized.imag, e.hx, e.ht, e.rat(m.ANGLE)
    switch = 2*e.pi*Y/ht
    assert 0 < switch < 1
    x_max = acb(arb(1)/4, Y)
    b_max = (-2*e.Ju(e.half-x_max)-2*e.Ju(x_max)).real
    ga = (e.Js(2*e.rat(m.ALPHA), 1)-4*e.Js(e.rat(m.ALPHA), 1)).real
    assert e.M-b_max-2*ga > arb(1)/5
    yT = (T/2).cos().atan()/e.pi
    assert e.rat(m.ALPHA) < yT < e.rat(m.BETA)
    root["central_period_wire_tail_rate"] = str(b_max+2*ga)
    root["central_period_wire_tail_gap"] = "1/5"
    root["real_outer_angle_wire_maximizer"] = str(yT)

    def phase(x, y, t, side_y, side_m):
        return (m.BASE_PHASE(y, t, side_y)
                - e.Js(e.half-x+t/(2*e.pi), -1)
                - e.Js(e.half-x-t/(2*e.pi), side_m)-2*e.Js(x, 1))

    def gradient(x, y, t, side_y, side_m):
        gy, gt = m.BASE_GRADIENT(y, t, side_y)
        lp = e.jp(e.half-x+t/(2*e.pi), -1)
        lm = e.jp(e.half-x-t/(2*e.pi), side_m)
        return lp+lm-2*e.jp(x, 1), gy, gt+(-lp+lm)/(2*e.pi)

    def hessian(x, y, t):
        yy, yt, tt = m.BASE_HESSIAN(y, t)
        den = (2*e.pi*x).cos()+t.cos()
        xx = -2*e.pi*(2*e.pi*x).sin()/den-2*e.pi/(e.pi*x).tan()
        xt = -t.sin()/den
        tt -= ((e.pi*x+t/2).tan()+(e.pi*x-t/2).tan())/(4*e.pi)
        z = acb(0)
        return ((xx, z, xt), (z, yy, yt), (xt, yt, tt))

    def mapping(a, p, q, kind, endpoint=None, part=None):
        x = acb(a, Y)
        z = acb(0)
        d0 = (acb(1), z, z)
        second = {}
        if kind in ("central", "negative", "lower"):
            sy = -1 if kind == "lower" else 1
            y, t = acb(p, sy*hy), acb(2*e.pi*q, -ht)
            dirs = (d0, (z, acb(1), z), (z, z, 2*e.pi))
            pen = 2*e.pi*hy if sy < 0 else arb(0)
            pd = (arb(0), arb(0), arb(0))
            sm = 1
        elif kind.startswith("bottom_endpoint_"):
            sy = 1 if kind.endswith("upper") else -1
            y, t = acb(e.rat(endpoint), sy*hy*q), acb(2*e.pi*p, -ht)
            dirs = (d0, (z, z, 2*e.pi), (z, sy*e.I*hy, z))
            coeff = 2*e.pi*hy if sy < 0 else arb(0)
            pen, pd, sm = coeff*q, (arb(0), arb(0), coeff), 1
        else:
            assert part in (0, 1)
            base, length = (arb(0), switch) if part == 0 else (switch, 1-switch)
            sm = -1 if part == 0 else 1
            sign = 1 if kind.endswith("positive") else -1
            if kind.startswith("outer_"):
                sy = -1 if kind.startswith("outer_lower_") else 1
                depth = base+length*q
                y, t = acb(p, sy*hy*depth), acb(sign*T, -ht*depth)
                dirs = (d0, (z, acb(1), z),
                        (z, sy*e.I*hy*length, -e.I*ht*length))
                coeff = 2*e.pi*hy if sy < 0 else arb(0)
                pen, pd = coeff*depth, (arb(0), arb(0), coeff*length)
            elif kind.startswith("nested_"):
                sy = 1 if "_upper_" in kind else -1
                depth = base+length*p
                y, t = acb(e.rat(endpoint), sy*hy*depth*q), acb(sign*T, -ht*depth)
                dirs = (d0, (z, sy*e.I*hy*length*q, -e.I*ht*length),
                        (z, sy*e.I*hy*depth, z))
                coeff = 2*e.pi*hy if sy < 0 else arb(0)
                pen = coeff*depth*q
                pd = (arb(0), coeff*length*q, coeff*depth)
                second[(1, 2)] = (sy*e.I*hy*length, coeff*length)
            else:
                raise ValueError(kind)
        return (x, y, t), dirs, sy, sm, pen, pd, second

    def local_certificate():
        worst = None
        grid = (4, 8, 8)
        for ix in range(grid[0]):
            for iy in range(grid[1]):
                for it in range(grid[2]):
                    vals = []
                    for j, i in enumerate((ix, iy, it)):
                        lo, hi = LOCAL[2*j:2*j+2]
                        vals.append(e.ball(lo+(hi-lo)*i/grid[j],
                                           lo+(hi-lo)*(i+1)/grid[j]))
                    x, y, t = acb(vals[0], Y), acb(vals[1], hy), acb(2*e.pi*vals[2], -ht)
                    H = hessian(x, y, t)
                    A, B, C = -H[0][0].real, -H[1][1].real, -H[2][2].real
                    U, V = -H[0][2].real, -H[1][2].real
                    determinant = A*B*C-A*V*V-B*U*U
                    assert A > 0 and B > 0 and determinant > 0
                    if worst is None or determinant.lower() < worst:
                        worst = determinant.lower()
        assert e.rat(LOCAL[0]) < e.polarized.real < e.rat(LOCAL[1])
        assert e.rat(LOCAL[2]) < e.xs.real < e.rat(LOCAL[3])
        assert e.rat(LOCAL[4]) < e.ts.real/(2*e.pi) < e.rat(LOCAL[5])
        return {"rectangle": [str(x) for x in LOCAL], "subboxes": 256,
                "negative_real_Hessian_determinant_lower": str(worst)}

    def bound(box, kind, endpoint, part, target):
        balls = [e.ball(box[2*j], box[2*j+1]) for j in range(3)]
        args, dirs, sy, sm, pen, pd, second = mapping(*balls, kind, endpoint, part)
        direct = phase(*args, sy, sm).real-pen
        if direct < target:
            return direct, "direct"
        centers = [e.rat((box[2*j]+box[2*j+1])/2) for j in range(3)]
        radii = [e.rat((box[2*j+1]-box[2*j])/2) for j in range(3)]
        ca, cd, csy, csm, cp, cpd, _ = mapping(*centers, kind, endpoint, part)
        f = phase(*ca, csy, csm).real-cp
        if f > target:
            raise RuntimeError(f"center violates requested gap: {kind}, {endpoint}, {part}, {box}, {f}")
        g = gradient(*ca, csy, csm)
        value = f
        for j in range(3):
            gj = sum(g[k]*cd[j][k] for k in range(3)).real-cpd[j]
            value += abs(gj)*radii[j]
        H = hessian(*args)
        grad_ball = gradient(*args, sy, sm) if second else None
        for j in range(3):
            for k in range(j, 3):
                z = sum(H[r][s]*dirs[j][r]*dirs[k][s]
                        for r in range(3) for s in range(3)).real
                if (j, k) in second:
                    ddy, dpen = second[(j, k)]
                    z += (grad_ball[1]*ddy).real-dpen
                value += abs(z)*radii[j]*radii[k]*(arb(1)/2 if j == k else 1)
        return value, "Taylor"

    return root, switch, local_certificate, bound


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument("--output", type=Path,
                        default=Path("repro/results/research-internal-pair-three-central-period.json"))
    parser.add_argument("--only", type=str)
    args = parser.parse_args()
    if args.precision < 140:
        parser.error("At least 140 bits are required.")
    root, switch, local, bound = setup(args.precision)
    document = {
        "status": "incomplete", "scope": "Central period phase bounds; finite-source assembly separate.",
        "precision_bits": args.precision, "python": platform.python_version(),
        "python_flint": flint.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies": {Path(p).name: hashlib.sha256(Path(p).read_bytes()).hexdigest()
                         for p in (m.__file__, e.__file__)},
        "internal_interval": [str(LEFT), str(RIGHT)], "root": root,
        "connector_split": str(switch), "local_Hessian": local(), "covers": [],
        "expected_logical_surfaces": 19, "expected_cover_domains": 31,
    }
    stop = Q(311, 1000)
    plan = [
        ("central", (m.ALPHA, m.BETA, Q(0), stop), Q(1, 10_000_000), None),
        ("negative", (m.ALPHA, m.BETA, -stop, Q(0)), Q(1, 1000), None),
        ("lower", (m.ALPHA, m.BETA, -stop, stop), Q(1, 1000), None),
    ]
    for sign in ("positive", "negative"):
        for prefix in ("outer_", "outer_lower_"):
            plan.append((prefix+sign, (m.ALPHA, m.BETA, Q(0), Q(1)), Q(1, 1000), None))
    for endpoint in (m.ALPHA, m.BETA):
        for side in ("upper", "lower"):
            plan.append(("bottom_endpoint_"+side, (-stop, stop, Q(0), Q(1)),
                         Q(1, 1000), endpoint))
            for sign in ("positive", "negative"):
                plan.append(("nested_"+side+"_"+sign, (Q(0), Q(1), Q(0), Q(1)),
                             Q(1, 1000), endpoint))
    assert len(plan) == 19
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for kind, box2, gap, endpoint in plan:
        if args.only and kind != args.only:
            continue
        parts = (0, 1) if kind.startswith(("outer_", "nested_")) else (None,)
        for part in parts:
            initial = (LEFT, RIGHT)+box2
            todo, leaves, counts = [initial], [], Counter()
            target = e.M-e.rat(gap)
            try:
                while todo:
                    box = todo.pop()
                    counts["visited"] += 1
                    if kind == "central" and all(
                        box[2*j] >= LOCAL[2*j] and box[2*j+1] <= LOCAL[2*j+1]
                        for j in range(3)):
                        leaves.append({"box": [str(z) for z in box], "method": "local Hessian"})
                        counts["local"] += 1
                        continue
                    upper, method = bound(box, kind, endpoint, part, target)
                    if upper < target:
                        leaves.append({"box": [str(z) for z in box],
                                       "method": method, "upper": str(upper.upper())})
                        counts[method] += 1
                        continue
                    if counts["visited"] > 200000:
                        raise RuntimeError("Subdivision budget exhausted.")
                    widths = [box[2*j+1]-box[2*j] for j in range(3)]
                    # Normalize height fractions to the wire/angle scales.
                    scales = [Q(1), Q(1), Q(1)]
                    if kind.startswith(("outer_", "nested_")):
                        scales[2] = Q(1, 3)
                    if kind.startswith("bottom_endpoint_"):
                        scales[2] = Q(1, 2)
                    j = max(range(3), key=lambda j: widths[j]*scales[j])
                    mid = (box[2*j]+box[2*j+1])/2
                    left, right = list(box), list(box)
                    left[2*j+1], right[2*j] = mid, mid
                    todo.extend((tuple(left), tuple(right)))
            except Exception as err:
                document["status"] = "failed"
                document["failure"] = {"surface": kind, "endpoint": str(endpoint),
                                       "part": part, "error": str(err), "counts": dict(counts)}
                args.output.write_text(json.dumps(document, indent=2)+"\n")
                raise
            assert counts["visited"] == 2*len(leaves)-1
            document["covers"].append({
                "surface": kind, "endpoint": str(endpoint), "part": part,
                "initial": [str(z) for z in initial], "gap": str(gap),
                "counts": dict(counts), "leaves": leaves})
            args.output.write_text(json.dumps(document, indent=2)+"\n")
            print(f"{kind} endpoint={endpoint} part={part}: {counts['visited']} boxes", flush=True)
    document["status"] = "certified" if len(document["covers"]) == 31 else "partial"
    args.output.write_text(json.dumps(document, indent=2)+"\n")
    print(f"{document['status']}: {len(document['covers'])} domains", flush=True)


if __name__ == "__main__":
    main()
