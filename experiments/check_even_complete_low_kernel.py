#!/usr/bin/env python3
"""Check exact original Newton interpolation at the even complete endpoint.

The convergence diagnostics do not replace the uniform estimates in the note.
No row is generated from the Riccati recurrence being used in that proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEPENDENCIES = (
    "experiments/check_even_complete_low_kernel.py",
    "notes/research_even_complete_low_kernel.md",
    "notes/research_last_physical_row_riccati.md",
    "notes/research_physical_row_riccati_transport.md",
)


def newton_values(z, colors, squares, count):
    result = [mp.mpc(1)]
    for k in range(1, count):
        result.append(result[-1] * (colors[k - 1] - z) / squares[k])
    return result


def relative_error(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-even-complete-low-kernel.json",
    )
    args = parser.parse_args()
    if args.precision < 100:
        parser.error("use at least 100 decimal digits for these comparisons")
    mp.mp.dps = args.precision
    free_colors = [mp.mpc(-2), mp.mpc("-0.2", "-2.4"),
                   mp.mpc("1.3", "-2.2"), mp.mpc("1.5", "0.5")]
    max_error = mp.mpf(0)
    identity_count = weight_count = 0
    records = []
    for level in (8, 16, 32, 64, 128, 256):
        m = level // 2
        theta = mp.pi / level
        colors = [2 * mp.cos((2 * j + 1) * theta) for j in range(m)]
        squares = [(2 * mp.sin(j * theta)) ** 2 for j in range(m)]
        complete = newton_values(-2, colors, squares, m)
        weights = [mp.cot((h + mp.mpf("0.5")) * theta) / m
                   for h in range(m)]
        weight_sum = mp.fsum((-1) ** h * weights[h] for h in range(m))
        max_error = max(max_error, abs(weight_sum - 1))
        weight_count += 1
        # Construct each row directly from its defining Newton factors.
        physical = []
        for j in range(m):
            physical.append(newton_values(colors[j], colors, squares, j + 1))
        for w in free_colors:
            ordinary = newton_values(w, colors, squares, m)
            low = mp.fsum(a * b for a, b in zip(complete, ordinary))
            rows = [mp.fsum(a * ordinary[k] for k, a in enumerate(row))
                    for row in physical]
            interpolated = mp.fsum(
                (-1) ** h * weights[h] * rows[m - 1 - h]
                for h in range(m)
            )
            error = relative_error(low, interpolated)
            max_error = max(max_error, error)
            identity_count += 1
            if rows[-1] == 0:
                raise AssertionError("the independently evaluated last row vanished")
            quotient = low / rows[-1]
            records.append({
                "level": level,
                "free_color": [mp.nstr(w.real, 24), mp.nstr(w.imag, 24)],
                "relative_interpolation_error": mp.nstr(error, 18),
                "low_to_last_ratio": [mp.nstr(quotient.real, 24),
                                      mp.nstr(quotient.imag, 24)],
                "sqrt_level_times_ratio_error":
                    mp.nstr(mp.sqrt(level) * abs(quotient - 1), 18),
            })
    tolerance = mp.power(10, -args.precision // 2)
    if max_error > tolerance:
        raise AssertionError(f"finite identity error {max_error} exceeds {tolerance}")
    record = {
        "status": "passed",
        "scope": "finite identity checks; convergence entries are diagnostics",
        "precision_digits": args.precision,
        "interpolation_identities": identity_count,
        "constant_weight_identities": weight_count,
        "maximum_relative_identity_error": mp.nstr(max_error, 24),
        "project_dependency_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in DEPENDENCIES
        },
        "cases": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: v for k, v in record.items()
                      if k not in ("cases", "project_dependency_sha256")}, indent=2))


if __name__ == "__main__":
    main()
