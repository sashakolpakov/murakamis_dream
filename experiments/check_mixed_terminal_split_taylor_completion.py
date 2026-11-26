#!/usr/bin/env python3
"""Saved-only verification and posterior bounds for four complete families."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_all_input_affine_enclosures.md'
SOURCE = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
DRIVER = 'experiments/check_mixed_terminal_split_taylor_inclusion.py'
OLD = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
AUDIT = 'repro/results/research-mixed-terminal-correlated-affine-family-saved-audit.json'
HELPER = 'experiments/check_mixed_terminal_correlated_affine_family_record.py'
REFERENCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
PINNED = {
    PROOF: '6412be85ca87c01a0b363191c724dc1e7357c00939ce5c379a7c501f3565215f',
    SOURCE: 'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    DRIVER: '26786865862f0d7bea3597d5c9f6edb485ade2f13dbc86f25d0024c69021e793',
    OLD: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    AUDIT: '2638c47a2b0216f04bb4f31e4f6bdd86d9c2b17cdfd00ea880835dcf80d97959',
    HELPER: '61bd1417e2ea4b0e9339a96f5d0440af967177e94dbafb0a454c29b77fe5f157',
    REFERENCE: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    'notes/research_mixed_terminal_split_taylor_inclusion.md':
        '461c0fe2eb943a791d91b94ce1627e4c650fcaf80623873cd0b53f963e05bd17',
}


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    assert all(isinstance(x, str) and len(x) == 64 for x in PINNED.values())
    inputs = {}

    def bind(name, digest):
        assert name not in inputs or inputs[name] == digest
        assert sha(ROOT/name) == digest, name
        inputs[name] = digest

    for name, digest in PINNED.items():
        bind(name, digest)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bind(own, sha(ROOT/own))
    source, old, audit, reference = [json.loads((ROOT/name).read_text())
        for name in (SOURCE, OLD, AUDIT, REFERENCE)]
    for record in (source, old, audit, reference):
        for key in ('input_sha256', 'dependencies_sha256'):
            for name, digest in record.get(key, {}).items():
                bind(name, digest)
        assert record['changed_inputs'] == []
    assert source['status'] == 'completed fixed saved-only protocol'
    assert source['source_path'] == OLD and source['source_sha256'] == inputs[OLD]
    assert source['original_audit_path'] == AUDIT and source['original_audit_sha256'] == inputs[AUDIT]
    assert source['checker_sha256'] == inputs[DRIVER]
    assert source['proof_sha256'] == inputs['notes/research_mixed_terminal_split_taylor_inclusion.md']
    assert len(source['input_sha256']) == 42
    assert source['candidates_checked'] == 16 and source['certified_families'] == 4
    assert source['all_four_input_families_certified'] is True
    for key in ('analytic_callbacks', 'root_solves', 'numerical_proposals', 'new_radius_vectors',
                'subdivisions', 'precision_retries', 'source_evaluations'):
        assert source[key] == 0
    assert source['uniform_source_gap_proved'] is source['knot_theorem_proved'] is False
    assert audit['status'] == 'passed' and audit['source_sha256'] == inputs[OLD]
    assert audit['checker_sha256'] == inputs[HELPER]
    assert old['status'] == 'completed fixed protocol'
    spec = importlib.util.spec_from_file_location('frozen_saved_interval_arithmetic', ROOT/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)  # Standard-library definitions only; main is not called.
    pi = h.interval(reference['pi']); ipi = (h.ZERO, pi)
    keys = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for record in (source, old, audit):
        assert [(c['beta'], c['epsilon']) for c in record['cases']] == keys
    residuals = {}
    for item in audit['posterior_refinements']+audit['uncertified_D3_formal_majorants']:
        key = item['beta'], item['epsilon']
        value = tuple(map(F, item['rebuilt_residual_rational']))
        assert key not in residuals or residuals[key] == value
        residuals[key] = value
    assert set(residuals) == set(keys)
    chosen = []
    inventory = []
    coarse_margins = list(map(F, ('11/10000', '118/100000', '63/100000', '77/100000')))
    for index, (case, prior, audited_case) in enumerate(zip(source['cases'], old['cases'], audit['cases'])):
        beta, epsilon = keys[index]
        assert case['case_index'] == prior['case_index'] == index
        assert case['source_case_canonical_sha256'] == canonical_sha(prior)
        assert case['original_center'] == prior['center']
        assert case['original_response'] == prior['response_exact']
        assert case['parameter_center'] == prior['parameter_center']
        assert case['parameter_radius_rational'] == prior['parameter_radius_rational']
        assert case['family_certified'] is True
        B = [[h.exact_complex(z) for z in row] for row in prior['inverse_exact']]
        M = prior['chirp_matrix']
        assert M == [[epsilon, 1, -1, 0, 0], [1, 0, 0, 0, 0], [-1, 0, epsilon, 1, 0],
                     [0, 0, 1, 1, -1], [0, 0, 0, -1, 1]]
        J0 = [[h.cs(ipi, F(M[i][j])) for j in range(5)] for i in range(5)]
        assert len(prior['primitive_terms']) == len(case['affine_terms']) == 11
        for term, (name, sigma, v, external, offset) in zip(prior['primitive_terms'], h.inventory(epsilon)):
            assert (term['name'], term['sigma'], term['v'], term['external'],
                    F(term['offset_rational'])) == (name, sigma, v, external, offset)
            jp = h.complex_interval(term['center_j_prime'])
            for i in range(5):
                for j in range(5):
                    J0[i][j] = h.ca(J0[i][j], h.cs(jp, F(sigma*v[i]*v[j])))
        J0 = [[h.ch(x, h.complex_interval(y)) for x, y in zip(row, saved)]
              for row, saved in zip(J0, prior['center_jacobian'])]
        E0 = [[h.ch(h.ca(h.exact_complex((int(i == j), 0)),
                        h.cn(h.csum(h.cm(B[i][k], J0[k][j]) for k in range(5)))),
                    h.complex_interval(prior['center_error_matrix'][i][j]))
               for j in range(5)] for i in range(5)]
        A = [[max(F(prior['center_error_matrix_upper_rational'][i][j]), h.abs_upper(E0[i][j]))
              for j in range(5)] for i in range(5)]
        for term, saved in zip(prior['primitive_terms'], case['affine_terms']):
            name, v = term['name'], term['v']
            radius = F(term['affine_curvature']['radius_upper_rational'])
            m = h.curvature(term['affine_curvature'], tuple(map(F, term['center_exact'])),
                            radius, 'affine', name, pi)
            coeff = list(map(F, term['preconditioned_sigma_modulus_uppers_rational']))
            contribution = [[coeff[i]*m*radius*abs(v[j]) for j in range(5)] for i in range(5)]
            assert saved['name'] == name and F(saved['affine_radius_rational']) == radius
            assert F(saved['curvature_upper_rational']) == m
            assert [list(map(F, row)) for row in saved['contribution_rational']] == contribution
            for i in range(5):
                for j in range(5):
                    A[i][j] += contribution[i][j]
        A = [[h.upper_round(x) for x in row] for row in A]
        assert [list(map(F, row)) for row in case['affine_error_matrix_upper_rational']] == A
        R = residuals[(beta, epsilon)]
        assert len(case['candidates']) == len(prior['candidates']) == len(audited_case['candidates']) == 4
        case_inventory = []
        for candidate_index, (candidate, original, oldaudit, multiplier) in enumerate(zip(
                case['candidates'], prior['candidates'], audited_case['candidates'], h.MULTIPLIERS)):
            assert candidate['candidate_index'] == candidate_index
            assert candidate['source_candidate_canonical_sha256'] == canonical_sha(original)
            assert F(candidate['multiplier_rational']) == F(original['multiplier_rational']) == F(oldaudit['multiplier_rational']) == multiplier
            rho = [multiplier*x for x in h.RHO]
            assert list(map(F, candidate['error_radii_rational'])) == rho
            assert candidate['old_criterion_pass'] == original['criterion_verified'] == oldaudit['rebuilt_pass']
            assert original['all_full_original_log_disks_regular'] is original['saved_central_root_contained'] is True
            eta_old = F(oldaudit['contraction_upper_rational'])
            assert F(candidate['unchanged_contraction_upper_rational']) == eta_old < 1
            assert tuple(map(F, candidate['residual_upper_rational'])) == R
            assert len(candidate['quadratic_terms']) == len(original['full_primitive_terms']) == 11
            Q = [F(0)]*5
            Cerr = [[F(0)]*5 for _ in range(5)]
            posterior_terms = []
            for term, full, saved in zip(prior['primitive_terms'], original['full_primitive_terms'], candidate['quadratic_terms']):
                name, v = term['name'], term['v']
                assert full['name'] == saved['name'] == name
                d = sum(abs(x)*y for x, y in zip(v, rho))
                assert d > 0 and F(saved['error_argument_radius_rational']) == d
                radius = F(term['affine_curvature']['radius_upper_rational'])+d
                m = h.curvature(full['full_curvature'], tuple(map(F, term['center_exact'])),
                                radius, 'full', name, pi)
                assert F(saved['full_curvature_upper_rational']) == m
                coeff = list(map(F, term['preconditioned_sigma_modulus_uppers_rational']))
                qterm = [x*m*d*d/2 for x in coeff]
                assert list(map(F, saved['contribution_rational'])) == qterm
                Q = [x+y for x, y in zip(Q, qterm)]
                cterm = [[qterm[i]*abs(v[j])/d for j in range(5)] for i in range(5)]
                for i in range(5):
                    assert sum(cterm[i][j]*rho[j] for j in range(5)) == qterm[i]
                    for j in range(5):
                        Cerr[i][j] += cterm[i][j]
                posterior_terms.append(dict(name=name, error_argument_radius_rational=str(d),
                    matrix_contribution_rational=[list(map(str, row)) for row in cterm]))
            Q = [h.upper_round(x) for x in Q]
            linear = [sum(x*y for x, y in zip(row, rho)) for row in A]
            total = [h.upper_round(R[i]+linear[i]+Q[i]) for i in range(5)]
            margin = [rho[i]-total[i] for i in range(5)]
            assert list(map(F, candidate['affine_linear_upper_rational'])) == linear
            assert list(map(F, candidate['error_quadratic_upper_rational'])) == Q
            assert list(map(F, candidate['total_upper_rational'])) == total
            assert list(map(F, candidate['inclusion_margins_rational'])) == margin
            oldmargin = list(map(F, oldaudit['inclusion_margins_rational']))
            assert list(map(F, candidate['old_inclusion_margins_rational'])) == oldmargin
            assert list(map(F, candidate['inclusion_improvement_rational'])) == [x-y for x, y in zip(margin, oldmargin)]
            passed = min(margin) > 0
            assert passed == candidate['criterion_pass'] == (multiplier == 2 or (beta == 1 and multiplier == 1))
            assert candidate['failed_coordinates'] == [n for n, value in zip(h.NAMES, margin) if value <= 0]
            assert candidate['status'] == ('uniform original canonical enclosure certified' if passed else 'inconclusive')
            case_inventory.append(dict(multiplier_rational=str(multiplier), passed=passed,
                minimum_margin_rational=str(min(margin)), contraction_upper_rational=str(eta_old)))
            if multiplier == 2-beta:
                assert passed and min(margin) > coarse_margins[index]
                C = [[h.upper_round(A[i][j]+Cerr[i][j]) for j in range(5)] for i in range(5)]
                C_rho = [sum(x*y for x, y in zip(row, rho)) for row in C]
                posterior_margin = [rho[i]-R[i]-C_rho[i] for i in range(5)]
                eta_C = max(x/y for x, y in zip(C_rho, rho))
                assert min(posterior_margin) > 0 and eta_C < 1
                matrix = [[F(int(i == j))-C[i][j] for j in range(5)] for i in range(5)]
                z = h.exact_solve(matrix, R)
                assert all(0 <= x < r for x, r in zip(z, rho))
                widths = list(map(F, prior['affine_halfwidths_rational']))
                center = [tuple(map(F, q)) for q in prior['center']]
                abs_u = list(map(F, prior['response_modulus_uppers_rational']))
                r = F(prior['parameter_radius_rational'])
                assert widths == [r*x for x in abs_u]
                assert all(x*x >= h.norm_squared(u) for x, u in zip(abs_u, prior['response_exact']))
                chosen.append(dict(beta=beta, epsilon=epsilon, multiplier_rational=str(multiplier),
                    source_case_canonical_sha256=canonical_sha(case),
                    source_candidate_canonical_sha256=canonical_sha(candidate),
                    center_exact=case['original_center'], response_exact=case['original_response'],
                    parameter_center=case['parameter_center'], parameter_radius_rational=case['parameter_radius_rational'],
                    original_radii_rational=list(map(str, rho)), residual_upper_rational=list(map(str, R)),
                    error_cost_matrix_rational=[list(map(str, row)) for row in C],
                    error_cost_terms=posterior_terms, error_cost_contraction_upper_rational=str(eta_C),
                    error_cost_inclusion_margins_rational=list(map(str, posterior_margin)),
                    posterior_radii_rational=list(map(str, z)), posterior_radii_display=[float(x) for x in z],
                    exact_linear_system_verified=True, error_cost_matrix_is_not_a_Jacobian_bound=True,
                    coordinate_enclosures={name: {
                        'real': {'finite': True, 'lower_rational': str(q[0]-w-error), 'upper_rational': str(q[0]+w+error)},
                        'imag': {'finite': True, 'lower_rational': str(q[1]-w-error), 'upper_rational': str(q[1]+w+error)}}
                        for name, q, w, error in zip(h.NAMES, center, widths, z)}))
        inventory.append(dict(beta=beta, epsilon=epsilon, candidates=case_inventory))
    assert len(chosen) == 4 and sum(c['passed'] for row in inventory for c in row['candidates']) == 6
    changed = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    assert changed == []
    result = dict(status='passed', source_path=SOURCE, source_sha256=inputs[SOURCE],
        checker_path=own, checker_sha256=inputs[own], proof_sha256=inputs[PROOF],
        input_sha256=inputs, changed_inputs=changed, source_binding_count=42,
        candidates_verified=16, successful_candidates=6, complete_families=4,
        all_four_input_disks_certified=True, candidate_inventory=inventory, posterior_enclosures=chosen,
        analytic_callbacks=0, root_solves=0, source_evaluations=0, new_candidate_radii=0,
        uniform_source_gap_proved=False, knot_theorem_proved=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2); stream.write('\n')
    print(json.dumps(dict(status='passed', sha256=sha(args.output), families=4,
        posterior=[dict(beta=x['beta'], epsilon=x['epsilon'], radii=x['posterior_radii_display'])
                   for x in chosen])), flush=True)


if __name__ == '__main__':
    main()
