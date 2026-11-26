#!/usr/bin/env python3
"""Fixed saved-only margin extraction. No original evaluator is imported."""
import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "repro/results/research-mixed-typed-last-row-support-attempt04.json"
REPLAY = "repro/results/research-mixed-typed-last-row-support-replay.json"
WRITER = "experiments/certify_mixed_typed_last_row_support.py"
OLD_PROOF = "notes/research_mixed_typed_last_row_support_certificate.md"
PROTOCOL = "notes/research_mixed_fourier_right_cap_last_row_saved_margin.md"
OUTPUT = ROOT / "repro/results/research-mixed-fourier-right-cap-last-row-saved-margin.json"
PINS = {
    AUTHOR: "be75ec2a2628d4ae6e594a31ee62ca254788528024d1c27680d63ad86b9f0e46",
    REPLAY: "99d0d67616cfd0272d5ff9139c5e6a70a16fe6da7ef8421e9cd580baa3f0c06e",
    WRITER: "fa35e484760e8de06ef310b99c99946400559bbfcb7cc566d6aacea03c1ac715",
    OLD_PROOF: "0387a95df2b25fe4d1a32281dad5ab4503b8ada4ad0289eafce125954ed69c1f",
    PROTOCOL: "e6d69c7afa5dc7fadd9425dbe5ce85983dcc0c7ba8ffb76d7b93c9d7af300679",
    "notes/research_mixed_fourier_allocation_curvature.md":
        "62391135303edcc915779027bd98e1729a459e83ff9a1af04d02518656be9b87",
    "notes/research_mixed_fourier_right_cap_annulus_completion.md":
        "e4f7442dd117adf58988902544fbcbf91aad19df8eff858ee1161bc49669b0d0",
    "notes/research_mixed_fourier_right_cap_bare_inner_contour.md":
        "7f68cb80c9eb25159cb6fabe9bbad1bd4b678af439bdeba39cb527b2d9ecc603",
    "notes/research_mixed_typed_last_row_envelopes.md":
        "5732f40ffc086acddb21632a5d6af3e4905ebad38f97e62e89953802b1bdd10d",
    "notes/research_mixed_horizontal_tail_reference_boundary.md":
        "edc890ddd4fd230dc9e2f3ece7a6e2ba7ee45df5e5fadae7f1945d34e22d7a45",
    "notes/research_mixed_reduced_disk_conditional_packets.md":
        "e7dc611d81d66765083a155b7f8a6190a6dc7dee6ce40b6ed89cc46711980723",
    "notes/research_mixed_typed_last_row_support_completion.md":
        "70e842fee569d7429cec8fe38441012dd5775c5fb248bba6656a2ea7cc1b24aa",
    "notes/research_mixed_four_left_cut_support.md":
        "5d7dc67647399fd1b3a35a5b3cf26cfd4fe654dd0fed09a4e2d85195c5efae12",
    "notes/research_mixed_half_row_support_completion.md":
        "65186e9d2bd3b3275bbcd316f3bf46a28ff8204e3bfcc1cea1939d7ad280e20b",
}
IMPORT_AUTHOR = "repro/diagnostics/2026-11-05-typed-last-row-low-cap/continuation.json"
IMPORT_REPLAY = "repro/diagnostics/2026-11-05-typed-last-row-low-cap/continuation-replay.json"
LO, HI = F(11, 50), F(9, 20)
DECIMAL = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
BALL = re.compile(r"\[\s*(" + DECIMAL + r")\s+\+/-\s+(" + DECIMAL + r")\s*\]")
POINT = re.compile(DECIMAL)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def path_for(name):
    require(isinstance(name, str), "non-string input path")
    path = (ROOT / name).resolve()
    require(path.is_relative_to(ROOT) and path != OUTPUT.resolve(), "unsafe input path")
    return path


def load(name):
    with path_for(name).open() as handle:
        return json.load(handle)


def bind(name, expected, result):
    require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
            "invalid digest for " + name)
    actual = digest(path_for(name))
    result["input_hashes_before"][name] = actual
    require(actual == expected, "input digest mismatch: " + name)


