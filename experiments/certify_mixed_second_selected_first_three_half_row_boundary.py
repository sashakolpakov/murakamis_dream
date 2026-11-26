#!/usr/bin/env python3
"""Evaluate alpha-zero half-row budgets on a completed saved beta-zero boundary.

Guarded until the new audited source/bank identities and counts are frozen.
No reference, root, transport, response or subdivision is evaluated here.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import gzip
import importlib
import json
from pathlib import Path
import signal
import time

from flint import acb, ctx

ROOT = Path(__file__).resolve().parents[1]
ALPHA = 0
BETA = 0
BANK = 'repro/results/research-mixed-second-selected-first-three-boundary-reference-bank.json.gz'
SOURCE = 'repro/results/research-mixed-second-selected-first-three-external-boundary-attempt01.json.gz'
AUDIT = 'repro/results/research-mixed-second-selected-first-three-external-boundary-saved-audit.json'
CHECKER = 'experiments/check_mixed_second_selected_first_three_external_boundary_record.py'
EXTRACTOR = 'experiments/extract_mixed_second_selected_first_three_boundary_references.py'
SPEC = 'notes/research_mixed_second_selected_first_three_half_row_boundary_evaluation.md'
EVALUATOR = 'experiments/evaluate_mixed_second_selected_first_three_half_row_budget.py'
PINNED = {
    BANK: '4b0bfa3cb2bfb68b622487c390879312b7d0832a056f03c3675a38cedeb8c323',
    SOURCE: '9744bb69bd81745f856b0424f7df3448b39f5208eae929f709dc7a3d639af956',
    AUDIT: '88d8f8177a439f4268980e7467fffc576b558776c22f2a6067361d0ab8b6a047',
    CHECKER: '9e53d3b6f9278289b7b2ba3ab3107b584d25f498d6a61dc5108ebb6c754315db',
    EXTRACTOR: '0367c8d65f99b6ecd077928b03bc38aae3b432f21815ac18294c117cb015d643',
    SPEC: 'dfcb01e5c4fffea5780b279da02f5e7f8d9c3f9bc22744ad74adeee9d2f3ca8b',
    EVALUATOR: 'b40de9e7c5b215ada0213010a0fe0569ca86a6c1e16277257b8c76750315e059',
    'notes/research_mixed_second_selected_first_three_half_row_evaluation.md':
        '8de75d8e7628977c48e2eab9a76b0a02bb3502b9b12247f64a0b683f6f801e75',
    'notes/research_mixed_second_selected_first_three_extension.md':
        'd488ff98e01cfd5cd077de664c7e3bee3bfeeb735009f8c78f7c0ac60c7ad0e2',
    'notes/research_mixed_second_selected_half_row_boundary_extension.md':
        '0aa085f65489e024fa9e31040a507db8b681fd409de349a59db91c39929c0152',
    'experiments/certify_mixed_second_selected_half_row_boundary.py':
        'f9761b35a15a439edb273b9a7e00a587f07431558b14c9cb87818c3ba9ec4bb0',
    'notes/research_mixed_second_selected_half_row_boundary_evaluation.md':
        '82c82be3e35ce3fa53e08b95ad94f15e72806367117d122ff5de50684f0aa7b1',
}
# Exact beta-zero counts from the completed source; checked against the audited bank.
EXPECTED_COUNTS = {
    'accepted': 782, 'terminal_geometry': 840,
    'geometry_excluded': 58, 'reference_excluded': 0,
    'accepted_k3': 387, 'accepted_k4': 395,
}
CHARTS = frozenset((
    'k3_circle_right', 'k3_circle_left', 'k3_lower_chord',
    'k3_upper_chord', 'k3_oblique_chord', 'k4_circle_right',
    'k4_circle_left', 'k4_lower_chord', 'k4_upper_chord',
))
PRECISION = 256
CANDIDATE_GAP = F(1, 3200)


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


def validate_inventory(values, names):
    if set(values) != set(names):
        raise ValueError('wrong saved complex inventory')
    for value in values.values():
        interval(value['real'])
        interval(value['imag'])


def verify_adapter_result(result):
    if result.get('alpha') != ALPHA or result.get('beta') != BETA:
        raise ValueError('half-row scalar belongs to the wrong reference family')
    metadata = result['alpha_adapter']
    if (metadata['frozen_helper_calls'] != 1
            or metadata['arithmetic_details_and_status_unchanged'] is not True
            or metadata['frozen_reported_alpha'] != 1
            or metadata['remove_for_original_result'] != ['alpha_adapter']):
        raise ValueError('unexpected scalar-adapter provenance')
    original = dict(result)
    del original['alpha_adapter']
    original.update(metadata['restore_original_metadata'])
    if canonical_sha(original) != metadata['frozen_result_canonical_sha256']:
        raise ValueError('frozen scalar-result restoration failed')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not str(args.output).endswith('.json.gz'):
        raise ValueError('output must end in .json.gz')
    required = {BANK, SOURCE, AUDIT, CHECKER, EXTRACTOR, SPEC, EVALUATOR}
    if (not required.issubset(PINNED)
            or any(not isinstance(x, str) or len(x) != 64 for x in PINNED.values())
            or any(not isinstance(x, int) or x < 0 for x in EXPECTED_COUNTS.values())):
        raise RuntimeError('completed source/bank/audit identities and counts are not frozen')
    bindings = dict(PINNED)
    verify(bindings)
    audit = json.loads((ROOT/AUDIT).read_text())
    if (audit['status'] != 'exact saved-data check passed' or audit['alpha'] != ALPHA
            or audit['source'] != SOURCE or audit['source_sha256'] != PINNED[SOURCE]
            or audit['checker_sha256'] != PINNED[CHECKER]
            or audit['complete_chart_cases'] != 18
            or not audit['all_alpha_zero_metadata_checked']
            or not audit['all_accepted_reference_response_scalar_associations_checked']
            or not audit['all_common_product_and_strict_height_checks_recomputed']
            or not audit['all_global_gamma_B_extrema_recomputed_separately']):
        raise ValueError('unexpected completed central audit')
    with gzip.open(ROOT/BANK, 'rt', encoding='utf-8') as stream:
        bank = json.load(stream)
    if (bank['schema'] != 'mixed-second-selected-first-three-certified-boundary-references-v1'
            or bank['alpha'] != ALPHA or bank['beta_cases'] != [0, 1]
            or bank['precision_bits'] != PRECISION
            or bank['pending_frontier'] or bank['unresolved_frontier']
            or bank['alpha_one_reference_data_used'] is not False
            or bank['source'] != SOURCE or bank['source_sha256'] != PINNED[SOURCE]
            or bank['saved_data_audit'] != AUDIT
            or bank['saved_data_audit_sha256'] != PINNED[AUDIT]
            or bank['source_visited_nodes'] != audit['visited_nodes']
            or bank['accepted_reference_count'] != audit['accepted_leaves']
            or bank['accepted_reference_count'] != len(bank['accepted_references'])
            or bank['terminal_geometry_count'] != audit['terminal_leaves']
            or bank['terminal_geometry_count'] != len(bank['terminal_geometry'])
            or bank['strict_geometry_exclusions'] != audit['strict_geometry_exclusions']
            or bank['certified_reference_exclusions'] != audit['certified_reference_exclusions']):
        raise ValueError('unexpected completed reference bank')
    merge(bindings, bank['input_sha256'])
    verify(bindings)

    # Every case is inherited from a positive, complete original central cover.
    audited = {(r['beta'], r['domain']): r for r in audit['domain_summaries']}
    inherited = {(r['beta'], r['domain']): r for r in bank['domain_summaries']}
    expected_domains = {(beta, domain) for beta in (0, 1) for domain in ('k3', 'k4')}
    if (set(audited) != expected_domains or set(inherited) != expected_domains
            or len(audit['domain_summaries']) != 4 or len(bank['domain_summaries']) != 4):
        raise ValueError('incomplete central domain inventory')
    for key in expected_domains:
        a, r = audited[key], inherited[key]
        if (a['alpha'] != ALPHA or r['alpha'] != ALPHA
                or not r['valid_for_whole_domain']
                or F(a['corrected_gap_rational']) <= 0
                or F(a['corrected_gap_rational']) != F(r['compensated_gap_rational'])
                or F(a['B_max_rational']) != F(r['observed_response_upper_rational'])):
            raise ValueError('inconsistent completed central domain bounds')

    selected = [(i, r) for i, r in enumerate(bank['accepted_references']) if r['beta'] == BETA]
    geometry = [g for g in bank['terminal_geometry'] if g['beta'] == BETA]
    observed_counts = {
        'accepted': len(selected), 'terminal_geometry': len(geometry),
        'geometry_excluded': sum(g['status'] == 'excluded' for g in geometry),
        'reference_excluded': sum(g['status'] == 'excluded by certified reference domain' for g in geometry),
        'accepted_k3': sum(r['external_domain'] == 'k3' for _, r in selected),
        'accepted_k4': sum(r['external_domain'] == 'k4' for _, r in selected),
    }
    if observed_counts != EXPECTED_COUNTS or not all(observed_counts['accepted_'+k] for k in ('k3', 'k4')):
        raise ValueError('incomplete beta-zero reference inventory')
    addresses = defaultdict(list)
    associations = {r['source_node_index']: (i, r) for i, r in selected}
    if len(associations) != len(selected):
        raise ValueError('duplicate reference source node')
    for i, r in selected:
        payload = dict(r)
        expected = payload.pop('compact_payload_canonical_sha256')
        if canonical_sha(payload) != expected:
            raise ValueError('changed compact reference payload')
        if (r['alpha'] != ALPHA or r['precision_bits'] != PRECISION
                or r['status'] != 'accepted boundary estimate'
                or r['response']['alpha'] != ALPHA or r['response']['beta'] != BETA
                or r['response']['status'] != 'enclosed'
                or not r['response']['height_conditions_verified']
                or not r['response']['common_prefix_product_verified']):
            raise ValueError('missing inherited reference family, height or common-product bound')
        validate_inventory(r['coordinates'], ('e', 'xi', 'a', 'u', 'z', 'v', 'b', 'c'))
        validate_inventory(r['negative_shapes'], ('e', 'a', 'u', 'z', 'v', 'b', 'c'))
        validate_inventory(r['derivatives'], ('e', 'xi', 'a', 'u', 'z', 'v', 'b'))
        blo, bhi = interval(r['response']['B'])
        if blo < 0 or bhi != F(r['response']['B_upper_rational']):
            raise ValueError('inconsistent saved response interval')
    seen_nodes, seen_references = set(), set()
    for g in geometry:
        if (g['alpha'] != ALPHA or g['chart'] not in CHARTS
                or g['external_domain'] != g['chart'][:2]
                or g['source_node_index'] in seen_nodes):
            raise ValueError('invalid inherited terminal association')
        seen_nodes.add(g['source_node_index'])
        addresses[g['chart']].append(g['address'])
        if g['status'] == 'accepted boundary estimate':
            i, r = associations[g['source_node_index']]
            if g['accepted_reference_index'] != i or i in seen_references:
                raise ValueError('wrong reference-bank index')
            seen_references.add(i)
            for key in ('alpha', 'beta', 'chart', 'address', 'external_domain',
                        'parameter_interval', 'external_coordinate_box', 'source_node_canonical_sha256'):
                if g[key] != r[key]:
                    raise ValueError('wrong terminal/reference association')
        elif g['status'] == 'excluded':
            if not g['source_exclusion']:
                raise ValueError('missing preserved geometry exclusion')
        elif g['status'] == 'excluded by certified reference domain':
            if not g['certified_reference_exclusion']:
                raise ValueError('missing preserved reference exclusion')
        else:
            raise ValueError('unresolved inherited geometry')
    if seen_references != {i for i, _ in selected}:
        raise ValueError('reference without a terminal boundary interval')
    expected_cases = {(beta, chart) for beta in (0, 1) for chart in CHARTS}
    cases = bank['coverage']['cases']
    if (len(cases) != 18 or {(c['beta'], c['chart']) for c in cases} != expected_cases
            or set(addresses) != CHARTS):
        raise ValueError('incomplete boundary-chart inventory')
    for chart, aa in addresses.items():
        ss = sorted(aa)
        if (len(set(ss)) != len(ss)
                or any(not isinstance(a, str) or set(a)-{'0', '1'} for a in ss)
                or any(b.startswith(a) for a, b in zip(ss, ss[1:]))
                or sum((F(1, 2**len(a)) for a in ss), F()) != 1):
            raise ValueError('invalid complete boundary partition: '+chart)
    for domain in ('k3', 'k4'):
        group = [r for _, r in selected if r['external_domain'] == domain]
        a = audited[(BETA, domain)]
        if (len(group) != a['accepted_cells']
                or max(F(r['response']['B_upper_rational']) for r in group) != F(a['B_max_rational'])):
            raise ValueError('saved reference response extrema differ from central audit')

    evaluator = importlib.import_module(Path(EVALUATOR).stem)
    if Path(evaluator.__file__).resolve() != (ROOT/EVALUATOR).resolve():
        raise ValueError('wrong first-type-three half-row evaluator module')
    initialization = evaluator.initialize()
    if initialization.get('alpha') != ALPHA or initialization.get('beta_cases') != [0, 1]:
        raise ValueError('unexpected scalar adapter family')
    merge(bindings, initialization['bindings'])
    old = importlib.import_module('diagnose_mixed_second_selected_central_budget')
    old_inputs, _ = old.verified_inputs()
    merge(bindings, old_inputs)
    four = importlib.import_module('diagnose_mixed_four_four_half_row_budget')
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    verify(bindings)

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
        row.update({'alpha': ALPHA, 'beta': BETA})
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
            verify_adapter_result(result)
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

    if stopped and reason == 'complete saved-reference pass':
        reason = 'stop signal received'
    changed = []
    for name, digest in bindings.items():
        p = Path(name)
        try:
            matches = sha(p if p.is_absolute() else ROOT/p) == digest
        except OSError:
            matches = False
        if not matches:
            changed.append(name)
    if changed:
        reason = 'input changed during run'
    completed_indices = {r['bank_reference_index'] for r in rows}
    pending = [i for i, _ in selected if i not in completed_indices]
    unresolved = [r['bank_reference_index'] for r in rows if r['status'] != 'finite bound']
    complete = not pending and not unresolved and not changed and not errors and not stopped
    summaries = []
    for domain, factor in (('k3', F(6889, 2000000)), ('k4', F(9, 5000))):
        cells = [r for r in rows if r['external_domain'] == domain and r['status'] == 'finite bound']
        gamma = min((F(r['boundary_gap_lower_rational']) for r in cells), default=None)
        B = max(F(r['response']['B_upper_rational']) for _, r in selected if r['external_domain'] == domain)
        delta = gamma-factor*B if complete and gamma is not None else None
        summaries.append({'alpha': ALPHA, 'beta': BETA, 'domain': domain, 'finite_bound_cells': len(cells),
            'observed_boundary_gap_lower_rational': None if gamma is None else str(gamma),
            'saved_response_upper_rational': str(B), 'barrier_factor_rational': str(factor),
            'compensated_gap_rational': None if delta is None else str(delta),
            'valid_positive_whole_domain_gap': delta is not None and delta > 0,
            'strictly_above_candidate_gap_1_over_3200': delta is not None and delta > CANDIDATE_GAP})
    result = {'status': reason, 'alpha': ALPHA, 'beta': BETA, 'precision_bits': PRECISION,
        'reference_bank': BANK, 'reference_bank_sha256': PINNED[BANK],
        'rows': rows, 'terminal_geometry': geometry, 'boundary_chart_count': 9,
        'inherited_geometric_exclusions': observed_counts['geometry_excluded'],
        'inherited_certified_reference_exclusions': observed_counts['reference_excluded'],
        'expected_reference_inventory': dict(EXPECTED_COUNTS),
        'observed_reference_inventory': observed_counts,
        'complete_reference_inventory': True,
        'saved_central_audit': AUDIT, 'saved_central_audit_sha256': PINNED[AUDIT],
        'saved_central_source': SOURCE, 'saved_central_source_sha256': PINNED[SOURCE],
        'alpha_one_reference_data_used': False,
        'candidate_gap_rational': str(CANDIDATE_GAP),
        'pending_bank_reference_indices': pending, 'unresolved_bank_reference_indices': unresolved,
        'complete_boundary_evaluation': complete, 'domain_summaries': summaries,
        'uniform_half_row_gap_proved': complete and all(s['valid_positive_whole_domain_gap'] for s in summaries),
        'candidate_gap_1_over_3200_proved': complete and all(s['strictly_above_candidate_gap_1_over_3200'] for s in summaries),
        'counts': dict(counts), 'input_sha256': bindings, 'changed_inputs': changed,
        'unexpected_errors': errors, 'stop_signals': stopped, 'elapsed_seconds': time.monotonic()-started,
        'source_root_evaluations': 0, 'new_reference_derivative_evaluations': 0,
        'parameter_subdivisions': 0, 'full_source_theorem_claimed': False,
        'global_filling_volume_theorem_claimed': False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(args.output, 'xt', compresslevel=1, encoding='utf-8') as stream:
        json.dump(result, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'status': reason, 'visited': len(rows),
        'complete_boundary_evaluation': complete,
        'uniform_half_row_gap_proved': result['uniform_half_row_gap_proved'],
        'domain_summaries': summaries, 'output_sha256': sha(args.output)}), flush=True)


if __name__ == '__main__':
    main()
