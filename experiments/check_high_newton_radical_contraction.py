#!/usr/bin/env python3
"""Finite-level checks for the high Newton radical contraction.

The proofs for all levels are in the research note. This script independently
checks the normalization by polynomial division, and compares a four-vertex
network with its physical-evaluation matching expansion. Floating-point
checks are diagnostics, not replacements for those proofs.
"""

import argparse
from functools import lru_cache
import hashlib
import itertools
import json
from math import comb
from pathlib import Path

import mpmath as mp


def multiply(a, b):
    result = [mp.mpc(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def evaluate(a, x):
    return mp.polyval(list(reversed(a)), x)


def level_data(level):
    degree, half = level - 1, level // 2
    eta = (-1) ** degree
    roots = [2 * mp.cos((2 * a + 1) * mp.pi / level)
             for a in range(level)]
    sine = [2 * mp.sin(a * mp.pi / level) for a in range(level)]
    factorial = [mp.mpf(1)]
    for a in range(1, level):
        factorial.append(factorial[-1] * sine[a])
    newton = [[mp.mpf(1)]]
    for j in range(1, level):
        newton.append([x / sine[j] ** 2 for x in
                       multiply(newton[-1], [roots[j - 1], -1])])

    # Construct the monic defining polynomial independently of its
    # Chebyshev expression and of the divided-difference weights.
    defining = [mp.mpf(1)]
    for root in roots:
        defining = multiply(defining, [-root, 1])

    def remainder(polynomial):
        result = list(polynomial) + [mp.mpc(0)] * max(0, level - len(polynomial))
        for j in range(len(result) - 1, level - 1, -1):
            coefficient = result[j]
            for k in range(level + 1):
                result[j - level + k] -= coefficient * defining[k]
        return result[:level]

    def trace(polynomial):
        return eta * level ** 2 * remainder(polynomial)[degree]

    weights = [[mp.mpf(0) for _ in range(half)] for _ in range(half)]
    for r in range(half):
        for a in range(r + 1):
            weights[r][a] = ((-1) ** (r + a) * sine[2 * a + 1]
                             * factorial[r] ** 2
                             / (factorial[r - a] * factorial[r + a + 1]))
    gram = [[sum(weights[r][a] * weights[r][b] for r in range(half))
             for b in range(half)] for a in range(half)]
    return degree, half, roots, newton, remainder, trace, weights, gram


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=
                        "repro/results/research-high-newton-radical.json")
    args = parser.parse_args()
    mp.mp.dps = 100
    tolerance = mp.mpf("1e-65")
    largest = mp.mpf(0)
    counts = {"trace_basis": 0, "radical_products": 0,
              "weight_bounds": 0, "row_sums": 0,
              "radical_fourier_bounds": 0,
              "matching_terms": 0, "whole_networks": 0}

    def equal(left, right, label):
        nonlocal largest
        error = abs(left - right) / max(1, abs(left), abs(right))
        largest = max(largest, error)
        if error > tolerance:
            raise AssertionError((label, mp.nstr(error, 12)))

    for level in range(3, 15):
        degree, half, roots, newton, rem, trace, weights, gram = level_data(level)
        for r in range(half):
            # Expand the original polynomial under w=-z-z^{-1}
            # directly, independently of its physical Hermite data.
            fourier = [mp.mpc(0) for _ in range(2*degree + 1)]
            for k, coefficient in enumerate(newton[degree-r]):
                for h in range(k + 1):
                    fourier[degree + k - 2*h] += (
                        coefficient * (-1)**k * comb(k, h))
            assert sum(map(abs, fourier)) <= mp.sqrt(level-1) + tolerance
            counts["radical_fourier_bounds"] += 1
            for a in range(half):
                assert abs(weights[r][a]) <= 2 + tolerance
                counts["weight_bounds"] += 1
            equal(sum(weights[r]), int(r == 0), ("row sum", level, r))
            counts["row_sums"] += 1
            for power in range(level):
                polynomial = [mp.mpc(0)] * power + newton[degree - r]
                value = sum(weights[r][a] * roots[a] ** power
                            for a in range(half))
                equal(trace(polynomial), value, ("trace", level, r, power))
                counts["trace_basis"] += 1
            for s in range(half):
                residual = rem(multiply(newton[degree-r], newton[degree-s]))
                equal(max(map(abs, residual)), 0, ("nilpotence", level, r, s))
                counts["radical_products"] += 1

        if level > 8:
            continue
        edges = [(0, 1), (1, 2), (2, 3)]
        low = range(level - half)
        high = range(level - half, level)
        coupons = [[mp.mpf(1), mp.mpf(v + 1)/7 + mp.j/5, mp.mpf(1)/11]
                   for v in range(4)]
        values = [[evaluate(e, roots[a]) for e in newton] for a in range(half)]

        @lru_cache(None)
        def vertex_trace(vertex, indices):
            polynomial = coupons[vertex]
            for index in indices:
                polynomial = multiply(polynomial, newton[index])
            return trace(polynomial)

        def index_contraction(domains):
            total = mp.mpc(0)
            for indices in itertools.product(*domains):
                term = mp.mpc(1)
                for vertex in range(4):
                    incident = tuple(indices[k] for k, edge in enumerate(edges)
                                     if vertex in edge)
                    term *= vertex_trace(vertex, incident)
                total += term
            return total

        full = index_contraction([range(level)] * 3)
        matching_sum = mp.mpc(0)
        for mask in range(8):
            selected_edges = [k for k in range(3) if mask & (1 << k)]
            endpoints = [v for k in selected_edges for v in edges[k]]
            matching = len(endpoints) == len(set(endpoints))
            direct = index_contraction(
                [high if k in selected_edges else low for k in range(3)])
            if not matching:
                equal(direct, 0, ("overlap", level, mask))
                counts["matching_terms"] += 1
                continue
            removed = sorted(endpoints)
            remaining_edges = [k for k in range(3) if k not in selected_edges]
            evaluated = mp.mpc(0)
            for colors in itertools.product(range(half), repeat=len(removed)):
                color = dict(zip(removed, colors))
                for indices in itertools.product(low, repeat=len(remaining_edges)):
                    edge_index = dict(zip(remaining_edges, indices))
                    term = mp.mpc(1)
                    for k in selected_edges:
                        v, w = edges[k]
                        term *= gram[color[v]][color[w]]
                    for vertex in range(4):
                        incident = tuple(edge_index[k] for k in remaining_edges
                                         if vertex in edges[k])
                        if vertex in color:
                            a = color[vertex]
                            term *= evaluate(coupons[vertex], roots[a])
                            for j in incident:
                                term *= values[a][j]
                        else:
                            term *= vertex_trace(vertex, incident)
                    evaluated += term
            equal(direct, evaluated, ("physical matching", level, mask))
            counts["matching_terms"] += 1
            matching_sum += evaluated
        equal(full, matching_sum, ("whole network", level))
        counts["whole_networks"] += 1

    result = {
        "status": "passed",
        "scope": "finite-level numerical diagnostics; uniform proofs are in the note",
        "precision_digits": mp.mp.dps,
        "trace_levels": [3, 14],
        "four_vertex_network_levels": [3, 8],
        "counts": counts,
        "largest_scaled_residual": mp.nstr(largest, 20),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"passed {sum(counts.values())} finite-level checks; {output}")


if __name__ == "__main__":
    main()