def specifications():
    boundaries = {3: ("L3", "R3", "H3-", "H3+", "S3"),
                  4: ("L4", "R4", "H4-", "H4+")}
    out = []
    for own in (0, 1):
        for types in ((3, 3), (3, 4), (4, 4)):
            for slot in ((0,) if types[0] == types[1] else (0, 1)):
                for curve in boundaries[types[slot]]:
                    for piece in ("lower", "upper"):
                        out.append(dict(own=own, types=list(types), slot=slot,
                                        curve=curve, piece=piece))
    require(len(out) == 72 and all(x["own"] == 1 for x in out[36:]), "chart inventory")
    return out


def envelopes(spec):
    return sum(4 * 2**((spec["types"][side] == 3) + (spec["own"] == 0))
               for side in (0, 1))


def tree_check(domain, spec):
    """Reconstruct saved closed dyadic boxes; evaluate no saved bound."""
    require(domain["kind"] == "computed" and domain["status"] == "complete", "tree status")
    require(domain["frontier"] == [], "nonempty saved frontier")
    stack = [("", [(F(0), F(1))] * 3, 0)]
    leaves, volume, maximum_depth = 0, F(0), 0
    cover_hash = hashlib.sha256()
    for node in domain["tree"]:
        require(stack and isinstance(node, list) and len(node) == 2, "malformed tree")
        address, box, depth = stack.pop()
        maximum_depth = max(maximum_depth, depth)
        require(depth <= 60, "depth guard")
        if node[0] == "S":
            axis = node[1]
            require(type(axis) is int and axis == depth % 3 and depth < 60, "split rule")
            low, high = box[axis]
            midpoint = (low + high) / 2
            left, right = list(box), list(box)
            left[axis], right[axis] = (low, midpoint), (midpoint, high)
            children = [(address + "0", left, depth + 1), (address + "1", right, depth + 1)]
            if axis in (0, 1):
                children.reverse()
            stack.extend(children)
        else:
            require(node[0] == "L" and isinstance(node[1], dict), "leaf format")
            leaf = node[1]
            require(isinstance(leaf["witness"], dict), "missing inherited witness")
            require(isinstance(leaf["max_upper"], str), "missing inherited bound")
            require(leaf["envelope_count"] == envelopes(spec), "leaf envelope inventory")
            trials = leaf["targets"]
            require(isinstance(trials, list) and len(trials) == 2, "target sides")
            for side in (0, 1):
                require(len(trials[side]) == 2, "target coordinates")
                for i, flag in enumerate((spec["types"][side] - 3, spec["own"])):
                    trial = trials[side][i]
                    if flag:
                        require(isinstance(trial, str) and LO <= F(trial) <= HI, "saved target")
                    else:
                        require(trial is None, "unexpected target")
            leaves += 1
            volume += F(1, 2**depth)
            encoded = [address, [[str(x) for x in pair] for pair in box], canonical(leaf)]
            cover_hash.update(json.dumps(encoded, separators=(",", ":")).encode() + b"\n")
    require(not stack and volume == 1, "incomplete dyadic cube")
    require(leaves == domain["leaves"] and len(domain["tree"]) == domain["tree_nodes"],
            "tree counts")
    require(str(volume) == domain["resolved_volume"] and
            maximum_depth == domain["maximum_depth"], "tree metadata")
    return dict(leaves=leaves, tree_nodes=len(domain["tree"]), maximum_depth=maximum_depth,
                resolved_volume_rational=str(volume), ordered_cover_sha256=cover_hash.hexdigest())


def upper_endpoint(display):
    require(isinstance(display, str), "non-string upper enclosure")
    match = BALL.fullmatch(display.strip())
    if match:
        midpoint, radius = map(F, match.groups())
        require(radius >= 0, "negative printed radius")
    else:
        require(POINT.fullmatch(display.strip()), "unsupported finite decimal enclosure")
        midpoint, radius = F(display), F(0)
    return midpoint, radius, midpoint + radius


