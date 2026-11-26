#!/usr/bin/env python3
"""Extract alias reserves on four unchanged canonical image rectangles.

Exact saved-data arithmetic only. No source/reference/analytic callback,
new partition, optimizer, target proposal or adaptive threshold.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_terminal_uniform_alias_reserves.md"
COVER = "repro/results/research-mixed-terminal-uniform-face-reserves.json"
COVER_PROOF = "notes/research_mixed_terminal_uniform_face_reserves.md"
COVER_CHECKER = "experiments/check_mixed_terminal_uniform_face_reserves.py"
REFINED = "repro/results/research-mixed-terminal-quadratic-residual-refinement.json"
OLD = "repro/results/research-mixed-terminal-canonical-face-reserve.json"
HELPER = "experiments/check_mixed_terminal_canonical_face_reserve.py"
AUDITS = {
    0: "repro/results/research-mixed-terminal-three-alias-reserve.json",
    1: "repro/results/research-mixed-terminal-four-alias-reserve.json",
}
REPLAYS = {
    0: "repro/results/research-mixed-terminal-three-aliases-replay.json",
    1: "repro/results/research-mixed-terminal-four-source-replay.json",
}
AUTHORS = {
    0: "repro/results/research-mixed-terminal-three-aliases-attempt01.json",
    1: "repro/results/research-mixed-terminal-four-source-stage4-attempt01.json",
}
PINNED = {
    PROOF: "c942ce53d48079e1a2aa0c9d087b7eb0c92c70de13685ba9b0d0f08a0b1bda8a",
    COVER: "37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3",
    COVER_PROOF: "b770a8d3c182c9936367c1f43edd2e74f483ffd5ead2d61fa44b85420109a363",
    COVER_CHECKER: "b631f8d2b23acab944fc8ab900c2a6dfcacd9da1922643f58919d4185ebb7a6d",
    REFINED: "2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331",
    OLD: "c85ef62dd25724f6bed335dc16982c2133e4f991a5badcd68e038a57b1a513aa",
    HELPER: "4cbeda03dfee69565262e5e25486d261f97e6cbc417934e7ed417f19d75cce04",
    "notes/research_mixed_terminal_canonical_source_domain.md":
        "d50929a1a1c02d034feb5ca5f9ebf6e6da70bd6b0a1eb4a67f67fd1108d18d11",
    "notes/research_mixed_terminal_concave_profile_envelope.md":
        "6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd",
    "notes/research_mixed_terminal_three_selected_height_completion.md":
        "e3fea31226612be459f23e8cec8773503e562799cced20b36efcc0e4cd70e186",
    "notes/research_mixed_terminal_four_selected_height_completion.md":
        "5b688d2adf67895f430a2fef77a5d98fcb8ac74846ebc2bbe1027cd6e3414127",
    "notes/research_mixed_terminal_reserved_plane_transfer.md":
        "0d4461c5b00e4f68dc00c0c1d6e824156c9c5050327eab70694f3cd21e714c70",
    "notes/research_mixed_terminal_three_alias_reserve.md":
        "8780ddc96481a15f6b75e54ed7311a7f4e6272c7969056c8f63265f7e5cb6d82",
    "notes/research_mixed_terminal_four_alias_reserve.md":
        "02619c9f58624475deb1b88d39125b907b37e97fa4d6b94a1573a4fe5a965eaa",
    "experiments/check_mixed_terminal_three_alias_reserve.py":
        "af6b799894e33c13971adc6e2a386cd564001f417ba5aba740969761121a203c",
    "experiments/check_mixed_terminal_four_alias_reserve.py":
        "b23f5e5067d4405f5b34a434377784b24c40d8e298170e9d147c66e4029a7f0f",
    AUDITS[0]: "039094505d49f8736485224fceaf280de836bba635301b1fa669e51c2d9fd483",
    AUDITS[1]: "6ff887ab81798ea4e237dfaf39cbd99f17cfecda367bc4e551f92ea61da351d0",
    REPLAYS[0]: "3b2b017023020d8ea2dce6ff7e5a429f87a0871a339467a2f0734454af4523f5",
    REPLAYS[1]: "3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79",
    AUTHORS[0]: "fc04d56f297524fc252dd0e0f131db11000d7490ec77a3b5300811cebb8e41cf",
    AUTHORS[1]: "e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3",
}
THREE_FAMILIES = [
    ["t", "-3/25", "0", "0", "0"], ["t", "-3/25", "0", "0", "1"],
    ["t", "3/25", "0", "0", "0"], ["t", "3/25", "0", "0", "1"],
    ["u", "0", "-3/25", "0", "0"], ["u", "0", "-3/25", "1", "0"],
    ["u", "0", "3/25", "0", "0"], ["u", "0", "3/25", "1", "0"],
    ["both", "-3/25", "-3/25", "0", "0"], ["both", "-3/25", "3/25", "0", "0"],
    ["both", "3/25", "-3/25", "0", "0"], ["both", "3/25", "3/25", "0", "0"],
]
FOUR_FAMILIES = (
    [["t_alias", None, None, h, "0", "0", retain]
     for h in ("-3/25", "3/25") for retain in ("0", "1")]
    + [["e_alias", None, None, "0", h, retain, "0"]
       for h in ("-11/200", "1/25") for retain in ("0", "1")]
    + [["double_alias", None, None, t, e, "0", "0"]
       for t in ("-3/25", "3/25") for e in ("-11/200", "1/25")]
)
LABELS = [
    ("-", "0", 1), ("-", "L", 0), ("-", "R", 0),
    ("+", "0", 3), ("+", "L", 2), ("+", "R", 2),
    ("0", "-", 5), ("L", "-", 4), ("R", "-", 4),
    ("0", "+", 7), ("L", "+", 6), ("R", "+", 6),
    ("-", "-", 8), ("-", "+", 9), ("+", "-", 10), ("+", "+", 11),
]
HEIGHT_DEBIT = F(41, 1000)
CASES = [(0, 0), (0, 1), (1, 0), (1, 1)]


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(",", ":")).encode()).hexdigest()


def interval(value):
    if "finite" in value:
        assert value["finite"] is True
    result = F(value["lower_rational"]), F(value["upper_rational"])
    assert result[0] <= result[1]
    return result


def encoded(box):
    return [[str(lo), str(hi)] for lo, hi in box]


def forbidden(*args, **kwargs):
    raise AssertionError("old extraction main is forbidden")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if any(value is None for value in PINNED.values()):
        raise AssertionError("all reviewed protocol pins must be frozen")
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    result = dict(
        status="initializing", proof_path=PROOF, proof_sha256=inputs[PROOF],
        checker_path=own, checker_sha256=inputs[own],
        image_cover_path=COVER, image_cover_sha256=inputs[COVER],
        refinement_sha256=inputs[REFINED], input_sha256=inputs, cases=[],
        selected_height_rational="1/100", height_debit_rational=str(HEIGHT_DEBIT),
        counts=dict(canonical_cases=0, source_family_cases=0, alias_label_cases=0,
            selected_job_reads=0, inherited_three_alias_jobs=0,
            inherited_four_alias_jobs=0, inherited_all_four_source_jobs=0,
            new_parameter_cells=0, subdivisions=0, source_replays=0,
            roots=0, analytic_evaluations=0, target_proposals=0, retries=0),
        all_uniform_alias_bounds_defined=False, uniform_joined_sign_claimed=False,
        complete_terminal_kernel_proved=False, knot_theorem_proved=False,
    )
    error = None
    try:
        def bind(name, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest

        def inherited(data):
            for key in ("input_sha256", "dependencies_sha256", "dependencies"):
                values = data.get(key)
                if isinstance(values, dict):
                    for name, digest in values.items():
                        bind(name, digest)

        for name, digest in list(inputs.items()):
            bind(name, digest)
        cover, refined, old = [json.loads((ROOT/path).read_text())
                               for path in (COVER, REFINED, OLD)]
        audits = {eps: json.loads((ROOT/path).read_text()) for eps, path in AUDITS.items()}
        for saved in (cover, refined, old, *audits.values()):
            inherited(saved)
        for saved in (cover, refined, old):
            assert saved["changed_inputs"] == []
        assert cover["status"] == "completed fixed saved-only extraction"
        assert cover["checker_sha256"] == inputs[COVER_CHECKER]
        assert cover["proof_sha256"] == inputs[COVER_PROOF]
        assert cover["source_sha256"] == inputs[REFINED]
        assert cover["inherited_all_job_audit_sha256"] == inputs[OLD]
        assert cover["all_uniform_bare_bounds_defined"] is True
        assert cover["counts"]["required_face_families"] == 36
        assert cover["counts"]["selected_job_reads"] == 1719
        assert old["status"] == "completed saved-only extraction"
        assert old["checker_sha256"] == inputs[HELPER]
        assert old["source_summary_counts"]["four"]["all_jobs_checked"] == 40131
        assert refined["status"] == "completed fixed saved-only protocol"
        assert [(c["beta"], c["epsilon"]) for c in cover["cases"]] == CASES
        assert [(c["beta"], c["epsilon"]) for c in refined["cases"]] == CASES
        assert audits[0]["status"] == audits[1]["status"] == "passed"
        assert audits[0]["final_bindings_verified"] is audits[1]["final_bindings_verified"] is True
        assert audits[0]["jobs"] == 40164 and audits[0]["family_counts"] == [3347]*12
        assert audits[1]["alias_jobs"] == 22932 and audits[1]["family_counts"] == [1911]*12
        assert audits[1]["jobs_with_source_bounds"] == 21936
        assert audits[1]["jobs_only_excluded"] == 996
        assert audits[0]["gap"] == audits[1]["gap"] == "1/10"
        result["counts"]["inherited_three_alias_jobs"] = 40164
        result["counts"]["inherited_four_alias_jobs"] = 22932
        result["counts"]["inherited_all_four_source_jobs"] = 40131

        # Frozen helper has stdlib definitions only. Reconstruct exact geometry,
        # not original source bounds, and forbid its execution routine.
        spec = importlib.util.spec_from_file_location("frozen_terminal_partition", ROOT/HELPER)
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        helper.main = forbidden
        for name, digest in helper.PINNED.items():
            bind(name, digest)
        roots, root_replay = [json.loads((ROOT/path).read_text())
                             for path in (helper.ROOT_AUTHOR, helper.ROOT_REPLAY)]
        cells, excluded, partition = helper.root_cells(roots, root_replay)
        assert partition == cover["original_partition"] == old["original_partition"]
        result["original_partition"] = partition

        replays = {eps: json.loads((ROOT/path).read_text()) for eps, path in REPLAYS.items()}
        summaries = {}
        for eps, replay in replays.items():
            inherited(replay)
            assert replay["status"] == "passed" and replay["active"] is None
            assert replay["fatal_error"] is None and replay["final_bindings_verified"] is True
            assert replay["input_sha256"] == inputs[AUTHORS[eps]]
            assert replay["precision_bits"] == 320
            cell_count, family_count = (3347, 12) if eps == 0 else (1911, 21)
            assert replay["original_own_three_cells" if eps == 0 else "original_own_four_cells"] == cell_count
            assert replay["face_families_per_cell"] == family_count
            assert replay["job_count"] == cell_count*family_count
            assert len(cells[eps]) == cell_count
            inventory = replay["family_inventory"]
            assert (inventory if eps == 0 else inventory[8:20]) == (
                THREE_FAMILIES if eps == 0 else FOUR_FAMILIES)
            summaries[eps] = replay["replay_summaries"]
            assert len(summaries[eps]) == cell_count*family_count
            assert all(row["job"] == i for i, row in enumerate(summaries[eps]))
            if eps == 0:
                assert all(row["maximum_upper"] is not None for row in summaries[eps])
            else:
                assert sum(row["maximum_upper"] is None for i, row in enumerate(summaries[eps])
                           if 8 <= i % 21 < 20) == 996
            result.setdefault("source_inventory", []).append(dict(epsilon=eps,
                replay_path=REPLAYS[eps], replay_sha256=inputs[REPLAYS[eps]],
                original_cell_count=cell_count, families_per_cell=family_count,
                local_alias_family_inventory=THREE_FAMILIES if eps == 0 else FOUR_FAMILIES))

        all_states = ("0", "L", "R", "-", "+")
        expected_labels = {p for p in product(all_states, repeat=2)
                           if "-" in p or "+" in p}
        assert len(LABELS) == 16
        assert {(t, v) for t, v, _ in LABELS} == expected_labels
        assert {k for _, _, k in LABELS} == set(range(12))

        for index, ((beta, eps), prior, reference) in enumerate(
                zip(CASES, cover["cases"], refined["cases"])):
            assert prior["refinement_case_canonical_sha256"] == canonical_sha(reference)
            q = reference["coordinate_enclosures"]["a"]
            abox = (interval(q["real"]), interval(q["imag"]))
            assert encoded(abox) == prior["physical_a_box_rational"]
            assert all(lo < hi for lo, hi in abox)
            assert F(".22") < abox[0][0] < abox[0][1] < F(".45")
            assert -F(".108") < abox[1][0] < abox[1][1] < -F(".001")
            assert helper.rectangle_in_disk(abox, helper.DISKS[1][:2], helper.DISKS[1][2])
            assert all(helper.intersect(abox, box) is None for box in excluded[eps])
            selected = [cell for cell in cells[eps] if cell["neighbor"] == 1
                        and helper.intersect(abox, cell["physical"]) is not None]
            assert len(selected) == (72, 49, 45, 25)[index]
            pieces = [helper.intersect(abox, cell["physical"]) for cell in selected]
            assert sum(map(helper.area, pieces)) == helper.area(abox)
            selected_records = []
            for cell, piece in zip(selected, pieces):
                selected_records.append(dict(
                    **{key: cell[key] for key in ("index", "domain", "node", "neighbor",
                        "address", "depth", "original_node_canonical_sha256")},
                    normalized_box=encoded(cell["box"]), physical_box=encoded(cell["physical"]),
                    intersection=encoded(piece)))
            assert selected_records == prior["intersecting_original_cells"]
            assert str(helper.area(abox)) == prior["covered_area_rational"] == prior["enclosure_area_rational"]
            case = dict(beta=beta, epsilon=eps, endpoint_neighbor_epsilon=1,
                image_cover_case_canonical_sha256=canonical_sha(prior),
                refinement_case_canonical_sha256=canonical_sha(reference),
                physical_a_box_rational=encoded(abox),
                covered_area_rational=str(sum(map(helper.area, pieces))),
                enclosure_area_rational=str(helper.area(abox)),
                intersecting_original_cells=selected_records, families=[], alias_labels=[],
                source_scope="canonical external K"+str(3+beta)+" with original endpoint source conditions",
                independent_image_rectangle_source_feasible_claimed=False)
            result["cases"].append(case)
            result["counts"]["canonical_cases"] += 1
            for local in range(12):
                family = local if eps == 0 else 8+local
                family_count = 12 if eps == 0 else 21
                contributions, nulls = [], []
                for cell in selected:
                    job = family_count*cell["index"]+family
                    summary = summaries[eps][job]
                    assert summary["job"] == job
                    raw = summary["maximum_upper"]
                    value = None if raw is None else helper.outward_saved_upper(raw)
                    assert value is None or value < -F(1, 10)
                    contributions.append(dict(job=job, original_cell_index=cell["index"],
                        summary_canonical_sha256=canonical_sha(summary),
                        saved_maximum_upper=raw,
                        decoded_upper_rational=None if value is None else str(value)))
                    if value is None:
                        nulls.append(job)
                    result["counts"]["selected_job_reads"] += 1
                finite = [F(c["decoded_upper_rational"]) for c in contributions
                          if c["decoded_upper_rational"] is not None]
                observed = max(finite) if finite else None
                complete = not nulls and observed is not None
                allocated = observed+HEIGHT_DEBIT if complete else None
                case["families"].append(dict(local_family=local, source_family=family,
                    source_replay=REPLAYS[eps],
                    source_family_definition=(THREE_FAMILIES if eps == 0 else FOUR_FAMILIES)[local],
                    contributing_jobs=contributions, null_jobs_unresolved=nulls,
                    complete_finite_coverage=complete,
                    observed_finite_maximum_rational=None if observed is None else str(observed),
                    uniform_bare_upper_rational=str(observed) if complete else None,
                    bare_reserve_rational=str(-observed) if complete else None,
                    allocated_upper_rational=None if allocated is None else str(allocated),
                    allocated_reserve_rational=None if allocated is None else str(-allocated),
                    attaining_jobs=[] if observed is None else [c["job"] for c in contributions
                        if c["decoded_upper_rational"] is not None and F(c["decoded_upper_rational"]) == observed]))
                result["counts"]["source_family_cases"] += 1
            for t_state, v_state, local in LABELS:
                family = case["families"][local]
                case["alias_labels"].append(dict(t_state=t_state, private_state=v_state,
                    local_family=local, source_family=family["source_family"],
                    complete_finite_coverage=family["complete_finite_coverage"],
                    uniform_bare_upper_rational=family["uniform_bare_upper_rational"],
                    allocated_upper_rational=family["allocated_upper_rational"],
                    allocated_reserve_rational=family["allocated_reserve_rational"]))
                result["counts"]["alias_label_cases"] += 1
            complete = all(f["complete_finite_coverage"] for f in case["families"])
            case["all_twelve_bare_bounds_defined"] = complete
            if complete:
                common = min(F(f["allocated_reserve_rational"]) for f in case["families"])
                assert common > F(59, 1000)
                case["common_allocated_reserve_rational"] = str(common)
                case["attaining_local_families"] = [f["local_family"] for f in case["families"]
                    if F(f["allocated_reserve_rational"]) == common]
            else:
                case["common_allocated_reserve_rational"] = None
                case["attaining_local_families"] = []
        assert result["counts"]["canonical_cases"] == 4
        assert result["counts"]["source_family_cases"] == 48
        assert result["counts"]["alias_label_cases"] == 64
        assert result["counts"]["selected_job_reads"] == 2292
        result["unresolved_family_cases"] = sum(not f["complete_finite_coverage"]
            for c in result["cases"] for f in c["families"])
        result["all_uniform_alias_bounds_defined"] = result["unresolved_family_cases"] == 0
        result["status"] = "completed fixed saved-only extraction"
    except Exception as exc:
        error = exc
        result["status"] = "failed saved-data extraction"
        result["error"] = dict(type=type(exc).__name__, message=str(exc))
    result["changed_inputs"] = [name for name, digest in inputs.items()
                                if sha(ROOT/name) != digest]
    if result["changed_inputs"]:
        result["status"] = "changed inputs"
        result["all_uniform_alias_bounds_defined"] = False
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, separators=(",", ":"))
        stream.write("\n")
    print(json.dumps(dict(status=result["status"], counts=result["counts"],
        all_uniform_alias_bounds_defined=result["all_uniform_alias_bounds_defined"],
        output_sha256=sha(args.output))))
    if error is not None:
        raise error
    if result["changed_inputs"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
