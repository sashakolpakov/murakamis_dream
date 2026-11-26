#!/usr/bin/env python3
"""Four saved-only correlated residual comparisons and posterior solves."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_quadratic_residual_refinement.md'
SOURCE = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
REFERENCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
HELPER = 'experiments/check_mixed_terminal_correlated_affine_family_record.py'
PINNED = {
    PROOF: 'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    SOURCE: 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    SPLIT: 'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    AFFINE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    REFERENCE: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    HELPER: '61bd1417e2ea4b0e9339a96f5d0440af967177e94dbafb0a454c29b77fe5f157',
    'experiments/check_mixed_terminal_split_taylor_completion.py':
        'bfa49b46454c324d05047352251e6f7aefa68cbec8d53ab5914c935bec502580',
    'notes/research_mixed_terminal_all_input_affine_enclosures.md':
        '6412be85ca87c01a0b363191c724dc1e7357c00939ce5c379a7c501f3565215f',
}


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def ir(value):
    assert value[0] <= value[1]
    return dict(finite=True, lower_rational=str(value[0]), upper_rational=str(value[1]))


def cr(value):
    return dict(real=ir(value[0]), imag=ir(value[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    bindings = {}

    def bind(name, digest):
        assert name not in bindings or bindings[name] == digest
        assert sha(ROOT/name) == digest, name
        bindings[name] = digest

    for name, digest in PINNED.items():
        bind(name, digest)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bind(own, sha(ROOT/own))
    posterior, split, affine, reference = [json.loads((ROOT/name).read_text())
        for name in (SOURCE, SPLIT, AFFINE, REFERENCE)]
    for record in (posterior, split, affine, reference):
        for key in ('input_sha256', 'dependencies_sha256'):
            for name, digest in record.get(key, {}).items():
                bind(name, digest)
        assert record['changed_inputs'] == []
    assert posterior['status'] == 'passed' and posterior['all_four_input_disks_certified'] is True
    assert posterior['source_path'] == SPLIT and posterior['source_sha256'] == bindings[SPLIT]
    assert posterior['checker_sha256'] == bindings['experiments/check_mixed_terminal_split_taylor_completion.py']
    assert posterior['proof_sha256'] == bindings['notes/research_mixed_terminal_all_input_affine_enclosures.md']
    assert split['status'] == 'completed fixed saved-only protocol' and split['all_four_input_families_certified'] is True
    assert split['source_path'] == AFFINE and split['source_sha256'] == bindings[AFFINE]
    assert affine['status'] == 'completed fixed protocol'
    assert reference['status'] == 'complete fixed diagnostic'
    keys = [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert [(c['beta'], c['epsilon']) for c in posterior['posterior_enclosures']] == keys
    for record in (split, affine, reference):
        assert [(c['beta'], c['epsilon']) for c in record['cases']] == keys
    spec = importlib.util.spec_from_file_location('frozen_rational_interval_helper', ROOT/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)  # Frozen standard-library definitions; no main().
    pi = h.interval(reference['pi']); ipi = (h.ZERO, pi)
    pi_square = (h.mul(pi, pi), h.ZERO)
    results = []
    for index, (prior, split_case, case, center_certificate) in enumerate(zip(
            posterior['posterior_enclosures'], split['cases'], affine['cases'], reference['cases'])):
        beta, epsilon = keys[index]
        assert prior['source_case_canonical_sha256'] == canonical_sha(split_case)
        assert split_case['source_case_canonical_sha256'] == canonical_sha(case)
        assert case['canonical_reference_case_sha256'] == canonical_sha(center_certificate)
        multiplier = F(2-beta)
        assert F(prior['multiplier_rational']) == multiplier
        candidate_index = 3-beta
        split_candidate, affine_candidate = split_case['candidates'][candidate_index], case['candidates'][candidate_index]
        assert F(split_candidate['multiplier_rational']) == F(affine_candidate['multiplier_rational']) == multiplier
        assert prior['source_candidate_canonical_sha256'] == canonical_sha(split_candidate)
        assert split_candidate['source_candidate_canonical_sha256'] == canonical_sha(affine_candidate)
        assert split_candidate['criterion_pass'] is True and prior['exact_linear_system_verified'] is True
        assert prior['center_exact'] == split_case['original_center'] == case['center']
        assert prior['response_exact'] == split_case['original_response'] == case['response_exact']
        center = [tuple(map(F, q)) for q in case['center']]
        uexact = [tuple(map(F, q)) for q in case['response_exact']]
        Bexact = [[tuple(map(F, q)) for q in row] for row in case['inverse_exact']]
        B = [[h.exact_complex(q) for q in row] for row in Bexact]
        u = list(map(h.exact_complex, uexact))
        b0 = tuple(map(F, prior['parameter_center']))
        r = F(prior['parameter_radius_rational'])
        assert b0 == h.CENTERS[beta] and r == h.RADII[beta]
        assert prior['parameter_center'] == case['parameter_center']
        assert prior['parameter_radius_rational'] == case['parameter_radius_rational']
        M = [[epsilon, 1, -1, 0, 0], [1, 0, 0, 0, 0], [-1, 0, epsilon, 1, 0],
             [0, 0, 1, 1, -1], [0, 0, 0, -1, 1]]
        n = [0, 0, 0, 0, 1]
        c = [-F(epsilon, 2), F(0), -F(epsilon, 2), -F(1, 2), -F(1, 2)]
        assert case['chirp_matrix'] == M and case['chirp_external'] == n
        assert list(map(F, case['chirp_constant_rational'])) == c
        f0 = [h.cm(ipi, h.exact_complex(h.exact_linear(M[i], center,
              (n[i]*b0[0]+c[i], n[i]*b0[1])))) for i in range(5)]
        J0 = [[h.cs(ipi, F(M[i][j])) for j in range(5)] for i in range(5)]
        second_sum = [h.CZ for _ in range(5)]
        cubic_terms = []
        term_records = []
        assert len(case['primitive_terms']) == 11
        for term, (name, sigma, v, external, offset) in zip(case['primitive_terms'], h.inventory(epsilon)):
            assert (term['name'], term['sigma'], term['v'], term['external'],
                    F(term['offset_rational'])) == (name, sigma, v, external, offset)
            z0 = h.exact_linear(v, center, (external*b0[0]+offset, external*b0[1]))
            lam = h.exact_linear(v, uexact, (F(external), F(0)))
            Bv = [h.exact_linear(v, row) for row in Bexact]
            assert tuple(map(F, term['center_exact'])) == z0
            assert tuple(map(F, term['lambda_exact'])) == lam
            assert [tuple(map(F, z)) for z in term['preconditioned_vector_exact']] == Bv
            lam2_modulus = h.norm_squared(lam)
            assert F(term['lambda_squared_modulus_rational']) == lam2_modulus
            lam_abs = F(term['lambda_modulus_upper_rational'])
            assert lam_abs >= 0 and lam_abs*lam_abs >= lam2_modulus
            lam_complex = h.exact_complex(lam)
            lam_complex_square = h.cm(lam_complex, lam_complex)
            jp = h.complex_interval(term['center_j_prime'])
            jvalue = h.complex_interval(term['center_j'])
            assert 0 < z0[0] < 1 and h.complex_interval(term['center_log_argument'])[0][0] > 0
            jsecond = h.cn(h.ca(pi_square, h.cm(jp, jp)))
            for i in range(5):
                f0[i] = h.ca(f0[i], h.cs(jvalue, F(sigma*v[i])))
                for j in range(5):
                    J0[i][j] = h.ca(J0[i][j], h.cs(jp, F(sigma*v[i]*v[j])))
            if name == 's+b':
                L0 = h.ch(h.ca(jp, ipi), h.complex_interval(case['center_external_forcing']))
            a_radius = r*lam_abs
            maff = h.curvature(term['affine_curvature'], z0, a_radius, 'affine', name, pi)
            jp_abs = h.abs_upper(jp)
            third = h.upper_round(2*(jp_abs+maff*a_radius)*maff)
            coeff = [max(F(old), abs(sigma)*h.abs_upper(h.exact_complex(z)))
                     for old, z in zip(term['preconditioned_sigma_modulus_uppers_rational'], Bv)]
            quadratic = [h.cs(h.cm(h.exact_complex(z), h.cm(jsecond, lam_complex_square)), F(sigma))
                         for z in Bv]
            second_sum = [h.ca(x, y) for x, y in zip(second_sum, quadratic)]
            remainder = [r*r*r/6*x*third*lam2_modulus*lam_abs for x in coeff]
            cubic_terms.append(remainder)
            term_records.append(dict(name=name, sigma=sigma, center_exact=list(map(str, z0)),
                lambda_exact=list(map(str, lam)), lambda_complex_square=cr(lam_complex_square),
                lambda_squared_modulus_rational=str(lam2_modulus), lambda_modulus_upper_rational=str(lam_abs),
                preconditioned_vector_exact=[list(map(str, z)) for z in Bv],
                center_jprime=cr(jp), center_jsecond=cr(jsecond),
                affine_radius_upper_rational=str(a_radius), affine_curvature_upper_rational=str(maff),
                center_jprime_modulus_upper_rational=str(jp_abs), third_derivative_upper_rational=str(third),
                sigma_vector_modulus_uppers_rational=list(map(str, coeff)),
                signed_complex_quadratic_coefficients=list(map(cr, quadratic)),
                cubic_residual_contributions_rational=list(map(str, remainder))))
        f0 = [h.ch(x, h.complex_interval(y)) for x, y in zip(f0, case['center_gradient'])]
        J0 = [[h.ch(x, h.complex_interval(y)) for x, y in zip(row, saved)]
              for row, saved in zip(J0, case['center_jacobian'])]
        cvalue = [h.ch(x, h.complex_interval(y)) for x, y in zip(h.matrix_vector(B, f0), case['preconditioned_center_residual'])]
        linear = h.matrix_vector(J0, u); linear[4] = h.ca(linear[4], L0)
        vvalue = [h.ch(x, h.complex_interval(y)) for x, y in zip(h.matrix_vector(B, linear), case['preconditioned_linear_defect'])]
        cabs, vabs, sabs = list(map(h.abs_upper, cvalue)), list(map(h.abs_upper, vvalue)), list(map(h.abs_upper, second_sum))
        cubic = [sum(row[i] for row in cubic_terms) for i in range(5)]
        quadratic = [r*r*x/2 for x in sabs]
        new_bound = [h.upper_round(cabs[i]+r*vabs[i]+quadratic[i]+cubic[i]) for i in range(5)]
        old_bound = list(map(F, prior['residual_upper_rational']))
        residual = [min(x, y) for x, y in zip(old_bound, new_bound)]
        assert all(0 <= x <= y for x, y in zip(residual, old_bound))
        C = [list(map(F, row)) for row in prior['error_cost_matrix_rational']]
        rho = list(map(F, prior['original_radii_rational']))
        oldz = list(map(F, prior['posterior_radii_rational']))
        assert rho == [multiplier*x for x in h.RHO]
        assert all(x >= 0 for row in C for x in row)
        assert all(0 <= x < y for x, y in zip(oldz, rho))
        C_rho = [sum(x*y for x, y in zip(row, rho)) for row in C]
        eta = max(x/y for x, y in zip(C_rho, rho))
        assert eta == F(prior['error_cost_contraction_upper_rational']) < 1
        assert [rho[i]-old_bound[i]-C_rho[i] for i in range(5)] == list(map(F, prior['error_cost_inclusion_margins_rational']))
        assert all(old_bound[i]+C_rho[i] < rho[i] for i in range(5))
        matrix = [[F(int(i == j))-C[i][j] for j in range(5)] for i in range(5)]
        assert all(sum(x*y for x, y in zip(row, oldz)) == value for row, value in zip(matrix, old_bound))
        newz = h.exact_solve(matrix, residual)
        assert all(0 <= x <= y for x, y in zip(newz, oldz))
        widths = list(map(F, case['affine_halfwidths_rational']))
        abs_u = list(map(F, case['response_modulus_uppers_rational']))
        assert widths == [r*x for x in abs_u]
        assert all(x >= 0 and x*x >= h.norm_squared(z) for x, z in zip(abs_u, uexact))
        results.append(dict(beta=beta, epsilon=epsilon, multiplier_rational=str(multiplier),
            source_posterior_canonical_sha256=canonical_sha(prior),
            split_case_canonical_sha256=canonical_sha(split_case), affine_case_canonical_sha256=canonical_sha(case),
            center_exact=prior['center_exact'], response_exact=prior['response_exact'],
            parameter_center=prior['parameter_center'], parameter_radius_rational=str(r),
            old_error_radii_rational=list(map(str, rho)), primitive_terms=term_records,
            reconstructed_preconditioned_center_residual=list(map(cr, cvalue)),
            reconstructed_preconditioned_linear_defect=list(map(cr, vvalue)),
            complex_quadratic_sums=list(map(cr, second_sum)),
            center_modulus_uppers_rational=list(map(str, cabs)),
            linear_modulus_uppers_rational=list(map(str, vabs)),
            quadratic_sum_modulus_uppers_rational=list(map(str, sabs)),
            quadratic_residual_upper_rational=list(map(str, quadratic)),
            cubic_residual_upper_rational=list(map(str, cubic)),
            second_order_residual_upper_rational=list(map(str, new_bound)),
            old_residual_upper_rational=list(map(str, old_bound)),
            chosen_residual_upper_rational=list(map(str, residual)),
            improved_components=[name for name, x, y in zip(h.NAMES, residual, old_bound) if x < y],
            unchanged_error_cost_matrix_rational=prior['error_cost_matrix_rational'],
            error_cost_contraction_upper_rational=str(eta), old_posterior_radii_rational=list(map(str, oldz)),
            posterior_radii_rational=list(map(str, newz)), posterior_radii_display=[float(x) for x in newz],
            exact_linear_system_verified=True,
            coordinate_enclosures={name: {
                'real': {'finite': True, 'lower_rational': str(q[0]-width-error), 'upper_rational': str(q[0]+width+error)},
                'imag': {'finite': True, 'lower_rational': str(q[1]-width-error), 'upper_rational': str(q[1]+width+error)}}
                for name, q, width, error in zip(h.NAMES, center, widths, newz)}))
    assert len(results) == 4
    changed = [name for name, digest in bindings.items() if sha(ROOT/name) != digest]
    assert changed == []
    result = dict(status='completed fixed saved-only protocol', source_path=SOURCE,
        source_sha256=bindings[SOURCE], split_source_sha256=bindings[SPLIT],
        affine_source_sha256=bindings[AFFINE], proof_sha256=bindings[PROOF],
        checker_sha256=bindings[own], input_sha256=bindings, changed_inputs=changed,
        cases=results, residual_comparisons=4, exact_posterior_solves=4,
        analytic_callbacks=0, root_solves=0, source_evaluations=0, height_integral_evaluations=0,
        scalar_phase_evaluations=0, changed_predictors=0, new_radius_candidates=0,
        uniform_main_phase_gap_proved=False, uniform_source_gap_proved=False,
        whole_knot_theorem_proved=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2); stream.write('\n')
    print(json.dumps(dict(status=result['status'], sha256=sha(args.output),
        posterior=[dict(beta=x['beta'], epsilon=x['epsilon'],
            improved_components=x['improved_components'], radii=x['posterior_radii_display'])
            for x in results])), flush=True)


if __name__ == '__main__':
    main()
