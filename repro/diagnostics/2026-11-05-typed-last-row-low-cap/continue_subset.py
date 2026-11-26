#!/usr/bin/env python3
"""Continue only the six saved low-cap boxes, or replay a completed subset.

Author mode imports all 253 accepted cells without proposals or numerical
reevaluation there. Only the exact saved frontier may be subdivided, with
at most 4095 additional visits and 30 seconds including setup. Replay uses
saved witnesses and rational target trials only: no proposal or subdivision.
Neither mode concerns the other 27 boundary cases or actual-word realization.
"""
import argparse
from contextlib import contextmanager
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import signal
import sys
import time

import numpy as np
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "experiments"))
import pilot_mixed_typed_last_row_low_cap as pilot

old = pilot.old
prior = pilot.prior
ORIGINAL = HERE / "result.json"
DESIGN = ROOT / "notes/research_mixed_typed_last_row_support_design.md"
PILOT_SCRIPT = ROOT / "experiments/pilot_mixed_typed_last_row_low_cap.py"
PINNED = {
    "notes/research_mixed_typed_last_row_support_design.md":
        "1fe596a46cc050a871f2b8f70427e42e47672de6ede78c79b714056248a3b840",
    "experiments/pilot_mixed_typed_last_row_low_cap.py":
        "7a4bf27dca2f87cf600573ea697f2e55924b8eb2b811664cdff4d81881c29b48",
    "repro/diagnostics/2026-11-05-typed-last-row-low-cap/result.json":
        "3032ec6861743b8bd2e73e9d477e90173db847365442640b25c2be8225ce26e4",
    "repro/diagnostics/2026-11-05-typed-last-row-low-cap/README.md":
        "1982c691595d6a9be9ab2abf3f20fa838c849b3c3c17460a934d413d5be1aa4f",
}
MAX_ADDITIONAL = 4095
MAX_SECONDS = 30
ORIGINAL_VISITS = 511
ORIGINAL_ACCEPTED = 253
EXPECTED_ENVELOPES = 24


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decode_pending(rows):
    return [(r["address"], [tuple(map(F, pair)) for pair in r["box"]], r["depth"])
            for r in rows]


def encode_pending(rows):
    return [dict(address=a, depth=d, box=[[str(v) for v in pair] for pair in b])
            for a, b, d in rows]


def audit_tree(nodes, pending, visits):
    """Exact prefix partition; no numerical enclosure/proposal occurs here."""
    kinds = {}
    for node in nodes:
        address = node["address"]
        assert address not in kinds
        assert node["depth"] == len(address)
        assert node["box"] == [[str(v) for v in pair]
                               for pair in pilot.box_from_address(address)]
        if node["kind"] == "split":
            assert node["axis"] == len(address) % 3
        else:
            assert node["kind"] == "accepted"
        kinds[address] = node["kind"]
    frontier = {}
    for address, box, depth in pending:
        assert address not in kinds and address not in frontier
        assert depth == len(address)
        assert box == pilot.box_from_address(address)
        frontier[address] = depth
    addresses = set(kinds) | set(frontier)
    assert "" in addresses
    for address in addresses:
        if address:
            assert kinds.get(address[:-1]) == "split"
        if kinds.get(address) == "split":
            assert address+"0" in addresses and address+"1" in addresses
        else:
            assert address+"0" not in addresses and address+"1" not in addresses
    accepted_volume = sum((F(1, 2**len(a)) for a, k in kinds.items()
                           if k == "accepted"), F(0))
    pending_volume = sum((F(1, 2**d) for d in frontier.values()), F(0))
    assert accepted_volume+pending_volume == 1
    assert len(nodes) <= visits <= len(nodes)+1
    assert ORIGINAL_VISITS <= visits <= ORIGINAL_VISITS+MAX_ADDITIONAL
    return accepted_volume, pending_volume


