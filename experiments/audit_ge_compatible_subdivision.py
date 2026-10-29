#!/usr/bin/env python3
"""Exact independent stress test of compatible regular refinement.

The test covers arbitrary affine identifications of opposite cube faces.
It checks every refinement and the final tetrahedra, rather than assuming
that nonzero compatible heights can be chosen generic in one step.
These finite checks audit the construction; they are not its general proof.
"""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path

import sympy as sp


VERTICES = tuple(product((0, 1), repeat=3))
VERTEX_ID = {p: i for i, p in enumerate(VERTICES)}
FULL = tuple(range(8))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


@lru_cache(None)
def facets(cell):
    result = set()
    for a, b, c in combinations(cell, 3):
        normal = cross(sub(VERTICES[b], VERTICES[a]),
                       sub(VERTICES[c], VERTICES[a]))
        if not any(normal):
            continue
        values = {v: dot(normal, sub(VERTICES[v], VERTICES[a])) for v in cell}
        if min(values.values()) < 0 < max(values.values()):
            continue
        result.add(tuple(v for v in cell if values[v] == 0))
    return tuple(sorted(result))


@lru_cache(None)
def bases(cell):
    result = []
    for base in combinations(cell, 4):
        matrix = sp.Matrix([[1, *VERTICES[v]] for v in base])
        if matrix.det():
            inverse = matrix.inv()
            weights = tuple(tuple(Fraction(t) for t in
                            (sp.Matrix([[1, *VERTICES[v]]])*inverse)) for v in cell)
            result.append((base, weights))
    assert result
    return tuple(result)


@lru_cache(None)
def dependencies(face):
    matrix = sp.Matrix([[1, *VERTICES[v]] for v in face]).T
    assert matrix.rank() == 3
    return tuple(tuple(t) for t in matrix.nullspace())


def boundary_maps(options):
    maps = {}
    for axis, option in enumerate(options):
        other = [i for i in range(3) if i != axis]
        for vertex, p in enumerate(VERTICES):
            if p[axis] != 0:
                continue
            u, v = (p[i] for i in other)
            if option & 4:
                u, v = v, u
            if option & 1:
                u = 1-u
            if option & 2:
                v = 1-v
            target = list(p)
            target[axis] = 1
            target[other[0]], target[other[1]] = u, v
            maps[(axis, vertex)] = VERTEX_ID[tuple(target)]
    return maps


def paired_faces(cells, maps):
    occurrences = defaultdict(list)
    for i, cell in enumerate(cells):
        for face in facets(cell):
            occurrences[face].append(i)
    pairs, used = [], set()
    for face, owners in sorted(occurrences.items()):
        if len(owners) == 2:
            pairs.append((owners[0], face, owners[1], face))
            used.add(face)
        else:
            assert len(owners) == 1
    for face, owners in sorted(occurrences.items()):
        if face in used:
            continue
        axes = [axis for axis in range(3)
                if all(VERTICES[v][axis] == 0 for v in face)]
        if not axes:
            continue
        assert len(axes) == 1
        mapped = tuple(maps[(axes[0], v)] for v in face)
        target = tuple(sorted(mapped))
        assert len(occurrences[target]) == 1
        pairs.append((owners[0], face, occurrences[target][0], mapped))
        used.update((face, target))
    assert used == set(occurrences)
    assert sum(len(facets(c)) for c in cells) == 2*len(pairs)
    return pairs


def compatible_heights(cells, pairs):
    gauges = [set(bases(cell)[0][0]) for cell in cells]
    variables = [(i, v) for i, cell in enumerate(cells) for v in cell
                 if v not in gauges[i]]
    index = {key: i for i, key in enumerate(variables)}
    rows = []
    for i, face, j, mapped in pairs:
        for dependency in dependencies(face):
            row = [sp.S.Zero]*len(variables)
            for v, w, coefficient in zip(face, mapped, dependency):
                if (i, v) in index:
                    row[index[i, v]] += coefficient
                if (j, w) in index:
                    row[index[j, w]] -= coefficient
            rows.append(row)
    matrix = sp.Matrix(rows) if rows else sp.zeros(0, len(variables))
    nullspace = matrix.nullspace()
    bound = sp.Rational(sum(len(facets(c))-4 for c in cells), 2)
    assert len(nullspace) >= bound
    assert nullspace
    heights = [{v: Fraction(0) for v in cell} for cell in cells]
    for key, value in zip(variables, nullspace[0]):
        heights[key[0]][key[1]] = Fraction(value)
    assert any(any(h.values()) for h in heights)
    return heights, len(nullspace), str(bound)


def lower_cells(cell, heights):
    result = set()
    for base, weights in bases(cell):
        values = [sum(t*heights[v] for t, v in zip(row, base)) for row in weights]
        if all(value <= heights[v] for value, v in zip(values, cell)):
            contact = tuple(v for value, v in zip(values, cell) if value == heights[v])
            result.add(contact)
    assert result
    return sorted(result)


def audit(options):
    maps, cells, stages = boundary_maps(options), [FULL], []
    while any(len(c) != 4 for c in cells):
        pairs = paired_faces(cells, maps)
        heights, dimension, bound = compatible_heights(cells, pairs)
        updated = [piece for cell, h in zip(cells, heights) for piece in lower_cells(cell, h)]
        assert len(updated) > len(cells)
        assert len(updated) <= len(bases(FULL))
        stages.append({"cells_before": len(cells), "cells_after": len(updated),
                       "compatible_dimension": dimension, "dimension_bound": bound})
        cells = updated
        # This validates that every matched boundary subdivision is identical.
        paired_faces(cells, maps)
    determinants = [abs(sp.Matrix([sub(VERTICES[v], VERTICES[cell[0]])
                                  for v in cell[1:]]).det()) for cell in cells]
    assert all(d > 0 for d in determinants)
    assert sum(determinants) == 6
    return {"opposite_face_maps": options, "stages": stages,
            "tetrahedra": len(cells), "total_volume": "1",
            "original_vertices_only": True, "all_face_pairs_compatible": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=512)
    args = parser.parse_args()
    records = []
    for options in list(product(range(8), repeat=3))[:args.limit]:
        records.append(audit(options))
        if len(records) % 64 == 0:
            print(json.dumps({"checked": len(records)}), flush=True)
    result = {"source": "Ge, arXiv:2609.27635v1, Sections 2--4",
              "scope": "Exact stress tests; the uniform argument is audited separately.",
              "systems_checked": len(records),
              "tetrahedron_counts": dict(Counter(r["tetrahedra"] for r in records)),
              "max_refinements": max(len(r["stages"]) for r in records),
              "records": records}
    Path(__file__).with_name("ge_compatible_subdivision_results.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "records"}), flush=True)


if __name__ == "__main__":
    main()
