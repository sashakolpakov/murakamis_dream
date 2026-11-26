#!/usr/bin/env python3
"""Complete-boundary attempt using original residual-certified prefixes.

All 18 beta/chart cases retain their complete interval frontiers.  Only
proved exclusions and uniform whole-cell bounds close a leaf.  Global
boundary gaps and response maxima are combined only after coverage.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import signal
import time

from flint import ctx


ROOT = Path(__file__).resolve().parents[1]
SPEC = 'notes/research_mixed_second_selected_external_boundary_evaluation.md'
PROVIDERS = {
    'geometry': 'experiments/mixed_second_selected_external_boundary.py',
    'reference': 'experiments/mixed_second_selected_external_reference.py',
    'response': 'experiments/mixed_second_selected_external_response.py',
    'improved': 'experiments/evaluate_mixed_second_selected_curvature_budget.py',
    'old': 'experiments/diagnose_mixed_second_selected_central_budget.py',
}
PINNED = {
    'experiments/mixed_second_selected_external_boundary.py': '806a68a3007f5c977465e0ca70b4ace0bedff63dd74354eb0719bdfc52572223',
    'experiments/mixed_second_selected_external_reference.py': 'bf665fcaef589bb4370a172a3db6ea6e917a385cf6dd9daae84bc3d263b37dc4',
    'experiments/mixed_second_selected_external_response.py': '0fee9946e37db655214307e3466fb4fc499e87721e2e78e31f8dff425afccba4',
    'experiments/evaluate_mixed_second_selected_curvature_budget.py': '9adc88e0c1cdf912574c6dc767d4b31f5bd88ba398446f77a7510cc90982e228',
    'experiments/diagnose_mixed_second_selected_central_budget.py': 'fa99e0b8de2a9b2bb4bf999f6057024dcf4500c35b5173638961ad226251e9ce',
    'notes/research_mixed_second_selected_external_boundary_evaluation.md': '8c2655e902090540a2ff8e8724052b95fb22ad149393057ad8dded96995a0f05',
    'notes/research_mixed_second_selected_external_boundary_charts.md': 'afb4a56ad99c2100285e791e1a1fd8549b40bb40004cf4ddc1df1b5b7a5dacba',
    'notes/research_mixed_second_selected_external_reference_evaluation.md': '0b2e5a3cece17d5db4a1d35536fef33ff5239a218cb88fffe8338148009b1f83',
    'notes/research_mixed_second_selected_external_response.md': '7d03b0e23e7811732bbfeb16bc5b4e246ea9835132ccedf89c72e85b31a6b8b4',
    'notes/research_mixed_second_selected_curvature_evaluation.md': 'db6931fee465f99623b9f75838c3e0b7ea6dbb684544de8f3e821a2ef33cbe2e',
    'notes/research_mixed_stationary_reference_boundary_extension.md': '86ca000c2778c1908e4428224692f883742f432083728307bc9e6a415a45514f',
    'notes/research_mixed_prefix_residual_localization.md': '5590b49394d112be5f5d23e7f20c31225bce8f1c19e6d3fd1dc3aa1ce40f0434',
    'repro/results/research-mixed-second-selected-external-jacobian.json': 'f4b83b2d676b899eb5cbe1d32269e496d4ad3c8c8ea414d97c1c442712ccded4',
    'experiments/check_mixed_second_selected_external_jacobian.py': '5d8e9c47010fdef08aece8d595ccbcd21fbc91bc022b3f186f788bd913198d2e',
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
    if not PINNED or not set(PROVIDERS.values()).issubset(PINNED) or SPEC not in PINNED:
        raise RuntimeError('boundary driver has not yet been frozen for execution')
    bindings = dict(PINNED)
    verify(bindings)
    modules = {key: importlib.import_module(Path(name).stem) for key, name in PROVIDERS.items()}
    for key, name in PROVIDERS.items():
        if Path(modules[key].__file__).resolve() != (ROOT/name).resolve():
            raise ValueError('unexpected provider module: '+name)
    old_inputs, _ = modules['old'].verified_inputs()
    merge(bindings, old_inputs)
    # The reference module returns metadata and the prescribed exact seed
    # centers; initialization performs no numerical evaluation.
    initialization = modules['reference'].initialize()
    merge(bindings, initialization['bindings'])
    merge(bindings, modules['improved'].PINNED)
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
    queue = deque({**case, 'address': '', 'seed_centers': None}
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
        leaf = {'beta': node['beta'], 'chart': node['chart'],
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
            queue.append({'beta': node['beta'], 'chart': node['chart'],
                          'address': child, 'seed_centers': seed})

    while queue and len(nodes) < MAX_NODES:
        if stop_signals:
            reason = 'stop signal received'
            break
        if counts['reference_calls'] >= MAX_REFERENCES:
            reason = 'reference cap'
            break
        item = queue.popleft()
        node = {key: item[key] for key in ('beta', 'chart', 'address')}
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
            node['reference'] = {'status': ref['status'], 'details': ref['details'],
                                 'counts': ref.get('counts', {})}
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
            counts.update({'response_'+k: v for k, v in reply.get('counts', {}).items()})
            if (reply['status'] != 'enclosed'
                    or not reply.get('height_conditions_verified')
                    or not reply.get('common_prefix_product_verified')):
                divide(node, 'external response or height condition incomplete', next_seed)
                continue
            primitive = Primitive()
            evaluator = old.Evaluator(four, primitive)
            scalar = improved.evaluate_reference(evaluator, shapes, coordinates, item['beta'])
            node['scalar'] = scalar
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
            summaries.append({'beta': beta, 'domain': domain, 'accepted_cells': len(selected),
                'observed_boundary_gap_lower_rational': None if gamma is None else str(gamma),
                'observed_response_upper_rational': None if response_max is None else str(response_max),
                'disk_barrier_factor_rational': str(factor),
                'compensated_gap_rational': None if deficit is None else str(deficit),
                'valid_for_whole_domain': all_complete and deficit is not None and deficit > 0})
    result = {'status': reason, 'alpha': 1, 'beta_cases': [0, 1],
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
    with args.output.open('x') as stream:
        stream.write(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': reason, 'nodes': len(nodes), 'counts': dict(counts),
        'complete_boundary_coverage': all_complete,
        'uniform_central_gap_proved': result['uniform_central_gap_proved'],
        'output_sha256': sha(args.output)}), flush=True)


if __name__ == '__main__':
    main()
