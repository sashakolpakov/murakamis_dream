#!/usr/bin/env python3
"""Continue only the seven pending boxes of adaptive attempt01, once.

The original record, driver and dependencies are hash-bound. Previously
accepted/excluded leaves are copied without reevaluation. Stop at the first
depth-limit failure or after at most 6000 additional inspect() calls.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time


REPO = Path(__file__).resolve().parents[1]
PREVIOUS = REPO/'repro/results/research-mixed-next-four-adaptive-budget-attempt01.json'
PREVIOUS_SHA256 = 'e7af3ac81f917fc97393e7711989eafbe1f020a0e7695c51565380b66c735faf'
DRIVER = REPO/'experiments/certify_mixed_next_four_adaptive_budget.py'
DRIVER_SHA256 = 'e97474c4a7cdcaf43fe691a8c2f6083f7c0bec2f0df745d1f97ce886f274281d'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(value):
    content = json.dumps(value, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(content).hexdigest()


def verify_partition(leaves, unresolved):
    addresses = [entry['address'] for entry in leaves+unresolved]
    if any(set(address)-set('01') for address in addresses):
        raise ValueError('nonbinary address')
    ordered = sorted(addresses)
    if len(set(addresses)) != len(addresses):
        raise ValueError('duplicate terminal address')
    if any(right.startswith(left) for left, right in zip(ordered, ordered[1:])):
        raise ValueError('terminal addresses are not prefix-free')
    if sum((Fraction(1, 2**len(address)) for address in addresses), Fraction()) != 1:
        raise ValueError('terminal dyadic masses do not sum to one')
    if any(entry['status'] not in ('accepted', 'excluded') for entry in leaves):
        raise ValueError('nonterminal entry in leaves')


def decode_box(address, base):
    box = base.ROOT
    for depth, branch in enumerate(address):
        box = base.split(box, depth)[int(branch)]
    return box


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-cells', type=int, default=6000)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not 1 <= args.max_cells <= 6000:
        parser.error('one continuation permits at most 6000 additional cells')
    if digest(PREVIOUS) != PREVIOUS_SHA256 or digest(DRIVER) != DRIVER_SHA256:
        raise ValueError('original record or driver hash mismatch')
    original = json.loads(PREVIOUS.read_text())
    if (original['precision_bits'] != 160 or original['max_depth'] != 20
            or original['visited_cells'] != 6000 or original['unresolved_count'] != 7):
        raise ValueError('unexpected original run limits or state')
    for path_text, expected in original['input_sha256'].items():
        path = Path(path_text)
        if not path.is_absolute():
            path = REPO/path
        if digest(path) != expected:
            raise ValueError('original dependency hash mismatch: '+path_text)
    verify_partition(original['leaves'], original['unresolved'])
    if Counter(entry['status'] for entry in original['leaves']) != original['terminal_counts']:
        raise ValueError('original terminal count mismatch')
    if any(entry['reason'] != 'cell budget; box not inspected'
           or entry['enclosures'] is not None for entry in original['unresolved']):
        raise ValueError('continuation requires only previously uninspected boxes')

    # Import the same inspect() only after validating its bytes and all inputs.
    import certify_mixed_next_four_adaptive_budget as driver
    from flint import ctx
    ctx.prec = original['precision_bits']
    base = driver.base
    if list(map(str, base.ROOT)) != original['initial_auxiliary_rectangle']:
        raise ValueError('initial box mismatch')
    stack = []
    for entry in original['unresolved']:
        address = entry['address']
        box = tuple(map(Fraction, entry['box']))
        if box != decode_box(address, base) or len(address) > original['max_depth']:
            raise ValueError('pending box does not match its exact address')
        stack.append((address, box))

    inputs = dict(original['input_sha256'])
    inputs[str(PREVIOUS)] = PREVIOUS_SHA256
    inputs[str(Path(__file__).resolve())] = digest(Path(__file__))
    original_leaf_digest = canonical_digest(original['leaves'])
    leaves = list(original['leaves'])
    unresolved, new_counts, visited = [], Counter(), 0
    depth_failure = False
    started = time.monotonic()
    while stack and visited < args.max_cells:
        address, box = stack.pop()
        kind, reason, details = driver.inspect(box)
        visited += 1
        if kind in ('accepted', 'excluded'):
            new_counts[kind] += 1
            leaf = {'address': address, 'status': kind, 'reason': reason}
            if kind == 'accepted':
                leaf['certificate'] = details
            leaves.append(leaf)
        elif len(address) >= original['max_depth']:
            unresolved.append({'address': address, 'box': driver.box_record(box),
                               'reason': reason, 'enclosures': details})
            depth_failure = True
            break
        else:
            children = base.split(box, len(address))
            stack.extend([(address+'1', children[1]), (address+'0', children[0])])
    stop_reason = ('first depth-limit failure' if depth_failure else
                   'cell budget' if stack else 'pending partition completed')
    unresolved.extend({'address': address, 'box': driver.box_record(box),
                       'reason': stop_reason+'; box not inspected',
                       'enclosures': None} for address, box in stack)
    verify_partition(leaves, unresolved)
    if canonical_digest(leaves[:len(original['leaves'])]) != original_leaf_digest:
        raise ValueError('original leaves changed')
    for path_text, expected in inputs.items():
        path = Path(path_text)
        if not path.is_absolute():
            path = REPO/path
        if digest(path) != expected:
            raise RuntimeError('input changed during continuation: '+path_text)
    remaining = sum((Fraction(1, 2**len(entry['address']))
                     for entry in unresolved), Fraction())
    record = dict(original)
    record.update({
        'status': 'unresolved' if unresolved else 'proved',
        'previous_record_sha256': PREVIOUS_SHA256,
        'previous_record': str(PREVIOUS),
        'previous_visited_cells': original['visited_cells'],
        'previous_terminal_counts': original['terminal_counts'],
        'original_leaves_canonical_sha256': original_leaf_digest,
        'original_leaves_preserved_count': len(original['leaves']),
        'continuation_initial_pending_addresses':
            [entry['address'] for entry in original['unresolved']],
        'continuation_max_cells': args.max_cells,
        'continuation_visited_cells': visited,
        'continuation_terminal_counts': dict(new_counts),
        'continuation_stop_reason': stop_reason,
        'continuation_elapsed_seconds': time.monotonic()-started,
        'visited_cells': original['visited_cells']+visited,
        'terminal_counts': dict(Counter(entry['status'] for entry in leaves)),
        'unresolved_count': len(unresolved),
        'unresolved_dyadic_fraction': str(remaining),
        'terminal_partition_verified': True,
        'input_sha256': inputs, 'leaves': leaves, 'unresolved': unresolved,
    })
    # Keep inherited max_cells/elapsed_seconds explicitly identified as the
    # first-run metadata; the additional and combined counts are separate.
    record['previous_max_cells'] = record.pop('max_cells')
    record['previous_elapsed_seconds'] = record.pop('elapsed_seconds')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({key: record[key] for key in
                     ('status', 'continuation_visited_cells',
                      'continuation_terminal_counts', 'continuation_stop_reason',
                      'visited_cells', 'terminal_counts', 'unresolved_count',
                      'unresolved_dyadic_fraction', 'continuation_elapsed_seconds')}))


if __name__ == '__main__':
    main()
