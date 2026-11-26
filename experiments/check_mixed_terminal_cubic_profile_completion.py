#!/usr/bin/env python3
"""Recombine saved four-reference terminal bounds with proved cubic costs.

Standard library only. No analytic, root, interval or source evaluator.
The legacy all-profile checker remains the authority for its source-cell
extraction; every inherited file hash is verified before and after this pass.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINAL = "repro/results/research-mixed-terminal-all-profile-completion.json"
PLANE = "repro/results/research-mixed-terminal-reserved-plane-transfer.json"
CURVATURE = "repro/results/research-mixed-terminal-joint-main-curvature-budget.json"
COMMON = "repro/results/research-mixed-terminal-joint-main-common-height.json"
ORIGINAL = "repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json"
PROOF = "notes/research_mixed_terminal_cubic_cost_and_response_bounds.md"
ASSEMBLY = "notes/research_mixed_terminal_cubic_profile_completion.md"
PINNED = {
    FINAL: "6db1882f7a090f3aa02ca7c6f44c3cfd5b6ef39e4ef39f8049288f9bed73d2df",
    PLANE: "b9ce042d50911acbd5e87fa755a5b9a50393845035b3dba984c07f7e6d759ffe",
    CURVATURE: "12677b1d1b20ece4ffe61c7a370cf54b3c98233fb81f082e0220435b30a89495",
    COMMON: "53789515f1b33ffe9397c7a4405be7bcaa3db865267ad1e7da0495399c691cba",
    ORIGINAL: "2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9",
    PROOF: "dfc3f415e742aa9c632707aea7c699bb2ccbdc054c08fc7ba640e943bcdaa741",
    "experiments/check_mixed_terminal_all_profile_completion.py":
        "29a7e4320159928c87d9af198edbb4de061651f2b95553a0cf673d6e39828e37",
    "notes/research_mixed_terminal_all_profile_completion.md":
        "dd6fe0212bbaf450680a65d33114d30ed5203aeeaf25956d7d070bb44046daa3",
    "notes/research_mixed_terminal_one_parameter_transport.md":
        "1fdc3b445ea4a43319f16eeee20e739d608d7133b5471ccb40042174affefddd",
    "notes/research_mixed_terminal_full_input_index_barrier.md":
        "45ae03bf28a78df930fc8e7c97054ca40689630423a4d36c0009b6b0bb900ee2",
    "notes/research_stationary_reduced_boundary_energy.md":
        "ba7c1846e9466bcda3bd8860e9bc1f62ca7a16f4e30159d7697d90cfd95908bc",
    ASSEMBLY: "25ee5e1514475fbbd582c2a940b2a7de819187d6705e4613df7bdeded1be0140",
}


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            digest.update(chunk)
    return digest.hexdigest()


def interval(value):
    assert value["finite"] is True
    lo, hi = F(value["lower_rational"]), F(value["upper_rational"])
    assert lo <= hi
    return lo, hi


def inside(value, lo, hi):
    return F(lo) < value[0] <= value[1] < F(hi)


def association(row):
    return (row["beta"], row["epsilon"], row["source_index"],
            row["source_case_sha256"])


def cubic_witnesses():
    # The scalar curvature proof's four cosh and coefficient margins.
    pi_lo = F(157, 50)
    args = (F(594, 875), F(671, 1750), F(363, 875), F(11, 175))
    c = (F(31, 25), F(43, 40), F(109, 100), F(101, 100))
    K = (F(44, 5), F(19, 2), F(47, 5), F(49, 5))
    cosh_reserves = [cc - (1 + q*q/2/(1-q*q/12))
                     for q, cc in zip(args, c)]
    coefficient_reserves = [2*pi_lo*pi_lo/(1+cc)-kk
                            for cc, kk in zip(c, K)]
    assert cosh_reserves == [F(3441, 9202775), F(841437, 1451990360),
                             F(813393, 301857700), F(294779, 36737900)]
    assert coefficient_reserves == [F(9, 2800), F(67, 20750),
                                    F(183, 5225), F(53, 5025)]
    angle = F(176, 175)
    sine_margin = F(1, 24)-7*angle*angle/240
    assert sine_margin == F(2129, 175000) > 0
    cot_margin = 2-3*(2*angle)**2/16-F(31, 25)
    assert cot_margin == F(43, 30625) > 0

    q, d, k, x = F(141, 1000), F(93, 500), F(19, 2), F(29, 250)
    assert 0 < x < d and q < k*d*d/2
    p = q*x-k*d*x*x/2+k*x**3/6
    slope = q-k*d*x+k*x*x/2
    s_tangent = p-slope*x
    assert slope == -F(7, 125000)
    assert s_tangent == F(2604577, 375000000) < F(7, 1000)

    q, d, k, x = F(51, 200), F(3, 20), F(47, 5), F(51, 400)
    p = q*x-k*d*x*x/2-k*x**3/6
    slope = q-k*d*x-k*x*x/2
    t_tangent = p-slope*x
    assert slope == -F(1887, 1600000)
    assert t_tangent == F(5745609, 320000000) < F(9, 500)
    return {
        "cosh_reserves": list(map(str, cosh_reserves)),
        "curvature_coefficient_reserves": list(map(str, coefficient_reserves)),
        "sine_polynomial_margin": str(sine_margin),
        "cotangent_comparison_margin": str(cot_margin),
        "s_tangent_upper_rational": str(s_tangent),
        "t_tangent_upper_rational": str(t_tangent),
        "new_s_gain_upper_rational": "7/1000",
        "new_t_gain_upper_rational": "9/500",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    assert all(isinstance(d, str) and len(d) == 64 for d in PINNED.values())
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    for path, digest in inputs.items():
        assert sha(ROOT/path) == digest, path
    records = {path: json.loads((ROOT/path).read_text())
               for path in (FINAL, PLANE, CURVATURE, COMMON, ORIGINAL)}
    final, plane, curvature, common, original = [
        records[path] for path in (FINAL, PLANE, CURVATURE, COMMON, ORIGINAL)]
    # Merge every inherited binding, checking collisions before hashing.
    for record in records.values():
        assert record["changed_inputs"] == []
        for path, digest in record["input_sha256"].items():
            assert path not in inputs or inputs[path] == digest, path
            inputs[path] = digest
    for path, digest in inputs.items():
        assert sha(ROOT/path) == digest, path
    assert final["status"] == "passed"
    assert final["checker_sha256"] == inputs[
        "experiments/check_mixed_terminal_all_profile_completion.py"]
    assert final["assembly_sha256"] == inputs[
        "notes/research_mixed_terminal_all_profile_completion.md"]
    assert final["completed_terminal_labels_per_case"] == [27]*4
    assert final["face_cases_recombined"] == 36
    assert final["complete_labeled_Fourier_comparisons"] == 216
    assert F(final["same_selected_height_rational"]) == F(1, 100)
    for key in ("uniform_reference_domain_claimed", "finite_word_realization_claimed",
                "whole_word_or_global_knot_theorem_claimed"):
        assert final[key] is False
    assert original["status"] == "complete fixed diagnostic"
    assert F(original["height_rational"]) == F(1, 100)
    for record in (plane, curvature, common):
        assert record["status"] == "passed"
        assert record["source_path"] == ORIGINAL
        assert record["source_sha256"] == inputs[ORIGINAL]
        assert record["canonical_reference_cases_checked"] == 4
    assert F(plane["selected_height_rational"]) == F(1, 100)
    assert F(common["initial_height_rational"]) == F(1, 100)
    assert common["both_branches_bound_on_full_P"] is True

    witnesses = cubic_witnesses()
    gs, gt = F(7, 1000), F(9, 500)
    old_coarse_s = F(19881, 1587200)
    assert F(curvature["coarse_gain_uppers_rational"][0]) == old_coarse_s
    old_coarse_plane = {k: F(v) for k, v in plane["coarse_plane_upper_rational"].items()}
    assert old_coarse_plane == {
        "factorial": F(19, 500)+old_coarse_s+F(127, 1000)**2/4,
        "forced": F(3, 500)+old_coarse_s+F(33, 200)*F(17, 100)}
    new_coarse_plane = {k: v-old_coarse_s+gs for k, v in old_coarse_plane.items()}
    assert max(new_coarse_plane.values()) < F(99, 2000)
    alias_gap = F(59, 1000)-max(new_coarse_plane.values())
    constant_gap = F(63, 1000)-max(new_coarse_plane.values())
    coarse_main = {
        "factorial": -F(463, 10000)+gs+gt+F(867, 80000),
        "forced_full_P": -F(109, 1000)+gs+gt+F(1071, 20000)}
    assert coarse_main == {"factorial": -F(837, 80000),
                           "forced_full_P": -F(609, 20000)}
    assert alias_gap > F(1, 125) and constant_gap > F(1, 125)
    assert all(v < -F(1, 100) for v in coarse_main.values())

    expected = list(itertools.product((0, 1), repeat=2))
    for rows in (final["canonical_cases"], plane["canonical_cases"],
                 curvature["canonical_cases"], common["canonical_cases"],
                 original["cases"]):
        assert [(r["beta"], r["epsilon"]) for r in rows] == expected
    results, face_bounds, private_bounds = [], [], []
    for index, (old, pl, cv, ch, row) in enumerate(zip(
            final["canonical_cases"], plane["canonical_cases"],
            curvature["canonical_cases"], common["canonical_cases"], original["cases"])):
        assert all(association(x) == association(row) for x in (old, pl, cv, ch))
        beta, eps = row["beta"], row["epsilon"]
        assert row["status"] == "both main-current bounds enclosed"
        assert row["ordinary_label_reduction_height_verified"] is True
        assert pl["original_height_and_source_guards_verified"] is True
        assert F(pl["selected_height_rational"]) == F(1, 100)
        q = row["actual_coordinate_enclosures"]
        assert all(q[name] == value for name, value in cv["coordinate_guards"].items())
        sr, ar, tr = [interval(q[n]["real"]) for n in ("s", "a", "t")]
        hs, ha, ht = [interval(q[n]["imag"]) for n in ("s", "a", "t")]
        assert inside(sr, ".28", ".314") and inside(ar, ".28", ".314")
        assert inside(tr, ".18", ".35")
        assert inside(hs, "-.102", "-.001") and inside(ha, "-.108", "-.001")
        assert max(map(abs, hs)) < F(61, 1000)
        assert max(map(abs, ht)) < F(33, 500)
        v = "xi" if eps == 0 else "e"
        assert inside(ht, "-.072", ".021") if eps == 0 else inside(ht, "-.108", "-.020")
        assert inside(interval(q[v]["real"]), ".1", ".4") if eps == 0 else inside(interval(q[v]["real"]), ".27", ".49")
        assert inside(interval(q[v]["imag"]), ".049", ".077") if eps == 0 else inside(interval(q[v]["imag"]), "-.051", "-.019")
        br, bh = map(F, row["outside_coordinate_rational"])
        assert (br, bh) == ((F(7, 20), -F(1, 100)) if beta == 0 else (F(3, 10), -F(13, 250)))
        assert F(11, 50) <= br <= F(9, 20) and F(-39, 500) <= bh <= F(21, 1000)
        assert [r["nu"] for r in row["branches"]] == [1, 0]
        fac, force = row["branches"]
        As, At = interval(row["force_s"]), interval(row["force_t"])
        Aa1, Aa0 = interval(fac["force_a"]), interval(force["force_a"])
        T1, T0 = interval(fac["lifted_reference_value"]), interval(force["lifted_reference_value"])
        assert inside(As, 0, ".141") and inside(At, "-.255", 0)
        assert inside(Aa1, "-.255", 0) and inside(Aa0, 0, ".315")
        assert T1[1] < -F(463, 10000) and T0[1] < -F(109, 1000)
        assert pl["Gs"] == row["force_s"] == cv["force_intervals"]["s"]
        assert row["force_t"] == cv["force_intervals"]["t"]
        assert force["force_a"] == ch["new_guards"]["A_a0"]
        assert force["lifted_reference_value"] == ch["new_guards"]["T0"]
        d = F(1, 2)-sr[1]
        assert d > F(93, 500)
        old_gs = 15*As[1]**2/(128*d)
        assert old_gs == F(pl["s_gain_upper_rational"])
        assert old_gs == F(cv["saved_input_gain_uppers_rational"][0])
        assert old_gs > gs  # This run records strict improvement in all four cases.
        Ga1, Ga0 = interval(pl["G_a1"]), interval(pl["G_a0"])
        J1, J0 = interval(pl["J1"]), interval(pl["J0"])
        assert inside(Ga1, "-.127", 0) and inside(Ga0, 0, ".165")
        assert J1[1] < F(19, 500) and J0[1] < F(3, 500)
        old_plane = {k: F(v) for k, v in pl["joined_plane_upper_rational"].items()}
        selected = {"factorial": Ga1[0]**2/4,
                    "forced": Ga0[1]*(F(9, 20)-ar[0])}
        assert selected == {k: F(v) for k, v in pl["selected_gain_upper_rational"].items()}
        assert old_plane == {"factorial": J1[1]+old_gs+selected["factorial"],
                             "forced": J0[1]+old_gs+selected["forced"]}
        new_plane = {k: value-old_gs+gs for k, value in old_plane.items()}
        assert all(new_plane[k] < new_coarse_plane[k] for k in new_plane)
        new_main = {"factorial": T1[1]+gs+gt+Aa1[0]**2/6,
                    "forced_full_P": T0[1]+gs+gt+Aa0[1]*(F(9, 20)-ar[0])}
        assert all(new_main[k] < coarse_main[k] for k in new_main)
        inventory = ([("three_mixed", i) for i in range(8)]+[("three_half", 0)]
                     if eps == 0 else [("four", i) for i in range(8)]+[("four", 20)])
        assert [(f["series"], f["family"]) for f in old["face_comparisons"]] == inventory
        faces = []
        for f in old["face_comparisons"]:
            raw = F(f["bare_upper_rational"])
            assert raw+max(old_plane.values()) == F(f["joined_upper_rational"])
            if eps == 1 and f["family"] == 2:
                assert raw < 0
                prior = final["new_private_left_face_bounds"][beta]
                assert association(prior) == association(row)
                assert F(prior["bare_face_upper_for_trial_offset_rational"]) == raw
                assert prior["original_t_force"] == row["force_t"]
                assert prior["coordinate_guards"] == {n: q[n] for n in ("t", "e")}
                assert prior["t_force_shift_strict_bounds_rational"] == ["0", "1/5"]
                assert inside(tr, ".304", ".308") and inside(interval(q["e"]["real"]), ".345", ".347")
                assert inside(ht, "-.066", "-.065") and inside(interval(q["e"]["imag"]), "-.038", "-.037")
                assert At[1] < -F(23, 100) and At[1]+F(1, 5) < 0
                upper = {k: value+raw for k, value in new_main.items()}
                assert all(value < -F(1, 125) for value in upper.values())
                private_bounds.append((max(upper.values()), (beta, eps)))
                mode = "direct private-left transfer with decreased negative t-force"
            else:
                upper = {k: value+raw for k, value in new_plane.items()}
                assert all(value < -F(1, 125) for value in upper.values())
                face_bounds.append((max(upper.values()), (beta, eps, f["series"], f["family"])))
                mode = "saved bare face plus improved reserved plane"
            faces.append({"series": f["series"], "family": f["family"], "mode": mode,
                          "bare_upper_rational": str(raw),
                          "new_branch_uppers_rational": {k: str(v) for k, v in upper.items()}})
        results.append({"beta": beta, "epsilon": eps, "source_index": row["source_index"],
                        "source_case_sha256": row["source_case_sha256"],
                        "old_s_gain_upper_rational": str(old_gs),
                        "new_s_gain_upper_rational": str(gs),
                        "new_t_gain_upper_rational": str(gt),
                        "old_plane_uppers_rational": {k: str(v) for k, v in old_plane.items()},
                        "new_plane_uppers_rational": {k: str(v) for k, v in new_plane.items()},
                        "new_main_uppers_rational": {k: str(v) for k, v in new_main.items()},
                        "face_comparisons": faces, "terminal_label_count": 27})
    assert len(face_bounds) == 34 and len(private_bounds) == 2
    worst, attaining = max(face_bounds)
    assert attaining == (1, 1, "four", 0)
    assert F(1, 125)-F(1, 1000)-F(1, 250) > 0
    changed = [path for path, digest in inputs.items() if sha(ROOT/path) != digest]
    result = {
        "status": "passed" if not changed else "input failure",
        "source_path": FINAL, "source_sha256": inputs[FINAL],
        "proof_path": PROOF, "proof_sha256": inputs[PROOF],
        "assembly_path": ASSEMBLY, "assembly_sha256": inputs[ASSEMBLY],
        "checker_sha256": inputs[own], "input_sha256": inputs,
        "changed_inputs": changed, "same_selected_height_rational": "1/100",
        "rational_witnesses": witnesses, "canonical_cases": results,
        "new_coarse_plane_uppers_rational": {k: str(v) for k, v in new_coarse_plane.items()},
        "new_coarse_main_uppers_rational": {k: str(v) for k, v in coarse_main.items()},
        "alias_endpoint_gap_lower_rational": str(alias_gap),
        "constant_profile_gap_lower_rational": str(constant_gap),
        "non_private_left_face_cases": len(face_bounds),
        "private_left_face_cases": len(private_bounds),
        "worst_recombined_face_upper_rational": str(worst),
        "attaining_case_family": list(attaining),
        "completed_terminal_labels_per_case": [27]*4,
        "complete_labeled_Fourier_comparisons": 216,
        "common_raw_profile_gap_rational": "1/125",
        "complete_finite_two_factor_kernel_gap_rational": "1/250",
        "analytic_evaluations": 0, "old_record_or_source_replays": 0,
        "uniform_reference_domain_claimed": False,
        "finite_word_realization_claimed": False,
        "whole_word_or_global_knot_theorem_claimed": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    assert not changed, changed
    print(json.dumps({"status": result["status"], "bindings": len(inputs),
                      "faces": len(face_bounds)+len(private_bounds),
                      "worst_face_upper": float(worst),
                      "labels": [27]*4, "raw_gap": "1/125", "finite_gap": "1/250",
                      "output_sha256": sha(args.output)}))


if __name__ == "__main__":
    main()
