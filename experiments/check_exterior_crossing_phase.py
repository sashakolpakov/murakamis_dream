#!/usr/bin/env python3
"""Exact exterior-product and characteristic algebra, with local branch bounds.

The script does not select a contribution from the original finite cycle
or estimate complementary contours. The uniform interpolation proof is
written in the accompanying note.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from flint import acb, arb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=256)
    parser.add_argument("--output", type=Path, default=ROOT /
                        "repro/results/research-exterior-crossing-phase.json")
    args = parser.parse_args()
    ctx.prec = args.precision
    exact = []

    def identity(name, expression):
        assert sp.cancel(expression) == 0, name
        exact.append(name)

    A, r, X, Y, Z, U, V, W, h = sp.symbols("A r X Y Z U V W h")
    for length in range(8):
        original = sp.prod(1-A*r**j for j in range(length))
        inverted = (-A)**length*r**(length*(length-1)//2) * \
            sp.prod(1-A**-1*r**-j for j in range(length))
        identity(f"finite product inversion length {length}", original-inverted)
    identity("exterior recurrence multiplier", -Z*(1-Z**-1)-(1-Z))
    identity("exterior logarithmic derivative exponential",
             -Z*(1-Z**-1)-(1-Z))
    ss, tt, nn, lx, lz, ip = sp.symbols("s t N logX logZ ipi")
    numerator_exponent = nn*ss*lx+nn*tt*lz \
        +ip*nn*((ss+tt)-(ss+tt)**2)/2-ip*(ss+tt)/2
    denominator_exponent = nn*(tt+1/nn)*(lz+ip) \
        -ip*nn*(tt+1/nn)**2+ip*(tt+1/nn)
    periodic_exponent = nn*ss*lx-lz-ip \
        +ip*nn*(ss-tt-ss**2-2*ss*tt+tt**2)/2+ip*(tt-ss)/2
    identity("full exterior summand wire-period multiplier cancels",
             numerator_exponent-denominator_exponent-periodic_exponent)

    polynomial = X*Y*W**2+(X+Y)*W+1-X*Y
    zz = (1+Y*(W+1))/(1-Y)
    vv = -Y/(1+Y*W)
    uu = (1-X)/(1+X*(W+1))
    first = uu*(1-vv)-(X**-1-1)
    second = vv*(1-uu)-(zz**-1-1)
    identity("first critical equation modulo angular polynomial",
             first-(X-1)*polynomial /
             (X*(W*Y+1)*(W*X+X+1)))
    identity("second critical equation modulo angular polynomial",
             second-Y*(W+2)*polynomial /
             ((W*Y+1)*(W*X+X+1)*(W*Y+Y+1)))
    identity("third critical equation", vv-Y/(zz*(Y-1)+Y))
    identity("left characteristic derivative",
             (X*uu-1)/(uu*(1-X))+(X**2+W*X+1)/(X-1)**2)
    identity("right characteristic derivative",
             (Y-zz)/(1-Y)+(Y**2+W*Y+1)/(Y-1)**2)

    # Converse elimination retains its nonzero denominator.
    v_from_z = Y/(Z*(Y-1)+Y)
    u_from_z = 1-(Z**-1-1)/v_from_z
    identity("converse characteristic elimination",
             (u_from_z*(1-v_from_z)-(X**-1-1)).subs(Z, zz)
             +polynomial/(X*(W*Y+1)))
    k = Z/(Z+2)
    identity("diagonal index s equation", Z**-1*2-(k**-1-1))
    identity("diagonal index t equation", -(1-Z**-1)-(Z**-1-1))
    identity("diagonal intermediate equation", -1-k/(Z*(k-1)+k))
    identity("diagonal angular branch", 1-k**-1-(-1-k**-1-(1-k**-1)*Z))

    base = -h/(Z+1)
    calculated = sp.Matrix([
        [base-h*k/(Z-k), base, 0],
        [base, base+h*Z/(Z+1), h/(Z+1)],
        [0, h/(Z+1),
         -h/(Z-1)-h/(Z+1)+h*Z/(Z-1)-h*Z/(Z-k)],
    ])
    claimed = h/(Z+1)*sp.Matrix([[-2,-1,0],[-1,Z-1,1],[0,1,-2]])
    for row in range(3):
        for column in range(3):
            identity(f"Hessian entry {row},{column}",
                     calculated[row,column]-claimed[row,column])
    positive_matrix = sp.Matrix([[2,1,0],[1,2,-1],[0,-1,2]])
    lam = sp.symbols("lam")
    identity("real Hessian spectrum",
             positive_matrix.charpoly(lam).as_expr()
             -(lam-2)*((lam-2)**2-2))

    # Algebra in the continuation proof fixes the additive phase constant.
    alpha, beta, rho, eps = sp.symbols("alpha beta rho eps", real=True)
    cut_polynomial = rho**2+(alpha+sp.I*beta-1)*rho+(alpha+sp.I*beta)**2
    identity("angular cut imaginary equation",
             sp.im(cut_polynomial)-beta*(rho+2*alpha))
    identity("angular cut real equation",
             sp.re(cut_polynomial).subs(rho,-2*alpha)
             -(3*alpha**2+2*alpha-beta**2))
    identity("angular cut modulus",
             (alpha**2+beta**2).subs(beta**2,3*alpha**2+2*alpha)
             -2*alpha*(2*alpha+1))
    approach = -1+sp.Rational(3,5)*eps**2+sp.I*eps
    modulus_squared = sp.expand(approach*sp.conjugate(approach))
    identity("calibration path stays below unit radius",
             modulus_squared-(1-eps**2/5+9*eps**4/25))
    identity("calibration path stays outside inner circle",
             3*modulus_squared+2*sp.re(approach)-1
             -(3*eps**2/5+27*eps**4/25))
    ipi = sp.symbols("ipi")
    I_limit, Iout_limit = -ipi/8, 7*ipi/8
    F_limit = ipi/2+ipi/2-I_limit-Iout_limit
    chi_limit = ipi/8+ipi/2-I_limit-ipi
    identity("interior product endpoint value",
             -(sp.Rational(1,6)+sp.Rational(1,12))*ipi/2-I_limit)
    identity("exterior product endpoint value",
             ipi-ipi/4+(sp.Rational(1,6)+sp.Rational(1,12))*ipi/2-Iout_limit)
    identity("three-vertex endpoint phase", F_limit-ipi/4)
    identity("crossing endpoint phase", chi_limit+ipi/4)
    identity("full phase constant is zero", F_limit+chi_limit)

    reference_path = ROOT / "repro/results/research-three-four-source-interface.json"
    reference = json.loads(reference_path.read_text())
    assert reference["status"] == "passed"
    assert reference["script_sha256"] == sha256(
        (ROOT/"experiments/check_three_four_source_interface.py").read_bytes()).hexdigest()
    for path, expected in reference["dependencies_sha256"].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == expected, path

    def rational(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    real, imag = reference["root_certificate"]["center"]
    radius = rational(reference["root_certificate"]["complex_disk_radius"])
    a = acb(rational(real)+arb(0,radius), rational(imag)+arb(0,radius))
    B = a*a*(2*a-1)**2/(2*(a-1))
    pi, ii = arb.pi(), acb(0,1)
    x = (a*a*B/(a*a+B)).sqrt().asin()/pi
    angle4 = 2*B.sqrt().acos()
    K = (2*pi*ii*x).exp()
    Z0 = 2*K/(1-K)
    z = Z0.log()/(2*pi*ii)
    s, t = z, acb(rational("1/2"))
    w = s+t
    checks = []

    def positive(name, value):
        assert value > 0, (name, str(value))
        checks.append({"name":name, "strict_positive_margin":str(value)})

    for name, value, lower, upper in [
        ("intermediate real coordinate", z.real, ".284", ".285"),
        ("intermediate height", z.imag, "-.043", "-.042"),
        ("exterior parameter modulus", abs(Z0), "1.30", "1.31"),
    ]:
        positive(name+" lower", value-rational(lower))
        positive(name+" upper", rational(upper)-value)
    positive("inside original parameter disk", rational(".61")-abs(K))
    positive("inside first endpoint product disk", rational(".468")-abs(K/Z0))
    positive("inside inverse exterior product disk", rational(".77")-abs(1/Z0))
    positive("factorial strip lower", w.real)
    positive("factorial strip upper", 1-w.real)
    positive("moving-residue factorial strip lower", z.real)
    positive("moving-residue factorial strip upper", 1-z.real)
    positive("upper-half-plane exterior parameter", Z0.imag)

    # Use the actual marked logs, not logs of already simplified ratios.
    sine_log = (2*(pi*w).sin()).log()
    exterior_log = 2*pi*ii*z+pi*ii
    inside_s = (1-K*(-2*pi*ii*s).exp()).log()
    out_t = exterior_log-2*pi*ii*t+(1+(1/Z0)).log()
    fs = sine_log+pi*ii*(1-2*w)/2+2*pi*ii*x-inside_s
    ft = sine_log+pi*ii*(1-2*w)/2+2*pi*ii*z-out_t
    out_z = 2*pi*ii*t+(1-1/Z0).log()-(1+1/Z0).log()
    chi_z = (2*(pi*z).sin()).log()+pi*ii*(1-2*z)/2 \
        +2*pi*ii*x-(1-K/Z0).log()-pi*ii
    fz = 2*pi*ii*t-out_z+pi*ii+chi_z
    for name, gradient in [("s",fs),("t",ft),("z",fz)]:
        positive(name+" gradient lies in zero logarithmic strip",
                 pi-abs(gradient.imag))

    c = 2*pi*ii/(Z0+1)
    coercivity = c.real*(2-arb(2).sqrt())
    positive("strict Hessian bound exceeds 2.19", coercivity-rational("2.19"))
    angular_derivative = (pi*x+angle4/2).cos().log() + \
        (pi*x-angle4/2).cos().log()-2*(pi*x).sin().log()
    left = 2*pi*ii*s+(1-K/Z0).log()-(1-K).log()-pi*ii
    right = 2*pi*ii*z+(1-K/Z0).log()-(1-K).log()-pi*ii
    for name, value in [("left",left),("right",right)]:
        positive(name+" angular derivative has same logarithmic lift",
                 pi-abs((value-angular_derivative).imag))

    dependencies = [
        "notes/research_exterior_crossing_phase.md",
        "notes/research_root_pochhammer_interpolation.md",
        "notes/research_three_four_source_interface.md",
        "notes/research_crossing_cauchy_transport.md",
        "notes/research_traced_three_vertex_endpoint.md",
        "notes/exact_factorial_interpolation_and_complex_contours.md",
    ]
    result = {
        "status":"passed",
        "precision_bits":args.precision,
        "scope":"Exact product inversion, critical/characteristic/Hessian identities, endpoint phase-calibration arithmetic, and logarithmic branch/domain enclosures at the inherited validated reference. The analytic continuation argument is written in the note. No finite-cycle selection or complementary-contour estimate is certified.",
        "exact_identity_count":len(exact),
        "exact_identities":exact,
        "strict_comparison_count":len(checks),
        "comparisons":checks,
        "reference_values":{
            "K":str(K), "Z":str(Z0), "intermediate_wire":str(z),
            "gradient_s":str(fs), "gradient_t":str(ft), "gradient_z":str(fz),
            "coercivity_lower_bound":str(coercivity),
            "angular_gradient_difference":str(left-angular_derivative),
        },
        "inherited_reference":{
            "path":str(reference_path.relative_to(ROOT)),
            "sha256":sha256(reference_path.read_bytes()).hexdigest(),
            "script_and_all_dependency_hashes_verified":True,
        },
        "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependencies_sha256":{
            path:sha256((ROOT/path).read_bytes()).hexdigest()
            for path in dependencies
        },
    }
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({key:result[key] for key in
                    ["status","exact_identity_count","strict_comparison_count"]},indent=2))
    print("Hessian lower bound:",coercivity)


if __name__ == "__main__":
    main()
