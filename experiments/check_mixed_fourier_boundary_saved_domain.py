#!/usr/bin/env python3
"""One fixed rational recombination of existing boundary-map enclosures."""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "repro/results/research-mixed-fourier-boundary-update.json"
SOURCE_SHA = "5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514"
PROTOCOL = ROOT / "notes/research_mixed_fourier_boundary_saved_domain_protocol.md"
OUTPUT = ROOT / "repro/results/research-mixed-fourier-boundary-k3-saved-domain.json"
NAMES = ("lower_imaginary", "upper_imaginary", "oblique")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def interval(value):
    require(value["finite"] is True, "nonfinite saved interval")
    lo, hi = F(value["lower_rational"]), F(value["upper_rational"])
    require(lo <= hi, "reversed saved interval")
    return lo, hi


def bindings(data):
    expected = data["input_sha256"]
    require(len(expected) == data["input_binding_count"], "binding count")
    require(expected == data["input_sha256_after"], "old inputs changed")
    actual = {name: sha(ROOT / name) for name in expected}
    require(actual == expected, "an original source binding changed")
    return actual


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--script-sha", required=True)
    parser.add_argument("--protocol-sha", required=True)
    args = parser.parse_args()
    result = {
        "status": "initializing",
        "analytic_evaluations": 0,
        "adaptive_choices": 0,
        "arcs": [],
        "source_sha256": SOURCE_SHA,
        "script_sha256": args.script_sha,
        "protocol_sha256": args.protocol_sha,
        "scope": "Whole independent D4 image only; no actual-word exclusion.",
    }
    # An existing result is never overwritten, including after an incomplete run.
    with OUTPUT.open("x") as out:
        try:
            require(sha(Path(__file__)) == args.script_sha, "script hash")
            require(sha(PROTOCOL) == args.protocol_sha, "protocol hash")
            require(sha(SOURCE) == SOURCE_SHA, "saved source hash")
            data = json.loads(SOURCE.read_text())
            require(data["status"] == "passed", "source status")
            require(data["inclusion_certified"] is True, "source inclusion")
            require(data["all_inputs_unchanged"] is True, "source bindings")
            require(data["full_analytic_inventory_completed"] is True,
                    "source inventory incomplete")
            require(data["visited_arcs"] == data["passed_arcs"] == 512,
                    "source arc counts")
            require(data["failed_arcs"] == data["inconclusive_arcs"] == 0,
                    "source failed arc")
            require([a["index"] for a in data["arcs"]] == list(range(512)),
                    "source arc inventory")
            result["bindings_before"] = bindings(data)
            for arc in data["arcs"]:
                i = arc["index"]
                require(arc["status"] == "passed", "arc status")
                require(all(arc["guards"].values()), "arc guard")
                require([F(v) for v in arc["parameter_rational"]] ==
                        [F(i, 512), F(i + 1, 512)], "arc coverage")
                radius_upper = F(
                    arc["conservative_squared_distance_upper_rational"])
                require(radius_upper < F(83, 1000) ** 2,
                        "saved radius does not enter P3")
                rlo, rhi = interval(arc["b"]["real"])
                ilo, ihi = interval(arc["b"]["imag"])
                lower = (ilo + F(9, 125), F(17, 250) - ihi,
                         F(76, 125) - rhi + 3 * ilo)
                upper = (ihi + F(9, 125), F(17, 250) - ilo,
                         F(76, 125) - rlo + 3 * ihi)
                checks = {}
                for name, lo, hi in zip(NAMES, lower, upper):
                    require(lo <= hi, "recombined margin interval")
                    status = ("contained" if lo >= 0 else
                              "violates" if hi < 0 else "inconclusive")
                    checks[name] = {
                        "lower_margin_rational": str(lo),
                        "upper_margin_rational": str(hi),
                        "status": status,
                    }
                result["arcs"].append({
                    "index": i,
                    "parameter_rational": arc["parameter_rational"],
                    "saved_b": arc["b"],
                    "radius_squared_upper_rational": str(radius_upper),
                    "checks": checks,
                })
            result["bindings_after"] = bindings(data)
            require(sha(SOURCE) == SOURCE_SHA, "saved source changed")
            require(sha(Path(__file__)) == args.script_sha, "script changed")
            require(sha(PROTOCOL) == args.protocol_sha, "protocol changed")
            flat = [(a["index"], name, a["checks"][name])
                    for a in result["arcs"] for name in NAMES]
            violations = [
                {"arc": i, "halfplane": name,
                 "upper_margin_rational": c["upper_margin_rational"]}
                for i, name, c in flat if c["status"] == "violates"
            ]
            result["certified_boundary_violations"] = violations
            result["counts"] = {
                status: sum(c["status"] == status for _, _, c in flat)
                for status in ("contained", "violates", "inconclusive")
            }
            result["status"] = (
                "disproved_on_boundary" if violations else
                "contained" if all(c["status"] == "contained"
                                   for _, _, c in flat) else "inconclusive"
            )
        except Exception as exc:
            result.update(status="invalid", error=repr(exc))
        json.dump(result, out, indent=2, sort_keys=True)
        out.write("\n")
    print(json.dumps({k: result[k] for k in
                      ("status", "analytic_evaluations", "adaptive_choices")}))
    if "counts" in result:
        print(json.dumps(result["counts"], sort_keys=True))
    if result["status"] == "invalid":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
