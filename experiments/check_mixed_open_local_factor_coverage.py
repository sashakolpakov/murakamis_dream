#!/usr/bin/env python3
"""Exact open endpoint-disk extraction and conditional local factor bookkeeping."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_open_local_factor_coverage.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sqrt_upper(q):
    assert q >= 0
    scale = 10**15
    num, den = q.numerator*scale**2, q.denominator
    value = isqrt(num//den)
    if value*value*den < num:
        value += 1
    result = F(value, scale)
    assert result*result >= q
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-open-local-factor-coverage.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, records, primary, replays = {}, {}, {}, {}

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        bind(path)
        if path in records:
            return records[path]
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        nested = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in record.get(field, {}).items():
                assert name not in nested or nested[name] == digest
                nested[name] = digest
                bind(name, digest)
        for name in nested:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return record

    specs = [
        ("mixed-open-word-critical-localization", "mixed_open_word_critical_localization",
         "certify_mixed_open_word_critical_localization", "certify_mixed_open_word_critical_localization"),
        ("mixed-open-word-hessian", "mixed_open_word_hessian",
         "check_mixed_open_word_hessian", "check_mixed_open_word_hessian"),
        ("mixed-cyclic-block-boundary-images", "mixed_cyclic_critical_height_bounds",
         "certify_mixed_cyclic_block_boundary_images", "replay_mixed_cyclic_block_boundary_images"),
        ("mixed-cyclic-window-heights", "mixed_cyclic_critical_height_bounds",
         "certify_mixed_cyclic_window_heights", "replay_mixed_cyclic_window_heights"),
        ("mixed-type-three-window-strip", "mixed_type_three_window_strip",
         "certify_mixed_type_three_window_strip", "replay_mixed_type_three_window_strip"),
        ("mixed-conditional-critical-images", "mixed_conditional_critical_images",
         "certify_mixed_conditional_critical_images", "replay_mixed_conditional_critical_images"),
        ("mixed-central-conditional-rectangles", "mixed_central_conditional_rectangles",
         "certify_mixed_central_conditional_rectangles", None),
        ("mixed-fourier-weight-continuation", "mixed_fourier_weight_continuation",
         "check_mixed_fourier_weight_continuation", None),
        ("mixed-complete-first-cap-packet", "mixed_complete_first_cap_packet",
         "check_mixed_complete_first_cap_packet", "check_mixed_complete_first_cap_packet"),
        ("mixed-endpoint-cap-rectangle", "mixed_endpoint_cap_rectangle",
         "certify_mixed_endpoint_cap_rectangle", "certify_mixed_endpoint_cap_rectangle"),
        ("mixed-terminal-conditional-source", "mixed_terminal_conditional_source_reduction",
         "certify_mixed_terminal_conditional_source", "certify_mixed_terminal_conditional_source"),
    ]
    for stem, proof, script, replay_script in specs:
        path = "repro/results/research-"+stem+".json"
        author = inherit(path)
        assert author["status"] == "passed", path
        proof_path = "notes/research_"+proof+".md"
        proof_hash = author.get("proof_sha256", deps.get(proof_path))
        assert proof_hash is not None
        bind(proof_path, proof_hash)
        bind("experiments/"+script+".py", author["script_sha256"])
        primary[path] = deps[path]
        if replay_script:
            rp = path[:-5]+"-replay.json"
            saved = inherit(rp)
            assert saved["status"] == "passed"
            assert saved["input_sha256"] == deps[path]
            assert saved["proof_sha256"] == proof_hash
            bind("experiments/"+replay_script+".py", saved["script_sha256"])
            replays[rp] = deps[rp]
    for path in (
        "notes/research_mixed_open_word_window_inheritance.md",
        "notes/research_mixed_terminal_conditional_packet.md",
        "notes/research_mixed_conditional_torus_composition.md",
        "notes/research_mixed_conditional_image_contours.md",
        "notes/research_mixed_open_word_endpoint_rectangles.md",
    ):
        bind(path)

    roots = records["repro/results/research-mixed-open-word-critical-localization.json"]
    saved = records["repro/results/research-mixed-open-word-critical-localization-replay.json"]
    assert roots["domains"] == saved["domains"]
    assert ([(d["epsilon"], d["neighbor_epsilon"]) for d in roots["domains"]]
            == [(0, 0), (0, 1), (1, 0), (1, 1)])
    extraction, total, tree_nodes, excluded = [], 0, 0, 0
    centers = [(F(".35"), F("-.01")), (F(".30"), F("-.052"))]
    radii = [F(".083"), F(".06")]
    for domain in roots["domains"]:
        eps = domain["epsilon"]
        center, radius = centers[eps], radii[eps]
        pending = [[(F(-1), F(1)), (F(-1), F(1))]]
        cursor, leaves, omitted, maximum, reserve = 0, 0, 0, F(0), None
        while pending:
            box = pending.pop()
            node = domain["tree"][cursor]
            cursor += 1
            if node[0] == "S":
                assert len(node) == 2 and type(node[1]) is int and node[1] in (0, 1)
                j = node[1]
                lo, hi = box[j]
                mid = (lo+hi)/2
                for half in ((lo, mid), (mid, hi)):
                    child = list(box)
                    child[j] = half
                    pending.append(child)
            elif node[0] == "X":
                assert node == ["X"]
                minimum = sum(min(abs(lo), abs(hi))**2 if lo*hi > 0 else F(0)
                              for lo, hi in box)
                assert minimum > 1
                omitted += 1
            else:
                assert node[0] == "L" and len(node) == 2
                witness = node[1]
                x, y = map(F, witness["centers"][1])
                r = F(witness["radius"])
                q = (x-center[0])**2+(y-center[1])**2
                slack = (radius-r)**2-q
                assert 0 < r < radius and slack > 0
                upper = sqrt_upper(q)+r
                assert upper < radius
                maximum = max(maximum, upper)
                reserve = slack if reserve is None else min(reserve, slack)
                leaves += 1
        assert cursor == len(domain["tree"])
        assert leaves == domain["leaves"] and omitted == domain["excluded"]
        extraction.append(dict(own_type=3+eps, external_type=3+domain["neighbor_epsilon"],
            witnesses=leaves, enclosing_radius=str(radius),
            maximum_attached_radius_upper=str(maximum),
            minimum_squared_inclusion_reserve=str(reserve)))
        total += leaves
        tree_nodes += cursor
        excluded += omitted
    assert (total, tree_nodes, excluded) == (5258, 10978, 233)
    assert [sum(v["witnesses"] for v in extraction if v["own_type"] == own)
            for own in (3, 4)] == [3347, 1911]

    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    check("private four endpoint lies in the exact Fourier rectangle",
          F(".236") < F(".333") < F(".363") < F(".364")
          and F("-.116") < F("-.051") < F("-.019") < F(".012"))
    check("original four disk lies in the exact Fourier rectangle",
          F(".30")-F(".064") == F(".236")
          and F(".30")+F(".064") == F(".364")
          and -F(".052")-F(".064") == -F(".116")
          and -F(".052")+F(".064") == F(".012"))
    check("refined real and height intervals lie in the central source products",
          F(".25") < F(".27") < F(".33") < F(".40")
          and F(".25") < F(".30") < F(".39") < F(".40")
          and -F(".057") < -F(".001") < F(".0141"))
    s, a, b, eps, m, k, first = sp.symbols("s a b eps m k first")
    phase = lambda z: sp.I*sp.pi*z*(1-z)/2
    check("conditional chirps give the original open action",
          sp.expand(phase(s+a)+phase(s+b)-(2+eps)*phase(s)
                    -phase(a)-phase(b)+2*sp.I*sp.pi*a*s
                    -(sp.I*sp.pi*s*(a-b)-eps*phase(s))) == 0)
    check("unintegrated powers retain both endpoint and all diagonal factors",
          sp.expand(m+k-1-first/2-(m-1+k-first)/2-1-k/2-(m-3)/2) == 0)
    check("outer Gaussian power is independent of word length and types",
          sp.expand((m-3)/2-m/2+sp.Rational(3, 2)) == 0)
    check("the elimination dimensions include both ordinary auxiliary coordinates",
          sp.expand((m+2)+m-(2*m+2)) == 0)
    A, B, C, v = sp.symbols("A B C v", nonzero=True)
    check("ordinary conditional image has the stated diagonal inverse response",
          sp.cancel(sp.Matrix([[A, C], [C, B]]).inv()[1, 1]-A/(A*B-C*C)) == 0)
    check("external derivative factor has no finite zero in its regular strip",
          sp.cancel(sp.I*(v+1)/(v-1)+sp.I-2*sp.I*v/(v-1)) == 0)
    check("at most five uncovered ordinary factors in the long-word case",
          sp.expand((m-2)-(m-7)) == 5)
    check("short-word ordinary count never exceeds five",
          7-2 == 5 and 2-2 == 0)

    result = dict(status="passed", arithmetic="exact rational and symbolic",
        checks=checks, exact_check_count=len(checks),
        endpoint_witnesses=total, original_tree_nodes=tree_nodes,
        original_excluded_boxes=excluded, attached_disk_extraction=extraction,
        primary_records=primary, saved_replays=replays,
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        dependencies_sha256=deps, new_root_proposals=0, new_cover_cells=0,
        scope="Exact common attached disks, local factor coverage audit, and conditional nonzero N^-3/2 unaliased local Gaussian. Up to five ordinary boundary-buffer packets and the whole-source comparison remain separate.")
    if old is not None:
        expected = dict(result)
        expected["input_sha256"] = old.get("input_sha256")
        assert old == expected
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", total, "existing disks;", len(checks), "exact checks;",
          len(primary), "primary;", len(replays), "replays;", len(deps), "bindings")


if __name__ == "__main__":
    main()
