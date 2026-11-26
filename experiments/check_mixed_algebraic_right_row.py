#!/usr/bin/env python3
"""Exact polynomial/quarter-row deduction for the original raw envelope.

No numerical root, parameter cover, or finite-sum lower bound is computed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_algebraic_right_row.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path, default=ROOT /
                    "repro/results/research-mixed-algebraic-right-row.json")
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    input_hash = None
    previous = None
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        previous = json.loads(raw)

    dependencies, visited, primary, replays = {}, set(), {}, {}

    def bind(path, expected=None):
        digest = sha(ROOT / path)
        if expected is not None:
            assert digest == expected, path
        assert path not in dependencies or dependencies[path] == digest, path
        dependencies[path] = digest
        return digest

    def inherit(path):
        bind(path)
        data = json.loads((ROOT / path).read_text())
        if path in visited:
            return data
        visited.add(path)
        inherited = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in data.get(field, {}).items():
                assert name not in inherited or inherited[name] == digest, name
                inherited[name] = digest
                bind(name, digest)
        for name in inherited:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return data

    for stem in ("mixed_complex_right_row_reduction",
                 "mixed_right_boundary_row_bracket",
                 "mixed_raw_row_stationarity"):
        name = "repro/results/research-" + stem.replace("_", "-") + ".json"
        data = inherit(name)
        assert data["status"] == "passed", name
        assert data["proof_sha256"] == bind("notes/research_" + stem + ".md")
        assert data["script_sha256"] == bind("experiments/check_" + stem + ".py")
        primary[stem] = data
        replay_name = name[:-5] + "-replay.json"
        replay = inherit(replay_name)
        assert replay["status"] == "passed", replay_name
        assert replay["proof_sha256"] == data["proof_sha256"], replay_name
        assert replay["script_sha256"] == data["script_sha256"], replay_name
        if "input_sha256" in replay:
            assert replay["input_sha256"] == dependencies[name], replay_name
        replays[stem] = replay
    for name in ("notes/research_mixed_angular_support_candidates.md",
                 "notes/research_mixed_two_right_source_bound.md"):
        bind(name)

    exact, rational = [], []

    def zero(name, expression):
        assert sp.cancel(sp.expand(expression)) == 0, (name, expression)
        exact.append(name)

    def check(name, condition):
        assert condition, name
        rational.append(name)

    r, A, B, L, w = sp.symbols("r A B L w", real=True)
    P = 1 + r*r - 2*r*A
    Q = 4*r*B
    R = 1 + r*r + 2*r*A
    base = P + Q*w + R*w*w
    cosine, sine = (1-w*w)/(1+w*w), 2*w/(1+w*w)
    shifted_modulus = 1+r*r-2*r*(A*cosine-B*sine)
    zero("shifted modulus under the row tangent substitution",
         shifted_modulus-base/(1+w*w))
    zero("nonnegative P decomposition", P-((1-r)**2+2*r*(1-A)))
    zero("nonnegative R decomposition", R-((1-r)**2+2*r*(1+A)))
    zero("strict nonzero coefficient sum", P+R-2*(1+r*r))

    polynomials, coefficients = {}, {}
    for eps in (0, 1):
        degree, leading = 4+2*eps, sp.Integer(4)**(1+eps)
        numerator = sp.expand(base*(1+w*w)**eps)
        polynomial = sp.expand(leading*w**degree-L*numerator)
        squared_exponential = (L*(4/(1+w*w))*shifted_modulus /
                               (4*w*w/(1+w*w))**(2+eps))
        zero("squared original row derivative eps=" + str(eps),
             squared_exponential-L*numerator/(leading*w**degree))
        zero("stationary polynomial eps=" + str(eps),
             leading*w**degree*(1-squared_exponential)-polynomial)
        expected = [P, Q, R] if eps == 0 else [P, Q, P+R, Q, R]
        actual = [sp.Poly(numerator, w).coeff_monomial(w**j)
                  for j in range(degree-1)]
        for j, (a, b) in enumerate(zip(actual, expected)):
            zero("nonnegative coefficient eps=%d j=%d" % (eps, j), a-b)
        check("degree and leading coefficient eps=" + str(eps),
              sp.degree(polynomial, w) == degree and
              sp.Poly(polynomial, w).LC() == leading)
        check("all divided powers strictly decrease eps=" + str(eps),
              all(j-degree <= -2 for j in range(len(actual))))
        divided = numerator/w**degree
        derivative = -sum((degree-j)*a*w**(j-degree-1)
                          for j, a in enumerate(actual))
        zero("divided equation derivative eps=" + str(eps),
             sp.diff(divided, w)-derivative)
        zero("root derivative identity eps=" + str(eps),
             sp.diff(polynomial, w) -
             (degree*polynomial/w-L*w**degree*sp.diff(divided, w)))
        zero("quarter polynomial sign eps=" + str(eps),
             polynomial.subs(w, 1) -
             2**(1+eps)*(2**(1+eps)-L*(1+r*r+2*r*B)))
        zero("quarter squared derivative eps=" + str(eps),
             squared_exponential.subs(w, 1) -
             L*(1+r*r+2*r*B)/2**(1+eps))
        polynomials[str(eps)] = str(polynomial)
        coefficients[str(eps)] = [str(sp.factor(a)) for a in actual]

    N0 = 1+r*r+2*r*B
    zero("type-four L=1 quarter nonnegative deficit",
         4-N0-((1-r)*(3+r)+2*r*(1-B)))
    zero("type-three L=r^-2 quarter nonnegative excess",
         N0-2*r*r-((1-r)*(1+r)+2*r*B))
    zero("remaining type-three quarter threshold",
         N0-2-2*r*(B-(1/r-r)/2))
    zero("remaining type-four quarter threshold",
         r*r*(N0/(r*r)-4)-(1+2*r*B-3*r*r))
    zero("type-four quarter tie r=1 B=1", (4-N0).subs({r: 1, B: 1}))
    zero("type-three quarter tie r=1 B=0",
         (N0-2*r*r).subs({r: 1, B: 0}))

    # Explicit limiting polynomials: the zero w=0 is never in the
    # positive tangent domain. These also recover the old real cases.
    F0 = 4*w**4-L*base
    F1 = 16*w**6-L*base*(1+w*w)
    zero("zero-angle zero-height quartic",
         F0.subs({r: 1, A: 1, B: 0, L: 1})-4*w*w*(w*w-1))
    zero("zero-angle zero-height sextic",
         F1.subs({r: 1, A: 1, B: 0, L: 1})-
         4*w*w*(4*w**4-w*w-1))
    zero("half-angle zero-height quartic",
         F0.subs({r: 1, A: -1, B: 0, L: 1})-4*(w**4-1))
    zero("half-angle zero-height sextic",
         F1.subs({r: 1, A: -1, B: 0, L: 1})-4*(4*w**6-w*w-1))
    v = sp.symbols("v", real=True)
    zero("old one-half type-four square-root polynomial",
         4*v**4-v*v*(1-v*v)-(1-v*v)**2-(4*v**4+v*v-1))
    zero("old two-half type-four cubic factorization",
         4*v**6-(1-v*v)**2-
         (2*v**3+v*v-1)*(2*v**3-v*v+1))

    height_cases = []
    for sign in (-1, 1):
        for d in (0, 1):
            # lambda/(2*pi*H), with h/H=sign and h_+/H=max(sign,0).
            power = max(sign, 0)-d*sign
            check("physical signed-height choice sign=%d d=%d" % (sign, d),
                  power in (0, 1))
            height_cases.append(dict(height_sign=sign, complex_target_first=d,
                                     lambda_over_2piH=power,
                                     L="r^-2" if power else "1"))
    whole = primary["mixed_complex_right_row_reduction"]
    check("literal signed-height table agrees with complete row source",
          [(c["height_sign"], c["complex_target_first"], c["lambda_over_2piH"])
           for c in height_cases] ==
          [(c["height_sign"], c["complex_target_first"], c["lambda_over_2piH"])
           for c in whole["height_cases"]])
    bracket = primary["mixed_right_boundary_row_bracket"]
    check("completed uniform open row bracket and radius input",
          bracket["row_interval"] == ["1/5", "2/5"] and
          F(bracket["maximum_absolute_height"]) == F(57, 1000) and
          bracket["exact_checks"] == 11 and bracket["scalar_comparisons"] == 3)
    stationarity = primary["mixed_raw_row_stationarity"]
    check("completed derivative endpoint theorem with all physical branches",
          stationarity["row_endpoints"] == ["1/5", "2/5"] and
          stationarity["physical_branch_count"] == 12 and
          stationarity["exact_identity_count"] == 41 and
          stationarity["rational_check_count"] == 26)
    check("completed independent derivative replay",
          replays["mixed_raw_row_stationarity"]["precision_bits"] == 384 and
          replays["mixed_raw_row_stationarity"]["physical_branches"] ==
          stationarity["physical_branches"])
    check("moving interval lies strictly inside the sine half-level interval",
          F(1, 12) < F(3, 25) < F(11, 50) < F(5, 12))
    check("strict radial sinh bound from the frozen r>2/3 input",
          (F(3, 2)-F(2, 3))/2 == F(5, 12) < F(1, 2))
    check("quarter refinement stays inside the old derivative bracket",
          F(1, 5) < F(1, 4) < F(2, 5))
    check("moving minimum excludes the type-four quarter equality angle",
          F(11, 50) < F(1, 4))

    if previous is not None:
        assert previous["status"] == "passed"
        assert previous["proof_sha256"] == ph and previous["script_sha256"] == sh
        assert previous["dependencies_sha256"] == dependencies
        assert previous["exact_identities"] == exact
        assert previous["rational_checks"] == rational
        assert previous["stationary_polynomials"] == polynomials
        assert previous["nonnegative_coefficients"] == coefficients
        assert previous["height_cases"] == height_cases
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT / path) == digest
               for path, digest in dependencies.items())
    if args.input:
        assert sha(args.input) == input_hash
    result = dict(
        status="passed", exact_identity_count=len(exact), exact_identities=exact,
        rational_check_count=len(rational), rational_checks=rational,
        stationary_polynomials=polynomials, nonnegative_coefficients=coefficients,
        height_cases=height_cases, polynomial_degrees=[4, 6],
        primary_records=len(primary), saved_replay_records=len(replays),
        current_bindings=len(dependencies), new_roots=0, new_parameter_cells=0,
        cyclic_word_enumerations=0, whole_flow_sign_certified=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope="Exact unique positive row root and quarter-row refinements for "
              "the original continuous absolute envelope. No finite-kernel "
              "lower bound, whole-flow sign, or full-period noncancellation.")
    if input_hash:
        result["input_sha256"] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS", len(exact), "exact identities;", len(rational),
          "rational/source checks;", len(primary), "primary;",
          len(replays), "saved replays;", len(dependencies), "bindings",
          flush=True)


if __name__ == "__main__":
    main()
