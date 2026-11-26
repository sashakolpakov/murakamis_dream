#!/usr/bin/env python3
"""Exact/outward checks for the conditional-image contour reductions.

This checks one genuine two-leg-image obstruction, not a whole-image
packet or a cyclic-source lower bound. Numerical roots only propose the
center of an outward complex Newton self-map.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_conditional_image_contours.md'


def sha(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-conditional-image-contours.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    mp.mp.dps = 85
    pi, ii = arb.pi(), acb(0, 1)

    def ar(x):
        x = Q(x)
        return arb(x.numerator) / x.denominator

    def point(z):
        return acb(ar(mp.nstr(mp.re(z), 80)), ar(mp.nstr(mp.im(z), 80)))

    checks = []

    def positive(name, margin):
        assert margin > 0, (name, str(margin))
        checks.append({'name': name, 'strict_margin': str(margin)})

    C = lambda x, y: (2*pi*x).sin()/((2*pi*y).cosh()-(2*pi*x).cos())
    cmin = min(C(ar('3/20'), ar('1/5')), C(ar('27/100'), ar('1/5')))
    positive('central left curvature exceeds one eighth',
             2*pi*(cmin-(19*pi/50).cot())-ar('1/8'))
    positive('central right curvature exceeds one eighth',
             2*pi*C(ar('49/100'), ar('1/5'))-ar('1/8'))
    positive('left sine ratio at shift .23 exceeds two',
             (19*pi/50).sin()-2*(3*pi/20).sin())
    positive('left sine ratio at shift .45 exceeds two',
             (3*pi/5).sin()-2*(3*pi/20).sin())
    positive('type-four extra left factor is favorable', 1-2*(3*pi/20).sin())
    positive('whole left-tail logarithmic slope exceeds one half',
             ar(4).log()-6*pi/25-ar('1/2'))

    exact = []
    w, cr, ci, dr, di = sp.symbols('w cr ci dr di', real=True)
    squared = (cr-w*dr)**2+(ci-w*di)**2
    assert sp.expand(sp.diff(squared, w)-2*((dr**2+di**2)*w-cr*dr-ci*di)) == 0
    exact.append('quadratic modulus derivative and unique vertex')
    s, a, b, epsilon = sp.symbols('s a b epsilon')
    phi = lambda z: sp.pi*(z-z*z)/2
    assert sp.expand(phi(s+a)+phi(s+b)-(2+epsilon)*phi(s)+2*sp.pi*a*s
                     -phi(a)-phi(b)-sp.pi*s*(a-b)
                     -epsilon*sp.pi*(s*s-s)/2) == 0
    exact.append('original quadratic phase including type-four term')

    # Original root products are checked in exact cyclotomic fields.
    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    A = sp.Symbol('A')
    for n, q in ((2, sp.I), (3, (1+sp.I*sp.sqrt(3))/2),
                 (4, (1+sp.I)/sp.sqrt(2)), (6, (sp.sqrt(3)+sp.I)/2)):
        r = field.from_sympy(q)**-2
        coefficients = [field.one]
        P = field.one
        for j in range(1, n):
            P *= 1-r**j
            nxt = [field.zero]*(len(coefficients)+1)
            for k, v in enumerate(coefficients):
                nxt[k] += v
                nxt[k+1] -= v*r**j
            coefficients = nxt
        assert P == field.from_sympy(sp.Integer(n))
        exact.append(f'N{n} original P_(N-1)=N')
        assert all(v == field.one for v in coefficients)
        exact.append(f'N{n} last product equals (1-A^N)/(1-A)')

    aa = mp.mpc('0.3131', '-0.1146')
    bb = mp.mpc('0.4028', '-0.0828')

    def mp_log(z):
        return mp.log(1-mp.exp(-2j*mp.pi*z))

    def mp_eq(s, t):
        return (mp_log(s+t)+mp_log(s+aa)-2*mp_log(s)+2j*mp.pi*aa,
                mp_log(s+t)+mp_log(t+bb)-2*mp_log(t)+2j*mp.pi*bb)

    root = mp.findroot(mp_eq, (mp.mpc('.405812', '.020538'),
                              mp.mpc('.337758', '.017916')),
                       tol=mp.mpf('1e-78'), maxsteps=30)
    zz = [point(root[j]) for j in (0, 1)]
    aa = acb(ar('3131/10000'), -ar('1146/10000'))
    bb = acb(ar('4028/10000'), -ar('828/10000'))
    gp = lambda z: (1-(-2*pi*ii*z).exp()).log()

    def equations(z):
        s, t = z
        return [gp(s+t)+gp(s+aa)-2*gp(s)+2*pi*ii*aa,
                gp(s+t)+gp(t+bb)-2*gp(t)+2*pi*ii*bb]

    def jacobian(z):
        s, t = z
        off = pi*(pi*(s+t)).cot()-pi*ii
        return [[off+pi*(pi*(s+aa)).cot()-2*pi*(pi*s).cot()+pi*ii, off],
                [off, off+pi*(pi*(t+bb)).cot()-2*pi*(pi*t).cot()+pi*ii]]

    J = jacobian(zz)
    det = J[0][0]*J[1][1]-J[0][1]*J[1][0]
    Y = [[J[1][1]/det, -J[0][1]/det], [-J[1][0]/det, J[0][0]/det]]
    radius = ar('1e-30')
    box = [z+acb(arb(0, radius), arb(0, radius)) for z in zz]
    residual = equations(zz)
    Jb = jacobian(box)
    err = max(abs(sum(Y[i][j]*residual[j] for j in (0, 1))) for i in (0, 1))
    contraction = max(sum(abs(acb(int(i == j))-sum(Y[i][k]*Jb[k][j]
                            for k in (0, 1))) for j in (0, 1)) for i in (0, 1))
    positive('complex Newton contraction below one half', ar('1/2')-contraction)
    positive('complex Newton polydisk maps strictly inside itself',
             radius-err-contraction*radius)
    positive('left input lies strictly inside type-four disk',
             ar('8/125')-abs(aa-acb(ar('3/10'), -ar('13/250'))))
    positive('right input lies strictly inside type-three disk',
             ar('9/100')-abs(bb-acb(ar('7/20'), -ar('1/100'))))
    for j, z in enumerate(box):
        positive(f'selected root {j} lies inside type-three disk',
                 ar('9/100')-abs(z-acb(ar('7/20'), -ar('1/100'))))
    for j, z in enumerate([aa, bb, *box, box[0]+box[1], box[0]+aa, box[1]+bb]):
        positive(f'original logarithm argument {j} lies right of zero', z.real)
        positive(f'original logarithm argument {j} lies left of one', 1-z.real)

    g = lambda z: ((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)
    s, t = box
    M = (g(s+aa)+g(s+t)-2*g(s)+2*pi*ii*aa*s).real
    H = (g(aa)+g(t)).real-2*pi*aa.imag+2*pi*t.imag
    positive('left reciprocal root lies inside the unit disk', -aa.imag)
    positive('right reciprocal root lies outside the unit disk', t.imag)
    positive('selected action lower enclosure', M-ar('6473/10000'))
    positive('selected action upper enclosure', ar('6474/10000')-M)
    positive('last-row rate lower enclosure', H-ar('6535/10000'))
    positive('last-row rate upper enclosure', ar('6536/10000')-H)
    positive('actual last-row excess exceeds one two-hundredth', H-M-ar('1/200'))

    dependencies = [
        'notes/research_mixed_cyclic_critical_localization.md',
        'notes/research_mixed_three_canonical_conditional.md',
        'notes/research_mixed_four_conditional_complex_neighbors.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
        'repro/results/research-mixed-cyclic-block-localization.json',
        'repro/results/research-mixed-cyclic-block-localization-replay.json',
    ]
    original_hashes = {p: sha(ROOT/p) for p in dependencies}
    out = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Exact contour reductions and one outward two-leg-image obstruction only; no full-source cancellation conclusion.',
        'exact_identity_count': len(exact), 'exact_identities': exact,
        'strict_comparison_count': len(checks), 'comparisons': checks,
        'inputs': [['3131/10000', '-1146/10000'], ['4028/10000', '-828/10000']],
        'root_centers': [[mp.nstr(root[j].real, 80), mp.nstr(root[j].imag, 80)] for j in (0, 1)],
        'root_polydisk_radius': '1e-30', 'newton_contraction': str(contraction),
        'selected_action': str(M), 'last_row_rate': str(H), 'excess': str(H-M),
        'script_sha256': sha(__file__), 'proof_sha256': sha(PROOF),
        'dependencies': original_hashes,
    }
    assert original_hashes == {p: sha(ROOT/p) for p in dependencies}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print(f'PASS {len(exact)} exact identities, {len(checks)} outward comparisons')
    print('last-row excess:', H-M)


if __name__ == '__main__':
    main()
