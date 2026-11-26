#!/usr/bin/env python3
"""Exact rational checks for the attached reflected-pair energy proof.

This checks the explicit trial, polynomial majorant and strict energy
gap. It does not numerically solve a filling equation or test a quantum
asymptotic. The analytic argument is in the accompanying research note.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/research_attached_even_reflected_pair_geometry.md"


def rational(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-attached-reflected-pair-energy.json",
    )
    args = parser.parse_args()

    # The imaginary filling constraints, normalized by pi.
    assert -F(1, 16) - F(15, 16) == -1
    assert -F(1, 10) - F(1, 10) - F(4, 5) == -1

    # Each first-edge coordinate is affine in z=1/k, 0<=z<=1/2.
    affine = [
        (F(15, 64), F(1, 20)),
        (F(15, 64), -F(1, 20)),
        (-F(1, 5), -F(1, 32)),
        (F(1, 5), -F(1, 32)),
        (-F(1, 5), F(0)),
        (-F(1, 5), F(0)),
    ]
    maxima = [max(abs(b), abs(a / 2 + b)) for a, b in affine]
    assert maxima == [
        F(107, 640), F(43, 640), F(21, 160), F(11, 160),
        F(1, 10), F(1, 10),
    ]

    # For P(z)=360-330z+29z^2-z^3, P'<0 on [0,9/8].
    zmax = F(9, 8)
    assert -330 + 58 * zmax < 0
    pmin = 360 - 330 * zmax + 29 * zmax**2 - zmax**3
    assert pmin == F(12303, 512) > 0

    pi_upper = F(22, 7)
    radius = F(1, 100)
    coordinates = [a * pi_upper for a in maxima]
    coordinates.extend([pi_upper / 20 + radius / 4] * 2)
    largest = max(coordinates)
    assert largest == F(107, 640) * pi_upper
    assert (2 * largest)**2 == F(1385329, 1254400) < zmax

    energy = (
        2 * sum(x**2 for x in coordinates)
        + F(4, 3) * sum(x**4 for x in coordinates)
    )
    assert energy == F(10300525426199761, 5900697600000000)
    assert energy < F(7, 4)

    catalan_partial = 1 - F(1, 9) + F(1, 25) - F(1, 49)
    assert catalan_partial > F(9, 10)
    boundary_lower = F(9, 5) - pi_upper * radius / 2
    assert boundary_lower == F(1249, 700) > F(7, 4)
    compactness_gap = F(9, 5) - F(7, 4) - pi_upper / 200
    assert compactness_gap > 0

    result = {
        "status": "passed",
        "scope": (
            "Exact rational trial-energy inequalities for every real k>=2 "
            "and |Re u|,|Im u|<=1/100. This is not a numerical filling "
            "certificate or an asymptotic test."
        ),
        "python": platform.python_version(),
        "dependencies": "Python standard library only; exact Fraction arithmetic",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(NOTE.read_bytes()).hexdigest(),
        "radius": rational(radius),
        "normalized_affine_coordinate_maxima": [rational(x) for x in maxima],
        "cosine_majorant_minimum": rational(pmin),
        "doubled_largest_coordinate_squared_upper": rational((2 * largest)**2),
        "trial_energy_upper": rational(energy),
        "boundary_energy_lower": rational(boundary_lower),
        "strict_energy_gap": rational(boundary_lower - energy),
        "compact_square_energy_gap": rational(compactness_gap),
        "catalan_alternating_lower": rational(catalan_partial),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "output": str(args.output),
        "script_sha256": result["script_sha256"],
        "strict_energy_gap": result["strict_energy_gap"],
    }))


if __name__ == "__main__":
    main()
