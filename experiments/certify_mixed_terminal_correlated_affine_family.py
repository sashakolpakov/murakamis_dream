#!/usr/bin/env python3
"""One fixed correlated-Taylor test of four canonical terminal families.

Exact saved q0, B, u; four unchanged error radii per case. No proposals,
root solve, subdivision, primitive action, source sum, or automatic retry.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_correlated_affine_family_certificate.md'
SOURCE = 'repro/results/research-mixed-terminal-affine-family.json'
OLD_SCRIPT = 'experiments/certify_mixed_terminal_affine_family.py'
OLD_PROOF = 'notes/research_mixed_terminal_affine_family_certificate.md'
REFERENCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
AUDIT = 'repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json'
AUDIT_CHECKER = 'experiments/check_mixed_terminal_horizontal_envelope_record.py'
PINNED = {
    PROOF: '0ba6a11f26a17e3642a41c6bd97cf93a01c1c7a5c4dd2437d3ee23435dfb8957',
    SOURCE: '908232a2fc15d731c13803cd503c7b0d70c579f9cbf1896543f7233df2196370',
    OLD_SCRIPT: 'cd86b3812a4b345616e6b2d9113beec2a18b935c9c24f883af630bc58ba4d556',
    OLD_PROOF: 'f2c87603ca31133ef9bba731533351dda39cfcc39774f36ae4a8b678878bcba9',
    REFERENCE: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    AUDIT: 'bedf680b3f57c799980517f7aa6178a7f9c5a0890bac8528947e9018baf7a4de',
    AUDIT_CHECKER: '23545f9f66ec7ba9e2ddb89410f9c198a64f4d615b95df4d346bc2083936cdcb',
}
NAMES = ('e', 'xi', 't', 'a', 's')
CENTERS = ((F(7, 20), -F(1, 100)), (F(3, 10), -F(13, 250)))
DISK_RADII = (F(9, 100), F(8, 125))
ERROR_RADII = tuple(map(F, ('1/500', '1/1000', '1/200', '1/200', '1/100')))
MULTIPLIERS = tuple(map(F, ('1/4', '1/2', '1', '2')))
COMMON = tuple(tuple(map(F, row)) for row in (
    ('.33', '.47', '-.09', '.08'), ('.21', '.25', '.01', '.10'),
    ('.23', '.45', '-.12', '.12'), ('.23', '.45', '-.12', '.12'),
    ('.23', '.45', '-.12', '.12')))


class DomainFailure(ValueError):
    """An expected failed regularity or containment guard."""

    def __init__(self, message, witness=None):
        super().__init__(message)
        self.witness = witness


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def pair(value):
    assert len(value) == 2
    return tuple(map(F, value))


def pairs_record(values):
    return [[str(x) for x in z] for z in values]


def linear(coefficients, values, constant=(F(0), F(0))):
    return tuple(constant[k] + sum(F(c)*z[k] for c, z in zip(coefficients, values))
                 for k in range(2))


def squared_modulus(z):
    return z[0]*z[0]+z[1]*z[1]


def terms(epsilon):
    rows = (
        ('e-xi', -1, (1, -1, 0, 0, 0), 0, F(0)),
        ('e+t', 1, (1, 0, 1, 0, 0), 0, F(0)),
        ('e', -epsilon, (1, 0, 0, 0, 0), 0, F(0)),
        ('1/2-xi', -2, (0, -1, 0, 0, 0), 0, F(1, 2)),
        ('xi', -3, (0, 1, 0, 0, 0), 0, F(0)),
        ('t+a', 1, (0, 0, 1, 1, 0), 0, F(0)),
        ('t', -(2+epsilon), (0, 0, 1, 0, 0), 0, F(0)),
        ('a+s', 1, (0, 0, 0, 1, 1), 0, F(0)),
        ('a', -3, (0, 0, 0, 1, 0), 0, F(0)),
        ('s+b', 1, (0, 0, 0, 0, 1), 1, F(0)),
        ('s', -3, (0, 0, 0, 0, 1), 0, F(0)),
    )
    return [dict(name=name, sigma=sigma, v=list(v), external=w,
                 offset_rational=str(offset)) for name, sigma, v, w, offset in rows]


def chirp(epsilon):
    matrix = [[epsilon, 1, -1, 0, 0], [1, 0, 0, 0, 0],
              [-1, 0, epsilon, 1, 0], [0, 0, 1, 1, -1],
              [0, 0, 0, -1, 1]]
    return matrix, [0, 0, 0, 0, 1], [
        -F(epsilon, 2), F(0), -F(epsilon, 2), -F(1, 2), -F(1, 2)]


def box_record(center, radii):
    return {name: {
        'real': {'finite': True, 'lower_rational': str(z[0]-r),
                 'upper_rational': str(z[0]+r)},
        'imag': {'finite': True, 'lower_rational': str(z[1]-r),
                 'upper_rational': str(z[1]+r)}}
        for name, z, r in zip(NAMES, center, radii)}


def common_containment(center, radii):
    return all(lo_r < z[0]-r and z[0]+r < hi_r
               and lo_i < z[1]-r and z[1]+r < hi_i
               for z, r, (lo_r, hi_r, lo_i, hi_i)
               in zip(center, radii, COMMON))


def central_root_containment(reference, center, rho):
    result = []
    for name, z, radius in zip(NAMES, center, rho):
        parts = reference['coordinate_enclosures'][name]
        distances = []
        for index, key in enumerate(('real', 'imag')):
            item = parts[key]
            assert item['finite'] is True
            lo, hi = F(item['lower_rational']), F(item['upper_rational'])
            assert lo <= hi
            distances.append(max(abs(lo-z[index]), abs(hi-z[index])))
        maximum = sum(x*x for x in distances)
        result.append(dict(coordinate=name,
            maximum_distance_squared_rational=str(maximum),
            candidate_radius_squared_rational=str(radius*radius),
            strictly_contained=maximum < radius*radius))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if any(not isinstance(value, str) or len(value) != 64 for value in PINNED.values()):
        raise ValueError('review pins are incomplete')
    inputs = {}

    def bind(name, digest):
        if name in inputs and inputs[name] != digest:
            raise ValueError('conflicting input identity: '+name)
        if sha(ROOT/name) != digest:
            raise ValueError('changed input: '+name)
        inputs[name] = digest

    def inherit(record):
        for key in ('input_sha256', 'dependencies_sha256'):
            mapping = record.get(key)
            if isinstance(mapping, dict):
                for name, digest in mapping.items():
                    bind(name, digest)

    for name, digest in PINNED.items():
        bind(name, digest)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bind(own, sha(ROOT/own))
    source, reference, audit = [
        json.loads((ROOT/name).read_text()) for name in (SOURCE, REFERENCE, AUDIT)]
    for record in (source, reference, audit):
        inherit(record)
    assert source['status'] == 'completed fixed protocol'
    assert source['changed_inputs'] == [] and source['precision_bits'] == 256
    assert source['certified_families'] == 0 and not source['all_full_disk_families_certified']
    assert source['counts']['candidates'] == 16
    assert source['counts']['inverse_proposals'] == source['counts']['derivative_proposals'] == 4
    assert source['counts']['root_solves'] == source['counts']['subdivisions'] == 0
    assert source['counts']['precision_retries'] == 0
    assert reference['status'] == 'complete fixed diagnostic' and reference['changed_inputs'] == []
    assert audit['status'] == 'passed'
    assert (audit['source_path'], audit['source_sha256'], audit['checker_sha256']) == (
        REFERENCE, inputs[REFERENCE], inputs[AUDIT_CHECKER])
    inventory = [(0, 0), (0, 1), (1, 0), (1, 1)]
    assert [(r['beta'], r['epsilon']) for r in source['cases']] == inventory
    assert [(r['beta'], r['epsilon']) for r in reference['cases']] == inventory

    from flint import arb, acb, ctx
    ctx.prec = 256
    pi, ii = arb.pi(), acb(0, 1)
    counts = dict(saved_cases_reused=0, candidates=0,
        center_gradient_evaluations=0, center_jacobian_evaluations=0,
        center_logarithms=0, center_cotangents=0,
        affine_curvature_sines=0, full_curvature_sines=0,
        inverse_proposals=0, response_proposals=0, root_solves=0,
        primitive_action_evaluations=0, quantum_source_evaluations=0,
        subdivisions=0, precision_retries=0, candidate_errors=0)

    def ar(value):
        value = F(value)
        return arb(value.numerator)/arb(value.denominator)

    def cp(value):
        return acb(ar(value[0]), ar(value[1]))

    def ends(value):
        if not value.is_finite():
            raise ArithmeticError('nonfinite outward value')
        return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

    def rr(value):
        lo, hi = ends(value)
        return dict(finite=True, lower_rational=str(lo), upper_rational=str(hi))

    def cr(value):
        return dict(real=rr(value.real), imag=rr(value.imag))

    def modulus_upper(value):
        return ends(abs(value))[1]

    def mv(matrix, vector):
        return [sum((a*b for a, b in zip(row, vector)), acb(0)) for row in matrix]

    def curvature(center, radius, stage, name):
        distance = min(center[0]-radius, 1-center[0]-radius)
        witness = dict(name=name, stage=stage, regular=False,
                       center_exact=list(map(str, center)),
                       radius_upper_rational=str(radius),
                       real_interval_rational=[str(center[0]-radius), str(center[0]+radius)],
                       strip_distance_rational=str(distance))
        if not 0 < distance <= F(1, 2):
            raise DomainFailure('shared argument disk leaves original regular strip', witness)
        sine = (pi*ar(distance)).sin()
        counts[stage+'_curvature_sines'] += 1
        witness['sine'] = rr(sine)
        if not sine > 0:
            raise DomainFailure('positive strip sine not separated', witness)
        bound = pi*pi/(sine*sine)
        upper = ends(bound)[1]
        witness.update(sine=rr(sine), curvature_bound=rr(bound),
                       curvature_upper_rational=str(upper), regular=True)
        return upper, witness

    cases = []
    for case_index, (saved, certified) in enumerate(zip(source['cases'], reference['cases'])):
        beta, epsilon = saved['beta'], saved['epsilon']
        row = dict(case_index=case_index, beta=beta, epsilon=epsilon,
            status='inconclusive', candidates=[],
            saved_affine_case_canonical_sha256=canonical_sha(saved),
            canonical_reference_case_sha256=canonical_sha(certified))
        setup_error = None
        try:
            assert certified['canonical_reference_certified'] is True
            center = list(map(pair, saved['center']))
            assert center == list(map(pair, certified['proposed_centers']))
            assert pair(saved['parameter_center']) == pair(certified['outside_coordinate']) == CENTERS[beta]
            radius = F(saved['parameter_radius_rational'])
            assert radius == DISK_RADII[beta]
            assert len(center) == len(saved['derivative_proposal']) == 5
            Bexact = [list(map(pair, part)) for part in saved['inverse_proposal']]
            assert len(Bexact) == 5 and all(len(part) == 5 for part in Bexact)
            uexact = list(map(pair, saved['derivative_proposal']))
            assert [F(c['multiplier_rational']) for c in saved['candidates']] == list(MULTIPLIERS)
            for old, multiplier in zip(saved['candidates'], MULTIPLIERS):
                assert list(map(F, old['error_radii_rational'])) == [multiplier*x for x in ERROR_RADII]
            counts['saved_cases_reused'] += 1
            B, u = [[cp(z) for z in part] for part in Bexact], list(map(cp, uexact))
            q0, b0 = list(map(cp, center)), cp(CENTERS[beta])
            uabs = list(map(modulus_upper, u))
            widths = [radius*x for x in uabs]
            M, n, c = chirp(epsilon)
            inventory_rows = terms(epsilon)
            row.update(center=pairs_record(center),
                parameter_center=list(map(str, CENTERS[beta])),
                parameter_radius_rational=str(radius),
                saved_inverse_proposal=saved['inverse_proposal'],
                saved_response_proposal=saved['derivative_proposal'],
                inverse_exact=[pairs_record(part) for part in Bexact],
                response_exact=pairs_record(uexact),
                chirp_matrix=M, chirp_external=n,
                chirp_constant_rational=list(map(str, c)))
            f0 = [acb(0) for _ in range(5)]
            J0 = [[ii*pi*M[i][j] for j in range(5)] for i in range(5)]
            for i in range(5):
                ch = linear(M[i], center, (n[i]*CENTERS[beta][0]+c[i],
                                           n[i]*CENTERS[beta][1]))
                f0[i] = ii*pi*cp(ch)
            term_data = []
            row['primitive_terms'] = term_data
            L0 = None
            for item in inventory_rows:
                v, sigma, external = item['v'], item['sigma'], item['external']
                z0 = linear(v, center, (external*CENTERS[beta][0]+F(item['offset_rational']),
                                        external*CENTERS[beta][1]))
                lam = linear(v, uexact, (F(external), F(0)))
                Bv = [linear(v, part) for part in Bexact]
                za, la = cp(z0), cp(lam)
                term_record = dict(**item, center_exact=list(map(str, z0)),
                    lambda_exact=list(map(str, lam)),
                    lambda_squared_modulus_rational=str(squared_modulus(lam)),
                    preconditioned_vector_exact=pairs_record(Bv))
                term_data.append(term_record)
                if not 0 < z0[0] < 1:
                    raise DomainFailure('center primitive left original strip',
                        dict(name=item['name'], stage='center', center_exact=list(map(str, z0))))
                argument = 2*(pi*za).sin()
                term_record['center_log_argument'] = cr(argument)
                if not argument.real > 0:
                    raise DomainFailure('center logarithm branch not separated',
                        dict(name=item['name'], stage='center', center_log_argument=cr(argument)))
                jvalue = argument.log()
                jp = pi*(pi*za).cot()
                counts['center_logarithms'] += 1
                counts['center_cotangents'] += 1
                if not (jvalue.is_finite() and jp.is_finite()):
                    raise ArithmeticError('nonfinite center primitive derivative')
                for i in range(5):
                    f0[i] += sigma*v[i]*jvalue
                    for j in range(5):
                        J0[i][j] += sigma*v[i]*v[j]*jp
                if item['name'] == 's+b':
                    L0 = jp+ii*pi
                lamabs = modulus_upper(la)
                coefficient_bounds = [abs(sigma)*modulus_upper(cp(z)) for z in Bv]
                affine_radius = radius*lamabs
                term_record.update(
                    lambda_modulus_upper_rational=str(lamabs),
                    preconditioned_sigma_modulus_uppers_rational=list(map(str, coefficient_bounds)),
                    center_j=cr(jvalue), center_j_prime=cr(jp))
                maff, affine_witness = curvature(z0, affine_radius, 'affine', item['name'])
                term_record['affine_curvature'] = affine_witness
            assert L0 is not None and len(term_data) == 11
            counts['center_gradient_evaluations'] += 1
            counts['center_jacobian_evaluations'] += 1
            center_defect = mv(B, f0)
            linear_vector = mv(J0, u)
            linear_vector[4] += L0
            linear_defect = mv(B, linear_vector)
            BJ0 = [[sum((B[i][k]*J0[k][j] for k in range(5)), acb(0))
                    for j in range(5)] for i in range(5)]
            E0 = [[int(i == j)-BJ0[i][j] for j in range(5)] for i in range(5)]
            E0plus = [[modulus_upper(z) for z in part] for part in E0]
            cplus, vplus = list(map(modulus_upper, center_defect)), list(map(modulus_upper, linear_defect))
            quadratic_terms = [[
                radius*radius/2*F(term['preconditioned_sigma_modulus_uppers_rational'][i])
                *F(term['affine_curvature']['curvature_upper_rational'])
                *F(term['lambda_squared_modulus_rational']) for term in term_data]
                for i in range(5)]
            resid = [cplus[i]+radius*vplus[i]+sum(quadratic_terms[i])
                     for i in range(5)]
            row.update(center=pairs_record(center), parameter_center=list(map(str, CENTERS[beta])),
                parameter_radius_rational=str(radius),
                saved_inverse_proposal=saved['inverse_proposal'],
                saved_response_proposal=saved['derivative_proposal'],
                inverse_exact=[pairs_record(part) for part in Bexact], response_exact=pairs_record(uexact),
                response_modulus_uppers_rational=list(map(str, uabs)),
                affine_halfwidths_rational=list(map(str, widths)),
                affine_coordinate_box=box_record(center, widths),
                affine_inside_common_domain=common_containment(center, widths),
                chirp_matrix=M, chirp_external=n, chirp_constant_rational=list(map(str, c)),
                primitive_terms=term_data, center_gradient=list(map(cr, f0)),
                center_jacobian=[list(map(cr, part)) for part in J0], center_external_forcing=cr(L0),
                preconditioned_center_residual=list(map(cr, center_defect)),
                preconditioned_linear_defect=list(map(cr, linear_defect)),
                center_error_matrix=[list(map(cr, part)) for part in E0],
                center_error_matrix_upper_rational=[list(map(str, part)) for part in E0plus],
                center_residual_upper_rational=list(map(str, cplus)),
                linear_defect_upper_rational=list(map(str, vplus)),
                affine_quadratic_terms_rational=[list(map(str, part)) for part in quadratic_terms],
                affine_residual_upper_rational=list(map(str, resid)))
        except Exception as error:
            setup_error = type(error).__name__+': '+str(error)
            row['setup_error'] = setup_error
            row['setup_error_kind'] = 'domain' if isinstance(error, DomainFailure) else 'error'
            if isinstance(error, DomainFailure) and error.witness is not None:
                row['setup_failure_witness'] = error.witness

        for multiplier in MULTIPLIERS:
            counts['candidates'] += 1
            rho = [multiplier*x for x in ERROR_RADII]
            candidate = dict(multiplier_rational=str(multiplier),
                error_radii_rational=list(map(str, rho)), status='inconclusive',
                criterion_verified=False, common_domain_containment_required=False)
            try:
                if setup_error:
                    candidate['error'] = 'case setup failed: '+setup_error
                    candidate['failure_kind'] = row['setup_error_kind']
                    if row['setup_error_kind'] == 'error':
                        counts['candidate_errors'] += 1
                    row['candidates'].append(candidate)
                    continue
                fullwidths = [w+r for w, r in zip(widths, rho)]
                candidate['full_coordinate_box'] = box_record(center, fullwidths)
                candidate['inside_original_common_domain'] = common_containment(center, fullwidths)
                witnesses = central_root_containment(certified, center, rho)
                candidate['saved_central_root_containment'] = witnesses
                candidate['saved_central_root_contained'] = all(w['strictly_contained'] for w in witnesses)
                if not candidate['saved_central_root_contained']:
                    raise DomainFailure('saved central canonical root not contained')
                full_terms = []
                candidate['full_primitive_terms'] = full_terms
                Eplus = [part[:] for part in E0plus]
                for term in term_data:
                    v = term['v']
                    fullradius = F(term['affine_curvature']['radius_upper_rational']) + sum(
                        abs(vj)*rj for vj, rj in zip(v, rho))
                    full_record = dict(name=term['name'])
                    full_terms.append(full_record)
                    mfull, witness = curvature(pair(term['center_exact']), fullradius,
                                               'full', term['name'])
                    full_record['full_curvature'] = witness
                    contribution = [[F(term['preconditioned_sigma_modulus_uppers_rational'][i])
                                     *mfull*fullradius*abs(v[j]) for j in range(5)]
                                    for i in range(5)]
                    for i in range(5):
                        for j in range(5):
                            Eplus[i][j] += contribution[i][j]
                    full_record['error_matrix_contribution_rational'] = [
                        list(map(str, part)) for part in contribution]
                linear_error = [sum(x*r for x, r in zip(part, rho)) for part in Eplus]
                margins = [rho[i]-resid[i]-linear_error[i] for i in range(5)]
                eta = max(x/r for x, r in zip(linear_error, rho))
                passed = eta < 1 and all(x > 0 for x in margins)
                candidate.update(full_primitive_terms=full_terms,
                    all_full_original_log_disks_regular=True,
                    error_matrix_upper_rational=[list(map(str, part)) for part in Eplus],
                    linear_error_upper_rational=list(map(str, linear_error)),
                    contraction_upper_rational=str(eta),
                    affine_residual_upper_rational=list(map(str, resid)),
                    inclusion_margin_rational=list(map(str, margins)), criterion_verified=passed)
                if passed:
                    candidate['status'] = 'uniform correlated affine enclosure certified'
                    candidate['identification'] = 'saved center root, local IFT, connected-disk identity theorem'
            except Exception as error:
                candidate['error'] = type(error).__name__+': '+str(error)
                candidate['failure_kind'] = 'domain' if isinstance(error, DomainFailure) else 'error'
                if isinstance(error, DomainFailure) and error.witness is not None:
                    candidate['failure_witness'] = error.witness
                if not isinstance(error, DomainFailure):
                    counts['candidate_errors'] += 1
            row['candidates'].append(candidate)
        assert len(row['candidates']) == 4
        if any(c['criterion_verified'] for c in row['candidates']):
            row['status'] = 'uniform correlated affine family certified'
        cases.append(row)
        print(json.dumps(dict(beta=beta, epsilon=epsilon, status=row['status'],
            candidates=[dict(multiplier=c['multiplier_rational'], status=c['status'],
                             eta=c.get('contraction_upper_rational'), error=c.get('error'))
                        for c in row['candidates']])), flush=True)

    assert len(cases) == 4 and counts['candidates'] == 16
    changed = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    successful = sum(row['status'] == 'uniform correlated affine family certified' for row in cases)
    result = dict(status='completed fixed protocol' if not changed else 'input failure',
        certified_families=successful, all_full_disk_families_certified=successful == 4 and not changed,
        source_path=SOURCE, source_sha256=inputs[SOURCE], proof_sha256=inputs[PROOF],
        script_sha256=inputs[own], reference_path=REFERENCE, reference_sha256=inputs[REFERENCE],
        precision_bits=256, exact_saved_proposals_only=True, counts=counts, cases=cases,
        input_sha256=inputs, changed_inputs=changed,
        full_common_domain_containment_required=False,
        canonical_identification='saved center enclosure plus holomorphic continuation',
        uniform_source_bound_claimed=False, finite_word_realization_claimed=False,
        knot_theorem_claimed=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], certified_families=successful,
                         sha256=sha(args.output))), flush=True)


if __name__ == '__main__':
    main()
