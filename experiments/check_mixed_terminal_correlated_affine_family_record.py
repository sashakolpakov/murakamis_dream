#!/usr/bin/env python3
"""Saved-only rational audit and posterior refinement of 16 affine tests.

No analytic package, source evaluator, proposal, root solve, or subdivision.
Separately serialized analytic intervals are recombined conservatively;
their outward hulls, not overlap tests, are used in the rebuilt criteria.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
DRIVER = 'experiments/certify_mixed_terminal_correlated_affine_family.py'
PROOF = 'notes/research_mixed_terminal_correlated_affine_family_certificate.md'
COMPLETION = 'notes/research_mixed_terminal_correlated_affine_family_completion.md'
OLD = 'repro/results/research-mixed-terminal-affine-family.json'
REFERENCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
AUDIT = 'repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json'
PINNED = {
    SOURCE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    DRIVER: 'db3e96fd4594707b099deca1543f090e5d132769bb02905e60619aa5a52e07f9',
    PROOF: '0ba6a11f26a17e3642a41c6bd97cf93a01c1c7a5c4dd2437d3ee23435dfb8957',
    COMPLETION: '5b814d6eadb78eb8636d6144505dc826898a8956f73aab28f03af36873946b3e',
    OLD: '908232a2fc15d731c13803cd503c7b0d70c579f9cbf1896543f7233df2196370',
    REFERENCE: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    AUDIT: 'bedf680b3f57c799980517f7aa6178a7f9c5a0890bac8528947e9018baf7a4de',
}
NAMES = ('e', 'xi', 't', 'a', 's')
CENTERS = ((F(7, 20), -F(1, 100)), (F(3, 10), -F(13, 250)))
RADII = (F(9, 100), F(8, 125))
RHO = tuple(map(F, ('1/500', '1/1000', '1/200', '1/200', '1/100')))
MULTIPLIERS = tuple(map(F, ('1/4', '1/2', '1', '2')))
COMMON = tuple(tuple(map(F, row)) for row in (
    ('.33', '.47', '-.09', '.08'), ('.21', '.25', '.01', '.10'),
    ('.23', '.45', '-.12', '.12'), ('.23', '.45', '-.12', '.12'),
    ('.23', '.45', '-.12', '.12')))
SCALE = 1 << 240
ZERO = (F(0), F(0))
CZ = (ZERO, ZERO)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def interval(value):
    assert value['finite'] is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def complex_interval(value):
    return interval(value['real']), interval(value['imag'])


def exact_complex(value):
    a, b = map(F, value)
    return (a, a), (b, b)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    products = [x*y for x in a for y in b]
    return min(products), max(products)


def hull(a, b):
    return min(a[0], b[0]), max(a[1], b[1])


def ca(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def cn(a):
    return neg(a[0]), neg(a[1])


def cm(a, b):
    return add(mul(a[0], b[0]), neg(mul(a[1], b[1]))), add(mul(a[0], b[1]), mul(a[1], b[0]))


def cs(a, scalar):
    return mul(a[0], (scalar, scalar)), mul(a[1], (scalar, scalar))


def ch(a, b):
    return hull(a[0], b[0]), hull(a[1], b[1])


def csum(values):
    result = CZ
    for value in values:
        result = ca(result, value)
    return result


def upper_round(value):
    value = F(value)
    return F(-((-value.numerator*SCALE)//value.denominator), SCALE)


def abs_upper(value):
    squared = sum(max(abs(lo), abs(hi))**2 for lo, hi in value)
    scaled = -((-squared.numerator*SCALE*SCALE)//squared.denominator)
    n = isqrt(scaled)
    if n*n < scaled:
        n += 1
    result = F(n, SCALE)
    assert result*result >= squared
    return result


def exact_linear(v, values, offset=(F(0), F(0))):
    return tuple(offset[k]+sum(F(x)*F(z[k]) for x, z in zip(v, values)) for k in range(2))


def norm_squared(z):
    return sum(F(x)*F(x) for x in z)


def inventory(epsilon):
    return [
        ('e-xi', -1, [1, -1, 0, 0, 0], 0, F(0)),
        ('e+t', 1, [1, 0, 1, 0, 0], 0, F(0)),
        ('e', -epsilon, [1, 0, 0, 0, 0], 0, F(0)),
        ('1/2-xi', -2, [0, -1, 0, 0, 0], 0, F(1, 2)),
        ('xi', -3, [0, 1, 0, 0, 0], 0, F(0)),
        ('t+a', 1, [0, 0, 1, 1, 0], 0, F(0)),
        ('t', -(2+epsilon), [0, 0, 1, 0, 0], 0, F(0)),
        ('a+s', 1, [0, 0, 0, 1, 1], 0, F(0)),
        ('a', -3, [0, 0, 0, 1, 0], 0, F(0)),
        ('s+b', 1, [0, 0, 0, 0, 1], 1, F(0)),
        ('s', -3, [0, 0, 0, 0, 1], 0, F(0)),
    ]


def curvature(w, center, radius, stage, name, pi):
    d = min(center[0]-radius, 1-center[0]-radius)
    assert w['name'] == name and w['stage'] == stage and w['regular'] is True
    assert tuple(map(F, w['center_exact'])) == center
    assert F(w['radius_upper_rational']) == radius
    assert list(map(F, w['real_interval_rational'])) == [center[0]-radius, center[0]+radius]
    assert F(w['strip_distance_rational']) == d and 0 < d <= F(1, 2)
    sine, bound = interval(w['sine']), interval(w['curvature_bound'])
    assert sine[0] > 0 and bound[0] > 0
    original = F(w['curvature_upper_rational'])
    assert original == bound[1]
    return upper_round(max(original, pi[1]**2/sine[0]**2))


def matrix_vector(matrix, vector):
    return [csum(cm(x, y) for x, y in zip(row, vector)) for row in matrix]


def exact_solve(matrix, vector):
    a = [list(row)+[value] for row, value in zip(matrix, vector)]
    for j in range(len(a)):
        pivot = next(i for i in range(j, len(a)) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        divisor = a[j][j]
        a[j] = [x/divisor for x in a[j]]
        for i in range(len(a)):
            if i != j:
                factor = a[i][j]
                a[i] = [x-factor*y for x, y in zip(a[i], a[j])]
    answer = [row[-1] for row in a]
    assert all(sum(x*y for x, y in zip(row, answer)) == value for row, value in zip(matrix, vector))
    return answer


def check_box(saved, center, widths):
    for name, z, width in zip(NAMES, center, widths):
        assert interval(saved[name]['real']) == (z[0]-width, z[0]+width)
        assert interval(saved[name]['imag']) == (z[1]-width, z[1]+width)
    return all(a < z[0]-w and z[0]+w < b and c < z[1]-w and z[1]+w < d
               for z, w, (a, b, c, d) in zip(center, widths, COMMON))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    # Exact determinant fractions may exceed Python's decimal display cap.
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    assert all(isinstance(x, str) and len(x) == 64 for x in PINNED.values())
    bindings = {}

    def bind(name, digest):
        assert name not in bindings or bindings[name] == digest
        assert sha(ROOT/name) == digest, name
        bindings[name] = digest

    for name, digest in PINNED.items():
        bind(name, digest)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bind(own, sha(ROOT/own))
    data, old, reference, audit = [json.loads((ROOT/p).read_text()) for p in (SOURCE, OLD, REFERENCE, AUDIT)]
    for record in (data, old, reference, audit):
        for key in ('input_sha256', 'dependencies_sha256'):
            for name, digest in record.get(key, {}).items():
                bind(name, digest)
    assert data['status'] == 'completed fixed protocol' and data['changed_inputs'] == []
    assert len(data['input_sha256']) == 36 and data['precision_bits'] == 256
    assert data['source_path'] == OLD and data['source_sha256'] == bindings[OLD]
    assert data['script_sha256'] == bindings[DRIVER] and data['proof_sha256'] == bindings[PROOF]
    assert data['reference_path'] == REFERENCE and data['reference_sha256'] == bindings[REFERENCE]
    assert data['exact_saved_proposals_only'] and not data['full_common_domain_containment_required']
    assert all(data[k] is False for k in ('uniform_source_bound_claimed', 'finite_word_realization_claimed', 'knot_theorem_claimed'))
    assert audit['status'] == 'passed' and audit['source_sha256'] == bindings[REFERENCE]
    expected_counts = dict(saved_cases_reused=4, candidates=16,
        center_gradient_evaluations=4, center_jacobian_evaluations=4,
        center_logarithms=44, center_cotangents=44, affine_curvature_sines=44,
        full_curvature_sines=176, inverse_proposals=0, response_proposals=0,
        root_solves=0, primitive_action_evaluations=0, quantum_source_evaluations=0,
        subdivisions=0, precision_retries=0, candidate_errors=0)
    assert data['counts'] == expected_counts
    case_keys = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for record in (data, old, reference):
        assert [(c['beta'], c['epsilon']) for c in record['cases']] == case_keys
    pi = interval(reference['pi'])
    assert F(157, 50) < pi[0] <= pi[1] < F(22, 7)
    ipi = (ZERO, pi)
    results = []
    posterior = []
    uncertified_majorants = []
    maximum_rebuild_widening = F(0)
    for index, (case, prior, certified) in enumerate(zip(data['cases'], old['cases'], reference['cases'])):
        beta, epsilon = case_keys[index]
        assert case['case_index'] == index
        assert case['saved_affine_case_canonical_sha256'] == canonical_sha(prior)
        assert case['canonical_reference_case_sha256'] == canonical_sha(certified)
        assert certified['canonical_reference_certified'] is True
        center = [tuple(map(F, z)) for z in case['center']]
        assert center == [tuple(map(F, z)) for z in prior['center']] == [tuple(map(F, z)) for z in certified['proposed_centers']]
        assert tuple(map(F, case['parameter_center'])) == CENTERS[beta] == tuple(map(F, certified['outside_coordinate']))
        radius = F(case['parameter_radius_rational']); assert radius == RADII[beta]
        assert case['saved_inverse_proposal'] == prior['inverse_proposal']
        assert case['saved_response_proposal'] == prior['derivative_proposal']
        Bexact = [[tuple(map(F, z)) for z in row] for row in case['inverse_exact']]
        uexact = [tuple(map(F, z)) for z in case['response_exact']]
        assert Bexact == [[tuple(map(F, z)) for z in row] for row in prior['inverse_proposal']]
        assert uexact == [tuple(map(F, z)) for z in prior['derivative_proposal']]
        B, u = [[exact_complex(z) for z in row] for row in Bexact], list(map(exact_complex, uexact))
        uabs = list(map(F, case['response_modulus_uppers_rational']))
        assert all(x >= 0 and x*x >= norm_squared(z) for x, z in zip(uabs, uexact))
        widths = [radius*x for x in uabs]
        assert list(map(F, case['affine_halfwidths_rational'])) == widths
        assert check_box(case['affine_coordinate_box'], center, widths) == case['affine_inside_common_domain']
        M = [[epsilon, 1, -1, 0, 0], [1, 0, 0, 0, 0], [-1, 0, epsilon, 1, 0],
             [0, 0, 1, 1, -1], [0, 0, 0, -1, 1]]
        n = [0, 0, 0, 0, 1]; c = [-F(epsilon, 2), F(0), -F(epsilon, 2), -F(1, 2), -F(1, 2)]
        assert case['chirp_matrix'] == M and case['chirp_external'] == n
        assert list(map(F, case['chirp_constant_rational'])) == c
        f0 = [cm(ipi, exact_complex(exact_linear(M[i], center,
              (n[i]*CENTERS[beta][0]+c[i], n[i]*CENTERS[beta][1])))) for i in range(5)]
        J0 = [[cs(ipi, F(M[i][j])) for j in range(5)] for i in range(5)]
        assert len(case['primitive_terms']) == 11
        term_bounds = []
        for term, (name, sigma, v, external, offset) in zip(case['primitive_terms'], inventory(epsilon)):
            assert (term['name'], term['sigma'], term['v'], term['external'], F(term['offset_rational'])) == (name, sigma, v, external, offset)
            z0 = exact_linear(v, center, (external*CENTERS[beta][0]+offset, external*CENTERS[beta][1]))
            lam = exact_linear(v, uexact, (F(external), F(0)))
            Bv = [exact_linear(v, row) for row in Bexact]
            assert tuple(map(F, term['center_exact'])) == z0
            assert tuple(map(F, term['lambda_exact'])) == lam
            assert [tuple(map(F, z)) for z in term['preconditioned_vector_exact']] == Bv
            lam2 = norm_squared(lam)
            assert F(term['lambda_squared_modulus_rational']) == lam2
            lab = F(term['lambda_modulus_upper_rational']); assert lab >= 0 and lab*lab >= lam2
            coeff = list(map(F, term['preconditioned_sigma_modulus_uppers_rational']))
            assert all(h >= 0 and h*h >= sigma*sigma*norm_squared(z) for h, z in zip(coeff, Bv))
            assert 0 < z0[0] < 1 and complex_interval(term['center_log_argument'])[0][0] > 0
            jvalue, jp = complex_interval(term['center_j']), complex_interval(term['center_j_prime'])
            for i in range(5):
                f0[i] = ca(f0[i], cs(jvalue, F(sigma*v[i])))
                for j in range(5):
                    J0[i][j] = ca(J0[i][j], cs(jp, F(sigma*v[i]*v[j])))
            if name == 's+b':
                L0 = ch(ca(jp, ipi), complex_interval(case['center_external_forcing']))
            maff = curvature(term['affine_curvature'], z0, radius*lab, 'affine', name, pi)
            term_bounds.append((name, v, z0, lam2, radius*lab, coeff, maff))
        f0 = [ch(x, complex_interval(y)) for x, y in zip(f0, case['center_gradient'])]
        J0 = [[ch(x, complex_interval(y)) for x, y in zip(row, saved)] for row, saved in zip(J0, case['center_jacobian'])]
        center_defect = [ch(x, complex_interval(y)) for x, y in zip(matrix_vector(B, f0), case['preconditioned_center_residual'])]
        linear = matrix_vector(J0, u); linear[4] = ca(linear[4], L0)
        linear_defect = [ch(x, complex_interval(y)) for x, y in zip(matrix_vector(B, linear), case['preconditioned_linear_defect'])]
        E0 = []
        for i in range(5):
            E0.append([ch(ca(exact_complex((int(i == j), 0)), cn(csum(cm(B[i][k], J0[k][j]) for k in range(5)))),
                          complex_interval(case['center_error_matrix'][i][j])) for j in range(5)])
        oldc, oldv = list(map(F, case['center_residual_upper_rational'])), list(map(F, case['linear_defect_upper_rational']))
        oldE = [list(map(F, row)) for row in case['center_error_matrix_upper_rational']]
        assert all(x >= 0 for x in oldc+oldv+[x for row in oldE for x in row])
        newc = [max(x, abs_upper(z)) for x, z in zip(oldc, center_defect)]
        newv = [max(x, abs_upper(z)) for x, z in zip(oldv, linear_defect)]
        newE = [[max(x, abs_upper(z)) for x, z in zip(row, saved)] for row, saved in zip(oldE, E0)]
        oldQ = [[radius*radius/2*F(term['preconditioned_sigma_modulus_uppers_rational'][i])
                 *F(term['affine_curvature']['curvature_upper_rational'])*F(term['lambda_squared_modulus_rational'])
                 for term in case['primitive_terms']] for i in range(5)]
        assert [list(map(F, row)) for row in case['affine_quadratic_terms_rational']] == oldQ
        oldR = [oldc[i]+radius*oldv[i]+sum(oldQ[i]) for i in range(5)]
        assert list(map(F, case['affine_residual_upper_rational'])) == oldR
        R = [upper_round(newc[i]+radius*newv[i]+sum(radius*radius/2*h[i]*maff*lam2
             for _, _, _, lam2, _, h, maff in term_bounds)) for i in range(5)]
        assert all(x >= y for x, y in zip(R, oldR))
        assert [F(q['multiplier_rational']) for q in case['candidates']] == list(MULTIPLIERS)
        case_rows = []
        for candidate, multiplier in zip(case['candidates'], MULTIPLIERS):
            rho = [multiplier*x for x in RHO]
            assert list(map(F, candidate['error_radii_rational'])) == rho
            assert candidate['common_domain_containment_required'] is False
            assert check_box(candidate['full_coordinate_box'], center, [x+y for x, y in zip(widths, rho)]) == candidate['inside_original_common_domain']
            for name, z, r, witness in zip(NAMES, center, rho, candidate['saved_central_root_containment']):
                coordinate = certified['coordinate_enclosures'][name]
                distance = sum(max(abs(x-z[k]) for x in interval(coordinate[key]))**2 for k, key in enumerate(('real', 'imag')))
                assert witness == dict(coordinate=name, maximum_distance_squared_rational=str(distance),
                    candidate_radius_squared_rational=str(r*r), strictly_contained=distance < r*r)
                assert distance < r*r
            assert candidate['saved_central_root_contained'] is True
            assert candidate['all_full_original_log_disks_regular'] is True
            assert len(candidate['full_primitive_terms']) == 11
            originalE = [row[:] for row in oldE]; rebuiltE = [row[:] for row in newE]
            for full, term, (_, v, z0, _, affine_radius, h, _) in zip(candidate['full_primitive_terms'], case['primitive_terms'], term_bounds):
                name = term['name']; assert full['name'] == name
                total_radius = affine_radius+sum(abs(x)*y for x, y in zip(v, rho))
                mf = curvature(full['full_curvature'], z0, total_radius, 'full', name, pi)
                oldmf = F(full['full_curvature']['curvature_upper_rational'])
                contribution = [[h[i]*oldmf*total_radius*abs(v[j]) for j in range(5)] for i in range(5)]
                assert [list(map(F, row)) for row in full['error_matrix_contribution_rational']] == contribution
                for i in range(5):
                    for j in range(5):
                        originalE[i][j] += contribution[i][j]
                        rebuiltE[i][j] += h[i]*mf*total_radius*abs(v[j])
            rebuiltE = [[upper_round(x) for x in row] for row in rebuiltE]
            assert [list(map(F, row)) for row in candidate['error_matrix_upper_rational']] == originalE
            oldlin = [sum(x*y for x, y in zip(row, rho)) for row in originalE]
            oldmargins = [rho[i]-oldR[i]-oldlin[i] for i in range(5)]
            oldeta = max(x/y for x, y in zip(oldlin, rho))
            assert list(map(F, candidate['linear_error_upper_rational'])) == oldlin
            assert list(map(F, candidate['affine_residual_upper_rational'])) == oldR
            assert list(map(F, candidate['inclusion_margin_rational'])) == oldmargins
            assert F(candidate['contraction_upper_rational']) == oldeta
            original_pass = oldeta < 1 and min(oldmargins) > 0
            assert candidate['criterion_verified'] is original_pass
            assert candidate['status'] == ('uniform correlated affine enclosure certified' if original_pass else 'inconclusive')
            lin = [sum(x*y for x, y in zip(row, rho)) for row in rebuiltE]
            margins = [rho[i]-R[i]-lin[i] for i in range(5)]
            eta = max(x/y for x, y in zip(lin, rho))
            rebuilt_pass = eta < 1 and min(margins) > 0
            assert rebuilt_pass == original_pass == (beta == 1 and multiplier >= 1)
            widening = max((R[i]+lin[i])-(oldR[i]+oldlin[i]) for i in range(5))
            assert widening >= 0
            maximum_rebuild_widening = max(maximum_rebuild_widening, widening)
            case_rows.append(dict(multiplier_rational=str(multiplier), original_pass=original_pass,
                rebuilt_pass=rebuilt_pass, contraction_upper_rational=str(eta),
                inclusion_margins_rational=list(map(str, margins)),
                maximum_total_widening_rational=str(widening)))
            if beta == 0 or multiplier == 1:
                matrix = [[F(int(i == j))-rebuiltE[i][j] for j in range(5)] for i in range(5)]
                z = exact_solve(matrix, R)
                assert eta < 1 and all(x >= 0 for x in z)
            if beta == 0:
                uncertified_majorants.append(dict(beta=beta, epsilon=epsilon,
                    multiplier_rational=str(multiplier),
                    candidate_radii_rational=list(map(str, rho)),
                    rebuilt_residual_rational=list(map(str, R)),
                    rebuilt_error_matrix_rational=[list(map(str, row)) for row in rebuiltE],
                    formal_majorant_solution_rational=list(map(str, z)),
                    formal_majorant_solution_display=[float(x) for x in z],
                    contraction_upper_rational=str(eta), exact_equation_verified=True,
                    is_canonical_root_enclosure=False,
                    interpretation='algebraic radius diagnostic only; original candidate failed inclusion'))
            if beta == 1 and multiplier == 1:
                assert all(0 <= x < r for x, r in zip(z, rho))
                posterior.append(dict(beta=beta, epsilon=epsilon, multiplier_rational='1',
                    center=case['center'], parameter_center=case['parameter_center'],
                    parameter_radius_rational=str(radius), response_exact=case['response_exact'],
                    original_error_radii_rational=list(map(str, rho)),
                    rebuilt_residual_rational=list(map(str, R)),
                    rebuilt_error_matrix_rational=[list(map(str, row)) for row in rebuiltE],
                    contraction_upper_rational=str(eta), posterior_radii_rational=list(map(str, z)),
                    posterior_radii_display=[float(x) for x in z],
                    absolute_coordinate_box={name: {
                        'real': {'finite': True, 'lower_rational': str(q[0]-width-error), 'upper_rational': str(q[0]+width+error)},
                        'imag': {'finite': True, 'lower_rational': str(q[1]-width-error), 'upper_rational': str(q[1]+width+error)}}
                        for name, q, width, error in zip(NAMES, center, widths, z)},
                    exact_equation_verified=True, analytic_replay_performed=False))
        assert case['status'] == ('uniform correlated affine family certified' if beta == 1 else 'inconclusive')
        results.append(dict(beta=beta, epsilon=epsilon, candidates=case_rows))
    assert data['certified_families'] == 2 and data['all_full_disk_families_certified'] is False
    assert len(posterior) == 2 and len(uncertified_majorants) == 8
    changed = [name for name, digest in bindings.items() if sha(ROOT/name) != digest]
    assert changed == []
    result = dict(status='passed', source_path=SOURCE, source_sha256=bindings[SOURCE],
        checker_path=own, checker_sha256=bindings[own], completion_sha256=bindings[COMPLETION],
        cases=results, original_candidates_verified=16, original_criterion_successes=4,
        rebuilt_criterion_successes=4, certified_full_D4_families=2,
        D3_family_certified=False, posterior_refinements=posterior,
        uncertified_D3_formal_majorants=uncertified_majorants,
        saved_source_binding_count=len(data['input_sha256']), input_sha256=bindings,
        changed_inputs=changed, maximum_total_rebuild_widening_rational=str(maximum_rebuild_widening),
        endpoint_convention='exact rational recombination, outward hull, upward dyadic rounding at 240 bits',
        center_primitives_and_sines_are_source_bound_analytic_inputs=True,
        analytic_callbacks=0, root_solves=0, source_evaluations=0, numerical_proposals=0,
        uniform_source_gap_proved=False, finite_word_realization_proved=False, knot_theorem_proved=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2); stream.write('\n')
    print(json.dumps(dict(status='passed', sha256=sha(args.output),
        certified_families=2, posterior_radii=[x['posterior_radii_display'] for x in posterior])), flush=True)


if __name__ == '__main__':
    main()
