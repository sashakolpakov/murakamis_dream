#!/usr/bin/env python3
"""Outward root rectangles and action reserves after outer alias shifts.

Only the conditional critical actions and local factorial density are
controlled here. Full shifted conditional sums remain a separate question.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-reoptimized-alias-action.json")
    args = parser.parse_args()
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)

    def ar(value):
        value = Q(value)
        return arb(value.numerator) / value.denominator

    def interval(a, b):
        return ar(a).union(ar(b))

    def gp(z):
        return (1 - (-2 * pi * ii * z).exp()).log()

    boxes = {
        3: tuple(map(Q, ("267/1000", "433/1000", "-65/1000", "68/1000"))),
        4: tuple(map(Q, ("27/100", "33/100", "-57/1000", "141/10000"))),
    }
    edge_count, slab_count = 32, 128
    edges = {}
    for kind, (left, right, bottom, top) in boxes.items():
        rows = []
        for j in range(edge_count):
            xl = left + (right - left) * Q(j, edge_count)
            xr = left + (right - left) * Q(j + 1, edge_count)
            yl = bottom + (top - bottom) * Q(j, edge_count)
            yr = bottom + (top - bottom) * Q(j + 1, edge_count)
            rows.extend((acb(interval(xl, xr), ar(bottom)),
                         acb(interval(xl, xr), ar(top)),
                         acb(ar(left), interval(yl, yr)),
                         acb(ar(right), interval(yl, yr))))
        edges[kind] = rows

    root_faces = []
    for epsilon, left_type, right_type in ((0, 4, 3), (1, 3, 4), (1, 4, 4)):
        for face in range(4):
            margins = []
            for j in range(slab_count):
                real = interval(Q(3, 20) + Q(17, 50) * Q(j, slab_count),
                                Q(3, 20) + Q(17, 50) * Q(j + 1, slab_count))
                imag = interval(-Q(3, 25) + Q(6, 25) * Q(j, slab_count),
                                -Q(3, 25) + Q(6, 25) * Q(j + 1, slab_count))
                s = (acb(ar("3/20"), imag), acb(ar("49/100"), imag),
                     acb(real, -ar("3/25")), acb(real, ar("3/25")))[face]
                component = (lambda z: z.real) if face < 2 else (lambda z: z.imag)
                left = [component(gp(s + a) + 2 * pi * ii * a)
                        for a in edges[left_type]]
                right = [component(gp(s + b)) for b in edges[right_type]]
                constant = component(-(2 + epsilon) * gp(s))
                if face in (0, 2):
                    margin = (min(v.lower() for v in left) +
                              min(v.lower() for v in right) + constant.lower())
                else:
                    margin = -(max(v.upper() for v in left) +
                               max(v.upper() for v in right) + constant.upper())
                assert margin > ar("1/50"), (
                    "root face", epsilon, left_type, right_type, face, j, str(margin))
                margins.append(margin)
            root_faces.append({
                "types": [epsilon, left_type, right_type], "face": face,
                "slabs": slab_count, "strict_margin": str(min(margins)),
            })
            print("root face passed", epsilon, left_type, right_type, face, flush=True)

    strict = []

    def positive(name, value):
        assert value > 0, (name, str(value))
        strict.append({"name": name, "margin": str(value)})

    c_inner = (17 * pi / 125).cosh()       # 2*pi*.068
    c_pair = (34 * pi / 125).cosh()        # 2*pi*.136
    positive("upper endpoint of pair interval is smaller",
             (83 * pi / 500).cos() - c_pair * (8 * pi / 25).cos())
    curvature = []
    for left, right in ((Q(3, 20), Q(233, 1000)),
                        (Q(233, 1000), Q(49, 100))):
        for j in range(512):
            x = interval(left + (right - left) * Q(j, 512),
                         left + (right - left) * Q(j + 1, 512))
            own = (2 * pi * x).sin() / (c_inner - (2 * pi * x).cos())
            z = x + ar("267/1000")
            other = ((pi * z).cot() if right <= Q(233, 1000) else
                     (2 * pi * z).sin() / (c_pair - (2 * pi * z).cos()))
            bound = 2 * pi * (own - other)
            assert bound > 4, ("curvature", str(x), str(bound))
            curvature.append(bound)
    cc = (237 * pi / 500).cos()
    positive("mixed cotangent height monotonicity", 1 - cc * (pi / 4).cosh())
    mixed = (pi / 4).sinh() / ((pi / 4).cosh() - cc)
    positive("mixed imaginary cotangent is below three quarters", ar("3/4") - mixed)
    k_fixed = pi * (3 * (27 * pi / 100).cot() + 2 * (11 * pi / 50).cot())
    positive("fixed-inner diagonal height bound", 16 - k_fixed)
    c0 = (33 * pi / 50).sin() * arb(2).log() / (2 * pi)
    c1 = 17 * pi / 50 - (33 * pi / 50).sin() / 2
    height = ar("7/500")
    positive("true weight is on the frequency branch",
             c0 + c1 * height - 2 * pi * height)
    cost = 8 + 49 * pi * pi / 64
    positive("stated optimized height coefficient", ar("15557/1000") - cost)
    gain = 2 * pi * height - cost * ar("71/1000") ** 2
    positive("optimized critical action reserve exceeds nine thousandths",
             gain - ar("9/1000"))
    positive("weight epsilon leaves the final one-over-125 reserve",
             gain - ar("1/1000") - ar("1/125"))

    proof = ROOT / "notes/research_mixed_reoptimized_alias_action.md"
    dependencies = [
        "notes/research_mixed_alias_reflection_budget.md",
        "notes/research_mixed_conditional_image_contours.md",
        "notes/research_mixed_cyclic_critical_height_bounds.md",
        "notes/research_mixed_fourier_weight_continuation.md",
        "notes/research_mixed_conditional_critical_images.md",
    ]
    record = {
        "status": "passed",
        "precision_bits": args.precision,
        "root_face_count": len(root_faces),
        "root_face_slabs": len(root_faces) * slab_count,
        "neighbor_edge_segments_per_type": 4 * edge_count,
        "root_face_threshold": "1/50",
        "root_faces": root_faces,
        "curvature_intervals": len(curvature),
        "curvature_threshold": "4",
        "minimum_curvature_bound": str(min(curvature)),
        "strict_comparison_count": len(strict),
        "strict_comparisons": strict,
        "optimized_height_cost": str(cost),
        "critical_action_reserve": str(gain),
        "scope": (
            "Original logarithmic conditional root existence on complete parameter rectangles, "
            "reoptimized critical-action comparison and exact-weight local density only; "
            "not a full shifted conditional packet or an outer-contour bound."
        ),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_sha256": sha256(proof.read_bytes()).hexdigest(),
        "dependencies": {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print("PASS", len(root_faces), "root faces,", len(curvature),
          "curvature intervals,", len(strict), "scalar margins")


if __name__ == "__main__":
    main()
