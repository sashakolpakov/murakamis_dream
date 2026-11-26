#!/usr/bin/env python3
"""Decode all saved alias maxima with exact fractions; never import source code."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_terminal_three_alias_reserve.md'
AUTHOR = 'repro/results/research-mixed-terminal-three-aliases-attempt01.json'
REPLAY = 'repro/results/research-mixed-terminal-three-aliases-replay.json'
AUTHOR_SHA = 'fc04d56f297524fc252dd0e0f131db11000d7490ec77a3b5300811cebb8e41cf'
REPLAY_SHA = '3b2b017023020d8ea2dce6ff7e5a429f87a0871a339467a2f0734454af4523f5'
NUMBER = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
BALL = re.compile(r'\[('+NUMBER+r') \+/- ('+NUMBER+r')\]')
FLOOR = F(1, 10)
FAMILIES = [
    ['t','-3/25','0','0','0'], ['t','-3/25','0','0','1'],
    ['t','3/25','0','0','0'], ['t','3/25','0','0','1'],
    ['u','0','-3/25','0','0'], ['u','0','-3/25','1','0'],
    ['u','0','3/25','0','0'], ['u','0','3/25','1','0'],
    ['both','-3/25','-3/25','0','0'], ['both','-3/25','3/25','0','0'],
    ['both','3/25','-3/25','0','0'], ['both','3/25','3/25','0','0']]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert not args.output.exists()
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
    bind(str(PROOF.relative_to(ROOT)))
    bind(str(Path(__file__).resolve().relative_to(ROOT)))
    author, replay = [json.loads((ROOT/name).read_text()) for name in (AUTHOR, REPLAY)]
    assert replay['input_sha256'] == AUTHOR_SHA
    for record in (author, replay):
        assert record['status'] == 'passed' and record['active'] is None
        assert record['fatal_error'] is None and record['final_bindings_verified']
        assert record['original_own_three_cells'] == 3347
        assert record['face_families_per_cell'] == 12 and record['job_count'] == 40164
        assert record['family_inventory'] == FAMILIES
        for name, digest in record['dependencies_sha256'].items():
            bind(name, digest)
        bind('notes/research_mixed_terminal_three_alias_certificate.md', record['proof_sha256'])
        bind('experiments/certify_mixed_terminal_three_aliases.py', record['script_sha256'])
    assert author['completed'] == replay['completed']
    assert len(replay['completed']) == len(replay['replay_summaries']) == 40164
    assert replay['precision_bits'] == 320
    assert all(replay[k] == 0 for k in ('new_nodes', 'root_proposals', 'target_proposals', 'refinements'))
    worst, worst_job = None, None
    counts = [0]*12
    for job, (tree, summary) in enumerate(zip(replay['completed'], replay['replay_summaries'])):
        assert summary['job'] == job
        assert len(tree) == 1 and tree[0][0] == 'L' and len(tree[0]) == 2
        assert summary['leaves'] == 1 and summary['exclusions'] == 0
        match = BALL.fullmatch(summary['maximum_upper'])
        assert match is not None, (job, summary['maximum_upper'])
        midpoint, radius = map(F, match.groups())
        assert radius >= 0
        upper = midpoint+radius
        assert upper < -FLOOR, (job, str(upper))
        if worst is None or upper > worst:
            worst, worst_job = upper, job
        counts[job % 12] += 1
    assert counts == [3347]*12
    for name, digest in dependencies.items():
        assert sha(ROOT/name) == digest, name
    result = dict(status='passed', arithmetic='exact rational saved-ball upper decoding',
                  gap=str(FLOOR), jobs=40164, family_counts=counts,
                  maximum_exact_upper=str(worst), worst_job=worst_job,
                  dependencies_sha256=dependencies, new_roots=0, new_cells=0,
                  source_evaluations=0, final_bindings_verified=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', result['jobs'], 'saved bounds; gap', result['gap'])


if __name__ == '__main__':
    main()

