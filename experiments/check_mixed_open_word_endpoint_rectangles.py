#!/usr/bin/env python3
"""Extract exact coordinate inclusions from already validated endpoint disks."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_open_word_endpoint_rectangles.md"
RECTANGLES = [
    [[".376", ".438", "-.019", ".037"],
     [".278", ".391", "-.072", ".021"],
     [".218", ".242", ".049", ".077"]],
    [[".333", ".363", "-.051", "-.019"],
     [".246", ".350", "-.108", "-.020"],
     [".217", ".234", ".027", ".045"]],
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_disk(center, radius, target):
    x, y = map(F, center)
    a, b, c, d = map(F, target)
    return min(x-radius-a, b-x-radius, y-radius-c, d-y-radius) > 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-open-word-endpoint-rectangles.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps = {}

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        assert path not in deps or deps[path] == digest, path
        deps[path] = digest
        return digest

    def pair(stem, proof, script):
        a = "repro/results/research-"+stem+".json"
        b = "repro/results/research-"+stem+"-replay.json"
        author = json.loads((ROOT/a).read_text())
        replay = json.loads((ROOT/b).read_text())
        bind(a)
        bind(b)
        assert author["status"] == replay["status"] == "passed"
        assert replay["input_sha256"] == deps[a]
        for record in (author, replay):
            bind(proof, record["proof_sha256"])
            bind(script, record["script_sha256"])
            for p, digest in record["dependencies_sha256"].items():
                bind(p, digest)
        return author, replay

    author, replay = pair("mixed-open-word-critical-localization",
        "notes/research_mixed_open_word_critical_localization.md",
        "experiments/certify_mixed_open_word_critical_localization.py")
    pair("mixed-endpoint-cap-rectangle",
        "notes/research_mixed_endpoint_cap_rectangle.md",
        "experiments/certify_mixed_endpoint_cap_rectangle.py")
    assert author["domains"] == replay["domains"]
    assert [(d["epsilon"], d["neighbor_epsilon"]) for d in author["domains"]] == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    total_leaves, total_excluded, total_visits = 0, 0, 0
    for domain in author["domains"]:
        eps = domain["epsilon"]
        stack = [[(F(-1), F(1)), (F(-1), F(1))]]
        cursor, leaves, excluded = 0, 0, 0
        while stack:
            box = stack.pop()
            node = domain["tree"][cursor]
            cursor += 1
            if node[0] == "S":
                assert len(node) == 2 and type(node[1]) is int and node[1] in (0, 1)
                axis = node[1]
                lo, hi = box[axis]
                mid = (lo+hi)/2
                for interval in ((lo, mid), (mid, hi)):
                    child = list(box)
                    child[axis] = interval
                    stack.append(child)
            elif node[0] == "X":
                assert node == ["X"]
                minimum_norm = sum(min(abs(a), abs(b))**2 if a*b > 0 else F(0)
                                   for a, b in box)
                assert minimum_norm > 1
                excluded += 1
            else:
                assert node[0] == "L" and len(node) == 2
                witness = node[1]
                radius = F(witness["radius"])
                assert radius > 0 and len(witness["centers"]) == 3
                assert all(check_disk(c, radius, rectangle) for c, rectangle in
                           zip(witness["centers"], RECTANGLES[eps]))
                leaves += 1
        assert cursor == len(domain["tree"])
        assert leaves == domain["leaves"] and excluded == domain["excluded"]
        total_leaves += leaves
        total_excluded += excluded
        total_visits += cursor
    assert (total_leaves, total_excluded, total_visits) == (5258, 233, 10978)
    assert (author["leaves"], author["excluded"], author["visits"]) == (
        total_leaves, total_excluded, total_visits)
    assert [v["epsilon"] for v in author["one_vertex"]] == [0, 1]
    for eps, one in enumerate(author["one_vertex"]):
        w = one["witness"]
        assert w == replay["one_vertex"][eps]["witness"]
        radius = F(w["radius"])
        assert radius > 0 and len(w["centers"]) == 2
        assert check_disk(w["centers"][0], radius, RECTANGLES[eps][0])
        assert check_disk(w["centers"][0], radius, RECTANGLES[eps][1])
        assert check_disk(w["centers"][1], radius, RECTANGLES[eps][2])
    cap = list(map(F, [".27", ".49", "-.055", ".04"]))
    for row in RECTANGLES:
        e = list(map(F, row[0]))
        assert cap[0] < e[0] < e[1] < cap[1]
        assert cap[2] < e[2] < e[3] < cap[3]
        t = list(map(F, row[1]))
        assert F(1, 2) < cap[0]+t[0] < cap[1]+t[1] < 1
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/p) == digest for p, digest in deps.items())
    result = dict(status="passed", arithmetic="exact rational",
        endpoint_maps=4, endpoint_witnesses=total_leaves,
        excluded_boxes=total_excluded, tree_nodes=total_visits,
        one_vertex_witnesses=2, rectangles=RECTANGLES,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope="Exact inclusions of existing validated disks; no new roots, source bounds or global contour theorem.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", total_leaves, "endpoint disks and 2 one-vertex disks;",
          total_visits, "tree nodes;", len(deps), "current bindings")


if __name__ == "__main__":
    main()
