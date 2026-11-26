#!/usr/bin/env python3
"""Scalar raw-row and two-angle reference covers for both low targets."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as Q
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_both_low_raw_support.md"
PRIMITIVE = ROOT / "experiments/certify_mixed_all_endpoint_support.py"
spec = importlib.util.spec_from_file_location("endpoint_primitive", PRIMITIVE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
DEPS = [
    "notes/research_mixed_all_endpoint_support.md",
    "experiments/certify_mixed_all_endpoint_support.py",
    "repro/results/research-mixed-all-endpoint-support.json",
    "notes/research_mixed_boundary_strip_bounds.md",
    "notes/research_mixed_fourier_weight_continuation.md",
    "notes/research_mixed_type_three_window_strip.md",
    "notes/research_mixed_type_four_height_refinement.md",
]
SOURCES = {(0, 0): Q(".45"), (0, 1): Q(".63"),
           (1, 0): Q(".54"), (1, 1): Q(".72")}
PLANES = {(0, 0): Q(".54"), (0, 1): Q(".65"),
          (1, 0): Q(".65"), (1, 1): Q(".735")}
L = Q(1, 10)
SCALE = (L / Q("11/50"))**2
HEIGHTS = {0: [-Q(".03") * SCALE, Q(".02") * SCALE],
           1: [-Q(".057") * SCALE, Q(".014") * SCALE]}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ar(v):
    q = Q(v)
    return arb(q.numerator) / q.denominator


def decode(ad, dim):
    b = [Q(0), Q(1)] * dim
    for j, bit in enumerate(ad):
        k = 2 * (j % dim)
        t = (b[k] + b[k + 1]) / 2
        b[k + 1 - int(bit)] = t
    return b


def cover(cells):
    ads = sorted(cells)
    assert len(ads) == len(set(ads))
    assert all(not b.startswith(a) for a, b in zip(ads, ads[1:]))
    assert sum((Q(1, 2**len(a)) for a in ads), Q(0)) == 1


def smooth(u, h, upper):
    # The angular maximizer is L below u=.8 and (1-u)/2 above.
    if upper:
        start, end = (1 - u) / 2, (1 + u) / 2
        value = m.g(acb(end, -ar(abs(h)))) - m.g(acb(start, -ar(abs(h))))
        derivative = (m.gp(acb(end, -ar(abs(h)))) + m.gp(acb(start, -ar(abs(h))))) / 2
        second = (m.gpp(acb(end, -ar(abs(h)))) - m.gpp(acb(start, -ar(abs(h))))) / 4
    else:
        start, end = ar(L), ar(L) + u
        value = m.g(acb(end, -ar(abs(h)))) - m.g(acb(start, -ar(abs(h))))
        derivative = m.gp(acb(end, -ar(abs(h))))
        second = m.gpp(acb(end, -ar(abs(h))))
    return value.real, derivative.real, second.real


def source_bound(ad, eta, eps, ha, hb, segment):
    dl, dh = decode(ad, 1)
    lo, hi = (Q(0), Q(4, 5)) if segment == 0 else (Q(4, 5), Q(1))
    ul, uh = lo + (hi - lo) * dl, lo + (hi - lo) * dh
    uc, radius = (ul + uh) / 2, (uh - ul) / 2
    U = ar(ul).union(ar(uh))
    va, da, _ = smooth(ar(uc), ha, segment)
    vb, db, _ = smooth(ar(uc), hb, segment)
    _, _, dda = smooth(U, ha, segment)
    _, _, ddb = smooth(U, hb, segment)
    linear = 2 * P * ar(max(ha, Q(0)) + max(hb, Q(0)) - ha)
    value = va + vb + linear * ar(uc) + ar(Q(eta + eps, 12))
    derivative = da + db + linear
    second = dda + ddb
    if ul > 0 and uh < 1:
        value -= (2 + eps) * m.J(uc)
        derivative -= (2 + eps) * (2 * (P * ar(uc)).sin()).log()
        second -= (2 + eps) * P * (P * U).cot()
        return value + abs(derivative) * ar(radius) + abs(second) * ar(radius)**2 / 2
    return (value - (2 + eps) * m.Jrange(ul, uh)[0]
            + abs(derivative) * ar(radius) + abs(second) * ar(radius)**2 / 2)


def reference_bound(ad, eta, eps, fa, fb):
    b = decode(ad, 2)
    pp, p0, velocities = [], [], []
    for j, (ty, face) in enumerate(((eta, fa), (eps, fb))):
        lo, hi = b[2*j:2*j+2]
        pp.append(m.edge(ty, face, lo, hi))
        p0.append(m.edge(ty, face, (lo+hi)/2, (lo+hi)/2))
        velocities.append(m.direction(ty, face))
    witness = m.root_box(*pp, *p0, eps)
    if witness is None:
        return None
    z, zp, w = witness
    f0, g0, _ = m.phase(zp, *p0, eta, eps)
    _, _, hh = m.phase(z, *pp, eta, eps)
    corners = [[acb(ar(x), ar(h)) for x in (Q(0), L) for h in HEIGHTS[ty]]
               for ty in (eta, eps)]
    lows = []
    for target in itertools.product(*corners):
        center = (f0 + sum((g0[j] * (target[j] - p0[j]) for j in (0, 1)), acb(0))).real
        cost = arb(0)
        for k in (0, 1):
            derivative = sum((hh[j][k] * (target[j] - pp[j]) * velocities[k]
                              for j in (0, 1)), acb(0))
            cost += abs(derivative.real) * ar((b[2*k+1] - b[2*k]) / 2)
        lows.append((center - cost).lower())
    lower = min(lows)
    if not lower > ar(PLANES[(eta, eps)]):
        return None
    return {"address": ad, "root": w, "plane_lower": str(lower)}


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--precision", type=int, default=192)
parser.add_argument("--output", type=Path, default=ROOT / "repro/results/research-mixed-both-low-raw-support.json")
args = parser.parse_args()
assert args.precision >= 128
ctx.prec = args.precision
P = m.pi = arb.pi()
initial = {p: sha(ROOT / p) for p in DEPS}
proof_hash, script_hash = sha(PROOF), sha(__file__)
up = json.loads((ROOT / DEPS[2]).read_text())
assert up["status"] == "passed"
assert up["proof_sha256"] == initial[DEPS[0]]
assert up["script_sha256"] == initial[DEPS[1]]
for key in ("dependencies", "dependencies_sha256"):
    for path, digest in up.get(key, {}).items():
        assert sha(ROOT / path) == digest, path
start = time.time()
# Entire-height convexity after angular maximization.
H = max(abs(h) for v in HEIGHTS.values() for h in v)
assert (2 * P * ar(L)).cos() * (2 * P * ar(H)).cosh() < 1
assert -m.J(Q(1, 6)) < ar(Q(1, 6))
assert min(PLANES[k] - SOURCES[k] for k in SOURCES) > Q(1, 100)

source = []
for eta, eps in itertools.product((0, 1), repeat=2):
    for ha, hb in itertools.product(HEIGHTS[eta], HEIGHTS[eps]):
        for segment in (0, 1):
            stack, cells, visited = [""], [], 0
            while stack:
                ad = stack.pop()
                visited += 1
                bound = source_bound(ad, eta, eps, ha, hb, segment)
                if bound < ar(SOURCES[(eta, eps)]):
                    cells.append({"address": ad, "upper": str(bound)})
                else:
                    assert len(ad) < 26, (eta, eps, ha, hb, segment, ad, bound)
                    stack.extend((ad + "0", ad + "1"))
            cover([v["address"] for v in cells])
            source.append({"types": [eta, eps], "heights": [str(ha), str(hb)],
                           "segment": segment, "cells": cells, "visited": visited})
            print("source", eta, eps, ha, hb, segment, len(cells), flush=True)

references = []
for eta, eps in itertools.product((0, 1), repeat=2):
    for fa, fb in itertools.product(range(4), repeat=2):
        stack, cells, visited = [""], [], 0
        while stack:
            ad = stack.pop()
            visited += 1
            try:
                answer = reference_bound(ad, eta, eps, fa, fb)
            except (ValueError, ZeroDivisionError):
                answer = None
            if answer is not None:
                cells.append(answer)
            else:
                assert len(ad) < 28, (eta, eps, fa, fb, ad)
                stack.extend((ad + "0", ad + "1"))
        cover([v["address"] for v in cells])
        references.append({"types": [eta, eps], "faces": [fa, fb],
                           "cells": cells, "visited": visited})
        print("reference", eta, eps, fa, fb, len(cells), flush=True)
assert len(source) == 32 and len(references) == 64
assert initial == {p: sha(ROOT / p) for p in DEPS}
assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
result = {
    "status": "passed", "precision_bits": args.precision,
    "scope": "Both target real coordinates in[0,.10], full typed taper height rectangles, all selections; original raw finite rows and true Fourier weights, geometric plane gap1/100.",
    "source_functions": 16, "source_segments": 32,
    "source_cells": sum(len(v["cells"]) for v in source),
    "reference_products": 64,
    "reference_cells": sum(len(v["cells"]) for v in references),
    "source_covers": source, "reference_covers": references,
    "source_bounds": {f"{a}{b}": str(v) for (a, b), v in SOURCES.items()},
    "plane_bounds": {f"{a}{b}": str(v) for (a, b), v in PLANES.items()},
    "target_real_cutoff": str(L), "height_scale": str(SCALE),
    "target_height_intervals": {str(k): list(map(str, v)) for k, v in HEIGHTS.items()},
    "scalar_comparisons": 3, "gap": "1/100",
    "proof_sha256": proof_hash, "script_sha256": script_hash,
    "dependencies": initial, "elapsed_seconds": time.time() - start,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2) + "\n")
print("PASS", result["source_cells"], "scalar cells", result["reference_cells"], "reference cells", flush=True)
