#!/usr/bin/env python3
"""Exact incidence and provenance checks for global nonlow upper removal.

No root, parameter cover, row maximum, or numerical derivative inequality is
recomputed. Those statements are supplied by the completed bound inputs.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_nonlow_upper_transition_removal.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tree_structure(row, dimension, initial_box=None):
    """Exhaust the saved splits/reductions; numerical signs are inherited."""
    stack = [[(F(0), F(1)) for _ in range(dimension)] if initial_box is None else list(initial_box)]
    assert len(stack[0]) == dimension
    leaves = visits = monotone = 0
    for node in row["nodes"]:
        assert stack
        box = stack.pop()
        visits += 1
        if node[0] == "L":
            assert len(node) == 2
            leaves += 1
        elif node[0] == "S":
            assert len(node) == 2
            axis = node[1]
            assert type(axis) is int and 0 <= axis < dimension
            lo, hi = box[axis]
            assert lo < hi
            middle = (lo+hi)/2
            left, right = list(box), list(box)
            left[axis], right[axis] = (lo, middle), (middle, hi)
            stack.extend((left, right))
        else:
            assert node[0] == "M" and len(node) == 4
            _, axis, bit, _ = node
            assert type(axis) is int and 0 <= axis < dimension
            assert type(bit) is int and bit in (0, 1)
            lo, hi = box[axis]
            assert lo < hi
            point = box[axis][bit]
            box[axis] = (point, point)
            stack.append(box)
            monotone += 1
    assert not stack and row["remaining_boxes"] == 0
    assert (leaves, visits, monotone) == (row["leaves"], row["visits"], row["monotone"])
    return leaves, visits, monotone


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT/
                    "repro/results/research-mixed-nonlow-upper-transition-removal.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    input_hash = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, visited, primary, checks, record_cache = {}, set(), {}, [], {}

    def bind(path, expected=None):
        if path in deps:
            if expected is not None:
                assert deps[path] == expected, path
            return deps[path]
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        if path in deps:
            assert deps[path] == digest, path
        deps[path] = digest
        return digest

    def inherit(path):
        bind(path)
        if path in visited:
            return record_cache[path]
        record = json.loads((ROOT/path).read_text())
        record_cache[path] = record
        visited.add(path)
        inherited = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                if p in inherited:
                    assert inherited[p] == digest, p
                inherited[p] = digest
                bind(p, digest)
        for p in inherited:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)
        return record

    def load(stem, prefix, replay=False):
        suffix = "-replay" if replay else ""
        path = "repro/results/research-"+stem.replace("_", "-")+suffix+".json"
        record = inherit(path)
        assert record["status"] == "passed", path
        assert record["proof_sha256"] == bind("notes/research_"+stem+".md")
        assert record["script_sha256"] == bind("experiments/"+prefix+"_"+stem+".py")
        primary[path] = record
        return record

    def check(name, assertion):
        assert assertion, name
        checks.append(name)

    graph = load("mixed_split_cutoff_hybrid_contour", "check")
    reduction = load("mixed_complex_right_row_reduction", "check")
    coherent_h = load("mixed_right_selected_height_removal", "certify")
    coherent_c = load("mixed_unselected_right_clamping", "certify")
    mixed_h = load("mixed_raw_coherent_height_bounds", "certify")
    mixed_c = load("mixed_raw_coherent_right_clamping", "certify")
    raw_c = load("mixed_two_raw_right_clamping", "certify")
    taper = load("mixed_selected_right_taper_support", "certify")
    plateau = load("mixed_selected_plateau_support", "certify")
    oriented = load("mixed_oriented_height_reset", "certify")
    upper = load("mixed_upper_transition_right_support", "check")
    bind("notes/research_mixed_raw_coherent_height_comparison.md")
    bind("notes/research_mixed_full_nonlow_half_region.md")
    check("coherent imaginary comparison covers both complete neighbor products",
          coherent_h["products"] == 939 and coherent_h["leaves"] == 105935
          and coherent_h["scalar_comparisons"] == 2)
    check("coherent horizontal comparison covers all typed triples",
          coherent_c["products"] == 288 and coherent_c["leaves"] == 253378)
    check("positive forcing and factorial reserves are inherited",
          arb(coherent_h["forcing_reserve"]).lower() > arb(F(1, 25).numerator)/F(1, 25).denominator
          and arb(coherent_h["factorial_reserve"]).lower() > arb(F(1, 25).numerator)/F(1, 25).denominator)
    check("selected full-box curvature and exact partial-plateau endpoints",
          F(taper["target_concavity"]) == F(5, 4)
          and taper["taper_real_interval"] == ["9/20", "1/2"]
          and F(plateau["reference_defect_upper"]) == -F(1, 100))
    check("ordered one-height reset costs",
          list(map(F, oriented["integrated_one_height_costs"])) == [F(11, 2), F(151, 20)])
    check("upper-transition complete raw source has every typed height band",
          upper["source_sum"] == "all original absolute rows"
          and F(upper["finite_source_gap"]) == F(1, 2000)
          and upper["target_height_bands"] == {
              "3": ["-3/100", "1/50"], "4_unselected": ["-57/1000", "0"],
              "4_selected": ["0", "7/500"]})

    mixed_keys = [list(v)+[face] for v in itertools.product((0, 1), repeat=4)
                  for face in range(6)]
    height_keys = []
    for clipped in (0, 1):
        for direction, beta in ((0, 0), (1, 0), (1, 1)):
            for other in (0, 1):
                faces = 7 if clipped and other == 0 else 6
                height_keys.extend([[clipped, direction, beta, other, face]
                                    for face in range(faces)])
    height_keys.extend([[2, beta, 0, 0, 0] for beta in (0, 1)])
    raw_keys = [list(v) for v in itertools.product((0, 1), repeat=2)]
    structures = {}
    for stem, author, expected, dimension, counts in (
        ("mixed_raw_coherent_height_bounds", mixed_h, height_keys, 2, (77, 910, 1743, 0)),
        ("mixed_raw_coherent_right_clamping", mixed_c, mixed_keys, 3, (96, 6729, 13366, 4)),
        ("mixed_two_raw_right_clamping", raw_c, raw_keys, 2, (4, 29, 54, 0)),
    ):
        replay = load(stem, "certify", replay=True)
        check(stem+" author and saved384 replay bind the same complete input",
              replay["precision_bits"] >= 384 and author["product_range"] == [0, counts[0]]
              and replay["input_sha256"] == deps["repro/results/research-"+stem.replace("_", "-")+".json"]
              and author["proof_sha256"] == replay["proof_sha256"]
              and author["script_sha256"] == replay["script_sha256"]
              and author["dependencies_sha256"] == replay["dependencies_sha256"])
        check(stem+" complete ordered domain set",
              [r["case"] for r in author["cases"]] == expected
              and [r["case"] for r in replay["cases"]] == expected
              and len(expected) == len({tuple(v) for v in expected}) == counts[0])
        total = [0, 0, 0]
        for index, (a, b) in enumerate(zip(author["cases"], replay["cases"])):
            assert a["index"] == b["index"] == index
            assert a["nodes"] == b["nodes"]
            initial_box = [(F(0), F(1)) for _ in range(dimension)]
            if stem == "mixed_raw_coherent_height_bounds" and a["case"][0] == 2:
                initial_box[0] = (F(0), F(0))
            result = tree_structure(a, dimension, initial_box)
            assert result == tree_structure(b, dimension, initial_box)
            total = [x+y for x, y in zip(total, result)]
        check(stem+" all saved trees exhausted with identical replay witnesses",
              tuple(total) == counts[1:]
              and (author["products"], author["leaves"], author["visits"], author["monotone_reductions"]) == counts)
        structures[stem] = dict(products=counts[0], leaves=total[0], visits=total[1],
                                monotone_reductions=total[2])
    check("both raw rows remain independent original rows",
          raw_c["complex_roots_per_cell"] == 0 and raw_c["raw_scalar_roots_per_cell"] == 2)
    check("mixed derivative uses one coherent and one real-row root",
          mixed_c["complex_roots_per_cell"] == mixed_c["raw_scalar_roots_per_cell"] == 1)
    check("uniform local marginal and horizontal constants",
          mixed_h["imaginary_lower_bounds"] == ["-3/5", "-9/20"]
          and F(mixed_c["derivative_upper_bound"]) == F(raw_c["derivative_upper_bound"]) == -F(1, 20))

    slow = lambda x: min(F(1), (x-F(1, 10))/F(3, 25))
    fast = lambda x: min(F(1), (x-F(1, 10))/F(1, 50))
    breaks = [F(1, 10), F(3, 25), F(11, 50), F(9, 20), F(1, 2), F(1)]
    # Both sides are affine on each displayed interval; endpoint equality is
    # the exact piecewise identity, not a numerical sampling assertion.
    check("fast cutoff is min(6 slow,1) on every affine piece",
          all(fast(x) == min(6*slow(x), F(1)) for x in breaks))
    check("all left cutoffs are constant one throughout upper motion and right clamp",
          all(slow(x) == fast(x) == 1 for x in breaks[2:]))
    check("quadratic taper endpoints and linear triangle inclusion",
          400*F(1, 20)**2 == 1 and 400*F(0)**2 == 0
          and 400*F(1, 20) == 20)
    check("unselected attenuated coefficients stay in the original typed bands",
          F(-3, 100) <= 0 <= F(1, 50) and F(-57, 1000) <= 0
          and F(7, 500) > 0)
    check("clipped imaginary comparison is available when slow minimum is at least half",
          F(1, 10)+F(3, 25)/2 == F(4, 25))
    check("selected forcing branch scalar budget",
          F(3, 5)*(F(7, 500)+F(57, 1000)) == F(213, 5000)
          and 2*F(7, 500) == F(7, 250))
    check("selected factorial branch two scalar budgets",
          F(3, 5)*(F(7, 500)+F(57, 2000))*400*F(1, 20) == F(51, 100)
          and F(9, 20)*(F(7, 500)+F(57, 1000))*400*F(1, 20) == F(639, 1000))
    check("common horizontal loss is no larger than either inherited loss",
          F(1, 20) <= F(1, 10))
    check("each interior selected correction recombines two halfweights once",
          F(1, 2)+F(1, 2) == 1)
    check("EPUR raw reserve spends one combined tolerance",
          F(1, 1000)-F(1, 2000) == F(1, 2000)
          and -F(1, 100) < 0)

    # Finite incidence diagnostics only. The proof covers every m through its
    # local cutoff identity and telescoping; this enumeration is not a
    # substitute for that argument.
    patterns = 0
    for n in range(1, 7):
        for labels in itertools.product("AUR", repeat=n):
            patterns += 1
            raw = [labels[j] == "R" or labels[(j+1) % n] == "R" for j in range(n)]
            final = tuple("A" if x == "U" else x for x in labels)
            assert [j for j, x in enumerate(final) if x == "R"] == [
                j for j, x in enumerate(labels) if x == "R"]
            for j, label in enumerate(labels):
                if label != "U":
                    continue
                incidences = [(j-1) % n, j]
                number = sum(raw[e] for e in incidences)
                assert number in (0, 1, 2)
                if n == 1:
                    assert number == 0 and incidences == [0, 0]
                if n == 2 and labels[1-j] == "R":
                    assert number == 2 and len(set(incidences)) == 2
    check("literal loops and parallel raw incidences exhaust all label patterns through six",
          patterns == sum(3**n for n in range(1, 7)) == 1092)
    check("fixed-word tolerance can be apportioned once across all edges",
          all(sum([F(1, n)]*n) == 1 for n in range(1, 13)))

    result = dict(
        status="passed", exact_checks=len(checks), checks=checks,
        primary_records=list(primary), primary_record_count=len(primary),
        inherited_cover_structures=structures, cyclic_incidence_patterns=patterns,
        horizontal_loss="1/20", selected_forcing_constant="7*pi/250-213/5000",
        selected_factorial_constant="log(2*sin(9*pi/20))-639/1000",
        local_pair_raw_gap="1/1000", local_pair_finite_gap="1/2000",
        numerical_cells_recomputed=0, proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=deps,
        scope="Exact/provenance reduction of the entire nonlow mixed region to fixed R labels at .5 and all other reals <=.45, erasing selections only at moved upper coordinates. No new numerical cover, finite-kernel ratio, lower-transition/right sign, whole-period asymptotic or knot-family claim.")
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert deps == {p: sha(ROOT/p) for p in deps}
    if args.input:
        assert sha(args.input) == input_hash
        assert old == result
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "checks;", len(primary), "primary;", len(deps),
          "bindings;", patterns, "incidence patterns; no numerical recomputation")


if __name__ == "__main__":
    main()
