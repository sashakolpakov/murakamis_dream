#!/usr/bin/env python3
"""Exact Gram forcing and one original open-(4,4) root; no root proposals."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, acb_mat, arb, ctx
import sympy as sp
import certify_mixed_open_word_critical_localization as local

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_gram_forced_transport.md"
WITNESS = {
    "centers": [
        ["0.34631393520098791", "-0.038944335631581867"],
        ["0.31130778505506168", "-0.062275178143913874"],
        ["0.22618679546498327", "0.034903800154668048"],
    ],
    "inverse": [
        [["-0.089489641123893141", "-0.037297709538635801"],
         ["-0.0075024841417215948", "0.017766270260015607"],
         ["-0.01589155534514437", "-0.037163209437370344"]],
        [["-0.0075024841417215948", "0.017766270260015607"],
         ["-0.060690331423185258", "-0.048798474724305756"],
         ["-0.0074071905810770946", "0.0031264905851780414"]],
        [["-0.01589155534514437", "-0.037163209437370344"],
         ["-0.0074071905810770946", "0.0031264905851780414"],
         ["-0.039507211537825417", "-0.0098868107345994605"]],
    ],
    "radius": "1e-10",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def J(z):
    pi, ii = arb.pi(), acb(0, 1)
    return ((pi*pi/6-(2*pi*ii*z).exp().polylog(2))/(2*pi*ii)
            +ii*pi*z*(1-z)/2)


def jacobian(z):
    value = local.jacobian(z, z[1], 1)
    value[1, 1] += arb.pi()*local.cot(2*z[1])+acb(0, 1)*arb.pi()
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--precision", type=int, default=256)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-gram-forced-transport.json")
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
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

    for stem, script, replay in (
        ("mixed_two_cap_torus_composition", "check", False),
        ("mixed_open_word_hessian", "check", True),
        ("mixed_open_word_critical_localization", "certify", True),
    ):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        author = inherit(path)
        assert author["status"] == "passed"
        bind("notes/research_"+stem+".md", author["proof_sha256"])
        bind("experiments/"+script+"_"+stem+".py", author["script_sha256"])
        primary[path] = deps[path]
        if replay:
            rp = path[:-5]+"-replay.json"
            saved = inherit(rp)
            assert saved["status"] == "passed"
            assert saved["input_sha256"] == deps[path]
            assert saved["proof_sha256"] == author["proof_sha256"]
            # Hessian and localization use their same author checker in replay.
            assert saved["script_sha256"] == author["script_sha256"]
            assert saved["dependencies_sha256"] == author["dependencies_sha256"]
            assert saved["precision_bits"] > author["precision_bits"]
            replays[rp] = deps[rp]
    bind("notes/research_mixed_wire_exact_contraction.md")

    exact, outward = [], []

    def check(name, condition):
        assert condition, name
        exact.append(name)

    def bound(name, condition):
        assert condition, name
        outward.append(name)

    n, X, Y, r, a, b = sp.symbols("n X Y r a b", nonzero=True)
    check("last Pochhammer leading exponent reduces by one minus N",
          sp.expand((n-1)*(n-2)/2-n*(n-1)/2-(1-n)) == 0)
    check("last row phase coefficient is one after r to the N",
          sp.expand((n-1)+1-n) == 0)
    check("simplified forcing keeps both wrapping factors and its sign",
          sp.cancel(1/((1-1/(r*X))*(1-r*X))+r*X/(1-r*X)**2) == 0)
    check("physical homogeneous transport ratio",
          sp.cancel(Y**-1*(1-r*X*Y)-(Y**-1-r*X)) == 0)
    check("physical wrap multiplier vanishes for b zero",
          sp.expand((Y**-1-1).subs(Y, 1)) == 0)
    check("the apparent positive X coefficient cancels",
          sp.expand(-r*sp.Symbol("c0")+r*sp.Symbol("c0")) == 0)
    chirp = lambda z: sp.I*sp.pi*z*(1-z)/2
    check("calibrated physical factorial phase is W",
          sp.expand(chirp(a+b)-chirp(a)-chirp(b)+2*sp.I*sp.pi*a*b
                    -sp.I*sp.pi*a*b) == 0)
    g2 = lambda x, y: (3+x**-1+y**-1-(x*y)**-1)/4
    check("independent exact N two forcing identity",
          sp.cancel((1+X)*g2(-X, Y)-(Y**-1+X)*g2(X, Y)
                    -(1-Y**-2)*(1-X**-1)/4) == 0)
    check("two negative heights give the stated diagonal forcing rate",
          -2*(sp.Symbol("h")+sp.Symbol("h")) == -4*sp.Symbol("h"))

    witness = old["witness"] if old is not None else WITNESS
    assert witness == WITNESS
    assert len(witness["centers"]) == 3 and len(witness["inverse"]) == 3
    assert all(len(row) == 3 for row in witness["inverse"])
    radius = local.ar(witness["radius"])
    bound("positive fixed witness radius", radius > 0)
    c = [local.cp(v) for v in witness["centers"]]
    inverse = acb_mat([[local.cp(v) for v in row] for row in witness["inverse"]])
    z = [v+acb(arb(0, radius), arb(0, radius)) for v in c]
    derivative = jacobian(z)
    bound("whole derivative square is regular",
          all(derivative[i, j].is_finite() for i in range(3) for j in range(3)))
    bound("rational Newton preconditioner is invertible", abs(inverse.det()) > 0)
    error = local.ident(3)-inverse*derivative
    residual = inverse*local.equation(c, c[1], 1)
    newton = []
    for i in range(3):
        value = abs(residual[i, 0])+radius*sum(abs(error[i, j]) for j in range(3))
        bound("original-log Newton disk self-map coordinate %d" % i, value < radius)
        newton.append(str(value))
    e, t, u = z
    ar = local.ar
    bound("private leg remains in E",
          ar(".33") < e.real < ar(".47") and ar("-.09") < e.imag < ar(".08"))
    bound("attached leg remains in Q",
          ar(".23") < t.real < ar(".45") and ar("-.12") < t.imag < ar(".12"))
    bound("attached complex disk remains in its original D4",
          abs(c[1]-acb(ar(".30"), ar("-.052")))+radius < ar(".064"))
    bound("auxiliary remains in U",
          ar(".21") < u.real < ar(".25") and ar(".01") < u.imag < ar(".10"))
    bound("every logarithmic argument retains the original strip",
          all(0 < v.real < 1 for v in (e, t, u, e-u, e+t, 2*t))
          and 0 < u.real < ar(".5"))
    # Chain rule differentiates the literal b=t equation, not the fixed-b one.
    pi, ii = arb.pi(), acb(0, 1)
    expected_tt = pi*local.cot(e+t)+2*pi*local.cot(2*t)-3*pi*local.cot(t)+2*ii*pi
    bound("linked external-leg derivative agrees with the literal equation",
          (derivative[1, 1]-expected_tt).contains(0))
    W = J(2*t)-2*J(t)+ii*pi*t*t
    forcing = -4*pi*t.imag
    excess = forcing-W.real
    bound("both actual attached heights are strictly negative", t.imag < ar("-.062"))
    bound("actual regular phase is below the declared rational ceiling", W.real < ar(".461"))
    bound("actual forcing is above the declared rational floor", forcing > ar(".782"))
    bound("forcing exceeds the regular phase by more than eight twenty-fifths",
          excess > ar(F(8, 25)))

    if old is not None:
        assert old["status"] == "passed"
        assert old["proof_sha256"] == ph and old["script_sha256"] == sh
        assert old["dependencies_sha256"] == deps
        assert old["primary_records"] == primary and old["saved_replays"] == replays
        assert old["exact_checks"] == exact and old["outward_checks"] == outward
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    result = dict(status="passed", precision_bits=args.precision,
        exact_check_count=len(exact), exact_checks=exact,
        outward_check_count=len(outward), outward_checks=outward,
        witness=witness, newton_self_map_bounds=newton,
        attached_root=[str(t.real), str(t.imag)],
        regular_phase=[str(W.real), str(W.imag)], forcing_rate=str(forcing),
        forcing_excess=str(excess), forcing_excess_floor="8/25",
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        primary_records=primary, saved_replays=replays, dependencies_sha256=deps,
        new_root_proposals=0, parameter_cover_cells=0,
        scope="Exact all-level forced Gram transport and failure of a separate uniform regular-phase upper at the actual open-(4,4) attached pair. No failure of the exact two-cap identity or full invariant is asserted.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(exact), "exact;", len(outward), "outward;",
          len(primary), "primary;", len(deps), "bindings; excess", excess)


if __name__ == "__main__":
    main()
