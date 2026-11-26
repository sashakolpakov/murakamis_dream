#!/usr/bin/env python3
"""Full smaller-disk terminal gaps on three original endpoint families.

Revalidate 457 old circle cells and four full raw-majorant branches per
cell. No diagnostic output, complex-root proposal, or subdivision is used.
Saved replay retains the exact original addresses and scalar row brackets.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
import check_mixed_terminal_raw_half_gap as raw

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_terminal_remaining_disk_gaps.md"
core, base, end = raw.core, raw.base, raw.end
ar, cp = raw.ar, raw.cp
FLOOR = F(1, 500)
CASES = ((0, 1), (1, 0), (1, 1))
COUNTS = (184, 135, 138)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def meets_circle(box, neighbor):
    radius = F(83, 90) if neighbor == 0 else F(15, 16)
    minimum = sum(min(lo*lo, hi*hi) if lo*hi > 0 else F(0)
                  for lo, hi in box)
    maximum = sum(max(lo*lo, hi*hi) for lo, hi in box)
    return minimum <= radius*radius <= maximum


def test(box, eps, neighbor, witness, row_witness=None):
    a = base.parameter(box, neighbor)
    a0 = base.parameter([((lo+hi)/2,)*2 for lo, hi in box], neighbor)
    assert base.test(witness, a, eps) is not None
    point = dict(witness, radius="1/10000000000")
    assert base.test(point, a0, eps) is not None
    centers = list(map(cp, witness["centers"]))
    radius, point_radius = ar(witness["radius"]), ar(point["radius"])
    t = centers[1] + acb(arb(0, radius), arb(0, radius))
    ep, tp, up = [z + acb(arb(0, point_radius), arb(0, point_radius))
                  for z in centers]
    v, vm, bracket = raw.raw_row(a, a0, eps, row_witness)
    value = core.action(a0, ep, tp, up, eps).real - HHALF
    values = [value-raw.row(vm, a0, eps),
              value+2*PI*a0.imag, value-B2/2,
              value-B2/2+PI*a0.imag]
    derivative = core.gp(t+a) + 2*PI*II*t - core.gp(a)
    derivatives = [core.gp(t+a)+2*PI*II*t-core.gp(a+v)-2*PI*II*v,
                   derivative-2*PI*II, derivative, derivative-PI*II]
    radii = [ar(base.DISKS[neighbor][2]*(hi-lo)/2) for lo, hi in box]
    lowers = []
    for index, (value, slope) in enumerate(zip(values, derivatives)):
        lower = value-abs(slope.real)*radii[0]-abs(slope.imag)*radii[1]
        assert lower > ar(FLOOR), ("terminal disk gap", eps, neighbor,
                                   box, index, lower)
        lowers.append(lower.lower())
    return bracket, lowers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-terminal-remaining-disk-gaps.json")
    parser.add_argument("--seconds", type=float, default=120)
    args = parser.parse_args()
    assert args.precision >= 192 and 0 < args.seconds <= 300
    ctx.prec = args.precision
    global PI, II, HHALF, B2
    PI, II = arb.pi(), acb(0, 1)
    half = acb(ar("1/2"))
    raw.PI, raw.II, raw.HALF = PI, II, half
    core.PI, core.II, core.HALF = PI, II, half
    end.PI, end.II = PI, II
    uh = acb(ar("1/4"), arb(3).log()/(4*PI))
    HHALF = (end.J(half)+end.phase(half, uh)).real
    B2 = -4*end.J(acb(ar("1/4"))).real
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    input_hash = sha(args.input) if args.input else None
    saved = json.loads(args.input.read_text()) if args.input else None
    dependencies, primary, records = {}, {}, {}

    def bind(path, expected=None):
        if path not in dependencies:
            dependencies[path] = sha(ROOT/path)
        if expected is not None:
            assert dependencies[path] == expected, path
        return dependencies[path]

    def inherit(path):
        bind(path)
        if path in records:
            return records[path]
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        nested = {}
        for field in ("dependencies_sha256", "dependencies"):
            for name, digest in record.get(field, {}).items():
                assert name not in nested or nested[name] == digest, name
                nested[name] = digest
                bind(name, digest)
        for name in nested:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return record

    def pair(stem, proof, script):
        author_path = "repro/results/research-"+stem+".json"
        replay_path = author_path.replace(".json", "-replay.json")
        author, replay = inherit(author_path), inherit(replay_path)
        assert author["status"] == replay["status"] == "passed"
        assert replay["input_sha256"] == dependencies[author_path]
        for record in (author, replay):
            bind("notes/"+proof+".md", record["proof_sha256"])
            bind("experiments/"+script+".py", record["script_sha256"])
        for field in ("proof_sha256", "script_sha256", "dependencies_sha256"):
            assert author[field] == replay[field], (stem, field)
        primary[author_path] = dependencies[author_path]
        primary[replay_path] = dependencies[replay_path]
        return author, replay

    roots, roots_replay = pair(
        "mixed-open-word-critical-localization",
        "research_mixed_open_word_critical_localization",
        "certify_mixed_open_word_critical_localization")
    assert roots["domains"] == roots_replay["domains"]
    pair("mixed-terminal-raw-half-gap", "research_mixed_terminal_raw_half_gap",
         "check_mixed_terminal_raw_half_gap")
    coverage, coverage_replay = pair(
        "mixed-open-local-factor-coverage", "research_mixed_open_local_factor_coverage",
        "check_mixed_open_local_factor_coverage")
    assert coverage["attached_disk_extraction"] == coverage_replay["attached_disk_extraction"]
    assert (coverage["endpoint_witnesses"], coverage["original_tree_nodes"],
            coverage["original_excluded_boxes"]) == (5258, 10978, 233)
    assert [(r["own_type"], r["external_type"]) for r in
            coverage["attached_disk_extraction"]] == [(3, 3), (3, 4), (4, 3), (4, 4)]
    for row in coverage["attached_disk_extraction"]:
        target = F(83, 1000) if row["own_type"] == 3 else F(3, 50)
        assert F(row["enclosing_radius"]) == target
        assert F(row["maximum_attached_radius_upper"]) < target
        assert F(row["minimum_squared_inclusion_reserve"]) > 0
    coupled, coupled_replay = pair(
        "mixed-terminal-coupled-disk-gap", "research_mixed_terminal_coupled_disk_gap",
        "check_mixed_terminal_coupled_disk_gap")
    for record in (coupled, coupled_replay):
        assert record["circle_cells"] == 165 and record["raw_majorant_branches"] == 4
        assert F(record["multiplier"]) == F(1, 200) and F(record["floor"]) == F(1, 4000)
        assert arb(record["minimum_lower_bound"]) > ar(F(1, 4000))
    assert [(r["node"], r["box"], r["row_bracket"]) for r in coupled["witnesses"]] == [
        (r["node"], r["box"], r["row_bracket"]) for r in coupled_replay["witnesses"]]
    for path in ("notes/research_mixed_terminal_half_row_envelope.md",
                 "notes/research_mixed_endpoint_polynomial_collar.md",
                 "notes/research_mixed_terminal_right_endpoint_reduction.md"):
        bind(path)
    for module in (raw, core, base, end):
        bind(str(Path(module.__file__).resolve().relative_to(ROOT)))

    if saved:
        assert saved["status"] == "passed"
        assert saved["proof_sha256"] == proof_hash and saved["script_sha256"] == script_hash
        assert saved["dependencies_sha256"] == dependencies
        assert saved["primary_records_sha256"] == primary
        assert saved["gap_floor"] == str(FLOOR)
        assert [(r["epsilon"], r["neighbor_epsilon"]) for r in saved["domains"]] == list(CASES)

    assert [(r["epsilon"], r["neighbor_epsilon"]) for r in roots["domains"]] == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    start = time.monotonic()
    domains = []
    nodes = leaves = excluded = 0
    for domain in roots["domains"]:
        eps, neighbor = domain["epsilon"], domain["neighbor_epsilon"]
        selected = (eps, neighbor) in CASES
        case_index = CASES.index((eps, neighbor)) if selected else None
        old_domain = saved["domains"][case_index] if saved and selected else None
        pending = [([(F(-1), F(1)), (F(-1), F(1))], 0)]
        witnesses = []
        minima = [None]*4
        local_nodes = local_leaves = local_excluded = 0
        for number, node in enumerate(domain["tree"]):
            assert time.monotonic()-start < args.seconds, "runtime bound"
            assert pending
            box, depth = pending.pop()
            nodes += 1
            local_nodes += 1
            if node[0] == "S":
                assert len(node) == 2 and node[1] == depth % 2
                left, right = base.split(box, node[1])
                pending.extend([(left, depth+1), (right, depth+1)])
                continue
            if node[0] == "X":
                assert len(node) == 1 and base.excluded(box)
                assert not meets_circle(box, neighbor)
                excluded += 1
                local_excluded += 1
                continue
            assert node[0] == "L" and len(node) == 2 and not base.excluded(box)
            leaves += 1
            local_leaves += 1
            if not selected or not meets_circle(box, neighbor):
                continue
            bracket = None
            strings = [[str(q) for q in side] for side in box]
            if old_domain:
                previous = old_domain["witnesses"][len(witnesses)]
                assert previous["node"] == number and previous["box"] == strings
                bracket = previous["row_bracket"]
            bracket, lowers = test(box, eps, neighbor, node[1], bracket)
            if old_domain:
                assert previous["row_bracket"] == bracket
            witnesses.append(dict(node=number, box=strings, row_bracket=bracket))
            for index, lower in enumerate(lowers):
                minima[index] = lower if minima[index] is None else min(minima[index], lower)
        assert not pending
        if not selected:
            continue
        assert len(witnesses) == COUNTS[case_index]
        if old_domain:
            assert witnesses == old_domain["witnesses"]
            assert (local_nodes, local_leaves, local_excluded) == (
                old_domain["original_nodes"], old_domain["original_leaves"],
                old_domain["original_exclusions"])
        domains.append(dict(epsilon=eps, neighbor_epsilon=neighbor,
                            original_nodes=local_nodes, original_leaves=local_leaves,
                            original_exclusions=local_excluded,
                            circle_cells=len(witnesses), witnesses=witnesses,
                            branch_minimum_lowers=[str(v) for v in minima]))
        print("PASS terminal disk family", eps, neighbor, len(witnesses),
              "cells; minimum", min(minima), flush=True)

    assert (nodes, leaves, excluded) == (10978, 5258, 233)
    assert [d["circle_cells"] for d in domains] == list(COUNTS)
    assert F(3, 2000)-F(1, 2000) == F(1, 1000)
    assert F(1, 5000) < F(1, 1000)
    assert sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/path) == digest for path, digest in dependencies.items())
    if args.input:
        assert sha(args.input) == input_hash
    result = dict(status="passed", precision_bits=args.precision, domains=domains,
                  gap_floor=str(FLOOR), finite_gap="1/1000", combined_finite_gap="1/5000",
                  raw_majorant_branches=4, circle_cells=sum(COUNTS),
                  branch_inequalities=4*sum(COUNTS), original_nodes=nodes,
                  original_leaves=leaves, original_exclusions=excluded,
                  new_complex_root_proposals=0, new_parameter_subdivisions=0,
                  proof_sha256=proof_hash, script_sha256=script_hash,
                  primary_records_sha256=primary, dependencies_sha256=dependencies,
                  input_sha256=input_hash, elapsed_seconds=time.monotonic()-start,
                  scope="Full smaller-disk raw gaps for own/external (0,1),(1,0),(1,1); finite terminal right sector near actual references at length>=2. With the separately replayed coupled3/3 theorem, all actual terminal references at length>=3. Length2 ending3/3 and global open-source dominance remain outside.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS 457 cells / 1828 branches;", len(primary), "primary records;",
          len(dependencies), "bindings", flush=True)


if __name__ == "__main__":
    main()
