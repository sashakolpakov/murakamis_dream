#!/usr/bin/env python3
"""Extended real zero collar: full reference-boundary cover for other angles [.1,.5]."""
import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_real_zero_collar_extension.md"
spec = importlib.util.spec_from_file_location(
    "zero_collar_endpoint_primitive", ROOT / "experiments/certify_mixed_all_endpoint_support.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
DEPS = [
    "notes/research_mixed_all_endpoint_support.md",
    "experiments/certify_mixed_all_endpoint_support.py",
    "repro/results/research-mixed-all-endpoint-support.json",
    "notes/research_mixed_endpoint_support_grid.md",
    "experiments/check_mixed_endpoint_support_grid.py",
    "repro/results/research-mixed-endpoint-support-grid.json",
    "notes/research_mixed_fourier_weight_continuation.md",
    "notes/research_mixed_boundary_strip_bounds.md",
    "notes/research_mixed_real_zero_collar.md",
    "experiments/certify_mixed_real_zero_collar.py",
    "repro/results/research-mixed-real-zero-collar.json",
]
L = Q(1, 1000)
SOURCE = {(0, 0, 0): Q(".332"), (0, 0, 1): Q(".332"),
          (0, 1, 0): Q(".523"), (0, 1, 1): Q(".471"),
          (1, 0, 0): Q(".335"), (1, 0, 1): Q(".394"),
          (1, 1, 0): Q(".526"), (1, 1, 1): Q(".526")}
PLANE = {key: value + Q(".061") for key, value in SOURCE.items()}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ar(x):
    x = Q(x)
    return arb(x.numerator) / x.denominator


def check_record(j):
    rec = json.loads((ROOT / DEPS[j + 2]).read_text())
    assert rec["status"] == "passed"
    assert rec["proof_sha256"] == initial[DEPS[j]]
    assert rec["script_sha256"] == initial[DEPS[j + 1]]
    for key in ("dependencies", "dependencies_sha256"):
        for p, h in rec.get(key, {}).items():
            assert sha(ROOT / p) == h, p
    return rec


def reference(case, ad):
    eta, eps, fa, fb = case
    al, ah, bl, bh = m.box(ad)
    a, b = m.edge(eta, fa, al, ah), m.edge(eps, fb, bl, bh)
    a0 = m.edge(eta, fa, (al + ah) / 2, (al + ah) / 2)
    b0 = m.edge(eps, fb, (bl + bh) / 2, (bl + bh) / 2)
    witness = m.root_box(a, b, a0, b0, eps)
    if witness is None:
        return None
    z, zp, w = witness
    value, grad, _ = m.phase(zp, a0, b0, eta, eps)
    _, _, hh = m.phase(z, a, b, eta, eps)
    pp, p0 = (a, b), (a0, b0)
    vel = (m.direction(eta, fa), m.direction(eps, fb))
    radii = ((ah - al) / 2, (bh - bl) / 2)
    lower = []
    for side in (0, 1):
        current = []
        for x, y in itertools.product((Q(0), L), (Q(".1"), Q(".5"))):
            target = (ar(x), ar(y)) if side == 0 else (ar(y), ar(x))
            center = (value + sum((grad[j] * (target[j] - p0[j]) for j in (0, 1)), acb(0))).real
            cost = arb(0)
            for k in (0, 1):
                derivative = sum((hh[j][k] * (target[j] - pp[j]) * vel[k] for j in (0, 1)), acb(0))
                cost += abs(derivative.real) * ar(radii[k])
            bound = (center - cost).lower()
            if not bound > ar(PLANE[(eta, eps, side)]):
                return None
            current.append(bound)
        lower.append(str(min(current)))
    return {"address": ad, "root": w, "plane_lowers": lower}


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--precision", type=int, default=256)
parser.add_argument("--output", type=Path, default=ROOT / "repro/results/research-mixed-real-zero-collar-extension.json")
args = parser.parse_args()
assert args.precision >= 160
ctx.prec = args.precision
P = m.pi = arb.pi()
initial = {p: sha(ROOT / p) for p in DEPS}
ph, sh = sha(PROOF), sha(__file__)
all_endpoint, earlier_grid = check_record(0), check_record(3)
collar = check_record(8)
assert collar["cutoff"] == "1/1000" and collar["reference_products"] == 64
assert collar["source_records"] == 2 and collar["scalar_comparisons"] == 18
constants = {}
for eps, beta in ((0, 0), (1, 0), (1, 1)):
    rows = [v for v in all_endpoint["source_grid"]
            if v["source"][:2] == [eps, beta] and v["height"] == "0" and v["kappa"] == "0"]
    assert rows
    vals = {Q(v["upper"]) for v in rows}
    assert len(vals) == 1
    constants[(eps, beta)] = vals.pop()
rows = [v for v in earlier_grid["source_grid"] if v["height"] == "0" and v["kappa"] == "0"]
assert len(rows) == 1
constants[(0, 1)] = Q(rows[0]["upper"])
expected = {(0, 0): Q(162533, 500000), (0, 1): Q(386681, 1000000),
            (1, 0): Q(115191, 250000), (1, 1): Q(515591, 1000000)}
assert constants == expected
nu = -m.J(L)
delta = ar(L) * arb(2).log() + nu
assert nu > 0 and 2 * (2 * P * ar(L)).sin() < ar("1/2")
budgets = []
for eta, eps, side in itertools.product((0, 1), repeat=3):
    lowtype, othertype = (eta, eps) if side == 0 else (eps, eta)
    bound = ar(constants[(eps, othertype)]) + delta + lowtype * nu / 2 + ar("1/100000")
    assert bound < ar(SOURCE[(eta, eps, side)])
    assert PLANE[(eta, eps, side)] - SOURCE[(eta, eps, side)] > Q(3, 50)
    budgets.append({"types": [eta, eps], "side": side, "source_upper": str(bound)})

cases = []
for case in itertools.product((0, 1), (0, 1), range(4), range(4)):
    stack, cells, visited = [""], [], 0
    while stack:
        ad = stack.pop()
        visited += 1
        try:
            ans = reference(case, ad)
        except (ValueError, ZeroDivisionError):
            ans = None
        if ans is None:
            assert len(ad) < 28, (case, ad)
            stack.extend((ad + "0", ad + "1"))
        else:
            cells.append(ans)
    m.cover([v["address"] for v in cells])
    cases.append({"case": list(case), "cells": cells, "visited": visited})
    print("reference", case, len(cells), flush=True)
assert len(cases) == 64
assert {tuple(row["case"]) for row in cases} == set(itertools.product((0, 1), (0, 1), range(4), range(4)))
assert initial == {p: sha(ROOT / p) for p in DEPS}
assert ph == sha(PROOF) and sh == sha(__file__)
for index in (0, 3, 8):
    check_record(index)
out = {
    "status": "passed", "precision_bits": args.precision,
    "scope": "Both target heights zero; one real angle in CLOSED[0,.001], the other in CLOSED[.1,.5]; both orientations/types/all selections; original raw source gap3/50.",
    "cutoff": str(L), "other_interval": ["1/10", "1/2"],
    "endpoint_source_constants": {f"{e}{b}": str(v) for (e, b), v in constants.items()},
    "row_increment": str(delta), "low_fourier_rate": str(nu),
    "source_budgets": budgets, "reference_products": 64,
    "reference_cells": sum(len(v["cells"]) for v in cases),
    "cases": cases, "scalar_comparisons": 18, "source_records": 2, "collar_input_records": 1,
    "plane_thresholds": {"".join(map(str,k)): str(v) for k,v in PLANE.items()},
    "proof_sha256": ph, "script_sha256": sh, "dependencies": initial,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(out, indent=2) + "\n")
print("PASS", out["reference_cells"], "reference cells + 18 scalar comparisons + 2 source records + 1 collar record")
