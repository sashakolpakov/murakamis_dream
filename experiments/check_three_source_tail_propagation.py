#!/usr/bin/env python3
"""Outward scalar budgets for the conditional original-source induction.

This checks the explicit numerical inequalities in the written proof.
It does not certify the kernel packets or an entrance-source envelope.
"""

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=192)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-three-source-tail-propagation.json')
    args = parser.parse_args()
    ctx.prec = args.precision
    start = time.monotonic()

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def interval(left, right):
        left, right = Q(left), Q(right)
        # Exact rational center and radius, both rounded outward by Arb.
        return arb(a((left+right)/2), a((right-left)/2))

    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    pi, root21 = arb.pi(), arb(21).sqrt()
    rho = (5-root21)/2
    alpha, beta = 8*pi*arb(3).sqrt()/21, -4*pi/7
    kmag = 4*pi/root21
    R, r, rc, H = map(a, [Q(1, 200), Q(1, 100), Q(3, 625), Q(1, 2500)])
    A, loss, B = a(Q(29, 20)), a(Q(3, 2)), arb(13)
    D = 5+root21
    Z = rho*a(Q(21, 20))/(1-a(Q(3, 10))*rho)
    C0 = kmag*(D+a(Q(3, 5)))/(2*(D-a(Q(3, 5)))**2)
    positive('gradient contraction below 47/200', a(Q(47, 200))-Z)
    positive('central drift coefficient below 87/500', a(Q(87, 500))-C0)
    positive('total initial normalization drift below .000144',
             a(Q(144, 10**6))-C0*a(Q(7, 250))**2/(1-Z**2))
    positive('three analytic entrances reach Hstar', H-a(Q(7, 250))*Z**3)
    positive('three analytic entrances below .000358',
             a(Q(358, 10**6))-a(Q(7, 250))*Z**3)
    positive('relaxed .03 entrance also reaches Hstar after three transforms',
             H-a(Q(3, 100))*Z**3)

    # The small class uses |h'|<=.18 and the established .1 kernel defect.
    critical_radius = (rho*a(Q(21, 20))*R+rho*H/2)/(1-rho*a(Q(7, 25))/2)
    positive('critical wire within radius 1/800', a(Q(1, 800))-critical_radius)
    positive('central contour rectangle lies inside source disk',
             R**2-rc**2-a(Q(1, 800))**2)
    positive('horizontal endpoint phase reserve',
             9*(rc-a(Q(1, 800)))**2-a(Q(1, 10**6)))
    positive('source real curvature exceeds 8',
             alpha*root21-kmag*a(Q(9, 50))-8)
    positive('joint real curvature exceeds 18',
             alpha*(root21+5)-kmag*a(Q(7, 25))-18)
    positive('quadratic completion is positive throughout both annuli',
             a(Q(72, 25))-rho*kmag)

    def annulus_error(tau, source_curvature):
        s = R*tau
        lam = 3*tau
        quad = lam*R**2+s**2*kmag**2*(lam-rho*alpha)/(lam**2-rho**2*kmag**2)
        return (C0*H**2+kmag*H*s+kmag*Z*H*R+a(Q(9, 100))*kmag*R**2
                -(a(source_curvature)+5*alpha/2)*s**2+quad+3*kmag*(s+R)**3)

    annuli = []
    for name, left, right, curvature in [
            ('packet annulus', Q(24, 25), Q(1), Q(4)),
            ('global-envelope annulus', Q(1), Q(2), Q(29, 20))]:
        cells = []
        # Uniform exact coverage is deliberately simple and reproducible.
        mesh = 1024
        for j in range(mesh):
            lo = left+(right-left)*Q(j, mesh)
            hi = left+(right-left)*Q(j+1, mesh)
            error = annulus_error(interval(lo, hi), curvature)
            margin = -error-a(Q(1, 10**6))
            assert margin > 0, (name, j, error)
            cells.append({'tau_interval': [str(lo), str(hi)],
                          'strict_margin_beyond_one_millionth': str(margin)})
        assert cells[0]['tau_interval'][0] == str(left)
        assert cells[-1]['tau_interval'][1] == str(right)
        assert all(cells[j]['tau_interval'][1] == cells[j+1]['tau_interval'][0]
                   for j in range(mesh-1))
        annuli.append({'name': name, 'source_quadratic_loss': str(curvature),
                       'exact_coverage': [str(left), str(right)], 'cells': cells})

    Lambda = (B+((alpha*root21-B)**2+(beta*root21)**2).sqrt())/2
    far_gap = ((A+loss)*r**2-kmag*H*r-C0*H**2-kmag*Z*H*R
               -a(Q(9, 100))*kmag*R**2-Lambda*R**2)
    reset_gap = (loss-A)*R**2-(C0+kmag**2/(4*(A+loss)))*H**2
    positive('complex-output far-input gap exceeds two millionths',
             far_gap-a(Q(2, 10**6)))
    positive('whole-real-period reset gap exceeds one millionth',
             reset_gap-a(Q(1, 10**6)))
    positive('small real packet dominates the desired envelope', arb(4)-A)

    # These exact identities independently check the 2x2 optimizations.
    import sympy as sp
    al, be, rh, lm = sp.symbols('alpha beta rho lambda', real=True)
    mat = sp.Matrix([[lm+rh*al, -rh*be], [-rh*be, lm-rh*al]])
    vec = sp.Matrix([al, -be])
    assert sp.simplify((vec.T*mat.inv()*vec)[0]
                       -(al**2+be**2)*(lm-rh*al)/(lm**2-rh**2*(al**2+be**2))) == 0
    ar, br, bb, ee = sp.symbols('a b B eigenvalue', real=True)
    height_matrix = sp.Matrix([[ar/2, -br/2], [-br/2, bb-ar/2]])
    assert sp.expand((ee*sp.eye(2)-height_matrix).det()
                     -(ee**2-bb*ee-(ar**2+br**2-2*ar*bb)/4)) == 0

    dependencies = [
        'notes/research_three_source_tail_propagation.md',
        'notes/research_three_phase_graph_transform.md',
        'notes/research_three_vertex_input_rectangle.md',
        'notes/research_three_vertex_capped_gaussian_bound.md',
        'notes/research_three_vertex_weighted_height_bound.md',
        'notes/research_three_prepared_cap_quantified_source.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
    ]
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'strict_scalar_comparison_count': len(checks), 'exact_algebra_identities': 2,
        'annulus_cells': sum(len(item['cells']) for item in annuli),
        'scope': 'Scalar budgets and exact univariate coverage for the conditional source-propagation proof. Does not certify the separately proved kernel inputs or the still-required entrance source envelope and entrance attachments.',
        'checks': checks, 'annuli': annuli,
        'constants': {'Z': str(Z), 'C0': str(C0), 'critical_radius': str(critical_radius),
                      'Lambda_B': str(Lambda), 'far_gap': str(far_gap),
                      'real_reset_gap': str(reset_gap)},
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {path: sha256((ROOT/path).read_bytes()).hexdigest()
                                for path in dependencies},
        'elapsed_seconds': time.monotonic()-start,
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in
                      ['status', 'strict_scalar_comparison_count', 'exact_algebra_identities',
                       'annulus_cells', 'elapsed_seconds']}, indent=2))
    print('far gap:', far_gap)
    print('real reset gap:', reset_gap)


if __name__ == '__main__':
    main()
