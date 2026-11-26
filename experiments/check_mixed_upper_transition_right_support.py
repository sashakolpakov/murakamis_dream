#!/usr/bin/env python3
"""Extract complete upper-transition/right support; no numerical cover rerun."""
import argparse
import hashlib
import itertools
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_upper_transition_right_support.md'
SPECS = [
    ('mixed_right_core_support_grid', 'certify', None, 'mixed_right_core_support'),
    ('mixed_right_core_support_grid', 'replay', 'replay', 'mixed_right_core_support'),
    ('mixed_right_core_support_reference', 'certify', None, 'mixed_right_core_support'),
    ('mixed_right_core_support_reference', 'certify', 'replay', 'mixed_right_core_support'),
    ('mixed_right_half_concavity', 'check', None, None),
    ('mixed_right_half_source_reduction', 'check', None, None),
    ('mixed_high_row_endpoint_reduction', 'certify', None, None),
    ('mixed_high_row_endpoint_reduction', 'replay', 'replay', None),
    ('mixed_all_endpoint_support', 'certify', None, None),
    ('mixed_all_endpoint_support', 'replay', 'replay', None),
    ('mixed_43_endpoint_support', 'check', None, None),
    ('mixed_43_endpoint_support', 'replay', 'replay', None),
    ('mixed_geometric_support_slopes', 'certify', None, None),
    ('mixed_geometric_support_slopes', 'replay', 'replay', None),
    ('mixed_fourier_weight_continuation', 'check', None, None),
    ('mixed_boundary_strip_bounds', 'check', None, None),
    ('mixed_split_cutoff_hybrid_contour', 'check', None, None),
]
ARCHIVE_SHA = '27c612712027db8aeaf62b1f919c298c8f82779a9570717f2344c1a686e02ee2'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def interval(text):
    """Exact endpoints of a recorded decimal ball; no new transcendental test."""
    text = text.strip()
    match = re.fullmatch(r'\[([^\[\]]+?)\s+\+/-\s+([^\[\]]+?)\]', text)
    if match:
        center, radius = map(F, match.groups())
        assert radius >= 0
        return center-radius, center+radius
    value = F(text)
    return value, value


def exact_cover(addresses):
    codes = sorted(addresses)
    assert codes and len(codes) == len(set(codes))
    assert all(set(code) <= {'0', '1'} for code in codes)
    assert all(not b.startswith(a) for a, b in zip(codes, codes[1:]))
    assert sum((F(1, 2**len(code)) for code in codes), F(0)) == 1
    return codes


