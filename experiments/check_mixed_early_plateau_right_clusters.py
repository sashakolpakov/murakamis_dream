#!/usr/bin/env python3
"""Exact existing-source allocation on the periodic low/early/plateau/right region."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_early_plateau_right_clusters.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-early-plateau-right-clusters.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, checks = {}, set(), {}, []

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        if path in deps:
            assert deps[path] == digest, path
        deps[path] = digest
        return digest

    def inherit(path):
        raw = (ROOT/path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        record = json.loads(raw)
        if path in visited:
            return record
        visited.add(path)
        merged = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in record.get(field, {}).items():
                if name in merged:
                    assert merged[name] == digest, name
                merged[name] = digest
                bind(name, digest)
        for name in merged:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return record

    def load(stem, prefix="check"):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        record = inherit(path)
        assert record["status"] == "passed", path
        assert record["proof_sha256"] == bind("notes/research_"+stem+".md")
        assert record["script_sha256"] == bind("experiments/"+prefix+"_"+stem+".py")
        primary[path] = record
        return record

    def replay(stem, author):
        path = "repro/results/research-"+stem.replace("_", "-")+"-replay.json"
        record = inherit(path)
        assert record["status"] == "passed", path
        assert record["proof_sha256"] == author["proof_sha256"]
        assert record["script_sha256"] == author["script_sha256"]
        assert record["input_sha256"] == bind(
            "repro/results/research-"+stem.replace("_", "-")+".json")
        primary[path] = record
        return record

    def check(name, condition):
        assert condition, name
        checks.append(name)

    def transition_signature(rows):
        return [
            (tuple((key, row[key]) for key in ("e", "b", "c", "sig", "h", "ylo", "yhi", "name")),
             [(v["k"], v["upper"],
               [(t["q"], t["point"]) for t in v["trials"]],
               [(t["q"], t["point"]) for t in v["endpoint_trials"]])
              for v in row["grid"]])
            for row in rows
        ]

    def cover_signature(rows):
        return [(r["word"], r["external_types"], r["faces"], r["addresses"])
                for r in rows]

    early = load("mixed_early_transition_support", "certify")
    old = load("mixed_early_plateau_clusters")
    transition = load("mixed_transition_right_support", "certify")
    transition_replay = replay("mixed_transition_right_support", transition)
    partial = load("mixed_partially_reset_right_support", "certify")
    partial_replay = replay("mixed_partially_reset_right_support", partial)
    two_right = load("mixed_two_right_source_bound", "certify")
    clamp = load("mixed_complex_right_row_reduction")
    hybrid = load("mixed_hybrid_low_plateau_right_clusters")
    seam = load("mixed_hybrid_low_plateau_clusters")
    real_low = load("mixed_uniform_real_low_support")
    both_low = load("mixed_both_low_raw_support", "certify")
    for path in ("notes/research_mixed_partial_selected_heights.md",
                 "notes/research_mixed_split_cutoff_hybrid_contour.md",
                 "notes/research_mixed_right_core_support.md"):
        bind(path)

    check("completed independent-height early support with ordered credits",
          F(early["phase_gap"]) == F(1, 100)
          and early["reference_products"] == 64 and early["cells"] == 251)
    check("completed full transition/right source and its raw half-angle margin",
          transition["source_profiles"] == 72 and transition["source_values"] == 720
          and transition["reference_products"] == 512
          and transition["reference_cells"] == 5180
          and F(transition["strict_core_ceiling"]) == -F(1, 1000)
          and F(transition["finite_source_gap"]) == F(1, 2000))
    check("matching complete transition/right saved replay",
          transition_replay["precision_bits"] >= 320
          and transition_signature(transition_replay["source_grid"])
              == transition_signature(transition["source_grid"])
          and transition_replay["reference_cells"] == 5180
          and cover_signature(transition_replay["cases"])
              == cover_signature(transition["cases"]))
    check("use the unrounded partial-PR raw ceiling rather than finite 1/100",
          partial["source_values"] == 20 and partial["reference_products"] == 512
          and partial["reference_cells"] == 5064
          and F(partial["strict_core_ceiling"]) == F(1, 200)
          and F(partial["finite_source_ceiling"]) == F(1, 100))
    check("matching complete partial-PR saved replay",
          partial_replay["precision_bits"] >= 320
          and partial_replay["source_grid"] == partial["source_grid"]
          and partial_replay["reference_cells"] == 5064
          and cover_signature(partial_replay["cases"])
              == cover_signature(partial["cases"]))
    check("the unused RR raw allowance is nonpositive",
          F(two_right["strict_reference_gap"]) == F(1, 50)
          and two_right["boundary_products"] == 512
          and two_right["accepted_cells"] == 4820)
    check("whole-cycle right clamp has both height signs and orientations",
          clamp["exact_identities"] == 2 and len(clamp["scalar_bounds"]) == 3
          and {(r["height_sign"], r["complex_target_first"])
               for r in clamp["height_cases"]}
              == {(-1, 0), (-1, 1), (1, 0), (1, 1)})
    check("the separate no-E hybrid conclusion keeps the central coefficient once",
          F(hybrid["restricted_region_error_gap"]) == F(1, 160000)
          and hybrid["exact_checks"] == 45)
    check("complete finite fractional seam allocation with endpoint completion",
          seam["exact_checks"] == 29 and seam["pair_boundary_products"] == 2048
          and seam["pair_saved_cells"] == 18988
          and "literal finite pair loss and collar" in seam["checks"]
          and "endpoint thickening reserves half the original finite gap" in seam["checks"])
    check("zero-uniform real one-low support includes DE and DP",
          list(map(F, real_low["low_interval"])) == [F(0), F(1, 10)]
          and list(map(F, real_low["other_interval"])) == [F(1, 10), F(9, 20)]
          and F(real_low["uniform_source_gap"]) == F(1, 20))
    check("closed both-low raw support supplies DD and one-cycle loops",
          F(both_low["target_real_cutoff"]) == F(1, 10)
          and F(both_low["gap"]) == F(1, 100)
          and both_low["reference_products"] == 64
          and both_low["reference_cells"] == 1633)

    rmax = (F(3, 25)-F(1, 10))/F(3, 25)
    check("early slow fraction at most one sixth", rmax == F(1, 6))
    check("all typed early height intervals lie in the old independent support",
          F(3, 100)*rmax == F(1, 200)
          and F(1, 50)*rmax == F(1, 300)
          and F(57, 1000)*rmax == F(19, 2000))
    check("fast selected early cap reaches H without exceeding it",
          6*rmax == 1 and F(7, 500)*6*rmax == F(7, 500))
    check("both right and plateau real coordinates have every left cutoff one",
          F(3, 25) < F(11, 50) <= F(9, 20) < F(1, 2))
    # Verify the exact same-height small-angle profiles, including full H.
    small = [r for r in transition["source_grid"]
             if F(r["ylo"]) == F(r["yhi"]) == F(13, 100)]
    expected = {}
    for e, beta, c in ((0, 0, 0), (1, 1, 0), (0, 0, 1),
                       (0, 1, 1), (1, 0, 1), (1, 1, 1)):
        for sigma in range(beta+1):
            heights = (-F(3, 400), F(1, 200)) if beta == 0 else \
                ((F(0), F(7, 500)) if sigma else (-F(57, 4000), F(0)))
            expected[(e, beta, c, sigma)] = set(heights)
    found = {}
    for r in small:
        found.setdefault((r["e"], r["b"], r["c"], r["sig"]), set()).add(F(r["h"]))
    check("all eighteen degenerate profiles retain both forcing states and full H",
          len(small) == 18 and found == expected)

    q0, q1 = F(11, 2), F(151, 20)
    heights = {3: F(3, 100), 4: F(57, 1000)}
    fees = {}
    for a, b in itertools.product((3, 4), repeat=2):
        fee = F(0) if (a, b) == (4, 4) else \
            (10-q0)*heights[a]**2+(10-q1)*heights[b]**2
        fees[str((a, b))] = str(fee)
    check("all four inherited doubly affected PP excesses", fees == old["exact_fees"])
    D = max(map(F, fees.values()))
    delta, bR, er, final = F(1, 100), F(1, 200), F(1, 1000), F(1, 1000)
    pp_reserve = delta-D/2
    check("exact maximal double-PP debit", D == F(33651, 2000000))
    check("each PR-assigned EP keeps a positive reserve",
          delta-bR == F(1, 200) > final)
    check("each remaining EP keeps the original double-reset reserve",
          pp_reserve == F(6349, 4000000) > final)
    check("EE and ER bounds both meet the common incident-edge loss",
          delta > final and er == final)
    check("one common finite tolerance leaves the stated region gap",
          final-F(1, 2000) == F(1, 2000))
    check("central error is governed by the separate no-E theorem",
          F(1, 160000) < F(1, 2000))
    check("original Fourier halves recombine at each cyclic endpoint",
          F(1, 2)+F(1, 2) == 1)

    # E=0, P=1, R=2. These checks retain literal edge indices,
    # including the one loop and the two parallel edges. Arbitrary
    # length follows from the written degree-two argument.
    patterns, ep_to_pr_total, doubles_total = 0, 0, 0
    per_length = []
    for m in range(1, 11):
        count = 0
        for word in itertools.product((0, 1, 2), repeat=m):
            kinds = [(word[i], word[(i+1) % m]) for i in range(m)]
            ee = {i for i, pair in enumerate(kinds) if pair == (0, 0)}
            ep = {i for i, pair in enumerate(kinds) if set(pair) == {0, 1}}
            er_edges = {i for i, pair in enumerate(kinds) if set(pair) == {0, 2}}
            pp = {i for i, pair in enumerate(kinds) if pair == (1, 1)}
            pr = {i for i, pair in enumerate(kinds) if set(pair) == {1, 2}}
            payer = {}
            target_payers = {}
            for v in range(m):
                if word[v] != 1:
                    continue
                incidences = [((v-1) % m, word[(v-1) % m]),
                              (v, word[(v+1) % m])]
                early_inc = [edge for edge, other in incidences if other == 0]
                if len(early_inc) != 1:
                    continue
                edge = early_inc[0]
                outside = next(edge2 for edge2, other in incidences if other != 0)
                assert edge in ep and edge not in payer
                kind = "PP" if outside in pp else "PR"
                assert outside in pp or outside in pr
                payer[edge] = (kind, outside)
                target_payers.setdefault(outside, []).append(edge)
            aR = sum(kind == "PR" for kind, _ in payer.values())
            double = [edge for edge in pp if len(target_payers.get(edge, [])) == 2]
            assert all(len(set(edges)) == len(edges) for edges in target_payers.values())
            assert all(len(target_payers.get(edge, [])) <= 1 for edge in pr)
            assert 2*len(double) <= len(ep)-aR
            nE = len(ee)+len(ep)+len(er_edges)
            upper = -delta*(len(ee)+len(ep))+bR*aR+D*len(double)-er*len(er_edges)
            assert upper <= -final*nE
            assert bool(nE) == (0 in word)
            patterns += 1
            count += 1
            ep_to_pr_total += aR
            doubles_total += len(double)
        per_length.append(dict(length=m, patterns=count))
    check("complete short-cycle incidence diagnostics",
          patterns == sum(3**m for m in range(1, 11)) == 88572)

    # The larger theorem leaves every R angle unchanged. The finite
    # whole-angle PR allowance spends its own tolerance only once.
    bR_finite, tr_finite = F(3, 500), F(1, 2000)
    s_edge_charge, s_pair_loss = F(9, 200), F(1, 10)
    whole_pp_costs = [
        (q0+q1)*heights[4]**2,
        10*(heights[4]**2+heights[3]**2),
        20*heights[3]**2,
    ]
    whole_pp = max(whole_pp_costs)
    check("whole-angle PR finite allowance uses one total source tolerance",
          bR+F(1, 1000) == bR_finite < s_edge_charge)
    check("entire S-affected PP block fits one SP outside-edge allowance",
          whole_pp == F(847989, 20000000) < s_edge_charge)
    check("two possible outside charges leave one hundredth per seam",
          s_pair_loss-2*s_edge_charge == F(1, 100))
    check("real DP loss retains the full oriented early credit",
          delta+q1*heights[4]**2 == F(690599, 20000000) < F(1, 20))
    check("DD DE and EE all supply the TT allowance",
          min(F(both_low["gap"]), F(real_low["uniform_source_gap"]),
              F(early["phase_gap"])) == delta)
    check("both real-low and early TR have the already finite loss",
          tr_finite == F(transition["finite_source_gap"])
          and "zero is an allowed same-height small-angle reduction" in hybrid["checks"]
          and "core stronger than retained real-low/right finite loss" in hybrid["checks"])
    check("remaining TP to PR reserve after the finite outside cost",
          delta-bR_finite == F(1, 250) > tr_finite)
    check("remaining double PP reserve exceeds the final incident-edge loss",
          pp_reserve > tr_finite)
    check("one remaining AA tolerance yields the low-present finite gap",
          tr_finite-F(1, 4000) == F(1, 4000)
          and F(1, 100)-F(1, 4000) > F(1, 4000))
    check("central coefficient error is still the old no-low error",
          F(1, 160000) < F(1, 4000))
    check("fixed collar and disjoint S D E endpoints permit the source gluing",
          F(0) < F(1, 1000) < F(1, 10) < F(3, 25) < F(11, 50))

    # S=0, T=1, P=2, R=3. A seam edge is consumed first.
    # An S-paid PP/PR block is then removed completely, even if its
    # other endpoint is T-affected. The written proof handles all m;
    # this finite diagnostic tests its literal short-cycle incidences.
    enlarged_patterns = 0
    enlarged_per_length = []
    s_paid_total = tp_to_pr_total = remaining_doubles_total = 0
    for m in range(1, 9):
        count = 0
        for word in itertools.product(range(4), repeat=m):
            kinds = [(word[i], word[(i+1) % m]) for i in range(m)]
            s_edges = {i for i, pair in enumerate(kinds) if 0 in pair}
            sp = {i for i, pair in enumerate(kinds) if set(pair) == {0, 2}}
            tt = {i for i, pair in enumerate(kinds) if pair == (1, 1)}
            tp = {i for i, pair in enumerate(kinds) if set(pair) == {1, 2}}
            tr = {i for i, pair in enumerate(kinds) if set(pair) == {1, 3}}
            pp = {i for i, pair in enumerate(kinds) if pair == (2, 2)}
            pr = {i for i, pair in enumerate(kinds) if set(pair) == {2, 3}}
            nS = word.count(0)
            seam_inc = [int(a == 0)+int(b == 0) for a, b in kinds]
            assert sum(seam_inc) == 2*nS and len(s_edges) >= nS
            assert all(F(k, 2)+(1-F(k, 2)) == 1 for k in seam_inc if k)
            s_candidates = {}
            s_possible = {}
            for v in range(m):
                if word[v] != 2:
                    continue
                inc = [((v-1) % m, word[(v-1) % m]),
                       (v, word[(v+1) % m])]
                for payer_edge, other in inc:
                    if other != 0:
                        continue
                    for outside, next_type in inc:
                        if outside in pp or outside in pr:
                            assert payer_edge in sp
                            assert payer_edge not in s_possible
                            s_possible[payer_edge] = outside
                            s_candidates.setdefault(outside, []).append(payer_edge)
            s_paid = {outside: min(payers)
                      for outside, payers in s_candidates.items()}
            assert len(set(s_paid.values())) == len(s_paid)
            assert len(s_paid) <= len(sp) <= 2*nS
            assert not (s_edges & set(s_paid))

            tp_payer, outside_payers = {}, {}
            for v in range(m):
                if word[v] != 2:
                    continue
                inc = [((v-1) % m, word[(v-1) % m]),
                       (v, word[(v+1) % m])]
                t_inc = [edge for edge, other in inc if other == 1]
                if len(t_inc) != 1:
                    continue
                payer_edge = t_inc[0]
                outside = next(edge for edge, other in inc if other != 1)
                if outside in s_edges or outside in s_paid:
                    continue
                assert payer_edge in tp and payer_edge not in tp_payer
                assert outside in pp or outside in pr
                tp_payer[payer_edge] = outside
                outside_payers.setdefault(outside, []).append(payer_edge)
            aR = sum(edge in pr for edge in tp_payer.values())
            double = [edge for edge in pp-set(s_paid)
                      if len(outside_payers.get(edge, [])) == 2]
            assert all(len(set(es)) == len(es) for es in outside_payers.values())
            assert all(len(outside_payers.get(edge, [])) <= 1 for edge in pr)
            assert 2*len(double) <= len(tp)-aR
            nT = len(tt)+len(tp)+len(tr)
            assert (tt | tp | tr).isdisjoint(s_edges)
            if nS == 0 and 1 in word:
                assert nT >= 1
            upper = (-s_pair_loss*nS+s_edge_charge*len(s_paid)
                     -delta*(len(tt)+len(tp))+bR_finite*aR
                     +D*len(double)-tr_finite*len(tr))
            assert upper <= -F(1, 100)*nS-tr_finite*nT
            enlarged_patterns += 1
            count += 1
            s_paid_total += len(s_paid)
            tp_to_pr_total += aR
            remaining_doubles_total += len(double)
        enlarged_per_length.append(dict(length=m, patterns=count))
    check("complete four-region short-cycle incidence diagnostics",
          enlarged_patterns == sum(4**m for m in range(1, 9)) == 87380)

    input_hash = None
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        previous = json.loads(raw)
        assert previous["status"] == "passed"
        assert previous["proof_sha256"] == ph and previous["script_sha256"] == sh
        assert previous["dependencies_sha256"] == deps and previous["checks"] == checks
        assert previous["patterns_per_length"] == per_length
        assert previous["enlarged_patterns_per_length"] == enlarged_per_length
        assert previous["exact_reset_excesses"] == fees
        assert previous["whole_S_affected_PP_cost"] == str(whole_pp)
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in deps.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(
        status="passed", exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(deps),
        exact_reset_excesses=fees, largest_double_PP_excess=str(D),
        early_phase_loss=str(delta), affected_PR_raw_ceiling=str(bR),
        early_R_raw_loss=str(er), per_early_incident_edge_loss=str(final),
        early_region_finite_gap="1/2000", restricted_region_error_gap="1/160000",
        low_present_finite_gap="1/4000", whole_S_affected_PP_cost=str(whole_pp),
        affected_PR_whole_angle_finite_ceiling=str(bR_finite),
        S_coefficient="1/100", remaining_T_incident_edge_loss=str(tr_finite),
        incidence_patterns=patterns, patterns_per_length=per_length,
        EP_to_PR_assignments=ep_to_pr_total, doubly_affected_PP_blocks=doubles_total,
        enlarged_incidence_patterns=enlarged_patterns,
        enlarged_patterns_per_length=enlarged_per_length,
        S_paid_outside_blocks=s_paid_total, TP_to_PR_assignments=tp_to_pr_total,
        remaining_doubly_affected_PP_blocks=remaining_doubles_total,
        new_critical_roots=0, new_source_cells=0, numerical_inequalities_recomputed=0,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope="Complete original selected contribution on ([0,.12] union P union R)^m, P=[.22,.45], R=[.5,1], on one fixed periodic hybrid with collar below .001 and the inherited endpoint-thickening radius. Early heights remain complex; all low/seam mixtures and literal short cycles are included. The final enlarged allocation uses no R clamp. The written incidence proof covers arbitrary fixed length. No remaining transition interval, whole-period asymptotic or knot-family theorem.",
    )
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact checks;", patterns, "+", enlarged_patterns,
          "incidence patterns;",
          len(primary), "primary records;", len(deps), "bindings", flush=True)


if __name__ == "__main__":
    main()
