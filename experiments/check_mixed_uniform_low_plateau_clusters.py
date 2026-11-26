#!/usr/bin/env python3
"""Exact zero-uniform cluster assembly with original source provenance."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_uniform_low_plateau_clusters.md"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"repro/results/research-mixed-uniform-low-plateau-clusters.json")
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    specs = [
        ("mixed_real_zero_collar", "certify"),
        ("mixed_real_one_small_support", "certify"),
        ("mixed_both_low_raw_support", "certify"),
        ("mixed_full_height_reset", "certify"),
        ("mixed_coupled_outer_graph", "check"),
        ("mixed_fourier_weight_continuation", "check"),
        ("mixed_plateau_accretivity", "check"),
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

    check("left cutoff matching", F(25, 3)*(F(11, 50)-F(1, 10)) == 1)
    check("right cutoff matching", 20*(F(1, 2)-F(9, 20)) == 1)
    check("three incidence derivative budget", 3*F(57, 1000)*20 == F(171, 50))
    check("Jacobian budget", 1+F(171, 50)**2 < F(18, 5)**2)
    check("plateau strictly below half endpoint", F(9, 20) < F(1, 2))
    check("zero collar meets compact low interval", F(0) < F(1, 1000) < F(1, 10))
    check("collar gap dominates uniform LP gap", F(3, 50) > F(1, 20))
    gap = F(1, 20)-10*F(57, 1000)**2
    check("exact LP debit after reset charging", gap == F(1751, 100000))
    check("LP reserve exceeds raw LL gap", gap > F(1, 100))
    check("critical type-three coordinates on plateau",
          F(11, 50) < F(30, 100) < F(39, 100) < F(9, 20))
    check("critical type-four coordinates on plateau",
          F(11, 50) < F(27, 100) < F(33, 100) < F(9, 20))
    patterns = []
    for length in range(1, 11):
        for low in itertools.product((0, 1), repeat=length):
            if not any(low):
                continue
            reset = [not low[j] and (low[(j-1) % length] or low[(j+1) % length])
                     for j in range(length)]
            rho = [1-v for v in low]
            height_kept = [rho[(j-1) % length]*rho[j]*rho[(j+1) % length]
                           for j in range(length)]
            assert all(height_kept[j] == int(not low[j] and not reset[j])
                       for j in range(length))
            nlp = sum(low[j] != low[(j+1) % length] for j in range(length))
            nll = sum(low[j] and low[(j+1) % length] for j in range(length))
            debit = sum(int(reset[j])+int(reset[(j+1) % length])
                        for j in range(length) if not low[j] and not low[(j+1) % length])
            assert debit <= nlp and nlp+nll >= 1
            loss = F(1, 20)*nlp+F(1, 100)*nll-10*F(57, 1000)**2*debit
            assert loss >= F(nlp+nll, 100)
            patterns.append({"length": length, "low": list(low),
                             "LP_edges": nlp, "LL_edges": nll, "PP_debit": debit})
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    result = {
        "status": "passed", "arithmetic": "exact rational and finite incidence arithmetic",
        "scalar_checks": len(checks), "checks": checks,
        "cyclic_patterns": len(patterns), "patterns": patterns,
        "source_records": len(specs),
        "unaliased_low_region_gap": "1/100",
        "proof_sha256": ph, "script_sha256": sh,
        "dependencies_sha256": deps,
        "scope": "Zero-uniform original unaliased low/plateau region on one exact coupled graph. No transition/right-region transfer, selected-alias or full-cycle claim.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "scalar checks,", len(patterns), "cyclic patterns,",
          len(specs), "current source records")


if __name__ == "__main__":
    main()
