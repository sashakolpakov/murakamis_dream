#!/usr/bin/env python3
"""Check the declared proof dependencies for the matched-sphere volume theorems.

This checks references, premise roles, level scope, assumptions, and cycles.
The mathematical assertions assigned to the nodes remain written proofs.
It neither proves those assertions nor infers them from source hashes.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "repro/manuscript_logic.json"
VOLUME_ROLES = {
    "exact_invariant", "nonzero_contribution", "full_remainder",
    "specified_metric", "absolute_volume", "rate_transfer",
}


class LogicError(ValueError):
    pass


def check(data: dict, root: Path = ROOT) -> dict:
    """Validate a finite, manually supplied dependency map, without modifying it."""
    nodes = data["nodes"]
    assumptions = data["assumptions"]
    reports = {}
    source_hashes = {}
    for identifier, node in nodes.items():
        if node["status"] not in {"written", "open"}:
            raise LogicError(f"{identifier}: invalid status")
        if node["levels"] not in {"all", "odd", "independent"}:
            raise LogicError(f"{identifier}: invalid level scope")
        if not node["statement"].strip():
            raise LogicError(f"{identifier}: empty mathematical statement")
        if set(node["assumptions"]) - assumptions.keys():
            raise LogicError(f"{identifier}: unknown assumption")
        location = node["location"]
        path = root / location["path"]
        if not path.is_file():
            raise LogicError(f"{identifier}: missing source {path}")
        content = path.read_text()
        if location["anchor"] not in content:
            raise LogicError(f"{identifier}: missing source anchor")
        source_hashes[location["path"]] = hashlib.sha256(path.read_bytes()).hexdigest()
        for role, dependency in node["requires"].items():
            if dependency not in nodes:
                raise LogicError(f"{identifier}: missing dependency {dependency}")
            if role not in nodes[dependency]["provides"]:
                raise LogicError(f"{identifier}: {dependency} does not supply {role}")
        if "volume_limit" in node["provides"] and set(node["requires"]) != VOLUME_ROLES:
            raise LogicError(f"{identifier}: a volume conclusion needs all six premise roles")

    def visit(identifier: str, stack: tuple[str, ...] = ()) -> dict:
        if identifier in stack:
            raise LogicError("Circular dependency: " + " -> ".join((*stack, identifier)))
        if identifier in reports:
            return reports[identifier]
        node = nodes[identifier]
        inherited = set(node["assumptions"])
        unresolved = {identifier} if node["status"] == "open" else set()
        odd = {identifier} if node["levels"] == "odd" else set()
        closure = {identifier}
        for dependency in node["requires"].values():
            report = visit(dependency, (*stack, identifier))
            inherited.update(report["assumptions"])
            unresolved.update(report["unresolved"])
            odd.update(report["odd_level_inputs"])
            closure.update(report["closure"])
        if node["levels"] == "all" and odd:
            raise LogicError(f"{identifier}: all-level conclusion uses odd-only input {sorted(odd)}")
        if node["status"] == "written" and unresolved:
            raise LogicError(f"{identifier}: written conclusion uses open input {sorted(unresolved)}")
        report = {
            "assumptions": sorted(inherited), "unresolved": sorted(unresolved),
            "odd_level_inputs": sorted(odd), "closure": sorted(closure),
        }
        reports[identifier] = report
        return report

    for identifier in nodes:
        visit(identifier)
    for identifier, contract in data["conclusions"].items():
        if identifier not in nodes:
            raise LogicError(f"Missing conclusion {identifier}")
        report = reports[identifier]
        if report["assumptions"] != sorted(contract["assumptions"]):
            raise LogicError(f"{identifier}: declared assumptions differ from dependency closure")
        if report["unresolved"] != sorted(contract["unresolved"]):
            raise LogicError(f"{identifier}: undeclared unresolved obligations")
    return {
        "scope": data["scope"],
        "meaning": "Structural consistency of the declared proof map; not verification of its mathematical nodes.",
        "conclusions": {key: reports[key] for key in data["conclusions"]},
        "nodes_checked": len(nodes), "source_sha256": source_hashes,
    }


def negative_controls(data: dict) -> list[str]:
    """Make actual defects in the map and require their rejection."""
    cases = []
    broken = deepcopy(data)
    del broken["nodes"]["weak_balance_volume"]["requires"]["full_remainder"]
    cases.append(("missing full-remainder premise", broken))
    broken = deepcopy(data)
    broken["nodes"]["weak_balance_volume"]["requires"]["full_remainder"] = "general_remainder"
    cases.append(("open remainder substituted into proved route", broken))
    broken = deepcopy(data)
    broken["nodes"]["weak_balance_remainder"]["levels"] = "odd"
    cases.append(("odd-only estimate used for all levels", broken))
    broken = deepcopy(data)
    broken["nodes"]["weak_balance_remainder"]["requires"]["volume_limit"] = "weak_balance_volume"
    cases.append(("conclusion reused to prove its remainder", broken))
    broken = deepcopy(data)
    broken["nodes"]["weak_balance_volume"]["requires"]["full_remainder"] = "central_contribution"
    cases.append(("central contribution substituted for full remainder", broken))
    broken = deepcopy(data)
    broken["conclusions"]["weak_balance_volume"]["assumptions"].remove("weak_balance")
    cases.append(("packing hypothesis omitted from conclusion", broken))
    broken = deepcopy(data)
    broken["nodes"]["specified_metric"]["location"]["anchor"] = "nonexistent-proof-anchor"
    cases.append(("missing geometric proof reference", broken))
    broken = deepcopy(data)
    broken["conclusions"]["ordinary_boundary_volume"]["assumptions"].remove("ordinary_boundary_inputs")
    cases.append(("thin-boundary certificate hypotheses omitted", broken))
    broken = deepcopy(data)
    broken["nodes"]["ordinary_boundary_certificate"]["requires"]["conditional_disk_action"] = "central_contribution"
    cases.append(("central period substituted for conditional disk identity", broken))
    rejected = []
    for name, broken in cases:
        try:
            check(broken)
        except LogicError:
            rejected.append(name)
        else:
            raise LogicError("Negative control was accepted: " + name)
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    report = check(data)
    report["negative_controls_rejected"] = negative_controls(data)
    for path in (MANIFEST, Path(__file__).resolve()):
        report["source_sha256"][str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Checked {report['nodes_checked']} declared proof steps and {len(report['negative_controls_rejected'])} invalid substitutions.")
    print("The general remainder remains open. The mathematical nodes retain their written proofs.")


if __name__ == "__main__":
    main()