def window_covers(record):
    expected = {(*word, ta, tb, fa, fb)
                for word in itertools.product((0, 1), repeat=3)
                for ta, tb in itertools.product((0, 1), repeat=2)
                for fa, fb in itertools.product(range(4), repeat=2)}
    found = {}
    for row in record['cases']:
        key = (*row['word'], *row['external'], *row['faces'])
        assert key not in found
        found[key] = exact_cover(row['addresses'])
        assert interval(row['min_gap'])[0] > F(1, 500)
    assert set(found) == expected
    assert sum(map(len, found.values())) == record['accepted_cells'] == 5546
    assert record['boundary_products'] == 512
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-upper-transition-right-support.json')
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, records, primary = {}, set(), {}, []

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        if path in dependencies:
            assert dependencies[path] == digest, path
        dependencies[path] = digest
        return digest

    def inherit(path):
        bind(path)
        record = json.loads((ROOT/path).read_text())
        if path in visited:
            return record
        visited.add(path)
        inherited = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for p, digest in record.get(field, {}).items():
                if p in inherited:
                    assert inherited[p] == digest, (path, p)
                inherited[p] = digest
                bind(p, digest)
        for p in inherited:
            if p.startswith('repro/results/') and p.endswith('.json'):
                inherit(p)
        # Recursive traversal checks bindings, not theorem status of diagnostics.
        return record

    for stem, prefix, suffix, proof_stem in SPECS:
        pp = 'notes/research_' + (proof_stem or stem) + '.md'
        sp = 'experiments/' + prefix + '_' + stem + '.py'
        rp = 'repro/results/research-' + stem.replace('_', '-')
        rp += ('-' + suffix if suffix else '') + '.json'
        record = inherit(rp)
        bind(pp)
        bind(sp)
        assert record['status'] == 'passed', rp
        assert record['script_sha256'] == dependencies[sp], rp
        proof_binding = record.get('proof_sha256')
        if proof_binding is None:
            proof_binding = record.get('dependencies', {}).get(
                pp, record.get('dependencies_sha256', {}).get(pp))
        assert proof_binding == dependencies[pp], rp
        records[stem, suffix] = record
        primary.append(dict(record=rp, proof=pp, script=sp))
    bind('notes/research_mixed_right_half_block_bound.md')

    checks = []

    def check(name, assertion):
        assert assertion, name
        checks.append(name)

    def rec(stem, suffix=None):
        return records['mixed_' + stem, suffix]

    def input_binding(stem):
        path = 'repro/results/research-mixed-' + stem.replace('_', '-') + '.json'
        return rec(stem, 'replay')['input_sha256'] == dependencies[path]

    check('all seventeen complete primary records present',
          len(records) == len(SPECS) == 17)
    source, source_replay = rec('right_core_support_grid'), rec('right_core_support_grid', 'replay')
    check('complete source-grid counts and independent input binding',
          source['source_profiles'] == source_replay['source_profiles'] == 75
          and source['support_values'] == source_replay['support_values'] == 750
          and source_replay['precision_bits'] == 320
          and input_binding('right_core_support_grid'))
    slope_grid = [F(-1, 5)+F(j, 20) for j in range(10)]
    check('source slopes cover original geometric slope interval',
          list(map(F, source['slope_grid'])) == slope_grid
          and slope_grid[0] == F(-1, 5) and slope_grid[-1] == F(1, 4))
    all_keys = {(0, 0, 0), (1, 1, 0), (0, 0, 1),
                (0, 1, 1), (1, 0, 1), (1, 1, 1)}
    check('all six source families retained',
          {(p['e'], p['b'], p['c']) for p in source['profiles']} == all_keys)
    selected = [p for p in source['profiles']
                if p['name'] in ('all3', 'part4')]
    expected = set()
    for e, beta, c in all_keys:
        if beta == 0:
            for h in (F(-3, 100), F(1, 50)):
                expected.add((e, beta, c, 0, F(13, 100), F(1, 2), h))
        else:
            for sigma, heights in ((0, (F(-57, 1000), F(0))),
                                   (1, (F(0), F(7, 500)))):
                for h in heights:
                    expected.add((e, beta, c, sigma, F(2, 5), F(1, 2), h))
    actual = [(p['e'], p['b'], p['c'], p['sig'],
               F(p['ylo']), F(p['yhi']), F(p['h'])) for p in selected]
    check('literal eighteen height endpoints cover independent full bands',
          len(actual) == len(set(actual)) == 18 and set(actual) == expected)
    support_values = 0
    for p in selected:
        check('complete ten slopes for '+str((p['e'], p['b'], p['c'], p['sig'], p['h'])),
              [F(v['k']) for v in p['grid']] == slope_grid)
        for value in p['grid']:
            support_values += 1
            qs = {0, p['b']}
            assert {t['q'] for t in value['trials']} == qs
            assert {t['q'] for t in value['endpoint_trials']} == qs
            upper = F(value['upper'])
            for t in value['trials']:
                u, y = map(F, t['point'])
                assert F(1, 5) <= u <= F(1, 2)
                assert F(p['ylo']) <= y <= F(p['yhi'])
                assert upper > interval(t['upper'])[1]
            for t in value['endpoint_trials']:
                assert F(p['ylo']) <= F(t['point']) <= F(p['yhi'])
                assert upper > interval(t['upper'])[1]
    check('all180 extracted supports retain both branches and row-one bounds',
          support_values == 180)
    for eta, eps, orientation in itertools.product((0, 1), repeat=3):
        key = (eps, eps, 0) if orientation == 0 else (eps, eta, 1)
        assert key in all_keys
    check('both orientations of every ordered type pair have source profiles', True)

    reference = rec('right_core_support_reference')
    reference_replay = rec('right_core_support_reference', 'replay')
    check('all512 complete reference covers agree across original256 and320 runs',
          window_covers(reference) == window_covers(reference_replay)
          and reference['precision_bits'] == 256
          and reference_replay['precision_bits'] == 320)
    check('same source and dependency bindings in both reference runs',
          reference['dependencies_sha256'] == reference_replay['dependencies_sha256'])
    archive = 'repro/results/research-mixed-right-core-support-reference-replay.json'
    check('historical independent320 record archived byte-identically',
          dependencies[archive] == ARCHIVE_SHA)
    check('strict whole-cell reference gap preserved',
          all(F(r['strict_support_gap']) == F(1, 500)
              and interval(r['minimum_accepted_gap'])[0] > F(1, 500)
              for r in (reference, reference_replay)))

    high = rec('high_row_endpoint_reduction')
    high_replay = rec('high_row_endpoint_reduction', 'replay')
    check('upper-row domain includes the entire extracted rectangle',
          high['domain'] == {'y': ['13/100', '1/2'],
                            'absolute_height': ['0', '57/1000'],
                            'w': ['0', '1'], 'upper_rows': ['1/2', '1']})
    check('complete high-row author and independent replay retained',
          high['case_count'] == high_replay['case_count'] == 2
          and high['accepted_cells'] == high_replay['original_cells'] == 21301
          and input_binding('high_row_endpoint_reduction'))
    for case in high['cases']:
        assert len(exact_cover(case['addresses'])) == case['accepted_cells']
    check('both high-row types have exact complete partitions',
          {case['epsilon'] for case in high['cases']} == {0, 1})
    check('seven endpoint families plus remaining43 orientation complete',
          rec('all_endpoint_support')['reference_products'] == 112
          and rec('all_endpoint_support', 'replay')['reference_products'] == 112
          and rec('43_endpoint_support')['case_count'] == 16
          and input_binding('all_endpoint_support'))
    check('independent43 geometry binding current',
          rec('43_endpoint_support', 'replay')['geometry_input_sha256']
          == dependencies['repro/results/research-mixed-43-endpoint-support.json'])
    check('full physical endpoint bands contain extracted type4 bands',
          list(map(F, rec('43_endpoint_support')['unselected_target_heights']))
          == [F(-57, 1000), F(0)]
          and list(map(F, rec('43_endpoint_support')['selected_target_heights']))
          == [F(0), F(7, 500)])
    check('source rectangles require no small-angle move',
          F(13, 100) < F(2, 5) <= F(9, 20) < F(1, 2))
    check('one core tolerance leaves its original finite gap',
          F(1, 500)-F(1, 1000) == F(1, 1000) > F(1, 2000))
    check('endpoint comparisons already have enough finite reserve',
          F(rec('all_endpoint_support')['gap']) == F(1, 1000)
          and F(rec('43_endpoint_support')['gap']) == F(1, 1000)
          and F(1, 1000)-F(1, 2000) == F(1, 2000))
    check('all target heights fit the generic same-height reductions',
          max(F(3, 100), F(1, 50), F(57, 1000), F(7, 500)) == F(57, 1000))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in dependencies.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=primary, extracted_height_profiles=18,
        extracted_support_values=180, original_reference_products=512,
        original_reference_cells=5546, numerical_cells_recomputed=0,
        extracted_real_interval=['2/5', '1/2'],
        upper_transition_interval=['9/20', '1/2'],
        target_height_bands={'3': ['-3/100', '1/50'],
                            '4_unselected': ['-57/1000', '0'],
                            '4_selected': ['0', '7/500']},
        finite_source_gap='1/2000', source_sum='all original absolute rows',
        historical_reference_replay_sha256=ARCHIVE_SHA,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Extraction from existing complete profiles and current covers; both orientations, all permitted selections, all levels and parities. No new numerical run or mixed-region assembly.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact;', len(primary), 'primary;',
          len(dependencies), 'bindings; no numerical cover rerun')


if __name__ == '__main__':
    main()
