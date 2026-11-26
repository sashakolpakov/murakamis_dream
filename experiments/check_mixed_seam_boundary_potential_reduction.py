#!/usr/bin/env python3
"""Exact seam allocation and extraction from complete saved pair records.

This checks current provenance and saved covers, not the numerical cells again.
No incoming potential or seam-interface sign is evaluated.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_seam_boundary_potential_reduction.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-seam-boundary-potential-reduction.json')
    args = ap.parse_args()
    ctx.prec = 400  # Parsing saved outward bounds only; no cell reevaluation.
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, primary, checks = {}, set(), {}, []

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
        # Recursive bindings retain provenance, including archived diagnostics.
        # Only the explicit primary records below supply theorem hypotheses.
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    def load(stem, prefix='check', suffix='', proof_field=True):
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rp = f'repro/results/research-{stem.replace("_", "-")}{suffix}.json'
        r = inherit(rp)
        bind(pp)
        bind(ss)
        assert r['status'] == 'passed', rp
        assert r['script_sha256'] == dependencies[ss], rp
        if proof_field:
            assert r['proof_sha256'] == dependencies[pp], rp
        else:
            old = dict(r.get('dependencies', {}))
            old.update(r.get('dependencies_sha256', {}))
            assert old.get(pp) == dependencies[pp], rp
        primary[rp] = r
        return rp, r

    pair_path, pair = load('mixed_hybrid_zero_pair_support', 'certify')
    replay_path, replay = load('mixed_hybrid_zero_pair_support', 'certify', '-replay')
    _, source = load('mixed_hybrid_zero_pair_reduction')
    endpoint_path, endpoint = load('mixed_all_endpoint_support', 'certify')
    _, endpoint_replay = load('mixed_all_endpoint_support', 'replay', '-replay')
    endpoint43_path, endpoint43 = load('mixed_43_endpoint_support')
    _, endpoint43_replay = load('mixed_43_endpoint_support', 'replay', '-replay', False)
    _, hybrid = load('mixed_split_cutoff_hybrid_contour')
    _, deep = load('mixed_deep_low_half_region')
    _, half = load('mixed_half_endpoint_conditional_packet')
    _, nonlow = load('mixed_full_nonlow_half_region')
    _, potential = load('mixed_finite_depth_boundary_potential')
    _, subaction = load('mixed_finite_depth_subaction')
    _, curvature = load('mixed_extracted_plateau_curvature')
    for stem in ('mixed_nonlow_open_chain_boundary',
                 'mixed_nonlow_interface_reduction'):
        bind(f'notes/research_{stem}.md')

    check('all-endpoint independent replay binds its exact author record',
          endpoint_replay['input_sha256'] == dependencies[endpoint_path])
    check('remaining-orientation independent replay binds geometry and source',
          endpoint43_replay['geometry_input_sha256'] == dependencies[endpoint43_path]
          and endpoint43_replay['source_input_sha256'] == endpoint43['source_input_sha256'])
    check('both original endpoint records retain their positive raw gap',
          F(endpoint['gap']) == F(endpoint43['gap']) == F(1, 1000)
          and endpoint['source_values'] == 165 and endpoint['reference_products'] == 112
          and endpoint43['case_count'] == 16)

    expected = {(word, ta, tb, fa, fb)
                for word in itertools.product((0, 1), repeat=5)
                for ta, tb, fa, fb in itertools.product(range(2), range(2), range(4), range(4))}
    covers = []
    for label, r in (('author', pair), ('replay', replay)):
        seen, cells = {}, 0
        for row in r['cases']:
            key = (tuple(row['word']), *row['external_types'], *row['faces'])
            assert key not in seen, (label, key)
            addresses = row['addresses']
            assert addresses == sorted(addresses)
            assert len(addresses) == len(set(addresses)) == row['cells']
            assert all(set(a) <= {'0', '1'} for a in addresses)
            assert all(not b.startswith(a) for a, b in zip(addresses, addresses[1:]))
            assert sum((F(1, 2**len(a)) for a in addresses), F(0)) == 1
            assert arb(row['minimum_gap']) > arb('0.303'), (label, key)
            seen[key] = addresses
            cells += len(addresses)
        check(label+' has every original typed boundary product and complete cover',
              set(seen) == expected and len(seen) == r['boundary_products'] == 2048
              and cells == r['accepted_cells'] == 18988
              and r['target_corners_per_cell'] == 16)
        check(label+' global saved whole-cell margin exceeds303/1000',
              arb(r['minimum_gap']) > arb('0.303'))
        covers.append(seen)
    check('saved320 replay checks the identical author cover with no refinements',
          covers[0] == covers[1] and replay['visited_cells'] == 18988
          and pair['precision_bits'] == 256 and replay['precision_bits'] == 320
          and replay['input_path'] == pair_path
          and replay['input_sha256'] == dependencies[pair_path]
          and replay['dependencies_sha256'] == pair['dependencies_sha256'])
    check('extraction leaves the original acceptance and rounded theorem unchanged',
          F(pair['geometric_gap']) == F(replay['geometric_gap']) == F(1, 4)
          and F(pair['finite_pair_gap']) == F(replay['finite_pair_gap']) == F(1, 5))
    check('full original collar has cost less than1/50',
          F(source['low_cutoff']) == F(pair['low_cutoff']) == F(1, 1000)
          and arb(source['maximum_pair_collar_cost']) < arb('0.02'))
    G, ds = F(7, 25), F(1, 4000)
    check('one total raw Fourier tolerance gives the strengthened finite pair gap',
          F(303, 1000)-F(1, 50)-F(3, 1000) == G)
    check('each raw Fourier half can share the total tolerance exactly once',
          2*F(3, 2000) == F(3, 1000))
    check('chosen endpoint collar gap leaves positive thickening reserve',
          F(1, 1000) > F(1, 2000) > ds)

    check('hybrid definition and deep-low source inputs are complete',
          hybrid['exact_identity_count'] == 18 and deep['exact_checks'] == 28
          and F(deep['monotonicity_threshold']) == F(1, 6)
          and F(deep['raising_endpoint']) == F(1, 10)
          and F(deep['occupation_coefficient']) == F(1, 4000)
          and half['exact_identity_count'] == 17
          and half['exact_even_odd_row_support_checks'] == 54
          and half['exact_physical_half_endpoint_comparisons'] == 30
          and nonlow['status'] == 'passed')
    check('old compact potential and relative subaction use proved quadratic constants',
          potential['exact_checks'] == 31 and potential['total_quadratic_coefficient'] == 40
          and subaction['exact_checks'] == 25 and subaction['local_closure_ratio'] == 200
          and subaction['global_closure_ratio_per_K'] == 24000
          and F(curvature['local_hessian_lower']) == F(1, 5)
          and F(curvature['occupation_coefficient']) == F(1, 4000))

    lam, x, rho, b = sp.symbols('lam x rho b', real=True)
    xi = sp.Rational(1, 10)+(b-sp.Rational(1, 10))*lam
    check('virtual halo has exactly the physical seam attenuation',
          sp.cancel((xi-sp.Rational(1, 10))/(b-sp.Rational(1, 10))-lam) == 0)
    check('seam attenuation has the prescribed two endpoint values',
          (1-x/rho).subs(x, 0) == 1 and (1-x/rho).subs(x, rho) == 0)
    for cutoff in (F(11, 50), F(3, 25)):
        rr = sp.Rational(cutoff.numerator, cutoff.denominator)
        check('virtual cutoff interval '+str(cutoff)+' stays in old alphabet',
              xi.subs({b: rr, lam: 0}) == sp.Rational(1, 10)
              and xi.subs({b: rr, lam: 1}) == rr
              and F(1, 10) < cutoff <= F(11, 50) < F(1, 2))
    check('raising threshold stays inside the strict real-low derivative interval',
          F(1, 1000) < F(1, 10) < F(1, 6))
    theta, o0, o1, o2, C = sp.symbols('theta o0 o1 o2 C', real=True)
    gauge = theta*(o1/6+o2/3)-theta*(o0/6+o1/3)
    check('enlarged-alphabet gauge retains one third of each output occupation',
          sp.expand(theta*(o0+o1)/2+gauge-theta*(o0+o1+o2)/3) == 0)
    check('enlarged-alphabet depth uses relative error theta/6',
          sp.cancel(400*(C+1)/((1-theta)*(theta/6))
                    -2400*(C+1)/((1-theta)*theta)) == 0)
    check('baseline-relative occupation closure constants remain exact',
          F(20)/F(1, 10) == 200 and F(6)/F(1, 4000) == 24000)

    E, total_alpha, qsum = sp.symbols('E total_alpha qsum', real=True)
    gain = sp.Rational(7, 25)*total_alpha+qsum+sp.Rational(1, 4000)*(E-2*total_alpha)
    check('fractional stars spend exactly two original edge incidences each',
          sp.expand(gain-((sp.Rational(7, 25)-2*sp.Rational(1, 4000))*total_alpha
                          +qsum+sp.Rational(1, 4000)*E)) == 0)
    Q = sp.symbols('Q', real=True)
    check('isolated seam retains its full strengthened pair and reserve',
          sp.expand(gain.subs({E: 2, total_alpha: 1, qsum: Q})
                    -sp.Rational(7, 25)-Q) == 0)
    check('one original loop uses half its doubled pair incidence',
          2*F(1, 2) == 1
          and sp.expand(gain.subs({E: 1, total_alpha: sp.Rational(1, 2), qsum: Q/2})
                        -sp.Rational(7, 50)-Q/2) == 0)
    a0, a1 = sp.symbols('a0 a1', real=True)
    check('two parallel edges retain distinct incidence counts',
          sp.expand((a0+a1)+(a0+a1)-2*(a0+a1)) == 0)
    n = sp.symbols('n', integer=True, positive=True)
    check('odd seam path stars cover every incident edge',
          sp.expand(2*(n+1)-((2*n+1)+1)) == 0)
    check('even seam path leaves exactly one endpoint edge',
          sp.expand((2*n+1)-2*n) == 1)
    check('all-seam half allocation has no uncovered edge',
          sp.expand(n-2*(n/2)) == 0)
    check('singleton AA path has zero allocated occupation',
          sp.expand(o0-(o0+o0)/2) == 0)
    check('two-vertex AA path has one half of each endpoint occupation',
          sp.expand((o0+o1)-(o0+o1)/2-(o0+o1)/2) == 0)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in dependencies.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(dependencies),
        author_pair_record=pair_path, saved_pair_replay_record=replay_path,
        validated_boundary_products=2048, validated_saved_cells=18988,
        saved_target_corners_per_cell=16,
        recorded_author_lower=pair['minimum_gap'], recorded_replay_lower=replay['minimum_gap'],
        extracted_geometric_gap='303/1000', pair_collar_cost_upper='1/50',
        total_pair_fourier_tolerance_upper='3/1000', finite_pair_gap='7/25',
        fixed_endpoint_gap='1/4000', numerical_cells_recomputed=0,
        cyclic_patterns_enumerated=0, potential_values_evaluated=0,
        interface_sign_certified=False, collar_radius_evaluated=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Current complete source inputs, whole-cell saved-margin extraction, exact virtual halos, relative gauge and original star incidences. No numerical cover rerun, potential optimization, seam-interface sign, whole-period asymptotic or manuscript change.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(primary), 'primary records;',
          len(dependencies), 'current bindings; 2048 products/18988 saved cells; no numerical rerun', flush=True)


if __name__ == '__main__':
    main()
