#!/usr/bin/env python3
"""Check the completed scaled certificate and its rational energy consequences.

This does not rerun the interval verification. It checks the saved independent
replay's provenance and the exact scalar arithmetic used after that verification.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    artifact = ROOT/"repro/results/research-pair-height-sector-scaled.json"
    report_path = artifact.with_name(artifact.stem+"-replay.json")
    report = json.loads(report_path.read_text())
    assert report["status"] == "passed"
    assert report["mode"] == "scaled" and report["precision_bits"] >= 160
    assert report["replayed_boxes"] == 77088
    assert report["parameter_cover"]["multiplicity"] == 1
    assert F(report["parameter_cover"]["area"]) == F(28, 25)
    assert report["certificate_sha256"] == sha256(artifact)
    replay_script = ROOT/"experiments/replay_pair_height_sector.py"
    assert report["script_sha256"] == sha256(replay_script)
    with artifact.open() as stream:
        header = stream.read(65536).split(',"certificate":', 1)[0]+"}"
    source = json.loads(header)
    assert source["status"] == "passed" and source["pending"] == []
    assert source["accepted_boxes"] == report["replayed_boxes"]
    assert source["domain"] == {
        "sector_coordinate": ["0", "1"],
        "height": ["3/100", "23/20"],
    }
    for filename, expected in source["sha256"].items():
        assert sha256(ROOT/filename) == expected, filename

    results = []

    def compare(name, left, right, relation="<"):
        assert (left < right) if relation == "<" else (left == right), name
        results.append({
            "name": name, "left": str(left), "relation": relation,
            "right": str(right),
        })

    slope, cap = F(59, 50), F(23, 20)
    switch = cap/slope
    compare("height-envelope switch", switch, F(115, 118), "=")
    integrated = slope*switch**2+2*cap*(1-switch)
    pair = F(2783, 2360)
    compare("integrated pair cost", integrated, pair, "=")
    catalan_lower = sum((F((-1)**j, (2*j+1)**2)
                         for j in range(64)), F(0))
    rate_lower = 4*catalan_lower/F(22, 7)
    compare("complete-edge rate lower bound", F(11657, 10000), rate_lower)
    compare("both powers at least four", F(8, 9)*pair, F(2783, 2655), "=")
    one_sided = cap+(pair-cap)*F(8, 15)
    compare("one power at least ten", one_sided, F(6877, 5900), "=")
    compare("both-power estimate is stronger", F(2783, 2655), one_sided)
    compare("isolated-edge gap", one_sided+F(1, 10000), F(11657, 10000))
    run_cost = (pair+cap)/2
    compare("two-edge run cost per edge", run_cost, F(5497, 4720), "=")
    compare("longer odd runs", pair, 3*cap)
    compare("nonisolated-edge gap", run_cost+F(1, 1000), F(11657, 10000))
    compare("singleton gap", cap+F(1, 1000), F(11657, 10000))
    # G<11/12 and pi>157/50 give M_infinity<550/471.
    catalan_upper = sum((F((-1)**j, (2*j+1)**2)
                         for j in range(15)), F(0))
    compare("Catalan upper bound", catalan_upper, F(11, 12))
    compare("Machin lower bound", F(157, 50),
            16*(F(1, 5)-F(1, 375))-F(4, 239))
    compare("scaled cost does not alone give the target", F(550, 471), pair)
    small_path = ROOT/"repro/results/research-pair-activation-small-height.json"
    small = json.loads(small_path.read_text())
    assert small["status"] == "passed"
    assert small["script_sha256"] == sha256(
        ROOT/"experiments/check_pair_activation_small_height.py")
    dependencies = (
        "experiments/check_scaled_pair_activation_consequences.py",
        "notes/research_scaled_pair_activation_consequences.md",
        "notes/research_pair_activation_small_height.md",
        "notes/research_edge_cut_energy_comparison.md",
        "repro/results/research-pair-height-sector-scaled-replay.json",
        "repro/results/research-pair-activation-small-height.json",
    )
    record = {
        "status": "passed",
        "scope": "Completed independent support replay and exact energy-comparison arithmetic",
        "rational_checks": len(results),
        "checks": results,
        "support_certificate_sha256": report["certificate_sha256"],
        "support_replay_sha256": sha256(report_path),
        "support_precision_bits": report["precision_bits"],
        "support_boxes": report["replayed_boxes"],
        "project_dependency_sha256": {
            name: sha256(ROOT/name) for name in dependencies
        },
    }
    output = ROOT/"repro/results/research-scaled-pair-activation-consequences.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({
        "status": "passed", "rational_checks": len(results),
        "support_boxes": report["replayed_boxes"],
        "support_precision_bits": report["precision_bits"],
    }, indent=2))


if __name__ == "__main__":
    main()
