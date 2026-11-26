#!/usr/bin/env python3
"""One bounded, fully archived third-selection product-boundary pass.

Only a complete accepted/excluded forest can prove the parameter-domain
comparison.  Caps, failed enclosures, and unfinished cells are retained.
No precision increase, alternative seed, or automatic retry is permitted.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

from flint import ctx

import mixed_second_selected_external_boundary as geometry
import mixed_third_selected_external_reference as provider
import evaluate_mixed_third_selected_tangent as evaluator


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'repro/results/research-mixed-third-selected-product-boundary-attempt01.json.gz'
ANCHOR_FILE = 'repro/results/research-mixed-third-selected-eight-center-diagnostic.json'
PROTOCOL = 'notes/research_mixed_third_selected_center_comparison.md'
PINNED = {
    ANCHOR_FILE: '69ea662427dd1499aea1451df25da519d0249dc3604b55afd0bdd55c7da4812a',
    PROTOCOL: '2e5305f3e37b3b50cfc5fdfae7d33b3a4b6cf7bf455381a635029c7ff7f5aff4',
    'experiments/check_mixed_third_selected_eight_center_record.py':
        '347d1015bce33c1761609467ce9e96e331fb5f81107ba37dc62933230ee48998',
    'repro/results/research-mixed-third-selected-eight-center-saved-audit.json':
        '14e3f08a8113a501b3073298fff532c9f9c4c4b2552c84f6d8aaecc6d43b9d14',
}
LIMITS = {
    'visited_cells': 4000,
    'provider_invocations': 2000,
    'reference_proposals': 2000,
    'combined_binary_depth': 16,
    'newton_steps_per_proposal': 20,
    'target_iterations_per_proposal': 200,
    'precision_bits': 256,
    'target_proposals_per_label': 1,
}
DELTA = F(1, 2000)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(2**20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        path = Path(name)
        if sha(path if path.is_absolute() else ROOT / path) != digest:
            raise ValueError('changed input: ' + name)


def bind(bindings, extra):
    for name, digest in extra.items():
        if name in bindings and bindings[name] != digest:
            raise ValueError('inconsistent input binding: ' + name)
        bindings[name] = digest


def cases():
    charts = geometry.chartlist()
    keys = sorted((beta, a.name, c.name)
                  for beta in (0, 1) for a in charts for c in charts)
    return [dict(case_index=i, beta=beta,
                 alpha=int(a[1])-3, sigma=int(c[1])-3,
                 chart_a=a, chart_c=c)
            for i, (beta, a, c) in enumerate(keys)]


def product_parameter(address):
    sides = [(-F(1), F(1)), (-F(1), F(1))]
    for digit in address:
        if digit not in '01':
            raise ValueError('invalid product address')
        axis = 0 if sides[0][1]-sides[0][0] >= sides[1][1]-sides[1][0] else 1
        sides[axis] = geometry.split(sides[axis])[int(digit)]
    return sides


def cell(case, address):
    aa, cc = product_parameter(address)
    return dict(case, address=address,
                interval_a=list(map(str, aa)), interval_c=list(map(str, cc)),
                abox=list(map(str, geometry.paramimage(case['chart_a'], aa))),
                cbox=list(map(str, geometry.paramimage(case['chart_c'], cc))))


def exclusion(row):
    for factor in ('a', 'c'):
        witness = geometry.exactsourceexclusionwitness(
            row['chart_' + factor], row['interval_' + factor])
        if witness is not None:
            return {'factor': factor, 'witness': witness}
    return None


def labels(beta):
    return tuple(itertools.product(('main', 'left', 'half'),
                                   ('main', 'half') if beta == 0 else ('main',),
                                   (0, 1)))


def freeze_inputs():
    bindings = dict(PINNED)
    verify(bindings)
    original = json.loads((ROOT / ANCHOR_FILE).read_text())
    bind(bindings, original['input_sha256'])
    pinfo, einfo = provider.initialize(), evaluator.initialize()
    bind(bindings, pinfo['bindings'])
    bind(bindings, einfo['bindings'])
    for path in (Path(__file__).resolve(), Path(geometry.__file__).resolve()):
        bind(bindings, {str(path.relative_to(ROOT)): sha(path)})
    anchors = {}
    inventory = []
    for index, anchor in enumerate(original['references']):
        key = (anchor['alpha'], anchor['beta'], anchor['external_right_type_flag'])
        if key in anchors:
            raise ValueError('duplicate anchor')
        anchors[key] = anchor
        inventory.append({
            'alpha': key[0], 'beta': key[1], 'sigma': key[2],
            'source_reference_index': index,
            'reference_canonical_sha256': canonical_hash(anchor),
            'coordinate_canonical_sha256': canonical_hash(anchor['reference_certificate']['coordinates']),
        })
    if set(anchors) != set(itertools.product((0, 1), repeat=3)):
        raise ValueError('incomplete anchor inventory')
    verify(bindings)
    return bindings, anchors, inventory, pinfo, einfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('refusing to overwrite a completed or partial record')
    ctx.prec = LIMITS['precision_bits']
    bindings, anchors, anchor_inventory, pinfo, einfo = freeze_inputs()
    inventory = cases()
    pending = [cell(case, '') for case in reversed(inventory)]
    nodes = []
    counts = Counter()
    provider_counts = Counter()
    stop_reason = None
    started = time.monotonic()
    record = {
        'status': 'bounded pass in progress', 'stop_reason': None,
        'limits': dict(LIMITS), 'precision_bits': ctx.prec, 'delta': str(DELTA),
        'input_sha256': bindings, 'cases': inventory, 'nodes': nodes,
        'pending': [], 'counts': {}, 'complete_partition': False,
        'full_domain_proved': False,
        'anchor_source': ANCHOR_FILE, 'anchor_inventory': anchor_inventory,
        'provider_initialization': pinfo, 'evaluator_initialization': einfo,
        'scope': 'third position, second position unselected; m>=5; full parameter comparison only if every chart is resolved',
        'parameter_clipping': 'none before residual certification; strict whole-factor geometric exclusions only',
        'ordering': 'lexicographic cases, depth first, longer normalized parameter side, a on ties',
    }
    active = None
    try:
        while pending:
            if len(nodes) >= LIMITS['visited_cells']:
                stop_reason = 'visited-cell limit reached'
                break
            # Keep an unevaluated nonexcluded cell on the frontier at the cap.
            if counts['provider_invocations'] >= LIMITS['provider_invocations']:
                stop_reason = 'provider-invocation limit reached'
                break
            active = pending.pop()
            active.update(node_index=len(nodes), profiles=[], status='unresolved')
            nodes.append(active)
            counts['visited_cells'] += 1
            witness = exclusion(active)
            if witness is not None:
                active.update(status='excluded', geometry_witness=witness)
            else:
                counts['provider_invocations'] += 1
                reference = provider.evaluate(active['alpha'], active['beta'],
                                              active['abox'], active['cbox'])
                active['reference'] = reference
                provider_counts.update(reference.get('counts', {}))
                if reference['status'] == 'error':
                    active.update(status='error', reason=reference.get('reason'))
                    stop_reason = 'unexpected reference error'
                    break
                if reference['status'] == 'enclosed':
                    counts['enclosed_references'] += 1
                    key = (active['alpha'], active['beta'], active['sigma'])
                    anchor = anchors[key]
                    active['anchor_reference_canonical_sha256'] = canonical_hash(anchor)
                    active['reference_coordinate_canonical_sha256'] = canonical_hash(reference['coordinates'])
                    for left, right, nu in labels(active['beta']):
                        profile = dict(incoming_profile=left, outgoing_profile=right, nu=nu)
                        active['profiles'].append(profile)
                        counts['target_proposals'] += 1
                        try:
                            trial, proposal = evaluator.propose_trial(
                                reference, active['alpha'], active['beta'], left, right, nu)
                        except evaluator.Inconclusive as error:
                            profile.update(status='inconclusive', reason=str(error),
                                           proposal_failed=True)
                            continue
                        profile.update(trial=list(map(str, trial)), proposal=proposal)
                        counts['profile_interval_bounds'] += 1
                        profile.update(evaluator.evaluate(
                            reference, anchor, active['alpha'], active['beta'],
                            left, right, nu, trial))
                        if profile.get('status') == 'error':
                            active.update(status='error', reason=profile.get('reason'))
                            stop_reason = 'unexpected target error'
                            break
                    if stop_reason is not None:
                        break
                    bounds = [F(p['compensated_upper_rational']) for p in active['profiles']
                              if 'compensated_upper_rational' in p]
                    if (len(bounds) == len(labels(active['beta']))
                            and all(p.get('status', 'enclosed') == 'enclosed' for p in active['profiles'])):
                        active['maximum_compensated_upper_rational'] = str(max(bounds))
                        if max(bounds) < -DELTA:
                            active['status'] = 'accepted'
                elif reference['status'] != 'inconclusive':
                    raise ValueError('unknown reference status')
                if active['status'] == 'unresolved':
                    if len(active['address']) >= LIMITS['combined_binary_depth']:
                        stop_reason = 'first unresolved depth-limit cell'
                        break
                    active['status'] = 'split'
                    aa, cc = product_parameter(active['address'])
                    active['split_axis'] = 'a' if aa[1]-aa[0] >= cc[1]-cc[0] else 'c'
                    case = inventory[active['case_index']]
                    pending.append(cell(case, active['address']+'1'))
                    pending.append(cell(case, active['address']+'0'))
            if len(nodes) % 20 == 0:
                print(json.dumps({'visited': len(nodes), 'pending': len(pending),
                                  'node_status': active['status'],
                                  'provider_invocations': counts['provider_invocations'],
                                  'profile_bounds': counts['profile_interval_bounds'],
                                  'elapsed_seconds': round(time.monotonic()-started, 1)}), flush=True)
            active = None
    except KeyboardInterrupt:
        stop_reason = 'interrupted; complete untouched frontier retained'
        if active is not None and active['status'] not in ('accepted', 'excluded', 'split'):
            active.update(status='unresolved', reason='interrupted during evaluation')
    except Exception as error:
        stop_reason = 'unexpected driver or evaluator exception'
        record['unexpected_error'] = repr(error)
        if active is not None:
            active.update(status='error', reason=repr(error))

    record['pending'] = list(reversed(pending))
    counts.update({'reference_proposals': provider_counts['proposal_calls']})
    for key, count in Counter(n['status'] for n in nodes).items():
        counts[key] = count
    counts['pending'] = len(pending)
    record['counts'] = dict(counts)
    record['provider_counts'] = dict(provider_counts)
    record['elapsed_seconds'] = time.monotonic()-started
    record['stop_reason'] = stop_reason
    frontiers = defaultdict(list)
    for row in nodes:
        if row['status'] != 'split':
            frontiers[row['case_index']].append(row['address'])
    for row in pending:
        frontiers[row['case_index']].append(row['address'])
    try:
        record['partition_summary'] = [
            dict(case_index=i, **geometry.validate_partition(frontiers[i]))
            for i in range(len(inventory))]
        record['complete_partition'] = True
    except Exception as error:
        record['partition_error'] = repr(error)
    try:
        verify(bindings)
        record['input_bindings_unchanged'] = True
    except Exception as error:
        record['input_bindings_unchanged'] = False
        record['input_binding_error'] = repr(error)
    record['full_domain_proved'] = bool(
        record['complete_partition'] and record['input_bindings_unchanged']
        and not pending and stop_reason is None
        and not counts['unresolved'] and not counts['error']
        and counts['visited_cells'] <= LIMITS['visited_cells']
        and counts['provider_invocations'] <= LIMITS['provider_invocations']
        and counts['reference_proposals'] <= LIMITS['reference_proposals'])
    record['status'] = ('complete domain comparison' if record['full_domain_proved']
                        else 'bounded pass stopped without a full-domain conclusion')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('xb') as stream:
        with gzip.GzipFile(fileobj=stream, mode='wb', mtime=0) as compressed:
            compressed.write(json.dumps(record, sort_keys=True, separators=(',', ':')).encode())
            compressed.write(b'\n')
    print(json.dumps({'status': record['status'], 'stop_reason': stop_reason,
                      'counts': record['counts'],
                      'complete_partition': record['complete_partition'],
                      'output_sha256': sha(args.output)}), flush=True)


if __name__ == '__main__':
    main()
