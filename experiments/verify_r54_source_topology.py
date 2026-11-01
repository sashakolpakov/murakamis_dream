#!/usr/bin/env python3
"""Check the recorded 54-region oriented sphere, matching, and source mark.

This is an incidence check, not a capacity estimate or knot-parity proof.
It uses only the Python standard library and writes JSON when --output is
supplied. Paths default relative to this script, not the working directory.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


if not __debug__:
    raise SystemExit("Assertions must be enabled; do not run with -O.")


def connected(vertices, edges):
    vertices = set(vertices)
    assert vertices
    adjacency = {v: set() for v in vertices}
    for a, b in edges:
        assert a in vertices and b in vertices and a != b
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {min(vertices)}
    pending = list(seen)
    while pending:
        for neighbor in adjacency[pending.pop()]:
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append(neighbor)
    return seen == vertices


def cyclic_equal(face, expected):
    return any(
        tuple(face) == tuple(expected[k:] + expected[:k])
        for k in range(len(expected))
    )


def verify_data(certificate):
    source = certificate["source"]
    faces = [tuple(face) for face in source["faces"]]
    assert len(faces) == 108
    assert all(
        len(face) == 3
        and len(set(face)) == 3
        and all(type(v) is int for v in face)
        for face in faces
    )
    assert len({tuple(sorted(face)) for face in faces}) == 108
    vertices = {v for face in faces for v in face}
    assert vertices == set(range(56))
    assert source["vertices"] == 56

    edge_occurrences = defaultdict(list)
    for i, face in enumerate(faces):
        for j in range(3):
            a, b = face[j], face[(j + 1) % 3]
            edge_occurrences[tuple(sorted((a, b)))].append((i, a, b))
    assert len(edge_occurrences) == 162
    for occurrences in edge_occurrences.values():
        assert len(occurrences) == 2
        _, a, b = occurrences[0]
        _, c, d = occurrences[1]
        assert (a, b) == (d, c), "The two incident orientations must oppose."
    assert connected(vertices, edge_occurrences)

    # Degree two alone permits several link circles. Connectedness is
    # checked separately, so each vertex has one disk neighborhood.
    for vertex in vertices:
        link_edges = [
            tuple(v for v in face if v != vertex)
            for face in faces
            if vertex in face
        ]
        assert len(link_edges) >= 3
        assert len({tuple(sorted(edge)) for edge in link_edges}) == len(link_edges)
        degree = Counter(v for edge in link_edges for v in edge)
        assert all(value == 2 for value in degree.values())
        assert connected(degree, link_edges)
    euler = len(vertices) - len(edge_occurrences) + len(faces)
    assert euler == 2

    # The checks above give a connected closed oriented triangulated
    # surface; Euler characteristic two identifies it as a sphere.
    matching = source["matching_faces"]
    quartets = source["ports"]
    assert len(matching) == len(quartets) == 54
    assert all(
        len(pair) == 2 and pair[0] != pair[1]
        and all(type(i) is int and 0 <= i < 108 for i in pair)
        for pair in matching
    )
    assert sorted(i for pair in matching for i in pair) == list(range(108))
    matched_edges = set()
    face_owner = {}
    for region, (pair, quartet) in enumerate(zip(matching, quartets)):
        i, j = pair
        assert len(quartet) == len(set(quartet)) == 4
        x, b, c, y = quartet
        assert cyclic_equal(faces[i], [x, b, y])
        assert cyclic_equal(faces[j], [x, y, c])
        assert set(faces[i]) & set(faces[j]) == {x, y}
        edge = tuple(sorted((x, y)))
        assert edge not in matched_edges
        assert {row[0] for row in edge_occurrences[edge]} == {i, j}
        matched_edges.add(edge)
        face_owner[i] = face_owner[j] = region
    assert len(matched_edges) == 54

    strand_edges = set(edge_occurrences) - matched_edges
    assert len(strand_edges) == 108
    region_edges = []
    for edge in strand_edges:
        first, second = edge_occurrences[edge]
        a, b = face_owner[first[0]], face_owner[second[0]]
        assert a != b
        region_edges.append((a, b))
    assert connected(range(54), region_edges)

    protected = tuple(sorted(source["protected"]))
    assert protected == (29, 50)
    assert protected in strand_edges
    assert protected not in matched_edges
    assert set(certificate["ordinary"]) == vertices - set(protected)
    assert len(certificate["ordinary"]) == 54
    assert certificate["anchor"] == 32
    assert quartets[32] == [0, 50, 16, 29]
    assert certificate["overloaded_face"] == 16
    assert certificate["overloaded_face"] not in protected
    assert len(certificate["tags"]) == 54
    assert [
        (i, label) for i, label in enumerate(certificate["tags"]) if label != "C"
    ] == [(32, "L")]

    return {
        "scope": "Oriented sphere, matching, ordered source arguments, and mark; no capacity or knot-parity conclusion.",
        "assertions_enabled": True,
        "vertices": 56,
        "edges": 162,
        "faces": 108,
        "each_edge_has_two_oppositely_oriented_triangles": True,
        "connected_surface": True,
        "all_vertex_links_single_cycles": True,
        "euler_characteristic": euler,
        "matching_regions": 54,
        "each_triangle_matched_once": True,
        "ordered_quartets_match_oriented_faces": True,
        "strand_edges": len(strand_edges),
        "connected_region_graph": True,
        "protected_mark": list(protected),
        "protected_mark_is_nonmatching_edge": True,
        "selected_region": 32,
        "selected_source_arguments_x_b_c_y": quartets[32],
        "selected_overloaded_ordinary_face": 16,
    }


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--certificate", type=Path,
        default=root / "experiments/actual_singleton_sector_obstruction_certificate.json",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    result = verify_data(json.loads(raw))
    result["certificate"] = args.certificate.name
    result["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
    result["verifier_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    serialized = json.dumps(result, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
