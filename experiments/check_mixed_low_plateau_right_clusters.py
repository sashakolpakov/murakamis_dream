#!/usr/bin/env python3
"""Closed-neighbor support extension and exact L/P/R source allocation."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_low_plateau_right_clusters.md"
SOURCES = [
    ("full_plateau_right_clusters", "check"),
    ("right_pair_raw_reduction", "check"),
    ("selected_low_plateau_clusters", "check"),
    ("uniform_low_plateau_clusters", "check"),
    ("both_low_raw_support", "certify"),
    ("real_zero_collar", "certify"),
    ("real_one_small_support", "certify"),
    ("oriented_height_reset", "certify"),
    ("full_height_reset", "certify"),
    ("same_sign_height_reset", "certify"),
    ("selected_reset_plateau_support", "certify"),
    ("selected_plateau_support", "certify"),
    ("coupled_outer_graph", "check"),
    ("conditional_torus_composition", "check"),
    ("fourier_weight_continuation", "check"),
    ("boundary_strip_bounds", "check"),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(x):
    x = F(x)
    return arb(x.numerator) / x.denominator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-low-plateau-right-clusters.json")
    args = parser.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    deps, records = {}, {}
    for stem, prefix in SOURCES:
        paths = [f"notes/research_mixed_{stem}.md",
                 f"experiments/{prefix}_mixed_{stem}.py",
                 f"repro/results/research-mixed-{stem.replace('_', '-')}.json"]
        for path in paths:
            deps[path] = sha(ROOT / path)
        record = json.loads((ROOT / paths[2]).read_text())
        assert record["status"] == "passed", stem
        inherited = record.get("dependencies_sha256", record.get("dependencies", {}))
        assert record.get("proof_sha256", inherited.get(paths[0])) == deps[paths[0]], stem
        assert record["script_sha256"] == deps[paths[1]], stem
        for key in ("dependencies", "dependencies_sha256"):
            for path, digest in record.get(key, {}).items():
                assert sha(ROOT / path) == digest, (stem, path)
        records[stem] = record

    pi = arb.pi()
    def ell(x):
        return (2 * (pi * ar(x)).sin()).log()

    outward = []
    def positive(name, value):
        assert value > 0, (name, value)
        outward.append({"name": name, "strict_positive_margin": str(value)})

    positive("lower inner derivative exceeds 13/20",
             ell(F(7, 10)) + ell(F(21, 50)) - 3 * ell(F(1, 5)) - ar(F(13, 20)))
    positive("upper inner derivative is below -1/10",
             -ar(F(1, 10)) - ell(F(4, 5)) - ell(F(13, 25)) + 2 * ell(F(3, 10)))
    positive("outward p derivative exceeds 1/25",
             ell(F(21, 50)) - ar(F(3, 2)) * ell(F(11, 50)) - ar(F(1, 4)) - ar(F(1, 25)))
    for point in (F(1, 5), F(3, 10), F(11, 50)):
        positive(f"ell({point}) positive", ell(point))
    positive("smaller ell endpoint is 21/50",
             ell(F(13, 25)) - ell(F(21, 50)))
    raw = records["right_pair_raw_reduction"]
    assert raw["slope_interval"] == ["-1/5", "1/4"]
    assert raw["target_interval"] == ["11/50", "9/20"]
    assert len(raw["profiles"]) == 4
    assert {(p["epsilon"], p["other_halfweight"]) for p in raw["profiles"]} == set(itertools.product((0, 1), repeat=2))
    for profile in raw["profiles"]:
        assert [F(row["slope"]) for row in profile["grid"]] == [F(-1, 5) + F(j, 40) for j in range(19)]

    # Every typed local reset case is exact rational arithmetic.  Indicators 0/1
    # mean type three/four, independently of the separate region labels below.
    heights = [F(3, 100), F(57, 1000)]
    first, second = F(11, 2), F(151, 20)
    fleft, fright = F(1683, 100000), F(1202, 100000)
    local = []
    for tp, tq in itertools.product((0, 1), repeat=2):
        hp, hq = heights[tp], heights[tq]
        cost = first * hp**2 + second * hq**2 if tp == tq == 1 else 10 * (hp**2 + hq**2)
        for cause in ("right-first", "right-second"):
            debit = cost - (first * hp**2 if cause == "right-first" else second * hq**2)
            assert 0 <= debit < F(1, 25)
            assert F(1, 20) - debit > F(1, 100)
            local.append({"types": [tp, tq], "right_cause": cause,
                          "low_debit": str(debit), "low_loss_remaining": str(F(1, 20) - debit)})
        if not (tp == tq == 1):
            excess = cost - first * hp**2 - second * hq**2
            assert excess < (fright if tp == 0 else fleft)
    assert 10 * heights[1]**2 < F(1, 25)
    assert F(1, 20) - F(1, 25) == F(1, 100)
    assert F(1, 5000) - F(1, 10000) == F(1, 10000)

    # Enumerate original directed edge slots, retaining m=1 loops and m=2
    # parallel edges. The proof's incidence argument is length independent.
    summaries, patterns, mixed_patterns = [], 0, 0
    for m in range(1, 11):
        count = 0
        for region in itertools.product("LPR", repeat=m):
            count += 1
            patterns += 1
            mixed_patterns += len(set(region)) == 3
            nr = region.count("R")
            if nr == m:
                assert F(m, 100) >= F(nr, 20000)
                continue
            runs = []
            for j in range(m):
                if region[j] == "R" and region[(j-1) % m] != "R":
                    run, k = [], j
                    while region[k] == "R":
                        run.append(k)
                        k = (k+1) % m
                    runs.append(run)
            pieces, singles, charges = [], [], {}
            for run_id, run in enumerate(runs):
                start, end = run[0], run[-1]
                a, c = (start-1) % m, (end+1) % m
                assert region[a] != "R" and region[c] != "R"
                charges[run_id, "L"] = a
                charges[run_id, "R"] = c
                if len(run) == 1:
                    pieces.append([(start-1) % m, start])
                elif len(run) == 2:
                    pieces.append([(start-1) % m, start, end])
                else:
                    pieces.extend([[(start-1) % m, start], [(end-1) % m, end]])
                    singles.extend(run[1:-2])
            used = [edge for piece in pieces for edge in piece] + singles
            assert len(used) == len(set(used))
            assert set(used) == {j for j in range(m) if region[j] == "R" or region[(j+1) % m] == "R"}
            low_uses, right_uses, fee_uses = [], [], []
            nlp = nll = 0
            for j in range(m):
                k = (j+1) % m
                if j in used:
                    continue
                if region[j] == region[k] == "L":
                    nll += 1
                    continue
                if region[j] == "L" or region[k] == "L":
                    assert {region[j], region[k]} == {"L", "P"}
                    nlp += 1
                    continue
                assert region[j] == region[k] == "P"
                causes = [region[(j-1) % m], region[(k+1) % m]]
                candidates = []
                for pos, cause in enumerate(causes):
                    if cause == "L":
                        low_edge = (j-1) % m if pos == 0 else k
                        assert set((region[low_edge], region[(low_edge+1) % m])) == {"L", "P"}
                        low_uses.append(low_edge)
                    elif cause == "R":
                        side, vertex = ("R", j) if pos == 0 else ("L", k)
                        keys = [key for key, v in charges.items() if key[1] == side and v == vertex]
                        assert len(keys) == 1
                        right_uses.extend(keys)
                        candidates.extend(keys)
                    else:
                        assert cause == "P"
                if causes == ["R", "R"]:
                    # Depending on the endpoint types, at most one of these
                    # allowances is spent. Checking both possible uses is stronger.
                    assert len(candidates) == 2
                    fee_uses.extend(candidates)
            assert len(low_uses) == len(set(low_uses)) <= nlp
            assert len(right_uses) == len(set(right_uses))
            assert len(fee_uses) == len(set(fee_uses))
            right_loss = F(len(pieces), 10000) + F(len(singles), 100)
            assert right_loss >= F(nr, 20000)
            low_loss = F(nlp, 20) - F(len(low_uses), 25) + F(nll, 100)
            assert low_loss >= F(nlp+nll, 100)
            if nr:
                assert right_loss + low_loss >= F(1, 20000)
            elif "L" in region:
                assert nlp+nll >= 1 and low_loss >= F(1, 100)
            else:
                assert set(region) == {"P"} and right_loss == low_loss == 0
        summaries.append({"length": m, "region_patterns": count})

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / p) == digest for p, digest in deps.items())
    result = dict(
        status="passed", precision_bits=args.precision,
        outward_support_checks=len(outward), outward_support_margins=outward,
        exact_mixed_reset_cases=local, source_records=len(SOURCES),
        region_patterns=patterns, genuinely_three_region_patterns=mixed_patterns,
        pattern_counts=summaries, all_selection_scope="Selections on real blocks have modulus one; active selected PP blocks replace nonnegative debits by proved losses.",
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope="Full original all-selection source bound on closed L/P/R boxes of the coupled contour. The open transition intervals and full outer-period theorem remain outside this result.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS", len(outward), "outward support checks;", len(local),
          "typed mixed reset cases;", patterns, "region patterns;", len(SOURCES), "current records", flush=True)


if __name__ == "__main__":
    main()
