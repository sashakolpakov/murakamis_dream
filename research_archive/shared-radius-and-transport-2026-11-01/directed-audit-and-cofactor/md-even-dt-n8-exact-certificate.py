#!/usr/bin/env python3
"""Exact N=8 all-real-face discriminants; no root sampling or floats.

The analytic implication from a nonvanishing discriminant and one
all-real base point is explained in the companion note. This finite
check does not assert an all-level stability theorem.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path,
                    default=Path(__file__).with_suffix('.json'))
    args = ap.parse_args()
    b, A, B = S.symbols('b A B')
    r = S.sqrt(2)
    u = S.sqrt(2 + r)
    w = r * u
    v = u**3 - 3*u
    field = S.QQ.algebraic_field(u)
    p = (A*A - B*B)/4
    sine = [0, v, r, u, S.Integer(2)]
    diagonal = [2+u, 2+v, 2-v, 2-u]
    R = [S.Poly(1, b, A, B, domain=field)]
    prefix = field.one
    for j in range(1, 5):
        prefix *= field.from_sympy(diagonal[j-1])
        value = S.Poly(field.to_sympy(prefix)*b**j, b, A, B,
                       domain=field)
        value += S.Poly(sine[j]**2*A, b, A, B, domain=field)*R[-1]
        if j >= 2:
            value += S.Poly(sine[j]*sine[j-1]*diagonal[j-1]*p,
                            b, A, B, domain=field)*R[-2]
        R.append(value)

    # Rows are coefficients in the exact basis 1, sqrt(2), u, sqrt(2)*u.
    certificate = {
        3: [
            [536, 448, 374, 190],
            [2162, 1665, 1206, 894],
            [1300, 1230, 562, 778],
            [354, 305, 162, 186],
        ],
        4: [
            [375223552, 265705480, 202764800, 143972688],
            [1973513088, 1397423840, 1066621536, 756964704],
            [727401568, 517412200, 391233312, 280823152],
            [104318848, 75412736, 54817728, 40985152],
            [766272, 828248, 46144, 423728],
            [24064, 14880, -12320, -5536],
            [1120, 312, -864, 16],
        ],
    }
    intervals = [(F(1), F(1)), (F(707,500), F(283,200)),
                 (F(1847,1000), F(231,125)),
                 (F(2613,1000), F(1307,500))]
    rl, rh = intervals[1]
    ul, uh = intervals[2]
    wl, wh = intervals[3]
    assert rl*rl < 2 < rh*rh
    assert ul*ul < 2+rl and 2+rh < uh*uh
    assert wl*wl < 4+2*rl and 4+2*rh < wh*wh

    reports = []
    for j, rows in certificate.items():
        degree = j*(j-1)
        target = sum(
            sum(c*q for c,q in zip(row,[1,r,u,w]))
            * A**(degree-2*k)*B**(2*k)
            for k,row in enumerate(rows))
        assert R[j].discriminant() == S.Poly(target,A,B,domain=field)
        lower = []
        for row in rows:
            bound = sum(F(c)*(lo if c>=0 else hi)
                        for c,(lo,hi) in zip(row,intervals))
            assert bound > 0
            lower.append(str(bound))
        reports.append({'degree':j,'discriminant_basis_rows':rows,
                        'strict_rational_lower_bounds':lower})

    # At A=0,B=1 the cubic is b*(a*b^2-c), a,c>0 by its path factors.
    cubic = S.Poly(R[3].as_expr().subs({A:0,B:1}),b,domain=field)
    assert cubic.coeff_monomial(1) == 0
    assert cubic.coeff_monomial(b*b) == 0
    ca = S.Poly(field.to_sympy(field.from_sympy(
        diagonal[0]*diagonal[1]*diagonal[2])), b, domain=field)
    assert field.from_sympy(cubic.coeff_monomial(b**3)) == ca.rep.nth(0)
    assert field.from_sympy(cubic.coeff_monomial(b)) == field.from_sympy(
        -sine[3]*sine[2]*diagonal[2]*diagonal[0]/4)

    quartic = S.Poly(R[4].as_expr().subs({A:0,B:1}),b,domain=field)
    beta = 1-r-2*u+w
    gamma = 1-r/4-u+w/2
    assert quartic == S.Poly(2*b**4+beta*b*b+gamma,b,domain=field)
    assert field.from_sympy(beta*beta-8*gamma) == field.from_sympy(2*w-2*r-1)
    assert 1-rl-2*ul+wh < 0
    assert 1-rh/4-uh+wl/2 > 0
    assert 2*wl-2*rh-1 > 0

    output = {
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'level':8,
        'arithmetic':'exact rational and real algebraic number field; no floats',
        'original_recurrence':True,
        'discriminants':reports,
        'base_point':{'A':0,'B':1,'cubic_real_simple_roots':True,
                      'quartic_real_simple_roots':True},
        'scope':'Exact all-real-face hyperbolicity at N=8 after the connectedness argument. Not an all-N or source-rate theorem.',
    }
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(args.output)


if __name__ == '__main__':
    main()
