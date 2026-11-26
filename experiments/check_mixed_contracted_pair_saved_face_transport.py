#!/usr/bin/env python3
"""Fixed exact transport of nine saved gradients to enlarged source faces.

Only stored rational enclosure endpoints are used. There is no analytic
library, function evaluation, new proposal, optimizer, gain or subdivision.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-contracted-pair-nine-faces.json'
SOURCE_WRITER = 'experiments/check_mixed_contracted_pair_nine_faces.py'
OLD_PROTOCOL = 'notes/research_mixed_contracted_pair_nine_faces_protocol.md'
PROTOCOL = 'notes/research_mixed_contracted_pair_saved_face_transport_protocol.md'
TAIL_THEORY = 'notes/research_mixed_contracted_pair_enlarged_tail_reduction.md'
CONCAVITY_THEORY = 'notes/research_mixed_contracted_pair_enlarged_rectangle.md'
PINNED = {
    SOURCE: '174752c3b6f5c026dc4153287e153515d7f94e12959a0188f188d4cbf4d42cbc',
    SOURCE_WRITER: '94b35c6d1877737ca020d128e52a6bde77416ecbebc9d4c6ed01d82c1eb415ac',
    OLD_PROTOCOL: '957aadc2dfc00126dd8474d0f3159081001c565326401adeb8f9d69fe43cfa74',
    'notes/research_mixed_contracted_pair_nine_faces_diagnosis.md':
        '0a61ed9f0ce3a8ec1c6e6b8f8927f51469081ae40ae9f4432fa173ec70af0631',
    PROTOCOL: 'fb596d653a0e8b446039db010ddc60f97b632e89200ef24876c800917ed3840c',
    TAIL_THEORY: '5652cc1d58beabc5929ef6ff9103abfa3415c06a747338ee1bb2b40efa654eda',
    CONCAVITY_THEORY: '597761e942e2956554fe4f25d22de0156838a880e37c04e4fa8fe843e087f0fc',
}
NAMES = ('s', 't', 'p', 'q')
OLD_BOX = ((F(1, 4), F(9, 20)), (F(1, 4), F(9, 20)),
           (F(1, 5), F(21, 50)), (F(1, 5), F(21, 50)))
NEW_BOX = ((F(1, 4), F(1, 2)), (F(1, 5), F(9, 20)),
           (F(1, 5), F(21, 50)), (F(1, 5), F(21, 50)))
ACTION_LOWER, GAP = F(3781, 2500), F(1, 100000)
TARGET = F(151239, 100000)
FAR_UPPER = F(2261, 1500)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def iv(value):
    require(value['finite'] is True, 'nonfinite saved interval')
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    require(lo <= hi, 'reversed saved interval')
    return lo, hi


def interval_record(value):
    return dict(finite=True, lower_rational=str(value[0]), upper_rational=str(value[1]))


def inventory():
    rows = []
    for index, name in enumerate(NAMES):
        for side in range(2):
            rows.append(dict(old_name=name+'='+str(OLD_BOX[index][side]),
                new_name=name+'='+str(NEW_BOX[index][side]), fixed_index=index,
                old_fixed=OLD_BOX[index][side], new_fixed=NEW_BOX[index][side],
                central_side=('lower', 'upper')[side]))
    rows.append(dict(old_name='s=0', new_name='s=0', fixed_index=0,
        old_fixed=F(0), new_fixed=F(0), central_side=None))
    return rows


def read_source_row(row, face):
    saved = row['face']
    fixed = face['fixed_index']
    free = [i for i in range(4) if i != fixed]
    require(saved['name'] == face['old_name'] and saved['fixed_index'] == fixed,
            'old face identity')
    require(F(saved['fixed_rational']) == face['old_fixed'], 'old fixed coordinate')
    require(saved['free_indices'] == free, 'old free coordinate inventory')
    require(tuple(tuple(map(F, pair)) for pair in saved['bounds_rational']) == OLD_BOX,
            'old central box')
    if face['central_side'] is not None:
        require(saved['central_side'] == face['central_side'], 'old face side')
    require(row['status'] in ('passed', 'inconclusive'), 'invalid inherited support')
    require(row['exact_support_in_face'] is True, 'inherited support guard')
    require(row['support_quantization_denominator'] == 10**12, 'old support denominator')
    iterations = row['proposal']['iterations']
    require(len(iterations) == 32, 'old proposal iteration count')
    for k, step in enumerate(iterations):
        require(step['index'] == k and F(step['damping']) == (F(1, 2) if k < 8 else F(1)),
                'old proposal schedule')
    y = tuple(F(row['support_coordinates_rational'][name]) for name in NAMES)
    require(y[fixed] == face['old_fixed'], 'old support fixed value')
    for i in free:
        require(OLD_BOX[i][0] < y[i] < OLD_BOX[i][1], 'old support interval')
        require((y[i]*10**12).denominator == 1, 'old support quantization')
    require(all(0 < y[i]+y[i+1] < 1 for i in range(3)), 'old support physical regularity')
    for i, name in enumerate(NAMES):
        lo, hi = iv(row['support_input_enclosures'][name])
        require(lo <= y[i] <= hi, 'old rational point enclosed')
    value = iv(row['E_at_support'])
    gradient = tuple(iv(row['gradient_at_support'][name]) for name in NAMES)
    upper = F(row['whole_face_upper_rational'])
    require(upper == iv(row['whole_face_tangent_bound'])[1], 'old recorded upper association')
    require(F(row['strict_target_margin_rational']) == TARGET-upper, 'old margin association')
    require(row['strict_comparison'] is (upper < TARGET), 'old comparison association')
    require((row['status'] == 'passed') is row['strict_comparison'], 'old status association')
    # Do not recombine twice-rounded old Arb products. Their reviewed writer
    # establishes these enclosures; the new transport below is fully rational.
    return y, value, gradient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/
        'repro/results/research-mixed-contracted-pair-saved-face-transport.json')
    args = parser.parse_args()
    with args.output.open('x') as stream:
        inputs = {}
        faces = inventory()
        result = dict(status='initializing', input_sha256=inputs, faces=[],
            source_path=SOURCE, protocol_path=PROTOCOL,
            script_path=str(Path(__file__).resolve().relative_to(ROOT)),
            scope='Saved outward affine supports for the enlarged physical complement only.',
            new_box_rational=[[str(lo), str(hi)] for lo, hi in NEW_BOX],
            action_lower_rational=str(ACTION_LOWER), target_rational=str(TARGET),
            requested_gap_rational=str(GAP), far_region_upper_rational=str(FAR_UPPER),
            pending_faces=[f['new_name'] for f in faces], active_face=None,
            rational_support_term_count=0, rational_endpoint_product_count=0,
            new_analytic_calls=0, new_proposals=0, new_optimization_calls=0,
            nonmain_complex_contour_claim=False, whole_source_claim=False)

        def bind(name, expected):
            require(isinstance(name, str) and isinstance(expected, str) and len(expected) == 64,
                    'pending/malformed source binding: '+str(name))
            require(name not in inputs or inputs[name] == expected, 'conflicting input pin: '+name)
            require(sha(ROOT/name) == expected, 'input hash mismatch: '+name)
            inputs[name] = expected

        try:
            require(TARGET == ACTION_LOWER-GAP and FAR_UPPER < TARGET, 'fixed rational targets')
            for name, expected in PINNED.items():
                bind(name, expected)
            bind(result['script_path'], sha(ROOT/result['script_path']))
            result['script_sha256'] = inputs[result['script_path']]
            result['protocol_sha256'] = inputs[PROTOCOL]
            result['source_sha256'] = inputs[SOURCE]
            result['analytic_premises'] = {
                CONCAVITY_THEORY: inputs[CONCAVITY_THEORY], TAIL_THEORY: inputs[TAIL_THEORY]}
            source = json.loads((ROOT/SOURCE).read_text())
            require(source['status'] == 'inconclusive' and source['changed_inputs'] == [],
                    'original experiment status must be preserved')
            require(source['input_binding_count'] == len(source['input_sha256']) == 33,
                    'inherited binding inventory')
            for name, expected in source['input_sha256'].items():
                bind(name, expected)
            require(source['script_sha256'] == inputs[SOURCE_WRITER] and
                    source['protocol_sha256'] == inputs[OLD_PROTOCOL], 'source writer/protocol binding')
            require(source['script_path'] == SOURCE_WRITER and source['protocol_path'] == OLD_PROTOCOL,
                    'source writer/protocol path')
            require(source['all_nine_support_bounds_valid'] is True and
                    source['all_nine_strict_comparisons_pass'] is False,
                    'original result interpretation')
            require(source['analytic_support_evaluations'] == 9 and len(source['faces']) == 9
                    and source['pending_faces'] == [] and source['active_face'] is None,
                    'original completed inventory')
            require(source['precision_bits'] == 256 and F(source['target_rational']) == TARGET
                    and F(source['action_lower_rational']) == ACTION_LOWER,
                    'original precision/target metadata')
            failures = [r['face']['name'] for r in source['faces'] if not r['strict_comparison']]
            require(failures == ['s=9/20', 't=1/4'], 'original failed face inventory')
            result['inherited_source_status'] = source['status']
            result['inherited_failed_faces'] = failures
            result['inherited_input_binding_count'] = len(source['input_sha256'])

            for old, face in zip(source['faces'], faces):
                row = dict(old_face=face['old_name'], new_face=face['new_name'],
                    source_row_canonical_sha256=canonical(old), status='initializing',
                    original_status=old['status'], original_strict_comparison=old['strict_comparison'])
                result['faces'].append(row)
                result['active_face'] = face['new_name']
                try:
                    y, value, gradient = read_source_row(old, face)
                    special = face['old_name'] == 's=0'
                    supporting_domain = list(NEW_BOX)
                    if special:
                        supporting_domain[0] = F(0), F(0)
                    require(all(lo <= point <= hi for point, (lo, hi) in zip(y, supporting_domain)),
                            'old support outside the new concavity domain')
                    target = list(NEW_BOX)
                    target[face['fixed_index']] = face['new_fixed'], face['new_fixed']
                    require(all(lo <= hi for lo, hi in target), 'target rectangle')
                    require(all(target[i][1]+target[i+1][1] < 1 for i in range(3)),
                            'new target outside strict physical support')
                    row.update(support_coordinates_rational=dict(zip(NAMES, map(str, y))),
                        saved_E=interval_record(value), saved_gradient={name: interval_record(v)
                            for name, v in zip(NAMES, gradient)},
                        concavity_domain_rational=[[str(lo), str(hi)] for lo, hi in supporting_domain],
                        target_face_rational=[[str(lo), str(hi)] for lo, hi in target],
                        original_tangent_upper_rational=old['whole_face_upper_rational'], terms=[])
                    upper = value[1]
                    for i, name in enumerate(NAMES):
                        displacement = target[i][0]-y[i], target[i][1]-y[i]
                        products = [g*d for g in gradient[i] for d in displacement]
                        contribution = max(products)
                        row['terms'].append(dict(coordinate=name,
                            derivative=interval_record(gradient[i]),
                            displacement_rationals=list(map(str, displacement)),
                            product_order='gradient lower/upper, then displacement lower/upper',
                            endpoint_products_rational=list(map(str, products)),
                            support_upper_rational=str(contribution), zero_cap_applied=False))
                        upper += contribution
                        result['rational_support_term_count'] += 1
                        result['rational_endpoint_product_count'] += 4
                    row['transported_face_upper_rational'] = str(upper)
                    row['strict_target_margin_rational'] = str(TARGET-upper)
                    row['strict_comparison'] = upper < TARGET
                    row['status'] = 'passed' if row['strict_comparison'] else 'inconclusive'
                except Exception as error:
                    row['status'] = 'failed'
                    row['error'] = dict(type=type(error).__name__, message=str(error))
                result['pending_faces'].remove(face['new_name'])
                result['active_face'] = None
            valid = all(row['status'] in ('passed', 'inconclusive') for row in result['faces'])
            require(len(result['faces']) == 9 and result['pending_faces'] == [], 'new face inventory')
            if valid:
                require(result['rational_support_term_count'] == 36 and
                        result['rational_endpoint_product_count'] == 144, 'fixed arithmetic inventory')
                maximum = max(F(row['transported_face_upper_rational']) for row in result['faces'])
                tail_upper = max(FAR_UPPER, maximum)
                result['maximum_face_upper_rational'] = str(maximum)
                result['whole_physical_complement_upper_rational'] = str(tail_upper)
                result['physical_complement_gap_lower_rational'] = str(ACTION_LOWER-tail_upper)
            passed = valid and all(row['strict_comparison'] for row in result['faces'])
            result['all_nine_transport_bounds_valid'] = valid
            result['all_nine_strict_comparisons_pass'] = passed
            result['status'] = 'passed' if passed else ('inconclusive' if valid else 'failed')
        except BaseException as error:
            result['status'] = 'failed'
            result['error'] = dict(type=type(error).__name__, message=str(error))
        finally:
            changes = []
            for name, expected in inputs.items():
                try:
                    actual = sha(ROOT/name)
                except OSError:
                    actual = None
                if actual != expected:
                    changes.append(dict(path=name, expected=expected, actual=actual))
            result['changed_inputs'] = changes
            result['input_binding_count'] = len(inputs)
            if changes:
                result['status'] = 'failed'
            json.dump(result, stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write('\n')
        print(json.dumps(dict(status=result['status'], faces=len(result['faces']),
            terms=result['rational_support_term_count'], products=result['rational_endpoint_product_count'],
            changed_inputs=len(result['changed_inputs']))))
        return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())
