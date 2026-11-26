#!/usr/bin/env python3
"""Extract the twelve terminal-four alias gaps from completed saved bounds."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_four_alias_reserve.md'
AUTHOR = 'repro/results/research-mixed-terminal-four-source-stage4-attempt01.json'
REPLAY = 'repro/results/research-mixed-terminal-four-source-replay.json'
AUTHOR_SHA = 'e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3'
REPLAY_SHA = '3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79'
NUMBER = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
BALL = re.compile(r'\[('+NUMBER+r') \+/- ('+NUMBER+r')\]')
ALIASES = (
    [['t_alias', None, None, h, '0', '0', retain]
     for h in ('-3/25', '3/25') for retain in ('0', '1')]
    + [['e_alias', None, None, '0', h, retain, '0']
       for h in ('-11/200', '1/25') for retain in ('0', '1')]
    + [['double_alias', None, None, t, e, '0', '0']
       for t in ('-3/25', '3/25') for e in ('-11/200', '1/25')]
)
TIERS = ('first_stage', 'second_stage', 'third_stage', 'new')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), 'use a new output path'
    dependencies = {}

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest
        dependencies[name] = digest
        return digest

    bind(AUTHOR, AUTHOR_SHA)
    bind(REPLAY, REPLAY_SHA)
    bind(PROOF)
    bind(str(Path(__file__).resolve().relative_to(ROOT)))
    author, replay = [json.loads((ROOT/name).read_text()) for name in (AUTHOR, REPLAY)]
    assert replay['input_sha256'] == AUTHOR_SHA and replay['precision_bits'] == 320
    for record in (author, replay):
        assert record['status'] == 'passed' and record['active'] is None
        assert record['fatal_error'] is None and record['final_bindings_verified']
        assert record['original_own_four_cells'] == 1911
        assert record['face_families_per_cell'] == 21 and record['job_count'] == 40131
        assert len(record['family_inventory']) == 21
        assert record['family_inventory'][8:20] == ALIASES
        for name, digest in record['dependencies_sha256'].items():
            bind(name, digest)
        bind('notes/research_mixed_terminal_four_coupled_source_continuation.md', record['proof_sha256'])
        bind('experiments/continue_mixed_terminal_four_source_coupled.py', record['script_sha256'])
    assert author['completed'] == replay['completed']
    assert len(replay['completed']) == len(replay['replay_summaries']) == 40131
    assert all(replay[k] == 0 for k in ('additional_nodes', 'attempted_nodes',
                                      'root_proposals', 'target_proposals', 'refinements'))
    counts = [0]*12
    source_jobs = empty_jobs = source_leaves = 0
    worst = worst_job = None
    for job, (tree, summary) in enumerate(zip(replay['completed'], replay['replay_summaries'])):
        assert summary['job'] == job
        if not 8 <= job % 21 < 20:
            continue
        counts[job % 21-8] += 1
        assert len(tree) == summary['nodes']
        kinds = [node[0] for node in tree]
        assert all(kind in ('S', 'L', 'X', 'F') for kind in kinds)
        leaves = kinds.count('L')
        assert leaves == sum(summary[tier+'_leaves'] for tier in TIERS)
        assert kinds.count('X') == sum(summary[tier+'_exclusions'] for tier in TIERS)
        assert kinds.count('F') == summary['inverse_exclusions']
        assert leaves+kinds.count('X')+kinds.count('F') == kinds.count('S')+1
        source_leaves += leaves
        if not leaves:
            assert summary['maximum_upper'] is None
            assert kinds.count('X')+kinds.count('F') > 0
            empty_jobs += 1
            continue
        match = BALL.fullmatch(summary['maximum_upper'])
        assert match is not None, (job, summary['maximum_upper'])
        midpoint, radius = map(F, match.groups())
        assert radius >= 0
        upper = midpoint+radius
        assert upper < -F(1, 10), (job, str(upper))
        if worst is None or upper > worst:
            worst, worst_job = upper, job
        source_jobs += 1
    assert counts == [1911]*12
    assert (source_jobs, empty_jobs) == (21936, 996)
    assert worst is not None
    for name, digest in dependencies.items():
        assert sha(ROOT/name) == digest, name
    result = dict(status='passed', arithmetic='exact rational saved-ball upper decoding',
                  gap='1/10', alias_jobs=1911*12, family_counts=counts,
                  jobs_with_source_bounds=source_jobs, jobs_only_excluded=empty_jobs,
                  source_leaves=source_leaves, maximum_exact_upper=str(worst),
                  worst_job=worst_job, dependencies_sha256=dependencies,
                  new_roots=0, new_cells=0, source_evaluations=0,
                  final_bindings_verified=True,
                  scope='All twelve original bare aliases on the necessary actual-reference set.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', result['alias_jobs'], 'alias jobs; gap', result['gap'])


if __name__ == '__main__':
    main()
