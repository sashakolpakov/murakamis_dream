#!/usr/bin/env python3
"""Exact first-cap assembly and current saved-source provenance; no new cover."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_complete_first_cap_packet.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def endpoints(value):
    """Read the outward decimal interval retained by a passed source record."""
    match = re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]", value)
    assert match, value
    mid, rad = map(F, match.groups())
    assert rad >= 0
    return mid-rad, mid+rad


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-complete-first-cap-packet.json")
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

    def source(stem, proof, script, replay=True):
        path = "repro/results/research-"+stem+".json"
        author = inherit(path)
        assert author["status"] == "passed", path
        bind("notes/"+proof+".md", author["proof_sha256"])
        bind("experiments/"+script+".py", author["script_sha256"])
        primary[path] = deps[path]
        if not replay:
            return author
        rp = "repro/results/research-"+stem+"-replay.json"
        saved = inherit(rp)
        assert saved["status"] == "passed", rp
        assert saved["input_sha256"] == deps[path], rp
        assert saved["proof_sha256"] == author["proof_sha256"]
        assert saved["script_sha256"] == author["script_sha256"]
        assert saved["dependencies_sha256"] == author["dependencies_sha256"]
        assert saved["precision_bits"] > author["precision_bits"] >= 192
        replays[rp] = deps[rp]
        return author, saved

    roots, roots_replay = source("mixed-open-word-critical-localization",
        "research_mixed_open_word_critical_localization",
        "certify_mixed_open_word_critical_localization")
    image = source("mixed-open-word-endpoint-rectangles",
        "research_mixed_open_word_endpoint_rectangles",
        "check_mixed_open_word_endpoint_rectangles", replay=False)
    packet, packet_replay = source("mixed-endpoint-cap-rectangle",
        "research_mixed_endpoint_cap_rectangle",
        "certify_mixed_endpoint_cap_rectangle")
    cuts, cuts_replay = source("mixed-cap-real-cut-gaps",
        "research_mixed_cap_real_cut_gaps", "check_mixed_cap_real_cut_gaps")
    tails, tails_replay = source("mixed-outer-cap-real-tails",
        "research_mixed_outer_cap_real_tails", "check_mixed_outer_cap_real_tails")
    aliases, aliases_replay = source("mixed-cap-outer-alias-curvature",
        "research_mixed_cap_outer_contour_reduction",
        "certify_mixed_cap_outer_alias_curvature")
    for path in (
        "notes/research_mixed_conditional_torus_composition.md",
        "notes/research_complete_boundary_full_index_interval.md",
        "notes/research_mixed_three_first_cap_fourier_reduction.md",
    ):
        bind(path)

    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    check("all four original endpoint maps and both one-vertex roots",
        [(d["epsilon"], d["neighbor_epsilon"]) for d in roots["domains"]]
        == [(0, 0), (0, 1), (1, 0), (1, 1)]
        and [v["epsilon"] for v in roots["one_vertex"]] == [0, 1]
        and roots["domains"] == roots_replay["domains"]
        and [(v["epsilon"], v["witness"]) for v in roots["one_vertex"]]
        == [(v["epsilon"], v["witness"]) for v in roots_replay["one_vertex"]]
        and (roots["leaves"], roots["excluded"], roots["visits"])
        == (5258, 233, 10978))
    check("exact image extraction retains every validated root disk",
        (image["endpoint_maps"], image["endpoint_witnesses"],
         image["one_vertex_witnesses"], image["tree_nodes"])
        == (4, 5258, 2, 10978))
    cap = list(map(F, [".27", ".49", "-.055", ".04"]))
    wanted = [
        [[".376", ".438", "-.019", ".037"],
         [".278", ".391", "-.072", ".021"],
         [".218", ".242", ".049", ".077"]],
        [[".333", ".363", "-.051", "-.019"],
         [".246", ".350", "-.108", "-.020"],
         [".217", ".234", ".027", ".045"]],
    ]
    check("literal certified private, attached and auxiliary rectangles",
          image["rectangles"] == wanted)
    for eps, row in enumerate(wanted):
        e, t, u = [list(map(F, rect)) for rect in row]
        check("type %d private image strictly inside the source rectangle" % (3+eps),
            cap[0] < e[0] < e[1] < cap[1]
            and cap[2] < e[2] < e[3] < cap[3])
        check("type %d all sine arguments and jet factor avoid zeros" % (3+eps),
            0 < cap[0] < cap[1] < F(1, 2)
            and 0 < t[0] < t[1] < F(1, 2)
            and F(1, 2) < cap[0]+t[0] < cap[1]+t[1] < 1
            and 0 < u[0] < u[1] < F(1, 2) and u[2] > 0)
    check("whole endpoint source rectangle and same saved trees",
        packet["parameter_domains"] == packet_replay["parameter_domains"] == 2
        and packet["accepted_cells"] == packet_replay["accepted_cells"] == 151
        and packet["visited_cells"] == packet_replay["visited_cells"] == 300
        and [c["nodes"] for c in packet["cases"]]
        == [c["nodes"] for c in packet_replay["cases"]]
        and [c["initial_box"] for c in packet["cases"]]
        == [[["27/100", "49/100"], ["-11/200", "0"]],
            [["27/100", "49/100"], ["0", "1/25"]]])
    check("endpoint source retains three positive complete-current gaps",
        packet["gap_floors"] == ["1/5", "1/50", "1/3"]
        and all(endpoints(value)[0] > F(floor)
                for record in (packet, packet_replay)
                for case in record["cases"]
                for value, floor in zip(case["minimum_gaps"], record["gap_floors"])))
    check("all correlated real-cut witnesses and both scalar floors",
        all(record["witness_counts"] == [3348, 1912]
            and record["endpoint_maps"] == 4
            and record["one_vertex_count"] == 2
            and record["selected_rate_floor"] == "1"
            and record["real_cut_gap_floor"] == "1/2000"
            and all(endpoints(row[0])[0] > 1
                    and all(endpoints(x)[0] > F(1, 2000) for x in row[1:])
                    for row in record["minimum_rate_left_right"])
            for record in (cuts, cuts_replay)))
    check("all real rows use the final 27-check two-tail theorem",
        tails["exact_and_scalar_checks"] == tails_replay["exact_and_scalar_checks"] == 27
        and tails["checks"] == tails_replay["checks"]
        and all(endpoints(record["scalars"]["upper_endpoint_rate_ceiling"])[1]
                < F(3, 4) for record in (tails, tails_replay)))
    expected_aliases = [[eps, a, z] for eps in (0, 1)
                        for a in range(4) for z in range(4)]
    check("all 32 alias boundary products have unchanged complete saved trees",
        [c["case"] for c in aliases["cases"]] == expected_aliases
        and [(c["case"], c["nodes"]) for c in aliases["cases"]]
        == [(c["case"], c["nodes"]) for c in aliases_replay["cases"]]
        and all((record["domains"], record["leaves"], record["visits"])
                == (32, 8341, 16650) for record in (aliases, aliases_replay)))
    check("strict whole-rectangle curvature and both horizontal alias gaps",
        all(record["curvature_ceiling"] == "24"
            and endpoints(record["K_upper"])[1] < 24
            and endpoints(record["upper_alias_gap"])[0] > F(3, 20)
            and endpoints(record["lower_alias_gap"])[0] > F(6, 25)
            for record in (aliases, aliases_replay)))

    e, z, eps, n = sp.symbols("e z eps n")
    chirp = lambda v: sp.I*sp.pi*v*(1-v)/2
    check("g and J rate bridge retains the constant chirp at a real cut",
        sp.expand(chirp(e+z)-chirp(z)+sp.I*sp.pi*e*z-chirp(e)) == 0)
    check("exact D inverse cancels the marked numerator order-one factor",
        sp.expand(-sp.I*sp.pi*(n*(e-e**2)-e)/2
                  +sp.I*sp.pi*n*(e-e**2)/2-sp.I*sp.pi*e/2) == 0)
    check("own reciprocal factorial keeps its phase and order-one multiplier",
        sp.expand(-eps*(sp.I*sp.pi*n*e*(1-e)/2-sp.I*sp.pi*e/2)
                  +eps*n*chirp(e)-eps*sp.I*sp.pi*e/2) == 0)
    check("outer Gaussian and original positive N give the stated cap power",
        sp.expand(-(3+eps)/2+1-sp.Rational(1, 2)-(-1-eps/2)) == 0)
    check("both literal cap powers", [-1-F(eps, 2) for eps in (0, 1)]
          == [F(-1), F(-3, 2)])
    check("signed ordinary derivative removes the negative endpoint phase sign",
          sp.expand((-sp.Symbol("v"))*(-1)-sp.Symbol("v")) == 0)
    check("both real-tail floors leave more than the required cut reserve",
          min(F(1)-F(1, 4), F(1)-F(3, 4)) > F(1, 2000))
    check("one source tolerance gives the displayed finite tail gap",
          F(1, 2000)-F(1, 4000) == F(1, 4000))
    check("strict margin permits a positive ordinary-color neighborhood budget",
          F(1, 2000)-F(1, 8000)-F(1, 16000) > F(1, 4000))

    result = dict(status="passed", arithmetic="exact symbolic and rational",
        exact_and_provenance_checks=len(checks), checks=checks,
        primary_record_count=len(primary), saved_replay_count=len(replays),
        primary_records=primary, saved_replays=replays,
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        dependencies_sha256=deps,
        inherited_endpoint_witnesses=5260, inherited_alias_products=32,
        new_root_proposals=0, new_interval_cells=0,
        scope="Both complete original first caps and signed ordinary jets near the all-word geometric outgoing images; all private rows and parities. No whole outgoing period or full open-word asymptotic.")
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
    print("PASS", len(checks), "checks;", len(primary), "primary records;",
          len(replays), "saved replays;", len(deps), "current bindings")


if __name__ == "__main__":
    main()
