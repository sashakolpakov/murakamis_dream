#!/usr/bin/env python3
"""Exact algebra and margins for the whole-circle conditional three packet.

This checks the analytic proof's universal constants, not a sample of
conditional saddles or mixed words. The original finite identity has its
own all-level proof and separately validated finite diagnostics.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-mixed-three-conditional-circle.json')
    args = parser.parse_args()
    identities, margins = [], []
    q = sp.Rational

    def identity(name, expression):
        assert sp.factor(expression) == 0, (name, sp.factor(expression))
        identities.append(name)

    def positive(name, expression):
        value = sp.factor(expression)
        assert value.is_Rational and value > 0, (name, value)
        margins.append({'name': name, 'strict_rational_margin': str(value)})

    rho, c, d = sp.symbols('rho c d', positive=True)
    Q = ((1-rho*rho)**2+4*rho*rho*d*d
         +4*rho*(1+rho*rho)*d*c+4*rho*rho*c*c)
    original = ((1+rho*rho)+2*rho*c*d)**2-4*rho*rho*(1-c*c)*(1-d*d)
    identity('paired root squared modulus', original-Q)
    identity('paired modulus is convex in cosine', sp.diff(Q, c, 2)-8*rho*rho)
    identity('projected distance dominates antipodal endpoint',
             Q-Q.subs(c, -1)-4*rho*(1+c)*((1+rho*rho)*d-rho*(1-c)))
    identity('pair gain from its center',
             Q.subs(c, 1)-Q-(1-c)*(4*rho*(1+rho*rho)*d+4*rho*rho*(1+c)))
    identity('paired derivative positive on short arc',
             sp.diff(Q, c)-4*rho*((1+rho*rho)*d+2*rho*c))

    curvature = rho*((1+rho*rho)*c+2*rho)/(1+rho*rho+2*rho*c)**2
    identity('factor curvature invariant under reciprocal radius',
             curvature-curvature.subs(rho, 1/rho))
    identity('factor curvature numerator from complex quotient',
             rho*c*(1+rho*rho)+2*rho*rho-rho*((1+rho*rho)*c+2*rho))
    p = rho*(2*rho-q(59,100)*(1+rho*rho))
    identity('curvature numerator derivative lower affine bound',
             sp.diff(p,rho)-((4-q(177,100))*rho-q(59,100))
             -q(177,100)*rho*(1-rho))
    identity('curvature numerator at minimum radius', p.subs(rho,q(1,3))-q(1,270))
    identity('curvature per factor', q(1,270)/16-q(1,4320))
    identity('total curvature from minimum factor count', q(2,5)*q(1,4320)-q(1,10800))

    radial=(rho*rho+rho*c)/(1+rho*rho+2*rho*c)
    identity('radial comparison at both end radii',
             radial-rho/(1+rho)
             -rho*(rho-1)*(1-c)/((1+rho)*(1+rho*rho+2*rho*c)))
    identity('lower-radius factor derivative', (rho/(1+rho)).subs(rho,q(1,3))-q(1,4))
    identity('upper-radius factor derivative', (rho/(1+rho)).subs(rho,3)-q(3,4))
    identity('lower radial endpoint reserve', (q(9,20)-3*q(1,5))/4+q(3,80))
    identity('upper radial endpoint reserve', (3*q(1,5)-q(9,20))/4-q(3,80))
    aa,bb=sp.symbols('a b', real=True)
    identity('harmonic optimized radial Schur bound', aa-(-bb)**2/(-aa)-aa-bb*bb/aa)
    identity('Cauchy coefficient conditional N power', 1-q(1,2)-q(1,2))

    # Elementary trigonometric enclosures use only 25/8 < pi < 22/7.
    lower_sin=q(5,32)-q(11,70)**3/6
    upper_sin=q(22,35)-q(5,8)**3/6+q(22,35)**5/120
    positive('sin(pi/20)>31/200 by lower Taylor bound',lower_sin-q(31,200))
    positive('sin(pi/5)<59/100 by upper Taylor bound',q(59,100)-upper_sin)
    positive('cos(pi/4)>7/10 from sqrt2>7/5',2-q(7,5)**2)
    positive('pair projection bracket reserve',2*q(31,200)-(1-q(7,10)))
    positive('short arc fits one semicircle',q(1,2)-q(1,4))
    positive('factor angles separated from negative real direction',1-q(7,10))
    positive('curvature numerator monotone on [1/3,1]',
             (4-q(177,100))*q(1,3)-q(59,100))
    positive('minimum curvature numerator',p.subs(rho,q(1,3)))
    positive('factor curvature denominator positive reserve',q(1,4320))
    positive('strict radial sign lower and upper',q(3,80))
    positive('global pair logarithmic loss reserve',
             4*q(3,16)*q(1,2)*q(31,200)-q(1,20))
    positive('central complement rounding reserve',q(1,86400)-q(1,88000))
    positive('full-circle Gaussian curvature',q(1,10800))
    # floor(a/2) >= a/2-1/2 >= N/12 for N>=30, a>=N/5.
    identity('minimum block-pair count at N30',30*q(1,10)-q(1,2)-30*q(1,12))
    positive('pair-count excess increases with N',q(1,10)-q(1,12))
    identity('far angular complement budget',q(1,40)*q(1,12)-q(1,480))
    identity('central angular complement budget',q(1,10800)/2/4-q(1,86400))
    identity('maximum center separation',q(9,20)-q(1,5)-q(1,4))
    identity('maximum central factor angle',q(9,20)+q(1,4)-q(7,10))
    AA,BB,ZZ,UU=sp.symbols('A B Z U')
    quadratic=(1-AA)+(BB-AA)*ZZ+AA*(BB-1)*ZZ**2
    identity('continuous conditional quadratic equation',
             (1+ZZ*AA)*(1+ZZ*BB)-AA*(1+ZZ)**2-quadratic)
    identity('original conditional root U equals minus Z',
             quadratic.subs(ZZ,-UU)-((1-UU*AA)*(1-UU*BB)-AA*(1-UU)**2))
    alpha,ww=sp.symbols('alpha w')
    ss=q(1,2)+sp.I*ww/(2*sp.pi)
    identity('absolute conditional phase calibration',
             -alpha*ww+sp.I*sp.pi*alpha-2*sp.pi*sp.I*alpha*ss)
    qq,hp=sp.symbols('q0 hprime')
    identity('actual zero lift fixes endpoint symbol',
             (-qq/(sp.pi*sp.I)-alpha-hp)*(-sp.pi*sp.I)
             -(qq+sp.pi*sp.I*(alpha+hp)))
    identity('conditional phase Hessian normalization',(-2*sp.pi*sp.I)**2+4*sp.pi**2)
    nn=sp.Symbol('N')
    identity('discrete parity carrier absorbed into original action',
             sp.I*sp.pi*(nn*alpha)-nn*(sp.I*sp.pi*alpha))

    upstream_path='repro/results/research-mixed-conditional-leg-sum.json'
    upstream=json.loads((ROOT/upstream_path).read_text())
    assert upstream['status']=='passed'
    upstream_script='experiments/check_mixed_conditional_leg_sum.py'
    assert upstream['script_sha256']==sha256((ROOT/upstream_script).read_bytes()).hexdigest()
    for path,digest in upstream['dependencies_sha256'].items():
        assert digest==sha256((ROOT/path).read_bytes()).hexdigest(),path
    dependencies=['notes/research_mixed_three_conditional_circle.md',
                  'notes/research_mixed_conditional_leg_sum.md',
                  'notes/research_mixed_absolute_complement_obstruction.md',
                  upstream_path,upstream_script]
    result={
        'status':'passed','symbolic_identity_count':len(identities),'symbolic_identities':identities,
        'strict_rational_margin_count':len(margins),'strict_rational_margins':margins,
        'source_provenance_count':1,
        'source_provenance':{'record':upstream_path,'exact_identity_count':upstream['exact_identity_count'],
                             'status':'all recorded script/proof dependency hashes current'},
        'scope':'Universal full-circle comparisons and Gaussian normalization for physical integer neighbors in [N/5,9N/20]. No complex-neighbor continuation, four-vertex packet, or mixed-word lower theorem is certified.',
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256':{path:sha256((ROOT/path).read_bytes()).hexdigest() for path in dependencies}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','symbolic_identity_count',
                      'strict_rational_margin_count','source_provenance_count')}))


if __name__=='__main__':
    main()
