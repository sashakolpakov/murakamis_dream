#!/usr/bin/env python3
"""Check the terminal constant profile using saved heights and plane ceilings.

Standard library and exact fractions only; no gain routine, primitive,
root, reference, optimizer, source or parameter evaluation.
"""
import argparse
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_terminal_uniform_constant_profile.md"
PLANE = "repro/results/research-mixed-terminal-uniform-joined-plane.json"
PLANE_PROOF = "notes/research_mixed_terminal_uniform_joined_plane.md"
PLANE_CHECKER = "experiments/check_mixed_terminal_uniform_joined_plane.py"
REFINED = "repro/results/research-mixed-terminal-quadratic-residual-refinement.json"
PINNED = {
    PROOF: "1aff3730e96efe0f62e00a44247150de54ac4d5f93eeed436a94952d89a60c96",
    PLANE: "4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88",
    PLANE_PROOF: "12ab4cd4e94a521ac97da4e8f71aa68b2352764cd2d283cf123e9f5f113b11e5",
    PLANE_CHECKER: "35fbf2b1a3d2722f1c930cf21704a3121ed0460e621fdfe9420f2b679f39dd16",
    REFINED: "2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331",
    "notes/research_mixed_terminal_canonical_source_domain.md":
        "d50929a1a1c02d034feb5ca5f9ebf6e6da70bd6b0a1eb4a67f67fd1108d18d11",
    "notes/research_mixed_terminal_selected_height_rows.md":
        "f282382e106a7669592ae5bf2755c307613a72780b957e3966e5b21ba9bb03e3",
    "notes/research_mixed_terminal_three_selected_height_completion.md":
        "e3fea31226612be459f23e8cec8773503e562799cced20b36efcc0e4cd70e186",
    "notes/research_mixed_terminal_concave_profile_envelope.md":
        "6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd",
    "notes/research_mixed_terminal_reserved_plane_transfer.md":
        "0d4461c5b00e4f68dc00c0c1d6e824156c9c5050327eab70694f3cd21e714c70",
}
HEIGHT_FLOORS = [-F(531, 10000), -F(60711, 1000000)]
PLANE_CEILINGS = [F(617, 10000), F(709, 10000)]
COARSE_RESERVES = [F(21909, 250000), F(2107179, 25000000)]
COARSE_DEFICITS = [F(6484, 250000), F(334679, 25000000)]


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
    lo, hi = F(value["lower_rational"]), F(value["upper_rational"])
    assert lo <= hi
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    result = dict(
        status="initializing", proof_path=PROOF, proof_sha256=inputs[PROOF],
        checker_path=own, checker_sha256=inputs[own], input_sha256=inputs,
        source_plane_path=PLANE, source_plane_sha256=inputs[PLANE],
        refinement_path=REFINED, refinement_sha256=inputs[REFINED],
        beta=1, external_source_domain="K4 with original canonical source eligibility",
        selected_height_rational="1/100", raw_constant_profile_rational="879/1000",
        original_bare_plane_lower_rational="99/100",
        halfweight_debit_coefficient_rational="11/25",
        common_raw_gap_rational="1/100", finite_gap_rational="1/200",
        cases=[], counts=dict(cases=0, branches=0, saved_vertex_totals=0,
            analytic_callbacks=0, gain_evaluations=0, roots=0,
            reference_evaluations=0, source_replays=0,
            optimizer_evaluations=0, subdivisions=0, retries=0),
        uniform_constant_profile_gap_proved=False,
        complete_terminal_kernel_proved=False, knot_theorem_proved=False,
    )
    error = None
    try:
        def bind(path, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert path not in inputs or inputs[path] == digest, path
            assert sha(ROOT/path) == digest, path
            inputs[path] = digest

        for path, digest in list(inputs.items()):
            bind(path, digest)
        plane, refined = [json.loads((ROOT/path).read_text())
                          for path in (PLANE, REFINED)]
        for saved in (plane, refined):
            assert saved["changed_inputs"] == []
            for key in ("input_sha256", "dependencies_sha256"):
                for path, digest in saved.get(key, {}).items():
                    bind(path, digest)
        assert plane["status"] == refined["status"] == "completed fixed saved-only protocol"
        assert plane["uniform_plane_ceilings_proved"] is True
        assert plane["proof_sha256"] == inputs[PLANE_PROOF]
        assert plane["checker_sha256"] == inputs[PLANE_CHECKER]
        assert plane["input_sha256"][REFINED] == inputs[REFINED]
        assert [(c["beta"], c["epsilon"]) for c in plane["cases"]] == [(1, 0), (1, 1)]
        assert [(c["beta"], c["epsilon"]) for c in refined["cases"]] == [
            (0, 0), (0, 1), (1, 0), (1, 1)]
        assert plane["counts"]["force_vertices"] == 48
        assert plane["counts"]["scalar_cubic_gains"] == 96
        assert plane["counts"]["independent_gain_checks"] == 96
        assert F(7, 50)*F(22, 7) == F(11, 25)
        assert F(99, 100)-F(879, 1000) == F(111, 1000)
        all_uppers = []
        for eps, old in enumerate(plane["cases"]):
            reference = refined["cases"][2+eps]
            assert old["status"] == "enclosed both joined-plane alternatives"
            assert old["refinement_case_canonical_sha256"] == canonical_sha(reference)
            assert reference["exact_linear_system_verified"] is True
            assert tuple(map(F, reference["parameter_center"])) == (F(3, 10), -F(13, 250))
            assert F(reference["parameter_radius_rational"]) == F(8, 125)
            c_lo, c_hi = interval(reference["coordinate_enclosures"]["a"]["imag"])
            assert HEIGHT_FLOORS[eps] <= c_lo <= c_hi < 0
            reserve = F(111, 1000)+F(11, 25)*c_lo
            coarse_reserve = F(111, 1000)+F(11, 25)*HEIGHT_FLOORS[eps]
            assert coarse_reserve == COARSE_RESERVES[eps]
            assert coarse_reserve-PLANE_CEILINGS[eps] == COARSE_DEFICITS[eps]
            assert COARSE_DEFICITS[eps] > F(1, 100)
            row = dict(beta=1, epsilon=eps,
                source_plane_case_canonical_sha256=canonical_sha(old),
                refinement_case_canonical_sha256=canonical_sha(reference),
                incoming_reference_height_rational=[str(c_lo), str(c_hi)],
                coarse_height_floor_rational=str(HEIGHT_FLOORS[eps]),
                coarse_plane_ceiling_rational=str(PLANE_CEILINGS[eps]),
                halfweight_debit_upper_rational=str(-F(11, 25)*c_lo),
                allocated_reserve_lower_rational=str(reserve),
                coarse_allocated_reserve_rational=str(coarse_reserve),
                coarse_joined_deficit_lower_rational=str(COARSE_DEFICITS[eps]),
                branches=[])
            result["cases"].append(row)
            result["counts"]["cases"] += 1
            assert [b["nu"] for b in old["branches"]] == [1, 0]
            for branch in old["branches"]:
                nu = branch["nu"]
                vertices = branch["vertices"]
                assert [v["endpoint_bits"] for v in vertices] == [
                    list(bits) for bits in product((0, 1), repeat=3 if nu else 4)]
                totals = []
                for vertex in vertices:
                    total = F(branch["trial_upper_rational"])+F(vertex["gain_sum_upper_rational"])
                    assert total == F(vertex["plane_upper_rational"])
                    totals.append(total)
                    result["counts"]["saved_vertex_totals"] += 1
                upper = max(totals)
                assert upper == F(branch["uniform_plane_upper_rational"])
                assert branch["attaining_vertices"] == [
                    v["endpoint_bits"] for v, total in zip(vertices, totals) if total == upper]
                assert upper < PLANE_CEILINGS[eps]
                joined = upper-reserve
                assert joined < -F(1, 100)
                all_uppers.append(joined)
                row["branches"].append(dict(nu=nu,
                    source_branch_canonical_sha256=canonical_sha(branch),
                    plane_upper_rational=str(upper),
                    allocated_reserve_lower_rational=str(reserve),
                    joint_defect_upper_rational=str(joined),
                    strict_deficit_lower_rational=str(-joined),
                    below_requested_gap=True))
                result["counts"]["branches"] += 1
        assert result["counts"]["cases"] == 2
        assert result["counts"]["branches"] == 4
        assert result["counts"]["saved_vertex_totals"] == 48
        assert max(F(branch["uniform_plane_upper_rational"])
            for case in plane["cases"] for branch in case["branches"]) == F(plane["common_plane_upper_rational"])
        result["common_exact_deficit_lower_rational"] = str(-max(all_uppers))
        result["uniform_constant_profile_gap_proved"] = True
        result["status"] = "passed"
    except Exception as exc:
        error = exc
        result["status"] = "failed saved-data comparison"
        result["error"] = dict(type=type(exc).__name__, message=str(exc))
    result["changed_inputs"] = [path for path, digest in inputs.items()
                                if sha(ROOT/path) != digest]
    if result["changed_inputs"]:
        result["status"] = "changed inputs"
        result["uniform_constant_profile_gap_proved"] = False
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, separators=(",", ":"))
        stream.write("\n")
    print(json.dumps(dict(status=result["status"], counts=result["counts"],
        uniform_constant_profile_gap_proved=result["uniform_constant_profile_gap_proved"],
        common_raw_gap_rational="1/100", output_sha256=sha(args.output))))
    if error is not None:
        raise error
    if result["changed_inputs"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
