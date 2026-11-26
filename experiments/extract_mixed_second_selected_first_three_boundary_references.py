#!/usr/bin/env python3
"""Extract alpha-zero references from the pinned compressed boundary record.

Stdlib-only saved-data projection. No root, analytic primitive, interval
provider or source evaluator is imported or called. Per-node boxes retain
their original external-parameter association. Individual height extrema
extend harmonically; this extraction asserts no interior joint correlation.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import gzip
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-second-selected-first-three-external-boundary-attempt01.json.gz'
AUDIT = 'repro/results/research-mixed-second-selected-first-three-external-boundary-saved-audit.json'
CHECKER = 'experiments/check_mixed_second_selected_first_three_external_boundary_record.py'
PINNED = {
    SOURCE: '9744bb69bd81745f856b0424f7df3448b39f5208eae929f709dc7a3d639af956',
    AUDIT: '88d8f8177a439f4268980e7467fffc576b558776c22f2a6067361d0ab8b6a047',
    CHECKER: '9e53d3b6f9278289b7b2ba3ab3107b584d25f498d6a61dc5108ebb6c754315db',
    'experiments/extract_mixed_second_selected_boundary_references.py':
        '1264b86d37f34719ff8e8363abd86723f8355dfa122f1277778d20c897abc0e4',
}
NAMES = ('e', 'xi', 'a', 'u', 'z', 'v', 'b')
SHAPES = ('e', 'a', 'u', 'z', 'v', 'b', 'c')
RESPONSE_DETAILS = (
    'pi', 'marginal_response_coefficients', 'pLprime', 'pRprime',
    'left_product', 'right_product', 'left_product_modulus', 'right_product_modulus',
)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(2**20), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def verify(bindings):
    for name, expected in bindings.items():
        path = Path(name)
        path = path if path.is_absolute() else ROOT/path
        if sha(path) != expected:
            raise ValueError('changed extraction input: '+name)


def merge(bindings, inputs):
    for name, digest in inputs.items():
        p = Path(name)
        name = str((p if p.is_absolute() else ROOT/p).relative_to(ROOT))
        if name in bindings and bindings[name] != digest:
            raise ValueError('conflicting extraction binding: '+name)
        bindings[name] = digest


def interval(record):
    if record.get('finite') is not True:
        raise ValueError('nonfinite saved enclosure')
    lo, hi = F(record['lower_rational']), F(record['upper_rational'])
    if lo > hi:
        raise ValueError('reversed saved interval')
    return lo, hi


def validate_complex_inventory(values, names):
    if set(values) != set(names):
        raise ValueError('wrong certified coordinate/derivative inventory')
    for value in values.values():
        interval(value['real'])
        interval(value['imag'])


def height_extrema(rows):
    """Extremal *enclosure endpoints*, not certified attained function values."""
    result = {}
    for name in ('v', 'b'):
        data = [(row['source_node_index'], *interval(row['coordinates'][name]['imag'])) for row in rows]
        if not data:
            raise ValueError('empty boundary height group')
        lo, hi = min(x[1] for x in data), max(x[2] for x in data)
        result['h_'+name] = {
            'lower_rational': str(lo), 'upper_rational': str(hi),
            'lower_decimal_display': float(lo), 'upper_decimal_display': float(hi),
            'lower_endpoint_source_nodes': [x[0] for x in data if x[1] == lo],
            'upper_endpoint_source_nodes': [x[0] for x in data if x[2] == hi],
        }
    return result


def main():
    if any(digest is None for digest in PINNED.values()):
        raise RuntimeError('extractor not frozen: completed source/audit identities are pending')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not (str(args.output).endswith('.json') or str(args.output).endswith('.json.gz')):
        raise ValueError('compact output must end in .json or .json.gz')
    bindings = dict(PINNED)
    verify(bindings)
    audit = json.loads((ROOT/AUDIT).read_text())
    if (audit['status'] != 'exact saved-data check passed' or audit['alpha'] != 0
            or audit['source'] != SOURCE or audit['source_sha256'] != PINNED[SOURCE]
            or audit['checker_sha256'] != PINNED[CHECKER]
            or audit['complete_chart_cases'] != 18):
        raise ValueError('unexpected source-audit association')
    with gzip.open(ROOT/SOURCE, 'rt', encoding='utf-8') as stream:
        data = json.load(stream)
    if (data['status'] != 'complete boundary coverage'
            or data['alpha'] != 0 or data['beta_cases'] != [0, 1]
            or not data['complete_boundary_coverage'] or not data['coverage_verified']
            or not data['uniform_central_gap_proved']
            or data['alpha_one_canonical_reference_data_used'] is not False
            or data['pending_frontier_next_is_first'] or data['unresolved_leaves']
            or data['changed_inputs'] or data['stop_signals_received']):
        raise ValueError('source record is not the completed audited cover')
    merge(bindings, data['input_sha256'])
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    verify(bindings)
    nodes = data['nodes']
    accepted, geometry, cases = [], [], defaultdict(list)
    seen_indices = set()
    for leaf in data['terminal_leaves']:
        i = leaf['node_index']
        if i in seen_indices:
            raise ValueError('duplicate source terminal node')
        seen_indices.add(i)
        node = nodes[i]
        if node['alpha'] != 0 or leaf['alpha'] != 0:
            raise ValueError('terminal belongs to the wrong first-flag family')
        for key in ('alpha', 'beta', 'chart', 'address'):
            if node[key] != leaf[key]:
                raise ValueError('source terminal association mismatch')
        if node['action'] != leaf['status']:
            raise ValueError('source action mismatch')
        source_hash = canonical_sha(node)
        terminal = {
            'source_node_index': i, 'source_node_canonical_sha256': source_hash,
            'alpha': 0, 'beta': node['beta'], 'chart': node['chart'], 'address': node['address'],
            'external_domain': node['chart'][:2], 'status': node['action'],
            'parameter_interval': node['parameter_interval'],
            'external_coordinate_box': node['external_coordinate_box'],
        }
        cases[(node['beta'], node['chart'])].append(node['address'])
        if node['action'] == 'excluded':
            terminal['source_exclusion'] = node['source_exclusion']
            geometry.append(terminal)
            continue
        if node['action'] == 'excluded by certified reference domain':
            terminal['certified_reference_exclusion'] = node['reference']
            geometry.append(terminal)
            continue
        if node['action'] != 'accepted boundary estimate':
            raise ValueError('unexpected terminal status')
        ref, response = node['reference'], node['response']
        rd = ref['details']
        if (ref['alpha'] != 0 or rd['alpha'] != 0 or response['alpha'] != 0
                or ref['beta'] != node['beta'] or rd['beta'] != node['beta']
                or response['beta'] != node['beta']
                or ref['status'] != 'enclosed' or response['status'] != 'enclosed'
                or not response['height_conditions_verified']
                or not response['common_prefix_product_verified']):
            raise ValueError('missing accepted reference/response certificate')
        coords, shapes = rd['actual_coordinate_enclosures'], rd['negative_shapes']
        deriv = rd['response_verification']['derivative_enclosures']
        validate_complex_inventory(coords, NAMES+('c',))
        validate_complex_inventory(shapes, SHAPES)
        validate_complex_inventory(deriv, NAMES)
        if response['details']['coordinates'] != coords or response['details']['qprime'] != deriv:
            raise ValueError('response uses a different reference or derivative box')
        lo, hi = interval(response['B'])
        if lo < 0 or hi != F(node['boundary_response_upper_rational']):
            raise ValueError('inconsistent saved response upper bound')
        row = {
            **terminal,
            'source_reference_certificate_canonical_sha256': canonical_sha(ref),
            'source_response_certificate_canonical_sha256': canonical_sha(response),
            'coordinates': coords, 'negative_shapes': shapes, 'derivatives': deriv,
            'reference_certificate_scope': rd['certificate_scope'],
            'precision_bits': rd['precision_bits'],
            'seed_role': rd['seed_role'],
            'seed_canonical_certification_required': rd['seed_canonical_certification_required'],
            'response': {
                'alpha': 0, 'beta': node['beta'],
                'status': response['status'], 'B': response['B'],
                'B_upper_rational': response['B_upper_rational'],
                'B_upper_components_rational': response['B_upper_components_rational'],
                'height_conditions_verified': response['height_conditions_verified'],
                'common_prefix_product_verified': response['common_prefix_product_verified'],
                'details': {key: response['details'][key] for key in RESPONSE_DETAILS},
            },
            'certified_central_gap_lower_rational': node['boundary_gap_lower_rational'],
        }
        row['compact_payload_canonical_sha256'] = canonical_sha(row)
        terminal['accepted_reference_index'] = len(accepted)
        accepted.append(row)
        geometry.append(terminal)
    if (len(accepted) != audit['accepted_leaves']
            or len(geometry) != audit['terminal_leaves']
            or len(nodes) != audit['visited_nodes']):
        raise ValueError('unexpected completed source counts')
    for status, expected_count in (
            ('excluded', audit['strict_geometry_exclusions']),
            ('excluded by certified reference domain', audit['certified_reference_exclusions'])):
        if sum(row['status'] == status for row in geometry) != expected_count:
            raise ValueError('source exclusion count mismatch')
    expected = {(case['beta'], case['chart']) for case in data['coverage']['cases']}
    if set(cases) != expected or len(cases) != 18:
        raise ValueError('incomplete typed chart inventory')
    for addresses in cases.values():
        ordered = sorted(addresses)
        if any(not isinstance(a, str) or set(a)-set('01') for a in ordered):
            raise ValueError('invalid chart address')
        if any(b.startswith(a) for a, b in zip(ordered, ordered[1:])):
            raise ValueError('overlapping chart terminal addresses')
        if sum((F(1, 2**len(a)) for a in ordered), F(0)) != 1:
            raise ValueError('incomplete chart parameter partition')
    grouped = {}
    for beta in (0, 1):
        for domain in ('k3', 'k4'):
            rows = [r for r in accepted if (r['beta'], r['external_domain']) == (beta, domain)]
            grouped[str(beta)+'_'+domain] = {'beta': beta, 'external_domain': domain,
                                            'accepted_reference_count': len(rows), **height_extrema(rows)}
    result = {
        'schema': 'mixed-second-selected-first-three-certified-boundary-references-v1',
        'status': 'compact projection of the completed audited boundary references',
        'alpha': 0, 'beta_cases': [0, 1], 'precision_bits': 256,
        'source': SOURCE, 'source_sha256': PINNED[SOURCE],
        'source_encoding': 'gzip-compressed complete JSON',
        'alpha_one_reference_data_used': False,
        'saved_data_audit': AUDIT, 'saved_data_audit_sha256': PINNED[AUDIT],
        'source_visited_nodes': len(nodes), 'accepted_reference_count': len(accepted),
        'terminal_geometry_count': len(geometry),
        'strict_geometry_exclusions': audit['strict_geometry_exclusions'],
        'certified_reference_exclusions': audit['certified_reference_exclusions'],
        'pending_frontier': [], 'unresolved_frontier': [],
        'coverage': data['coverage'], 'domain_summaries': data['domain_summaries'],
        'accepted_references': accepted, 'terminal_geometry': geometry,
        'height_extrema': {'global_accepted_boundary': height_extrema(accepted),
                          'by_beta_and_external_domain': grouped},
        'input_sha256': bindings,
        'source_root_primitive_or_interval_evaluations': 0,
        'scope': {
            'references_are_conditional_on_actual_external_points_in_their_saved_cell': True,
            'per_cell_enclosures_and_all_boundary_geometry_preserved': True,
            'individual_height_extrema_extend_harmonically_on_each_fixed_beta_K': True,
            'interior_joint_correlations_claimed': False,
            'new_half_row_or_full_source_sign_claimed': False,
            'finite_suffix_realization_claimed': False,
        },
    }
    verify(bindings)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    opener = (gzip.open(args.output, 'xt', compresslevel=1, encoding='utf-8')
              if str(args.output).endswith('.json.gz') else args.output.open('x'))
    with opener as stream:
        json.dump(result, stream, sort_keys=True, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'status': result['status'], 'accepted_references': len(accepted),
                      'terminal_geometry': len(geometry), 'input_bindings': len(bindings),
                      'height_extrema': result['height_extrema'],
                      'output_bytes': args.output.stat().st_size, 'output_sha256': sha(args.output)}))


if __name__ == '__main__':
    main()
