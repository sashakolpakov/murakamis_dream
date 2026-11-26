#!/usr/bin/env python3
"""Exact scalar and degree bookkeeping for the whole-boundary theorem.

This does not test or replace the written source and contour proof.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    gamma, delta, pi_upper = F(1, 100), F(21, 200), F(22, 7)
    comparisons = {
        "1/(20*pi_upper)-gamma": F(1, 20) / pi_upper - gamma,
        "delta-2*gamma": delta - 2 * gamma,
        "2*delta-4*gamma": 2 * delta - 4 * gamma,
    }
    assert all(value > 0 for value in comparisons.values())

    # Each literal edge has degree <=N-1 in each slot. A loop uses
    # the same variable in both slots; tracing other variables cannot
    # increase this degree. We check this accounting independently
    # by counting edge endpoints and by formal edgewise exponents.
    fixtures = [
        ("one_free_path", [(0, 1), (1, 2), (2, 3)], {0, 1, 2}, {3}),
        ("two_free_path", [(0, 1), (1, 2), (2, 3)], {1, 2}, {0, 3}),
        ("branching", [(0, 1), (0, 2), (0, 3)], {0}, {1, 2, 3}),
        ("outside_loop_and_parallel", [(0, 1), (0, 1), (1, 1)], {0}, {1}),
        ("selected_loop", [(0, 0), (0, 1)], {0}, {1}),
    ]
    rows = []
    for name, edges, selected, outside in fixtures:
        vertices = set(sum(([a, b] for a, b in edges), []))
        degrees = {v: sum((a == v) + (b == v) for a, b in edges) for v in vertices}
        assert sum(degrees.values()) == 2 * len(edges)
        for level in (2, 3, 8, 17):
            bound = {v: degrees[v] * (level - 1) for v in outside}
            edgewise = {v: 0 for v in outside}
            for a, b in edges:
                for endpoint in (a, b):
                    if endpoint in outside:
                        edgewise[endpoint] += level - 1
            assert bound == edgewise
        m, e = len(selected), len(edges)
        exponent = 2 * m - F(3, 2) * e - F(1, 2) * m
        assert exponent == F(3, 2) * (m - e)
        if name == "one_free_path":
            assert exponent == 0
        elif name == "two_free_path":
            assert exponent == F(-3, 2)
        rows.append({"name": name, "degrees": degrees, "source_N_power": str(exponent)})

    root = Path(__file__).resolve().parents[1]
    paths = [
        Path(__file__).resolve(),
        root / "notes/research_network_whole_boundary_decay.md",
        root / "notes/research_uniform_path_trace_assembly.md",
        root / "notes/research_degree_controlled_network_source.md",
        root / "notes/research_network_degree_power_source.md",
        root / "notes/research_bare_kernel_thin_rectangle.md",
        root / "notes/research_path_mixed_trace_currents.md",
        root / "notes/research_affine_reduction_fibers_and_core_obligation.md",
        root / "notes/research_boundary_crossing_packet_preservation.md",
    ]
    result = {
        "status": "all exact bookkeeping checks passed",
        "scope": "Three rational loss comparisons; literal incidence degrees and source N powers. No contour-proof validation.",
        "strict_margins": {key: str(value) for key, value in comparisons.items()},
        "degree_fixtures": rows,
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