def common(record, precision):
    wanted = dict(schema="typed-last-row-height-charts-v1", chart_count=72,
                  imported_chart_index=18, proof_sha256=PINS[OLD_PROOF],
                  script_sha256=PINS[WRITER], precision_bits=precision,
                  max_nodes_per_attempt=200000, max_seconds_per_attempt=300,
                  maximum_depth_guard=60, target_interval=["11/50", "9/20"],
                  target_curvature="1/5", kappa="1/2500000", requested_deficit_upper="0",
                  status="passed", positive_point=None)
    for key, value in wanted.items():
        require(record[key] == value, "original metadata: " + key)
    require(len(record["domains"]) == 72, "original domain count")


def invalidate(result):
    result["own_four_boundary_certified"] = False
    result["whole_own_four_margin_certified"] = False
    result["bare_last_row_certified"] = False
    result["three_inner_rows_certified"] = False
    result["certified_gaps_rational"] = None


def check(result):
    for name, expected in PINS.items():
        bind(name, expected, result)
    author = load(AUTHOR)
    common(author, 256)
    require(author["mode"] == "author" and author["complete_charts"] == 72 and
            author["pending_boxes_total"] == 0, "incomplete author")
    dependencies = author["dependencies_sha256"]
    require(isinstance(dependencies, dict) and len(dependencies) == 37, "old dependency inventory")
    for name, expected in dependencies.items():
        if name in PINS:
            require(PINS[name] == expected, "conflicting direct/inherited pin")
        bind(name, expected, result)
    specs = specifications()
    author_hashes = []
    for domain, spec in zip(author["domains"], specs):
        require(domain["spec"] == spec and domain["status"] == "complete", "author chart")
        author_hashes.append(canonical(domain))
    require(sum(d["leaves"] for d in author["domains"]) == author["accepted_cells_total"],
            "author leaf total")
    require(sum(d["tree_nodes"] for d in author["domains"]) == author["tree_nodes_total"],
            "author tree total")
    del author
    replay = load(REPLAY)
    common(replay, 320)
    require(replay["mode"] == "saved_replay" and replay["stop_reason"] == "all72 saved charts replayed",
            "incomplete old replay")
    require(replay["input_sha256"] == PINS[AUTHOR] and
            replay["dependencies_sha256"] == dependencies, "replay source association")
    require(replay["proposals"] == replay["refinements"] == 0, "old replay changed trials")
    summaries = replay["replay_summaries"]
    require(len(summaries) == 72, "summary inventory")
    require(replay["replayed_cells"] == 121696 and replay["replayed_envelope_bounds"] == 2844564,
            "original fixed totals")
    result["inherited_replay"] = dict(cells=replay["replayed_cells"],
                                      envelope_bounds=replay["replayed_envelope_bounds"],
                                      proposals=0, refinements=0)
    leaf_total = envelope_total = tree_total = 0
    for index, (domain, spec, summary) in enumerate(zip(replay["domains"], specs, summaries)):
        require(domain["spec"] == spec and canonical(domain) == author_hashes[index],
                "author/replay domain identity: " + str(index))
        require(summary["index"] == index and summary["spec"] == spec, "summary association")
        if index == 18:
            wanted = dict(spec=spec, kind="imported", status="complete", leaves=402,
                          tree_nodes=803, resolved_volume="1",
                          record=IMPORT_AUTHOR, record_sha256=dependencies[IMPORT_AUTHOR],
                          replay=IMPORT_REPLAY, replay_sha256=dependencies[IMPORT_REPLAY])
            require(domain == wanted, "imported domain identity")
            coverage = dict(leaves=402, tree_nodes=803, resolved_volume_rational="1",
                            inherited_import_only=True)
        else:
            coverage = tree_check(domain, spec)
            tree_total += 1
        require(summary["leaves"] == domain["leaves"] and
                summary["envelope_bounds"] == domain["leaves"] * envelopes(spec),
                "summary leaf/envelope counts")
        leaf_total += summary["leaves"]
        envelope_total += summary["envelope_bounds"]
        result["chart_associations"].append(dict(
            index=index, spec=spec, domain_canonical_sha256=author_hashes[index],
            summary_canonical_sha256=canonical(summary), coverage=coverage))
        if index >= 36:
            comparison = dict(index=index, spec=spec,
                              maximum_upper_display=summary["maximum_upper"],
                              threshold_rational="-1/50", strictly_below_threshold=False)
            result["own_four_comparisons"].append(comparison)
            midpoint, radius, upper = upper_endpoint(summary["maximum_upper"])
            comparison.update(
                midpoint_rational=str(midpoint), radius_rational=str(radius),
                upper_rational=str(upper), strictly_below_threshold=upper < -F(1, 50))
    require(leaf_total == 121696 and envelope_total == 2844564 and tree_total == 71,
            "new association inventory")
    require(len(result["own_four_comparisons"]) == 36 and
            [row["index"] for row in result["own_four_comparisons"]] == list(range(36, 72)),
            "fixed own-four comparison inventory")
    result["inventory"] = dict(chart_associations=72, reconstructed_trees=71,
                               inherited_imported_trees=1, own_four_comparisons=36,
                               analytic_calls=0, source_replays=0, gain_calls=0,
                               root_calls=0, proposals=0, refinements=0)
    result["all_comparisons_passed"] = all(
        row["strictly_below_threshold"] for row in result["own_four_comparisons"])
    boundary_gap, matched_gap, correction = F(1, 50), F(1, 1000), F(33, 70000)
    whole_gap = min(boundary_gap, matched_gap)
    last_gap, cut_gap = whole_gap - correction, F(1, 2000) - correction
    require(whole_gap == F(1, 1000) and last_gap == F(37, 70000) and
            last_gap > F(1, 2000) and cut_gap == F(1, 35000), "deduction arithmetic")
    result["conditional_gap_arithmetic"] = dict(
        boundary_gap=str(boundary_gap), matched_gap=str(matched_gap), whole_gap=str(whole_gap),
        allocation_correction=str(correction), bare_last_row_gap=str(last_gap),
        inherited_cut_gap=str(cut_gap), common_inner_row_gap=str(min(last_gap, cut_gap)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--script-sha", required=True)
    args = parser.parse_args()
    own_name = Path(__file__).resolve().relative_to(ROOT).as_posix()
    require(re.fullmatch(r"[0-9a-f]{64}", args.script_sha), "malformed frozen script digest")
    require(digest(__file__) == args.script_sha, "frozen script digest mismatch")
    result = dict(schema="fourier-right-cap-last-row-saved-margin-v1", status="initializing",
                  script_sha256=args.script_sha, input_hashes_before={}, input_hashes_after={},
                  chart_associations=[], own_four_comparisons=[], errors=[],
                  all_comparisons_passed=False,
                  scope="Own-four last-row and three inner-row rate margins only; "
                        "outgoing q-source, whole cap and noncancellation are not certified.",
                  arithmetic_scope="Saved decimal upper parsing and provenance/tree association; "
                                   "analytic replay maxima are inherited without reevaluation.")
    invalidate(result)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("x", encoding="utf-8") as handle:
        try:
            bind(own_name, args.script_sha, result)
            check(result)
            result["status"] = "pending_final_bindings"
        except BaseException as error:
            result["errors"].append(type(error).__name__ + ": " + str(error))
            result["status"] = "calculation_failure"
        finally:
            for name, before in result["input_hashes_before"].items():
                try:
                    after = digest(path_for(name))
                    result["input_hashes_after"][name] = after
                    require(after == before, "changed input: " + name)
                except BaseException as error:
                    result["errors"].append(type(error).__name__ + ": " + str(error))
                    result["status"] = "calculation_failure"
            result["all_inputs_unchanged"] = (
                result["input_hashes_before"] == result["input_hashes_after"])
            if not result["errors"] and result["status"] == "pending_final_bindings":
                result["status"] = "passed" if result["all_comparisons_passed"] else "inconclusive"
                if result["status"] == "passed":
                    result["own_four_boundary_certified"] = True
                    result["whole_own_four_margin_certified"] = True
                    result["bare_last_row_certified"] = True
                    result["three_inner_rows_certified"] = True
                    result["certified_gaps_rational"] = result["conditional_gap_arithmetic"]
            if result["status"] != "passed":
                invalidate(result)
            json.dump(result, handle, sort_keys=True, indent=2, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    print(json.dumps(dict(status=result["status"], comparisons=len(result["own_four_comparisons"]),
                          bindings=len(result["input_hashes_before"]), output=str(OUTPUT),
                          errors=result["errors"]), sort_keys=True))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
