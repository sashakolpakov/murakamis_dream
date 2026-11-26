#!/usr/bin/env python3
"""Outward original-index certificate for the canonical type-three conditional.

Numerical roots only propose rational Newton centers. The full parameter
square, action floor and both endpoint gaps are interval-certified. Exact
finite algebra checks all revived rows and the original support.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time

import mpmath as mp
import sympy as sp
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--output', type=Path, default=ROOT/
                        'repro/results/research-mixed-three-canonical-conditional.json')
    args = parser.parse_args()
    ctx.prec = args.precision
    mp.mp.dps = 95
    start = time.monotonic()
    pi, ii = arb.pi(), acb(0, 1)

    def ar(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def interval(low, high):
        return ar(low).union(ar(high))

    def square(z, radius):
        return acb(z.real+arb(0, ar(radius)), z.imag+arb(0, ar(radius)))

    def log_sine(z):
        return (2*(pi*z).sin()).log()

    def J(z):
        return ((2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(-2*pi*ii) \
            +ii*pi*z*(1-z)/2

    def phase(s, a, b):
        return J(s+a)+J(s+b)-2*J(s)+ii*pi*s*(a-b)

    def gradient(s, a, b):
        return log_sine(s+a)+log_sine(s+b)-2*log_sine(s)+ii*pi*(a-b)

    def hessian(s, a, b):
        return pi*((pi*(s+a)).cot()+(pi*(s+b)).cot()-2*(pi*s).cot())

    def supnorm(z):
        return max(abs(z.real).upper(), abs(z.imag).upper())

    def rows(z):
        return abs(z.real)+abs(z.imag)

    scalars = []

    def positive(name, value):
        assert value > 0, (name, str(value))
        scalars.append({'name': name, 'strict_margin': str(value)})

    positive('uniform negative real Hessian exceeds one fifth',
             2*pi*(pi/10).sin()/(1+(2*pi/5).cosh())**2-ar('1/5'))
    positive('uniform Hessian modulus below46',
             46-2*pi*((3*pi/50).cot()+(3*pi/20).cot()))
    positive('circle critical height fits seven fortieths', 7*pi/20-ar(3).log())
    positive('left real tail monotonicity', (pi/5).sin()**2-(3*pi/20).sin()**2)
    positive('right real tail reflection ordering', 2*ar('49/100')+ar('1/5')-1)
    eps = ar('1/100000')
    positive('both horizontal alias gaps exceed1/25000',
             3*pi*eps/2-5313*eps**2-ar('1/25000'))
    positive('whole same-side endpoint gap exceeds1/1500',
             ar('9/100')**2/10-46*eps*ar('9/100')-23*eps**2-ar('1/1500'))
    positive('endpoint quadratic bound decreases past distance .09',
             ar('9/100')/5-46*eps)
    positive('adaptive contour stays in fixed height rectangle',
             ar('1/5')-ar('7/40')-eps)
    positive('revived-row entropy below one sixth', ar('1/6')-J(acb(ar('5/6'))).real)
    positive('revived-row reserve exceeds one thirteenth',
             ar('1/4')-ar('1/6')-ar('1/13'))

    identities = []
    A, B, U = sp.symbols('A B U')
    expression = (1-A*U)*(1-B*U)-A*(1-U)**2
    assert sp.expand(expression-(1-A+(A-B)*U+A*(B-1)*U**2)) == 0
    identities.append('original conditional stationary quadratic')
    s, a, b = sp.symbols('s a b')
    phi = lambda z: sp.pi*(z-z*z)/2
    assert sp.expand(phi(s+a)+phi(s+b)-2*phi(s)+2*sp.pi*a*s
                     -phi(a)-phi(b)-sp.pi*s*(a-b)) == 0
    identities.append('absolute marked phase and both parameter constants')
    assert sp.expand(-sp.pi*(s+a+s+b-2*s)/2+sp.pi*(a+b)/2) == 0
    identities.append('order-one sine symbol carrier')
    assert Q(46**2, 4)*10+23 == 5313
    identities.append('horizontal displacement quadratic completion')

    field = sp.QQ.algebraic_field(sp.I, sp.sqrt(2), sp.sqrt(3))
    one, zero = field.one, field.zero
    cv = lambda z: field.from_sympy(sp.sympify(z))

    def product(values):
        result = one
        for value in values:
            result *= value
        return result

    finite_checks = []
    for level, qq in ((2, sp.I), (3, (1+sp.I*sp.sqrt(3))/2),
                      (4, (1+sp.I)/sp.sqrt(2)), (6, (sp.sqrt(3)+sp.I)/2)):
        r = cv(qq)**-2
        P = [product(1-r**h for h in range(1, j+1)) for j in range(level)]
        for aa in range(level):
            for bb in range(level):
                continued = original = zero
                for j in range(level):
                    row = (r**(-aa*j)*P[aa]*P[bb]
                           *product(1-r**(aa+h) for h in range(1, j+1))
                           *product(1-r**(bb+h) for h in range(1, j+1))/P[j]**2)
                    target = (r**(-aa*j)*P[j+aa]*P[j+bb]/P[j]**2
                              if j+max(aa, bb) < level else zero)
                    assert row == target, (level, aa, bb, j)
                    finite_checks.append(f'N{level} physical row a{aa} b{bb} j{j}')
                    continued += row
                    original += target
                assert continued == original
                finite_checks.append(f'N{level} whole original conditional a{aa} b{bb}')

    def proposal(a, b):
        aa, bb = mp.mpf(a.numerator)/a.denominator, mp.mpf(b.numerator)/b.denominator
        def fp(z):
            return (mp.log(2*mp.sin(mp.pi*(z+aa)))+mp.log(2*mp.sin(mp.pi*(z+bb)))
                    -2*mp.log(2*mp.sin(mp.pi*z))+1j*mp.pi*(aa-bb))
        z = mp.findroot(fp, (mp.mpc('.33', '0'), mp.mpc('.33', '.04')),
                        tol=mp.mpf('1e-85'))
        return [mp.nstr(z.real, 85), mp.nstr(z.imag, 85)]

    def certify(box, address):
        al, ah, bl, bh = box
        am, bm = (al+ah)/2, (bl+bh)/2
        center = proposal(am, bm)
        z = acb(ar(Q(center[0])), ar(Q(center[1])))
        a0, b0 = acb(ar(am)), acb(ar(bm))
        inv = 1/hessian(z, a0, b0)
        point_radius = Q(1, 10**40)
        zp = square(z, point_radius)
        kp = rows(1-inv*hessian(zp, a0, b0))
        ep = supnorm(inv*gradient(z, a0, b0))
        assert kp < ar('1/2') and ep+kp*ar(point_radius) < ar(point_radius)
        ab, bb = acb(interval(al, ah)), acb(interval(bl, bh))
        residual = supnorm(inv*gradient(z, ab, bb))
        radius = Q(1, 2**16)
        while ar(radius) < 3*residual:
            radius *= 2
        if radius > Q(1, 16):
            return None
        zs = square(z, radius)
        contraction = rows(1-inv*hessian(zs, ab, bb))
        if not (contraction < ar('1/2')
                and residual+contraction*ar(radius) < ar(radius)):
            return None
        if not (zs.real > ar('3/20') and zs.real < ar('49/100')
                and zs.imag > -ar('1/5') and zs.imag < ar('1/5')):
            return None
        da = (log_sine(zs+ab)+ii*pi*zs).real
        db = (log_sine(zs+bb)-ii*pi*zs).real
        action = (phase(zp, a0, b0).real
                  -abs(da)*ar((ah-al)/2)-abs(db)*ar((bh-bl)/2))
        if not action > ar('1/4'):
            return None
        gaps = []
        for cut in (Q(3, 20), Q(49, 100)):
            c = acb(ar(cut))
            center_gap = (phase(zp, a0, b0)-phase(c, a0, b0)).real
            da = (log_sine(zs+ab)-log_sine(c+ab)+ii*pi*(zs-c)).real
            db = (log_sine(zs+bb)-log_sine(c+bb)-ii*pi*(zs-c)).real
            gap = center_gap-abs(da)*ar((ah-al)/2)-abs(db)*ar((bh-bl)/2)
            if not gap > ar('1/100'):
                return None
            gaps.append(str(gap))
        return {'address': address, 'bounds': list(map(str, box)), 'center': center,
                'radius': str(radius), 'point_radius': str(point_radius),
                'newton_contraction': str(contraction), 'newton_residual': str(residual),
                'action_lower_bound': str(action), 'endpoint_gaps': gaps}

    pending = [((Q(1, 5), Q(9, 20), Q(1, 5), Q(9, 20)), '')]
    leaves, visited = [], 0
    while pending:
        box, address = pending.pop()
        visited += 1
        assert len(address) <= 24, ('unresolved parameter cell', box, address)
        accepted = certify(box, address)
        if accepted:
            leaves.append(accepted)
            continue
        low = 2*(len(address) % 2)
        midpoint = (box[low]+box[low+1])/2
        for bit in (0, 1):
            child = list(box)
            child[low+1-bit] = midpoint
            pending.append((tuple(child), address+str(bit)))
    codes = {leaf['address'] for leaf in leaves}
    assert len(codes) == len(leaves)

    def cover(prefix):
        if prefix in codes:
            assert not any(c.startswith(prefix) and c != prefix for c in codes)
            return
        for bit in '01':
            assert any(c.startswith(prefix+bit) for c in codes)
            cover(prefix+bit)
    cover('')

    dependencies = [
        'notes/research_mixed_three_canonical_conditional.md',
        'notes/research_mixed_three_conditional_circle.md',
        'notes/research_mixed_conditional_leg_sum.md',
        'notes/research_mixed_four_conditional_complex_neighbors.md',
        'notes/exact_factorial_interpolation_and_complex_contours.md',
        'notes/research_uniform_factorial_and_boundary_decay.md',
    ]
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'strict_scalar_count': len(scalars), 'scalars': scalars,
        'exact_identity_count': len(identities), 'exact_identities': identities,
        'finite_identity_count': len(finite_checks), 'finite_identities': finite_checks,
        'visited_cells': visited, 'accepted_cells': len(leaves), 'leaves': leaves,
        'parameter_domain': ['1/5', '9/20', '1/5', '9/20'],
        'middle_rectangle': ['3/20', '49/100', '-1/5', '1/5'],
        'action_lower_bound': '1/4', 'endpoint_gap': '1/100',
        'elapsed_seconds': time.monotonic()-start,
        'scope': ('Canonical fixed N-term source, exact physical support, and full-square '
                  'root/action/endpoint certificate. The written original-index contour '
                  'and product regularization prove the complex packet; no outer mixed-word '
                  'contraction or volume limit is checked.'),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {path: sha256((ROOT/path).read_bytes()).hexdigest()
                                for path in dependencies},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'status', 'strict_scalar_count', 'exact_identity_count', 'finite_identity_count',
        'visited_cells', 'accepted_cells')}))


if __name__ == '__main__':
    main()
