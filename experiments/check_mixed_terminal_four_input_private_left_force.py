#!/usr/bin/env python3
"""Saved-only whole-D4 private-left force check; no analytic evaluator."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_four_input_private_left_force.md'
SOURCE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
OLD = 'repro/results/research-mixed-terminal-affine-family.json'
REFERENCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
PINNED = {
    PROOF: '28fd9890765e9b4f666d7fe11bc0364c4e1b6c9de4ae45506251c0ec27679f3b',
    SOURCE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    OLD: '908232a2fc15d731c13803cd503c7b0d70c579f9cbf1896543f7233df2196370',
    REFERENCE: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    'notes/research_mixed_terminal_correlated_affine_family_certificate.md':
        '0ba6a11f26a17e3642a41c6bd97cf93a01c1c7a5c4dd2437d3ee23435dfb8957',
    'experiments/certify_mixed_terminal_correlated_affine_family.py':
        'db3e96fd4594707b099deca1543f090e5d132769bb02905e60619aa5a52e07f9',
    'notes/research_mixed_terminal_private_left_uniform_force.md':
        '20361d2a52affe5273ab4aa056f66b250fa498bb9f87742609f1d9450b9b2ee2',
    'notes/research_mixed_terminal_private_left_joint_transfer.md':
        '41de4b6ab3197e2180bab6174fe01406d525a551ae470f964d0478e8171075ff',
    'notes/research_mixed_full_unselected_plateau.md':
        'abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6',
    'notes/research_mixed_terminal_four_coupled_source_continuation.md':
        'ee52ddb19be76ed0147a2e23309f2feafd812b4f8758eecabdd3096b8f0b0830',
    'repro/results/research-mixed-terminal-four-source-stage4-attempt01.json':
        'e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3',
    'repro/results/research-mixed-terminal-four-source-replay.json':
        '3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79',
}
NAMES = ('e', 'xi', 't', 'a', 's')
ROUNDED = {
    'e': tuple(map(F, ('.3443', '.3473', '-.0394', '-.0364'))),
    't': tuple(map(F, ('.3022', '.3131', '-.0707', '-.0599'))),
    'a': tuple(map(F, ('.2996', '.3212', '-.0631', '-.0416'))),
}


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def mul(a, b):
    result = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs, details, error = {}, {}, None

    def bind(name, digest):
        assert name not in inputs or inputs[name] == digest, name
        assert sha(ROOT/name) == digest, name
        inputs[name] = digest

    try:
        for name, digest in PINNED.items():
            bind(name, digest)
        bind(own, sha(ROOT/own))
        source, old, reference = [
            json.loads((ROOT/name).read_text()) for name in (SOURCE, OLD, REFERENCE)]
        for record in (source, old, reference):
            for key in ('input_sha256', 'dependencies_sha256'):
                for name, digest in record.get(key, {}).items():
                    bind(name, digest)
        assert source['status'] == 'completed fixed protocol'
        assert source['changed_inputs'] == [] and source['precision_bits'] == 256
        assert source['certified_families'] == 2
        assert not source['all_full_disk_families_certified']
        assert source['source_path'] == OLD and source['source_sha256'] == inputs[OLD]
        assert source['reference_path'] == REFERENCE
        assert source['reference_sha256'] == inputs[REFERENCE]
        assert source['proof_sha256'] == inputs[
            'notes/research_mixed_terminal_correlated_affine_family_certificate.md']
        assert source['script_sha256'] == inputs[
            'experiments/certify_mixed_terminal_correlated_affine_family.py']
        inventory = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for record in (source, old, reference):
            assert [(r['beta'], r['epsilon']) for r in record['cases']] == inventory
            assert record['changed_inputs'] == []
        row, saved, certified = (record['cases'][3] for record in (source, old, reference))
        assert row['status'] == 'uniform correlated affine family certified'
        assert row['saved_affine_case_canonical_sha256'] == canonical_sha(saved)
        assert row['canonical_reference_case_sha256'] == canonical_sha(certified)
        assert certified['canonical_reference_certified'] is True
        center = [tuple(map(F, z)) for z in row['center']]
        response = [tuple(map(F, z)) for z in row['response_exact']]
        assert center == [tuple(map(F, z)) for z in saved['center']]
        assert center == [tuple(map(F, z)) for z in certified['proposed_centers']]
        assert response == [tuple(map(F, z)) for z in saved['derivative_proposal']]
        assert tuple(map(F, row['parameter_center'])) == (F(3, 10), -F(13, 250))
        radius = F(row['parameter_radius_rational'])
        assert radius == F(8, 125)
        candidates = row['candidates']
        assert list(map(F, [c['multiplier_rational'] for c in candidates])) == [
            F(1, 4), F(1, 2), F(1), F(2)]
        candidate = candidates[2]
        assert candidate['criterion_verified'] is True
        assert candidate['status'] == 'uniform correlated affine enclosure certified'
        assert candidate['saved_central_root_contained'] is True
        assert candidate['all_full_original_log_disks_regular'] is True
        assert len(candidate['full_primitive_terms']) == 11
        for term in candidate['full_primitive_terms']:
            assert term['full_curvature']['regular'] is True
            assert F(term['full_curvature']['strip_distance_rational']) > 0
        rho = list(map(F, candidate['error_radii_rational']))
        assert rho == list(map(F, ('1/500', '1/1000', '1/200', '1/200', '1/100')))
        for item, radius_i in zip(candidate['saved_central_root_containment'], rho):
            assert item['strictly_contained'] is True
            assert F(item['candidate_radius_squared_rational']) == radius_i**2
            assert F(item['maximum_distance_squared_rational']) < radius_i**2
        E = [list(map(F, line)) for line in candidate['error_matrix_upper_rational']]
        residual = list(map(F, candidate['affine_residual_upper_rational']))
        assert residual == list(map(F, row['affine_residual_upper_rational']))
        assert len(E) == len(residual) == 5 and all(len(line) == 5 for line in E)
        assert all(value >= 0 for line in E for value in line)
        assert all(value >= 0 for value in residual)
        linear = [sum(E[i][j]*rho[j] for j in range(5)) for i in range(5)]
        assert linear == list(map(F, candidate['linear_error_upper_rational']))
        eta = max(value/radius_i for value, radius_i in zip(linear, rho))
        assert eta == F(candidate['contraction_upper_rational']) < 1
        posterior = [residual[i]+linear[i] for i in range(5)]
        margins = [rho[i]-posterior[i] for i in range(5)]
        assert margins == list(map(F, candidate['inclusion_margin_rational']))
        assert all(value > 0 for value in margins)
        rounded_errors = [F(n, 1000000) for n in (655, 281, 2119, 3804, 9592)]
        assert all(p < bound for p, bound in zip(posterior, rounded_errors))
        widths = list(map(F, row['affine_halfwidths_rational']))
        abs_u = list(map(F, row['response_modulus_uppers_rational']))
        assert widths == [radius*x for x in abs_u]
        assert all(x >= 0 and x*x >= z[0]**2+z[1]**2 for x, z in zip(abs_u, response))
        boxes = {}
        for i, name in enumerate(NAMES):
            extent = widths[i]+posterior[i]
            box = (center[i][0]-extent, center[i][0]+extent,
                   center[i][1]-extent, center[i][1]+extent)
            boxes[name] = box
            if name in ROUNDED:
                lo, hi, bot, top = ROUNDED[name]
                assert lo < box[0] <= box[1] < hi
                assert bot < box[2] <= box[3] < top
        assert F('.299') < boxes['a'][0] and boxes['a'][1] < F('.36')
        assert F('.302') < boxes['t'][0] and boxes['t'][1] < F('.35')
        assert -F('.071') < boxes['t'][2] and boxes['t'][3] < -F('.02')
        assert F('.333') < boxes['e'][0] and boxes['e'][1] < F('.363')
        assert -F('.051') < boxes['e'][2] and boxes['e'][3] < -F('.019')
        details.update(
            beta=1, epsilon=1, candidate_index=2, multiplier_rational='1',
            source_case_canonical_sha256=canonical_sha(row),
            source_candidate_canonical_sha256=canonical_sha(candidate),
            center_exact=[list(map(str, z)) for z in center],
            response_exact=[list(map(str, z)) for z in response],
            parameter_center=row['parameter_center'], parameter_radius_rational=str(radius),
            original_error_radii_rational=list(map(str, rho)),
            affine_residual_upper_rational=list(map(str, residual)),
            error_matrix_upper_rational=[list(map(str, line)) for line in E],
            linear_error_upper_rational=list(map(str, linear)),
            posterior_error_upper_rational=list(map(str, posterior)),
            posterior_rounded_upper_rational=list(map(str, rounded_errors)),
            affine_halfwidths_rational=list(map(str, widths)),
            posterior_coordinate_boxes_rational={k:list(map(str, v)) for k,v in boxes.items()},
            containing_coordinate_boxes_rational={k:list(map(str, v)) for k,v in ROUNDED.items()})

        T, A, height = F('.302'), F('.299'), F('.071')
        r0, k, c1, c2, R0 = map(F, ('.63', '.32', '.81', '.9', '.94'))
        X = (2*T-F(1, 2))*F(157, 50)
        Y = (2*(T+A)-1)*F(157, 50)
        Z = (2*(T+F(27, 100))-1)*F(157, 50)
        W = 2*height*F(22, 7)
        gaps = [X-X**3/6-k, c1-(1-Y**2/2+Y**4/24),
                c2-(1-Z**2/2+Z**4/24),
                1/r0-1-W-W**2/(2*(1-W/3))]
        assert gaps == list(map(F, (
            '1107220079/1464843750000',
            '41359056567086399/9375000000000000000',
            '368268659413/762939453125000', '483193/20110500')))
        z = F(157, 2500)
        selected_gap = 1+z+z*z/2-F(50, 47)
        assert selected_gap == F(553503, 587500000)
        assert all(value > 0 for value in gaps+[selected_gap])
        base = [F(1), 2*k, F(1)]
        D = mul(mul(base, base), base)
        N = mul([R0*R0, 2*c1*R0, F(1)], [F(1), 2*c2, F(1)])
        P = [D[i]-(N[i] if i < len(N) else 0) for i in range(7)]
        shifted = [sum(P[j]*comb(j, i)*r0**(j-i)*(1-r0)**i
                       for j in range(i, 7)) for i in range(7)]
        bernstein = [sum(shifted[j]*F(comb(i,j),comb(6,j)) for j in range(i+1))
                     for i in range(7)]
        expected = [F(n, 15000000000000) for n in (
            2461503846015, 6691602565740, 13102522533472, 22512461911476,
            36025059204800, 55128208400000, 81831360000000)]
        assert bernstein == expected and min(bernstein) == bernstein[0] > 0
        force_gap = bernstein[0]/(2*(2+2*k)**3)
        assert force_gap == F(54700085467, 12266496000000) > 0
        details.update(elementary_witnesses_rational=list(map(str, gaps)),
            selected_height_witness_rational=str(selected_gap),
            polynomial_coefficients_rational=list(map(str, P)),
            bernstein_coefficients_rational=list(map(str, bernstein)),
            negative_face_force_gap_rational=str(force_gap),
            selected_height_interval=['1/100', '7/500'],
            actual_source_additional_debit_rational='1/20000')
    except Exception as exc:
        error = dict(type=type(exc).__name__, message=str(exc))
    changed = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    passed = error is None and not changed
    result = dict(status='passed' if passed else 'failed',
        source_path=SOURCE, source_sha256=PINNED[SOURCE],
        proof_path=PROOF, proof_sha256=PINNED[PROOF], checker_sha256=inputs.get(own),
        input_sha256=inputs, changed_inputs=changed, details=details, error=error,
        whole_D4_force_contraction_proved=passed,
        bare_source_scope='actual oriented and inverse-feasible K4 inputs only',
        uniform_negative_main_budget_claimed=False,
        whole_word_or_knot_theorem_claimed=False,
        analytic_evaluations=0, root_evaluations=0, source_replays=0)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(status=result['status'], bindings=len(inputs),
                         output_sha256=sha(args.output), error=error)))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
