#!/usr/bin/env python3
"""Exact winding gate on actual octahedral edges, including real-ray ties.

This supplements the written general proof.  It does not identify a
topological exterior from its shape equations or verify quantum growth.
"""

from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path

from audit_actual_reflected_two_circle_octahedral_base import (
    complex_multiply, tetrahedral_certificate,
)


def winding(shapes):
    partial = (F(1), F(0))
    count = 0
    real_hits = []
    for index, shape in enumerate(shapes, 1):
        if shape[1] <= 0:
            raise ValueError("Every incident shape must be strictly upper-half-plane")
        previous = partial
        partial = complex_multiply(partial, shape)
        count += previous[1] < 0 <= partial[1]
        if partial[1] == 0:
            real_hits.append((index, "positive" if partial[0] > 0 else "negative"))
    if partial != (1, 0):
        raise ValueError("The exact edge product must equal one")
    return count, real_hits


def main():
    actual, _, _ = tetrahedral_certificate()
    shape_triple = ((F(0), F(1)), (F(1, 2), F(1, 2)), (F(1), F(1)))
    tested_orderings = 0
    for edge in actual["edges"]:
        shapes = [shape for shape, count in zip(shape_triple, edge["shape_counts"])
                  for _ in range(count)]
        # Winding is invariant under reordering: every increment is positive
        # and the total argument is the same. Different orders hit different
        # intermediate real rays and exercise the exact endpoint convention.
        for ordering in set(permutations(shapes)):
            assert winding(ordering)[0] == 1
            tested_orderings += 1

    straight = (F(0), F(1))
    assert winding([straight] * 4) == (1, [(2, "negative"), (4, "positive")])
    assert winding([straight] * 8)[0] == 2
    assert winding([straight] * 12)[0] == 3
    w, v = (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5))
    for ordering in set(permutations((w, v, w, v))):
        assert winding(ordering)[0] == 1
    # Same algebraic edge product, distinct integer branch: doubling an
    # admissible list must be rejected by the UNIT-winding criterion.
    assert winding([w, v] * 4)[0] == 2
    for invalid in ([(F(-1), F(0))] * 2, [w, w]):
        try:
            winding(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("An invalid certificate was admitted")

    result = {
        "status": "PASS",
        "actual_octahedral_edges": len(actual["edges"]),
        "exact_shape_orderings": tested_orderings,
        "positive_and_negative_real_partial_products": "PASS",
        "product_one_higher_winding_rejected": [2, 3],
        "rational_complex_non_root_of_unity_factors": "PASS",
        "strict_positivity_and_edge_product_gates": "PASS",
        "scope": "Exact edge-winding gate, not a universal existence or quantum asymptotic proof.",
    }
    Path(__file__).with_name("finite_real_algebraic_geometric_certificate_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(f"PASS {len(actual['edges'])} actual edges, {tested_orderings} exact orderings; "
          "real-ray ties and higher-winding rejection")


if __name__ == "__main__":
    main()
