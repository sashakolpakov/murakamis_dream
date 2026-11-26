#!/usr/bin/env python3
"""Evaluate the two half-row budgets on the complete saved beta-zero boundary."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path
import signal
import time

from flint import acb, ctx

ROOT = Path(__file__).resolve().parents[1]
BANK = 'repro/results/research-mixed-second-selected-boundary-reference-bank.json'
SPEC = 'notes/research_mixed_second_selected_half_row_boundary_evaluation.md'
EVALUATOR = 'experiments/evaluate_mixed_second_selected_half_row_budget.py'
PINNED = {
    BANK: '3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb',
    SPEC: '82c82be3e35ce3fa53e08b95ad94f15e72806367117d122ff5de50684f0aa7b1',
    EVALUATOR: 'ad5130b15bd3b403d4fdcc59ab97a73e536bdbff8e8e44be67d742cbe403f639',
    'notes/research_mixed_second_selected_half_row_evaluation.md':
        '4ed8584c2ee32c2f31d24a3e8b1dca73fc6edaff0fa2e078bfda9af6f6ca134f',
    'notes/research_mixed_second_selected_half_row_boundary_extension.md':
        '0aa085f65489e024fa9e31040a507db8b681fd409de349a59db91c39929c0152',
    'notes/research_mixed_second_selected_central_completion.md':
        'ad694fed3707db09dfe1d926affdabf7557d519f142d975e9cc02fe54bf3ce00',
}
PRECISION = 256


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(2**20), b''):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def verify(bindings):
    for name, digest in bindings.items():
        p = Path(name)
        if sha(p if p.is_absolute() else ROOT/p) != digest:
            raise ValueError('changed half-row boundary input: '+name)


def merge(bindings, source):
    for name, digest in source.items():
        p = Path(name)
        relative = str((p if p.is_absolute() else ROOT/p).relative_to(ROOT))
        if relative in bindings and bindings[relative] != digest:
            raise ValueError('conflicting input binding: '+relative)
        bindings[relative] = digest


def interval(record):
    if record.get('finite') is not True:
        raise ValueError('nonfinite saved scalar')
    lo, hi = F(record['lower_rational']), F(record['upper_rational'])
    if lo > hi:
        raise ValueError('reversed saved scalar')
    return lo, hi


def complex_box(record, frozen):
    return acb(frozen.interval(*interval(record['real'])),
               frozen.interval(*interval(record['imag'])))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not {BANK, SPEC, EVALUATOR}.issubset(PINNED):
        raise RuntimeError('half-row attempt has not been frozen for execution')
    bindings = dict(PINNED)
    verify(bindings)
    bank = json.loads((ROOT/BANK).read_text())
    if (bank['schema'] != 'mixed-second-selected-certified-boundary-references-v1'
            or bank['alpha'] != 1 or bank['precision_bits'] != PRECISION
            or bank['pending_frontier'] or bank['unresolved_frontier']):
        raise ValueError('unexpected reference bank')
    merge(bindings, bank['input_sha256'])
    verify(bindings)
    evaluator = importlib.import_module(Path(EVALUATOR).stem)
    if Path(evaluator.__file__).resolve() != (ROOT/EVALUATOR).resolve():
        raise ValueError('wrong half-row evaluator module')
    initialization = evaluator.initialize()
    merge(bindings, initialization['bindings'])
    old = importlib.import_module('diagnose_mixed_second_selected_central_budget')
    old_inputs, _ = old.verified_inputs()
    merge(bindings, old_inputs)
    four = importlib.import_module('diagnose_mixed_four_four_half_row_budget')
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    verify(bindings)

    selected = [(i, r) for i, r in enumerate(bank['accepted_references']) if r['beta'] == 0]
    geometry = [g for g in bank['terminal_geometry'] if g['beta'] == 0]
    if len(selected) != 785 or len(geometry) != 843:
        raise ValueError('incomplete beta-zero reference inventory')
    if (sum(g['status'] == 'excluded' for g in geometry) != 58
            or sum(r['external_domain'] == 'k3' for _, r in selected) != 388
            or sum(r['external_domain'] == 'k4' for _, r in selected) != 397):
        raise ValueError('unexpected typed reference or exclusion counts')
    addresses = defaultdict(list)
    associations = {r['source_node_index']: (i, r) for i, r in selected}
    if len(associations) != len(selected):
        raise ValueError('duplicate reference source node')
    for i, r in selected:
        payload = dict(r)
        expected = payload.pop('compact_payload_canonical_sha256')
        if canonical_sha(payload) != expected:
            raise ValueError('changed compact reference payload')
        if (not r['response']['height_conditions_verified']
                or not r['response']['common_prefix_product_verified']):
            raise ValueError('missing inherited height or common-product bound')
    for g in geometry:
        addresses[g['chart']].append(g['address'])
        if g['status'] == 'accepted boundary estimate':
            i, r = associations[g['source_node_index']]
            if g['accepted_reference_index'] != i:
                raise ValueError('wrong reference-bank index')
            for key in ('chart', 'address', 'parameter_interval', 'external_coordinate_box',
                        'source_node_canonical_sha256'):
                if g[key] != r[key]:
                    raise ValueError('wrong terminal/reference association')
        elif g['status'] != 'excluded':
            raise ValueError('unresolved inherited geometry')
    expected_charts = {c['chart'] for c in bank['coverage']['cases'] if c['beta'] == 0}
    if set(addresses) != expected_charts or len(expected_charts) != 9:
        raise ValueError('incomplete boundary-chart inventory')
    for chart, aa in addresses.items():
        ss = sorted(aa)
        if (len(set(ss)) != len(ss)
                or any(set(a)-{'0', '1'} for a in ss)
                or any(b.startswith(a) for a, b in zip(ss, ss[1:]))
                or sum((F(1, 2**len(a)) for a in ss), F()) != 1):
            raise ValueError('invalid complete boundary partition: '+chart)

    ctx.prec = PRECISION
    def forbidden(*args, **kwargs):
        raise RuntimeError('source, reference or transport evaluation forbidden')
    for module in (old, four, four.frozen, four.maps_four, four.BASE):
        module.inspect = module.main = module.reference = forbidden
    old.Evaluator.inspect = old.Evaluator.reference = old.Evaluator.transfer = forbidden
    four.reference_four = forbidden
    Primitive = old.make_primitive_class(four)
    stopped = []
    def stop(signum, frame):
        stopped.append(signum)
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    started = time.monotonic()
    rows, counts, errors = [], Counter(), []
    reason = 'complete saved-reference pass'
    for bank_index, reference in selected:
        if stopped:
            reason = 'stop signal received'
            break
        row = {key: reference[key] for key in
               ('source_node_index', 'chart', 'address', 'external_domain',
                'compact_payload_canonical_sha256')}
        row['bank_reference_index'] = bank_index
        row['boundary_response_upper_rational'] = reference['response']['B_upper_rational']
        rows.append(row)
        try:
            coordinates = {k: complex_box(v, four.frozen) for k, v in reference['coordinates'].items()}
            shapes = {k: complex_box(v, four.frozen) for k, v in reference['negative_shapes'].items()}
            primitive = Primitive()
            e = old.Evaluator(four, primitive)
            result = evaluator.evaluate_reference(e, shapes, coordinates, 0)
            row['scalar'] = result
            calls = e.counts + primitive.counts
            row['counts'] = dict(calls)
            counts.update(calls)
            if (calls['node_conjugates'] > 1 or calls['centered_primitive_calls'] > 11
                    or ctx.prec != PRECISION):
                raise ValueError('per-reference call or precision cap violated')
            if result.get('unexpected_error') or result.get('status') == 'error':
                raise RuntimeError('unexpected evaluator error')
            if result.get('fully_evaluated_pair'):
                branches = result['details']['branches']
                if set(branches) != {'forced', 'factorial'}:
                    raise ValueError('incomplete Fourier-alternative inventory')
                upper = max(interval(branches[name]['budget'])[1] for name in branches)
                row['boundary_gap_lower_rational'] = str(-upper)
                row['status'] = 'finite bound'
            else:
                row['status'] = 'unresolved arithmetic'
        except Exception as error:
            row['status'] = 'unexpected error'
            row['error'] = repr(error)
            errors.append({'source_node_index': reference['source_node_index'], 'error': repr(error)})
            reason = 'unexpected error'
            break
        finally:
            if len(rows) % 20 == 0:
                print(json.dumps({'visited': len(rows),
                    'finite': sum(r['status'] == 'finite bound' for r in rows),
                    'unresolved': sum(r['status'] != 'finite bound' for r in rows),
                    'elapsed_seconds': time.monotonic()-started}), flush=True)

    changed = []
    for name, digest in bindings.items():
        p = Path(name)
        if sha(p if p.is_absolute() else ROOT/p) != digest:
            changed.append(name)
    if changed:
        reason = 'input changed during run'
    completed_indices = {r['bank_reference_index'] for r in rows}
    pending = [i for i, _ in selected if i not in completed_indices]
    unresolved = [r['bank_reference_index'] for r in rows if r['status'] != 'finite bound']
    complete = not pending and not unresolved and not changed and not errors
    summaries = []
    for domain, factor in (('k3', F(6889, 2000000)), ('k4', F(9, 5000))):
        cells = [r for r in rows if r['external_domain'] == domain and r['status'] == 'finite bound']
        gamma = min((F(r['boundary_gap_lower_rational']) for r in cells), default=None)
        B = max(F(r['response']['B_upper_rational']) for _, r in selected if r['external_domain'] == domain)
        delta = gamma-factor*B if complete and gamma is not None else None
        summaries.append({'beta': 0, 'domain': domain, 'finite_bound_cells': len(cells),
            'observed_boundary_gap_lower_rational': None if gamma is None else str(gamma),
            'saved_response_upper_rational': str(B), 'barrier_factor_rational': str(factor),
            'compensated_gap_rational': None if delta is None else str(delta),
            'valid_positive_whole_domain_gap': delta is not None and delta > 0,
            'strictly_above_common_gap_1_over_3200': delta is not None and delta > F(1, 3200)})
    result = {'status': reason, 'alpha': 1, 'beta': 0, 'precision_bits': PRECISION,
        'reference_bank': BANK, 'reference_bank_sha256': PINNED[BANK],
        'rows': rows, 'terminal_geometry': geometry, 'boundary_chart_count': 9,
        'inherited_geometric_exclusions': 58, 'complete_reference_inventory': True,
        'pending_bank_reference_indices': pending, 'unresolved_bank_reference_indices': unresolved,
        'complete_boundary_evaluation': complete, 'domain_summaries': summaries,
        'uniform_half_row_gap_proved': complete and all(s['valid_positive_whole_domain_gap'] for s in summaries),
        'common_gap_1_over_3200_proved': complete and all(s['strictly_above_common_gap_1_over_3200'] for s in summaries),
        'counts': dict(counts), 'input_sha256': bindings, 'changed_inputs': changed,
        'unexpected_errors': errors, 'stop_signals': stopped, 'elapsed_seconds': time.monotonic()-started,
        'source_root_evaluations': 0, 'new_reference_derivative_evaluations': 0,
        'parameter_subdivisions': 0, 'full_source_theorem_claimed': False,
        'global_filling_volume_theorem_claimed': False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'status': reason, 'visited': len(rows),
        'complete_boundary_evaluation': complete,
        'uniform_half_row_gap_proved': result['uniform_half_row_gap_proved'],
        'domain_summaries': summaries, 'output_sha256': sha(args.output)}), flush=True)


if __name__ == '__main__':
    main()
