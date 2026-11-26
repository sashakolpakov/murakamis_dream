#!/usr/bin/env python3
"""Outward height certificate allowing every filling charge in [0, 1].

The return enclosures are those of the unit-charge certificate. Here every
separating slope is required to be nonpositive, so decreasing a charge can
only strengthen its strict separation. Existence of a positive solution is
not asserted by this program.
"""

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

import certify_positive_path_maximum_height as base


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--maximum-boxes", type=int, default=100000)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1]
                        / "repro/results/research-fractional-path-maximum-height.json")
    args = parser.parse_args()
    if args.precision < 100:
        parser.error("Use at least 100 bits.")
    base.ctx.prec = args.precision
    base.PI = base.arb.pi()
    original_selector = base.choose_slope
    base.choose_slope = lambda box: min(original_selector(box), F(0))
    coarse = ((base.arb(5) / 2).cosh() - (base.arb(1) / 2).cosh()
              - base.arb(2).cosh() - 1)
    assert coarse > 0
    stack = [(F(i, 8), F(i + 1, 8),
              F(23, 20) + F(17 * j, 80),
              F(23, 20) + F(17 * (j + 1), 80))
             for i in range(8) for j in range(4)]
    accepted = []
    visits = 0
    started = time.monotonic()
    try:
        while stack:
            box = stack.pop()
            visits += 1
            assert visits <= args.maximum_boxes, "Unfinished coverage; no result saved."
            result = base.certify_box(box, 384)
            if result is not None:
                assert F(result["slope"]) <= 0
                accepted.append(result)
                continue
            al, ah, hl, hh = box
            if math.pi * float(ah - al) >= float(hh - hl):
                middle = (al + ah) / 2
                stack.extend(((al, middle, hl, hh), (middle, ah, hl, hh)))
            else:
                middle = (hl + hh) / 2
                stack.extend(((al, ah, hl, middle), (al, ah, middle, hh)))
    finally:
        base.choose_slope = original_selector
    area = sum((F(r["box"][1]) - F(r["box"][0]))
               * (F(r["box"][3]) - F(r["box"][2])) for r in accepted)
    assert area == F(17, 20)
    here = Path(__file__).resolve()
    dependency = Path(base.__file__).resolve()
    record = {
        "status": "passed",
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "dependency_sha256": {
            dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()
        },
        "precision_bits": base.ctx.prec,
        "domain": {"angle_over_pi": ["0", "1"], "height": ["23/20", "2"]},
        "charges": "[0,1]; every accepted support slope is nonpositive",
        "powers": "all n >= 3",
        "scope": "Height exclusion for existing positive solutions; no existence inference.",
        "coarse_height_two_margin": str(coarse),
        "accepted_boxes": len(accepted),
        "visited_boxes": visits,
        "boundary_segments": sum(sum(r["boundary_segments"].values()) for r in accepted),
        "elapsed_seconds": time.monotonic() - started,
        "certificate": accepted,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: v for k, v in record.items() if k != "certificate"}, indent=2))


if __name__ == "__main__":
    main()
