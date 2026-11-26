#!/usr/bin/env python3
"""Exact assembly of the all-word unaliased local open Gaussian.

Bind the two completed theorem/replay pairs and all inherited files;
check the common disks and complete reduced-disk trees without proposing
roots or rerunning their numerical acceptance tests.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_open_local_gaussian.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-open-local-gaussian.json")
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, records, primary, replays = {}, {}, {}, {}

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        bind(path)
        if path in records:
            return records[path]
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        nested = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in record.get(field, {}).items():
                assert name not in nested or nested[name] == digest, name
                nested[name] = digest
                bind(name, digest)
        for name in nested:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return record

    for stem, script in (
        ("open-local-factor-coverage", "check_mixed_open_local_factor_coverage"),
        ("reduced-disk-conditional-packets", "certify_mixed_reduced_disk_conditional_packets"),
    ):
        path = "repro/results/research-mixed-"+stem+".json"
        rp = path[:-5]+"-replay.json"
        author, saved = inherit(path), inherit(rp)
        assert author["status"] == saved["status"] == "passed"
        proof = "notes/research_mixed_"+stem.replace("-", "_")+".md"
        bind(proof, author["proof_sha256"])
        bind("experiments/"+script+".py", author["script_sha256"])
        assert saved["input_sha256"] == deps[path]
        assert saved["proof_sha256"] == author["proof_sha256"]
        assert saved["script_sha256"] == author["script_sha256"]
        primary[path], replays[rp] = deps[path], deps[rp]

    coverage = records["repro/results/research-mixed-open-local-factor-coverage.json"]
    coverage_replay = records["repro/results/research-mixed-open-local-factor-coverage-replay.json"]
    exact_copy = dict(coverage_replay)
    exact_copy["input_sha256"] = coverage["input_sha256"]
    assert exact_copy == coverage
    assert (coverage["endpoint_witnesses"], coverage["original_tree_nodes"],
            coverage["original_excluded_boxes"]) == (5258, 10978, 233)
    assert coverage["new_root_proposals"] == coverage["new_cover_cells"] == 0
    assert len(coverage["attached_disk_extraction"]) == 4
    assert {(v["own_type"], v["external_type"])
            for v in coverage["attached_disk_extraction"]} == {
                (3, 3), (3, 4), (4, 3), (4, 4)}
    for value in coverage["attached_disk_extraction"]:
        radius = F(".083") if value["own_type"] == 3 else F(".060")
        assert F(value["enclosing_radius"]) == radius
        assert F(value["maximum_attached_radius_upper"]) < radius
        assert F(value["minimum_squared_inclusion_reserve"]) > 0

    source = records["repro/results/research-mixed-reduced-disk-conditional-packets.json"]
    saved = records["repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"]
    specifications = [(eps, a, b) for eps in (0, 1)
                      for a, b in ((0, 0), (0, 1), (1, 1))]
    assert source["precision_bits"] >= 256 and saved["precision_bits"] >= 320
    for record in (source, saved):
        assert record["domain_count"] == 6 and record["orientations_per_domain"] == 2
        assert [tuple(d["types"]) for d in record["domains"]] == specifications
        assert [[F(x) for x in row] for row in record["parameter_disks"]] == [
            [F(".35"), F("-.01"), F(".083")],
            [F(".30"), F("-.052"), F(".060")]]
        assert F(record["real_cut_and_last_row_gap"]) == F(1, 1000)
        assert F(record["horizontal_alias_gap"]) == F(1, 10)
        assert F(record["right_tail_shape_upper"]) == 1
        assert list(map(F, record["middle_rectangle"])) == [
            F(".15"), F(".49"), -F(".20"), F(".20")]
        assert record["alias_intervals_per_side"] == 8
        assert record["tail_shape_intervals"] == 12
    leaves, nodes, per_domain = 0, 0, []
    for domain, replay_domain in zip(source["domains"], saved["domains"]):
        assert domain["tree"] == replay_domain["tree"]
        assert domain["leaves"] == replay_domain["leaves"]
        pending = [([(F(0), F(1)), (F(0), F(1))], 0)]
        cursor, accepted = 0, 0
        while pending:
            box, depth = pending.pop()
            node = domain["tree"][cursor]
            cursor += 1
            if node[0] == "S":
                assert len(node) == 2 and type(node[1]) is int and node[1] == depth % 2
                axis = node[1]
                lo, hi = box[axis]
                middle = (lo+hi)/2
                for interval in ((lo, middle), (middle, hi)):
                    child = list(box)
                    child[axis] = interval
                    pending.append((child, depth+1))
            else:
                assert node[0] == "L" and len(node) == 2
                assert len(node[1]["radii"]) == 2
                assert all(F(r) > 0 for r in node[1]["radii"])
                accepted += 1
        assert cursor == len(domain["tree"])
        assert accepted == domain["leaves"] and cursor == 2*accepted-1
        per_domain.append(accepted)
        leaves += accepted
        nodes += cursor
    assert per_domain == [1157, 1033, 960, 529, 406, 324]
    assert (leaves, nodes) == (4409, 8812)
    for record in (source, saved):
        assert (record["accepted_cells"], record["visited_nodes"]) == (leaves, nodes)

    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    ordered = [(eps, a, b) for eps in (0, 1) for a in (0, 1) for b in (0, 1)]
    check("six unordered products and both orientations cover all ordered local types",
          all((eps, min(a, b), max(a, b)) in specifications for eps, a, b in ordered))
    check("the reduced source disks equal the completed common nonprivate disks",
          [F(r) for r in ("83/1000", "3/50")] == [F(".083"), F(".060")])
    m, k, first, s, a, b, eps = sp.symbols("m k first s a b eps")
    chirp = lambda z: sp.I*sp.pi*z*(1-z)/2
    check("conditional phase chirps retain the original open action",
          sp.expand(chirp(s+a)+chirp(s+b)-(2+eps)*chirp(s)
                    -chirp(a)-chirp(b)+2*sp.I*sp.pi*a*s
                    -(sp.I*sp.pi*s*(a-b)-eps*chirp(s))) == 0)
    before = m+k-1-first/2-(m-1+k-first)/2-1-k/2
    check("all literal factor powers before outer integration",
          sp.expand(before-(m-3)/2) == 0)
    check("the original local Gaussian power is minus three halves",
          sp.expand(before-m/2+sp.Rational(3, 2)) == 0)
    check("one-vertex normalization uses no conditional factor",
          sp.expand(before.subs({m: 1, k: first})+1) == 0)
    check("the full dimension includes both ordinary endpoint auxiliaries",
          sp.expand((m+2)+m-(2*m+2)) == 0)
    check("one- and two-vertex words have no ordinary internal factors",
          max(1-2, 0) == max(2-2, 0) == 0)

    result = dict(status="passed", arithmetic="exact rational and symbolic",
        checks=checks, exact_check_count=len(checks), primary_records=primary,
        saved_replays=replays, inherited_endpoint_witnesses=5258,
        source_type_families=6, ordered_local_type_cases=len(ordered),
        source_orientations_per_family=2, source_cells=leaves,
        source_tree_nodes=nodes, source_cells_by_family=per_domain,
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        dependencies_sha256=deps, new_root_proposals=0, new_cover_cells=0,
        written_inputs=["Every ordinary external leg is nonprivate, including either buffer endpoint.",
                        "Original block uniqueness identifies the actual conditional graph.",
                        "Completed source germs and the complex Schur lemma give the local Gaussian."],
        scope="Every fixed open 3/4 word: nonzero UNALIASED LOCAL N^-3/2 Gaussian and ordinary-color germs. No full outgoing contour, selected-alias suppression, boundary-strip theorem, volume identification, or short-filling conclusion.")
    if old is not None:
        expected = dict(result)
        expected["input_sha256"] = old.get("input_sha256")
        assert expected == old
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact;", len(primary), "primary;", len(replays),
          "saved replays;", leaves, "inherited source cells;", len(deps), "bindings")


if __name__ == "__main__":
    main()
