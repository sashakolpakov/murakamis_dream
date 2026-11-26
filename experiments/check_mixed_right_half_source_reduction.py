#!/usr/bin/env python3
"""Exact algebra and scalar margins for the full-source right-half reduction.

This does not check a geometric supporting-plane gap or the analytic
Riemann-sum/maximum-principle arguments in the proof.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_right_half_source_reduction.md'
DEPS = [
    'notes/research_mixed_fourier_weight_continuation.md',
    'notes/research_mixed_boundary_strip_bounds.md',
    'notes/research_mixed_conditional_torus_composition.md',
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=192)
    parser.add_argument('--output', type=Path, default=ROOT / 'repro/results/research-mixed-right-half-source-reduction.json')
    args = parser.parse_args()
    ctx.prec = args.precision
    before = {p: sha(ROOT / p) for p in DEPS}
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    checks = []

    def exact(name, expr):
        assert s.cancel(expr) == 0, name
        checks.append(name)

    R, c, t, C, S, d = s.symbols('R c t C S d', real=True)
    D0 = 1 + R**2 - 2*R*c
    D1 = 1 + R**2 - 2*R*(c*C-t*S)
    H = (1+R**2)/(2*R)
    exact('squared modulus and cosh form', D0-2*R*(H-c))
    exact('stationary trigonometric equation',
          D1-d*D0-2*R*((1-d)*H-(C-d)*c+S*t))
    exact('reciprocal radius modulus', D0-R**2*(1+R**-2-2*c/R))
    exact('unweighted derivative sign numerator', D1-D0-2*R*((1-C)*c+S*t))
    exact('half-period modulus comparison',
          (1+R**2+2*R*c)-(1+R**2-2*R*c)-4*R*c)
    exact('zero/full-length constant angular derivative',
          (D1-D0).subs({C: 1, S: 0}))

    A, B, K, z = s.symbols('A B K z', real=True)
    norm = A*A+B*B
    discriminant = norm-K*K
    for sign in (-1, 1):
        cc = (A*K-sign*B*z)/norm
        ss = (B*K+sign*A*z)/norm
        exact(f'candidate linear equation {sign}', A*cc+B*ss-K)
        num = s.together(cc*cc+ss*ss-1).as_numer_denom()[0]
        rem = s.rem(s.Poly(num, z), s.Poly(z*z-discriminant, z)).as_expr()
        exact(f'candidate unit-circle equation {sign}', rem)

    X = s.symbols('X')
    for N in range(2, 13):
        exact(f'forcing polynomial N={N}',
              (1-X)*sum(X**j for j in range(N))-(1-X**N))
    margins = {
        'all current negative heights lie below 3/50': s.Rational(3, 50)-s.Rational(57, 1000),
        'positive alias height lies below 3/50': s.Rational(3, 50)-s.Rational(7, 500),
        '2pi H below 2/5 using pi<22/7': s.Rational(2, 5)-2*s.Rational(22, 7)*s.Rational(3, 50),
        'geometric exponential majorant below two': 2-1/(1-s.Rational(2, 5)),
    }
    assert all(v > 0 for v in margins.values())
    # exp(t) <= sum t^j = 1/(1-t) for 0<=t<1, so the last
    # two strict rational margins imply exp(2pi*3/50)<2.
    u = s.symbols('u')
    a = s.Rational(197, 20)
    D = s.Rational(1, 5)-a*u*u/2-a*a*u**4/12
    polynomials = [
        ('short-row tangent bound', 3*(s.Rational(1, 5)-u)**2-D*(s.Rational(1, 2)-u), s.Rational(0), s.Rational(21, 1000)),
        ('short-row curvature bound', 6*a*u*(s.Rational(1, 5)-u)**2-D*D, s.Rational(21, 1000), s.Rational(49, 250)),
    ]
    sturm = []
    for name, poly, lo, hi in polynomials:
        poly = s.Poly(poly, u)
        assert poly.count_roots(lo, hi) == 0
        assert poly.eval(lo) > 0 and poly.eval(hi) > 0
        sturm.append({'name': name, 'interval': [str(lo), str(hi)], 'roots': 0,
                      'left_value': str(poly.eval(lo)), 'right_value': str(poly.eval(hi))})
    assert D.subs(u, s.Rational(49, 250)) < 0
    P = arb.pi()
    radius = (-arb(57)*P/500).exp()
    derivative = (2*(P/5).cos()).log()+(1+radius**2-2*radius*(7*P/5).cos()).log()/2-3*(2*(P/5).sin()).log()-P/25
    analytic_margins = {
        'pi squared exceeds 197/20': P*P-arb(197)/20,
        'pi exceeds three': P-3,
        'no extra right candidate above row 1/5': -arb(1)/5-(P/5).cos().log(),
        'core triangle criterion': radius-(13*P/50).cos(),
        'row derivative exceeds 19/100': derivative-arb(19)/100,
    }
    C = (arb(57)*P/500).cosh()
    for label, y in [('zero', arb(0)), ('13/100', arb(13)/100)]:
        ratio = ((C-(2*P*(y+arb(1)/10)).cos())/(C-(2*P*y).cos())).log()/2
        analytic_margins[f'small-angle ratio at {label} exceeds 9/20'] = ratio-arb(9)/20
    for label, h in [('negative', -arb(57)/1000), ('positive', arb(1)/50)]:
        rad = (2*P*h).exp()
        analytic_margins[f'small-angle modulus below one at {label} endpoint'] = 1-(1+rad*rad-2*rad*(13*P/50).cos())
    lowrow = arb(2).log()+2*(P/10).cos().log()-(2*(P/10).sin()).log()-P/25
    analytic_margins['small-row derivative exceeds 9/10'] = lowrow-arb(9)/10
    pi_symbol = s.symbols('pi_symbol')
    exact('small-angle candidate absorption',
          s.Rational(9, 10)*(s.Rational(1, 10)-u)+pi_symbol/100
          -3*(s.Rational(1, 5)-u)**2-(pi_symbol-3)/100
          -3*u*(s.Rational(1, 10)-u))
    assert all(v > 0 for v in analytic_margins.values())
    assert before == {p: sha(ROOT / p) for p in DEPS}
    assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
    record = {
        'status': 'passed',
        'scope': 'Elementary polynomial identities, exact Sturm signs, and scalar height/core margins; no geometric supporting-plane gap or analytic full-source proof is computationally certified.',
        'exact_identities': len(checks),
        'identity_names': checks,
        'strict_rational_margins': {k: str(v) for k, v in margins.items()},
        'exact_sturm_checks': sturm,
        'negative_upper_row_polynomial_value': str(D.subs(u, s.Rational(49, 250))),
        'precision_bits': args.precision,
        'strict_outward_margins': {k: str(v) for k, v in analytic_margins.items()},
        'proof_sha256': proof_hash,
        'script_sha256': script_hash,
        'dependencies_sha256': before,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(f'PASS {len(checks)} exact identities, {len(margins)} rational margins, {len(sturm)} exact Sturm checks, {len(analytic_margins)} outward margins; no supporting-plane gap claimed')


if __name__ == '__main__':
    main()