def saved_trial(node):
    """Verify all exact branches, then extract the unique weighted trial."""
    rows = node["rows"]
    assert len(rows) == EXPECTED_ENVELOPES
    weighted = {F(r["trial_target"][0]) for r in rows if r["side"] == 1}
    assert len(weighted) == 1
    trial = weighted.pop()
    assert pilot.LO <= trial <= pilot.HI
    found = set()
    for row in rows:
        side = row["side"]
        assert side in (0, 1) and row["eta"] == side and row["own_epsilon"] == 0
        x, z = map(F, row["trial_target"])
        assert z in (pilot.LO, pilot.HI)
        assert x in ((pilot.LO, pilot.HI) if side == 0 else (trial,))
        v, w = row["carrier"]
        assert v in (0, 1) and w in (0, 1)
        key = (side, x, z, v, w)
        assert key not in found
        found.add(key)
    expected = {
        (side, x, z, v, w)
        for side in (0, 1)
        for x in ((pilot.LO, pilot.HI) if side == 0 else (trial,))
        for z in (pilot.LO, pilot.HI)
        for v in (0, 1) for w in (0, 1)
    }
    assert found == expected
    return trial


@contextmanager
def fixed_target(trial):
    """In-memory override only; the frozen helper files are never edited.

    The frozen acceptance code calls trial_x exactly once for the weighted
    first target of side 1. All other targets are the two exact endpoints.
    """
    assert isinstance(trial, F) and pilot.LO <= trial <= pilot.HI
    previous = prior.trial_x
    calls = [0]

    def use_saved(*_):
        calls[0] += 1
        assert calls[0] == 1
        return trial

    prior.trial_x = use_saved
    try:
        yield calls
    finally:
        prior.trial_x = previous


def check_with_trial(box, pp, p0, dp, certificate, trial):
    with fixed_target(trial) as calls:
        result = pilot.check_deficits(box, pp, p0, dp, certificate)
    assert calls == [1]
    assert saved_trial(dict(rows=result[1])) == trial
    return result


def containing_frontier(address, original_pending):
    matches = [a for a, _, _ in original_pending if address.startswith(a)]
    assert len(matches) == 1
    return matches[0]


