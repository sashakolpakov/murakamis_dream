#!/usr/bin/env python3
"""Reproduce the five interval certificates for the internal (3,3) pair.

The default recomputes every certificate. --verify-saved checks that the
complete saved records match their current source files; it does not
recompute their numerical inequalities or verify the written proofs.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"
RESULTS = ROOT / "repro/results"
CASES = [
    ("mixed_packet", "mixed-packet", "surfaces", 19),
    ("central_period", "central-period", "covers", 31),
    ("low_wire_complement", "low-wire-complement", "surfaces", 3),
    ("right_period", "right-period", "surfaces", 4),
    ("high_half", "high-half", "surfaces", 6),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-saved", action="store_true")
    parser.add_argument("--precision", type=int, default=180)
    args = parser.parse_args()
    if args.precision < 140:
        parser.error("Use at least 140 bits.")
    checked = []
    for suffix, slug, field, count in CASES:
        script = EXPERIMENTS / ("certify_internal_pair_three_" + suffix + ".py")
        result = RESULTS / ("research-internal-pair-three-" + slug + ".json")
        if not args.verify_saved:
            subprocess.run(
                [sys.executable, str(script), "--precision", str(args.precision),
                 "--output", str(result)],
                cwd=ROOT, check=True,
            )
        record = json.loads(result.read_text())
        assert record["status"] == "certified", result
        assert len(record[field]) == count, (result, field, count)
        assert record["script_sha256"] == digest(script), script
        aliases = {
            "engine_sha256": "certify_terminal_three_central_phase.py",
            "mixed_root_script_sha256": "certify_internal_pair_three_mixed_packet.py",
            "root_script_sha256": "certify_internal_pair_three_mixed_packet.py",
        }
        for key, filename in aliases.items():
            if key in record:
                assert record[key] == digest(EXPERIMENTS / filename), (result, key)
        for filename, expected in record.get("dependencies", {}).items():
            assert expected == digest(EXPERIMENTS / filename), (result, filename)
        checked.append({
            "certificate": str(result.relative_to(ROOT)),
            "sha256": digest(result),
            "complete_cover_domains": count,
        })
        print(slug + ": complete, sources match", flush=True)
    report = {
        "status": "saved-records-verified" if args.verify_saved else "recomputed",
        "scope": (
            "Five complete interval-certificate records with matching sources. "
            "The source identities, contour assembly, geometric identification, "
            "and asymptotic implications retain their written proofs."
        ),
        "runner_sha256": digest(Path(__file__)),
        "certificates": checked,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    path = RESULTS / "research-internal-pair-three-reproduction.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(str(path), flush=True)


if __name__ == "__main__":
    main()
