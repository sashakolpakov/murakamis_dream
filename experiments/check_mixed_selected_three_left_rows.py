#!/usr/bin/env python3
"""Exact rational inequalities for the ordinary left-cut comparison.

This verifies the finite elementary step in the cited written proof.
It does not evaluate a quantum sum, find a critical point, or certify
the remaining boundary comparisons.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_selected_three_left_rows.md"
DEPENDENCIES = (
    PROOF,
    ROOT / "notes/research_mixed_half_index_contour.md",
    ROOT / "notes/research_mixed_selected_four_three_finite_reduction.md",
    Path(__file__).resolve(),
)
PI_LO, PI_HI = F(157, 50), F(22, 7)
H, D, MID = F(7, 625), F(7, 100), F(37, 200)
HS = (F(-13, 200), F(17, 250))
HB = (F(-13, 200), F(0), F(17, 250))
REGIONS = (
    (F(11, 50), F(7, 25), F(0), F(1, 5)),
    (F(7, 25), F(9, 20), F(-3, 5), F(0)),
)
TABLE = ((F(243, 5000), F(207, 20000)),
         (F(409, 50000), F(1543, 100000)))


def log_lower(r):
    """Positive finite series below log(r), r > 1."""
    assert r > 1
    t = (r - 1) / (r + 1)
    assert 0 < t < 1
    return 2 * sum((t ** (2*k + 1) / (2*k + 1)
                    for k in range(8)), F(0))


def floor_rational(q, denominator=10**8):
    return F((q.numerator * denominator) // q.denominator, denominator)


def verify():
    # Bounds used for the real cotangent on the two coordinate intervals.
    for angle, upper in ((F(3, 50), F(1, 5)),
                         (F(17, 100), F(3, 5))):
        t = PI_HI * angle
        sin_upper = t - t**3 / 6 + t**5 / 120
        cos_lower = 1 - t**2 / 2
        assert cos_lower > 0
        assert sin_upper < upper * cos_lower

    assert max(abs(hs) for hs in HS) * F(3, 5) < D
    t = MID * PI_HI
    sine_upper = t - t**3 / 6 + t**5 / 120
    assert 0 < t < 1 and sine_upper > 0
    corners = (F(11, 50), F(7, 25), F(9, 20))
    sine_lower = {
        w: 1 - (PI_HI * abs(F(1, 2) - MID - w))**2 / 2
        for w in corners
    }
    assert all(x > 0 for x in sine_lower.values())

    records, grouped = [], []
    for iy, (yl, yu, cylo, cyhi) in enumerate(REGIONS):
        for iv, (vl, vu, cvlo, cvhi) in enumerate(REGIONS):
            entries = []
            for y in (yl, yu):
                for v in (vl, vu):
                    ratio = sine_lower[y] * sine_lower[v] / sine_upper**2
                    horizontal = D * log_lower(ratio)
                    for hs in HS:
                        for hb in HB:
                            if hs >= 0:
                                phase = y-v + H*cyhi + max(hb*cvlo, hb*cvhi)
                            else:
                                phase = y-v + H*cylo + min(hb*cvlo, hb*cvhi)
                            q = D*(hb-H) - hs*phase
                            lower = horizontal + (PI_HI if q < 0 else PI_LO)*q
                            assert lower > TABLE[iy][iv] > F(1, 125)
                            rounded_lower = floor_rational(lower)
                            assert TABLE[iy][iv] < rounded_lower <= lower
                            entry = {
                                "region": [iy, iv],
                                "y": str(y), "v": str(v),
                                "h_s": str(hs), "h_b": str(hb),
                                "lower_bound": str(rounded_lower),
                                "table_bound": str(TABLE[iy][iv]),
                            }
                            records.append(entry)
                            entries.append((lower, entry))
            minimum, witness = min(entries, key=lambda pair: pair[0])
            assert len(entries) == 24
            grouped.append({
                "region": [iy, iv],
                "number_checked": len(entries),
                "minimum_lower_bound": str(floor_rational(minimum)),
                "minimizing_corner": witness,
                "proved_table_bound": str(TABLE[iy][iv]),
            })
    assert len(records) == 96
    return {
        "status": "passed",
        "scope": "96 exact rational corner inequalities in Theorem 1; "
                 "convexity and finite-source transfer retain their written proofs",
        "gap": "1/125",
        "height_range": ["0", str(H)],
        "arithmetic": "fractions.Fraction; no floating-point inequalities",
        "checks": records,
        "regions": grouped,
        "sha256": {
            str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in DEPENDENCIES
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        with args.output.open("x") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    print(json.dumps({
        "status": result["status"],
        "corner_inequalities": len(result["checks"]),
        "gap": result["gap"],
        "region_lower_bounds": [r["minimum_lower_bound"] for r in result["regions"]],
        "output": str(args.output) if args.output else None,
    }, indent=2))


if __name__ == "__main__":
    main()
