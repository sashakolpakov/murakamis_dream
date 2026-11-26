#!/usr/bin/env python3
"""Outward upper bounds on the right part of the internal Fourier circle.

The outer Newton index remains a real finite sum. Only the original
trace is moved. This certifies limiting phase inequalities; the finite
source interpretation is proved separately.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

from flint import acb, arb
import certify_internal_pair_three_mixed_packet as mixed

e = mixed.e
LEFT, RIGHT = Q(3, 10), Q(1, 2)
HEIGHT, STOP = Q(4, 5), Q(311, 1000)


def fixed_real(x, t):
    """Real factorial phase, including either side of a negative cut."""
    def real_j(z, side):
        if z.real > 0:
            return e.Ju(z).real
        if z.real < 0:
            return -e.Ju(-z).real-e.pi*abs(z.imag)
        return e.Js(z, side).real
    plus = e.half-x+t/(2*e.pi)
    minus = e.half-x-t/(2*e.pi)
    return -real_j(plus, -1)-real_j(minus, 1)-2*e.Ju(x).real


def certify(kind, initial, target, fixed_a=None):
    todo, accepted, visited = [initial], [], 0
    while todo:
        box = todo.pop()
        visited += 1
        if visited > 200000:
            raise RuntimeError("Subdivision limit reached; no certificate.")
        intervals = [e.ball(a, b) for a, b in box]
        if fixed_a is None:
            a, y, parameter = intervals
        else:
            a, (y, parameter) = e.rat(fixed_a), intervals
        x = acb(a, e.polarized.imag)
        if kind.endswith("horizontal"):
            t = acb(2*e.pi*parameter, -e.rat(HEIGHT))
        else:
            sign = 1 if kind.startswith("positive") else -1
            t = acb(sign*e.rat(mixed.ANGLE), -e.rat(HEIGHT)*parameter)
        bound = mixed.BASE_PHASE(acb(y), t, 1).real+fixed_real(x, t)
        if bound.is_finite() and bound < target:
            accepted.append({
                "box": [[str(a), str(b)] for a, b in box],
                "upper_bound": str(bound.upper()),
            })
            continue
        # Normalize each coordinate by the width of its original interval.
        coordinate = max(
            range(len(box)),
            key=lambda k: (box[k][1]-box[k][0])/(initial[k][1]-initial[k][0]),
        )
        a, b = box[coordinate]
        middle = (a+b)/2
        for interval in ((a, middle), (middle, b)):
            child = list(box)
            child[coordinate] = interval
            todo.append(tuple(child))
    return {
        "surface": kind, "fixed_real_wire": str(fixed_a),
        "initial_box": [[str(a), str(b)] for a, b in initial],
        "visited": visited, "cover": accepted,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument("--only")
    parser.add_argument("--output", type=Path,
                        default=Path("repro/results/research-internal-pair-three-right-period.json"))
    args = parser.parse_args()
    root = mixed.setup(args.precision)
    target = e.M-arb(1)/1000
    assert e.rat(STOP)*2*e.pi > e.rat(mixed.ANGLE)
    # These are the hypotheses used in the written monotonicity proof
    # for nonnegative real trace angles on a in [3/10,1/2].
    assert e.rat(HEIGHT).sinh()**2 < arb(21)/25
    assert e.rat(HEIGHT).cosh() < arb(7)/5
    assert (2*e.pi*e.rat(STOP)).cos() > -arb(2)/5
    xleft = acb(e.rat(LEFT), e.polarized.imag)
    g_alpha = (e.Js(2*e.rat(mixed.ALPHA), 1)
               -4*e.Js(e.rat(mixed.ALPHA), 1)).real
    wire_tail = fixed_real(xleft, acb(0))+2*g_alpha
    T = e.rat(mixed.ANGLE)
    yT = (T/2).cos().atan()/e.pi
    edge_T = (mixed.BASE_PHASE(yT, T, 1)
              -3*e.I*T*T/(4*e.pi)+e.I*T).real
    angular_tail = fixed_real(xleft, T)+edge_T
    assert wire_tail < target and angular_tail < target
    wire = (mixed.ALPHA, mixed.BETA)
    interval = (LEFT, RIGHT)
    plan = [
        ("positive_horizontal", (wire, (Q(0), STOP)), LEFT),
        ("negative_horizontal", (interval, wire, (-STOP, Q(0))), None),
        ("positive_connector", (wire, (Q(0), Q(1))), LEFT),
        ("negative_connector", (interval, wire, (Q(0), Q(1))), None),
    ]
    doc = {
        "status": "incomplete", "precision_bits": args.precision,
        "scope": "Limiting trace-only phase upper bounds, not finite-source assembly.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "mixed_root_script_sha256": hashlib.sha256(Path(mixed.__file__).read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest(),
        "root": root, "trace_height": str(HEIGHT), "gap": "1/1000",
        "original_wire_tail_rate": str(wire_tail),
        "original_angular_tail_rate": str(angular_tail),
        "real_wire_interval": [str(LEFT), str(RIGHT)], "surfaces": [],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for kind, box, face in plan:
        if args.only and args.only != kind:
            continue
        result = certify(kind, box, target, face)
        doc["surfaces"].append(result)
        args.output.write_text(json.dumps(doc, indent=2)+"\n")
        print(kind, result["visited"], flush=True)
    doc["status"] = "certified" if len(doc["surfaces"]) == 4 else "partial"
    args.output.write_text(json.dumps(doc, indent=2)+"\n")
    print(doc["status"], flush=True)


if __name__ == "__main__":
    main()
