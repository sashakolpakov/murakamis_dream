#!/usr/bin/env python3
"""Saved-only exact audit of the eight terminal joint-main support budgets."""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json'
SOURCE_SHA = '2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9'
REFERENCES = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def interval(v):
    assert v['finite'] is True
    lo, hi = F(v['lower_rational']), F(v['upper_rational'])
    assert lo <= hi
    return lo, hi


def fragment_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    assert sha(ROOT / SOURCE) == SOURCE_SHA
    data = json.loads((ROOT / SOURCE).read_text())
    assert data['status'] == 'complete fixed diagnostic' and data['changed_inputs'] == []
    assert data['precision_bits'] == 256 and F(data['height_rational']) == F(1, 100)
    assert len(data['input_sha256']) == 37
    for name, digest in data['input_sha256'].items():
        assert sha(ROOT / name) == digest, name
    refs = json.loads((ROOT / REFERENCES).read_text())
    assert refs['status'] == 'complete fixed diagnostic' and refs['changed_inputs'] == []
    assert data['counts'] == {
        'saved_reference_cases': 4, 'primitive_evaluations': 24,
        'log_derivative_evaluations': 24, 'branch_bounds': 8,
        'reference_proposals': 0, 'root_solves': 0,
        'reference_transport_evaluations': 0, 'target_optimizations': 0,
        'subdivisions': 0, 'precision_retries': 0,
        'terminal_private_action_evaluations': 0, 'finite_quantum_source_evaluations': 0}
    assert not data['all_eight_main_bounds_negative']
    assert not data['whole_source_sign_claimed'] and not data['uniform_reference_domain_claimed']
    assert not data['finite_word_realization_claimed'] and not data['complete_54_profile_pass_performed']
    pi_lo, pi_hi = interval(data['pi'])
    assert F(157, 50) < pi_lo <= pi_hi < F(22, 7)
    expected = list(itertools.product((0, 1), repeat=2))
    assert [(c['beta'], c['epsilon']) for c in data['cases']] == expected
    summaries, products_checked = [], 0
    for index, (row, ref) in enumerate(zip(data['cases'], refs['cases'])):
        assert row['source_index'] == index
        assert row['source_case_sha256'] == fragment_sha(ref)
        assert (row['beta'], row['epsilon']) == (ref['beta'], ref['epsilon'])
        assert ref['canonical_reference_certified'] and row['status'] == 'both main-current bounds enclosed'
        assert row['outside_coordinate_rational'] == ref['outside_coordinate']
        assert row['saved_coordinate_enclosures'] == ref['coordinate_enclosures']
        assert row['ordinary_label_reduction_height_verified']
        assert row['force_signs_theoretically_proved'] and row['outward_force_signs_verified']
        assert not row['finite_word_realization_claimed']
        saved = row['saved_coordinate_enclosures']
        actual = row['actual_coordinate_enclosures']
        for name in ('e', 'xi', 't', 'a', 's'):
            for part in ('real', 'imag'):
                assert contains(interval(actual[name][part]), interval(saved[name][part]))
        assert interval(row['force_s'])[0] > 0 and interval(row['force_t'])[1] < 0
        assert F(row['height_rational']) == F(1, 100)
        # These are necessary input rectangles from the exact certified boxes,
        # not twice-serialized live Arb boxes. No primitive is reevaluated.
        for name in ('a', 'sa', 'ta', 'aH', 'saH', 'taH'):
            target = row['original_values'][name]
            assert target['original_strip_and_cuts_verified']
            real, imag = interval(saved['a']['real']), interval(saved['a']['imag'])
            if name.endswith('H'):
                imag = (F(1, 100), F(1, 100))
            if name.startswith('s') or name.startswith('t'):
                coordinate = name[0]
                real = add(real, interval(saved[coordinate]['real']))
                imag = add(imag, interval(saved[coordinate]['imag']))
            assert contains(interval(target['argument']['real']), real)
            assert contains(interval(target['argument']['imag']), imag)
            assert F(0) < interval(target['argument']['real'])[0]
            assert interval(target['argument']['real'])[1] < F(1)
            for value in ('g', 'g_prime', 'exponential'):
                interval(target[value]['real']); interval(target[value]['imag'])
        assert [b['nu'] for b in row['branches']] == [1, 0]
        summary = {'beta': row['beta'], 'epsilon': row['epsilon'], 'branches': []}
        for branch in row['branches']:
            nu = branch['nu']
            selected = (F(11, 50), F(9, 20)) if nu else (F(2, 5), F(9, 20))
            assert list(map(F, branch['selected_target_interval_rational'])) == list(selected)
            assert branch['label'] == ('factorial' if nu else 'forced')
            assert not branch['forced_trial_lower_bound_claimed'] and not branch['whole_source_sign_claimed']
            total_lo, total_hi = interval(branch['lifted_reference_value'])
            for name, bounds in (('s', (F(1, 8), F(1, 2))),
                                 ('a', selected), ('t', (F(3, 20), F(1, 2)))):
                support = branch['supports'][name]
                force = branch['force_a'] if name == 'a' else row['force_' + name]
                assert support['force'] == force and support['center'] == actual[name]['real']
                assert list(map(F, support['target_interval_rational'])) == list(bounds)
                assert not support['truncated_at_zero']
                fl, fh = interval(force); cl, ch = interval(support['center'])
                product_intervals = []
                for record, x in zip(support['endpoint_products'], bounds):
                    assert F(record['target_rational']) == x
                    disp = x - ch, x - cl
                    assert interval(record['displacement']) == disp
                    corners = [d * z for d in (fl, fh) for z in disp]
                    assert list(map(F, record['product_corners_rational'])) == corners
                    assert interval(record['value']) == (min(corners), max(corners))
                    product_intervals.append(interval(record['value']))
                    products_checked += 4
                support_bounds = tuple(max(v[j] for v in product_intervals) for j in (0, 1))
                assert interval(support['value']) == support_bounds
                total_lo += support_bounds[0]; total_hi += support_bounds[1]
            assert F(branch['total_upper_rational']) == total_hi
            assert branch['main_profile_negative_proved'] is (total_hi < 0)
            assert not branch['factorial_positive_trial_proved']
            if nu:
                assert total_lo > F(1, 50)
                assert interval(branch['lifted_reference_value'])[1] < -F(1, 25)
            else:
                assert total_hi < -F(1, 400)
            summary['branches'].append({'nu': nu, 'label': branch['label'],
                                        'support_budget_lower_rational': str(total_lo),
                                        'support_budget_upper_rational': str(total_hi),
                                        'lifted_reference_value': branch['lifted_reference_value']})
        summaries.append(summary)
    assert products_checked == 192
    out = {'status': 'passed', 'source_path': SOURCE, 'source_sha256': SOURCE_SHA,
           'checker_sha256': sha(Path(__file__)), 'input_bindings_checked': 37,
           'certified_reference_associations_checked': 4, 'branch_bounds_checked': 8,
           'exact_endpoint_products_checked': products_checked, 'cases': summaries,
           'forced_main_gap_rational': '1/400', 'factorial_support_budget_lower_rational': '1/50',
           'factorial_lifted_value_upper_rational': '-1/25',
           'whole_source_sign_claimed': False, 'uniform_reference_domain_claimed': False,
           'finite_word_realization_claimed': False, 'factorial_main_sign_claimed': False,
           'primitive_or_reference_replays': 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'audit_sha256': sha(args.output),
                      'references': 4, 'branches': 8, 'forced_main_gap': '1/400'}))


if __name__ == '__main__':
    main()
