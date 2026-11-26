#!/usr/bin/env python3
"""Exact algebra and outward scalars for the literal outer-cap real tails."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx
import sympy as sp
import certify_mixed_endpoint_packet_extension as endpoint

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_outer_cap_real_tails.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-outer-cap-real-tails.json")
    args = parser.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    pi = arb.pi()
    ar = endpoint.ar
    endpoint.PI, endpoint.II = pi, acb(0, 1)
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
        nested = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in record.get(field, {}).items():
                assert name not in nested or nested[name] == digest
                nested[name] = digest
                bind(name, digest)
        for name in nested:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)

    for stem, proof, script in (
        ("complete-boundary-full-index-interval",
         "research_complete_boundary_full_index_interval",
         "check_complete_boundary_full_index_interval"),
        ("mixed-open-word-endpoint-rectangles",
         "research_mixed_open_word_endpoint_rectangles",
         "check_mixed_open_word_endpoint_rectangles"),
        ("mixed-half-angle-seam-source",
         "research_mixed_half_angle_seam_source",
         "check_mixed_half_angle_seam_source"),
    ):
        path = "repro/results/research-"+stem+".json"
        inherit(path)
        record = json.loads((ROOT/path).read_text())
        assert record["status"] == "passed", path
        proof_path = "notes/"+proof+".md"
        proof_hash = record.get("proof_sha256",
                                record.get("dependencies_sha256", {}).get(proof_path))
        assert proof_hash is not None, proof_path
        bind(proof_path, proof_hash)
        bind("experiments/"+script+".py", record["script_sha256"])
        primary[path] = deps[path]
    bind("notes/research_mixed_conditional_torus_composition.md")
    bind("notes/research_complete_boundary_complex_index.md")
    bind("notes/research_uniform_factorial_and_boundary_decay.md")
    bind("experiments/certify_mixed_endpoint_packet_extension.py")

    checks, scalars = [], {}

    def check(name, statement):
        assert statement, name
        checks.append(name)

    b, q = sp.symbols("b q", real=True)
    check("root modulus cancellation for the derivative identity",
          sp.rem(sp.expand((1+q-b)*(1+q+b)-2*q*(1+q)),
                 b*b+q*q-1, b) == 0)
    check("trigonometric modulus from the real discriminant",
          sp.expand(2*(1-(1-q-q*q))-2*q*(1+q)) == 0)
    check("A squared exceeds four when q+b is at least one",
          sp.expand((1+q+b)**2-4-(q+b-1)*(q+b+3)) == 0)
    check("lower endpoint entropy coefficients retain epsilon one",
          2+1+1+1 == 5)
    check("upper endpoint reflection arguments are complementary",
          sp.expand((1-sp.Symbol("d")-sp.Symbol("u"))+
                    (sp.Symbol("u")+sp.Symbol("d"))-1) == 0)
    check("Catalan alternating upper sum",
          F(1)-F(1,9)+F(1,25) == F(209,225))
    check("Catalan entropy rational ceiling",
          pi > ar(F(31,10)) and 2*F(209,225)/F(31,10) < F(3,5))

    e = acb(ar(F(49,100)))
    u, disc = endpoint.critical(e)
    beta, lift = endpoint.partials(e, u)
    check("bridge uses the original regular zero-lift saddle",
          disc.real > 1 and u.real > 0 and u.real < e.real
          and u.imag > 0 and lift.imag > -pi and lift.imag < pi)
    scalars["lambda_prime_49"] = str(beta.real)
    scalars["J_prime_49"] = str(endpoint.gp(e).real)
    check("bridge endpoint derivatives",
          beta.real < -ar(F(3,5)) and endpoint.gp(e).real > ar(F(3,5)))

    gamma = (ar(F(21,1000))*pi).exp()*(
        (ar(F(139,500))*pi).cos()**2+
        (ar(F(9,125))*pi).sinh()**2).sqrt()
    scalars["type_three_high_derivative_exponential_bound"] = str(gamma)
    check("type three high-row derivative bound", gamma < ar(F(3,4)))
    check("negative product portion is below the selected cosine",
          (ar(F(139,500))*pi).cos() > ar(F(1,2)))
    bridge = 2*(ar(F(21,1000))*pi).exp()*(
        (ar(F(96,125))*pi).sin()**2+
        (ar(F(9,125))*pi).sinh()**2).sqrt()
    scalars["type_three_bridge_product_bound"] = str(bridge)
    check("type three bridge product logarithm below one half",
          bridge < ar(F(1,2)).exp())
    check("all displayed derivative reserves exceed one tenth",
          ar(F(3,4)).log() < -ar(F(1,10))
          and arb(2).log() > ar(F(1,2))
          and -F(3,5)+F(1,2) == -F(1,10)
          and -F(3,5)-F(3,5)+F(7,10) == -F(1,2))
    check("bridge outgoing real interval",
          F(49,100)+F(139,500) == F(96,125)
          and F(1,2)+F(391,1000) == F(891,1000))

    low = acb(ar(F(27,100)))
    lu, ld = endpoint.critical(low)
    lbeta, llift = endpoint.partials(low, lu)
    check("lower-tail point is the original regular zero-lift saddle",
          ld.real > 1 and lu.real > 0 and lu.real < low.real
          and lu.imag > 0 and llift.imag > -pi and llift.imag < pi)
    scalars["lambda_prime_27"] = str(lbeta.real)
    scalars["J_prime_27"] = str(endpoint.gp(low).real)
    check("lower-tail endpoint derivatives",
          lbeta.real > ar(F(27,50))
          and endpoint.gp(low).real < ar(F(41,100)))
    check("lower-tail shifted real interval",
          F(246,1000) > 0 and F(27,100)+F(391,1000) == F(661,1000)
          and F(246,1000) < F(1,2) < F(661,1000) < 1)
    check("lower-tail cosine maxima occur below one sixteenth",
          (2*pi*ar(F(246,1000))).cos() < ar(F(1,16))
          and (2*pi*ar(F(661,1000))).cos() < ar(F(1,16)))
    check("lower-tail inward radial modulus exceeds one half",
          (-2*pi*ar(F(27,250))).exp() > ar(F(1,2)))
    check("lower-tail product and derivative reserves",
          F(1,2)-2*F(1,16) > 0
          and F(27,50)-F(41,100) == F(13,100))

    check("lower endpoint product bound",
          1+(ar(F(21,500))*pi).exp() < ar(F(9,4)))
    check("lower endpoint logarithm bounds",
          arb(25).log() < ar(F(7,2))
          and arb(2).log() < ar(F(7,10))
          and ar(F(9,4)).log() < 1)
    check("lower endpoint rational ceiling",
          2*F(1,100)*F(7,10)+5*F(1,100)*(F(7,2)+1)+F(1,100)
          == F(249,1000) < F(1,4))
    check("attached rectangles lie in endpoint-tail containing box",
          F(24,100) < F(246,1000) < F(350,1000) < F(40,100)
          and F(24,100) < F(278,1000) < F(391,1000) < F(40,100)
          and -F(20,1000) < F(21,1000))
    check("last product angles stay in the stated sector",
          F(24,100)-F(1,100) == F(23,100)
          and F(40,100) < F(1,2))
    denominator = (ar(F(23,50))*pi).sin()
    scalars["upper_endpoint_factor_floor"] = str(denominator)
    check("last factors are uniformly nonzero",
          denominator > ar(F(99,100)))
    ceiling = (ar(F(3,5))+ar(F(21,500))*pi+
               ar(F(1,100))*ar(F(200,99)).log())
    scalars["upper_endpoint_rate_ceiling"] = str(ceiling)
    check("upper endpoint rate below three quarters",
          ceiling < ar(F(3,4)))
    if old is not None:
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
        assert old["primary_records"] == primary and old["checks"] == checks
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path,digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    result = dict(status="passed", precision_bits=args.precision,
        exact_and_scalar_checks=len(checks), checks=checks, scalars=scalars,
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        primary_records=primary, primary_record_count=len(primary),
        dependencies_sha256=deps,
        scope="Literal outer-row bounds and both real-tail monotonicities only; no cap-action comparison or outer-contour dominance.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "checks;", len(primary), "primary records;",
          len(deps), "current bindings")


if __name__ == "__main__":
    main()
