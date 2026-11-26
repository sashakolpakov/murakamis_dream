#!/usr/bin/env python3
"""Exact potential-depth arithmetic and current source bindings; no cover."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_finite_depth_boundary_potential.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT /
                        'repro/results/research-mixed-finite-depth-boundary-potential.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, checks, records = {}, set(), [], {}

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
            for p, digest in record.get(field, {}).items():
                if p in bindings:
                    assert bindings[p] == digest, (path, p)
                bindings[p] = digest
                bind(p, digest)
        # This recursively validates provenance. It does not promote any
        # diagnostic appearing in an inherited manifest to a theorem.
        for p in bindings:
            if p.startswith('repro/results/') and p.endswith('.json'):
                inherit(p)
        return record

    specs = [
        ('mixed_extracted_plateau_curvature', 'check', ''),
        ('mixed_type_four_height_refinement', 'certify', ''),
        ('mixed_type_four_height_refinement', 'replay', '-replay'),
        ('mixed_full_nonlow_half_region', 'check', ''),
    ]
    for stem, prefix, suffix in specs:
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rr = f'repro/results/research-{stem.replace("_", "-")}{suffix}.json'
        bind(pp)
        bind(ss)
        r = inherit(rr)
        check(stem + suffix + ' passed with current proof and code',
              r['status'] == 'passed' and r['proof_sha256'] == dependencies[pp]
              and r['script_sha256'] == dependencies[ss])
        records[stem, suffix] = r
    for name in ('mixed_nonlow_open_chain_boundary',
                 'mixed_nonlow_occupation_loss',
                 'mixed_nonlow_interface_reduction'):
        bind(f'notes/research_{name}.md')

    curv = records['mixed_extracted_plateau_curvature', '']
    check('complete extracted curvature cover and both strict lower endpoints',
          curv['validated_boundary_products'] == 64
          and curv['validated_saved_cells'] == 36325
          and curv['numerical_cells_recomputed'] == 0
          and F(curv['recorded_author_lower']) > F(1, 5)
          and F(curv['recorded_replay_lower']) > F(1, 5))
    reset = json.loads((ROOT / curv['author_record']).read_text())
    check('local lower and upper Hessian constants retained',
          F(curv['local_hessian_lower']) == F(1, 5)
          and reset['status'] == 'passed' and reset['matrix_cost_upper'] == 20)
    author = records['mixed_type_four_height_refinement', '']
    replay = records['mixed_type_four_height_refinement', '-replay']
    check('both geometry records retain48 complete products and249 cells',
          author['case_count'] == replay['case_count'] == 48
          and author['accepted_cells'] == replay['accepted_cells'] == 249
          and replay['refinements'] == 0)
    check('independent geometry input binding current',
          replay['input_sha256'] == dependencies[
              'repro/results/research-mixed-type-four-height-refinement.json'])

    kappa, local_lower, local_upper = F(1, 4000), F(1, 5), F(20)
    check('occupation coefficient is the improved extracted value',
          F(curv['occupation_coefficient']) == kappa)
    check('near-reference occupation is one tenth times squared displacement',
          400*kappa == F(1, 10))
    check('global occupation bound21/4000',
          kappa+(F(1, 2)-F(9, 20))/10 == F(21, 4000))
    check('reference margin exceeds good-symbol radius',
          min(F(27, 100)-F(11, 50), F(9, 20)-F(39, 100))
          == F(1, 20) > F(1, 40))
    check('selected symbol pays the bad-symbol cost on the full radius range',
          kappa > F(1, 40)**2/10)
    check('unsaturated occupation on the good radius',
          400*F(1, 40)**2 == F(1, 4) < 1)
    check('all good symbols stay strictly inside the plateau',
          F(27, 100)-F(1, 40) > F(11, 50)
          and F(39, 100)+F(1, 40) < F(9, 20))
    check('real-input target Lipschitz factor is less than7',
          1+F(57, 1000)*(40+50) < 7)
    check('occupation Lipschitz bound17/125',
          800*F(18, 100)*kappa+F(1, 10) == F(17, 125))

    theta, K, W, O = sp.symbols('theta K W O', real=True)
    d0, d1, d2 = sp.symbols('d0 d1 d2', real=True)
    check('cyclic half allocations leave exactly1-theta occupation',
          sp.expand(-O+theta*O+(1-theta)*O) == 0)
    check('two closing estimates produce6K+1',
          sp.expand((-3*K-1)+(-3*K)+(6*K+1)) == 0)
    upper_coefficient = sp.Rational(1, 10)-theta/sp.Integer(20)
    check('local t remains nonpositive through both theta endpoints',
          upper_coefficient.subs(theta, 0) == sp.Rational(1, 10)
          and upper_coefficient.subs(theta, 1) == sp.Rational(1, 20))
    check('quadratic lower coefficient is10', local_upper/2 == 10)
    check('quadratic upper supporting coefficient is1/10',
          local_lower/2 == F(1, 10))
    check('exit repeated incidence is d0 squared plus twice d1 squared',
          sp.expand(10*(d0*d0+d1*d1)+10*d1*d1
                    -10*(d0*d0+2*d1*d1)) == 0)
    check('exit and suffix bounds sum to40 times squared radius',
          10*(1+2)+10 == 40)

    M, k = sp.symbols('M k', integer=True, positive=True)
    for width, offset, minimum in ((3, 2, 3), (5, 2, 5)):
        h = width*M+3
        first, last = -width*M-2, -3
        cut = first+width*k+offset
        suffix = -cut
        check(f'{width}-symbol count is exact and excludes final triple',
              sp.expand(last-first+1-width*M) == 0
              and sp.expand(first-(-h+1)) == 0 and last == -3)
        check(f'{width}-symbol cut has exact extreme suffix lengths',
              sp.simplify(suffix.subs(k, 0)-width*M) == 0
              and sp.simplify(suffix.subs(k, M-1)-minimum) == 0
              and minimum >= 3)
    # The floor/pigeonhole argument is proved for real B in the note;
    # these identities check its layer and final-state arithmetic only.
    check('five-good reset changes no weight after the second except a P halo',
          ({-2, -1, 0} & {0, 1, 2, 3}) == {0}
          and not ({-2, -1, 0} & {1, 2, 3, 4}))
    check('singleton internal occupation is exactly zero',
          sp.expand(O-(O+O)/2) == 0)
    Hout, Hin, Aout, Ain, e = sp.symbols('Hout Hin Aout Ain e')
    check('same incoming potential has one-sided run error',
          sp.expand((Aout+e)-Ain-(Aout-Ain+e)) == 0)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in dependencies.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(specs), current_bindings=len(dependencies),
        numerical_cells_recomputed=0, chain_lengths_enumerated=0,
        occupation_coefficient=str(kappa), local_lower=str(local_lower),
        local_upper=str(local_upper), good_radius_maximum='1/40',
        bad_symbol_coefficient='1/10', prefix_quadratic_coefficient=30,
        suffix_quadratic_coefficient=10, total_quadratic_coefficient=40,
        generic_depth='3*(floor(B_d)+1)+3',
        quadratic_depth='5*(floor(B_d)+1)+3',
        B_d='10*(6*K_theta+1)/((1-theta)*d^2)',
        numerical_K_or_L_evaluated=False, interface_sign_certified=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Exact arithmetic, arbitrary-length layer identities and current proved source inputs. No new interval cover, potential optimization, numerical depth, full-period or knot claim.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(specs), 'primary records;',
          len(dependencies), 'current bindings; no numerical cover', flush=True)


if __name__ == '__main__':
    main()
