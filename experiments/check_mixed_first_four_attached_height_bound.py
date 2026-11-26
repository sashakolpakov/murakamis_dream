#!/usr/bin/env python3
"""Bind the completed saved-box extraction; do not repeat its arithmetic.

No numerical source module is imported, no root is evaluated, and no
compatibility search is rerun. The verbatim raw program and its completed
output are immutable evidence, separately reviewed with the proof.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = "notes/research_mixed_first_four_attached_height_bound.md"
RAW_SCRIPT = "experiments/extract_mixed_first_four_attached_height_raw.py"
RAW_RECORD = "repro/results/research-mixed-first-four-attached-height-raw.json"
RAW_SCRIPT_SHA = "88f3a93a3154c5416f9978aedcf66845ee84429b1207f662a1e763e2fb559642"
RAW_RECORD_SHA = "af744080d271f208ff50351d8156902e0859be10293e8da1a243ccc718ed5e32"
IMAGE = "repro/results/research-mixed-cyclic-block-images.json.gz"
ORDINARY = "repro/results/research-mixed-cyclic-block-localization.json"
ORDINARY_REPLAY = "repro/results/research-mixed-cyclic-block-localization-replay.json"
ENDPOINT = "repro/results/research-mixed-open-word-critical-localization.json"
ENDPOINT_REPLAY = "repro/results/research-mixed-open-word-critical-localization-replay.json"
CASES = [[0, 0, 0], [0, 0, 1], [0, 1, 1],
         [1, 0, 0], [1, 0, 1], [1, 1, 1]]
EXPECTED = [
    ([0, 0, 1], 315, 192812, 0, 0, "-7/100"),
    ([0, 1, 1], 315, 165255, 0, 0, "-7/100"),
    ([1, 0, 1], 351, 72288, 491, 21,
     "-38608669884819457/500000000000000000"),
    ([1, 1, 1], 351, 50648, 275, 16,
     "-1505860369933393/20000000000000000"),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decode(address):
    lo, hi = [F(-1)]*4, [F(1)]*4
    for depth, bit in enumerate(address):
        assert bit in "01"
        axis = depth % 4
        midpoint = (lo[axis]+hi[axis])/2
        if bit == "0":
            hi[axis] = midpoint
        else:
            lo[axis] = midpoint
    return list(zip(lo, hi))


def outside_disk(box):
    return sum(min(a*a, b*b) if a*b > 0 else F(0)
               for a, b in box) > 1


def check_ordinary_cover(case):
    accepted, excluded = case["accepted"], case["excluded"]
    words = sorted(accepted+excluded)
    assert len(words) == len(set(words))
    assert all(not b.startswith(a) for a, b in zip(words, words[1:]))
    assert sum((F(1, 2**len(a)) for a in words), F(0)) == 1
    assert case["visited"] == 2*len(words)-1
    assert case["max_depth"] == max(map(len, words))
    for address in excluded:
        box = decode(address)
        assert outside_disk(box[:2]) or outside_disk(box[2:])


def check_endpoint_tree(domain):
    stack = [[(F(-1), F(1)), (F(-1), F(1))]]
    leaves = excluded = 0
    for node in domain["tree"]:
        assert stack
        box = stack.pop()
        if node[0] == "S":
            assert len(node) == 2 and type(node[1]) is int and node[1] in (0, 1)
            axis = node[1]
            a, b = box[axis]
            midpoint = (a+b)/2
            # The saved author uses left-then-right pushes: right first.
            for interval in ((a, midpoint), (midpoint, b)):
                child = list(box)
                child[axis] = interval
                stack.append(child)
        elif node[0] == "X":
            assert node == ["X"] and outside_disk(box)
            excluded += 1
        else:
            assert node[0] == "L" and len(node) == 2
            witness = node[1]
            assert F(witness["radius"]) > 0
            assert len(witness["centers"]) == 3
            assert all(len(center) == 2 for center in witness["centers"])
            for center in witness["centers"]:
                tuple(map(F, center))
            leaves += 1
    assert not stack
    assert leaves == domain["leaves"] and excluded == domain["excluded"]
    assert len(domain["tree"]) == 2*(leaves+excluded)-1
    return leaves, excluded, len(domain["tree"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-first-four-attached-height-bound.json")
    args = parser.parse_args()
    dependencies = {}
    proof_hash, script_hash = sha(ROOT/PROOF), sha(__file__)

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest
        dependencies[name] = digest
        return digest

    def record(name):
        bind(name)
        value = json.loads((ROOT/name).read_text())
        for field in ("dependencies", "dependencies_sha256"):
            for path, digest in value.get(field, {}).items():
                bind(path, digest)
        return value

    bind(RAW_SCRIPT, RAW_SCRIPT_SHA)
    bind(RAW_RECORD, RAW_RECORD_SHA)
    raw = json.loads((ROOT/RAW_RECORD).read_text())
    assert raw["arithmetic"] == "Exact Fraction compatibility of old full-dimensional boxes"
    assert raw["threshold"] == "-7/100"
    assert set(raw["inputs"]) == {IMAGE, ORDINARY, ENDPOINT}
    for name, digest in raw["inputs"].items():
        bind(name, digest)

    ordinary, replay = record(ORDINARY), record(ORDINARY_REPLAY)
    assert ordinary["status"] == replay["status"] == "passed"
    assert replay["input_sha256"] == dependencies[ORDINARY]
    bind("experiments/certify_mixed_cyclic_block_localization.py",
         ordinary["script_sha256"])
    bind("experiments/replay_mixed_cyclic_block_localization.py",
         replay["script_sha256"])
    for rec in (ordinary, replay):
        bind("notes/research_mixed_cyclic_critical_localization.md", rec["proof_sha256"])
    images = json.loads(gzip.decompress((ROOT/IMAGE).read_bytes()))
    assert images["status"] == "passed" and images["schema"] == "correlated-block-images-v1"
    assert images["author_record_sha256"] == dependencies[ORDINARY]
    bind("experiments/certify_mixed_cyclic_block_localization.py", images["source_sha256"])
    bind("experiments/extract_mixed_cyclic_block_images.py", images["script_sha256"])
    bind("notes/research_mixed_cyclic_critical_localization.md", images["proof_sha256"])
    assert images["columns"] == [
        "address", "center_complex_pairs", "linear_complex_pairs", "remainder_radii"]
    assert images["interpretation"] == (
        "z(p)=center+linear*(p-exact_parameter_midpoint)+w, |w_i|<=remainder_radii[i]. "
        "Inputs and midpoint decode from the frozen typed-disk address.")
    for rec in (ordinary, replay, images):
        assert len(rec["cases"]) == 6
        assert [case["types"] for case in rec["cases"]] == CASES
    ordinary_leaves = 0
    for k in range(6):
        case, rep, img = ordinary["cases"][k], replay["cases"][k], images["cases"][k]
        check_ordinary_cover(case)
        assert [row[0] for row in img["rows"]] == case["accepted"]
        assert rep["original_boxes"] == rep["replay_boxes"] == len(case["accepted"])
        assert rep["refinements"] == 0
        for address, centers, linear, radii in img["rows"]:
            assert len(centers) == len(linear) == len(radii) == 2
            assert all(len(z) == 2 for z in centers)
            assert all(len(row) == 2 and all(len(z) == 2 for z in row) for row in linear)
            assert all(F(radius) > 0 for radius in radii)
        ordinary_leaves += len(case["accepted"])
    assert ordinary_leaves == 156905

    endpoint, endpoint_replay = record(ENDPOINT), record(ENDPOINT_REPLAY)
    assert endpoint["status"] == endpoint_replay["status"] == "passed"
    assert endpoint_replay["input_sha256"] == dependencies[ENDPOINT]
    assert endpoint["domains"] == endpoint_replay["domains"]
    assert len(endpoint["domains"]) == 4
    assert [(d["epsilon"], d["neighbor_epsilon"]) for d in endpoint["domains"]] == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    for rec in (endpoint, endpoint_replay):
        bind("notes/research_mixed_open_word_critical_localization.md", rec["proof_sha256"])
        bind("experiments/certify_mixed_open_word_critical_localization.py", rec["script_sha256"])
    totals = [0, 0, 0]
    for domain in endpoint["domains"]:
        counts = check_endpoint_tree(domain)
        totals = [a+b for a, b in zip(totals, counts)]
    assert totals == [5258, 233, 10978]

    # Existing exact domain deductions, with their original saved replay.
    coverage = record("repro/results/research-mixed-open-local-factor-coverage.json")
    coverage_replay = record("repro/results/research-mixed-open-local-factor-coverage-replay.json")
    assert coverage["status"] == coverage_replay["status"] == "passed"
    assert coverage_replay["input_sha256"] == dependencies[
        "repro/results/research-mixed-open-local-factor-coverage.json"]
    for rec in (coverage, coverage_replay):
        bind("notes/research_mixed_open_local_factor_coverage.md", rec["proof_sha256"])
        bind("experiments/check_mixed_open_local_factor_coverage.py", rec["script_sha256"])
    for name in (
        "notes/research_mixed_actual_last_row_reference_domains.md",
        "notes/research_mixed_typed_last_row_envelopes.md",
        "notes/research_mixed_open_word_endpoint_rectangles.md",
        "notes/research_mixed_first_cap_oriented_plateau_certificate.md",
    ):
        bind(name)
    cap = record("repro/results/research-mixed-first-cap-coupled-plateau-attempt01.json")
    cap_replay = record("repro/results/research-mixed-first-cap-coupled-plateau-replay.json")
    assert cap["status"] == cap_replay["status"] == "passed"
    assert cap_replay["input_sha256"] == dependencies[
        "repro/results/research-mixed-first-cap-coupled-plateau-attempt01.json"]
    for rec in (cap, cap_replay):
        bind("notes/research_mixed_first_cap_coupled_plateau_certificate.md", rec["proof_sha256"])
        bind("experiments/continue_mixed_first_cap_coupled_plateau.py", rec["script_sha256"])
    assert cap["oriented_input_extraction"] == cap_replay["oriented_input_extraction"]
    oriented = cap["oriented_input_extraction"]
    assert oriented["checked_outputs"] == 16421
    assert set(oriented["cases"]) == {"(1, 0, 1)", "(1, 1, 1)"}
    for value in oriented["cases"].values():
        assert F(value["exact_lower"]) > F(value["floor"]) >= F(259, 1000)
    assert dependencies[IMAGE] == raw["inputs"][IMAGE]

    assert len(raw["cases"]) == 4
    for got, expected in zip(raw["cases"], EXPECTED):
        types, candidates, tested, pairs, nodes, lower = expected
        assert (got["types"], got["candidate_endpoint_leaves"], got["tested_pairs"],
                got["compatible_pairs"], got["compatible_endpoint_nodes"], got["exact_lower"]
                ) == (types, candidates, tested, pairs, nodes, lower)
        assert F(got["exact_lower"]) > F(-39, 500)
        assert (got["worst"] is None) == (pairs == 0)
    assert sum(c["tested_pairs"] for c in raw["cases"]) == 481003
    assert sha(ROOT/PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
    result = dict(
        status="passed", arithmetic="bindings, full-tree structure, exact rational comparisons",
        theorem_scope="Actual attached type-four endpoints of all mixed words m>=3; no m2 claim.",
        uniform_height_lower="-39/500", next_three_height_lower="-7/100",
        raw_compatibility_sha256=RAW_RECORD_SHA, raw_program_sha256=RAW_SCRIPT_SHA,
        ordinary_full_cover_leaves=ordinary_leaves, endpoint_full_cover_leaves=totals[0],
        raw_cases=raw["cases"], raw_pair_tests=481003,
        compatibility_arithmetic_repeated=False, new_roots=0, new_cover_cells=0,
        proof_sha256=proof_hash, script_sha256=script_hash,
        dependencies_sha256=dependencies)
    assert args.output.resolve() not in {
        (ROOT/name).resolve() for name in dependencies
    } | {(ROOT/PROOF).resolve(), Path(__file__).resolve()}
    assert not args.output.exists(), "write only a fresh provenance record"
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS provenance/structure:", ordinary_leaves, "ordinary leaves;",
          totals[0], "endpoint leaves;", len(dependencies),
          "bindings; no compatibility arithmetic repeated")


if __name__ == "__main__":
    main()
