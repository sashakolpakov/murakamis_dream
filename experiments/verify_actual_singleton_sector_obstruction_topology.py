#!/usr/bin/env python3
"""Exact incidence and knot-parity check; no capacity or quantum estimate."""
from pathlib import Path
from collections import defaultdict, Counter
import hashlib
import json
import argparse

if not __debug__:
    raise SystemExit("Do not run with -O")



def cyclic(a, b):
    return any(tuple(a) == tuple(b[k:] + b[:k]) for k in range(len(b)))


def edge_rows(faces):
    result = defaultdict(list)
    for i, f in enumerate(faces):
        for j in range(3):
            a, b = f[j], f[(j + 1) % 3]
            result[tuple(sorted((a, b)))].append((i, a, b))
    return result


def connected(vertices, edges):
    vertices = set(vertices)
    if not vertices:
        return True
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        for b in adj[stack.pop()]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    return seen == vertices


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def root(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def join(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        self.parent[b] = a
        return True


def main():
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, default=repo/'experiments/actual_singleton_sector_obstruction_certificate.json')
    parser.add_argument('--output', type=Path, default=repo/'experiments/actual_singleton_sector_obstruction_topology_results.json')
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    cert = json.loads(raw)
    source = cert["source"]
    faces = [tuple(f) for f in source["faces"]]
    edges = edge_rows(faces)
    vertices = set(v for f in faces for v in f)
    assert len(vertices) == 56
    assert len(faces) == len(set(tuple(sorted(f)) for f in faces)) == 108
    assert all(len(set(f)) == 3 for f in faces)
    assert all(len(rows) == 2 and rows[0][1:] == rows[1][1:][::-1]
               for rows in edges.values())
    assert connected(vertices, edges)
    assert len(vertices) - len(edges) + len(faces) == 2
    # Independently verify the closed 2-manifold condition at every vertex.
    for v in vertices:
        link = [tuple(x for x in f if x != v) for f in faces if v in f]
        degree = Counter(x for e in link for x in e)
        assert set(degree.values()) == {2}
        assert connected(degree, link)

    # Replay the oriented stellar subdivisions and legal diagonal flips.
    replay = [(0, 1, 2), (0, 3, 1), (1, 3, 2), (0, 2, 3)]
    counts = Counter()
    for operation in cert["sphere_history"]:
        counts[operation["kind"]] += 1
        if operation["kind"] == "stellar":
            i, w = operation["index"], operation["new"]
            assert replay[i] == tuple(operation["old"])
            assert w not in {v for f in replay for v in f}
            a, b, c = replay.pop(i)
            replay.extend([(a, b, w), (b, c, w), (c, a, w)])
        else:
            assert operation["kind"] == "flip"
            i, j = operation["i"], operation["j"]
            a, b, c, d = [operation[k] for k in "abcd"]
            assert cyclic(replay[i], [a, b, c])
            assert cyclic(replay[j], [b, a, d])
            assert len({a, b, c, d}) == 4
            assert tuple(sorted((c, d))) not in edge_rows(replay)
            replay[i], replay[j] = (c, a, d), (d, b, c)
    assert replay == faces

    matching = source["matching_faces"]
    quartets = source["ports"]
    R = len(quartets)
    assert R == 54 and sorted(i for pair in matching for i in pair) == list(range(108))
    matched_edges = set()
    terminals = defaultdict(list)
    for e, ((i, j), quartet) in enumerate(zip(matching, quartets)):
        x, b, c, y = quartet
        assert len(set(quartet)) == 4
        assert cyclic(faces[i], [x, b, y])
        assert cyclic(faces[j], [x, y, c])
        assert set(faces[i]) & set(faces[j]) == {x, y}
        matched_edges.add(tuple(sorted((x, y))))
        # C0=x/c, C1=x/b, C2=b/y, C3=c/y, as in the disk maps.
        for t, side in enumerate([(x, c), (x, b), (b, y), (c, y)]):
            terminals[tuple(sorted(side))].append(4 * e + t)
    assert len(matched_edges) == R
    main_edges = set(edges) - matched_edges
    assert set(terminals) == main_edges
    assert all(len(ts) == 2 for ts in terminals.values())
    mark = tuple(sorted(source["protected"]))
    assert mark == (29, 50) and mark in main_edges
    assert connected(range(R), [(a // 4, b // 4) for a, b in terminals.values()])

    def strand_components(odd):
        dsu = DSU(4 * R)
        for a, b in terminals.values():
            dsu.join(a, b)
        for e in range(R):
            pairs = [(0, 2), (1, 3)] if e in odd else [(0, 1), (2, 3)]
            for a, b in pairs:
                dsu.join(4 * e + a, 4 * e + b)
        return dsu

    original = strand_components(set())
    roots = sorted({original.root(i) for i in range(4 * R)})
    rid = {r: i for i, r in enumerate(roots)}
    tree = DSU(len(roots))
    odd = []
    for e in range(R):
        a = rid[original.root(4 * e)]
        b = rid[original.root(4 * e + 2)]
        if tree.join(a, b):
            odd.append(e)
    assert len(odd) == len(roots) - 1
    final = strand_components(set(odd))
    assert len({final.root(i) for i in range(4 * R)}) == 1
    assert len(cert["tags"]) == R
    assert [(i, t) for i, t in enumerate(cert["tags"]) if t != "C"] == [(32, "L")]
    assert quartets[32] == [0, 50, 16, 29]
    assert cert["overloaded_face"] == 16 not in source["protected"]
    assert set([quartets[32][0], quartets[32][1], quartets[32][3]]) - set(mark) == {0}

    result = {
        "scope": "Exact oriented topology, original frame and knot-parity check only; no capacity claim.",
        "input": args.certificate.name,
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "vertices": len(vertices), "edges": len(edges), "faces": len(faces),
        "Euler_characteristic": 2, "all_vertex_links_cycles": True,
        "oriented_history_counts": dict(counts),
        "original_matching_regions": R, "main_edges": len(main_edges),
        "mark": list(mark),
        "mark_terminal_occurrences": [
            {"crossing": t // 4, "C_label": t % 4} for t in terminals[mark]],
        "untwisted_main_components": len(roots),
        "odd_crossings_for_one_knot": odd,
        "resulting_main_components": 1,
        "selected_crossing": 32, "selected_label": "LEFT",
        "selected_ordered_quartet": quartets[32],
        "overloaded_ordinary_face": 16,
        "retained_supported_triangle": [0],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "verified", "main_components": 1, "crossings": R, "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
