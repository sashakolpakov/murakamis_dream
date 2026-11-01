#!/usr/bin/env python3
"""Replay the exact input certificates and finite protected-sum constructions.

The two interval certificates establish properties of the seventeen-region
input. The topology checks below construct a finite sequence of tetrahedral
attachments and check that the four possible failed balance regions survive.
The general closure proof, its analytic inputs, and its volume conclusion
remain the written arguments of Appendix Q.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"


def check_sphere(regions: list[tuple[int, int, int, int]],
                 protected: set[int]) -> dict[str, int]:
    triangles = [t for x, b, c, y in regions
                 for t in ((x, b, y), (x, y, c))]
    assert all(len(set(q)) == 4 for q in regions)
    assert len({tuple(sorted(t)) for t in triangles}) == len(triangles)
    vertices = set().union(*(set(t) for t in triangles))
    edge_faces = defaultdict(list)
    links = {v: defaultdict(set) for v in vertices}
    for i, t in enumerate(triangles):
        for j, v in enumerate(t):
            a, b = t[(j + 1) % 3], t[(j + 2) % 3]
            links[v][a].add(b)
            links[v][b].add(a)
            edge_faces[tuple(sorted((v, a)))].append(i)
    assert all(len(fs) == 2 for fs in edge_faces.values())
    # A connected cyclic link at every vertex rules out pinched surfaces.
    for link in links.values():
        assert all(len(neighbors) == 2 for neighbors in link.values())
        todo = [next(iter(link))]
        reached = set()
        while todo:
            v = todo.pop()
            if v not in reached:
                reached.add(v)
                todo.extend(link[v] - reached)
        assert reached == set(link)
    adjacent = defaultdict(set)
    for i, j in edge_faces.values():
        adjacent[i].add(j)
        adjacent[j].add(i)
    todo, reached = [0], set()
    while todo:
        i = todo.pop()
        if i not in reached:
            reached.add(i)
            todo.extend(adjacent[i] - reached)
    assert len(reached) == len(triangles)
    assert len(vertices) - len(edge_faces) + len(triangles) == 2
    matching = [tuple(sorted((q[0], q[3]))) for q in regions]
    assert len(set(matching)) == len(regions)
    for e, edge in enumerate(matching):
        assert set(edge_faces[edge]) == {2 * e, 2 * e + 1}
    assert tuple(sorted(protected)) in edge_faces
    assert tuple(sorted(protected)) not in matching
    assert len(vertices - protected) == len(regions)
    return {"vertices": len(vertices), "triangles": len(triangles),
            "edges": len(edge_faces), "regions": len(regions),
            "ordinary_targets": len(vertices - protected)}


def attach_tetrahedron(regions: list[tuple[int, int, int, int]],
                       index: int, protected: set[int]) -> int:
    x, b, c, y = regions[index]
    assert x in protected and y not in protected
    assert (b in protected) != (c in protected)
    fresh = 1 + max(v for q in regions for v in q)
    if b in protected:
        # Existing quartet (u,v,c,B), new input (u,a,v,B).
        regions[index] = (x, fresh, c, y)
        regions.append((b, y, x, fresh))
    else:
        # Existing quartet (u,a,v,B), new input (u,v,c,B).
        regions[index] = (x, b, fresh, y)
        regions.append((c, x, y, fresh))
    return len(regions) - 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attachments", type=int, default=8,
                        help="Number of finite tetrahedral attachments to check.")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.attachments < 1:
        parser.error("--attachments must be positive")
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    jobs = [
        ("audit_actual_sector_cover.py", "sector-cover.json"),
        ("audit_actual_shared_radius_anchor_obstruction.py", "anchor-obstruction.json"),
    ]
    for script, result in jobs:
        completed = subprocess.run(
            [sys.executable, str(EXPERIMENTS / script), "--output", str(out / result)],
            cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out / (result + ".log")).write_text(completed.stdout)
        if completed.returncode:
            raise SystemExit(completed.stdout)
    cover_path = EXPERIMENTS / "actual_sector_cover_certificate.json"
    obstruction_path = EXPERIMENTS / "actual_shared_radius_anchor_obstruction_certificate.json"
    cover = json.loads(cover_path.read_text())
    obstruction = json.loads(obstruction_path.read_text())
    assert cover["ports"] == obstruction["ports"]
    assert cover["protected"] == obstruction["protected"] == [0, 16]
    protected = set(cover["protected"])
    candidates = set(obstruction["spectator_mixed_ports"]) | {obstruction["anchor"]}
    assert candidates == {2, 4, 7, 12}
    regions = list(map(tuple, cover["ports"]))
    original = list(regions)
    assert regions[15] == (16, 14, 0, 17)
    stages = [{"attachments": 0, **check_sphere(regions, protected)}]
    join = 15
    for n in range(1, args.attachments + 1):
        assert join not in candidates
        join = attach_tetrahedron(regions, join, protected)
        assert all(regions[e] == original[e] for e in candidates)
        counts = check_sphere(regions, protected)
        assert counts["regions"] == 17 + n
        stages.append({"attachments": n, **counts})
    inputs = [Path(__file__), cover_path, obstruction_path,
              EXPERIMENTS / "audit_actual_original_marked_face_coefficient.py",
              *(EXPERIMENTS / name for name, _ in jobs)]
    report = {
        "scope": "Exact input certificates and finite simple-sphere constructions. The general analytic, geometric, and volume implications remain written proofs.",
        "protected_vertices": sorted(protected),
        "retained_possible_balance_failure_regions": sorted(candidates),
        "initial_attachment_region": 15,
        "stages": stages,
        "final_ordered_quartets": regions,
        "input_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in inputs},
        "result": "Both interval certificates and every listed finite incidence check completed.",
    }
    (out / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Replayed both input certificates; checked {args.attachments} attachments.")
    print(f"Final sphere: {len(regions)} regions; possible failed balance regions retained.")
    print(f"Report: {out / 'summary.json'}")


if __name__ == "__main__":
    main()
