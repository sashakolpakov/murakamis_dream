#!/usr/bin/env python3
"""Four next-four left-cut corner lower bounds on one prescribed box.

Reuses the frozen own-four reference and centered primitive only. No central
or half-row inspect, parameter cover, root solve or finite quantum sum.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, ctx

import diagnose_mixed_four_four_half_row_budget as four


REPO = Path(__file__).resolve().parents[1]
HELPER = REPO/"experiments/diagnose_mixed_four_four_half_row_budget.py"
HELPER_SHA = "cc1d86c233ef74f343796b6ad64967ca8a86c8dd315546b1de7c440cd9f9f82f"
PROOF = REPO/"notes/research_mixed_selected_four_left_row_corners.md"
PROOF_SHA = "c83695e631cdd77bc4852480fe9a9b9e37c77ecd138fc8e3a436b949b0ea6f59"
SPEC = REPO/"notes/research_mixed_selected_four_left_row_corner_evaluation.md"
SPEC_SHA = "e71174d48990278b3c3f55d5abd87a62d17d9d8d61ee3fd7bdb5387818ae8c1a"
TARGETS = (("22", F(11, 50)), ("45", F(9, 20)))
KEYS = tuple(left+"_"+right for left, _ in TARGETS for right, _ in TARGETS)
GAP = F(1, 2000)
CenteredPrimitives = four.CenteredPrimitives


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect(box, primitive):
    """Return four rigorous lower endpoints; acceptance requires all four>0."""
    details = {}
    frozen = four.frozen
    try:
        state, reason, ref = four.reference_four(box, primitive)
        if state != "retained":
            return state, reason, details
        auxiliary, shapes, coordinates = ref
        s, b = coordinates["s"], coordinates["b"]
        pi, ii = primitive.pi, primitive.ii
        cut = frozen.rat(F(1, 8))
        gs, gcut = primitive.g(s), primitive.g(acb(cut))
        height_chirp = -2*pi*primitive.height*(s.real-cut)
        common = -3*gs.real+3*gcut.real+height_chirp
        if not common.is_finite():
            raise frozen.Inconclusive("nonfinite common corner term")

        incoming, outgoing = {}, {}
        for name, target in TARGETS:
            value = frozen.rat(target)
            z = acb(value, primitive.height)
            bout = acb(value, b.imag)
            incoming[name] = ((primitive.g(s+z)-primitive.g(acb(cut)+z)).real
                              -2*pi*value*s.imag)
            outgoing[name] = (primitive.g(s+bout)-primitive.g(acb(cut)+bout)).real
            if not incoming[name].is_finite() or not outgoing[name].is_finite():
                raise frozen.Inconclusive("nonfinite corner term at"+name)

        details["auxiliary"] = frozen.complex_record(auxiliary)
        details["reference_shapes"] = {
            name: frozen.complex_record(value) for name, value in shapes.items()}
        details["reference_coordinates"] = {
            name: frozen.complex_record(value) for name, value in coordinates.items()}
        details["g_actual_index"] = frozen.complex_record(gs)
        details["g_real_cut"] = frozen.complex_record(gcut)
        details["common_height_chirp"] = frozen.real_record(height_chirp)
        details["K"] = frozen.real_record(common)
        details["I"] = {name: frozen.real_record(value) for name, value in incoming.items()}
        details["O"] = {name: frozen.real_record(value) for name, value in outgoing.items()}
        details["outgoing_halfweight_cancels_in_difference"] = True
        corners = {}
        for left, epsilon in TARGETS:
            for right, eta in TARGETS:
                value = common+incoming[left]+outgoing[right]
                if not value.is_finite():
                    raise frozen.Inconclusive("nonfinite corner "+left+"_"+right)
                lo = frozen.lower(value)
                corners[left+"_"+right] = {
                    "incoming_real": str(epsilon), "outgoing_real": str(eta),
                    "value": frozen.real_record(value),
                    "lower_nonnegative": lo >= 0,
                    "lower_strictly_positive": lo > 0,
                    "lower_at_least_candidate_gap": lo >= GAP,
                }
        details["corners"] = corners
        details["minimum_corner_lower_rational"] = str(min(
            F(corners[key]["value"]["lower_rational"]) for key in KEYS))
        if all(corners[key]["lower_strictly_positive"] for key in KEYS):
            return "accepted", "four strictly positive corner lower bounds", details
        return "inconclusive", "corner signs not certified on this box", details
    except frozen.Inconclusive as error:
        return "inconclusive", str(error), details


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    for path, expected in ((HELPER, HELPER_SHA), (PROOF, PROOF_SHA), (SPEC, SPEC_SHA)):
        if digest(path) != expected:
            raise ValueError("frozen helper/proof/spec mismatch: "+str(path))
    bindings = dict(four.PINNED)
    for path in (HELPER, PROOF, SPEC, Path(__file__).resolve()):
        bindings[str(path.relative_to(REPO))] = digest(path)
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("pinned input mismatch: "+name)
    previous = json.loads((REPO/four.PREVIOUS).read_text())
    if previous["status"] != "proved" or previous["unresolved"]:
        raise ValueError("inherited central record is not complete")
    for name, expected in previous["input_sha256"].items():
        path = Path(name)
        relative = str((path if path.is_absolute() else REPO/path).relative_to(REPO))
        if relative in bindings and bindings[relative] != expected:
            raise ValueError("conflicting inherited binding: "+relative)
        bindings[relative] = expected
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("frozen dependency mismatch: "+name)

    accepted = [leaf for leaf in previous["leaves"] if leaf["status"] == "accepted"]
    depth = max(len(leaf["address"]) for leaf in accepted)
    chosen = min((leaf for leaf in accepted if len(leaf["address"]) == depth),
                 key=lambda leaf: leaf["address"])
    if chosen["address"] != four.ADDRESS or depth != 18:
        raise ValueError("prescribed deterministic address mismatch")
    box = four.BASE.ROOT
    if list(map(str, box)) != previous["initial_auxiliary_rectangle"]:
        raise ValueError("original root rectangle mismatch")
    for split_depth, branch in enumerate(four.ADDRESS):
        box = four.BASE.split(box, split_depth)[int(branch)]
    if box != four.BOX:
        raise ValueError("exact inherited box reconstruction failed")

    def forbidden(*args, **kwargs):
        raise RuntimeError("old scalar inspect forbidden in the corner diagnostic")

    four.inspect = four.frozen.inspect = four.maps_four.inspect = four.BASE.inspect = forbidden
    ctx.prec = 160
    started = time.monotonic()
    result = inspect(box, CenteredPrimitives())
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during diagnostic: "+name)
    record = {
        "status": "diagnostic complete",
        "scope": "Four next-four ordinary-left-cut corner lower bounds on one inherited box",
        "actual_word_realization_claimed": False,
        "precision_bits": 160, "height": str(four.H),
        "acceptance_threshold": "strictly positive lower endpoints",
        "optional_candidate_gap": str(GAP),
        "tested_address": four.ADDRESS, "tested_box": list(map(str, box)),
        "inherited_leaf": chosen,
        "formula": "Four-corner theorem Eq(21)/(22), K+I_epsilon+O_eta",
        "result": {"status": result[0], "reason": result[1], "details": result[2]},
        "inspect_calls": 1, "old_scalar_inspect_calls": 0,
        "tested_boxes": 1, "subdivisions": 0, "automatic_retries": 0,
        "root_proposals": 0, "finite_source_evaluations": 0,
        "elapsed_seconds": time.monotonic()-started,
        "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as output:
        output.write(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": record["status"], "tested_address": four.ADDRESS,
        "result_status": result[0], "reason": result[1],
        "elapsed_seconds": record["elapsed_seconds"],
        "lower_bounds": {
            key: value["value"]["lower_rational"]
            for key, value in result[2].get("corners", {}).items()},
    }), flush=True)


if __name__ == "__main__":
    main()
