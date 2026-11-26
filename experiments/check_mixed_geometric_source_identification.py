#!/usr/bin/env python3
"""Exact algebra for the written mixed-path critical-point identification.

No roots are proposed and no numerical domains are sampled. The written
continuation, segment and Hessian arguments remain essential proof inputs.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_geometric_source_identification.md"
INPUTS = [
    "notes/research_mixed_unit_cotangent_bounds.md",
    "notes/research_mixed_endpoint_cotangent_barrier.md",
    "notes/research_mixed_three_endpoint_pair_sum.md",
    "notes/research_mixed_cotangent_cone_injectivity.md",
    "notes/research_mixed_geometric_action_calibration.md",
    "notes/research_mixed_geometric_source_log_lifts.md",
    "notes/research_mixed_wire_before_inverse_leg.md",
    "notes/research_mixed_all_leg_half_plane.md",
    "notes/research_positive_path_fractional_charge_cube.md",
    "notes/research_positive_path_real_wire_order.md",
    "notes/research_mixed_unit_period_leg_elimination.md",
    "notes/research_mixed_open_word_critical_localization.md",
    "notes/research_mixed_open_word_hessian.md",
    "notes/research_mixed_open_local_gaussian.md",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-mixed-geometric-source-identification.json")
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    dependencies = {name: sha(ROOT/name) for name in INPUTS}
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    C, c = sp.symbols("C c", real=True)
    height = (C-1)*(1-c)/(C+c)**2
    check("outside wire height decreases with the cosine",
          sp.factor(sp.diff(height, c)+(C-1)*(C+2-c)/(C+c)**3) == 0)
    first = height.subs(c, -sp.Rational(3, 5))
    check("first outside rectangle has the stated derivative and maximum",
          sp.factor(sp.diff(first, C)-40*(7-5*C)/(5*C-3)**3) == 0
          and first.subs(C, sp.Rational(6, 5)) == sp.Rational(8, 9))
    second = height.subs(c, -sp.Rational(1, 2))
    check("second outside rectangle has an exact square remainder",
          sp.factor(sp.Rational(3, 4)-second
                    -3*(2*C-3)**2/(4*(2*C-1)**2)) == 0)
    h, P = sp.symbols("h P", real=True)
    check("outside cotangent lower barrier has a positive square remainder",
          sp.expand(2*h*h-h+sp.Rational(1, 2)
                    -2*(h-sp.Rational(1, 4))**2-sp.Rational(3, 8)) == 0)

    u, a, v, q, alpha = sp.symbols("u a v q alpha")
    cot1 = sp.I+alpha/(q+sp.I)
    cot2 = sp.I+(q*q+1-alpha)/(q+sp.I)
    check("shared cotangents retain the exact wire root",
          sp.factor(cot1+cot2-sp.I-q) == 0
          and sp.factor((cot1-sp.I)*(cot1+cot2)-alpha) == 0)
    check("type-three cotangent equation is the literal unit relation",
          sp.expand((u+a)*(u+v)-(a-sp.I)*(v+sp.I)
                    -(u*u+u*(a+v)+sp.I*(v-a)-1)) == 0)

    x, b, t = sp.symbols("x b t", real=True)
    uc, ac = x-sp.I, b+sp.I*t
    cc = (uc+sp.I)*(uc+ac)
    den = cc-2*sp.I*(ac-sp.I)
    num = -cc*uc-2*(ac-sp.I)
    sos = ((x*x+4)*(b*b+(t-4/(x*x+4))**2)
           +2*b*x*(x*x+2)+x**4*(x*x+3)/(x*x+4))
    check("type-four lower-boundary numerator is the exact positive sum of squares",
          sp.factor(-sp.re(num*sp.conjugate(den))-x*sos) == 0)
    y = sp.symbols("y", real=True)
    check("the upper imaginary boundary contradicts the cosine half-plane",
          sp.expand(sp.im((x+sp.I*y-sp.I)*(x+sp.I*y+b+sp.I*t))
                    -x*(2*y+t-1)-b*(y-1)) == 0)
    check("the first ratio margin at real cotangent at least two",
          sp.expand((x+b)**2+(y+t)**2-b*b-(t-1)**2
                    -(x*x-4+2*x*b+(y-1)**2)-2*(y+1)*(t+1)) == 0)
    check("the second ratio margin at real cotangent at least two",
          sp.expand((x+b)**2+(y+t)**2-b*b-(t+1)**2
                    -(x*x-4+2*x*b+(y+1)**2)-2*(y-1)*(t-1)) == 0)
    angle = sp.atan((1-y)/P)+sp.atan((1+y)/P)
    check("the leg argument sum decreases toward either boundary of the cone",
          sp.factor(sp.diff(angle, y)
                    +4*P*y/((P*P+(1-y)**2)*(P*P+(1+y)**2))) == 0)
    check("the geometric height constant fits the required source visibility bound",
          153**2-3*88**2 == 177 and sp.Rational(22, 175) < sp.Rational(2, 15))

    k = sp.symbols("k", real=True)
    r = P+sp.I*k
    qq = r-sp.I
    pp = qq-1/r
    vv = -qq*qq/(pp+sp.I)-sp.I
    D = sp.expand(sp.re((r*r-1)*sp.conjugate(r*r-1)))
    check("type-three endpoint cotangent addition identity",
          sp.factor((pp*vv-1)/(pp+vv)-(r**3-r-sp.I)) == 0)
    check("type-three endpoint private real part",
          sp.factor(sp.re(pp)-P*(1-1/(P*P+k*k))) == 0)
    check("type-three endpoint opposite real part",
          sp.factor(sp.re(vv)*D-P*(4*k*(1-k)-(P*P+k*k-1)**2)) == 0)
    T = sp.symbols("T", real=True)
    f = -k*T*T+(2+2*k-2*k**3)*T-k**5-2*k**3-2*k*k-k-2
    check("type-three endpoint upper cone numerator",
          sp.factor((sp.im(vv)-1)*D-f.subs(T, P*P)) == 0)
    check("type-three endpoint threshold sign and derivative",
          sp.factor(f.subs(T, 1+3*k*k)+4*k*k*(2*k-1)*(2*k*k+k+1)) == 0
          and sp.expand(sp.diff(f, T)-2*(1+k-k**3-k*T)) == 0)

    xx, yy, ww = sp.symbols("xx yy ww", real=True)
    pp, qq = P+sp.I*yy, b+sp.I*ww
    re_cot_sum = sp.simplify(sp.re((pp*qq-1)/(pp+qq)))
    cot_den = (P+b)**2+(yy+ww)**2
    check("the pair Hessian determinant is exactly the cone expression",
          sp.factor((P*b-re_cot_sum*(P+b))*cot_den
                    -((P+b)**2-(P*ww-b*yy)**2)) == 0)
    fun = -sp.log(sp.cos(2*sp.pi*xx))/(2*sp.pi)
    support = fun+sp.diff(fun, xx)*(sp.Rational(23, 100)-xx)
    check("the tangent support to the cone boundary is increasing on the required interval",
          sp.simplify(sp.diff(support, xx)
                      -2*sp.pi*(sp.Rational(23, 100)-xx)/sp.cos(2*sp.pi*xx)**2) == 0)
    check("the leftmost tangent strictly dominates all source heights",
          sp.Rational(23, 100)-sp.Rational(1, 8) == sp.Rational(21, 200)
          and sp.Rational(1, 32)+sp.Rational(21, 200) > sp.Rational(3, 25))
    check("source endpoint sums satisfy the retained linear conditions",
          sp.Rational(33, 100)+sp.Rational(23, 100) > sp.Rational(1, 2)
          and 2*sp.Rational(33, 100) > sp.Rational(1, 2))

    result = dict(status="passed", arithmetic="exact symbolic and rational",
        exact_check_count=len(checks), checks=checks,
        proof_sha256=ph, script_sha256=sh, input_sha256=ih,
        dependencies_sha256=dependencies, new_root_proposals=0,
        numerical_parameter_cells=0,
        scope="Exact algebra supporting the written unit cotangent bounds, endpoint sums, segment argument and geometric/source critical-point equality. No whole finite-sum or finite-exception conclusion.")
    if old is not None:
        expected = dict(result)
        expected["input_sha256"] = old.get("input_sha256")
        assert old == expected
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(checks), "exact checks;", len(dependencies), "written inputs")


if __name__ == "__main__":
    main()
