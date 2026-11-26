#!/usr/bin/env python3
"""Exact all-selection, closed low/plateau cluster assembly."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_selected_low_plateau_clusters.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-mixed-selected-low-plateau-clusters.json")
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    specs = [
        ("mixed_uniform_low_plateau_clusters", "check"),
        ("mixed_selected_reset_plateau_support", "certify"),
        ("mixed_selected_plateau_support", "certify"),
        ("mixed_conditional_torus_composition", "check"),
    ]
    deps = {}
    for stem, prefix in specs:
        pp = f"notes/research_{stem}.md"
        ss = f"experiments/{prefix}_{stem}.py"
        rr = f"repro/results/research-{stem.replace('_', '-')}.json"
        for p in (pp, ss, rr):
            deps[p] = sha(ROOT/p)
        rec = json.loads((ROOT/rr).read_text())
        assert rec["status"] == "passed", stem
        assert rec["script_sha256"] == deps[ss], stem
        inherited = rec.get("dependencies_sha256", rec.get("dependencies", {}))
        assert rec.get("proof_sha256", inherited.get(pp)) == deps[pp], stem
        for key in ("dependencies", "dependencies_sha256"):
            assert all(sha(ROOT/p) == h for p, h in rec.get(key, {}).items()), stem
    checks = []

    def check(name, value):
        assert value, name
        checks.append(name)

    check("selected height within Jacobian budget", F(7, 500) < F(57, 1000))
    check("exact LP loss after maximal reset debit",
          F(1, 20)-10*F(57, 1000)**2 == F(1751, 100000))
    check("LP residual exceeds LL loss", F(1751, 100000) > F(1, 100))
    check("low region loss exceeds selected-only loss", F(1, 100) > F(1, 200))
    check("selected source phase reserve", F(1, 100) > F(1, 200))
    summary, total = [], 0
    for length in range(1, 8):
        count = 0
        # The four states are all combinations of low/not-low and selected/not-selected.
        # Allowing a selection at every vertex includes every legal type-four subset.
        for state in itertools.product(range(4), repeat=length):
            low = [v//2 for v in state]
            selected = [v % 2 for v in state]
            reset = [not low[j] and (low[(j-1) % length] or low[(j+1) % length])
                     for j in range(length)]
            active = [bool(selected[j] and not low[j] and not reset[j])
                      for j in range(length)]
            nlp = nll = ns = debit = 0
            for j in range(length):
                k = (j+1) % length
                if low[j] and low[k]:
                    nll += 1
                elif low[j] or low[k]:
                    nlp += 1
                elif active[j] or active[k]:
                    ns += 1
                    # If one endpoint is reset this is the new selected-reset source;
                    # otherwise it is the completed selected-plateau source.
                    assert not (reset[j] and reset[k])
                else:
                    debit += int(reset[j])+int(reset[k])
                    assert all(not selected[v] or reset[v] for v in (j, k))
            assert debit <= nlp
            loss = F(nlp, 20)+F(nll, 100)+F(ns, 200)-10*F(57, 1000)**2*debit
            assert loss >= F(nlp+nll, 100)+F(ns, 200)
            if any(low):
                assert nlp+nll >= 1 and loss >= F(1, 100)
            elif any(selected):
                assert ns >= 1 and loss >= F(1, 200)
            else:
                assert nlp == nll == ns == debit == 0 and loss == 0
            count += 1
        summary.append({"length": length, "patterns": count})
        total += count
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    result = {
        "status": "passed", "arithmetic": "exact rational and finite incidence arithmetic",
        "scalar_checks": len(checks), "checks": checks,
        "selection_and_low_patterns": total, "pattern_counts": summary,
        "source_records": len(specs), "low_region_gap": "1/100", "selected_plateau_gap": "1/200",
        "proof_sha256": ph, "script_sha256": sh, "dependencies_sha256": deps,
        "scope": "All original selected terms on the closed low/plateau region of specified coupled graphs. No remaining-region or full-cycle claim.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "scalar checks,", total, "selection/low patterns,", len(specs), "current source records")


if __name__ == "__main__":
    main()
