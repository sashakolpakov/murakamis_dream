#!/usr/bin/env python3
"""Exact identities and fixed outward scalars for the outgoing cap seam.

The whole-row and endpoint arguments are written proof inputs. No root
search, row grid, parameter cover or optimization is performed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx
import sympy as sp
import certify_mixed_endpoint_packet_extension as endpoint

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_cap_seam_source_bounds.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-cap-seam-source-bounds.json")
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    endpoint.PI, endpoint.II = arb.pi(), acb(0, 1)
    ar = endpoint.ar
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, visited, primary = {}, set(), {}

    def bind(path, expected=None):
        value = sha(ROOT/path)
        if expected is not None:
            assert value == expected, path
        assert path not in deps or deps[path] == value, path
        deps[path] = value
        return value

    def inherit(path):
        bind(path)
        if path in visited:
            return
        visited.add(path)
        record = json.loads((ROOT/path).read_text())
        # Inherited provenance includes archived partial-run records. Their
        # bytes are bound, but only the primary completed inputs are used as
        # passed theorems below.
        nested = {}
        for field in ("dependencies", "dependencies_sha256"):
            for p, digest in record.get(field, {}).items():
                assert p not in nested or nested[p] == digest, p
                nested[p] = digest
                bind(p, digest)
        for p in nested:
            if p.startswith("repro/results/") and p.endswith(".json"):
                inherit(p)

    for stem, proof, script in (
        ("complete-boundary-full-index-interval", "research_complete_boundary_full_index_interval",
         "check_complete_boundary_full_index_interval"),
        ("mixed-outer-cap-real-tails", "research_mixed_outer_cap_real_tails",
         "check_mixed_outer_cap_real_tails"),
    ):
        path = "repro/results/research-"+stem+".json"
        inherit(path)
        record = json.loads((ROOT/path).read_text())
        assert record["status"] == "passed", path
        proof_path = "notes/"+proof+".md"
        expected = record.get("proof_sha256", record.get("dependencies_sha256", {}).get(proof_path))
        assert expected is not None
        bind(proof_path, expected)
        bind("experiments/"+script+".py", record["script_sha256"])
        primary[path] = deps[path]
    replay_path = "repro/results/research-mixed-outer-cap-real-tails-replay.json"
    inherit(replay_path)
    replay = json.loads((ROOT/replay_path).read_text())
    assert replay["status"] == "passed"
    author_path = "repro/results/research-mixed-outer-cap-real-tails.json"
    author = json.loads((ROOT/author_path).read_text())
    assert replay["input_sha256"] == sha(ROOT/author_path)
    for key in ("proof_sha256", "script_sha256", "dependencies_sha256"):
        assert replay[key] == author[key]
    primary[replay_path] = deps[replay_path]
    for path in (
        "notes/research_mixed_complete_first_cap_packet.md",
        "notes/research_mixed_cap_outer_contour_reduction.md",
        "notes/research_mixed_conditional_torus_composition.md",
        "notes/research_mixed_complete_boundary_sum.md",
        "notes/research_mixed_real_zero_collar.md",
        "experiments/certify_mixed_endpoint_packet_extension.py",
    ):
        bind(path)

    checks, scalars = [], {}

    def check(name, condition):
        assert condition, name
        checks.append(name)

    b, q = sp.symbols("b q", real=True)
    relation = b*b+q*q-1
    A = 1+q+b
    check("the modulus cancellation also holds with negative b",
          sp.rem(sp.expand((1+q-b)*A-2*q*(1+q)), relation, b) == 0)
    check("the logarithmic derivative reduces to the signed b ratio",
          sp.rem(sp.expand(A*A-2*(1+q)*(1+b)), relation, b) == 0
          and sp.rem(sp.expand(q*q-(1-b)*(1+b)), relation, b) == 0)
    check("the two seam powers are the literal P exponents", [1-e for e in (0, 1)] == [1, 0])

    s0 = ar(F(7, 20))
    u0, _ = endpoint.critical(acb(s0))
    lam0 = endpoint.phase(acb(s0), u0).real
    slope, lift = endpoint.partials(acb(s0), u0)
    check("the tangent evaluation retains the original logarithmic lift",
          lift.imag > -endpoint.PI and lift.imag < endpoint.PI
          and 0 < u0.real < s0 and u0.imag > 0)
    check("the lower-half tangent has negative slope", slope.real < 0)
    tangent = lam0-s0*slope.real
    check("the type-four whole-row tangent ceiling is below .866", tangent < ar(F(433, 500)))
    scalars.update(lambda_at_7_20=lam0, slope_at_7_20=slope.real, tangent_ceiling=tangent)

    mid = acb(ar(F(1, 2)))
    um, _ = endpoint.critical(mid)
    lm = endpoint.phase(mid, um).real
    _, liftm = endpoint.partials(mid, um)
    check("the midpoint evaluation retains its original logarithmic lift",
          liftm.imag > -endpoint.PI and liftm.imag < endpoint.PI
          and 0 < um.real < ar(F(1, 2)) and um.imag > 0)
    check("the type-three whole-row maximum is below .808", lm < ar(F(101, 125)))
    scalars["lambda_at_half"] = lm

    delta = ar(F(1, 100))
    jd = endpoint.J(acb(delta)).real
    newton_max = -4*endpoint.J(acb(ar(F(1, 4)))).real
    low = 2*delta*arb(2).log()-4*jd
    high_c = ar(F(3, 5))+delta*arb(2).log()
    high_h = high_c-jd
    check("the complete Newton entropy is below three fifths", newton_max < ar(F(3, 5)))
    check("the small physical rows have rate below one quarter", low < ar(F(1, 4)))
    check("the last physical C rows have rate below .61", high_c < ar(F(61, 100)))
    check("the last physical H rows have rate below .65", high_h < ar(F(13, 20)))
    check("all literal endpoint ceilings are below both seam ceilings",
          F(13, 20) < F(101, 125) < F(433, 500))
    scalars.update(J_at_1_100=jd, newton_entropy_max=newton_max,
                   low_rows=low, high_C_rows=high_c, high_H_rows=high_h)

    result = dict(status="passed", precision_bits=args.precision,
        exact_and_scalar_check_count=len(checks), checks=checks,
        scalar_enclosures={k: str(v) for k, v in scalars.items()},
        seam_ceilings=["101/125", "433/500"],
        primary_records_sha256=primary, dependencies_sha256=deps,
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        parameter_cover_cells=0, root_searches=0,
        scope="Complete-color outgoing seam cap source ceilings, their small ordinary-color neighborhoods and the existing real-collar transfer. No adjacent-edge or boundary-sign comparison.")
    if old:
        for key in result:
            if key not in ("precision_bits", "scalar_enclosures", "input_sha256"):
                assert old[key] == result[key], key
        assert old["scalar_enclosures"].keys() == scalars.keys()
        assert all(value.overlaps(arb(old["scalar_enclosures"][key])) for key, value in scalars.items())
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact/scalar checks;", len(primary), "primary records;", len(deps), "bindings")


if __name__ == "__main__":
    main()
