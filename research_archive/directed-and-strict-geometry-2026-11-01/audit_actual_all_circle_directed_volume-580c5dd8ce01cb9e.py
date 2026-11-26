#!/usr/bin/env python3
"""Reproduce the directed-volume criterion's finite arithmetic and pairings.

Run from the repository root:
    python3 experiments/audit_actual_all_circle_directed_volume.py

The default output is experiments/actual_all_circle_directed_volume_results.json
beside this script. --output may select another path. Only the Python standard
library is required.

The inequalities use exact rational enclosures, with the elementary inputs
3 < pi < 22/7 and r^2/2 - r^4/24 <= 1-cos(r) <= r^2/2. The all-degree
deductions are the symbolic inequalities in the accompanying proof, not a scan
over degrees. The pairing calculation uses the original ordered stacking rule.
No quantum invariant, large-level asymptotic, or geometric completion is tested
numerically here. Decimal ratios in the output are explanatory only; all
decisions use fractions.Fraction.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def normalized_pairing(pairs):
    return tuple(sorted(tuple(sorted(pair)) for pair in pairs))


I = normalized_pairing(((0, 3), (1, 2)))
X = normalized_pairing(((0, 2), (1, 3)))
H = normalized_pairing(((0, 1), (2, 3)))


def components(nodes, edges):
    parent = {node: node for node in nodes}

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for a, b in edges:
        parent[find(a)] = find(b)
    groups = {}
    for node in nodes:
        groups.setdefault(find(node), []).append(node)
    return list(groups.values())


def stack(first, second):
    """Join first's upper 2,3 to second's lower 1,0, respectively."""
    nodes = [(side, i) for side in (0, 1) for i in range(4)]
    edges = [((0, a), (0, b)) for a, b in first]
    edges += [((1, a), (1, b)) for a, b in second]
    edges += [((0, 2), (1, 1)), ((0, 3), (1, 0))]
    boundary = {(0, 0): 0, (0, 1): 1, (1, 2): 2, (1, 3): 3}
    pairs = []
    closed = 0
    for group in components(nodes, edges):
        endpoints = [boundary[p] for p in group if p in boundary]
        if not endpoints:
            closed += 1
        elif len(endpoints) == 2:
            pairs.append(tuple(endpoints))
        else:
            raise AssertionError("A stacked component has the wrong boundary size")
    return normalized_pairing(pairs), closed


def turn(pairing):
    return normalized_pairing((((a + 1) % 4, (b + 1) % 4)
                               for a, b in pairing))


def closure_components(pairing):
    return len(components(range(4), list(pairing) + [(0, 3), (1, 2)]))


def pairing_checks():
    checks = []

    def record(name, obtained, expected):
        if obtained != expected:
            raise AssertionError(name)
        checks.append({"name": name, "obtained": obtained, "expected": expected})

    record("quarter-turn of an odd braid", turn(X), X)
    record("quarter-turn of an even braid", turn(I), H)
    record("two odd turned leaves", stack(X, X), (I, 0))
    record("through pairing before an odd leaf", stack(I, X), (X, 0))
    record("through pairing after an odd leaf", stack(X, I), (X, 0))
    record("terminal odd braid against the turned even product", stack(X, H), (H, 0))
    record("reversed terminal stack", stack(H, X), (H, 0))
    record("cylindrical closure of the final pairing", closure_components(H), 1)
    return checks


def rational_checks():
    k = F(1, 2**16)
    c = k / 2
    t = F(1, 2**14)
    rho = F(1, 16)
    b0 = F(1, 2**11)
    pi_lo, pi_hi = F(3), F(22, 7)
    chi_lo = rho**2 / 2 - rho**4 / 24
    chi_hi = rho**2 / 2
    delta_lo = c * chi_lo / (4 * (1 + c))
    checks = []

    def check(name, left, right):
        left, right = F(left), F(right)
        if not left < right:
            raise AssertionError(name)
        checks.append({
            "name": name,
            "left": str(left),
            "right": str(right),
            "strict_less": True,
            "decimal_ratio": float(left / right),
        })

    check("common strip lower bound", F(1, 2**30), delta_lo)
    check("first tail bound for all degrees and |n|>=2^27",
          64 * pi_hi / (t * delta_lo), 2**54)
    check("second tail bound for all degrees and |n|>=2^27",
          32 * pi_hi**2 / (t**2 * k), 2**54)
    check("outgoing patch under either degree or twist alternative",
          F(330, 361), F(3071, 3072))
    check("uniform charge cutoff", 2, t * 2**27 / (2 * pi_hi))

    # A fixed leaf of the short-center star. Its selected conservative height
    # lies below each of the four branches of the actual height definition.
    n = 2**60 + 1
    D_lo, D_hi = F(n) / (2 * pi_hi), F(n + 1) / (2 * pi_lo)
    A_lo, B_hi = 2 * k / pi_hi**2, F(16)
    C_hi = B_hi + (F(n) / (2 * pi_lo))**2 / (4 * A_lo)
    y_leaf = t * k / (2 * n)
    check("leaf height: strip", y_leaf, b0 / 2)
    check("leaf height: chirp", y_leaf, t * D_lo / (4 * C_hi))
    check("leaf height: endpoint", y_leaf,
          2 * k / (8 * (F(n, 2) + t * D_hi)))
    check("leaf height: quadratic endpoint cost", y_leaf**2, k / 64)
    beta_leaf = 420 * pi_hi / (361 * n**2)
    eta_leaf = [t * D_lo * y_leaf / 2, k, A_lo * rho**2,
                F(1) / (2 * pi_hi) * rho**2 / 8]
    for j, eta in enumerate(eta_leaf):
        check(f"leaf first-charge drop versus error branch {j}", 2 * beta_leaf, eta)
    check("leaf outgoing patch", beta_leaf, (k - c) * chi_lo)
    check("leaf charge cutoff", 2, t * D_lo)

    # Central vertex: no outgoing-message patch is imposed at the final root.
    d = 30_000_001
    D_lo, D_hi = F(d) / (2 * pi_hi), F(d + 1) / (2 * pi_lo)
    A_lo = F(d) * c / pi_hi**2
    C_hi = F(d) + (1 / pi_lo)**2 / (4 * A_lo)
    y_center = delta_lo / 2
    check("center height: chirp", y_center, t * D_lo / (4 * C_hi))
    check("center height: endpoint", y_center,
          F(d) * c / (8 * (1 + t * D_hi)))
    check("center height: quadratic endpoint cost", y_center**2, c / 8)
    beta_center = 420 * pi_hi * d / (361 * (d**2 + 4))
    eta_center = [t * D_lo * y_center / 2, F(d) * c / 2,
                  A_lo * rho**2, F(d) / (2 * pi_hi) * rho**2 / 8]
    for j, eta in enumerate(eta_center):
        check(f"center first-charge drop versus error branch {j}",
              2 * beta_center, eta)
    check("center charge cutoff", 2, t * D_lo)
    check("star lies outside the old summed criterion",
          F(1, 2**25), F(d, d**2 + 4))
    check("center cannot pay any outgoing patch",
          k * chi_hi, 420 * pi_lo * d / (361 * (d**2 + 4)))

    star = {
        "central_degree": d,
        "central_power": 2,
        "leaf_power": n,
        "leaf_decay_budget": str(c),
        "center_upper_2beta_over_lower_eta": float(2 * beta_center / min(eta_center)),
        "leaf_upper_2beta_over_lower_eta": float(2 * beta_leaf / min(eta_leaf)),
    }
    return checks, star


def main():
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=repo / "experiments/actual_all_circle_directed_volume_results.json",
        help="JSON output path; the default is inferred from this script's repository",
    )
    args = parser.parse_args()
    inequalities, star = rational_checks()
    pairings = pairing_checks()
    note = repo / "notes/actual_all_circle_directed_volume.md"
    result = {
        "scope": (
            "Exact rational constant comparisons and original endpoint-pairing identities. "
            "No quantum finite sum, asymptotic limit, or geometric completion is numerically tested."
        ),
        "uniform_corollary": {
            "minimum_abs_power": 2**27,
            "alternative_minimum_degree": 2**28,
            "all_degrees": "Symbolic inequalities (49)-(53b); no degree scan.",
        },
        "star": star,
        "rational_checks": inequalities,
        "pairing_checks": pairings,
        "pairing_scope": (
            "The generator identities imply every even stack of odd turned leaves has "
            "the through pairing and no internal component. This does not identify knot types."
        ),
        "sources": {
            "experiments/audit_actual_all_circle_directed_volume.py":
                hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "notes/actual_all_circle_directed_volume.md":
                hashlib.sha256(note.read_bytes()).hexdigest(),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"rational_checks": len(inequalities),
                      "pairing_checks": len(pairings), "output": str(args.output)}))


if __name__ == "__main__":
    main()
