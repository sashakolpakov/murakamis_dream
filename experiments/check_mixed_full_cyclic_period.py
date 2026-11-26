#!/usr/bin/env python3
"""Check exact assembly budgets and current sources of the full cyclic theorem.

This is a dependency and exact-arithmetic check. It does not replace the
written contour proofs or replay their numerical parameter covers.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_full_cyclic_period.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path, default=ROOT /
                        'repro/results/research-mixed-full-cyclic-period.json')
    args = parser.parse_args()
    proof_sha, script_sha = sha(PROOF), sha(__file__)
    dependencies, records, primary, checks = {}, {}, {}, []

    def bind(name, expected=None):
        digest = sha(ROOT / name)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest, name
        dependencies[name] = digest
        return digest

    def inherit(name):
        if name in records:
            return records[name]
        bind(name)
        record = json.loads((ROOT / name).read_text())
        records[name] = record
        merged = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for path, digest in record.get(field, {}).items():
                assert path not in merged or merged[path] == digest, path
                merged[path] = digest
                bind(path, digest)
        for path in merged:
            if path.startswith('repro/results/') and path.endswith('.json'):
                inherit(path)
        return record

    names = (
        'mixed_closed_half_period',
        'mixed_nonlow_middle_transport',
        'mixed_seam_raw_exterior_repair',
        'mixed_central_outer_integral',
        'mixed_extracted_plateau_curvature',
        'mixed_split_cutoff_hybrid_contour',
        'mixed_local_outer_contribution',
        'mixed_conditional_torus_composition',
    )
    for stem in names:
        path = 'repro/results/research-' + stem.replace('_', '-') + '.json'
        rec = inherit(path)
        assert rec['status'] == 'passed', path
        note = f'notes/research_{stem}.md'
        script = f'experiments/check_{stem}.py'
        # Older records store their proof binding in the dependency map.
        expected = rec.get('proof_sha256', dependencies.get(note))
        assert expected is not None, (stem, 'missing historical proof binding')
        bind(note, expected)
        bind(script, rec['script_sha256'])
        primary[stem] = rec

    replay_names = []
    for stem in ('mixed_closed_half_period', 'mixed_nonlow_middle_transport',
                 'mixed_seam_raw_exterior_repair'):
        base = 'repro/results/research-' + stem.replace('_', '-')
        replay_path = base + '-replay.json'
        replay = inherit(replay_path)
        author = primary[stem]
        assert replay['status'] == 'passed', replay_path
        assert replay['input_sha256'] == dependencies[base + '.json'], replay_path
        for key in ('proof_sha256', 'script_sha256'):
            assert replay[key] == author[key], (replay_path, key)
        replay_names.append(replay_path)

    def check(name, condition):
        assert condition, name
        checks.append(name)

    half = primary['mixed_closed_half_period']
    middle = primary['mixed_nonlow_middle_transport']
    seam = primary['mixed_seam_raw_exterior_repair']
    curvature = primary['mixed_extracted_plateau_curvature']
    check('closed half includes the original zero collar and all selections',
          half['closed_half_remainder_loss'] == '1/8000'
          and half['singleton_phase_reserve'] == '3/1000')
    check('nonlow right-region rate is before the finite tolerance',
          middle['nonlow_phase_loss'] == '1/1000'
          and middle['nonlow_finite_loss'] == '1/2000')
    check('seam reduction leaves the ordinary nonlow envelope',
          seam['seam_phase_loss_per_vertex'] == '3/1000'
          and seam['global_nonlow_bound_asserted'] is False)
    check('repaired point retains a right label and pays one finite tolerance',
          F(1,1000) + F(3,1000) - F(1,2000) > F(1,2000))
    check('all longer seam runs improve the same loss', F(3,1000) > 0)
    check('one finite tolerance preserves nonseam right-region loss',
          F(1,1000) - F(1,2000) == F(1,2000))
    check('full-period remainder inherits the smaller half-period loss',
          min(F(1,8000), F(1,2000)) == F(1,8000))

    # This four-case partition concerns coordinate labels, not a test of
    # finitely many cyclic words in place of the arbitrary-length proof.
    region_partition = []
    for has_right in (False, True):
        for has_seam in (False, True):
            route = ('closed_half' if not has_right else
                     'seam_repair_then_nonlow' if has_seam else 'nonlow')
            region_partition.append(dict(has_right=has_right,
                                         has_seam=has_seam, route=route))
    check('each region has exactly one assigned estimate',
          len(region_partition) == 4
          and sum(x['route'] == 'closed_half' for x in region_partition) == 2
          and sum(x['route'] == 'nonlow' for x in region_partition) == 1
          and sum(x['route'] == 'seam_repair_then_nonlow'
                  for x in region_partition) == 1)

    check('original plateau has the stated cyclic Hessian',
          curvature['cyclic_hessian_lower'] == '2/5'
          and curvature['local_taylor_coefficient'] == '1/10')
    left_distance = F(27,100)-F(1,4)
    right_distance = F(2,5)-F(39,100)
    check('central cube contains every actual critical real coordinate',
          left_distance > 0 and right_distance > 0)
    check('distance from central cube complement has explicit floor',
          min(left_distance, right_distance) == F(1,100))
    phase_gap = F(2,5) / 2 * min(left_distance, right_distance)**2
    check('plateau-to-central phase loss', phase_gap == F(1,50000))
    check('one tolerance pays the plateau-to-central finite loss',
          phase_gap-F(1,100000) == F(1,100000))
    check('full outer complement has explicit absolute loss',
          min(F(1,8000), F(1,100000)) == F(1,100000))
    check('hybrid graph has bounded level-independent Jacobian',
          primary['mixed_split_cutoff_hybrid_contour'][
              'example_jacobian_base_upper'] == 60)
    check('central source retains the original Gaussian normalization',
          primary['mixed_local_outer_contribution'][
              'exact_power_identity_count'] == 3
          and primary['mixed_central_outer_integral'][
              'strict_inequality_groups'] == 5)
    # Coefficients of m and k in the level powers, before and after
    # the outer Gaussian. All constants are independent of those integers.
    check('inner sums and outer factorials leave level power m/2',
          F(1)-F(1,2) == F(1,2)
          and F(1)-F(1,2)-F(1,2) == 0)
    check('outer Gaussian leaves cyclic level power zero',
          F(1,2)-F(1,2) == 0)
    check('inner and outer Gaussian constants give (2pi)^m',
          F(1,2)+F(1,2) == 1)

    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(primary), saved_replays=replay_names,
        region_partition=region_partition, current_bindings=len(dependencies),
        right_region_finite_loss='1/2000', plateau_remainder_loss='1/8000',
        central_cube_remainder_loss='1/100000', cyclic_level_power='0',
        numerical_cells_recomputed=0, cyclic_word_enumerations=0,
        proof_sha256=proof_sha, script_sha256=script_sha,
        dependencies_sha256=dependencies,
        scope='Complete original cyclic trace for every fixed word in 3 and 4, '
              'with nonzero original Gaussian coefficient at both parities. '
              'No open-tangle or arbitrary short partial-filling theorem.')
    input_sha = None
    if args.input:
        raw = args.input.read_bytes()
        input_sha = hashlib.sha256(raw).hexdigest()
        old = json.loads(raw)
        for key, value in result.items():
            assert old[key] == value, key
        result['input_sha256'] = input_sha
    assert sha(PROOF) == proof_sha and sha(__file__) == script_sha
    assert all(sha(ROOT/path) == digest for path, digest in dependencies.items())
    if input_sha:
        assert sha(args.input) == input_sha
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(primary), 'primary;',
          len(dependencies), 'bindings; no numerical recomputation', flush=True)


if __name__ == '__main__':
    main()
