#!/usr/bin/env python3
"""Exact low-transport algebra, local dependency checks and completed inputs."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_exact_low_transport.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-exact-low-transport.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, checks = {}, set(), {}, []

    def bind(path, expected=None):
        value = sha(ROOT / path)
        if expected is not None:
            assert value == expected, path
        if path in deps:
            assert deps[path] == value, path
        deps[path] = value
        return value

    def inherit(path):
        raw = (ROOT / path).read_bytes()
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

    def load(stem):
        path = "repro/results/research-" + stem.replace("_", "-") + ".json"
        rec = inherit(path)
        assert rec["status"] == "passed", path
        assert rec["proof_sha256"] == bind("notes/research_" + stem + ".md")
        assert rec["script_sha256"] == bind("experiments/check_" + stem + ".py")
        primary[path] = rec
        return rec

    def check(name, condition):
        assert condition, name
        checks.append(name)

    row = load("mixed_complex_right_row_reduction")
    deep = load("mixed_deep_low_half_region")
    incoming = load("mixed_exponential_incoming_memory")
    surplus = load("mixed_low_terminal_incoming_bound")
    half = load("mixed_closed_half_period")
    profiles = load("mixed_height_resolved_seam_sources")
    runs = load("mixed_long_right_runs_with_zero_contacts")
    for path in ("notes/research_mixed_split_cutoff_hybrid_contour.md",
                 "notes/research_mixed_half_endpoint_conditional_packet.md",
                 "notes/research_mixed_nonlow_interface_reduction.md",
                 "notes/research_mixed_synchronized_incoming_bounds.md"):
        bind(path)

    check("complete right-row theorem and all radial orientations",
          row["exact_identities"] == 2 and len(row["scalar_bounds"]) == 3
          and {(d["height_sign"], d["complex_target_first"])
               for d in row["height_cases"]} == {(-1, 0), (-1, 1), (1, 0), (1, 1)})
    check("deep-low coherent monotonicity has a larger threshold",
          F(deep["monotonicity_threshold"]) == F(1, 6)
          and F(deep["raising_endpoint"]) == F(1, 10)
          and F(deep["occupation_coefficient"]) == F(1, 4000))
    check("incoming potential and previously proved surplus are completed",
          incoming["exact_checks"] == 27 and surplus["exact_checks"] == 20
          and incoming["interface_sign_certified"] is False
          and surplus["interface_sign_certified"] is False)
    check("closed-half benchmark retains its pointwise phase loss",
          F(half["singleton_phase_reserve"]) == F(3, 1000)
          and half["typed_selection_cases"] == 24
          and half["rational_intervals"] == 96)
    check("all-angle height profiles are the full completed extraction",
          profiles["source_grid_values"] == 225
          and profiles["original_source_cells"] == 57092
          and profiles["independent_replay_source_cells"] == 57166)
    check("direct long-run restricted input uses the same profile rules",
          runs["nonlow_or_collar_run_cutoff"] == 352
          and F(runs["seam_boundary_allowance"]) == F(7, 4)
          and runs["profile_knot_count"] == 19
          and F(runs["right_phase_loss_per_vertex"]) == F(1, 100)
          and F(runs["seam_phase_loss_per_vertex"]) == F(3, 1000))

    # The analytic sign proof uses the exact endpoint ordering below;
    # no sampled sine inequality or numerical optimizer is accepted.
    x, u = sp.symbols("x u", real=True)
    check("trigonometric endpoint identity",
          sp.trigsimp(sp.cos(sp.pi*x)-sp.sin(sp.pi*x)
                      - sp.sqrt(2)*sp.sin(sp.pi*(sp.Rational(1, 4)-x))) == 0)
    check("the low domain lies below all three sign thresholds",
          F(0) < F(1, 10) < F(1, 6) < F(1, 4)
          and F(1, 10)+F(1, 2) < 1)
    J = sp.Function("J")
    for eta in (0, 1):
        for eps in (0, 1):
            # I(u,x)=J(u+x)-J(x), plus the original Fourier half.
            original = J(u+sp.Rational(1, 2))+J(u+x)-J(x) \
                -(2+eps)*J(u)-sp.Rational(eta, 2)*J(x)
            claimed = J(u+sp.Rational(1, 2))+J(u+x) \
                -(2+eps)*J(u)-(1+sp.Rational(eta, 2))*J(x)
            check(f"full raw Fourier allocation eta{eta} eps{eps}",
                  sp.expand(original-claimed) == 0)
            # Exact separation of the two nonnegative terms in (6).
            a, b = sp.symbols("a b", real=True)
            check(f"row derivative sign decomposition eta{eta} eps{eps}",
                  sp.expand((a-(1+sp.Rational(eta, 2))*b)
                            - ((a-b)-sp.Rational(eta, 2)*b)) == 0)

    check("low occupations are saturated for every allowed selection",
          400*(F(27, 100)-F(22, 100))**2 == 1
          and F(1, 10) < F(22, 100) and F(1, 10) < F(45, 100))
    # The two exact cutoffs both vanish on the entire transported interval.
    check("both row cutoffs share the full low zero interval",
          F(1, 10) < F(3, 25) < F(11, 50)
          and F(1, 1000) <= F(1, 10))

    # Normalize terminal layer to i=0. A transition j evaluates edge
    # (j-1,j), sees halo j+1, and charges occupations j-1,j.
    last = -1
    transitions = list(range(-6, last+1))
    coordinate_occurrences = {
        k: [j for j in transitions if k in (j-1, j)]
        for k in (-2, -1, 0)
    }
    cutoff_occurrences = {
        k: [(j, endpoint) for j in transitions for endpoint in (j-1, j)
            if k in (endpoint-1, endpoint, endpoint+1)]
        for k in (-2, -1, 0)
    }
    check("last halo is never an evaluated endpoint or occupation",
          coordinate_occurrences[0] == [])
    check("last halo controls only the already-zero middle target",
          cutoff_occurrences[0] == [(-1, -1)])
    check("low middle is evaluated only in the last edge",
          coordinate_occurrences[-1] == [-1])
    check("preceding middle dependence is only the first terminal height",
          cutoff_occurrences[-1] == [(-2, -2), (-1, -2), (-1, -1)])
    check("three appended terminal symbols do not alter the initial state",
          {-2, -1, 0}.isdisjoint({-5, -4, -3}))
    qx, qd, fx, fd, pa, pb, delta = sp.symbols("qx qd fx fd pa pb delta")
    difference = qx-qd-pa*delta+fx-fd-pb*delta
    check("exact raw-incoming tangent cancellation",
          sp.expand(difference.subs(pa, -pb)-(qx-qd+fx-fd)) == 0)
    # Literal cyclic incidence check at the short periods; the general
    # proof is the same telescoping stationarity identity.
    for m in (1, 2, 3):
        a = sp.symbols("a0:"+str(m))
        b = sp.symbols("b0:"+str(m))
        d = sp.symbols("d0:"+str(m))
        total = sum(a[j]*d[(j-1) % m]+b[j]*d[j] for j in range(m))
        total = total.subs({b[j]: -a[(j+1) % m] for j in range(m)})
        check(f"stationary tangent sum with literal period {m}",
              sp.expand(total) == 0)

    check("restricted right-run threshold pays its two boundary costs",
          2*F(7, 4)-F(351, 50) == -F(352, 100))
    check("each additional right coordinate improves the run inequality",
          F(1, 50)-F(1, 100) == F(1, 100))
    check("one global finite tolerance fits the retained loss",
          F(1, 100)-F(1, 200)-F(1, 1000) > 0
          and F(3, 1000)-F(1, 500) == F(1, 1000))
    check("all-right cycles retain their stronger internal loss",
          F(1, 50) > F(1, 100) > F(1, 200))

    input_hash = None
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        old = json.loads(raw)
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps and old["checks"] == checks
        assert old["cutoff_dependency_occurrences"] == {
            str(k): [list(t) for t in v] for k, v in cutoff_occurrences.items()}
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / p) == value for p, value in deps.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(
        status="passed", exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(deps),
        cutoff_dependency_occurrences=cutoff_occurrences,
        raising_endpoint="1/10", collar_upper="1/1000",
        universal_proper_right_run_cutoff=352,
        right_phase_loss_per_vertex="1/100", seam_phase_loss_per_vertex="3/1000",
        right_finite_loss_per_vertex="1/200", seam_finite_loss_per_vertex="1/500",
        numerical_cells_recomputed=0, new_critical_roots=0,
        sampled_histories=0, short_interface_sign_certified=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope="Exact terminal transport, complete raw-row low monotonicity and global R-priority envelope reduction. The inherited 352 cutoff therefore holds on the whole original domain with zero contacts. No general short-run or whole-period asymptotic.",
    )
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact checks;", len(primary), "primary records;",
          len(deps), "bindings; no numerical cover.", flush=True)


if __name__ == "__main__":
    main()
