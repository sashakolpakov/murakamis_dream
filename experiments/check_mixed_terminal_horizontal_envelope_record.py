#!/usr/bin/env python3
"""Exact saved-only audit of four terminal horizontal-envelope lower tests."""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
SOURCE_SHA = 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b'
NAMES = ('e', 'xi', 't', 'a', 's')
RADIUS = F(1, 10**30)
CENTERS = ((F(7, 20), -F(1, 100)), (F(3, 10), -F(13, 250)))


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def interval(record):
    assert record['finite'] is True
    lo, hi = F(record['lower_rational']), F(record['upper_rational'])
    assert lo <= hi
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    assert sha(ROOT/SOURCE) == SOURCE_SHA
    data = json.loads((ROOT/SOURCE).read_text())
    assert data['status'] == 'complete fixed diagnostic'
    assert data['changed_inputs'] == []
    assert len(data['input_sha256']) == 27
    for name, digest in data['input_sha256'].items():
        assert sha(ROOT/name) == digest, name
    assert data['precision_bits'] == 256
    assert data['proposal_precision_digits'] == 80 and data['proposal_maxsteps'] == 30
    assert data['proposal_tolerance'] == '1e-55' and data['proposal_saved_digits'] == 60
    assert data['counts'] == {
        'reference_proposals': 4, 'original_residual_evaluations': 4,
        'marginal_enclosures': 4, 'lower_tests': 12,
        'dilogarithm_evaluations': 0, 'target_optimizations': 0,
        'finite_quantum_sums': 0, 'parameter_subdivisions': 0,
        'alternate_seeds': 0, 'precision_retries': 0}
    assert data['heights_rational'] == ['0', '1/100', '7/500']
    assert not data['whole_source_sign_claimed'] and not data['uniform_domain_sign_claimed']
    assert not data['full_378_profile_pass_performed']
    pi_lo, pi_hi = interval(data['pi'])
    assert F(157, 50) < pi_lo <= pi_hi < F(22, 7)
    summaries = []
    expected = list(itertools.product((0, 1), repeat=2))
    assert [(r['beta'], r['epsilon']) for r in data['cases']] == expected
    roundings = (F(1023, 100000), F(1309, 100000), F(1782, 100000), F(2042, 100000))
    for row, (beta, epsilon), coarse in zip(data['cases'], expected, roundings):
        assert row['status'] == 'canonical reference and lower tests certified'
        assert row['canonical_reference_certified'] is True
        assert not row['suffix_realization_claimed'] and not row['source_comparison_claimed']
        assert list(map(F, row['outside_coordinate'])) == list(CENTERS[beta])
        center = [[F(v) for v in z] for z in row['proposed_centers']]
        assert len(center) == 5 and F(row['radius_rational']) == RADIUS
        for name, (x, y) in zip(NAMES, center):
            box, guard = row['coordinate_enclosures'][name], row['domain_checks'][name]
            assert interval(box['real']) == (x-RADIUS, x+RADIUS)
            assert interval(box['imag']) == (y-RADIUS, y+RADIUS)
            assert guard['common_product_verified'] and guard['typed_rectangle_verified']
            common = ('.33', '.47', '-.09', '.08') if name == 'e' else (
                ('.21', '.25', '.01', '.10') if name == 'xi' else ('.23', '.45', '-.12', '.12'))
            typed = ({'e': ('.376', '.438', '-.019', '.037'),
                      'xi': ('.218', '.242', '.049', '.077'),
                      't': ('.278', '.391', '-.072', '.021')} if epsilon == 0 else
                     {'e': ('.333', '.363', '-.051', '-.019'),
                      'xi': ('.217', '.234', '.027', '.045'),
                      't': ('.246', '.350', '-.108', '-.020')}).get(
                          name, ('.24', '.36', '-.102', '-.001'))
            assert list(map(F, guard['common_bounds'])) == list(map(F, common))
            assert list(map(F, guard['typed_bounds'])) == list(map(F, typed))
            for key in ('common_bounds', 'typed_bounds'):
                lo, hi, bot, top = map(F, guard[key])
                assert lo < x-RADIUS < x+RADIUS < hi
                assert bot < y-RADIUS < y+RADIUS < top
        for name, kind in (('a', 1), ('s', 1), ('t', epsilon)):
            z = center[NAMES.index(name)]
            cx, cy = CENTERS[kind]
            rr = F(83, 1000) if kind == 0 else F(3, 50)
            distance = (abs(z[0]-cx)+RADIUS)**2+(abs(z[1]-cy)+RADIUS)**2
            guard = row['domain_checks'][name]
            assert F(guard['typed_disk_squared_distance_upper_rational']) == distance < rr**2
            assert F(guard['typed_disk_radius_squared_rational']) == rr**2
        if epsilon == 1:
            guard = row['domain_checks']['a']
            assert F(guard['oriented_real_floor_rational']) == center[3][0]-RADIUS > F(259, 1000)
            assert F(guard['oriented_threshold_rational']) == F(259, 1000)
        residual = row['original_gradient_residual']
        assert len(residual) == 5
        r2 = sum(max(map(abs, interval(v[part])))**2 for v in residual for part in ('real', 'imag'))
        mu = F(6, 49)*pi_lo
        threshold = mu**2*RADIUS**2
        assert F(row['accretivity_lower_rational']) == mu
        assert F(row['residual_squared_upper_rational']) == r2 < threshold
        assert F(row['residual_threshold_rational']) == threshold
        for name in ('a', 't'):
            for part in ('real', 'imag'):
                lo, hi = interval(row['actual_marginal_input_enclosures'][name][part])
                original_lo, original_hi = interval(row['coordinate_enclosures'][name][part])
                assert lo <= original_lo <= original_hi <= hi
        plo, phi = interval(row['allocated_terminal_marginal']['imag'])
        clo, chi = interval(row['coordinate_enclosures']['a']['imag'])
        lows = []
        assert [x['height_rational'] for x in row['lower_tests']] == ['0', '1/100', '7/500']
        for test in row['lower_tests']:
            h = F(test['height_rational'])
            delta = (h-chi, h-clo)
            products = [d*p for d in delta for p in (plo, phi)]
            lower, upper = min(products)-h*pi_hi, max(products)-h*pi_lo
            assert interval(test['delta']) == delta
            assert list(map(F, test['product_corner_rationals'])) == products
            assert interval(test['L']) == (lower, upper)
            assert test['positive_majorant_trial_proved'] is (lower > 0)
            lows.append(lower)
        minimum = min(lows[0], lows[2])
        assert row['all_allowed_heights_obstructed'] and minimum > coarse > F(1, 100)
        summaries.append({'beta': beta, 'epsilon': epsilon,
                          'height_lower_bounds_rational': list(map(str, lows)),
                          'all_height_lower_bound_rational': str(minimum),
                          'conservative_lower_bound_rational': str(coarse),
                          'strictly_above_1_over_100': True})
    out = {'status': 'passed', 'source_sha256': SOURCE_SHA, 'source_path': SOURCE,
           'checker_sha256': sha(Path(__file__)), 'inherited_bindings_checked': 27,
           'canonical_references_checked': 4, 'residual_components_checked': 40,
           'exact_lower_tests_checked': 12, 'cases': summaries,
           'common_majorant_obstruction_lower_rational': '1/100',
           'parameter_range': {'height_lower': '0', 'height_upper': '7/500'},
           'source_counterexample_claimed': False, 'finite_suffix_realization_claimed': False,
           'uniform_reference_domain_claimed': False, 'analytic_callbacks': 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'audit_sha256': sha(args.output),
                      'references': 4, 'lower_tests': 12, 'common_lower': '1/100'}))


if __name__ == '__main__':
    main()
