#!/usr/bin/env python3
"""First-type-three complete-boundary attempt with original residual certificates.

All 18 beta/chart cases retain their complete interval frontiers.  Only
proved exclusions and uniform whole-cell bounds close a leaf.  Global
boundary gaps and response maxima are combined only after coverage.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction as F
import gzip
import hashlib
import importlib
import json
from pathlib import Path
import signal
import time

from flint import ctx


ROOT = Path(__file__).resolve().parents[1]
SPEC = 'notes/research_mixed_second_selected_first_three_external_boundary_evaluation.md'
ALPHA = 0
PROVIDERS = {
    'geometry': 'experiments/mixed_second_selected_external_boundary.py',
    'reference': 'experiments/mixed_second_selected_first_three_external_reference.py',
    'response': 'experiments/mixed_second_selected_first_three_external_response.py',
    'improved': 'experiments/evaluate_mixed_second_selected_curvature_budget.py',
    'old': 'experiments/diagnose_mixed_second_selected_central_budget.py',
}
PINNED = {
    'experiments/mixed_second_selected_external_boundary.py': '806a68a3007f5c977465e0ca70b4ace0bedff63dd74354eb0719bdfc52572223',
    'experiments/mixed_second_selected_first_three_external_reference.py': '695ae91ad46581c74419e5ade992d7a233112761b88643199c9690a12b3df1d3',
    'experiments/mixed_second_selected_first_three_external_response.py': '476be0189ffb5b887316d230b0b8362108b5f5d97ec59c77d8232b3d9696a312',
    'experiments/evaluate_mixed_second_selected_curvature_budget.py': '9adc88e0c1cdf912574c6dc767d4b31f5bd88ba398446f77a7510cc90982e228',
    'experiments/diagnose_mixed_second_selected_central_budget.py': 'fa99e0b8de2a9b2bb4bf999f6057024dcf4500c35b5173638961ad226251e9ce',
    'notes/research_mixed_second_selected_first_three_external_boundary_evaluation.md': '27a46e35949c4fb31b8b01b2f68a6a6e4c4b0fd33887302c115127249525d8a8',
    'notes/research_mixed_second_selected_external_boundary_charts.md': 'afb4a56ad99c2100285e791e1a1fd8549b40bb40004cf4ddc1df1b5b7a5dacba',
    'notes/research_mixed_second_selected_first_three_external_reference_evaluation.md': '564710c4b10719fb0e81312e94289242cdc3857273d9d83b3dd1c965b490394f',
    'notes/research_mixed_second_selected_first_three_external_response.md': 'c34b62481899d7d7d1eef8a385da228577097964bd048e5e69d0749105c72568',
    'notes/research_mixed_second_selected_first_three_extension.md': 'd488ff98e01cfd5cd077de664c7e3bee3bfeeb735009f8c78f7c0ac60c7ad0e2',
    'notes/research_mixed_second_selected_curvature_evaluation.md': 'db6931fee465f99623b9f75838c3e0b7ea6dbb684544de8f3e821a2ef33cbe2e',
    'notes/research_mixed_stationary_reference_boundary_extension.md': '86ca000c2778c1908e4428224692f883742f432083728307bc9e6a415a45514f',
    'notes/research_mixed_prefix_residual_localization.md': '5590b49394d112be5f5d23e7f20c31225bce8f1c19e6d3fd1dc3aa1ce40f0434',
    'experiments/certify_mixed_second_selected_external_boundary.py': 'b866529f1df827151e98d86a6238985c20e170afaae2a80cb3372fe13394b9b5',
    'notes/research_mixed_second_selected_external_boundary_evaluation.md': '8c2655e902090540a2ff8e8724052b95fb22ad149393057ad8dded96995a0f05',
    'experiments/check_mixed_second_selected_first_three_external_jacobian.py': '268b86f8088a24deea6591b2c9ab9ccb488c1f17ecab5accd8b1abb2ae875a9b',
    'repro/results/research-mixed-second-selected-first-three-external-jacobian.json': 'dcd9d7f17d2f36dcafbab661932a59951fa48269fd163fa797259f57b729c4df',
}
MAX_NODES, MAX_REFERENCES, MAX_DEPTH = 12000, 4000, 18
PRECISION = 256
PRE_SPLIT_WIDTH = F(1, 200)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        if sha(ROOT/name) != digest:
            raise ValueError('changed boundary-certificate input: '+name)


def merge(bindings, source):
    for name, digest in source.items():
        path = Path(name)
        relative = str((path if path.is_absolute() else ROOT/path).relative_to(ROOT))
        if relative in bindings and bindings[relative] != digest:
            raise ValueError('conflicting input: '+relative)
        bindings[relative] = digest


def load_inputs():
    if (not PINNED or not set(PROVIDERS.values()).issubset(PINNED) or SPEC not in PINNED
            or any(digest.startswith('PENDING') for digest in PINNED.values())):
        raise RuntimeError('boundary driver has not yet been frozen for execution')
    bindings = dict(PINNED)
    verify(bindings)
    modules = {key: importlib.import_module(Path(name).stem) for key, name in PROVIDERS.items()}
    for key, name in PROVIDERS.items():
        if Path(modules[key].__file__).resolve() != (ROOT/name).resolve():
            raise ValueError('unexpected provider module: '+name)
    old_inputs, _ = modules['old'].verified_inputs()
    merge(bindings, old_inputs)
    merge(bindings, modules['reference'].PINNED)
    merge(bindings, modules['response'].PINNED)
    merge(bindings, modules['improved'].PINNED)
    verify(bindings)
    # These exact fixed seeds are proposals only, not canonical records.
    initialization = modules['reference'].initialize()
    if (initialization.get('alpha') != ALPHA
            or initialization.get('precision_bits') != PRECISION
            or initialization.get('seed_canonical_certification_required') is not False):
        raise ValueError('wrong first-type-three reference initialization')
    merge(bindings, initialization['bindings'])
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    verify(bindings)
    four = importlib.import_module('diagnose_mixed_four_four_half_row_budget')
    return modules, four, initialization, bindings


def interval(record):
    if record.get('finite') is not True:
        raise ValueError('nonfinite serialized scalar interval')
    lo, hi = F(record['lower_rational']), F(record['upper_rational'])
    if lo > hi:
        raise ValueError('reversed scalar interval')
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not str(args.output).endswith('.json.gz'):
        raise ValueError('first-type-three boundary output must end in .json.gz')
    if args.output.exists():
        raise FileExistsError(args.output)
    modules, four, initialization, bindings = load_inputs()
    geometry, reference, response, improved, old = (modules[k] for k in
        ('geometry', 'reference', 'response', 'improved', 'old'))
    ctx.prec = PRECISION
    def forbidden(*args, **kwargs):
        raise RuntimeError('old reference/source/transport callback forbidden')
    for provider in (old, four, four.frozen, four.maps_four, four.BASE):
        provider.inspect = provider.main = provider.reference = forbidden
    old.Evaluator.inspect = old.Evaluator.reference = old.Evaluator.transfer = forbidden
    four.reference_four = forbidden
    Primitive = old.make_primitive_class(four)
    queue = deque({**case, 'alpha': ALPHA, 'address': '', 'seed_centers': None}
                  for case in geometry.case_list())
    nodes, leaves, unresolved = [], [], []
    counts = Counter()
    reason = 'node cap'
    started = time.monotonic()
    stop_signals = []
    def request_stop(signum, frame):
        stop_signals.append(signum)
    signal.signal(signal.SIGINT, request_stop)
    signal.signal(signal.SIGTERM, request_stop)

    def close(node, status):
        node['action'] = status
        leaf = {'alpha': ALPHA, 'beta': node['beta'], 'chart': node['chart'],
                'address': node['address'], 'node_index': len(nodes)-1, 'status': status}
        (unresolved if status.startswith('unresolved') else leaves).append(leaf)

    def divide(node, why, seed):
        if len(node['address']) >= MAX_DEPTH:
            node['unresolved_reason'] = why
            close(node, 'unresolved depth limit')
            return
        node['action'], node['split_reason'] = 'split', why
        node['children'] = [node['address']+'0', node['address']+'1']
        for child in node['children']:
            queue.append({'alpha': ALPHA, 'beta': node['beta'], 'chart': node['chart'],
                          'address': child, 'seed_centers': seed})

    while queue and len(nodes) < MAX_NODES:
        if stop_signals:
            reason = 'stop signal received'
            break
        if counts['reference_calls'] >= MAX_REFERENCES:
            reason = 'reference cap'
            break
        item = queue.popleft()
        node = {key: item[key] for key in ('alpha', 'beta', 'chart', 'address')}
        nodes.append(node)
        try:
            parameter = geometry.parameter_interval(item['address'])
            node['parameter_interval'] = list(map(str, parameter))
            cbox = geometry.paramimage(item['chart'], parameter)
            node['external_coordinate_box'] = list(map(str, cbox))
            exclusion = geometry.exactsourceexclusionwitness(item['chart'], parameter)
            if exclusion is not None:
                node['source_exclusion'] = exclusion
                counts['geometry_exclusions'] += 1
                close(node, 'excluded')
                continue
            if max(cbox[1]-cbox[0], cbox[3]-cbox[2]) > PRE_SPLIT_WIDTH:
                counts['geometry_presplits'] += 1
                divide(node, 'external box exceeds prescribed proposal width', item['seed_centers'])
                continue
            middle = (parameter[0]+parameter[1])/2
            midpoint_box = geometry.paramimage(item['chart'], (middle, middle))
            if midpoint_box[0] != midpoint_box[1] or midpoint_box[2] != midpoint_box[3]:
                raise ValueError('chart midpoint is not exact')
            cmid = (midpoint_box[0], midpoint_box[2])
            counts['reference_calls'] += 1
            ref = reference.evaluate(cbox, cmid, item['beta'], item['seed_centers'])
            node['reference'] = {'alpha': ref.get('alpha'), 'beta': ref.get('beta'),
                                 'status': ref['status'], 'details': ref['details'],
                                 'counts': ref.get('counts', {})}
            if ref.get('alpha') != ALPHA or ref['details'].get('alpha') != ALPHA:
                raise ValueError('reference belongs to the wrong first-flag family')
            counts.update({'reference_'+k: v for k, v in ref.get('counts', {}).items()})
            next_seed = None
            if ref['status'] == 'error' or ref.get('unexpected_error'):
                raise RuntimeError('reference provider error: '+ref.get('reason', 'unknown'))
            if ref['status'] == 'excluded':
                counts['certified_reference_exclusions'] += 1
                close(node, 'excluded by certified reference domain')
                continue
            if ref['status'] != 'enclosed':
                divide(node, 'original reference enclosure incomplete', next_seed)
                continue
            coordinates, shapes = ref['coordinates'], ref['shapes']
            counts['response_calls'] += 1
            reply = response.evaluate(coordinates, ref['derivatives'], item['beta'])
            node['response'] = reply
            if reply.get('alpha') != ALPHA:
                raise ValueError('response belongs to the wrong first-flag family')
            counts.update({'response_'+k: v for k, v in reply.get('counts', {}).items()})
            if (reply['status'] != 'enclosed'
                    or not reply.get('height_conditions_verified')
                    or not reply.get('common_prefix_product_verified')):
                divide(node, 'external response or height condition incomplete', next_seed)
                continue
            primitive = Primitive()
            evaluator = old.Evaluator(four, primitive)
            scalar = improved.evaluate_reference(evaluator, shapes, coordinates, item['beta'])
            if 'alpha' in scalar and scalar['alpha'] != ALPHA:
                raise ValueError('scalar metadata belongs to the wrong first-flag family')
            # The frozen helpers contain no alpha-dependent arithmetic.
            # Add caller provenance without changing any frozen branch values.
            scalar = {**scalar, 'alpha': ALPHA, 'alpha_provenance_supplied_by_driver': True}
            node['scalar'] = scalar
            if ctx.prec != PRECISION:
                raise ValueError('outward precision changed during a cell')
            scalar_counts = evaluator.counts+primitive.counts
            node['scalar_counts'] = dict(scalar_counts)
            counts.update({'scalar_'+k: v for k, v in scalar_counts.items()})
            if (scalar_counts['directional_reference_attempts'] != 1
                    or scalar_counts['node_conjugates'] > 3
                    or scalar_counts['directional_branch_attempts'] > 2
                    or scalar_counts['centered_primitive_calls'] > 12):
                raise ValueError('per-cell scalar callback cap exceeded')
            if not scalar.get('fully_evaluated_pair'):
                divide(node, 'scalar arithmetic incomplete', next_seed)
                continue
            branches = scalar['details']['branches']
            upper = max(interval(branches[label]['budget'])[1]
                        for label in ('forced', 'factorial'))
            original = scalar['details']['frozen_result']['details']['branches']
            width = max(interval(original[label]['budget'])[1]-interval(original[label]['budget'])[0]
                        for label in ('forced', 'factorial'))
            b_lo, b_hi = interval(reply['B'])
            gap = -upper
            phase_resolved = gap > 0 and (gap >= F(1, 200) or width <= gap/2)
            adequate = phase_resolved and b_hi-b_lo <= max(F(1, 100), b_hi/4)
            node['resolution_test'] = {
                'weakest_branch_upper_rational': str(upper),
                'largest_frozen_budget_width_rational': str(width),
                'phase_resolution_by_gap_or_width': phase_resolved,
                'response_width_rational': str(b_hi-b_lo),
                'response_width_limit_rational': str(max(F(1, 100), b_hi/4)),
                'passed': adequate,
            }
            if adequate:
                node['boundary_gap_lower_rational'] = str(gap)
                node['boundary_response_upper_rational'] = str(b_hi)
                close(node, 'accepted boundary estimate')
                counts['accepted'] += 1
            else:
                divide(node, 'finite estimates require finer parameter enclosure', next_seed)
        except Exception as error:
            node['unexpected_error'] = repr(error)
            close(node, 'unresolved unexpected error')
            reason = 'unexpected error'
            break
        finally:
            if len(nodes) % 20 == 0:
                print(json.dumps({'nodes': len(nodes), 'references': counts['reference_calls'],
                    'accepted': counts['accepted'], 'excluded': counts['geometry_exclusions'],
                    'pending': len(queue), 'unresolved': len(unresolved),
                    'elapsed_seconds': time.monotonic()-started}), flush=True)
    if not queue and reason == 'node cap':
        reason = 'frontier exhausted with unresolved leaves' if unresolved else 'complete boundary coverage'
    frontiers = {(case['beta'], case['chart']): [] for case in geometry.case_list()}
    for leaf in leaves+unresolved+list(queue):
        frontiers[(leaf['beta'], leaf['chart'])].append(leaf['address'])
    try:
        coverage = geometry.validate_coverage(frontiers)
        if len(nodes)+len(queue) != 2*coverage['total_frontier_leaves']-18:
            raise ValueError('visited/pending forest node count mismatch')
        coverage_verified = True
    except Exception as error:
        coverage = {'validation_error': repr(error)}
        coverage_verified = False
        reason = 'coverage validation failure'
    changed_inputs = [name for name, digest in bindings.items()
                      if sha(ROOT/name) != digest]
    if changed_inputs:
        reason = 'input changed during run'
    all_complete = coverage_verified and not changed_inputs and not queue and not unresolved
    summaries = []
    for beta in (0, 1):
        for domain in ('k3', 'k4'):
            selected = [node for node in nodes if node['beta'] == beta
                        and node['chart'].startswith(domain+'_')
                        and node.get('action') == 'accepted boundary estimate']
            gamma = min((F(node['boundary_gap_lower_rational']) for node in selected), default=None)
            response_max = max((F(node['boundary_response_upper_rational']) for node in selected), default=None)
            factor = geometry.DOMAINS[domain].radius**2/2
            deficit = None if not all_complete or gamma is None else gamma-factor*response_max
            summaries.append({'alpha': ALPHA, 'beta': beta, 'domain': domain, 'accepted_cells': len(selected),
                'observed_boundary_gap_lower_rational': None if gamma is None else str(gamma),
                'observed_response_upper_rational': None if response_max is None else str(response_max),
                'disk_barrier_factor_rational': str(factor),
                'compensated_gap_rational': None if deficit is None else str(deficit),
                'valid_for_whole_domain': all_complete and deficit is not None and deficit > 0})
    result = {'status': reason, 'alpha': ALPHA, 'beta_cases': [0, 1],
        'seed_role': 'fixed rational proposals only; no canonical-seed proof premise',
        'alpha_one_canonical_reference_data_used': False,
        'boundary_case_count': 18, 'nodes': nodes, 'terminal_leaves': leaves,
        'unresolved_leaves': unresolved, 'pending_frontier_next_is_first': list(queue),
        'coverage': coverage, 'coverage_verified': coverage_verified,
        'changed_inputs': changed_inputs, 'complete_boundary_coverage': all_complete,
        'domain_summaries': summaries,
        'uniform_central_gap_proved': all_complete and all(row['valid_for_whole_domain'] for row in summaries),
        'half_row_bound_claimed': False, 'full_source_theorem_claimed': False,
        'global_filling_volume_theorem_claimed': False,
        'maximum_nodes': MAX_NODES, 'maximum_references': MAX_REFERENCES,
        'maximum_depth': MAX_DEPTH, 'precision_bits': PRECISION,
        'proposal_width_limit_rational': str(PRE_SPLIT_WIDTH),
        'counts': dict(counts), 'input_sha256': bindings,
        'stop_signals_received': stop_signals,
        'elapsed_seconds': time.monotonic()-started}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(args.output, 'xt', compresslevel=1, encoding='utf-8') as stream:
        json.dump(result, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'status': reason, 'nodes': len(nodes), 'counts': dict(counts),
        'complete_boundary_coverage': all_complete,
        'uniform_central_gap_proved': result['uniform_central_gap_proved'],
        'output_sha256': sha(args.output)}), flush=True)


if __name__ == '__main__':
    main()