def continue_frontier(base):
    """Accepted original nodes are copied exactly; only pending nodes run."""
    nodes = list(base["nodes"])
    original_pending = decode_pending(base["pending"])
    todo = list(original_pending)
    active = None
    added_visits = added_accepted = 0
    failures = dict(root=0, deficit=0)
    status, reason = "continuation_incomplete", "not started"
    positive = None

    def expired(*_):
        raise prior.PilotDeadline()

    handler = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, max(.000001, MAX_SECONDS-(time.monotonic()-START)))
    try:
        while todo:
            if added_visits >= MAX_ADDITIONAL:
                reason = "4095-additional-node budget"
                break
            if time.monotonic()-START >= MAX_SECONDS:
                raise prior.PilotDeadline()
            with prior.atomic_bookkeeping():
                address, box, depth = todo.pop()
                active = dict(address=address, box=box, depth=depth)
                added_visits += 1
            source_address = containing_frontier(address, original_pending)
            pp, dp = pilot.parameters(box)
            p0, _ = pilot.parameters([((lo+hi)/2,)*2 for lo, hi in box])
            proposed = None
            detail = dict(reason="root enclosure")
            try:
                proposed = prior.propose(pp, p0)
                if proposed is not None:
                    witness, certificate = proposed
                    # Author-only floating proposal of one rational target.
                    # The outward acceptance uses that exact rational number.
                    trial = prior.trial_x(certificate["point"][1],
                                          p0[1], certificate["point"][0])
                    ok, rows, point = check_with_trial(
                        box, pp, p0, dp, certificate, trial)
                    detail = dict(reason="deficit enclosure", rows=rows,
                                  weighted_target_trial=str(trial))
                    if point is not None:
                        positive = dict(
                            parameters=[str(z) for z in p0],
                            roots=[str(z) for z in certificate["point"]],
                            trial=point, witness=witness,
                            weighted_target_trial=str(trial),
                            containing_address=address, original_frontier=source_address,
                            containing_box=[[str(v) for v in pair] for pair in box],
                            membership="Exact K3 slanted-chord times K4 bottom-cap chart.",
                            actual_geometry="Entire first chord is outside O3 union A3.")
                        status = "positive_auxiliary_point"
                        reason = "outward positive fixed trial on the auxiliary envelope"
                        break
                    if ok:
                        with prior.atomic_bookkeeping():
                            nodes.append(dict(
                                address=address, depth=depth,
                                box=[[str(v) for v in pair] for pair in box],
                                kind="accepted", original_frontier=source_address,
                                witness=witness, weighted_target_trial=str(trial), rows=rows))
                            added_accepted += 1
                            active = None
                        continue
            except (AssertionError, ValueError, ZeroDivisionError, OverflowError,
                    np.linalg.LinAlgError) as exc:
                detail = dict(reason="uncertain interval or proposal", exception=type(exc).__name__)
            failures["root" if proposed is None else "deficit"] += 1
            axis = depth % 3
            left, right = old.split(box, axis)
            children = [(address+"0", left, depth+1), (address+"1", right, depth+1)]
            if axis in (0, 1):
                children.reverse()
            with prior.atomic_bookkeeping():
                nodes.append(dict(
                    address=address, depth=depth,
                    box=[[str(v) for v in pair] for pair in box],
                    kind="split", axis=axis, original_frontier=source_address, detail=detail))
                todo.extend(children)
                active = None
        else:
            status, reason = "subset_complete", "all six imported frontier boxes resolved"
    except prior.PilotDeadline:
        reason = "30-second budget including setup"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, handler)
    pending = list(todo)
    if active is not None:
        pending.append((active["address"], active["box"], active["depth"]))
    assert nodes[:len(base["nodes"])] == base["nodes"]
    for node in nodes[len(base["nodes"]):]:
        assert node["original_frontier"] == containing_frontier(node["address"], original_pending)
    for address, _, _ in pending:
        containing_frontier(address, original_pending)
    visits = ORIGINAL_VISITS+added_visits
    accepted_volume, pending_volume = audit_tree(nodes, pending, visits)
    assert sum(n["kind"] == "accepted" for n in nodes) == ORIGINAL_ACCEPTED+added_accepted
    if status == "subset_complete":
        assert not pending and positive is None and accepted_volume == 1
    return dict(
        status=status, mode="bounded_continuation", stop_reason=reason,
        original_accepted_cells_imported=ORIGINAL_ACCEPTED,
        original_accepted_cells_numerically_rechecked=0,
        original_frontier=base["pending"],
        additional_visited_nodes=added_visits, additional_accepted_cells=added_accepted,
        additional_failure_counts=failures, visited_nodes_total=visits,
        accepted_cells_total=ORIGINAL_ACCEPTED+added_accepted,
        nodes=nodes, pending=encode_pending(pending), positive_point=positive,
        exact_accepted_parameter_volume=str(accepted_volume),
        exact_pending_parameter_volume=str(pending_volume),
        exact_terminal_and_pending_volume=str(accepted_volume+pending_volume))


