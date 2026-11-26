#!/usr/bin/env python3
"""Exact constants for the real Newton entropy and far-period source bound."""

from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

import verify_next_crossing_complex_phase as base
from verify_three_crossing_real_tail_rates import unit_dilogarithm


ROOT = Path(__file__).resolve().parents[1]
R, C, PI, IM = base.R, base.C, base.PI, base.IM


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def J(t):
    """Real sine integral, with an outward unit-circle dilogarithm."""
    clock = base.exponential(2 * IM * C(PI) * C(t))
    return -unit_dilogarithm(clock).im / (2 * PI)


def run():
    scalar_path = ROOT / "repro/results/research-three-crossing-real-tail-rates.json"
    scalar = json.loads(scalar_path.read_text())
    scalar_script = ROOT / "experiments/verify_three_crossing_real_tail_rates.py"
    assert scalar["status"] == "passed"
    assert scalar["script_sha256"] == digest(scalar_script)
    for name, expected in scalar["dependencies"].items():
        assert digest(ROOT / name) == expected
    peak_upper = F(scalar["certificates"]["A_global_peak"]["interval"][1])
    assert peak_upper < F(4531, 10000)

    catalan_upper = sum((F((-1)**j, (2*j+1)**2) for j in range(65)), F(0))
    assert PI.lo > F(31415, 10000) and PI.hi < F(22, 7)
    assert 2 * catalan_upper / F(31415, 10000) < F(729, 1250)
    sqrt_three_upper = F(17321, 10000)
    assert sqrt_three_upper**2 > 3
    loss_lower = (128 - 63 * sqrt_three_upper) / (72 * F(22, 7))
    assert loss_lower == F(1321439, 15840000) > 0
    far_rate = 2 * F(729, 1250) + F(4531, 10000) - loss_lower
    assert far_rate == F(24331441, 15840000) < F(1537, 1000)

    y = R(F(13, 40))
    a = R(F(3, 10)) / PI
    assert (R(F(1, 2)) - y - a).lo > 0
    newton_tail = (-J(R(F(1, 2)) - y + a)
                   -J(R(F(1, 2)) - y - a)-2*J(y))
    assert newton_tail.hi < F(249, 500)
    tail_rate = F(249, 500) + F(729, 1250) + F(4531, 10000)
    assert tail_rate == F(15343, 10000) < F(1537, 1000)

    dependencies = {
        str(scalar_script.relative_to(ROOT)): digest(scalar_script),
        str(Path(base.__file__).relative_to(ROOT)): digest(Path(base.__file__)),
    }
    return {
        "status": "passed",
        "method": "Rational outward arithmetic with explicit logarithm and dilogarithm tails.",
        "b2_upper": "729/1250",
        "A_peak_upper": "4531/10000",
        "angular_loss_at_pi_over_three_lower": str(loss_lower),
        "far_period_rate_upper": str(far_rate),
        "comparison_geometric_rate_lower": "1537/1000",
        "newton_tail_angle": "3/5",
        "newton_tail_y": "13/40",
        "newton_tail_interval": newton_tail.record(),
        "newton_tail_upper": "249/500",
        "newton_tail_source_rate_upper": str(tail_rate),
        "script_sha256": digest(Path(__file__).resolve()),
        "dependencies": dependencies,
        "scalar_certificate": str(scalar_path.relative_to(ROOT)),
        "scalar_certificate_sha256": digest(scalar_path),
        "scope": (
            "Real Newton entropy constants and original source upper bounds only. "
            "No intermediate-angle contour estimate is asserted."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-three-crossing-real-period-constants.json",
    )
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("Exact real-period Newton constants passed.")
    print(f"Saved {args.output}")
