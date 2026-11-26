#!/usr/bin/env python3
"""Actual type-three critical strip from ten universal three-vertex windows.

The frozen affine Newton primitive is re-evaluated on every accepted
two-angle box. Whole-bidisk root existence is an earlier proof input.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as Q
from pathlib import Path
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'experiments/certify_mixed_cyclic_window_heights.py'
PROOF = ROOT / 'notes/research_mixed_type_three_window_strip.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision', type=int, default=192)
parser.add_argument('--max-visits', type=int, default=100000)
parser.add_argument('--output', type=Path, default=ROOT / 'repro/results/research-mixed-type-three-window-strip.json')
args = parser.parse_args()
dependencies = [
    'experiments/certify_mixed_cyclic_window_heights.py',
    'notes/research_mixed_cyclic_critical_height_bounds.md',
    'notes/research_mixed_cyclic_critical_localization.md',
    'repro/results/research-mixed-cyclic-block-localization.json',
    'repro/results/research-mixed-cyclic-block-localization-replay.json',
    'repro/results/research-mixed-cyclic-window-heights.json',
    'repro/results/research-mixed-cyclic-window-heights-replay.json',
]
hashes = {p: sha(ROOT / p) for p in dependencies}
proof_hash, script_hash = sha(PROOF), sha(__file__)
for p in dependencies:
    if p.endswith('.json'):
        assert json.loads((ROOT / p).read_text())['status'] == 'passed'
old = json.loads((ROOT / 'repro/results/research-mixed-cyclic-window-heights.json').read_text())
assert old['script_sha256'] == sha(SOURCE)
assert old['proof_sha256'] == sha(ROOT / 'notes/research_mixed_cyclic_critical_height_bounds.md')
spec = importlib.util.spec_from_file_location('frozen_window_newton', SOURCE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
ctx.prec = args.precision
m.PI = arb.pi()


def decode(address):
    box = [Q(0), Q(1), Q(0), Q(1)]
    for depth, bit in enumerate(address):
        k = 2 * (depth % 2)
        mid = (box[k] + box[k + 1]) / 2
        box[k + 1 - int(bit)] = mid
    return box


cases = []
for left, right, ta, tb in itertools.product((0, 1), repeat=4):
    word = (left, 0, right)
    whole = (ta,) + word + (tb,)
    if whole <= whole[::-1]:
        cases.append((word, ta, tb))
assert len(cases) == 10
start = time.time()
visits = 0
output = []
for word, ta, tb in cases:
    stack = ['']
    accepted = []
    hull = None
    while stack:
        address = stack.pop()
        visits += 1
        assert visits <= args.max_visits, 'explicit total visit budget'
        result = m.certify(word, ta, tb, decode(address), Q(-3, 100))
        good = result and all(
            m.ar('3/10') < z.real < m.ar('39/100')
            and m.ar('-3/100') < z.imag < m.ar('1/50')
            for z in result)
        if good:
            accepted.append(address)
            hull = result if hull is None else [
                acb(hull[j].real.union(result[j].real), hull[j].imag.union(result[j].imag))
                for j in (0, 1)]
        else:
            assert len(address) < 26, ('explicit depth budget', word, ta, tb, address)
            stack.extend([address + '0', address + '1'])
    codes = set(accepted)
    assert len(codes) == len(accepted)
    assert sum((Q(1, 2 ** len(a)) for a in codes), Q(0)) == 1
    prefixes = {a[:j] for a in codes for j in range(len(a))}
    assert not (codes & prefixes)
    assert all(all(p + bit in codes or p + bit in prefixes for bit in '01') for p in prefixes)
    row = {
        'word': list(word), 'external_types': [ta, tb], 'addresses': accepted,
        'accepted_cells': len(accepted),
        'middle_coordinate_hulls': [[z.real.str(25, more=True), z.imag.str(25, more=True)] for z in hull],
    }
    output.append(row)
    print(json.dumps({k: v for k, v in row.items() if k != 'addresses'}), flush=True)

assert hashes == {p: sha(ROOT / p) for p in dependencies}
assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
record = {
    'status': 'passed',
    'scope': 'Universal original type-three critical geometry only; no finite-source or whole-cycle bound.',
    'precision_bits': args.precision, 'window_size': 3, 'case_count': len(output),
    'accepted_cells': sum(row['accepted_cells'] for row in output), 'visited_cells': visits,
    'target_rectangle': ['3/10', '39/100', '-3/100', '1/50'],
    'cases': output, 'elapsed_seconds': time.time() - start,
    'script_sha256': script_hash, 'proof_sha256': proof_hash, 'dependencies': hashes,
    'computational_scope': 'Reuses the unchanged proved affine Newton primitive, rerunning every accepted case; global existence is an explicit earlier theorem.',
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(record, indent=2) + '\n')
print('PASS', len(output), 'cases,', record['accepted_cells'], 'cells,', visits, 'visits', flush=True)