def replay_complete(source, base):
    """No root/target proposal or adaptive subdivision occurs in this path.

    Exact reconstruction of already saved address boxes is only bookkeeping.
    """
    assert source["status"] == "subset_complete" and source["mode"] == "bounded_continuation"
    assert source["original_frontier"] == base["pending"]
    assert source["nodes"][:len(base["nodes"])] == base["nodes"]
    assert source["original_accepted_cells_imported"] == ORIGINAL_ACCEPTED
    assert source["original_accepted_cells_numerically_rechecked"] == 0
    assert 0 <= source["additional_visited_nodes"] <= MAX_ADDITIONAL
    assert source["visited_nodes_total"] == ORIGINAL_VISITS+source["additional_visited_nodes"]
    assert not source["pending"] and source["positive_point"] is None
    volume, pending_volume = audit_tree(source["nodes"], [], source["visited_nodes_total"])
    assert volume == 1 and pending_volume == 0
    assert source["exact_accepted_parameter_volume"] == "1"
    assert source["exact_pending_parameter_volume"] == "0"
    assert source["exact_terminal_and_pending_volume"] == "1"
    original_pending = decode_pending(base["pending"])
    checked = []
    accepted = 0
    # Guard against accidental future proposal additions to the replay path.
    proposal = prior.propose
    floating_trial = prior.trial_x
    floating_block = old.base.block

    def forbidden(*_, **__):
        raise RuntimeError("saved replay cannot propose roots or target trials")

    prior.propose = prior.trial_x = old.base.block = forbidden
    try:
        for index, node in enumerate(source["nodes"]):
            if index >= len(base["nodes"]):
                assert node["original_frontier"] == containing_frontier(
                    node["address"], original_pending)
            if node["kind"] == "split":
                checked.append(node)
                continue
            assert node["kind"] == "accepted"
            box = [tuple(map(F, pair)) for pair in node["box"]]
            pp, dp = pilot.parameters(box)
            p0, _ = pilot.parameters([((lo+hi)/2,)*2 for lo, hi in box])
            certificate = old.root_box(node["witness"], pp, p0, 0)
            assert certificate is not None, node["address"]
            trial = saved_trial(node)
            if "weighted_target_trial" in node:
                assert F(node["weighted_target_trial"]) == trial
            ok, rows, positive = check_with_trial(box, pp, p0, dp, certificate, trial)
            assert ok and positive is None, node["address"]
            refreshed = dict(node)
            refreshed["rows"] = rows
            refreshed["weighted_target_trial"] = str(trial)
            checked.append(refreshed)
            accepted += 1
    finally:
        prior.propose = proposal
        prior.trial_x = floating_trial
        old.base.block = floating_block
    assert accepted == source["accepted_cells_total"]
    assert accepted == ORIGINAL_ACCEPTED+source["additional_accepted_cells"]
    # Witnesses, target trials, and exact tree are unchanged; only outward
    # numerical enclosures in accepted-cell rows have been refreshed.
    for original, refreshed in zip(source["nodes"], checked):
        assert original["address"] == refreshed["address"]
        assert original["box"] == refreshed["box"] and original["kind"] == refreshed["kind"]
        if original["kind"] == "accepted":
            assert original["witness"] == refreshed["witness"]
            assert saved_trial(original) == saved_trial(refreshed)
    audit_tree(checked, [], source["visited_nodes_total"])
    return dict(
        status="passed", mode="saved_replay", stop_reason="complete subset independently replayed",
        original_frontier=base["pending"],
        original_accepted_cells_imported=ORIGINAL_ACCEPTED,
        original_accepted_cells_numerically_rechecked=ORIGINAL_ACCEPTED,
        additional_visited_nodes=source["additional_visited_nodes"],
        additional_accepted_cells=source["additional_accepted_cells"],
        visited_nodes_total=source["visited_nodes_total"], accepted_cells_total=accepted,
        replayed_accepted_cells=accepted, proposals=0, refinements=0,
        nodes=checked, pending=[], positive_point=None,
        exact_accepted_parameter_volume="1", exact_pending_parameter_volume="0",
        exact_terminal_and_pending_volume="1")


