#!/usr/bin/env python3
"""Exact source-profile and incidence accounting on the hybrid L/P/R boxes."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_hybrid_low_plateau_right_clusters.md'

# Explicit complete theorem inputs. A record's inherited hashes are checked;
# a diagnostic record is not promoted to a theorem by appearing among them.
SPECS = [
    ('mixed_hybrid_zero_pair_support', 'certify', None, None),
    ('mixed_hybrid_zero_pair_support', 'certify', 'replay', None),
    ('mixed_all_endpoint_support', 'certify', None, None),
    ('mixed_all_endpoint_support', 'replay', 'replay', None),
    ('mixed_43_endpoint_support', 'check', None, None),
    ('mixed_43_endpoint_support', 'replay', 'replay', None),
    ('mixed_uniform_real_low_support', 'check', None, None),
    ('mixed_both_low_raw_support', 'certify', None, None),
    ('mixed_full_height_reset', 'certify', None, None),
    ('mixed_selected_plateau_support', 'certify', None, None),
    ('mixed_selected_reset_plateau_support', 'certify', None, None),
    ('mixed_selected_right_taper_support', 'certify', None, None),
    ('mixed_split_cutoff_hybrid_contour', 'check', None, None),
    ('mixed_selected_low_plateau_clusters', 'check', None, None),
    ('mixed_hybrid_low_plateau_clusters', 'check', None, None),
    ('mixed_right_core_support_grid', 'certify', None, 'mixed_right_core_support'),
    ('mixed_right_core_support_reference', 'certify', None, 'mixed_right_core_support'),
    ('mixed_right_half_source_reduction', 'check', None, None),
    ('mixed_small_angle_high_rows', 'certify', None, None),
    ('mixed_small_angle_high_rows', 'replay', 'replay', None),
    ('mixed_high_row_endpoint_reduction', 'certify', None, None),
    ('mixed_high_row_endpoint_reduction', 'replay', 'replay', None),
    ('mixed_geometric_support_slopes', 'certify', None, None),
    ('mixed_geometric_support_slopes', 'replay', 'replay', None),
    ('mixed_two_right_source_bound', 'certify', None, None),
    ('mixed_low_plateau_right_clusters', 'check', None, None),
    ('mixed_partially_reset_right_support', 'certify', None, None),
    ('mixed_partially_reset_right_support', 'certify', 'replay', None),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_cover(addresses):
    codes = sorted(addresses)
    assert codes and len(codes) == len(set(codes))
    assert all(set(code) <= {'0', '1'} for code in codes)
    assert all(not b.startswith(a) for a, b in zip(codes, codes[1:]))
    assert sum((F(1, 2**len(code)) for code in codes), F(0)) == 1
    return codes


def window_covers(record, length, external_key='external_types'):
    expected = set(itertools.product(itertools.product((0, 1), repeat=length),
                                     range(2), range(2), range(4), range(4)))
    out = {}
    for row in record['cases']:
        key = (tuple(row['word']), *row[external_key], *row['faces'])
        assert key not in out
        codes = exact_cover(row['addresses'])
        assert row.get('cells', len(codes)) == len(codes)
        out[key] = codes
    assert set(out) == expected
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT / 'repro/results/research-mixed-hybrid-low-plateau-right-clusters.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, records, bindings = {}, {}, []

    def bind(path, expected=None):
        digest = sha(ROOT / path)
        if expected is not None:
            assert digest == expected, path
        if path in deps:
            assert deps[path] == digest, path
        deps[path] = digest
        return digest

    for stem, prefix, suffix, proof_stem in SPECS:
        pp = f'notes/research_{proof_stem or stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rr = 'repro/results/research-' + stem.replace('_', '-')
        rr += ('-' + suffix if suffix else '') + '.json'
        for path in (pp, ss, rr):
            bind(path)
        record = json.loads((ROOT / rr).read_text())
        assert record['status'] == 'passed', rr
        assert record['script_sha256'] == deps[ss], rr
        inherited = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for path, digest in record.get(field, {}).items():
                if path in inherited:
                    assert inherited[path] == digest, (rr, path)
                inherited[path] = digest
                bind(path, digest)
        assert record.get('proof_sha256', inherited.get(pp)) == deps[pp], rr
        records[stem, suffix] = record
        bindings.append(dict(record=rr, proof=pp, script=ss))

    checks = []

    def check(name, claim):
        assert claim, name
        checks.append(name)

    def rec(stem, suffix=None):
        return records['mixed_' + stem, suffix]

    def replay_binding(stem):
        path = 'repro/results/research-mixed-' + stem.replace('_', '-') + '.json'
        return rec(stem, 'replay')['input_sha256'] == deps[path]

    check('all 28 complete primary inputs present', len(records) == len(SPECS) == 28)
    check('inherited hybrid L/P inputs all explicitly retained',
          set(row['record'] for row in rec('hybrid_low_plateau_clusters')['primary_records'])
          <= set(row['record'] for row in bindings))
    pair, pair_replay = rec('hybrid_zero_pair_support'), rec('hybrid_zero_pair_support', 'replay')
    check('same complete seam-pair covers and final replay binding',
          window_covers(pair, 5) == window_covers(pair_replay, 5)
          and replay_binding('hybrid_zero_pair_support'))
    check('literal seam-pair source loss and fixed collar',
          pair['boundary_products'] == pair_replay['boundary_products'] == 2048
          and pair['accepted_cells'] == pair_replay['accepted_cells'] == 18988
          and F(pair['finite_pair_gap']) == F(pair_replay['finite_pair_gap']) == F(1, 5)
          and F(pair['low_cutoff']) == F(1, 1000))
    check('all seven endpoint orientations and eighth orientation retained',
          rec('all_endpoint_support')['reference_products']
          == rec('all_endpoint_support', 'replay')['reference_products'] == 112
          and rec('43_endpoint_support')['case_count'] == 16)
    check('deep-low plateau and closed both-low gaps',
          F(rec('uniform_real_low_support')['uniform_source_gap']) == F(1, 20)
          and F(rec('both_low_raw_support')['gap']) == F(1, 100)
          and F(rec('both_low_raw_support')['target_real_cutoff']) == F(1, 10))

    # Read the literal saved h=0 profiles, rather than extending an old graph
    # theorem to heights outside its stated graph. Type-three h=0 is convex.
    grid = rec('right_core_support_grid')
    source_keys = {(0, 0, 0), (1, 1, 0), (0, 0, 1),
                   (0, 1, 1), (1, 0, 1), (1, 1, 1)}
    slope_grid = [F(-1, 5) + F(j, 20) for j in range(10)]
    check('six complete source orientations and all slope intervals',
          {(p['e'], p['b'], p['c']) for p in grid['profiles']} == source_keys
          and [F(x) for x in grid['slope_grid']] == slope_grid
          and grid['source_profiles'] == len(grid['profiles']) == 75
          and grid['support_values'] == 750)
    profile_keys = set()
    for p in grid['profiles']:
        key = (p['e'], p['b'], p['c'], p['sig'], F(p['h']),
               F(p['ylo']), F(p['yhi']), p['name'])
        assert key not in profile_keys
        profile_keys.add(key)
        assert [F(v['k']) for v in p['grid']] == slope_grid
        assert all(v['trials'] and v['endpoint_trials'] for v in p['grid'])
    for e, beta, orientation in sorted(source_keys):
        if beta:
            for selected in (0, 1):
                check(f'literal type-four zero-height degenerate profile {e}{orientation}{selected}',
                      (e, beta, orientation, selected, F(0), F(13, 100), F(13, 100), 'small')
                      in profile_keys)
        else:
            check(f'type-three full-height profile includes zero {e}{orientation}',
                  all((e, beta, orientation, 0, h, F(13, 100), F(1, 2), 'all3')
                      in profile_keys for h in (F(-3, 100), F(1, 50))))
    check('zero-height type-three convex interpolation',
          F(2, 5)*F(-3, 100) + F(3, 5)*F(1, 50) == 0)
    core = rec('right_core_support_reference')
    check('all original reference products supporting zero-height profiles',
          len(window_covers(core, 3, 'external')) == core['boundary_products'] == 512
          and sum(len(r['addresses']) for r in core['cases']) == core['accepted_cells'] == 5546
          and F(core['strict_support_gap']) == F(1, 500)
          and F(core['finite_partial_source_gap']) == F(1, 1000))
    check('complete small-angle upper-row cover and current alternate replay',
          len(exact_cover(rec('small_angle_high_rows')['addresses'])) == 1392
          and len(exact_cover(rec('small_angle_high_rows', 'replay')['addresses'])) == 2557
          and replay_binding('small_angle_high_rows'))
    check('zero is an allowed same-height small-angle reduction',
          F(0) <= F(3, 100) and F(1, 10) < F(13, 100))
    check('complete angular candidate and small-angle lower-row reductions bound',
          rec('right_half_source_reduction')['exact_identities'] == 22)
    check('both-high-row endpoint source cases remain current',
          rec('high_row_endpoint_reduction')['case_count'] == 2
          and {row['epsilon'] for row in rec('high_row_endpoint_reduction')['cases']} == {0, 1}
          and sum(len(exact_cover(row['addresses']))
                  for row in rec('high_row_endpoint_reduction')['cases']) == 21301
          and replay_binding('high_row_endpoint_reduction'))
    check('core stronger than retained real-low/right finite loss', F(1, 1000) > F(1, 2000))

    partial, partial_replay = rec('partially_reset_right_support'), rec('partially_reset_right_support', 'replay')
    check('same complete new partial-reset right source covers',
          window_covers(partial, 3) == window_covers(partial_replay, 3)
          and replay_binding('partially_reset_right_support')
          and partial['reference_products'] == partial_replay['reference_products'] == 512
          and sum(len(r['addresses']) for r in partial['cases'])
          == partial['reference_cells'] == partial_replay['reference_cells'] == 5064)
    expected_grid = {(e, 1, k) for e in (0, 1) for k in slope_grid}

    def grid_points(record):
        out = {}
        for row in record['source_grid']:
            key = (row['own_type'], row['moving_type'], F(row['kappa']))
            assert key not in out
            point = tuple(F(x) for x in row['point'])
            endpoint = F(row['endpoint_point'])
            assert F(1, 5) <= point[0] <= F(1, 2)
            assert F(11, 50) <= point[1] <= F(9, 20)
            assert F(11, 50) <= endpoint <= F(9, 20)
            out[key] = (point, endpoint)
        assert set(out) == expected_grid
        return out

    check('all twenty rational zero-height source tangent proposals retained',
          grid_points(partial) == grid_points(partial_replay)
          and partial['source_values'] == partial_replay['source_values'] == 20)
    check('partial-reset finite ceiling and plateau domain',
          F(partial['strict_core_ceiling']) == F(1, 200)
          and F(partial['finite_source_ceiling']) == F(partial_replay['finite_source_ceiling']) == F(1, 100)
          and [F(x) for x in partial['moving_real_interval']] == [F(11, 50), F(9, 20)])
    check('all-real right/right finite loss',
          F(rec('two_right_source_bound')['finite_source_gap']) == F(1, 100)
          and len(window_covers(rec('two_right_source_bound'), 3)) == 512)
    check('common partial-height plateau ceiling and selected corners',
          rec('full_height_reset')['integrated_cost_upper'] == 10
          and F(rec('selected_right_taper_support')['target_concavity']) == F(5, 4)
          and F(rec('selected_plateau_support')['reference_defect_upper']) == -F(1, 100)
          and F(rec('selected_reset_plateau_support')['phase_gap']) == F(1, 100))
    check('old pointwise right-box and pure-selected plateau gaps',
          F(rec('selected_right_taper_support')['finite_block_gap']) == F(1, 2000)
          and F(rec('selected_low_plateau_clusters')['selected_plateau_gap']) == F(1, 200))

    # These local identities support the arbitrary-length written injection.
    # No finite list of cyclic words is used to assert the general theorem.
    for k in (1, 2):
        check(f'fractional source allocation for {k} seam incidences',
              F(k, 2)+(1-F(k, 2)) == 1 and 0 <= 1-F(k, 2) <= F(1, 2))
        check(f'one distinct low incidence for each remaining P incidence at k={k}',
              0 <= 2-k <= k)
    check('one-cycle seam pair counted twice before half-weight', F(2)*F(1, 2) == 1)
    check('two-cycle mixed plateau vertex has no third incidence', 2-2 == 0)
    debit = F(10)*F(57, 1000)**2
    seam, deep = F(1, 10)-2*debit, F(1, 20)-debit
    check('exact per-endpoint ceiling includes an entire affected PR edge',
          debit == F(3249, 100000) > F(1, 100))
    check('exact seam and deep-low plateau coefficients',
          seam == F(1751, 50000) and deep == F(1751, 100000))
    check('each larger-loss alternative exceeds one thousandth',
          min(seam, deep, F(1, 100)) > F(1, 1000))
    check('remaining cyclic deep-low vertex has two distinct right incidences',
          F(2)*F(1, 2000) == F(1, 1000))
    check('one total PP tolerance leaves the claimed finite loss',
          F(1, 1000)-F(1, 2000) == F(1, 2000))
    check('old pointwise right-box tolerance can be used on the restricted boxes',
          F(1, 80000)-F(1, 160000) == F(1, 160000)
          and min(F(1, 2000), F(1, 160000)) == F(1, 160000))
    for eta, eps in itertools.product((0, 1), repeat=2):
        check(f'original allocated kernel level power {eta}{eps}',
              -F(1+eps, 2)-F(eta+eps, 4) == -F(2+eta+3*eps, 4))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / path) == digest for path, digest in deps.items())
    result = dict(status='passed', arithmetic='exact rational source-profile and incidence assembly',
                  exact_checks=len(checks), checks=checks, primary_record_count=len(SPECS),
                  primary_records=bindings, zero_height_source_orientations=6,
                  partial_right_source_values=20, partial_right_products=512,
                  partial_right_saved_cells=5064, cycle_pattern_enumerations=0,
                  new_numerical_inequalities=0, incidence_debit=str(debit),
                  seam_coefficient=str(seam), deep_low_plateau_coefficient=str(deep),
                  real_low_right_finite_gap='1/2000', pre_tolerance_low_reserve='1/1000',
                  finite_low_region_gap='1/2000', restricted_region_error_gap='1/160000',
                  collar_scope='Fixed positive epsilon <=1/1000 below the uniform endpoint-thickening radius, independent of N; no numerical radius asserted.',
                  source_scope='Original complete finite source, all selections, both parities, zero-uniform; h=0 right profiles are checked literally.',
                  proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                  scope='Periodic hybrid on (L union P union R)^m, L=[0,.1], P=[.22,.45], R=[.5,1]. No open transitions or full-period asymptotic.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(SPECS), 'primary records;', len(deps), 'current bindings', flush=True)


if __name__ == '__main__':
    main()
