#!/usr/bin/env python3
"""Exact rational comparisons for the small-charge path source theorem."""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path("repro/results/research-small-charge-path-source.json"))
    args = parser.parse_args()
    checks = []

    def less(label, left, right):
        assert left < right, (label, left, right)
        checks.append({
            "comparison": label, "left": str(left), "right": str(right),
            "positive_difference": str(right-left)})

    pi_upper = F(22, 7)
    radius = F(1, 100)
    charge = F(1, 320)
    delta = F(1, 15000)
    cubic_sum = (F(1, 8)
                 + F(2, 5)*(F(51, 100)*F(101, 100))**3
                 + F(51, 350))
    less("one-incidence quadratic error", cubic_sum, F(1, 3))
    less("asinh argument on the larger polydisk",
         F(51, 100)*2*radius*F(101, 100), F(1, 50))
    assert 2*radius**2/3 == delta
    less("fixed-point angle coefficient",
         2*pi_upper/(3-delta), F(21, 10))
    less("fixed-point image radius", F(21, 10)*charge, radius)
    less("fixed-point row contraction",
         2*pi_upper*charge*8*radius/(3-delta)**2, F(1, 1000))
    less("height coefficient",
         2*pi_upper*(2+delta)/(3-delta)**2, F(3, 2))
    less("thin-kernel height", F(3, 2)*charge, F(1, 200))
    less("vertical real displacement",
         F(7, 12), F(94, 100)-F(21, 10)*charge)
    less("vertical mixed-Hessian absorption",
         126*charge, 3*(F(94, 100)-F(21, 10)*charge))
    less("mixed-current gap", F(1, 400), F(49, 5760)/pi_upper)
    less("subset action budget", F(3, 4)*charge**2, F(1, 800))
    x = F(9, 10)
    less("outer angular loss", F(1, 600),
         (x*x/2-x**4/24)/200)
    assert F(1, 600)-F(1, 800) == F(1, 2400)

    # Corollary 3: arbitrary fixed signed powers, including zero.
    signed_charge = F(1, 2000)
    signed_coefficient = F(63, 10)
    less("signed fixed-point angle coefficient",
         2*pi_upper/(1-delta), signed_coefficient)
    less("signed fixed-point image radius",
         signed_coefficient*signed_charge, radius)
    less("signed fixed-point row contraction",
         2*pi_upper*signed_charge*8*radius/(1-delta)**2, F(1, 1000))
    less("signed thin-kernel height",
         signed_coefficient*signed_charge, F(1, 200))
    displacement = F(94, 100)-signed_coefficient*signed_charge
    height_change = 2*signed_coefficient*signed_charge
    less("signed positive vertical displacement", F(0), displacement)
    less("signed mixed-current gap without filling absorption", F(1, 400),
         (displacement**2/40-F(42, 4)*height_change**2)/pi_upper)
    less("signed subset action budget",
         F(63, 20)*signed_charge**2, F(1, 800))

    # Corollary 4: arbitrary fixed incidence degrees, with d_v >= 1.
    graph_epsilon = radius**2/3
    assert graph_epsilon == F(1, 30000)
    less("graph fixed-point angle and height coefficient",
         2*pi_upper/(1-graph_epsilon), signed_coefficient)
    less("graph fixed-point row contraction",
         2*pi_upper*signed_charge*(8*radius/3)/(1-graph_epsilon)**2,
         F(1, 1000))

    note = Path("notes/research_small_charge_path_source.md")
    result = {
        "status": "passed", "arithmetic": "exact fractions",
        "checks": len(checks), "comparisons": checks,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "passed", "checks": len(checks),
                      "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
