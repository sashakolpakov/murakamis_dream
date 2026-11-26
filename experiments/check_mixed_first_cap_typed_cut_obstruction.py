#!/usr/bin/env python3
"""Sole higher-precision replay of two pinned original-root cut deficits."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx
import certify_mixed_first_cap_typed_plateau as cap

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_first_cap_typed_cut_obstruction.md'
DIAGNOSTIC = 'repro/results/research-mixed-first-cap-typed-cut-fixed-points.json'
FAILED = 'repro/results/research-mixed-first-cap-typed-plateau-attempt01.json'
HELPER = 'experiments/certify_mixed_first_cap_typed_plateau.py'
PINS = {
    DIAGNOSTIC: 'ec11312d8c33044ab006658af7a9d707332f893931c15031bcaf359214dc553a',
    FAILED: 'd1321329fde521bd4100bd9d6195306acaf257cad6dac9eb9d0bc610abd1015f',
    HELPER: 'c0be1949e217444ee4e7365300cde87744ce7a8f15b5594d768695b0afcf8ffc',
    cap.ROOT_AUTHOR: 'ac2991d4cd5b7a78d202a237efebf98a9ad7ab77b6bacc4ab82568b8aa3cdad5',
    cap.ROOT_REPLAY: '2b5d91f8fbfa860d978f7b2076270b33bbe40d7410d39e91c9733e41b03ec247',
}
POINTS = [[F(-15359, 16384), F(0)], [F(-15359, 16384), F(1, 1024)]]
TARGET = ['372948142107/1000000000000']
FLOORS = [F(1, 200000), F(1, 1000000)]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=320)
    parser.add_argument('--input', type=Path, default=ROOT/DIAGNOSTIC)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert args.precision >= 320 and not args.output.exists()
    assert args.input.resolve() == (ROOT/DIAGNOSTIC).resolve()
    assert args.input.resolve() != args.output.resolve()
    input_hash = sha(args.input)
    assert input_hash == PINS[DIAGNOSTIC]
    ctx.prec = args.precision
    cap.PI, cap.II = arb.pi(), acb(0, 1)
    cap.primitive.PI, cap.primitive.II = cap.PI, cap.II
    cap.old.propose = cap.original_root_proposals_forbidden
    cap.propose_targets = cap.target_proposals_forbidden
    proof_hash, script_hash = sha(ROOT/PROOF), sha(__file__)
    dependencies, records = {}, {}

    def bind(name, expected=None):
        path = Path(name)
        path = path if path.is_absolute() else ROOT/path
        name = str(path.resolve().relative_to(ROOT))
        digest = sha(path)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest
        dependencies[name] = digest
        return digest

    def inherit(name):
        bind(name, PINS.get(name))
        if name in records:
            return records[name]
        record = json.loads((ROOT/name).read_text())
        records[name] = record
        for key in ('dependencies_sha256', 'dependencies'):
            for path, digest in record.get(key, {}).items():
                bind(path, digest)
                normalized = str(Path(path).resolve().relative_to(ROOT)) if Path(path).is_absolute() else path
                if normalized.startswith('repro/results/') and normalized.endswith('.json'):
                    inherit(normalized)
        return record

    for name, digest in PINS.items():
        bind(name, digest)
    diagnostic, failed = inherit(DIAGNOSTIC), inherit(FAILED)
    roots, replay = inherit(cap.ROOT_AUTHOR), inherit(cap.ROOT_REPLAY)
    assert roots['status'] == replay['status'] == 'passed'
    assert replay['input_sha256'] == dependencies[cap.ROOT_AUTHOR]
    assert roots['domains'] == replay['domains']
    for record in (roots, replay):
        bind('notes/research_mixed_open_word_critical_localization.md', record['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py', record['script_sha256'])
    assert failed['status'] == 'incomplete' and failed['fatal_error'] is None
    assert failed['script_sha256'] == dependencies[HELPER]
    bind('notes/research_mixed_first_cap_typed_plateau_certificate.md', failed['proof_sha256'])
    assert failed['active']['job'] == diagnostic['source_job'] == 19732
    assert failed['active']['failure']['targets'] == TARGET
    assert diagnostic['original_cell'] == 4933
    cell = cap.original_cells(roots)[4933]
    assert cell['own'] == cell['neighbor'] == 1
    expected_box = [(F(-15, 16), F(-29, 32)), (F(0), F(1, 16))]
    assert cell['box'] == expected_box
    assert diagnostic['source_box'] == cap.encoded_box(expected_box)
    assert cap.FACES[19732 % 4] == ('cut', F(27, 100), F(0))
    inputs = [dict(normalized_point=list(map(str, point)), target=TARGET,
                   strict_floor=str(floor)) for point, floor in zip(POINTS, FLOORS)]
    assert len(diagnostic['results']) == 2
    for old, prescribed in zip(diagnostic['results'], inputs):
        assert old['normalized_point'] == prescribed['normalized_point']
        assert old['target'] == TARGET and old['deficit_strictly_positive'] is True
        assert arb(old['bounds']['point']) > cap.ar(F(prescribed['strict_floor']))
    context = cap.root_context(cell)
    results = []
    for point, floor in zip(POINTS, FLOORS):
        assert all(lo <= v <= hi for v, (lo, hi) in zip(point, expected_box))
        assert sum(v*v for v in point) < F(15, 16)**2
        assert F(-7, 8) < point[1] < F(51, 64)
        box = [(v, v) for v in point]
        passed, trial, info, _ = cap.check_face(cell, context, box, cap.FACES[0], TARGET)
        assert trial == TARGET and not passed
        assert arb(info['variation']) == 0
        assert arb(info['point']) > cap.ar(floor)
        results.append(dict(normalized_point=list(map(str, point)), target=trial,
                            fixed_target_deficit=info['point'], strict_floor=str(floor)))
    assert sha(ROOT/PROOF) == proof_hash and sha(__file__) == script_hash
    assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
    assert sha(args.input) == input_hash
    result = dict(format_version=1, status='passed', precision_bits=args.precision,
                  proof_sha256=proof_hash, script_sha256=script_hash,
                  input_sha256=input_hash, dependencies_sha256=dependencies,
                  original_cell=4933, original_witness=cell['witness'], inputs=inputs,
                  results=results, original_log_root_selfmap_rechecked=True,
                  root_proposals=0, target_proposals=0, refinements=0,
                  scope='Positive fixed-target cut deficit on two correlated auxiliary K4 '
                        'references. No actual-word realization or full finite-source failure.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS two fixed original-root cut deficits; no proposals or cover')


if __name__ == '__main__':
    main()
