#!/usr/bin/env python3
"""Exact conversion of the published R54 triangle witness to original four-loads.

This checks the feasible flow and every retained CROSS split.  Entropy interval
bounds are the separately proved public certificate; this script does not
estimate a signed coefficient or a knot invariant.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import argparse
import hashlib
import json


def verify(path):
    data = json.loads(path.read_text())
    source = data["source"]
    quartets = source["ports"]
    ordinary = set(data["ordinary"])
    protected = set(source["protected"])
    anchor = data["anchor"]
    vals = [F(*v["value"]) for v in data["variables"]]
    lam = vals[data["lambda_variable"]]
    assert quartets[anchor] == [0, 50, 16, 29]
    assert protected == {29, 50} and 0 < lam < 1
    rows = {}
    for row in data["rows"]:
        key = (row["crossing"], row["side"])
        assert key not in rows
        rows[key] = dict(zip(row["faces"],
                            (vals[i] for i in row["variables"])))
    loads = defaultdict(F)
    records = []
    for e, (x, b, c, y) in enumerate(quartets):
        if e == anchor:
            u = lam / 2
            q = [u, F(0), 1-u, F(0)]
            assert rows[e, 0] == {x: u} and (e, 1) not in rows
            assert F(1, 2) < q[2] < 1
            record = {"crossing": e, "quartet": quartets[e],
                      "sector": "LEFT",
                      "load": list(map(str, q)),
                      "sharp_score": "0 exactly",
                      "endpoint_h": "-2 f(u)", "relative_g": "2 f(u)",
                      "envelope_h": "0"}
        else:
            left, right = rows[e, 0], rows[e, 1]
            assert set(left) == {x, b, y} - protected
            assert set(right) == {x, c, y} - protected
            A = [left.get(v, F(0)) for v in (x, b, y)]
            B = [right.get(v, F(0)) for v in (x, c, y)]
            assert min(A+B) >= 0
            assert sum(A) == sum(B) == F(1, 2)
            q = [A[0]+B[0], A[1], B[1], A[2]+B[2]]
            assert q[1] <= F(1, 2) and q[2] <= F(1, 2)
            s = A[0]
            lo = max(F(0), q[0]+q[2]-F(1, 2))
            hi = min(q[0], F(1, 2)-q[1])
            assert lo <= s <= hi
            assert A == [s, q[1], F(1, 2)-q[1]-s]
            assert B == [q[0]-s, q[2],
                         F(1, 2)-q[2]-q[0]+s]
            record = {"crossing": e, "quartet": quartets[e],
                      "sector": "CROSS", "load": list(map(str, q)),
                      "first_triangle": list(map(str, A)),
                      "second_triangle": list(map(str, B)),
                      "split": str(s), "split_interval": [str(lo), str(hi)]}
        assert sum(q) == 1 and min(q) >= 0
        for face, value in zip(quartets[e], q):
            assert face not in protected or value == 0
            loads[face] += value
        records.append(record)
    assert all(loads[v] == 1 for v in ordinary)
    assert all(loads[v] == 0 for v in protected)
    assert set(loads) == ordinary | protected
    u = lam/2
    return {
        "certificate": str(path),
        "certificate_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "counts": {"crossings": len(quartets),
                   "retained_cross_splits": len(quartets)-1,
                   "ordinary_face_targets": len(ordinary),
                   "protected_face_targets": len(protected)},
        "lambda": str(lam), "selected_u": str(u),
        "unavoidable_positive_triangle_load_defect": str(F(1, 2)-u),
        "conclusion": "sum h_sharp >= the same certified dual entropy",
        "scope": "Exact flow/support transformation; no signed-sum lower bound.",
        "records": records
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=Path(
        "/private/tmp/murakamis_dream-publication/experiments/"
        "actual_singleton_sector_obstruction_certificate.json"))
    parser.add_argument("--output", type=Path, default=Path(
        "/private/tmp/md-endpoint-conditioned-singleton-flow-results.json"))
    args = parser.parse_args()
    result = verify(args.certificate)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "records"},
                     indent=2))
