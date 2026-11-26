#!/usr/bin/env python3
"""One fixed-box centered-primitive diagnostic; no subdivision or source sum."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time


REPO = Path(__file__).resolve().parents[1]
PREVIOUS = REPO/"repro/results/research-mixed-selected-half-row-budget-attempt02.json"
PREVIOUS_SHA = "8728c18541d17fd0a6533deb60bacfe8bbb8c728c50b90123ee3bc8fc6f5ba22"
DRIVER = REPO/"experiments/certify_mixed_selected_half_row_budget.py"
DRIVER_SHA = "c3fcced82e6677c65f7f76242e9ca7b00712e236d50a3608bca589e5456f0f34"
PROOF = REPO/"notes/research_mixed_centered_primitive_enclosure.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if digest(PREVIOUS) != PREVIOUS_SHA or digest(DRIVER) != DRIVER_SHA:
        raise ValueError("immutable input hash mismatch")
    previous = json.loads(PREVIOUS.read_text())
    if previous["precision_bits"] != 160 or previous["visited_cells"] != 12000:
        raise ValueError("unexpected original record")
    bindings = dict(previous["input_sha256"])
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise ValueError("original dependency changed: "+name)
    bindings[str(PREVIOUS.relative_to(REPO))] = PREVIOUS_SHA
    bindings[str(PROOF.relative_to(REPO))] = digest(PROOF)
    bindings[str(Path(__file__).resolve().relative_to(REPO))] = digest(Path(__file__))

    candidates = [item for item in previous["leaves"] if item["status"] == "accepted"]
    leaf = max(candidates, key=lambda item: F(
        item["certificate"]["majorants"]["main_factorial"]["value"]["upper_rational"]))
    if len(leaf["address"]) < 2:
        raise ValueError("selected leaf has no two-level parent")
    address = leaf["address"][:-2]

    import certify_mixed_selected_half_row_budget as driver
    from flint import acb, ctx
    ctx.prec = 160
    box = driver.base.ROOT
    for depth, branch in enumerate(address):
        box = driver.base.split(box, depth)[int(branch)]

    class CenteredPrimitives(driver.OriginalPrimitives):
        def g(self, w):
            self.regular(w)
            center = acb(w.real.mid(), w.imag.mid())
            center_value = super().g(center)
            derivative = (1-(-2*self.pi*self.ii*w).exp()).log()
            if not derivative.is_finite():
                raise driver.Inconclusive("centered primitive derivative not finite")
            result = center_value+derivative*(w-center)
            if not result.is_finite():
                raise driver.Inconclusive("centered primitive enclosure not finite")
            return result

    started = time.monotonic()
    original = driver.inspect(box, driver.OriginalPrimitives())
    centered = driver.inspect(box, CenteredPrimitives())
    comparison = {}
    if "majorants" in original[2] and "majorants" in centered[2]:
        for key in driver.KEYS:
            first = original[2]["majorants"][key]["value"]
            second = centered[2]["majorants"][key]["value"]
            first_width = F(first["upper_rational"])-F(first["lower_rational"])
            second_width = F(second["upper_rational"])-F(second["lower_rational"])
            comparison[key] = {
                "original": first, "centered": second,
                "width_ratio_original_over_centered":
                    str(first_width/second_width) if second_width else None,
                "upper_drop_rational":
                    str(F(first["upper_rational"])-F(second["upper_rational"])),
            }
    for name, expected in bindings.items():
        if digest(REPO/name) != expected:
            raise RuntimeError("input changed during diagnostic: "+name)
    record = {
        "status": "diagnostic complete", "precision_bits": 160,
        "scope": "One exact two-level ancestor box; no cover or uniform sign",
        "selected_accepted_address": leaf["address"],
        "selected_saved_main_factorial_upper":
            leaf["certificate"]["majorants"]["main_factorial"]["value"]["upper_rational"],
        "tested_address": address, "tested_box": list(map(str, box)),
        "original": {"status": original[0], "reason": original[1], "details": original[2]},
        "centered": {"status": centered[0], "reason": centered[1], "details": centered[2]},
        "comparison": comparison, "inspect_calls": 2, "tested_boxes": 1,
        "root_proposals": 0, "finite_source_evaluations": 0, "subdivisions": 0,
        "elapsed_seconds": time.monotonic()-started,
        "input_sha256": bindings,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": record["status"], "selected_accepted_address": leaf["address"],
        "tested_address": address, "original_status": original[0],
        "centered_status": centered[0], "elapsed_seconds": record["elapsed_seconds"],
        "comparison": {key: {
            "original_upper": value["original"]["upper_rational"],
            "centered_upper": value["centered"]["upper_rational"],
            "width_ratio": value["width_ratio_original_over_centered"]}
            for key, value in comparison.items()},
    }), flush=True)


if __name__ == "__main__":
    main()
