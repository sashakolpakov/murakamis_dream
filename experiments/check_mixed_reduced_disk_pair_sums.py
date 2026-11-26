#!/usr/bin/env python3
"""Extract pair sums from unchanged reduced-disk affine source witnesses.

No root proposals, cell refinements, or new source inequalities occur.
The type-four/two-type-three vertex sum remains explicitly unresolved.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx
import certify_mixed_reduced_disk_conditional_packets as source

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_reduced_disk_pair_sums.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def affine_support(constant, coefficients, radius, box, types, midpoint):
    value = constant.real
    for axis, (coefficient, typ) in enumerate(zip(coefficients, types)):
        center = acb(source.ar(source.CENTERS[typ][0]),
                     source.ar(source.CENTERS[typ][1]))
        value -= (coefficient*(midpoint[axis]-center)).real
        if abs(coefficient) > 0:
            angle = (2*source.PI*source.ar(box[axis][0]).union(
                source.ar(box[axis][1])) + coefficient.arg())
            value += source.ar(source.RADII[typ])*abs(coefficient)*angle.cos()
        else:
            assert coefficient.is_zero()
    return value + arb(0, radius.upper())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-reduced-disk-pair-sums.json")
    args = parser.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    source.PI, source.II = arb.pi(), acb(0, 1)
    source.base.PI, source.base.I = source.PI, source.II
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    bindings = {}

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        assert path not in bindings or bindings[path] == digest, path
        bindings[path] = digest
        return digest

    paths = ["repro/results/research-mixed-reduced-disk-conditional-packets"+
             suffix+".json" for suffix in ("", "-replay")]
    records = []
    for path in paths:
        bind(path)
        record = json.loads((ROOT/path).read_text())
        assert record["status"] == "passed"
        for name, digest in record["dependencies_sha256"].items():
            bind(name, digest)
        bind("notes/research_mixed_reduced_disk_conditional_packets.md",
             record["proof_sha256"])
        bind("experiments/certify_mixed_reduced_disk_conditional_packets.py",
             record["script_sha256"])
        records.append(record)
    author, replay = records
    assert replay["input_sha256"] == bindings[paths[0]]
    assert author["precision_bits"] >= 256 and replay["precision_bits"] >= 320
    specs = [(eps, a, b) for eps in (0, 1) for a, b in ((0, 0), (0, 1), (1, 1))]
    for record in records:
        assert [tuple(d["types"]) for d in record["domains"]] == specs
        assert record["domain_count"] == 6 and record["orientations_per_domain"] == 2
        assert (record["accepted_cells"], record["visited_nodes"]) == (4409, 8812)
    if old:
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == bindings

    start = time.monotonic()
    domains, total, nodes = [], 0, 0
    vertex_floors = [F(3, 5), F(3, 5), F(3, 5), F(49, 100), F(21, 40), F(11, 20)]
    for index, (domain, saved) in enumerate(zip(author["domains"], replay["domains"])):
        assert domain["tree"] == saved["tree"]
        assert domain["leaves"] == saved["leaves"]
        eps, ta, tb = domain["types"]
        pending = [([(F(0), F(1)), (F(0), F(1))], 0)]
        cursor, leaves = 0, 0
        minimum, maximum, addresses = [None]*3, [None]*3, [None]*3
        while pending:
            box, depth = pending.pop()
            node = domain["tree"][cursor]
            cursor += 1
            nodes += 1
            if node[0] == "S":
                assert len(node) == 2 and type(node[1]) is int and node[1] == depth % 2
                left, right = source.split(box, node[1])
                pending.extend([(left, depth+1), (right, depth+1)])
                continue
            assert node[0] == "L" and len(node) == 2
            witness = node[1]
            parameters = source.parameter(box, (ta, tb))
            midpoint = source.parameter([(sum(v, F(0))/2,)*2 for v in box], (ta, tb))
            assert source.root_box(witness, parameters, midpoint, eps) is not None
            centers = list(map(source.cp, witness["centers"]))
            affine = [[source.cp(v) for v in row] for row in witness["affine"]]
            radii = list(map(source.ar, witness["radii"]))
            data = [
                (centers[0]+centers[1], [affine[0][j]+affine[1][j] for j in range(2)],
                 sum(radii, arb(0))),
                (centers[0]+midpoint[0], [affine[0][0]+1, affine[0][1]], radii[0]),
                (centers[1]+midpoint[1], [affine[1][0], affine[1][1]+1], radii[1]),
            ]
            for j, (constant, coefficients, radius) in enumerate(data):
                value = affine_support(constant, coefficients, radius, box, (ta, tb), midpoint)
                lower = F(str(value.lower().fmpq()))
                upper = F(str(value.upper().fmpq()))
                assert lower > (vertex_floors[index] if j == 0 else F(109, 200))
                assert upper < F(77, 100)
                if minimum[j] is None or lower < minimum[j]:
                    minimum[j] = lower
                    addresses[j] = dict(node=cursor-1,
                        angles=[[str(v) for v in interval] for interval in box])
                maximum[j] = upper if maximum[j] is None else max(maximum[j], upper)
            leaves += 1
            total += 1
        assert cursor == len(domain["tree"]) == 2*leaves-1
        assert leaves == domain["leaves"]
        domains.append(dict(types=[eps, ta, tb], leaves=leaves,
            lower=list(map(str, minimum)), upper=list(map(str, maximum)),
            lower_addresses=addresses, vertex_floor=str(vertex_floors[index])))
        print("PASS pair sums", eps, ta, tb, leaves, flush=True)
    assert (total, nodes) == (4409, 8812)
    result = dict(status="passed", precision_bits=args.precision,
        quantities=["Re(s+t)", "Re(a+s)", "Re(t+b)"], domains=domains,
        accepted_cells=total, visited_nodes=nodes, source_type_families=6,
        source_orientations_per_family=2, wire_lower="109/200", upper="77/100",
        vertex_floors=list(map(str, vertex_floors)),
        unresolved_vertex_case=[1, 0, 0],
        unresolved_statement="Re(s+t)>1/2 is neither proved nor disproved in the own4/external3,3 case.",
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=bindings,
        primary_records={path: bindings[path] for path in paths}, input_sha256=ih,
        new_root_proposals=0, new_cover_cells=0, changed_source_witnesses=0,
        elapsed_seconds=time.monotonic()-start,
        scope="Existing complete affine witnesses prove all wire sums and five vertex-sum cases on reduced external disks. No positive geometric branch or global source identification is inferred.")
    if old:
        assert old["accepted_cells"] == total and old["visited_nodes"] == nodes
        assert old["wire_lower"] == result["wire_lower"] and old["upper"] == result["upper"]
        assert old["vertex_floors"] == result["vertex_floors"]
        assert old["unresolved_vertex_case"] == [1, 0, 0]
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in bindings.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", total, nodes, len(bindings), "bindings; one vertex case unresolved")


if __name__ == "__main__":
    main()
