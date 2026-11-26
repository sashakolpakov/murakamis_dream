#!/usr/bin/env python3
"""Exact raw-row derivatives, endpoint reduction, and Schur comparison.

Three scalar bounds accompany the written inequalities. No root proposal,
parameter cover, source cell, or mixed minimum-flow sign is evaluated.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_raw_row_stationarity.md'
PREVIOUS = dict(
    scope='Completed before adding Corollary 2; no mathematical or acceptance correction.',
    exact_identity_count=39, rational_check_count=23, scalar_comparisons=3,
    physical_branch_count=12, current_bindings=304,
    proof_sha256='8448faa95319055507d81c0f58c778fefb174a8e2f971f7b10feb9ddd08f89de',
    script_sha256='62838ce07e01d957ac644055307f638a6e6180bf0bf8ac1869433982f7fee625',
    author_record_sha256='e35c58fd677ba742708aab6b2b875759c452f14b930c989019973988ae18de7b',
    saved_384_record_sha256='b24764e8b311935d82757ff6a8fbc9073341d572d868b809fcb66216c119a47c',
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=320)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-raw-row-stationarity.json')
    args = ap.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary = {}, set(), {}

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        if path in deps:
            assert deps[path] == digest, path
        deps[path] = digest
        return digest

    def inherit(path):
        raw = (ROOT/path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        rec = json.loads(raw)
        if path in visited:
            return rec
        visited.add(path)
        merged = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in rec.get(field, {}).items():
                if name in merged:
                    assert merged[name] == digest, name
                merged[name] = digest
                bind(name, digest)
        for name in merged:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return rec

    for stem in ('mixed_right_boundary_row_bracket',
                 'mixed_closed_cotangent_roots',
                 'mixed_seam_attenuation_vertices'):
        path = f'repro/results/research-{stem.replace("_","-")}.json'
        rec = inherit(path)
        assert rec['status'] == 'passed', path
        assert rec['proof_sha256'] == bind(f'notes/research_{stem}.md')
        assert rec['script_sha256'] == bind(f'experiments/check_{stem}.py')
        primary[path] = rec
    bracket = primary['repro/results/research-mixed-right-boundary-row-bracket.json']
    assert bracket['row_interval'] == ['1/5','2/5']
    assert bracket['neighboring_real_interval'] == ['1/10','1/2']
    assert bracket['maximum_absolute_height'] == '57/1000'
    assert primary['repro/results/research-mixed-closed-cotangent-roots.json']['exact_identity_count'] == 13
    bind('notes/research_mixed_split_cutoff_hybrid_contour.md')

    identities, checks = [], []

    def zero(name, expr):
        assert sp.simplify(sp.expand(expr)) == 0, name
        identities.append(name)

    def check(name, condition):
        assert condition, name
        checks.append(name)

    I, pi = sp.I, sp.pi
    s,z = sp.symbols('s z')
    alpha,eps,d,sigma,q = sp.symbols('alpha eps d sigma q',real=True)
    g = sp.Function('g')
    Q = (g(s+sp.Rational(1,2))+g(s+z)-(2+eps)*g(s)
         +2*pi*I*(d*z+(1-d)/2)*s)
    F = Q-(1+(alpha-q)/2)*g(z)+pi*I*(sigma-q)*z
    K = sp.diff(g(s+z),z)-(1+(alpha-q)/2)*sp.diff(g(z),z)+2*pi*I*d*s+pi*I*(sigma-q)
    zero('original marginal including orientation and Fourier branch', sp.diff(F,z)-K)
    zero('outer Fourier alternatives leave the inner equation unchanged', sp.diff(F,s)-sp.diff(Q,s))
    U,G,h = sp.symbols('U G h',real=True)
    branches = []
    cases = [(0,0,0),(1,1,0),(0,0,1),(0,1,1),(1,0,1),(1,1,1)]
    for ee,aa,dd in cases:
        for ss in range(aa+1):
            for qq in sorted({0,ss}):
                phase = U-(1+sp.Rational(aa-qq,2))*G-pi*(ss-qq)*h
                if qq == 0:
                    literal = U-G-aa*G/2-aa*ss*pi*h
                else:
                    assert aa == ss == 1
                    literal = U-G+aa*pi*h-aa*ss*pi*h
                zero(f'literal allocated branch {ee}{aa}{dd}{ss}{qq}',phase-literal)
                check(f'nonnegative remaining own coefficient {ee}{aa}{dd}{ss}{qq}',aa-qq>=0)
                branches.append([ee,aa,dd,ss,qq])
    assert len(branches) == 12

    # Second derivatives of the row-dependent directional marginal.
    w = sp.symbols('w')
    zero('third derivative of the original logarithmic primitive',
         sp.diff(pi*sp.cot(pi*w)-pi*I,w)+pi*pi/sp.sin(pi*w)**2)
    tau,k = sp.symbols('tau k',real=True)
    zero('positive moving-real sine numerator',
         sp.re((1+I*k)/(1+I*tau)**2)
         -(1-tau*tau+2*k*tau)/(1+tau*tau)**2)
    C,D = sp.symbols('C D',real=True)
    zero('height-only row derivative and original chirp',
         sp.re((pi*(C+I*D)-pi*I+2*pi*I*d)*I*k)
         -pi*k*(1-2*d-D))
    check('minimum-flow height velocity bound',Fr(57,1000)/Fr(3,25)==Fr(19,40))
    check('moving shifted real interval',
          Fr(3,25)+Fr(1,5)==Fr(8,25)
          and Fr(11,50)+Fr(2,5)==Fr(31,50))
    check('reflected interval still above eight twenty-fifths',
          1-Fr(31,50)>Fr(8,25))
    check('strict hyperbolic tangent bound from pi upper',
          Fr(22,7)*Fr(57,1000)<Fr(9,50))
    check('sine angle ratio bound',Fr(2,3)*Fr(9,50)==Fr(3,25))
    check('positive moving-real quadratic numerator',
          1-Fr(3,25)**2-2*Fr(19,40)*Fr(3,25)==Fr(2179,2500)>0)

    v,H = sp.symbols('v H',real=True)
    sn = sp.sin(pi*v)*sp.cosh(pi*H)+I*sp.cos(pi*v)*sp.sinh(pi*H)
    cs = sp.cos(pi*v)*sp.cosh(pi*H)-I*sp.sin(pi*v)*sp.sinh(pi*H)
    zero('imaginary cotangent numerator',
         sp.im(cs*sp.conjugate(sn))+sp.sinh(2*pi*H)/2)
    zero('cotangent denominator',
         sp.trigsimp(sp.expand_trig(sp.expand_complex(sn*sp.conjugate(sn))
                      -(sp.cosh(2*pi*H)-sp.cos(2*pi*v))/2)))
    zero('imaginary-cotangent threshold identity',
         sp.cosh(H)-sp.sinh(H)-sp.exp(-H))
    check('height-only full shifted interval',
          Fr(3,25)+Fr(1,5)==Fr(8,25)
          and Fr(1,2)+Fr(2,5)==Fr(9,10))
    check('flat part distance to one',
          1-Fr(9,20)-Fr(2,5)==Fr(3,20))
    check('flat height condition uses the same pi threshold',
          Fr(57,1000)/Fr(3,20)**2==Fr(38,15))
    check('taper ratio extremum',
          Fr(1,20)/(Fr(1,10)+Fr(1,20))==Fr(1,3)
          and 2*Fr(1,20)==Fr(1,10))
    check('quadratic taper coefficient',
          Fr(57,1000)*400==Fr(114,5)
          and Fr(114,5)/9==Fr(38,15))
    endpoints = []
    for orientation,sign in itertools.product((0,1),(-1,1)):
        increasing = sign*(1-2*orientation)>0
        endpoint = '1/5' if increasing else '2/5'
        endpoints.append(dict(orientation=orientation,height_velocity_sign=sign,
                              minimizing_endpoint=endpoint))
    assert endpoints == [
        dict(orientation=0,height_velocity_sign=-1,minimizing_endpoint='2/5'),
        dict(orientation=0,height_velocity_sign=1,minimizing_endpoint='1/5'),
        dict(orientation=1,height_velocity_sign=-1,minimizing_endpoint='1/5'),
        dict(orientation=1,height_velocity_sign=1,minimizing_endpoint='2/5')]

    # Real maximization eliminates only the real inner coordinate.
    a,b,c,d0,e,f = sp.symbols('a b c d0 e f',real=True)
    real_hessian = sp.Matrix([[-a,-c,-d0],[-c,-e,-f],[-d0,-f,e]])
    reduced = real_hessian[1:,1:]-real_hessian[1:,0:1]*real_hessian[0:1,1:]/(-a)
    for i,j,expected in ((0,0,-e+c*c/a),(1,1,e+d0*d0/a),(0,1,-f+c*d0/a)):
        zero(f'real Schur component {i}{j}',reduced[i,j]-expected)
    zero('real concavity follows from the determinant',
         -e+c*c/a+(a*e-c*c)/a)

    u,y,arg = sp.symbols('u y arg',real=True)
    original_imag = -pi*u+arg-(2+eps)*(pi/2-pi*u)+2*pi*(d*y+(1-d)/2)
    normal = arg+(1+eps)*pi*u-eps*pi/2+d*pi*(2*y-1)
    zero('original normal force at a real raw row',original_imag-normal)
    real_normal = eps*pi*u+pi*((1-eps)/2-y+d*(2*y-1))
    zero('normal force for real A neighbor',normal.subs(arg,pi/2-pi*(u+y))-real_normal)
    for orientation in (0,1):
        zero(f'type-three normal force orientation{orientation}',
             real_normal.subs({eps:0,d:orientation})-(1-2*orientation)*pi*(sp.Rational(1,2)-y))

    def gpp(x):
        return pi*sp.cot(pi*x)-pi*I
    inner,outer = sp.Rational(1,4),sp.Rational(1,2)
    hss = 2*gpp(inner+outer)-2*gpp(inner)
    hyy = gpp(inner+outer)-gpp(outer)
    zero('minimal example original zero logarithmic lift',
         2*(-pi/4)-2*(pi/4)+pi)
    zero('minimal example inner Hessian',hss+4*pi)
    zero('minimal example outer Hessian',hyy+pi)
    for orientation in (0,1):
        hsy = gpp(inner+outer)+2*pi*I*orientation
        zero(f'minimal example mixed Hessian orientation{orientation}',
             hsy-(-pi+I*pi*(2*orientation-1)))
        raw_second = sp.re(hyy)-sp.re(hsy)**2/sp.re(hss)
        coherent_second = sp.re(hyy-hsy*hsy/hss)
        zero(f'minimal example raw real Schur orientation{orientation}',raw_second+3*pi/4)
        zero(f'minimal example coherent complex Schur orientation{orientation}',coherent_second+pi)
        zero(f'minimal example gap curvature orientation{orientation}',raw_second-coherent_second-pi/4)

    # Unselected vertical-sign corollary. The inequalities for the
    # argument are proved on the entire regular shifted interval.
    zero('unselected orientation difference',
         K.subs({q:0,sigma:0,d:1})-K.subs({q:0,sigma:0,d:0})-2*pi*I*s)
    zero('ramp height maximum quadratic identity',
         sp.Rational(19,16)*y*y-sp.Rational(19,40)*(y-sp.Rational(1,10))
         -sp.Rational(19,16)*(y-sp.Rational(1,5))**2)
    check('flat initial-height cone bound',
          Fr(19,16)*Fr(11,50)**2-Fr(57,1000)==Fr(19,40000)>0)
    check('initial-height threshold below proved pi lower',
          Fr(19,16)<Fr(38,15))
    check('unselected first-argument imaginary reserve',
          Fr(1,5)-(Fr(1,2)-Fr(3,25))/2==Fr(1,100)>0)

    def ar(x):
        x = Fr(x)
        return arb(x.numerator)/x.denominator
    scalars = [
        ('pi below22/7',ar(Fr(22,7))-arb.pi()),
        ('moving-real cotangent below2/3',ar(Fr(2,3))-(arb.pi()*ar(Fr(8,25))).cot()),
        ('taper cotangent threshold pi above38/15',arb.pi()-ar(Fr(38,15))),
    ]
    for name,value in scalars:
        assert value.lower()>0,(name,value)

    input_hash = None
    if args.input:
        raw = args.input.read_bytes()
        input_hash = hashlib.sha256(raw).hexdigest()
        old = json.loads(raw)
        assert old['status']=='passed'
        assert old['proof_sha256']==ph and old['script_sha256']==sh
        assert old['dependencies_sha256']==deps
        assert old['exact_identities']==identities and old['rational_checks']==checks
        assert old['physical_branches']==branches and old['height_only_endpoints']==endpoints
        assert old['previous_completed_version']==PREVIOUS
    assert ph==sha(PROOF) and sh==sha(__file__)
    assert all(sha(ROOT/path)==digest for path,digest in deps.items())
    if args.input:
        assert input_hash==sha(args.input)
    result = dict(status='passed',precision_bits=args.precision,
        exact_identity_count=len(identities),exact_identities=identities,
        rational_check_count=len(checks),rational_checks=checks,
        scalar_comparisons=len(scalars),
        scalar_reserves=[dict(name=name,value=str(value))for name,value in scalars],
        physical_branch_count=len(branches),physical_branches=branches,
        height_only_endpoints=endpoints,row_endpoints=['1/5','2/5'],
        moving_minimum_interval=['3/25','11/50'],maximum_height_velocity='19/40',
        primary_records=len(primary),current_bindings=len(deps),
        previous_completed_version=PREVIOUS,
        new_roots=0,source_cells_recomputed=0,minimum_flow_sign_certified=False,
        proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,
        scope='Exact Danskin and real-Schur identities; two-row endpoint reduction for the stated hybrid minimum-flow derivative, retaining all physical branches and outer correlations; a local counterexample to automatic raw/coherent derivative domination. No mixed-flow sign, new packet, or full-period asymptotic.')
    if input_hash:
        result['input_sha256']=input_hash
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(identities),'identities;',len(checks),'rational checks;',
          len(scalars),'scalars;',len(branches),'physical branches;',
          len(deps),'current bindings',flush=True)


if __name__=='__main__':
    main()
