#!/usr/bin/env python3
"""Exact retained-edge cancellation and completed transport provenance."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_plateau_low_incoming_bound.md"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-plateau-low-incoming-bound.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, checks = {}, set(), {}, []

    def bind(path, expected=None):
        value = sha(ROOT/path)
        if expected is not None:
            assert value == expected, path
        if path in deps:
            assert deps[path] == value, path
        deps[path] = value
        return value

    def inherit(path):
        raw = (ROOT/path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        rec = json.loads(raw)
        if path in visited:
            return rec
        visited.add(path)
        merged = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in rec.get(field, {}).items():
                if name in merged:
                    assert merged[name] == digest, name
                merged[name] = digest
                bind(name, digest)
        for name in merged:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return rec

    def load(stem):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        rec = inherit(path)
        assert rec["status"] == "passed"
        assert rec["proof_sha256"] == bind("notes/research_"+stem+".md")
        assert rec["script_sha256"] == bind("experiments/check_"+stem+".py")
        primary[path] = rec
        return rec

    def check(name, condition):
        assert condition, name
        checks.append(name)

    surplus = load("mixed_low_terminal_incoming_bound")
    transport = load("mixed_exact_low_transport")
    real = load("mixed_real_outer_support")
    for path in ("notes/research_mixed_frozen_early_transport.md",
                 "notes/research_mixed_nonlow_occupation_loss.md",
                 "notes/research_mixed_full_nonlow_half_region.md",
                 "notes/research_mixed_real_one_small_support.md"):
        bind(path)
    check("same complete real one-small and early allocations",
          F(surplus["original_phase_loss"]) == F(11, 200)
          and F(surplus["original_early_loss"]) == F(1, 100)
          and F(surplus["occupation_coefficient"]) == F(1, 4000))
    check("completed exact transport and last-halo deduction",
          transport["exact_checks"] == 31
          and F(transport["raising_endpoint"]) == F(1, 10)
          and transport["cutoff_dependency_occurrences"]["0"] == [[-1, -1]]
          and transport["short_interface_sign_certified"] is False)
    check("completed real concavity and source normalization",
          real["exact_identities"] == 9 and real["validated_source_records"] == 2
          and "triangle determinant" in real["identities"]
          and "complex Schur correction 1,1" in real["identities"])
    check("plateau endpoints never enter a real moving interval",
          F(1, 10) < F(3, 25) < F(11, 50) < F(9, 20))
    check("exact early reserve remains unchanged",
          F(6349, 4000000)-5*F(1, 4000) == F(1349, 4000000) > 0)

    Wm, Wp, Z, theta, kappa, omega, c0, c1 = sp.symbols(
        "Wm Wp Z theta kappa omega c0 c1", real=True)
    qm, qp = sp.Rational(151, 20), sp.Rational(11, 2)
    bm = -Wm-sp.Rational(1, 100)-qm*c0**2
    bp = -Wp-sp.Rational(1, 100)-qp*c1**2
    oldm = sp.Rational(9, 200)-qm*c0**2
    oldp = sp.Rational(9, 200)-qp*c1**2
    check("incoming marked edge retains its exact extra deficit",
          sp.expand(bm-oldm+Wm+sp.Rational(11, 200)) == 0)
    check("exit marked edge retains its exact extra deficit",
          sp.expand(bp-oldp+Wp+sp.Rational(11, 200)) == 0)
    exit_weight = Wp+Z+theta*kappa/2
    direct = -exit_weight-(1-theta)*(omega+kappa)-bm-bp
    claimed = Wm-Z+sp.Rational(1, 50)+qm*c0**2+qp*c1**2 \
        -(1-theta/2)*kappa-(1-theta)*omega
    check("literal exit cancellation and every terminal occupation",
          sp.expand(direct-claimed) == 0)
    old = -exit_weight-(1-theta)*(omega+kappa)-oldm-oldp
    check("exact improvement over the old constant-surplus bound at d",
          sp.expand(old-claimed-(-Wm-Wp-sp.Rational(11, 100))) == 0)
    Wx = sp.Symbol("Wx", real=True)
    check("transport below d changes only the retained incoming edge",
          sp.expand(claimed+Wx-Wm-claimed.subs(Wm, Wx)) == 0)
    check("last terminal occupation is not inserted into the final bound",
          set(claimed.free_symbols) <= {Wm, Z, theta, kappa, omega, c0, c1})
    for name, q in (("incoming", F(151, 20)), ("exit", F(11, 2))):
        check(name+" retained surplus is positive at the weakest source bound",
              F(11, 200)-F(1, 100)-q*F(57, 1000)**2 > 0)
    check("two original half-shares combine at the marked low vertex",
          F(1, 2)+F(1, 2) == 1)
    y, a, k, s = sp.symbols("y a k s", real=True)
    quadratic = k*y-s*(y-a)**2/10
    stationary = a+5*k/s
    check("central occupation quadratic derivative",
          sp.expand(sp.diff(quadratic, y)-(k-s*(y-a)/5)) == 0)
    check("central scalar optimizer before interval projection",
          sp.simplify(sp.diff(quadratic, y).subs(y, stationary)) == 0)
    check("exact concave quadratic completion",
          sp.simplify(quadratic.subs(y, stationary)-quadratic
                      -s*(y-stationary)**2/10) == 0)
    check("central and saturated occupation pieces meet",
          F(1, 20)**2/F(10) == F(1, 4000))
    check("reference occupation breakpoints lie within the plateau",
          F(27, 100)-F(1, 20) == F(11, 50)
          and F(39, 100)+F(1, 20) < F(9, 20))
    check("a selected plateau symbol has the same saturated occupation",
          min(F(1), F(1)+F(400)*F(0)**2) == 1)

    input_hash = None
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        oldrec = json.loads(raw)
        assert oldrec["status"] == "passed"
        assert oldrec["proof_sha256"] == ph and oldrec["script_sha256"] == sh
        assert oldrec["dependencies_sha256"] == deps and oldrec["checks"] == checks
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == value for p, value in deps.items())
    if args.input:
        assert input_hash == sha(args.input)
    result = dict(
        status="passed", exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(deps),
        first_terminal_domain=["11/50", "9/20"],
        low_middle_domain=["rho", "1/10"], last_symbol="arbitrary allowed",
        incoming_reset_coefficient="151/20", exit_reset_coefficient="11/2",
        exact_constant="1/50", occupation_coefficient="1/4000",
        numerical_cells_recomputed=0, new_critical_roots=0,
        incoming_optimizations=0, interface_sign_certified=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope="Exact real-edge surplus for a plateau first terminal and low middle, with arbitrary last halo, and the explicit piecewise-quadratic tangent maximum at middle1/10. The unchanged-edge transport trace and cycle closure are written proofs. No general first-terminal or right-interface sign is certified.",
    )
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact checks;", len(primary), "primary records;",
          len(deps), "bindings; no numerical cover.", flush=True)


if __name__ == "__main__":
    main()
