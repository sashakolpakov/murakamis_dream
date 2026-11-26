#!/usr/bin/env python3
"""Saved alias floors and exact vertical-transport budgets; no new root/cover."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_four_first_vertical_source_transport.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def lower(text):
    match = re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]", text)
    assert match, text
    midpoint, radius = map(F, match.groups())
    assert radius >= 0
    return midpoint-radius


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-vertical-source-transport.json")
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, records, primary = {}, {}, {}

    def bind(path, expected=None):
        value = sha(ROOT/path)
        assert path not in deps or deps[path] == value, path
        if expected is not None:
            assert value == expected, path
        deps[path] = value
        return value

    def inherit(path):
        bind(path)
        if path in records:
            return records[path]
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        children = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in record.get(field, {}).items():
                assert name not in children or children[name] == digest
                children[name] = digest
                bind(name, digest)
        for name in children:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return record

    sources = {}
    for stem, proof, script in (
        ("mixed-reduced-disk-conditional-packets",
         "research_mixed_reduced_disk_conditional_packets.md",
         "certify_mixed_reduced_disk_conditional_packets.py"),
        ("mixed-terminal-conditional-source",
         "research_mixed_terminal_conditional_source_reduction.md",
         "certify_mixed_terminal_conditional_source.py"),
        ("mixed-four-first-vertical-phase",
         "research_mixed_four_first_vertical_phase.md",
         "check_mixed_four_first_vertical_phase.py"),
    ):
        ap = "repro/results/research-"+stem+".json"
        rp = ap.replace(".json", "-replay.json")
        author, replay = inherit(ap), inherit(rp)
        assert author["status"] == replay["status"] == "passed"
        assert replay["input_sha256"] == deps[ap]
        for field in ("proof_sha256", "script_sha256", "dependencies_sha256"):
            assert author[field] == replay[field], (stem, field)
        bind("notes/"+proof, author["proof_sha256"])
        bind("experiments/"+script, author["script_sha256"])
        primary[ap], primary[rp] = deps[ap], deps[rp]
        sources[stem] = (author, replay)

    floors = {0: (F(9,10), F(19,50)),
              1: (F(989,1000), F(191,500))}
    extracted = []
    observations = {0: [], 1: []}
    ordinary = sources["mixed-reduced-disk-conditional-packets"]
    assert len(ordinary[0]["domains"]) == len(ordinary[1]["domains"]) == 6
    assert [d["types"] for d in ordinary[0]["domains"]] == [
        [0,0,0], [0,0,1], [0,1,1], [1,0,0], [1,0,1], [1,1,1]]
    assert ordinary[0]["accepted_cells"] == ordinary[1]["accepted_cells"] == 4409
    assert ordinary[0]["visited_nodes"] == ordinary[1]["visited_nodes"] == 8812
    for author, replay in zip(ordinary[0]["domains"], ordinary[1]["domains"]):
        assert author["types"] == replay["types"]
        assert author["tree"] == replay["tree"]
        for side, first in enumerate(author["types"][1:]):
            assert len(author["extrema"][side]) == len(replay["extrema"][side]) == 9
            values = [min(lower(d["extrema"][side][j]) for d in (author,replay))
                      for j in (6,7)]
            assert all(value > floor for value, floor in zip(values, floors[first]))
            assert all(lower(d["extrema"][side][j]) > F(1,1000)
                       for d in (author,replay) for j in range(6))
            observations[first].append(values)
            extracted.append(dict(source="ordinary", types=author["types"],
                                  orientation=side, first_type=3+first,
                                  lower_bounds=list(map(str,values))))
    terminal = sources["mixed-terminal-conditional-source"]
    assert len(terminal[0]["domains"]) == len(terminal[1]["domains"]) == 4
    assert [(d["epsilon"],d["neighbor_epsilon"]) for d in terminal[0]["domains"]] == [
        (0,0),(0,1),(1,0),(1,1)]
    assert sum(d["counts"]["boundary"] for d in terminal[0]["domains"]) == 632
    for author, replay in zip(terminal[0]["domains"], terminal[1]["domains"]):
        for key in ("epsilon","neighbor_epsilon","counts","original_leaf_node_indices"):
            assert author[key] == replay[key], key
        assert len(author["extrema"]) == len(replay["extrema"]) == 9
        first = author["neighbor_epsilon"]
        values = [min(lower(d["extrema"][j]) for d in (author,replay)) for j in (6,7)]
        assert all(value > floor for value, floor in zip(values, floors[first]))
        assert all(lower(d["extrema"][j]) > F(1,1000)
                   for d in (author,replay) for j in range(6))
        observations[first].append(values)
        extracted.append(dict(source="terminal", epsilon=author["epsilon"],
                              first_type=3+first, lower_bounds=list(map(str,values))))
    assert len(extracted) == 16 and all(len(values) == 8 for values in observations.values())

    checks = []
    def check(name, condition):
        assert condition, name
        checks.append(name)
    pi_upper = F(22,7)
    h, xmin, xmax, cut = F(7,500), F(6,25), F(363,1000), F(3,20)
    check("all v at or beyond the cut have negative unselected derivative",
          F(1,4)-xmin/2-cut < 0)
    check("selected factorial derivative coefficient is at most 11/100",
          F(1,2)-xmin-cut == F(11,100))
    factorial_growth = h*pi_upper*F(11,100)
    forced_growth = h*pi_upper*(1-cut)
    credit = F(137,3500)
    check("factorial growth is less than 1/200", factorial_growth == F(121,25000)
          and factorial_growth < F(1,200))
    check("cosine quadratic gives sin(.363pi)>9/10",
          1-((F(1,2)-xmax)*pi_upper)**2/2 > F(9,10))
    check("the logarithmic atanh credit is 137/3500",
          (F(1,2)-xmax)*F(4,7)/2 == credit)
    check("the forced branch credit pays all positive-height growth",
          forced_growth == F(187,5000) and credit > forced_growth)
    check("the old real-tail gap leaves excess below 1/250",
          factorial_growth-F(1,1000) < F(1,250))
    length = h+F(51,500)
    check("the whole height interval is at most 29/250", length == F(29,250))
    check("the upper horizontal alias retains 1/60",
          floors[1][1]-pi_upper*length > F(1,60))
    check("the lower horizontal alias retains 1/4",
          floors[1][0]-2*pi_upper*length > F(1,4))
    check("source excess 1/100 leaves first-pair reserve 1/25",
          F(1,20)-F(1,100) == F(1,25))

    result = dict(status="passed", exact_checks=len(checks), checks=checks,
                  extracted_source_orientations=len(extracted), extracted=extracted,
                  alias_floors={str(3+k):list(map(str,v)) for k,v in floors.items()},
                  real_tail_allowance="1/250", primary_records_sha256=primary,
                  dependencies_sha256=deps, proof_sha256=ph, script_sha256=sh,
                  input_sha256=ih, new_root_proposals=0, root_enclosures_recomputed=0,
                  new_parameter_cover_cells=0, complete_finite_source_upper_proved=False,
                  scope="Existing source alias floors and elementary type-four vertical real-tail budgets only; central zero-mode source control remains separate.")
    if old:
        assert old == dict(result, input_sha256=old["input_sha256"])
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path,digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("PASS",len(checks),"exact checks;",len(extracted),"saved source orientations;",
          len(primary),"primary records;",len(deps),"bindings; no root or cover rerun")


if __name__ == "__main__":
    main()
