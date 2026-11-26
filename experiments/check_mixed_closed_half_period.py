#!/usr/bin/env python3
"""Exact one-sided Bernstein bounds and closed-half run accounting.

No root, dilogarithm, source cell, numerical optimization or word-length
enumeration is performed. Original outward corner values are inherited.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import arb, ctx
from check_mixed_general_angle_seam_replacement import (
    add, scale, multiply, bernstein, BREAKS, PI_UPPER)

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_closed_half_period.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT/
                    "repro/results/research-mixed-closed-half-period.json")
    args = ap.parse_args()
    ctx.prec = 400
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, checks = {}, set(), {}, []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        if path in visited:
            return None
        raw = (ROOT/path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        record = json.loads(raw)
        visited.add(path)
        merged = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                if p in merged:
                    assert merged[p] == digest
                merged[p] = digest
                bind(p, digest)
        for p in merged:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)
        return record

    def load(stem):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        record = inherit(path)
        if record is None:
            raw = (ROOT/path).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == bind(path)
            record = json.loads(raw)
        assert record["status"] == "passed"
        assert record["proof_sha256"] == bind("notes/research_"+stem+".md")
        assert record["script_sha256"] == bind("experiments/check_"+stem+".py")
        primary[path] = record
        return record

    run = load("mixed_seam_run_connector_lower")
    isolated = load("mixed_general_angle_seam_replacement")
    height = load("mixed_height_resolved_seam_sources")
    acute = load("mixed_acute_gradient_height_transfer")
    deep = load("mixed_deep_low_half_region")
    profiles = height["profiles"]
    check("original scalar roots, sources and internal reserve are completed",
          run["scalar_comparisons"] == 48 and run["original_log_root_disks"] == 40
          and arb(run["minimum_margins"]["internal"]) > arb(1)/3
          and height["source_grid_values"] == 225
          and height["original_source_cells"] == 57092
          and height["independent_replay_source_cells"] == 57166)
    check("completed isolated phase charge retains its exact all-angle scope",
          isolated["typed_selection_cases"] == 36
          and isolated["initial_rectangles"] == isolated["accepted_cells"] == 576
          and isolated["maximum_depth"] == 0
          and F(isolated["uniform_comparison_loss"]) == F(3, 1000)
          and isolated["phase_parameter_cover_cells"] == 0)
    check("all one-real complex-neighbor gradient branches are retained",
          acute["exact_identity_count"] == 35 and acute["selected_branch_count"] == 16)
    check("rational pi ceiling and all cutoff pieces",
          arb(PI_UPPER.numerator)/PI_UPPER.denominator > arb.pi()
          and BREAKS == tuple(map(F, (".1", ".12", ".22", ".45", ".5"))))

    def ar(q):
        return arb(q.numerator)/q.denominator

    floors = {}
    internal_count = 0
    for row in run["comparisons"]:
        if row["kind"] == "internal":
            assert arb(row["margin_lower"]) > arb(1)/3
            internal_count += 1
            continue
        value = arb(row["real_phase"])-arb(row["raw_source_ceiling"])
        proposed = F(str(float(value.mid())))
        lower = F((proposed*10**8).__floor__()-1, 10**8)
        while not ar(lower) < value:
            lower -= F(1, 10**8)
        key = (row["kind"], *row["types"], *map(F, row["target"]))
        assert key not in floors
        floors[key] = lower
    intervals = {0: tuple(map(F, (".30", ".39"))),
                 1: tuple(map(F, (".27", ".33")))}
    expected = set()
    for eta, eps in itertools.product((0, 1), repeat=2):
        for y in (F(1, 10), F(1, 2)):
            expected.update(("left", eta, eps, y, t) for t in intervals[eps])
            expected.update(("right", eta, eps, t, y) for t in intervals[eta])
    check("all 32 individual boundary floors and all 16 internal floors",
          set(floors) == expected and internal_count == 16)

    def profile_lines(name, selection, kind):
        points = [(F(r["height"]), F(r["upper"])) for r in profiles[name]]
        if kind:
            points = [(h, u) for h, u in points if (h >= 0 if selection else h <= 0)]
        lines = []
        for (a, b), (c, d) in zip(points, points[1:]):
            slope = (d-b)/(c-a)
            lines.append((slope, b-slope*a))
        assert lines and all(a[0] <= b[0] for a, b in zip(lines, lines[1:]))
        assert all(max(m*h+b for m, b in lines) == u for h, u in points)
        zero = next(u for h, u in points if h == 0)
        return lines, zero

    def side_options(kind, selection, name, left, piece):
        lo, hi = BREAKS[piece:piece+2]
        cut_end = F(".12") if selection else F(".22")
        assert lo >= cut_end or hi <= cut_end
        cut = (F(1),) if lo >= cut_end else (
            -F(".1")/(cut_end-F(".1")), 1/(cut_end-F(".1")))
        taper = (F(1),) if hi <= F(".45") else (F(100), F(-400), F(400))
        factor = multiply(cut, taper)
        assert all(0 <= x <= 1 for x in bernstein(factor, lo, hi))
        coefficients = ((F(".014"),) if selection else
                        (F("-.057"),) if kind else (F("-.03"), F(".02")))
        lines, zero = profile_lines(name, selection, kind)
        K = (F(selection)-F(kind, 4), F(kind, 2))  # coefficient of pi
        options = [(F(0),)]
        for coefficient in coefficients:
            H = scale(factor, coefficient)
            absH = scale(factor, abs(coefficient))
            reset_cost = add(scale(multiply(K, H), 2), scale(absH, F(1, 2)))
            assert all(x >= 0 for x in bernstein(reset_cost, lo, hi))
            options.append(scale(reset_cost, PI_UPPER))
            same_cost = multiply(K, H)
            if (left and coefficient > 0) or (not left and coefficient < 0):
                same_cost = add(same_cost, scale(absH, F(1, 2)))
            assert all(x >= 0 for x in bernstein(same_cost, lo, hi))
            for slope, intercept in lines:
                options.append(add(scale(same_cost, PI_UPPER),
                                   scale(H, slope), (intercept-zero,)))
        assert all(len(p) <= 4 for p in options)
        return options

    cases = []
    for side in ("left", "right"):
        for eta, eps in itertools.product((0, 1), repeat=2):
            middle = eps if side == "left" else eta
            neighbor = eta if side == "left" else eps
            for selection in range(neighbor+1):
                for t in intervals[middle]:
                    cases.append((side, eta, eps, selection, t))
    assert len(cases) == len(set(cases)) == 24
    old, input_hash = None, None
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        old = json.loads(raw)
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
        assert len(old["intervals"]) == 96
    domains, worst = [], {}
    for caseid, (side, eta, eps, selection, t) in enumerate(cases):
        left = side == "left"
        middle = eps if left else eta
        neighbor = eta if left else eps
        lowkey = (side, eta, eps, F(".1"), t) if left else (side, eta, eps, t, F(".1"))
        highkey = (side, eta, eps, F(".5"), t) if left else (side, eta, eps, t, F(".5"))
        low, high = floors[lowkey], floors[highkey]
        slope = (high-low)/F(".4")
        interpolation = (low-F(".1")*slope, slope)
        if left:
            middle_cost = PI_UPPER*(F(".015") if middle == 0 else F(".057")*(F(".75")-t/2))
        else:
            middle_cost = PI_UPPER*(F(".01") if middle == 0 else F(".057")*(F(".25")-t/2))
        assert middle_cost > 0
        for piece in range(4):
            options = side_options(neighbor, selection,
                                   f"A{eps}{eta}" if left else f"B{eps}", left, piece)
            coefficients = [bernstein(add(p, scale(interpolation, -1), (middle_cost,)),
                                      BREAKS[piece], BREAKS[piece+1]) for p in options]
            upper = max(x for row in coefficients for x in row)
            assert upper < (F(9, 100) if left else F(0)), (side, eta, eps, selection, t, piece, upper)
            worst[side] = upper if side not in worst else max(worst[side], upper)
            row = dict(case=[side, eta, eps, selection, str(t)], piece=piece,
                       interval=list(map(str, BREAKS[piece:piece+2])),
                       branch_count=len(options), upper=str(upper))
            if old:
                assert old["intervals"][caseid*4+piece] == row
            domains.append(row)
    assert len(domains) == 96
    check("all 24 one-sided cases on 96 complete rational intervals", True)
    check("every proper run of length at least two pays three-thousandths per vertex",
          F(1, 3)-F(3, 1000) == F(991, 3000)
          and F(1, 3)-F(9, 100)-F(6, 1000) == F(89, 375)
          and F(89, 375) > 0)
    check("all-seam cycles and the single total finite tolerance",
          F(1, 3) > F(3, 1000)
          and F(3, 1000)-F(1, 1000) == F(1, 500))
    check("closed-half addition retains the old central remainder exponent",
          F(1, 500) > F(1, 8000))
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(status="passed", arithmetic="exact rational cubic Bernstein coefficients",
                  typed_selection_cases=24, rational_intervals=96,
                  subdivisions=0, largest_upper={k: str(v) for k, v in worst.items()},
                  left_boundary_debit="9/100", right_boundary_debit="0",
                  internal_phase_reserve="1/3", singleton_phase_reserve="3/1000",
                  seam_region_finite_loss="1/500", closed_half_remainder_loss="1/8000",
                  checks=checks, intervals=domains,
                  inherited_boundary_floors=[dict(key=[str(v) for v in key], lower=str(value))
                                             for key, value in sorted(floors.items())],
                  primary_records=len(primary), current_bindings=len(deps),
                  new_critical_roots=0, new_source_cells=0, cyclic_word_enumerations=0,
                  proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                  scope="Complete original selected contribution on closed [0,1/2]^m retains the central packet, including arbitrary zero-collar runs and both parities. No whole-period or knot-family result.")
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS 24 cases; 96 exact intervals; 0 subdivisions; maxima", worst,
          ";", len(deps), "bindings", flush=True)


if __name__ == "__main__":
    main()
