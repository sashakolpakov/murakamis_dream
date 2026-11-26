#!/usr/bin/env python3
"""Extract uniform real-face reserves from immutable source certificates.

Four canonical image rectangles, nine source families each. Only exact
rational arithmetic, existing summaries and the original endpoint partition.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_uniform_face_reserves.md'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
REFINED_PROOF = 'notes/research_mixed_terminal_quadratic_residual_refinement.md'
REFINED_CHECKER = 'experiments/check_mixed_terminal_quadratic_residual_refinement.py'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
OLD = 'repro/results/research-mixed-terminal-canonical-face-reserve.json'
OLD_PROOF = 'notes/research_mixed_terminal_canonical_face_reserve.md'
HELPER = 'experiments/check_mixed_terminal_canonical_face_reserve.py'
PINNED = {
    PROOF: 'b770a8d3c182c9936367c1f43edd2e74f483ffd5ead2d61fa44b85420109a363',
    REFINED: '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    REFINED_PROOF: 'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    REFINED_CHECKER: '251fc4b3c656201ab5451287577baddb4d4be8122ff34a1318078de0f8501a05',
    POSTERIOR: 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    OLD: 'c85ef62dd25724f6bed335dc16982c2133e4f991a5badcd68e038a57b1a513aa',
    OLD_PROOF: '45d3def413d15478b3fe968409f98b3730f686a9124195b1e718b5afe027ed8e',
    HELPER: '4cbeda03dfee69565262e5e25486d261f97e6cbc417934e7ed417f19d75cce04',
}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def interval(value):
    if 'finite' in value:
        assert value['finite'] is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def encoded(box):
    return [[str(lo), str(hi)] for lo, hi in box]


def forbidden(*args, **kwargs):
    raise AssertionError('original extraction main must not be called')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    result = dict(status='initializing', proof_path=PROOF, proof_sha256=inputs[PROOF],
        checker_path=own, checker_sha256=inputs[own], source_path=REFINED,
        source_sha256=inputs[REFINED], inherited_all_job_audit_path=OLD,
        inherited_all_job_audit_sha256=inputs[OLD], input_sha256=inputs, cases=[],
        counts=dict(canonical_families=0, required_face_families=0, selected_job_reads=0,
            inherited_checked_jobs=0, new_parameter_cells=0, root_or_source_replays=0,
            analytic_evaluations=0, subdivisions=0, retries=0),
        all_uniform_bare_bounds_defined=False, uniform_joined_bound_proved=False,
        whole_finite_source_proved=False, knot_theorem_proved=False)
    error = None
    try:
        def bind(name, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest

        def inherited(data):
            for key in ('input_sha256', 'dependencies_sha256', 'dependencies'):
                values = data.get(key)
                if isinstance(values, dict):
                    for name, digest in values.items():
                        bind(name, digest)

        for name, digest in list(inputs.items()):
            bind(name, digest)
        old, refined, posterior = [json.loads((ROOT/p).read_text())
                                  for p in (OLD, REFINED, POSTERIOR)]
        for data in (old, refined, posterior):
            assert data['changed_inputs'] == []
            inherited(data)
        assert old['status'] == 'completed saved-only extraction'
        assert old['proof_sha256'] == inputs[OLD_PROOF]
        assert old['checker_sha256'] == inputs[HELPER]
        assert old['canonical_reference_cases_checked'] == 4
        assert old['required_family_cases_checked'] == 36
        assert old['analytic_evaluations'] == old['root_or_source_replays'] == 0
        assert refined['status'] == 'completed fixed saved-only protocol'
        assert refined['proof_sha256'] == inputs[REFINED_PROOF]
        assert refined['checker_sha256'] == inputs[REFINED_CHECKER]
        assert refined['source_path'] == POSTERIOR
        assert refined['source_sha256'] == inputs[POSTERIOR]
        expected_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]
        assert [(c['beta'], c['epsilon']) for c in refined['cases']] == expected_cases
        assert [(c['beta'], c['epsilon']) for c in posterior['posterior_enclosures']] == expected_cases

        # The pinned helper has standard-library imports and definitions only.
        # Reuse its exact partition decoder, never its old execution routine.
        spec = importlib.util.spec_from_file_location('frozen_canonical_face_reader', ROOT/HELPER)
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        helper.main = forbidden
        for name, digest in helper.PINNED.items():
            bind(name, digest)
        roots, replay = [json.loads((ROOT/p).read_text())
                         for p in (helper.ROOT_AUTHOR, helper.ROOT_REPLAY)]
        cells, excluded, partition = helper.root_cells(roots, replay)
        assert partition == old['original_partition']
        result['original_partition'] = partition

        # The old immutable audit checked every source tree. Read only saved
        # summaries here; a new numerical source or tree replay is forbidden.
        summaries = {}
        expected_job_counts = {'three_mixed': 26776, 'three_half': 3347, 'four': 40131}
        for key, series in helper.SERIES.items():
            audit_row = old['source_summary_counts'][key]
            jobs = series['cells']*series['families']
            assert jobs == expected_job_counts[key] == audit_row['all_jobs_checked']
            assert audit_row['family_count'] == series['families']
            assert audit_row['original_cell_count'] == series['cells']
            assert audit_row['finite_jobs']+audit_row['null_jobs'] == jobs
            saved = json.loads((ROOT/series['replay']).read_text())
            assert saved['status'] == 'passed' and saved['active'] is None
            assert saved['fatal_error'] is None and saved['final_bindings_verified'] is True
            assert saved['input_sha256'] == inputs[series['author']]
            assert saved['proof_sha256'] == inputs[series['proof']]
            assert saved['script_sha256'] == inputs[series['script']]
            assert saved['job_count'] == jobs and saved['face_families_per_cell'] == series['families']
            assert saved['precision_bits'] == 320
            summaries[key] = saved['replay_summaries']
            assert len(summaries[key]) == jobs
            assert all(s['job'] == i for i, s in enumerate(summaries[key]))
            assert sum(s['maximum_upper'] is None for s in summaries[key]) == audit_row['null_jobs']
            result['counts']['inherited_checked_jobs'] += jobs
        assert result['counts']['inherited_checked_jobs'] == 70254

        for index, (row, prior) in enumerate(zip(refined['cases'], posterior['posterior_enclosures'])):
            beta, eps = expected_cases[index]
            assert row['source_posterior_canonical_sha256'] == canonical_sha(prior)
            assert row['exact_linear_system_verified'] is True
            for key in ('center_exact', 'response_exact', 'parameter_center', 'parameter_radius_rational'):
                assert row[key] == prior[key]
            assert tuple(map(F, row['parameter_center'])) == helper.DISKS[beta][:2]
            assert F(row['parameter_radius_rational']) == helper.DISKS[beta][2]
            assert len(row['posterior_radii_rational']) == len(prior['posterior_radii_rational']) == 5
            assert all(0 <= F(a) <= F(b) for a, b in
                       zip(row['posterior_radii_rational'], prior['posterior_radii_rational']))
            q = row['coordinate_enclosures']
            abox = (interval(q['a']['real']), interval(q['a']['imag']))
            assert all(lo < hi for lo, hi in abox)
            assert F('.22') < abox[0][0] <= abox[0][1] < F('.45')
            assert -F('.108') < abox[1][0] <= abox[1][1] < -F('.001')
            if eps == 1:
                assert abox[0][0] > F('.259')
                assert helper.rectangle_in_disk(abox, helper.DISKS[1][:2], F('.060'))
            cr, ci, radius = helper.DISKS[1]
            normalized = (((abox[0][0]-cr)/radius, (abox[0][1]-cr)/radius),
                          ((abox[1][0]-ci)/radius, (abox[1][1]-ci)/radius))
            max_square = sum(max(lo*lo, hi*hi) for lo, hi in normalized)
            assert max_square < 1
            assert all(helper.intersect(abox, box) is None for box in excluded[eps])
            selected = [c for c in cells[eps] if c['neighbor'] == 1
                        and helper.intersect(abox, c['physical']) is not None]
            assert selected
            pieces = [helper.intersect(abox, c['physical']) for c in selected]
            assert sum(map(helper.area, pieces)) == helper.area(abox)
            case = dict(beta=beta, epsilon=eps, endpoint_neighbor_epsilon=1,
                refinement_case_canonical_sha256=canonical_sha(row),
                source_posterior_canonical_sha256=canonical_sha(prior),
                parameter_center=row['parameter_center'], parameter_radius_rational=row['parameter_radius_rational'],
                physical_a_box_rational=encoded(abox), normalized_a_box_rational=encoded(normalized),
                maximum_normalized_radius_squared=str(max_square),
                covered_area_rational=str(sum(map(helper.area, pieces))),
                enclosure_area_rational=str(helper.area(abox)),
                source_scope=('original endpoint source on the full canonical disk' if eps == 0 else
                              'canonical parameters satisfying original oriented and inverse-feasible source conditions'),
                all_auxiliary_parameters_source_feasible_claimed=(eps == 0),
                independent_image_rectangle_source_feasible_claimed=False,
                intersecting_original_cells=[], families=[])
            result['cases'].append(case)
            result['counts']['canonical_families'] += 1
            for cell, piece in zip(selected, pieces):
                case['intersecting_original_cells'].append(dict(
                    **{k: cell[k] for k in ('index', 'domain', 'node', 'neighbor', 'address',
                                           'depth', 'original_node_canonical_sha256')},
                    normalized_box=encoded(cell['box']), physical_box=encoded(cell['physical']),
                    intersection=encoded(piece)))
            requests = ([('three_mixed', f) for f in range(8)]+[('three_half', 0)] if eps == 0
                        else [('four', f) for f in range(8)]+[('four', 20)])
            for key, family in requests:
                contributing, nulls = [], []
                for cell in selected:
                    job = helper.SERIES[key]['families']*cell['index']+family
                    summary = summaries[key][job]
                    assert summary['job'] == job
                    raw = summary['maximum_upper']
                    value = None if raw is None else helper.outward_saved_upper(raw)
                    assert value is None or value < 0
                    contributing.append(dict(job=job, original_cell_index=cell['index'],
                        summary_canonical_sha256=canonical_sha(summary), saved_maximum_upper=raw,
                        decoded_upper_rational=None if value is None else str(value)))
                    if value is None:
                        nulls.append(job)
                    result['counts']['selected_job_reads'] += 1
                finite = [F(c['decoded_upper_rational']) for c in contributing
                          if c['decoded_upper_rational'] is not None]
                observed = max(finite) if finite else None
                complete = not nulls and observed is not None
                case['families'].append(dict(series=key, family=family,
                    contributing_jobs=contributing, null_jobs_unresolved=nulls,
                    complete_finite_coverage=complete,
                    observed_finite_maximum_rational=None if observed is None else str(observed),
                    uniform_bare_upper_rational=str(observed) if complete else None,
                    attaining_jobs=[] if observed is None else [c['job'] for c in contributing
                        if c['decoded_upper_rational'] is not None and F(c['decoded_upper_rational']) == observed],
                    reserve_rational=str(-observed) if complete else None,
                    exceeds_old_reserve_11over200=complete and observed < -F(11, 200)))
                result['counts']['required_face_families'] += 1
            case['all_nine_uniform_bare_bounds_defined'] = all(f['complete_finite_coverage'] for f in case['families'])
        assert result['counts']['canonical_families'] == 4
        assert result['counts']['required_face_families'] == 36
        result['all_uniform_bare_bounds_defined'] = all(c['all_nine_uniform_bare_bounds_defined'] for c in result['cases'])
        result['unresolved_family_cases'] = sum(not f['complete_finite_coverage'] for c in result['cases'] for f in c['families'])
        result['status'] = 'completed fixed saved-only extraction'
    except Exception as exc:
        error = exc
        result['status'] = 'failed saved-data extraction'
        result['error'] = dict(type=type(exc).__name__, message=str(exc))
    result['changed_inputs'] = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    if result['changed_inputs']:
        result['status'] = 'changed inputs'
        result['all_uniform_bare_bounds_defined'] = False
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps(dict(status=result['status'], counts=result['counts'],
        all_uniform_bare_bounds_defined=result['all_uniform_bare_bounds_defined'],
        output_sha256=sha(args.output))))
    if error is not None:
        raise error


if __name__ == '__main__':
    main()
