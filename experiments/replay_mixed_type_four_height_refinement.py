#!/usr/bin/env python3
"""Independent sine/cotangent replay of the type-four height refinement.

No author Newton routine is imported. The separately established sine-lift
primitive supplies proposals and derivatives; this script reconstructs
the rectangle edge parameters and verifies each affine Newton enclosure,
both output heights, complete covers, and all inherited provenance.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE = ROOT / "experiments/replay_mixed_cyclic_block_localization.py"
AUTHOR = ROOT / "experiments/certify_mixed_type_four_height_refinement.py"
PROOF = ROOT / "notes/research_mixed_type_four_height_refinement.md"
RECTS = [
    ["3/10", "39/100", "-3/100", "1/50"],
    ["27/100", "33/100", "-57/1000", "-1/1000"],
]
INHERITED = [
    ("mixed_cyclic_block_localization", "mixed-cyclic-block-localization",
     "research_mixed_cyclic_critical_localization.md"),
    ("mixed_cyclic_window_heights", "mixed-cyclic-window-heights",
     "research_mixed_cyclic_critical_height_bounds.md"),
    ("mixed_type_three_window_strip", "mixed-type-three-window-strip",
     "research_mixed_type_three_window_strip.md"),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decode(address):
    lo, hi = [Q(0), Q(0)], [Q(1), Q(1)]
    for j, bit in enumerate(address):
        assert bit in "01"
        k = j % 2
        midpoint = (lo[k] + hi[k]) / 2
        if bit == "0":
            hi[k] = midpoint
        else:
            lo[k] = midpoint
    return lo, hi


def verify_cover(addresses):
    leaves = sorted(addresses)
    assert len(leaves) == len(set(leaves))
    assert all(not b.startswith(a) for a, b in zip(leaves, leaves[1:]))
    assert sum((Q(1, 2 ** len(a)) for a in leaves), Q(0)) == 1
    for address in leaves:
        decode(address)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path, default=ROOT /
                    "repro/results/research-mixed-type-four-height-refinement.json")
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-type-four-height-refinement-replay.json")
    args = ap.parse_args()
    assert args.precision >= 160
    source_bytes = args.input.read_bytes()
    source = json.loads(source_bytes)
    assert source["status"] == "passed"
    assert source["script_sha256"] == sha(AUTHOR)
    assert source["proof_sha256"] == sha(PROOF)
    assert [[Q(x) for x in row] for row in source["rectangles"]] == [
        [Q(x) for x in row] for row in RECTS]
    assert Q(source["upper_height"]) == -Q(1, 50)
    dependencies = dict(source["dependencies"])
    for path, digest in dependencies.items():
        assert sha(ROOT / path) == digest, path
    for stem, record_stem, proof_name in INHERITED:
        prior_author = ROOT / f"repro/results/research-{record_stem}.json"
        prior_replay = ROOT / f"repro/results/research-{record_stem}-replay.json"
        old = json.loads(prior_author.read_text())
        review = json.loads(prior_replay.read_text())
        for data, script in (
            (old, ROOT / f"experiments/certify_{stem}.py"),
            (review, ROOT / f"experiments/replay_{stem}.py"),
        ):
            assert data["status"] == "passed"
            assert data["script_sha256"] == sha(script)
            assert data["proof_sha256"] == sha(ROOT / "notes" / proof_name)
            for key in ("dependencies", "dependencies_sha256"):
                for name, digest in data.get(key, {}).items():
                    assert sha(ROOT / name) == digest, (record_stem, name)
        assert review["input_sha256"] == sha(prior_author)
    dependencies[str(PRIMITIVE.relative_to(ROOT))] = sha(PRIMITIVE)
    dependencies[str(AUTHOR.relative_to(ROOT))] = sha(AUTHOR)
    dependencies[str(PROOF.relative_to(ROOT))] = sha(PROOF)
    initial = dict(dependencies)
    script_hash = sha(__file__)
    proof_hash = sha(PROOF)
    source_hash = hashlib.sha256(source_bytes).hexdigest()

    spec = importlib.util.spec_from_file_location("independent_sine_block", PRIMITIVE)
    primitive = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primitive)
    ctx.prec = args.precision
    primitive.PI = arb.pi()
    pi, ar, pt = primitive.PI, primitive.ar, primitive.pt
    centers, radii = primitive.CENTERS, primitive.RADII
    inclusion = []
    for t, rectangle in enumerate(RECTS):
        xl, xh, yl, yh = map(Q, rectangle)
        cr, ci = centers[t]
        distance = max((x-cr)**2 + (y-ci)**2
                       for x in (xl, xh) for y in (yl, yh))
        margin = radii[t]**2 - distance
        assert margin > 0
        inclusion.append(str(margin))
    assert inclusion == source["rectangle_disk_inclusion_margins"]

    def edge(t, face, lo, hi):
        xl, xh, yl, yh = map(Q, RECTS[t])
        parameter = ar(lo).union(ar(hi))
        if face in (0, 2):
            return acb(ar(xl) + ar(xh-xl)*parameter,
                       ar(yl if face == 0 else yh))
        assert face in (1, 3)
        return acb(ar(xh if face == 1 else xl),
                   ar(yl) + ar(yh-yl)*parameter)

    def verify(address, types, faces):
        eps, ta, tb = types
        lo, hi = decode(address)
        pp = [edge(t, faces[j], lo[j], hi[j])
              for j, t in enumerate((ta, tb))]
        midpoint = [(lo[j]+hi[j])/2 for j in (0, 1)]
        p0 = [edge(t, faces[j], midpoint[j], midpoint[j])
              for j, t in enumerate((ta, tb))]
        pf = [complex(float(v.real.mid()), float(v.imag.mid())) for v in p0]
        z, Y, D = primitive.propose(*pf, eps)
        zz = [pt(v) for v in z]
        yy = [[pt(v) for v in row] for row in Y]
        dd = [[pt(v) for v in row] for row in D]
        if not abs(yy[0][0]*yy[1][1]-yy[0][1]*yy[1][0]) > 0:
            return None
        f0, J0, E0 = primitive.fg(zz, p0, eps)
        degree = 2+eps
        dp = [pp[j]-p0[j] for j in (0, 1)]
        dz = [sum((dd[i][j]*dp[j] for j in (0, 1)), acb(0)) for i in (0, 1)]
        linear = [
            f0[i] + sum((
                (sum((J0[i][k]*dd[k][j] for k in (0, 1)), acb(0)) +
                 (E0[i] if i == j else 0))*dp[j]
                for j in (0, 1)), acb(0))
            for i in (0, 1)
        ]

        def remainder(base, delta):
            box = base + acb(arb(0, abs(delta.real).upper()),
                             arb(0, abs(delta.imag).upper()))
            if not (box.real > 0 and box.real < 1):
                return arb.pos_inf()
            return pi*pi*abs(1/(pi*box).sin()**2)*abs(delta)**2/2

        shared = remainder(zz[0]+zz[1], dz[0]+dz[1])
        remainders = [
            shared + remainder(zz[j]+p0[j], dz[j]+dp[j]) +
            degree*remainder(zz[j], dz[j]) for j in (0, 1)
        ]
        residual = [
            abs(sum((yy[i][j]*linear[j] for j in (0, 1)), acb(0))) +
            sum((abs(yy[i][j])*remainders[j] for j in (0, 1)), arb(0))
            for i in (0, 1)
        ]
        if any(not v.is_finite() for v in residual):
            return None
        for factor in (1.25, 1.5, 2, 1.375, 1.75):
            rad = [Q(max(1, int(np.ceil(float(b.upper())*factor*2**40))), 2**40)
                   for b in residual]
            center = acb(ar(centers[eps][0]), ar(centers[eps][1]))
            if not all(abs(zz[i]+dz[i]-center)+ar(rad[i]) < ar(radii[eps])
                       for i in (0, 1)):
                continue
            hz = [dz[i]+acb(arb(0, ar(rad[i])), arb(0, ar(rad[i])))
                  for i in (0, 1)]
            roots = [zz[i]+hz[i] for i in (0, 1)]
            if not all(v.real > ar(Q(23, 100)) and v.real < ar(Q(9, 20))
                       and abs(v.imag) < ar(Q(3, 25)) for v in roots+pp):
                continue

            def cot_difference(base, delta):
                return -(pi*delta).sin()/((pi*(base+delta)).sin()*(pi*base).sin())

            cross = cot_difference(zz[0]+zz[1], hz[0]+hz[1])
            diag = [cot_difference(zz[i]+p0[i], hz[i]+dp[i]) -
                    degree*cot_difference(zz[i], hz[i]) for i in (0, 1)]
            defect = [
                [acb(int(i == j)) -
                 sum((yy[i][k]*J0[k][j] for k in (0, 1)), acb(0)) -
                 pi*((yy[i][0]+yy[i][1])*cross+yy[i][j]*diag[j])
                 for j in (0, 1)] for i in (0, 1)
            ]
            if not all(residual[i]+sum((
                    abs(defect[i][j])*ar(rad[j]) for j in (0, 1)), arb(0)) < ar(rad[i])
                    for i in (0, 1)):
                continue
            if not all(v.imag < -ar(Q(1, 50)) for v in roots):
                continue
            return max(v.imag.upper() for v in roots)
        return None

    expected = {(1, a, b, fa, fb) for a, b in ((0, 0), (0, 1), (1, 1))
                for fa in range(4) for fb in range(4)}
    cases = source["cases"]
    assert len(cases) == source["case_count"] == 48
    assert {(*case["types"], *case["faces"]) for case in cases} == expected
    assert sum(c["accepted"] for c in cases) == source["accepted_cells"] == 249
    total, refinements, results = 0, 0, []
    start = time.time()
    for case in cases:
        verify_cover(case["addresses"])
        assert case["accepted"] == len(case["addresses"])
        accepted, count, maximum = [], 0, None
        for original_address in case["addresses"]:
            work = [original_address]
            while work:
                address = work.pop()
                value = verify(address, case["types"], case["faces"])
                if value is not None:
                    accepted.append(address)
                    maximum = value if maximum is None else max(maximum, value)
                    continue
                assert len(address) < len(original_address)+12, (
                    case["types"], case["faces"], address)
                work.extend([address+"0", address+"1"])
                count += 1
        verify_cover(accepted)
        row = {
            "types": case["types"], "faces": case["faces"],
            "original_cells": len(case["addresses"]), "replay_cells": len(accepted),
            "refinements": count, "addresses": sorted(accepted),
            "maximum_imaginary_upper": str(maximum),
        }
        results.append(row)
        total += len(accepted)
        refinements += count
        print(json.dumps({k: v for k, v in row.items() if k != "addresses"}), flush=True)
    assert args.input.read_bytes() == source_bytes
    assert initial == {p: sha(ROOT/p) for p in initial}
    assert script_hash == sha(__file__) and proof_hash == sha(PROOF)
    out = {
        "status": "passed", "precision_bits": args.precision,
        "case_count": 48, "original_cells": source["accepted_cells"],
        "accepted_cells": total, "refinements": refinements, "cases": results,
        "rectangles": RECTS, "upper_height": "-1/50",
        "rectangle_disk_inclusion_margins": inclusion,
        "primitive": str(PRIMITIVE.relative_to(ROOT)),
        "analytic_independence": "Original sine-log equations, cotangent differences and csc-square Taylor remainders; no author Newton routine imported.",
        "scope": "Both original type-four block outputs on the entire independent critical rectangles; all cyclic lengths via previously proved global holomorphy and harmonic maximum principles. No new finite-source bound.",
        "elapsed_seconds": time.time()-start,
        "input_sha256": source_hash, "script_sha256": script_hash,
        "proof_sha256": proof_hash, "dependencies": initial,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+"\n")
    print("PASS", len(results), "boundary products,", total,
          "replayed cells,", refinements, "refinements", flush=True)


if __name__ == "__main__":
    main()
