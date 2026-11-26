#!/usr/bin/env python3
"""Fixed saved-only split-Taylor inclusion test on the original 16 tubes."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_split_taylor_inclusion.md'
SOURCE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
AUDIT = 'repro/results/research-mixed-terminal-correlated-affine-family-saved-audit.json'
HELPER = 'experiments/check_mixed_terminal_correlated_affine_family_record.py'
REFERENCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
PINNED = {
    PROOF: '461c0fe2eb943a791d91b94ce1627e4c650fcaf80623873cd0b53f963e05bd17',
    SOURCE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    AUDIT: '2638c47a2b0216f04bb4f31e4f6bdd86d9c2b17cdfd00ea880835dcf80d97959',
    HELPER: '61bd1417e2ea4b0e9339a96f5d0440af967177e94dbafb0a454c29b77fe5f157',
    REFERENCE: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
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
    source, audit, reference = [json.loads((ROOT/p).read_text()) for p in (SOURCE, AUDIT, REFERENCE)]
    for record in (source, audit, reference):
        for key in ('input_sha256', 'dependencies_sha256'):
            for name, digest in record.get(key, {}).items():
                bind(name, digest)
    assert source['status'] == 'completed fixed protocol' and source['changed_inputs'] == []
    assert audit['status'] == 'passed' and audit['changed_inputs'] == []
    assert audit['source_path'] == SOURCE and audit['source_sha256'] == inputs[SOURCE]
    assert audit['checker_path'] == HELPER and audit['checker_sha256'] == inputs[HELPER]
    assert audit['original_candidates_verified'] == 16
    assert audit['original_criterion_successes'] == audit['rebuilt_criterion_successes'] == 4
    assert audit['saved_source_binding_count'] == len(source['input_sha256']) == 36
    assert source['precision_bits'] == 256 and source['exact_saved_proposals_only'] is True
    assert source['counts']['candidates'] == 16 and source['counts']['candidate_errors'] == 0
    assert reference['changed_inputs'] == []
    # The helper is frozen and imports only the standard library. Its main()
    # is never called; only exact interval arithmetic and inventory functions.
    spec = importlib.util.spec_from_file_location('frozen_affine_saved_arithmetic', ROOT/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    pi = h.interval(reference['pi'])
    ipi = (h.ZERO, pi)
    keys = [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert [(c['beta'], c['epsilon']) for c in source['cases']] == keys
    assert [(c['beta'], c['epsilon']) for c in audit['cases']] == keys
    residuals = {}
    for item in audit['posterior_refinements']+audit['uncertified_D3_formal_majorants']:
        key = (item['beta'], item['epsilon'])
        R = tuple(map(F, item['rebuilt_residual_rational']))
        assert len(R) == 5 and min(R) >= 0
        assert key not in residuals or residuals[key] == R
        residuals[key] = R
    assert set(residuals) == set(keys)
    cases = []
    for index, (case, oldaudit) in enumerate(zip(source['cases'], audit['cases'])):
        beta, epsilon = keys[index]
        assert case['case_index'] == index and len(case['candidates']) == len(oldaudit['candidates']) == 4
        B = [[h.exact_complex(z) for z in row] for row in case['inverse_exact']]
        M = case['chirp_matrix']
        assert M == [[epsilon, 1, -1, 0, 0], [1, 0, 0, 0, 0], [-1, 0, epsilon, 1, 0],
                     [0, 0, 1, 1, -1], [0, 0, 0, -1, 1]]
        J0 = [[h.cs(ipi, F(M[i][j])) for j in range(5)] for i in range(5)]
        terms = case['primitive_terms']
        assert len(terms) == 11
        for term, (name, sigma, v, external, offset) in zip(terms, h.inventory(epsilon)):
            assert (term['name'], term['sigma'], term['v'], term['external'],
                    F(term['offset_rational'])) == (name, sigma, v, external, offset)
            jp = h.complex_interval(term['center_j_prime'])
            for i in range(5):
                for j in range(5):
                    J0[i][j] = h.ca(J0[i][j], h.cs(jp, F(sigma*v[i]*v[j])))
        J0 = [[h.ch(x, h.complex_interval(y)) for x, y in zip(row, saved)]
              for row, saved in zip(J0, case['center_jacobian'])]
        E0 = [[h.ch(h.ca(h.exact_complex((int(i == j), 0)),
                        h.cn(h.csum(h.cm(B[i][k], J0[k][j]) for k in range(5)))),
                    h.complex_interval(case['center_error_matrix'][i][j]))
               for j in range(5)] for i in range(5)]
        A = [[max(F(case['center_error_matrix_upper_rational'][i][j]), h.abs_upper(E0[i][j]))
              for j in range(5)] for i in range(5)]
        affine_terms = []
        for term in terms:
            name, v = term['name'], term['v']
            z0 = tuple(map(F, term['center_exact']))
            radius = F(term['affine_curvature']['radius_upper_rational'])
            m = h.curvature(term['affine_curvature'], z0, radius, 'affine', name, pi)
            coeff = list(map(F, term['preconditioned_sigma_modulus_uppers_rational']))
            contribution = [[coeff[i]*m*radius*abs(v[j]) for j in range(5)] for i in range(5)]
            for i in range(5):
                for j in range(5):
                    A[i][j] += contribution[i][j]
            affine_terms.append(dict(name=name, affine_radius_rational=str(radius),
                curvature_upper_rational=str(m),
                contribution_rational=[list(map(str, row)) for row in contribution]))
        A = [[h.upper_round(x) for x in row] for row in A]
        R = residuals[(beta, epsilon)]
        results = []
        for j, (candidate, audited, multiplier) in enumerate(zip(case['candidates'], oldaudit['candidates'], h.MULTIPLIERS)):
            assert F(candidate['multiplier_rational']) == F(audited['multiplier_rational']) == multiplier
            rho = [multiplier*x for x in h.RHO]
            assert list(map(F, candidate['error_radii_rational'])) == rho
            assert candidate['all_full_original_log_disks_regular'] is True
            assert candidate['saved_central_root_contained'] is True
            assert candidate['criterion_verified'] == audited['original_pass'] == audited['rebuilt_pass']
            eta = F(audited['contraction_upper_rational'])
            assert F(candidate['contraction_upper_rational']) <= eta < 1
            assert len(candidate['full_primitive_terms']) == 11
            quadratic = [F(0)]*5
            quadratic_terms = []
            for term, full in zip(terms, candidate['full_primitive_terms']):
                name, v = term['name'], term['v']
                assert full['name'] == name
                d = sum(abs(x)*y for x, y in zip(v, rho))
                total = F(term['affine_curvature']['radius_upper_rational'])+d
                m = h.curvature(full['full_curvature'], tuple(map(F, term['center_exact'])),
                                total, 'full', name, pi)
                coeff = list(map(F, term['preconditioned_sigma_modulus_uppers_rational']))
                contribution = [x*m*d*d/2 for x in coeff]
                quadratic = [x+y for x, y in zip(quadratic, contribution)]
                quadratic_terms.append(dict(name=name, error_argument_radius_rational=str(d),
                    full_curvature_upper_rational=str(m),
                    contribution_rational=list(map(str, contribution))))
            linear = [sum(x*y for x, y in zip(row, rho)) for row in A]
            Q = [h.upper_round(x) for x in quadratic]
            total = [h.upper_round(R[i]+linear[i]+Q[i]) for i in range(5)]
            margin = [rho[i]-total[i] for i in range(5)]
            passed = min(margin) > 0
            oldmargin = list(map(F, audited['inclusion_margins_rational']))
            assert len(oldmargin) == 5
            results.append(dict(candidate_index=j, multiplier_rational=str(multiplier),
                source_candidate_canonical_sha256=canonical_sha(candidate),
                error_radii_rational=list(map(str, rho)),
                unchanged_contraction_upper_rational=str(eta),
                old_criterion_pass=audited['rebuilt_pass'], criterion_pass=passed,
                residual_upper_rational=list(map(str, R)),
                affine_linear_upper_rational=list(map(str, linear)),
                error_quadratic_upper_rational=list(map(str, Q)),
                quadratic_terms=quadratic_terms, total_upper_rational=list(map(str, total)),
                inclusion_margins_rational=list(map(str, margin)),
                old_inclusion_margins_rational=list(map(str, oldmargin)),
                inclusion_improvement_rational=[str(x-y) for x, y in zip(margin, oldmargin)],
                failed_coordinates=[name for name, value in zip(h.NAMES, margin) if value <= 0],
                status='uniform original canonical enclosure certified' if passed else 'inconclusive'))
        cases.append(dict(case_index=index, beta=beta, epsilon=epsilon,
            source_case_canonical_sha256=canonical_sha(case),
            original_center=case['center'], original_response=case['response_exact'],
            parameter_center=case['parameter_center'], parameter_radius_rational=case['parameter_radius_rational'],
            affine_error_matrix_upper_rational=[list(map(str, row)) for row in A],
            affine_terms=affine_terms, candidates=results,
            family_certified=any(x['criterion_pass'] for x in results)))
    assert len(cases) == 4 and sum(len(c['candidates']) for c in cases) == 16
    changed = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    assert changed == []
    result = dict(status='completed fixed saved-only protocol', source_path=SOURCE,
        source_sha256=inputs[SOURCE], original_audit_path=AUDIT, original_audit_sha256=inputs[AUDIT],
        proof_sha256=inputs[PROOF], checker_sha256=inputs[own], input_sha256=inputs,
        changed_inputs=changed, candidates_checked=16, cases=cases,
        certified_families=sum(c['family_certified'] for c in cases),
        all_four_input_families_certified=all(c['family_certified'] for c in cases),
        analytic_callbacks=0, root_solves=0, numerical_proposals=0, new_radius_vectors=0,
        subdivisions=0, precision_retries=0, source_evaluations=0,
        uniform_source_gap_proved=False, knot_theorem_proved=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2); stream.write('\n')
    print(json.dumps(dict(status=result['status'], sha256=sha(args.output),
        certified_families=result['certified_families'],
        candidates=[dict(beta=c['beta'], epsilon=c['epsilon'],
            results=[dict(multiplier=q['multiplier_rational'], passed=q['criterion_pass'],
                          minimum_margin=float(min(map(F, q['inclusion_margins_rational']))))
                     for q in c['candidates']]) for c in cases])), flush=True)


if __name__ == '__main__':
    main()
