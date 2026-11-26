#!/usr/bin/env python3
"""Sixty-four original-source scalar connector lower bounds; no parameter cover.

Every root is accepted by an original-logarithm disk self-map. Floating
polynomial roots propose centers only; --input reuses saved rational centers.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import acb, arb, ctx
import certify_mixed_real_small_support as core

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_low_endpoint_connector_lower.md"
INTERVALS = {0: (F(3, 10), F(39, 100)),
             1: (F(27, 100), F(33, 100))}
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
                    "repro/results/research-mixed-low-endpoint-connector-lower.json")
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
        path = str(path)
        if path not in deps:
            deps[path] = sha(ROOT / path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        if path in visited:
            return None
        raw = (ROOT / path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        record = json.loads(raw)
        visited.add(path)
        bindings = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                if p in bindings:
                    assert bindings[p] == digest, (path, p)
                bindings[p] = digest
                bind(p, digest)
        for p in bindings:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)
        return record

    def load(stem, prefix="check"):
        path = "repro/results/research-" + stem.replace("_", "-") + ".json"
        record = inherit(path)
        if record is None:
            raw = (ROOT / path).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == bind(path)
            record = json.loads(raw)
        assert record["status"] == "passed", path
        assert record["proof_sha256"] == bind("notes/research_" + stem + ".md")
        assert record["script_sha256"] == bind("experiments/" + prefix + "_" + stem + ".py")
        primary[path] = record
        return record

    real = load("mixed_real_outer_support")
    reset = load("mixed_full_height_reset", "certify")
    heights = load("mixed_height_resolved_seam_sources")
    vertices = load("mixed_seam_attenuation_vertices")
    three = load("mixed_type_three_window_strip", "certify")
    four = load("mixed_type_four_height_refinement", "certify")
    small = load("mixed_real_small_support", "certify")
    deep = load("mixed_deep_low_half_region")
    half = load("mixed_half_angle_connector_lower", "certify")
    half_replay_path = "repro/results/research-mixed-half-angle-connector-lower-replay.json"
    half_replay = inherit(half_replay_path)
    if half_replay is None:
        raw = (ROOT / half_replay_path).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == bind(half_replay_path)
        half_replay = json.loads(raw)
    assert half_replay["status"] == "passed" and half_replay["precision_bits"] >= 320
    assert half_replay["proof_sha256"] == half["proof_sha256"]
    assert half_replay["script_sha256"] == half["script_sha256"]
    assert half_replay["input_sha256"] == bind(
        "repro/results/research-mixed-half-angle-connector-lower.json")
    check("completed independent half-angle reserve for the mixed-class corollary",
          half["boundary_products"] == half_replay["boundary_products"] == 2048
          and half["accepted_cells"] == half_replay["accepted_cells"] == 18988
          and half_replay["refinements"] == 0
          and F(half["strict_reserve"]) == F(1, 20)
          and arb(half_replay["minimum_reserve"]) > core.ar(F(1, 20)))
    bind("notes/research_mixed_admissible_boundary_halos.md")
    check("completed original real phase, reset curvature and source inputs",
          real["validated_source_records"] == 2
          and reset["domains"] == 64 and reset["cells"] == 36325
          and F(reset["matrix_cost_upper"]) == 20
          and arb(reset["min_negative_real_hessian_eigenvalue"]) > 0
          and heights["source_grid_values"] == 225
          and heights["original_source_cells"] == 57092
          and heights["independent_replay_source_cells"] == 57166)
    check("current critical rectangles and the original zero-lift helper",
          tuple(map(F, three["target_rectangle"])) ==
          (F(".30"), F(".39"), F("-.03"), F(".02"))
          and tuple(map(F, four["rectangles"][1])) ==
          (F(".27"), F(".33"), F("-.057"), F("-.001"))
          and F(four["upper_height"]) == F("-.02")
          and {int(k): v for k, v in small["rectangles"].items()} == core.RECTS)
    for kind, values in reset["parameter_rectangles"].items():
        expected = [".22", ".50", "-.03", ".02"] if kind == "0" else [
            ".22", ".50", "-.057", "0"]
        assert list(map(F, values)) == list(map(F, expected))
        lo, hi = INTERVALS[int(kind)]
        assert F(values[0]) < lo < hi < F(values[1])
    check("all vertical reference-to-real segments stay in admitted reset boxes", True)
    for name, value in ZERO.items():
        knots = heights["profiles"][name]
        found = [F(row["upper"]) for row in knots if F(row["height"]) == 0]
        assert found == [value], (name, found)
    check("all six exact height-zero source ceilings extracted", True)

    input_hash, old = None, None
    old_centers = {}
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
        assert len(old_centers) == 24

    ell = core.ar("1/1000")
    J = core.g(acb(ell)).real
    nu = -J
    delta = ell * arb(2).log() - J
    scalar_checks = []

    def scalar(name, margin):
        assert margin.is_finite() and margin > 0, (name, margin)
        scalar_checks.append({"name": name, "margin": str(margin)})

    scalar("the collar derivative has negative J prime",
           1 - 2 * (core.pi * ell).sin())
    scalar("the middle full Fourier collar cost is positive", nu)
    scalar("the finite product collar perturbation is positive", delta)
    scalar("selected real endpoint correction vanishes",
           -core.g(acb(core.ar("1/10"))).real)

    roots = {}

    def root(a, b, eps):
        key = (F(a), F(b), eps)
        if key in roots:
            return roots[key][0]
        aa, bb = acb(core.ar(a)), acb(core.ar(b))
        center = old_centers[key] if old is not None else None
        accepted = core.point_root(aa, bb, eps, center)
        assert accepted is not None, key
        box, center = accepted
        c = acb(core.ar(center[0]), core.ar(center[1]))
        r = core.ar("1e-12")
        Y = 1 / core.second(c, aa, bb, eps)
        contraction = abs(1 - Y * core.second(box, aa, bb, eps))
        residual = abs(Y * core.equation(c, aa, bb, eps))
        reserve = r - residual - contraction * r
        assert reserve > 0 and contraction < 1
        S = (core.pi * box).cot()
        assert S.real > 0 and abs(S.imag) < 1
        assert all(0 < z.real < 1 for z in (box, box + aa, box + bb))
        row = dict(a=str(F(a)), b=str(F(b)), epsilon=eps,
                   center=center, radius="1/1000000000000",
                   root_box=str(box), cotangent_box=str(S),
                   scaled_residual=str(residual),
                   contraction_upper=str(contraction.upper()),
                   disk_selfmap_reserve=str(reserve))
        roots[key] = (box, row)
        return box

    def phase(a, b, eta, eps):
        z = root(a, b, eps)
        value = core.phase(z, acb(core.ar(a)), acb(core.ar(b)), eta, eps)[0]
        assert value.is_finite()
        return value.real

    comparisons = []
    minimum = None
    for alpha, beta, gamma in itertools.product((0, 1), repeat=3):
        source = core.ar(ZERO[f"A{beta}{alpha}"] + ZERO[f"B{gamma}"]) + 2 * delta + beta * nu
        for eleft, x, eright in itertools.product((F(1, 10), F(1, 2)),
                                                 INTERVALS[beta],
                                                 (F(1, 10), F(1, 2))):
            left = phase(eleft, x, alpha, beta)
            right = phase(x, eright, beta, gamma)
            margin = left + right - source
            assert margin > core.ar(F(11, 50)), (alpha, beta, gamma, eleft, x, eright, margin)
            lower = margin.lower()
            minimum = lower if minimum is None else min(minimum, lower)
            comparisons.append(dict(types=[alpha, beta, gamma],
                                    left_real=str(eleft), middle_real=str(x), right_real=str(eright),
                                    left_phase=str(left), right_phase=str(right),
                                    complete_source_ceiling=str(source),
                                    margin=str(margin), margin_lower=str(lower)))
    assert len(comparisons) == 64 and len(roots) == 24
    expected = {(a, b, c, l, x, r) for a, b, c in itertools.product((0, 1), repeat=3)
                for l, x, r in itertools.product((F(1, 10), F(1, 2)),
                                                 INTERVALS[b],
                                                 (F(1, 10), F(1, 2)))}
    assert {(tuple(row["types"]) + (F(row["left_real"]), F(row["middle_real"]), F(row["right_real"])))
            for row in comparisons} == expected
    if old is not None:
        assert set(roots) == set(old_centers)
    scalar("uniform sixty-four-scalar reserve exceeds 11/50",
           minimum - core.ar(F(11, 50)))
    check("all 64 exact corner cases and 24 unique original-log disk roots", True)
    check("the qualitative neighborhood has a positive reserve budget",
          F(11, 50) - F(1, 5) == F(1, 50))
    check("uniform low-neighbor height slopes for all selections",
          max(F(".03")/F(".12"), F(".057")/F(".12"),
              F(".014")/F(".02")) == F(7, 10)
          and F(".057")/F(".12") == F(19, 40))
    check("two endpoint incidences per independent seam pay every changed AA incidence",
          2*F(7, 10) == F(7, 5))
    check("strict pair, AA error and one finite tolerance leave the stated region loss",
          F(1, 5)-F(1, 20)-F(1, 20) == F(1, 10))
    check("mixed classes have the same height-change bound and retain their loss",
          F(".057")*400*F(".02") < F(7, 10)
          and F(1, 40)-F(1, 200)-F(1, 200) > F(1, 100))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / p) == digest for p, digest in deps.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(status="passed", precision_bits=args.precision,
                  scalar_comparisons=64, original_log_root_disks=24,
                  checks=checks, scalar_checks=scalar_checks,
                  primary_records=len(primary), current_bindings=len(deps),
                  middle_real_intervals={str(k): list(map(str, v)) for k, v in INTERVALS.items()},
                  zero_height_source_ceilings={k: str(v) for k, v in ZERO.items()},
                  collar_width_upper="1/1000", collar_nu=str(nu), collar_delta=str(delta),
                  strict_connector_reserve="11/50",
                  qualitative_neighborhood_reserve="1/5",
                  minimum_margin_lower=str(minimum), comparisons=comparisons,
                  roots=[row for _, row in roots.values()],
                  new_parameter_cover_cells=0,
                  proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                  scope="Uniform real-neighbor pair lower bound from 64 corners; low-endpoint repaired-halo consequence and qualitative independent-seam region assembly. No full transition or whole-period result.")
    if input_hash:
        result["input_sha256"] = input_hash
        result["saved_root_proposals_reused"] = 24
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS 64 scalar comparisons; 24 original-log disks;",
          len(deps), "bindings; minimum", minimum, flush=True)


if __name__ == "__main__":
    main()
