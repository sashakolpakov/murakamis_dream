#!/usr/bin/env python3
"""Floating evaluation of 48 analytic seam-run floors; no optimization/proof."""
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HELPER = ROOT / "repro/diagnostics/2026-11-05-seam-attenuation-vertices/phase_helpers.py"
spec = importlib.util.spec_from_file_location("phase_helpers", HELPER)
ph = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ph)
I = {0: (.3, .39), 1: (.27, .33)}
A = {(0, 0): .325066, (0, 1): .386681,
     (1, 0): .460764, (1, 1): .515591}
B = [.325066, .515591]
nu = -ph.g(.001).real
delta = .001 * math.log(2) + nu


def left_cost(kind, x):
    return .02 * math.pi if kind == 0 else .057 * math.pi * (.5-x)/2


def right_cost(kind, x):
    return .03 * math.pi if kind == 0 else .057 * math.pi * (1+(.5-x)/2)


rows = []
for eta, eps in itertools.product((0, 1), repeat=2):
    for a, b in itertools.product(I[eta], I[eps]):
        f = ph.phase(a, b, eta, eps)[0].real
        cost = left_cost(eta, a) + right_cost(eps, b)
        raw = eps/6 + 2*delta + (eta+eps)*nu/2
        rows.append(dict(kind="internal", types=[eta, eps], target=[a, b],
                         realphase=f, cost=cost, raw=raw, gap=f-cost-raw))
    for y in (.1, .5):
        for x in I[eps]:
            f = ph.phase(y, x, eta, eps)[0].real
            cost = 0 if y == .1 else right_cost(eps, x)
            raw = A[eps, eta] + delta + eps*nu/2
            rows.append(dict(kind="left", types=[eta, eps], target=[y, x],
                             realphase=f, cost=cost, raw=raw, gap=f-cost-raw))
        for x in I[eta]:
            f = ph.phase(x, y, eta, eps)[0].real
            cost = 0 if y == .1 else left_cost(eta, x)
            raw = B[eps] + delta + eta*nu/2
            rows.append(dict(kind="right", types=[eta, eps], target=[x, y],
                             realphase=f, cost=cost, raw=raw, gap=f-cost-raw))
rows.sort(key=lambda row: row["gap"])
assert len(rows) == 48
result = dict(scope="Floating scalar diagnostic of analytic coarse-gradient floors only; no outward proof, optimizer, complex-neighbor extrapolation or cycle enumeration.",
              original_source="Original allocated phi and literal endpoint ceilings, collar width .001.",
              helper=str(HELPER.relative_to(ROOT)),
              helper_sha256=hashlib.sha256(HELPER.read_bytes()).hexdigest(),
              scalar_count=48, rows=rows)
(HERE/"results.json").write_text(json.dumps(result, indent=2)+"\n")
print("48 scalar proposals; minimum", rows[0]["gap"],
      "; internal minimum", min(r["gap"] for r in rows if r["kind"] == "internal"))