def main():
    global START
    START = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.input:
        assert args.precision >= 320
    else:
        assert args.precision == 256
    output = args.output or HERE / ("continuation-replay.json" if args.input else "continuation.json")
    assert not output.exists(), "use a new output; frozen records are never overwritten"
    if args.input:
        assert output.resolve() != args.input.resolve()
    assert output.resolve() not in {(ROOT/p).resolve() for p in PINNED}
    ctx.prec = args.precision
    PI, II = arb.pi(), acb(0, 1)
    pilot.PI = prior.PI = old.PI = old.base.PI = PI
    pilot.II = prior.II = old.II = old.base.I = II
    assert (pilot.MAX_NODES, pilot.MAX_SECONDS) == (511, 30)
    assert pilot.EXPECTED_ENVELOPES == EXPECTED_ENVELOPES
    assert prior.KAPPA == pilot.KAPPA == F(1, 2500000)
    assert prior.CURVATURE == pilot.CURVATURE == F(1, 5)
    deps = {}

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in deps or deps[name] == digest, name
        deps[name] = digest
        return digest

    for name, digest in PINNED.items():
        bind(name, digest)
    base = json.loads(ORIGINAL.read_text())
    for name, digest in base["dependencies_sha256"].items():
        bind(name, digest)
    assert base["proof_sha256"] == sha(DESIGN)
    assert base["script_sha256"] == sha(PILOT_SCRIPT)
    assert base["status"] == "pilot_incomplete" and base["precision_bits"] == 256
    assert base["visited_nodes"] == ORIGINAL_VISITS and len(base["nodes"]) == ORIGINAL_VISITS
    assert base["accepted_cells"] == ORIGINAL_ACCEPTED and base["excluded_cells"] == 0
    assert len(base["pending"]) == 6 and base["positive_point"] is None
    accepted_volume, pending_volume = audit_tree(
        base["nodes"], decode_pending(base["pending"]), ORIGINAL_VISITS)
    assert accepted_volume == F(5, 8) and pending_volume == F(3, 8)
    assert sum(n["kind"] == "accepted" for n in base["nodes"]) == ORIGINAL_ACCEPTED
    for node in base["nodes"]:
        if node["kind"] == "accepted":
            saved_trial(node)  # Exact branch/target inventory, no numerical replay.
    script_hash = sha(__file__)
    if args.input:
        input_hash = sha(args.input)
        source = json.loads(args.input.read_text())
        assert source["script_sha256"] == script_hash
        assert source["proof_sha256"] == sha(DESIGN)
        assert source["dependencies_sha256"] == deps
        assert source["original_result_sha256"] == sha(ORIGINAL)
        assert source["max_additional_nodes"] == MAX_ADDITIONAL
        assert source["max_seconds"] == MAX_SECONDS
        result = replay_complete(source, base)
        assert sha(args.input) == input_hash
        result["input_sha256"] = input_hash
    else:
        result = continue_frontier(base)
    assert sha(__file__) == script_hash
    assert all(sha(ROOT/name) == digest for name, digest in deps.items())
    result.update(
        precision_bits=args.precision, original_result_sha256=sha(ORIGINAL),
        original_driver_sha256=sha(PILOT_SCRIPT), proof_sha256=sha(DESIGN),
        script_sha256=script_hash, dependencies_sha256=deps,
        own_epsilon=0, external_types=[3, 4], boundary_slot=0, chart=base["chart"],
        conditional_orientations=2, carrier_branches_per_orientation=4,
        target_interval=base["target_interval"], kappa=base["kappa"],
        target_curvature=base["target_curvature"],
        target_envelopes_per_accepted_cell=EXPECTED_ENVELOPES,
        requested_deficit_upper="0", max_additional_nodes=MAX_ADDITIONAL,
        max_seconds=MAX_SECONDS, elapsed_seconds=time.monotonic()-START,
        scope="Only the original slanted K3 chord times bottom K4 cap. The first "
              "chord lies outside actual O3 union A3. No other case, actual-word "
              "realization, or finite-kernel noncancellation is concluded.")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(result["status"], "additional nodes", result["additional_visited_nodes"],
          "total accepted", result["accepted_cells_total"], "pending", len(result["pending"]),
          "volume", result["exact_accepted_parameter_volume"], "bindings", len(deps),
          "seconds", round(result["elapsed_seconds"], 3), "output", output)
    return 0 if result["status"] in ("subset_complete", "passed") else 2


if __name__ == "__main__":
    raise SystemExit(main())
