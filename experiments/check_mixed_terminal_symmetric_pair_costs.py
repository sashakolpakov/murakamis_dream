#!/usr/bin/env python3
"""Saved-only exact verification of the stronger terminal main costs.

Canonical existence, zero lifts, primitive/logarithm enclosures, index barriers
and scalar curvature are inherited from hash-bound proofs and successful audits.
This checker recomputes the saved reference guards, new rational pair witnesses,
two cubic tangents, and eight main budgets. It imports no analytic evaluator.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_terminal_symmetric_pair_costs.md"
CUBIC = "repro/results/research-mixed-terminal-cubic-profile-completion.json"
SOURCE = "repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json"
REFERENCES = "repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json"
CURVATURE = "repro/results/research-mixed-terminal-joint-main-curvature-budget.json"
COMMON = "repro/results/research-mixed-terminal-joint-main-common-height.json"
SOURCE_AUDIT = "repro/results/research-mixed-terminal-joint-main-budget-saved-audit.json"
REFERENCE_AUDIT = "repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json"
PINNED = {
    PROOF: "b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f",
    CUBIC: "c9673af4a62912ed4626d88d1776921dc9572f05ea5a8b69c5eeca7adcd16e18",
    SOURCE: "2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9",
    REFERENCES: "ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b",
    CURVATURE: "12677b1d1b20ece4ffe61c7a370cf54b3c98233fb81f082e0220435b30a89495",
    COMMON: "53789515f1b33ffe9397c7a4405be7bcaa3db865267ad1e7da0495399c691cba",
    SOURCE_AUDIT: "fceffb2a2bfe677579bb6ff94087b5129c9db0daf8f85674b94ee6de7fa3dda6",
    REFERENCE_AUDIT: "bedf680b3f57c799980517f7aa6178a7f9c5a0890bac8528947e9018baf7a4de",
    "experiments/check_mixed_terminal_cubic_profile_completion.py":
        "b60f553c3e6dde985d135ad114cffdecba65893a2c8d031ca736d44bfe3951e6",
    "notes/research_mixed_terminal_main_optimizer_localization.md":
        "6e88ab6d8635255877ae6ba570d6d8e434880f8a01c710452ed48b4cde482295",
    "notes/research_mixed_terminal_cubic_cost_and_response_bounds.md":
        "dfc3f415e742aa9c632707aea7c699bb2ccbdc054c08fc7ba640e943bcdaa741",
    "notes/research_mixed_terminal_full_input_index_barrier.md":
        "45ae03bf28a78df930fc8e7c97054ca40689630423a4d36c0009b6b0bb900ee2",
}


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            digest.update(block)
    return digest.hexdigest()


def fragment_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def interval(value):
    assert value["finite"] is True
    lo, hi = F(value["lower_rational"]), F(value["upper_rational"])
    assert lo <= hi
    return lo, hi


def inside(bounds, lo, hi):
    return F(lo) < bounds[0] <= bounds[1] < F(hi)


def association(row):
    return row["beta"], row["epsilon"], row["source_index"], row["source_case_sha256"]


def rational_witnesses():
    pi_lo, pi_hi = F(157, 50), F(22, 7)
    u, v = F(69, 100), F(132, 175)
    assert 0 < u < F(11, 50)*pi_lo and v == F(6, 25)*pi_hi
    cosine_reserve = F(1, 5)-F(3, 50)*pi_hi
    cotangent_reserve = 5*(u-u**3/6)-4*(1-u*u/2+u**4/24)
    cosh_reserve = F(13, 10)-(1+(v*v/2)/(1-v*v/12))
    assert cosine_reserve > 0
    assert cotangent_reserve == F(18132793, 200000000) > 0
    assert cosh_reserve == F(399, 291730) > 0
    assert (1-F(1, 5))/(F(13, 10)-F(1, 5)) == F(8, 11)
    rank_one = F(11, 4)*(1-F(16, 25))
    assert rank_one == F(99, 100) < 1

    q, d, k, x = F(141, 1000), F(93, 500), F(19), F(23, 500)
    assert 0 < x < d and q < k*d*d/2
    value = q*x-k*d*x*x/2+k*x**3/6
    s_slope = q-k*d*x+k*x*x/2
    s_intercept = value-s_slope*x
    assert s_slope == -F(731, 500000)
    assert s_intercept == F(2341883, 750000000) < F(1, 320)

    q, d, k, x = F(51, 200), F(3, 20), F(141, 10), F(93, 1000)
    assert x > 0 and k == F(3, 2)*F(47, 5)
    value = q*x-k*d*x*x/2-k*x**3/6
    t_slope = q-k*d*x-k*x*x/2
    t_intercept = value-t_slope*x
    assert t_slope == -F(53409, 20000000)
    assert t_intercept == F(64633977, 5000000000) < F(13, 1000)

    selected = F(51, 200)**2/8
    forced_affine = F(63, 200)*(F(9, 20)-F(7, 25))
    assert selected == F(2601, 320000)
    assert forced_affine == F(1071, 20000)
    budgets = {
        "factorial": -F(463, 10000)+F(1, 320)+F(13, 1000)+selected,
        "forced_full_P": -F(109, 1000)+F(1, 320)+F(13, 1000)+forced_affine,
    }
    assert budgets == {"factorial": -F(1411, 64000),
                       "forced_full_P": -F(1573, 40000)}
    assert all(value < -F(1, 50) for value in budgets.values())
    return {
        "cosine_reserve": str(cosine_reserve),
        "cotangent_reserve": str(cotangent_reserve),
        "cosh_reserve": str(cosh_reserve),
        "rank_one_upper": str(rank_one),
        "s_slope": str(s_slope), "s_intercept": str(s_intercept),
        "t_slope": str(t_slope), "t_intercept": str(t_intercept),
        "selected_gain_upper": str(selected),
        "forced_affine_upper": str(forced_affine),
    }, budgets


def verify(inputs):
    paths = (CUBIC, SOURCE, REFERENCES, CURVATURE, COMMON,
             SOURCE_AUDIT, REFERENCE_AUDIT)
    for name, digest in inputs.items():
        assert sha(ROOT/name) == digest, name
    records = {name: json.loads((ROOT/name).read_text()) for name in paths}
    for record in records.values():
        if "changed_inputs" in record:
            assert record["changed_inputs"] == []
        for name, digest in record.get("input_sha256", {}).items():
            assert name not in inputs or inputs[name] == digest, name
            inputs[name] = digest
    for name, digest in inputs.items():
        assert sha(ROOT/name) == digest, name
    cubic, source, refs, curvature, common, audit, refaudit = [records[p] for p in paths]
    assert cubic["status"] == curvature["status"] == common["status"] == "passed"
    assert audit["status"] == refaudit["status"] == "passed"
    assert source["status"] == refs["status"] == "complete fixed diagnostic"
    assert cubic["checker_sha256"] == inputs[
        "experiments/check_mixed_terminal_cubic_profile_completion.py"]
    assert cubic["completed_terminal_labels_per_case"] == [27]*4
    assert audit["source_path"] == SOURCE and audit["source_sha256"] == inputs[SOURCE]
    assert audit["branch_bounds_checked"] == 8
    assert audit["certified_reference_associations_checked"] == 4
    assert refaudit["source_path"] == REFERENCES and refaudit["source_sha256"] == inputs[REFERENCES]
    assert refaudit["canonical_references_checked"] == 4
    for record in (curvature, common):
        assert record["source_path"] == SOURCE and record["source_sha256"] == inputs[SOURCE]
        assert record["canonical_reference_cases_checked"] == 4
    assert common["both_branches_bound_on_full_P"] is True
    assert F(common["initial_height_rational"]) == F(1, 100)
    assert F(source["height_rational"]) == F(cubic["same_selected_height_rational"]) == F(1, 100)
    pi = interval(source["pi"])
    assert F(157, 50) < pi[0] <= pi[1] < F(22, 7)
    witnesses, budgets = rational_witnesses()
    expected = list(itertools.product((0, 1), repeat=2))
    for rows in (source["cases"], refs["cases"], cubic["canonical_cases"],
                 curvature["canonical_cases"], common["canonical_cases"]):
        assert [(r["beta"], r["epsilon"]) for r in rows] == expected
    summaries = []
    for index, (row, ref, old, cv, ch) in enumerate(zip(
            source["cases"], refs["cases"], cubic["canonical_cases"],
            curvature["canonical_cases"], common["canonical_cases"])):
        assert row["source_index"] == index
        assert row["source_case_sha256"] == fragment_sha(ref)
        assert all(association(r) == association(row) for r in (old, cv, ch))
        assert ref["canonical_reference_certified"] is True
        assert row["status"] == "both main-current bounds enclosed"
        assert F(row["height_rational"]) == F(1, 100)
        assert row["saved_coordinate_enclosures"] == ref["coordinate_enclosures"]
        assert row["outside_coordinate_rational"] == ref["outside_coordinate"]
        assert ch["all_original_height_and_curvature_guards_verified"] is True
        q = row["actual_coordinate_enclosures"]
        for name in ("e", "xi", "t", "a", "s"):
            for part in ("real", "imag"):
                outer, inner = interval(q[name][part]), interval(ref["coordinate_enclosures"][name][part])
                assert outer[0] <= inner[0] <= inner[1] <= outer[1]
        assert all(q[name] == value for name, value in cv["coordinate_guards"].items())
        s, a, t = [interval(q[name]["real"]) for name in ("s", "a", "t")]
        hs, ha, ht = [interval(q[name]["imag"]) for name in ("s", "a", "t")]
        assert inside(s, ".28", ".314") and inside(a, ".28", ".314")
        assert inside(t, ".22", ".35")  # Stronger containing product than the old .18 guard.
        assert inside(hs, "-.102", "-.001") and inside(ha, "-.108", "-.001")
        assert max(map(abs, hs)) < F(61, 1000)
        assert max(map(abs, ht)) < F(33, 500)
        beta, eps = row["beta"], row["epsilon"]
        v = "xi" if eps == 0 else "e"
        vr, hv = interval(q[v]["real"]), interval(q[v]["imag"])
        if eps == 0:
            assert inside(ht, "-.072", ".021") and inside(hv, ".049", ".077")
            assert inside(vr, ".1", ".4")
        else:
            assert inside(ht, "-.108", "-.020") and inside(hv, "-.051", "-.019")
            assert inside(vr, ".27", ".49")
        br, bh = map(F, row["outside_coordinate_rational"])
        assert (br, bh) == ((F(7, 20), -F(1, 100)) if beta == 0 else (F(3, 10), -F(13, 250)))
        assert F(11, 50) <= br <= F(9, 20) and -F(3, 25) <= bh <= F(2, 25)
        assert [branch["nu"] for branch in row["branches"]] == [1, 0]
        fac, forced = row["branches"]
        As, At = interval(row["force_s"]), interval(row["force_t"])
        Aa1, Aa0 = interval(fac["force_a"]), interval(forced["force_a"])
        T1, T0 = interval(fac["lifted_reference_value"]), interval(forced["lifted_reference_value"])
        assert inside(As, 0, ".141") and inside(At, "-.255", 0)
        assert inside(Aa1, "-.255", 0) and inside(Aa0, 0, ".315")
        assert T1[1] < -F(463, 10000) and T0[1] < -F(109, 1000)
        assert F(1, 2)-s[1] > F(93, 500) and F(1, 2)-t[1] > F(3, 20)
        assert cv["force_intervals"] == {"s": row["force_s"], "t": row["force_t"], "a": fac["force_a"]}
        assert cv["factorial_trial_value"] == fac["lifted_reference_value"]
        assert ch["new_guards"] == {"T0": forced["lifted_reference_value"],
                                    "A_a0": forced["force_a"], "a_real": q["a"]["real"]}
        case_bounds = {
            "factorial": T1[1]+F(1, 320)+F(13, 1000)+Aa1[0]**2/8,
            "forced_full_P": T0[1]+F(1, 320)+F(13, 1000)+Aa0[1]*(F(9, 20)-a[0]),
        }
        assert all(case_bounds[k] < budgets[k] < -F(1, 50) for k in budgets)
        summaries.append({"beta": beta, "epsilon": eps, "source_index": index,
                          "source_case_sha256": row["source_case_sha256"],
                          "saved_guards_recomputed": True,
                          "canonical_existence_and_zero_lifts_inherited": True,
                          "terminal_reference_above_022_verified": True,
                          "upper_bounds_rational": {k: str(v) for k, v in case_bounds.items()}})
    return {"rational_witnesses": witnesses,
            "coarse_upper_bounds_rational": {k: str(v) for k, v in budgets.items()},
            "coarse_gap_reserves_above_1over50_rational":
                {k: str(-v-F(1, 50)) for k, v in budgets.items()},
            "canonical_cases": summaries, "canonical_reference_cases_checked": 4,
            "main_branch_bounds_checked": 8, "selected_height_rational": "1/100",
            "common_main_gap_rational": "1/50", "both_branches_bound_on_full_P": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), "fresh output required"
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs = dict(PINNED)
    inputs[own] = sha(ROOT/own)
    result = {"status": "checking", "proof_path": PROOF,
              "proof_sha256": inputs[PROOF], "source_path": SOURCE,
              "source_sha256": inputs[SOURCE], "checker_sha256": inputs[own],
              "input_sha256": inputs, "analytic_evaluations": 0,
              "old_checkers_or_evaluators_imported": 0,
              "primitive_or_reference_replays": 0,
              "new_full_terminal_source_gap_claimed": False,
              "uniform_reference_domain_sign_claimed": False,
              "finite_word_realization_claimed": False,
              "whole_word_or_global_knot_theorem_claimed": False}
    error = None
    try:
        result.update(verify(inputs))
        result["changed_inputs"] = [p for p, d in inputs.items() if sha(ROOT/p) != d]
        assert not result["changed_inputs"], result["changed_inputs"]
        result["status"] = "passed"
    except Exception as exc:
        error = exc
        result["status"] = "failed saved-data verification"
        result["error"] = {"type": type(exc).__name__, "message": str(exc)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "bindings": len(inputs),
                      "common_main_gap": result.get("common_main_gap_rational"),
                      "output_sha256": sha(args.output)}))
    if error is not None:
        raise error


if __name__ == "__main__":
    main()
