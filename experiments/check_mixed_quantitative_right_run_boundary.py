#!/usr/bin/env python3
"""Focused root algebra, real-corner extraction and explicit right-run costs.

No new root proposals, source cells, parameter cover or word enumeration.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_quantitative_right_run_boundary.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-quantitative-right-run-boundary.json")
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, primary = {}, set(), {}

    def bind(path, expected=None):
        if path not in dependencies:
            dependencies[path] = sha(ROOT / path)
        if expected is not None:
            assert dependencies[path] == expected, path
        return dependencies[path]

    def inherit(path):
        if path in visited:
            return None
        raw = (ROOT / path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        record = json.loads(raw)
        visited.add(path)
        merged = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in record.get(field, {}).items():
                if name in merged:
                    assert merged[name] == digest
                merged[name] = digest
                bind(name, digest)
        for name in merged:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return record

    def load(stem, kind="check"):
        path = "repro/results/research-" + stem.replace("_", "-") + ".json"
        record = inherit(path)
        if record is None:
            raw = (ROOT / path).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == bind(path)
            record = json.loads(raw)
        assert record["status"] == "passed"
        proof_path = "notes/research_" + stem + ".md"
        proof_hash = record.get("proof_sha256")
        if proof_hash is None:
            proof_hash = record["dependencies_sha256"][proof_path]
        assert proof_hash == bind(proof_path)
        assert record["script_sha256"] == bind("experiments/" + kind + "_" + stem + ".py")
        primary[path] = record
        return record

    source = load("mixed_seam_run_connector_lower")
    load("mixed_acute_gradient_height_transfer")
    load("mixed_real_outer_support")
    load("mixed_closed_cotangent_roots")
    load("mixed_boundary_strip_bounds")
    load("mixed_fourier_weight_continuation")
    reset = load("mixed_full_height_reset", "certify")
    extraction = load("mixed_extracted_plateau_curvature")
    slopes = load("mixed_geometric_support_slopes", "certify")
    right = load("mixed_two_right_source_bound", "certify")
    load("mixed_deep_low_half_region")
    bind("notes/research_mixed_direct_right_run_replacement.md")
    bind("notes/research_mixed_split_cutoff_hybrid_contour.md")

    # The exact original polynomials, including both endpoint evaluations.
    S, p, q, x = sp.symbols("S p q x", real=True)
    F0 = S**2 + (p + q)*S - 1 + sp.I*(q-p)
    F1 = (S+sp.I)*(S+p)*(S+q)-2*sp.I*(p-sp.I)*(q+sp.I)
    exact = []

    def identity(name, lhs, rhs):
        assert sp.simplify(sp.expand(lhs-rhs)) == 0, name
        exact.append(name)

    identity("quadratic at i", F0.subs(S, sp.I), -2+2*sp.I*q)
    identity("quadratic at minus i", F0.subs(S, -sp.I), -2-2*sp.I*p)
    identity("cubic at i", F1.subs(S, sp.I), -4*(q+sp.I))
    identity("cubic at minus i", F1.subs(S, -sp.I),
             -2*sp.I*(p-sp.I)*(q+sp.I))
    identity("original cubic coefficients", F1,
             S**3+(p+q+sp.I)*S**2+(p*q+sp.I*(p+q))*S
             -sp.I*p*q+2*p-2*q-2*sp.I)
    identity("cubic middle coefficient triangle bound",
             (2*p+1)-(p*q+p+q), (p+1)*(1-q))
    identity("cubic constant coefficient triangle bound",
             (3*p+4)-(p*q+2*p+2*q+2), (p+2)*(1-q))
    identity("numerator factor for p at least three",
             sp.Rational(17, 3)*p-(4*p+5), sp.Rational(5, 3)*(p-3))
    identity("denominator factor for p at least three",
             5*p-(3*p+6), 2*(p-3))
    identity("ratio majorant coefficient",
             sp.Rational(17, 3)*25/2, sp.Rational(425, 6))
    C = sp.symbols("C", real=True)
    identity("integrable derivative primitive",
             sp.diff(x*(C+sp.Rational(7, 2)-sp.Rational(7, 2)*sp.log(x)), x),
             C-sp.Rational(7, 2)*sp.log(x))
    aa, bb, hh = sp.symbols("aa bb hh", real=True)
    identity("imaginary gradient response along height",
             sp.im(sp.I*(-aa+sp.I*bb)*hh), -aa*hh)
    slope_re, slope_im, dx, h = sp.symbols("slope_re slope_im dx h", real=True)
    identity("boundary tangent sign",
             sp.re((slope_re+sp.I*slope_im)*(dx-sp.I*h)),
             slope_re*dx+slope_im*h)

    # Freshly parse the full outward corner intervals; never use a midpoint.
    intervals = {0: (F("0.30"), F("0.39")), 1: (F("0.27"), F("0.33"))}
    expected = set()
    for eta, eps in itertools.product((0, 1), repeat=2):
        for endpoint in (F(1, 10), F(1, 2)):
            expected.update(("left", eta, eps, endpoint, t) for t in intervals[eps])
            expected.update(("right", eta, eps, t, endpoint) for t in intervals[eta])
    corners = {}
    for row in source["comparisons"]:
        if row["kind"] == "internal":
            continue
        key = (row["kind"], *row["types"], *map(F, row["target"]))
        assert key not in corners
        ball = arb(row["real_phase"])
        assert ball > arb(11)/25, key
        corners[key] = row["real_phase"]
    assert set(corners) == expected and len(corners) == 32
    minimum_real = min(arb(v).lower() for v in corners.values())
    assert source["scalar_comparisons"] == 48 and source["original_log_root_disks"] == 40
    assert extraction["validated_boundary_products"] == 64
    assert extraction["validated_saved_cells"] == 36325
    assert reset["domains"] == 64 and reset["cells"] == 36325
    assert slopes["case_count"] == 512 and slopes["accepted_cells"] == 4820
    assert right["boundary_products"] == 512 and right["accepted_cells"] == 4820

    pi = arb.pi()
    scalar_checks = []

    def positive(name, value):
        assert value.is_finite() and value > 0, (name, value)
        scalar_checks.append(dict(name=name, margin=str(value)))

    positive("moving cotangent at one tenth exceeds three",
             (pi/10).cos()/(pi/10).sin()-3)
    g_sixth = ((acb(0, -pi/3).exp().polylog(2)-pi*pi/6) /
               acb(0, 2*pi))
    positive("all real factorial rates below one sixth",
             arb(1)/6+g_sixth.real)
    C0 = (arb(425)/6).log()-3*pi.log()-arb(2).log()
    integral = (C0+arb(7)/2*(1+arb(10).log()))/10
    positive("integrable low-coordinate loss below 119/100",
             arb(119)/100-integral)
    positive("all admitted height losses below one fifth",
             arb(1)/5-arb(609)/10000*pi)
    gradient = pi/2+arb(23)/200*pi+arb(57)/50*arb(2).sqrt()
    positive("actual reference imaginary gradient below 18/5",
             arb(18)/5-gradient)
    raw = arb(5)/4+arb(57)/500*pi
    positive("complete raw boundary ceiling below 13/8",
             arb(13)/8-raw)

    rational_checks = []

    def rational(name, condition):
        assert condition, name
        rational_checks.append(name)

    rational("deep real phase floor", F(11, 25)-F(119, 100) == -F(3, 4))
    rational("nonlow complex phase floor", F(11, 25)-F(1, 5) == F(6, 25))
    gamma = F(1, 5)*F(73, 100)+F(18, 5)*F(57, 1000)
    rational("only changed right tangent cost", gamma == F(439, 1250))
    general = F(13, 8)+F(3, 4)+gamma
    nonlow = F(13, 8)-F(6, 25)+gamma
    rational("general boundary strict reserve", F(11, 4)-general == F(119, 5000) > 0)
    rational("nonlow boundary strict reserve", F(7, 4)-nonlow == F(69, 5000) > 0)
    for cost, cutoff in ((F(11, 4), 552), (F(7, 4), 352)):
        rational(f"run threshold {cutoff}", 2*cost-F(cutoff-1, 50) == -F(cutoff, 100))
    rational("longer-run coefficient stays favorable", F(1, 50)-F(1, 100) == F(1, 100) > 0)
    rational("fixed-word finite tolerance", F(1, 100)-F(1, 200) == F(1, 200))

    old, input_hash = None, None
    if args.input:
        raw_input = args.input.read_bytes()
        input_hash = hashlib.sha256(raw_input).hexdigest()
        old = json.loads(raw_input)
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == dependencies
        assert old["exact_checks"] == exact
        assert old["rational_checks"] == rational_checks
        assert old["real_corners"] == [
            dict(key=list(map(str, key)), value=value)
            for key, value in sorted(corners.items())]
        assert old["run_cutoffs"] == {"outside_collar": 552, "nonlow": 352}
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(
        status="passed", precision_bits=args.precision,
        exact_identity_count=len(exact), exact_checks=exact,
        scalar_comparison_count=len(scalar_checks), scalar_checks=scalar_checks,
        rational_check_count=len(rational_checks), rational_checks=rational_checks,
        real_corner_count=32, minimum_real_corner=str(minimum_real),
        real_corners=[dict(key=list(map(str, key)), value=value)
                      for key, value in sorted(corners.items())],
        low_derivative_integral=str(integral),
        reference_imaginary_gradient_bound=str(gradient),
        raw_boundary_ceiling=str(raw),
        boundary_costs={"outside_collar": "11/4", "nonlow": "7/4"},
        run_cutoffs={"outside_collar": 552, "nonlow": 352},
        primary_records=len(primary), current_bindings=len(dependencies),
        new_critical_roots=0, new_source_cells=0, new_parameter_cells=0,
        cyclic_word_enumerations=0, proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=dependencies,
        scope="Explicit long-right-run suppression outside a fixed positive zero collar; no short-run, physical-zero-contact, full-period or knot-family conclusion.",
    )
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(exact), "identities;", len(scalar_checks), "scalars;",
          len(rational_checks), "rational checks; 32 corners;",
          len(dependencies), "bindings", flush=True)


if __name__ == "__main__":
    main()
