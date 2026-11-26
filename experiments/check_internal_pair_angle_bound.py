#!/usr/bin/env python3
"""Exact scalar identities in the internal-pair angle bound."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json

import sympy as s


def main():
    x, y = s.symbols("x y", real=True)
    identities = 0
    polynomial = 4*x**5-4*x**4+8*x**3-8*x**2+x+1
    coefficients = (
        (Q(1), Q(11,10), Q(1), Q(4,5), Q(11,20), Q(3,8)),
        (Q(3,8), Q(1,5), Q(1,10), Q(1,5), Q(7,10), Q(2)),
    )
    for low, row in zip((Q(0), Q(1,2)), coefficients):
        bernstein = sum(s.Rational(c.numerator, c.denominator)*comb(5,j)
                        *y**j*(1-y)**(5-j) for j,c in enumerate(row))
        assert s.expand(polynomial.subs(x, s.Rational(low.numerator, low.denominator)+y/2)
                        -bernstein) == 0
        assert min(row) > 0
        identities += 1

    # Equation (17), after X=sqrt(2)sinh(H/2).
    # Its real part is sqrt(1+X^2/2)*(4X-2X^2-1)/sqrt(2);
    # its imaginary part is X^3+3X/2-1.
    real_squared = (1+x*x/2)*(4*x-2*x*x-1)**2/2
    imaginary = x**3+3*x/2-1
    assert s.expand(s.Rational(1,2)-real_squared+imaginary**2-polynomial) == 0
    identities += 1

    # Correct rotated-sinh identity and the exact quadrant derivative
    # formulas. The earlier checker did not test this proof step.
    a, b, cw, sw, cg, sg = s.symbols("a b cw sw cg sg", real=True)
    relations = s.groebner(
        [b*b-a*a-1, cg*cg+sg*sg-1, cw*cw+sw*sw-1],
        b, cg, cw, a, sg, sw, domain=s.QQ)
    real = a*cw*cg-b*sw*sg
    imag = a*sw*cg+b*cw*sg
    corrected = ((cw*cw-sw*sw)*((a*a+b*b)*(cg*cg-sg*sg)-1)
                 -(2*cw*sw)*(2*a*b)*(2*cg*sg))/2
    real_derivative = -a*cw*sg-b*sw*cg
    imag_derivative = -a*sw*sg+b*cw*cg
    for expression in (
            real**2-imag**2-corrected,
            b*real_derivative+a*imag+sw*cg,
            b*imag_derivative-a*real-cw*cg,
            b*b*cw*cw+a*a*sw*sw-a*a-cw*cw):
        assert relations.reduce(s.expand(expression))[1] == 0
        identities += 1

    # A rational regression point distinguishes the corrected identity
    # from the erroneous expression that used cosh(2k) in both terms.
    old_expression = ((a*a+b*b)
                      *((cw*cw-sw*sw)*(cg*cg-sg*sg)-4*cw*sw*cg*sg)
                      -(cw*cw-sw*sw))/2
    regression = {a:s.Rational(3,4), b:s.Rational(5,4),
                  cw:s.Rational(4,5), sw:s.Rational(3,5),
                  cg:s.Rational(12,13), sg:s.Rational(5,13)}
    assert s.simplify((corrected-old_expression).subs(regression)) != 0

    # The original C_* formula itself remains valid: check its first
    # hyperbolic product before using the polynomial in X.
    ch, sh = s.symbols("ch sh", real=True)
    product = ((3*sh+4*sh**3-s.I*(4*ch**3-3*ch))*(ch+s.I*sh)
               -(4*sh*ch-s.I)*(ch**2+sh**2))
    hyperbolic_relation = s.groebner([ch**2-sh**2-1], ch, sh)
    for expression in (s.re(s.expand(product)), s.im(s.expand(product))):
        assert hyperbolic_relation.reduce(expression)[1] == 0
        identities += 1

    z, c = s.symbols("z c", positive=True)
    axis_value = z*(1+z)/(z+c)
    for expression in (
            s.diff(axis_value,z)-(z*z+2*c*z+c)/(z+c)**2,
            s.diff(axis_value,c)+z*(1+z)/(z+c)**2):
        assert s.simplify(expression) == 0
        identities += 1

    inequalities = (
        Q(4,7)>Q(9,16),          # sech H > (3/4)^2
        Q(51,83)>Q(23,40),
        Q(34,33)>1,
        Q(53,47)<Q(8,7),        # cosh(1/2) Taylor bound
        Q(24,29)<Q(7,8),        # sinh(3/4) Taylor bound
        Q(8,7)*Q(7,8)**2<1,
        Q(49,25)<2,
        Q(9,20)<Q(1,2),         # angle bound for n>=5
        4*Q(7,20)-2*Q(7,20)**2-1>0,
        4-2-1>0,
        Q(17,11)<2,            # cosh(1) <= 17/11
        Q(7,8)**2<2<Q(3,2)**2, # 1/2 < H_c < 1
    )
    assert all(inequalities)
    assert (Q(1,3)+Q(7,30))/(1-Q(1,3)*Q(7,30)) == Q(51,83)
    assert (Q(1,2)+Q(7,20))/(1-Q(1,2)*Q(7,20)) == Q(34,33)
    # log 2 = 2 sum_{j>=0} (1/3)^(2j+1)/(2j+1) > 2/3.
    assert Q(2,3)+Q(2,81)>Q(2,3)
    root = Path(__file__).resolve().parents[1]
    inputs = [Path(__file__).resolve(),
              root/"notes/research_internal_pair_angle_bound.md"]
    record = {
        "status":"passed",
        "exact_algebraic_identities":identities,
        "positive_Bernstein_rows":len(coefficients),
        "rational_comparisons":len(inequalities)+3,
        "incorrect_identity_regression_points":1,
        "scope":"The repaired integer-power angle theorem; no continuous-power extension is asserted.",
        "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in inputs},
    }
    output = root/"repro/results/research-internal-pair-angle-bound.json"
    output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({k:v for k,v in record.items() if k != "sha256"}))


if __name__ == "__main__":
    main()
