#!/usr/bin/env python3
"""Reevaluate an existing five-window cover for the lower bound -7/125."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import time

from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_four_before_four_height_lower.md"
OLD_PROOF = "notes/research_mixed_four_before_four_height.md"
OLD_SCRIPT = "experiments/certify_mixed_four_before_four_height.py"
OLD_RECORD = "repro/results/research-mixed-four-before-four-height.json"
OLD_REPLAY = "repro/results/research-mixed-four-before-four-height-replay.json"
RECTS = [["3/10", "39/100", "-3/100", "1/50"],
         ["27/100", "33/100", "-57/1000", "-1/50"]]
LOWER, UPPER = F(-7, 125), F(-6, 125)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decode(address):
    box = [F(0), F(1), F(0), F(1)]
    for j, bit in enumerate(address):
        assert bit in "01"
        k = 2*(j % 2)
        mid = (box[k]+box[k+1])/2
        box[k+1-int(bit)] = mid
    return box


def cover(addresses):
    codes = sorted(addresses)
    assert codes and len(codes) == len(set(codes))
    assert all(not b.startswith(a) for a, b in zip(codes, codes[1:]))
    assert sum((F(1, 2**len(a)) for a in codes), F(0)) == 1
    for a in codes:
        decode(a)
    return codes


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--independent", action="store_true")
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-four-before-four-height-lower.json")
    args = ap.parse_args()
    assert args.precision >= 160
    if args.independent:
        assert args.input is not None
        assert args.output.resolve() != args.input.resolve()
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited = {}, set()

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        if path in deps:
            assert deps[path] == digest, path
        deps[path] = digest
        return digest

    def inherit(path):
        bind(path)
        record = json.loads((ROOT/path).read_text())
        if path in visited:
            return record
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

    old, old_replay = inherit(OLD_RECORD), inherit(OLD_REPLAY)
    for record in (old, old_replay):
        assert record["status"] == "passed"
        assert record["proof_sha256"] == bind(OLD_PROOF)
        assert record["script_sha256"] == bind(OLD_SCRIPT)
        assert record["boundary_products"] == 512 and record["accepted_cells"] == 4745
        assert record["rectangles"] == RECTS and F(record["upper_height"]) == UPPER
    assert old_replay["input_sha256"] == bind(OLD_RECORD)
    expected = [
        ((a, b, 1, 1, c), ta, tb, fa, fb)
        for a, b, c in itertools.product((0, 1), repeat=3)
        for ta, tb, fa, fb in itertools.product(range(2), range(2), range(4), range(4))
    ]
    assert len(expected) == len(set(expected)) == 512

    def saved_covers(record):
        found = {}
        for row in record["cases"]:
            key = (tuple(row["word"]), *row["external_types"], *row["faces"])
            assert key not in found
            found[key] = cover(row["addresses"])
            assert len(found[key]) == row["accepted"]
        assert set(found) == set(expected)
        assert sum(map(len, found.values())) == 4745
        return found

    addresses = saved_covers(old)
    assert addresses == saved_covers(old_replay)
    # Both implementations are bound in every output. Independent mode
    # imports only the independent sine/logarithm Newton primitive.
    primitives = [
        "experiments/certify_mixed_cyclic_window_heights.py",
        "experiments/replay_mixed_cyclic_window_heights.py",
    ]
    for p in primitives:
        bind(p)
    primitive = ROOT/primitives[int(args.independent)]
    spec = importlib.util.spec_from_file_location("original_five_window", primitive)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.PI = arb.pi()
    faces = [0, 0]

    def params(box, ta, tb):
        result = []
        for j, t in enumerate((ta, tb)):
            xl, xh, yl, yh = map(F, RECTS[t])
            v = m.ar(box[2*j]).union(m.ar(box[2*j+1]))
            f = faces[j]
            if f in (0, 2):
                result.append(acb(m.ar(xl)+m.ar(xh-xl)*v,
                                  m.ar(yl if f == 0 else yh)))
            else:
                result.append(acb(m.ar(xh if f == 1 else xl),
                                  m.ar(yl)+m.ar(yh-yl)*v))
        return result

    m.params = params
    inclusions = []
    for t, row in enumerate(RECTS):
        xl, xh, yl, yh = map(F, row)
        cr, ci = m.CENT[t]
        d = max((x-cr)**2+(y-ci)**2 for x in (xl, xh) for y in (yl, yh))
        margin = m.RAD[t]**2-d
        assert margin > 0
        inclusions.append(str(margin))
    ih = None
    if args.input:
        ih = sha(args.input)
        previous = json.loads(args.input.read_text())
        assert previous["status"] == "passed"
        assert previous["proof_sha256"] == ph and previous["script_sha256"] == sh
        assert previous["dependencies_sha256"] == deps
        assert previous["rectangles"] == RECTS
        assert F(previous["lower_height"]) == LOWER and F(previous["upper_height"]) == UPPER
        assert saved_covers(previous) == addresses

    start = time.monotonic()
    rows, visited_cells, minimum, maximum = [], 0, None, None
    for number, case in enumerate(expected):
        word, ta, tb, fa, fb = case
        faces[:] = [fa, fb]
        cell_min, cell_max = None, None
        for address in addresses[case]:
            assert time.monotonic()-start < 900
            result = m.certify(word, ta, tb, decode(address), F(-3, 25))
            assert result is not None, ("original window self-map failed", case, address)
            h = result[1].imag
            assert h > m.ar(LOWER) and h < m.ar(UPPER), (case, address, str(h))
            lo, hi = h.lower(), h.upper()
            cell_min = lo if cell_min is None else min(cell_min, lo)
            cell_max = hi if cell_max is None else max(cell_max, hi)
            visited_cells += 1
        minimum = cell_min if minimum is None else min(minimum, cell_min)
        maximum = cell_max if maximum is None else max(maximum, cell_max)
        rows.append(dict(word=list(word), external_types=[ta, tb], faces=[fa, fb],
                         addresses=addresses[case], accepted=len(addresses[case]),
                         height_lower=str(cell_min), height_upper=str(cell_max)))
        if (number+1) % 32 == 0:
            print("PASS", number+1, "/512;", visited_cells,
                  "saved cells; minimum", minimum, flush=True)
    assert visited_cells == 4745 and len(rows) == 512
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in deps.items())
    if args.input:
        assert ih == sha(args.input)
    output = dict(
        status="passed", precision_bits=args.precision, independent=args.independent,
        boundary_products=512, accepted_cells=visited_cells, visited_cells=visited_cells,
        subdivisions=0, cases=rows, rectangles=RECTS, lower_height=str(LOWER),
        upper_height=str(UPPER), minimum_height_lower=str(minimum),
        maximum_height_upper=str(maximum), rectangle_disk_inclusion_margins=inclusions,
        primitive="independent sine/logarithm and cotangent" if args.independent else
                  "original exponential/logarithm",
        elapsed_seconds=time.monotonic()-start, primary_records=2,
        current_bindings=len(deps), proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=deps,
        scope="Actual type-four right leg followed by type four: -.056<Im t_j<-.048. All512 original domains and4745 whole saved cells reevaluated, no subdivision. Geometry only; no transport or source sign.")
    if ih:
        output["input_sha256"] = ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+"\n")
    print("FULL PASS512", visited_cells, "minimum", minimum, flush=True)


if __name__ == "__main__":
    main()
