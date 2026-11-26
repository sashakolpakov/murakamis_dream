#!/usr/bin/env python3
"""Outward bounds for 0 <= Re x <= 7/100 at the mixed geometric height.

The outer Newton wire remains real and finite. Only the original trace
angle is deformed, so the certificate has one horizontal rectangle and
two angular connector rectangles, with no wire-lattice corrections.
"""

import argparse
import hashlib
import json
import platform
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import acb, arb

import certify_internal_pair_three_mixed_packet as mixed

e = mixed.e
A, HEIGHT, ANGLE = Q(7, 100), Q(13, 20), Q(39, 20)
ALPHA, BETA = Q(1, 32), Q(15, 32)


def setup(precision):
    root = mixed.setup(precision)
    Y = e.polarized.imag
    x = acb(e.rat(A), Y)
    h, T = e.rat(HEIGHT), e.rat(ANGLE)
    assert (2*e.pi*e.rat(A)).cos() > arb(9)/10
    assert (2*e.pi*e.rat(A)).sin() < arb(9)/20
    assert (2*e.pi*Y).cosh() > arb(8)/7
    assert (2*e.pi*Y).sinh() < arb(5)/8
    assert T.cos() > -arb(2)/5
    assert h.cosh() < arb(5)/4
    assert arb(1)/2-e.rat(A)-T/(2*e.pi) > 0
    quadratic_minimum = Q(41, 175)-Q(9, 16)**2/(4*Q(103, 175))
    assert quadratic_minimum == Q(1843727, 18457600) > 0

    def fixed_b(t):
        return (-e.Ju(e.half-x+t/(2*e.pi))
                -e.Ju(e.half-x-t/(2*e.pi))-2*e.Ju(x))

    def phase(y, t, side):
        return mixed.BASE_PHASE(y, t, side)+fixed_b(t)

    def gradient(y, t, side):
        gy, gt = mixed.BASE_GRADIENT(y, t, side)
        gt += (-e.jp(e.half-x+t/(2*e.pi), 1)
               +e.jp(e.half-x-t/(2*e.pi), 1))/(2*e.pi)
        return gy, gt

    def hessian(y, t):
        yy, yt, tt = mixed.BASE_HESSIAN(y, t)
        tt -= ((e.pi*x+t/2).tan()+(e.pi*x-t/2).tan())/(4*e.pi)
        return yy, yt, tt

    def mapping(p, q, kind, endpoint=None):
        if kind == "bottom":
            y, t = acb(p), acb(q, -h)
            directions = ((acb(1), acb(0)), (acb(0), acb(1)))
        elif kind in ("positive_connector", "negative_connector"):
            sign = 1 if kind == "positive_connector" else -1
            y, t = acb(p), acb(sign*T, -q)
            directions = ((acb(1), acb(0)), (acb(0), -e.I))
        else:
            raise ValueError(kind)
        return y, t, directions, 1, arb(0), (arb(0), arb(0))

    e.phase, e.gradient, e.hessian = phase, gradient, hessian
    e.mapping, e.boundbox = mapping, mixed.BASE_BOUND_AFFINE
    # M remains the actual geometric mixed action, not the new phase at a
    # guessed critical point.
    g_alpha = (e.Js(2*e.rat(ALPHA), 1)-4*e.Js(e.rat(ALPHA), 1)).real
    wire_tail = fixed_b(acb(0)).real+2*g_alpha
    yT = (T/2).cos().atan()/e.pi
    outer_edge = mixed.BASE_PHASE(yT, T, 1)-3*e.I*T*T/(4*e.pi)+e.I*T
    angular_tail = fixed_b(T).real+outer_edge.real
    assert e.M-wire_tail > arb(1)/100
    assert e.M-angular_tail > arb(1)/100
    return {
        "geometric_root": root,
        "fixed_internal_height": str(Y),
        "right_endpoint": str(x),
        "trace_height": str(HEIGHT),
        "angle_cutoff": str(ANGLE),
        "monotonicity_quadratic_minimum": str(quadratic_minimum),
        "wire_tail_rate": str(wire_tail),
        "angular_tail_rate": str(angular_tail),
        "physical_tail_gap": "1/100",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument(
        "--output", type=Path,
        default=Path("repro/results/research-internal-pair-three-low-wire-complement.json"),
    )
    args = parser.parse_args()
    if args.precision < 140:
        parser.error("At least 140 bits are required.")
    inputs = setup(args.precision)
    plan = [
        ("bottom", (ALPHA, BETA, -ANGLE, ANGLE)),
        ("positive_connector", (ALPHA, BETA, Q(0), HEIGHT)),
        ("negative_connector", (ALPHA, BETA, Q(0), HEIGHT)),
    ]
    cases = []
    document = {
        "status": "incomplete",
        "scope": "Outward phase bounds with the exact finite outer wire retained; finite-source passage is written separately.",
        "precision_bits": args.precision,
        "python_version": platform.python_version(),
        "python_flint_version": flint.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "mixed_root_script_sha256": hashlib.sha256(Path(mixed.__file__).read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest(),
        "inputs": inputs,
        "surfaces": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for kind, box in plan:
        result = e.certify(kind, box, Q(1, 100))
        cases.append(result)
        args.output.write_text(json.dumps(document, indent=2)+"\n")
        print(f"{kind}: {result['counts']['visited']} boxes", flush=True)
    document["status"] = "certified"
    args.output.write_text(json.dumps(document, indent=2)+"\n")
    print("Certified all three rectangles and both physical tail gaps.", flush=True)


if __name__ == "__main__":
    main()
