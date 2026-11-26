#!/usr/bin/env python3
"""Extract early/Q and partial-Q/right support from saved source inputs."""
import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_early_upper_transition_support.md"
HELPER = ROOT / "experiments/certify_mixed_early_transition_support.py"
spec = importlib.util.spec_from_file_location("early_original_witnesses", HELPER)
early = importlib.util.module_from_spec(spec)
spec.loader.exec_module(early)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-early-upper-transition-support.json")
    args = ap.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    early.core.pi, early.core.ii = arb.pi(), acb(0, 1)
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, checks = {}, set(), {}, []

    def bind(path, expected=None):
        value = sha(ROOT/path)
        if expected is not None:
            assert value == expected, path
        if path in deps:
            assert deps[path] == value, path
        deps[path] = value
        return value

    def inherit(path):
        bind(path)
        record = json.loads((ROOT/path).read_text())
        if path in visited:
            return record
        visited.add(path)
        inherited = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                if p in inherited:
                    assert inherited[p] == digest, p
                inherited[p] = digest
                bind(p, digest)
        for p in inherited:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)
        return record

    def load(stem, prefix):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        record = inherit(path)
        assert record["status"] == "passed", path
        proof_path = "notes/research_"+stem+".md"
        proof_hash = record.get("proof_sha256")
        if proof_hash is None:
            proof_hash = record.get("dependencies", {}).get(
                proof_path, record.get("dependencies_sha256", {}).get(proof_path))
        assert proof_hash == bind(proof_path)
        assert record["script_sha256"] == bind("experiments/"+prefix+"_"+stem+".py")
        primary[path] = record
        return record

    def check(name, condition):
        assert condition, name
        checks.append(name)

    original = load("mixed_early_transition_support", "certify")
    slopes = load("mixed_geometric_support_slopes", "certify")
    closed = load("mixed_closed_cotangent_roots", "check")
    curvature = load("mixed_selected_height_reference_extension", "check")
    interface = load("mixed_left_right_interface_source", "certify")
    cap = load("mixed_early_selected_source_cap", "certify")
    partial = load("mixed_partially_reset_right_support", "certify")
    upper = load("mixed_upper_transition_right_support", "check")
    fourier = load("mixed_fourier_weight_continuation", "check")
    for p in ("notes/research_mixed_early_plateau_right_clusters.md",
              "notes/research_mixed_full_height_reset.md",
              "notes/research_mixed_oriented_height_reset.md",
              "notes/research_mixed_unselected_right_clamping.md",
              "notes/research_mixed_selected_right_taper_support.md"):
        bind(p)

    check("original early support and exact oriented phase gap",
          original["reference_products"] == 64 and original["cells"] == 251
          and F(original["phase_gap"]) == F(1, 100))
    cases = list(itertools.product((0, 1), (0, 1), range(4), range(4)))
    assert [tuple(r["case"]) for r in original["cases"]] == cases
    for r in original["cases"]:
        early.core.cover([c["address"] for c in r["leaves"]])
    check("all original reference partitions remain complete",
          sum(len(r["leaves"]) for r in original["cases"]) == 251)
    check("actual geometric slopes use the complete original window family",
          slopes["case_count"] == 512 and slopes["accepted_cells"] == 4820
          and slopes["full_family"] is True)
    check("closed root and branchwise curvature derivation are completed inputs",
          closed["exact_identity_count"] == 13 and curvature["exact_checks"] == 11)
    check("actual full cap and cap-right source products are completed",
          cap["products"] == 161 and cap["accepted"] == 71240
          and interface["products"] == 84 and interface["accepted"] == 7740)
    check("unrounded partial-P/right and independent upper-transition bounds",
          F(partial["strict_core_ceiling"]) == F(1, 200)
          and partial["reference_products"] == 512
          and partial["reference_cells"] == 5064
          and upper["extracted_height_profiles"] == 18
          and upper["extracted_support_values"] == 180
          and F(upper["finite_source_gap"]) == F(1, 2000))
    check("overlapping source intervals cover the enlarged Q",
          F(11, 50) < F(2, 5) < F(9, 20) < F(1, 2))
    check("whole-angle finite ceiling spends one source tolerance",
          F(1, 200)+F(1, 1000) == F(3, 500)
          and -F(upper["finite_source_gap"]) < F(3, 500))
    check("last original tangent interval and rational midpoint",
          early.INTERVALS[-1] == (F(137, 320), F(9, 20))
          and sum(early.INTERVALS[-1])/2 == F(281, 640))
    check("rational target slope leaves a positive actual-plane slope margin",
          -F(101, 500)-(-F(1, 5)) == -F(1, 500))
    check("hybrid early slow and fast fractions give the original height bands",
          (F(3, 25)-F(1, 10))/F(3, 25) == F(1, 6)
          and F(3, 100)/6 == F(1, 200)
          and F(1, 50)/6 == F(1, 300)
          and F(57, 1000)/6 == F(19, 2000))
    check("quadratic right taper remains inside its linear source triangle",
          F(400)*F(1, 20) == 20)
    cot_margin = early.ar(F(1, 2)) - \
        (2*early.core.pi*early.ar(F(7, 500))).sinh() / \
        (2*(early.core.pi*early.ar(F(1, 10))).sin()**2)
    check("closed enlarged target rectangle remains in the cotangent domain",
          cot_margin > 0)

    old = {tuple(r["key"]): r["center"] for r in original["tangent_roots"]}
    assert len(old) == len(original["tangent_roots"])
    roots, rows = {}, []
    worst, worst_key = None, None
    for eta, eps in itertools.product((0, 1), repeat=2):
        for sa, sb in itertools.product(range(eta+1), range(eps+1)):
            for fa, fb in itertools.product(range(sa+1), range(sb+1)):
                for h0, h1 in itertools.product(early.HEIGHTS[eta, sa],
                                                early.HEIGHTS[eps, sb]):
                    for side in (0, 1):
                        real = (F(3, 25), F(281, 640)) if side == 0 else \
                               (F(281, 640), F(3, 25))
                        c = [acb(early.ar(real[k]), early.ar((h0, h1)[k]))
                             for k in (0, 1)]
                        key = (eps, str(h0), str(h1), side, 15)
                        if key not in roots:
                            assert key in old
                            # The old proposal is untrusted: rerun its original
                            # logarithmic point self-map, with no new proposal.
                            result = early.core.point_root(*c, eps, old[key])
                            assert result is not None, key
                            roots[key] = result[0]
                        _, grad, _ = early.core.phase(roots[key], *c, eta, eps)
                        k = 1-side
                        forcing, selected = (fa, fb)[k], (sa, sb)[k]
                        derivative = (grad[k]+early.ar(F(forcing, 2))*early.core.gp(c[k])
                                      +early.core.pi*early.core.ii*(selected-forcing)).real
                        assert derivative < -early.ar(F(101, 500)), key
                        case = [eta, eps, sa, sb, fa, fb, str(h0), str(h1), side]
                        rows.append(dict(case=case, root_key=list(key),
                                         derivative_upper=str(derivative.upper())))
                        if worst is None or derivative.upper() > worst:
                            worst, worst_key = derivative.upper(), case
    check("all exact branch and height-corner derivatives were tested",
          len(rows) == 128 and len(roots) == 50
          and len({tuple(r["case"]) for r in rows}) == 128)
    check("every accepted derivative has the stated rational ceiling",
          worst < -early.ar(F(101, 500)))
    ih = None
    if args.input:
        ih = sha(args.input)
        previous = json.loads(args.input.read_text())
        assert previous["status"] == "passed"
        assert previous["proof_sha256"] == ph and previous["script_sha256"] == sh
        assert previous["dependencies_sha256"] == deps
        assert previous["checks"] == checks
        assert [r["case"] for r in previous["derivatives"]] == [r["case"] for r in rows]
        assert [r["root_key"] for r in previous["derivatives"]] == [r["root_key"] for r in rows]
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in deps.items())
    if args.input:
        assert ih == sha(args.input)
    result = dict(
        status="passed", precision_bits=args.precision, exact_checks=len(checks),
        checks=checks, derivative_tests=len(rows), saved_point_roots=len(roots),
        derivative_ceiling="-101/500", derivative_upper=str(worst),
        worst_case=worst_key, derivatives=rows, cotangent_margin=str(cot_margin),
        early_phase_gap="1/100", upper_angle_gain="1/500",
        partial_Q_right_finite_ceiling="3/500",
        primary_records=len(primary), current_bindings=len(deps),
        new_root_proposals=0, new_reference_cells=0, new_source_cells=0,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope="Early coherent support through Q=[.22,.5] at actual cyclic references, and partial-Q/right full raw finite ceiling. No enlarged Q/Q allocation or whole-region claim.")
    if ih:
        result["input_sha256"] = ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "checks;", len(rows), "derivatives;",
          len(roots), "saved point roots;", len(primary), "primary;",
          len(deps), "bindings; maximum", worst, flush=True)


if __name__ == "__main__":
    main()
