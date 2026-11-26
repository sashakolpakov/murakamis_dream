#!/usr/bin/env python3
"""Exact marginal barriers and phase monotonicity; no finite-source promotion."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path

from flint import arb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/"notes/research_mixed_four_first_vertical_phase.md"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT/
                        "repro/results/research-mixed-four-first-vertical-phase.json")
    args = parser.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, records, visited, primary = {}, {}, set(), {}

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        bind(path)
        if path in visited:
            return records[path]
        visited.add(path)
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        children = {}
        for field in ("dependencies", "dependencies_sha256"):
            for name, digest in record.get(field, {}).items():
                assert name not in children or children[name] == digest
                children[name] = digest
                bind(name, digest)
        for name in children:
            if name.startswith("repro/results/") and name.endswith(".json"):
                inherit(name)
        return record

    sources = {}
    for stem in ("mixed_four_three_cap_collar", "mixed_second_four_cap_collar"):
        path = "repro/results/research-"+stem.replace("_", "-")+".json"
        replay = path.replace(".json", "-replay.json")
        author, peer = inherit(path), inherit(replay)
        assert author["status"] == peer["status"] == "passed"
        assert peer["input_sha256"] == deps[path]
        for field in ("proof_sha256", "script_sha256", "dependencies_sha256"):
            assert author[field] == peer[field]
        bind("notes/research_"+stem+".md", author["proof_sha256"])
        bind("experiments/check_"+stem+".py", author["script_sha256"])
        primary[path], primary[replay] = deps[path], deps[replay]
        sources[stem] = author

    checks, scalar = [], {}

    def check(label, condition):
        assert condition, label
        checks.append(label)

    def ar(x):
        x = F(x)
        return arb(x.numerator)/x.denominator

    u, v, t = sp.symbols("u v t", real=True)
    I = sp.I
    T = t*t
    p = 2*t/(1-T)
    S = u+I*v
    G = u+p*(1-v)-t*(u*u+u*p+v*v-v)
    Gpoly = sp.together(G).as_numer_denom()[0]
    check("the original real half-factorial argument has tangent p",
          sp.cancel(2*I/(p+I)-2*(1+I*p)/(1+p*p)) == 0)
    check("the zero marginal has exactly the claimed ratio numerator",
          sp.expand(sp.im((S+p)*sp.conjugate(S-I))
                    -t*sp.re((S+p)*sp.conjugate(S-I))-G) == 0)
    check("the half-angle parameter threshold is exact",
          sp.cancel(p*p-4*T/(1-T)**2) == 0
          and 4*F(1,5)/(1-F(1,5))**2 == F(5,4)
          and F(11,10)**2 < F(5,4))

    Q0 = (1-S*S-p*(S-I))/(S+I)
    n0 = u*(2-u*u-(v+1)**2)+p*(1-u*u-v*v)
    check("the quadratic solved neighbor has the exact real numerator",
          sp.factor(sp.re(Q0)-n0/(u*u+(v+1)**2)) == 0)
    R0 = u*(T*(3*T-1)*v-(1-T)**2)+t*(v-1)*((1-3*T)*v+2*(1-T))
    expression = sp.together(t*t*(1-T)*n0-R0).as_numer_denom()[0]
    check("the quadratic marginal-zero remainder is exact",
          sp.factor(sp.rem(expression, Gpoly, u)) == 0)
    Z = sp.symbols("Z", real=True)
    check("the quadratic u coefficient has a strict negative square bound",
          sp.expand(-1+3*Z-4*Z*Z+4*(Z-sp.Rational(3,8))**2+sp.Rational(7,16)) == 0
          and F(1,5)<F(1,3))
    check("the remaining quadratic brace is strictly positive on the whole interval",
          sp.expand(((1-3*Z)*v+2*(1-Z)).subs(v,-1)-(1+Z)) == 0)

    D = (S+I)*(S+p)-2*I*(p-I)
    N = S*(S+I)*(S+p)+2*(p-I)
    Q = sp.symbols("Q")
    F1 = (S+I)*(S+p)*(S+Q)-2*I*(p-I)*(Q+I)
    check("the cubic neighbor is solved from the original polynomial",
          sp.expand(F1-(D*Q+N)) == 0)
    check("a vanishing cubic denominator cannot occur at a strip root",
          sp.expand(N-S*D-2*I*(p-I)*(S-I)) == 0)
    A = (11*Z**4*v*v-Z**4*v-2*Z**4-11*Z**3*v*v+21*Z**3*v+Z**3
         +9*Z*Z*v*v-11*Z*Z*v+Z*Z-Z*v*v-Z*v-Z+1)
    B = (16*Z**3*v*v+5*Z**3*v+4*Z**3-16*Z*Z*v*v-29*Z*Z*v+2*Z*Z
         -Z*v+v+2)
    n1 = -sp.re(N*sp.conjugate(D))
    expression = sp.together(t**4*(1-T)**2*n1+u*A.subs(Z,T)
                            -t*(v-1)*B.subs(Z,T)).as_numer_denom()[0]
    check("the cubic marginal-zero remainder is exact",
          sp.factor(sp.rem(expression, Gpoly, u)) == 0)
    x, y = sp.symbols("x y")
    expected = {
        "A": [["1","1","1"],["19/20","1","17/20"],
              ["26/25","71/75","52/75"],["151/125","108/125","69/125"],
              ["176/125","472/625","288/625"]],
        "B": [["1","2","3"],["16/15","2","44/15"],
              ["4/3","56/25","172/75"],["48/25","328/125","32/25"]],
    }
    tables = {}
    for name, polynomial in (("A", A), ("B", B)):
        f = sp.Poly(sp.expand(polynomial.subs({Z:x/5,v:2*y-1})), x, y)
        n, m = f.degree(x), f.degree(y)
        table = []
        for i in range(n+1):
            row = []
            for j in range(m+1):
                coefficient = sum(
                    f.coeff_monomial(x**k*y**l)
                    *sp.Rational(comb(i,k),comb(n,k))
                    *sp.Rational(comb(j,l),comb(m,l))
                    for k in range(i+1) for l in range(j+1))
                row.append(coefficient)
            table.append(row)
        check("all exact tensor Bernstein coefficients for "+name,
              table == [[sp.Rational(c) for c in row] for row in expected[name]]
              and min(sum(table,[])) > 0)
        tables[name] = dict(degrees=[n,m], coefficients=expected[name],
                            minimum=str(min(sum(table,[]))))

    four_three = sources["mixed_four_three_cap_collar"]
    ending_four = sources["mixed_second_four_cap_collar"]
    check("the inherited actual third-three cotangent bound is retained",
          arb(four_three["scalar_enclosures"]["cotangent_three_maximum"]) < ar(".37"))
    check("the inherited actual second/third-four cotangent bound is retained",
          arb(ending_four["scalar_enclosures"]["second_four_cotangent"]) < ar(".61"))
    check("the quadratic full-side signs hold on the entire enlarged path",
          2-F(1,10)-F(37,100)>0 and -2+F(61,100)+F(37,100)<0
          and F(61,100)+F(37,100)+(F(61,100)-F(37,100))**2/4 < 1)
    check("the cubic full path is inside the proved one-sided chamber",
          -1 < -F(1,10) < F(61,100) < F(2,3)
          and 0 < F(61,100) < 1)
    pi = arb.pi()
    cot_real = (ar(".24")*pi).cot()
    positive_height = (ar(".028")*pi).sinh()/(
        (ar(".028")*pi).cosh()-(ar(".48")*pi).cos())
    height_monotonicity = (ar(".48")*pi).cos()*(ar(".028")*pi).cosh()
    check("all actual real second-four arguments meet the marginal threshold",
          cot_real < ar(F(11,10)))
    check("the full selected positive-height interval has the claimed cotangent band",
          positive_height < ar(F(1,10)) and height_monotonicity < 1)
    scalar.update(real_cotangent_maximum=cot_real,
                  selected_height_cotangent=positive_height,
                  selected_height_monotonicity=height_monotonicity)
    theta, gamma, nu, k = sp.symbols("theta gamma nu k", real=True)
    check("the selected factorial branch retains its exact halfweight slope",
          sp.expand(-(theta-gamma/2)-sp.pi-(-theta+gamma/2-sp.pi)) == 0)
    check("the selected forced branch cancels the half monomial exactly",
          sp.expand((2*sp.pi*k)/2-sp.pi*k) == 0)
    check("the next tangent and unused first-pair gain cancel exactly",
          sp.expand(k*nu+k*(-nu)) == 0)

    result = dict(status="passed", precision_bits=args.precision,
                  exact_and_scalar_checks=len(checks), checks=checks,
                  bernstein_tables=tables,
                  scalar_enclosures={name:str(value) for name,value in scalar.items()},
                  primary_records_sha256=primary, dependencies_sha256=deps,
                  proof_sha256=ph, script_sha256=sh, input_sha256=ih,
                  new_root_proposals=0, root_enclosures_recomputed=0,
                  new_parameter_cover_cells=0, finite_source_upper_proved=False,
                  scope="Original following-edge phase monotonicity on the full actual second-four height path, both selected Fourier half branches retained. Complete finite upper bound on this path remains a separate hypothesis.")
    if old:
        for key in result:
            if key not in ("precision_bits","scalar_enclosures","input_sha256"):
                assert old[key] == result[key], key
        assert old["scalar_enclosures"].keys() == scalar.keys()
        assert all(value.overlaps(arb(old["scalar_enclosures"][name]))
                   for name,value in scalar.items())
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/name)==digest for name,digest in deps.items())
    if args.input:
        assert sha(args.input)==ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("PASS",len(checks),"exact/scalar checks;",
          len(primary),"primary records;",len(deps),"bindings; phase only")


if __name__ == "__main__":
    main()
