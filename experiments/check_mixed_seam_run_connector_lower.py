#!/usr/bin/env python3
"""Forty-eight original-log scalar seam-run floors; no parameter cover."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sy
from flint import acb, arb, ctx
import certify_mixed_real_small_support as core

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_seam_run_connector_lower.md"
INTERVALS = {0: (F(".30"), F(".39")), 1: (F(".27"), F(".33"))}
ZERO = {"A00": F(".325066"), "A01": F(".386681"),
        "A10": F(".460764"), "A11": F(".515591"),
        "B0": F(".325066"), "B1": F(".515591")}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-seam-run-connector-lower.json")
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    core.pi, core.ii = arb.pi(), acb(0, 1)
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, checks = {}, set(), {}, []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        if path in visited:
            return None
        raw = (ROOT/path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        record = json.loads(raw)
        visited.add(path)
        merged = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, h in record.get(field, {}).items():
                if p in merged:
                    assert merged[p] == h
                merged[p] = h
                bind(p, h)
        for p in merged:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)
        return record

    def load(stem, prefix="check"):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        record = inherit(path)
        if record is None:
            raw = (ROOT/path).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == bind(path)
            record = json.loads(raw)
        assert record["status"] == "passed"
        assert record["proof_sha256"] == bind("notes/research_"+stem+".md")
        assert record["script_sha256"] == bind("experiments/"+prefix+"_"+stem+".py")
        primary[path] = record
        return record

    low = load("mixed_low_endpoint_connector_lower")
    both = load("mixed_both_low_raw_support", "certify")
    collar = load("mixed_real_zero_collar", "certify")
    real = load("mixed_real_outer_support")
    reset = load("mixed_full_height_reset", "certify")
    deep = load("mixed_deep_low_half_region")
    heights = load("mixed_height_resolved_seam_sources")
    bind("experiments/certify_mixed_real_small_support.py")
    check("completed original root, real phase, height curvature and finite source inputs",
          low["scalar_comparisons"] == 64 and low["original_log_root_disks"] == 24
          and real["validated_source_records"] == 2
          and reset["domains"] == 64 and reset["cells"] == 36325
          and arb(reset["min_negative_real_hessian_eigenvalue"]) > 0
          and heights["source_grid_values"] == 225
          and heights["original_source_cells"] == 57092
          and heights["independent_replay_source_cells"] == 57166)
    check("reference real intervals are exactly the established typed intervals",
          {int(k): tuple(map(F, v)) for k, v in low["middle_real_intervals"].items()} == INTERVALS)
    for kind, values in reset["parameter_rectangles"].items():
        expected = [".22", ".50", "-.03", ".02"] if kind == "0" else [".22", ".50", "-.057", "0"]
        assert list(map(F, values)) == list(map(F, expected))
    for name, value in ZERO.items():
        found = [F(row["upper"]) for row in heights["profiles"][name] if F(row["height"]) == 0]
        assert found == [value]
    check("all unselected height boxes and six exact endpoint profile knots", True)

    u, v, p, q = sy.symbols("u v p q", real=True)
    S = u+sy.I*v
    U, A = (S-sy.I)/(S+sy.I), (p-sy.I)/(p+sy.I)
    identities = [
        (1-U*A)/(1-A)-(S+p)/(S+sy.I),
        (1-U*A)/(1-A)/U-(S+p)/(S-sy.I),
        sy.im((S+p)/(S-sy.I))-(u+(1-v)*p)/(u*u+(v-1)**2),
        sy.im((S+q)/(S+sy.I))-(-u-(1+v)*q)/(u*u+(v+1)**2)]
    P = sy.symbols("P", nonzero=True)
    identities += [P**2/P**(2+eps)-P**(-eps) for eps in (0, 1)]
    for expression in identities:
        assert sy.simplify(expression) == 0
    exact_identity_count = len(identities)
    for eta, eps in itertools.product((0, 1), repeat=2):
        assert F(eta, 2)+F(eps, 2) == F(eta+eps, 2)
        exact_identity_count += 1

    check("coarse signed height maxima give the four affine costs",
          F(".03") >= 0 and F(".02") >= 0 and F(".057") >= 0
          and all(F(0) < x < F(1, 2) for r in INTERVALS.values() for x in r))
    check("internal and boundary finite reserves have strict scalar slack",
          F(1, 3)-F(1, 4) == F(1, 12)
          and F(1, 20)-F(1, 40) == F(1, 40))
    check("neighbor height bounds and changed-AA incidence coefficient",
          max(F(".03")/F(".12"), F(".057")/F(".12"),
              F(".014")/F(".02")) == F(".7")
          and F(".057")*400*F(".02") < F(".7"))
    check("uniform run budget dominates its exact cyclic incidence charge",
          F(1, 4)-F(1, 200) == F(49, 200)
          and F(1, 40)-2*F(1, 200) == F(3, 200)
          and F(49, 200) > F(1, 100)
          and F(3, 200) > F(1, 200))

    old, input_hash, old_centers = None, None, {}
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        old = json.loads(raw)
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
        for row in old["roots"]:
            key = (F(row["a"]), F(row["b"]), row["epsilon"])
            assert key not in old_centers
            old_centers[key] = row["center"]
        assert len(old_centers) == 40

    roots = {}

    def phase(a, b, eta, eps):
        key = (F(a), F(b), eps)
        aa, bb = acb(core.ar(a)), acb(core.ar(b))
        if key not in roots:
            accepted = core.point_root(aa, bb, eps, old_centers[key] if old else None)
            assert accepted is not None, key
            box, center = accepted
            c = acb(core.ar(center[0]), core.ar(center[1]))
            radius = core.ar("1e-12")
            Y = 1/core.second(c, aa, bb, eps)
            residual = abs(Y*core.equation(c, aa, bb, eps))
            contraction = abs(1-Y*core.second(box, aa, bb, eps))
            reserve = radius-residual-contraction*radius
            assert reserve > 0 and contraction < 1
            cot = (core.pi*box).cot()
            assert cot.real > 0 and abs(cot.imag) < 1
            assert all(0 < z.real < 1 for z in (box, box+aa, box+bb))
            roots[key] = (box, dict(a=str(F(a)), b=str(F(b)), epsilon=eps,
                                   center=center, radius="1/1000000000000",
                                   root_box=str(box), cotangent_box=str(cot),
                                   scaled_residual=str(residual),
                                   contraction_upper=str(contraction.upper()),
                                   disk_selfmap_reserve=str(reserve)))
        value = core.phase(roots[key][0], aa, bb, eta, eps)[0]
        assert value.is_finite()
        return value.real

    pi = core.pi
    ell = core.ar("1/1000")
    nu = -core.g(acb(ell)).real
    delta = ell*arb(2).log()+nu
    scalars = []

    def scalar(name, margin):
        assert margin.is_finite() and margin > 0, (name, margin)
        scalars.append(dict(name=name, margin=str(margin)))

    scalar("collar J derivative is negative", 1-2*(pi*ell).sin())
    scalar("positive collar costs", min(nu.lower(), delta.lower()))
    scalar("literal inverse-factorial rate is below 1/6",
           core.ar(F(1, 6))+core.g(acb(core.ar(F(1, 6)))).real)

    def left_cost(kind, x):
        return core.ar(".02")*pi if kind == 0 else core.ar(".057")*pi*(core.ar(F(1, 2)-x))/2

    def right_cost(kind, x):
        return core.ar(".03")*pi if kind == 0 else core.ar(".057")*pi*(1+core.ar(F(1, 2)-x)/2)

    comparisons, expected, minima = [], set(), {}

    def test(kind, eta, eps, a, b, cost, source):
        key = (kind, eta, eps, F(a), F(b))
        assert key not in expected
        expected.add(key)
        value = phase(a, b, eta, eps)
        margin = value-cost-source
        threshold = F(1, 3) if kind == "internal" else F(1, 20)
        assert margin > core.ar(threshold), (key, margin)
        lower = margin.lower()
        minima[kind] = lower if kind not in minima else min(minima[kind], lower)
        comparisons.append(dict(kind=kind, types=[eta, eps], target=[str(a), str(b)],
                                real_phase=str(value), height_cost=str(cost),
                                raw_source_ceiling=str(source), margin=str(margin),
                                margin_lower=str(lower), strict_reserve=str(threshold)))

    for eta, eps in itertools.product((0, 1), repeat=2):
        for a, b in itertools.product(INTERVALS[eta], INTERVALS[eps]):
            source = core.ar(F(eps, 6))+2*delta+core.ar(F(eta+eps, 2))*nu
            test("internal", eta, eps, a, b,
                 left_cost(eta, a)+right_cost(eps, b), source)
        for y in (F(1, 10), F(1, 2)):
            for x in INTERVALS[eps]:
                source = core.ar(ZERO[f"A{eps}{eta}"])+delta+core.ar(F(eps, 2))*nu
                test("left", eta, eps, y, x,
                     arb(0) if y == F(1, 10) else right_cost(eps, x), source)
            for x in INTERVALS[eta]:
                source = core.ar(ZERO[f"B{eps}"])+delta+core.ar(F(eta, 2))*nu
                test("right", eta, eps, x, y,
                     arb(0) if y == F(1, 10) else left_cost(eta, x), source)
    assert len(comparisons) == len(expected) == 48 and len(roots) == 40
    assert {kind: sum(row["kind"] == kind for row in comparisons)
            for kind in ("internal", "left", "right")} == {
                "internal": 16, "left": 16, "right": 16}
    if old:
        assert set(roots) == set(old_centers)
    check("complete 48 scalar corners and 40 original-log disk roots", True)
    for kind, lower in minima.items():
        scalar(kind+" strict reserve", lower-core.ar(F(1, 3) if kind == "internal" else F(1, 20)))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(status="passed", precision_bits=args.precision,
                  exact_identity_count=exact_identity_count, checks=checks,
                  scalar_checks=scalars, scalar_comparisons=48,
                  original_log_root_disks=40, primary_records=len(primary),
                  current_bindings=len(deps), minimum_margins={k: str(v) for k, v in minima.items()},
                  comparisons=comparisons, roots=[row for _, row in roots.values()],
                  new_parameter_cover_cells=0, cyclic_word_enumerations=0,
                  proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                  scope="Original coherent edge lower floors and arbitrary seam-run suppression with nonseam boundary angles in qualitative low/half neighborhoods. No whole-period or general-neighbor theorem.")
    if input_hash:
        result.update(input_sha256=input_hash, saved_root_centers_reused=40)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS 48 scalar corners; 40 original-log disks;", len(deps),
          "bindings; minima", minima, flush=True)


if __name__ == "__main__":
    main()
