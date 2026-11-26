#!/usr/bin/env python3
"""Exact scalar checks for the internal-pair angular-tail proof.

This checks only the explicitly listed rational comparisons. The uniform
recurrence and Fourier implications have their written proofs in the note.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json


def main():
    root = Path(__file__).resolve().parents[1]
    checks = []

    def less(name, left, right):
        assert left < right, (name, left, right)
        checks.append({
            "name": name, "left": str(left), "right": str(right),
            "positive_margin": str(right - left),
        })

    x = F(107, 100)
    less("sinh tail ratio", x*x/F(42), F(1))
    less("sinh(107/100) upper majorant",
         x+x**3/F(6)+x**5/(F(120)*(1-x*x/F(42))), F(4, 3))
    less("sqrt(13) upper square", F(13), F(361, 100)**2)
    less("sqrt(5) upper square", F(5), F(56, 25)**2)
    upper_k_imag = F(1, 3)*(1+F(1, 4)/(1+F(16, 9)))
    assert upper_k_imag == F(109, 300)
    less("imaginary harmonic coordinate", upper_k_imag, F(3, 8))
    cosh_lower = 1+F(3, 4)**2/2+F(3, 4)**4/24
    less("wire-height ellipse bound", F(1033, 800), cosh_lower)
    tail_ceiling = F(3, 2)*F(7, 6)+F(3, 4)+F(1, 100)
    assert tail_ceiling == F(251, 100)
    less("angular-tail ceiling versus pair lower bound",
         tail_ceiling, F(63, 25))
    assert F(63, 25)-tail_ceiling == F(1, 100)
    dependencies = [
        "notes/research_internal_pair_angular_tail_transport.md",
        "notes/research_physical_row_riccati_transport.md",
        "notes/research_even_complete_low_kernel.md",
        "notes/research_last_physical_row_riccati.md",
        "notes/research_internal_pair_complete_edge_gap.md",
        "notes/research_positive_path_real_wire_order.md",
        "notes/research_pair_triangular_normal_region.md",
        "notes/research_internal_pair_combined_contour_reduction.md",
    ]
    record = {
        "status": "passed",
        "scope": "Exact rational scalar comparisons only; analytic implications are written proofs.",
        "strict_comparisons": len(checks),
        "exact_identities": 3,
        "checks": checks,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: sha256((root/name).read_bytes()).hexdigest()
            for name in dependencies
        },
    }
    output = root/"repro/results/research-internal-pair-angular-tail-transport.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"passed: {len(checks)} strict rational comparisons, 3 exact identities")
    print(output)


if __name__ == "__main__":
    main()
