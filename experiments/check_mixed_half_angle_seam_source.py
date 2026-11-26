#!/usr/bin/env python3
"""Exact all-row half-angle reductions and outward scalar source maxima."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_half_angle_seam_source.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-half-angle-seam-source.json')
    args = ap.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, checks, scalars = {}, set(), [], {}

    def check(name, value):
        assert value, name
        checks.append(name)

    def bind(path, expected=None):
        digest = sha(ROOT / path)
        if expected is not None:
            assert digest == expected, path
        if path in dependencies:
            assert dependencies[path] == digest, path
        dependencies[path] = digest
        return digest

    def inherit(path):
        bind(path)
        record = json.loads((ROOT / path).read_text())
        if path in visited:
            return record
        visited.add(path)
        bindings = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in record.get(field, {}).items():
                if name in bindings:
                    assert bindings[name] == digest, (path, name)
                bindings[name] = digest
                bind(name, digest)
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    records = {}
    for stem, prefix in (
            ('mixed_hybrid_zero_pair_reduction', 'check'),
            ('mixed_two_right_source_bound', 'certify'),
            ('mixed_seam_boundary_potential_reduction', 'check')):
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rp = f'repro/results/research-{stem.replace("_", "-")}.json'
        rec = inherit(rp)
        bind(pp)
        bind(ss)
        check(stem + ' passed with current proof and code',
              rec['status'] == 'passed'
              and rec['proof_sha256'] == dependencies[pp]
              and rec['script_sha256'] == dependencies[ss])
        records[stem] = rec
    reduction = records['mixed_hybrid_zero_pair_reduction']
    previous = records['mixed_two_right_source_bound']
    seam = records['mixed_seam_boundary_potential_reduction']
    A = {(e, d): F(reduction['left_endpoint_constants'][f'{e}{d}'])
         for e, d in itertools.product((0, 1), repeat=2)}
    B = {e: F(reduction['right_endpoint_constants'][str(e)]) for e in (0, 1)}
    check('literal original source constants are retained',
          A == {(0, 0): F('.360050'), (0, 1): F('.447948'),
                (1, 0): F('.485081'), (1, 1): F('.551147')}
          and B == {0: F('.347548'), 1: F('.515591')})
    check('existing saved whole-cell pair input remains complete',
          seam['validated_boundary_products'] == 2048
          and seam['validated_saved_cells'] == 18988
          and seam['saved_target_corners_per_cell'] == 16)
    check('stronger geometric floor and finite tolerance are extracted once',
          F(seam['extracted_geometric_gap']) == F(303, 1000)
          and F(seam['pair_collar_cost_upper']) == F(1, 50)
          and F(seam['total_pair_fourier_tolerance_upper']) == F(3, 1000)
          and F(seam['finite_pair_gap']) == F(7, 25)
          and F(303, 1000)-F(1, 50)-F(3, 1000) == F(7, 25))
    check('half-angle constants come from the original full-row corner family',
          previous['status'] == 'passed'
          and {'epsilon0_halfcount1', 'epsilon1_halfcount1'}
          <= set(previous['source_corner_constants']))

    P, p, X = sp.symbols('P p X', nonzero=True)
    j = sp.symbols('j', integer=True)
    for e, orientation in itertools.product((0, 1), repeat=2):
        check(f'endpoint cancels one factorial, type{e}, orientation{orientation}',
              sp.simplify(X**(-orientation*j)*p*P/P**(2+e)
                          - X**(-orientation*j)*p/P**(1+e)) == 0)
    v = (sp.sqrt(17)-1)/8
    check('positive four-type sine square solves exact critical equation',
          sp.simplify(4*v*v+v-1) == 0)
    u, e = sp.symbols('u e', positive=True)
    deriv = sp.log(2*sp.cos(sp.pi*u))-(1+e)*sp.log(2*sp.sin(sp.pi*u))
    check('whole low-row second derivative is strictly negative',
          sp.simplify(sp.diff(deriv, u)+sp.pi*sp.tan(sp.pi*u)
                      +(1+e)*sp.pi*sp.cot(sp.pi*u)) == 0)
    check('three-type quarter row is critical',
          sp.simplify(deriv.subs({e: 0, u: sp.Rational(1, 4)})) == 0)
    Jlo, Jshift = sp.symbols('Jlo Jshift', real=True)
    check('upper rows reflect to negative lower-row rate',
          sp.expand((-Jshift+(1+e)*Jlo)+(Jshift-(1+e)*Jlo)) == 0)
    R, t = sp.symbols('R t', positive=True)
    check('radial sine-square form of the product modulus',
          sp.expand(1+R*R-2*R*sp.cos(2*t)
                    -((1-R)**2+4*R*sp.sin(t)**2)).trigsimp() == 0)
    for beta in (0, 1):
        check(f'middle two Fourier halves have exact power{beta}',
              F(beta, 2)+F(beta, 2) == beta)
    G, old, new, collar, tol, Q = sp.symbols('G old new collar tol Q', real=True)
    deficit = G-old-collar-tol
    check('actual source replacement adds its saving without another debit',
          sp.expand(deficit+(old-new)-(G-new-collar-tol)) == 0)
    Aold, Bold, cleft, cright = sp.symbols('Aold Bold cleft cright', real=True)
    for label, saving, rate in (
            ('left', Aold-cleft, cleft+Bold),
            ('right', Bold-cright, Aold+cright)):
        check(label+' half-angle replacement leaves the other source unchanged',
              sp.expand(G-Aold-Bold-collar-tol+saving
                        -(G-rate-collar-tol)) == 0)
    alpha, endpoints, ds = sp.symbols('alpha endpoints ds', real=True)
    check('constant deficit recovers the original fractional star allocation',
          sp.expand(alpha*(G+Q)+ds*(endpoints-2*alpha)
                    -(G*alpha+Q*alpha+ds*(endpoints-2*alpha))) == 0)
    check('one loop uses half its literal pair without duplication', 2*F(1, 2) == 1)

    pi, ii = arb.pi(), acb(0, 1)

    def J(value):
        z = acb(value)
        return (((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)).real

    sine_square = (arb(17).sqrt()-1)/8
    assert sine_square > 0 and sine_square < ar('1/2')
    scalars['positive_sine_square'] = str(sine_square)
    u1 = sine_square.sqrt().asin()/pi
    assert u1 > 0 and u1 < ar('1/2')
    scalars['type_four_maximizer'] = str(u1)
    c = {0: -2*J(ar('1/4')), 1: J(ar('1/2')+u1)-2*J(u1)}
    for typ, lo, hi in ((0, '.291560', '.291561'), (1, '.443533', '.443534')):
        assert ar(lo) < c[typ] < ar(hi)
        scalars[f'constant_type{typ}'] = str(c[typ])
        assert c[typ].overlaps(arb(previous['source_corner_constants']
                                  [f'epsilon{typ}_halfcount1']))
    savings = {}
    for alpha, beta, gamma in itertools.product((0, 1), repeat=3):
        value = ar(A[beta, alpha]+B[gamma])-c[beta]-c[gamma]
        assert value > ar('.097534'), (alpha, beta, gamma, value)
        savings[f'{alpha}{beta}{gamma}'] = str(value)
    assert ar(A[0, 1]+B[1])-c[0]-c[1] > ar('.228444')
    one_sided = {}
    for beta, alpha in itertools.product((0, 1), repeat=2):
        value = ar(A[beta, alpha])-c[beta]
        assert value > ar('.041547')
        one_sided[f'left_type{beta}{alpha}'] = str(value)
    for gamma in (0, 1):
        value = ar(B[gamma])-c[gamma]
        assert value > ar('.055987')
        one_sided[f'right_type{gamma}'] = str(value)
    rho = ar('1/1000')
    nu = -J(rho)
    delta = rho*arb(2).log()+nu
    assert nu > 0 and delta > 0 and 2*delta+nu < ar('1/50')
    scalars['maximum_collar_cost'] = str(2*delta+nu)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/path) == digest for path, digest in dependencies.items())
    result = dict(
        status='passed', precision_bits=args.precision,
        exact_checks=len(checks), checks=checks,
        scalar_values=scalars, type_savings=savings, one_sided_savings=one_sided,
        primary_records=len(records), current_bindings=len(dependencies),
        all_type_saving_lower='.097534', alternating_three_saving_lower='.228444',
        numerical_cells_recomputed=0, boundary_potential_values_evaluated=0,
        geometric_cover_extended=False, interface_sign_certified=False,
        source_neighborhood_radius_evaluated=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='All-row half-angle endpoint source reduction, two outward exact '
              'maxima and eight source savings with current inherited source '
              'bindings. No new geometric cover, evaluated potential, '
              'interface sign or whole-period theorem.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks; 2 scalar maxima; 8 source savings;',
          len(records), 'primary records;', len(dependencies), 'current bindings',
          flush=True)


if __name__ == '__main__':
    main()
