#!/usr/bin/env python3
"""Compare full tree messages with independent root-grid/normal contractions.

This is a finite identity check, not a test of the asymptotic criterion.
The polynomial side uses canonical quotient multiplication. The original
edge-index contraction uses the generic spectral trace, and at the complete
root the explicit first-normal trace, including the crossing derivative.
All indices 0,...,N-1 and the paired edge weights are retained.

From the repository root, run:
    python3 experiments/audit_all_circle_local_message_recursion.py
The optional --repo and --output flags override the inferred repository and
default JSON path. The imported polynomial and trace routines are recorded
by source hash.
Formal independent vertex grid assignments test the algebraic identity;
the script does not assert that every assignment is a new physical diagram.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import mpmath as mp


def load_source(repo):
    path = repo / "experiments/audit_main_meridian_direct_fillings.py"
    spec = importlib.util.spec_from_file_location("direct_fillings", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, path


def case(mod, N, s, name, edges, powers):
    count = len(powers)
    adjacent = [[] for _ in range(count)]
    for ei, (v, w) in enumerate(edges):
        adjacent[v].append((w, ei))
        adjacent[w].append((v, ei))
    # Test constant normal channels together with both moving assignments.
    sigmas = [s if v % 3 == 0 else -s if v % 3 == 2 else mp.mpc(0)
              for v in range(count)]
    basis = [mod.newton(N, k) for k in range(N)]
    rel = [mod.relation(N, z) for z in sigmas]
    crossing = [mod.power_mod(mod.physical_crossing(N, sigmas[v]),
                             powers[v], rel[v]) for v in range(count)]
    q = mp.exp(mp.j * mp.pi / N)
    H = mp.mpc(1) if s == 0 else mp.sin(mp.pi * s) / (N * mp.sin(mp.pi * s / N))
    paired = [mp.mpc(1)]
    for k in range(1, N):
        paired.append(paired[-1] * (1 - mp.sin(mp.pi * s / N)**2
                                   / mp.sin(mp.pi * k / N)**2))
    weights = []
    for ei in range(len(edges)):
        sign = (-1, 0, 1)[ei % 3]
        gamma = mp.exp(mp.j * mp.pi * sign * s*s / (2*N))
        weights.append([gamma * H / x for x in paired])

    @lru_cache(None)
    def original_vertex(v, indices):
        raw = mod.raw_product(N, indices)
        if sigmas[v] == 0:
            return mod.complete_first_normal(N, powers[v], raw)
        return mod.generic_spectral_trace(N, sigmas[v], powers[v], raw)

    def original_sum(allowed):
        terms = []
        for labels in itertools.product(allowed, repeat=len(edges)):
            value = mp.mpc(1)
            for ei, k in enumerate(labels):
                value *= weights[ei][k]
            for v in range(count):
                inds = tuple(labels[ei] for _, ei in adjacent[v])
                value *= original_vertex(v, inds)
            terms.append(value)
        return mp.fsum(terms)

    original = original_sum(range(N))
    low = original_sum(range((N - 1)//2 + 1))
    degree_checks = []

    def recursive(root):
        def visit(v, parent):
            raw = [mp.mpc(1)]
            for w, _ in adjacent[v]:
                if w != parent:
                    raw = mod.multiply(raw, visit(w, v))
            if parent is None:
                return mod.polynomial_trace(N, rel[v], crossing[v], raw)
            ei = next(e for w, e in adjacent[v] if w == parent)
            out = [mp.mpc(0)]
            for k in range(N):
                coefficient = mod.polynomial_trace(
                    N, rel[v], crossing[v], mod.multiply(raw, basis[k]))
                out = mod.add(out, mod.scale(basis[k], weights[ei][k]*coefficient))
            degree_checks.append(len(out) <= N)
            return out
        return visit(root, None)

    values = [recursive(root) for root in range(count)]
    errors = [mod.err(original, value) for value in values]
    return {
        "N": N, "main_parameter": mp.nstr(s, 20), "tree": name,
        "edges": edges, "powers": powers,
        "vertex_grid_parameters": [mp.nstr(x, 20) for x in sigmas],
        "full_index_states": N**len(edges),
        "root_choices": count,
        "max_relative_recursion_error": mp.nstr(max(errors), 15),
        "all_parent_degrees_below_N": all(degree_checks),
        "full_minus_low_relative": mp.nstr(mod.err(original, low), 15),
        "original_value": [mp.nstr(mp.re(original), 18), mp.nstr(mp.im(original), 18)]
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--output", type=Path)
    ap.add_argument("--digits", type=int, default=80)
    args = ap.parse_args()
    mp.mp.dps = args.digits
    args.repo = args.repo.resolve()
    if args.output is None:
        args.output = args.repo / "experiments/actual_local_tree_message_recursion_results.json"
    mod, source = load_source(args.repo)
    trees = [
        ("edge", [(0, 1)], [2, -6]),
        ("path", [(0, 1), (1, 2), (2, 3)], [2, -6, 0, 3]),
        ("star", [(0, 1), (0, 2), (0, 3)], [0, 2, -6, 3]),
        ("branched", [(0, 1), (1, 2), (1, 3), (3, 4)], [2, -6, 0, 3, -2]),
    ]
    params = [mp.mpc(0), mp.mpc("0.23", "0.11"), mp.mpc("0.72", "0.09")]
    records = [case(mod, N, s, name, edges, powers)
               for N in (2, 3, 4, 5) for s in params
               for name, edges, powers in trees]
    tolerance = mp.mpf(10)**(-args.digits//2)
    result = {
        "scope": "Finite full-index recursion versus independent spectral/full-normal contraction",
        "limits": "High-precision numerical identities; not an asymptotic or topological proof.",
        "digits": args.digits,
        "source": source.relative_to(args.repo).as_posix(),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": len(records),
        "root_choices": sum(r["root_choices"] for r in records),
        "max_relative_error": max((r["max_relative_recursion_error"] for r in records),
                                  key=mp.mpf),
        "all_degree_checks": all(r["all_parent_degrees_below_N"] for r in records),
        "high_channel_witness_cases": sum(mp.mpf(r["full_minus_low_relative"]) > tolerance
                                          for r in records),
        "all_identities_within_tolerance": all(
            mp.mpf(r["max_relative_recursion_error"]) < tolerance for r in records),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "cases", "root_choices", "max_relative_error", "all_degree_checks",
        "high_channel_witness_cases", "all_identities_within_tolerance")}, indent=2))
    if not (result["all_identities_within_tolerance"] and result["all_degree_checks"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
