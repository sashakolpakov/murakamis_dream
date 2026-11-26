#!/usr/bin/env python3
"""Sine/cotangent replay of the actual type-three critical strip.

The independent frozen sine/cotangent primitive is evaluated on every
saved author cell; the author Newton routine is not imported. Whole-bidisk root existence is an earlier proof input.
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
SOURCE = ROOT / 'experiments/replay_mixed_cyclic_window_heights.py'
PROOF = ROOT / 'notes/research_mixed_type_three_window_strip.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision', type=int, default=256)
parser.add_argument('--input', type=Path, default=ROOT / 'repro/results/research-mixed-type-three-window-strip.json')
parser.add_argument('--output', type=Path, default=ROOT / 'repro/results/research-mixed-type-three-window-strip-replay.json')
args = parser.parse_args()
record_in=json.loads(args.input.read_text())
assert record_in['status']=='passed'
assert record_in['script_sha256']==sha(ROOT/'experiments/certify_mixed_type_three_window_strip.py')
assert record_in['proof_sha256']==sha(PROOF)
for p,h in record_in['dependencies'].items():assert sha(ROOT/p)==h
hashes={**record_in['dependencies'],'experiments/replay_mixed_cyclic_window_heights.py':sha(SOURCE)}
proof_hash,script_hash,input_hash=sha(PROOF),sha(__file__),sha(args.input)
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
    author_case=next(c for c in record_in['cases'] if c['word']==list(word) and c['external_types']==[ta,tb])
    stack=list(author_case['addresses'])
    assert len(stack)==len(set(stack))
    assert sum((Q(1,2**len(a)) for a in stack),Q(0))==1
    codes_in=sorted(stack)
    assert all(not b.startswith(a) for a,b in zip(codes_in,codes_in[1:]))
    accepted = []
    hull = None
    while stack:
        address = stack.pop()
        visits += 1
        assert visits <= 100000, 'explicit replay visit budget'
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
            raise AssertionError(('saved cell failed independent replay',word,ta,tb,address))
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

assert hashes == {p: sha(ROOT / p) for p in hashes}
assert input_hash==sha(args.input)
assert {(tuple(c['word']),*c['external_types']) for c in record_in['cases']}==set(cases)
assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
record = {
    'status': 'passed',
    'scope': 'Universal original type-three critical geometry only; no finite-source or whole-cycle bound.',
    'precision_bits': args.precision, 'window_size': 3, 'case_count': len(output),
    'accepted_cells': sum(row['accepted_cells'] for row in output), 'visited_cells': visits,
    'target_rectangle': ['3/10', '39/100', '-3/100', '1/50'],
    'cases': output, 'elapsed_seconds': time.time() - start,
    'input_sha256':input_hash,'script_sha256': script_hash, 'proof_sha256': proof_hash, 'dependencies': hashes,
    'computational_scope': 'Replays every saved author cell with the independent sine/cotangent primitive, no author routine imported; global existence remains an explicit earlier theorem.',
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(record, indent=2) + '\n')
print('PASS', len(output), 'cases,', record['accepted_cells'], 'cells,', visits, 'visits', flush=True)
